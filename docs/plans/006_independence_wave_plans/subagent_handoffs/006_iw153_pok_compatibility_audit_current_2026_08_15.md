# IW-153 POK compatibility preservation audit — 2026-08-15

## Disposition

IW-153 remains a dormant, package-local, `specific_community_variant_only` boundary and is not admitted to the Event 006 release pool. No gameplay or central source patch is justified by this audit.

## Preservation result

The current wrappers preserve the vanilla POK carrier contract. The context requires a living `original_tag = POK` country with an active Independence Wave origin, `liberation_origin = independence_wave`, package id `iw_153`, and a future named-community selection flag that the wrapper itself never writes.

The character witness checks `INS_syarif_muhammad_alkadrie`, matching vanilla `history/countries/POK - Pontianak.txt` and the character definition in vanilla `common/characters/INS.txt`. The core witness checks POK cores in states 334 and 1022, matching vanilla state history. The releasable witness reads `POK` from Indonesia's `INS_releasables` array and never mutates that array. The strict contract additionally requires ownership and control of state 334 and a state-334 capital.

The only persistent effect is cleanup of the future `independence_wave_iw_153_named_community_selected` marker after the complete context gate passes. The wrappers do not recruit or transfer characters, add or remove cores, change state ownership, alter cosmetics, call or override `indonesia_transfer_POK`, or add central dispatch, attestation, preflight, scenario, or Join entries.

## Current MCP evidence

Read-only `hoi4.map_inspect` for states 334 and 1022 returned `MAP_INSPECTED` at current workspace revision `89247d6facadfde63a77f62c34a2218de00a72e30745e98ae6ff41ed403bbdac`. Selected state membership, geometry, and network checks passed. The aggregate map validation remains false only because the workspace-wide locator diagnostic ceiling retains 2,654 unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` errors from `mod:map/buildings.txt`; no selected-state POK geometry or ID blocker was reported.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5e81f9798a94a1495e790e79891b54a22f6109b0c38180efc1cce2d6fbea613/11699b72ec0bfd9ef2aeec8f21d932f506fd5335436ec4f6a40edf30adcf6038/map-inspect.89247d6facadfde6.json`.

No focus, event, GUI, technology, or weighted surface was changed or exposed by this dormant wrapper, so no additional MCP route was applicable. No live game or save/load claim is made.

## Remaining gates

The future named Dayak community, territory and host-remnant policy, period-valid leader or institution, portrait/source asset, symbol/flag provenance, and any runtime caller remain unresolved. The adapter must stay dormant until those sources and an explicit parent-owned package plan exist. This audit does not advance Event 006 authority counts or claim whole-event completion.
