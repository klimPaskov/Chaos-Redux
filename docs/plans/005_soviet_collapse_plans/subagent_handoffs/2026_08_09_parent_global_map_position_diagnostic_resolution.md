# Event 005 Global Map-Position Diagnostic Resolution

Date: 2026-08-09

## Scope

This handoff resolves the global map-position finding raised during the Event 005 completion pass without changing valid map data.

The mandatory global `hoi4.map_inspect` pass returned `MAP_INSPECTED` and verified province definitions, bitmap geometry, state and strategic-region membership, adjacencies, supply nodes, and railways. Its only failed validation family was `map-positions-locators`.

## Diagnostic root cause

The global result reported 2,654 omitted errors under the diagnostic ceiling:

- 1,323 `MAP_BUILDING_POSITION_INVALID` findings
- 1,331 `MAP_PORT_ADJACENT_SEA_INVALID` findings

The retained examples all begin at `map/buildings.txt` line 26,352 and identify `floating_harbor` rows. The first row is `12;floating_harbor;3178.00;9.50;1681.00;1.57;9317`.

The mod contains 2,334 `floating_harbor` rows. The complete set is byte-for-text identical to the installed vanilla file at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/map/buildings.txt`; a direct set comparison found zero differences. The same installed vanilla definitions classify every final province field on these `floating_harbor` rows as land, while all 2,362 vanilla `naval_base_spawn` final province fields resolve to sea.

The installed MCP validator treats `floating_harbor` and `naval_base_spawn` as the same port-position record. It requires the model coordinate to resolve inside the declared land state and requires the final province field to be sea for both types. Current vanilla data deliberately uses a sea model position and a land attachment province for `floating_harbor`, so the validator reverses both parts of the current vanilla contract and emits the paired false positives.

## Event 005 map evidence

The bounded Event 005 state inspection covered states 247, 569, 570, 571, 572, 578, 583, 585, 586, and 827. The MCP returned no unknown province IDs, no missing geometry, and no state, region, adjacency, supply, or railway blocker for those consumers.

Event 005 does not own a map-definition, province bitmap, state-definition, adjacency, building-position, supply-node, or railway rewrite. Its focus, decision, and release effects consume existing states through normal country/state scope effects.

## Resolution

No map source was changed. Replacing the current vanilla `floating_harbor` records with values tailored to the validator would corrupt the installed-game map contract and would be a real gameplay regression rather than a repair.

The global finding is therefore resolved as an MCP validator defect proven against the exact installed vanilla source, not as an Event 005 content omission. The linked Event 005 state consumers remain valid under the map geometry and topology checks that the MCP completed successfully.

No fallback or content simplification was introduced.
