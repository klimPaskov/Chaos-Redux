# Fallout Living World Pilot Report Event GFX Handoff

## Handoff status

Three dedicated Fallout report-event textures are registered in `interface/fallout_world_end.gfx`. Asset production and sprite registration are complete. Event attachment remains pending because the reserved event roots are not implemented.

Suggested target file: `interface/fallout_world_end.gfx`

## Files created

- `docs/assets/fallout_world_end/living_world_pilot/manifest.md`
- `docs/assets/fallout_world_end/living_world_pilot/gfx_handoff.md`
- `docs/assets/fallout_world_end/living_world_pilot/contact_sheets/fallout_living_world_pilot_report_events_contact_sheet.png`, RGB PNG, `1420x1435`
- `docs/assets/fallout_world_end/living_world_pilot/source_png/report_event_fallout_last_inventory_source.png`, RGB PNG, `1448x1086`
- `docs/assets/fallout_world_end/living_world_pilot/source_png/report_event_fallout_river_intake_at_dawn_source.png`, RGB PNG, `1448x1086`
- `docs/assets/fallout_world_end/living_world_pilot/source_png/report_event_fallout_rail_crew_twenty_seven_source.png`, RGB PNG, `1448x1086`
- `docs/assets/fallout_world_end/living_world_pilot/processed_png/report_event_fallout_last_inventory.png`, RGBA PNG, `210x176`
- `docs/assets/fallout_world_end/living_world_pilot/processed_png/report_event_fallout_river_intake_at_dawn.png`, RGBA PNG, `210x176`
- `docs/assets/fallout_world_end/living_world_pilot/processed_png/report_event_fallout_rail_crew_twenty_seven.png`, RGBA PNG, `210x176`
- `gfx/event_pictures/fallout_world_end/report_event_fallout_last_inventory.dds`, uncompressed BGRA DDS, `210x176`
- `gfx/event_pictures/fallout_world_end/report_event_fallout_river_intake_at_dawn.dds`, uncompressed BGRA DDS, `210x176`
- `gfx/event_pictures/fallout_world_end/report_event_fallout_rail_crew_twenty_seven.dds`, uncompressed BGRA DDS, `210x176`

All three verbatim ImageGen prompts, source-mode rationales, provenance records, rights notes, hashes, processing parameters, and per-image risks are embedded in `manifest.md`.

## Registered sprite definitions

```text
spriteTypes = {
	spriteType = {
		name = "GFX_report_event_fallout_last_inventory"
		texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_last_inventory.dds"
	}

	spriteType = {
		name = "GFX_report_event_fallout_river_intake_at_dawn"
		texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_river_intake_at_dawn.dds"
	}

	spriteType = {
		name = "GFX_report_event_fallout_rail_crew_twenty_seven"
		texturefile = "gfx/event_pictures/fallout_world_end/report_event_fallout_rail_crew_twenty_seven.dds"
	}
}
```

These three inner `spriteType` blocks are present in the existing `spriteTypes = { ... }` root.

## Exact asset map

| Accepted anchor | Final identity | Registered sprite | Final DDS | Size | Format | Intended event binding |
| --- | --- | --- | --- | --- | --- | --- |
| The Last Inventory | `report_event_fallout_last_inventory` | `GFX_report_event_fallout_last_inventory` | `gfx/event_pictures/fallout_world_end/report_event_fallout_last_inventory.dds` | `210x176` | legacy one-level uncompressed 32-bit BGRA DDS | `chaosx.fallout.100`, opening food inventory and ration-law chain |
| River Intake at Dawn | `report_event_fallout_river_intake_at_dawn` | `GFX_report_event_fallout_river_intake_at_dawn` | `gfx/event_pictures/fallout_world_end/report_event_fallout_river_intake_at_dawn.dds` | `210x176` | legacy one-level uncompressed 32-bit BGRA DDS | `chaosx.fallout.107`, water intake closure, filter rationing, upstream control, or testing chain |
| Rail Crew Twenty-Seven | `report_event_fallout_rail_crew_twenty_seven` | `GFX_report_event_fallout_rail_crew_twenty_seven` | `gfx/event_pictures/fallout_world_end/report_event_fallout_rail_crew_twenty_seven.dds` | `210x176` | legacy one-level uncompressed 32-bit BGRA DDS | `chaosx.fallout.114`, protected rail-repair and corridor-control chain |

The Fallout event ID ledger reserves visible roots `chaosx.fallout.100`, `chaosx.fallout.107`, and `chaosx.fallout.114` for these three sprites. The Last Inventory, River Intake, and Rail Crew Twenty-Seven roots have concrete localisation and dormant event bindings. The River Intake and Rail Crew sprites are bound inside the Fallout-owned block in `events/fallout_world_end_events.txt`.

## Review evidence

Contact sheet:

`docs/assets/fallout_world_end/living_world_pilot/contact_sheets/fallout_living_world_pilot_report_events_contact_sheet.png`

The sheet compares every `1448x1086` generated source, its `210x176` RGBA card, and the decoded final DDS over a checker background.

Crop review findings:

- The Last Inventory keeps both clerks, the ledger, sealed tins and parcels, sacks, nearly empty crate, and empty shelving inside the final card.
- River Intake at Dawn keeps all three workers, intake grate, pump, hoses, brick pump house, river, and dawn light inside the final card.
- Rail Crew Twenty-Seven keeps all four protected workers, the damaged joint, hand tools, dirty snow, telegraph corridor, and secondary work train inside the final card.

DDS review findings for all three files:

- declared dimensions `210x176`
- exact file length `147,968` bytes
- DDS magic and header size correct
- pixel format block begins at byte 76 and uses size `32`, flags `65`, fourCC `0`, bit count `32`
- masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`
- `DDSCAPS_TEXTURE` at byte 108
- alpha range `0-255`
- all four corner alpha values `0`
- decoded DDS is pixel-identical to the processed PNG with maximum channel delta `0`

## Risks and main-agent follow-up

- These are fictional generated documentary scenes, not historical evidence. Do not attribute them to a real archive, named photographer, real waterworks, railway, or ration office.
- Clothing, respirators, pump equipment, and railway hardware are generic period-plausible forms. They are deliberately not tied to one country's exact issued equipment.
- The distant rail vehicle is secondary and not model-identifiable at the final crop.
- The accepted anchor names are planning labels, not final localisation.
- `texconv` was not available on `PATH`; the repository converter used its supported ffmpeg raw-BGRA backend. The complete header, size, alpha, and visual decode checks passed. If the parent requires DirectXTex provenance specifically, rerun the same processed PNGs with `TEXCONV_PATH` set; no art regeneration is needed.
- The main agent must confirm the three exact sprite names are used by the final Fallout event blocks before promoting the manifest to event-wired or complete.

No cross-feature asset reuse, placeholder, alternate image, or content simplification was used.
