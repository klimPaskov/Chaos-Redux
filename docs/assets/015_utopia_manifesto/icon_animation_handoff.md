# Event 015 icon and animation handoff

Runtime sprite registry: `interface/015_utopia_manifesto.gfx`

## Static Icon Packages

All Event 015 runtime icon families have final DDS files, source PNGs, processed PNG previews, DDS staging copies, contact sheets, and subagent handoffs.

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

## Animated GUI Pieces

All animated GUI pieces are built from discrete generated source frames, not transform-only movement of a single still. Each animated asset has source frames, processed frames, a sheet PNG, a final DDS sheet, a static fallback DDS, and a contact sheet or GIF preview under `docs/assets/015_utopia_manifesto/animations/`.

The full `gfx/interface/utopia_manifesto/` runtime family was regenerated from actual imagegen source art on 2026-07-01 after the earlier UI pieces were rejected as visually weak. The regenerated package covers the three Ledger panels, all five animated sheets, and all five static fallbacks. Source proof lives in `docs/assets/015_utopia_manifesto/source_png/utopia_*_source.png` and `docs/assets/015_utopia_manifesto/source_png/utopia_*_sheet_source.png`; review proof lives in `docs/assets/015_utopia_manifesto/contact_sheets/utopia_runtime_panels_regenerated_contact.png` and each animation's `previews/` folder.

| Asset | Static sprite | Animated sprite | Frame count | Frame size | Sheet size | Runtime use |
| --- | --- | --- | --- | --- | --- | --- |
| Ledger seal | `GFX_utopia_ledger_seal_static` | `GFX_utopia_ledger_seal_animated` | 8 | `64x64` | `512x64` | wired in `interface/015_utopia_manifesto_ledger.gui` |
| Overreach warning | `GFX_utopia_overreach_warning_static` | `GFX_utopia_overreach_warning_animated` | 8 | `64x64` | `512x64` | visible in the Ledger under high Overreach, high Suspicion, Marked Bounds pressure, or Marked Bounds State identity |
| Storehouse fill | `GFX_utopia_storehouse_fill_static` | `GFX_utopia_storehouse_fill_animated` | 8 | `64x16` | `512x16` | visible in the Ledger once store network, local storehouse, or Common Store State route exists |
| New Utopia seal | `GFX_utopia_new_utopia_seal_static` | `GFX_utopia_new_utopia_seal_animated` | 10 | `96x96` | `960x96` | visible in the Ledger after `utopia_manifesto_new_utopia_identity` |
| Marked Bounds seal | `GFX_utopia_marked_bounds_seal_static` | `GFX_utopia_marked_bounds_seal_animated` | 10 | `96x96` | `960x96` | visible in the Ledger after `utopia_manifesto_marked_bounds_state_identity` |

Panel regeneration:

- `GFX_utopia_ledger_background_panel` -> `gfx/interface/utopia_manifesto/utopia_ledger_background_panel.dds` (`700x500`)
- `GFX_utopia_ledger_header_plate` -> `gfx/interface/utopia_manifesto/utopia_ledger_header_plate.dds` (`700x96`)
- `GFX_utopia_ledger_warning_panel` -> `gfx/interface/utopia_manifesto/utopia_ledger_warning_panel.dds` (`320x128`)

Runtime visibility triggers:

- `utopia_ledger_new_utopia_seal_visible`
- `utopia_ledger_marked_bounds_seal_visible`
- `utopia_ledger_storehouse_fill_visible`
- `utopia_ledger_overreach_warning_visible`

## Runtime Coverage

- Every `GFX_goal_utopia_*`, `GFX_decision_utopia_*`, `GFX_decision_category_utopia_*`, `GFX_idea_utopia_*`, Event 015 achievement sprite, Event 015 GUI sprite, report image, news image, and super-event image has a registered sprite or valid HOI4 flag path.
- Static fallbacks exist for every animated GUI piece.
- No icon family is marked complete from placeholder-only art.
