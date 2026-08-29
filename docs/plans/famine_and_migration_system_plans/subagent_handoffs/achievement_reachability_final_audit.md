# Famine and Migration Achievement Reachability Final Audit

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-25.

Audit mode: read-only source, documentation, asset, and MCP review. No gameplay, localisation, asset, workbook, specification, plan, or documentation source was edited except this handoff. No game was launched and no commit was created.

## Final determination

The eight achievement definitions, English names/descriptions/tooltips, sprite registrations, and 24 final DDS consumers are complete and internally aligned. The gameplay achievement surface is not complete.

`Break the Blockade` is source-unreachable because its only blockade-start producer is nested inside a stable-stage recovery branch while simultaneously requiring famine or catastrophic-famine stage flags. `They Were Hungry, Not Contagious` has an exact arrival-exposure receipt, but the achievement ledger does not consume it during the controlled-reception action that starts the first observation; the source path can only complete through a later exposed transfer, a second observation, and a later generic durable-outcome callback, with no achievement-level cohort/generation binding. `Bread Across the Front` has no achievement attempt identity or reset and can combine different corridor episodes. `The Country Did Not Empty` samples the protected floor only at stable recovery and does not cover multiple live player tag-switch routes. `Roads Home` tracks only the persisted cohort-owner country, not the separate host/origin identity promised by the specification. Several disqualifier flags are also campaign-global even where the specification requires the exact crisis or cohort.

All eight additionally depend in `possible` on a flag and population baseline written only by `on_startup`. The offline achievement documentation states that `possible` is checked at game start and that a false result permanently prevents the achievement. No authoritative documentation or installed MCP route proves that the mod's `on_startup` effects run before that one-time evaluation. This is an engine-ordering blocker for all eight, not a completion pass.

Owner patches are required before any of the eight should be certified. `The Grain Stayed Home` and `A Place at the Table` have the strongest source-side identity chains, but they still inherit the common `possible` blocker and broad campaign disqualifier policy.

## Scope and required sources read

The audit read `AGENTS.md`, all 43 files under `docs/specs/famine_and_migration_system_specs/`, the full `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `chaos-redux-decisions-missions` skills, and the existing achievement, hook, asset, completion, disposition, source-of-truth, and resume handoffs under `docs/plans/famine_and_migration_system_plans/`.

The offline wiki pages read for this audit include Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Achievement modding. The installed vanilla documentation consulted includes `documentation/triggers_documentation.md`, `documentation/effects_documentation.md`, `documentation/script_concept_documentation.md`, and `documentation/console_commands_documentation.md`. Vanilla precedent was checked in `common/achievements.txt` and the normal/grey/not-eligible triplets under `gfx/achievements/`.

The central audited source snapshot was based on Git `HEAD` `ba119e7591d6e43ac65eb4277181c2e67aa595ab`; the worktree was intentionally not assumed clean because parallel owners were active. Central file hashes at review time were:

| File | SHA-256 |
| --- | --- |
| `common/achievements/chaos_redux_achievements.txt` | `08ACC9F3B70CFE7671A40071E1E653084673DF8AF4861614409AC5C29B71C08A` |
| `common/scripted_triggers/famine_migration_achievement_triggers.txt` | `94198A431CEE0F8C947D3FEE458DA6C2C9D7023BC39141D872AED3D5BBA456FA` |
| `common/scripted_effects/famine_migration_achievement_effects.txt` | `E601258DFD06ED61DA17C2291D95DCC8B71AF617ABB92AA243C1AA3C8468567B` |
| `common/on_actions/chaosx_famine_migration_on_actions.txt` | `57EAF588921134D5323EE04B0EEAF6C1331E2FB3BBC721FA3FAC4D7CB53D82F7` |
| `common/decisions/famine_migration_decisions.txt` | `BEE9FE255E0B1F395119FB8EF690CC15001515261DBCBCB4FD8E1AA3EA8BFC76` |
| `interface/famine_and_migration_system.gfx` | `948B285D7FAB0A4F96CCE2D523E37196A806CFBB41506C3A25F4759E7D35C1C5` |
| `localisation/english/famine_migration_l_english.yml` | `50EB67F1447800F31512D88CEB98D6495B53C40EF0B3EF20C9CBE42D65BE9EA3` |

## Files and identifiers audited

Primary achievement surfaces:

- `common/achievements/chaos_redux_achievements.txt`: `unique_id = chaos_redux_achievements` and the eight definitions at lines 3850-3888.
- `common/scripted_triggers/famine_migration_achievement_triggers.txt`: `famine_migration_achievement_natural_campaign_is_valid` and the eight `*_is_complete` predicates at lines 9-158.
- `common/scripted_effects/famine_migration_achievement_effects.txt`: baseline, initialization, generation, state processing, arrival, major-cohort, blockade, gate, return, custody, corridor, medical, integration, extraction, tag-switch, and annexation recorders.
- `common/on_actions/chaosx_famine_migration_on_actions.txt`: `on_startup`, `on_daily_CXT`, `on_annex`, control/war callbacks, and exact corridor attack callbacks.
- `common/scripted_effects/chaosx_famine_migration_effects.txt`: exact cohort arrays, transfer/finalization, country cohort reconciliation, state food evaluation, achievement state pulse, retirement, and durable-outcome calls.
- `common/scripted_effects/famine_migration_decision_owner_effects.txt` and `common/scripted_triggers/famine_migration_decision_owner_triggers.txt`: exact medical exposure receipt and host/cohort/generation validation.
- `common/scripted_effects/famine_migration_corridor_effects.txt`: prepared route generation, exact offer acceptance, gate binding, terminal cleanup, and exact attack receipts.
- `common/scripted_effects/famine_migration_adapter_effects.txt`, `common/scripted_effects/camp_repression_rework_effects.txt`, and `common/scripted_effects/famine_migration_cohort_history_effects.txt`: exact custody owner receipts and A-B-A visit-cycle detection.
- `common/decisions/famine_migration_decisions.txt`: relief, corridor, medical observation, extraction, arrivals, integration, resettlement, voluntary return, forced return, and related achievement callsites.
- Player-continuation/tag-switch callsites in `events/014_cannibalism.txt`, `events/016_brilliant_scientist_containment_events.txt`, `events/018_random_resource.txt`, `common/scripted_effects/006_independence_wave_join_effects.txt`, `common/scripted_effects/014_cannibalism_effects.txt`, `common/scripted_effects/fallout_consolidated_effects.txt`, and the excluded CXT setup path in `common/scripted_effects/chaosx_test_country_effects.txt`.
- `common/scripted_effects/famine_migration_cxt_test_effects.txt` and the CXT extension setup only to confirm that the fixture cannot legitimately unlock these achievements.

Presentation surfaces:

- `localisation/english/famine_migration_l_english.yml` lines 237-261.
- `interface/famine_and_migration_system.gfx` lines 23-46.
- `gfx/achievements/famine_migration_*.dds` for all normal, `_grey`, and `_not_eligible` consumers.
- `docs/assets/famine_and_migration_system/manifest.csv` lines 22-45, source and processed achievement PNGs, `gfx_handoff.md`, contact sheets, ImageGen source log, and `subagent_handoffs/final_asset_audit.md`.

## Common definition, eligibility, and one-time semantics

The achievement registry has one root `unique_id` at `common/achievements/chaos_redux_achievements.txt:8`. Each of the eight IDs occurs exactly once at lines 3850-3888, uses the shared natural-campaign predicate in `possible`, and uses its exact completion predicate in `happened`.

The offline achievement wiki states at `paradox_wiki/Achievement modding - Hearts of Iron 4 Wiki.md:34-37` that `possible` is checked at game start and that a false result permanently prevents earning, while `happened` is the continuing completion test. The shared `possible` predicate requires `famine_migration_achievement_tracking_initialized` and a positive initial-core baseline at `common/scripted_triggers/famine_migration_achievement_triggers.txt:9-18`. The only normal producer is the guarded startup seed at `common/scripted_effects/famine_migration_achievement_effects.txt:14-37`, called by `on_startup` for every existing country at `common/on_actions/chaosx_famine_migration_on_actions.txt:11-24`. The only repair call is `on_daily_CXT` at lines 27-40, while CXT is excluded by `is_special_chaos_country = no` in the natural-campaign predicate.

This ordering is not completion-safe without engine proof. If the one-time `possible` evaluation precedes `on_startup`, the flag is false and all eight become permanently ineligible. The installed HOI4 MCP exposes no achievement inspect/render/runtime route, and live HOI4 launch is forbidden. An owner should remove runtime-initialized evidence from `possible` and retain it in `happened`, or provide authoritative runtime evidence that the startup seed precedes the one-time achievement eligibility evaluation.

The write-once baseline itself is otherwise well formed: it guards against reseeding, sums starting core-state population, and derives the integration and national-threat targets at `famine_migration_achievement_effects.txt:14-37`. The achievement engine supplies the final one-time unlock behavior; there is no need for a second completed-achievement flag.

## Eight-achievement disposition table

The `Localisation and assets` cells use this common verified package unless noted: exactly one `_NAME`, `_DESC`, and `_tooltip`; one normal, one grey, and one not-eligible sprite; three existing final 64x64 BGRA8 DDS files; no exact-byte duplicate in the full repository achievement DDS directory; and a passing strict recomposition audit.

| Achievement and exact definition | Producer and callsite chain | Reset and one-time semantics | Identity and ownership | Localisation and assets | Verdict |
| --- | --- | --- | --- | --- | --- |
| `famine_migration_break_the_blockade`, “Break the Blockade”; registry lines 3850-3853; completion trigger lines 21-38 | State food evaluation calls `famine_migration_achievement_process_state`; intended blockade start writes state/generation and `blockade_famine_proven` at effect lines 331-354; convoy/airlift deliveries call `record_blockade_relief` from decision lines 1391-1395 and 1551-1555; stable recovery calls `record_blockade_recovery` at effect lines 294-300 | Intended new state/generation clears old positive outcome flags at lines 341-352, and recovery clears the state tracker at lines 495-517; the start writer is unreachable, so this reset design never begins normally | Evidence is written to state `OWNER`, not `CONTROLLER`; therefore the specification's controller-eligible route is absent. Relief and recovery require the same state/generation when a tracker exists | Complete; localisation lines 238-240; sprites lines 23-25; manifest lines 22-24 | **Blocked/unreachable.** Mutually exclusive stage requirements prevent the only start flag; controller ownership is also incomplete |
| `famine_migration_no_one_left_at_the_gate`, “No One Left at the Gate”; registry lines 3855-3858; trigger lines 40-59 | Prepared corridor generation and acceptance bind origin/front/counterpart/offered cohort in `famine_migration_corridor_effects.txt:108-112, 285-325`; `record_gate_crisis` builds exact qualifying arrays at achievement effect lines 520-648; exact arrival branches record protection; integration/resettlement/return record exact resolution; cleanup snapshots terminal arrays at lines 742-819 | A new gate crisis clears active and terminal arrays/flags at lines 522-540; terminal cleanup preserves one completed generation and clears active identity; duplicate cohort IDs are rejected | Receiving-country ledger with exact corridor generation, origin state, front state, counterpart, cohort IDs, amounts, zero route deaths, and exact destination owner. Positive identity is strong | Complete; localisation lines 241-243; sprites lines 26-28; manifest lines 25-27 | **Partial/conditionally reachable.** Positive path is exact, but campaign-global pushback/forced-return/custody flags are not tied to the protected gate generation/cohort, and common eligibility is unproved |
| `famine_migration_roads_home`, “Roads Home”; registry lines 3860-3863; trigger lines 61-76 | Registered-country reconciliation selects one unique qualifying row and calls `record_major_cohort_duration` in `chaosx_famine_migration_effects.txt:3274-3340`; exact voluntary-return finalization calls `record_voluntary_return` at decision lines 3761-3772 | Changing the exact major cohort advances generation and clears prior return facts at achievement effect lines 419-442; maturity is date-bound; completion requires return cohort ID and generation equal the major cohort | The reconciler considers only `global.famine_migration_cohort_owners`, while the decision actor is the country managing the current host/return. A separate foreign host is not given the major-cohort ledger and a foreign origin normally cannot execute the host decision. The source path is therefore effectively limited to same-country/internal displacement | Complete; localisation lines 244-246; sprites lines 29-31; manifest lines 28-30 | **Partial.** Same-country path is exact and reachable; the specified “origin or host country” cross-border path is not implemented, and any unrelated forced return globally disqualifies it |
| `famine_migration_bread_across_the_front`, “Bread Across the Front”; registry lines 3865-3868; trigger lines 78-86 | Exact corridor preparation creates a route generation at `famine_migration_corridor_effects.txt:108-112`; acceptance calls `record_corridor_started` at lines 316-324; successful mission finalization calls `record_corridor_completed` at `famine_migration_decisions.txt:157-166`; exact attack callbacks reach `mark_corridor_attack_disqualified` at corridor effect lines 775-807 | Achievement recorders at `famine_migration_achievement_effects.txt:1060-1079` set only persistent country flags. No achievement generation/state/counterpart/cohort is stored and no producer clears any of the six corridor achievement flags | The requester country receives front/target/completion flags, but completion is not bound to the exact prepared corridor. A start from corridor A can combine with completion from corridor B; an attack or manufactured-crisis flag permanently blocks every later corridor | Complete; localisation lines 247-249; sprites lines 32-34; manifest lines 31-33 | **Partial and truth-unsafe.** A normal success can unlock, but stale cross-attempt combination and permanent unrelated disqualification violate exact generation semantics |
| `famine_migration_hungry_not_contagious`, exact title “They Were Hungry, Not Contagious”; registry lines 3870-3873; trigger lines 88-98 | Exact destination receipt is created after atomic transfer/finalization in `famine_migration_decisions.txt:2988-2999` through `famine_migration_decision_record_medical_reception_receipt` at owner effect lines 234-260; the controlled-medical decision starts observation at decision lines 2813-2845; a later exposed distribution can call the achievement recorder at lines 3006-3024; observation success calls `record_reception_safe` at lines 438-470; a later integration/dormant/gate resolver calls `record_durable_outcome` | The exact state receipt carries cohort/origin/host/generation/transaction. The achievement flags at effect lines 1081-1095 carry no cohort/generation; starting a recorded attempt clears safe/durable flags, failure clears all, but `famine_migration_medical_reception_active` is set once at decision line 2842 and is never cleared | Exact exposure is proven at arrival from an origin currently satisfying `black_plague_state_is_infected_or_worse` at owner effect lines 248-260. The exact identity is lost when country flags are written, so safe and durable facts can come from another cohort/episode | Complete; localisation lines 250-252; sprites lines 35-37; manifest lines 34-36 | **Partial; technically reachable only through an unintended multi-episode path.** The advertised single controlled-reception episode cannot unlock it |
| `famine_migration_a_place_at_the_table`, “A Place at the Table”; registry lines 3875-3878; trigger lines 100-123 | Exact successful transfer calls `record_arrival`, which adds each origin country once at achievement effect lines 362-378; exact local integration calls `record_integrated_receiving_state` at decision lines 3426-3441; state food pulses refresh only bound receiving states at achievement effect lines 1097-1220; visit history records A-B-A failure at `famine_migration_cohort_history_effects.txt:251-260` | Distinct origins and integration totals are campaign cumulative. Receiving states receive stable generations and de-duplicated state/cohort arrays; unsafe food stages remove a state and later recovery can re-add it. Cycle and coercion disqualifiers persist | Host-country ledger; origin country IDs come from successful transfer receipts; integrated destination state/cohort pairs and state food safety are explicit | Complete; localisation lines 253-255; sprites lines 38-40; manifest lines 37-39 | **Partial/conditionally reachable.** Positive identity and cycle detection are substantially complete; common eligibility and campaign-global coercion scope remain unresolved |
| `famine_migration_the_grain_stayed_home`, “The Grain Stayed Home”; registry lines 3880-3883; trigger lines 125-135 | Active extraction shock is recorded by the state food pulse at achievement effect lines 133-159; `fm_release_reserves` records suspension and alternative logistics at decision lines 966-984; other exact relief/reserve/route results can record same-state alternative logistics; stable state pulse records recovery at effect lines 1271-1283 | Each extraction activation receives a fresh generation; a new state/generation resets suspension, recovery, and alternative-logistics flags at effect lines 1230-1254; suspension, recovery, and logistics require the exact same state/generation | State `OWNER` country ledger with exact state ID and extraction generation; alternative logistics checks the same state. The strained-state requisition disqualifier is durable | Complete; localisation lines 256-258; sprites lines 41-43; manifest lines 40-42 | **Source-side complete except for common eligibility/runtime evidence.** This is the strongest of the eight |
| `famine_migration_the_country_did_not_empty`, “The Country Did Not Empty”; registry lines 3885-3888; trigger lines 137-158 | State pulse records qualifying core states, war/displacement, threatened amount, generation, recovery, and floor evidence at achievement effect lines 161-355; country cohort reconciliation supplies exact major-cohort resolution; `on_annex` records annexation at on-action lines 56-64; only the Fallout continuation wrapper records tag switches before `change_tag_from` at `fallout_consolidated_effects.txt:43159-43166` | Threat arrays reset when a closed/all-recovered window restarts at achievement effect lines 188-218; severe/recovered arrays are generation-bound. The floor is tested only within the stable recovery branch at lines 303-320, not during the active crisis | Country owner ledger and core-state IDs are explicit. Annexation is exact. Player tag switching is not centralized and several live continuations bypass the disqualifier. The terminal-only floor sample can miss an earlier breach followed by population recovery | Complete; localisation lines 259-261; sprites lines 44-46; manifest lines 43-45 | **Partial.** Positive threat/recovery identity is strong, but protected-floor exposure and tag continuity are incomplete |

## Explicit reachability proof: `They Were Hungry, Not Contagious`

The task referred to “The Hungry Were Not Contagious”; that string is not the implemented identity. The specification, registry ID, English localisation, DDS stems, and sprites agree on `famine_migration_hungry_not_contagious`, with exact title “They Were Hungry, Not Contagious” at `localisation/english/famine_migration_l_english.yml:250`.

The exact implemented exposure path is:

1. A successful exact distribution finalizes a positive debit and survivor credit, then calls `famine_migration_decision_record_medical_reception_receipt` at `common/decisions/famine_migration_decisions.txt:2988-2999`.
2. The receipt writer requires aligned cohort arrays, the exact persisted origin target, matching projection/history cohort ID and generation, and `black_plague_state_is_infected_or_worse` on that exact origin at `common/scripted_effects/famine_migration_decision_owner_effects.txt:234-260`. It stores cohort ID, origin state ID, host state ID, generation, transaction, and outbreak exposure class.
3. `famine_migration_decision_reception_exposure_receipt_is_valid` rechecks the receipt, aligned arrays, exact current hosted cohort, host state, generation, transaction, and exposure class at `common/scripted_triggers/famine_migration_decision_owner_triggers.txt:81-100`. This portion is exact and fail-closed.
4. The player can select `fm_controlled_medical_reception`, which requires the exact receipt and starts an observation mission at `common/decisions/famine_migration_decisions.txt:2774-2852`. That completion block sets `famine_migration_medical_reception_active` and `famine_migration_mission_reception_active`, but it does not call `famine_migration_achievement_record_medical_reception`.
5. The first observation can succeed and call `famine_migration_achievement_record_reception_safe` at decision lines 438-470, but that recorder writes the safe flags only if `famine_migration_achievement_controlled_medical_reception_used` already exists at `famine_migration_achievement_effects.txt:1222-1228`. It does not exist after step 4, so the first exact episode cannot produce the achievement's safe flags.
6. Mission completion clears only `famine_migration_mission_reception_active` at decision line 470. A full source census finds the durable `famine_migration_medical_reception_active` flag set at line 2842 and tested at line 3008, with no clear producer.
7. A later exact exposed distribution, while no observation is active, can enter decision lines 3006-3024 because `famine_migration_medical_reception_active` remains set. That later branch finally calls `famine_migration_achievement_record_medical_reception`, which clears prior safe/durable flags and sets `outbreak_exposed_cohort_received` plus `controlled_medical_reception_used` at achievement effect lines 1081-1087.
8. The second observation can now call `record_reception_safe` and set the no-outbreak/not-overloaded flags. Completion still does not set `medical_reception_durable_outcome`; a later generic durable-outcome call from integration, gate resolution/cleanup, or dormant resolution must run after all four flags exist at achievement effect lines 892-916.

Therefore the source path is technically reachable after the common eligibility caveat, but only through at least two exposed transfer/observation phases and a later durable resolver. The exact state receipt does not save the achievement because the country-level flags have no cohort ID or generation. Safe evidence from one cohort and a durable callback from another transaction can combine. An owner patch must arm the achievement recorder when the controlled-medical action starts the exact first receipt, persist the exact cohort/origin/host/generation on the achievement ledger, require that identity at safe and durable callbacks, and clear the policy/attempt state on every terminal path.

## Exact defects requiring owner action

### ACH-FM-01: all eight have unproved one-time eligibility ordering

Evidence: achievement definitions at `common/achievements/chaos_redux_achievements.txt:3850-3888`; runtime-seeded requirements at `common/scripted_triggers/famine_migration_achievement_triggers.txt:9-18`; sole normal seed at `common/scripted_effects/famine_migration_achievement_effects.txt:14-37`; startup caller at `common/on_actions/chaosx_famine_migration_on_actions.txt:11-24`; one-time `possible` semantics at `paradox_wiki/Achievement modding - Hearts of Iron 4 Wiki.md:34-37`.

Impact: if engine eligibility precedes `on_startup`, all eight are permanently not eligible. The current toolset cannot prove the ordering.

Owner action: move runtime baseline/flag conditions out of `possible` and keep them in `happened`, or obtain authoritative runtime proof before certification.

### ACH-FM-02: `Break the Blockade` start is mutually unsatisfiable

Evidence: `famine_migration_achievement_process_state` starts at effect line 107. The outer block at lines 251-355 requires `famine_migration_food_stage = stable`. Brace-depth inspection shows the intended blockade-start `if` at line 331 begins while that outer block remains open. Its limit at lines 333-338 simultaneously requires `famine_migration_food_stage_famine` or `_catastrophic`. The canonical transition helper clears every stage flag before setting exactly one current stage at `common/scripted_effects/chaosx_famine_migration_effects.txt:4255-4279, 4328-4340`.

Impact: the only writer of `famine_migration_achievement_blockade_famine_proven` at effect line 352 cannot run under normal stage processing, so the completion predicate's first required flag is unreachable.

Owner action: close the stable-recovery branch before the floor/cleanup/blockade-start blocks and re-audit the intended order. Bind the result to the eligible owner/controller contract.

### ACH-FM-03: crisis/cohort disqualifiers are not scoped to the achievement identity

Evidence: `famine_migration_achievement_record_forced_return` at effect lines 952-955 sets both the generic forced-return and blockade-forced-removal flags without a state, cohort, or generation check. `record_violent_pushback` at lines 961-963 is equally global. Exact custody recorders at lines 965-1039 prove a real hosted cohort action but do not test membership in the active/terminal gate cohort arrays or the medical attempt identity. The gate, roads, hungry, place, and blockade predicates consume these persistent country flags at trigger lines 33-37, 55-58, 74-75, 95-97, and 119-122.

Impact: an unrelated forced return can permanently disqualify five achievements, and custody of an unrelated cohort can disqualify gate/medical outcomes whose specification names the protected or exposed cohort.

Owner action: persist disqualifier state/cohort/generation and compare it to the exact achievement attempt, retaining campaign-global behavior only where the accepted design explicitly calls for campaign-wide ethics.

### ACH-FM-04: `Bread Across the Front` has no achievement attempt identity or reset

Evidence: `record_corridor_started` and `record_corridor_completed` at `famine_migration_achievement_effects.txt:1060-1079` set six country flags and no identity variables. A full setter/clearer census finds one setter and zero clearers for `corridor_front_proven`, `corridor_target_proven`, `corridor_held_full_term`, `corridor_resolved_crisis`, `corridor_attacked`, and `corridor_manufactured_crisis`. The real corridor generation at `famine_migration_corridor_effects.txt:108-112` is not copied into the achievement ledger or checked by the trigger at `famine_migration_achievement_triggers.txt:78-86`.

Impact: different corridors can combine into a false unlock, while one old attack/manufactured-crisis episode makes every later legitimate attempt permanently impossible.

Owner action: bind start, completion, attack, and manufacture proof to one exact route generation, origin/front/counterpart, reset a new attempt atomically, and require that identity in the trigger.

### ACH-FM-05: controlled medical reception does not arm the first exact attempt

Evidence: the explicit reachability proof above. The sole achievement recorder call is in the later distribution branch at `famine_migration_decisions.txt:3006-3024`, while `fm_controlled_medical_reception` at lines 2774-2852 does not call it. Achievement safe/durable flags have no cohort/generation fields.

Impact: advertised single-episode completion is unreachable, a two-episode cross-cohort combination is possible, and `famine_migration_medical_reception_active` is never cleared.

Owner action: bind and arm the exact first receipt during the controlled-medical decision, carry its identity through safe/durable callbacks, and clean it on success, failure, cancellation, timeout, control change, annexation, and invalid-host cleanup.

### ACH-FM-06: `Roads Home` does not implement the specified origin-or-host ownership

Evidence: the registered-country projection explicitly matches only `global.famine_migration_cohort_owners` to the current country at `common/scripted_effects/chaosx_famine_migration_effects.txt:3274-3322`. Cohort creation writes the origin state's `OWNER` into that array at `chaosx_famine_migration_effects.txt:95-102`. The voluntary-return achievement recorder runs on the country executing the hosted return decision at `common/decisions/famine_migration_decisions.txt:3761-3772`.

Impact: a foreign host lacks the major-cohort maturity ledger, while a foreign origin normally lacks the host-side return action. The exact path works for internal/same-country displacement, not the specification's full origin-or-host route.

Owner action: select and document the earning actor, persist both origin-country and host-country identity, and route maturity/return evidence consistently to that actor without duplicating population or cohort history.

### ACH-FM-07: `The Country Did Not Empty` samples the protected floor only at recovery

Evidence: the core-floor block at `famine_migration_achievement_effects.txt:303-320` is nested inside the stable recovery block opened at line 251. It compares population only when the state has returned to stable. State population can change through movement after an earlier breach.

Impact: a core state can fall below the protected floor during the crisis and later rise before stable recovery without setting `famine_migration_achievement_core_floor_breached`, contrary to specification line 245 and tooltip line 261.

Owner action: evaluate the exact bound state's protected floor during every active severe-generation pulse before terminal cleanup, preserving the durable breach flag.

### ACH-FM-08: player tag-switch disqualification is not centralized

Evidence: the only achievement recorder call before `change_tag_from` is the Fallout wrapper at `common/scripted_effects/fallout_consolidated_effects.txt:43159-43166`. Live player continuations without the recorder exist at `events/014_cannibalism.txt:234-246`, `events/016_brilliant_scientist_containment_events.txt:103-123`, `events/018_random_resource.txt:2777-2794`, `common/scripted_effects/006_independence_wave_join_effects.txt:379-403`, and human-continuation branches at `common/scripted_effects/014_cannibalism_effects.txt:12465-12473, 12646-12653, 18866-18875`. The CXT `change_tag_from` at `chaosx_test_country_effects.txt:290-302` is excluded by the natural-campaign rule and is not a legitimate unlock path.

Impact: the player can continue as another country without setting `famine_migration_achievement_tag_switch_disqualified`, so `The Country Did Not Empty` can survive prohibited continuity changes.

Owner action: centralize player continuation through an exact pre-switch recorder that marks both prior and target ledgers, or patch every authoritative player-switch owner and audit the full `change_tag_from` census.

## Asset and localisation completion

All eight presentation identities are complete.

- Each achievement has exactly one registry definition and exactly one English `_NAME`, `_DESC`, and `_tooltip` key in `localisation/english/famine_migration_l_english.yml:238-261`. The file has a UTF-8 BOM.
- `interface/famine_and_migration_system.gfx:23-46` defines exactly one normal, one grey, and one not-eligible sprite for each ID, each pointing to the matching final DDS.
- All 24 final files exist under `gfx/achievements/`, are 64x64 legacy uncompressed BGRA8 one-level DDS files, and pass the official `process_achievement_icons.py --audit` recomposition contract for their exact source layers and canonical templates.
- A SHA-256 census across all 1,005 DDS files in `gfx/achievements/` found zero duplicate hash groups. The eight source PNG masters and all 24 final famine/migration DDS states are mutually distinct.
- Visual inspection of the eight source masters found eight separate achievement concepts matching the accepted directions, with no visible placeholder label, watermark, copied vanilla icon, or unrelated fallback. `docs/plans/famine_and_migration_system_plans/subagent_handoffs/final_asset_audit.md:75-98, 142-156` and `docs/assets/famine_and_migration_system/gfx_handoff.md:30-32` record the canonical template and provenance details.
- The processed achievement PNGs are transparent motif layers, while the canonical achievement template produces nearly opaque final DDS underlays. This is documented at `final_asset_audit.md:75-77` and is not an alpha-loss defect.

Normal-state SHA-256 identities:

| Achievement | Final normal DDS SHA-256 |
| --- | --- |
| `famine_migration_break_the_blockade` | `A76649C81A4A62F98202E1507A08575B7BF1599CE83DBE94B337979667BAE510` |
| `famine_migration_no_one_left_at_the_gate` | `9A52FD405029C7CA2EDE7C6B248E6BA6E85F78D144CF125F7089F396D9EC93C9` |
| `famine_migration_roads_home` | `BBE1D35E58B4C9AE6724198C0E10392B3272CCDC4A2F315E56F3E7A1C1AC71BB` |
| `famine_migration_bread_across_the_front` | `4FEF1411D75EFAEE8D11CBDCBACA3864EF891325ADE90ADEFD0A455E37C52690` |
| `famine_migration_hungry_not_contagious` | `24942868B4C8E1AB1326BBD3498FF4E073B7CF9BCD57ED4C9D1F1404D15674BE` |
| `famine_migration_a_place_at_the_table` | `2CF0867B72ABD75CBF993743FBAD6787D23CA3EAFDE5F6F827437545428C69B0` |
| `famine_migration_the_grain_stayed_home` | `4F8E9B14842FAEB5FCED0E8F503C8984F28B95516C37B0B78295D7E88CB92C98` |
| `famine_migration_the_country_did_not_empty` | `04E93896342C0DEEFBF5ED2B1C292A24345F044DD5F62E301C19FCA49AC6CAF8` |

No asset or localisation owner patch is required for these eight identities.

## MCP and task-specific validation evidence

There is no direct event chain in the shared achievement system. The only event chains in this audit are the three player-only tag-switch continuations whose missing recorder affects `The Country Did Not Empty`.

Fresh `hoi4.event_inspect` trace and `hoi4.event_render` reachability calls were run for all three. Every call used event graph revision `59143acd4a234aef98ca0b6cfbb7b07211d4aa80f99536718b30e126b1deb6f9` and graph hash `e403ad99017a9482e4ca09f8ce0bde4146fd96bd0576d31f6bd9951d13d55660`.

| Event | Inspect | Render | Limit |
| --- | --- | --- | --- |
| `chaosx.nr14.30` | `EVENT_INSPECTED_PARTIAL`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3cb3de44ccea005f86c138af0279d317e73f8f278c48b30784ef4e1683171ebd/713f46a560c90797d763597a13967f42418ba7e74feba5819b4107eebe1ccc0f/event-trace-59143acd4a23.json` | `EVENT_RENDERED_PARTIAL`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30ab8d4b818fec4f92910580256bec9f6d56e06dd62e5f384365f8e30ac0aa15/dd6bd990ec23930b9d13860c48b269ad7b4eafb796a7b7a6d82bcc127b2f54ec/event-reachability-59143acd4a23.json` | 6 selected nodes, 41,238 omitted, zero branch renders |
| `chaosx.nr16.31` | `EVENT_INSPECTED_PARTIAL`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c2e53c7fb67703f1881dce679542730e8b0a05ad9f30a02079ba78c7f636def/7e6b1edc9d60b5156d81e1c07856681ca02ff237224a436af3f8199545275b9c/event-trace-59143acd4a23.json` | `EVENT_RENDERED_PARTIAL`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c201c358f04f554ca18e319d5b53b92ab1488c0edd5fd488b53ede1aae96673/a5860cce6d591a1d828a930f6c5c5925622a6e56ed711e88eb03e6c1c98ccbe3/event-reachability-59143acd4a23.json` | 5 selected nodes, 41,239 omitted, zero branch renders |
| `chaosx.nr18.80` | `EVENT_INSPECTED_PARTIAL`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4ab11a73d4679dfff98a3f74ac829930be3eb573ab68563d08a13cd338214a5/b071424368431ff2b08724bb7a585da1a3ecbbc7a3804d356561c3c950c19f22/event-trace-59143acd4a23.json` | `EVENT_RENDERED_PARTIAL`; `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b4432788919988aa5bba193be3c3531ff06374f39a3705e1d8394341d3c3b57/e14656fe541b857f72334bda3aa895dbd190091a9f7572f7ed944f7966b14989/event-reachability-59143acd4a23.json` | 7 selected nodes, 41,237 omitted, zero branch renders |

The shared projection contained 9,513 events, 8,301 unresolved nodes, 24,105 diagnostics, and 14 blocking diagnostics. The results are structural navigation evidence only. A required `hoi4.event_compare` probe returned exact blocker `EVENT_COMPARISON_BASELINE_REQUIRED: Provide a cached revision, graph artifact, or proposed source overlay`; no comparison result is claimed.

The three event option sets contain `ai_chance` surfaces, so the weighted pass was routed to `chaosx_ai_probability_auditor` as required. Probability evidence is recorded in the next subsection.

### Probability audit of tag-switch event options

The required read-only `chaosx_ai_probability_auditor` pass found that all three uncovered tag-changing options are player-only (`is_ai = no`). Their `ai_chance` values control AI auto-selection; they do not make the human option unavailable. Adjusting these weights therefore cannot close the achievement identity/disqualifier gap.

| Event option set | Probability result | Achievement-relevant conclusion |
| --- | --- | --- |
| `chaosx.nr14.30.a/.b` | `PROBABILITY_ANALYZED`; exact conditional pool; scenario hash `d391d1a92cdfaf9aa5ee9c96dc1d4ea13f0bf22d9a2333b145b0ae43ecb44c8e` | In the player scenario, `.a` has raw weight 100/probability 1 and `.b` has raw weight 0/probability 0, but `.b` remains player-eligible. For AI, `.b` is ineligible. The zero AI chance is not an achievement guard. |
| `chaosx.nr16.31.a/.b` | `PROBABILITY_ANALYZED_PARTIAL`; scenario hash `827032a4ce903a46599f128a77c5c5af8c1e1e48e1c9c89cf7e1078afa253d7e` | `.31.a` has raw weight 12/probability 1 in supplied scenarios. `.31.b` has raw weight 0 and is AI-blocked by `is_ai = no`; human eligibility remains structurally available but the MCP fixture could not resolve the typed `KRG` state scope. |
| `chaosx.nr18.80.a/.b/.c` | `PROBABILITY_ANALYZED_PARTIAL`; scenario hash `7c87dcd0db650e87fab33e1260f15a4863312e83f791f34601e4b354d7ad19fa` | `.80.c` is player-only and raw weight 0, so AI cannot select it. Human eligibility remains structurally available; the MCP adapter did not resolve the direct flag representation or typed `DHO` scope. `.80.a/.b` base weights are 105/110, but unresolved war/major modifiers prevent a valid normalized-probability claim. |

The Event 018 two-point numeric sweep returned `PROBABILITY_ANALYZED_PARTIAL` with five unresolved inputs and proved no rank reversal or probability sensitivity. Boolean `is_ai` sweeps were unavailable (`INTERNAL_ERROR` for Events 014/016; `PROBABILITY_SWEEP_RANGE_REQUIRED` for Event 018). `probability_compare` was not applicable because no before/after or alternative implementation was supplied. Simulation and sequence analysis were not claimed because no uncertain-input distribution or complete pool-cadence manifest exists.

The probability source revision was `c9092c1604f1d550cfacbeeb6165afef1a61a6bfe7690df508edb90677dc3d53`; source hashes were `e965dd5d8ff4aee1966343cc6d271ec59c5691569bda80822a2c7c517c7f66e0` (Event 014), `4b3102f2084048b511f70bf3a2b1af786a8fff22168a4c81839125a1effe5e66` (Event 016), and `da108b9aac1676779c25315f45220eccb7f0b0a06fe62940867a8fd58f835187` (Event 018). Machine-readable artifacts:

- Event 014: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fefc0e8fa3a77c9f8c0b5e03105d6ce924a0693d0a93458a7b3e9edbaca4938/a3e859928be44510d6c9bac52f87939b7763c3a1a914bf1556a84ad3219707b0/probability-d3c5dc098f599d9cacf60288.json`.
- Event 016: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5de54640d6e30451a85ea86b34dffb668fe126058ad68fc182a916ad2df9538b/bcab636e95c6517c037ec9c6536d39bc53f33565caea985957785d01ef41bb6f/probability-b642366c6ba08bb09de641f5.json`.
- Event 018: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c03a9523263b456600f7dc799555a39fea12acc06b341e53309f8b94451d9a48/e9742d6a5fd13386748c6e200e6888db20c39965f1670553e9a73d2fc38953a8/probability-7549106c4c40e40cd31c124c.json`.
- Event 018 sweep: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ae05f83a1f176f74437398b605ce97a5287a2f14d713acfa7191736b9a62dc2/e3eec7640eff334b816066e3180979f5ebccb7dda761d7ee1ba94207c5286a0e/probability-ee29b0f71fe683a90e224c83.json`.

Other meaningful validation:

- Brace-depth tracing proved that the blockade start, protected-floor sample, and related blocks begin at depth two inside the stable recovery branch even though the file is globally brace-balanced.
- A producer census found the sole normal baseline writer/caller pair, the sole medical achievement recorder call, no clearer for `famine_migration_medical_reception_active`, no clearer for any Bread corridor achievement flag, one annexation producer, and only one wrapped `change_tag_from` owner.
- The official achievement asset processor returned `AUDIT OK` for all eight triplets, verifying strict 64x64 BGRA output and source-layer equality.
- Definition/localisation/sprite/DDS census returned one definition, one name, one description, one tooltip, one normal sprite, one grey sprite, one not-eligible sprite, and three existing DDS files for each ID.
- No HOI4 runtime, save/reload, or actual unlock test was performed because repository policy assigns live testing to the user. No source-only result is represented as runtime evidence.
- The installed HOI4 MCP has no achievement-specific inspection/rendering route. Event tools cannot prove custom-achievement `possible` ordering or continuing `happened` evaluation.

## Accepted-plan disposition

| Plan or handoff | Final disposition from this audit |
| --- | --- |
| `subagent_handoffs/achievement_identity_generation_closure.md` | **Partially accepted, not completion proof.** Gate, blockade relief/recovery, Roads, receiving-state, extraction, and threat identity structures are present. Its claim that blockade start is bound at catastrophic start is refuted by the current brace nesting, and its protected-floor account covers only terminal recovery sampling. It intentionally did not close Bread or Hungry. |
| `subagent_handoffs/achievement_hook_closure.md` | **Superseded in part.** Its custody, corridor-attack, annexation, and visit-cycle blockers have later exact source owners. Its statement that only the supported player tag-switch path is covered remains incomplete because the repository has other human continuation paths. |
| `subagent_handoffs/camp_generic_custody_owner_patch.md` | **Accepted as an exact real custody transaction.** It closes the prior “no producer” gap, but the achievement consumer still treats any exact cohort custody as a global disqualifier rather than matching the protected gate/medical identity. |
| `subagent_handoffs/corridor_attack_owner_closure.md` | **Accepted for its bounded project owners.** Native invasion/paradrop/nuclear callbacks and the bounded owner resolvers submit exact state/attacker receipts. Bread still lacks achievement attempt generation/reset. Ordinary unsupported combat surfaces remain explicit limits rather than inferred proof. |
| `subagent_handoffs/final_asset_audit.md`, `icon_artist.md`, and the asset disposition in `handoff_dispositions.md` | **Accepted.** All eight distinct achievement triplets, provenance, canonical templates, sprites, and English consumers pass the final static audit. |
| `completion_report.md` and `subagent_handoffs/completion_final_audit.md` | **Stale for current achievement ownership.** They predate later custody/attack/annex/cycle closures and the exact medical exposure receipt, but their incomplete overall verdict remains correct. The older title “The Hungry Were Not Contagious” must not replace the implemented “They Were Hungry, Not Contagious.” |
| `source_of_truth_map.md` and `resume_packet.md` | **Still correctly route achievements to final audit.** Their previous “awaits achievement-audit review” state should be promoted to the defects and conditional statuses in this handoff after owner patches land. |

No accepted achievement plan can be promoted as complete while ACH-FM-01 through ACH-FM-08 remain unresolved.

## Shared-system boundary and non-applicable surfaces

This is a shared famine and migration system, not a named event. It requires no event ID, event-pool registration, event pacing weight, event-log row, event-details row, evolution row, or replacement for retired Event 149. The three inspected events are relevant only because they expose unrecorded player tag switches.

No named event introduces a dedicated scripted GUI here, so `chaosx_event_ui_worker` and event-owned GUI proof are not applicable. No focus tree, country package, formable, super-event, portrait, animation, 3D model, custom unit sound, unit counter, or achievement-specific GUI is part of these eight achievement definitions.

The CXT fixture is registered idempotently but is a special Chaos country excluded by `famine_migration_achievement_natural_campaign_is_valid`; it is not a legitimate achievement reachability harness and should not be used as unlock proof.

## Required owner patch order

1. Make the common `possible` contract independent of runtime-seeded flags or produce authoritative engine-ordering proof.
2. Repair `famine_migration_achievement_process_state` block ownership so blockade start is reachable and protected-floor sampling runs during the active exact generation.
3. Add exact per-attempt generation/state/country/cohort binding and reset for Bread and Hungry, including every terminal cleanup path.
4. Scope forced-return, pushback, custody, and blockade disqualifiers to the exact relevant state/cohort/generation unless the design is explicitly changed to campaign-global and localisation/specs are updated together.
5. Resolve Roads Home's origin/host earning actor and route maturity plus return evidence to that same identity.
6. Centralize or exhaustively patch player `change_tag_from` owners, then rerun the same callsite census and the three event inspect/render routes.
7. After patches, run a new final read-only achievement audit, preserve an event graph baseline for a real `hoi4.event_compare`, repeat strict asset/consumer census only if presentation files changed, and leave runtime unlock/save-reload confirmation to the user.

## Completion status by surface

| Surface | Status |
| --- | --- |
| Eight registry definitions and root identity | Complete |
| English names, descriptions, tooltips, and exact title identity | Complete |
| Normal/grey/not-eligible sprite and DDS consumers | Complete |
| Asset originality, provenance, strict format, and duplicate audit | Complete |
| Common natural-campaign eligibility | Blocked by unproved one-time startup ordering |
| Break the Blockade gameplay path | Blocked/unreachable |
| No One Left at the Gate gameplay path | Partial/conditionally reachable |
| Roads Home gameplay path | Partial; internal/same-country path only |
| Bread Across the Front gameplay path | Partial and generation-unsafe |
| They Were Hungry, Not Contagious gameplay path | Partial; unintended multi-episode path only |
| A Place at the Table gameplay path | Partial/conditionally reachable |
| The Grain Stayed Home gameplay path | Source-side complete except common eligibility/runtime proof |
| The Country Did Not Empty gameplay path | Partial; floor exposure and tag continuity incomplete |
| CXT registration/test relevance | Complete exclusion; not an unlock harness |
| Event MCP evidence for tag-switch continuations | Partial structural evidence; comparison baseline blocked |
| Achievement runtime, save/reload, and actual unlock proof | Not performed and not available to this agent |

Overall status: **incomplete; owner patch required**.
