# Corridor Route-Proof Patch Handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Status: bounded scripted-system patch complete in the corridor-owned source and documentation surfaces. No commit was created. Concurrent edits outside the owned files were preserved.

## Changed files and identifiers

- `common/scripted_triggers/famine_migration_corridor_triggers.txt`.
  - Normalized all 20 malformed hybrid `check_variable` comparisons to the explicit `var`, `value`, and `compare` form required by the vanilla trigger documentation.
  - Added `famine_migration_corridor_front_destination_is_safe` as the affirmative current destination gate.
  - Extended `famine_migration_corridor_front_state_is_valid` with current origin ownership, exact front ownership/control, stored relation revalidation, capacity revision/headroom, native rail/bombing checks, and supported persecution, active-camp, contamination, fallout, outbreak, zombie, and natural-disaster warning/chain exclusions.
  - Extended route geometry and offer predicates with positive cohort, route-generation, and proof-generation identity, requiring proof generation to equal route generation.
  - Extended the country offer predicate with mirrored operation, cohort, and route-generation identity checks.
  - Kept enemy-front relations available only as the explicit war relation; accepted operation still requires positive ceasefire proof through the route geometry predicate.
- `common/scripted_effects/famine_migration_corridor_effects.txt`.
  - Replaced the preparation-time orphan route-unsafe read with the owned affirmative destination-safety trigger.
  - Made preparation's transport proof require the established named minimum infrastructure threshold and the live transport-component field on both exact adjacent endpoints.
  - Mirrored `famine_migration_corridor_offer_route_generation` when submitting an offer and cleared it on acceptance, rejection, and terminal cleanup.
  - Left the exact movement primitive, organized-evacuation role request, replay receipt, achievement gates, reserve path, route-death output, and cleanup behavior intact.
- `common/scripted_effects/famine_migration_corridor_effects.md`.
  - Documented the destination safety gate, current native producer semantics, host-capacity requirement, identity mirror, and the distinction between safety refresh and attack-receipt ownership.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/corridor_route_proof_patch.md`.
  - This handoff.

No decisions, main famine effects/triggers, mapmodes, localisation, assets, workbook, or probability-bearing surface was edited.

## Before and after contract

Before the patch, preparation and both route predicates read an orphan route-unsafe marker whose producer/refresh/clear contract was not owned by the corridor. Twenty trigger comparisons used the malformed hybrid syntax `var = name > value`; the effect file's five corresponding hybrids had already been normalized by concurrent shared-worktree edits before this patch was applied. The stored counterpart mirror did not carry a route-generation identity, and the route validator did not re-prove current ownership, destination capacity, or the supported destination hazard channels.

After the patch, absence of the orphan marker is irrelevant. An exact corridor offer or operation requires the persisted origin and adjacent front, current origin owner/controller, current counterpart owner/controller, the stored relation, positive transport and border proof, both endpoints above the established named infrastructure threshold with live transport-component fields, current destination capacity with spare headroom, native rail and bombing clearance, and clear supported destination hazard channels including unresolved natural-disaster chains. Accepted operation additionally requires positive safety and ceasefire proof, positive food/reception proof for the selected operation, positive cohort and route-generation identity, and equality between route and proof generations. Enemy-front war remains a permitted relation only when the accepted ceasefire proof is present; non-enemy relations retain their current non-war/faction requirements.

The existing terminal reason enum for an unsafe route remains part of expiry/rejection reporting; it is a reason value, not a route-safety flag or affirmative evidence source.

The route is still bounded to the exact stored adjacent state. No remote state, arbitrary country, sea geometry, air geometry, weighted destination, whole-world scan, event ID, event pool, or GUI was introduced.

## Conservation and replay implications

The patch changes validation and identity only. `famine_migration_execute_corridor_evacuation` still sets the organized-evacuation transfer role immediately before the one call to `famine_migration_transfer_civilians_exact` at `common/scripted_effects/famine_migration_corridor_effects.txt:536-537` in the current source. No population or reserve effect was added to preparation, offer, acceptance, safety validation, rejection, expiry, or cleanup.

The exact transfer remains the only population mutation. Its measured origin debit is the only trapped-population decrement; its route-death output remains separate from survivor credit; only positive measured survivors are bound to the exact destination and reception ledger. The durable `famine_migration_corridor_evacuation_proven` receipt, route generation, cohort destination binding, mission proof, achievement crisis gate, and terminal cleanup remain in their existing owner paths. The new offer-generation mirror prevents accepting a stale crisis or cohort under a reused country offer name.

## Source-based callsite and producer proof

- `famine_migration_corridor_offer_route_is_valid` is used by preparation and offer submission, and by acceptance through `famine_migration_corridor_acceptance_is_valid`.
- `famine_migration_corridor_route_geometry_is_valid` is used by operation validity; operation validity gates route binding, evacuation, relief, and mission validity.
- `famine_migration_corridor_front_state_is_valid` is reused by route geometry, offer validation, attack-receipt validation, sparse relation checks, and cleanup revalidation.
- The live native projection producer is `common/scripted_effects/chaosx_famine_migration_effects.txt:famine_migration_refresh_native_state_safety_projections` (currently around `:4711-4741`).
  - `famine_migration_route_damaged` is set when `damaged_building_level@rail_way` is above `constant:famine_migration_core_reconciliation.route_damage_threshold` and cleared when that condition is false.
  - `famine_migration_bombing_active` is set when `days_since_last_strategic_bombing` is below `constant:chaos_meter_deaths.strategic_bombing_days_recent` and cleared outside that window.
  - The producer is called before registered food/displacement state processing and for registered reception candidates through the sparse runtime registry, not by a new world scan. The corridor also checks the native current values at the exact front scope so it does not treat a stale sparse mirror as safety.
- Current destination capacity semantics are provided by `famine_migration_reception_capacity_is_valid` and its published revision/load fields. The corridor uses the same owner-country capacity contract as the established destination selector.
- The existing attack adapter remains receipt-driven. Ordinary land-combat and strategic-bombing callbacks with exact corridor origin/front/attacker identity are not available in the current source surface, so no attacker is inferred from war, control, bombing recency, damage, or death totals.

## Validation performed

- Owned route-unsafe census across `famine_migration_corridor_effects.txt`, `famine_migration_corridor_triggers.txt`, and `famine_migration_corridor_effects.md`: zero references.
- Owned hybrid-comparison census using a brace-bounded `check_variable` search across both corridor scripts: zero malformed forms remain. All 20 trigger hybrids were changed to explicit syntax; the five effect hybrids were already normalized in the shared working tree and remain explicit.
- Brace/nesting hygiene: effects file has 517 opening and 517 closing braces with no negative-depth line; triggers file has 191 opening and 191 closing braces with no negative-depth line.
- Source callsite proof was rerun with `rg` for route geometry, offer, operation, front-state, and route-binding helpers. No callsite outside the existing corridor lifecycle and the parent-owned decisions was added.
- No probability or AI weights changed, so no probability baseline/compare was applicable to this patch.

## MCP and source blockers

The installed HOI4 MCP inventory exposes read-only event, focus, GUI, map, technology, and probability routes, but no scripted-effect or scripted-trigger inspection route. A bounded `hoi4.map_inspect` call was still made for the adjacency surface because the contract relies on the engine's state-neighbor relation. It returned `MAP_INSPECTED` for workspace `mod_chaos_redux_ea3b2d67c2c0` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/978cb238e3fce6632d213c546888d2d03a79a70a1351c7ce9ad5c54aff726f22/f9dde0560c9c44c561c0f73c4d4723394dd8d3c044acc44f1fa3417a4a5472bd/map-inspect.11f81b8704b94497.json`; its state/region membership and network/adjacency checks passed, while unrelated map-building/port locator diagnostics failed and the overall map validation remained false. This owned patch has no event, focus, GUI, map rewrite, technology, or weighted surface; no matching script-helper inspection route exists. Source review is not claimed as engine evidence.

The inherited famine/migration handoffs record `hoi4_agent_tools/hoi4.event_inspect` timing out after 180 seconds for the decision surface, `hoi4_agent_tools/hoi4.map_inspect` returning `INTERNAL_ERROR` with `Unexpected internal error`, and the required `chaosx_ai_probability_auditor` route not being callable. Those are carried as blockers, not replaced with source-only engine claims.

Runtime validation remains required for `var:<database_id>` scope resolution after save/reload, counterpart decision visibility, capacity refresh timing for a newly selected front, and live behavior of the native dynamic rail/bombing values. The route also cannot claim owner-specific hazard evidence for a future hazard channel that has no current producer; such a channel needs an authoritative adapter before it can be added to the affirmative contract.

## Remaining risks and follow-up

- The ownership requirement intentionally fails closed for an occupied front whose controller is not also the stored counterpart owner. If the design later permits occupied-front corridors, that must be an explicit contract change with a separate ownership/authorization proof rather than a relaxation of this trigger.
- The sparse native projection refresh remains owned by the main famine core. Any change to its producer cadence, threshold, or clear semantics must update this handoff and the corridor safety documentation.
- A future exact land-combat or strategic-bombing attack owner may call the existing receipt adapter, but this patch does not invent one.
- No simplification, fallback, probability change, population mutation, or unrelated file edit was made.
