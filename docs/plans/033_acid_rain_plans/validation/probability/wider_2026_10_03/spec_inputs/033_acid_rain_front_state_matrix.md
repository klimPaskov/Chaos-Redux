# Event 033 Acid Rain front and phase state matrix

## Global phase machine

| State | Entry trigger | Required entry work | Scheduled work | Allowed exits | Invalid-state response |
| --- | --- | --- | --- | --- | --- |
| Inactive | Campaign start or completed event | Event availability only | None | Formation | Clear stale nonhistorical runtime |
| Formation locked | Accepted Major or cluster dispatch | Set schema, build frozen registry, initialize countries, choose stage | None until transaction commits | Regional active, split opening, global warning | Roll back before history commit, fail closed after commit |
| Regional active | Baseline opening or post-migration front | Create front 1 and active footprint | 3-day exposure, 6-day drift, 7-day Air, front movement | Severe-capable regional, split warning, global warning, coverage wait | Rebuild missing derived values once, never reroll committed target |
| Severe-capable regional | Evolution I active | Enable severe evaluation | Regional pulses plus severe checks | Split warning, global warning, coverage wait | Skip invalid cell and retain front |
| Split warning | Evolution II transition starts | Freeze transition date, warn world, reserve distinct region | Existing front continues until safe split | Multiple-front active | Defer split until distinct valid region exists |
| Multiple-front active | Second front footprint valid | Apply split receipt and direct Chaos once | Independent front pulses, severe checks, third-front rolls | Global warning, coverage wait | Close only invalid slot, preserve valid fronts |
| Global warning | Evolution III transition starts | Freeze 3-day date, notify countries, block new regional warnings | Existing exposure until transition | Global layer active | Defer one pulse if an exposure transaction is open |
| Global layer active | Transition date | Close front slots, mark all eligible states active and touched | 3-day global exposure, superstorm checks, 7-day Air, 14-day dissipation after minimum | Dissipating | Bounded registry repair, guaranteed end remains |
| Coverage wait | All frozen states touched in regional phase | Store final coverage date | Existing fronts continue, scheduled dissipation checks | Dissipating, global warning | Restore missing final coverage date from receipt only |
| Dissipating | Successful check or controlled active disable | Block new weather, close cells, remove acute state | One transaction with resumable step | Recovery tail | Resume stored cleanup step |
| Recovery tail | Acute cleanup complete, aftermath or commitments remain | Show recovery category and retain history | State recovery and commitment completion | Closed | Rebuild country aftermath counts from tracked states once |
| Closed | No acute weather and no unresolved event-owned national work | Remove active category, retain permanent history | None | None | Idempotent cleanup only |
| Terminal cleanup | World-end or incompatible terminal transition | Stop weather and hand off retained consequences | Terminal owner controls further state | Closed or terminal-owned state | Never wait for coverage |

## Ordinary front slot state machine

| Front state | Entry | Stored facts | Pulse behavior | Exit |
| --- | --- | --- | --- | --- |
| Empty | Slot unused | Stable front ID only | None | Region entry |
| Region entry | New or moved front | Region, previous region, visit sequence, quota, dwell window, intensity | Build initial footprint | Active drift |
| Active drift | Footprint exists | Active and retired arrays, visit touched count | Exposure and six-day drift | Warning prepared, severe forecast, forced completion |
| Warning prepared | Seven days before move | Frozen next region and arrival window | Continue exposure and drift | Moving |
| Moving | Due date and departure conditions | Completed visit result | Close old footprint, select new anchor | Region entry |
| Severe forecast | Cell draw succeeds | Episode ID, target states, forecast and end dates | Parent front continues | Severe active or cancelled if target invalid |
| Severe active | Forecast matures | Cell intensity, opening receipt, cooldown plan | Severe opening and sustained pulses | Cooldown |
| Cooldown | Cell ends | Next eligible cell date | Parent front only | Active drift |
| Forced completion | Second visit or coverage correction | Compulsory untouched state set | Drift cannot leave until set cleared | Warning prepared |
| Closing | Split replacement, global transition, or dissipation | Cleanup step | Remove memberships and warning | Empty |

## State exposure transitions

| Prior state | Trigger | New state | Opening shock | Coverage change | Aftermath behavior |
| --- | --- | --- | --- | --- | --- |
| Never touched | Added to ordinary footprint | Ordinary active | On next exposure pulse | Touched count `+1` | None yet |
| Touched inactive for 6 or more days | Added to ordinary footprint | New ordinary episode | On next exposure pulse | None | Existing aftermath pauses or combines through modifier rule |
| Touched inactive for fewer than 6 days | Added to ordinary footprint | Same ordinary episode | None | None | Same episode continues |
| Ordinary active | Selected for severe forecast | Ordinary plus forecast | None until severe starts | None | None |
| Ordinary active | Severe starts | Severe active | Severe opening on next pulse | None | Severe history begins |
| Severe active | Severe ends, parent remains | Ordinary active | None | None | Severe contribution retained for final aftermath |
| Ordinary active | Parent front leaves | Inactive aftermath | None | None | Calculate or update aftermath tier |
| Any eligible state | Global transition | Global active | Global opening on next pulse | Mark touched if needed | Existing aftermath merges into acute state |
| Global active | Superstorm begins | Global superstorm | Superstorm opening on next pulse | None | Superstorm contribution retained |
| Any acute state | Dissipation | Aftermath or clear | None | None | Final tier computed and acute modifier removed |

## Transition invariants

- One ordinary state has at most one parent front.
- One state has at most one severe cell or superstorm episode at a time.
- Touched membership is permanent for the event.
- Region visit history is not a substitute for state coverage.
- Opening-shock receipts are keyed by episode ID.
- A front warning has one frozen destination.
- Front slot order remains stable across save and reload.
- Global transition closes ordinary slots before global sustained pulses begin.
- Dissipation blocks every new creation path before removing current modifiers.
