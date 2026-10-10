# Event 34 Industrial Boom decision map

Rules, costs and effects for each row are owned by [part 3](034_industrial_boom_spec_part_3_decisions_missions.md); evolution rows by [part 5](034_industrial_boom_spec_part_5_evolutions.md).
This map shows only when each row is visible.

## Visibility by state and band

"Opening" is the first lifecycle state; the band columns apply to the Running state; "Landing" is while Prepare a Controlled Landing is active.

| Row | Opening | Sustainable | Strained | Dangerous | Critical | Landing |
| --- | --- | --- | --- | --- | --- | --- |
| Run the Economy Hot | Yes | Yes | Yes, costlier | Shown locked | Hidden | Hidden |
| Stabilize Supply Chains | Yes | Yes | Yes | Emergency strength | Emergency strength | Yes |
| Build an Industrial Reserve | When none held | When none held | When none held | Hidden | Hidden | Hidden |
| Cool the Expansion | Only if started at 40 or more | Yes | Yes | Yes | Yes | Hidden |
| Designate an Industrial Project (per region) | Yes | Yes | Yes | Hidden | Hidden | Hidden |
| Protect an Industrial Region (per region) | Yes | Yes | Yes | Yes | Yes | Yes |
| Abandon a Project (per region) | Hidden | When threatened | When threatened | Yes | Yes | Yes |
| Prepare a Controlled Landing (start) | Hidden | Yes | Yes | Hidden | Hidden | Active mission |
| Prevent the Crash | Hidden | Hidden | Hidden | Hidden | Active mission | Hidden |
| Emergency Production Halt | Hidden | Hidden | Hidden | Yes | Yes | Hidden |
| Approve a Speculative Expansion (Evolution I) | Offer | Offer | Offer | Hidden | Hidden | Hidden |
| Declare a Miracle Region (Evolution II, per region) | Yes | Yes | Yes | Hidden | Hidden | Hidden |
| Contain the Spread (Evolution III) | Yes | Yes | Yes | Yes | Yes | Yes |

Each region shows only one of its rows at a time, in the priority given in part 3.

## Typical routes

```text
Balanced baseline
  Opening -> designate one project -> reserve -> optional hot window in Sustainable
  -> stabilize in Strained -> project Secured -> start landing below 70
  -> controlled landing below 40

Wartime exploitation
  Opening during war -> run hot -> Factory Conversion project
  -> stabilize as pressure rises -> stop pushing before Dangerous
  -> controlled landing, or rough landing when the war timetable matters more

Late emergency
  Dangerous -> cool and stabilize -> abandon weak projects
  -> Critical: Prevent the Crash
     -> success: back to Running, no hot running for 90 days
     -> failure: crash into Event 35
  -> or Emergency Production Halt
     -> succeeds with a held reserve, or below 90 with a protected region
     -> otherwise crash into Event 35
```

## Failure ownership

| Failure | Immediate result | Owner afterwards |
| --- | --- | --- |
| Landing mission cancelled | Back to Running, 60-day cooldown | Event 34 |
| Project lost or abandoned | Progress lost, unfinished works | Event 34 until landing or crash |
| Prevent the Crash fails | Frozen snapshot, landing state failed | Event 35 |
| Emergency Production Halt fails | Frozen snapshot, landing state failed | Event 35 |
| Region occupied | Project paused, shock | Event 34, then Event 35 if a crash follows |
