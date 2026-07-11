# Event 005 Command and Corridors Backend Handoff

Date: 2026-07-11

Agent role: `chaosx_scripted_system_architect`

Status: backend implementation complete for the assigned constants, scripted-trigger, scripted-effect, and handoff surfaces. Parent-owned decisions, localisation, AI, event text, selected-target lifecycle, and focus call sites remain outside this patch.

## Changed Files

- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_07_11_soviet_command_corridors_backend_handoff.md`

No decision, event, localisation, MTTH, focus, AI, or recurring on-action file was edited by this agent.

## Mission Family Classification

All 118 existing Soviet missions remain present and keep their existing identifiers. Their existing primary outcome helper supplies one exclusive backend family:

- Chain of Command: `command`, `authority`, and `cleanup` outcomes; 37 missions.
- Corridors and Depots: `rail` and `depot` outcomes; 21 missions.
- Republic Settlement: `settlement`, `foreign`, `league`, `legal`, and `old_movement` outcomes; 60 missions.

Public active-family triggers:

- `has_active_soviet_collapse_chain_of_command_objective`
- `has_active_soviet_collapse_corridors_and_depots_objective`
- `has_active_soviet_collapse_republic_settlement_objective`

Each trigger enumerates its exact live mission identifiers. The three sets are disjoint and their union is all 118 missions.

## Priority Backend

Public persistent priority variables:

- `soviet_collapse_chain_of_command_priority`
- `soviet_collapse_corridors_and_depots_priority`
- `soviet_collapse_republic_settlement_priority`

Public effects:

- `soviet_collapse_compute_operational_family_priorities`
- `soviet_collapse_activate_priority_operational_objectives`
- `soviet_collapse_activate_priority_chain_of_command_objective`
- `soviet_collapse_activate_priority_corridors_and_depots_objective`
- `soviet_collapse_activate_priority_republic_settlement_objective`

Public dominant-priority flags and scripted-localisation triggers:

- `soviet_collapse_priority_chain_of_command` / `is_soviet_collapse_chain_of_command_priority`
- `soviet_collapse_priority_corridors_and_depots` / `is_soviet_collapse_corridors_and_depots_priority`
- `soviet_collapse_priority_republic_settlement` / `is_soviet_collapse_republic_settlement_priority`

One-shot next-refill flags:

- `soviet_collapse_next_priority_chain_of_command`
- `soviet_collapse_next_priority_corridors_and_depots`
- `soviet_collapse_next_priority_republic_settlement`

The priority calculation measures Authority and Obedience shortfalls or Republic and Depot excesses against calm, contested, or crisis recovery bands. Foreign Appetite, League Cohesion, and Old Movement pressure then modify all three scores with family-specific weights. The one-shot flags add a centralized priority boost and are cleared only after the family prefill has run.

The existing `soviet_collapse_activate_opening_objectives` flow now:

1. prunes the existing invalid missions;
2. refreshes or clears the corridor state target;
3. prunes active corridor missions if no valid geography exists;
4. counts active missions and computes the unchanged active cap;
5. prunes the unchanged surplus ordering;
6. prefills at most one mission per family, highest priority first; and
7. runs the complete existing 118-mission remainder in its prior order.

This is not a second mission board. The existing refill event, monthly refill cap, active-objective cap, mission IDs, and done flags remain authoritative.

## Outcome and Compromise API

Public family delta helpers:

- `soviet_collapse_apply_chain_of_command_decisive_outcome`
- `soviet_collapse_apply_chain_of_command_compromise_outcome`
- `soviet_collapse_apply_chain_of_command_failure_outcome`
- `soviet_collapse_apply_corridors_and_depots_decisive_outcome`
- `soviet_collapse_apply_corridors_and_depots_compromise_outcome`
- `soviet_collapse_apply_corridors_and_depots_failure_outcome`
- `soviet_collapse_apply_republic_settlement_decisive_outcome`
- `soviet_collapse_apply_republic_settlement_compromise_outcome`
- `soviet_collapse_apply_republic_settlement_failure_outcome`

The existing command, depot, and settlement success/failure wrappers delegate to the matching family helpers without changing their previous decisive or failure deltas and delayed report events. Other existing outcome wrappers retain their specialized deltas; their safe success/failure hooks clear or record the corresponding operational release pressure where a direct mapping exists.

Compromise directions are exact:

- Chain of Command: Authority `+1`, Military Obedience `+1`, Republic Confidence pressure `+2`.
- Corridors and Depots: Depot Vulnerability `-2`, Authority `-2`, Foreign Appetite `+1`, League Cohesion `+2`.
- Republic Settlement: Republic Confidence pressure `-2`, Authority `-2`, Foreign Appetite `+1`, League Cohesion `+2`.

Compromise increments neither the monthly success nor monthly failure counter.

Public affordability and payment helpers:

- `can_pay_soviet_collapse_chain_of_command_compromise_cost` / `soviet_collapse_pay_chain_of_command_compromise_cost`: 15 command power.
- `can_pay_soviet_collapse_corridors_and_depots_compromise_cost` / `soviet_collapse_pay_corridors_and_depots_compromise_cost`: 35 political power.
- `can_pay_soviet_collapse_republic_settlement_compromise_cost` / `soviet_collapse_pay_republic_settlement_compromise_cost`: 50 political power.

Public one-mission resolvers:

- `soviet_collapse_resolve_active_chain_of_command_objective_by_compromise`
- `soviet_collapse_resolve_active_corridors_and_depots_objective_by_compromise`
- `soviet_collapse_resolve_active_republic_settlement_objective_by_compromise`

Each resolver finds the first active mission in its family, sets that mission's existing `soviet_collapse_mission_NNN_done` flag, removes it, applies one compromise outcome, and queues the existing refill. `remove_mission` was verified against current vanilla documentation: it does not run mission timeout or completion effects. Parent compromise decisions currently call the payment helper and resolver separately, so they must not also charge an ordinary decision `cost`.

## Corridor Geography API

Public state/country triggers and effects:

- `is_soviet_collapse_corridor_state_candidate`: state scope, with `ROOT` required to be the Soviet crisis owner.
- `has_soviet_collapse_corridor_state_candidate`: Soviet country scope.
- `has_soviet_collapse_selected_corridor_state`: Soviet country scope.
- `soviet_collapse_select_corridor_state_candidate`
- `soviet_collapse_clear_corridor_state_candidate`
- `soviet_collapse_prune_corridor_objectives_without_geography`

The country-scope state pointer is `soviet_collapse_corridor_state_target`; the selected state also carries `soviet_collapse_corridor_state_target` as a state flag. The pointer is suitable for scripted localisation as `[?soviet_collapse_corridor_state_target.GetName]`.

A candidate must be original Union territory, currently owned and controlled by the Soviet crisis owner, passable, and meaningful because it has a supply node, naval base, a verified railway connection to the capital, or a border with territory not owned and controlled by Moscow. The implementation uses officially documented state variables, state flags, `random_owned_state`, `has_railway_connection`, `supply_node`, `naval_base`, and scope-valued variables. The building-presence comparisons use the vanilla `> 0` existence sentinel because those state building triggers do not take script-constant tokens.

There is no hardcoded substitute state. If no candidate exists, the 21 corridor-family activations in both prefill and remainder are suppressed, and already active corridor missions are removed without being marked done so they can return after valid geography exists.

## Release Cause Integration

Public effects:

- `soviet_collapse_record_dominant_release_cause`
- `soviet_collapse_apply_recorded_release_cause_force_package`
- `soviet_collapse_apply_recorded_release_cause_setup`
- `soviet_collapse_apply_release_cause_neighbor_reactions`

Released-country numeric variable and flags:

- `soviet_collapse_release_cause`
- `soviet_collapse_release_cause_command_fracture`
- `soviet_collapse_release_cause_corridor_depot_loss`
- `soviet_collapse_release_cause_negotiated_political_break`
- `soviet_collapse_release_cause_foreign_league_rupture`

Public cause triggers use the corresponding `has_soviet_collapse_release_cause_*` names.

The release setup package records the cause after the existing source-pressure and evolution bookkeeping, then applies it inside the existing dynamic force package and republic-component initialization. Cause values are `1` command, `2` corridor/depot, `3` negotiated break, and `4` foreign/League rupture. Recent mapped mission failures contribute a centralized score boost; the live crisis values remain the dominant comparison.

Cause consequences:

- command fracture adds local-authority pressure and one field unit, and prioritizes command next;
- corridor/depot loss adds local depot control and one field unit, and prioritizes corridors next;
- negotiated break adds institution strength and independence resilience, and prioritizes settlement next; and
- foreign/League rupture adds liaison reach, patronage risk, and League support, and prioritizes settlement next.

`soviet_collapse_release_sponsor_interest` and `soviet_collapse_release_sponsor_interest_active` expose sponsor interest without scanning or hardcoding patron tags. Neighboring countries already marked as Event 005 breakaways receive a bounded, one-time `soviet_collapse_neighbor_release_reaction_pending` flag, `soviet_collapse_last_neighbor_release_cause`, a cause-specific reaction flag, and a small matching component adjustment. This uses `every_neighbor_country` only during a release; no recurring country or world iteration was introduced.

The cause recorder requires `SOV` to exist. Canonical Event 005 release paths meet that precondition. It deliberately does nothing outside that context rather than inventing a fallback cause.

## UWR and KMB Shared Hooks

Shared KMB tuning:

- `constant:soviet_collapse_kmb_ai.superiority_ratio = 1.25`
- the six decision costs are centralized in `soviet_collapse_kmb_balance` as `deepen_subsoil_extraction_cost`, `sell_coal_for_machines_cost`, `open_export_auction_cost`, `sign_resource_treaty_cost`, `trade_oil_for_trucks_cost`, and `force_mining_concession_cost`.

Public KMB country-scope hooks:

- `soviet_collapse_apply_kmb_treaty_corridor_crisis_hook`: local Depot Control `+4`; SOV Depot Vulnerability `+2`; SOV Foreign Appetite `+1`; next corridor priority.
- `soviet_collapse_apply_kmb_concession_crisis_hook`: SOV Depot Vulnerability `+4`; SOV Republic Confidence pressure `+3`; SOV Foreign Appetite `+2`; next corridor and settlement priorities.

Public UWR affected-state hook:

- `soviet_collapse_mark_uwr_contaminated_state_for_aftermath`: records `soviet_collapse_uwr_contamination_aftermath` and an owner pointer once, then gives SOV Republic Confidence pressure `+3`, Foreign Appetite `+2`, and next settlement priority.
- `has_soviet_collapse_uwr_contamination_aftermath`: state trigger for later aftermath work.

These hooks add no scheduler. At handoff time, the parent still needs to call the KMB treaty hook from `kmb_sign_resource_treaty`, the KMB concession hook from `kmb_force_mining_concession`, and the UWR state hook at each actual contamination application site. The backend intentionally does not guess which states are contaminated.

## Validation Evidence

- Decision mission definitions: 118 unique IDs.
- Family maps: 37 command + 21 corridor + 60 settlement = 118; no missing or duplicate membership.
- Priority prefill maps: 118; no missing or duplicate mission.
- Compromise resolver maps: 118; no missing or duplicate mission.
- Existing remainder activation map: 118; no missing mission.
- Corridor remainder geography guards: 21 of 21 corridor missions.
- Nine progressive-release scheduler/effect bodies compared byte-normalized with `HEAD`: no changes.
- Six progressive-release gate/candidate trigger bodies compared byte-normalized with `HEAD`: no changes.
- All new public effect and trigger identifiers have one definition; all 108 new shared-constant references resolve to a defined key.

## Remaining Parent Wiring and Risks

- Wire the three UWR/KMB call sites listed above. Until then their constants and helpers are inert.
- If player-facing corridor mission text should name the selected state, use the stored state pointer in localisation. This agent did not edit mission localisation.
- The existing missions are non-targeted missions. The backend binds the corridor family to one valid runtime state and suppresses it without geography, but it does not rewrite all 21 mission completion requirements into state-specific projects. That broader rewrite was unsafe inside the assigned scripted-backend boundary and should be designed separately if desired.
- Sponsor interest is exposed through released-country state for the existing selected target desks and AI to consume; no new patron scan or tag list was added.
- No fallback state, fallback cause, parallel mission board, second release scheduler, recurring world loop, or simplification was introduced in the assigned backend.
