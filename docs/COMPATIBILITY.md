# Compatibility and safety

Tuya datapoints are product- and firmware-specific. A controller that looks
identical can expose different DPs or value types. Writing an unverified value
can make a device unresponsive until it is power-cycled or re-paired.

## Verified configuration

The original setup used:

- [Hombli Smart Christmas Light RGB](https://hombli.com/collections/ambiance/products/hombli-smart-christmas-light-rgb)
  controller—the physical source device used to capture and test this project
- LocalTuya protocol 3.3
- DP20 for power
- DP21 for work mode
- DP25 for the built-in scene code
- DP103 for animation speed
- DP105 for scene brightness

No power, voltage, current or energy datapoint was observed on the tested
controller.

## Before installing

1. Export or record your working LocalTuya configuration.
2. Confirm the device ID used by your LocalTuya entry.
3. Inspect LocalTuya diagnostics or debug logs while changing settings in the
   Hombli app.
4. Confirm the DPs and value types above.
5. Test with a single scene at low brightness.
6. Keep the vendor app available for recovery and know how to power-cycle the
   controller.

## What to collect for another variant

When reporting a compatible or incompatible controller, include:

- Exact product name and model number
- Firmware version
- LocalTuya protocol version
- Country/region if the product SKU differs
- The DPs seen for power, mode, scene, speed and scene brightness
- A redacted log excerpt showing the DP changes

Never publish a device ID, local key, cloud token, IP address or Home Assistant
URL.
