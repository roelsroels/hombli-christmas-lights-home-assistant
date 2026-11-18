# HACS publication checklist

This repository is structured as a single HACS integration repository. The
installable files live in:

```text
custom_components/hombli_christmas_lights/
```

## Already implemented

- One integration directory under `custom_components/`
- `manifest.json` with domain, name, documentation, issue tracker, code owner
  and semantic version
- UI config flow with unique device-ID enforcement
- Config-entry runtime data and clean platform unloading
- Native Select, Number, Button and Switch entities
- English strings and translations
- Redacted diagnostics
- Local 256×256 transparent brand icon
- Root `hacs.json`
- HACS and hassfest validation workflow
- Public README, open-source license, issue template and changelog
- HACS-first installation and removal documentation
- One-click My Home Assistant link for adding the custom repository to HACS

## Before publishing a stable release

1. Install the integration as a HACS custom repository on a test Home Assistant
   instance.
2. Verify setup, unload/reload, restart, all five entities, diagnostics and
   LocalTuya error handling.
3. Confirm the tested minimum Home Assistant version and add it to `hacs.json`
   if a minimum should be enforced.
4. Replace the beta version in `manifest.json` with the stable release version.
5. Update `CHANGELOG.md` and publish a GitHub release whose tag matches the
   manifest version, for example `v2.0.0`.
6. Confirm that the scheduled HACS and hassfest workflow passes on the release.

## Default HACS catalogue submission

The GitHub repository must remain public, have Issues enabled, use an OSI
license, have a concise repository description and relevant repository topics.
After the stable release is tested, submit it through the HACS default
repository inclusion process as an **Integration**.

Suggested topics:

```text
home-assistant hacs localtuya tuya hombli christmas-lights rgbic
smart-home custom-integration lovelace
```

The custom-repository installation route works before default-catalogue
acceptance and is the recommended beta-test path.
