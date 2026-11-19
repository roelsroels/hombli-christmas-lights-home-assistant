# Marketplace publication checklist

This repository is structured as a single Marketplace integration repository. The
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
- Marketplace and hassfest validation workflow
- Public README, open-source license, issue template and changelog
- Marketplace-first installation and removal documentation
- One-click My Home Assistant link for adding the custom repository to Marketplace

## Stable release and verification

Version `2.0.0` is the first Marketplace-installable release. After installing it on a
test Home Assistant instance:

1. Verify setup, unload/reload, restart, all five entities, diagnostics and
   LocalTuya error handling.
2. Confirm the tested minimum Home Assistant version and add it to `hacs.json`
   if a minimum should be enforced.
3. Confirm that the scheduled Marketplace and hassfest workflow continues to pass on
   the release.

## Default Marketplace catalogue submission

The GitHub repository must remain public, have Issues enabled, use an OSI
license, have a concise repository description and relevant repository topics.
After the stable release is tested, submit it through the Marketplace default
repository inclusion process as an **Integration**.

Suggested topics:

```text
home-assistant hacs localtuya tuya hombli christmas-lights rgbic
smart-home custom-integration lovelace
```

The custom-repository installation route works before default-catalogue
acceptance and is the recommended verification path.
