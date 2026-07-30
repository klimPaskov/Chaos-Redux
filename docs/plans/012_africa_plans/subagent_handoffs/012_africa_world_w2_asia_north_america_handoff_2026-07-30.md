# Event 012 W2 Asia and North America scripted-system handoff

## Scope and ownership

This handoff covers the second-wave Asia and North America package loops assigned to `/root/africa_world_w2_asia_north_america`. The implementation owns package-local scripted effects, events, focus call sites, event localisation, and this handoff. Shared constants, shared triggers, the decision category, and `012_africa_world_order_effects.txt` remain parent-owned and were not edited.

The event file uses `add_namespace = africa_world_package` with IDs `.300-.306` for Asia and `.400-.406` for North America. South America and Oceania may use the same namespace with their own ID ranges.

## Files changed

- `common/scripted_effects/012_africa_world_asia_north_america_effects.txt` adds named decision effects, shared-lane effects, route-aware North America extensions, founding and lifecycle result effects, and final proof gates.
- `common/national_focus/012_africa_world_asia_focus.txt` opens `.300`, calls the Asia shared-lane helpers, and requires founding, shared-lane, lifecycle, heartland, constituent, and ratification proof before final identity.
- `common/national_focus/012_africa_world_north_america_focus.txt` opens `.400`, calls the North America W2 extensions after each existing shared helper, and requires the same proof sequence before final identity.
- `events/012_africa_world_package_asia_north_america.txt` adds the fourteen country events and no periodic on-action scan.
- `localisation/english/012_africa_world_asia_north_america_l_english.yml` adds event and named-decision localisation. The file is UTF-8 with BOM.

## Helper map

| Helper | Scope | Inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- | --- |
| `africa_asia_seat_regional_centres` | Country package actor | Four centre variables | Raises the weakest centre, records `africa_asia_centres_seated` and decision-use flags, clamps package ledgers | Parent decision block below |
| `africa_asia_coordinate_food_river_monsoon_security` | Country package actor | Food, southern, and inland variables | Variable-driven food or southern gain, inland support, `africa_asia_food_lane_proof` | Parent decision block below |
| `africa_asia_open_rail_maritime_corridors` | Country package actor | Corridor, eastern, archipelago variables | Variable-driven corridor or centre gain, inland support, `africa_asia_rail_lane_proof` | Parent decision block below |
| `africa_asia_apply_food_river_monsoon_board` | Country package actor | Food lane focus | Board flag, food/southern gains, stability, food proof | `africa_asia_food_river_and_monsoon_board` |
| `africa_asia_apply_rail_maritime_corridors` | Country package actor | Rail lane focus and food/defence flags | Corridor/archipelago gains, trains, rail proof, one-time `.305` trigger when the other lane is proven | `africa_asia_rail_and_maritime_corridors` |
| `africa_asia_apply_defence_autonomy_law` | Country package actor | Food and rail proof flags | Withdrawal and union consent, command/equipment rewards, one-time `.305` trigger | `africa_asia_common_defence_and_autonomy_law` |
| `africa_asia_maybe_open_shared_lane_ratification` | Country package actor | Food, rail, defence proof flags | Idempotently opens `.305` once all three grounded Asia lanes are present | Asia lane helpers and named decision effects |
| `africa_asia_apply_indian_ocean_partnership` | Country package actor | Partnership focus | Treaty and partnership proof, archipelago/corridor gains, convoys | `africa_asia_indian_ocean_partnership` |
| `africa_asia_try_record_ratification_proof` | Country package actor | Parent `africa_world_package_ratification_is_proven` trigger | Sets `africa_asia_package_ratification_proof` only when the parent proof contract is true | Asia capstone completion |
| `africa_north_america_negotiate_caribbean_central_membership` | Country package actor | Existing North America ledgers | Caribbean, federal, sovereignty gains, decision-use flag | Parent decision block below |
| `africa_north_america_settle_indigenous_land_representation` | Country package actor | Existing Indigenous/federal/migration ledgers | Indigenous safeguards, federal representation, migration gain, local-jurisdiction flag | Parent decision block below |
| `africa_north_america_balance_industry_mobility_command` | Country package actor | Industry, migration, command ledgers | Distinct industrial/mobility/command gains and balance flag | Parent decision block below |
| `africa_north_america_extend_resources_withdrawal_law_w2` | Country package actor | Existing shared resource helper and route flags | Sets resource-lane proof and applies route-specific representation/sovereignty/industry adjustment | North America resources focus after shared helper |
| `africa_north_america_extend_two_ocean_defence_w2` | Country package actor | Existing defence helper and route flags | Sets defence-lane proof and applies route-specific command/industry/representation adjustment | North America defence focus after shared helper |
| `africa_north_america_extend_islands_settlement_w2` | Country package actor | Existing islands helper and route flags | Sets islands-lane proof and applies route-specific island settlement adjustment | North America islands focus after shared helper |
| `africa_north_america_extend_africa_diaspora_treaty_w2` | Country package actor | Existing diaspora helper and route flags | Sets diaspora-lane proof, preserves voluntary return/local acceptance/skills-and-investment flags, and triggers `.405` once all four lanes are proven | North America diaspora focus after shared helper |
| `africa_north_america_try_record_ratification_proof` | Country package actor | Parent `africa_world_package_ratification_is_proven` trigger | Sets `africa_north_america_package_ratification_proof` only when the parent proof contract is true | North America capstone completion |

## Shared crisis-result contract

All fourteen events use the parent-owned variable `africa_world_package_crisis_result`. The events write only the parent constants `constant:africa_world_package_crisis_result.none`, `.success`, `.compromise`, and `.failure`. No local result enum or conflicting numeric values were introduced. The opening events initialise `.none`, founding outcome helpers write the selected result, and shared-lane outcomes write the current result before the lifecycle event resolves.

## Event sequence and cleanup

Asia follows `.300` opening, `.301` founding choice, `.302` success, `.303` compromise, `.304` failure, `.305` shared-lane ratification, and `.306` lifecycle crisis. North America follows the identical shape with `.400-.406`. The opening focus sets the opening flag and fires the opening event. Founding options set a single outcome flag and fire exactly one result event. Result events clear pending and selected flags while retaining durable success, compromise, failure, and resolved evidence. Shared-lane helpers fire `.305` or `.405` once through `*_shared_lane_event_fired`; options resolve the lane and open the lifecycle crisis. Lifecycle options clear the transient outcome flags and retain `*_lifecycle_crisis_resolved`.

No global event target is created. No all-country daily, weekly, or monthly action is used. The package actor's existing constituent/event-target lifecycle remains untouched. The North American diaspora helpers do not move people, transfer states, create cores, or force citizenship. They preserve `africa_north_america_voluntary_return_only`, `africa_north_america_return_requires_local_acceptance`, and `africa_north_america_skills_and_investment_compact`.

## Decision integration blocks

Append these blocks inside the existing `africa_world_polity_actions_category` in `common/decisions/012_africa_decisions.txt`. The parent must add the constants described below before enabling them. The icon intentionally reuses the existing charter-ledger icon.

```text
	africa_asia_seat_the_regional_centres = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_asia_package has_country_flag = africa_asia_regional_congress_system_open }
		available = { has_country_flag = africa_world_asia_package has_country_flag = africa_asia_regional_congress_system_open NOT = { has_country_flag = africa_asia_regional_centres_decision_used } }
		cost = constant:africa_world_package_protocol.routine_pp_cost
		custom_effect_tooltip = africa_asia_seat_the_regional_centres_tt
		complete_effect = { africa_asia_seat_regional_centres = yes }
		ai_will_do = { base = constant:africa_world_order.ai_normal modifier = { factor = 2 check_variable = { africa_asia_inland_centre < constant:africa_measure.low } } }
	}

	africa_asia_coordinate_food_river_and_monsoon_security = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_asia_package has_country_flag = africa_asia_regional_congress_system_open }
		available = { has_country_flag = africa_world_asia_package has_country_flag = africa_asia_regional_congress_system_open NOT = { has_country_flag = africa_asia_food_monsoon_security_action } }
		cost = constant:africa_world_package_protocol.negotiated_pp_cost
		custom_effect_tooltip = africa_asia_coordinate_food_river_and_monsoon_security_tt
		complete_effect = { africa_asia_coordinate_food_river_monsoon_security = yes }
		ai_will_do = { base = constant:africa_world_order.ai_normal modifier = { factor = 2 check_variable = { africa_asia_food_and_river_security < constant:africa_measure.medium } } }
	}

	africa_asia_open_rail_and_maritime_corridors = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_asia_package has_country_flag = africa_asia_regional_congress_system_open }
		available = { has_country_flag = africa_world_asia_package has_country_flag = africa_asia_regional_congress_system_open NOT = { has_country_flag = africa_asia_rail_maritime_action } }
		cost = constant:africa_world_package_protocol.negotiated_pp_cost
		custom_effect_tooltip = africa_asia_open_rail_and_maritime_corridors_tt
		complete_effect = { africa_asia_open_rail_maritime_corridors = yes }
		ai_will_do = { base = constant:africa_world_order.ai_normal modifier = { factor = 2 check_variable = { africa_asia_corridor_coordination < constant:africa_measure.medium } } }
	}

	africa_north_america_negotiate_caribbean_and_central_membership = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_north_america_package has_country_flag = africa_north_america_continental_bargain_open }
		available = { has_country_flag = africa_world_north_america_package has_country_flag = africa_north_america_continental_bargain_open NOT = { has_country_flag = africa_north_america_caribbean_membership_negotiated } }
		cost = constant:africa_world_package_protocol.negotiated_pp_cost
		custom_effect_tooltip = africa_north_america_negotiate_caribbean_and_central_membership_tt
		complete_effect = { africa_north_america_negotiate_caribbean_central_membership = yes }
		ai_will_do = { base = constant:africa_world_order.ai_normal modifier = { factor = 2 check_variable = { africa_north_america_caribbean_inclusion < constant:africa_measure.medium } } }
	}

	africa_north_america_settle_indigenous_land_and_representation = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_north_america_package has_country_flag = africa_north_america_continental_bargain_open }
		available = { has_country_flag = africa_world_north_america_package has_country_flag = africa_north_america_continental_bargain_open NOT = { has_country_flag = africa_north_america_indigenous_settlement_negotiated } }
		cost = constant:africa_world_package_protocol.negotiated_pp_cost
		custom_effect_tooltip = africa_north_america_settle_indigenous_land_and_representation_tt
		complete_effect = { africa_north_america_settle_indigenous_land_representation = yes }
		ai_will_do = { base = constant:africa_world_order.ai_normal modifier = { factor = 2 check_variable = { africa_north_america_indigenous_settlement < constant:africa_measure.medium } } }
	}

	africa_north_america_balance_industry_mobility_and_command = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_north_america_package has_country_flag = africa_north_america_continental_bargain_open }
		available = { has_country_flag = africa_world_north_america_package has_country_flag = africa_north_america_continental_bargain_open NOT = { has_country_flag = africa_north_america_industry_mobility_command_balanced } }
		cost = constant:africa_world_package_protocol.intervention_pp_cost
		custom_effect_tooltip = africa_north_america_balance_industry_mobility_and_command_tt
		complete_effect = { africa_north_america_balance_industry_mobility_command = yes }
		ai_will_do = { base = constant:africa_world_order.ai_normal modifier = { factor = 2 check_variable = { africa_north_america_industrial_balance < constant:africa_measure.medium } } }
	}
```

## Constants required from the parent

No shared constants were edited in this subtask. The parent already owns `africa_world_package_protocol`, `africa_world_package_phase`, and `africa_world_package_crisis_result`. Add the W2 decision-cost and timing fields below to the existing protocol category. Values are tuning proposals and should be reconciled with the parent table before merge:

```text
africa_world_package_protocol = {
	schema = {
		any_key = yes
		data = fixed_point
	}
	routine_pp_cost = 25
	negotiated_pp_cost = 35
	intervention_pp_cost = 50
	crisis_response_pp_cost = 35
	ratification_days = 70
	lifecycle_review_days = 45
}
```

The event and helper files use the already-present parent-owned result category:

```text
africa_world_package_crisis_result = {
	schema = {
		any_key = yes
		data = int
	}
	none = 0
	success = 1
	compromise = 2
	failure = 3
}
```

If W1 places the result constants in another category, update only the four `constant:` references in this event/effect package and keep the variable name unchanged.

## Trigger integration contracts

The parent has added `africa_world_package_ratification_is_proven` and the package-specific North America balance trigger. Reconcile the shared trigger's package flags with the local proof flags below before the final load. The local focus files call the shared aggregate directly.

```text
africa_asia_centers_of_asia_is_balanced = {
	custom_trigger_tooltip = {
		tooltip = africa_asia_centers_of_asia_is_balanced_tt
		check_variable = { africa_asia_eastern_centre > constant:africa_measure.low }
	}
	check_variable = { africa_asia_southern_centre > constant:africa_measure.low }
	check_variable = { africa_asia_inland_centre > constant:africa_measure.low }
	check_variable = { africa_asia_archipelago_centre > constant:africa_measure.low }
	check_variable = { africa_asia_food_and_river_security > constant:africa_measure.low }
	check_variable = { africa_asia_corridor_coordination > constant:africa_measure.low }
}
```

`africa_world_package_ratification_is_proven` should be a country-scope aggregate trigger that requires `africa_world_package_is_installed`, `africa_world_package_heartland_is_proven`, `africa_world_package_constituent_settlement_is_proven`, the package's withdrawal law, a successful or compromise founding result, the relevant shared-lane proof, the relevant lifecycle crisis resolved flag, and a route-specific balance trigger. It must reject a pending constituent settlement and must not require or set an implementation-readiness flag. The two local proof effects set their package proof flags only after this trigger returns true.

For North America, reuse the existing `africa_north_america_continental_bargain_is_balanced` trigger. Extend it in the parent trigger aggregate with the four W2 lane proof flags and the voluntary diaspora flags. Do not add any population relocation condition.

## Focus call-site migration

- Asia preserves both same-block OR prerequisite sets for food and rail. The old direct gains were moved into the package-local helpers so each lane records proof once. Defence and Indian Ocean calls now use the package-local helpers. The capstone requires the parent proof trigger plus heartland and constituent proof and calls the local proof effect before final identity.
- North America preserves the shared resources prerequisite OR block and all separate industrial/citizenship prerequisites. Existing world-order helpers remain first in each completion reward, followed by the W2 extension. The diaspora extension explicitly repeats the voluntary and local-acceptance flags as a guardrail. The capstone requires the parent proof trigger and local founding/shared/lifecycle proof flags.
- The Asia helpers also set the generic shared-trigger flags `africa_asia_food_river_board_ratified`, `africa_asia_corridor_settlement_ratified`, and `africa_asia_indian_ocean_partnership_ratified`. The North America defence extension sets `africa_north_america_two_ocean_defence_ratified`, so the existing aggregate route and shared-lane triggers can recognise these lanes without a shared-trigger rewrite.
- No route is activated by these edits. The existing Celestial Covenant and Storm Frontier Compact branches retain their high-chaos gates.

## Validation evidence

Task-specific checks run after the edits:

- Confirmed the new event IDs are unique in the repository and limited to `africa_world_package.300-.306` and `.400-.406`.
- Confirmed the Asia and North America shared-lane prerequisite blocks remain same-block OR blocks and the North America industrial/citizenship prerequisite blocks remain separate AND blocks.
- Confirmed the localisation file starts with UTF-8 BOM and that every event/decision key referenced by the new files is present.
- Confirmed no new `on_daily`, `on_weekly`, or `on_monthly` action and no `<=` or `>=` operator was introduced.
- Read-only MCP inspection completed with workspace `mod_chaos_redux_ea3b2d67c2c0`. The Asia focus inspection returned `FOCUS_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53ebcbc08a8d9ed2917231e0116b732b96e6190212a2f12a66a7b97be27b9c59/91d8dcebef9206ac4a5b5fc8357ef33e860e7e3085caa96393fc5d4e364d61df/focus-inspect.b313cacb5d1bed89.json`. The North America focus inspection returned `FOCUS_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10a1ea71bb557536e18249f279657577a8b9555272bea0ec318e91e6f5ea62d4/8e9f7cab404d530f38a8fa9f9a4d5ddac8f28dbfa93cc605d5765a5a36596fe0/focus-inspect.32b4dabf9abaffe4.json`. The event lint inspection returned `EVENT_INSPECTED_PARTIAL` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3856848120fdc82952153174ff9a3b9fc23667b14d434a3c820b197322d813c/afa25f032a51c94e9a29e6d7372da898dbde76c6861bce7749df5e2013d5174b/event-lint-0e5872be0df1528cc8e567ef1f217dd6bacaee1de6fb61be4269c86809b826d4`. The event report was workspace-wide and deferred helper projections. Its bounded diagnostics were dominated by unrelated vanilla continuous-focus icon references, with no blocking diagnostic for the new package event IDs in the returned summary. Repository inspection and offline wiki/vanilla documentation remain the source evidence for these call sites.

## Known limitations and follow-up

- The parent must add the six W2 decision-cost/timing fields to the existing protocol constant category and reconcile the shared proof trigger with the local package proof flags before the final load. This is an explicit integration dependency, not a local fallback.
- The parent decision category still needs the six blocks above. They were intentionally not written in the shared decisions file.
- The parent should reconcile result-constant category placement with W1 and run the final package-level weighted logic and focus render checks.
- No simplification or fallback was used. The high-chaos routes remain deferred, as required, and voluntary diaspora mechanics do not force relocation.
