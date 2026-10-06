# Event 006 status window reference and visual-state mapping

This record preserves the accepted Event 006 board layout and documents the bounded copy, animation-state, and severe-warning frame corrections.

The parent accepted keeping the institutional-board composition and all controls while correcting visible defects. The player-facing title and tab header must avoid the bookkeeping term ledger.

Part 3 of the accepted Event 006 specification assigns a compact scripted GUI to the Event 006 decision category and calls for five country values, former-host and patron status, network standing, founding phase, active missions, five tabs, and state-driven cues. See docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md, lines 320-344.

The dedicated window is independence_wave_status_window in interface/006_independence_wave.gui. The presentation binding is independence_wave_status_scripted_gui in common/scripted_guis/006_independence_wave_scripted_gui.txt. The owner entry point is independence_wave_founding_category in common/decisions/categories/006_independence_wave_categories.txt.

On 2026-10-06 the parent accepted a narrow animation-state correction. The four static state symbols remain visible at all times. Their animated siblings become optional decorative bronze ring loops and must not cycle through semantic statuses.

The accepted icon handoff is one eight-frame transparent-centre bronze ornament and ribbon ring. The parent owns its asset and GFX repointing into the existing animated sprite identifiers.

The parent also authorized a one-line severe-warning repair after reviewing the warning-state render. The separate instability badge must use the existing three-frame dependency-warning strip at frame 3 when the severe-instability trigger shows it, matching the red danger frame used by the top dependency marker.

The G5 and G6 rationale recorded by the parent is that the true state remains legible with animation on or off, and decorative motion must not impersonate a changing status.

The accepted composition reference is docs/plans/006_independence_wave_plans/references/006_event6_network_standing_league_explanation_reference_2026-09-27.png, SHA-256 1892B363E3ADC35C5E15E10F84E022740D8F4C52A20311C3D9D5F27A96F4A469.

The companion standing reference is docs/plans/006_independence_wave_plans/references/006_event6_network_standing_reference_2026-09-27.png, SHA-256 3CFB12E90AE8603A30F2279FD066ED05D4A638EC9817E14EEF9A9BA486CF6A21.

The annotated baseline image is docs/plans/006_independence_wave_plans/references/006_event6_statehood_status_baseline_annotated_2026-10-06.png, SHA-256 427ADE6DBF57EA9B05624F9FBB2702425C1502FB39E79DF79BB7601D73F5CCDE. It preserves the supplied reference pixels and adds numbered region callouts.

| Reference region | Native element and bounds | Content and state mapping |
| --- | --- | --- |
| Painted board and frame | independence_wave_status_panel_background at (0,0), window 700x500 | Decorative GFX_independence_wave_status_panel. Live text, values, and controls remain native. |
| Title and subtitle | independence_wave_status_title at (26,16), max 510x30. independence_wave_status_subtitle at (28,48), max 520x34 | Native instantTextBoxType elements use hoi_24header and hoi_16mbs. The title reads Independence Status. |
| Utility controls | independence_wave_status_toggle_animation at (526,16), 78x26. independence_wave_status_refresh at (610,16), 64x26 | Two native buttons keep their shared button sprite and scripted actions. The animation tooltip says the decorative ring can be shown or hidden. |
| Country values | Five text rows at x 74 and y 92, 142, 192, 242, and 292. Matching icons are at x 24. | Legitimacy, recognition, capacity, security, and instability remain native value text with Event 006 idea sprites. |
| Supporting status | Former host y 84-174. Patron y 184-248. Network y 258-322. Founding phase y 334-382. Mission y 386-450. All begin at x 366. | Native headings and dynamic text show host, patron, network, phase, and mission state. |
| Status symbols | Recognition seal (598,54). Dependency warning (540,54). League seal (598,326). Formable seal (598,388). Severe-instability badge (318,384). | The four semantic symbols use their value-selected state strips and remain visible. The optional animated siblings overlay the accepted eight-frame bronze ring while animation is enabled. The separate severe-instability badge uses frame 3 of GFX_independence_wave_dependency_warning_states when has_independence_wave_severe_instability is true. |
| Navigation | Tabs are at y 380, 412, and 444. Four are 112x28. Ambitions is 230x28. | Five native tabs select one detail panel with mutually exclusive Event 006 flags. The heading reads Status panels. |
| Selected detail | Five native text panels share (280,444), max 386x42. | The selected government, recognition, security, League, or ambitions explanation appears here. |

The visual hierarchy remains the background, title and subtitle, utility controls, five country values, supporting status, then tab navigation and one selected detail panel.

The authorized copy changes are independence_wave_status_gui_title to Independence Status, independence_wave_status_gui_tabs_header to Status panels, and independence_wave_status_gui_toggle_animation_tt to “Show or hide the decorative ring around status icons.” The accepted state change makes the four static icon triggers always visible and leaves each animated sibling gated by independence_wave_status_gui_show_animation. The severe-instability badge is bound to frame 3 of the existing dependency-warning state strip; its source visibility trigger remains unchanged.

The accepted mechanic-value count remains five values under the parent's explicit decision. The seven visible controls are two presentation utilities and five navigation tabs. No gameplay action or spendable cost is displayed.

The rendered matrix covers Government, Recognition, Security, League, and Ambitions at 1920x1080 and 1366x768, UI scale 1, with the selected tab explicit in each root scenario. Government is rendered with animation on and off; a targeted hover tooltip preview covers the corrected Animate description. A separate Government scenario uses instability 70, the Severe band, and the severe-warning badge. This status surface has no disabled gameplay action or list, so disabled, completed, empty-list, and crowded-list states are not applicable.

The before-warning severe fixture is docs/plans/006_independence_wave_plans/subagent_handoffs/evidence/gui_takeover_20261006/current_render/government_severe_warning_1920_full.png, SHA-256 E0793F77C01D458DCFF46EC62DC052DA5847D9EA2C013EDD3EE395E6B39E1D5F. The matched post-fix SVG is docs/plans/006_independence_wave_plans/subagent_handoffs/evidence/gui_takeover_20261006/current_render/government_severe_warning_1920_after.svg, SHA-256 328F4EF3ED47A43C9527C6D8B2C201317F15170932EE210D4F00084C0A7A68F6, and its reviewed PNG is government_severe_warning_1920_after.png. A raw RGBA comparison changed 1,203 pixels inside a 35x44 rectangle around the separate badge; all other pixels match.

The pre-change inspect source revision is 67487dd6be4182029278ae57611b9dd6b675c32aebb75fc0753407d719f18731, scenario event006_statehood_baseline_government_1920x1080_20261006. The exact inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78697d2c03f1ee50cea3f7ccb7f8e59d8b03ce54fb6b76fe1fd718158f72dc43/649690449ec57d907eb2a75252c334375946f9bdda1d3ca13e73885271628c09/gui-inspect.67487dd6be418202.json.

The inspect artifact was assembled from 28 contiguous byte ranges totaling 911069 bytes. Its full SHA-256 was verified as 78697d2c03f1ee50cea3f7ccb7f8e59d8b03ce54fb6b76fe1fd718158f72dc43.

The inspect resolved 48 window elements, 77499 graph nodes, 191107 edges, 3516 UI elements, 44509 sprites, 186 fonts, and 117 scripted GUIs, with no skipped sources or missing sprite, texture, font, or localisation finding.

The standalone .agents/skills/chaos-redux-scripted-gui/references/visual-review.md path is absent. The complete visual review checklist embedded in .agents/skills/chaos-redux-scripted-gui/SKILL.md was read and applied.

The initial inspect evidence above predates the GUI repairs. The final root scenarios, frame repair, source hashes, updated asset wiring, script validation results, and remaining limits are recorded in docs/plans/006_independence_wave_plans/subagent_handoffs/gui_takeover_20261006.md.
