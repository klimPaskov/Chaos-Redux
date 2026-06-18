# Event 012 Africa Regional Authority Portrait GFX Handoff

Date: `2026-06-18`
Scope: static leader portraits for human regional authority tags
Status: parent-wired

## Portrait Sprite Handoff

| Tag | History leader name | Sprite name | Final DDS path | `.gfx` file | Use note |
| --- | --- | --- | --- | --- | --- |
| `WAC` | West African Congress | `GFX_portrait_012_africa_west_african_congress` | `gfx/leaders/012_africa/leader_012_africa_wac_west_african_congress.dds` | `interface/012_africa.gfx` | human regional congress portrait |
| `SAH` | Sahel Caravan | `GFX_portrait_012_africa_sahel_caravan` | `gfx/leaders/012_africa/leader_012_africa_sah_sahel_caravan.dds` | `interface/012_africa.gfx` | human caravan-logistics authority portrait |
| `MAG` | Maghreb Coast | `GFX_portrait_012_africa_maghreb_coast` | `gfx/leaders/012_africa/leader_012_africa_mag_maghreb_coast.dds` | `interface/012_africa.gfx` | human coastal authority portrait |
| `NHR` | Nile-Horn League | `GFX_portrait_012_africa_nile_horn_league` | `gfx/leaders/012_africa/leader_012_africa_nhr_nile_horn_league.dds` | `interface/012_africa.gfx` | human Nile-Horn diplomatic authority portrait |
| `EAC` | East African Railway Congress | `GFX_portrait_012_africa_east_african_railway_congress` | `gfx/leaders/012_africa/leader_012_africa_eac_east_african_railway_congress.dds` | `interface/012_africa.gfx` | human railway authority portrait |
| `GLK` | Great Lakes Council | `GFX_portrait_012_africa_great_lakes_council` | `gfx/leaders/012_africa/leader_012_africa_glk_great_lakes_council.dds` | `interface/012_africa.gfx` | human Great Lakes civic authority portrait |
| `CBC` | Congo Basin Charter | `GFX_portrait_012_africa_congo_basin_charter` | `gfx/leaders/012_africa/leader_012_africa_cbc_congo_basin_charter.dds` | `interface/012_africa.gfx` | human river-basin charter authority portrait |
| `ZSC` | Zambezi-Stone Cities | `GFX_portrait_012_africa_zambezi_stone_cities` | `gfx/leaders/012_africa/leader_012_africa_zsc_zambezi_stone_cities.dds` | `interface/012_africa.gfx` | human southern stone-seat authority portrait |
| `SLC` | South African Liberation Congress | `GFX_portrait_012_africa_south_african_liberation_congress` | `gfx/leaders/012_africa/leader_012_africa_slc_south_african_liberation_congress.dds` | `interface/012_africa.gfx` | human liberation congress portrait |
| `IOC` | Indian Ocean Congress | `GFX_portrait_012_africa_indian_ocean_congress` | `gfx/leaders/012_africa/leader_012_africa_ioc_indian_ocean_congress.dds` | `interface/012_africa.gfx` | human island/ocean congress portrait |

## Parent Wiring Note

The sprite registrations are already in `interface/012_africa.gfx`, and the matching `history/countries/` files reference the registered sprite ids. No generic fallback portrait remains for these ten regional authority histories.
