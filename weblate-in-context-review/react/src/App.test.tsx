import { fireEvent, render, screen } from "@testing-library/react";
import { expect, test } from "vitest";
import App from "./App";

test("uses every Weblate string in the application workflow", () => {
  render(<App />);

  const initialKeys = new Set(
    Array.from(document.querySelectorAll("[data-l10n-key]"), (element) =>
      element.getAttribute("data-l10n-key"),
    ),
  );
  expect(initialKeys).toEqual(
    new Set([
      "account.sign_out",
      "app.name",
      "button.cancel",
      "button.save",
      "error.network",
      "items.count",
      "navigation.home",
      "navigation.settings",
      "welcome.message",
    ]),
  );

  fireEvent.click(screen.getByRole("button", { name: /Abmelden/ }));
  expect(document.querySelector('[data-l10n-key="account.sign_in"]')).not.toBeNull();

  fireEvent.click(screen.getByRole("button", { name: "Increase item count" }));
  expect(screen.getByText("Sie haben 5 Elemente.")).toBeInTheDocument();

  const nameInput = screen.getByLabelText("Display name");
  fireEvent.change(nameInput, { target: { value: "Jonas" } });
  expect(screen.getByText("Willkommen, Jonas!")).toBeInTheDocument();
  fireEvent.click(screen.getByRole("button", { name: "Cancel" }));
  expect(nameInput).toHaveValue("Mara");
});