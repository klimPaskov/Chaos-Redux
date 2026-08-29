# Event 31 icon artist handoff

Status: complete for the bounded static icon, emblem, and achievement-triplet scope, with one provenance item marked `needs_user_review`.

The package contains 198 static source/processed/runtime DDS rows and 36 achievement state rows, for 234 final DDS files in total. No required final DDS file is missing within the defined scope.

## Manifest and evidence

- Full per-file manifest with source path, processed path, final consumer path, dimensions, observed alpha extrema, consumer, and SHA256: `docs/assets/031_random_terror/manifest.md`.
- Achievement triplet contact sheet: `docs/assets/031_random_terror/contact_sheets/031_achievement_triplets_contact_sheet.png`.
- Focus contact sheet: `docs/assets/031_random_terror/contact_sheets/031_focus_icons_contact_sheet.png`.
- Idea contact sheet: `docs/assets/031_random_terror/contact_sheets/031_idea_icons_contact_sheet.png`.
- Decision and mission contact sheet: `docs/assets/031_random_terror/contact_sheets/031_decision_mission_icons_contact_sheet.png`.
- Faction emblem contact sheet: `docs/assets/031_random_terror/contact_sheets/031_faction_emblems_contact_sheet.png`.
- Official ImageGen prompts and the transparent-background fallback record: `docs/assets/031_random_terror/prompts/031_icon_artist_prompt_record.md`.

Each static contact sheet compares the retained source PNG, processed PNG, enlarged smooth processed preview, and decoded DDS roundtrip. The achievement contact sheet compares all three retained state layers with their decoded final DDS files.

## Runtime consumers and observed sizes

| Family | Count | Final consumer path | Processed/final canvas | Alpha result |
|---|---:|---|---:|---|
| Focus icons | 114 | `gfx/interface/goals/031_random_terror/*.dds` | 94x86 | source and final `0..255` |
| Idea/national-spirit icons | 29 | `gfx/interface/ideas/031_random_terror/*.dds` | 64x64 | source and final `0..255` |
| Decision icons | 40 | `gfx/interface/decisions/031_random_terror/*.dds` | 32x32 | source and final `0..255` |
| Mission icons | 7 | `gfx/interface/decisions/031_random_terror/*.dds` | 32x32 | source and final `0..255` |
| Faction emblems, large | 4 | `gfx/interface/emblems/031_random_terror/*faction_icon_*.dds` | 200x100 | source and final `0..255` |
| Faction emblems, miniature | 4 | `gfx/interface/emblems/031_random_terror/*faction_icon_*_miniature.dds` | 32x32 | source and final `0..255` |
| Achievement completed/grey/not eligible | 36 | `gfx/achievements/031_*.dds` | 64x64 | source `0..255`, final `254..255` because the inspected achievement consumer requires the opaque vanilla achievement template background |

The achievement IDs are `031_no_second_blast`, `031_the_long_watch`, `031_the_city_still_stands`, `031_cut_every_route`, `031_the_false_claim_rejected`, `031_no_collective_punishment`, `031_enemy_of_my_enemy`, `031_fracture_from_within`, `031_maximum_survivor`, `031_false_revelation_denied`, `031_victims_before_victory`, and `031_war_without_a_capital`. Each ID has the completed, `_grey`, and `_not_eligible` root DDS variants.

The achievement directory is intentionally root-only under `gfx/achievements/`; `gfx/interface/achievements/031_random_terror` was not created because the inspected engine family and processor consume achievement files from the root path.

There is no standalone Event 31 icon consumer defined for `gfx/interface/events/031_random_terror`, so no file was emitted there. If the parent adds an exact event-icon filename and consumer, that one family needs a new bounded request rather than a guessed asset.

The three existing opaque decision-category picture DDS files under `gfx/interface/decisions/031_random_terror` were inspected and left untouched as parent-owned assets.

## Processing and validation

The canonical reference contact sheets were inspected before individual references under the single approved root `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`, covering focuses, ideas, decisions, missions, achievements, and factions.

All static PNGs were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` at the exact processed dimensions. Achievement triplets were emitted with `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py --write-png` and audited with `--audit`; all 12 triplets reported strict 64x64 BGRA and source-layer equality.

A strict local DDS audit decoded all 234 final files, checked the legacy 124-byte header, one-level uncompressed BGRA masks, exact file lengths, dimensions, alpha extrema, and deterministic processed-to-DDS roundtrip pixels. All 234 passed.

No animation was needed, so `chaos-redux-frame-animation` was not invoked and no transform-only animation was produced.

## Needs user review and blockers

The inherited 198 static source PNGs did not have per-asset ImageGen prompt records in the workspace when this worker began. They were retained, visually inspected, processed at exact target sizes, converted, and documented in the manifest, but their prompt provenance remains `needs_user_review` if the parent requires a source-prompt audit.

The two new achievement state atlases initially failed native transparency validation because ImageGen returned RGB checkerboard-looking backdrops. The rejected outputs, targeted edit, rembg attempt, final fallback-alpha sources, and settings are retained and recorded in the prompt record. The final source layers have genuine alpha with transparent corners and the final achievement DDS files have the opaque template background required by the consumer.

No sacred or real extremist imagery, custom unit/counter/3D asset, animation, GFX edit, gameplay edit, localisation edit, spreadsheet edit, or guessed event-icon file was created.
