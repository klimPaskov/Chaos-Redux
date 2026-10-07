# Riches Found physical cost contract

This document covers the ten physical-cost profiles and ordinary deep-section output loss implemented on 2026-10-07.
The acceptance basis is the human Event 029 goal and Part 3's named cost profiles, not an approval of fixed prices as the full dynamic-cost system.
The complete Event 029 package remains incomplete.

## Payment and capacity

The action's shared affordability trigger is used in both `available` and `custom_cost_trigger`.
The same resource-specific predicates colour the displayed costs.
Discrete resources are paid by the country taking the decision.
If its delayed result loses the valid mine, the original payer receives exactly the discrete resources that this profile charged.
Two civilian factories are committed through the native decision `civilian_factory_use` modifier for `days_remove`, not removed or refunded as buildings.
Inline cost rows show no more than three values, while full tooltips disclose every cost.

| Action | Upfront discrete payment | Capacity and output commitment |
| --- | --- | --- |
| Survey | 100 manpower, 25 trucks | Two civilian factories for 30 days |
| Claim Register | 10 political power, 300 manpower | Two civilian factories for 30 days |
| Reserve Deposit | 25 political power, 100 manpower, 25 support equipment | Two civilian factories for 30 days |
| Camp Administration | 300 manpower, 25 support equipment | Two civilian factories for 60 days |
| Drive Deeper | 300 manpower, 150 support equipment | Two civilian factories for 90 days, 25 percent temporary output loss |
| Seal Depths | 300 manpower, 150 support equipment | Two civilian factories for 60 days, permanent loss of a quarter of ordinary output potential |
| Nationalize With Compensation | 40 political power | Two civilian factories for 90 days |
| Buyout | 40 political power | Two civilian factories for 90 days |
| Repair | 75 trucks, 75 support equipment | Two civilian factories for 90 days |
| Permanent Seal | 600 manpower, 150 support equipment | Two civilian factories for 90 days, permanent end of mine output |

Amounts and durations come from `029_riches_found_constants.txt`.
The file-local two-factory alias in the decision file mirrors the shared capacity constant because the native modifier uses a static value.
Every row stays within four cost types, including foregone output where applicable.
Repair can consume the mine's one-use stabilization reserve and return the same trucks and support equipment paid upfront.
That reserve pays only while the deciding country owns the mine.
That reserve does not release the native factory commitment early.
Compensated nationalization and buyout retain their existing partner compensation and settled-opinion outcomes.
Nationalization adds eight foreign claim pressure and buyout removes eight, as disclosed by their effect tooltips.

## Sealed deposit capacity

Ordinary Seal Depths retains the persistent state flag `riches_found_depths_sealed` and lowers development, extraction pressure and deep excavation through its existing result.
`riches_found_refresh_mine_contribution` applies `riches_found_exposure.sealed_depth_output_factor` after the ordinary contribution ceiling and before deriving all controller components.
The retained fraction is 0.75.
Drive Deeper's temporary output commitment also runs after the ordinary ceiling, so an over-ceiling raw calculation cannot conceal its quarter-share commitment.
Rebuilding the score from state inputs on each refresh prevents an exponential loss from repeated refreshes.
The state flag survives ordinary closure, restoration and controller changes, so those operations do not recover the sealed capacity.
The more restrictive `riches_found_mine_partial_seal` and bound-account conditions keep their existing operating factors without also paying this ordinary reduction.
This does not validate every severe partial-seal or account output path.

## Files and presentation

Gameplay consumers are `common/decisions/029_riches_found_decisions.txt`, `common/scripted_triggers/029_riches_found_cost_triggers.txt`, `common/scripted_effects/029_riches_found_effects.txt` and `common/script_constants/029_riches_found_constants.txt`.
Player-facing costs and consequences are in `localisation/english/029_riches_found_decisions_l_english.yml`.
This tranche uses the existing category, action sprites and texticons in `interface/029_riches_found.gfx` and `interface/chaosx_texticons.gfx`.
No new visual asset or dedicated GUI is required by this cost repair.
The complete asset-family audit is a separate acceptance requirement.

## Evidence and limits

The read-only `physical_cost_audit_2026_10_07.md` crosschecks all ten debits, invalid-result refunds, shared gates and native commitment values.
Its identified repair and compensated-exit wording gaps are corrected in the owning localisation.
The prior seal-output gap is corrected in source, not only described by a tooltip.
The localisation audit also identified missing mission-start text, ambiguous native factory durations, a missing reserve ownership condition and a pre-ceiling deep-project multiplier.
Those findings are corrected in the owning source and localisation.
Source arithmetic checks cover raw contribution 0, 20, 100 and 140 against the ordinary ceiling of 100, yielding sealed values 0, 15, 75 and 75.
Repeating that derived calculation or changing the controller leaves those values unchanged.
These are bounded source checks, not observations from HOI4.

Native precedent: installed `common/decisions/AST.txt`, `AST_union_strike`, lines 2-42 uses a timed `civilian_factory_use` modifier.
Installed `documentation/modifiers_documentation.md:2202-2206`, revision `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`, documents the factory commitment.
Offline `Modifiers - Hearts of Iron 4 Wiki.md:686`, revision `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f`, describes the flat civilian-factory use.
Offline `Decision modding - Hearts of Iron 4 Wiki.md:339-356`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, documents the timer, active modifier and delayed removal.
Installed `common/decisions/_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, documents decision and target scopes.
The whole-decision MCP validator returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, with 723 unchecked argument blocks and 96 unknown scope roots.
That result is not engine or parameter validation.
One-below, exact and one-above native factory availability, stale clicks, cancellation timing and actor callback identity remain runtime-evidence gaps.
No agent launched HOI4.

## Remaining work and future integration

The tier prices above are anchors, not the full required population, damage, distance, wartime, supply, disorder, concession-exposure and prior-failure scaling.
Transport-family helpers exist as a separate unintegrated module, with callback-generation identity and native reservation atomicity unresolved.
Physical processing, housing, funded diversification and contract construction results still need full spec integration and map/route evidence.
The category's surviving-contract and aftermath lifecycle remains incomplete.
The named probability comparison and full event acceptance matrix remain required before package completion.
Future extension should integrate those accepted systems with one exact quote and paid receipt, not introduce replacement currencies, whole-world pulses or resource-type fallbacks.
