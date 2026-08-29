# Famine/migration persecution owner patch

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: bounded owner implementation complete in the current workspace; no commit created.

## Scope and ownership boundary

This patch implements only the state-scoped current-risk projection for `famine_migration_persecution_active`. The projection is written after exact accepted camp, Gulag, extermination, or CBRN owner mutations and is cleared only by matching owner terminal callbacks. It does not reinterpret ideology, war, country regime, site or building presence, quota, famine pressure, evidence, occupation law, or forced movement as persecution.

The famine core, famine decisions, mapmodes, presentation, achievements, workbook, localisation, and famine/migration adapter files were not edited. `common/scripted_effects/camp_repression_action_dispatcher_effects.txt` was inspected but not edited because its accepted generic action IDs already dispatch into the concrete owner functions patched below; adding a second dispatcher writer would duplicate the transaction.

## Files changed

- `common/script_constants/famine_migration_persecution_constants.txt` adds the shared owner-class enum: `none`, `detention`, `expanded_labor`, `labor_project`, `gulag`, `extermination`, and `cbrn_coercive_operation`.
- `common/scripted_effects/famine_migration_persecution_effects.txt` adds the state-local generation, owner marker, aggregate recompute, camp terminal preparation, and generation-matched clear helpers.
- `common/scripted_effects/famine_migration_persecution_effects.md` documents helper contracts, fields, call sites, exclusions, and lifecycle limits.
- `common/scripted_effects/camp_repression_rework_effects.txt` wires generic detention, expanded labor, generic labor projects, radicalization, evidence/inactive unregister, dismantlement, and project completion/failure.
- `common/scripted_effects/camp_repression_major_country_effects.txt` wires German/Auschwitz, German prisoner-transfer source, Japanese experiment, Soviet industrial Gulag, and Soviet extreme-repression owners.
- `common/scripted_effects/genocide_crisis_effects.txt` wires accepted Japanese experimentation and accepted German transfer source/destination owners without touching the generic registration helpers.
- `common/scripted_effects/cbrn_occupation_effects.txt` wires the accepted coercive nerve-suppression operation, responsible-country operational end, and the existing expired-record cleanup helper.
- `common/on_actions/cbrn_occupation_on_actions.txt` recomputes the state projection after the exact CBRN control-loss owner callback.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/persecution_owner_patch.md` is this handoff.

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Exact call sites |
| --- | --- | --- | --- |
| `famine_migration_persecution_issue_generation` | State scope after an accepted owner has supplied exact state and actor proof. | Initializes the state-local counter at `0`, then increments it by the shared one-unit constant. | Internal to `famine_migration_persecution_record_state`. |
| `famine_migration_persecution_record_state` | State scope; pending owner class is greater than `none`, pending actor is an existing country scope equal to `ROOT`, and an optional pending generation may be supplied by an owner with a durable nonce. | Allocates one durable state-local generation when no owner generation is supplied, forwards it to the class marker, and clears pending owner/actor/generation fields. Missing or mismatched actor proof fails closed. | All accepted owner writers listed below. |
| `famine_migration_persecution_mark_state` | State scope; pending owner class and pending generation. | Stores a separate class-active state flag, generation, actor country ID, and cause-class field. A newer generation replaces an older active generation only when it is also newer than the last ended generation. Equal active generations are idempotent; lower or already-ended generations are ignored. | Internal to the record helper; direct use is reserved for future exact owner callbacks that already have a generation. |
| `famine_migration_persecution_recompute_state` | State scope; the six exact class markers and their complete metadata. | Sets the canonical flag only when at least one class has active flag, generation, actor ID, and cause class. Metadata is selected by priority `CBRN > extermination > Gulag > expanded labor > labor project > detention`; all overlapping class markers remain active. | Called after every mark and clear, plus the exact CBRN control-loss on-action. |
| `famine_migration_persecution_prepare_camp_terminal` | State scope before evidence resolution or inactive unregister; refreshes the current camp profile at that exact owner seam. | Maps detention, expanded labor, Gulag, radicalized, or experiment profile to one class and snapshots that class generation. Contaminated and `none` profiles do not qualify. | `camp_rework_resolve_site_evidence` and `camp_rework_unregister_inactive_site`. |
| `famine_migration_persecution_prepare_camp_dismantlement` | State scope before `camp_rework_complete_dismantlement` clears concrete site flags. | Snapshots every camp-owned class generation so a dismantlement callback cannot clear a newer overlapping class through a single profile. | `camp_rework_complete_dismantlement`. |
| `famine_migration_persecution_clear_owner_state` | State scope; pending owner class and a generation captured by its exact terminal callback. | Persists the last ended generation, clears only the matching class marker/metadata, and recomputes the aggregate. A stale or lower callback does nothing. | Evidence/site invalidation, inactive unregister, generic labor project completion/failure, dismantlement, CBRN control loss, and the existing CBRN expiry-cleanup helper. |
| `famine_migration_persecution_clear_camp_owners` | State scope; dismantlement snapshots from the preparation helper. | Clears detention, expanded labor, generic project, Gulag, and extermination classes one by one, leaves CBRN ownership untouched, and recomputes again at the end. | `camp_rework_complete_dismantlement`, including Soviet dismantlement loops through the shared owner. |

## Exact writer census

| Owner class | Writer and proof boundary | State/actor/generation handling |
| --- | --- | --- |
| Detention/internment | `camp_rework_activate_detention_in_action_state` after concrete active-site registration and the existing exact-cohort custody commit. | The selected `camp_rework_action_state_id` is the state; `ROOT` is the accepting country; the state-local generation is issued only after the mutation. |
| Expanded forced labor | `camp_rework_expand_labor_in_action_state` after the accepted expansion mutates the state site and applies its existing owner effects. | The action-state pointer and `ROOT` actor are retained separately; the projection does not use quota, labor output, or Deaths as proof. |
| Generic labor project | `camp_rework_start_generic_labor_project_in_action_state` after the exact project state flag and existing custody commit. | The project gets its own class so project completion cannot clear an expanded-labor class; state-local generation is independent of the country project variable. |
| Radicalized/extermination camp | `camp_rework_radicalize_site_in_action_state` only inside `genocide_camp_conversion_succeeded > 0`. | The concrete conversion state is the target and `ROOT` is the actor; a failed conversion cannot write the projection. |
| Soviet industrial Gulag | `camp_rework_soviet_transfer_prisoners_to_industrial_camps_in_action_state` after accepted remote-Gulag pool validation, site registration, and the existing Gulag death/evidence owner. | The selected action state is exact and `ROOT` is the Soviet actor; quota, famine pressure, mission, and building values are not read as the flag. |
| Soviet extreme repression | `camp_rework_soviet_extreme_repression_in_action_state` after the exact action state receives mass-repression and mass-deportation markers and passes `camp_rework_state_can_accept_responsibility_from_root`. | Radicalization may also create an extermination class; the Gulag class is separate and overlap-safe. |
| German Auschwitz layers | `camp_rework_germany_register_auschwitz_layers` after accepted state control and only when its concrete `genocide_camp_conversion_succeeded > 0` result proves the extermination conversion. | The conversion guard prevents focus/preparation calls that only register a laboratory/profile from creating a persecution owner. The action country remains `ROOT`. |
| German prisoner transfer source | `camp_rework_germany_apply_prisoner_transfer` in the exact accepted source-state transaction after its state deaths/evidence owner. | Source state is `FROM`; actor is the transfer country `ROOT`; the accepted transfer itself supplies the concrete operation proof. State 88 is handled by the separate Auschwitz owner call. |
| Japanese prisoner experiment | `camp_rework_japan_apply_prisoner_experiment` after accepted target validation and only when `genocide_camp_conversion_succeeded > 0`. | The exact source/target state scope and `ROOT` action actor are separate from the canonical boolean. |
| Accepted genocide wrappers | `genocide_japan_prisoner_experimentation_in_from_accepted` after its conversion-success branch, and `genocide_germany_transfer_prisoners_to_experiment_site_in_from_accepted` for its exact transfer source and state-88 experiment destination. | Both wrappers keep actor and state in their existing accepted scopes. Generic `genocide_register_*_site_for_root` helpers remain writer-free. |
| Accepted CBRN coercive operation | `cbrn_occupation_apply_accepted_operation_state` only inside the existing supplied-proof plus `nerve_suppression` delivery-route branch. | The operation state is the current state scope; the actor pointer is `event_target:cbrn_action_actor` and must equal `ROOT`; the state-local generation is allocated after the exact record/chemical bridge call. Protected administration never reaches this branch. |

Every writer uses separate fields for actor ID, cause class, and generation. No writer places identity into `famine_migration_persecution_active`, and no writer calls a pressure adapter solely because the canonical flag was set.

## Exact clearer census and overlap behavior

| Terminal path | Matching clear contract |
| --- | --- |
| `camp_rework_resolve_site_evidence` | Captures the current detention, expanded, Gulag, radicalized, or experiment profile before clearing evidence responsibility, then clears only that class with its captured generation. |
| `camp_rework_unregister_inactive_site` | Captures the current profile before setting `camp_state_site_type = none`, then clears only the matching class. The exact genocide control-change path reaches this owner through `genocide_on_state_control_changed`. |
| `camp_rework_complete_dismantlement` | Captures all camp class generations before clearing concrete site flags, lets the shared unregister path clean the active registry, then clears each captured class. CBRN ownership is deliberately not touched. |
| Generic labor project completion or failure | Captures the project generation before clearing `camp_rework_labor_project_active` and clears only the project class. A missing generation fails closed. |
| Soviet Gulag dismantlement | Existing Soviet exact state loop calls `camp_rework_complete_dismantlement`, so the shared generation snapshots cover each selected Gulag state without a world scan. |
| CBRN responsible-country operational end | `cbrn_occupation_end_responsible_country_operational_modifiers` snapshots the CBRN generation before clearing the operation flags and calls the generation-matched clear. The exact `on_state_control_changed` hook then recomputes at `FROM.FROM` state scope. |
| CBRN timed expiry | `cbrn_occupation_apply_delayed_backlash` now calls the existing `cbrn_occupation_cleanup_expired_state_records` at the exact state-scoped `cbrn_occupation.1` boundary. The operation schedules `.1` after `backlash_delay_days`; current constants bind that delay to `active_days` (both 60). The cleanup helper itself requires `NOT has_state_flag = cbrn_occupation_nerve_suppression_active`, carries the current CBRN generation, and clears/recomputes only that state. A mismatched delay or replay therefore fails closed. |

The clear helper stores `*_last_ended_generation` before clearing the active class. A lower or stale callback cannot clear a newer class. If another class remains complete, recompute keeps the canonical flag set. The canonical flag is cleared only when no exact class marker has complete current state/actor/cause/generation proof.

## Generation and formula contract

For each target state and class, the counter starts at `0` and an accepted owner call advances it to the next positive generation unless the owner supplies a durable pending generation. A new class record is accepted when there is no current class generation, or when `pending_generation > current_generation` and `pending_generation > last_ended_generation`. An equal generation while still active only reasserts the class marker and does not rewrite actor/cause metadata. A lower generation, a generation equal to the last ended value, or a callback without exact state/actor proof is ignored.

The aggregate formula is `famine_migration_persecution_active = OR(current detention proof, current expanded-labor proof, current project proof, current Gulag proof, current extermination proof, current CBRN proof)`. Priority affects only the separately stored presentation metadata; it never suppresses an overlapping class. There is no Deaths formula, population formula, quota formula, famine-pressure formula, or migration-pressure side effect in this helper family.

## Event target and cleanup plan

No global event target was introduced. Pending actor pointers are short-lived state variables and are cleared by `famine_migration_persecution_record_state` after the write attempt. The CBRN writer reuses the existing `event_target:cbrn_action_actor` and existing responsible-country/action-record fields. Durable state-local fields retain class generation, actor ID, cause class, and last-ended generation for later terminal matching.

All cleanup is callback-owned and state-local. The helper does not use `every_state`, `any_state`, `every_country`, an on-daily world pulse, or a global scan. The existing bounded camp registry cleanup remains responsible for enumerating its own exact invalid-site array and calls the local unregister seam.

The focused CBRN census found no occupation active-state array/registry, no durable CBRN state event target, and no CBRN-specific `on_daily`, `on_weekly`, or `on_monthly` callback. The operation's regular event targets are action-chain pointers only; the durable state variables and timed state flag remain state-local. The existing `cbrn_occupation.1` state event is therefore the authoritative scheduled seam: it is created by the accepted operation, runs on that exact state, and reaches the expiry helper only after the owner callback's due-day and responsible-controller proof. No periodic or world-scan fallback was added.

## Migration plan from duplicated owner logic

1. Keep action selection and accepted-action validation in the existing dispatcher and country-specific owners.
2. At the end of each exact owner mutation, set the pending class and actor and call `famine_migration_persecution_record_state` once.
3. At the start of each exact owner terminal path, snapshot the current generation before the owner clears site/project/operation state.
4. Call `famine_migration_persecution_clear_owner_state` only with the captured class and generation.
5. Let `famine_migration_persecution_recompute_state` preserve overlap and clear the canonical projection only when no complete owner remains.
6. Do not add writers to generic camp registration, profile refresh, generic genocide registration, occupation-law resolution, or forced movement.

No duplicated canonical flag logic remains in the patched owner files; the dispatcher remains unchanged because it already reaches these concrete seams.

## Excluded branches and reasons

- Generic occupation-law transitions remain blocked because no callback supplies changed state, responsible actor, durable action generation, and replay identity together.
- Generic occupation-repression mortality remains blocked because its exact state/actor/amount/proximate-loss callback is absent.
- Protected CBRN administration, protective-aid, ordinary occupation law, and profile-only CBRN state changes never qualify.
- Generic camp registration, profile resolver output, passive buildings, historical/inherited/static/test registration, evidence alone, quotas, famine pressure, ideology, and country regime state never qualify.
- Generic genocide registration helpers remain writer-free because they are reached from inherited, static, test, and other non-operation paths.
- Forced movement or German transfer custody alone is not a generic persecution writer; only the concrete accepted prisoner/extermination owner seams above write the state class.
- CBRN timed expiry is covered by the exact state-scoped `cbrn_occupation.1` callback at the active-window boundary. The control-loss path remains covered separately by `cbrn_occupation_end_responsible_country_operational_modifiers` and `on_state_control_changed`.

## MCP artifacts and unsupported analysis

The required read-only owner inspection used the existing Soviet Gulag and CBRN event artifacts from the source-map handoff. The Soviet artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d505593d9cabf6588a362f43381235252d5dfe1dd26b0e44a9b70a20263c6166/964fe19800ab28a42c48000ce2a588e3d576da40c31a40b1a7351105f6594534/event-state_flow-4de24027e9ca.json` and rendered manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4341bbb35d2444911575f2728847d88b79a588e49a7de57f992819915da3496/181585f50dff96f3bae030046df87e835fd556934fbd38544236f043885511eb/event-state-4de24027e9ca-manifest.json`.

The CBRN artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b37b9275d0be40a956984735e75bdbe885e4781d01a746ba79fb55202d4fe02a/dad6f2edbcd8eb9247e2bc033d768693c87105003e495741270c726e5928b72d/event-state_flow-4de24027e9ca.json` and rendered manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4438e56af06f7be7109a5fe07f2d328b0fc1827b61c8366d1cf1ce143cdaaaae/6458efad22404ec1541761b2b1a9d6f01b57b9c0850a3f22bc595c79600d3c81/event-state-4de24027e9ca-manifest.json`.

Both event artifacts report partial inline-source coverage because `MCP_INLINE_FILES_TRUNCATED`; they establish the exact event/state callback surfaces but are not a complete repository-wide event proof. No event file was changed in this bounded owner patch.

Fresh read-only MCP checks against the current workspace also returned `EVENT_INSPECTED_PARTIAL` for `soviet_gulag.1` with state-flow artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/690230a0f3ab4deb349426c3d4846722df6010896381c3f3506c9149ca43e276/ed1924dd35bd940a10bf513dd37b88b007ea5c41b56d07bb5f39db39f4ae4970/event-state_flow-be852408485b.json` and for `cbrn_occupation.1` with state-flow artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ac6c965db41b5aa4ada7c8d4857984e199463e9181946567baab5a20373c454/c2fea5344c49f6bf9678f3b08bcba7868691f06157b1474d53626013c62fb1a3/event-state_flow-be852408485b.json`.

A follow-up `hoi4.event_inspect` refresh for `events/cbrn_occupation_events.txt` returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/36ad2d1c0f8c31eaaabbb20b796fdf488fa2e1772b86d2c0c8df7faf26aed6ed/5c3f5e3019af67c67ac4c86845dd199240b12ac3371c3de863a515c58561e960/event-state_flow-59143acd4a23.json`. It reported no blocking diagnostics, but the MCP inventory remained limited to the game tree plus the configured inline-source cap, so the exact mod callback proof remains the source census above; no new event file was introduced.

Fresh state renders returned `EVENT_RENDERED_PARTIAL` with Soviet manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ea27338bae39f35a8e7c7be70ce2e46a0cf8f491177eb13e0094031c053fb32/87161d26f90e39106bfc08f1b92f444e38509e6f9c01376e146ea573edd1041b/event-state-be852408485b-manifest.json` and CBRN manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fbd3f56cf53d882078258a83a14ff7c67d2694c007e4c48e333098a50c48ef37/51eab85e69b8a066e1449ef54a9d107418af179eb228d066474d287e27c41136/event-state-be852408485b-manifest.json`; these remain partial structural evidence.

A bounded CBRN event lint also returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85fff1e88d107acfd363b8a9c593b0e77a905671b001596a5e95f80ee3782b7f/b6af49fa653c0f9014d6bc2755a722f292de9b13bbbe785f8aba038f442fd0e1/event-lint-be852408485b.json`; the report remains subject to the MCP inline-source truncation limitation.

The mandatory probability inspections from the source-map handoff are the relief-donor artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6fe325b5f8d18593b60cedd5ad2db68759113de3f510578a3a605e4f544adab/5cbc7e89908ed791809bbdfb722c33b1f20fe35127fe538675f3dd3114a8fb96/probability-inspect-0f75dc209eba.json` and destination artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec3443bf0631130030434a7aaadabf92941eb6602f1b1289dea069ccb441b194/0b0b84ddb948539885c903817d278bfe842aabc275b652aaf31949803fae4a3b/probability-inspect-4d7797526b0f.json`; both are `PROBABILITY_SOURCE_INSPECTED` with incomplete candidate pools and no diagnostics. The custom `chaosx_ai_probability_auditor` was not callable in this runtime, and no weighted AI/probability helper was changed here, so no new probability compare was applicable.

## Validation and remaining risks

- The new helper and constants files, plus every touched Clausewitz script file, were checked for balanced braces and no early closing brace.
- A focused call-site census verified each writer has a nearby pending class and actor assignment, and verified the canonical flag has no direct writers outside the new recompute helper.
- The helper was checked for no world-scan effects, no population/Deaths effects, no pressure adapter calls, and no unsupported `<=` or `>=` operators.
- The owner terminal census verified evidence resolution, inactive unregister, complete dismantlement, Soviet dismantlement routing, generic project completion/failure, and CBRN control-loss routing.
- No live Hearts of Iron IV process was launched; live consumer validation remains with the parent/user.

The CBRN owner now has both exact control-loss and active-window expiry callbacks. The current constants couple `backlash_delay_days` to `active_days`; the cleanup helper's expired-flag guard remains the fail-closed protection if that tuning is later separated. The generic actions also lack owner-supplied nonces, so current call sites use the durable state-local monotonic generation and stale-terminal rejection; a future owner with an authoritative transaction nonce can supply it through `famine_migration_persecution_pending_generation` for stronger replay identity. No unsupported fallback was added.

No commit was created, as requested.
