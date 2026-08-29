# Event 31 Random Terror generated event-art handoff

Producer: `chaosx_generated_event_art`.

Scope completed: fourteen missing fictional non-portrait report-event scenes were generated, processed, converted, and placed under `gfx/event_pictures/031_random_terror/`.

No existing Event 31 runtime DDS was overwritten.

## Runtime report assets

Every row below has a generated source PNG under `docs/assets/031_random_terror/source_png/`, a processed 210x176 RGBA preview under `docs/assets/031_random_terror/processed_png/`, and a final 210x176 DDS at the listed runtime path.

| Final DDS | Proposed sprite | Consumer target | Alpha/format | Review |
|---|---|---|---|---|
| `gfx/event_pictures/031_random_terror/report_event_armed_enclave_captured_town.dds` | `GFX_report_event_031_random_terror_armed_enclave_captured_town` | Event 31 report-event picture slot for captured-town enclave scene | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_border_corridor_military_protection.dds` | `GFX_report_event_031_random_terror_border_corridor_military_protection` | Event 31 report-event picture slot for protected border corridor | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_burned_depot_captured_equipment.dds` | `GFX_report_event_031_random_terror_burned_depot_captured_equipment` | Event 31 report-event picture slot for burned depot aftermath | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_capital_emergency_guard.dds` | `GFX_report_event_031_random_terror_capital_emergency_guard` | Event 31 report-event picture slot for capital emergency guard | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_defecting_soldiers_insurgency.dds` | `GFX_report_event_031_random_terror_defecting_soldiers_insurgency` | Event 31 report-event picture slot for defector-insurgency scene | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_intelligence_raid_recovered_documents.dds` | `GFX_report_event_031_random_terror_intelligence_raid_recovered_documents` | Event 31 report-event picture slot for intelligence raid aftermath | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_international_network_gathering.dds` | `GFX_report_event_031_random_terror_international_network_gathering` | Event 31 report-event picture slot for fictional international network gathering | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Replacement selected after rejecting national-like banner candidate; parent review pending |
| `gfx/event_pictures/031_random_terror/report_event_liberation_reconstruction.dds` | `GFX_report_event_031_random_terror_liberation_reconstruction` | Event 31 report-event picture slot for liberation and reconstruction | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_public_building_emergency.dds` | `GFX_report_event_031_random_terror_public_building_emergency` | Event 31 report-event picture slot for indirect public-building crisis | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Safer evacuation/cordon formulation accepted after initial provider rejection; parent review pending |
| `gfx/event_pictures/031_random_terror/report_event_relief_workers_attack_aftermath.dds` | `GFX_report_event_031_random_terror_relief_workers_attack_aftermath` | Event 31 report-event picture slot for relief workers and victims aftermath | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_religious_civic_rejection.dds` | `GFX_report_event_031_random_terror_religious_civic_rejection` | Event 31 report-event picture slot for fictional religious/civic rejection scene | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_rival_factions_border_standoff.dds` | `GFX_report_event_031_random_terror_rival_factions_border_standoff` | Event 31 report-event picture slot for rival faction standoff | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_synchronized_uprising.dds` | `GFX_report_event_031_random_terror_synchronized_uprising` | Event 31 report-event picture slot for synchronized uprising | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |
| `gfx/event_pictures/031_random_terror/report_event_territorial_proclamation.dds` | `GFX_report_event_031_random_terror_territorial_proclamation` | Event 31 report-event picture slot for territorial proclamation | RGBA card with transparent corners; one-level 32-bit BGRA DDS | Parent visual review and `.gfx` wiring pending |

## Suggested `.gfx` handoff

The exact Event 31 `.gfx` registry file and runtime event-picture identifiers were not provided, so the main agent must place these entries in the existing Event 31 report-picture registry after checking its local convention.

```text
spriteType = {
	name = "GFX_report_event_031_random_terror_<basename>"
	texturefile = "gfx/event_pictures/031_random_terror/report_event_<basename>.dds"
}
```

Replace `<basename>` with the stable basename in the runtime table and keep the sprite names unchanged once wired.

## Existing assets preserved

The following existing report DDS files were inspected and left untouched: `report_event_01_evacuation_station.dds`, `report_event_02_medic_civilian_aid.dds`, `report_event_03_railway_bridge_repair.dds`, and `report_event_04_bomb_damaged_rail_bridge.dds`.

The existing six Event 31 news DDS files, three decision-category picture DDS files, and two super-event DDS files were also inspected and left untouched because their dimensions and standard BGRA headers were valid.

## Evidence

Source and processed contact sheets are `docs/assets/031_random_terror/contact_sheets/report_generated_sources_contact_sheet.png` and `docs/assets/031_random_terror/contact_sheets/report_generated_processed_contact_sheet.png`.

Round-trip DDS decodes are retained under `docs/assets/031_random_terror/roundtrip/`.

The complete source/prompt/hash manifest is `docs/plans/031_random_terror_plans/subagent_handoffs/031_generated_event_art_manifest.md`.

The source prompt records are `docs/assets/031_random_terror/prompts/report_generated_prompts.md`.

## Remaining gaps and scope boundaries

- Parent `.gfx` registration and event/event-log consumer wiring remain pending because the exact registry file and runtime identifiers were not supplied to this bounded worker.
- Parent visual review remains pending; all fourteen generated rows are marked `needs_user_review` rather than claiming in-game completion.
- Flags were not produced because the prompt provides pool counts but no finalized tag or cosmetic-tag identifiers, asset basenames, simultaneous assignment list, or exact runtime consumers; the parent must supply those before flat flag filenames can be locked.
- Focus, idea, national-spirit, decision, mission, state-modifier, map-mode, and achievement icon families were not changed because they are separate icon surfaces routed to `chaosx_icon_artist` and no exact accepted runtime identifiers were provided to this worker.
- Faction emblems, progression-state UI pieces, and event-owned GUI decorations were not promoted because exact visible identifiers, `.gfx`/GUI consumers, and state bindings were not supplied; existing staged files under `docs/assets/031_random_terror/` were not silently treated as runtime-ready.
- No portraits, sound, gameplay, localisation, `.gfx`, GUI, workbook, 3D model, or custom unit counter files were edited.
- No custom Event 31 unit counter was created, consistent with the explicit scope boundary.

## Validation summary

All fourteen selected final DDS files passed exact 210x176 dimensions, repository legacy BGRA header fields, exact uncompressed byte length, transparent-corner checks, and decoded DDS round-trip pixel equality against the processed PNG.

Generated event scenes were checked for modern props, readable generated text, watermarks, fake UI, graphic gore, sacred hostile branding, real extremist symbols, and national-like banner risk; the first international-gathering candidate was rejected and replaced before handoff.
