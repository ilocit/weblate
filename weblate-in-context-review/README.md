# Weblate in-context review prototype

This directory contains the first read-only vertical slice described in
[`docs/specs/in-context-localization-review.md`](../docs/specs/in-context-localization-review.md).
It remains separate from Weblate core and has three deployable parts:

- `addon`: optional Weblate add-on that publishes signed key-to-unit manifests.
- `gateway`: separate API that stores manifests and reads unit metadata from
  Weblate without exposing its API token to reviewed applications.
- `react`: React occurrence adapter, portal overlay, context panel, and demo.

## Current scope

The prototype supports:

- Key-based source and target unit bindings.
- Explicit reporting of keyless, ambiguous, and duplicate bindings.
- HMAC-authenticated manifest delivery.
- Bearer-authenticated review metadata lookup.
- Source drift rejection using Weblate `content_hash`.
- React occurrence registration without changing visible translations.
- Selection outlines, source and target metadata, and a Weblate permalink.
- Translation-specific comments submitted through the review gateway.
- Full-page PNG capture with the selected occurrence outlined and uploaded to
  Weblate as source-unit context.

Suggestions, direct editing, approval, automated capture scenarios, persistent
manifest storage, and production session issuance are planned phases. The
prototype's configured review token is suitable only for local development.

## Weblate add-on

Install the package into the same Python environment as Weblate:

```console
uv pip install -e ./weblate-in-context-review/addon
```

Register the add-on in the Weblate settings override:

```python
WEBLATE_ADDONS += (
    "weblate_in_context_addon.addon.InContextReviewManifestAddon",
)
```

Restart Weblate, install **In-context review manifest** on a component, and
configure:

- Gateway URL: `https://review.example/v1/manifests`
- Signing secret: a random value of at least 32 characters

The gateway URL is visible in add-on history; the signing secret is redacted.
The add-on publishes after component updates, on installation, and when run
manually. Weblate's private-target webhook policy also applies to delivery.

## Gateway

Create an isolated environment and configure it:

```console
cd weblate-in-context-review/gateway
python -m venv .venv
.venv/bin/pip install -e .
export WEBLATE_URL=http://localhost:8080
# Required only for private projects.
export WEBLATE_API_TOKEN=wlu_server_side_token
export MANIFEST_SECRET=replace-with-the-add-on-secret
export REVIEW_SESSION_TOKEN=replace-for-local-development
export REVIEW_ALLOWED_ORIGINS=http://localhost:5173
.venv/bin/uvicorn weblate_in_context_gateway.main:create_app_from_environment \
  --factory --host 0.0.0.0 --port 8090
```

For public projects, `WEBLATE_API_TOKEN` can be omitted for review metadata.
Screenshot uploads require a token with screenshot add and edit permissions,
even for public projects. Comment submission requires the `comment.add`
permission. The gateway accepts PNG uploads up to 8 MB, stores them under the
component's source language, and associates the corresponding source unit. The
token must never be placed in the React build or reviewed application.
Production deployments must replace the static review token with short-lived,
user-bound sessions.

The initial manifest store is in memory. Restarting the gateway requires the
add-on to publish each component again.

For this repository's public sample project, seed a development gateway without
installing the add-on:

```console
.venv/bin/python -m weblate_in_context_gateway.bootstrap \
  --secret replace-with-the-add-on-secret
```

## React demo

```console
cd weblate-in-context-review/react
npm install
npm run dev
```

The demo expects the gateway at `http://localhost:8090` and uses the local-only
review token `review-token`. An application integration wraps its normal
translated output:

```tsx
<ReviewProvider gatewayUrl={gatewayUrl} reviewToken={shortLivedSessionToken}>
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
</ReviewProvider>
```

Only enable the provider and overlay in an authorized review environment.

## Validation

```console
cd weblate-in-context-review/addon
PYTHONPATH=src python -m unittest discover -s tests -v

cd ../gateway
.venv/bin/python -m unittest discover -s tests -v

cd ../react
npm test
npm run build
```
