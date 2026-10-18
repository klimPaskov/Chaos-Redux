# Event 023 GFX handoff

This handoff records the final consumer wiring for `sov_nuclear_bombs`. Gameplay and decision owners retain responsibility for selecting the correct alias; the asset package owns source provenance, processing, DDS conversion, and this inventory.

## Registry files

| Consumer family | Registry file | Rule |
| --- | --- | --- |
| Event reports, news, decisions, missions, ideas, and category | `interface/023_sov_nuclear_bombs.gfx` | 53 ordinary sprite aliases; all paths are stable and use the `gfx/.../023_sov_nuclear_bombs/` runtime folders |
| Super-event image | `interface/chaosx_super_events.gfx` | `GFX_super_event_108_soviet_nuclear_major_exchange` uses the shared slot-108 registry |
| Achievement triplets | `interface/chaosx_achievements.gfx` | The seven Event 023 achievement IDs each resolve to eligible, grey, and not-eligible sprites |
| Super-event audio | `music/chaosx_super_event_music.asset` | `chaosx_super_event_108_*` music variants play `music/023_sov_nuclear_bombs/super_event_108_first_major_exchange.ogg` |

## Category and event-picture wiring

`sov_nuclear_bombs_command_category` uses exactly one static picture, `GFX_decision_category_sov_nuclear_command_picture`. `GFX_decision_category_sov_nuclear_command_icon` is the category icon and is not a second category picture.

The report aliases are `GFX_report_event_sov_nuclear_arsenal_opening`, `GFX_report_event_sov_nuclear_test_report`, `GFX_report_event_sov_nuclear_accident_report`, and `GFX_report_event_sov_nuclear_breakaway_custody`. The news aliases are `GFX_news_event_sov_nuclear_public_test`, `GFX_news_event_sov_nuclear_ultimatum`, `GFX_news_event_sov_nuclear_first_use`, and `GFX_news_event_sov_nuclear_breakaway_custody`.

The generated report pictures use the repository report-card alpha treatment. News, category-picture, and super-event pictures are full-canvas compositions. None is an animation or a scripted-GUI background.

## Decision, mission, and idea wiring

The 25 decision aliases and 11 mission aliases are listed in `manifest.md` and correspond one-to-one with the `icon =` fields in `common/decisions/023_sov_nuclear_bombs_decisions.txt`. The seven `GFX_idea_sov_nuclear_spirit_*` aliases correspond to the seven Event 023 ideas in `common/ideas/023_sov_nuclear_bombs_ideas.txt`.

The two late-added mission aliases are `GFX_mission_sov_nuclear_bombs_delivery_crews_mission` and `GFX_mission_sov_nuclear_bombs_command_exercise_mission`. Their source, processing, alpha, and byte-for-byte DDS evidence is in `notes/mission_additions_validation.md`.

## Six decision-icon promotions, 2026-10-03

Disposition: `implemented` for the parent-promoted six-icon replacement, with status `fixed (parent DDS/native approved/runtime promoted)`.
Acceptance comes from the user's explicit new-generation and replacement authorization and the parent's 2026-10-03 completed source, native, DDS, RGBA, neutral-preview, and storage-v2 edge review supplied in this reconciliation request.
The exact basenames are `sov_nuclear_decision_accounting`, `sov_nuclear_decision_storage_hardening`, `sov_nuclear_decision_reactor_construction`, `sov_nuclear_decision_device_assembly`, `sov_nuclear_decision_delivery_preparation`, and `sov_nuclear_decision_command_exercise`.
Each retains `GFX_decision_<basename>` in `interface/023_sov_nuclear_bombs.gfx` and runtime `gfx/interface/decisions/023_sov_nuclear_bombs/<basename>.dds`.
No GFX edit was required.

[The current six-row manifest](manifest.md#current-six-decision-icon-runtime-replacements-2026-10-03) identifies the selected source masters, processed PNGs, package DDS files, and runtime destinations.
[The replacement GFX handoff](decision_icon_replacements_v1/gfx_handoff.md) records exact registrations, and [the replacement manifest](decision_icon_replacements_v1/manifest.md) preserves bounds, alpha purpose, strict DDS evidence, review references, and six hashes.
The [exact prompt trace](decision_icon_replacements_v1/prompts/generation_trace.md) preserves the new generation lineage without claiming recovery of `prompts/icon_prompt_set.md`.
The parent selected storage v2 and accepted its low-alpha antialiasing after pixel proof and neutral native and 4x review including a bilinear preview.
Storage v1, v3, and v4 remain unselected with their source findings preserved.

All six runtime hashes match the parent-selected package DDS hashes.
The prior runtime copies under `decision_icon_replacements_v1/runtime_before_promotion/` match the retained old DDS mirrors under `dds/gfx/interface/decisions/023_sov_nuclear_bombs/` for these six basenames.
Those old mirrors and the corresponding old source and processed PNGs are historical archives rather than current chains.
The [dated documentation handoff](../../plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_six_decision_icon_promotion_documentation_2026-10-03.md) records this transaction and its six hash pairs.
The historical producer handoff remains unchanged, with its candidate-only status superseded by the dated current promotion record.
Actual live consumer validation and MCP category acceptance remain pending.
The 75-asset inventory count is unchanged and full asset review remains incomplete.

## Achievement wiring

Disposition: `implemented` artwork replacement at the existing 21 DDS destinations, with live consumer status `needs_user_review`.
Acceptance comes from the user's explicit fresh-generation and replacement authorization and the parent's selection and completed review stated in the current reconciliation request.
The [runtime promotion handoff](../../../docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_achievement_icon_runtime_promotion_2026-09-26.md) records selection and 21/21 selected-candidate SHA-256 matches.
The [current 21-state crosswalk](notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26.md#current-selected-runtime-crosswalk) is the exact source, processed, candidate, runtime, and alias inventory.
The selected set is v2 GEN-08/GEN-09/GEN-10 for A Hundred Suns, The Bomb Never Fell, and First and Last, plus v1 GEN-03/EDIT-04A/EDIT-05A/GEN-07 for Ultimatum Without Ash, Scattered Arsenal, Firebreak, and The Last Telephone.

The seven stable achievement IDs are:

- `023_sov_nuclear_bombs_a_hundred_suns`
- `023_sov_nuclear_bombs_the_bomb_never_fell`
- `023_sov_nuclear_bombs_ultimatum_without_ash`
- `023_sov_nuclear_bombs_scattered_arsenal`
- `023_sov_nuclear_bombs_firebreak`
- `023_sov_nuclear_bombs_first_and_last`
- `023_sov_nuclear_bombs_the_last_telephone`

Each ID has a normal, `_grey`, and `_not_eligible` DDS state. The runtime sprite naming follows the achievement registry convention in `interface/chaosx_achievements.gfx`; no achievement icon is reused as a decision, idea, or mission icon.

## Review boundary

The selected achievement package has parent review of the full source images and v1/v2 native64, 4x, lineage, alpha, and DDS round-trip sheets, as stated in the current reconciliation request and promotion handoff.
The seven v1 and three v2 candidate triplets passed their canonical source/template audits, and all 21 selected runtime files match their selected candidate DDS bytes by SHA-256.
Generated masters and processed state layers preserve genuine alpha, while the final canonical template-backed DDS alpha remains 254..255.
No live HOI4 consumer acceptance is inferred from these static results.

The source recovery masters under `source_png/achievements/`, derived inputs under `processed_png/achievement_subject_layers/`, composites under `processed_png/achievement_layers/`, and package DDS under `dds/achievements/` retain the historical 2026-09-25 recovery record.
Its package/runtime equality claims and recovery sheets describe the inventory at that date and are `superseded` as current inventory by the versioned selected replacement crosswalk.
The repeatable recovery builder `tools/build_achievement_source_recovery_sheets.py` and its source/package/runtime sheets remain preserved as historical evidence.

The original per-icon prompt file `prompts/icon_prompt_set.md` remains absent from the checkout and Git history, and no original prompt was reconstructed or recovered.
The selected replacement sources have verbatim new provenance in `prompts/icon_prompt_set_replacement_2026-09-26.md` and `prompts/icon_prompt_set_replacement_2026-09-26_v2.md`.
The historical non-visual `scattered_arsenal_grey` PNG encoding/hash note remains in `notes/achievement_state_audit_2026-09-25.md` and does not describe the current selected candidate chain.
The [documentation reconciliation handoff](../../../docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_achievement_asset_documentation_reconciliation_2026-10-03.md) records document dispositions and validation limits.
Final live consumer review remains `needs_user_review`.

No portrait, flag, custom unit, counter, 3D model, animation, or dedicated scripted GUI handoff is required by the accepted Event 023 scope.
