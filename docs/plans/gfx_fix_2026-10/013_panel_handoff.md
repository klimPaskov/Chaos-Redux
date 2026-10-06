# Event 013 damaged abnormal-map panel handoff

Status: the parent-accepted candidate is installed at the preexisting runtime path, and matching synthetic baseline/post GUI renders are locally archived and visually reviewed. The parent inspected the full baseline/post renders and accepted the asset comparison: the central crack is clear while text, buttons, the panel grid, and the single-card fixture remain aligned and readable. Full GUI completion remains unresolved because gui_inspect timed out, the root scripted-GUI visible predicate remains unresolved in the preview, and the renderer reports existing layout and state-coverage warnings.

## Event ownership and scope

Event: 013, natural_disasters.

The dedicated window natural_disaster_abnormal_path_window is defined in interface/013_natural_disasters.gui and is labeled Event 013 ABNORMAL DISASTER PATH MAP in that file. The owner comment in common/scripted_guis/013_natural_disasters_scripted_gui.txt identifies natural_disaster_abnormal_path_gui as a player-only Evolution III/manual-abnormal surface. It is an event-owned window, not the shared event log or event-details framework.

The script's entry path is the existing natural_disaster_open_abnormal_gui effect in common/scripted_effects/013_natural_disasters_effects.txt:13164, called by Event 013 event chaosx.nr13.4 at events/013_natural_disasters.txt:169 and by decision natural_disaster_review_abnormal_path_map at common/decisions/013_natural_disasters_decisions.txt:99.

Exact GUI identifier: natural_disaster_abnormal_path_window.

Exact scripted-GUI identifier: natural_disaster_abnormal_path_gui.

Exact GFX registration: GFX_013_abnormal_disaster_panel_damaged in interface/013_natural_disasters.gfx:124, pointing to gfx/interface/013_natural_disasters/013_abnormal_disaster_panel_damaged.dds.

Clean comparison alias: GFX_013_abnormal_disaster_panel, still pointing to gfx/interface/013_natural_disasters/013_abnormal_disaster_panel.dds.

Exact GUI elements: natural_disaster_gui_damaged_panel and natural_disaster_gui_normal_panel in interface/013_natural_disasters.gui.

The damaged element is selected by natural_disaster_gui_damaged_panel_visible when the selected record result is greater than the normal result; the clean element is selected by natural_disaster_gui_normal_panel_visible when the selected result equals normal. The triggers are in common/scripted_guis/013_natural_disasters_scripted_gui.txt:399 and :403.

The source uses natural_disaster_animations_disabled; the parent brief's animations_disabled label was shorthand. The render fixture uses the exact source flag.

## Accepted design and reference

The parent task explicitly accepts the user's plan row at C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md:596, directing visible main-pane cracked glass, a soot mark in a corner, a torn left paper edge, and an unchanged panel grid.

The baseline reference is docs/assets/gfx_fix_parent_2026-10/013_damaged_before.png. Candidate 04 is docs/assets/gfx_fix_disaster_panel_resume/source_png/013_damaged_candidate_04.png, with its 760x520 processed view at docs/assets/gfx_fix_disaster_panel_resume/processed_png/013_abnormal_disaster_panel_damaged_760x520.png.

The parent reviewed candidate 04 at native 760x520 against the saved original and accepted it because the light pane crack is distinct, damage remains localized, and all five slots, dividers, and usable regions are preserved.

The prompt and immutable candidate lineage are in docs/assets/gfx_fix_disaster_panel_resume/prompts/.

The region-to-native mapping, source bounds, asset states, acceptance basis, and resolution targets are in docs/assets/gfx_fix_disaster_panel_resume/reference_mapping.md.

## Native mapping and visual rationale

The full opaque background canvas is 760x520 and appears in a 1087x744 window through iconType elements at scale 1.43. The GUI source comments describe the header, five-slot left column, path canvas, right detail panel, legend tray, and severity strip.

Candidate 04 adds thin glass cracks within the largest central pane, a short tear confined to the outer-left paper trim, and a small soot mark on the upper-right outside rim. The cracks do not draw map paths or labels, the paper tear does not replace a card, and the soot does not cover the right detail pane or header text. Buttons, text, dynamic values, click regions, hover states, and all gameplay information remain separate native elements.

Before the patch, the parent plan reports that the two 760x520 panes differed by a mean pixel difference of 4/255 and looked indistinguishable side by side. After the asset replacement, the damaged state has a distinct crack, corner soot, and torn edge while preserving the clean panel and all native source definitions.

No layout adaptation, fake control, baked text, localization change, gameplay change, cost change, AI change, or GFX registry change was made.

## Changed files and identifiers

Installed runtime asset: gfx/interface/013_natural_disasters/013_abnormal_disaster_panel_damaged.dds, now SHA-256 68e5b6d2b49dd87ed8491d04ac88644138773eb6a663b045c9b71ce273ec4978.

The replaced pre-change DDS is preserved at docs/assets/gfx_fix_disaster_panel_resume/source_dds/013_abnormal_disaster_panel_damaged_original.dds with SHA-256 c79bd8e079371fc5e0a725c798f1682a669edb23fbcc6fdd19479e311be8489b. The parent-provided decoded original remains at docs/assets/gfx_fix_parent_2026-10/013_damaged_before.png with SHA-256 d11a64d6eb077db0cdd34172f514f4cced12b1fc9b91efe214690ae7ca08d339.

The existing GFX alias and texture path were reused; interface/013_natural_disasters.gfx and interface/013_natural_disasters.gui were not edited.

Documentation and source PNGs are in docs/assets/gfx_fix_disaster_panel_resume/, including the manifest, four full prompt records, reference mapping, processed preview, temporary conversion candidate, and original DDS backup.

No scripted-GUI, localization, event, decision, effect, trigger, shared registry, spreadsheet, or other GUI source was changed.

The linked source identities read before installation were: interface/013_natural_disasters.gui SHA-256 c5f3c5274aeeb9161769ebb2fd4d0a16461aab10a04401f8a590a8720c62791f; interface/013_natural_disasters.gfx SHA-256 376d56d4fc010dd35d5a9522bce2b47bd224d8e6b38f174f1c87d0bb3efbfe18; common/scripted_guis/013_natural_disasters_scripted_gui.txt SHA-256 513d0aa2e298d5561f480da34df3778797328f42b11872eebfc056c7d958921a; events/013_natural_disasters.txt SHA-256 fe29ce013f8a076b2f30ea6a75f4aab21ec89c5267d37954d5170b87e98c6718; common/scripted_effects/013_natural_disasters_effects.txt SHA-256 93a82c24e7870521c0914131c48a32142bf9523e4502d0ff42a8c77b417cafe8; common/decisions/013_natural_disasters_decisions.txt SHA-256 45ab9463291dd87694c11f67e25900ba56f8fd677f852f349babe9313b13b0f9.

## Sources and precedents inspected

The offline wiki Interface modding iconType section was read at lines 178-195, id d60f2d2e0d14a99d98f3b190050d656abc24f1dea889af1cd09479c963adabee, revision b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c. It identifies iconType as image content and documents spriteType, position, transparency, and related properties.

The offline wiki Scripted GUI modding window-assignment section was read at lines 40-67, id c3fdbebd7bd9df1124240c76a29539e6a348631e0bc2db4a42ff7440ffe75018, revision b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30. It requires window_name to reference an independent container.

Installed game documentation common/scripted_guis/_documentation.md was read at lines 1-146, id e6d2e249edc2c6865ee3d109cfb67e3e30ebafd179ff4f2cb6b6bc2eb1494322, revision 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838. Lines 1-80 document player_context, window_name, default parent behavior, visibility triggers, and element triggers.

The role-referenced references/visual-review.md file was not present under the scoped scripted-GUI skill or repository docs path. The relevant inline visual and usability checklist in chaos-redux-scripted-gui/SKILL.md was read and applied to the texture candidate; MCP visual evidence remains separately blocked as described below.

The offline Graphical asset modding spriteType section was read directly from paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md at lines 30-100 because hoi4.reference_read for returned id e71a709739ed01353c6300e5587cc50f7d653b44a95a9ddc3c31be8891d45f5b and revision f8e3d4ad382f4e5f8e170492a484d090bad62e3711cabfb5d3bf84e58ab32dd9 returned REFERENCE_SECTION_UNKNOWN. The section describes the GFX spriteType name and texturefile mapping.

The exact vanilla precedent was inspected in C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/sov_paranoia_system_scripted_gui.gui and common/scripted_guis/SOV_paranoia_system_scripted_gui.txt. It separates background, meter, and foreground iconType layers from scripted text and properties. hoi4.source_lookup resolved game:interface/sov_paranoia_system_scripted_gui.gui at line 1 under source revision 8b451fd20bc75be278fffe8dc7d491fcaaf19031d4e1e6437c0cf047963ece3a.

## Asset production and validation

Candidate 04 was produced with built-in ImageGen edit mode and preserved as a distinct source PNG. Candidate 01 was rejected for broad soot and tearing; candidates 02 and 03 were retained as rejected/intermediate lineage. Exact prompts, tool paths, input roles, dimensions, and hashes are listed under docs/assets/gfx_fix_disaster_panel_resume/prompts/.

The processed RGB preview is exactly 760x520, matching the clean comparison panel and existing damaged-panel canvas. The existing full-window image is opaque, so consumer_opaque was used; no transparency fallback was needed.

The repository converter .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py generated the 32-bit BGRA output. Its 128-byte header, DDS_HEADER size, pixel-format fields and masks, DDSCAPS_TEXTURE, dimensions, exact file size, and alpha range were checked. The DDS was decoded back to PNG and compared pixel-for-pixel with the processed preview; the images are equal.

The clean comparison panel's DDS hash is 180ba4da87137b04e332fd6497accbd2d2203828b206c5a0beff82139777f512 and remains unchanged.

## UI budgets and state matrix

This asset change adds no visible mechanic value, primary action, explanatory string, cost, or texticon. It adds no text to the artwork. Existing native UI values and actions remain unchanged and parent-owned.

Cost-count audit: this decorative panel texture introduces zero gameplay-changing controls and zero new costs.

Texticon coverage: no new cost or resource string is introduced, so no texticon is required.

State logic: normal panel is visible when the selected result entry equals normal; damaged panel is visible when the selected result is greater than normal. The panel open state uses natural_disaster_abnormal_map_open with natural_disaster_abnormal_map_available or the Evolution III logged flag.

Requested render matrix: 1920x1080 at UI scale 1.0 and 1366x768 at UI scale 1.0. The rejected visibility-override render is preserved under docs/assets/gfx_fix_disaster_panel_resume/renders/rejected_fixture_v1/. The corrected baseline and post runs each have a 1920x1080 full image, a 1920x1080 window crop, and a resolution-scale matrix containing both 1920x1080 and 1366x768 views; the MCP result did not emit separate full or cropped PNGs for 1366x768.

## MCP evidence and blockers

The exact baseline inspect call used mcp__hoi4_agent_tools__hoi4_gui_inspect for natural_disaster_abnormal_path_window with scenario id event013_abnormal_map_baseline_inspect, closedFlags true, natural_disaster_abnormal_map_open true, natural_disaster_abnormal_map_available true, and natural_disaster_animations_disabled true. It returned: tool call failed for hoi4_agent_tools/hoi4.gui_inspect; timed out awaiting tools/call after 600s. It returned no artifacts, source revision, hierarchy report, or click-region report.

The first render attempt was submitted in parallel with that inspect for event013_abnormal_map_damaged_baseline, two target resolutions, and the normal, hover, selected, active, disabled, warning, completed, empty-list, and full-list states. The outer exec was terminated after the MCP requests remained pending, so that attempt returned no render artifact and no source identity.

A second, narrow render was submitted for event013_damaged_panel_synthetic_baseline with closedFlags true, the exact open/available/animation flags, visibility keys damaged_panel=true and normal_panel=false, generated scenarios disabled, state normal, and both target resolutions at UI scale 1.0. It returned GUI_RENDERED with 27 artifacts under workspace mod_chaos_redux_ea3b2d67c2c0 and sourceRevision 9a9c2d1ca811d49769590e18166780835ebdc9c8dfe8e2a29c2d7ee77611b517.

The call had been submitted before installing the accepted texture but returned afterward, and the tool response does not identify the consumed DDS hash. Therefore its asset source state is unresolved and it cannot be treated as a matched pre-change or post-change render.

The returned scenario JSON records resolution 1920x1080 at UI scale 1, state normal, closedFlags true, the three flags, the two short visibility keys, and no scripted-GUI variables or values. The actual source visibility triggers are natural_disaster_gui_damaged_panel_visible and natural_disaster_gui_normal_panel_visible; the tool did not resolve the short keys. Diagnostic GUI_UNRESOLVED_VISIBILITY_OVERLAP says both background elements render together.

The full-window PNG is artifact SHA-256 bf521a987e6560c1ece16945cec11a2551291120ca4c3c505035ca81db63649b, provenance hash 3b442bda3e7cc0967a0b6d816539651689f78d387ea5a6616d8269ad99469d13, size 1,381,431 bytes. It was retrieved in 43 byte ranges of 32,766 bytes (final tail included), checked for complete contiguous coverage, PNG signature, total byte count, and exact SHA-256 before review.

The reviewed production render shows unresolved [dynamic_loc] values throughout the list, header, and detail panel. It cannot establish whether the crack, tear, and soot remain visible behind the populated native map and labels because the panel visibility fixture is unresolved.

The returned diagnostics also report GUI_RESOLUTION_DRIFT of 18.1% for the window and both panel layers between the requested 1920x1080 and 1366x768 modes, GUI_SPRITE_DECLARED_SIZE_MISMATCH for the existing GFX_tiled_window_transparent sprite, and missing coverage for hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states. These are renderer findings for the existing event-owned surface; the asset-only scope did not authorize a GUI-source repair.

The tool reports comparison.changedPixels=0 for the rejected first-pass single-scenario package; this is not a before/after source comparison. The later corrected fixture and matched render sequence are recorded below.

The exact returned artifact references share this resource prefix: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/{artifactSha256}/{provenanceHash}/{name}. The full render URI is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf521a987e6560c1ece16945cec11a2551291120ca4c3c505035ca81db63649b/3b442bda3e7cc0967a0b6d816539651689f78d387ea5a6616d8269ad99469d13/natural_disaster_abnormal_path_window-full.png. The scenario JSON is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db4e3713bcc1f83c0efc68ca048e08224fdd166102c465180b8564092d6d80f7/e17f27139558876b0bfe29aac4687ee2d188e1dde244b019cf9e09a2168b7a67/natural_disaster_abnormal_path_window-scenario.json.

The source-only asset preview and the parent's native-size candidate review establish artwork acceptance, not GUI renderer, scaling, state, resolution, hierarchy, or click-region acceptance.

### Corrected matched baseline and post-change render

The parent supplied a renewed fixture pass after the rejected output showed missing variable inputs. The corrected fixture is event013_damaged_panel_corsica_earthquake_partial_warning_fixture_v3 and uses the actual Event 013 variable arrays, not visibility overrides.

The returned layout JSON identifies natural_disaster_gui_normal_panel as gui_element_fa08c56083949e17a341eceb and natural_disaster_gui_damaged_panel as gui_element_fdaa5991b637a30990986860. Both are iconType elements with the same parent gui_element_9d84a1a734dbbe2b9c3a6680 and the same 1086.8x743.6 bounds at x417,y168 in the 1920x1080 view.

The corrected visibility values are natural_disaster_gui_state_entries^num=1, natural_disaster_gui_selected_index=0, and natural_disaster_gui_record_result_entries^0=1. The result constants define normal=0 and partial=1, so the damaged background trigger passes and the normal background trigger fails. The fixture also supplies natural_disaster_gui_origin_family_entries^natural_disaster_gui_selected_index=1 to resolve the source layer predicates for the earthquake family.

The synthetic record uses installed vanilla state 1, Corsica; Event 013 family earthquake=1; abnormal severity=5; recovery record status=4; degraded card state=4; late reconstruction phase=3; recovery path status=6; population warning protection=1; no foreign relief=0; and no follow-up route=0. The visible scripted-localisation outputs come from Event 013 source: active header with one affected state and the unresolved-domain fallback; the one-card path queue; Earthquake, Abnormal, and Seismic; not-scheduled impact; recovery underway; the population-warning result; no follow-up; no foreign relief; and Late reconstruction. The scenario supplies these as values under the exact GetNaturalDisasterGui method names and supplies Corsica from state 1's installed localization.

Source hashes supporting those fixture values are: common/scripted_triggers/013_natural_disasters_triggers.txt 4630e30ab1c70e9151341ee94ec1f87244525cefcdda6d9f93e37e62a05ed00c; common/scripted_localisation/013_natural_disasters_scripted_localisation.txt e4e7ba2184747c6dd19165f22077fcd5f7f77fea1ec1f17c30917c9b75c34196; common/script_constants/013_natural_disasters_constants.txt 9497e89bb172cb5bc50f3ff83b572736ec2c46b985956c5a9a6a9fc343dbedbe; localisation/english/013_natural_disasters_l_english.yml c05cb702c59f7dbaad369850f4bfcede99a5dcb7ea615bc17ae137d6601e59e0; vanilla history/states/1-France.txt 445eb44bab28c76b55979cd7d699bdf1fd17655c55cfff5c9a29cff1c7161b6b; and vanilla localisation/english/state_names_l_english.yml f7247c8df59674f02a68358761bd6f2b6509364354baf6e6a5a1121d9a2641a7.

For the corrected baseline, the archived original DDS was installed at the sole owned runtime texture path and verified at SHA-256 c79bd8e079371fc5e0a725c798f1682a669edb23fbcc6fdd19479e311be8489b before the call. The corrected render returned GUI_RENDERED with 27 artifacts, sourceRevision 68259080f629b36d2330b4bcf706f3763dde93591d2035bda9eaee2176cdc2a1, resolutionCount=2, scenarioCount=1, and fidelity unresolved count 1.

The corrected baseline full PNG is artifact SHA-256 f21c6fdd4fceca69c8be35a55925fda9933bbd21a0a84a1373a7d708d19aa858, provenance hash f945f6dd03b0eb1b2baedbee823805f9d5b0184fccfab7507043224b69552bf2, size 1,377,371 bytes. It was retrieved in 43 byte ranges and verified for contiguous coverage, PNG signature, total byte count, and SHA-256 before review.

The baseline image shows one Corsica card, the damaged panel layer, no volcano overlay, resolved visible text, and a clear central map pane beneath the marker. It is usable for comparing the added crack, left tear, and upper-right soot.

Candidate 04 was restored immediately after the baseline call and the runtime DDS was verified at SHA-256 68e5b6d2b49dd87ed8491d04ac88644138773eb6a663b045c9b71ce273ec4978. The post-change render used the identical stored scenario and resolution matrix and returned GUI_RENDERED with 27 artifacts, sourceRevision 6d870dd3b34db5eeb212c08993eb9972e72853acaa0ef99a0fd2ba3cc2a0e410, resolutionCount=2, scenarioCount=1, and fidelity unresolved count 1.

The post-change full PNG is artifact SHA-256 e4aa88f0bc950b9e584a2d2235c3e0218d36217da8018581995e133283b73afc, provenance hash c01e5762e14f3cd05b0f11efb4ebda35ca0de7ee059bf03a301a238c7fb2b448, size 1,183,161 bytes. It was retrieved in 37 byte ranges and verified for contiguous coverage, PNG signature, exact byte count, and SHA-256 before review.

The post full-window and cropped renders visibly add the central-pane crack and retain the left-edge tear and upper-right soot while keeping the native card and pane grid, labels, values, buttons, and marker alignment unchanged. The baseline and post full/cropped images use the same fixture, 1920x1080 and 1366x768 resolution matrix, UI scale 1, language, flags, variables, and scripted-localisation values; the old versus candidate DDS hashes are the only intended source difference.

The post click-region and hierarchy artifacts confirm the background icons remain non-clickable and do not create new hit regions. The damaged icon is shown at the source-declared 1086.8x743.6 bounds; the normal icon is hidden. The renderer state is normal for controls while the selected record result value 1 drives the damaged background branch.

The remaining fidelity JSON's single unresolved item is natural_disaster_abnormal_path_gui.visible, whose source requires is_ai = no. The scenario supplies the open and available flags and all displayed data, but the offline view does not confirm the player-context AI fact. No live engine behavior is claimed.

The installed MCP package docs/gui.md scenario-field section at line 187 documents named scopes, and its line 108 example binds an actor tag inside FROM. It does not specify a player_context root binding for resolving is_ai = no; no guessed actor scope was added to the render fixture.

The baseline diagnostics still report GUI_RESOLUTION_DRIFT of 18.1% at 1366x768, GUI_SPRITE_DECLARED_SIZE_MISMATCH for the existing GFX_tiled_window_transparent sprite, missing state coverage for hover, selected, locked, disabled, warning, active, completed, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation, plus GUI_ACCIDENTAL_CLIPPING and GUI_INVALID_SIZE for the intentionally hidden normal background at 0x0 bounds. These are existing event-owned GUI findings; this asset task does not authorize changes to .gui or gameplay sources.

The corrected baseline full-render URI is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f21c6fdd4fceca69c8be35a55925fda9933bbd21a0a84a1373a7d708d19aa858/f945f6dd03b0eb1b2baedbee823805f9d5b0184fccfab7507043224b69552bf2/natural_disaster_abnormal_path_window-full.png. The matched post full-render URI is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4aa88f0bc950b9e584a2d2235c3e0218d36217da8018581995e133283b73afc/c01e5762e14f3cd05b0f11efb4ebda35ca0de7ee059bf03a301a238c7fb2b448/natural_disaster_abnormal_path_window-full.png. The cached MCP artifacts have been copied byte-for-byte into docs/assets/gfx_fix_disaster_panel_resume/renders/ with a matching artifact manifest beside each file; every copied file's SHA-256 was checked against its artifact identity.

The local baseline files are docs/assets/gfx_fix_disaster_panel_resume/renders/baseline/full_1920x1080.png, cropped_window_1920.png, resolution_scale_1920x1080_and_1366x768.png, scenario.json, layout.json, validation.json, fidelity.json, annotated_1920.png, click_regions_1920.png, and state_matrix.png. The local post files are docs/assets/gfx_fix_disaster_panel_resume/renders/post/full_1920x1080.png, cropped_window_1920.png, resolution_scale_1920x1080_and_1366x768.png, scenario.json, layout.json, validation.json, fidelity.json, annotated_1920.png, click_regions_1920.png, state_matrix.png, and hierarchy.svg. The rejected first-pass full image and scenario are docs/assets/gfx_fix_disaster_panel_resume/renders/rejected_fixture_v1/full_1920x1080.png and scenario.json.

The repository .gitignore rule at line 80 ignores docs/assets/, so these local render copies remain available for review but will not be included by a normal git add.

Selected exact artifact hashes and provenance hashes are listed below. Construct each resource URI with workspace id mod_chaos_redux_ea3b2d67c2c0 and the standard artifact/{sha256}/{provenanceHash}/{name} path.

| View | Baseline SHA / provenance | Post-change SHA / provenance |
|---|---|---|
| Full PNG | f21c6fdd4fceca69c8be35a55925fda9933bbd21a0a84a1373a7d708d19aa858 / f945f6dd03b0eb1b2baedbee823805f9d5b0184fccfab7507043224b69552bf2 | e4aa88f0bc950b9e584a2d2235c3e0218d36217da8018581995e133283b73afc / c01e5762e14f3cd05b0f11efb4ebda35ca0de7ee059bf03a301a238c7fb2b448 |
| Cropped PNG | a033265db5ccb1aaf6e1e71534ec6164702c4c5cccd01122e0674cf46fb709d4 / b7825c90dd0174f42db45c353fedb08f1cdb69a452ba5e67244a0be7a770eb66 | 89a636e52bd553a49ac8e2bf488dba109b845a4e7625ad7ef14713e9e5ad046a / a94a7aa0785e1e753f50cdab1fd412b8c2068b516f69d6128e8a5cc14758b7d7 |
| Annotated PNG | 9c34576459a823cb2047289139398f253b9ec321124642fbdf43224b6906f524 / b67359e2432c98d45882610c5eed3f1bf51192300df106b672a6584879b6aa35 | 10035a84ab43e7cca3cbad78722f65b7ccc58ab29250077ded0fa706893967e6 / 814bd3506b823787df968f821736b03e7f386f42261753af6cdf554865321d21 |
| Click-regions PNG | f3a8e41e1cf9b908bcdf78b51c860632912ef0fa638994a0b94cbc93e47ac5b0 / ae1b129a51fc3ff934c673dbce3b4a4f093d8f10045c78f5f7c2d9cc9fe15c9c | f302366987f89e1f8ac3ac02313196ff3267dcf6ad72e904e038d52fe6b50d4c / cb73fbe8899cac1b448c6cd18fabf6d72cc4cc0927045105894086c77f267fab |
| Hierarchy SVG | 73141ea88260c6e4f694c040054d6b15788278d2a8e79df3d8f9e4a1d0ccd2f7 / 49d9a7fb195ed42e8888404981aade94876d8cf95311be01e16712d48e5dbfe0 | 73141ea88260c6e4f694c040054d6b15788278d2a8e79df3d8f9e4a1d0ccd2f7 / 49d9a7fb195ed42e8888404981aade94876d8cf95311be01e16712d48e5dbfe0 |
| Layout JSON | c45a725f713a2f3fa2cdffb34af98fb4f231ba6476f56176a022186264adb93d / ba7115e844a2f40ed210b437193bbe8eab5704389ddd0b155e880a3a7826fcaa | c45a725f713a2f3fa2cdffb34af98fb4f231ba6476f56176a022186264adb93d / ba7115e844a2f40ed210b437193bbe8eab5704389ddd0b155e880a3a7826fcaa |
| Scenario JSON | a0019047ae581d2147f75fd4946b548bc4d45ce7f5842d36b5dab9029b3261d7 / a7293fd8930f132d37e2d209676133731228ca723de1488b2e6a80725fd3daac | a0019047ae581d2147f75fd4946b548bc4d45ce7f5842d36b5dab9029b3261d7 / 8acfaef738dc1155f168a5333102c9df75d99b658cce41f67d3ccfe22fe92e3b |
| Fidelity JSON | 7886703b6f63e6994e6303f045a595d1b686a94cc13b4e1de815dc34e9cd38e1 / f505a12cecc4ed08f1d53902db1d3f9122b265a9c3874d855ef59c2f4a0fefe7 | 7886703b6f63e6994e6303f045a595d1b686a94cc13b4e1de815dc34e9cd38e1 / 17e8dc496b927e90dec24fb5ddcd2b23908f072810b1b07143ecbd886ef4050f |
| State-matrix PNG | b5279aa3e7863cd9b80353281e42e6a684983531a8e35dac82292a9a775cd110 / 3dea6b5e2daa7ec2ddede03bf073b688f7b1de6adc03e6a8c535e7a04a94397a | c6089d3405ef55425995f50e49b0caf5d9ba481d06226100643fbb7819a5de01 / 152d027451a9a64902684e35c82d55a4f186d53d0112cb9690c3ad5146be6f06 |
| Resolution-scale PNG | 8b33d400684f071c1aa556662754ec306fb6d91dd04bcd885c2e1630b99c4b68 / 40e85cf6828518ecac2d73f931863bf3657e56d371707c0644138ceeb45dd171 | 10abb3b5d5715c436fb65be35ac00cfaf2e3f1d668e7c1397216ff49611ddbbf / d46521ad4210544eacfb879b0fe649b79e2e0cc0d4116681c8520f32f60cee6a |

There is no separate GUI source-comparison tool. The visual before/after review used the full and cropped PNGs from the same fixture and resolution matrix; the visible delta is the new crack and localized damage. The renderer's single-scenario comparison.json reports zero changed pixels and is not used as the before/after proof.

## Before and after

Before, the existing damaged and clean panels were visually indistinguishable according to the accepted plan. After installation, only the damaged DDS differs: the main pane has a thin glass crack, the outer-left paper edge has a short tear, and the upper-right rim has a small soot mark. The normal panel, GUI hierarchy, state triggers, control layout, hit regions, text, decisions, costs, effects, and gameplay remain unchanged.

The installed damaged texture uses the already-registered GFX_013_abnormal_disaster_panel_damaged alias and preserves the original runtime asset in the workspace backup. No runtime wiring edit was required.

## Remaining review

Parent review of candidate 04 is complete and accepted. The matched synthetic baseline and post-change renders have been inspected; parent disposition remains necessary for the unresolved root visibility fact, resolution drift, hidden-element size diagnostics, and uncovered GUI states.

The user owns live in-game consumer validation. No game process was launched.

Unresolved: gui_inspect timed out after 600 seconds; the first narrow fixture was rejected; the matched synthetic renders retain one unresolved root visibility fact, 18.1% resolution drift, zero-size warnings for the intentionally hidden normal background, and unrendered hover, selected, locked, disabled, warning, active, completed, empty/full-list, value-boundary, long-text, and missing-localisation states. The asset repair is visually demonstrated in matched synthetic renders, but full GUI and in-game completion are not claimed.
