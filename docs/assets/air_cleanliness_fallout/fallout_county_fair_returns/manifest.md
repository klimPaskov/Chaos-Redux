# The County Fair Returns — report-event asset manifest

- Asset slug: `fallout_county_fair_returns`
- Working event identity: `chaosx.fallout.565` / `FALLOUT-565` (provisional only; the addendum relinquishes those ids and the parent must collision-rescan before wiring).
- Asset type: fictional ordinary Fallout report-event image.
- Intended use: static report popup for the North American rural-recovery chain “The County Fair Returns.”
- Source mode: `$imagegen` (built-in imagegen tool).
- Source rationale: the scene is fictional alternate-history post-Fallout material with no required real person, real place, real event, or archival object; generation provides the requested empty county fairground and controlled no-text composition.
- Canonical family inspected: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/` and its `contact_sheet.png`; vanilla report cards use a 210x176 sepia documentary-card treatment with transparent corners.
- Visual constraints honored: cold but hopeful frost-browned rural recovery; repaired timber barns and sheet-metal pens; seed, preserved-food, and repaired-tool tables; guarded entry; blank community/remembrance boards; no people, flags, readable text, logos, zombies, corpses, radioactive creatures, modern props, amusement rides, or super-event composition.
- Source PNG: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/source_png/report_event_fallout_county_fair_returns_source.png` (1536x1024 RGB; generated source retained).
- Prompt record: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/prompts/report_event_fallout_county_fair_returns_imagegen.txt`.
- Processed PNG: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/processed_png/report_event_fallout_county_fair_returns.png` (exact 210x176 RGBA; local `process_report_event_image.py`; sepia, grain, tilted card, soft shadow, transparent corners).
- Final DDS: `gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds` (exact 210x176, one-level uncompressed BGRA 32-bit; repository `convert_to_dds.py`).
- Proposed sprite: `GFX_report_event_fallout_county_fair_returns`.
- Target `.gfx`: existing Fallout report-event sprite registry selected by the parent wiring pass; this asset-only subagent did not edit or guess a new `.gfx` file.
- Related consumer: opening report event for the County Fair Returns ordinary chain; no animation, icon family, audio, portrait, GUI, or super-event surface.
- Status: `handed_off` (source, processed preview, runtime DDS, prompt, hashes, and handoff are complete; parent still owns `.gfx` registration and collision-checked gameplay wiring).
- Retained alternate candidate: `source_png/fallout_county_fair_returns_source.png` with `processed_png/fallout_county_fair_returns_processed.png`; this earlier generated composition includes fictional civilians and is not the selected runtime source for this handoff. Its review sheet is `contact_sheets/fallout_county_fair_returns_contact.png`.
- Contact-sheet note: the retained sheet documents the alternate candidate; the selected people-free source is documented separately by its source/processed paths and hash pair.
- Hashes: `docs/assets/air_cleanliness_fallout/fallout_county_fair_returns/hashes.sha256`.

## Requirement-to-runtime crosswalk

| Requirement | Source package | Runtime path / sprite | Status |
| --- | --- | --- | --- |
| One dedicated static fictional Fallout report image for The County Fair Returns | `source_png/report_event_fallout_county_fair_returns_source.png` → `processed_png/report_event_fallout_county_fair_returns.png` | `gfx/event_pictures/fallout_world_end/report_event_fallout_county_fair_returns.dds` → proposed `GFX_report_event_fallout_county_fair_returns` | Handed off; parent `.gfx` registration pending |

The retained alternate is provenance/review evidence only and does not replace the selected runtime source above.
