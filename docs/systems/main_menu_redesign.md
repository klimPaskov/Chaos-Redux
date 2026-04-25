# Main Menu Redesign

## Overview

The main menu is implemented through `interface/frontendmainview.gui` with assets registered in `interface/frontendmainviewbg.gfx`. The layout follows the style reference in `tmp/maxresdefault.jpg`: a full-screen background, a large centered mod logo that overlaps the lower overlay, and a wide lower menu panel with an about text on the left, main navigation in the middle, and the Discord community button on the right.

## Structure

1. `frontend_background` keeps using `GFX_frontend_bg`, which points at `gfx/chaosx_main_menu.dds`.
2. `mainmenu_panel_upperleft` now acts as the centered logo container and displays `GFX_chaos_redux_logo`.
3. `mainmenu_panel_bottom` is a larger lower centered panel with the visible main menu controls.
4. `mainmenu_single_player` uses the same lower panel placement so the single-player submenu opens in the same visual area.
5. Vanilla social links and subscription widgets are kept in the GUI by name for compatibility, but moved out of the visible area.
6. The about text uses `chaosx_welcome_intro_loc` with `chaosx_left_standardtext_slider` so the full welcome intro can be read inside the shorter left column with the scrollbar on the left.

## Assets

| Asset | GFX token | File |
| --- | --- | --- |
| Main menu background | `GFX_frontend_bg` | `gfx/chaosx_main_menu.dds` |
| Main logo | `GFX_chaos_redux_logo` | `gfx/interface/chaos_redux_logo.dds` |
| Discord button | `GFX_discord_button` | `gfx/interface/discord_button.dds` |

No additional assets are required for the current implementation. If you want the right side to match the reference more closely, add optional decorative badge art at `gfx/interface/chaosx_main_menu_badge.dds` and register it in `interface/frontendmainviewbg.gfx`.

## Localisation

Visible custom menu text lives in `localisation/english/chaosx_gui_l_english.yml`:

- `chaosx_main_menu_about`
- `chaosx_welcome_intro_loc`
- `chaosx_main_menu_community`
- `chaosx_main_menu_discord`

The Discord tooltip reuses `chaosx_discord_button_tt`.
