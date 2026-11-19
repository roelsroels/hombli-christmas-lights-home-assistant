# Troubleshooting

## The integration entities exist but the light does not change

- Confirm the device ID entered in **Settings → Devices & services → Hombli
  Christmas Lights → Configure** belongs to the same LocalTuya device.
- Confirm LocalTuya shows the controller as connected.
- Confirm DP20, DP21 and DP25 on your controller.
- Enable LocalTuya debug logging temporarily and inspect the action call.
- Make sure another automation or the Hombli app is not immediately changing
  the controller again.
- Power-cycle the controller after an invalid DP write.

## `localtuya.set_dp` is unknown

LocalTuya is missing, disabled or failed to load. Install/configure LocalTuya
and restart Home Assistant before loading this integration.

## Hombli Christmas Lights does not appear under Add integration

Confirm Marketplace downloaded
`custom_components/hombli_christmas_lights/manifest.json`, then restart Home
Assistant and clear the browser cache. Check the Home Assistant log for an
integration manifest or import error.

## Unknown helper or script entities

These are leftovers from the pre-2.0 package dashboard. Remove the old package,
restart Home Assistant, and replace the dashboard view with the current
`dashboards/sections-view.yaml` file. The current integration uses native
Select, Number, Button and Switch entities instead.

## The dashboard says `Custom element doesn't exist: button-card`

Install Button Card, add its frontend resource if your installation requires
that step, and hard-refresh the browser.

## The active scene is not highlighted with the Marketplace integration

The highlight follows `select.hombli_christmas_lights_scene`. It changes after
the integration successfully sends a scene through LocalTuya. A scene selected
in the Hombli app cannot update this assumed-state entity.

If the entity ID has a numeric suffix, replace the example entity ID throughout
the dashboard YAML.

## The preview and physical lights are out of phase

This is expected. The controller does not expose live per-LED frames. The
preview replays a measured approximation and scales it using the speed and
brightness controls.

## Spook reports removed helpers or scripts

Another saved dashboard still references an older configuration. Open the view
named by Spook and replace its raw configuration with the current dashboard
file, or remove the obsolete cards manually.

## Safe rollback

1. Remove the Hombli Christmas Lights config entry from **Settings → Devices &
   services**.
2. Remove the integration from Marketplace.
3. Restart Home Assistant.
4. Remove or replace the example dashboard view.

This does not remove or reconfigure the LocalTuya device.
