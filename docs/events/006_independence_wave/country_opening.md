# Event 006 country opening

## Purpose

Every country released by a committed Event 006 wave receives a tailored first-government event after the public wave report is acknowledged.
The human player chooses an early governing posture, while AI countries resolve the same posture deterministically.
The opening establishes the country-specific government, territory, force origin, former-host condition, regional context, and most urgent public problem before its longer founding and survival routes continue.

## Delivery sequence

1. Hidden entry `chaosx.nr6.1` publishes only a committed standalone or joint Event 006 result.
2. Before firing the public `chaosx.nr6.2` report, the root captures the exact committed Event 006-owned country rows and a generation/package receipt for each valid actor.
3. The `.2` report sets a global pending receipt that holds planner reset and blocks another report until its single option is taken or the option times out. `timeout_days` uses the file-scoped 13-day report timeout, and the engine selects its first option automatically when the timeout expires.
4. The `.2` option dispatches the frozen cohort once and schedules hidden `chaosx.nr6.42` after `constant:independence_wave_opening_timing.post_report_dispatch_days`.
5. The hidden router validates the actor's current origin, package, generation, anchor, former host, force profile/level, and five Statehood values.
6. AI countries resolve a civilian or security posture deterministically; a human country receives `chaosx.nr6.41` with those two choices.
7. After either posture resolves, IW-043 and IW-058 schedule their existing package introductions with generation receipts and the centralized `package_followup_days` delay.

The report queue contains at most ten selected Event 006 actors, fails closed when any required cohort data is missing, and quarantines overlapping `.2` callbacks because a country event option does not carry a plan-instance ID.
It excludes Event 005-owned rows, Join conversions, failed setups, and rolled-back releases.
No world-country iteration, on-action, global event target, package grant, state transfer, or Event 005 mutation is part of this family.

## Country-specific text

The opening uses the released country's ruling party, stored anchor state, package region, force profile, former-host pointer, host outcome, and live Statehood values.
The region selector names one of the 14 accepted regions and adds a concise geographic concern for its districts.
The force-profile selectors name both the brigade template and a separate recruitment source derived from the approved Event 006 military archetype, including local defense units, industrial guards, inherited host formations, frontier detachments, coastal units, mobile forces, river/forest units, or foreign volunteers.
The former-host sentence names a surviving host and its current condition, or uses a neutral no-longer-governs sentence when the host has been eliminated.
The urgent-problem selector prioritizes severe host pressure, founding instability, low Security, low Capacity, low Recognition, and low Legitimacy before a general administrative issue.
Missing required actor data fails closed instead of displaying a generic replacement.

## Posture effects

Civilian administration raises Legitimacy, Recognition, and Capacity by the existing minor or standard delta according to their current bands.
It reduces founding Instability by the existing minor, standard, or major loss delta according to the live band, raises Event 006 network standing by the existing recognition gain, and gives up Security by a minor loss or a standard loss during war, severe host threat, or a fragile/viable starting force tier.
If the former host survives, it also reduces the country's bilateral claims, hostility, obligations, domestic pressure, and fear of reconquest by the existing minor value loss and advances border settlement by the existing minor value gain.

Frontier security raises Security from a minor to decisive existing delta according to force tier and current Security, with an additional profile path for security-oriented formations.
It reduces Legitimacy and Capacity by the existing minor loss and reduces network standing by the existing minor loss.
Instability rises by a standard gain only during war or a severe living-host threat.
Against a surviving former host, bilateral hostility and domestic pressure rise by a minor gain while fear of reconquest falls by a minor loss.

Both postures call the shared five-value, host-relation, and network-standing mutation helpers, which clamp values and refresh Statehood phases, lifecycles, and display state.
They grant no political power, equipment, territory, claims, divisions, paid receipts, or automatic government route.
AI uses no weighted option pool and receives exactly the same effect branches as a human choosing the corresponding posture.

## Integration and asset wiring

The `.2` report actor mapping continues to use the existing Event 006 event ID and `independence_wave_latest_actor` mapping.
The shared Event Details entry explains the first civilian-administration versus frontier-security choice, and `Events!C7` in the catalog workbook carries matching wording.
The Event Details body uses its existing scroll pane; GUI inspection reported a nonblocking overlap, and the production render for the updated description did not return, so text wrapping and overflow remain unverified.

| Asset | Runtime path | Sprite registration | Consumer |
| --- | --- | --- | --- |
| Shared country-opening report image | `gfx/event_pictures/006_independence_wave/report_event_006_country_opening.dds` | `GFX_report_event_006_country_opening` in `interface/006_independence_wave_small_assets.gfx` | `chaosx.nr6.41` across all 14 regions |

No new focus, decision, scripted-GUI, button, achievement, flag, portrait, or 3D model icon is introduced by this family.

## Future work and suggestions

The accepted Part 2 plan also calls for tiered former-host responses, interest-gated foreign reactions, and recurring statehood incidents; those are separate pending families and must retain the post-report order.
The broader Event 006 task still has package-admission, focus, formable, AI, asset, and MCP lifecycle gaps recorded in the source-of-truth map.
Future report-image variants should be added only when an accepted asset plan needs a distinct regional or milestone scene, since the current neutral image intentionally serves every region.
The bounded Event MCP routes returned partial helper/lifecycle coverage and the baseline graph comparison was not available; a supported same-revision comparison and live user validation remain open evidence tasks.
