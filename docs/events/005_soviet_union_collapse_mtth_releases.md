# Event 005 MTTH Release Events

## Overview

The progressive release system turns the old flat threat-band roll into an MTTH-weighted SOV scheduler. Event `chaosx.nr5.129` remains a hidden Soviet-only delayed event, so the implementation does not add world-iteration on-actions. Every pass computes two MTTH values from `common/mtth/005_soviet_collapse_mtth.txt`: `soviet_collapse_progressive_release_weight` and `soviet_collapse_progressive_release_miss_weight`.

The release weight rises from Union Collapse Threat, weak Moscow Authority, weak Command Obedience, existing breakaways, regional cascades, depot vulnerability, foreign penetration, League cohesion, old-movement pressure, failed Soviet mission flags, Soviet war pressure, and chaos tier. The miss weight moves in the opposite direction: a strong center and low threat make another release less likely, while severe threat, cascades, and failed objectives shorten the gap between declarations.

## Event Flow

1. `chaosx.nr5.129` fires only for `SOV` while the collapse is active and terminal collapse has not started.
2. `soviet_collapse_maybe_release_threat_breakaway` checks the low-threat floor and the progressive-release cooldown.
3. At 100 threat, `soviet_collapse_show_union_unmade_super_event` resolves terminal collapse immediately.
4. Below terminal collapse, the effect stores the MTTH release and miss weights in temporary variables and rolls between them.
5. A successful roll calls `soviet_collapse_fire_progressive_release_event`, which selects one visible cause event.
6. The cause event releases one eligible republic through `soviet_collapse_release_one_threat_breakaway_republic`, applies the normal dynamic support package, loads the runtime focus tree for an event-created republic, and starts the cooldown.

## Cause Events

The visible release events describe the authority failure that pushed the republic into open declaration:

- `chaosx.nr5.130`: ministry refuses orders
- `chaosx.nr5.131`: rail office changes seal
- `chaosx.nr5.132`: border guards accept republican command
- `chaosx.nr5.133`: local party committee declares emergency sovereignty
- `chaosx.nr5.134`: foreign liaison accelerates declaration
- `chaosx.nr5.135`: depot commanders swear to local authority
- `chaosx.nr5.136`: old movement forces a republic to act first
- `chaosx.nr5.137`: League envoy coordinates declaration

## Tuning

Tuning lives in `constant:soviet_collapse_release_mtth` inside `common/script_constants/005_soviet_collapse_constants.txt`. The old progressive threat thresholds remain in `constant:soviet_collapse_progressive_release`, but the release and miss chances are now produced by MTTH entries instead of being selected by flat `if`/`else_if` bands.

Kazakhstan remains gated by `has_soviet_collapse_three_smaller_central_asian_republics_free = yes` inside the candidate selector, so progressive releases cannot make Kazakhstan the first Central Asian breakaway.

## Icon And Asset Surface

No new icons or images are required for this mechanic. The release events reuse `GFX_report_union_crisis`, which is already wired in `interface/005_soviet_collapse_events.gfx` and documented in the Event 005 asset manifests.

## Future Plans

The next deeper pass can persist the selected republic as an event target before showing the visible cause event, allowing the event text to name the exact republic that declared. Another useful extension would split MTTH entries by region so Baltic, Caucasus, Central Asian, western, and Moldovan cascades can each report their own pressure clocks in the Soviet crisis UI.
