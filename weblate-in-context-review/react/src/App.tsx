import {
  CloudOff,
  Home,
  LogIn,
  LogOut,
  Minus,
  Plus,
  Settings,
} from "lucide-react";
import { type PropsWithChildren, useState } from "react";
import { L10nOccurrence, ReviewProvider } from "./ReviewContext";
import { ReviewOverlay } from "./ReviewOverlay";
import "./demo.css";

const translations = {
  "account.sign_in": "Anmelden",
  "account.sign_out": "Abmelden",
  "app.name": "Beispielanwendung",
  "button.cancel": "Cancel",
  "button.save": "Save",
  "error.network":
    "Verbindung konnte nicht hergestellt werden. Bitte versuchen Sie es erneut.",
  "items.count": "Sie haben {0} Elemente.",
  "navigation.home": "Startseite",
  "navigation.settings": "Einstellungen",
  "welcome.message": "Willkommen, {0}!",
} as const;

type TranslationKey = keyof typeof translations;

const baseIdentity = {
  project: "sample-i18n",
  component: "messages",
  language: "de",
};

function format(template: string, value: string | number) {
  return template.replace("{0}", String(value));
}

function Localized({
  context,
  children,
}: PropsWithChildren<{ context: TranslationKey }>) {
  return (
    <L10nOccurrence identity={{ ...baseIdentity, context }}>
      {children ?? translations[context]}
    </L10nOccurrence>
  );
}

export default function App() {
  const [signedIn, setSignedIn] = useState(true);
  const [itemCount, setItemCount] = useState(4);
  const [showNetworkError, setShowNetworkError] = useState(true);
  const [formValues, setFormValues] = useState({ name: "Mara", digest: true });
  const [savedValues, setSavedValues] = useState(formValues);

  const cancelChanges = () => setFormValues(savedValues);
  const saveChanges = () => setSavedValues(formValues);

  return (
    <ReviewProvider gatewayUrl="http://localhost:8090" reviewToken="review-token">
      <main className="demo-shell">
        <nav aria-label="Main navigation">
          <strong>
            <Localized context="app.name" />
          </strong>
          <a href="#home" className="active">
            <Home aria-hidden="true" />
            <Localized context="navigation.home" />
          </a>
          <a href="#settings">
            <Settings aria-hidden="true" />
            <Localized context="navigation.settings" />
          </a>
          <button
            className="account-action"
            onClick={() => setSignedIn((current) => !current)}
          >
            {signedIn ? <LogOut aria-hidden="true" /> : <LogIn aria-hidden="true" />}
            <Localized context={signedIn ? "account.sign_out" : "account.sign_in"} />
          </button>
        </nav>

        <div className="app-layout">
          <section id="home" className="overview">
            <div className="intro">
              <p className="demo-eyebrow">Localization workspace</p>
              <h1>
                <Localized context="welcome.message">
                  {format(translations["welcome.message"], formValues.name)}
                </Localized>
              </h1>
              <p className="item-count">
                <Localized context="items.count">
                  {format(translations["items.count"], itemCount)}
                </Localized>
              </p>
              <div className="counter" aria-label="Item count">
                <button
                  onClick={() => setItemCount((count) => Math.max(0, count - 1))}
                  aria-label="Decrease item count"
                  title="Decrease"
                >
                  <Minus aria-hidden="true" />
                </button>
                <output aria-live="polite">{itemCount}</output>
                <button
                  onClick={() => setItemCount((count) => count + 1)}
                  aria-label="Increase item count"
                  title="Increase"
                >
                  <Plus aria-hidden="true" />
                </button>
              </div>
            </div>

            {showNetworkError && (
              <div className="network-alert" role="alert">
                <CloudOff aria-hidden="true" />
                <Localized context="error.network" />
                <button
                  onClick={() => setShowNetworkError(false)}
                  aria-label="Dismiss network error"
                  title="Dismiss"
                >
                  &times;
                </button>
              </div>
            )}
          </section>

          <section id="settings" className="settings-panel">
            <header>
              <Settings aria-hidden="true" />
              <h2>
                <Localized context="navigation.settings" />
              </h2>
            </header>
            <label>
              Display name
              <input
                value={formValues.name}
                onChange={(event) =>
                  setFormValues((current) => ({
                    ...current,
                    name: event.target.value,
                  }))
                }
              />
            </label>
            <label className="toggle-row">
              <input
                type="checkbox"
                checked={formValues.digest}
                onChange={(event) =>
                  setFormValues((current) => ({
                    ...current,
                    digest: event.target.checked,
                  }))
                }
              />
              Weekly activity digest
            </label>
            <div className="form-actions">
              <button className="secondary" onClick={cancelChanges}>
                <Localized context="button.cancel" />
              </button>
              <button className="primary" onClick={saveChanges}>
                <Localized context="button.save" />
              </button>
            </div>
          </section>
        </div>
      </main>
      <ReviewOverlay />
    </ReviewProvider>
  );
}
