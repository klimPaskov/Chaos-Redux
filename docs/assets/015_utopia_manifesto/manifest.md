# Event 015 Utopia Manifesto Asset Manifest

Event id: `015`
Event slug: `utopia_manifesto`
Runtime sprite registry: `interface/015_utopia_manifesto.gfx`

## Final Runtime Assets

- Event pictures:
  - `GFX_report_event_utopia_manifesto_found` -> `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_found.dds`
  - `GFX_news_event_utopia_boundary_crisis` -> `gfx/event_pictures/015_utopia_manifesto/news_event_utopia_boundary_crisis.dds`
- Super-event pictures:
  - `GFX_super_event_utopia_new_utopia` -> `gfx/super_events/015_utopia_manifesto/super_event_utopia_new_utopia.dds`
  - `GFX_super_event_utopia_marked_bounds` -> `gfx/super_events/015_utopia_manifesto/super_event_utopia_marked_bounds.dds`
- Ledger GUI:
  - `GFX_utopia_ledger_background_panel`
  - `GFX_utopia_ledger_header_plate`
  - `GFX_utopia_ledger_warning_panel`
  - `GFX_utopia_ledger_seal_static`
  - `GFX_utopia_ledger_seal_animated`
- Animated GUI pieces with static fallbacks:
  - `utopia_ledger_seal`
  - `utopia_overreach_warning`
  - `utopia_storehouse_fill`
  - `utopia_new_utopia_seal`
  - `utopia_marked_bounds_seal`
- Focus icons:
  - Every `GFX_goal_utopia_*` sprite referenced by `common/national_focus/015_utopia_manifesto_focus_tree.txt` has a final DDS under `gfx/interface/goals/015_utopia_manifesto/`.
- Decision and category icons:
  - Every `GFX_decision_utopia_*` and `GFX_decision_category_utopia_*` sprite referenced by `common/decisions/015_utopia_manifesto_decisions.txt` and `common/decisions/categories/015_utopia_manifesto_categories.txt` has a final DDS under `gfx/interface/decisions/015_utopia_manifesto/`.
- Idea icons:
  - Every `GFX_idea_utopia_*` sprite referenced by `common/ideas/015_utopia_manifesto_ideas.txt` has a final DDS under `gfx/interface/ideas/015_utopia_manifesto/`.
- Achievements:
  - All 12 achievement icons and their `_grey` and `_not_eligible` variants are under `gfx/achievements/`.
- Cosmetic flags:
  - `utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_league_of_need`, and `utopia_marked_bounds_state` exist in normal, medium, and small HOI4 flag folders.
  - Each cosmetic tag also has `democratic`, `communism`, `fascism`, and `neutrality` variants in normal, medium, and small folders, derived from the corresponding generated base flag art so arbitrary accepting countries do not retain ideology-specific original flags.

## Source, Processed, and Preview Files

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/`
- Processed PNGs: `docs/assets/015_utopia_manifesto/processed_png/`
- DDS staging copies: `docs/assets/015_utopia_manifesto/dds/`
- Contact sheets: `docs/assets/015_utopia_manifesto/contact_sheets/`
- Animation frame packages: `docs/assets/015_utopia_manifesto/animations/`
- Tooling:
  - `docs/assets/015_utopia_manifesto/_tooling/process_utopia_assets.py`
  - `docs/assets/015_utopia_manifesto/_tooling/complete_utopia_assets.py`
  - `docs/assets/015_utopia_manifesto/_tooling/regenerate_utopia_runtime_visuals.py`

## 2026-07-01 Focus Icon Regeneration

Scope: focus icons only.

The full Event 015 focus icon family was regenerated from actual imagegen source art after the previous focus pack was rejected as placeholder-like. The pass covers all 109 existing `goal_utopia_*` runtime focus DDS files under `gfx/interface/goals/015_utopia_manifesto/`, including the 99 focus-tree-referenced sprites and the additional focus-family DDS files already present in the runtime folder.

Source mode:

- Seven imagegen-generated focus atlases were copied into `docs/assets/015_utopia_manifesto/source_png/` as `focus_atlas_*_imagegen_atlas.png`.
- Each `<stem>_source.png` focus source is a crop from one of those imagegen atlases.
- Local processing was limited to chroma-key removal, transparent cropping/fitting, 94x86 resizing, contact-sheet creation, and DDS export.
- No primitive shape, local-script-only, or white-square placeholder source art was used for regenerated focus icons.

Updated focus deliverables:

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/goal_utopia_*_source.png`
- Processed previews: `docs/assets/015_utopia_manifesto/processed_png/goal_utopia_*.png`
- Package DDS copies: `docs/assets/015_utopia_manifesto/dds/goal_utopia_*.dds`
- Runtime DDS files: `gfx/interface/goals/015_utopia_manifesto/goal_utopia_*.dds`
- Review sheets:
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_01.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_02.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_03.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_04.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_all.png`

Validation summary:

- Focus DDS coverage: 109 regenerated, 109 runtime `goal_utopia_*` files present.
- Target size: every regenerated focus DDS is 94x86.
- Transparency: regenerated focus DDS files have transparent unused corners and no opaque white square background.
- Visual review: contact sheets were inspected after a second matte pass to remove visible chroma-key edge artifacts.

Blocked focus icons: none.

Needs parent review: none flagged by this pass.

## 2026-07-01 Decision and Idea Icon Regeneration

Scope: decision, decision-category, and idea icons only.

The Event 015 runtime decision/category and idea icon families were regenerated from actual imagegen source art after placeholder, simple-shape, white-background, and misalignment concerns were raised. This pass covers all 25 existing runtime `*.dds` files under `gfx/interface/decisions/015_utopia_manifesto/` and all 31 existing runtime `*.dds` files under `gfx/interface/ideas/015_utopia_manifesto/`.

Source mode:

- Three imagegen-generated atlases were copied into `docs/assets/015_utopia_manifesto/source_png/` as:
  - `decision_idea_regenerated_imagegen_decision_atlas_source.png`
  - `decision_idea_regenerated_imagegen_idea_atlas_01_source.png`
  - `decision_idea_regenerated_imagegen_idea_atlas_02_source.png`
- `idea_utopia_common_stores_unproven_source.png` uses a separate imagegen-generated replacement source because the first idea atlas cell produced an explicit question-mark prop.
- Each final `<stem>_source.png` decision or idea source derives from imagegen output.
- Local processing was limited to atlas cropping, chroma-key removal, transparent fitting, restrained outline/drop shadow, exact-size resizing, contact-sheet creation, and DDS export.
- No primitive shape, local-script-only, or white-square placeholder source art was used for regenerated decision/category or idea icons.

Updated decision and idea deliverables:

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/decision_*_source.png` and `docs/assets/015_utopia_manifesto/source_png/idea_*_source.png`
- Processed previews: `docs/assets/015_utopia_manifesto/processed_png/decision_*.png` and `docs/assets/015_utopia_manifesto/processed_png/idea_*.png`
- Package DDS copies: `docs/assets/015_utopia_manifesto/dds/decision_*.dds` and `docs/assets/015_utopia_manifesto/dds/idea_*.dds`
- Runtime DDS files:
  - `gfx/interface/decisions/015_utopia_manifesto/*.dds`
  - `gfx/interface/ideas/015_utopia_manifesto/*.dds`
- Review sheets:
  - `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_decisions.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_ideas.png`

Validation summary:

- Decision/category DDS coverage: 25 regenerated, 25 runtime files present.
- Idea DDS coverage: 31 regenerated, 31 runtime files present.
- Target size: every regenerated decision/category DDS is 32x32; every regenerated idea DDS is 64x64.
- Transparency: regenerated runtime DDS files have transparent unused corners and no opaque white square background.
- Visual review: contact sheets were inspected over checker backgrounds for alignment, white-square backgrounds, and chroma-key remnants.

Blocked decision or idea icons: none.

Needs parent review: none flagged by this pass.

## 2026-07-01 Achievement Icon Regeneration

Scope: Event 015 achievement icons and their disabled variants.

The Event 015 achievement icon family was regenerated from actual imagegen source art after parent review found the earlier achievement contact sheet still looked like flat placeholder emblems. This pass covers all 12 achievement stems and their `_grey` and `_not_eligible` variants.

Updated achievement deliverables:

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/015_utopia_*_source.png`
- Processed previews: `docs/assets/015_utopia_manifesto/processed_png/015_utopia_*.png`
- Package DDS copies: `docs/assets/015_utopia_manifesto/dds/015_utopia_*.dds`
- Runtime DDS triplets: `gfx/achievements/015_utopia_*.dds`
- Review sheet: `docs/assets/015_utopia_manifesto/contact_sheets/achievements_regenerated_imagegen_contact.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_achievement_icon_regeneration.md`

Validation summary:

- Achievement DDS coverage: 12 stems with base, `_grey`, and `_not_eligible` variants; 36 runtime files present.
- Target size: every regenerated achievement DDS is 64x64.
- Visual review: contact sheet was inspected for imagegen-backed medal art, disabled variants, and absence of white square backgrounds.

Blocked achievement icons: none.

## 2026-07-01 Cosmetic Flag Generation

Scope: late-route cosmetic identity flags.

Four late cosmetic identities were generated from actual imagegen source art and exported into the project-standard HOI4 flag folders.

Runtime flag deliverables:

- `gfx/flags/utopia_new_utopia.tga`
- `gfx/flags/utopia_necessary_commonwealth.tga`
- `gfx/flags/utopia_league_of_need.tga`
- `gfx/flags/utopia_marked_bounds_state.tga`
- matching `gfx/flags/medium/` and `gfx/flags/small/` copies
- ideology-specific copies for each tag in normal, medium, and small folders:
  - `_democratic.tga`
  - `_communism.tga`
  - `_fascism.tga`
  - `_neutrality.tga`

Review and source files:

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/flag_utopia_*_source.png`
- Processed PNGs: `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_*_processed.png`
- Contact sheet: `docs/assets/015_utopia_manifesto/contact_sheets/utopia_cosmetic_flags_imagegen_contact.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_cosmetic_flag_asset_handoff.md`

Validation summary:

- Normal flags are 82x52, medium flags are 41x26, and small flags are 10x7.
- Final TGAs match the repo's existing flag pattern and remain visually distinct at small size.
- Parent follow-up after the country-package-adjacent audit added all ideology-specific flag variants from the generated base flags, closing the runtime cosmetic-flag fallback risk for countries with ideology-specific original flags.

## 2026-07-01 Runtime Ledger Panel and Animation Regeneration

Scope: the full runtime family in `gfx/interface/utopia_manifesto/`.

The Event 015 Ledger panels and animated GUI pieces were regenerated from actual imagegen source art after the runtime UI folder was rejected as visually weak. This pass covers all 13 runtime DDS files in `gfx/interface/utopia_manifesto/`, including static panels, animated frame sheets, and static fallbacks.

Source mode:

- Imagegen-generated sources were copied into `docs/assets/015_utopia_manifesto/source_png/` as `utopia_*_source.png` and `utopia_*_sheet_source.png`.
- Animated pieces were processed into discrete per-frame source PNGs under `docs/assets/015_utopia_manifesto/animations/<asset>/source_frames/`.
- Local processing was limited to transparent extraction, frame fitting, sheet construction, contact/previews, DDS export, and staging copies.
- No primitive shape, local-script-only, single-still transform-only, or white-square placeholder source art was used for the regenerated Ledger runtime family.

Updated runtime deliverables:

- `gfx/interface/utopia_manifesto/utopia_ledger_background_panel.dds` (`700x500`)
- `gfx/interface/utopia_manifesto/utopia_ledger_header_plate.dds` (`700x96`)
- `gfx/interface/utopia_manifesto/utopia_ledger_warning_panel.dds` (`320x128`)
- `gfx/interface/utopia_manifesto/utopia_ledger_seal_sheet.dds` (`512x64`, 8 frames)
- `gfx/interface/utopia_manifesto/utopia_ledger_seal_static.dds` (`64x64`)
- `gfx/interface/utopia_manifesto/utopia_overreach_warning_sheet.dds` (`512x64`, 8 frames)
- `gfx/interface/utopia_manifesto/utopia_overreach_warning_static.dds` (`64x64`)
- `gfx/interface/utopia_manifesto/utopia_storehouse_fill_sheet.dds` (`512x16`, 8 frames)
- `gfx/interface/utopia_manifesto/utopia_storehouse_fill_static.dds` (`64x16`)
- `gfx/interface/utopia_manifesto/utopia_new_utopia_seal_sheet.dds` (`960x96`, 10 frames)
- `gfx/interface/utopia_manifesto/utopia_new_utopia_seal_static.dds` (`96x96`)
- `gfx/interface/utopia_manifesto/utopia_marked_bounds_seal_sheet.dds` (`960x96`, 10 frames)
- `gfx/interface/utopia_manifesto/utopia_marked_bounds_seal_static.dds` (`96x96`)

Review files:

- Panel contact sheet: `docs/assets/015_utopia_manifesto/contact_sheets/utopia_runtime_panels_regenerated_contact.png`
- Animation contact sheets and preview GIFs: `docs/assets/015_utopia_manifesto/animations/<asset>/previews/`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_runtime_gui_animation_regeneration.md`

Runtime wiring:

- `GFX_utopia_ledger_seal_animated` is visible in the Utopian Ledger header.
- `GFX_utopia_storehouse_fill_animated` is visible once the store network/local storehouse/common-store route exists.
- `GFX_utopia_overreach_warning_animated` is visible under high Overreach, high Foreign Suspicion, Marked Bounds route pressure, or Marked Bounds State identity.
- `GFX_utopia_new_utopia_seal_animated` and `GFX_utopia_marked_bounds_seal_animated` are visible in the Ledger header after their late identities are applied.

Validation summary:

- All 13 runtime DDS files exist with expected dimensions.
- Animated sheets have the expected frame counts: Ledger seal 8, Overreach warning 8, Storehouse fill 8, New Utopia seal 10, Marked Bounds seal 10.
- Runtime sprites are registered in `interface/015_utopia_manifesto.gfx`, and live visibility triggers are wired through `interface/015_utopia_manifesto_ledger.gui` and `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`.
- Contact sheets were visually inspected for panel readability, centered transparent icons, frame distinction, and lack of white matte.

All animated GUI pieces are built from discrete generated source frames, not transform-only movement of a single still. Each animated asset has:

- source frame PNGs
- processed frame PNGs
- sheet PNG
- final sheet DDS
- static fallback DDS
- contact sheet or GIF preview

Runtime use:

- `GFX_utopia_ledger_seal_animated`, `GFX_utopia_overreach_warning_animated`, `GFX_utopia_storehouse_fill_animated`, `GFX_utopia_new_utopia_seal_animated`, and `GFX_utopia_marked_bounds_seal_animated` are all registered in `interface/015_utopia_manifesto.gfx` and wired into `interface/015_utopia_manifesto_ledger.gui` with route/value visibility triggers in `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`.

## Validation Notes

- Icon families were regenerated through subagent imagegen passes for focus, decision/category, idea, and achievement icons.
- Cosmetic flags were generated through a separate imagegen asset sidecar.
- `interface/015_utopia_manifesto.gfx` registers the final runtime sprite names used by Event 015 gameplay, UI, and super-event localisation.
- The implementation validation pass checks that every Event 015 `GFX_*` reference in script has a registered sprite and a DDS file on disk.
