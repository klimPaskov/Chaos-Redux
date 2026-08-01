# Event 006 focus geometry reflow follow-up - 2026-08-01

## Decision

Keep the bounded coordinate-only reflow in `common/national_focus/006_independence_wave_focus.txt`. The candidate preserves all focus IDs, prerequisites, rewards, icons, localisation keys, AI blocks, and CAT additive/full-framework boundaries, while the regular-focus static graph reduces crossings and point-on-segment through-node hits without adding duplicate nodes or extra close pairs. MCP post-validation was attempted repeatedly but is blocked by `SCAN_BYTE_LIMIT`; no MCP PASS is claimed.

## Changed files and focus IDs

| File | Changed IDs | Change |
| --- | --- | --- |
| `common/national_focus/006_independence_wave_focus.txt` | `independence_wave_build_regional_transport_authority` | `(x=32,y=4)` -> `(x=32,y=5)` |
| `common/national_focus/006_independence_wave_focus.txt` | `independence_wave_establish_customs_service` | `(x=32,y=5)` -> `(x=32,y=6)` |
| `common/national_focus/006_independence_wave_focus.txt` | `independence_wave_activate_package_economic_program` | `(x=32,y=6)` -> `(x=32,y=7)` |
| `common/national_focus/006_independence_wave_focus.txt` | `independence_wave_create_independent_treasury` | `(x=32,y=7)` -> `(x=28,y=8)` |
| This handoff | N/A | Records the candidate evidence and MCP limitation. |

No other focus source, shared-focus overlay, localisation, icon, reward, prerequisite, mutual-exclusion, or AI content was changed.

## Route behavior before and after

The economy chain remains semantically identical: `independence_wave_secure_food_and_fuel` still unlocks `independence_wave_build_regional_transport_authority`, which still unlocks `independence_wave_establish_customs_service`, then `independence_wave_activate_package_economic_program`, then `independence_wave_create_independent_treasury`. The new rows are monotone `y=3 -> 5 -> 6 -> 7 -> 8`; the two-row jump into the transport authority is layout-only and does not alter focus availability or completion order.

The treasury capstone now sits at `x=28,y=8`, three columns left of the first y=8 military choice at `x=31`, so the moved economy endpoint does not create a same-row duplicate or spacing violation in the static graph. The CAT additive overlay root and all full-framework assignment gates remain untouched.

## Static before/after evidence

The source parser recognized 184 regular focus blocks and 223 prerequisite connectors before and after the patch. The focus-ID set is identical, and hashes of every block after removing only `x`/`y` lines are identical, proving that prerequisites, rewards, icons, localisation references, AI blocks, and other gameplay text were not changed.

The regular-focus graph static scan reports the following baseline-to-candidate changes:

| Metric | Baseline | Candidate | Result |
| --- | ---: | ---: | --- |
| Straight-segment crossings | 57 | 53 | Improved by 4 in the source-level graph model. |
| Long connectors using the MCP thresholds | 28 | 28 | Unchanged. |
| Same-row gaps below 2 columns | 5 | 5 | Unchanged. |
| Exact duplicate coordinates | 0 | 0 | Unchanged. |
| Point-on-segment through-node hits | 3 | 2 | Improved by 1 in the source-level graph model. |

The static improvement is explained by moving the transport-authority endpoint below the y=4 founding fan and moving the economic chain’s later nodes with it. It removes the source-model crossings between the founding-settlement fan and the transport-authority edge and removes the source-model through-node hit involving the moved economic chain. The MCP baseline’s known diagnostics remain the authoritative pre-patch reference: 45 crossings, 7 node intersections, 28 long connectors, and 14 blocking diagnostics.

## MCP validation and limitation

The pre-patch MCP inspect/render evidence was the default `independence_wave_focus_tree` inspection of `common/national_focus/006_independence_wave_focus.txt`, with layout hash `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf` and artifacts recorded in the v82 audit handoff.

After applying the four-coordinate candidate, `hoi4.focus_inspect` and `hoi4.focus_render` were retried with the same tree and spacing parameters. Both returned `SCAN_BYTE_LIMIT` with `filesScanned=[]`, `proposedFiles=[]`, and no diagnostics or artifacts, so no post-patch MCP layout hash or MCP metric is available. This is an MCP scan limitation; it is not treated as validation success or failure of the coordinate candidate.

The retained candidate therefore has static source evidence only for its after-state. Parent review should rerun MCP inspect/render when the workspace scan is below the configured byte limit and reject the candidate if the full-tree crossing, node-intersection, or long-connector totals worsen.

## Other bounded candidates not retained

- Opening handoff test: moving `independence_wave_integrate_provinces_and_councils` to `x=28` and the entire economy lane to `x=26` removed the source-model opening crossing, but increased same-row close pairs from 5 to 7 and pulled the economy chain between government routes; it was reverted before the retained patch.
- Depot-spine tests: moving `independence_wave_integrate_militia_commands`, `independence_wave_secure_national_depots`, `independence_wave_recall_and_vet_officers`, and `independence_wave_form_border_guard` left the source-model crossing count unchanged or increased it and did not safely remove the fan crossings; no military-spine coordinate was retained.
- Professional-defence tests: moving `independence_wave_adopt_military_archetype_program` toward the capstone reduced one long edge but increased source-model crossings; moving the ten y=8 choices created close pairs; no military-choice or capstone coordinate was retained.

## Remaining route and geometry risks

- The opening oath/economy crossing remains because `independence_wave_bind_the_first_oath`, `independence_wave_integrate_provinces_and_councils`, `independence_wave_inventory_the_state`, and `independence_wave_establish_emergency_revenue` were not moved by this safe tranche.
- The depot/recall fan and professional-defence merge remain coupled; a full fix still requires a coordinated y=5..9 reflow that preserves the ten military choices, five OR prerequisite groups, and all mutual exclusions.
- MCP post-patch geometry is unverified until the scan-byte limit is cleared, so the static improvement must not be presented as validator-clean completion.

## Parent handoff

Commit only `common/national_focus/006_independence_wave_focus.txt` and this handoff from this subtask. Preserve unrelated worktree edits. On the next MCP pass, compare the full-tree totals against the baseline `45 crossings / 7 node intersections / 28 long connectors / 14 blockers`; retain the four-coordinate patch only if no global metric regresses.
