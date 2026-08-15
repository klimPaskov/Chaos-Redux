# Event 19 Muster Board GUI and Decision Audit

## Scope and outcome

This audit covered the direct Event 19 Muster Board GUI, its scripted-GUI contract, the opening decision and category, direct GUI localisation, and the registered background asset.

The board is functionally wired as a human-only top-bar window rather than a decision-category embed, so the category correctly does not declare `scripted_gui = infantry_spawn_muster_board_scripted_gui`.

The board opens through `infantry_spawn_open_muster_board` and closes through `infantry_spawn_muster_board_close`.

No broad mechanic or Event Log file was changed.

## Changed files and identifiers

- `interface/019_infantry_spawn_muster_board.gui`
  - Repositioned the 23 visible action-label controls inside their corresponding scaled `buttonType` bounds on the Lots, Command, and Anomalous panels.
  - Reduced `infantry_spawn_muster_history_list_panel` from 374 to 346 pixels and its dynamic grid from 366 to 338 pixels so both end within the 450-pixel parent panel.
  - Corrected `alwaysTransparent` to the documented `alwaystransparent` token on `infantry_spawn_muster_lot_entry_text`, `infantry_spawn_muster_family_entry_text`, and `infantry_spawn_muster_history_entry_text`.
- `localisation/english/019_infrantry_spawn_l_english.yml`
  - Added the existing support-equipment cost line to `infantry_spawn_muster_gui_lot_cadres_tt`.

The relevant direct contract IDs are `infantry_spawn_muster_board_window`, `infantry_spawn_muster_board_scripted_gui`, `infantry_spawn_open_muster_board`, and `infantry_spawn_formation_management_category`.

## Before and after behavior

Before this patch, the Lots, Command, and Anomalous text labels were displaced above and in some cases outside their intended button hit regions.

After this patch, those labels are visually centered within their scaled controls and remain transparent to clicks, so their underlying button receives the action.

Before this patch, the history list extended 18 pixels beyond its clipped parent panel.

After this patch, the list viewport ends at 440 pixels inside a 450-pixel panel and displays eight complete 42-pixel entries before scrolling.

Before this patch, the Cadres GUI action omitted the same support-equipment cost already declared on the equivalent decision.

After this patch, its hover tooltip presents the action result and the actual shared cost.

## Audit findings by severity

### Medium — unresolved renderer evidence

`hoi4.gui_inspect` and `hoi4.gui_render` both returned `SCAN_BYTE_LIMIT` for the `mod_chaos_redux_ea3b2d67c2c0` workspace before scanning any file or producing an artifact.

No MCP render, resolution comparison, hover-state capture, or artifact reference is therefore available for this pass.

Source geometry and the active background DDS were inspected as the fallback, but that cannot prove final in-game pixel fidelity.

### Low — fixed action-label alignment and hit-region clarity

The 23 text overlays for Lots, Command, and Anomalous actions did not sit within the rendered positions of their buttons.

They now lie inside their buttons and use `alwaystransparent = yes` so hover and clicks resolve to the matching interactive control.

### Low — fixed history clipping

The history viewport exceeded its parent clipping boundary by 18 pixels.

The viewport and grid now terminate inside the panel boundary.

### Low — fixed Cadres cost disclosure

`infantry_spawn_preserve_specialist_companies` has a support-equipment custom cost and subtracts it in `infantry_spawn_start_specialist_preservation`.

The direct GUI tooltip now exposes that same cost.

## Lifecycle and route-lock notes

The scripted GUI is visible only to human players with `infantry_spawn_muster_board_open` and `infantry_spawn_muster_board_is_available`.

Availability requires the ordinary management category to remain relevant, Evolution III, and no world-end state.

The country pulse calls `infantry_spawn_muster_board_close_if_irrelevant` and `infantry_spawn_muster_board_refresh_if_open`, so an invalid board flag is cleared and an open valid board is rebuilt.

`infantry_spawn_muster_board_rebuild_view_unlocked` returns the active tab to Overview if the active claimant vanishes or if the anomalous registry or a relevant family becomes unavailable.

The Command and Anomalous tabs, their panels, and their conditional controls each have matching scripted-GUI visibility triggers.

## Decision and mission quality notes

The board has 41 action controls and the scripted GUI has a one-to-one `*_click` effect and `*_click_enabled` trigger for every control.

The human-only GUI button AI state is intentional because AI uses the corresponding decision AI or direct common effects rather than interacting with a player window.

`infantry_spawn_run_anomalous_family_ai` is called from `common/scripted_effects/019_infantry_spawn_pulse_effects.txt` for eligible non-derivative AI countries.

That controller selects the highest-pressure family, validates the same resource and route triggers as the GUI, and chooses containment, dispersal, sustainment, cantonment, restricted deployment, liaison, or a train/spawn action through weighted direct effects.

Claimant actions retain nonzero decision AI weights in `common/decisions/019_infantry_spawn_claimant_decisions.txt`.

The active missions are non-selectable timed state displays in `infantry_spawn_formation_management_category` rather than GUI buttons.

| Mission set | Owner and category | Region or target | Duration and outcome | Duplicate risk |
| --- | --- | --- | --- | --- |
| `infantry_spawn_formation_roll_call_mission`, `infantry_spawn_standardization_cycle_mission`, `infantry_spawn_supervised_demobilization_mission`, `infantry_spawn_training_cycle_mission`, `infantry_spawn_muster_districts_mission`, `infantry_spawn_officer_search_mission`, `infantry_spawn_specialist_preservation_mission`, and `infantry_spawn_rail_corridor_mission` | Event 19 country in `infantry_spawn_formation_management_category` | Country-level, with stable selected-lot targets where applicable | Dynamic mission-day variables and a dedicated defer-or-complete timeout effect | Low because each running-state flag gates visibility and start availability |
| `infantry_spawn_request_cooldown_mission` | Event 19 country in the same category | Country-level request cooldown | Dynamic cooldown duration and `infantry_spawn_defer_or_finish_request_cooldown` | Low because the request cooldown flag blocks repeat requests |
| `infantry_spawn_achievement_combat_trial_mission` | Event 19 country in the same category | Country-level achievement trial | Dynamic timeout and a cancellation cleanup effect | Low because its active flag controls visibility and cancellation |

## Cost, tooltip, cleanup, and exploit-risk notes

Request, lot-management, claimant, and anomalous-family GUI actions use dedicated hover tooltips rather than raw script triggers.

The request and anomalous-family tooltips show the matching dynamic decision description and cost localisation.

Every transaction rechecks its availability trigger inside the effect, which protects against stale GUI state and prevents a free action after a resource, target, or route change.

The family ledger is rebuilt and expired management state is cleaned during refreshes.

No passive political-power-only exchange, free unit loop, cooldown bypass, or missing cleanup path was found in this direct GUI surface.

## Asset and localisation notes

`GFX_infantry_spawn_muster_board_background` correctly points to `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds`.

The active DDS hash matches `docs/assets/019_infantry_spawn/gui_background_richer_2026_07/runtime_dds/infantry_spawn_muster_board_background_richer_960x640.dds` with SHA-256 `758A9EC88A7F329B9A3AAF7A6570135E1E15BECB75EF1BFD8F1A8DB8439AA849`.

The active 960 by 640 background intentionally provides a frame, header field, and neutral interior rather than pre-authored interactive slots, so it does not conflict with the panel layout.

All 67 direct GUI text keys resolve in `localisation/english/019_infrantry_spawn_l_english.yml`, which retains its UTF-8 BOM.

## Meaningful validation

- Static GUI contract check found 41 `buttonType` controls, 41 matching scripted-GUI click effects, and 41 matching click-enabled triggers.
- Static localisation check found all 67 direct GUI text keys in the English localisation file.
- No camel-case `alwaysTransparent` tokens remain in the Muster Board GUI.
- The history viewport arithmetic is `94 + 346 = 440`, which is within the 450-pixel parent panel, and the grid arithmetic is `0 + 338 = 338`, which is within the 346-pixel viewport.
- `git diff --check -- interface/019_infantry_spawn_muster_board.gui` returned no whitespace errors.

The meaningful validation deliberately skipped an MCP visual render because the service scan failed with `SCAN_BYTE_LIMIT` before artifact creation.

## Completion assessment

The direct GUI and decision integration satisfy the decision-and-mission skill's action-contract, cost disclosure, AI-parity, lifecycle, cleanup, and tooltip requirements on source evidence.

Full visual fidelity remains unverified until the MCP scan-byte-limit problem is resolved or an in-game consumer review supplies render evidence.

No separate broad-mechanic plan was required.
