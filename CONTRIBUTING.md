# Contributing

Contributions are welcome, especially confirmed mappings for other Hombli or
Tuya Christmas-light variants.

## Please include evidence

For mapping changes, include:

- Product/model and firmware version
- LocalTuya protocol version
- A redacted log excerpt or reproducible capture method
- Which DPs and value types were observed
- Whether existing mappings still work

Do not include device IDs, local keys, tokens, IP addresses, Home Assistant URLs
or other private installation data.

## Pull-request checklist

- [ ] No secrets or installation-specific identifiers are committed.
- [ ] YAML parses successfully.
- [ ] The package passes Home Assistant's configuration check.
- [ ] Every scene name matches its `scene_codes` key exactly.
- [ ] Dashboard action names match package script/entity names.
- [ ] Documentation describes compatibility and rollback implications.

Please keep vendor-app spelling in compatibility tables, even when it contains
a typo, and explain the preserved spelling in a note.
