# Event 025 acceptance scenario matrix

This matrix is the implementation-side test plan for docs/specs/025_alien_technology_in_antarctica_specs/specs/014_acceptance_criteria.md. It records deterministic source checks and the current evidence limit; it does not claim live-game validation.

| ID | Scenario | Expected invariant | Current evidence |
| --- | --- | --- | --- |
| 01 | Human maritime major wins baseline | Entry, route, phase actions, final recovery, one winner, owner API reward | Source path present; live runtime pending. |
| 02 | Human landlocked minor enters through chartered route | Human offer is unconditional and expensive route remains valid | Entry trigger and gateway actions present; live runtime pending. |
| 03 | AI major fails reserve floors | AI candidate remains out when reserves fail | AI candidate and reserve triggers present; probability audit pending. |
| 04 | All evolutions disabled | Baseline race still resolves | Evolution gates are separate from baseline; live runtime pending. |
| 05 | Each evolution enters during an active phase | Five independent Chaos and MTTH gates enter without resetting baseline | Evolution opening events and MTTH source present; probability audit pending. |
| 06 | Each evolution changes its opening | Evolved opening/report/log milestone exists for each evolution | Five opening event blocks and milestone effects present; completion audit pending. |
| 07 | Rival sabotage hidden/suspected/attributed | Privacy, evidence, cooldown, countermeasure, partial outcome, cleanup | Source guards and GUI privacy flags present; live runtime pending. |
| 08 | Outpost loss and restoration | Outpost state can degrade and be restored with valid costs | Runtime and mission helpers present; live runtime pending. |
| 09 | Same-day final tie | Deterministic survey, readiness, outpost, exposure, date, entry-order arbitration | Comparator source present; probability/event evidence pending. |
| 10 | No-participant closure | Entry controller closes without dangling active race | Event 025.299 and cleanup paths present; live runtime pending. |
| 11 | All active participants fail | Race closes safely without granting a false winner | Failure/analysis paths present; live runtime pending. |
| 12 | Winner owns no Event 016 technology | Missing base operational family is selected first | Event016 external API call through ledger; technology MCP timed out. |
| 13 | Winner owns every base family | Compatible upgrade pool is selected | Event016 API fallback present; technology MCP timed out. |
| 14 | Winner owns the full external pool | Alien Systems Integration capstone or documented reinforcement applies | Event016 API fallback present; technology MCP timed out. |
| 15 | Event 025 first, Event 036 later overlap | Exact aircraft/propulsion overlap converts later reward | Shared country ledger resolvers present; live runtime pending. |
| 16 | Event 036 first, Event 025 later overlap | Event025 requests different valid owner-API result | Shared ledger and source Event036 bridge present; live runtime pending. |
| 17 | Winner transfer and destruction aftermath | Evolution V custody paths are non-terminal and recoverable | Decision routes and runtime effects present; completion audit pending. |
| 18 | Evolution V contain and integrate timed routes | Dependence changes, accidents/recovery remain possible | Dependence routes and pulse present; live runtime pending. |
| 19 | Participant annexation and selected-target cleanup | Invalid participant/target state is cleared without dangling pointer | Cleanup helpers present; live runtime pending. |
| 20 | Save and reload through each major phase | Phase, mission, values, fragment owners, winner, aftermath persist | Persistent variables and targets are source-backed; save inspection not available. |
| 21 | Two human participants and observer | Only each participant sees its own board and private state | Scripted GUI visibility and opt-in rival flags present; live runtime pending. |
| 22 | Supported UI resolutions and terminal states | Board, map, tray, confirmation, winner, loser, disabled animation render without clipping | Source repair and decoded asset evidence present; targeted GUI MCP inspect timed out. |

## Static checks

The Event 025 GFX inventory resolves 130 texture paths.

The complete Event 025 DDS inventory contains 136 files across reports/news, board, achievements, super-event, decision art, and ideas.

The sector hitbox package and runtime mirrors are both 384x58 with four 96x58 frames and identical SHA-256.

The Event 025 source contains only participant-scoped recurring pulse events; no Event025 on_daily, on_weekly, or on_monthly whole-world scan was added.

The Event 025 reward path calls chaosx_grant_external_alien_recovery_reward and does not define a duplicate custom technology implementation.

## Evidence limits

Live GUI inspect/render/compare evidence is unavailable because the targeted hoi4.gui_inspect request timed out after 180 seconds.

Targeted technology inspection for the affected Event 016 technology families timed out after 180 seconds.

Baseline and post-patch weighted probability evidence must be attached from the isolated probability auditor before the event can be claimed complete.

The user performs live HOI4 validation; the agent does not launch the game under the repository rules.
