# Event 005 MTTH Release Events

## Overview

The progressive release system turns the old flat threat-band roll into an MTTH-weighted SOV scheduler. Event `chaosx.nr5.129` remains a hidden Soviet-only delayed event, so the implementation does not add world-iteration on-actions. Objective-board refreshes and regional-league defensive-war effects apply pressure but do not roll immediate extra releases. Every scheduler pass computes two MTTH values from `common/mtth/005_soviet_collapse_mtth.txt`: `soviet_collapse_progressive_release_weight` and `soviet_collapse_progressive_release_miss_weight`.

The release weight rises from Union Collapse Threat, weak Moscow Authority, weak Command Obedience, gated breakaway cascades, gated regional cascades, depot vulnerability, foreign penetration, League cohesion, old-movement pressure, failed Soviet mission flags, Soviet war pressure, and chaos tier. The miss weight moves in the opposite direction: a strong center and low threat make another release less likely, while severe threat, cascades, and failed objectives shorten the gap between declarations.

The balance pass keeps the 0-100 scale but makes the release curve sharper and safer. Calm strong-center games get `release_base = 0`, a high miss path, tighter opening-lock component caps, stronger high-authority/high-obedience suppression, a `can_soviet_collapse_roll_progressive_release` gate, and a candidate-count guard before the scheduler rolls. Breakaway and regional cascade weights require moderate threat, at least five breakaways, weak center signals, war pressure, or capital-loss pressure before they contribute. Release-level component pressure uses dedicated `constant:soviet_collapse_release_gate` thresholds rather than the lower focus-AI pressure gates, while strong-center suppression tapers at severe threat so the center cannot indefinitely suppress real collapse conditions. Distributed pressure can still roll when high total threat combines with critical Moscow Authority or critical Command Obedience.

## Event Flow

1. `chaosx.nr5.129` fires only for `SOV` while the collapse is active and terminal collapse has not started.
2. `soviet_collapse_maybe_release_threat_breakaway` checks `can_soviet_collapse_roll_progressive_release`, which includes cooldown, terminal-state block, and a real collapse signal beyond the opening wave.
3. At 100 threat, `soviet_collapse_show_union_unmade_super_event` resolves terminal collapse only after the terminal pacing gates are mature.
4. Below terminal collapse, the effect counts eligible candidates before rolling. If the pool is empty, it clears the sustained-pressure accumulator and does not start the cooldown.
5. If candidates exist, sustained unresolved pressure adds to the release weight up to the configured cap and slightly reduces the miss path after the first pressure month. The accumulator grows from a small base plus urgency score, candidate count, regional cascade score, threat band, weak center signals, and failed strategic objectives. Progressive selection uses `global.soviet_collapse_progressive_release_selection` as a scratch array, leaving first-wave memory intact for later candidate exclusion.
6. A successful roll calls `soviet_collapse_fire_progressive_release_event`, which saves one release target as `event_target:soviet_collapse_release_target` before selecting a visible cause event. If a regional cascade is active, target selection first checks the matching family: western, Baltic, Caucasus, Central Asian, Kazakhstan after the southern gate, then internal republics. If that active-family pool is empty, the generic candidate pool is still used.
7. The cause event releases that selected republic through `soviet_collapse_release_one_threat_breakaway_republic`, applies the normal dynamic support package, loads the runtime focus tree for an event-created republic, and starts the cooldown only after a candidate was actually selected.
8. Progressive candidates now cover western and eastern European republics, Baltic republics, Caucasus republics, Central Asian republics, Kazakhstan after southern cascade pressure, and vanilla-supported internal republics. Internal republics enter the progressive selector only after moderate threat, at least five breakaways, or higher chaos.

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

Tuning lives in `constant:soviet_collapse_release_mtth` inside `common/script_constants/005_soviet_collapse_constants.txt`. Progressive threat thresholds live in `constant:soviet_collapse_progressive_release` at 35/50/65/80/92 for low, moderate, high, severe, and critical pressure. Release and miss chances are produced by MTTH entries instead of flat `if`/`else_if` bands.

The current tuning anchors are:

| Pressure state | Intended pacing |
| --- | --- |
| Low threat with high Moscow Authority and high Command Obedience | Very low monthly release chance; the first calm month should normally miss. |
| Moderate threat with one or more breakaways | Occasional additional declarations, especially when regional cascade or failed mission flags exist. |
| High threat with weak authority or weak obedience | Release chance becomes competitive with the miss path and should create visible map changes over repeated scheduler passes. |
| Severe or critical threat with cascades, failed missions, or war pressure | Release chance should dominate unless the candidate pool is exhausted or terminal collapse has already started. |

Release-level component gates are separate from focus AI thresholds: Republic Momentum 50, severe Republic Momentum 65, depot vulnerability 50, Foreign Penetration 45, League Cohesion 45, and old-movement pressure 35.

Kazakhstan remains gated by southern cascade pressure inside the candidate selector. When a southern cascade exists, the selector tries remaining smaller Central Asian republics before Kazakhstan, then allows Kazakhstan if the smaller southern pool is already empty or unavailable. High chaos can still make Kazakhstan eligible through the generic pool, but not as a calm first southern release.

The sustained-pressure accumulator is `soviet_collapse_progressive_release_pressure`. It adds `constant:soviet_collapse_release_mtth.sustained_pressure_monthly_add` plus dynamic pressure from `urgency_pressure_per_score`, `candidate_pressure_per_candidate`, `regional_cascade_pressure_per_score`, threat-band adders, weak-center adders, and failed-objective adders. The gain is capped by `sustained_pressure_monthly_gain_cap`, the total accumulator is capped by `sustained_pressure_cap`, and the value resets after a real release or an empty candidate pool. Current tuning starts at 4 per eligible monthly pass, caps monthly gain at 32, caps stored pressure at 72, opens the accumulated-pressure roll gate at 16, and applies the 0.85 miss-weight factor once stored pressure reaches 12. This prevents empty-pool cooldowns while still making repeated unresolved pressure visible.

The Soviet crisis category includes a non-clickable Republic Release Risk Ledger in `common/decisions/005_soviet_collapse_release_visibility_decisions.txt`. It exposes `soviet_collapse_release_urgency_score`, `soviet_collapse_progressive_release_candidate_count`, and `soviet_collapse_progressive_release_pressure` before a release event fires. Candidate count is stored as a normal variable so the ledger can show the latest monthly candidate pool instead of losing the value after the scheduler chain ends.

Resolved Moscow-federated subjects are excluded from the progressive candidate trigger through `soviet_collapse_moscow_federated_subject`, so republics settled through the Moscow federal compact do not consume later MTTH releases.

## Family Audit

The detailed family-by-family audit is in `docs/events/005_soviet_collapse_mtth_family_audit.md`.

| Family | Source-level result |
| --- | --- |
| Western and eastern European republics | `UKR`, `BLR`, and `MOL` are progressive MTTH candidates and route through breakaway setup plus runtime focus loading. |
| Baltic republics | `LIT`, `LAT`, and `EST` are progressive MTTH candidates and can later form or join the Baltic local league where quorum exists. |
| Caucasus republics | `GEO`, `ARM`, and `AZR` are progressive MTTH candidates and can later form or join the Caucasus local league where quorum exists. |
| Central Asian republics | `UZB`, `KYR`, `TAJ`, and `TMS` are progressive MTTH candidates and use the Central Asian runtime focus tree. |
| Kazakhstan | `KAZ` is a progressive MTTH candidate after the southern cascade gate, with smaller Central Asian candidates checked first during active southern cascades. |
| Internal republics | `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, and `TAN` are progressive MTTH candidates after moderate threat, existing breakaway pressure, or higher chaos, and they load the internal republic tree. |
| North Caucasus or Mountain Republic | `MRC` is covered by the implementation-defined Mountain Republic high-chaos spawn path rather than a normal vanilla release. |

## Icon And Asset Surface

No new icons or images are required for this mechanic. The release events reuse `GFX_report_union_crisis`, which is already wired in `interface/005_soviet_collapse_events.gfx` and documented in the Event 005 asset manifests.

## Future Plans

A useful extension would split MTTH entries by region so Baltic, Caucasus, Central Asian, western, and Moldovan cascades can each report their own pressure clocks in the Soviet crisis UI.
