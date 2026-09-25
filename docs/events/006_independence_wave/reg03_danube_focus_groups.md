# REG-03 Danube Package Focus Groups

## Purpose and ownership

The IW-023 Transylvania, IW-029 Bosnia, and IW-026 Macedonia packages each receive a five-node shared-focus group that connects local institutions and transport to the package's existing settlement ledgers. The three groups are defined once as root-level `shared_focus` blocks in `common/national_focus/006_independence_wave_focus.txt`; the full Event 006 tree imports all fifteen IDs, while `common/national_focus/austro_hungarian_releasable_shared.txt` imports only the ten TRA and BOS IDs supported by the reviewed Austro-Hungarian carrier. MAC remains full-framework only.

TRA and BOS open after either the full tree's capital-administration focus or the shared-overlay independence review focus, expressed as two `focus =` entries inside one native OR `prerequisite` block, then use their matching package contract and controlled-capital anchor at state 84 or 104. MAC opens from the full tree's capital-administration focus and uses state 106. Exact package gates prevent a group from appearing for another release. The user approved preserving the shared definitions and recording the current shared-focus layout evidence as blocked because the installed MCP inspector omits imported root-level `shared_focus` nodes.

Each route takes four focuses: a 5-unit opening, a 5-unit logistics step, one 7-unit mutually exclusive branch, and a 7-unit docket. The selected route costs 24 focus units, or 168 days at normal speed. The existing 420-day founding crises and all decision costs, project durations, cancellation conditions, and failure effects remain in force.

## Group routes and effects

| Package | Opening and logistics | Civilian branch | Frontier branch | Docket and gate |
| --- | --- | --- | --- | --- |
| IW-023 TRA | `independence_wave_tra_register_district_authorities` gives federal legitimacy +5; `independence_wave_tra_account_for_rails_and_mines` gives frontier cohesion +5. | `independence_wave_tra_seat_the_district_assembly` gives federal legitimacy +10 and frontier cohesion −5. | `independence_wave_tra_mandate_the_frontier_guard` gives frontier cohesion +10 and federal legitimacy −5. | `independence_wave_tra_publish_border_arbitration_docket` gives both ledgers +5 and requires the paid assembly or regulars-screening receipt. |
| IW-029 BOS | `independence_wave_bos_convene_sarajevo_service_board` gives Drina civic mandate +5; `independence_wave_bos_map_drina_passes_and_depots` gives mountain defence +5. | `independence_wave_bos_bind_cantonal_guarantees` gives Drina civic mandate +10 and mountain defence −5. | `independence_wave_bos_commission_mountain_veterans` gives mountain defence +10 and Drina civic mandate −5. | `independence_wave_bos_publish_drina_corridor_docket` gives both ledgers +5 and requires the paid cantonal-council or garrison-screening receipt. |
| IW-026 MAC | `independence_wave_mac_register_vardar_municipal_offices` gives civic mandate +5; `independence_wave_mac_survey_vardar_rail_and_grain` gives mountain defence +5. | `independence_wave_mac_ratify_village_appeals` gives civic mandate +10 and mountain defence −5. | `independence_wave_mac_screen_mountain_veterans` gives mountain defence +10 and civic mandate −5. | `independence_wave_mac_publish_vardar_arbitration_docket` gives both ledgers +5 and requires the paid community-council or veteran-screening receipt. |

All changes use the existing package-specific pressure constants and `independence_wave_change_tra_settlement_values`, `independence_wave_change_bos_ledgers`, or `independence_wave_change_mac_ledgers` effect. Those helpers clamp the values and refresh their lifecycle ideas. The focus group does not set mission-completion or paid-decision flags, add claims or cores, transfer states, admit countries, settle a former host, open a network, or bypass paid projects.

The selected branch's companion paid action supplies one further +5 to that branch ledger. When the paid receipt already exists, the branch focus applies the companion during its own completion reward. When the focus is already complete, the successful decision's `remove_effect` applies it after setting its paid-only receipt. The six callbacks check the exact package, receipt, matching completed focus, and an awarded marker, then set both temporary ledger deltas before calling the existing clamped ledger effect. The awarded markers survive package cleanup when the additive carrier retains completed focus history, preventing a later generation from granting the same companion again. A full-framework reload clears those markers alongside the focus history it resets. The branch foci are mutually exclusive, so at most one companion applies per selected route. Cancellation never reaches `remove_effect` and grants no companion.

Each docket's `available` trigger wraps its paid-receipt OR in a `custom_override_tooltip` with positive and negative text, so the focus view explains the paid-project condition whether it is met or unmet. Its completion reward changes only the package's two settlement ledgers. Former-host settlement, Danube access, depots, government routes, and durable sovereignty remain separate actions with their original costs and gates.

## Icons and localisation

No new art is required. Every group reuses these existing focus icon definitions from `interface/006_independence_wave.gfx`:

| Focus sprite ID | Texture |
| --- | --- |
| `GFX_goal_independence_wave_founding_administration` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_founding_administration.dds` |
| `GFX_goal_independence_wave_infrastructure_authority` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_infrastructure_authority.dds` |
| `GFX_goal_independence_wave_popular_councils` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_popular_councils.dds` |
| `GFX_goal_independence_wave_army_integration` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_army_integration.dds` |
| `GFX_goal_independence_wave_former_host_settlement` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_former_host_settlement.dds` |

The fifteen focus title, description, and reward tooltip keys, six paid-companion tooltip keys, and three paid-docket requirement/status pairs are in localisation/english/006_independence_wave_focus_l_english.yml, encoded as UTF-8 with BOM (57 keys total).

## AI, layout evidence, and future work

The new focuses have no custom `ai_will_do` blocks, so they inherit the engine's default focus score of 1. The read-only `chaosx_ai_probability_auditor` baseline `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_reg03_focus_ai_baseline_2026-09-25.md` found an incomplete candidate pool and unresolved typed campaign inputs. Its adapter also omits imported shared focuses. It does not establish route rankings or probabilities, so route-aware AI scoring remains unresolved and no numeric score was inferred from that audit.

The installed focus inspector reports direct `focus = {}` definitions and omits imported root-level shared definitions from both its counts and renders. The full-tree and carrier layout attachment therefore remain blocked at MCP; source coordinates do not replace the required in-engine layout evidence. The user performs live-game validation, and no live game was launched for this work.

Future work should first provide complete typed campaign fixtures and a probability adapter that includes imported shared focuses, then compare any proposed route-aware AI scoring on the same named scenarios as its baseline. Any further branch must keep the paid project boundary, package-specific ledger ownership, controlled anchor, mutually exclusive tradeoff, and existing tree carriers intact. New focus art is only warranted if later accepted design introduces a visual role that the five existing icons cannot represent.
