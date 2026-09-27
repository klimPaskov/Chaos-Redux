# Event 006 military-lane geometry follow-up — 2026-09-27

**Current disposition:** `implemented` for the direct-tree coordinate repair at source and direct MCP graph level. Imported root-level `shared_focus` attachment and visual/layout proof remain `blocked` because the focus inspector and render omit those nodes. This handoff records the parent-applied candidate 2 map; it does not claim assembled-tree or live-game acceptance.

**Event status:** HOLD / PARTIAL.

## Current parent integration and evidence

**Design authority:** the user approved the full Event 006 objective and retained root-level `shared_focus` imports while accepting blocked MCP layout evidence for imported nodes. Part 4 assigns final x/y positions to implementation. The parent accepted candidate 2 as a coordinate-only direct-tree improvement under that authority; the two-coordinate and four-coordinate rejected trials below remain history.

**Source implementation:** the parent-reviewed `common/national_focus/006_independence_wave_focus.txt` has SHA-256 `05FFFF53EAC51A18F5E2223C36AF6D748A50DAA4A8802B0186755A746169629B`. Relative to the `B38C72F1000E326EE8D63D7CB30DCDC2050D010CF38CBB7CC90D185EE39F12C2` baseline, it changes exactly the seven x/y assignments in the candidate 2 table below. No focus ID, parent, prerequisite, mutual exclusion, reward, AI block, localisation, icon, or import changed.

**Direct-tree MCP evidence:** parent `hoi4.focus_inspect` revision `ef6a5b9e901119fe7a88077105b39bdba0c6d014a5eb4e5b4bb471ef5f2419d6` returned `FOCUS_INSPECTED`, validation passed, layout hash `ea3ad753bd8a8841e959710671564f9fa392b172c9cc8b8d2e7e0f6ea21ccafb`, 184 direct focuses, 196 connectors, zero crossings, zero node intersections, zero long connectors, zero too-close same-row pairs, minimum spacing 2, maximum horizontal span 8, and maximum Manhattan span 9. The only non-layout warning is the unrelated vanilla continuous-focus localisation reference. [Parent inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/139a5a3982b5a72d40056702ab9cf38ac5af0e8df94b4dd6931eba202f05ab78/9bd9aff25f10dfa09184521ebf4ec68ed63859d6b27f41d47f9472a06ef0739b/focus-inspect.ef6a5b9e901119fe.json). A separate read-only curator inspect of the current source returned the same layout hash and graph metrics at revision `28f0a3050f66e60fb4d8f810a59afb00efc5fe340d74f00d8bd867345a7d0682`, with [its own artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1eb9b84bd788932e06c0949b76f3fd4262e23600951ec40779f8ae1b75cb3f1f/789f613a60c589b242e5d2fef47d8a3dd5f5d3c7fbe7802dbf31e3a142e4e815/focus-inspect.28f0a3050f66e60f.json).

**Direct-tree visual evidence:** the matching parent `hoi4.focus_render` has that same layout hash and an SVG of 1,655,885 bytes with SHA-256 `2bed01a54008000c3db448322daada11e41b1f5fb7b7adbb7d083c972ccc395d`. The matching [parent focus raster](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bae86340970fbfcecb25f39c4104cf85d484ec7843df25db20a45980979cfa3/70bba126fd77078deb5f991f37dfa7df8fc803823dc22684c09cad0b86d061c3/independence_wave_focus_tree.focus.png) at `reviewScale=0.5` is 10,712×1,220 pixels, 562,185 bytes, SHA-256 `3bae86340970fbfcecb25f39c4104cf85d484ec7843df25db20a45980979cfa3`; the parent retrieved it in 16,383-byte ranges and visually reviewed the full tree at overview scale. A detailed military-lane crop and imported-node visual acceptance were not obtained.

**Imported-node limit:** the candidate source scan parsed 3,949 focus/shared-focus definitions across 34 files, including 353 Event 006 IDs, 169 shared definitions, and 62 imported roots; it found zero candidate-position collisions and zero same-row pairs below spacing 2. That source-only result does not prove imported-node attachment, connector clearance, or live-game layout. The inspector/render omission is a route capability limit despite the read-only focus tools being exposed and healthy for direct nodes; the accepted shared architecture remains in force without direct-focus fallback copies.

## Scope and acceptance boundary

This handoff covers only the direct Event 006 military lane in `common/national_focus/006_independence_wave_focus.txt`.

The user approved the complete Event 006 focus design and explicitly selected root-level `shared_focus` imports; no direct-focus fallback copies or inlined imports were added or considered.

The parent subsequently accepted candidate 2 based on its clean direct-tree MCP geometry and the source-level coordinate collision scan; imported-node visual proof is recorded as a separate limitation and does not block parent application of the direct-node coordinate map.

At the original candidate handoff, the restored source SHA-256 was `B38C72F1000E326EE8D63D7CB30DCDC2050D010CF38CBB7CC90D185EE39F12C2`, matching that handoff's supplied baseline.

That candidate handoff retained no source change; the later parent integration is recorded in the current section above.

## Baseline route geometry

The parent `independence_wave_adopt_military_archetype_program` is at `(42,7)`, the ten route-choice endpoints are all at `y=8`, and the `independence_wave_found_professional_defense_institution` capstone is at `(40,9)`.

| Route choice pair | Focus ids | Baseline positions | Geometry status |
| --- | --- | --- | --- |
| Civilian control / military autonomy | `independence_wave_confirm_civilian_control` / `independence_wave_grant_military_autonomy` | `(34,8)` / `(36,8)` | Adjacent mutual-exclusion pair; retained |
| Mass reserve / professional core | `independence_wave_raise_mass_reserve` / `independence_wave_build_professional_core` | `(38,8)` / `(40,8)` | Adjacent mutual-exclusion pair; retained |
| Domestic arsenals / foreign arms | `independence_wave_fund_domestic_arsenals` / `independence_wave_accept_foreign_arms` | `(42,8)` / `(44,8)` | Adjacent mutual-exclusion pair; retained |
| Border defense / reclamation doctrine | `independence_wave_adopt_border_defense` / `independence_wave_adopt_reclamation_doctrine` | `(46,8)` / `(32,8)` | Mutual-exclusion pair; reclamation has the long parent connector |
| League standardization / independent command | `independence_wave_standardize_with_league` / `independence_wave_preserve_independent_command` | `(48,8)` / `(50,8)` | Adjacent mutual-exclusion pair; retained |

The capstone’s three prerequisite blocks remain the existing AND of OR-pairs: reserve/core, domestic/foreign arms, and border defense/reclamation doctrine. Its existing availability and AI conditions remain untouched.

The baseline `hoi4.focus_inspect` at revision `867b5b01ea9bf401c0f72540e8f85693bd455664c7fe44d6576bc1f1def06ebe` reported 184 direct focuses and 196 connectors, zero connector crossings, zero node intersections, zero too-close same-row pairs, and one long connector.

The sole Event 006 layout warning is `FOCUS_LAYOUT_LONG_CONNECTOR` from `independence_wave_adopt_military_archetype_program (42,7)` to `independence_wave_adopt_reclamation_doctrine (32,8)`, with horizontal span 10 and Manhattan span 11 against thresholds of 8 and 10.

The baseline layout hash is `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.

Final restoration was confirmed by `hoi4.focus_inspect` revision `9799263c16c7bed14c7fb8101b98a9b555370d800070bbf248ea73bcf941ccd7`, which returned the same layout hash and baseline counts and diagnostics.

## Reference evidence and route gaps

`hoi4.reference_read` read the offline `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`, lines 254–274, revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`, SHA-256 `BD989A13237C464F140A0AA671CC42C30A48E84A27DAE791B8914654FB9C6203`; those lines describe absolute `x`/`y` positions and `relative_position_id` offsets.

The installed vanilla `interface/nationalfocusview.gui`, lines 631–634, defines `focus_spacing` as 96 horizontal by 130 vertical pixels per coordinate unit.

The supplied vanilla precedent is `common/national_focus/austro_hungarian_releasable_shared.txt`, lines 1–65.

The connected `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` routes were exposed; the targeted focus search returned the offline wiki position section, while the context/search result contained no applicable installed-game national-focus documentation section and reported `script_doc` unavailable with zero files.

`hoi4.source_lookup` resolved `independence_wave_adopt_military_archetype_program` in the mod source at lines 648–665, revision `9d9a7c6ad843b710f4315e33047af9e8cc9796aa766ed1814d5788c45bfef09e`.

## Candidate history

| Candidate | Coordinate plan | MCP evidence | Disposition |
| --- | --- | --- | --- |
| Parent two-coordinate trial | `independence_wave_adopt_military_archetype_program` moved `x:42→40`; `independence_wave_preserve_independent_command` moved `x:50→48` | Revision `a1c43797d963a9a4fa5701322a80832f8a52291c19a0186a3d602f76a279dd00`, layout hash `6bb84d7393aea202712a72246b52f7b383783660b4ee12bb0ea373381342bb9d`; duplicate at `(48,8)` with `independence_wave_standardize_with_league`, two node intersections, and connector-through-node warnings | Rejected by parent; not repeated |
| Prior four-coordinate trial | Parent moved to `(40,7)`, reclamation to `(40,9)`, independent command to `(42,9)`, and capstone to `(40,10)` | Revision `6c16993d6e30aa91ef52e18e0622ecb4e69c52073282edc99cd29eee92869407`, layout hash `deb452ab1204bd988aed0083cb5061caa85cbd437bee0c9a5436adf1b6341e0e`; two crossings and nine node intersections | Rejected and documented in `006_event6_reclamation_doctrine_connector_repair_2026-09-27.md` |
| Local candidate 1 | `raise_mass_reserve`, `build_professional_core`, `fund_domestic_arsenals`, `accept_foreign_arms`, `adopt_border_defense` moved from row 8 to row 9; `adopt_reclamation_doctrine` moved `(32,8)→(48,9)`; capstone moved `(40,9)→(42,10)` | Revision `b4c8d7a57e37786ab7dd6bdf98ec09013ec102d23275659f2dbeae14fda4e089`, layout hash `69c0c481f6070cf6592c4fa96f15105b0c84cffc41cf808b91e8eef3f571a088`; zero crossings/intersections/too-close pairs, but one new long connector from capstone `(42,10)` to `independence_wave_secure_durable_sovereignty (33,11)`, source lines 3438–3456, span 9 | Rejected; source restored to baseline and inspect returned layout hash `a4d2d61f` at revision `38724ffe6edac6a318b2b8248f7d24b17372a585a430bfd24c4c7f66406be14f` |
| Local candidate 2 | Same five row-8-to-row-9 moves and reclamation move as candidate 1; capstone moved `(40,9)→(41,10)` | Revision `fd6dbda0f97fb7c0d6aa29a6e0d1670d801e16330b24ff3d4384a72cc1c8308c`, layout hash `ea3ad753bd8a8841e959710671564f9fa392b172c9cc8b8d2e7e0f6ea21ccafb`; 184 focuses, 196 connectors, zero crossings, zero node intersections, zero too-close pairs, zero long connectors, maximum horizontal span 8, maximum Manhattan span 9 | Accepted by parent and later implemented in the current direct tree; source was restored at the original handoff pending parent application; imported-node visual/layout proof remains blocked |

Candidate 2’s exact coordinate map is:

| Focus id | Baseline `(x,y)` | Candidate 2 `(x,y)` |
| --- | --- | --- |
| `independence_wave_raise_mass_reserve` | `(38,8)` | `(38,9)` |
| `independence_wave_build_professional_core` | `(40,8)` | `(40,9)` |
| `independence_wave_fund_domestic_arsenals` | `(42,8)` | `(42,9)` |
| `independence_wave_accept_foreign_arms` | `(44,8)` | `(44,9)` |
| `independence_wave_adopt_border_defense` | `(46,8)` | `(46,9)` |
| `independence_wave_adopt_reclamation_doctrine` | `(32,8)` | `(48,9)` |
| `independence_wave_found_professional_defense_institution` | `(40,9)` | `(41,10)` |

No other focus moved; the parent remains at `(42,7)`, and the other three choice endpoints remain at civilian/autonomy `(34,8)/(36,8)` and league/independent command `(48,8)/(50,8)`.

## Source-level collision check for candidate 2

A read-only coordinate scan parsed 3,949 `focus` and `shared_focus` node definitions across all 34 files under `common/national_focus`, including `relative_position_id` resolution.

The scan found 353 Event 006-prefixed source node ids, including 169 `shared_focus` definitions; the target file has 62 root-level `shared_focus` references, and all 62 imported roots resolved to source coordinates.

There were zero duplicate Event 006 source definition ids, zero exact coordinate collisions at the seven candidate destinations against any Event 006-prefixed direct or shared-focus definition, and zero same-row coordinate pairs under the two-column spacing minimum.

One direct-focus vertical neighbor is present at `(48,8)` and `(48,9)`: `independence_wave_standardize_with_league` and moved `independence_wave_adopt_reclamation_doctrine`.

That pair has distinct coordinates one row apart; candidate 2’s direct-tree `hoi4.focus_inspect` reported zero node intersections, while the source scan found no imported Event 006 shared-focus node at the candidate destinations or within the same-row spacing threshold.

This source check establishes coordinate non-collision for the parsed Event 006 direct/shared definitions; it does not establish imported-node attachment or connector-path clearance in the assembled in-game tree.

Candidate 2’s temporary source SHA-256 was `05FFFF53EAC51A18F5E2223C36AF6D748A50DAA4A8802B0186755A746169629B`.

Comparing candidate 2 against the immutable baseline after removing only `x` and `y` lines returned `NonCoordinateSourceUnchanged=True`; IDs, imports, prerequisites, mutual exclusions, rewards, AI blocks, and other source were unchanged during the candidate.

At the original candidate handoff, the final copy restored from the immutable baseline had SHA-256 `B38C72F1000E326EE8D63D7CB30DCDC2050D010CF38CBB7CC90D185EE39F12C2`; that handoff retained no source diff.

## Artifact links and visual retrieval

Baseline inspect JSON: [final restored inspect](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4a1f67ae3be26613cf404f90f8b1aaa7fa1e858fdcddbce14560fe155939aad/81aa69587981ca76873647b2eda9174c56ccca480519537e8771b7171f7ecba1/focus-inspect.9799263c16c7bed1.json).

Baseline render SVG: [focus render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f1075d909d746081ec6ff328167f365885b99d32b62a585bcab0af59b1c036b/601195d0b550c5ff05ec96670731350a52bcdad7d3cdbbf84c5ae3c05df876/independence_wave_focus_tree.focus.svg).

Baseline quarter-scale raster artifact: [focus raster PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c488ac42b6faeac23f71ac94d721efa3da02e27a2b25d3447e30d205a8a37fa1/dcd6372ee66558828e8729457478895eadc50404ec7a9a8195b62cffef1d31d4/independence_wave_focus_tree.focus.png), SHA-256 `c488ac42b6faeac23f71ac94d721efa3da02e27a2b25d3447e30d205a8a37fa1`, 5,356×610 pixels at `reviewScale=0.25`.

Candidate 2 SVG: [direct-tree render](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91f9bf70482761696315c748993c2d31332b4c6b10ec23a573cfb63ceb5d075c/7e26169180c036165b56a40df77cbd214b8c0bab15a429a8438c1e81b10e4447/independence_wave_focus_tree.focus.svg).

Candidate 2 PNG SHA-256 was `0165f08b9617a0aa5dce3999fa7553e6eb166eb9e762d33ba3d9a3126ce6ef92`; it is not a visual acceptance artifact because the MCP resource could not be retrieved completely.

The full-scale raster attempt returned `RENDER_DIMENSIONS_BLOCKED` because 21,424×2,440 exceeds the 16,384-pixel ceiling; the quarter-scale full-tree raster is too small for detailed lane review.

One 16,383-byte range from the baseline PNG was returned with a continuation URI, but subsequent range reads returned the exact error `Mcp error -32603: Artifact provenance manifest is unavailable`.

A later full-length raster read declared 173,513 bytes complete but returned only 47,202 base64 characters, decoding to 35,400 bytes; the image display reported `image content omitted because it could not be processed`.

No successful detailed visual review of the military lane was obtained.

## Bounded audit outputs

| Audit surface | Result |
| --- | --- |
| Route coverage in scope | The ten direct choice endpoints, five existing mutual-exclusion pairs, and capstone prerequisite groups remain unchanged; no route was removed or added |
| Missing or simplified content | No content patch was made; imported root-level `shared_focus` nodes remain omitted from MCP inspect/render, and the complete Event 006 content audit was not part of this geometry task |
| Icon references | Existing lane IDs retain their source icon references; inspect emitted no missing lane-icon diagnostic, but no independent asset or in-game icon review was completed |
| Localisation and rewards | No mismatch audit was performed; localisation keys and reward blocks were untouched and byte-identical in the coordinate candidate comparison |
| AI behavior | No AI audit or probability comparison was performed; AI blocks and focus weights were unchanged |

| Focus id | Existing icon id | Geometry-task coverage |
| --- | --- | --- |
| `independence_wave_adopt_military_archetype_program` | `GFX_goal_independence_wave_army_integration` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_confirm_civilian_control` | `GFX_goal_independence_wave_constitutional_state` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_grant_military_autonomy` | `GFX_goal_independence_wave_military_emergency` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_raise_mass_reserve` | `GFX_goal_independence_wave_army_integration` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_build_professional_core` | `GFX_goal_independence_wave_army_integration` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_fund_domestic_arsenals` | `GFX_goal_independence_wave_infrastructure_authority` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_accept_foreign_arms` | `GFX_goal_independence_wave_patron_client` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_adopt_border_defense` | `GFX_goal_independence_wave_army_integration` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_adopt_reclamation_doctrine` | `GFX_goal_independence_wave_high_chaos_sovereignty` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_standardize_with_league` | `GFX_goal_independence_wave_league_congress` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_preserve_independent_command` | `GFX_goal_independence_wave_army_integration` | Reference unchanged; no missing-icon diagnostic |
| `independence_wave_found_professional_defense_institution` | `GFX_goal_independence_wave_army_integration` | Reference unchanged; no missing-icon diagnostic |

At the restored baseline, the direct-tree reclamation connector at `independence_wave_adopt_reclamation_doctrine`, source line 825, from `independence_wave_adopt_military_archetype_program`, source line 807, remained the sole authored layout defect; the parent-applied candidate 2 repair supersedes that current-state finding.

The top-level baseline inspect also reports the unrelated vanilla localisation warning for `continuous_restrict_freedom_desc`; it is outside this task.

## Files, checks, and remaining blocker

At the original candidate handoff, only this document was retained and `common/national_focus/006_independence_wave_focus.txt` was restored exactly to the supplied baseline; the parent later applied candidate 2 as recorded above.

No focus IDs, prerequisites, rewards, AI, localisation, icons, or `shared_focus` imports were changed, and no probability-bearing source was patched.

No tests or HOI4 launch were run, and no commit was created.

Candidate 2 is implemented in the parent-reviewed current source and has clean direct-tree MCP graph evidence; its earlier `accepted and queued` disposition is superseded.

Imported-node attachment and visual/layout evidence remain blocked because focus inspect/render omit the root-level `shared_focus` nodes; the later parent retrieval of the current overview raster does not include imported nodes or a detailed military-lane crop.

The source-level coordinate scan and current direct-tree MCP diagnostics support candidate 2 as a non-colliding implemented direct-tree improvement; they do not establish connector-path clearance or visual acceptance for the assembled tree including imported nodes.

## Skills

Applied `chaos-redux-focus-trees` and consulted the required Event 006, decisions/missions, event-assets, and subagent skill guidance for this bounded focus task.

No skill was created or updated; `chaos-redux-improvement-loop` was not used because this was not a route-depth or route-design task.
