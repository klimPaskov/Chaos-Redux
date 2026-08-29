# Destination Selection Architect Handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-24

Owner route: `chaosx_scripted_system_architect`, isolated with no inherited parent-thread context.

## Parent disposition

Accepted with parent modifications.

The architect's centralized pool identifiers, candidate trigger split, two-pass weighted draw, and internal-first wrapper were retained. The parent completed the interrupted effects file, replaced all seven flat `random_neighbor_state` consumers, and tightened the proposal after review by adding origin and destination infrastructure proof, stable control, camp exclusions, state reception-load pressure, Air Cleanliness and fallout pressure, route-damage scoring, reserve production and transport pressure, selector-owned route proofs, and a real timed reserve-requisition protection created by successful reserve release.

No suggested global scan, fallback candidate, event registration, or event-pacing pulse was accepted.

## Changed files

- `common/script_constants/famine_migration_destination_selection_constants.txt`
- `common/scripted_triggers/famine_migration_destination_selection_triggers.txt`
- `common/scripted_effects/famine_migration_destination_selection_effects.txt`
- `common/decisions/famine_migration_decisions.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`

## Implemented identifiers

- Pools: `internal_safe_route`, `foreign_safe_evacuation`, `foreign_transit`, `third_country_resettlement`, and `safe_food_reserve_donor`.
- Public wrappers: `famine_migration_select_general_safe_evacuation_destination`, `famine_migration_select_internal_safe_route_destination`, `famine_migration_select_foreign_transit_destination`, `famine_migration_select_third_country_resettlement_destination`, and `famine_migration_select_safe_food_reserve_donor`.
- Shared internals: `famine_migration_destination_selection_candidate_is_valid`, `famine_migration_destination_selection_calculate_candidate_weight`, and `famine_migration_destination_selection_run_weighted_pool`.
- Timed protection: `famine_migration_food_reserve_requisition_protected` for the centralized `reserve_requisition_protection_days` duration after a successful reserve release.

## Consumer disposition

The seven former uniform selections now route as follows:

| Consumer | Selector |
| --- | --- |
| `fm_famine_evacuation` | internal-first safe evacuation |
| `fm_evacuate_vulnerable` | internal-first safe evacuation |
| `fm_evacuate_workers` | internal-first safe evacuation |
| `fm_requisition_safer_state` | safe reserve donor |
| `fm_distribute_arrivals` | internal safe route |
| `fm_transit_only` | foreign transit |
| `fm_third_country_resettlement` | third-country resettlement |

## Selection and route proof

Each pool enumerates the complete directly adjacent state set twice with the same fail-closed trigger. The first pass sums only positive valid weights. The second pass consumes one uniform draw over that total and binds the first candidate crossing the draw. A zero total binds nothing.

Adjacency is physical route geometry supplied by `every_neighbor_state`; both origin and destination must have positive infrastructure. Internal candidates must be owned and controlled by `ROOT`. Foreign candidates must be controlled by their valid owner, have admissible border policy, reception headroom, and a controller not at war with `ROOT`. Direct famine, camps, persecution, bombing, trapped population, unsafe-route evidence, severe outbreak, chemical contamination, nuclear fallout, and forced-return policy exclude the candidate before weighting.

Successful migration selection is the owner of border, transport, safety, actor, destination-food, and destination-reception proof. The exact population transfer remains a separate consumer and performs the debit, route-death, survivor-credit, and conservation transaction.

## Weight model

All tuning is in the destination-selection script-constant file. Additive terms cover pool base, intact route, damaged-route penalty, country capacity headroom, state reception load, donor reserves, border posture, opinion, alliance, faction, subject, access, guarantee, bounded ideology affinity, and current food, flight, fallout, Air Cleanliness, production, and transport pressure. The final score is clamped from zero to the centralized maximum.

Ideology can only add six points to an otherwise valid candidate. It cannot admit a candidate excluded for persecution, camps, famine, bombing, war, contamination, unsafe route, exhausted capacity, or forced-return policy.

## Validation and open evidence

Source review found no remaining `random_neighbor_state` in `common/decisions/famine_migration_decisions.txt`, and all four changed Clausewitz files have balanced braces. The mandatory post-change probability inspection, named scenario evaluation, sweep, comparison, and rendered evidence remain owned by the final read-only probability auditor and are not claimed by this implementation handoff.

The map MCP route is not reclassified by this handoff. Its most recent narrow call remains blocked by `ARTIFACT_STORAGE_LIMIT: Artifact batch cannot fit after reclaiming expired artifacts`; earlier successful map evidence is retained in `docs/plans/famine_and_migration_system_plans/mapmode_validation.md`.
