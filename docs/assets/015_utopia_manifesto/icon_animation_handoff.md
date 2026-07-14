# Event 015 icon and animation handoff

Runtime sprite registry: `interface/015_utopia_manifesto.gfx`

## Current Exact Package (2026-07-14)

- Focus use: `122` assignments, `72` unique base sprites, `72` matching `_shine` sprites, all current textures `94x86`. The folder retains `109` family DDS files in total.
- Decisions/categories/missions: `decision_icon_mapping.csv` contains `139` exact rows (`9` categories, `98` decisions, `32` missions). Every mapped sprite has a registered `32x32` DDS. The parent implementation agent still needs to add the gameplay `icon =` assignments.
- Ideas: all `12` unique picture tokens used by the current `50` idea entries have registered `64x64` DDS files; ten missing exact pictures were generated in this pass.
- Achievements: all `14` exact current `utopia_manifesto_*` ids have base, `_grey`, and mandated-overlay `_not_eligible` files (`42` total), plus `42` explicit sprite aliases. The older `36` `015_utopia_*` files are retained historical assets, not current coverage.
- Live authored-frame additions:
  - `GFX_utopia_need_warning_{static,animated}`: `8` distinct source frames, `64x64`, `512x64` sheet, `5 fps`.
  - `GFX_utopia_reserve_fill_{static,animated}`: `8` distinct source frames, `300x24`, `2400x24` sheet, `4 fps`.
  - `GFX_utopia_formation_ready_seal_{static,animated}`: `10` distinct source frames, `96x96`, `960x96` sheet, `5 fps`.
- Source and review proof:
  - `docs/assets/015_utopia_manifesto/source_png/final_icons/`
  - `docs/assets/015_utopia_manifesto/processed_png/final_icons/`
  - `docs/assets/015_utopia_manifesto/animations/<asset>/`
  - `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json`

## Historical 2026-07-01 Static Icon Package Notes

The subsections below preserve the earlier regeneration handoffs. Their decision/idea and achievement counts are superseded by the current exact package above. The cosmetic-flag subsection remains the separate flag handoff and was not changed by the icon/frame pass.

### Focus Icons

- Runtime folder: `gfx/interface/goals/015_utopia_manifesto/`
- Runtime size: `94x86`
- Source proof: `docs/assets/015_utopia_manifesto/source_png/focus_atlas_*_imagegen_atlas.png`
- Contact sheets:
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_01.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_02.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_03.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_04.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_all.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_focus_icon_regeneration.md`
- Validation: 109 runtime `goal_utopia_*` DDS files exist, are `94x86`, and have transparent unused corners.

### Decision, Category, and Idea Icons

- Decision/category runtime folder: `gfx/interface/decisions/015_utopia_manifesto/`
- Idea runtime folder: `gfx/interface/ideas/015_utopia_manifesto/`
- Decision/category runtime size: `32x32`
- Idea runtime size: `64x64`
- Source proof:
  - `docs/assets/015_utopia_manifesto/source_png/decision_idea_regenerated_imagegen_decision_atlas_source.png`
  - `docs/assets/015_utopia_manifesto/source_png/decision_idea_regenerated_imagegen_idea_atlas_01_source.png`
  - `docs/assets/015_utopia_manifesto/source_png/decision_idea_regenerated_imagegen_idea_atlas_02_source.png`
- Contact sheets:
  - `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_decisions.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_ideas.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_decision_idea_icon_regeneration.md`
- Validation: 25 runtime decision/category DDS files are `32x32`; 31 runtime idea DDS files are `64x64`; the regenerated icons have transparent unused corners and no obvious white square backgrounds.

### Achievement Icons

- Runtime folder: `gfx/achievements/`
- Runtime size: `64x64`
- Stems covered:
  - `015_utopia_new_utopia`
  - `015_utopia_need_not_greed`
  - `015_utopia_friends_without_treaties`
  - `015_utopia_six_hour_country`
  - `015_utopia_no_bloody_glory`
  - `015_utopia_inland_island`
  - `015_utopia_storehouses_abroad`
  - `015_utopia_league_of_need`
  - `015_utopia_marked_bounds_survivor`
  - `015_utopia_all_useful_arts`
  - `015_utopia_renounced_bounds`
  - `015_utopia_paper_no_more`
- Variants: base, `_grey`, and `_not_eligible`
- Contact sheet: `docs/assets/015_utopia_manifesto/contact_sheets/achievements_regenerated_imagegen_contact.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_achievement_icon_regeneration.md`
- Validation: all 36 runtime achievement DDS files exist, are `64x64`, and have no obvious white square backgrounds.

### Cosmetic Flags

- Runtime folders:
  - `gfx/flags/`
  - `gfx/flags/medium/`
  - `gfx/flags/small/`
- Cosmetic tags:
  - `utopia_new_utopia`
  - `utopia_necessary_commonwealth`
  - `utopia_league_of_need`
  - `utopia_marked_bounds_state`
- Runtime sizes: `82x52`, `41x26`, and `10x7`
- Ideology variants: each cosmetic tag has `democratic`, `communism`, `fascism`, and `neutrality` copies in all three runtime flag folders.
- Source proof: `docs/assets/015_utopia_manifesto/source_png/flag_utopia_*_source.png`
- Contact sheet: `docs/assets/015_utopia_manifesto/contact_sheets/utopia_cosmetic_flags_imagegen_contact.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_cosmetic_flag_asset_handoff.md`
- Validation: final TGAs match the existing HOI4 flag convention, remain readable by color and silhouette at small size, and include ideology variants so cosmetic tags replace arbitrary accepting-country flags consistently.

## Historical 2026-07-01 Animated GUI Package

This section preserves the older five-animation generation tranche. Those pieces use discrete generated frames, but only the Ledger seal is referenced by the current GUI; the other four remain registered legacy sequences. The current live Need, reserve, and formation-ready animations are listed above.

The full `gfx/interface/015_utopia_manifesto/` runtime family was regenerated from actual imagegen source art on 2026-07-01 after the earlier UI pieces were rejected as visually weak. The regenerated package covers the three Ledger panels, all five historical animated sheets, and all five static fallbacks. Source proof lives in `docs/assets/015_utopia_manifesto/source_png/utopia_*_source.png` and `docs/assets/015_utopia_manifesto/source_png/utopia_*_sheet_source.png`; review proof lives in `docs/assets/015_utopia_manifesto/contact_sheets/utopia_runtime_panels_regenerated_contact.png` and each animation's `previews/` folder.

| Asset | Static sprite | Animated sprite | Frame count | Frame size | Sheet size | Runtime use |
| --- | --- | --- | --- | --- | --- | --- |
| Ledger seal | `GFX_utopia_ledger_seal_static` | `GFX_utopia_ledger_seal_animated` | 8 | `64x64` | `512x64` | wired in `interface/015_utopia_manifesto_ledger.gui` |
| Overreach warning | `GFX_utopia_overreach_warning_static` | `GFX_utopia_overreach_warning_animated` | 8 | `64x64` | `512x64` | retained registered legacy sequence |
| Storehouse fill | `GFX_utopia_storehouse_fill_static` | `GFX_utopia_storehouse_fill_animated` | 8 | `64x16` | `512x16` | retained registered legacy sequence |
| New Utopia seal | `GFX_utopia_new_utopia_seal_static` | `GFX_utopia_new_utopia_seal_animated` | 10 | `96x96` | `960x96` | retained registered legacy sequence |
| Marked Bounds seal | `GFX_utopia_marked_bounds_seal_static` | `GFX_utopia_marked_bounds_seal_animated` | 10 | `96x96` | `960x96` | retained registered legacy sequence |

Panel regeneration:

- `GFX_utopia_ledger_background_panel` -> `gfx/interface/015_utopia_manifesto/utopia_ledger_background_panel.dds` (`700x500`)
- `GFX_utopia_ledger_header_plate` -> `gfx/interface/015_utopia_manifesto/utopia_ledger_header_plate.dds` (`700x96`)
- `GFX_utopia_ledger_warning_panel` -> `gfx/interface/015_utopia_manifesto/utopia_ledger_warning_panel.dds` (`320x128`)

Runtime visibility triggers:

- `utopia_ledger_new_utopia_seal_visible`
- `utopia_ledger_marked_bounds_seal_visible`
- `utopia_ledger_storehouse_fill_visible`
- `utopia_ledger_overreach_warning_visible`

## Current Runtime Coverage

- Every current focus and idea reference has a registered, present, correctly sized texture.
- Every row in `decision_icon_mapping.csv` has a registered, present, correctly sized texture; gameplay icon fields are the remaining parent integration step.
- Every exact current Event 015 achievement id has its complete triplet in the root `gfx/achievements/` folder.
- Every current Ledger GUI sprite reference resolves, and the three requested live animations have static fallbacks, distinct source frames, exact sheets, GIF previews, and contact sheets.
- Report/news/super-event completeness is tracked separately in `manifest.md`; the icon/frame package does not claim the five blocked route-specific super-event images.
