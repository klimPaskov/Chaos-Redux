# Event 006 dedicated status GUI handoff, 2026-10-06

## Disposition

The dedicated Event 006 status window received three narrow presentation repairs: the title and tab heading use plain status wording, the animation tooltip describes the decorative ring accurately, and the severe-instability badge uses the danger frame when it appears.

The static recognition, dependency, League, and formable symbols remain visible with animation on or off. The optional eight-frame bronze ring overlays those symbols without replacing or changing their meanings.

The final visual pass includes one explicit root scenario for each of the five tabs at 1920×1080 and 1366×768, UI scale 1, plus a Government animation-on view, a Government animation-tooltip hover view, and a severe-warning view before and after the final badge-frame repair. The full evidence and hash-verified PNGs are under docs/plans/006_independence_wave_plans/subagent_handoffs/evidence/gui_takeover_20261006/current_render/.

The user performs live game validation. This handoff claims source-model review only.

No commit was made by this worker; the parent owns the final commit and integration.

## Event ownership and acceptance basis

Event id and slug: 006_independence_wave.

The dedicated window is independence_wave_status_window in interface/006_independence_wave.gui. Its presentation binding is independence_wave_status_scripted_gui in common/scripted_guis/006_independence_wave_scripted_gui.txt. The Event 006 entry point is independence_wave_founding_category in common/decisions/categories/006_independence_wave_categories.txt.

Part 3 of the accepted Event 006 specification explicitly assigns this compact window and names its values, supporting status, tabs, and state cues. The source of truth is docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md, lines 320-344. The parent corrected the initial Part 2/Part 6 attribution and confirmed Part 3 as the ownership authority.

The parent accepted preserving the institutional-board composition and all controls. The parent explicitly accepted all five country values and five tabs for this panel. The parent also accepted keeping semantic state symbols visible while optional motion adds a state-neutral ring.

After reviewing the severe-instability render, the parent authorized one surgical frame correction in the existing status window. No gameplay, cost, AI, scripted outcome, shared UI, or asset source was changed by this worker.

The initially named interface/006_independence_wave_statehood.gui file does not exist in this workspace. The widget lookup confirmed that independence_wave_status_instability_warning is owned by interface/006_independence_wave.gui at line 25, so the authorized one-line repair was applied to that actual event-owned layout file without creating a duplicate window.

The window is event-owned. It does not own the shared event log, event details, settings, super-events, shared registries, formable state-puzzle interfaces, or unrelated GUIs.

## Surface and identifiers

The window id is independence_wave_status_window. The scripted GUI id is independence_wave_status_scripted_gui. The category entry point is independence_wave_founding_category.

The seven buttons are independence_wave_status_toggle_animation, independence_wave_status_refresh, independence_wave_status_tab_government, independence_wave_status_tab_recognition, independence_wave_status_tab_security, independence_wave_status_tab_league, and independence_wave_status_tab_ambitions. The five mutually exclusive detail panels are independence_wave_status_government_panel, independence_wave_status_recognition_panel, independence_wave_status_security_panel, independence_wave_status_league_panel, and independence_wave_status_ambitions_panel.

The five visible country values are legitimacy, recognition, government capacity, security readiness, and post-release instability. Supporting status groups show the former host, strongest patron, network and League phase, founding phase, and active commitments. There are no displayed spendable costs or texticons.

The four static status sprites are GFX_independence_wave_recognition_seal_states, GFX_independence_wave_dependency_warning_states, GFX_independence_wave_league_charter_activation_states, and GFX_independence_wave_formable_eligibility_seal_states. Their animated siblings are the existing *_animated aliases in interface/006_independence_wave.gfx. The separate severe-instability badge is independence_wave_status_instability_warning.

## Reference and native mapping

The accepted composition reference is docs/plans/006_independence_wave_plans/references/006_event6_network_standing_league_explanation_reference_2026-09-27.png, SHA-256 1892B363E3ADC35C5E15E10F84E022740D8F4C52A20311C3D9D5F27A96F4A469. The companion standing reference is docs/plans/006_independence_wave_plans/references/006_event6_network_standing_reference_2026-09-27.png, SHA-256 3CFB12E90AE8603A30F2279FD066ED05D4A638EC9817E14EEF9A9BA486CF6A21.

The annotated baseline reference is docs/plans/006_independence_wave_plans/references/006_event6_statehood_status_baseline_annotated_2026-10-06.png, SHA-256 427ADE6DBF57EA9B05624F9FBB2702425C1502FB39E79DF79BB7601D73F5CCDE. The native-element mapping and acceptance record is docs/plans/006_independence_wave_plans/references/006_event6_statehood_status_baseline_mapping_2026-10-06.md.

| Reference region | Native element and bounds | State mapping |
| --- | --- | --- |
| Painted board | independence_wave_status_panel_background at (0,0) in a 700×500 window | Decorative background; live values and controls remain native. |
| Title and subtitle | Title at (26,16), max 510×30. Subtitle at (28,48), max 520×34. | Native instant text uses hoi_24header and hoi_16mbs. |
| Utility controls | Animate at (526,16), 78×26. Refresh at (610,16), 64×26. | Native buttons; Animate toggles the decorative ring, and Refresh keeps its existing refresh action. |
| Country values | Five rows begin at x=74, y=92/142/192/242/292. Matching icons begin at x=24. | Legitimacy, recognition, capacity, security, and instability. |
| Supporting status | Former host y=84-174. Patron y=184-248. Network y=258-322. Founding phase y=334-382. Active commitments y=386-450. | Host, patron, network, League, founding, and mission text. |
| Status symbols | Recognition (598,54), dependency (540,54), League (598,326), formable (598,388), severe-instability badge (318,384). | Four value-selected semantic strips remain visible. The optional animated siblings overlay the eight-frame ring. The separate severe badge displays frame 3 of the dependency warning strip only when severe instability is present. |
| Navigation | Tabs at y=380, 412, and 444. Four tabs are 112×28; Ambitions is 230×28. | Five native tabs select one detail panel through Event 006 flags. |
| Selected detail | Five native text boxes share (280,444), max 386×42. | One Government, Recognition, Security, League, or Ambitions explanation. |

The native frame-field precedent is the iconType mission_icon in game:interface/airselectionview.gui, lines 629-635, source revision 8b451fd20bc75be278fffe8dc7d491fcaaf19031d4e1e6437c0cf047963ece3a. The exact frame assignment is frame = 17 at line 633. The offline Interface modding iconType section says the frame attribute selects a frame from a multi-frame image, lines 178-195, source revision b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c. The installed documentation folder had no interface or sprite-frame section; the live source lookup and vanilla GUI precedent supplied that syntax evidence.

The offline Scripted GUI Modding Window assignment section was read at lines 40-67, source revision b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30. The offline Interface modding Containers section was read at lines 73-80, and its instantTextBoxType and buttonType sections at lines 196-256, source revision b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c. The offline Decision modding Category examples were read at lines 229-263, source revision 7713b9bcee5f3818d63aafbd45f18d812a9173a7c59ab238384b57db60db6162. Installed common/scripted_guis/_documentation.md was read at lines 1-146, source revision 43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838. Vanilla precedent files were interface/sov_paranoia_system_scripted_gui.gui and common/scripted_guis/SOV_paranoia_system_scripted_gui.txt; source lookup located the vanilla textbox block at line 47, revision 8b451fd20bc75be278fffe8dc7d491fcaaf19031d4e1e6437c0cf047963ece3a, and both files were read at lines 20-74 and 1-85.

## Implemented repairs and parent-owned asset integration

The worker-owned changes are common/scripted_guis/006_independence_wave_scripted_gui.txt, interface/006_independence_wave.gui, and localisation/english/006_independence_wave_gui_l_english.yml.

The title key now displays “Independence Status” instead of “Statehood Ledger.” The tab heading displays “Status panels” instead of “Ledger views.” The animation tooltip says “Show or hide the decorative ring around status icons,” because semantic symbols remain visible with animation off.

The four static state-symbol visibility triggers now use always = yes. The four animated siblings remain gated by independence_wave_status_gui_show_animation. No gameplay trigger or effect was changed in that binding.

The severe-instability badge now uses GFX_independence_wave_dependency_warning_states at frame 3 instead of the calm static dependency sprite. It keeps its original (318,384) position, 0.75 scale, alwaystransparent setting, and existing severe-instability visibility trigger. The dependency strip has three frames; the accepted constant registry maps dependency_danger to 3. The existing refresh helper selects that same frame for severe instability.

The parent owns the GFX and DDS integration. interface/006_independence_wave.gfx points all four animated aliases to gfx/interface/006_independence_wave/animations/independence_wave_ornamental_ring_sheet.dds, eight frames at 5 FPS, and points their animated-static fallbacks to independence_wave_ornamental_ring_static.dds. The recognition state-strip cell 0 was updated to the ornate seal; cells 1-4 remain byte-identical.

The current parent-owned asset manifest is docs/assets/006_independence_wave/animations/manifest.md. The complete parent icon handoff is docs/plans/006_independence_wave_plans/subagent_handoffs/graphics_icons_20261006.md. The asset package records source frames, processed frames, preview, transparent centre, DDS hashes, and native/4× status-icon composites.

## Source hashes

| File | Ownership | SHA-256 | Bytes |
| --- | --- | --- | ---: |
| interface/006_independence_wave.gui | Worker-owned | 24BFE2FD7EA55F67C97717D0B6DD29F2050B62CDCAD1E9A428F5B10930455BAD | 11,967 |
| common/scripted_guis/006_independence_wave_scripted_gui.txt | Worker-owned | 98208013250BD1E7F189F70B662098580C8D9B62FABDB54A07CFDAA8C0E7FEC0 | 5,972 |
| localisation/english/006_independence_wave_gui_l_english.yml | Worker-owned | D8E99056BBD7283CE78633B4A5ED573DA6C10E72D82433E25FF7892525F8DE6C | 8,249 |
| interface/006_independence_wave.gfx | Parent-owned | 77AA72DCB48ACBB2D353D4FBEC0BD2FB3E53D8557C44D60D5D0453D295B34F13 | 20,003 |
| gfx/interface/006_independence_wave/animations/independence_wave_ornamental_ring_sheet.dds | Parent-owned | 0D6EED365F410C82B4C81CDF8976CE0C55E95DFF2533D03D0DD306CF64438640 | 131,200 |
| gfx/interface/006_independence_wave/animations/independence_wave_ornamental_ring_static.dds | Parent-owned | F1707DC0ED3508C3C758B64541519A12C931EABD5D8C619EA2CC4001962D51EB | 16,512 |
| gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_sheet.dds | Parent-owned | 105DB40C60DB38E948CACCD82F33148CE7A811C1AAA44895A464CB740175DAF8 | 82,048 |
| docs/assets/006_independence_wave/animations/manifest.md | Parent-owned | 03DFA7BCB0D999C7C9518A1A6BB50C912BA804F33BB9C15BEBEB11B2B0C32ED0 | 6,110 |

The title/tab/tooltip localisation file is UTF-8 with BOM. The accepted pre-change YAML is frozen at docs/plans/006_independence_wave_plans/subagent_handoffs/evidence/gui_takeover_20261006/pre_change/006_independence_wave_gui_l_english.yml, SHA-256 64C5DFE32A0D077B86322F0A7A5A10ADACAC549FB687E41FF0A5F5280C058663. The exact pre-change scripted-GUI Git source is frozen at docs/plans/006_independence_wave_plans/subagent_handoffs/evidence/gui_takeover_20261006/pre_change/006_independence_wave_scripted_gui.txt, SHA-256 C5EE3BEEA0B029504737F8C8766002F26D4F4E2E42F5052E5CBCD43BB15E427D.

The GUI layout file was byte-identical to Git HEAD before the severe-warning repair. That pre-change source is frozen at docs/plans/006_independence_wave_plans/subagent_handoffs/evidence/gui_takeover_20261006/pre_warning_fix/006_independence_wave.gui, SHA-256 D8B2A3DDE2E33B6643664EB4560243647A9069DA3BA58987C33BD284F52E677F. The final GUI source delta is one iconType sprite/frame assignment. No GFX, DDS, event, decision, scripted effect, AI, cost, shared interface, spreadsheet, or CSV was edited by this worker.

## Scenario fixture

Every root scenario uses date 1936.1.1, l_english, UI scale 1, closedFlags = true, independence_wave_active_origin = true, independence_wave_origin_ended = false, liberation_origin = 6, and exactly one selected-tab flag. Animation is explicitly off except for the Government/on view. The animation-on scenario samples animationTimeSeconds = 0.8.

The shared declared country values are legitimacy 62, recognition 48, capacity 54, security 42, instability 28, network standing 24, host claim intensity 8, hostility 24, host obligations 1, and strongest patron influence 0. The normal semantic frame values are recognition 3, dependency 1, League 1, and formable 1. The severe fixture uses instability 70, the “Severe” band, dependency frame 3, and the visible warning badge.

The scenario supplies source-derived outputs for all four previously unresolved text selectors: host “Unsettled,” League “Congress failed,” founding “Recognized State,” and mission “No timed commitment is currently active.” It also supplies the source-derived metric bands and patron name. These are declared preview inputs, not observed game state. No country tag or forced visibility override is supplied.

The parent asked to preserve the nested exists = yes fact as a fixture limitation. The renderer still reports independence_wave_status_scripted_gui.visible as unresolved even though the active-origin flag and liberation-origin value are supplied. The screenshot shows the explicitly selected root window; it does not establish the real category trigger’s in-game eligibility.

## Rendered root scenarios

The following 12 unique scenarios were rendered as separate roots. The Government/off 1920 scenario includes an explicit hover tooltip preview. The severe-warning fixture is the same scenario before and after the final one-line frame repair.

| Scenario | Resolution and state | Source revision | Reviewed full PNG and SHA-256 |
| --- | --- | --- | --- |
| event006_SCO_1936_government_ring_off_toggle_tooltip_1920 | 1920×1080, Government selected, ring off, Animate hovered | eeffe8eaf8e1a8140756ee1a3e510913d8c443d234281206fb74ffd306c3b4cc | current_render/full.png — 8EE6EF6B774030B8517A350FE0652D451F34E9B47E5173A69FCC15AAFC122575 |
| event006_SCO_1936_government_ring_on_1920_final | 1920×1080, Government selected, ring on at 0.8 s | e45643d56407408a4a344a3d1445542dc9223e8b2878a8871f42559014932991 | current_render/gov_on_1920_full.png — 1EA33FC510DB81592115B9A5497340BC373D822D830C52F7A2D372DD79DC590B |
| event006_SCO_1936_recognition_ring_off_selected_1920_final | 1920×1080, Recognition selected, ring off | 4b59bc3260e311e81a011419ba994271ac8d93ace12ccea942c942678010ef2e | current_render/recognition_1920_full.png — EBA29E52FEF566F4926295E06B0ED5E141A3A520492749040321ED4771566A76 |
| event006_SCO_1936_security_ring_off_selected_1920_final | 1920×1080, Security selected, ring off | 4b59bc3260e311e81a011419ba994271ac8d93ace12ccea942c942678010ef2e | current_render/security_1920_full.png — E870E99D6CA16D1D213BC43596880A1AA89824F45FC326AC36A904C56BE52349 |
| event006_SCO_1936_league_ring_off_selected_1920_final | 1920×1080, League selected, ring off | 4b59bc3260e311e81a011419ba994271ac8d93ace12ccea942c942678010ef2e | current_render/league_1920_full.png — EBECDC28BE24FD32AFC30B114FD6C5A6EAF8B2E74E5261EA7C52F442650D8FB8 |
| event006_SCO_1936_ambitions_ring_off_selected_1920_final | 1920×1080, Ambitions selected, ring off | 4b59bc3260e311e81a011419ba994271ac8d93ace12ccea942c942678010ef2e | current_render/ambitions_1920_full.png — E34742925135B12A4F5F20406E559034CC93453F496ED33F02F88FA97994A3A8 |
| event006_SCO_1936_government_ring_off_selected_1366_final | 1366×768, Government selected, ring off | 4b59bc3260e311e81a011419ba994271ac8d93ace12ccea942c942678010ef2e | current_render/government_1366_full.png — 2BA3EC759B5FB99DEF7E0E961C80BF6CA828ABCD5DB62823D8649ABF0A3EFEC5 |
| event006_SCO_1936_recognition_ring_off_selected_1366_final | 1366×768, Recognition selected, ring off | 024f3ebcdc1fc1e56f776812c3233c777fddba890898162ef9bb213b3c546115 | current_render/recognition_1366_full.png — 5CDBC7606F535EE1739B0BCAA84CB022F8130B91A2E5BEEEC92ACFEC3C6FE4E4 |
| event006_SCO_1936_security_ring_off_selected_1366_final | 1366×768, Security selected, ring off | 98bad52d6d3d10d1706ef352f36a529f4f2c5cf1f428185944a98bbd6a02bd08 | current_render/security_1366_full.png — BE27670894AC9F97B8DFF5FDC0BC611FC6E8ABF2A9BC9186AE99E412565B0F7F |
| event006_SCO_1936_league_ring_off_selected_1366_final | 1366×768, League selected, ring off | 98bad52d6d3d10d1706ef352f36a529f4f2c5cf1f428185944a98bbd6a02bd08 | current_render/league_1366_full.png — B99EBB066310275AD6A730F7C92690417213D9699E419F020DBF9781521A80BC |
| event006_SCO_1936_ambitions_ring_off_selected_1366_final | 1366×768, Ambitions selected, ring off | 4b59bc3260e311e81a011419ba994271ac8d93ace12ccea942c942678010ef2e | current_render/ambitions_1366_full.png — 52B7595CF1DC3E82A96FE903CCFE3B015489208952A8DFCA5D3E8AE3E009B678 |
| event006_SCO_1936_government_ring_off_severe_warning_1920_final | 1920×1080, Government selected, instability 70, warning visible | before 8900a4823ff29296d507cbd9b3ef6949d16fb7be91a9b137412eec5e3f447f6c; after fe7cd2cb1e49725a5edd7a12e6ad4d37b8a9771c8e3b52e52739e19fc0141b19 | before current_render/government_severe_warning_1920_full.png — E0793F77C01D458DCFF46EC62DC052DA5847D9EA2C013EDD3EE395E6B39E1D5F; after current_render/government_severe_warning_1920_after.png — 6C34ED423B0D4D9671E25BFB46CB97B8DB3D0B342B427542DE96960B7C9C7563 |

The full/cropped/annotated Government-off hover preview artifacts are current_render/full.png, current_render/cropped.png, and current_render/annotated.png. Their SHA-256 values are 8EE6EF6B774030B8517A350FE0652D451F34E9B47E5173A69FCC15AAFC122575, 2D87E3378B0C0F225A00E35368C0F7281517EDE571186ADAC27A82C61E6F148A, and B9B9ABF2DBB597629D8184937A6C124FCCAC2CC6A733982859A7DA67DE262F98, respectively. The declared tooltip popup at x=700, y=40, width=520, padding=8 fits on one line and does not cover the status text.

The matching declared scenario, fidelity, validation, and scenario-matrix JSON files are current_render/scenario_government_off_tooltip.json (SHA-256 2FDFB33426C43E1CD1AE426A7FB6A0B5BAD233E49561C0B03F8453FB643DA687), fidelity_government_off_tooltip.json (C1D332E9298FE4ABDC3F42ACD1FFC156644783E678E9038A267F7CC9A9157F12), validation_government_off_tooltip.json (00FD5AB560A640C99FEC3472712C4548162D8B4262EF4028B0CDFE56767CFB8C), and scenario_matrix_government_off_tooltip.json (494B660134C0DF25D14388952DDFC0B96FA9B0F2B117102CB21C089BF231951A). The matrix records 39 visible elements, no unresolved click regions, and no unresolved visibility entries.

Click-region PNGs were retrieved, byte-range checked, hash-verified, and reviewed at both resolutions. The 1920×1080 Government/on click map is current_render/gov_on_1920_click_regions.png, SHA-256 7283A8EDCF076149A76F0D1FE49730993C8A3093E5448700337472E8572A9408. The 1366×768 Security/off click map is current_render/security_1366_click_regions.png, SHA-256 AEBE3834787D6CC6B4A87C4E0BA3EB4062BBAA093611926A2C3873FC9E440B8E. Both show the two utility buttons and five tabs; the regions are distinct, inside the board, and do not overlap. Their representative scenario matrices report zero unresolved click regions and zero unresolved visibility entries.

The severe-warning before/after comparison is in current_render/severe_warning_frame_comparison_20261006.json, SHA-256 878FD06282DC06D3ED90CEFD266AEC160D5C1C9D0308C5025E4342D839282A3C. It records a 35 by 44 pixel difference box at x=324, y=386, with 1,203 changed pixels and no differences elsewhere in the 1920 by 1080 image. The pre-fix GUI source is the byte-verified Git HEAD snapshot at pre_warning_fix/006_independence_wave.gui, SHA-256 D8B2A3DDE2E33B6643664EB4560243647A9069DA3BA58987C33BD284F52E677F; that exact text was supplied as sourceBaseline to the matched severe render. The MCP response exposed the full SVG but not a separate comparison PNG. The full SVG SHA-256 is 328f4ef3ed47a43c9527c6d8b2c201317f15170932ee210d4f00084c0a7a68f6; the reviewed after PNG is a Sharp conversion of that SVG. The red badge is the only visual change.

The first 14-related-scenario render completed at source revision 86d476d77fe69b2a1bbdd93acc02ee41d2930474a2630e1650742221ececa443 but returned MCP_RESPONSE_TRUNCATED (40,408 bytes over a 32,768-byte inline budget) and exposed only the Government/off 1920x1080 full SVG, SHA-256 f8d2da2812b7178b0976a5b5e83efaf88a8650812e4be0eb47cb426b7a9ceb5c. It was retained as intermediate evidence and not counted as coverage for the other tabs. Each final tab and resolution was then rendered as its own root scenario. The final root calls returned GUI_RENDERED with status ok and no blockers.

## Visual findings and budgets

All five tab details were visually reviewed at both resolutions. Government, Recognition, Security, League, and Ambitions detail text fits within the 386×42 box; the longest Ambitions copy occupies two lines. The five numeric values, host relation, patron status, network and phase, active commitments, title, subtitle, and all controls remain within the 700×500 board. The window remains within both viewports at UI scale 1.

The title measured 209 px inside its 510 px bound and the subtitle measured 484 px inside its 520 px bound in the normal GUI measurement. No screenshot contains a raw [dynamic_loc] token. The five country values are the explicit parent-accepted count. The seven buttons remain two utilities and five navigation tabs; no spendable cost is shown.

Animation off retains the semantic symbols. Animation on adds a state-neutral bronze ring; the inner recognition star, dependency shield, League symbol, and formable seal remain legible at the sampled 0.8-second frame. The severe warning badge now shows the same red danger state as the dependency marker.

The representative Government-off validation reports 39 background/child overlap findings, 16 clipping findings, 9 invalid-size findings, 13 missing global-state-gallery states, 13 informational alignment findings, and one informational spacing finding. The overlaps are the painted board containing its children. The 0×0 findings apply to elements whose source visibility is false in that fixture, including the four animated overlays when ring animation is off, hidden tabs, and the warning badge outside severe-instability state; no screenshot shows a clipped visible element. The GUI root reports one unresolved scripted-GUI visibility fact from exists = yes. These warnings remain recorded rather than suppressed.

The state root scenarios explicitly set the selected tab with elementStates and one matching tab flag. The Government-off tooltip root also sets the Animate button to hover. Other controls do not have disabled, completed, or list states, so those categories are not applicable. No minimum/maximum-value stress fixture was rendered; the screenshots use the coherent mid-range 1936 source-derived values listed above.

## Inspect and documentation evidence

The pre-change GUI inspection returned GUI_INSPECTED with 48 window elements, no skipped sources, and source revision 67487dd6be4182029278ae57611b9dd6b675c32aebb75fc0753407d719f18731. Its artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78697d2c03f1ee50cea3f7ccb7f8e59d8b03ce54fb6b76fe1fd718158f72dc43/649690449ec57d907eb2a75252c334375946f9bdda1d3ca13e73885271628c09/gui-inspect.67487d6be418202.json.

The post-copy inspection returned GUI_INSPECTED with shared revision eeffe8eaf8e1a8140756ee1a3e510913d8c443d234281206fb74ffd306c3b4cc. Its first tooltip request was too narrow at 78 px and reported GUI_TOOLTIP_BOUNDS; the final corrected tooltip render uses width 520 and has no tooltip-bounds warning.

The post-frame-repair inspection returned GUI_INSPECTED with shared revision fe7cd2cb1e49725a5edd7a12e6ad4d37b8a9771c8e3b52e52739e19fc0141b19, parsed the modified window without blockers, and retained only the known parent-requested exists = yes visibility limitation plus non-blocking board/child overlap diagnostics.

Its exact inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e92bc717e8e39a53a5a3deb814c4b25f973453c961547f23e019867f2fb536f4/42ac302f2d44ceef92aabb7e89a0ee7bcca3e9fc4e1029f1cf890030e8dd6790/gui-inspect.fe7cd2cb1e49725a.json, 935,905 bytes. The widget lookup located independence_wave_status_instability_warning at mod:interface/006_independence_wave.gui line 25, source lookup revision 8b451fd20bc75be278fffe8dc7d491fcaaf19031d4e1e6437c0cf047963ece3a. The strip definition is interface/006_independence_wave.gfx line 97 with noOfFrames = 3. The source maps dependency_danger to frame 3, and the refresh helper selects that constant at severe instability.

Offline Scripted GUI Modding Window assignment lines 40-67, Interface modding iconType lines 178-195, Containers lines 73-80, and instantTextBoxType/buttonType lines 196-256 were read from the wiki snapshot. Installed common/scripted_guis/_documentation.md lines 1-146 was read for the existing context and window assignment. The installed game documentation folder contains no interface or sprite-frame documentation file; the vanilla GUI iconType frame example and offline wiki frame rule were used for the badge edit.

The active-origin trigger is common/scripted_triggers/006_independence_wave_triggers.txt lines 9-14, source revision 0353ff9a177a822d6617b39f8a9a83ca5930095d2a624ea5a81c8a09cb547e4f. Its origin constant is liberation_origin.independence_wave = 6 at common/script_constants/chaosx_liberation_release_constants.txt line 90, revision 6904d7d22002fcd54c4e56fb1a5e89cab29282f55528c240a42790ad09195f54. The severe-warning threshold is 65; frame mapping dependency_danger is 3 in common/script_constants/006_independence_wave_constants_registry.txt. The three-frame GFX strip and the refresh helper’s severe state mapping were checked in source.

## Script validation and remaining limits

The changed scripted-GUI file received whole-file SCRIPT_CHECK_PARTIAL because its family is unsupported and zero commands were checked. A country-scope always = yes trigger snippet returned SCRIPT_CHECKED with valid = true for one supported command.

The parent’s 12 requested whole-file validations are recorded in docs/plans/006_independence_wave_plans/subagent_handoffs/evidence/gui_takeover_20261006/script_validate_results_final_20261006.jsonl. They used installed game documentation revision 9227e238bce49345e9c358598b4dd4940c733d906b72324e8e02a57ecb42093b. Three files returned SCRIPT_CHECKED: the Pacific decisions (662 commands), main Event 006 events (230), and host-response events (58). They reported no findings, but 12, 35, and 9 native argument blocks remained unchecked, respectively.

Seven scripted trigger/effect files returned SCRIPT_CHECK_PARTIAL because every root had an unknown scope: FORM05 triggers (37 roots, 319 commands checked, 35 argument blocks unchecked), decision triggers (72, 566, 93), main effects (147, 2,490, 891), opening dispatch (6, 183, 96), host-response orchestration (7, 120, 42), FORM03 effects (46, 762, 201), and the Event021 adapter registry effects (3, 364, 97). Both the scripted-localisation registry and constants registry are unsupported families and had zero commands checked. All partial results had valid = null, zero findings, zero unresolved command tokens, and parametersChecked = false.

The renderer cannot establish the live decision-category trigger because exists = yes remains unresolved without a country binding; the parent asked to preserve that fact instead of forcing visibility. Its immediate-tooltip preview approximates caller-declared position and tooltip composition, and does not model native tooltip timing or click_to_front. The animation preview marks effectFile unsupported even though the sampled ring overlay renders clearly. No game process or desktop was launched.

The user’s live validation should confirm the real Event 006 category opens only for an eligible active-origin country, all tabs select the matching detail, the Animate control adds/removes the ring without hiding or changing state symbols, the severe warning badge and top dependency marker both use the danger frame, and the tooltip behaves at the intended native location. The user should check the window at 1920×1080 and 1366×768 at UI scale 1.

## Skills used

Skills applied: chaos-redux-scripted-gui, chaos-redux-decisions-missions, chaos-redux-events, chaos-redux-event-assets, chaos-redux-frame-animation, and chaos-redux-subagents. No skill was created or changed.
