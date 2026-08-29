# Event 005 Soviet Collapse Focus Tree Repair — Incomplete Handoff

## Status

This repair tranche is incomplete and must not be treated as a completion claim.

The Event 005 focus-tree surface contains 43 trees. The integrated source audit currently records 36 trees with zero connector crossings, zero connector-through-node intersections, and zero long connectors. Seven trees still fail the required layout bar.

## Implemented work

- Repaired the layout and dependency staging of the ancient-restoration and factory-successor families.
- Repaired the Baltic tree to zero crossings, zero node intersections, and zero long connectors, including a visible military-border sequence rather than hidden availability gates.
- Repaired the Kazakhstan and Belarus republic trees to the same hard-layout standard.
- Repaired 26 custom-splinter trees to the same hard-layout standard, including KHC after a final staged supply, diplomatic, customs, and enemy-front pass.
- Added long-tree shortcuts to the full custom-splinter trees where the route depth required navigation support.
- Removed redundant direct prerequisites and replaced several misleading visible-OR/hidden-AND route surfaces with explicit staged dependencies.
- Added missing Ukraine annexation and industry filters where the rewards actually grant territorial or industrial outcomes.
- Added the missing UWR and KMB focus localisation keys.
- Confirmed every Event 005 focus has at least one `search_filters` entry, a title and description key, and a resolved mod or vanilla focus sprite in the source-level coverage audit.

## Remaining hard-layout failures

| Tree | Crossings | Node intersections | Long connectors | Principal unresolved surface |
|---|---:|---:|---:|---|
| `soviet_collapse_ukraine_focus_tree` | 3 | 1 | 0 | Duplicate early convergence and the commander/league lanes |
| `soviet_collapse_breakaway_focus_tree` | 1 | 4 | 1 | Depot-repair convergence and the neutrality/endurance lanes |
| `soviet_collapse_internal_republic_focus_tree` | 0 | 1 | 4 | The common autonomy statute fans directly into four distant regional lanes |
| `soviet_collapse_caucasus_focus_tree` | 6 | 2 | 1 | Oil directorate, route-fork, restoration, and defense-lane convergence |
| `soviet_collapse_central_asia_focus_tree` | 0 | 2 | 0 | The cotton-rail connector crosses the Bishkek and Khwarazm nodes |
| `soviet_collapse_moldova_focus_tree` | 0 | 3 | 3 | The river-state capstone combines endpoints at incompatible route depths |
| `NLC_soviet_collapse_focus_tree` | 8 | 5 | 0 | Generic trunk lanes overlap the polar logistics and station-government branches |

## MCP evidence

- `KHC_soviet_collapse_focus_tree` passed official `hoi4.focus_inspect` geometry with 47 focuses, zero crossings, zero node intersections, and zero long connectors. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82c988d0ae933c317268a4266ae9767dd2b9f3b115c2852fcccb506c4d0bfb7a/89d9f2227493de26ed2931b7c377b2c38adec5caf248af1b189cbc1c498dd433/focus-inspect.81263a006d87199a.json`.
- The KHC inspection resolved all 47 Event 005 focus icons. Its blocking sprite diagnostics are the MCP server's unrelated vanilla continuous-focus references, not KHC assets.
- `AEX_soviet_collapse_focus_tree` previously passed official inspection at zero crossings, zero node intersections, and zero long connectors with all 47 focus textures resolved.
- Official Ukraine `hoi4.focus_rewrite` returned `FOCUS_COMPACT_QUALITY_BLOCKED`; the proposed compact layout retained the hard geometry failures, so no rewrite was applied.
- Whole-file and several per-tree inspections/renders repeatedly timed out during shared-server contention. Source-only layout evidence is not treated as equivalent to MCP evidence.

## Files in the repair tranche

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Assets

No new focus icons are required by this tranche. Existing Event 005 DDS sprites and `interface/005_soviet_collapse_focus_icons.gfx` remain the asset source.

## Completion blockers

- The seven trees in the table require route-specific dependency redesign, not a blind coordinate shuffle.
- The final `chaosx_focus_tree_auditor`, `chaosx_localisation_auditor`, and `chaosx_ai_probability_auditor` passes have not been completed against a fully clean integrated source.
- No task commit has been created because the requested all-tree repair is not complete.

## Next implementation order

1. Resolve NLC and the four large republic layouts with explicit regional convergence focuses or staged existing endpoints.
2. Resolve the two Central Asia connector-through-node diagnostics without introducing cross-tag prerequisites.
3. Run the complete 43-tree MCP inspect/render sweep and compare the final geometry to this handoff.
4. Run focus, localisation, and weighted-AI specialist audits.
5. Update this handoff to a completion report and create the task-only commit only after every required surface passes.
