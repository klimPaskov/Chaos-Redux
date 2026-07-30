# W2 Crossroads and Europe scripted-system handoff

## Scope and ownership

This handoff covers the non-model Middle East Crossroads and Europe Continental Settlement loops requested by the W2 addendum. It does not edit the shared world-order effects, constants, scripted triggers, decisions file, or implementation-readiness flags. The parent remains responsible for integrating the six decision blocks below and for reviewing the shared trigger implementation.

## Files changed

- `common/national_focus/012_africa_world_middle_east_focus.txt`
- `common/national_focus/012_africa_world_europe_focus.txt`
- `common/scripted_effects/012_africa_world_crossroads_europe_effects.txt`
- `events/012_africa_world_package_crossroads_europe.txt`
- `localisation/english/012_africa_world_crossroads_europe_l_english.yml`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_world_w2_crossroads_europe_2026-07-30.md`

The localisation file was written with a UTF-8 BOM. Existing icon registrations and focus coordinates were preserved.

## Helper map

All helpers use COUNTRY scope on the installed package actor.

| Helper | Inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `africa_crossroads_open_congress` | Crossroads root focus | Opens the mandate-exit board, sets the founding crisis pending flag and phase, fires `.100` | Middle East root focus |
| `africa_crossroads_begin_mandate_exit_board` | Named decision | Opens the mandate-exit board and fires `.100` | Decision block below |
| `africa_crossroads_begin_water_pipeline_board` | Named decision | Opens water, food, and pipeline board and fires `.100` | Decision block below |
| `africa_crossroads_begin_protected_routes_board` | Named decision | Opens protected-routes and holy-sites board and fires `.100` | Decision block below |
| `africa_crossroads_apply_command_settlement` | Desert and mountain command focus | Route-sensitive Anatolian, Persian, Arab, minority, water, or oil adjustment, proof flag, lane-pending flag, `.105` | Middle East shared focus |
| `africa_crossroads_apply_red_sea_nile_treaty` | Red Sea and Nile focus | Route-sensitive water, oil, port, pipeline, or holy-site adjustment, proof flag, lane-pending flag, `.105` | Middle East shared focus |
| `africa_crossroads_apply_withdrawal_guarantees_law` | Withdrawal focus | Sets union withdrawal proof and consent, route-specific guarantee adjustment, lane-pending flag, `.105` | Middle East shared focus |
| `africa_crossroads_apply_settlement_congress` | Crossroads settlement congress focus | Sets constitution and settlement-congress proof, phase, route-independent legitimacy/minority adjustment, `.105` | Middle East congress focus |
| `africa_crossroads_resolve_shared_lane_success` / `..._compromise` | `.105` option | Clears lane context and records full or transitional ratification with distinct authority, legitimacy, stability, and holy-site effects | Crossroads `.105` |
| `africa_crossroads_resolve_founding_success` / `..._compromise` / `..._failure` | `.102-.104` | Writes package crisis result, removes founding problem only for success or compromise, or opens lifecycle crisis after failure | Crossroads `.102-.104` |
| `africa_crossroads_resolve_lifecycle_success` / `..._compromise` / `..._prolong_lifecycle_crisis` | `.106` option | Resolves failure with distinct repair or compromise, or leaves the lifecycle crisis open with additional losses | Crossroads `.106` |
| `africa_europe_open_congress` | Europe root focus | Opens border-arbitration board, sets founding crisis pending and phase, fires `.200` | Europe root focus |
| `africa_europe_begin_border_arbitration_board` | Named decision | Opens border and minority guarantee board and fires `.200` | Decision block below |
| `africa_europe_begin_reconstruction_access_board` | Named decision | Opens reconstruction and industrial access board and fires `.200` | Decision block below |
| `africa_europe_begin_colonial_debt_board` | Named decision | Opens colonial debt and external guarantees board and fires `.200` | Decision block below |
| `africa_europe_apply_common_defence_law` | Common army and air defence focus | Route-sensitive defence adjustment, common-defence proof, lane-pending flag, `.205` | Europe shared focus |
| `africa_europe_apply_withdrawal_crisis_law` | Withdrawal and crisis focus | Sets union withdrawal proof and consent, route-specific guarantee adjustment, lane-pending flag, `.205` | Europe shared focus |
| `africa_europe_apply_post_colonial_treaty` | Post-colonial treaty focus | Sets post-colonial proof and treaty-ready flag, route-sensitive debt/border adjustment, lane-pending flag, `.205` | Europe shared focus |
| `africa_europe_resolve_shared_lane_success` / `..._compromise` | `.205` option | Clears lane context and records full or transitional ratification with distinct authority, legitimacy, stability, industrial, war-memory, and sovereignty effects | Europe `.205` |
| `africa_europe_resolve_founding_success` / `..._compromise` / `..._failure` | `.202-.204` | Writes package crisis result, removes founding problem only for success or compromise, or opens lifecycle crisis after failure | Europe `.202-.204` |
| `africa_europe_resolve_lifecycle_success` / `..._compromise` / `..._prolong_lifecycle_crisis` | `.206` option | Resolves failure with distinct repair or compromise, or leaves the lifecycle crisis open with additional losses | Europe `.206` |

## Event chain and cleanup

Crossroads uses `africa_world_package.100-.106`; Europe uses `.200-.206` in the shared `africa_world_package` namespace. `.100` and `.200` are opening congress events. `.101` and `.201` expose variable-driven success, compromise, and failure choices. `.102/.103` and `.202/.203` apply successful or compromised founding outcomes. `.104` and `.204` keep the founding problem active and schedule the lifecycle review after a 35-day file-local delay. `.105` and `.205` record full or transitional shared-lane ratification. `.106` and `.206` offer full repair, compromise, or deferral.

The event outcome helpers clear action flags, pending outcome flags, lane-event flags, and lane-pending flags. Success and compromise remove `africa_world_middle_east_founding_problem` or `africa_world_europe_founding_problem`. Failure does not remove the idea. Lifecycle repair or compromise removes it later and changes `africa_world_package_crisis_result` to success or compromise so the parent-owned ratification trigger can become true. Deferral leaves the lifecycle flag open and schedules another review.

## Ready-to-integrate decision blocks

Insert these six blocks inside `africa_world_polity_actions_category` in `common/decisions/012_africa_decisions.txt`. They use the existing package category and the existing protocol cost constants. No new category is required.

```text
	# Crossroads named boards.
	africa_crossroads_convene_mandate_exit_board = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_middle_east_package has_country_flag = africa_world_package_polity_foundation_initialised }
		available = {
			africa_world_package_is_installed = yes
			NOT = { has_country_flag = africa_crossroads_founding_crisis_pending }
			NOT = { has_country_flag = africa_crossroads_lifecycle_crisis_pending }
			NOT = { has_country_flag = africa_crossroads_shared_lane_event_open }
			NOT = { has_country_flag = africa_world_package_sovereign_complete }
			political_power > constant:africa_world_package_protocol.counterterm_pp_cost
		}
		cost = constant:africa_world_package_protocol.counterterm_pp_cost
		complete_effect = { africa_crossroads_begin_mandate_exit_board = yes }
		ai_will_do = { base = constant:africa_world_order.ai_high }
	}

	africa_crossroads_allocate_water_food_and_pipeline_access = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_middle_east_package has_country_flag = africa_world_package_polity_foundation_initialised }
		available = {
			africa_world_package_is_installed = yes
			NOT = { has_country_flag = africa_crossroads_founding_crisis_pending }
			NOT = { has_country_flag = africa_crossroads_lifecycle_crisis_pending }
			NOT = { has_country_flag = africa_crossroads_shared_lane_event_open }
			NOT = { has_country_flag = africa_world_package_sovereign_complete }
			political_power > constant:africa_world_package_protocol.counterterm_pp_cost
		}
		cost = constant:africa_world_package_protocol.counterterm_pp_cost
		complete_effect = { africa_crossroads_begin_water_pipeline_board = yes }
		ai_will_do = { base = constant:africa_world_order.ai_normal }
	}

	africa_crossroads_ratify_protected_routes_and_holy_sites = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_middle_east_package has_country_flag = africa_world_package_polity_foundation_initialised }
		available = {
			africa_world_package_is_installed = yes
			NOT = { has_country_flag = africa_crossroads_founding_crisis_pending }
			NOT = { has_country_flag = africa_crossroads_lifecycle_crisis_pending }
			NOT = { has_country_flag = africa_crossroads_shared_lane_event_open }
			NOT = { has_country_flag = africa_world_package_sovereign_complete }
			political_power > constant:africa_world_package_protocol.withdrawal_safeguard_pp_cost
		}
		cost = constant:africa_world_package_protocol.withdrawal_safeguard_pp_cost
		complete_effect = { africa_crossroads_begin_protected_routes_board = yes }
		ai_will_do = { base = constant:africa_world_order.ai_high }
	}

	# Europe named boards.
	africa_europe_arbitrate_border_and_minority_guarantees = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_europe_package has_country_flag = africa_world_package_polity_foundation_initialised }
		available = {
			africa_world_package_is_installed = yes
			NOT = { has_country_flag = africa_europe_founding_crisis_pending }
			NOT = { has_country_flag = africa_europe_lifecycle_crisis_pending }
			NOT = { has_country_flag = africa_europe_shared_lane_event_open }
			NOT = { has_country_flag = africa_world_package_sovereign_complete }
			political_power > constant:africa_world_package_protocol.counterterm_pp_cost
		}
		cost = constant:africa_world_package_protocol.counterterm_pp_cost
		complete_effect = { africa_europe_begin_border_arbitration_board = yes }
		ai_will_do = { base = constant:africa_world_order.ai_high }
	}

	africa_europe_allocate_reconstruction_and_industrial_access = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_europe_package has_country_flag = africa_world_package_polity_foundation_initialised }
		available = {
			africa_world_package_is_installed = yes
			NOT = { has_country_flag = africa_europe_founding_crisis_pending }
			NOT = { has_country_flag = africa_europe_lifecycle_crisis_pending }
			NOT = { has_country_flag = africa_europe_shared_lane_event_open }
			NOT = { has_country_flag = africa_world_package_sovereign_complete }
			political_power > constant:africa_world_package_protocol.counterterm_pp_cost
		}
		cost = constant:africa_world_package_protocol.counterterm_pp_cost
		complete_effect = { africa_europe_begin_reconstruction_access_board = yes }
		ai_will_do = { base = constant:africa_world_order.ai_normal }
	}

	africa_europe_settle_colonial_debt_and_external_guarantees = {
		icon = GFX_decision_012_africa_charter_ledger
		visible = { has_country_flag = africa_world_europe_package has_country_flag = africa_world_package_polity_foundation_initialised }
		available = {
			africa_world_package_is_installed = yes
			NOT = { has_country_flag = africa_europe_founding_crisis_pending }
			NOT = { has_country_flag = africa_europe_lifecycle_crisis_pending }
			NOT = { has_country_flag = africa_europe_shared_lane_event_open }
			NOT = { has_country_flag = africa_world_package_sovereign_complete }
			political_power > constant:africa_world_package_protocol.withdrawal_safeguard_pp_cost
		}
		cost = constant:africa_world_package_protocol.withdrawal_safeguard_pp_cost
		complete_effect = { africa_europe_begin_colonial_debt_board = yes }
		ai_will_do = { base = constant:africa_world_order.ai_high }
	}
```

## Constants and triggers

The helper and event files use the already shared `africa_world_package_crisis_result.success`, `.compromise`, and `.failure` constants and the existing `africa_world_package_phase.constituent_bargaining`, `.route_committed`, `.ratification`, and `.shared_lanes` values. They use the existing package protocol costs and AI values, plus `africa_world_order.package_minor_loss = 5`, which must be present in the parent-owned constants category before load. The event duration fields use file-local `@crossroads_crisis_review_days = 35` and `@europe_crisis_review_days = 35` because duration fields are not consistently dynamic-constant safe. If the parent later centralizes this delay, add `crisis_review_days = 35` to `africa_world_package_protocol` and replace the two file-local values.

The capstones now call the parent-owned `africa_world_package_ratification_is_proven = yes` trigger in `available` while preserving their existing withdrawal and route-specific treaty or constitution flags. They also remain unavailable while the package-specific shared-lane event is open, so proof cannot be consumed before the ratification choice is recorded. This trigger must remain the full proof gate for heartland, grounded route, resolved crisis, shared lanes, withdrawal law, constituent protocol, and package metrics.

## Validation and limitations

Task-specific validation performed after implementation: checked all helper and event identifiers with `rg`, checked that Crossroads IDs are `.100-.106` and Europe IDs are `.200-.206`, checked that each shared focus calls its exact helper, checked that each capstone keeps its pre-existing availability flags and adds the shared proof trigger, checked that Middle East and Europe prerequisite OR lists remain single same-block prerequisite clauses, and checked that the localisation file begins with a UTF-8 BOM. No game launch was performed.

The six decision blocks are intentionally not inserted into the shared decisions file in this subtask because that file is parent-owned. The shared constants and ratification trigger are likewise parent-owned. No fallback route, new country tag, new model, Event006 activation, or high-chaos readiness flag was added.
