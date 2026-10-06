# Event 005 Kazakhstan graphics review

Disposition: the twenty Kazakhstan sprite findings are implemented, combining the prior shared edge repair (`77bbd81e1`) with this reviewed residual pass.
The full Event 005 task remains incomplete.
The user's October graphics instructions are the acceptance basis for these repairs.

Eight DDS paths change: normal legacy and focus-consumed copies of `british_and_american_engineers`, `league_cavalry_school`, `southern_republics_do_not_kneel` (the focus copy includes `the_`), and `turkish_language_channels` under `gfx/interface/goals/005_soviet_collapse/`.
Their exact paths and delivered hashes are in `docs/assets/005_soviet_collapse/gfx_fix_kaz/repairs.json` and `validated.json`.
The durable committed crosswalk, original/output hashes, exact removals, decoded validation, and MCP results are also in `005_kaz_evidence.json` beside this report, with `005_kaz_review.png` as the paired final review.
Sprite names, 94x86 canvas, frame counts, consumer bindings and gameplay are preserved.

## Complete review-table disposition

| Reviewed sprite suffix | Severity | Evidence and disposition |
| --- | --- | --- |
| the_written_alash_program | 2 | Earlier edge repair retained; current native and enlarged review has neutral edges. |
| steppe_land_statutes | 2 | Earlier edge repair retained; purple laurel outline removed. |
| alash_memory_restored | 2 | Earlier edge repair retained; neutral cut-out edge. |
| semey_legal_circle | 2 | Earlier edge repair retained; neutral cut-out edge. |
| the_alash_courts | 2 | Earlier edge repair retained; neutral cut-out edge. |
| restore_alash_names | 2 | Earlier edge repair retained; neutral cut-out edge. |
| constitutional_kurultai | 2 | Earlier edge repair retained; neutral cut-out edge. |
| multi_vector_recognition | 2 | Current compass/letters composition fits within bounds (4,2,90,84); retained after source and native review. |
| british_and_american_engineers | 3 | Faint outer alpha below 32 removed; helmets and girders remain readable without a surrounding dark smear. |
| turkish_language_channels | 3 | Faint outer alpha below 32 and one detached pixel removed; radio, bell, papers and surviving antialiasing preserved. |
| call_the_steppe_congress | 2 | Earlier green-edge repair retained; horn and derrick remain intact. |
| crush_the_road_militias | 2 | Earlier green-edge repair retained; neutral wreath edge. |
| the_southern_republics_do_not_kneel | 2 | Earlier internal neon-spill mask repair retained; detached alpha above and below the flags removed in this pass. |
| basmachi_roads_reopen | 2 | Earlier reviewed spill-mask repair retained; old review sheet's neon blobs are absent from current rider/truck art. |
| the_southern_republics_write_together | 2 | Prior repair removed the isolated dashes; current alpha contains only the main silhouette. |
| league_cavalry_school | 2 | Detached dash and dots removed; colour-only bleeding removes the retained fringe without eroding flag ribbons. |
| common_steppe_passports | 3 | Prior repair removed the specks; current alpha contains only the main silhouette. |
| kyrgyz_mountain_liaisons | 3 | Prior repair removed the specks; current alpha contains only the main silhouette. |
| kyrgyz_border_cavalry | 3 | Prior repair removed the specks; current alpha contains only the main silhouette. |
| steppe_defense_council | 3 | Prior repair removed the two lower specks; current alpha contains only the main silhouette. |

The complete family review covers 184 non-shine registrations, 184 registered paths, and 92 actual focus consumers in the current republics source.
Counts refer to registrations, files and consumers separately.
Baseline, consumer source spans, exact per-path hashes, whole-family before/after sheets, original PNGs, selected processed PNGs and decoded DDS proof are in `docs/assets/005_soviet_collapse/gfx_fix_kaz/`.
No already-repaired texture is eroded again.

## Meaningful validation

All eight delivered DDSs decode exactly to their selected PNGs at 94x86.
The lowest mean alpha on surviving subject pixels is 231.516/255.
Before/after comparison confirms preserved thin flag details, removal of detached fragments and no shifted subject anchors.
Matching MCP focus rasters produced changed PNG hashes with identical layout/source-map/plan hashes after installation, confirming texture changes without focus-structure changes.
The parent inspected the full native family sheets and the matching decoded MCP crops; the machine result reports no blocking focus diagnostics.
The existing report-colour audit returned zero coloured report/news keys during this pass.

References read: offline `National focus modding - Hearts of Iron 4 Wiki.md` lines 303–382, revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`; offline `Graphical asset modding - Hearts of Iron 4 Wiki.md` lines 30–99, revision `f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9`; installed `documentation/effects_documentation.md` lines 681–689 and 4771–4786, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Vanilla regular/shine definitions were read in `interface/goals.gfx` and `interface/goals_shine.gfx`; source lookup located `GFX_goal_generic_political_pressure` at `game:interface/goals.gfx:677–681`, index revision `5f044eab9771a00d3f94cf795a6b9089f5285bfa3e69dd3d39d41866e9c58404`.
The canonical focus reference contact sheet and its catalog were reviewed.
MCP results and artifact hashes are preserved in the package, without a refresh request.

## Design decisions and remaining limits

Colour-only correction is selected for the cavalry flag's fragile ribbons after visual review, under the user's existing authority to fix these assets.
Opacity is not boosted and replacement art is not substituted for any Kazakhstan focus.
Both legacy and focus aliases are repaired to prevent the defect surviving through a second registered texture.
The decision is recorded in `docs/plans/005_soviet_collapse_plans/agent_decisions_2026-10-05.md`.

No simplification or fallback art is used for these twenty sprite findings.
The MCP also reports five long linear connector detours in the existing focus layout, plus the installed generic continuous-focus description warning.
Those remain unresolved by this asset-only tranche; no focus-layout completion is claimed.
The remaining Event 005 trees, portraits and other sprite rows are separate open work.
Live consumer behavior has not been observed by this agent.

## Exact orchestrator live checks

Use a paused 1936 USA graphics fixture at 1920x1080 and UI scale 1.
Run `effect load_focus_tree = { tree = soviet_collapse_kazakhstan_focus_tree }` and open the focus view.
At normal zoom and close zoom, inspect League Cavalry School, The Southern Republics Do Not Kneel, Turkish Language Channels, and British and American Engineers.
Expected: no coloured rim or floating dash on the cavalry flag, no detached fragments above/below the southern flags, crisp engineers/radio outlines, and readable intact subject paint.
Inspect one available focus, one locked focus, and their hover-detail windows for stable icon anchoring and both regular/shine texture states.
Compare the Alash political, steppe military and foreign-contract icon families with the final native sheets; the earlier repaired edges should remain clean.
The long-connector warnings remain open and must not be counted as fixed by this check.

Skills used: `chaos-redux-event-assets`, `chaos-redux-focus-trees`, `chaos-redux-events` for event ownership, `chaos-redux-subagents`, `imagegen` for the wider production work, and `chaos-redux-shared-git-commit`.
No skill is created or changed by this tranche.
