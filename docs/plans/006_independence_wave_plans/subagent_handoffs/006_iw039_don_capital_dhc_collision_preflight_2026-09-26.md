# IW-039 Cossack Don capital and DHC collision preflight

**Disposition:** accepted and queued for IW-039 package implementation. The user explicitly selected the 245 anchor/capital, optional 238 compact, and both-order DHC exclusion policy below; package implementation and its remaining readiness gates are still open.

## Accepted design and current binding

The candidate registry identifies IW-039 as the vanilla `DON` carrier, listing states 245 Millerovo and 238 Volgodonsk in the anchor field, in shared reservation group `RG-DON-KUBAN`. The package research row preserves those same state IDs and classifies the package as available only when the registered tag is not living. Neither row distinguishes a unique anchor state from a secondary compact state. References: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:40` and `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:40`.

The installed-map binding records `245|238` in both its `anchor_state_ids` and `compact_state_ids` fields, names them Millerovo and Volgodonsk, and records `SOV=219` as the protected host remnant. This is a two-state binding and does not select which state is the unique required anchor. The map reservation group gives `RG-DON-KUBAN` a maximum of one automatic package per wave and lists IW-039 and IW-040. References: `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:40` and `006_current_map_reservation_groups.csv:75`.

The current planner shell provisionally resolves that binding by saving state 245 as its anchor and host-capture source in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:883-895`; its reservation wrapper requires 245 as the anchor and attempts 238 as compact territory at `:969`. This source shape does not establish acceptance of that exact division. Its current package archetype is `mountain_or_frontier`, while the accepted IW-039 force mapping uses `mounted_mobile` in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:40`; this mismatch is an additional admission blocker.

The current region trigger registry prevents a second package in `RG-DON-KUBAN` in the same wave for both IW-039 and IW-040 (`common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:345-363`). This matches the binding's maximum of one package per wave. The older map-rule sentence says “same coarse state,” which is less precise than the explicit maximum and implementation; retain the capacity-one value unless the accepted design is changed.

## Capital and Event 005 conflict

Vanilla DON's country history sets capital state 218, Rostov Area. Event 006's accepted IW-039 binding does not include state 218. The 2026-08-10 IW-039 preflight records that Event 005's Don Host Emergency Circle (DHC) uses capital 218 and transfers/claims states 218 and 238. Current Event 005 source sets `soviet_collapse_don_host_successor` and capital 218 in `common/scripted_effects/005_soviet_collapse_effects.txt:22505-22510`; its DHC spawn path calls `soviet_collapse_setup_dhc_successor` at `:23531`. The older preflight contains the detailed DHC state and collision review at `subagent_handoffs/006_iw039_preflight_2026_08_10.md`.

At the time of this initial preflight, the accepted documents did not select a unique Event 006 anchor, capital, or DHC coexistence policy. That gap is now resolved by the user's explicit decision recorded below; the package still requires implementation and the specified event-order validation.

## Accepted user decision (2026-09-26)

Acceptance basis: the user chose “Use 245 as Event 006 anchor/capital; 238 is optional compact; exclude DHC in both event orders.” This selects state 245/Millerovo as IW-039's unique required anchor and capital, allows state 238/Volgodonsk only as optional compact territory, and keeps vanilla DON capital/state 218 outside Event 006. The Event 005 DHC and Event 006 IW-039 must be mutually exclusive regardless of which event would execute first. Reject IW-039 if DHC is live or an Event 005 reservation conflicts with states 218/238; once IW-039 is active, block Event 005 from creating or overwriting DHC across the same DON/Volgodonsk collision. Preserve the capacity-one `RG-DON-KUBAN` limit and protected SOV state 219. This is accepted design; it does not claim source implementation or engine proof.

## Current MCP map receipt

Read-only `hoi4_map_inspect` inspected states 218, 219, 234, 238, and 245 in workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `MAP_INSPECTED`, status `ok`, revision `e33d722dc4dc4375c9c17db161fae128a50134d40cf2663c66150b1d35b0a396`, and three artifacts. The [full map inspection artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee599d30696d7690c48aad9a1ea1c490b3a42133496b5e783e9a62c08796db68/00bb00070fec10b1a660b7d2d9ab20cc9de1d38126471a5d4ee0c41d38ac8e3c/map-inspect.e33d722dc4dc4375.json) records the selected records and complete map catalog. The state/region-membership, bitmap geometry, adjacency, supply-node, and railway validation checks passed; overall positions/locators validation failed on existing workspace-wide `map/buildings.txt` diagnostics, including 2,654 position/port errors beyond the returned diagnostic ceiling. No map files were changed.

The installed binding and earlier focused preflight agree that states 218, 219, 234, 238, and 245 are currently Soviet-owned; 219 is the protected SOV remnant, 234 is IW-040/KUB's anchor, 238 is the DHC overlap and IW-039 compact, and 245 is the IW-039 anchor. This does not prove the campaign-time owner/controller matrix or DHC event-order behavior.

## Implementation contract and remaining gates

Implement the accepted 245/238/218 split and DHC mutual exclusion in both event orders. Preserve vanilla DON history and ordinary capital outside the Event 006 package, keep SOV's state 219 remnant, and retain `RG-DON-KUBAN` capacity one per wave. The current planner shell's archetype mismatch and all other package gates remain to be resolved.

The alternative that retains state 218 as the active Event 006 capital was not selected. Do not add state 218, use a nearby-state substitute, or set the content-ready flag to bypass admission.

No source, trigger, capital, reservation group, attestation, setup, cleanup, localisation, focus, decision, mission, asset, or spec was changed by this preflight. Event 006 remains **HOLD / PARTIAL**.
