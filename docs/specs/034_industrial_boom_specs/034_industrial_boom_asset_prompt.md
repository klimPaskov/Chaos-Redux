# Asset production prompt for Event 34 Industrial Boom

Produce the Event 34 visual package listed in the asset inventory of [part 9](034_industrial_boom_spec_part_9_presentation_assets_text.md#asset-inventory).
Part 9 owns the subjects, the art rules and the presentation choice; this prompt carries only the production handoff.
Follow `CLAUDE.md` and the `chaos-redux-event-assets` skill, which own the image-generation route, transparency, processing and DDS rules.

## Scope

- Generated scenes (opening report image, one static category picture) route to `chaosx_generated_event_art`.
- Icons (category, decisions and missions, country effects, state modifiers, four achievement triplets) route to `chaosx_icon_artist`.
- Out of scope: portraits, flags, focus icons, unit counters, 3D models, super-event assets, animation, meters and phase variants of the category picture.
- The Long Fall triplet already exists under `gfx/achievements/` and is not recreated.

## Working identifiers

Use these stems for files and the sprites the parent will register:

| Family | Stems |
| --- | --- |
| Report and category | `034_industrial_boom_opening_report`, `034_industrial_boom_category_picture`, `034_industrial_boom_category_icon` |
| Decisions and missions | `034_industrial_boom_run_hot`, `_stabilize_supply`, `_build_reserve`, `_cool_expansion`, `_designate_project`, `_protect_region`, `_abandon_project`, `_controlled_landing`, `_prevent_crash`, `_emergency_halt`, `_speculative_expansion`, `_miracle_region`, `_contain_spread` |
| Country effects | `034_industrial_boom_idea_boom`, `_idea_speculative_mania`, `_idea_industrial_miracle`, `_idea_runaway`, `_idea_export_orders`, `_idea_reconversion`, `_idea_exhaustion` |
| State modifiers | `034_industrial_boom_state_region`, `_state_protected`, `_state_secured`, `_state_fragile_miracle`, `_state_spreading`, `_state_unfinished_works` |
| Achievements | `chaos_redux_034_managed_expansion`, `chaos_redux_034_miracle_holds`, `chaos_redux_034_redline_nation`, `chaos_redux_034_built_to_last`, each with grey and not-eligible variants matching the existing Long Fall triplet |

Decision and mission stems carry the `034_industrial_boom` prefix shown in the first stem.

## Per-family requirements

- Inspect the exact consumer and reference family for each family before production, and use its native dimensions.
- Related state and effect icons share palette and frame logic but differ by symbol, never by color alone.
- Category art contains no buttons, numbers or meters.
- Achievement filenames match the achievement IDs and sit where the existing Long Fall files sit.

## Handoff

Use `docs/assets/034_industrial_boom/` as the working folder and write its `manifest.md` and `gfx_handoff.md` with, per asset: stem, family, source mode, prompt, reference consumer, final path, dimensions, alpha mode, DDS settings, proposed sprite name and review result.
Final runtime files go into event-scoped engine folders; nothing in runtime references the working folder.
Do not edit gameplay, localisation, GUI, `.gfx` or the catalog workbook; the parent wires and validates the assets.
