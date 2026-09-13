# Repression ledger parser repair reference

The parent selects `screenshots/repression_ledger_mcp_before.png` as the intended unchanged overview composition for this bounded parser repair.
Acceptance is within the user's explicit authorization to fix errors with small GUI tweaks while preserving the design.
This is an MCP reference image, not a live-game capture or teaser asset.
No generated replacement art is required because the intended geometry and assets are identical to the baseline.

The authorized runtime file is `interface/camp_repression_ledger.gui` and the linked window is `repression_ledger_window`.
The existing opener and tab/selection bindings remain in `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`; this repair does not edit that file.
The baseline scenario is `startup_repression_overview`, with the overview visible and the state-pools, locations, selected-location, country and discovery panels hidden, at 2560 × 1440 and UI scale 1.
Exact fixture arguments are in `gui_render_arguments.json`.

| Reference region | Existing native IDs | Intended repair and preserved behavior |
| --- | --- | --- |
| Left navigation background | `camp_ui_navigation_background` | Replace the invalid sized icon with a same-size container and the same tiled sprite background. |
| Overview cards | `camp_ui_harm_surface`, `camp_ui_strain_surface`, `camp_ui_evidence_surface` | Same container conversion, preserving every position, dimension and sprite; retain overlaid live text. |
| Accountability cards | `camp_ui_record_exposure`, `camp_ui_record_losses`, `camp_ui_record_closure` | Same container conversion; retain the existing tab visibility and live labels. |
| Five navigation selection overlays | `repression_ledger_tab_overview_mark`, `repression_ledger_tab_state_pools_mark`, `repression_ledger_tab_sites_mark`, `repression_ledger_tab_country_mark`, `repression_ledger_tab_discovery_mark` | Use sized buttons with the existing sprite, frame and click-through field; preserve their visibility bindings. |
| Dynamic selected rows | `camp_ui_pool_selected`, `camp_ui_site_selected` | Preserve row size, position, selected frame and click-through behavior using a sized button. |

The engine constraint is demonstrated by 14 fresh `Unexpected token: size` errors for `iconType` in launch 02.
Installed vanilla `interface/airselectionview.gui` provides a sized-button precedent and `interface/career_profile/award_display.gui` provides sized containers with backgrounds.
The rejected all-button candidate had no pixel difference but seven missing-action blockers for passive background elements; the revised source addresses those blockers without adding actions.

The overview reference has three mechanic values and five navigation choices.
Its dynamic-localisation placeholders reflect unsupplied runtime data in this fixture and do not establish correct live values or text fitting.
The user authorized direct source repair on resumption, and the updated scripted-GUI skill makes the rewrite route optional.
The applied 14-element delta is preserved in `applied_repression_parser_fix.patch`; it retains intervening title and navigation-label alignment work.
The production post-repair overview and click-region images are in `gui_post_repair_artifacts/`, with the response in `gui_post_repair_result.json`.
Visual review found intact overview cards, readable static labels and navigation hit regions aligned with the five buttons, with no additional hit regions over the passive cards.
The requested fixture resolution was 2560 × 1440, but the returned full image is 1920 × 1080 and the crop is 992 × 632; these artifacts only demonstrate their actual dimensions.
The render's default same-source zero-pixel comparison does not establish before-and-after equivalence.
Launch 03 cleared the 14 GUI parser errors but still crashed before the main menu.
Remaining acceptance work includes crash resolution, live startup, populated values, all tabs and dynamic rows, hover/selected states, and save/reload behavior.
No whole-interface completion or live visual acceptance is claimed.

The parent compared the archived baseline crop and post-repair crop visually.
The static cards and content geometry are retained; the visible differences are the intervening centered navigation labels and small title alignment adjustment preserved from current source.
The post-repair production source revision is dbcf01f39d0345caf198aa63268bf26587767c77f039be1fbaf1281399052481.
Dynamic placeholders in both fixtures are unresolved runtime data, so no populated-value text-fitting claim is made.

