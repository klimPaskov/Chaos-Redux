# Event 012 World-Order Flag Asset Handoff

Status: complete for the requested 39 cosmetic identities and 117 final TGA textures.

The source masters, processed PNG previews, and contact sheet are retained in `docs/assets/012_africa_world_order_flags/`. The durable runtime outputs are the 117 RGBA TGA textures in the three HOI4 flag ladders. No `.gfx` edit is required for these engine-convention flag lookups; the existing cosmetic tags should resolve the exact uppercase filenames below without adding or renaming tags.

Runtime paths for every tag follow this stable contract:

```text
gfx/flags/<TAG>.tga
gfx/flags/medium/<TAG>.tga
gfx/flags/small/<TAG>.tga
```

The normal, medium, and small canvases are 82x52, 41x26, and 10x7 respectively. Each TGA is 32-bit RGBA with raw pixels and a bottom-left origin descriptor (`descriptor = 8`, no top-origin bit), matching the vanilla flag ladder convention. The generated design is preserved through mechanical center-crop to the HOI4 aspect ratio, LANCZOS resizing, and TGA export; no procedural emblem redraw, palette swap, or recolour-only variant was used.

| Cosmetic tag | Normal | Medium | Small | Sprite / `.gfx` target |
| --- | --- | --- | --- | --- |
| `MIDDLE_EASTERN_FEDERATION` | `gfx/flags/MIDDLE_EASTERN_FEDERATION.tga` | `gfx/flags/medium/MIDDLE_EASTERN_FEDERATION.tga` | `gfx/flags/small/MIDDLE_EASTERN_FEDERATION.tga` | Engine flag lookup; no `.gfx` sprite |
| `CROSSROADS_FEDERATION` | `gfx/flags/CROSSROADS_FEDERATION.tga` | `gfx/flags/medium/CROSSROADS_FEDERATION.tga` | `gfx/flags/small/CROSSROADS_FEDERATION.tga` | Engine flag lookup; no `.gfx` sprite |
| `MIDDLE_EASTERN_CONCERT` | `gfx/flags/MIDDLE_EASTERN_CONCERT.tga` | `gfx/flags/medium/MIDDLE_EASTERN_CONCERT.tga` | `gfx/flags/small/MIDDLE_EASTERN_CONCERT.tga` | Engine flag lookup; no `.gfx` sprite |
| `MIDDLE_EASTERN_REPUBLICS` | `gfx/flags/MIDDLE_EASTERN_REPUBLICS.tga` | `gfx/flags/medium/MIDDLE_EASTERN_REPUBLICS.tga` | `gfx/flags/small/MIDDLE_EASTERN_REPUBLICS.tga` | Engine flag lookup; no `.gfx` sprite |
| `DESERT_COVENANT` | `gfx/flags/DESERT_COVENANT.tga` | `gfx/flags/medium/DESERT_COVENANT.tga` | `gfx/flags/small/DESERT_COVENANT.tga` | Engine flag lookup; no `.gfx` sprite |
| `EUROPEAN_FEDERATION` | `gfx/flags/EUROPEAN_FEDERATION.tga` | `gfx/flags/medium/EUROPEAN_FEDERATION.tga` | `gfx/flags/small/EUROPEAN_FEDERATION.tga` | Engine flag lookup; no `.gfx` sprite |
| `EUROPEAN_SOCIALIST_UNION` | `gfx/flags/EUROPEAN_SOCIALIST_UNION.tga` | `gfx/flags/medium/EUROPEAN_SOCIALIST_UNION.tga` | `gfx/flags/small/EUROPEAN_SOCIALIST_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `EUROPEAN_CONCERT` | `gfx/flags/EUROPEAN_CONCERT.tga` | `gfx/flags/medium/EUROPEAN_CONCERT.tga` | `gfx/flags/small/EUROPEAN_CONCERT.tga` | Engine flag lookup; no `.gfx` sprite |
| `EUROPEAN_CONTINENTAL_COMMAND` | `gfx/flags/EUROPEAN_CONTINENTAL_COMMAND.tga` | `gfx/flags/medium/EUROPEAN_CONTINENTAL_COMMAND.tga` | `gfx/flags/small/EUROPEAN_CONTINENTAL_COMMAND.tga` | Engine flag lookup; no `.gfx` sprite |
| `EUROPEAN_CONFEDERATION` | `gfx/flags/EUROPEAN_CONFEDERATION.tga` | `gfx/flags/medium/EUROPEAN_CONFEDERATION.tga` | `gfx/flags/small/EUROPEAN_CONFEDERATION.tga` | Engine flag lookup; no `.gfx` sprite |
| `EUROPEAN_MYTHIC_COMPACT` | `gfx/flags/EUROPEAN_MYTHIC_COMPACT.tga` | `gfx/flags/medium/EUROPEAN_MYTHIC_COMPACT.tga` | `gfx/flags/small/EUROPEAN_MYTHIC_COMPACT.tga` | Engine flag lookup; no `.gfx` sprite |
| `ASIAN_FEDERATION` | `gfx/flags/ASIAN_FEDERATION.tga` | `gfx/flags/medium/ASIAN_FEDERATION.tga` | `gfx/flags/small/ASIAN_FEDERATION.tga` | Engine flag lookup; no `.gfx` sprite |
| `ASIAN_REVOLUTIONARY_UNION` | `gfx/flags/ASIAN_REVOLUTIONARY_UNION.tga` | `gfx/flags/medium/ASIAN_REVOLUTIONARY_UNION.tga` | `gfx/flags/small/ASIAN_REVOLUTIONARY_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `ASIAN_IMPERIAL_CONGRESS` | `gfx/flags/ASIAN_IMPERIAL_CONGRESS.tga` | `gfx/flags/medium/ASIAN_IMPERIAL_CONGRESS.tga` | `gfx/flags/small/ASIAN_IMPERIAL_CONGRESS.tga` | Engine flag lookup; no `.gfx` sprite |
| `ASIAN_ANTI_COLONIAL_FRONT` | `gfx/flags/ASIAN_ANTI_COLONIAL_FRONT.tga` | `gfx/flags/medium/ASIAN_ANTI_COLONIAL_FRONT.tga` | `gfx/flags/small/ASIAN_ANTI_COLONIAL_FRONT.tga` | Engine flag lookup; no `.gfx` sprite |
| `ASIAN_CELESTIAL_COVENANT` | `gfx/flags/ASIAN_CELESTIAL_COVENANT.tga` | `gfx/flags/medium/ASIAN_CELESTIAL_COVENANT.tga` | `gfx/flags/small/ASIAN_CELESTIAL_COVENANT.tga` | Engine flag lookup; no `.gfx` sprite |
| `NORTH_AMERICAN_REPUBLICS` | `gfx/flags/NORTH_AMERICAN_REPUBLICS.tga` | `gfx/flags/medium/NORTH_AMERICAN_REPUBLICS.tga` | `gfx/flags/small/NORTH_AMERICAN_REPUBLICS.tga` | Engine flag lookup; no `.gfx` sprite |
| `NORTH_AMERICAN_COMMONWEALTH` | `gfx/flags/NORTH_AMERICAN_COMMONWEALTH.tga` | `gfx/flags/medium/NORTH_AMERICAN_COMMONWEALTH.tga` | `gfx/flags/small/NORTH_AMERICAN_COMMONWEALTH.tga` | Engine flag lookup; no `.gfx` sprite |
| `NORTH_AMERICAN_COMMAND` | `gfx/flags/NORTH_AMERICAN_COMMAND.tga` | `gfx/flags/medium/NORTH_AMERICAN_COMMAND.tga` | `gfx/flags/small/NORTH_AMERICAN_COMMAND.tga` | Engine flag lookup; no `.gfx` sprite |
| `NORTH_AMERICAN_SOCIALIST_UNION` | `gfx/flags/NORTH_AMERICAN_SOCIALIST_UNION.tga` | `gfx/flags/medium/NORTH_AMERICAN_SOCIALIST_UNION.tga` | `gfx/flags/small/NORTH_AMERICAN_SOCIALIST_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `NORTH_AMERICAN_STORM_COMPACT` | `gfx/flags/NORTH_AMERICAN_STORM_COMPACT.tga` | `gfx/flags/medium/NORTH_AMERICAN_STORM_COMPACT.tga` | `gfx/flags/small/NORTH_AMERICAN_STORM_COMPACT.tga` | Engine flag lookup; no `.gfx` sprite |
| `SOUTH_AMERICAN_REPUBLICS` | `gfx/flags/SOUTH_AMERICAN_REPUBLICS.tga` | `gfx/flags/medium/SOUTH_AMERICAN_REPUBLICS.tga` | `gfx/flags/small/SOUTH_AMERICAN_REPUBLICS.tga` | Engine flag lookup; no `.gfx` sprite |
| `SOUTH_AMERICAN_FEDERATION` | `gfx/flags/SOUTH_AMERICAN_FEDERATION.tga` | `gfx/flags/medium/SOUTH_AMERICAN_FEDERATION.tga` | `gfx/flags/small/SOUTH_AMERICAN_FEDERATION.tga` | Engine flag lookup; no `.gfx` sprite |
| `SOUTH_AMERICAN_SOCIALIST_UNION` | `gfx/flags/SOUTH_AMERICAN_SOCIALIST_UNION.tga` | `gfx/flags/medium/SOUTH_AMERICAN_SOCIALIST_UNION.tga` | `gfx/flags/small/SOUTH_AMERICAN_SOCIALIST_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `SOUTH_AMERICAN_COMMAND` | `gfx/flags/SOUTH_AMERICAN_COMMAND.tga` | `gfx/flags/medium/SOUTH_AMERICAN_COMMAND.tga` | `gfx/flags/small/SOUTH_AMERICAN_COMMAND.tga` | Engine flag lookup; no `.gfx` sprite |
| `SOUTH_AMERICAN_CONCERT` | `gfx/flags/SOUTH_AMERICAN_CONCERT.tga` | `gfx/flags/medium/SOUTH_AMERICAN_CONCERT.tga` | `gfx/flags/small/SOUTH_AMERICAN_CONCERT.tga` | Engine flag lookup; no `.gfx` sprite |
| `SOUTH_AMERICAN_SUN_COVENANT` | `gfx/flags/SOUTH_AMERICAN_SUN_COVENANT.tga` | `gfx/flags/medium/SOUTH_AMERICAN_SUN_COVENANT.tga` | `gfx/flags/small/SOUTH_AMERICAN_SUN_COVENANT.tga` | Engine flag lookup; no `.gfx` sprite |
| `OCEANIAN_FEDERATION` | `gfx/flags/OCEANIAN_FEDERATION.tga` | `gfx/flags/medium/OCEANIAN_FEDERATION.tga` | `gfx/flags/small/OCEANIAN_FEDERATION.tga` | Engine flag lookup; no `.gfx` sprite |
| `OCEANIAN_DOMINION` | `gfx/flags/OCEANIAN_DOMINION.tga` | `gfx/flags/medium/OCEANIAN_DOMINION.tga` | `gfx/flags/small/OCEANIAN_DOMINION.tga` | Engine flag lookup; no `.gfx` sprite |
| `OCEANIAN_PEOPLES_UNION` | `gfx/flags/OCEANIAN_PEOPLES_UNION.tga` | `gfx/flags/medium/OCEANIAN_PEOPLES_UNION.tga` | `gfx/flags/small/OCEANIAN_PEOPLES_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `OCEANIAN_MARITIME_COMMONWEALTH` | `gfx/flags/OCEANIAN_MARITIME_COMMONWEALTH.tga` | `gfx/flags/medium/OCEANIAN_MARITIME_COMMONWEALTH.tga` | `gfx/flags/small/OCEANIAN_MARITIME_COMMONWEALTH.tga` | Engine flag lookup; no `.gfx` sprite |
| `OCEANIAN_DEEP_SEA_COVENANT` | `gfx/flags/OCEANIAN_DEEP_SEA_COVENANT.tga` | `gfx/flags/medium/OCEANIAN_DEEP_SEA_COVENANT.tga` | `gfx/flags/small/OCEANIAN_DEEP_SEA_COVENANT.tga` | Engine flag lookup; no `.gfx` sprite |
| `AFRICA_MIDDLE_EASTERN_UNION` | `gfx/flags/AFRICA_MIDDLE_EASTERN_UNION.tga` | `gfx/flags/medium/AFRICA_MIDDLE_EASTERN_UNION.tga` | `gfx/flags/small/AFRICA_MIDDLE_EASTERN_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `AFRO_EUROPEAN_UNION` | `gfx/flags/AFRO_EUROPEAN_UNION.tga` | `gfx/flags/medium/AFRO_EUROPEAN_UNION.tga` | `gfx/flags/small/AFRO_EUROPEAN_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `AFRO_ASIAN_UNION` | `gfx/flags/AFRO_ASIAN_UNION.tga` | `gfx/flags/medium/AFRO_ASIAN_UNION.tga` | `gfx/flags/small/AFRO_ASIAN_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `AFRO_NORTH_AMERICAN_UNION` | `gfx/flags/AFRO_NORTH_AMERICAN_UNION.tga` | `gfx/flags/medium/AFRO_NORTH_AMERICAN_UNION.tga` | `gfx/flags/small/AFRO_NORTH_AMERICAN_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `AFRO_SOUTH_AMERICAN_UNION` | `gfx/flags/AFRO_SOUTH_AMERICAN_UNION.tga` | `gfx/flags/medium/AFRO_SOUTH_AMERICAN_UNION.tga` | `gfx/flags/small/AFRO_SOUTH_AMERICAN_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `AFRO_OCEANIAN_UNION` | `gfx/flags/AFRO_OCEANIAN_UNION.tga` | `gfx/flags/medium/AFRO_OCEANIAN_UNION.tga` | `gfx/flags/small/AFRO_OCEANIAN_UNION.tga` | Engine flag lookup; no `.gfx` sprite |
| `AFRICA_THE_WORLD` | `gfx/flags/AFRICA_THE_WORLD.tga` | `gfx/flags/medium/AFRICA_THE_WORLD.tga` | `gfx/flags/small/AFRICA_THE_WORLD.tga` | Engine flag lookup; no `.gfx` sprite |

The parent agent owns any final runtime audit and the decision to promote permanent provenance after Event 012 acceptance. This handoff does not edit `.gfx` or gameplay files.
