# Event 019 Decision/Mission Specialist Audit — 2026-07-15

## Mandate and verdict

This is the required read-only `chaosx_decision_mission_auditor` pass over the live Event 019, Infantry Spawn, worktree after the improvement planner closed without an addendum. No gameplay, localisation, asset, specification, workbook, registry, or event source was edited by this audit.

Live specialist verdict: **parent remediation accepted for the audited decision/mission surface: P0: 0, P1: 0, P2: 0**. Event 019 is still not globally completion-ready because the two explicit owner-approval blockers remain deliberately fail-closed and unchanged.

| Class | Count | Verdict |
| --- | ---: | --- |
| P0 | 0 | No immediate corrupting or unbounded player exploit was found in the decision/mission surface. |
| P1 | 0 | DMM-019-P1-001 is resolved by the frozen exact-proof set and annexer-owned retry queue verified in the parent-resolution re-audit below. |
| P2 | 0 | DMM-019-P2-001 is resolved: all sixteen payable claimant comparisons accept equality and debit the matching exact constants once. |
| Explicit owner-approval blockers | 2 | Exact recorded-formation transfer and four exact same-battle achievements remain deliberately fail-closed. No fallback was used. |

The implemented decision/mission inventory is exact: **63 decisions plus 13 missions across 3 dynamic categories**. The counts, shared GUI paths, ordinary request transactions, selected-lot proof, prototype route, derivative actions, scenario deferral, AI coverage, localisation, and icon wiring otherwise match the reviewed Event 019 design.

## Required reference gate

The required references were consulted before the live Event 019 source:

- Offline Paradox wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI modding, Achievement modding, Division modding, Equipment modding, and Unit modding.
- Installed vanilla documentation: `common/decisions/_documentation.md`, `common/scripted_guis/_documentation.md`, `common/on_actions/_documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, and the relevant units/equipment documentation.
- Vanilla precedents included `common/decisions/AST.txt` and `common/decisions/categories/AST_decision_categories.txt`. Vanilla confirms that effect-activated missions may use `allowed = { always = no }` and `activation = { always = no }` and still be started by `activate_mission`.
- Repo guidance used in full: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`.

No web copy of the Paradox wiki was used.

## Exact inventory

### Categories

1. `infantry_spawn_formation_management_category`
2. `infantry_spawn_claimant_category`
3. `infantry_spawn_derivative_operations_category`

All three use load-safe `allowed = { always = yes }` and dynamic `visible` gates. The ordinary and claimant categories require `infantry_spawn_country_is_active`; all three require `infantry_spawn_scenario_transaction_is_idle`. The derivative category is restricted by `is_infantry_spawn_derivative_country` and active derivative phase flags. Evidence: `common/decisions/categories/019_infantry_spawn_decision_categories.txt:11-36`, `common/decisions/categories/019_infantry_spawn_claimant_categories.txt:10-19`, and `common/decisions/categories/019_infantry_spawn_derivative_decision_categories.txt:10-24`.

### Decisions: 63

`common/decisions/019_infantry_spawn_decisions.txt` — **35 decisions**:

1. `infantry_spawn_open_muster_board`
2. `infantry_spawn_select_next_ordinary_lot`
3. `infantry_spawn_select_next_unaccounted_lot`
4. `infantry_spawn_settle_selected_lot_obligations`
5. `infantry_spawn_audit_selected_lot`
6. `infantry_spawn_assign_territorial_roles`
7. `infantry_spawn_open_standardization_cycle`
8. `infantry_spawn_supervised_demobilization`
9. `infantry_spawn_emergency_field_integration`
10. `infantry_spawn_establish_muster_districts`
11. `infantry_spawn_appoint_integration_staff`
12. `infantry_spawn_issue_common_tables`
13. `infantry_spawn_preserve_specialist_companies`
14. `infantry_spawn_recognize_emergency_reserve`
15. `infantry_spawn_survey_formation_lots`
16. `infantry_spawn_open_training_cycle`
17. `infantry_spawn_reserve_rail_corridors`
18. `infantry_spawn_preserve_prototype_formation`
19. `infantry_spawn_cannibalize_advanced_lot`
20. `infantry_spawn_request_field_reinforcement`
21. `infantry_spawn_request_mobile_reserve`
22. `infantry_spawn_request_territorial_defenders`
23. `infantry_spawn_request_specialist_firepower`
24. `infantry_spawn_request_numbers`
25. `infantry_spawn_request_discipline`
26. `infantry_spawn_request_firepower`
27. `infantry_spawn_request_mobility`
28. `infantry_spawn_request_anything`
29. `infantry_spawn_request_selected_anomalous_family`
30. `infantry_spawn_open_selected_family_cantonment_decision`
31. `infantry_spawn_appoint_selected_family_liaison_decision`
32. `infantry_spawn_restrict_selected_family_deployment_decision`
33. `infantry_spawn_sustain_selected_family_decision`
34. `infantry_spawn_seal_selected_family_breach_decision`
35. `infantry_spawn_disperse_selected_anomalous_lot_decision`

`common/decisions/019_infantry_spawn_claimant_decisions.txt` — **6 decisions**:

1. `infantry_spawn_recognize_claimant`
2. `infantry_spawn_accept_claimant_demand`
3. `infantry_spawn_refuse_claimant_demand`
4. `infantry_spawn_counter_command_claimant`
5. `infantry_spawn_discredit_claimant`
6. `infantry_spawn_arrest_claimant`

`common/decisions/019_infantry_spawn_derivative_decisions.txt` — **22 decisions**:

1. `infantry_spawn_derivative_rotate_collective_commands_decision`
2. `infantry_spawn_derivative_centralize_collective_muster_decision`
3. `infantry_spawn_derivative_ratify_species_compacts_decision`
4. `infantry_spawn_derivative_proclaim_family_primacy_decision`
5. `infantry_spawn_derivative_secure_muster_depot_decision`
6. `infantry_spawn_derivative_authorize_base_zombie_training_decision`
7. `infantry_spawn_derivative_rally_zombie_band_decision`
8. `infantry_spawn_derivative_manifest_ghost_host_decision`
9. `infantry_spawn_derivative_bind_golem_host_decision`
10. `infantry_spawn_derivative_pay_family_sustainment_decision`
11. `infantry_spawn_derivative_establish_sustainment_site_decision`
12. `infantry_spawn_derivative_offer_zombie_containment_decision`
13. `infantry_spawn_derivative_offer_ghost_border_recognition_decision`
14. `infantry_spawn_derivative_offer_golem_material_agreement_decision`
15. `infantry_spawn_derivative_integrate_zombie_muster_district_decision`
16. `infantry_spawn_derivative_recognize_ghost_anchor_district_decision`
17. `infantry_spawn_derivative_bind_golem_foundry_district_decision`
18. `infantry_spawn_derivative_suppress_fragmentation_decision`
19. `infantry_spawn_derivative_break_former_parent_command_net_decision`
20. `infantry_spawn_derivative_demand_local_submission_decision`
21. `infantry_spawn_derivative_preserve_claimant_decision`
22. `infantry_spawn_derivative_replace_claimant_decision`

### Missions: 13

Ordinary management — **10 missions**:

1. `infantry_spawn_formation_roll_call_mission`
2. `infantry_spawn_standardization_cycle_mission`
3. `infantry_spawn_supervised_demobilization_mission`
4. `infantry_spawn_training_cycle_mission`
5. `infantry_spawn_muster_districts_mission`
6. `infantry_spawn_officer_search_mission`
7. `infantry_spawn_specialist_preservation_mission`
8. `infantry_spawn_prototype_maintenance_trial_mission`
9. `infantry_spawn_rail_corridor_mission`
10. `infantry_spawn_request_cooldown_mission`

Derivative — **3 missions**:

1. `infantry_spawn_derivative_integrate_conquered_district_mission`
2. `infantry_spawn_derivative_submission_warning_mission`
3. `infantry_spawn_derivative_survive_former_parent_front`

## Findings

### DMM-019-P1-001 — annex cleanup marks an invariant failure complete and permanently suppresses retry

Severity: **P1**. Status: **resolved in the live parent-resolution re-audit; historical snapshot evidence retained below**.

`infantry_spawn_cleanup_annexed_ordinary_country` enters only for an ordinary Event 019 participant without `infantry_spawn_country_cleanup_complete` (`common/scripted_effects/019_infantry_spawn_management_effects.txt:7627-7633`). It finalizes only after proving the exact unit and template sets absent (`:7637-7649`). Each failure branch sets both `infantry_spawn_annex_cleanup_invariant_failure` and `infantry_spawn_country_cleanup_complete` (`:7651-7663`).

That second flag is terminal:

- The same cleanup effect refuses a later entry once `infantry_spawn_country_cleanup_complete` exists (`:7632`).
- The only live caller is the one-shot `on_annex` path (`common/on_actions/019_infantry_spawn_achievement_on_actions.txt:30-53`).
- `infantry_spawn_country_is_active` also rejects the cleanup-complete state (`common/scripted_triggers/019_infantry_spawn_triggers.txt:34-39`), hiding normal management instead of repairing it.

The failure branches do not call `infantry_spawn_finalize_annexed_ordinary_country_cleanup`. The skipped finalizer is the only path that clears state markers, claimant data, runtime ideas and missions, achievement attempts, exact profile totals, private ledgers, auxiliary arrays, scenario state, runtime flags and variables, `infantry_spawn_participant`, and the cleanup lock (`common/scripted_effects/019_infantry_spawn_management_effects.txt:7608-7625`). The skipped runtime remover explicitly removes all ten ordinary missions and the Event 019 management/claimant ideas (`:7313-7340`).

Consequence: an exact deletion failure is correctly detected, but the country is permanently declared clean without being clean. Active missions, timed ideas, participant/ledger data, scenario residue, and locks can survive annexation. If the country scope is later restored or released, those effects can remain while both cleanup and ordinary management are suppressed. This is fail-closed for further mutation, but it is not a recoverable or complete cleanup state.

#### Assessment of the proposed annexer-owned retry queue

The proposed exact retry queue resolves this P1 if it observes all of these constraints:

1. Failure branches must keep `infantry_spawn_annex_cleanup_invariant_failure` and the evidence-bearing participant/ledger state, but must **not** set `infantry_spawn_country_cleanup_complete`.
2. In `on_annex`, store the exact `FROM` country scope in a ROOT/annexer-local persistent scope array, deduplicated with `is_in_array`. A regular event target is insufficient because it does not persist into a delayed event.
3. Use one annexer-local scheduled flag so simultaneous failures cannot create duplicate event chains. Use a centralized delay constant.
4. The hidden annexer event should process only one exact entry per firing. A safe deterministic pattern is `for_each_scope_loop` with `break` to save the first entry as a temporary event target, then retry and modify the queue **after** the loop. The offline wiki explicitly warns that array entries cannot be removed while `for_each_scope_loop` is running.
5. Remove the queued country only after that exact target positively has `infantry_spawn_country_cleanup_complete`. If the queue still contains entries, schedule the next retry.
6. Do not classify `exists = no`, ownership loss, no current states, an invariant-failure flag, or a derivative mismatch as “stale.” Those are not proofs that Event 019 residue is absent. A non-complete entry may be removed only after an explicit no-residue contract proves no Event 019 units/templates, missions, ideas, participant state, ledgers, scenario state, or runtime data remain.
7. Retry the cleanup effect directly. Normal active-country triggers deliberately reject invariant-failure countries and must not gate repair.
8. Preserve queue ownership if the annexer is itself annexed before its queue drains; migrate its pending exact country scopes to the next annexer or an equivalently persistent exact queue owner.

This is an exact repair path, not a gameplay fallback. It preserves the invariant evidence and never substitutes blanket deletion, whole-army transfer, or guessed tag ownership.

### DMM-019-P2-001 — exact claimant costs are treated as unaffordable

Severity: **P2**. Status: **resolved in the live parent-resolution re-audit; historical snapshot evidence retained below**.

There are **16 strict `>` checks across 11 payable claimant contracts**. The corresponding effects revalidate and debit the exact constants, so a country holding exactly the displayed cost is falsely rejected. The decision, scripted GUI, and AI all share these triggers, giving consistent but incorrect behavior.

| Decision contract | Payable branch | Strict comparisons | Source |
| --- | --- | ---: | --- |
| `infantry_spawn_accept_claimant_demand` | equipment share | infantry equipment and support equipment, 2 | `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:219-227` |
| `infantry_spawn_accept_claimant_demand` | autonomous district | command power, 1 | `:228-235` |
| `infantry_spawn_accept_claimant_demand` | another formation | army experience, 1 | `:236-245` |
| `infantry_spawn_accept_claimant_demand` | political seat | political power, 1 | `:246-253` |
| `infantry_spawn_accept_claimant_demand` | emergency powers | stability, 1 | `:254-262` |
| `infantry_spawn_accept_claimant_demand` | subordinate command | army experience and command power, 2 | `:263-271` |
| `infantry_spawn_accept_claimant_demand` | parallel command | political power and command power, 2 | `:272-280` |
| `infantry_spawn_recognize_claimant` | recognition | political power, 1 | `:284-295` |
| `infantry_spawn_counter_command_claimant` | counter-command | army experience and command power, 2 | `:297-302` |
| `infantry_spawn_discredit_claimant` | discredit | political power, 1 | `:304-308` |
| `infantry_spawn_arrest_claimant` | arrest | command power and stability, 2 | `:310-316` |

Demand acceptance contributes 10 comparisons; the four response actions contribute 6. Total: **16**.

Recommended correction: use explicit `check_variable` contracts with `compare = greater_than_or_equals` for political power, command power, stability, army experience, and `num_equipment@...` stockpiles. Do not use unsupported `>=`. This changes only the exact-equality boundary and does not weaken cost payment, target validation, or AI parity.

## Clean surface trace

### Selected-lot proof and Muster Board parity

- Selected-lot gates validate the row index, aligned ledgers, exact nonterminal lot status, scenario idleness, and transaction locks before action.
- The ordinary decisions and Muster Board call the same action wrappers. Examples include `infantry_spawn_execute_selected_lot_audit_action`, `infantry_spawn_execute_selected_lot_territorial_action`, `infantry_spawn_execute_selected_lot_training_action`, `infantry_spawn_execute_selected_lot_standardization_action`, `infantry_spawn_execute_selected_lot_specialist_preservation_action`, `infantry_spawn_execute_selected_lot_demobilization_action`, `infantry_spawn_execute_selected_lot_emergency_integration_action`, `infantry_spawn_execute_selected_prototype_preservation_action`, and `infantry_spawn_execute_selected_prototype_cannibalization_action`. Evidence: `common/decisions/019_infantry_spawn_decisions.txt:92-179,287-289,353-355,412-449` and `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:26-27,55-63,164-174`.
- All six claimant buttons call the same response effects used by their decisions, and their enabled gates use the same `infantry_spawn_can_*` triggers (`common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:71-92,182-190`; `common/decisions/019_infantry_spawn_claimant_decisions.txt:9-160`).
- All seven anomalous-family GUI buttons call the same family effects used by the decisions. GUI AI is disabled; ordinary decision weights or the dedicated family dispatcher use the shared gates/effects.

### Prototype-management route

- `infantry_spawn_preserve_prototype_formation` and `infantry_spawn_cannibalize_advanced_lot` are distinct decision routes, mirrored by two Muster Board buttons and AI-selectable through the same shared wrappers.
- Preservation captures the immutable lot UID and exact expected live unit set, validates the finite prototype cohort, charges the centralized resources, clamps a dynamic mission duration, and starts `infantry_spawn_prototype_maintenance_trial_mission`.
- Completion re-proves the exact cohort before applying full, partial, or failed results, keeps research insight finite, clears the immutable target, removes the running flag, and refreshes the burden (`common/scripted_effects/019_infantry_spawn_management_effects.txt:3860-3977`).
- Cannibalization uses the exact teardown transaction rather than a division-count proxy.

### Costs, affordability, rollback, and exploit protection

- Ordinary request costs are refreshed from centralized constants plus controlled-state, event-division, congestion, active-lot, control-shortfall, prior-request, and war terms. The scale is clamped to a positive minimum before costs are rounded (`common/scripted_effects/019_infantry_spawn_management_effects.txt:4050-4232`).
- The nine ordinary request modes use explicit greater-than-or-equals affordability checks over army experience, equipment, fuel, and manpower (`common/scripted_triggers/019_infantry_spawn_muster_board_triggers.txt:178-279`).
- The paid request snapshots all affected ledger lengths, global counters, engine-division count, resources, relevant flags, and prototype stockpiles before dispatch (`common/scripted_effects/019_infantry_spawn_management_effects.txt:4470-4545`). Failed materialisation rolls back exact created units/templates and ledgers and refunds the recorded costs; cooldown begins only for a committed request.
- Anomalous-family reinforcement goes through the sole provider registry, revalidates the selected family/provider, pays provider and shared overhead costs, proves materialisation, refunds on failure, and starts cooldown only on success.
- Derivative targeted actions revalidate the target and route state immediately before payment or mutation. Integration stores the target state and cancels cleanly on ownership/control loss; submission stores the exact target and creates a bounded war goal only after timeout revalidation.

### Mission activation, timeout, cancellation, and scenario interaction

- All ten ordinary timed missions are intentionally effect-activated. Each timeout calls a dedicated `infantry_spawn_defer_or_*` wrapper rather than applying directly during a same-tag scenario transaction (`common/decisions/019_infantry_spawn_decisions.txt:755-874`).
- Each deferred path records an immutable lot UID/state or a dedicated pending flag. `infantry_spawn_resume_deferred_management_completions` independently replays all ten paths after the scenario transaction closes; one invalid path does not suppress the others.
- The derivative integration and submission missions have explicit activation, cancellation triggers, cancellation effects, and timeout revalidation (`common/decisions/019_infantry_spawn_derivative_decisions.txt:439-479,541-560`). The former-parent survival mission clears its opening-crisis state on cancel or timeout (`:579-600`).
- Category visibility, scripted GUI availability, ordinary action wrappers, claimant responses, family actions, and derivative actions all use `infantry_spawn_scenario_transaction_is_idle` at their shared boundaries. No Event 019 daily, weekly, or monthly whole-world on-action was found.

### Derivative governance, diplomacy, integration, expansion, and defeat

- Governance route: rotate/centralize collective command, ratify species compacts/proclaim family primacy, and secure a muster depot.
- Family route: zombie training/rally, ghost manifestation, golem binding, registry sustainment, and sustainment sites.
- Diplomacy route: zombie containment, ghost border recognition, and golem material agreements validate exact country targets through `FROM`.
- Integration route: the three family district decisions, timed conquered-district integration, and fragmentation suppression validate state ownership/control and clean state markers on cancel/complete.
- Expansion route: former-parent command-net disruption and local-submission warning validate target relevance, relation, war, truce, and adjacency conditions before effect.
- Claimant governance: preserve/replace claimant actions validate derivative claimant state.
- Defeat cleanup cancels integration/submission, removes the three derivative missions, closes decisions, and the final cleanup clears derivative flags, variables, ideas, ledgers, and state markers.

No target-scope inversion or derivative cost-without-effect path was found.

### AI equivalence

- All **63 decisions** contain `ai_will_do`; none of the 13 missions incorrectly contains it.
- Human decisions, scripted GUI buttons, and AI actions converge on the same effects and shared feasibility triggers.
- Anomalous-family decisions that intentionally have zero ordinary AI weight are covered by the dedicated `infantry_spawn_run_anomalous_family_ai` dispatcher, which uses the same selected-family gates and effects.
- Claimant AI inherits the same exact-equality P2 as the player/GUI; it does not bypass payment.

### Localisation and icons

- All **76 unique decision/mission IDs** have both title and `_desc` localisation keys.
- All three category IDs have name and `_desc` keys.
- All **118 unique decision/category tooltip and custom-cost references** resolve to localisation.
- All **125 unique Muster Board `text`, `buttonText`, and `pdx_tooltip` references** resolve to localisation.
- The decision/category surface uses **51 unique icon references**. Every reference is defined in `interface/019_infantry_spawn.gfx`; all **154 unique texture paths** in that file exist.

### Registry boundary

Exactly one live Event 019 unit registry code file exists:

`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`

No registry file was created or edited. Family request, provider payment/refund, derivative formation materialisation, and selected-family validation route through that single registry surface.

## Explicit owner-approval blockers and consequences

### B-019-001 — exact recorded loyal-formation transfer

`infantry_spawn_natural_recorded_formation_transfer_is_available` is explicitly fail-closed with `always = no` (`common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:168-173`). `infantry_spawn_selected_claimant_can_revolt` requires it (`:175-189`).

Consequences:

- Natural multi-state claimant revolt cannot stage.
- Natural anomalous-family release prepares an exact region and transfer set but stops before ownership mutation (`common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:513-520,522-766`).
- A retained non-microstate warning is cleared without false revolt or achievement credit (`common/scripted_effects/019_infantry_spawn_claimant_effects.txt:287-311`).
- Microstate takeover/failed-coup outcomes remain available because they do not pretend to transfer an exact loyal subset.

No whole-army transfer, ratio transfer, blanket unit move, or recreate/delete substitute was used. The documented recreate/prove/delete alternative remains an explicit fallback requiring owner approval.

### B-019-002 — four exact same-battle achievements

The exact combat contract requires one exact division event target plus enemy-strength ratio, battle duration, and enemy casualties from the same victory (`common/scripted_triggers/019_infantry_spawn_achievement_triggers.txt:110-116`). The effect `infantry_spawn_achievement_record_exact_division_significant_victory` is implemented but deliberately has no public on-action caller because installed callbacks do not provide the complete atomic tuple (`common/scripted_effects/019_infantry_spawn_achievement_effects.txt:1138-1194`; `common/on_actions/019_infantry_spawn_achievement_on_actions.txt:4-11`).

The four registered but currently unobtainable achievements are:

1. `019_infantry_spawn_one_battalion_wonder` — **One Battalion Wonder**
2. `019_infantry_spawn_combined_arms_accident` — **Combined-Arms Accident**
3. `019_infantry_spawn_borrowed_future` — **Borrowed Future**
4. `019_infantry_spawn_barracks_of_babel` — **Barracks of Babel**

Their definitions are at `common/achievements/chaos_redux_achievements.txt:3131-3210`; player-facing names/tooltips are at `localisation/english/chaosx_achievements_l_english.yml:629-652`. No country-level combat proxy, leader-victory proxy, duration guess, casualty guess, or simulated-battle fallback was used.

## Validation evidence

Read-only mechanical checks over the live worktree produced these results:

- Top-level brace-aware inventory: 35 decisions/10 missions in the ordinary file, 6/0 in the claimant file, 22/3 in the derivative file; 76 unique IDs total.
- AI scan: 63/63 decisions contain `ai_will_do`; 0/13 missions contain it.
- Localisation scan: 0 missing title keys, 0 missing `_desc` keys, 0 missing category name/description keys, 0 missing among 118 decision/category cost-tooltip keys, and 0 missing among 125 Muster Board text-tooltip keys.
- Asset scan: 0 missing sprite definitions among 51 referenced decision/category icons and 0 missing files among 154 textures registered by `interface/019_infantry_spawn.gfx`.
- Registry scan: exactly one live Event 019 unit registry code file.
- Source trace: all ordinary mission timeouts use dedicated defer/replay wrappers; derivative integration/submission missions include cancellation and revalidation; request/provider transactions snapshot/pay/prove/refund; GUI and decisions share effects.

## Simplifications, omissions, blockers, and residual risk

- No simplification or fallback was introduced by this audit.
- Historical snapshot state: P1 and P2 were open when the original audit was written. The live parent-resolution re-audit below resolves both findings; the two explicit owner-approval blocks above remain unresolved.
- The exact-transfer and same-battle omissions are intentional fail-closed omissions, not silently substituted mechanics.
- This was a source-level specialist audit of a concurrently changing worktree. The required parent-resolution recheck of DMM-019-P1-001 and DMM-019-P2-001 is recorded below.

## Files changed by this subagent

1. `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_decision_mission_specialist_audit_2026_07_15.md` — this audit handoff only.

No gameplay, localisation, asset, specification, workbook, registry, or existing documentation file was changed.

## Parent resolution re-audit — 2026-07-15

### Live verdict

The live parent remediation resolves both historical decision/mission findings. The audited severity counts are **P0: 0, P1: 0, P2: 0**. No replacement P0, P1, or P2 finding was found in the exact-cost paths, annex cleanup transaction, retry ownership, decision/mission inventory, AI parity, deferred completion paths, Muster Board wiring, or scenario-bypass cleanup.

The original DMM-019-P1-001 and DMM-019-P2-001 sections above remain as resolved history: their line references and descriptions record the defective snapshot and are not the live verdict.

### DMM-019-P2-001 resolution — exact claimant affordability and payment

A mechanical scan of `infantry_spawn_selected_claimant_demand_can_be_paid` plus the four payable claimant-response triggers finds **16** `compare = greater_than_or_equals` resource comparisons and **0** strict shorthand resource comparisons in the audited contract (`common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:210-316`). Demand acceptance contributes ten comparisons and recognition, counter-command, discredit, and arrest contribute six.

| Payable path | Equality-accepting gates | Exact debit evidence |
| --- | ---: | --- |
| Equipment share | infantry equipment and support equipment, 2 | The same two `infantry_spawn_claimant_cost.equipment_share_*` constants are separately negated and removed once, then applied to their matching obligation families (`common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt:294-309`). |
| Autonomous district | command power, 1 | The same `autonomous_district_command_power` constant is passed once through the shared payment helper (`:311-324`). |
| Another formation | army experience, 1 | The same `another_formation_army_experience` constant is debited once, and only after exact registry materialisation succeeds; failure retains the unresolved demand without charging (`:353-403`). |
| Political seat | political power, 1 | The same `political_seat_political_power` constant is debited once (`:405-412`). |
| Emergency powers | stability, 1 | The same `emergency_power_stability` constant is debited once (`:414-422`). |
| Subordinate command | army experience and command power, 2 | The two matching `infantry_spawn_generalissimo_cost.subordinate_command_*` constants are each debited once (`:424-436`). |
| Parallel command | political power and command power, 2 | The two matching `infantry_spawn_generalissimo_cost.parallel_command_*` constants are each debited once (`:438-450`). |
| Recognition | political power, 1 | The same `recognition_political_power` constant is negated and debited once (`common/scripted_effects/019_infantry_spawn_claimant_response_effects.txt:8-19`). |
| Counter-command | army experience and command power, 2 | The matching two `counter_command_*` constants are each debited once (`:21-41`). |
| Discredit | political power, 1 | The same `discredit_political_power` constant is debited once (`:43-58`). |
| Arrest | command power and stability, 2 | The matching two `arrest_*` constants are each debited once (`:60-79`). |

The shared demand payment helper negates the current temporary cost before dispatching exactly one resource effect (`common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt:200-218`). `infantry_spawn_accept_selected_claimant_demand` revalidates the live selected claimant, pending demand, demand row, and current resources at effect entry, snapshots only the current demand discriminator, executes one mutually exclusive branch, and closes the demand once only after successful resolution (`:459-506`). The four response effects likewise re-enter their shared `infantry_spawn_can_*` triggers immediately before debit and mutation. The decision, scripted-GUI, and AI routes all call these same triggers and effects. No underpayment, double charge, or stale affordability snapshot remains.

### DMM-019-P1-001 resolution — frozen proof and exact-country retry

`infantry_spawn_prepare_annex_cleanup_unit_set` now creates one immutable set of exact unit UIDs, delete-cohort IDs, and template UIDs only after aligned-ledger and safe-scenario preflight. It deduplicates each identity, verifies stored live-division identity, and sets `infantry_spawn_annex_cleanup_set_frozen` only after success (`common/scripted_effects/019_infantry_spawn_management_effects.txt:6930-7090`). A failed preflight before destructive work clears the incomplete arrays. Once frozen, retries do not recalculate or clear the set, so a partial deletion cannot erase the original proof obligation (`:7091-7101`).

Deletion and absence proof remain exact: stored verified division scopes, delete-cohort IDs, and UID-filtered divisions are checked on the annexed country and the recorded annexer, without a recurring or whole-world cleanup pass (`:7104-7260`). Template deletion and proof use only the frozen template identities (`:7262-7330`). The cleanup failure branches set only `infantry_spawn_annex_cleanup_invariant_failure`; they do not set the completion flag and immediately enqueue the same exact country for retry (`:7650-7689`).

`infantry_spawn_finalize_annexed_ordinary_country_cleanup` clears all three frozen proof arrays and `infantry_spawn_annex_cleanup_set_frozen`, then clears state markers, claimant/runtime mission and idea state, achievement attempts, profile totals, ledgers, auxiliary arrays, scenario state, flags, variables, participant state, and the cleanup lock. Its final statement is the sole live `set_country_flag = infantry_spawn_country_cleanup_complete` in Event 019 (`:7627-7648`). The only other repository occurrence that mutates this flag clears it during fresh country-system initialization; no failure path sets it.

The annexer-owned retry contract is exact and bounded:

1. `infantry_spawn_enqueue_annex_cleanup_retry` stores the annexed country scope in an annexer-local persistent scope array, checks `is_in_array` before adding, and calls the scheduler (`:7707-7731`).
2. `infantry_spawn_schedule_annex_cleanup_retry` uses one annexer-local scheduled flag and the centralized `infantry_spawn_event.annex_cleanup_retry_days` constant, so simultaneous failures cannot create parallel drain chains (`:7692-7705`; `common/script_constants/019_infantry_spawn_constants.txt:34`).
3. Hidden event `chaosx.nr19.916` calls only the queue processor. Each firing selects index zero, retries that exact country directly, and removes it only after that country positively reports `infantry_spawn_country_cleanup_complete`; it then safely schedules the next firing if work remains (`common/scripted_effects/019_infantry_spawn_management_effects.txt:7733-7753`; `events/019_infantry_spawn.txt:663-674`). There is no removal based on `exists = no`, state loss, an invariant flag, or any guessed stale condition.
4. `infantry_spawn_migrate_annex_cleanup_retry_queue` copies each exact pending country into the next annexer's queue with deduplication, clears the former owner's queue and scheduled marker, and schedules the new owner (`common/scripted_effects/019_infantry_spawn_management_effects.txt:7755-7799`). `on_annex` invokes this migration before defeat history and before cleanup of the former queue owner, so an annexer annexed while holding retries cannot lose them (`common/on_actions/019_infantry_spawn_achievement_on_actions.txt:30-56`).

Retries do not replay annex victory, claimant victory, derivative defeat, transfer, death, or progression effects: those remain in the one-shot `on_annex` history path, while event `nr19.916` calls only cleanup. Queue deduplication, the scheduled marker, the completion guard, and positive-only removal prevent duplicate finalization. Already absent frozen UIDs do not satisfy later destroy passes, all deletion uses `disband = no`, and final accounting state is cleared once by the finalizer rather than incremented by retry. Official scope documentation also states that variable scopes remain valid scopes; the queue nevertheless requires a successfully saved exact event target before invoking cleanup and never treats a nonexistent country as proof of completion. No stale-scope removal, invalid ROOT/FROM assumption, duplicate transfer/death/count/progression path, or recurring whole-world retry loop was found.

### Full decision, mission, GUI, AI, and scenario regression pass

The live top-level inventory remains exact:

| Surface | Decisions | Missions | Decisions with `ai_will_do` |
| --- | ---: | ---: | ---: |
| Ordinary management | 35 | 10 | 35 |
| Claimant | 6 | 0 | 6 |
| Derivative operations | 22 | 3 | 22 |
| **Total** | **63** | **13** | **63** |

All three categories still use load-safe `allowed = { always = yes }`, transaction-idle visibility, and their intended ordinary, claimant, or derivative phase gates (`common/decisions/categories/019_infantry_spawn_decision_categories.txt:11-37`; `common/decisions/categories/019_infantry_spawn_claimant_categories.txt:10-20`; `common/decisions/categories/019_infantry_spawn_derivative_decision_categories.txt:10-25`). Every decision has `ai_will_do`; none of the thirteen mission blocks does. Human and AI completion use the same shared feasibility and execution effects.

All ten ordinary timed missions remain effect-activated and route timeout through dedicated `infantry_spawn_defer_or_*` wrappers (`common/decisions/019_infantry_spawn_decisions.txt:755-874`). Their independent replay functions validate immutable lot UID/state evidence or their dedicated pending flag, apply or quarantine only their own result, and clear only their own evidence. `infantry_spawn_resume_deferred_management_completions` calls all ten independently, and the aggregate replay runs only after `infantry_spawn_scenario_transaction_is_idle` (`common/scripted_effects/019_infantry_spawn_management_effects.txt:5022-5428,6751-6761`). The three derivative missions retain activation, cancellation, cleanup, and timeout revalidation for exact state/country targets (`common/decisions/019_infantry_spawn_derivative_decisions.txt:439-479,541-560,579-600`).

Selected-lot and phased Muster Board parity is unchanged. The ordinary decisions and GUI call the same nine selected-lot/prototype execution wrappers; claimant decisions and all six claimant buttons call the same response effects; all seven family actions share the same gates and effects. GUI enabled blocks reuse the decision-side `infantry_spawn_can_*` triggers, while scripted-GUI AI remains disabled so it cannot create a second AI execution path (`common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:26-102,109-198,229`; ordinary and claimant decision files).

Scenario bypass cleanup is clean at P0, P1, and P2 severity. Applying a scenario profile first clears any previous bypass/profile/evolution-force flags, actor package evaluation clears them before either commit or rollback, identity failure clears them, failed same-tag actor cleanup clears them, annex finalization clears them, and the launch-level final sweep removes any residual flag from every processed actor (`common/scripted_effects/019_infantry_spawn_scenario_effects.txt:85-134,2015-2026,2351-2540,2836-2848`; management finalizer `:7639`). Successful same-tag commit and proven rollback both use `infantry_spawn_scenario_finish_same_tag_transaction`, which clears the active/cleanup flags and snapshot before replaying deferred Event 019 actions (`common/scripted_effects/019_infantry_spawn_scenario_effects.txt:1744-1759,2148-2189`). The only `every_country` passes are the one-time scenario launch host selection and final bypass sweep; no Event 019 daily, weekly, or monthly whole-world on-action exists.

Exactly one permitted Event 019 registry code file remains:

`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`

No Event 019 registry file was added, duplicated, or edited by this subagent.

### Residual blockers and simplifications

The two explicit owner-approval blockers remain unchanged: B-019-001 exact recorded loyal-formation transfer and B-019-002 the four exact same-battle achievements. Both remain fail-closed; this re-audit introduced no fallback, simplification, or weaker proxy. They do not reopen a P0, P1, or P2 decision/mission finding, but they still prevent a global Event 019 completion claim.

This re-audit changed only this handoff file. No gameplay, localisation, asset, specification, workbook, registry, event, decision, mission, scripted effect, scripted trigger, GUI, on-action, or constant source was edited.
