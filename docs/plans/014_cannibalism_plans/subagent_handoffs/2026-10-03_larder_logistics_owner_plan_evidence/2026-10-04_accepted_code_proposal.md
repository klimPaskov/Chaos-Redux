# Accepted Larder tuning and static meta distance proposal

Disposition: accepted and queued under the parent's 2026-10-04 instruction.
This is an evidence-only source proposal and is not installed gameplay code.
The source freeze remains in force until the parent confirms auditor `01a10385` has captured the baseline and explicitly instructs application.
The accepted owner plan remains authoritative for transaction placement, dispatched/received accounting, post-annex finalization, autonomy exclusion and the separate generation guard.
No weight or reserve/bonus predicate is retuned.

## Accepted tuning fragment

Future location: the existing `common/script_constants/014_cannibalism_constants.txt`.

```txt
cannibalism_larder_logistics = {
	schema = {
		any_key = yes
		data = fixed_point
	}
	capacity_base = 1200
	capacity_per_controlled_state = 100
	capacity_per_development_point = 50
	distance_loss_divisor = 10000
	distance_loss_maximum = 0.60
	zero = 0
	one = 1
	minus_one = -1
}
```

The existing hard ceiling remains `constant:cannibalism_unification.global_larder_maximum`, equal to 5000.
The normal country cap remains `constant:cannibalism_consumption.larder_max`, equal to 2000.
Each contributing development flag adds the existing 5 score points, so the coefficient 50 continues to add 250 capacity per flag.
For one controlled state and zero score, `1200 + 100 = 1300` permits the unchanged inclusive reserve `800 + 400 = 1200` and the strict `Larder > 1200` bonus.
This replaces the former base-1000 proposal's one-state cap 1100.
A zero-state, zero-score host still has capacity 1200 and cannot earn the strict bonus.
Availability, actual store generation and other costs still require the auditor's declared scenarios.

## Capacity calculation body

Future location: `cannibalism_refresh_larder_effective_capacity` in the Event014 owner effects file.
Scope: country.
Output: the regular country `cannibalism_larder_effective_capacity` for normal-country and unified tooltip/data consumers.
Scratch temporaries remain private to this helper and do not escape, so they need no caller allocation.
This calculation never clamps stores, writes the global Larder mirror, changes a GUI field or calls a full operational-profile refresh.
The subsequent mutation finalizer handles stores and global publication at the accepted transaction boundaries.

```txt
cannibalism_refresh_larder_effective_capacity = {
	set_variable = { cannibalism_larder_effective_capacity = constant:cannibalism_consumption.larder_max }
	if = {
		limit = {
			OR = {
				is_cannibalism_unified_country = yes
				is_cannibalism_wendigo_hannibal_country = yes
			}
		}
		cannibalism_unified_refresh_contract_capacities = yes
		set_variable = { cannibalism_larder_effective_capacity = constant:cannibalism_larder_logistics.capacity_base }
		set_temp_variable = { cannibalism_larder_capacity_territory_work = num_of_controlled_states }
		multiply_temp_variable = { cannibalism_larder_capacity_territory_work = constant:cannibalism_larder_logistics.capacity_per_controlled_state }
		add_to_variable = { cannibalism_larder_effective_capacity = cannibalism_larder_capacity_territory_work }
		set_temp_variable = { cannibalism_larder_capacity_development_work = cannibalism_unified_larder_capacity }
		multiply_temp_variable = { cannibalism_larder_capacity_development_work = constant:cannibalism_larder_logistics.capacity_per_development_point }
		add_to_variable = { cannibalism_larder_effective_capacity = cannibalism_larder_capacity_development_work }
		clamp_variable = {
			var = cannibalism_larder_effective_capacity
			min = constant:cannibalism_larder_logistics.capacity_base
			max = constant:cannibalism_unification.global_larder_maximum
		}
	}
}
```

## Caller storage and frozen state capture

The actual constructor, later absorption owner or autonomy owner allocates these temporaries at its own frame entry, before either country scope and before any nested helper.
The distance sentinel prevents an unwritten meta output from being interpreted as a valid same-state zero distance.
The two capture proofs are transient inputs, not persistent numerical flags.

```txt
set_temp_variable = { cannibalism_larder_source_capital_captured = constant:cannibalism_larder_logistics.zero }
set_temp_variable = { cannibalism_larder_destination_capital_captured = constant:cannibalism_larder_logistics.zero }
set_temp_variable = { cannibalism_transfer_distance = constant:cannibalism_larder_logistics.minus_one }
set_temp_variable = { cannibalism_transfer_dispatch = constant:cannibalism_larder_logistics.zero }
set_temp_variable = { cannibalism_transfer_received = constant:cannibalism_larder_logistics.zero }
set_temp_variable = { cannibalism_transfer_loss_fraction = constant:cannibalism_larder_logistics.zero }
set_temp_variable = { cannibalism_transfer_retention = constant:cannibalism_larder_logistics.zero }
set_temp_variable = { cannibalism_transfer_result = constant:cannibalism_larder_logistics.zero }

# The owner binds both regular country targets explicitly before this block.
# Enter only the validated actual countries for later absorption and autonomy.
event_target:cannibalism_larder_source_country = {
	capital_scope = {
		save_event_target_as = cannibalism_larder_source_capital
		set_temp_variable = { cannibalism_larder_source_capital_captured = constant:cannibalism_larder_logistics.one }
	}
}
event_target:cannibalism_larder_destination_country = {
	capital_scope = {
		save_event_target_as = cannibalism_larder_destination_capital
		set_temp_variable = { cannibalism_larder_destination_capital_captured = constant:cannibalism_larder_logistics.one }
	}
}
```

Initial CBL uses its existing explicit selected-host capital policy.
Capture the source capital and bind both capital targets to that actual selected-host state before the capital owner/controller transfer, since current source explicitly installs this same state as CBL's capital.
This is the constructor's documented planned destination anchor and yields true same-state zero distance before CBL's creation.
Do not try to scope an uncreated CBL's current capital or use a generic invalid-capital fallback.
Bind the destination country as the explicit CBL transaction recipient and retain the existing constructor's native recipient validity checks before any transfer commit.
Initial transformed Wendigo captures its actual in-place destination capital and the primary donor's actual capital before identity change.
The both-human branch skips donor quote/debit/credit and retains the zero donor snapshot.
Every path must repeat capture with fresh zeroed proofs before reuse, because regular targets cannot be manually cleared and may remain in the same effect chain.

## Quote helper and exact static meta expansion

Future scope: actual donor country, entered explicitly by the transaction owner.
The owner validates country identity/generation and transaction eligibility through its existing constructor or post-reveal guard before invoking the quote.
For post-reveal transfers the separate accepted host-generation guard must pass before debit, credit, autonomy, annexation or slot retirement.
The quote only reads state distance and donor stores, and writes the six preallocated temporary outputs.
Input `cannibalism_transfer_route_fraction` contains the existing route fraction with its existing preparation/relief modifier applied before distance.
Missing capital targets, absent native capture proof or an unwritten/negative distance reject the quote and mutate no stores.
Quote success does not authorize an annex or payment by itself.
The transaction owner still requires migration success and its own valid explicit recipient before committing anything.

```txt
cannibalism_prepare_larder_transfer_quote = {
	set_temp_variable = { cannibalism_transfer_distance = constant:cannibalism_larder_logistics.minus_one }
	set_temp_variable = { cannibalism_transfer_dispatch = constant:cannibalism_larder_logistics.zero }
	set_temp_variable = { cannibalism_transfer_received = constant:cannibalism_larder_logistics.zero }
	set_temp_variable = { cannibalism_transfer_loss_fraction = constant:cannibalism_larder_logistics.zero }
	set_temp_variable = { cannibalism_transfer_retention = constant:cannibalism_larder_logistics.zero }
	set_temp_variable = { cannibalism_transfer_result = constant:cannibalism_larder_logistics.zero }
	if = {
		limit = {
			has_event_target = cannibalism_larder_source_capital
			has_event_target = cannibalism_larder_destination_capital
			check_variable = { var = cannibalism_larder_source_capital_captured value = constant:cannibalism_larder_logistics.one compare = equals }
			check_variable = { var = cannibalism_larder_destination_capital_captured value = constant:cannibalism_larder_logistics.one compare = equals }
		}
		meta_effect = {
			text = {
				[SOURCE] = {
					set_temp_variable = { cannibalism_transfer_distance = distance_to@[DESTINATION] }
				}
			}
			SOURCE = "[cannibalism_larder_source_capital.GetID]"
			DESTINATION = "[cannibalism_larder_destination_capital.GetID]"
		}
		if = {
			limit = {
				check_variable = {
					var = cannibalism_transfer_distance
					value = constant:cannibalism_larder_logistics.zero
					compare = greater_than_or_equals
				}
			}
			set_temp_variable = { cannibalism_transfer_fraction_work = cannibalism_transfer_route_fraction }
			clamp_temp_variable = { var = cannibalism_transfer_fraction_work min = constant:cannibalism_larder_logistics.zero max = constant:cannibalism_larder_logistics.one }
			set_temp_variable = { cannibalism_transfer_dispatch = cannibalism_larder }
			clamp_temp_variable = { var = cannibalism_transfer_dispatch min = constant:cannibalism_larder_logistics.zero }
			multiply_temp_variable = { cannibalism_transfer_dispatch = cannibalism_transfer_fraction_work }
			set_temp_variable = { cannibalism_transfer_loss_fraction = cannibalism_transfer_distance }
			divide_temp_variable = { cannibalism_transfer_loss_fraction = constant:cannibalism_larder_logistics.distance_loss_divisor }
			clamp_temp_variable = { var = cannibalism_transfer_loss_fraction min = constant:cannibalism_larder_logistics.zero max = constant:cannibalism_larder_logistics.distance_loss_maximum }
			set_temp_variable = { cannibalism_transfer_retention = constant:cannibalism_larder_logistics.one }
			subtract_from_temp_variable = { cannibalism_transfer_retention = cannibalism_transfer_loss_fraction }
			set_temp_variable = { cannibalism_transfer_received = cannibalism_transfer_dispatch }
			multiply_temp_variable = { cannibalism_transfer_received = cannibalism_transfer_retention }
			set_temp_variable = { cannibalism_transfer_result = constant:cannibalism_larder_logistics.one }
		}
	}
	set_temp_variable = { cannibalism_larder_source_capital_captured = constant:cannibalism_larder_logistics.zero }
	set_temp_variable = { cannibalism_larder_destination_capital_captured = constant:cannibalism_larder_logistics.zero }
	set_temp_variable = { cannibalism_transfer_route_fraction = constant:cannibalism_larder_logistics.zero }
}
```

For frozen source state 123 and destination state 124 the meta body becomes exactly:

```txt
123 = {
	set_temp_variable = { cannibalism_transfer_distance = distance_to@124 }
}
```

For one actual frozen state used at both endpoints, the generated expression is a valid state-to-itself read, not an assumed zero.
No `distance_to@var:...`, `ROOT.capital`, internal `state.id` formatting or global capital target appears in this proposal.
The `event_target:` prefix is present in script scopes and intentionally absent in the two localisation namespace parameters.
Do not add `debug = yes` or runtime log code while source is frozen.

## Commit boundaries and documentation after authorization

The quote's one-shot inputs are cleared after use while its caller-owned outputs remain available for the same transaction.
Later absorption and autonomy debit `cannibalism_transfer_dispatch` from the donor and credit only `cannibalism_transfer_received` to the recipient.
Opening identity inheritance uses the received value once in its existing assignment and does not invoke a second donor-credit path.
Post-annex finalization reads the recipient's actual controlled-state count and fresh contract score, then clamps/publishes once.
Autonomy finalization never adds the donor's land to capacity.
The owner plan's eight global-ceiling sites, mixed actor pulse and shared foreign-seed hook still require migration, and its warlord-only local clamps remain unchanged.
This code proposal does not implement those call sites or the separate generation guard, and the parent must not treat it as a complete source patch.
After application, document the private helper contracts and direct callers in the owner documentation and matching dynamic-helper index, then retain the mandatory auditor baseline/evaluate/sweep/compare evidence.

## Reference proof and remaining validation

Installed `documentation/loc_objects_documentation.md:629–647` declares state `GetID`.
Installed `documentation/effects_documentation.md:4833–4851` declares meta text construction and named parameter substitution into a scope.
Installed `documentation/dynamic_variables_documentation.md:1127–1129` gives `123.distance_to@124` as the exact literal-state primary expression.
Offline Effects `4617–4646` shows localisation namespace evaluation in meta parameter strings.
Offline Data structures `301` omits the `event_target:` prefix in localisation, `305` defines regular-target lifetime, `1671` distinguishes internal state pointer from public state ID and recommends GetID meta use, and `1681` declares the distance state target.
Offline Localisation `531–536` allows event-target namespaces and `626` defines state GetID with meta usage.
Existing Event006 `common/scripted_effects/006_independence_wave_decision_effects.txt:1065–1075` uses exactly a saved state target's `.GetID` as a meta parameter.
Vanilla operation state-scope distance reads remain the primary gameplay calculation precedents retained in the owner plan.
The primary namespace and meta parameter components are established for this planned implementation choice.
No supported-component syntax blocker remains identified, and this is not runtime execution proof.
`hoi4.script_validate` remains absent, the complete probability baseline/fixture has not been supplied, and no gameplay code is applied or engine test claimed.
No simplification, zero-distance fallback, new route or AI retune is introduced.
