# Event 016 Directorate compact redesign handoff

## Scope and ownership

This handoff covers only Event 016 `brilliant_scientist` and its dedicated decision-category scripted GUI.

Ownership is explicit in source: `brilliant_scientist_directorate_category` in `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt` attaches `scripted_gui = brilliant_scientist_directorate_scripted_gui`; that definition declares `window_name = "kruger_directorate_container"`; the window is defined in `interface/016_brilliant_scientist_directorate.gui`.

No gameplay outcome, decision cost, duration, AI weight, scripted effect, scripted localisation selector, portrait identity, portrait asset, shared interface, or unrelated event surface was changed.

## Identifiers and files

- Event: `016`, `brilliant_scientist`.
- Decision entry: `brilliant_scientist_directorate_category`.
- Scripted GUI: `brilliant_scientist_directorate_scripted_gui`.
- Root window: `kruger_directorate_container`.
- Full panel: `kruger_directorate_full_panel`.
- Collapsed panel: `kruger_directorate_compact_panel`.
- Full background sprite: `GFX_kruger_directorate_background`.
- Collapsed header sprite: `GFX_kruger_directorate_compact_header`.
- Portrait sprite binding: `GFX_portrait_KRG_doctor_warren_kruger_stage_0` as the authored fallback, with the existing dynamic portrait selector retained.
- Changed layout: `interface/016_brilliant_scientist_directorate.gui`.
- Changed presentation wiring: `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt`.
- Changed Event 016 GUI localisation: `localisation/english/016_brilliant_scientist_directorate_gui_l_english.yml`.
- Final background was produced by the asset owner at `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds`; the sprite path was already correct, so `interface/016_brilliant_scientist_directorate.gfx` did not require an edit.

## References inspected

The required offline `Interface Modding` and `Scripted GUI Modding` wiki pages were consulted with the repository's core wiki references. Installed vanilla documentation was consulted, including `common/scripted_guis/_documentation.md`, `documentation/script_concept_documentation.md`, and localisation documentation. Vanilla decision-category scripted-GUI precedent was inspected in `common/scripted_guis/RAJ_tax_fraud_scripted_gui.txt` and `interface/RAJ_eic_tax_fraud.gui`. Event 016 source ownership, accepted plans, prior handoffs, and the decision-category registration were inspected directly.

## Rejected baseline and pre-change evidence

The prior 500x620 five-tab dashboard is treated as failed. The exact pre-change evidence was reviewed in `.tmp/mcp_event16_directorate_render.png` and `.tmp/mcp_event16_directorate_render_crop.png`. It showed portrait ornament intrusion into the value region, Exposure/control collisions, oversized navigation, and all mutually exclusive lower panels painted together by the offline visibility approximation.

Pre-change `hoi4.gui_inspect` completed with `GUI_INSPECTED`, shared revision `47c49e425c0a58d71d92cc9e3193a16b9d7192c13e6eccf53a2978ec2374e878`, and 65 exact inspected elements.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/481625ca8b10ca7eb839a94288984ae4e3134bf20be911ca3b7bb20a96c3fc6f/a6d7dbe6e4b74f975569ef7d993174c8a42e7b02ad07d3a64b32620cef873d87/gui-inspect.47c49e425c0a58d7.json`.
- Render artifact for the full/state/resolution/click/hierarchy request: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15a685315b971621a000906cd4113b88966968f9be749ed977c39cd5c2f38415/27739586aecadccb44d49503ed5ac9763e8b5cb4c91703a3220d1a9405109f4d/kruger_directorate_container-full.svg`.

## Mandatory rewrite attempt

After the pre-change evidence review, `hoi4.gui_rewrite` was attempted in source mode against `interface/016_brilliant_scientist_directorate.gui`, exact window `kruger_directorate_container`, and scenario `event016_directorate_compact_rewrite`. The adapter returned `status = error`, `code = INTERNAL_ERROR`, and `Unexpected internal error` after approximately two minutes. It wrote no file and returned no artifact. The bounded source patch was therefore applied through the normal repository patch workflow.

## Implemented compact layout

The full display is exactly 500x360. The collapsed header remains 500x58. The hierarchy is deliberately flat below the full panel so unresolved scripted visibility cannot stack former tab bodies.

- Header title/subtitle safe area: x 36..412, y 10..64.
- Collapse control: x 420..468, y 10..50.
- Portrait safe area: x 38..158, y 80..226.
- Name: x 32..164, y 234..256.
- Mandate row: x 176..458, y 82..114; meter x 176..294; value x 304..458.
- Dependence row: x 176..458, y 126..158; meter x 176..294; value x 304..458.
- Exposure row: x 176..458, y 170..202; meter x 176..294; value x 304..458.
- Capacity row: x 176..458, y 214..246; meter x 176..294; value x 304..458.
- Qualitative role/control line: x 36..464, y 270..300.
- Footer: x 36..464, y 322..346.

The portrait and meter columns have an 18-pixel horizontal separation before the first meter. Meter rows use a fixed 44-pixel vertical rhythm. Labels and dynamic values share fixed baselines and widths. Only installed fonts already present in the prior Event 016 GUI are used: `hoi_24header`, `hoi_20b`, and `hoi_16mbs`.

The five Overview/Projects/Facilities/Foreign/Sovereignty tabs, tab controls, tab labels, cards, lower content panels, project/facility/foreign/sovereignty prose, warning markers, project markers, singularity markers, and animation toggle were removed from the window and its presentation wiring. Their gameplay decisions remain below the attachment.

## Background coverage and asset evidence

The asset owner supplied the exact 500x360 runtime DDS at `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds`.

- Size: 720128 bytes.
- SHA-256: `C981DF3D82FEF7D8CBE7806FD4EBFE4E27908B6FA23A96F07F32F8ABE0984FF4`.
- Decoded runtime evidence: `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/decoded_dds/directorate_background.png`.
- Safe-region evidence: `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/contact_sheets/directorate_background_safe_regions.png`.
- PNG-to-DDS roundtrip comparison: `docs/assets/016_brilliant_scientist/directorate_ui/compact_refresh/contact_sheets/directorate_background_roundtrip_contact.png`.

The decoded DDS and roundtrip contact sheet were reviewed visually. Ornament is confined to the perimeter, the portrait and four meter bays are clear, the header centre remains readable, and the two lower text strips contain no competing decoration.

## Budgets and density audit

- Visible mechanic values: exactly four, Mandate, Dependence, Exposure, and Capacity.
- Government Control: one qualitative phrase inside the single role/control line; it is not a fifth meter.
- Gameplay actions in the GUI: zero. Decisions below remain the action surface.
- Utility controls: one expand control in collapsed state or one collapse control in full state.
- Spendable GUI costs: zero.
- Texticon coverage: not applicable because the compact attachment paints no cost.
- Paragraph blocks: zero.
- Footer: one concise dynamic line pointing to the relevant decisions.
- Duplicate counts: none.

Each value has one compact tooltip describing meaning, primary sources of change, and why a high value matters. Tooltips are two short lines rather than the prior ledgers. The longest qualitative role strings were shortened for localisation expansion safety.

## State and interaction matrix

| State | Expected presentation | Interaction |
| --- | --- | --- |
| Full normal | Header, Kruger portrait/name, four meters, role/control line, footer | Collapse only |
| Hover/selected/active | Same content; only the close control uses its registered four-state sprite behavior | Collapse only |
| Disabled/warning/completed | No fake state cards or duplicate panels; the read-only values remain legible | Collapse remains enabled |
| Empty/full decision list | Attachment remains compact; decisions below own list density | No action added to attachment |
| Long text | Fixed title, 154-pixel value fields, 428-pixel role/footer fields | No overlap-dependent content swapping |
| Collapsed | 500x58 header, title, expand control | Expand only |

The open and close click regions match their authored 48x40 safe regions at x 422, y 11. No decorative element is styled as a clickable button.

## Post-change MCP evidence

The post-source inspect completed with `GUI_INSPECTED`, revision `32df38fbe8b54e58a17c1827e0e0ad99cec3571c11da9c574302a5f7eeff595d`, and 23 exact inspected elements, down from 65. Its artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de6313a47a786ffde80922dcbd3d899704e0062cf34d0543379ee5d91b5f29fc/e341959a91b175e8d43a81e9ec2412f0ab0ad84bb4aeb2fcd367457820c4759b/gui-inspect.32df38fbe8b54e58.json`.

The corresponding 1366x768 and 1920x1080 multi-state render completed with `GUI_RENDERED` for normal, hover, disabled, warning, active, completed, and long-text states. The linked full-window artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa578ff158f3093ebf63e6b31445e7a105b5d6f245d578f97b3c9adb0d488403/09580aa87981749dc861474fb74474ce6c5e395d9200c20056624fc3da91027d/kruger_directorate_container-full.svg`.

After the final 500x360 DDS was installed, a forced current inspect completed with `GUI_INSPECTED`, shared revision `aed02946b443e301ee4e4c994b1301ea31cbe161dbf8fe683bdbbdd9686bfab7`, 23 exact inspected elements, and no exact-window blocker. Its artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c028c2ef74d776b90ca6cbb5a58d573046c65f3934f67a2fa9b85bcddbf9e69d/b34745d3f51a532b2727a16ba92a1c3a99bda09a07037eeae95b9669ba03fdf9/gui-inspect.aed02946b443e301.json`.

A forced post-art render requested 1366x768 and 1920x1080 plus normal, hover, selected, active, disabled, warning, completed, empty-list, full-list, and long-text states, with the rejected baseline as comparison. It completed with `GUI_RENDERED`, no blockers, and no render diagnostics:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa578ff158f3093ebf63e6b31445e7a105b5d6f245d578f97b3c9adb0d488403/dfccdf54939cce68d182038b23ea83b065895ba0d8341b033e916e24c2d8b704/kruger_directorate_container-full.svg`.

A collapsed-flag render was also requested at both resolutions for normal, hover, disabled, and long-text states. It completed with `GUI_RENDERED`:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa578ff158f3093ebf63e6b31445e7a105b5d6f245d578f97b3c9adb0d488403/503f3ba808ea4a43e650db49234d7e28eb44003ddf1f15c46c1c783b81cb4fb9/kruger_directorate_container-full.svg`.

The render artifact SHA remained `AA578FF158F3093EBF63E6B31445E7A105B5D6F245D578F97B3C9ADB0D488403` across the pre-art, post-art, and collapsed requests even though the inspect revision changed and the installed DDS has SHA `C981DF3D...`. This is an MCP render-artifact cache limitation. The attempted local artifact stream produced only 32746 bytes of the advertised 534064-byte SVG. It was rasterized after its lock released and visually reviewed; the browser reported `EntityRef: expecting ';'` at column 23438 and could render no GUI content, confirming that the stream was incomplete rather than usable final evidence. This handoff therefore does not claim that the linked SVG visibly incorporated the final DDS pixels. The decoded final DDS and fresh 500x360 source geometry are the authoritative final-art review evidence.

The inspect response retained a repository-wide `GUI_VALIDATION_DIAGNOSTICS_TRUNCATED` ceiling. The only inline diagnostic unrelated to the ceiling was an Event 005 sprite collision. No exact Event 016 blocker was returned. Aggregate repository diagnostic counts are not treated as a scoped Event 016 verdict.

## Before and after rationale

Before, the window attempted to duplicate the decision system in five tabbed summaries and depended on mutually exclusive scripted visibility for safe geometry. Offline unresolved visibility therefore produced an unreadable stack, and the 620-pixel body displaced the actual decisions.

After, the attachment answers only who directs the programme, how four accepted pressures currently stand, and where the player acts next. Its 360-pixel body removes 260 pixels of vertical bulk, eliminates all content swapping, reduces the exact element graph from 65 to 23 elements, and keeps the portrait and meters in separate grid columns.

## Remaining parent-owned validation and limitations

- Parent/user live consumer validation remains required for the decision-category attachment, dynamic scripted localisation values, dynamic meter sprite selection, hover frames, and open/collapse behavior.
- The final post-art SVG could not be visually certified because MCP reused a cached render SHA and the local artifact stream was truncated to 32746 of 534064 bytes; its rasterized browser view showed an XML `EntityRef` parse error rather than the GUI. The exact decoded DDS and safe-region contact sheet were visually certified instead.
- `hoi4.gui_rewrite` remains blocked by the recorded adapter `INTERNAL_ERROR`; the normal bounded patch is present.
- Dormant localisation for the removed dashboard remains in the Event 016 GUI localisation file because deleting unused strings was not necessary for presentation correctness and would broaden this visual patch. None of those keys is painted or bound by this window.
- No gameplay simplification or fallback was introduced. The redesign intentionally delegates all orders to the existing decisions, as required by the accepted brief.

## Parent acceptance addendum

After the worker handoff, parent review removed the redundant subtitle and moved the single title from y 10 to y 22. The matching subtitle visibility binding was removed. This reduced the expanded exact element count from 23 to 22 and kept the four-value surface unchanged.

A fresh final `hoi4.gui_inspect` and `hoi4.gui_render` both completed with `GUI_INSPECTED` and `GUI_RENDERED`. The final exact 1366x768 normal-state SVG was streamed without truncation: 532257 of 532257 bytes, 17 chunks, closing SVG tag present, SHA-256 `6F444EE55E353657A7C6CFB2743A037B171D2172C710164305FCA8D68A2EBA40`.

Final artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f444ee55e353657a7c6cfb2743a037b171d2172c710164305fca8d68a2eba40/fe655d71ae7e423de16d93ebfb43b0d833e9bc79a8d610f8da416489fad5ff2e/kruger_directorate_container-full.svg`.

The rasterized final artifact was visually reviewed. It shows one clear title, the close control, the isolated Kruger portrait and name, four evenly spaced meter/value rows, one role/control line, and one footer. No tabs, cards, duplicate panels, text collisions, meter collisions, or ornamental collisions remain. The MCP-only `OFFLINE APPROXIMATION · NOT HOI4` badge overlaps the upper-left of the title region; this badge is injected by the renderer and is not part of the authored GUI.
