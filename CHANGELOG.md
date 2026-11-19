# Changelog

## Unreleased

- Renamed user-facing terminology to Home Assistant Marketplace while
  retaining the required technical filenames and redirect identifiers.

## 2.1.2 — 2026-11-19

- Changed the dashboard LED preview to static grey bulbs while the physical
  light entity is off; scene animation resumes automatically when it turns on.

## 2.1.1 — 2026-11-18

- Fixed random-cycle shutdown detection when scene control uses LocalTuya but
  the dashboard power entity is provided by the standard Tuya integration.
- Added the detected power light entity to redacted diagnostics.

## 2.1.0 — 2026-11-18

- Removed the obsolete pre-Marketplace package, its duplicate dashboard and its
  secrets example.
- Replaced the legacy installation documentation with a concise migration path
  to the Marketplace integration.

## 2.0.1 — 2026-11-18

- Stop an active random scene cycle when the matching LocalTuya light turns
  off, preventing a later timer tick from turning the string back on.
- Added the same off-state protection to the legacy package automation.

## 2.0.0 — 2026-11-18

- Added a UI-configured Home Assistant custom integration for Marketplace.
- Added native Scene, Speed, Scene brightness, Random scene and Random scene
  cycle entities backed by LocalTuya's `set_dp` action.
- Added redacted diagnostics, translations and a project-owned integration
  icon.
- Added Marketplace and hassfest validation workflows and publication documentation.
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
