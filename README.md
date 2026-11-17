# Hombli Christmas Lights for Home Assistant

Local Home Assistant control for the **Hombli Smart Christmas Lights RGB**
controller, including all 57 scenes exposed by the Hombli app, scene speed and
scene brightness controls, a compact Sections dashboard, active-scene
highlighting, and a recording-derived animated preview.

> [!IMPORTANT]
> This is a device-specific community project. The DP assignments and scene
> codes were captured from one Hombli/Tuya controller using LocalTuya protocol
> 3.3. Verify the datapoints on your own hardware before writing values.

This project is not affiliated with Hombli, Tuya, Home Assistant, LocalTuya, or
the Button Card project.

## What is included

- Exact DP25 codes for 57 named scenes from the Hombli app
- Power, scene mode, speed and scene-brightness control
- A Home Assistant package with helpers and scripts
- A four-column Sections dashboard example
- Compact scene buttons with active-scene highlighting
- An 18-light animated preview calibrated from a full recording of the physical
  light string
- A reference-capture script for comparing other firmware/device variants

## Confirmed datapoints

| DP | Purpose | Values used here |
|---:|---|---|
| 20 | Power | `true` / `false` |
| 21 | Work mode | `scene` |
| 25 | Built-in scene | Four-character scene code, e.g. `0006` |
| 103 | Animation speed | Integer `1`–`100` |
| 105 | Scene brightness | Integer `1`–`100` |

See [Compatibility and safety](docs/COMPATIBILITY.md) before installing.

## Requirements

- Home Assistant with [configuration packages](https://www.home-assistant.io/docs/configuration/packages/) enabled
- [LocalTuya](https://github.com/rospogrigio/localtuya) configured for the light controller
- [Button Card](https://github.com/custom-cards/button-card) installed for the
  supplied dashboard and animated preview
- A LocalTuya light entity for the controller
- The Tuya/Hombli device ID and local key obtained through your usual LocalTuya
  setup process

## Installation

### 1. Confirm the device

Do not start by sending the scene codes. First verify that your controller uses
the same datapoints listed above. Read [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md).

### 2. Install the package

Copy:

```text
packages/christmas_lights.yaml
```

to:

```text
/config/packages/christmas_lights.yaml
```

If packages are not enabled yet, add this beneath the existing
`homeassistant:` key in `/config/configuration.yaml`:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Do not create a second `homeassistant:` section.

### 3. Add the device ID secret

Add the device ID used by LocalTuya to `/config/secrets.yaml`:

```yaml
hombli_christmas_lights_device_id: "YOUR_TUYA_DEVICE_ID"
```

The local key is intentionally not referenced or stored by this package. Keep
all credentials and identifiers out of Git.

### 4. Check and restart

In Home Assistant:

1. Open **Developer tools → YAML**.
2. Run **Check configuration**.
3. Restart Home Assistant.

The restart is required because the package creates helpers and scripts.

### 5. Install the dashboard view

The supplied example is a [Sections view](https://www.home-assistant.io/dashboards/sections/).
Open the target dashboard view in raw configuration mode and paste the contents
of:

```text
dashboards/sections-view.yaml
```

If your light entity is not
`light.hombli_smart_christmas_lights_rgb`, replace that entity ID in the
dashboard file.

## Entities and scripts created

| Entity | Purpose |
|---|---|
| `input_select.christmas_lights_scene` | Scene selected in Home Assistant |
| `input_number.christmas_lights_animation_speed` | DP103 control |
| `input_number.christmas_lights_scene_brightness` | DP105 control |
| `input_text.christmas_lights_active_scene` | Last scene successfully sent by these scripts |
| `script.christmas_lights_set_scene` | Sends one named scene |
| `script.christmas_lights_apply_controls` | Sends scene, speed and scene brightness |
| `script.christmas_lights_capture_reference` | Runs all scenes in order for a comparison video |

## How the dashboard state works

Each scene button calls `script.christmas_lights_set_scene`. The active button
is highlighted from `input_text.christmas_lights_active_scene`, so merely
changing the dropdown does not falsely mark a scene as active.

The controller exposes the selected scene code but not its live per-LED frames.
The animated preview therefore replays a recording-derived approximation. It
shows the correct scene-specific grouping, colours, dark states and movement,
but is not phase-locked to the physical string.

## Scene map

The complete captured scene-to-DP25 table is in [docs/SCENES.md](docs/SCENES.md).

## Adapting this for a related controller

1. Confirm your DP mapping in LocalTuya diagnostics.
2. Make a copy of the package; do not overwrite the verified map immediately.
3. Test power and work mode first.
4. Test one scene code at low brightness.
5. Capture the values reported while selecting scenes in the vendor app.
6. Update both `scene_codes` and the `input_select` options.
7. Use `script.christmas_lights_capture_reference` to record the real effects.

Please contribute confirmed mappings with the device model, firmware version,
protocol version and evidence. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Limitations

- App-originated scene changes do not update
  `input_text.christmas_lights_active_scene` automatically.
- The preview is illustrative, not a live LED feed.
- Power monitoring was not found on the tested controller.
- DP assignments can differ across Tuya products and firmware versions.
- The supplied dashboard depends on Button Card.

## Troubleshooting

See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for LocalTuya errors,
unknown entities/actions, missing cards, inactive highlights and safe rollback.

## License

Configuration and documentation in this repository are released under the
[MIT License](LICENSE). Vendor names and trademarks belong to their respective
owners.
