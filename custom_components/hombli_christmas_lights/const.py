"""Constants for the Hombli Christmas Lights integration."""

from homeassistant.const import Platform

DOMAIN = "hombli_christmas_lights"

CONF_DEVICE_ID = "device_id"
CONF_NAME = "name"
DEFAULT_NAME = "Hombli Christmas Lights"

DP_POWER = 20
DP_MODE = 21
DP_SCENE = 25
DP_SPEED = 103
DP_BRIGHTNESS = 105

MODE_SCENE = "scene"
RANDOM_CYCLE_INTERVAL_SECONDS = 30

PLATFORMS: tuple[Platform, ...] = (
    Platform.BUTTON,
    Platform.NUMBER,
    Platform.SELECT,
    Platform.SWITCH,
)

# Captured from the Hombli Smart Christmas Light RGB controller. Keep the
# vendor-app spelling for compatibility, including "Mistery Mix".
SCENE_CODES: dict[str, str] = {
    "Rainbow Cascade": "0006",
    "Disco dance": "0007",
    "Spectrum Sparkle": "0009",
    "National holiday": "0015",
    "Valentine day": "0017",
    "Festive Fireworks": "0022",
    "Dreamland": "0023",
    "Coral Reef": "0024",
    "Polka dots": "0026",
    "Aurora Borealis": "0028",
    "Celestial Symphony": "0034",
    "Water fountain": "0040",
    "Candle Light": "0046",
    "Cupid's flight": "0049",
    "Shiny pearls": "0057",
    "Winter Whirlwind": "0002",
    "Festival of Lights": "0005",
    "Harmonic Hues": "0008",
    "Electric blip": "0011",
    "Confetti party": "0014",
    "Swedish Rave": "0016",
    "Mixed signals": "0025",
    "Radiant Rhapsody": "0029",
    "Prismatic Play": "0051",
    "Valentine's favorite": "0003",
    "Crazy Colors": "0004",
    "Color flash": "0021",
    "Strobe": "0037",
    "Cosmic Pulse": "0055",
    "Fire truck": "0056",
    "Electric sparks": "0012",
    "Santa's party": "0018",
    "Santa's little helpers": "0019",
    "Polar Express": "0035",
    "Christmas Carol": "0038",
    "Reindeer Run": "0039",
    "Red white and blue": "0043",
    "Dazzling Santa": "0044",
    "Crushed ice": "0045",
    "Mistletoe Magic": "0050",
    "Icicle Illusion": "0054",
    "Starry night": "0058",
    "Soul pulse": "0020",
    "Nordic pulse": "0031",
    "Fire storm": "0036",
    "Ocean Breeze": "0041",
    "Snowy grasslands": "0052",
    "Police siren": "0010",
    "The hulk": "0013",
    "Vibrant Vortex": "0027",
    "Glowing lanterns": "0030",
    "Cherry wave": "0032",
    "Dragon dance": "0033",
    "Strawberry disco": "0042",
    "Space alien": "0047",
    "Mistery Mix": "0048",
    "Luminous Lagoon": "0053",
}

SCENES: tuple[str, ...] = tuple(SCENE_CODES)
