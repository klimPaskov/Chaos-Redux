# Event 023 visual and audio asset manifest

Status: selected achievement runtime inventory reconciled 2026-10-03 against the 2026-09-26 promotion handoff and the parent's explicit selection in the current reconciliation request.
Three v2 triplets and four v1 triplets occupy the existing 21 achievement DDS destinations.
Parent static review is recorded separately from live consumer status, which remains `needs_user_review`.

This manifest is the source-to-runtime inventory for Event 023, `sov_nuclear_bombs`.
The achievement selection and promotion evidence is recorded below, while ordinary asset and audio records retain their existing scope.
Live HOI4 consumer acceptance remains pending.

## Runtime inventory

The package currently contains 75 Event 023 DDS files: 54 non-achievement DDS files and 21 achievement-state DDS files. The 54 non-achievement files are 2 category assets, 4 report pictures, 4 news pictures, 25 decision icons, 11 mission icons, 7 idea icons, and 1 super-event picture. The category has one static picture; the category icon is a separate ordinary icon.

| Family | Count | Runtime location | Consumer or registry | Format evidence |
| --- | ---: | --- | --- | --- |
| Category picture | 1 | `gfx/interface/decisions/023_sov_nuclear_bombs/decision_category_sov_nuclear_command_picture.dds` | `sov_nuclear_bombs_command_category`, `GFX_decision_category_sov_nuclear_command_picture` | `notes/validation.md`, 114x101 legacy BGRA DDS |
| Category icon | 1 | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_command_category_icon.dds` | `GFX_decision_category_sov_nuclear_command_icon` | `notes/decoded_dds_icons/sov_nuclear_command_category_icon.png` |
| Event reports | 4 | `gfx/event_pictures/023_sov_nuclear_bombs/report_event_sov_nuclear_*.dds` | Event 023 report events | `notes/validation.md`, report-card alpha preserved |
| News pictures | 4 | `gfx/event_pictures/023_sov_nuclear_bombs/news_event_sov_nuclear_*.dds` | public test, ultimatum, first use, breakaway custody | `notes/validation.md`, 397x153 opaque DDS |
| Decision icons | 25 | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_*.dds` | ordinary Event 023 decisions | `notes/decoded_dds_icons/` for the legacy family and `decision_icon_replacements_v1/manifest.md` for the six promoted 33x32 replacements |
| Mission icons | 11 | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_mission_*.dds` and `sov_nuclear_bombs_mission_*.dds` | ordinary Event 023 missions | `notes/mission_additions_validation.md` plus existing icon contact sheet |
| Idea icons | 7 | `gfx/interface/ideas/023_sov_nuclear_bombs/sov_nuclear_spirit_*.dds` | seven Event 023 spirits | `notes/decoded_dds_icons/`, 60x68 icon family |
| Super-event picture | 1 | `gfx/super_events/023_sov_nuclear_bombs/super_event_sov_nuclear_major_exchange.dds` | shared super-event slot 108 | `notes/validation.md`, 457x328 opaque DDS |
| Achievement states | 21 | `gfx/achievements/023_sov_nuclear_bombs_*.dds` | Seven stable achievement triplets, selected v1/v2 artwork | `notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26.md`, selected source/template audits and 21/21 runtime SHA-256 matches |

### Exact ordinary sprite aliases

The 53 aliases in `interface/023_sov_nuclear_bombs.gfx` are grouped below. The super-event alias is registered by the shared file `interface/chaosx_super_events.gfx` and is listed separately.

| Group | Aliases |
| --- | --- |
| Category | `GFX_decision_category_sov_nuclear_command_picture`, `GFX_decision_category_sov_nuclear_command_icon` |
| Reports | `GFX_report_event_sov_nuclear_arsenal_opening`, `GFX_report_event_sov_nuclear_test_report`, `GFX_report_event_sov_nuclear_accident_report`, `GFX_report_event_sov_nuclear_breakaway_custody` |
| News | `GFX_news_event_sov_nuclear_public_test`, `GFX_news_event_sov_nuclear_ultimatum`, `GFX_news_event_sov_nuclear_first_use`, `GFX_news_event_sov_nuclear_breakaway_custody` |
| Ideas | `GFX_idea_sov_nuclear_spirit_secret_arsenal`, `GFX_idea_sov_nuclear_spirit_demonstrated_arsenal`, `GFX_idea_sov_nuclear_spirit_coercive_arsenal`, `GFX_idea_sov_nuclear_spirit_retaliatory_command`, `GFX_idea_sov_nuclear_spirit_unrestrained_release`, `GFX_idea_sov_nuclear_spirit_atomic_moratorium`, `GFX_idea_sov_nuclear_spirit_broken_chain` |
| Decisions | `GFX_decision_sov_nuclear_decision_accounting`, `GFX_decision_sov_nuclear_decision_authentication`, `GFX_decision_sov_nuclear_decision_command_exercise`, `GFX_decision_sov_nuclear_decision_concealed_test`, `GFX_decision_sov_nuclear_decision_counterintelligence`, `GFX_decision_sov_nuclear_decision_delivery_preparation`, `GFX_decision_sov_nuclear_decision_depot_recall`, `GFX_decision_sov_nuclear_decision_device_assembly`, `GFX_decision_sov_nuclear_decision_device_disablement`, `GFX_decision_sov_nuclear_decision_dismantlement`, `GFX_decision_sov_nuclear_decision_final_authorization`, `GFX_decision_sov_nuclear_decision_hold_abort`, `GFX_decision_sov_nuclear_decision_hotline_standdown`, `GFX_decision_sov_nuclear_decision_joint_custody`, `GFX_decision_sov_nuclear_decision_private_signal`, `GFX_decision_sov_nuclear_decision_public_test`, `GFX_decision_sov_nuclear_decision_public_ultimatum`, `GFX_decision_sov_nuclear_decision_rail_security`, `GFX_decision_sov_nuclear_decision_reactor_construction`, `GFX_decision_sov_nuclear_decision_recovery_raid`, `GFX_decision_sov_nuclear_decision_storage_hardening`, `GFX_decision_sov_nuclear_decision_strike_preparation`, `GFX_decision_sov_nuclear_decision_target_selection`, `GFX_decision_sov_nuclear_decision_test_site_survey`, `GFX_decision_sov_nuclear_decision_wartime_demonstration` |
| Missions | `GFX_mission_sov_nuclear_mission_breakaway_operationalization`, `GFX_mission_sov_nuclear_mission_device_assembly`, `GFX_mission_sov_nuclear_mission_dismantlement_inspection`, `GFX_mission_sov_nuclear_mission_joint_custody_transfer`, `GFX_mission_sov_nuclear_mission_rail_corridor_security`, `GFX_mission_sov_nuclear_mission_retaliation_window`, `GFX_mission_sov_nuclear_mission_strike_preparation`, `GFX_mission_sov_nuclear_mission_test_preparation`, `GFX_mission_sov_nuclear_mission_ultimatum_response`, `GFX_mission_sov_nuclear_bombs_delivery_crews_mission`, `GFX_mission_sov_nuclear_bombs_command_exercise_mission` |

Achievement aliases are the stable triplets `GFX_achievement_023_sov_nuclear_bombs_<achievement>`, `GFX_achievement_023_sov_nuclear_bombs_<achievement>_grey`, and `GFX_achievement_023_sov_nuclear_bombs_<achievement>_not_eligible` for the seven IDs in `common/achievements/chaos_redux_achievements.txt`.

## Current six decision-icon runtime replacements, 2026-10-03

Disposition: `implemented` for the six parent-promoted artwork replacements, with status `fixed (parent DDS/native approved/runtime promoted)`.
Acceptance rests on the user's explicit authorization for new generation and replacement after `prompts/icon_prompt_set.md` was absent from checkout and history, plus the parent's explicit 2026-10-03 selection, review, storage-v2 edge acceptance, and completed runtime promotion supplied in this reconciliation request.
The parent opened all six initial masters, storage v2, all six actual decoded DDS files, processed native and 4x previews, and storage neutral-composited native and 4x previews including a bilinear preview.
The [selected package manifest](decision_icon_replacements_v1/manifest.md) records exact crop and alpha bounds, scale, source sizes, strict DDS evidence, and six selected DDS hashes.
The [promotion documentation handoff](../../plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_six_decision_icon_promotion_documentation_2026-10-03.md) records the acceptance basis and independently checked candidate/runtime and archive/mirror hash matches.

All paths in the selected-source, processed, and selected-package-DDS columns below are relative to this workspace.
Each row retains the existing `GFX_decision_<basename>` sprite in `interface/023_sov_nuclear_bombs.gfx` and the exact runtime destination.

| Decision-icon basename | Purpose | Selected source master | Current processed PNG | Selected package DDS | Promoted runtime DDS |
| --- | --- | --- | --- | --- | --- |
| `sov_nuclear_decision_accounting` | Stockpile accounting decision | `decision_icon_replacements_v1/source_png/sov_nuclear_decision_accounting.png` | `decision_icon_replacements_v1/processed_png/sov_nuclear_decision_accounting.png` | `decision_icon_replacements_v1/dds/sov_nuclear_decision_accounting.dds` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_accounting.dds` |
| `sov_nuclear_decision_storage_hardening` | Storage hardening decision | `decision_icon_replacements_v1/source_png/sov_nuclear_decision_storage_hardening_v2.png` | `decision_icon_replacements_v1/processed_png/sov_nuclear_decision_storage_hardening.png` | `decision_icon_replacements_v1/dds/sov_nuclear_decision_storage_hardening.dds` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_storage_hardening.dds` |
| `sov_nuclear_decision_reactor_construction` | Reactor construction decision | `decision_icon_replacements_v1/source_png/sov_nuclear_decision_reactor_construction.png` | `decision_icon_replacements_v1/processed_png/sov_nuclear_decision_reactor_construction.png` | `decision_icon_replacements_v1/dds/sov_nuclear_decision_reactor_construction.dds` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_reactor_construction.dds` |
| `sov_nuclear_decision_device_assembly` | Device assembly decision | `decision_icon_replacements_v1/source_png/sov_nuclear_decision_device_assembly.png` | `decision_icon_replacements_v1/processed_png/sov_nuclear_decision_device_assembly.png` | `decision_icon_replacements_v1/dds/sov_nuclear_decision_device_assembly.dds` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_device_assembly.dds` |
| `sov_nuclear_decision_delivery_preparation` | Delivery preparation decision | `decision_icon_replacements_v1/source_png/sov_nuclear_decision_delivery_preparation.png` | `decision_icon_replacements_v1/processed_png/sov_nuclear_decision_delivery_preparation.png` | `decision_icon_replacements_v1/dds/sov_nuclear_decision_delivery_preparation.dds` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_delivery_preparation.dds` |
| `sov_nuclear_decision_command_exercise` | Command exercise decision | `decision_icon_replacements_v1/source_png/sov_nuclear_decision_command_exercise.png` | `decision_icon_replacements_v1/processed_png/sov_nuclear_decision_command_exercise.png` | `decision_icon_replacements_v1/dds/sov_nuclear_decision_command_exercise.dds` | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_command_exercise.dds` |

The five non-storage selections use their initial source outputs, and storage uses v2.
Storage v1, v3, and v4 remain unselected historical branches, with the recorded v3/v4 fringe findings preserved.
The parent accepted storage v2 low-alpha antialiasing after RGBA pixel proof and neutral previews.
No background-removal fallback or local painting was used.
Each runtime DDS is exact 33x32 legacy BGRA32, one-level mipless, 4352 bytes, and retains native alpha with decoded pixels equal to the selected processed PNG according to parent validation.

The six initial verbatim prompts are `decision_icon_replacements_v1/prompts/sov_nuclear_decision_<stem>.md` for the six named stems above.
The selected storage edit prompt is `decision_icon_replacements_v1/prompts/sov_nuclear_decision_storage_hardening_v2_edit.md`.
[The generation trace](decision_icon_replacements_v1/prompts/generation_trace.md) retains call IDs, source hashes, exact tool-returned paths, and storage edit-input lineage.
These are new prompts and do not recover the missing original prompt set.
Other legacy icon prompt coverage remains unresolved.

The six former runtime DDS files are retained in `decision_icon_replacements_v1/runtime_before_promotion/<basename>.dds`.
The parent verified old-runtime equality with `dds/gfx/interface/decisions/023_sov_nuclear_bombs/<basename>.dds` before overwrite, and the curator verified all six retained archive/mirror pairs afterward.
The corresponding old `source_png/decisions/<basename>_source.png`, `processed_png/decisions/<basename>_33x32.png`, and legacy DDS mirrors are historical archives rather than current sources for these six rows.
No GFX change or deletion was required, and the 75-asset inventory count is unchanged.
The [historical producer handoff](../../plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_production_decision_icon_replacements_v1_2026-10-03.md) remains untouched, with candidate-only and parent-edge-pending status `superseded` by this dated current ledger.

Actual live consumer validation and MCP category acceptance remain pending.
No current category render or relevant acceptance artifact supports these six promoted icons, and full review of all 75 Event 23 assets remains incomplete.
The parent reported an absent namespace and current handshake gap in its own context.
In this curator session `mcp__hoi4_agent_tools__hoi4_decision_inspect` was exposed, but its read-only category inventory call timed out awaiting `tools/call` after 600 seconds and returned no artifact.
Tool exposure and a validation response do not establish service health, a standalone viewer, or current consumer acceptance.

## Current selected achievement runtime inventory

Disposition: `implemented` for the documented artwork replacement, with live consumer status `needs_user_review`.
The acceptance basis is the user's explicit authorization for fresh generation and replacement after the original prompt was absent, plus the parent's seven selected candidates and completed source, native64, 4x, lineage, and alpha review supplied in the current reconciliation request.
The [runtime promotion handoff](../../../docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_achievement_icon_runtime_promotion_2026-09-26.md) records the completed copies and 21/21 selected-candidate SHA-256 matches.
The [current 21-state crosswalk](notes/achievement_requirement_runtime_crosswalk_replacement_2026-09-26.md#current-selected-runtime-crosswalk) lists every exact generated master, processed state layer, composited preview, candidate DDS, runtime destination, and stable alias.

| Stable achievement ID | Selected lineage | Exact selected master relative to this workspace | Runtime state family | Parent visual finding |
| --- | --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | v2 `GEN-08` | `source_png/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_a_hundred_suns_native_source.png` | `gfx/achievements/023_sov_nuclear_bombs_a_hundred_suns{,_grey,_not_eligible}.dds` | Unmarked storage cabinet and sealed casings. |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | v2 `GEN-09` | `source_png/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_the_bomb_never_fell_native_source.png` | `gfx/achievements/023_sov_nuclear_bombs_the_bomb_never_fell{,_grey,_not_eligible}.dds` | Visibly empty locked cradle, keys, and dismantlement tools. |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | v1 `GEN-03` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_ultimatum_without_ash_native_source.png` | `gfx/achievements/023_sov_nuclear_bombs_ultimatum_without_ash{,_grey,_not_eligible}.dds` | Unused sealed device, separate keys, and blank document. |
| `023_sov_nuclear_bombs_scattered_arsenal` | v1 `EDIT-04A` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_scattered_arsenal_candidate_v2_edit.png` | `gfx/achievements/023_sov_nuclear_bombs_scattered_arsenal{,_grey,_not_eligible}.dds` | Closed depot, converging rails, distinct crates, and guard. |
| `023_sov_nuclear_bombs_firebreak` | v1 `EDIT-05A` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_firebreak_candidate_v2_edit.png` | `gfx/achievements/023_sov_nuclear_bombs_firebreak{,_grey,_not_eligible}.dds` | Rejoined field-telephone splice within the frame. |
| `023_sov_nuclear_bombs_first_and_last` | v2 `GEN-10` | `source_png/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_first_and_last_native_source.png` | `gfx/achievements/023_sov_nuclear_bombs_first_and_last{,_grey,_not_eligible}.dds` | Empty rack and tools with one cloud confined to the wrench reflection. |
| `023_sov_nuclear_bombs_the_last_telephone` | v1 `GEN-07` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_the_last_telephone_native_source.png` | `gfx/achievements/023_sov_nuclear_bombs_the_last_telephone{,_grey,_not_eligible}.dds` | Period telephone and sealed launch-key capsule. |

Selected state layers retain native generated alpha, deterministic grayscale, and the unchanged not-eligible overlay.
The canonical processor audits recorded in the v1 and v2 handoffs passed all seven v1 and three v2 candidate triplets, including the seven selected triplets.
Final 64x64 BGRA DDS states have template-backed alpha 254..255, while transparent generated masters and state-layer inputs preserve their genuine alpha.
No background-removal fallback was used.
Achievement IDs, GFX aliases, definitions, localisation, and destination filenames are unchanged.

The exact replacement prompts are `prompts/icon_prompt_set_replacement_2026-09-26.md` and `prompts/icon_prompt_set_replacement_2026-09-26_v2.md`.
The original `prompts/icon_prompt_set.md` remains missing and was never reconstructed or recovered.
All previous masters, source/edit branches, prompt files, processed outputs, candidate DDS files, and dated review evidence remain retained.
The reconciliation and document dispositions are recorded in [the asset documentation handoff](../../../docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_achievement_asset_documentation_reconciliation_2026-10-03.md).
The ignored `docs/assets/` evidence remains unstaged for the parent to stage explicitly through the shared-Git commit workflow.

## Source, processing, and review evidence

The source and processed image families for the other non-achievement assets remain under `source_png/` and `processed_png/`.
The six current decision-icon source and processed chains use the `decision_icon_replacements_v1/` paths above, while their earlier top-level files remain historical archives.
The 2026-09-25 achievement recovery record retains seven original masters at `source_png/achievements/<achievement_id>_native_source.png` with source hashes in `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_achievement_source_recovery_2026-09-25.md`.
Those masters are historical evidence, and their current-runtime inventory claims are `superseded` by the selected versioned sources above.

The historical recovery package's 21 derived subject-state layers remain under `processed_png/achievement_subject_layers/`, with processed composites under `processed_png/achievement_layers/` and `dds/achievements/review/`, and package DDS under `dds/achievements/`.
These are the 2026-09-25 recovery outputs, which were not promoted by that recovery pass.
Their exact original per-icon prompt provenance remains unresolved because `prompts/icon_prompt_set.md` is absent.
The selected replacement artwork has separate verbatim v1/v2 prompts and versioned source-to-runtime chains.

The ordinary asset decoded views remain under `notes/decoded_dds/` and `notes/decoded_dds_icons/`.
The achievement recovery sheets and `tools/build_achievement_source_recovery_sheets.py` retain the dated 2026-09-25 comparison record.
Those achievement sheets do not certify the selected replacement inventory, whose reviewed sheets are listed in the v1/v2 sections below.

The ten event/category/super-event pictures pass the raw legacy DDS header, dimensions, length, masks, and alpha checks recorded in `notes/validation.md`. The two mission additions pass source-to-processed checksums and byte-for-byte decoded-DDS equality in `notes/mission_additions_validation.md`. The icon and achievement families have decoded runtime views and family contact sheets in `notes/decoded_dds_icons/` and `contact_sheets/`.

The current parent review opened the event-art round-trip sheet, decision sheet, mission sheet, idea sheet, category sheet, mission alpha review, device-disablement review, breakaway-custody review, and achievement decoded views. A live native HOI4 consumer render is not available in this environment, so every family remains marked `needs_user_review` for the final in-game presentation gate.

The seven historical achievement triplets passed canonical source-layer audits on 2026-09-25.
That audit recorded 21 processed states equal to the then-current package/runtime DDS, 63/63 populated recovery cells, and 42/42 populated package/runtime comparison cells.
`notes/achievement_state_audit_2026-09-25.md` retains those dated static findings and the historical non-visual PNG encoding/hash note.
The original package's equivalence to current runtime is superseded by the selected replacement inventory and promotion handoff.

No background-removal fallback was used. Transparent consumers retain alpha through processing and DDS conversion. Full-canvas report, news, category-picture, and super-event consumers retain their required opaque or report-card treatment.

## Historical v1 achievement candidate package, 2026-09-26

Disposition: the candidate-only inventory below is `superseded` as current inventory by the current selected achievement runtime inventory and the runtime promotion handoff.
V1 GEN-01, GEN-02, and GEN-06 were superseded by v2 GEN-08, GEN-09, and GEN-10 after the three visual mismatches were reviewed.
V1 GEN-03, EDIT-04A, EDIT-05A, and GEN-07 were selected and promoted.
The table retains the original candidate-stage paths and review status as dated evidence.

The original `prompts/icon_prompt_set.md` is still absent from the checkout and Git history; its text was not recovered or reconstructed. After the user explicitly authorized new prompts and replacement candidates, seven distinct native ImageGen subjects were created with transparent backgrounds. The new prompts are recorded verbatim in `prompts/icon_prompt_set_replacement_2026-09-26.md`. This is new candidate provenance, not recovered provenance.

The immutable v1 generated masters and focused-edit candidates remain under `source_png/achievements/replacement_2026-09-26/`.
The historical staged input triplets remain under `processed_png/achievements/replacement_2026-09-26/source_triplets/`, with candidate DDS and review PNGs under `dds_candidates/achievements/replacement_2026-09-26/`.
At the candidate handoff no runtime files had been promoted.
The later promotion copied four selected v1 triplets and three v2 triplets to the stable runtime destinations.

| Achievement ID | Selected source PNG | Source triplet files | Staged DDS candidate files | Existing sprite family | Status |
| --- | --- | --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_a_hundred_suns_native_source.png` | `processed_png/achievements/replacement_2026-09-26/source_triplets/023_sov_nuclear_bombs_a_hundred_suns{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_a_hundred_suns{,_grey,_not_eligible}.dds` | `GFX_achievement_023_sov_nuclear_bombs_a_hundred_suns{,_grey,_not_eligible}` | `needs_user_review` |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_the_bomb_never_fell_native_source.png` | `processed_png/achievements/replacement_2026-09-26/source_triplets/023_sov_nuclear_bombs_the_bomb_never_fell{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_the_bomb_never_fell{,_grey,_not_eligible}.dds` | `GFX_achievement_023_sov_nuclear_bombs_the_bomb_never_fell{,_grey,_not_eligible}` | `needs_user_review` |
| `023_sov_nuclear_bombs_ultimatum_without_ash` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_ultimatum_without_ash_native_source.png` | `processed_png/achievements/replacement_2026-09-26/source_triplets/023_sov_nuclear_bombs_ultimatum_without_ash{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_ultimatum_without_ash{,_grey,_not_eligible}.dds` | `GFX_achievement_023_sov_nuclear_bombs_ultimatum_without_ash{,_grey,_not_eligible}` | `needs_user_review` |
| `023_sov_nuclear_bombs_scattered_arsenal` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_scattered_arsenal_candidate_v2_edit.png` | `processed_png/achievements/replacement_2026-09-26/source_triplets/023_sov_nuclear_bombs_scattered_arsenal{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_scattered_arsenal{,_grey,_not_eligible}.dds` | `GFX_achievement_023_sov_nuclear_bombs_scattered_arsenal{,_grey,_not_eligible}` | `needs_user_review` |
| `023_sov_nuclear_bombs_firebreak` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_firebreak_candidate_v2_edit.png` | `processed_png/achievements/replacement_2026-09-26/source_triplets/023_sov_nuclear_bombs_firebreak{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_firebreak{,_grey,_not_eligible}.dds` | `GFX_achievement_023_sov_nuclear_bombs_firebreak{,_grey,_not_eligible}` | `needs_user_review` |
| `023_sov_nuclear_bombs_first_and_last` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_first_and_last_native_source.png` | `processed_png/achievements/replacement_2026-09-26/source_triplets/023_sov_nuclear_bombs_first_and_last{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_first_and_last{,_grey,_not_eligible}.dds` | `GFX_achievement_023_sov_nuclear_bombs_first_and_last{,_grey,_not_eligible}` | `needs_user_review` |
| `023_sov_nuclear_bombs_the_last_telephone` | `source_png/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_the_last_telephone_native_source.png` | `processed_png/achievements/replacement_2026-09-26/source_triplets/023_sov_nuclear_bombs_the_last_telephone{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26/023_sov_nuclear_bombs_the_last_telephone{,_grey,_not_eligible}.dds` | `GFX_achievement_023_sov_nuclear_bombs_the_last_telephone{,_grey,_not_eligible}` | `needs_user_review` |

At the v1 candidate handoff all seven replacement rows were `needs_user_review` and awaited parent selection.
The native-size, 4x, alpha/round-trip, and lineage sheets remain under `contact_sheets/achievement_replacement_2026-09-26/` as `replacement_native_triplets.png`, `replacement_4x_nearest.png`, `replacement_pipeline_alpha_roundtrip.png`, and `replacement_source_lineage.png`.
Source hashes, processor output, and candidate findings remain in `notes/achievement_replacement_2026-09-26/processor_output.log` and `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_icon_artist_replacement_2026-09-26.md`.
The current crosswalk separates selected v1 rows from the three superseded v1 branches.

The stable achievement IDs, root-level runtime DDS destinations, and `GFX_achievement_<achievement_id>` aliases remain unchanged.
Parent review and promotion of the seven selected triplets are recorded in the current selected inventory.
No live HOI4 consumer validation is claimed.

## Historical v2 achievement candidate package, 2026-09-26

Disposition: all three v2 triplets are `implemented` as selected runtime replacements with parent review recorded in the promotion handoff.
The candidate-stage review status in the table is retained as dated evidence and is `superseded` as current inventory by the current selected inventory.
Live consumer status remains `needs_user_review`.

The parent reviewed the v1 sheets and identified three mismatches: A Hundred Suns showed an unrequested red star, The Bomb Never Fell showed a bomb in the cradle, and First and Last lacked a discernible cloud reflection at 64x64. Three fresh built-in ImageGen sources were generated with one original transparent-generation call per ID. The exact additional prompts are in `prompts/icon_prompt_set_replacement_2026-09-26_v2.md`; the original missing prompt set remains unrecovered, and the v1 prompt file and all v1 art outputs remain unchanged.

| Achievement ID | Fresh v2 selected source | V2 source triplet | V2 staged DDS triplet | Status |
| --- | --- | --- | --- | --- |
| `023_sov_nuclear_bombs_a_hundred_suns` | `source_png/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_a_hundred_suns_native_source.png` | `processed_png/achievements/replacement_2026-09-26_v2/source_triplets/023_sov_nuclear_bombs_a_hundred_suns{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_a_hundred_suns{,_grey,_not_eligible}.dds` | `needs_user_review` |
| `023_sov_nuclear_bombs_the_bomb_never_fell` | `source_png/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_the_bomb_never_fell_native_source.png` | `processed_png/achievements/replacement_2026-09-26_v2/source_triplets/023_sov_nuclear_bombs_the_bomb_never_fell{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_the_bomb_never_fell{,_grey,_not_eligible}.dds` | `needs_user_review` |
| `023_sov_nuclear_bombs_first_and_last` | `source_png/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_first_and_last_native_source.png` | `processed_png/achievements/replacement_2026-09-26_v2/source_triplets/023_sov_nuclear_bombs_first_and_last{,_grey,_not_eligible}.png` | `dds_candidates/achievements/replacement_2026-09-26_v2/023_sov_nuclear_bombs_first_and_last{,_grey,_not_eligible}.dds` | `needs_user_review` |

V2 reviewed sheets remain under `contact_sheets/achievement_replacement_2026-09-26_v2/` as `v2_native_triplets.png`, `v2_4x_nearest.png`, `v2_pipeline_alpha_roundtrip.png`, and `v2_source_lineage.png`.
The processor output and hash inventory remain in `notes/achievement_replacement_2026-09-26_v2/processor_output.log` and `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_icon_artist_replacement_2026-09-26_v2.md`.
All three v2 triplets passed strict 64x64 BGRA and source/template equality audits and were subsequently promoted to `gfx/achievements/` after parent review.

## Audio

The unique Event 023 exchange cue is `sound/023_sov_nuclear_bombs/super_event_108_first_major_exchange.wav`. Its public-domain source, rights evidence, conversion command, metadata, and checksum are recorded in `docs/super_events/023_sov_nuclear_bombs_super_event_research.md` and `provenance/`. The shared sound registry owns the playback definition `chaosx_super_event_108_track` and settings-aware wrappers.

## Picture reuse for the round 2 report and news events

The report and news events added in round 2 reuse existing Event 023 pictures, and the two foreign timed ideas reuse vanilla idea icons; no new art was made, by design (lead round 2 decision 8), so none is pending.

| Runtime use | Sprite |
| --- | --- |
| `chaosx.nr23.107` intelligence report | `GFX_report_event_sov_nuclear_test_report` |
| `chaosx.nr23.111` missing physicist and `chaosx.nr23.113` foreign aircraft | `GFX_report_event_sov_nuclear_test_report` |
| `chaosx.nr23.112` rail manifest and `chaosx.nr23.115` lost component | `GFX_report_event_sov_nuclear_breakaway_custody` |
| `chaosx.nr23.114` contaminated workers | `GFX_report_event_sov_nuclear_accident_report` |
| `chaosx.news.235` secret test detected | `GFX_news_event_sov_nuclear_public_test` |
| `chaosx.nr23.190` and `chaosx.nr23.191` major strategic reports | `GFX_report_event_sov_nuclear_test_report` |
| `chaosx.nr23.192` atomic race report | `GFX_report_event_sov_nuclear_arsenal_opening` |
| `chaosx.nr23.193` Soviet partner report | `GFX_report_event_sov_nuclear_arsenal_opening` |
| `sov_nuclear_bombs_enforcement_window_mission` | `GFX_mission_sov_nuclear_mission_ultimatum_response` |
| `sov_nuclear_bombs_counterintelligence_sweep` | `GFX_decision_sov_nuclear_decision_counterintelligence` |
| `sov_nuclear_bombs_foreign_atomic_priority` idea | vanilla `GFX_idea_generic_research_bonus` |
| `sov_nuclear_bombs_foreign_air_defence` idea | vanilla `GFX_idea_generic_anti_air` |

## Scope exclusions

Event 023 introduces no portrait, flag, custom unit, counter, 3D model, animation, or dedicated scripted GUI. No runtime file refers to those excluded asset families. Event 023 has no private Fallout or Final Silence picture and no Event 023 world-end row.
