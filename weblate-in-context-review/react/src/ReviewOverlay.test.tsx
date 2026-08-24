import { cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, expect, test, vi } from "vitest";
import { L10nOccurrence, ReviewProvider } from "./ReviewContext";
import { ReviewOverlay } from "./ReviewOverlay";

afterEach(() => {
  cleanup();
  vi.restoreAllMocks();
});

test("selects a rendered key and loads its Weblate unit", async () => {
  const fetchMock = vi.spyOn(globalThis, "fetch").mockResolvedValue(
    new Response(
      JSON.stringify({
        binding: {
          context: "navigation.home",
          targets: {
            de: {
              unit_id: 202,
              content_hash: 2202,
              web_url: "https://weblate.example/target",
            },
          },
        },
        unit: { source: ["Home"], target: ["Startseite"], state: 20 },
      }),
      { status: 200, headers: { "Content-Type": "application/json" } },
    ),
  );

  render(
    <ReviewProvider gatewayUrl="https://gateway.example" reviewToken="session">
      <L10nOccurrence
        identity={{
          project: "sample-i18n",
          component: "messages",
          language: "de",
          context: "navigation.home",
        }}
      >
        Startseite
      </L10nOccurrence>
      <ReviewOverlay />
    </ReviewProvider>,
  );

  fireEvent.click(
    await screen.findByRole("button", { name: "Review navigation.home" }),
  );

  await waitFor(() => expect(fetchMock).toHaveBeenCalledOnce());
  expect(await screen.findByText("Home")).toBeInTheDocument();
  expect(screen.getByRole("link", { name: /Open in Weblate/ })).toHaveAttribute(
    "href",
    "https://weblate.example/target",
  );
  expect(fetchMock.mock.calls[0][1]).toMatchObject({
    headers: { Authorization: "Bearer session" },
  });
});

test("pauses markers so the application remains interactive", async () => {
  render(
    <ReviewProvider gatewayUrl="https://gateway.example" reviewToken="session">
      <button>Application action</button>
      <L10nOccurrence
        identity={{
          project: "sample-i18n",
          component: "messages",
          language: "de",
          context: "button.save",
        }}
      >
        Save
      </L10nOccurrence>
      <ReviewOverlay />
    </ReviewProvider>,
  );

  expect(
    await screen.findByRole("button", { name: "Review button.save" }),
  ).toBeInTheDocument();
  fireEvent.click(screen.getByRole("button", { name: "Pause review mode" }));
  expect(
    screen.queryByRole("button", { name: "Review button.save" }),
  ).not.toBeInTheDocument();
  expect(screen.getByRole("button", { name: "Start review mode" })).toHaveAttribute(
    "aria-pressed",
    "false",
  );
});

test("submits a comment for the selected Weblate unit", async () => {
  const fetchMock = vi.spyOn(globalThis, "fetch").mockImplementation(async (input) => {
    if (String(input).includes("/v1/comments/")) {
      return new Response(JSON.stringify({ id: 77 }), { status: 200 });
    }
    return new Response(
      JSON.stringify({
        binding: {
          context: "button.cancel",
          targets: {
            de: {
              unit_id: 20,
              content_hash: 2202,
              web_url: "https://weblate.example/target",
            },
          },
        },
        unit: { source: ["Cancel"], target: [], state: 0 },
      }),
      { status: 200, headers: { "Content-Type": "application/json" } },
    );
  });

  render(
    <ReviewProvider gatewayUrl="https://gateway.example" reviewToken="session">
      <L10nOccurrence
        identity={{
          project: "sample-i18n",
          component: "messages",
          language: "de",
          context: "button.cancel",
        }}
      >
        Cancel
      </L10nOccurrence>
      <ReviewOverlay />
    </ReviewProvider>,
  );

  fireEvent.click(await screen.findByRole("button", { name: "Review button.cancel" }));
  fireEvent.click(
    await screen.findByRole("button", { name: "Add comment to Weblate" }),
  );
  fireEvent.change(screen.getByRole("textbox", { name: "Comment" }), {
    target: { value: "Use the translated action label." },
  });
  fireEvent.click(screen.getByRole("button", { name: "Submit" }));

  expect(await screen.findByText("Comment added to Weblate.")).toBeInTheDocument();
  expect(fetchMock).toHaveBeenLastCalledWith(
    "https://gateway.example/v1/comments/sample-i18n/messages/de/button.cancel",
    {
      method: "POST",
      headers: {
        Authorization: "Bearer session",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ comment: "Use the translated action label." }),
    },
  );
});