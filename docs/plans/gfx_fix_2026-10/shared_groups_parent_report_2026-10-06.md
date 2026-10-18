# Shared graphics repair parent report

This report covers the 188 original findings across the 28 assigned shared and system groups, plus seven small-counter defects discovered during the required visual review.
The original severity counts are 25 severity-1, 93 severity-2, and 70 severity-3 findings.
The accepted source is `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md`, its 16 cross-cutting rules, and the unchanged `gfx_issues.json` beside it.
The task excludes `countrystateview` and `countrytechtreeview`; those owners retain their files.

Status: implementation and parent review are ongoing for the final achievement and equipment tranches.
Historical portrait finals and successful MCP GUI evidence remain explicit completion gaps.

## Group coverage and commits

Each linked group report retains the per-finding disposition, exact textures, sources, processing evidence, and remaining consumer checks.
Commit identifiers below refer to implemented artwork and wiring; an accepted external package is identified explicitly.

| Group | Original rows | Findings and changes | Commits and disposition |
| --- | ---: | --- | --- |
| [countryoccupationview](countryoccupationview_report.md) | 1 | Painted occupation skull replaces the last strip frame; first 17 frames remain pixel-identical. | `e69df23f5`; implemented. |
| [mapmodes_interface](mapmodes_interface_report.md) | 4 | Wheat and migration selected/unselected pictograms are complete, solid and contained at 20x18. | `e69df23f5`; implemented, engine-render gap. |
| [frontendmainviewbg](frontendmainviewbg_report.md) | 1 | Black bars removed with native scene extension; exact 1920x1440 BC1 background. | `e69df23f5`; implemented, engine-render gap. |
| [visual_consistency_repair](visual_consistency_repair_report.md) | 16 | Eight category icons gain transparent margin; seven zombie category scenes share thin vanilla paper framing; Event006 assets independently accepted. | `62ad3457e`, `5f0340afe`; accepted external Event006 package recorded in the group report. |
| [_scientists_portraits](_scientists_portraits_report.md) | 5 | Fictional Aryan portrait corrected; authentic Otto source cropped without caption; bounded historical-source research completed twice. | `7a30b87c0`, `81ee08276`; historical finals/source gaps remain. |
| [alien_infantry_system](alien_infantry_system_report.md) | 2 | Large green and small white silhouettes become full-opacity same-unit busts with retained/verified frame-2 art. | `37e369007`; implemented. |
| [portal_raider_system](portal_raider_system_report.md) | 2 | Opaque hooded silhouettes and clear ring/bar NATO glyph replace faint counters. | `37e369007`, source lineage `3b08d3268`; implemented. |
| [clone_system](clone_system_report.md) | 7 | Four large/small/text counter strips repaired; wide vat-access equipment drawing restored at 131x52. | `001014065`; implemented. Hidden access technology is not claimed as a visible research node. |
| [germany_mengele_world_order](germany_mengele_world_order_report.md) | 1 | Three pale nodes and their required red links become solid and centered within the existing 32px consumer. | `8c8d5c9ba`; implemented. |
| [shared_chaosx_ability](shared_chaosx_ability_report.md) | 8 | Native-size review confirms consistent masks/winged variants and no row spill. | Accepted external `cc5f0e876`. |
| [shared_chaosx_achievements](shared_chaosx_achievements_report.md) | 21 | Distinct object medals, clearer unlocked accents, unified laurels, consistent grey/X states, and per-subject 005 framing review. | `1706a8445`, `544ef6ab9`, `b25b18589`, `b6bc6b421`, `e53a03a9a`, `aa6d07040`; accepted external `18bf22a36`. Remaining 005 framing is in production. |
| [shared_chaosx_buildings](shared_chaosx_buildings_report.md) | 3 | Original Gulag camp is separate from concentration/extermination camps; strip gains frame36; facility aliases use their real dark-plate cells. | `147e8db7a`; implemented without editing the excluded state-view file. |
| [shared_chaosx_characters](shared_chaosx_characters_report.md) | 7 | Three fictional small portraits corrected; actual Chigi authentic source placeholder installed; ZZZ/THR current packages accepted. | `7a30b87c0`; collective and Chigi painted finals remain pending. |
| [shared_chaosx_decision_category_pictures](shared_chaosx_decision_category_pictures_report.md) | 1 | Space Race scene becomes a restrained sepia V2 category picture rather than a mismatched collage. | `806e07083`; implemented. |
| [shared_chaosx_decisions](shared_chaosx_decisions_report.md) | 2 | Rocket exhaust fits within its roundel; doom skull uses the flat beige 34px convention. | `c5d4b8f01`; implemented. |
| [shared_chaosx_dynamic_modifiers](shared_chaosx_dynamic_modifiers_report.md) | 1 | Contamination glyph is a solid orange line symbol with clean margin at 30x20. | `b23031359`; implemented. |
| [shared_chaosx_equipment](shared_chaosx_equipment_report.md) | 11 | Seven separate 131x52 cylinders, seven original 70x43 shells, 27 complete 56x42 air modules, a transparent golem bust, distinct Tabun projectile and Livens archetype; protected research icons retain their original textures. | `d3c613a2c`, `08ed41a37`, `55b2efa02`; four rows remain in production and Tularemia wide art is blocked. |
| [shared_chaosx_formable_state_puzzles](shared_chaosx_formable_state_puzzles_report.md) | 5 | 272 exact-mask palette/ring textures, eight geographic-anchor-preserving GUI shifts, nine canonical manifests, and 382 processed previews. | `8afe365b8`; accepted external FORM11/18 `1cb4d061f`; Friesland fragments are real islets and remain unchanged. Engine-render gap remains. |
| [shared_chaosx_gfx_cleanup](shared_chaosx_gfx_cleanup_report.md) | 3 | Flask and trefoil division-template emblems rebuilt with consistent transparent margins. | `2fd2f9258`; implemented. |
| [shared_chaosx_ideas](shared_chaosx_ideas_report.md) | 7 | Eleven icons repaired, including five mass-panic states; memorial receives its own coherent medal instead of a shared unrelated texture. | `248dd887e`; implemented. |
| [shared_chaosx_missing_unit_texticons](shared_chaosx_missing_unit_texticons_report.md) | 9 | Missing/faint symbols restored; same-unit silhouettes and verified vanilla NATO plates retained. | `37e369007`, `bc3a45d86`, `07e229d3d`; accepted external CBRN instruments. |
| [shared_chaosx_pictures](shared_chaosx_pictures_report.md) | 16 | All 16 inconsistent or poorly cropped report/news scenes replaced; reports use 210x176 sepia tilted cards, news uses 397x153 black-and-white. | `46b93c607`, `e74aa1e5f`, `02c541a64`; Tibet leaf wired. |
| [shared_chaosx_raids](shared_chaosx_raids_report.md) | 7 | Six distinct painted 32px icons replace aliases, indistinct objects and inconsistent symbols; scientist category/unit and portal leaves are wired separately. | `35142b2c4`; implemented. |
| [shared_chaosx_subuniticons](shared_chaosx_subuniticons_report.md) | 8 | Cannibal, coal, cave, zombie and elephant families gain coherent same-unit counters; obsolete chemical-tank row is retired. | `37e369007`, `d6280f69c`; accepted external CBRN and retirement packages. |
| [shared_chaosx_super_events](shared_chaosx_super_events_report.md) | 2 | AZL picture has no baked text; Final Silence gains its own visibly decayed terminal scene. | `4607d54f9`; final-silence leaf wired, main terminal unchanged. |
| [shared_chaosx_techtree](shared_chaosx_techtree_report.md) | 21 | Every raw technology-art row independently reviewed against the existing 21-icon painted CBRN replacement package. | Accepted external `38ae4996e`; no duplicate replacement artwork. |
| [shared_chaosx_texticons](shared_chaosx_texticons_report.md) | 12 | Eleven zombie strips, ghost and death glyphs repaired; correct CBRN/Livens packages adopted; obsolete tank row retired. | `37e369007`, `07e229d3d`; accepted external packages recorded in the group report. |
| [shared_chaosx_traits](shared_chaosx_traits_report.md) | 5 | Antarctic medal rebuilt; later Swedish rulebook medal and CBRN trait package independently reviewed and adopted. | `1109c6733`, reconciliation `29a62824e`; accepted external `18bf22a36`, `8450deaf8`. |

The seven additional G5 small-counter repairs are committed in `65b1bb762` and tracked separately from the original 188 rows.
They restore opaque frame-1 silhouettes on the installed vanilla two-frame convention without altering the accepted large-counter sources.

## Design decisions

The user's ban on baked text takes precedence over the plan's older GA/CG/Z and Roman-numeral suggestions.
Agent-specific palette and genuinely different silhouettes carry equipment identity.
Creative bitmap replacements were made with native ImageGen, with real alpha requested initially for transparent families.
Existing geometric map masks, verified vanilla NATO cells, and achievement state overlays were processed deterministically because their exact geometry is part of the accepted requirement.
The first thick zombie category frame, wrong-source-alpha puzzle v2, faint counter candidates, and weak achievement accents were rejected and retained as review history rather than installed.
The 005 scale row cites 46 subjects, while the current source contains 40 registered and five unregistered legacy color textures; the 45 verified assets were reviewed without inventing a missing 46th or registering an orphan.
Protected 64px research art is separated from wide equipment textures only where consumer inspection proves that both uses exist.

## Meaningful validation and limits

Parent review includes native and enlarged before/after contact sheets, installed consumer inspection, exact processed-preview versus decoded-DDS comparison, alpha bounds and readable margins, and guarded promotion against frozen originals.
The final chemical-air tranche independently passes all 27 installed DDS versus approved-preview comparisons in `docs/assets/gfx_fix_2026-10/shared_chaosx_equipment/evidence/chem_air_variant_parent_independent_27.json`.
The 63 Event020/027/028 achievement states independently match canonical-template/source composition, and the 60 Event005/010/016/019 selected states independently match their approved processed review pixels and native-source/prompt hashes.
The coal, Tabun and Livens-archetype outputs independently match their approved processed PNGs; all checks use the actual installed DDS files.
Fresh `report_colour_audit.py` passes for 004,048,074,092 and `_chaosx_news` found zero reached title/description keys containing colour codes; separate final JSON results are retained beside the pictures evidence.
The puzzle package independently passes all 272 pixel comparisons, current manifest hashes and canonical digests; the preserved original core coordinates agree with all eight GUI leaves.
The original first 17 occupation frames and first 35 building cells are pixel-identical to their frozen baselines.
Current accepted external artwork was decoded and viewed instead of accepted solely from its handoff status.
Exact paths, source revisions, installed examples, commands, hashes and task-specific audits remain in the individual evidence packages.

HOI4 MCP tools are exposed, but the live transport closed after earlier stalls/timeouts.
Every affected puzzle window received matching before/after inspect and render requests; all 24 returned `Transport closed` and produced no engine PNG or validation artifact.
Those requests/results are retained in `docs/assets/gfx_fix_shared_chaosx_formable_state_puzzles/parent_mcp_gui_before.json` and `parent_mcp_gui_after.json`.
The menu/map requests and narrow technology inspection likewise have no successful engine render; source-derived sheets and map mosaics are not described as engine-equivalent evidence.
No game or desktop window was launched.

Two workers accidentally invoked the old external sheet script with `--help`; it has no argument parser and overwrote external review JPGs/index files before their processes were stopped.
The plan and raw issue JSON remain unchanged.
The incident is recorded, and subsequent before/after comparisons use isolated frozen DDS/LFS baselines and task-owned sheets; overwritten global JPGs are not original-review evidence.

## Remaining issues and simplifications

The achievement and equipment production/integration rows identified above remain ongoing at this draft's revision.
The Tularemia wide equipment image was refused by ImageGen twice at output moderation; both exact requests/results are preserved, the old consumer remains unchanged, and no replacement or substitute was installed.
Six historical painted finals remain user-supplied: Otto Ambros, Weigl, Rascher, Dufraisse, Ludovico Chigi, and the Event001 collective.
Weigl, Rascher and Dufraisse also lack eligible attributed frontal source photographs after bounded primary-source research; their rejected candidates and reasons are recorded.
Authentic Otto, Chigi and collective photographs are explicitly pending source placeholders rather than finished painted portraits.
Successful MCP GUI render/compare evidence and the orchestrator's live consumer checks are still missing.
Some original puzzle `source_png` files remain absent; preserved DDS masks and exact reconstructed processed previews are identified honestly rather than called original source layers.
There are no unapproved design substitutions; the accepted source-restoration, genuine-islet no-change, external-package adoption and obsolete-asset retirement dispositions are stated above.
The whole task is incomplete while the named production, portrait and engine-evidence gaps remain.

## Exact orchestrator live checks

Use separate 1936.1.1 fixtures at 1920x1080 UI scale1, then repeat the contained-icon and popup checks at 1440x1080.

| Surface | Setup and actions | Expected visible result |
| --- | --- | --- |
| Frontend, map modes, occupation | Inspect the menu at both resolutions; enter a country, select and deselect Famine/Migration map modes; use CXT's occupation fixture to inspect all 18 policy icons. | Full-bleed river scene; complete wheat/people silhouettes in grey/beige; final painted skull with the preceding 17 frames unchanged. |
| CXT counters, buildings, equipment | Start as USA, run `e chaosx_test`, advance beyond its one-hour receiver, then use the existing Apply Registered Systems, Refill Equipment and Deploy Test Formations debug decisions. Inspect division designer, map counters in both icon modes, tooltips, stockpile and equipment designers. | Opaque green large symbols, white on-map silhouettes, correct filled NATO plates and clear small glyphs; distinct Gulag cell36; clean wide cylinders, distinct shells and complete 56x42 air variants. |
| Space Race and doom | In a separate USA fixture open `event chaosx.nr44.2 USA`, inspect Space Race category/picture and its rocket badge; inspect the doom intervention decision when its ordinary prerequisites are met. | Restrained sepia rocket scene, contained exhaust with margin, and flat beige skull fitting the decision row. |
| Report/news images | In a separate USA fixture open report popups `chaosx.nr4.2`, `chaosx.nr92.2`, `chaosx.nr74.2`, `chaosx.nr48.2`; open news `chaosx.news.73`, `.65`, `.74`, `.51`, `.54`, `.41`, `.68`, plus the Tibet consumer named in the pictures report. | Thin tilted sepia report cards and full-canvas monochrome news; correct focal crops, no modern podium or atlas lettering. Railway, foreign-liaison and Balkan art are registry-only where source lookup found no active consumer; do not invent trigger commands for them. |
| Super-events | Separate USA fixture with `world_end_fallout` unset: `e set_global_flag = { flag = super_event_visible value = 2 days = 30 }`; close it, then repeat with value8 and value9. | Text-free AZL picture; intact main terminal and clearly decayed Final Silence terminal remain visually distinct. |
| Puzzle windows | Open North Sea, Scandinavia, GOE Hindustan, Maghreb, Greater Italy and Latin Africa formable detail windows; inspect both unmet/qualifying variants and hover each of the eight markers listed in the puzzle report. | Rings keep the geographic core centered, retain transparent padding, fit the 440x180 map and show the same state tooltip; no collisions or duplicated tooltip targets. Repeat both screen sizes and test click/hover rectangles. |
| Achievements | Inspect color, grey and not-eligible states of Events005,007,010,016,019,020,023,024,027,028 and031 in the existing achievement interface using its ordinary state fixtures. | Coherent laurels, distinct unclipped focal objects, visible unlocked color, fully grayscale locked art and one canonical red-X overlay. Verify all 005 repaired subjects against unchanged sibling plate/laurel placement. |
| Ideas, raids, traits and portraits | Inspect repaired national spirits including all five mass-panic states; open the scientist/chemical/cure raid selection map; inspect Antarctic/Swedish/CBRN medals; inspect the fictional DHO small cards and Aryan portrait, then the Otto/Chigi/collective source placeholders. | Clear native-size emblems, distinct raid silhouettes and clean margins; correctly sized fictional portraits; historical photographs remain visibly marked pending in documentation and are not treated as final painted art. |

## Skills used and maintained

Used: `chaos-redux-event-assets`, `imagegen`, `chaos-redux-subagents`, `chaos-redux-shared-git-commit`, `chaos-redux-scripted-gui`, `chaos-redux-super-events`, and `skill-creator`.
Updated the asset skill with frozen-baseline/isolated-sheet safeguards, research-palette matching and actual-consumer inspection; updated the shared Git skill with explicit LF patch-byte handling.
Those reusable changes are committed in `a7304582f`, `3ed75a3ad`, and `8723e12a4`.
No spreadsheet or export CSV was edited, and no catalog wording change is required by these asset-only repairs.
