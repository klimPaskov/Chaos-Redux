# Fallout Blackout GUI Repair Handoff

Disposition: incomplete and visually blocked. The presentation wiring now names an explicit empty pointer-click handler, but the click-region geometry remains unresolved and there is no post-change GUI inspection or render evidence.

## Ownership and acceptance

Event-owned mechanic and slug: Fallout transition / `air_cleanliness_fallout`. The parent prompt identifies `chaosx.fallout.900` as the manual entry and `chaosx.fallout.903` and `chaosx.fallout.904` as related callbacks/notices; it does not provide a separate numeric root event id for the general transition mechanic.

The dedicated window is `fallout_world_end_blackout_window`, with scripted GUI `fallout_world_end_blackout_scripted_gui`, owned by the Fallout transition mechanic. The accepted baseline is documented in [03_blackout_transition.md](../../../specs/air_cleanliness_fallout_specs/specs/baseline/03_blackout_transition.md), while this task's parent prompt explicitly accepts the scoped repair design: a full opaque black viewport, the existing centered message, and pointer input absorbed without advancing the transition or changing gameplay.

The event source enters the manual Fallout consequence through `chaosx.fallout.900` at `events/fallout_world_end_events.txt:11587`, whose immediate block calls `fallout_manual_scenario_begin`. The related manual countdown and terminal notice are `chaosx.fallout.903` at line 12368 and `chaosx.fallout.904` at line 12380. No decision entry point for this window was supplied; the source-backed entry is the event and global transition mechanic. The transition admission effect `fallout_lock_transition` begins at `common/scripted_effects/fallout_consolidated_effects.txt:41299`, sets global `fallout_transition_active` at line 41341, and calls `fallout_mark_blackout_gui_dirty`; the owned scripted GUI is visible only to a human `player_context` while that global flag is present.

This is a parentless top-level Fallout transition overlay, not the shared event log, event-details framework, settings window, options UI, or super-event framework. The parent retains GFX, localisation, gameplay, and final integration ownership.

## Reference and native mapping

The scoped reference was created and visually reviewed before the source edit. It reflects the parent-accepted composition and is an annotation only, not a production GUI render or runtime asset: [blackout_reference.svg](blackout_ui_2026-10-06/blackout_reference.svg) and its [PNG preview](blackout_ui_2026-10-06/blackout_reference_preview.png).

| Reference region | Native element and asset | Intended behavior and state | Bounds or constraint |
| --- | --- | --- | --- |
| Full black viewport | `fallout_world_end_blackout_window` container and existing `GFX_fallout_blackout_tile` sprite | Opaque black while `fallout_transition_active = yes`; hidden when false | 100% by 100% window at the root. The tile is a 10 by 10 opaque black DDS. The live render needed to prove coverage did not return. |
| Center message | `fallout_world_end_blackout_text` using `fallout_world_end_blackout_display` | One existing dynamic transition line at a time | Source places a 1200 by 192 text box at centered offsets `x = -600`, `y = -96`; glyph centering, wrapping, and clipping remain unverified. |
| Pointer sink | `fallout_world_end_click_blocker` using the same black tile | Non-transparent pointer control with an intentionally empty scripted-GUI click handler | The current source remains at `x = -5000`, `y = -5000`, `scale = 1000`. Parent-supplied diagnostics report clipping and click-bounds problems, so full-viewport input coverage is unresolved. |

The sprite registration `GFX_fallout_blackout_tile` is at `interface/fallout_consolidated.gfx:287` and resolves to `gfx/interface/fallout_world_end/fallout_blackout_tile.dds`. The DDS header and pixel bytes show a 10 by 10 image with one opaque black pixel value repeated across all 100 pixels. No asset handoff or GFX edit was needed.

The dynamic localiser `GetFalloutWorldEndBlackoutText` selects one of twelve existing strings: snapshot, state grading, population loss, physical collapse, government sorting, survivor allocation, player continuation, map return, transition error, peace-conference reset hold, diplomacy hold, or player-continuation hold. The phase constants are `snapshot = 1`, `state_grading = 2`, `population_loss = 3`, `physical_collapse = 4`, `government_sorting = 5`, `survivor_allocation = 6`, `player_continuation = 7`, `map_return = 8`, and `complete = 9` in `common/script_constants/fallout_consolidated_constants.txt`. These dynamic states were not rendered.

## Source changes

The only runtime edits are the owned blocks in `interface/fallout_consolidated.gui` and `common/scripted_guis/fallout_consolidated_scripted_gui.txt`.

`fallout_world_end_click_blocker_click = { }` is now explicitly mapped to the button. This uses the installed Scripted GUIs documentation's element-name click-effect pattern, including an empty block. The GUI comment now describes the intentional no-op. A pointer click on this control has no scripted effect that can advance the transition or mutate world state.

The window, sprite, text key, dimensions, position, scale, parentless context, visibility condition, and dirty-variable ownership are unchanged. The edit addresses only the reported missing-click-effect association. It does not repair or prove full-screen pointer coverage.

| File | Before SHA-256 | After SHA-256 | Identifiers changed |
| --- | --- | --- | --- |
| `interface/fallout_consolidated.gui` | `48A033AC8BF21733DE9A0FF0E508A8863638C034486B133A6DE9AC5FBC8BFF92` | `5604299016C04805A2160F515901EE48839E7ACCDB25B210360FC8ACC8C1605E` | Comment inside `fallout_world_end_blackout_window`; no layout fields changed. |
| `common/scripted_guis/fallout_consolidated_scripted_gui.txt` | `CBDBEF5A85842C1ED64F60E34C770D45EA7A44FD7852754C460F2174F8C59423` | `742DDCD79829D6C367BCD17818B950952C0AE429EF3577B94DD352EE250C7B06` | Empty effect `fallout_world_end_click_blocker_click` inside `fallout_world_end_blackout_scripted_gui`. |

There were no GFX, localisation, event, decision, gameplay, or shared-interface edits. The parent-owned GFX and localisation files were read only.

## Layout and action audit

The hierarchy is one parentless `containerWindowType` with the black pointer button and the dynamic text box as children. The scripted GUI uses `player_context`, `is_ai = no`, `fallout_transition_active` visibility, and `fallout_blackout_gui_dirty` updates.

The window exposes zero mechanic values and zero gameplay actions. It has one dynamic message element and one pointer sink; the pointer sink has no cost, requirement, AI action, or gameplay side effect. Cost-count and texticon audits are not applicable because no cost is shown. The dynamic message is a single existing sentence per selected string, but rendered line count, long-string fit, glyph centering, and vertical placement remain unresolved without production images.

The intended scenario matrix is an active human transition and a hidden transition with `fallout_transition_active = false`, each at 1920 by 1080, 1366 by 768, and 2560 by 1440 at UI scale 1. The requested native GUI states are normal/active and hidden. The pointer button has a single-frame black sprite, so there are no designed hover, selected, warning, completed, or disabled visual variants. All runtime state and resolution coverage remains unverified.

At 1920 by 1080 and UI scale 1, centering the 10 by 10 sprite in the source container and applying `scale = 1000` gives nominal 10,000 by 10,000 bounds. With the source offsets `x = -5000`, `y = -5000`, the centered window origin yields a nominal blocker center of approximately `(-4040, -4460)` in screen coordinates and bounds ending at the viewport center. This source-derived geometry is consistent with the supplied clipping/click-bounds findings, but does not replace inspection of the production image or effective click-region artifact.

Keyboard capture and exclusive-input behavior remain engine-unproven as required by the parent brief. No keyboard behavior is asserted or added.

## MCP and reference evidence

The parent supplied the pre-change inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc76b64220f1d6ba7ce85149df787e6b1525df59a2c9d5afc6c498e5de87de27/4aec06d9f7a67a0a15e236e5b81feda38bd86cc00765668f0164f9c7ac5f3/gui-inspect.6ddaf038e7d63971.json` and reported clipping/click-bounds diagnostics plus a missing click effect. This artifact predates the local source hashes above. I did not obtain an independently verified full artifact payload or any render image from that artifact URI.

The connected GUI route rejected `isAI` and `nativeGUI` as unrecognized scenario keys. A subsequent minimal `hoi4.gui_inspect` call for `fallout_world_end_blackout_window`, with explicit `fallout_transition_active = yes` and a related hidden scenario, remained running for 57 seconds and was terminated without a result. The matching pre-change `hoi4.gui_render` call, requesting normal/active states and 1920 by 1080, 1366 by 768, and 2560 by 1440 at UI scale 1, also remained running for 57 seconds and was terminated without a result.

After the source edit, the same minimal inspect and render routes were called once with matching active/hidden scenarios and the three-resolution matrix. Both remained running for 57 seconds and were terminated without results. There is no post-change inspect, render, click-region report, image comparison, or visual acceptance evidence. The requested `isAI = false` and `nativeGUI = global` fixture fields could not be supplied because the live route rejected them; source context and visibility remain explicit in the files.

The optional `hoi4.source_lookup` request for vanilla `SOV_paranoia_system_scripted_gui` with `kind = scripted_gui`, `view = source`, and `maxLines = 80` also remained running for 57 seconds. The exact vanilla files were read locally instead. `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/sov_paranoia_system_scripted_gui.gui` and `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt` show the native named-container and child-element pattern, including separate text and art consumers.

The connected reference routes succeeded. Evidence read includes offline `Interface modding` wiki revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, Arguments lines 81-109 and buttonType lines 227-256; offline `Scripted GUI modding` wiki revision `b07d850ea78c4e1e3fc113574059ad2f3ea37df320b9259128d66814023c1f30`, player_context line 154 and Effects lines 179-193; and installed `common/scripted_guis/_documentation.md` revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, lines 1-146. The wiki confirms that `buttonType` exposes `scale` and `alwaystransparent`, and does not list a rectangular `size` property. It also says container clipping crops child elements only when a background exists. These constraints do not establish a safe replacement click rectangle, so the geometry was left unchanged rather than guessed.

## Remaining work and blockers

The visual task is incomplete. The source geometry still requires a supported correction that covers the full viewport with an accurate click region and avoids the reported clipping/click-bounds defects. The text box also requires rendered checks for horizontal and vertical glyph centering, long-text wrapping, background coverage, z-order, and all three resolutions. The accepted cinematic prompt also mentions fading text beats, but this bounded task did not add or verify fade animation; the parent should retain that as a separate spec-to-source question if it remains in scope.

The parent should rerun exact-window `hoi4.gui_inspect` and `hoi4.gui_render` from a responsive connected session using the active/hidden fixtures and phase values above. The production images must cover the whole window, annotated and cropped views, hierarchy, click regions, normal/active and hidden states, and matching resolution/UI-scale cases. If those routes remain unavailable, this GUI remains visually blocked; the source patch is not equivalent evidence.

No accepted content was flattened, removed, or substituted. The no-op click handler is a presentation-only repair. The full viewport and pointer-coverage repair, post-change visual gate, and user live-game validation remain outstanding; no in-game completion is claimed.
