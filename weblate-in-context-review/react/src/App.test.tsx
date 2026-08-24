import { fireEvent, render, screen } from "@testing-library/react";
import { expect, test } from "vitest";
import App from "./App";

test("renders Home and Settings as separate pages", () => {
  window.location.hash = "#home";
  render(<App />);

  expect(screen.getByRole("heading", { name: "Willkommen, Mara!" })).toBeVisible();
  expect(screen.queryByLabelText("Display name")).not.toBeInTheDocument();
  expect(screen.getByRole("alert")).toHaveTextContent(
    "Verbindung konnte nicht hergestellt werden. Bitte versuchen Sie es erneut.",
  );

  fireEvent.click(screen.getByRole("button", { name: /Abmelden/ }));
  expect(document.querySelector('[data-l10n-key="account.sign_in"]')).not.toBeNull();

  fireEvent.click(screen.getByRole("button", { name: "Increase item count" }));
  expect(screen.getByText("Sie haben 5 Elemente.")).toBeInTheDocument();

  fireEvent.click(screen.getByRole("link", { name: /Einstellungen/ }));
  expect(screen.getByRole("heading", { name: "Einstellungen" })).toBeVisible();
  expect(screen.queryByText("Willkommen, Mara!")).not.toBeInTheDocument();

  const nameInput = screen.getByLabelText("Display name");
  fireEvent.change(nameInput, { target: { value: "Jonas" } });
  fireEvent.click(screen.getByRole("button", { name: "Cancel" }));
  expect(nameInput).toHaveValue("Mara");

  const visibleKeys = new Set(
    Array.from(document.querySelectorAll("[data-l10n-key]"), (element) =>
      element.getAttribute("data-l10n-key"),
    ),
  );
  expect(visibleKeys).toEqual(
    new Set([
      "account.sign_in",
      "app.name",
      "button.cancel",
      "button.save",
      "error.network",
      "navigation.home",
      "navigation.settings",
    ]),
  );
});