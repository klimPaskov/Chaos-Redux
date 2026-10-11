# Main Menu Redesign

## Overview

The main menu is implemented through `interface/frontendmainview.gui` with assets registered in `interface/frontendmainviewbg.gfx` and `interface/frontendmainviewbg_basic.gfx`.
The layout is a full-screen Chaos Redux painting, a large centred mod logo, and a lower menu panel with the about text on the left, main navigation in the middle, and community links on the right.

## Structure

1. `frontend_background` keeps the vanilla anchoring: centred, 100% wide, height from the 4:3 aspect ratio, so the painting covers the screen and is cropped evenly at the top and bottom.
2. `mainmenu_panel_bottom` is anchored to the bottom centre (`center_down`), 1070x355, 10 px above the bottom edge.
3. `mainmenu_panel_upperleft` covers the screen with a 26 px top margin and a 389 px bottom margin, reserving the lower panel, its 10 px bottom offset, and a 24 px gap.
4. Its centred `logo_reserve` child is 741 px high, capped to the available height, and spans the available width.
The `logo_art` child uses `center_up` for both orientation and origo, with a 36 px vertical inset.
It holds the 592x669 painting at natural size and clamps both dimensions to the reserve with `preserve_aspect_ratio = yes`.
The reserve's 72 px of extra height balances the inset when it fits; when it clamps, the inset lowers the logo while preserving its size.
The `GFX_chaos_redux_logo_scaled` background fills that child, preserving the original artwork and its aspect ratio.
5. `mainmenu_single_player` uses the same lower panel placement so the single-player submenu opens in the same visual area.
6. Vanilla social links, subscription widgets, the credits and nudge buttons, and the `frontend_game_logo` icon are kept by name for the frontend controller but moved out of the visible area.
7. The about text uses `chaosx_welcome_intro_loc` with `chaosx_left_standardtext_slider`, whose offsets follow the 300 px column width so the scrollbar sits left of the text.

Shared layout tuning uses the `@chaosx_menu_*` constants at the top of `interface/frontendmainview.gui`.

## Background registration

The background manager replaces the texture of `GFX_frontend_bg` with the selected entry from `common/frontend/backgrounds`.
Chaos Redux overrides `common/frontend/backgrounds/base_backgrounds.txt` with the single entry `chaosx_main_menu`, keeps the texture at `gfx/loadingscreens/chaosx_main_menu.dds` as the manager requires, and points both `GFX_frontend_bg` and `GFX_frontend_bg_basic` at it.
With one background the vanilla background picker has nothing to offer, so `change_background_button` is hidden, following the Kaiserreich precedent.

## Resolution and UI-scale coverage

HOI4 UI scale divides the physical resolution into the virtual GUI canvas.
The logo height is the smaller of its natural 669 px and the virtual canvas height minus 415 px.
The following dimensions are calculated in virtual GUI pixels, with the two scale-1 target resolutions also checked in game:

| Resolution | UI scale | Virtual canvas | Logo (px) | Free area above panel |
| --- | --- | --- | --- | --- |
| 1920x1080 | 1.0 | 1920x1080 | 588x665 | 715 |
| 1920x1080 | 1.5 | 1280x720 | 270x305 | 355 |
| 2560x1440 | 1.0 | 2560x1440 | 592x669 | 1075 |
| 3840x2160 | 1.5 | 2560x1440 | 592x669 | 1075 |
| 1366x768 | 1.0 | 1366x768 | 312x353 | 403 |
| 1366x768 | 1.25 | 1093x614 | 176x199 | 249 |

At 1366x768 with UI scale 1.5 (911x512) the 1070 px panel is wider than the screen; the vanilla main menu does not fit that canvas either.
The 2560x1440 composition retains the lower panel from the user-selected `13b8fabb9` reference and places the logo centre within two pixels of that revision's vertical anchor.
The natural-size ceiling preserves space around the painting at that resolution.
At 1920x1080 the painting keeps its 665 px height and starts at y=62, placing its bottom at y=727, 12 px behind the lower panel's logical top at y=715.
The lower panel is declared after the decorative logo window and supplies the covering foreground.

### Small-height logo placement

Acceptance basis: the user's 1920x1080 screenshot `C:/Users/klimp/AppData/Local/Temp/claude/C--Users-klimp-OneDrive-Documents-Paradox-Interactive-Hearts-of-Iron-IV-mod-chaos-redux/b61fc2d1-fe9b-40e4-933a-f2accfc459e6/images/20.webp` and explicit instructions to lower the hand by 25–40 px, retain the current 1080 size, and preserve the 1440 placement exactly.
The reference maps the decorative painting to `mainmenu_panel_upperleft/logo_reserve/logo_art` and the covering panel to `mainmenu_panel_bottom`; controls, their hit regions, animation timing, and artwork retain their existing definitions.
At the settled animation position and UI scale 1, let `A = screen height - 415`, `L = min(669, A)`, and `R = min(741, A)` for the requested widths, none of which constrain the logo horizontally.
The old top is `26 + (A - L) / 2`; the settled top is `26 + (A - R) / 2 + 36`.
The shift is 36 px at heights through 1084, tapers continuously to zero between 1084 and 1156, and is zero at larger heights.
This avoids a resolution-specific percentage-position formula and preserves the natural-size composition above the reserve's clamp threshold.

| Resolution, UI scale 1 | Logo size, unchanged | Before top–bottom | Settled top–bottom | Shift | Lower panel top |
| --- | --- | --- | --- | --- | --- |
| 1920x1080 | 588.46x665 | 26–691 | 62–727 | +36 | 715 |
| 2560x1440 | 592x669 | 204–873 | 204–873 | 0 | 1075 |
| 1920x1200 | 592x669 | 84–753 | 84–753 | 0 | 835 |
| 1366x768 | 312.37x353 | 26–379 | 62–415 | +36 | 403 |

The source-derived previews and exact geometry are in `.tmp/menu_logo_clamp_20261011/`, with `before_<width>x<height>.png`, `after_<width>x<height>.png`, and `geometry.json`.
They decode the unchanged artwork and draw a labelled opaque guide for panel coverage; they omit controls and are calculated layout illustrations, not native or MCP renders.
The 1440 and 1200 preview content is byte-identical above the phase caption, and the check asserts the unchanged 665 px logo height and 36 px shift at 1080.
The top is clear at every requested resolution.
The 12 px logical overlap is source evidence; the exact textured panel-edge occlusion remains unobserved in the engine.

Reference evidence: `hoi4.reference_context(surface=gui)` and `hoi4.reference_search` succeeded and returned the offline Interface modding revision `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c` and installed scripted-GUI documentation revision `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`.
The read request starting before its selected section was rejected; its corrected request stalled together with the installed-documentation read and source lookup, so the relevant local sections were read directly.
Interface modding lines 77–98 document nested containers, parent-relative percentage sizes, orientation, origo, and clipping; lines 369–386 document orientation-relative positioning.
Installed `common/scripted_guis/_documentation.md` lines 1–40 document attachment, but do not specify percentage-position semantics; no installed prose documentation for that behavior was found.
Vanilla `interface/combatlogview.gui` lines 393–429 places the nested `lower` container at `y=50%%` below its half-height `upper` sibling, supporting a parent-relative interpretation rather than a screen-relative one; this is precedent-derived inference, not an explicit prose rule.
That file's SHA-256 is `2a0f4a8679891835068de10c125731b369205eade41497304a4f3ba3a38f5a5f`.
Vanilla `interface/frontendmainview.gui` lines 1–12 demonstrates capped, aspect-preserving container size, revision `17e5f3cde42d170b9e4ac40bb2312cd2d505767920b6e995c5c58b48c38efd1b`; `interface/AST_cabinet_trust_scripted_gui.gui` lines 16–21 demonstrates `center_up` placement.

The four-resolution `hoi4.gui_render` baseline request stalled without artifacts and was stopped.
The narrower 1080 retry first rejected `uiScale` inside `scenario.resolution`; the corrected schema request timed out at 90 seconds without artifacts.
No MCP before/after paths, visual verdict, or engine test is claimed; no further renderer retry is justified unless service health changes or new input addresses the stall.
The source implementation and calculated comparison are present with no design simplifications; the explicitly requested MCP before/after render output remains unavailable.
Skills used: `chaos-redux-scripted-gui` and `chaos-redux-shared-git-commit`.

Live evidence from Linux HOI4 1.19.3, windowed at UI scale 1, is under `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/after/live_2026-10-11/`: `main_menu_1920x1080.png` and `main_menu_2560x1440.png`.
The other rows are source geometry, not live checks.
The offline preview did not faithfully apply the margins or hidden controller-icon placement, so it was not used for visual acceptance.

## Animation

1. `mainmenu_panel_bottom` starts below the screen at `@chaosx_menu_panel_start_y` and settles at `@chaosx_menu_panel_y` over `@chaosx_menu_panel_anim_time`. Its `hide_position` is also `@chaosx_menu_panel_y`, so switching away from the first menu has no slide-out movement.
2. `mainmenu_panel_upperleft` starts 120 px lower at `@chaosx_menu_logo_start_y` and rises to its zero offset over the same beat, fading in.
Its margins place the painting within the free area, and its `hide_position` equals the settled position.
3. Main menu and single-player menu buttons remain direct children of their hard-coded parent windows. The frontend controller searches those parent windows directly by button name, so nesting these buttons inside helper containers breaks menu binding.
4. `mainmenu_single_player` uses the final panel position directly and has no animation attributes.

## Assets

| Asset | GFX token | File |
| --- | --- | --- |
| Main menu background | `GFX_frontend_bg`, `GFX_frontend_bg_basic` | `gfx/loadingscreens/chaosx_main_menu.dds` |
| Main logo (stretched) | `GFX_chaos_redux_logo_scaled` | `gfx/interface/chaos_redux_logo.dds` |
| Main logo (hidden controller icon) | `GFX_chaos_redux_logo` | `gfx/interface/chaos_redux_logo.dds` |
| Community buttons | `GFX_discord_button`, `GFX_donation_button`, `GFX_homepage_button`, `GFX_github_button`, `GFX_documentation_button`, `GFX_chaosx_youtube_button` | `gfx/interface/*.dds`, registered in `interface/chaosx.gfx` |

## Localisation

Visible custom menu text lives in `localisation/english/chaosx_gui_l_english.yml`:

- `chaosx_main_menu_about`
- `chaosx_welcome_intro_loc`
- `chaosx_main_menu_community`
- `chaosx_main_menu_version`

## Future plans

- A dedicated small thumbnail would let the background picker return if Chaos Redux ever ships several menu paintings.
