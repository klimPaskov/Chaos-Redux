# Event 006 formable state-puzzle GUI footprint review — 2026-09-20

Disposition: blocked and source unchanged.

No safe source-local fix was proven for the unresolved dynamic iconType footprint route, so this handoff records the exact evidence and the next required engine-equivalent evidence without changing the Event 006 GUI sources.

## Ownership and authorization

Event: 006 Independence Wave.

Event entry: chaosx.nr6.1 in events/006_independence_wave.txt.

The parent task explicitly authorizes only the Event 006 formable state-puzzle GUI source, its directly necessary documentation, and this dated handoff.

The user direction in the parent task is the acceptance basis for preserving the current reviewed 440 by 180 state-puzzle composition, family-isolated overlays, qualifying and unresolved sprite branches, and exact state-piece positions while testing a deterministic footprint fix.

The dedicated surface is event-owned because common/decisions/categories/006_independence_wave_categories.txt attaches independence_wave_formable_state_puzzle_scripted_gui to Event 006 formable categories, the GUI visible and overlay triggers use Event 006 formable activation flags, and no shared event log, event-details, settings, status, or super-event window is involved.

## Exact identifiers and source links

GUI source: interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui.

Independent window: chaosx_independence_wave_formable_state_puzzle_window.

Window geometry: position 0,0, size 440 by 206, clipping enabled.

Family overlays: independence_wave_form01_overlay, independence_wave_form02_overlay, independence_wave_form03_overlay, independence_wave_form04_overlay, independence_wave_form05_overlay, independence_wave_form07_overlay, independence_wave_form08_overlay, independence_wave_form09_overlay, independence_wave_form12_overlay, independence_wave_form13_overlay, independence_wave_form16_overlay, independence_wave_form18_overlay, independence_wave_form39_overlay, and independence_wave_form48_overlay.

Each family map container is independence_wave_formXX_map, positioned at 0,24 with size 440 by 180 and clipping enabled.

Scripted-GUI source: common/scripted_guis/chaosx_formable_state_puzzles.txt.

Scripted-GUI block: independence_wave_formable_state_puzzle_scripted_gui.

Context: decision_category.

Attached window: chaosx_independence_wave_formable_state_puzzle_window.

The scripted GUI has no gameplay-changing effects block and has ai_enabled = { always = no }.

Decision entry source: common/decisions/categories/006_independence_wave_categories.txt.

Primary entry category: independence_wave_formables_category with scripted_gui = independence_wave_formable_state_puzzle_scripted_gui.

Other Event 006 formable category entries use the same scripted GUI for family-specific progression categories and retain their parent-owned visibility and gameplay rules.

Dynamic image properties: each independence_wave_formXX_state_STATE_piece maps to GetChaosxFormableIndependenceWaveFormXXStateSTATESprite in the scripted-GUI properties block.

Overlay visibility properties: independence_wave_formXX_overlay_visible maps to independence_wave_formable_state_puzzle_formXX_activation = yes in the scripted-GUI triggers block.

GFX source inspected read-only: interface/chaosx_formable_state_puzzles.gfx.

Event 006 sprite identifiers use GFX_independence_wave_formXX_state_STATE_unresolved and GFX_independence_wave_formXX_state_STATE_qualifying.

Event 006 DDS roots are gfx/interface/formables/state_puzzles/006_formXX_state_puzzle/states/ for the matching family.

Scripted-localisation source inspected read-only: common/scripted_localisation/chaosx_formable_state_puzzles.txt.

Each GetChaosxFormableIndependenceWaveFormXXStateSTATESprite returns the qualifying GFX name when the matching independence_wave_formable_state_puzzle_formXX_state_STATE_qualifies trigger is true and the unresolved GFX name otherwise.

Player-facing localisation source inspected read-only: localisation/english/chaosx_formable_state_puzzles_l_english.yml.

The summary keys are chaosx_formable_state_puzzle_independence_wave_formXX_summary and the delayed tooltip keys are chaosx_formable_state_puzzle_independence_wave_formXX_state_STATE_tt.

## Reference images and native mapping

Reviewed reference images:

- docs/formables/state_puzzles/006_form01_state_puzzle/independence_wave_form01_state_puzzle_projection_440x180.png
- docs/formables/state_puzzles/006_form01_state_puzzle/independence_wave_form01_state_puzzle_projection_440x180_qualifying.png
- docs/formables/state_puzzles/006_form02_state_puzzle/independence_wave_form02_state_puzzle_projection_440x180.png
- docs/formables/state_puzzles/006_form02_state_puzzle/independence_wave_form02_state_puzzle_projection_440x180_qualifying.png

The first pair is the sparse reference and its qualifying-state branch.

The second pair is the crowded reference and its qualifying-state branch.

The explicit user direction in the parent task and the existing Event 006 visual-repair handoff docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_state_puzzle_visual_repair_applied_2026-09-19.md authorize these reviewed references as the acceptance basis for the current composition.

| Reference region | Native element and bounds | Content and state | Adaptation basis |
| --- | --- | --- | --- |
| Summary strip | independence_wave_formXX_summary, 0,0, max width 440, max height 22 | One centered qualifying-count and status line | Uses native instantTextBoxType and current localisation. |
| Transparent map canvas | independence_wave_formXX_map, 0,24, 440 by 180 | Family-isolated state pieces | Uses the reviewed 440 by 180 projection canvas. |
| State piece | iconType named independence_wave_formXX_state_STATE_piece at the exact reviewed position below | Grey unresolved or green qualifying state sprite with delayed tooltip | Uses native spriteType plus scripted-GUI properties.image. |
| Family visibility | independence_wave_formXX_overlay and independence_wave_formXX_overlay_visible | Only the active Event 006 family is shown | Offline inspection cannot evaluate every family flag simultaneously, so its cross-overlay overlap findings are nonblocking and not a geometry rewrite target. |

The native hierarchy is one independent containerWindowType, fourteen family overlay containers, one summary text box and one map container per family, and fifty informational state iconType pieces.

The current source preserves the reference hierarchy, transparent negative space, exact positions, family-specific maps, and separate qualifying and unresolved sprite artwork.

## Exact reviewed geometry

The following positions are relative to each family map container.

| Family | State pieces and positions |
| --- | --- |
| FORM01 | 14 @ 206,149; 121 @ 204,8; 122 @ 191,64; 133 @ 192,8 |
| FORM02 | 100 @ 268,14; 121 @ 415,143; 133 @ 408,143; 331 @ 8,94; 337 @ 391,79 |
| FORM03 | 6 @ 139,107; 34 @ 174,125; 36 @ 223,8 |
| FORM04 | 42 @ 171,83; 51 @ 166,8 |
| FORM05 | 1 @ 149,8; 114 @ 140,52; 115 @ 233,131 |
| FORM07 | 165 @ 328,62; 171 @ 8,25; 792 @ 206,38 |
| FORM08 | 82 @ 47,57; 84 @ 168,8 |
| FORM09 | 104 @ 121,8; 105 @ 170,46; 106 @ 216,72; 184 @ 267,81; 185 @ 188,101; 802 @ 201,54 |
| FORM12 | 249 @ 182,126; 397 @ 169,8; 399 @ 205,101; 651 @ 228,126; 833 @ 163,113 |
| FORM13 | 249 @ 182,126; 397 @ 169,8; 399 @ 205,101; 651 @ 228,126; 833 @ 163,113 |
| FORM16 | 229 @ 205,45; 230 @ 135,62; 231 @ 86,8 |
| FORM18 | 413 @ 241,102; 421 @ 209,76; 676 @ 119,8 |
| FORM39 | 523 @ 104,68; 636 @ 406,150; 669 @ 8,11 |
| FORM48 | 378 @ 352,8; 629 @ 253,110; 684 @ 57,154 |

The asset manifests under docs/formables/state_puzzles/006_formXX_state_puzzle/manifest.json record the matching reviewed 440 by 180 projection canvas and geometry provenance for each family.

## Pre-change MCP evidence

MCP workspace: mod_chaos_redux_ea3b2d67c2c0.

The current source files were unchanged during this review.

Current 1920 by 1080 inspect request: window chaosx_independence_wave_formable_state_puzzle_window, scenario event006_formable_activated_normal, UI scale 1, generated scenarios disabled.

Current 1920 by 1080 inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/675b1559559f48af244bdf7064fcca97fdb813256c6676f9cd62dd5ed5afaf01/c386b5f3fda05e66d35cbb0bb57b71f2bfb72c5f6f7848c615335621ebeaa291/gui-inspect.1c312e1b9c0161da.json.

Current 1920 by 1080 inspect shared revision: 1c312e1b9c0161da9ccb88c11580d3d436f94576ac59f4c7133efb9e9b323dc2.

Current 1920 by 1080 inspect result: GUI_INSPECTED, 93 inspected elements, 643 modelled, 1 approximated, 50 ignored, 0 missing, 0 unsupported, and 15 unresolved.

Current 1280 by 720 inspect request: window chaosx_independence_wave_formable_state_puzzle_window, scenario event006_formable_activated_normal, UI scale 1, generated scenarios disabled.

Current 1280 by 720 inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8503f58238bb1475419badae10a2ad17224f4b3419138c1a4001e770084a2a33/e36cf38c57b7cc08412bc89b61c9adbcd1792ba03d8abc7bab63b6e05dfaf746/gui-inspect.1c312e1b9c0161da.json.

The 1280 by 720 inspection reports GUI_ACCIDENTAL_CLIPPING for the Event 006 state icons, including independence_wave_form01_state_14_piece, independence_wave_form01_state_121_piece, independence_wave_form01_state_122_piece, independence_wave_form01_state_133_piece, independence_wave_form02_state_100_piece, independence_wave_form02_state_121_piece, independence_wave_form02_state_133_piece, independence_wave_form02_state_331_piece, and independence_wave_form02_state_337_piece.

The same inspection reports GUI_UNRESOLVED_DYNAMIC_VALUE for summary getters such as [GetChaosxFormableIndependenceWaveForm01QualifyingCount] and [GetChaosxFormableIndependenceWaveForm01SummaryStatus].

The prior 2026-09-19 Event 006 formable receipt records repeated GUI_INVALID_SIZE and GUI_ACCIDENTAL_CLIPPING findings for dynamic form summaries and state pieces, including the FORM01 and FORM02 pieces.

The current aggregate render request covered normal, warning, and long-text states at 1920 by 1080 and 1280 by 720 with UI scale 1 and generated scenarios disabled.

Current aggregate render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2349cbee9b6ef7425a0fbd3c50e73ffe3881e9bf02339aa65d160cbf35c5cf44/0274a7449d6bf623ab17d966bec8450a4ba65e3d9ee27f598eebafc6103d31c5/chaosx_independence_wave_formable_state_puzzle_w-full.svg.

Current aggregate render result: GUI_RENDERED with one primary linked full-window SVG and an inline MCP_RESPONSE_TRUNCATED warning because the complete render evidence is linked.

The linked SVG declares a 1920 by 1080 offline render and exposes three small embedded PNG state pieces at positions and sizes corresponding to the FORM48 layout, while the dynamic image route remains unresolved for the offline renderer.

The embedded unresolved pieces were visually inspected as grey state shapes. The full SVG could not be rasterized by the conversation image viewer, so this evidence does not establish a visual acceptance pass.

The complete prior 2026-09-19 render receipt records 27 artifacts, 5 variants, 3 requested states, and 2 resolutions.

Prior full render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d202974f6702e6d78f473c71dc4a53874a21ba0aa6996197805f8fa63c769756/fc03ef4eda714de107220379ce658b4e9e493220f1c753c721b9ba9d697a6b08/chaosx_independence_wave_formable_state_puzzle_w-full.svg.

Prior state-matrix artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86475140e85d59254f4092827c97a8afaa0e432eb2f732dc8ee3da932b2b37e0/774e70f77504fd46469ac87e39721013ca46d1bb59b3c8305ce35f3e84497907/chaosx_independence_wave_formable_state_puzzle_w-state-matrix.svg.

Prior click-region artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d202974f6702e6d78f473c71dc4a53874a21ba0aa6996197805f8fa63c769756/7fc4952c3f60dd20b1cf2d9715e66f1b949406ff0b0b7abfbb38537e0e9f60da/chaosx_independence_wave_formable_state_puzzle_w-click-regions.svg.

The prior render receipt is retained as historical pre-change evidence because the scoped GUI sources remained unchanged, but its source revision was f64910d82b5c3d9ae81785e4ae57357dde6e129485079e1901a0bf5ae8f3e829 and it is not presented as a post-change comparison.

## Safe-fix assessment

No source edit was applied to common/scripted_guis/chaosx_formable_state_puzzles.txt or interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui.

The offline Interface modding wiki documents iconType fields for name, position, orientation, spriteType, quadTextureSprite, frame, transparency, hints, tooltips, and centerposition, but it does not document an iconType.size field.

The same page documents size for containerWindowType as the container boundary and clipping or scrollbar basis, not as an explicit child icon footprint.

The installed common/scripted_guis/_documentation.md documents scripted-GUI properties.image, properties.frame, and dynamic x or y properties, but it does not document a footprint property for an iconType.

The installed vanilla precedent interface/sov_paranoia_system_scripted_gui.gui with common/scripted_guis/SOV_paranoia_system_scripted_gui.txt uses static spriteType icons and dynamic frame properties, with no explicit icon size.

The installed vanilla war_escalation_scripted_gui.txt and war_escalation_scripted_gui.gui provide a second dynamic-image precedent in which the native icon footprint comes from the resolved sprite registration.

Every Event 006 state icon already has a static unresolved spriteType in the .gui file and a scripted-GUI properties.image getter that selects the qualifying or unresolved registered sprite at runtime.

Adding an undocumented size key to each iconType is therefore not a safe Clausewitz change because neither the offline wiki, installed documentation, nor the exact vanilla precedents establish that the field is accepted or that it overrides the sprite-derived footprint.

Wrapping each icon in a sized container would only establish a parent boundary and would not prove an icon footprint or preserve the effective tooltip and z-order geometry.

Replacing the dynamic image properties with duplicate static qualifying and unresolved icons would change the accepted dynamic property route, add a second visibility system, and require a new source and MCP review of fifty state branches.

Removing the dynamic properties would display only the unresolved branch and would violate the requirement to preserve the qualifying and unresolved state choice.

No safe source-local deterministic-footprint fix is proven by the available evidence.

## State, resolution, hierarchy, and click-region matrix

| Surface | Requested coverage | Evidence | Disposition |
| --- | --- | --- | --- |
| Normal | event006_formable_activated_normal at 1920 by 1080 and 1280 by 720, UI scale 1 | Current inspect artifacts and current aggregate render artifact above | Source graph is present, dynamic values remain unresolved, visual acceptance blocked. |
| Warning | Same scenario and both resolutions | Included in the current aggregate render request and the complete 2026-09-19 state matrix | No matching current per-state artifact was emitted inline, so warning-state visual acceptance remains unresolved. |
| Long text | Same scenario and both resolutions | Included in the current aggregate render request and the complete 2026-09-19 state matrix | No matching current per-state artifact was emitted inline, so long-text visual acceptance remains unresolved. |
| Family visibility | Fourteen activation flags and fourteen overlay visibility triggers | Scripted-GUI source and current inspect hierarchy | Source mapping is family-isolated. Offline overlap findings are nonblocking because the renderer does not evaluate all hidden-family flags. |
| Hover and tooltip | Fifty iconType delayed tooltips | GUI source pdx_tooltip_delayed entries and prior click-region artifact | No gameplay buttons or scripted-GUI effects exist. Tooltip bounds remain tied to unresolved dynamic icon bounds. |
| Selected, active, completed, disabled, empty, and crowded action states | Not applicable to this information-only map surface | No buttonType, click effect, list, or action control exists in the authorized window | No action-state claim is made. Crowded geometry is represented by FORM02 and the exact source positions. |

The source hierarchy is one independent window, fourteen gated overlays, fourteen summary boxes, fourteen map containers, and fifty informational state icons.

The current aggregate render did not emit a current separate click-region artifact.

The prior click-region artifact is retained above for the matching pre-change route, but dynamic icon bounds remain unresolved and therefore do not establish a final click-region acceptance result.

## Visual acceptance checklist

Reference fidelity: source composition, hierarchy, family grouping, transparent negative space, qualifying and unresolved branches, and reviewed positions are preserved.

Native-element mapping: summary text uses instantTextBoxType, state pieces use native iconType, and family gating uses scripted-GUI triggers.

Label centering: the source uses format = center with max width 440, but the dynamic summary values are unresolved in MCP and glyph-level centering is not accepted as proven.

Painted and logical bounds: the asset manifests establish reviewed 440 by 180 projection canvases, while the MCP route cannot consistently resolve the dynamic icon footprint.

Spacing and symmetry: the accepted source positions remain unchanged. No geometry rewrite is justified by the unresolved renderer output.

Scaling: 1920 by 1080 and 1280 by 720 at UI scale 1 were inspected or requested. No live-game scaling claim is made.

Clipping and overflow: unresolved GUI_INVALID_SIZE and GUI_ACCIDENTAL_CLIPPING warnings block visual acceptance.

Z-order: family overlays intentionally share the same source bounds and are gated by activation triggers. The offline renderer reports 521 nonblocking visible-overlap findings because it cannot prove all overlay visibility states.

Click regions: no primary action control exists. State icons carry delayed tooltips, but their dynamic footprint is not proven by the current offline route.

Background and assets: no custom background is part of this bounded window. Existing Event 006 state-puzzle DDS pairs and GFX registrations were inspected read-only and no asset change or fallback was made.

## Budget and action audit

Visible mechanic values: each active family exposes one qualifying-state count and one summary status, for two visible values.

Primary actions: zero. The window is informational and contains no gameplay-changing control.

Cost count: zero.

Texticon coverage: no gameplay cost is displayed.

Text density: one concise summary line per family and one delayed tooltip per state piece. Long tooltip text remains parent-owned localisation and was not changed.

AI, cost, requirements, effects, and cleanup remain outside this GUI-only handoff and were not changed.

## Before and after behavior

Before this review, the GUI source showed the same exact family-isolated maps and used dynamic scripted-localisation image getters for every state piece.

During this review, MCP inspected the unchanged source at both requested resolutions and rendered the requested normal, warning, and long-text state set.

After this review, the GUI source remains byte-for-byte unchanged, the dynamic qualifying or unresolved selection remains intact, and no geometry or footprint fallback was introduced.

There is no post-change inspect or render comparison because no source change was proven safe or applied.

## Files changed

Changed file: docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_formable_gui_footprint_blocker_2026-09-20.md.

Unchanged authorized GUI files: common/scripted_guis/chaosx_formable_state_puzzles.txt and interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui.

Unchanged linked files: interface/chaosx_formable_state_puzzles.gfx, common/scripted_localisation/chaosx_formable_state_puzzles.txt, localisation/english/chaosx_formable_state_puzzles_l_english.yml, Event 006 decisions, events, gameplay effects, and assets.

No unrelated Event 021, zombie, 3D-pipeline, temporary, shared GUI, or user-owned file was changed.

## Missing evidence and next route

The next evidence must come from a renderer route that evaluates Event 006 scripted localisation in decision_category scope and resolves GetChaosxFormableIndependenceWaveFormXXStateSTATESprite to the registered qualifying or unresolved GFX name for explicit family activation fixtures.

That route must return matching full-window, crop, hierarchy, state, resolution, and click-region artifacts for normal, warning, and long-text at 1920 by 1080 and 1280 by 720 with UI scale 1.

The route should cover at least one sparse family, one crowded family, and the FORM12 or FORM13 identical-geometry pair while keeping the family activation flags mutually exclusive.

If that evidence proves a live geometry defect, the parent must authorize a specific engine-supported footprint field or an accepted native-element redesign before any source edit.

If that evidence proves the current sprite-derived footprint is correct, the parent can close this source blocker and proceed to user live-game validation without a GUI geometry rewrite.

## Assets, integrations, blockers, and simplifications

Existing asset production and repair handoffs were reused as read-only evidence. No new asset request is required for this footprint blocker.

No frame-sheet animation is used by this static state-puzzle surface, so chaos-redux-frame-animation was not invoked for an asset change.

No source fallback, generic emblem, fake control, duplicate static branch, wrapper geometry, unsupported size field, localisation rewrite, or gameplay simplification was used.

Remaining parent-owned work is runtime integration of Event 006 gameplay and any decision or formable validation outside this GUI source boundary.

Live consumer validation remains pending with the user. This handoff does not claim in-game acceptance.

