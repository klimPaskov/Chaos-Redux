# IW-039 Cossack Don capital and DHC collision preflight

**Disposition:** `blocked` pending an explicit Event 006 anchor/capital and DON-versus-DHC coexistence policy. No gameplay or specification choice was made in this preflight.

## Accepted design and current binding

The candidate registry identifies IW-039 as the vanilla `DON` carrier, listing states 245 Millerovo and 238 Volgodonsk in the anchor field, in shared reservation group `RG-DON-KUBAN`. The package research row preserves those same state IDs and classifies the package as available only when the registered tag is not living. Neither row distinguishes a unique anchor state from a secondary compact state. References: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:40` and `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:40`.

The installed-map binding records `245|238` in both its `anchor_state_ids` and `compact_state_ids` fields, names them Millerovo and Volgodonsk, and records `SOV=219` as the protected host remnant. This is a two-state binding and does not select which state is the unique required anchor. The map reservation group gives `RG-DON-KUBAN` a maximum of one automatic package per wave and lists IW-039 and IW-040. References: `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:40` and `006_current_map_reservation_groups.csv:75`.

The current planner shell provisionally resolves that binding by saving state 245 as its anchor and host-capture source in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:883-895`; its reservation wrapper requires 245 as the anchor and attempts 238 as compact territory at `:969`. This source shape does not establish acceptance of that exact division. Its current package archetype is `mountain_or_frontier`, while the accepted IW-039 force mapping uses `mounted_mobile` in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:40`; this mismatch is an additional admission blocker.

The current region trigger registry prevents a second package in `RG-DON-KUBAN` in the same wave for both IW-039 and IW-040 (`common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:345-363`). This matches the binding's maximum of one package per wave. The older map-rule sentence says “same coarse state,” which is less precise than the explicit maximum and implementation; retain the capacity-one value unless the accepted design is changed.

## Capital and Event 005 conflict

Vanilla DON's country history sets capital state 218, Rostov Area. Event 006's accepted IW-039 binding does not include state 218. The 2026-08-10 IW-039 preflight records that Event 005's Don Host Emergency Circle (DHC) uses capital 218 and transfers/claims states 218 and 238. Current Event 005 source sets `soviet_collapse_don_host_successor` and capital 218 in `common/scripted_effects/005_soviet_collapse_effects.txt:22505-22510`; its DHC spawn path calls `soviet_collapse_setup_dhc_successor` at `:23531`. The older preflight contains the detailed DHC state and collision review at `subagent_handoffs/006_iw039_preflight_2026_08_10.md`.

The accepted documents do not select one unique Event 006 anchor from 245/238, decide whether active Event 006 DON moves its capital from vanilla state 218, decide whether state 218 joins its territory, or decide whether DON may coexist with DHC. The previous preflight explicitly says not to select a capital or transfer the compact set until a DON-versus-DHC ownership matrix is explicit and tested in both event orders. It proposes guarding DHC ownership/control and frozen reservations for 218/238, then adding reverse guards so Event 005 cannot create or overwrite a live Event 006 DON. These are proposals in the preflight, not accepted design.

## Current MCP map receipt

Read-only `hoi4_map_inspect` inspected states 218, 219, 234, 238, and 245 in workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `MAP_INSPECTED`, status `ok`, revision `e33d722dc4dc4375c9c17db161fae128a50134d40cf2663c66150b1d35b0a396`, and three artifacts. The [full map inspection artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee599d30696d7690c48aad9a1ea1c490b3a42133496b5e783e9a62c08796db68/00bb00070fec10b1a660b7d2d9ab20cc9de1d38126471a5d4ee0c41d38ac8e3c/map-inspect.e33d722dc4dc4375.json) records the selected records and complete map catalog. The state/region-membership, bitmap geometry, adjacency, supply-node, and railway validation checks passed; overall positions/locators validation failed on existing workspace-wide `map/buildings.txt` diagnostics, including 2,654 position/port errors beyond the returned diagnostic ceiling. No map files were changed.

The installed binding and earlier focused preflight agree that states 218, 219, 234, 238, and 245 are currently Soviet-owned; 219 is the protected SOV remnant, 234 is IW-040/KUB's anchor, 238 is the DHC overlap and IW-039 compact, and 245 is the IW-039 anchor. This does not prove the campaign-time owner/controller matrix or DHC event-order behavior.

## Concrete choices for parent/user resolution

One source-aligned proposal is to accept the source shell's 245 required anchor and 238 optional compact, move the active Event 006 DON capital to 245, keep vanilla history and its ordinary 218 capital outside Event 006, and make DHC and Event 006 IW-039 mutually exclusive in both event orders. Under that proposal, a live DHC or an Event 005 reservation over 218/238 blocks IW-039; an active Event 006 IW-039 blocks DHC creation rather than allowing Event 005 to reclaim state 238. `RG-DON-KUBAN` remains capacity one, so DON and KUB cannot both be selected in one automatic wave. This is a recommendation for resolution, not accepted design.

The alternative is to retain vanilla capital 218 and revise the package territory/capital and DHC collision contract explicitly, including which country can own or control 218 and 238 when either event fires first. The package remains blocked until that matrix and its event-order checks are accepted. Do not silently add state 218, use a nearby-state substitute, or set the content-ready flag to bypass admission.

No source, trigger, capital, reservation group, attestation, setup, cleanup, localisation, focus, decision, mission, asset, or spec was changed by this preflight. Event 006 remains **HOLD / PARTIAL**.
