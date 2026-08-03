# Event 012 W2 South America and Oceania scripted-system handoff

Date: 2026-07-30

Follow-up repair: 2026-08-03.

Owner: `/root/africa_world_w2_south_america_oceania`

Scope: grounded South American and Oceanian package loops only. The implementation keeps the existing package actors, variables, route helpers, focus IDs, and shared world-order proof surfaces. It does not create tags, models, high-chaos routes, readiness setters, recurring all-country scans, or new event targets.

The 2026-08-03 follow-up closes a receipt mismatch in the shared proof trigger. The successful `.505.a` ratification callback now writes `africa_south_america_resource_debt_law_ratified` and `africa_south_america_south_atlantic_partnership_ratified`; the successful `.605.a` callback now writes `africa_oceania_pacific_reserve_ratified` and `africa_oceania_africa_sea_treaty_ratified`. These are permanent ratification receipts, not focus-click shortcuts, and are written only after the existing local proof, founding, heartland, constituent, and balance/network gates pass.

## Changed files

- `common/scripted_effects/012_africa_world_south_america_oceania_effects.txt` adds the country-scoped decision contracts, founding outcomes, shared-lane wrappers, ratification gates, lifecycle responses, retry helpers, and terminal cleanup for both packages.
- `common/national_focus/012_africa_world_south_america_focus.txt` opens the South American congress, calls the three W2 shared-lane wrappers, requires the local proof flags and lifecycle proof at the existing capstone, and delegates sovereign completion to the W2 helper.
- `common/national_focus/012_africa_world_oceania_focus.txt` performs the analogous Oceanian wiring without changing the existing same-block OR prerequisite structure.
- `events/012_africa_world_package_south_america_oceania.txt` defines `africa_world_package.500` through `.506` and `.600` through `.606` for opening congress, founding success or compromise or failure, shared-lane ratification, and lifecycle review.
- `localisation/english/012_africa_world_south_america_oceania_l_english.yml` adds the six decision contracts, all twenty-eight event title, description, option, and tooltip keys, and the focus proof tooltips. The file is UTF-8 with BOM.
- This handoff is the integration record. No shared constants, triggers, decisions, world-order effects, event-log surfaces, spreadsheet rows, or assets were edited by this subagent.

## Helper map

All helpers below are country-scoped and are called on the installed package actor.

| Helper | Inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `africa_south_america_open_world_package_congress` | Installed South American package and no opening marker | Sets opening congress and phase `opening_congress`, resets shared crisis result to `none`, and fires `.500` once | Opening focus completion |
| `africa_south_america_balance_the_three_regions` | Existing Andean, Amazon, Plata, authority, and indigenous variables | Locks the action, lifts the weakest regional voice, adds indigenous representation and authority, clamps the ledger, and opens `.501`; first calls the deferred-ratification retry helper | Future package decision block and `.500.a` |
| `africa_south_america_audit_resource_concessions_and_debt` | Existing resource, debt, indigenous, legitimacy variables | Locks the action, raises resource sovereignty and debt freedom, conditionally raises indigenous representation, clamps the ledger, and opens `.501`; first calls the deferred-ratification retry helper | Future package decision block and `.500.b` |
| `africa_south_america_protect_river_forest_and_corridor_rights` | Existing Amazon, indigenous, resource variables | Locks the action, raises river, forest, indigenous, and corridor support, grants the existing train and convoy reward, clamps the ledger, and opens `.501`; first calls the deferred-ratification retry helper | Future package decision block and `.500.c` |
| `africa_south_america_open_founding_dispute` | No open, success, or compromise founding state and no sovereign completion | Sets the founding-dispute flag and fires `.501` | The three decision contracts |
| `africa_south_america_resolve_founding_success`, `..._compromise`, `..._failure` | Open founding dispute | Writes the shared crisis enum, adjusts regional and package variables, removes the existing founding-problem idea only for success or compromise, clears action locks, clamps, and fires `.502`, `.503`, or `.504` | `.501.a`, `.501.b`, `.501.c` |
| `africa_south_america_apply_resource_and_debt_law_w2`, `...apply_defence_and_corridors_w2`, `...apply_south_atlantic_partnership_w2` | Installed package and existing shared focus lane | Calls the accepted old helper, records one local proof flag, sets phase `shared_lanes`, and the final partnership wrapper opens `.505` once | The three existing shared focus completion rewards |
| `africa_south_america_maybe_reopen_shared_lane_ratification` | Pending local ratification review, all three local proof flags, and the existing three-region balance trigger | Clears the pending marker, reopens `.505`, and prevents a deferral from deadlocking the capstone | First line of each named decision contract |
| `africa_south_america_mark_shared_lane_ratification` | All local proof flags, founding success or compromise, balance, heartland, and constituent proof | Sets local shared-lane ratification, clears pending review, sets phase `ratification`, and adds legitimacy | `.505.a` |
| `africa_south_america_complete_sovereign_package_w2` | Installed package, shared-lane ratification, lifecycle resolution, and shared `africa_world_package_ratification_is_proven` | Sets constitution proof, sets phase `sovereign`, calls `africa_world_finalize_distinct_package_identity`, and runs transient cleanup | Existing South American capstone reward |
| `africa_south_america_maybe_open_lifecycle_crisis`, `...resolve_lifecycle_crisis`, `...impose_emergency_lifecycle_terms`, `...defer_lifecycle_settlement` | Existing low package or South American variables and lifecycle flags | Opens `.506` when needed; the three responses clear the open flag, set lifecycle resolved, adjust package ledgers, and retain a failure memory for defer | First two shared wrappers and `.506` |
| `africa_south_america_cleanup_w2_play_loop` | Sovereign completion | Clears opening, event-seen, open, lock, shared-ratification-seen, and pending-review flags while preserving permanent proof and route history | Sovereign completion helper |
| `africa_oceania_open_world_package_congress` | Installed Oceanian package and no opening marker | Sets opening congress and phase `opening_congress`, resets crisis result to `none`, and fires `.600` once | Opening focus completion |
| `africa_oceania_seat_the_island_congress` | Existing island, indigenous, air, and legitimacy variables | Locks the action, strengthens island and indigenous representation, clamps, and opens `.601`; first calls the deferred-ratification retry helper | Future package decision block and `.600.a` |
| `africa_oceania_maintain_convoy_air_and_disaster_networks` | Existing convoy, air, dispersed-industry variables | Locks the action, raises convoy reach, air network, and dispersed industry, grants the existing convoy reward, clamps, and opens `.601`; first calls the deferred-ratification retry helper | Future package decision block and `.600.b` |
| `africa_oceania_settle_land_basing_and_evacuation_rights` | Existing indigenous, naval, and island variables | Locks the action, raises consent and protection, records refusal rights, clamps, and opens `.601`; first calls the deferred-ratification retry helper | Future package decision block and `.600.c` |
| `africa_oceania_open_founding_dispute`, `...resolve_founding_success`, `...resolve_founding_compromise`, `...resolve_founding_failure` | Oceanian founding flags and existing ledgers | Mirrors the South American founding lifecycle through `.601` to `.602`, `.603`, or `.604` with Oceanian variables and the shared crisis enum | Oceanian decision contracts and `.601` |
| `africa_oceania_apply_constitution_and_withdrawal_law_w2`, `...apply_pacific_defence_and_disaster_reserve_w2`, `...apply_africa_sea_treaty_w2` | Installed package and existing shared focus lane | Calls the accepted old helper, records one local proof flag, sets phase `shared_lanes`, and the final treaty wrapper opens `.605` once | The three existing shared focus completion rewards |
| `africa_oceania_maybe_reopen_shared_lane_ratification`, `africa_oceania_mark_shared_lane_ratification` | Pending review or all local proof, founding, network, heartland, and constituent proof | Reopens `.605` after deferral or records local shared-lane ratification and phase `ratification` | Named decision contracts and `.605.a` |
| `africa_oceania_complete_sovereign_package_w2` | Installed package, shared-lane ratification, lifecycle resolution, and shared `africa_world_package_ratification_is_proven` | Sets constitution proof, sets phase `sovereign`, calls the accepted finalizer, and runs transient cleanup | Existing Oceanian capstone reward |
| `africa_oceania_maybe_open_lifecycle_crisis`, `...resolve_lifecycle_crisis`, `...impose_emergency_lifecycle_terms`, `...defer_lifecycle_settlement`, `africa_oceania_cleanup_w2_play_loop` | Existing Oceanian ledgers and lifecycle flags | Mirrors the South American lifecycle open, response, and cleanup rules through `.606` | Shared wrappers, `.606`, and sovereign completion |

## Exact decision integration blocks

Insert these blocks into the existing `africa_world_polity_actions_category` in `common/decisions/012_africa_decisions.txt`. The blocks intentionally use existing decision syntax and the package actor's country scope. The `hidden_effect` wrapper keeps the player-facing tooltip authoritative while the scripted effect performs the ledger mutation.

```text
africa_south_america_balance_the_three_regions = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { africa_world_package_is_installed = yes has_country_flag = africa_world_south_america_package NOT = { has_country_flag = africa_world_package_sovereign_complete } }
	available = { NOT = { has_country_flag = africa_south_america_balance_action_lock } }
	cost = constant:africa_world_package_protocol.routine_action_pp_cost
	custom_cost_trigger = { political_power > constant:africa_world_package_protocol.routine_action_pp_cost }
	custom_cost_text = africa_world_package_action_cost
	complete_effect = { custom_effect_tooltip = africa_south_america_balance_the_three_regions_tt hidden_effect = { africa_south_america_balance_the_three_regions = yes } }
	ai_will_do = {
		base = constant:africa_world_package_protocol.ai_negotiate
		modifier = { factor = constant:africa_world_order.ai_modifier_double check_variable = { africa_south_america_amazon_voice < constant:africa_measure.medium } }
	}
}

africa_south_america_audit_resource_concessions_and_debt = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { africa_world_package_is_installed = yes has_country_flag = africa_world_south_america_package NOT = { has_country_flag = africa_world_package_sovereign_complete } }
	available = { NOT = { has_country_flag = africa_south_america_resource_debt_action_lock } }
	cost = constant:africa_world_package_protocol.negotiated_action_pp_cost
	custom_cost_trigger = { political_power > constant:africa_world_package_protocol.negotiated_action_pp_cost }
	custom_cost_text = africa_world_package_action_cost
	complete_effect = { custom_effect_tooltip = africa_south_america_audit_resource_concessions_and_debt_tt hidden_effect = { africa_south_america_audit_resource_concessions_and_debt = yes } }
	ai_will_do = {
		base = constant:africa_world_package_protocol.ai_negotiate
		modifier = { factor = constant:africa_world_order.ai_modifier_double check_variable = { africa_south_america_debt_freedom < constant:africa_measure.medium } }
	}
}

africa_south_america_protect_river_forest_and_corridor_rights = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { africa_world_package_is_installed = yes has_country_flag = africa_world_south_america_package NOT = { has_country_flag = africa_world_package_sovereign_complete } }
	available = { NOT = { has_country_flag = africa_south_america_corridor_action_lock } }
	cost = constant:africa_world_package_protocol.major_action_pp_cost
	custom_cost_trigger = { political_power > constant:africa_world_package_protocol.major_action_pp_cost }
	custom_cost_text = africa_world_package_action_cost
	complete_effect = { custom_effect_tooltip = africa_south_america_protect_river_forest_and_corridor_rights_tt hidden_effect = { africa_south_america_protect_river_forest_and_corridor_rights = yes } }
	ai_will_do = {
		base = constant:africa_world_package_protocol.ai_negotiate
		modifier = { factor = constant:africa_world_order.ai_modifier_double check_variable = { africa_south_america_indigenous_representation < constant:africa_measure.medium } }
	}
}

africa_oceania_seat_the_island_congress = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { africa_world_package_is_installed = yes has_country_flag = africa_world_oceania_package NOT = { has_country_flag = africa_world_package_sovereign_complete } }
	available = { NOT = { has_country_flag = africa_oceania_island_congress_action_lock } }
	cost = constant:africa_world_package_protocol.routine_action_pp_cost
	custom_cost_trigger = { political_power > constant:africa_world_package_protocol.routine_action_pp_cost }
	custom_cost_text = africa_world_package_action_cost
	complete_effect = { custom_effect_tooltip = africa_oceania_seat_the_island_congress_tt hidden_effect = { africa_oceania_seat_the_island_congress = yes } }
	ai_will_do = {
		base = constant:africa_world_package_protocol.ai_negotiate
		modifier = { factor = constant:africa_world_order.ai_modifier_double check_variable = { africa_oceania_indigenous_settlement < constant:africa_measure.medium } }
	}
}

africa_oceania_maintain_convoy_air_and_disaster_networks = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { africa_world_package_is_installed = yes has_country_flag = africa_world_oceania_package NOT = { has_country_flag = africa_world_package_sovereign_complete } }
	available = { NOT = { has_country_flag = africa_oceania_network_action_lock } }
	cost = constant:africa_world_package_protocol.negotiated_action_pp_cost
	custom_cost_trigger = { political_power > constant:africa_world_package_protocol.negotiated_action_pp_cost }
	custom_cost_text = africa_world_package_action_cost
	complete_effect = { custom_effect_tooltip = africa_oceania_maintain_convoy_air_and_disaster_networks_tt hidden_effect = { africa_oceania_maintain_convoy_air_and_disaster_networks = yes } }
	ai_will_do = {
		base = constant:africa_world_package_protocol.ai_negotiate
		modifier = { factor = constant:africa_world_order.ai_modifier_double check_variable = { africa_oceania_convoy_reach < constant:africa_measure.medium } }
	}
}

africa_oceania_settle_land_basing_and_evacuation_rights = {
	icon = GFX_decision_012_africa_charter_ledger
	visible = { africa_world_package_is_installed = yes has_country_flag = africa_world_oceania_package NOT = { has_country_flag = africa_world_package_sovereign_complete } }
	available = { NOT = { has_country_flag = africa_oceania_land_basing_action_lock } }
	cost = constant:africa_world_package_protocol.major_action_pp_cost
	custom_cost_trigger = { political_power > constant:africa_world_package_protocol.major_action_pp_cost }
	custom_cost_text = africa_world_package_action_cost
	complete_effect = { custom_effect_tooltip = africa_oceania_settle_land_basing_and_evacuation_rights_tt hidden_effect = { africa_oceania_settle_land_basing_and_evacuation_rights = yes } }
	ai_will_do = {
		base = constant:africa_world_package_protocol.ai_negotiate
		modifier = { factor = constant:africa_world_order.ai_modifier_double check_variable = { africa_oceania_indigenous_settlement < constant:africa_measure.medium } }
	}
}
```

## Required shared constants and triggers

The following shared values are required by the blocks above and the new scripted effects. The phase and crisis categories already exist in the current shared constants file and must not be duplicated.

```text
africa_world_package_protocol = {
	routine_action_pp_cost = 25
	negotiated_action_pp_cost = 35
	major_action_pp_cost = 50
}
```

The current shared categories consumed by this package are `constant:africa_world_package_phase.opening_congress`, `constituent_bargaining`, `route_committed`, `shared_lanes`, `ratification`, and `sovereign`, plus `constant:africa_world_package_crisis_result.none`, `success`, `compromise`, and `failure`.

The current shared trigger consumed by both capstones is `africa_world_package_ratification_is_proven = yes`. Its existing prerequisites include package installation, polity foundation, heartland proof, grounded route, resolved crisis, shared-lane proof, withdrawal-law proof, cleared protocol pending state, authority, legitimacy, capacity, and the accepted voluntary quorum branch. The package-local checks remain explicit in each focus and helper: South American three-region balance, the three local lane proof flags, founding success or compromise, lifecycle resolution, and Oceanian network connectivity with the three local lane proof flags, founding success or compromise, and lifecycle resolution.

No new scripted trigger is required for this tranche. If the decision owner introduces a convenience trigger, it must remain a thin wrapper around the existing package trigger and must not weaken the voluntary quorum or pending-protocol checks.

## Event target and cleanup plan

The package loops use ordinary country flags and variables only. They do not save a new event target. Existing package event targets such as `africa_host` remain owned by the shared world-order effects.

The founding dispute is guarded by `africa_south_america_founding_dispute_open` or `africa_oceania_founding_dispute_open`. Each outcome clears the open flag and all three action locks. Shared-lane review is guarded by the corresponding `...shared_lane_ratification_event_seen` and `...ratification_review_pending` flags; the decision contracts can reopen `.505` or `.605` after a defer choice. Lifecycle review is guarded by `...lifecycle_crisis_open`, and every lifecycle option marks `...lifecycle_crisis_resolved`, including the penalty-bearing defer path.

Sovereign cleanup clears the opening, event-seen, open, lock, shared-ratification-seen, and pending-review flags. Permanent proof flags, route identity, crisis result, and lifecycle history remain available to the shared terminal systems. The open congress helpers also reject a sovereign-complete actor, so clearing the event-seen marker cannot restart a completed package.

## Migration from duplicated logic

The existing three South American and three Oceanian shared focus rewards now call W2 wrappers rather than calling the old helper directly. The wrappers preserve the old route-sensitive helper behavior and add exactly one local proof flag plus the package event hook. The old helpers remain the source of route-specific institution effects and are not duplicated.

The first focus in each tree now calls the package opening helper after retaining the existing opening flag. The capstones retain their IDs and same-block OR prerequisites, add local proof and lifecycle gates, and delegate finalization to the W2 sovereign helper. No high-chaos branch was activated.

## Validation evidence

- Read the required offline Paradox Wiki pages and the relevant vanilla documentation before editing.
- Ran read-only `hoi4.event_inspect` lint against `events/012_africa_world_package_south_america_oceania.txt`. The MCP returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics; the workspace-wide helper projection was deferred and remains an analysis limitation.
- Ran read-only `hoi4.focus_inspect` for `africa_south_america_world_focus_tree` and `africa_oceania_world_focus_tree`. The inspector found the trees and preserved their layouts. It also reported pre-existing missing-helper diagnostics for shared helper resolution in the bounded focus analysis; those helpers are present in the shared scripted-effect file and are outside this handoff's ownership.
- Checked the touched Clausewitz files for balanced braces and confirmed all fourteen event IDs are unique in this file.
- Checked all new event and focus localisation references against the repository localisation key set. No new reference was missing, no duplicate key was introduced, and the new localisation file has a UTF-8 BOM.
- Confirmed the new event file has no raw AI or duration magic numbers and uses the shared response-chance and AI modifier constants.

## Risks and unsupported analysis

- The six decision blocks are handoff-only. They require the three `africa_world_package_protocol.*_action_pp_cost` keys above and the existing `africa_world_package_action_cost` localisation key to be merged by the decision owner.
- The generic ratification trigger is intentionally strict. A local shared-lane event can record its proof before the external voluntary quorum is complete, but the capstone remains unavailable until the shared trigger proves the quorum and all package-wide thresholds.
- No live HOI4 session, save, or gameplay simulation was run. The parent owns final decision wiring, event-log and spreadsheet alignment, and consumer validation.
- No fallback or simplification was used. The only unresolved surface in this handoff is the parent-owned decision integration and the shared event-log or spreadsheet documentation tranche.
