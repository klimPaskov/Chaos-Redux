# Main Menu Redesign

## Overview

The main menu is implemented through `interface/frontendmainview.gui` with assets registered in `interface/frontendmainviewbg.gfx` and `interface/frontendmainviewbg_basic.gfx`.
The layout is a full-screen Chaos Redux painting, a large centred mod logo, and a lower menu panel with the about text on the left, main navigation in the middle, and community links on the right.

## Structure

1. `frontend_background` keeps the vanilla anchoring: centred, 100% wide, height from the 4:3 aspect ratio, so the painting covers the screen and is cropped evenly at the top and bottom.
2. `mainmenu_panel_bottom` is anchored to the bottom centre (`center_down`), 1070x355, 10 px above the bottom edge.
3. `mainmenu_panel_upperleft` covers the screen with a 26 px top margin and a 389 px bottom margin, reserving the lower panel, its 10 px bottom offset, and a 24 px gap.
4. Its centred `logo_art` child holds the 592x669 painting at natural size and clamps both dimensions to the available area with `preserve_aspect_ratio = yes`.
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
At 1920x1080 the painting fills the available height between the top margin and lower panel gap.

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
