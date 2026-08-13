# Soviet-collapse focus layout repair — MCP pass

## Scope

This pass covers the 43 national focus trees loaded from the Soviet-collapse focus sources:

- `005_soviet_collapse_ancient_restorations.txt`: APX, SOG, ANX, ABX (4 trees).
- `005_soviet_collapse_factory_successors.txt`: CFR, OGB, MFR (3 trees).
- `005_soviet_collapse_republics.txt`: Ukraine, Breakaway, Internal Republic, Baltic, Caucasus, Central Asia, Moldova, Belarus, Kazakhstan (9 trees).
- `005_soviet_collapse_custom_splinters.txt`: 27 custom splinter trees.

The request was handled with `chaos-redux-focus-trees`, the offline HOI4 references, and the HOI4 MCP workspace `mod_chaos_redux_ea3b2d67c2c0`.

## Implementation

The source changes are coordinate-only. Prerequisites, mutual exclusions, rewards, AI weights, localisation keys, focus IDs, icons, and route logic were preserved. Fixed-coordinate rows were re-spaced where MCP identified duplicate or too-close focus cells, then selected endpoints were moved using MCP layout metrics and diagnostics as the acceptance signal.

The Holy Realm cleanup is also coordinate-only. `THR_sit_beneath_prayer_flags` was brought closer to its doctrine parent, `THR_fourth_quiet` was moved clear of the mountain-granary connector, and `THR_buddha_mandate` was shifted to reduce convergence through-node pressure.

No new icons are required. Existing icon references remain in their original `.gfx` registrations and existing focus sprite folders.

## Evidence

The local structural audit covers all 43 Soviet-collapse trees and reports:

- duplicate focus coordinates: `0`
- same-row pairs closer than the required two-column spacing: `0`

The MCP per-tree inspections completed for all 27 custom splinter trees. Each returned `status: ok` and `tooClose: 0`. Representative final MCP layout metrics are:

| Tree | Focuses | Crossings | Node intersections | Long connectors | Max horizontal span |
| --- | ---: | ---: | ---: | ---: | ---: |
| APX | 16 | 2 | 0 | 0 | 6 |
| CFR | 47 | 0 | 0 | 0 | 8 |
| OGB | 23 | 0 | 1 | 0 | 8 |
| MFR | 58 | 8 | 5 | 0 | 8 |
| Ukraine | 83 | 17 | 19 | 3 | 9 |
| Breakaway | 36 | 12 | 10 | 5 | 12 |
| Central Asia | 45 | 13 | 6 | 1 | 9 |
| Kazakhstan | 92 | 12 | 24 | 3 | 13 |
| Holy Realm | 111 | 31 | 22 | 11 | 30 |

MCP render checks completed for Ukraine, Holy Realm, and dense custom UDC, returning HTML, SVG, PNG, JSON, source-map, and layout-plan artifacts.

## Remaining MCP limitations

The automatic MCP compact rewrite was attempted on Ukraine, APX, and UDC. It was quality-gate blocked and wrote no files, so the final coordinate patch was applied in the repository and re-inspected through MCP.

Some connector crossings and through-node warnings remain in dense, semantically convergent branches. Removing those completely would require a route redesign or additional rows, not a safe layout-only adjustment. MCP also reports existing partial helper inventories and several truncated DDS pixel-data references in focus icons; those are outside this coordinate-only pass and are not changed here.

## Future work

If the remaining connector warnings become a visual release blocker, handle them as a separate route-layout tranche: redesign one tree at a time, move convergence nodes with their dependent branch cohorts, render before/after, and re-audit focus route readability and mutual-exclusion semantics.
