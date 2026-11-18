# Changelog

## 2.0.0 — 2026-11-18

- Added a UI-configured Home Assistant custom integration for HACS.
- Added native Scene, Speed, Scene brightness, Random scene and Random scene
  cycle entities backed by LocalTuya's `set_dp` action.
- Added redacted diagnostics, translations and a project-owned integration
  icon.
- Added HACS and hassfest validation workflows and publication documentation.
- Converted the primary dashboard example to the custom-integration entities.
- Retained the original package and its matching dashboard as a legacy/manual
  installation path.

## 1.1.0 — 2026-11-18

- Added a dashboard button and package automation for starting and stopping a
  random scene cycle. It immediately selects a different scene and repeats every
  30 seconds without changing the selected speed or scene brightness.
- Updated the dashboard screenshot to show the random scene cycle in use.

## 1.0.1 — 2026-11-17

- Added a privacy-safe dashboard screenshot and custom GitHub social preview.
- Expanded repository metadata, topics and README terminology for better Home
  Assistant, LocalTuya and Tuya RGB string-light discovery.
- Linked the exact Hombli source product and documented how the mappings and
  animated preview were captured from the physical controller.
- Added the Buy Me a Coffee funding link.
- Documented the separate PowerCalc work for potential power monitoring.

## 1.0.0 — 2026-11-17

- Published the verified 57-scene DP25 mapping.
- Added DP103 animation-speed and DP105 scene-brightness controls.
- Added the Home Assistant package and compact Sections dashboard.
- Added active-scene highlighting.
- Added the recording-derived animated LED preview.
- Added a reference-capture workflow and public reuse documentation.
