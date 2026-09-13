# Event 35 scripted-system architect handoff

## Status

This handoff records an interrupted architecture slice and is superseded by the parent implementation.

`common/scripted_effects/035_great_depression_effects.txt` now exists, `great_depression_start_or_deepen` is implemented, and its caller integrations, receipt transaction, input/output cleanup, registry handling, and active-crisis cleanup are present. The remaining body is retained as historical design evidence, not as the current implementation status.

No Event 35 events, decisions, ideas, dynamic modifiers, on actions, cluster files, localisation, achievements, spreadsheets, shared gameplay files, generated Qoder files, or generated Cursor files were edited.

## Files changed in this slice

- `common/script_constants/035_great_depression_constants.txt` was already present as an untracked Event 35 constants scaffold and now includes the API enum, policy, severity-seed, and shock-strength additions described below.
- `common/scripted_triggers/035_great_depression_triggers.txt` was added with country-scope API validation predicates.
- `docs/plans/035_great_depression_plans/subagent_handoffs/architect_api.md` is this handoff.

`common/scripted_effects/chaosx_dynamic_effects.md` was not changed because the public contract section could not be completed without the effect implementation.

## Constants added or extended

The existing `great_depression_event`, `great_depression_caller`, `great_depression_pacing`, `great_depression_history_mode`, `great_depression_evolution`, `great_depression_severity_profile`, `great_depression_shock_profile`, `great_depression_result`, and `great_depression_reject_reason` categories remain the source of the package's existing tuning and enum values.

The following additions are intended for the pending public effect implementation.

| Category | Purpose |
| --- | --- |
| `great_depression_api` | Zero/one values, contract version, Event 34/35 IDs, minimum IDs, economy gate floors, and episode/receipt increments. |
| `great_depression_severity_input` | `starting_severity`, `deepen_amount`, and `severity_profile` mode identifiers. |
| `great_depression_report_policy` | `suppress`, `queue`, and `force` report policy identifiers. |
| `great_depression_news_policy` | `suppress`, `queue`, and `force` news policy identifiers. |
| `great_depression_severity_seed` | Hidden starting seeds for independent, inherited, conversion, relapse, and active-deepening profiles. |
| `great_depression_shock_strength` | Hidden ordering used to apply only a stronger opening shock during active deepening. |

`great_depression_result` now also has the contract-facing result aliases from `accepted_merge_without_severity_change` through `rejected_invalid_economy`.

`great_depression_reject_reason` now includes `invalid_severity_input` and `receipt_ledger_full` as implementation-level extensions.

## Implemented trigger map

All predicates are country-scope unless a nested target is explicitly entered.

| Identifier | Inputs/read state | Result and intended caller |
| --- | --- | --- |
| `great_depression_has_viable_economy` | Ordinary civilian systems, non-special/nonhuman classifier, available factories, and one controlled populated industrial state. | Economy gate for all new starts and deepening calls. |
| `great_depression_is_valid_independent_target` | Viable economy, major or human-controlled, no active crisis, transition, incompatible-state, refire, or stale active-registry marker. | Independent target selector. |
| `great_depression_active_crisis_is_coherent` | Active flag, positive episode ID, bounded public Depression Severity, and bounded evolution floor. | Prevents overwriting malformed active state. |
| `great_depression_call_receipt_is_duplicate` | Country-owned `great_depression_committed_receipt_ids` array and the temporary receipt input. | Source-receipt idempotence check. |
| `great_depression_call_receipt_ledger_has_capacity` | Receipt-array length against `great_depression_event.receipt_history_cap`. | Fail-closed ledger capacity check. |
| `great_depression_call_caller_is_known` | `great_depression_call_caller_type`. | Accepts the six contract caller classes only. |
| `great_depression_call_pacing_mode_is_known` | `great_depression_call_pacing_mode`. | Accepts the four contract pacing modes. |
| `great_depression_call_history_mode_is_known` | `great_depression_call_history_mode`. | Accepts the existing Event 35 history enum. |
| `great_depression_call_report_policy_is_known` | `great_depression_call_report_policy`. | Accepts report policy values. |
| `great_depression_call_news_policy_is_known` | `great_depression_call_news_policy`. | Accepts news policy values. |
| `great_depression_call_evolution_floor_is_valid` | Floor, proof, and baseline-to-III bounds. | Validates inherited evolution floors. |
| `great_depression_call_severity_profile_is_known` | `great_depression_call_severity_profile`. | Validates profile-mode selectors. |
| `great_depression_call_shock_profile_is_known` | `great_depression_call_opening_shock_profile`. | Validates supported shock profiles. |
| `great_depression_call_event34_snapshot_is_valid` | Snapshot proof, target proof, collapse receipt, final/peak Overheating, and ordering. | Event 34 collapse context gate. |
| `great_depression_call_contagion_context_is_valid` | Source target proof, link receipt, exposure stage/proofs, and source episode proof. | Financial Contagion conversion gate. |
| `great_depression_call_worldwide_context_is_valid` | Worldwide episode, pressure stage, conversion receipt/proofs, and optional origin target. | Worldwide conversion gate. |
| `great_depression_call_relapse_context_is_valid` | Prior completed episode, window/scar/profile proofs, and no refire safeguard. | Post-recovery relapse gate. |
| `great_depression_call_source_context_is_valid` | Caller-specific source Event/episode IDs and the three context gates above. | Fail-closed source routing. |
| `great_depression_call_opening_shock_is_compatible` | Caller class and shock profile. | Stops a caller from selecting another caller's shock. |
| `great_depression_call_pacing_is_compatible` | Caller class and pacing mode. | Enforces independent-only normal pacing and no-pacing conversions. |
| `great_depression_call_new_crisis_target_is_valid` | Viable economy and no active/transition/incompatible state. | New-crisis branch gate. |
| `great_depression_call_active_target_is_valid` | Coherent active crisis and approved deepening caller. | Active-crisis deepening branch gate. |

The pending effect should use these predicates in the contract order: reset outputs, contract/country/economy/caller/source/receipt/mode/evolution/severity/context/target validation, then one transaction, then input cleanup.

## Public contract expected by the pending effect

The public effect identifier remains `great_depression_start_or_deepen` in country scope.

The required temporary inputs are the exact `great_depression_call_*` fields in `035_great_depression_reusable_crisis_api.md`, including caller type, source Event/episode IDs, receipt, contract proof, pacing/history/report/news policies, evolution floor/proof, one severity-mode proof, and opening-shock profile.

The proof fields referenced by the trigger file are:

- `great_depression_call_starting_severity_proof`.
- `great_depression_call_deepen_amount_proof`.
- `great_depression_call_severity_profile_proof`.
- `great_depression_call_source_country_proof` with regular target `great_depression_call_source_country`.
- `great_depression_call_source_state_proof` with regular target `great_depression_call_source_state`.
- `great_depression_call_worldwide_origin_proof` with regular target `great_depression_call_worldwide_origin`.
- `great_depression_call_snapshot_supplied_proof`, `great_depression_call_snapshot_target_proof`, and `great_depression_call_snapshot_collapse_receipt_id`.
- `great_depression_call_snapshot_final_overheating` and `great_depression_call_snapshot_peak_overheating`.
- `great_depression_call_contagion_link_receipt_id`, `great_depression_call_contagion_exposure_stage`, `great_depression_call_contagion_exposure_proof`, `great_depression_call_contagion_conversion_proof`, and `great_depression_call_contagion_source_episode_proof`.
- `great_depression_call_worldwide_episode_id`, `great_depression_call_worldwide_episode_proof`, `great_depression_call_worldwide_pressure_stage`, `great_depression_call_worldwide_conversion_receipt_id`, and `great_depression_call_worldwide_conversion_proof`.
- `great_depression_call_relapse_prior_episode_id`, `great_depression_call_relapse_prior_completion_proof`, `great_depression_call_relapse_window_proof`, `great_depression_call_relapse_scar_proof`, and `great_depression_call_relapse_profile`.

The effect must reset and expose the following temporary outputs without persisting derived public selectors: `great_depression_call_result`, `great_depression_call_reject_reason`, `great_depression_call_episode_id`, `great_depression_call_started`, `great_depression_call_deepened`, `great_depression_call_no_op`, `great_depression_call_active_evolution`, `great_depression_call_final_severity`, `great_depression_call_opening_shock_applied`, `great_depression_call_report_queued`, `great_depression_call_history_recorded`, and `great_depression_call_pacing_counted`.

Depression Severity must remain the only public Event 35 event-specific number. Episode IDs, receipt rows, phase, shock strength, source rows, and evolution flags are internal registry state.

## Original helper map for `035_great_depression_effects.txt` (implemented)

The following helper map is the smallest implementation needed to complete the requested slice.

| Helper | Scope | Inputs | Outputs/side effects |
| --- | --- | --- | --- |
| `great_depression_reset_call_outputs` | Country | None. | Resets every public output before validation. |
| `great_depression_clear_call_inputs` | Country | All temporary `great_depression_call_*` inputs and proof selectors. | Clears selectors after success or rejection; regular caller targets remain chain-owned and auto-clear. |
| `great_depression_resolve_starting_severity` | Country | Starting severity or profile mode, plus optional Event 34 snapshot values. | Temporary resolved starting severity clamped to the public 0–100 range. |
| `great_depression_resolve_deepening` | Country | Active Severity, deepen amount or profile, and current floor. | Temporary bounded Severity candidate and change proof. |
| `great_depression_apply_evolution_floor` | Country | Validated floor and current floor. | Raises the floor and lower-stage hidden flags without lowering an existing floor. |
| `great_depression_apply_opening_shock` | Country | Validated shock profile and current hidden shock strength. | Stores the stronger shock profile once, sets a parent-consumption pending flag, and returns the applied proof. |
| `great_depression_register_active_episode` | Country | Allocated episode ID. | Adds the country once to `global.great_depression_active_countries` and updates its count without world iteration. |
| `great_depression_record_source_receipt` | Country | Caller, source Event/episode, receipt, and optional source targets. | Appends receipt and aligned source arrays, preserving reload idempotence. |
| `great_depression_record_history` | Country | Episode, caller, receipt, and history mode. | Appends Event 35-owned history rows and returns the history proof. |
| `great_depression_queue_external_surfaces` | Country | Report/news policies and episode/source metadata. | Sets pending report/news flags for the parent Event History/report adapters. |
| `great_depression_initialize_new_crisis` | Country | Validated inputs and resolved severity. | Allocates one global episode ID, sets active state, stores the sole public Severity value, and marks center/modifier/category work pending for parent wiring. |
| `great_depression_deepen_active_crisis` | Country | Coherent active state and validated conversion/deepening inputs. | Preserves the episode, raises only bounded Severity/floor/shock state, merges one receipt, and avoids a second category/idea/pacing transaction. |
| `great_depression_cleanup_active_crisis` | Country | Current Event 35 active state. | Removes active flags/runtime variables and the country from the active registry while preserving receipt/history arrays and earned scars. |
| `great_depression_reconcile_active_registry` | Country | Current active flag and registry entry. | Repairs one country entry after load or removes one stale entry without scanning the world. |
| `great_depression_start_or_deepen` | Country | Full public contract. | Orchestrates validation and exactly one new/deepen/duplicate/reject outcome. |

## Registry and cleanup plan

Receipt idempotence should use a persistent country-scoped numeric array named `great_depression_committed_receipt_ids`, checked with `is_in_array` before any mutation and appended only after all validation succeeds.

Aligned Event 35-owned arrays should preserve `great_depression_committed_source_events`, `great_depression_committed_source_episodes`, `great_depression_committed_callers`, `great_depression_committed_pacing_modes`, and `great_depression_committed_history_modes`.

The active registry should be `global.great_depression_active_countries`; the active episode ID remains on each country as `great_depression_active_episode_id`, avoiding an aligned global array that cleanup would have to splice by index.

Cleanup must clear active runtime flags and variables, including `great_depression_active`, `great_depression_depression_severity`, `great_depression_active_episode_id`, `great_depression_evolution_floor`, phase, trend, opening-shock, pending-work, and hidden evolution flags.

Cleanup must preserve committed receipt arrays, source/history rows, repeat memory, scars, and other completed recovery records.

## Integration points for the parent

- Event 35's independent event must select a country with `great_depression_is_valid_independent_target = yes`, fill the full public contract, use `normal_event`, and call `great_depression_start_or_deepen = yes` in that exact country scope.
- Event 34 must freeze its snapshot and call the API with `industrial_boom_collapse`, `source_event_id = constant:great_depression_api.event_34_id`, `consequence_no_pacing`, snapshot proof fields, and one collapse receipt before clearing its mutable boom state.
- Financial Contagion must supply the source country target and contagion link/exposure proofs and use `conversion_no_pacing`.
- Worldwide conversion must supply the global episode/pressure/conversion proofs and use `conversion_no_pacing`; the global row remains owned by the worldwide system.
- Relapse must supply the prior completed episode and window/scar/profile proofs and use `conversion_no_pacing`.
- Parent-owned effects still need to consume pending center initialization, modifier refresh, active evaluation registration, report/news, Event History, and cluster/pacing flags because those files were explicitly out of this slice.
- The Event 34 inherited-region companion `great_depression_register_inherited_region` is not implemented here and remains a separate parent/architect integration point.

## Assumptions and known limitations

- The trigger layer assumes the existing Chaos Redux classifiers `uses_normal_civilian_systems`, `is_special_chaos_country`, and `is_actual_nonhuman_country` remain available.
- The economy gate uses the documented `num_of_factories`, `any_controlled_state`, `state_population_k`, `industrial_complex`, `arms_factory`, and `dockyard` triggers.
- The transition, incompatible-state, and refire hooks are Event 35-owned flags intended for the parent lifecycle implementation; this slice does not define or synchronize them.
- No shared crisis-conflict adapter exists in this slice, so an external crisis cannot be inferred safely. The parent must set the local incompatible-state hook or add an explicit adapter before allowing independent selection.
- The trigger layer allows the existing Event 35 severity-profile enum and the `relapse` shock profile extension. The reusable API contract lists eight opening shock profiles and does not name a relapse shock profile, so the parent should either accept this documented owner extension or map relapse to an approved contract profile before integration.
- The original slice left the effect transaction, rollback snapshot, receipt append, public-output reset, public-input cleanup, and active-crisis cleanup pending; the parent implementation subsequently completed them.
- No central MCP router or wrapper skill was created.

## Validation and MCP evidence

Required offline wiki and vanilla documentation were consulted before patching, including Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, the vanilla script-constants concept documentation, script-constants schema documentation, effects documentation, triggers documentation, and scripted localisation documentation.

The read-only `hoi4.event_inspect` scan for selector `{ kind = event eventId = chaosx.nr35 }` returned `EVENT_INSPECTED_PARTIAL` with workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `e0e9419d1631a1697d0c77465dc4d1f97a07a7b5c87c9a6fc87eed5e4e75ee38`, graph hash `d2bbe9623e2e9a44e7d846afd51c095e109d9069a43ed37ef9c262bedd78cc3e`, and artifact `event-scan-e0e9419d1631.json` SHA-256 `44a4c319d623d6a4730c2ebe35c919971d7e8574e7d04b220b5c3b34bdf895b5`.

The read-only `hoi4.event_render` state view returned `EVENT_RENDERED_PARTIAL` with the same workspace/revision and artifacts `event-state-e0e9419d1631.json` SHA-256 `86b996192a905f1d178cec8cffb132f832f9423b27fa3da016f6fe2f81776434`, `event-state-e0e9419d1631.svg` SHA-256 `9a7cb857ddd10f12e2850eb76be16dccb2ad9ebc1e98588a6e17d19ca03795f8`, and `event-state-e0e9419d1631.png` SHA-256 `d95464d1cac95af9ed6e1c3aa222319b61fe33e6dd910378af43110978219f87`.

The MCP reports had no hard blocker, but both deferred workspace-wide helper/lifecycle projections and reported `MCP_INLINE_FILES_TRUNCATED`. These artifacts predate the completed Event 35 source/effect implementation and remain historical bounded engine evidence.

No probability inspection or AI probability audit was run because the current slice contains no weighted, random, MTTH, AI-score, or probability-bearing helper.

No local Clausewitz parse or in-game validation was run in the interrupted slice because the public effect file did not yet exist and this subagent does not launch Hearts of Iron IV.

## Git status

No commit was created for the interrupted slice. Its implemented descendants belong to the parent Event 35 tranche.
