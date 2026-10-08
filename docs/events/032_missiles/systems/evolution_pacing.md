# Missile evolution pacing

Event 032 uses five independent native MTTH clocks and one finite observation receiver.
The first high-chaos firing has a separate short-delay exception.
Neither clock mode schedules a recurring programme-registry watch.

## Observation model

Part 4 places a bounded evolution pulse before eligibility and timing, and permits firing, chaos changes, finite jobs and exact mutation boundaries.
The implementation observes pressure at those boundaries rather than claiming continuous knowledge of every native country change.
Programme transactions call `missiles_notify_evolution_change`, which coalesces simultaneous notifications into one `chaosx.nr32.192` delivery after one hour.
The receiver has no self-scheduling successor.
Numeric programme notifications compare stage, reserve, readiness, control and network values against their previous notification receipt; unchanged clamp or network refreshes create no work.
State-status, explicit evolution-setting, war, peace, control, release, annexation and chaos-threshold boundaries provide their own notifications.
The chaos-band comparison distinguishes 899 from 900 even though both are inside the same named tier.

Shared payload owners notify only after settled stock transactions.
Chemical debit and conversion completion notify their country; an accepted profile change also schedules one `.193` observation after its known conversion duration plus one day.
Event 23 notifies completed opening, production, evolution credit, commitment and custody transfers without changing its ledger or stock arithmetic.
Nuclear custody returns retain the actual debited donor in a private temporary array through the holder overwrite, then notify that country and SOV after settlement.
Biological custody capture, recapture, recovery and proven accident loss notify the affected country; native raid bridges notify after their existing outcome resolver, including rejected release after native equipment collection.
These subscriptions do not grant, refund or deliver a payload and do not reconstruct native production or cancellation callbacks that the engine does not expose.

Native stability drift, research completion and equipment production have no universal callback in the consulted installed documentation.
They can therefore remain unobserved until the next permitted pulse.
An eligibility lapse and recovery between observations is not reconstructed, and a final validation cannot retroactively correct earlier waiting time.
This is the spec's finite-pulse observation model, not a claim of continuously current pressure or a bounded detection delay for every native change.

`missiles_measure_evolution_pressure` publishes normal global values only after a complete observation.
It counts live managed programmes, operational programmes, mature programmes, response-capable programmes, available missile reserve, wars, vulnerability, readiness strain, overstock, maintenance neglect and qualifying payload owners.
Native technology is normalized without granting another technology step.
The chemical owner check uses current shared CBRN technology/profile/real-stock checks or a paid preparation receipt; a profile token alone is not sufficient.
Observation date and generation identify the published snapshot.
Empty denominators produce zero shares through explicit guards rather than an undocumented regular-division fallback parameter.

Operational countries are frozen into a local pool before relationship counting.
Each unordered pair is counted once by country ID.
War is direct hostility; outside war, an actual war goal or active justification in either direction supplies a concrete strategic-threat signal, excluding alliance and subject ties.
Mere negative opinion or global tension alone does not invent a hostile dyad.
The detailed Automatic Retaliation conditions in part 4 require two operational programmes, one hostile pair and one response-capable country separately; the responder can be a third country.
Operational stage, complete-line maturity and response capability are not interchangeable counts.

## Ordinary native clocks

| Track | Event | Base day scale | Few-usable programme count |
| --- | --- | ---: | --- |
| Rogue Launch Commands | `chaosx.nr32.201` | 120 | Vulnerable programmes |
| Unreliable Guidance | `chaosx.nr32.202` | 105 | Operational programmes |
| Saturation Arsenals | `chaosx.nr32.203` | 90 | Operational programmes |
| Special Warheads | `chaosx.nr32.204` | 120 | Qualifying payload owners |
| Automatic Retaliation | `chaosx.nr32.205` | 150 | Response-capable programmes |

`common/mtth/032_missiles_evolution_mtth.txt` evaluates the shared base constants, the 1.5 few-usable factor, the 0.5 corresponding-pressure factor and the 0.8 World Collapse tier factor.
The resulting normal global day scales feed one-day native `mean_time_to_happen` bases.
The event engine supplies the stochastic clock; no uniform-delay draw stands in for MTTH.
The consulted offline event reference describes an initial trigger-check cadence of 20 days and daily MTTH checks while eligible, so native activation latency is distinct from the quoted MTTH scale.
Probability evidence must use the verified game-version adapter rather than assume that a source formula or test model proves engine timing.

Recurring native triggers read only host identity, complete observation state, pending mode, enabled/recorded/terminal flags and cached prerequisites.
They contain no country or programme-registry iteration.
Before an attempted unlock records anything, a fresh observation checks the actual prerequisites.
A stale-positive attempt is disarmed and waits for an authorized future observation; it does not start a polling retry loop.
Successful unlock flags and the fresh recorder acknowledgement enforce once-only logging.
The attempt events deliberately do not use `fire_only_once`, because a rejected attempt must not permanently consume the track's sole event firing.

## First-high-chaos short mode

Only tracks eligible at the first observation receive the finite `21 + 14 * eligible-index` day exception, in Rogue, Guidance, Saturation, Special and Automatic order.
`chaosx.nr32.190` owns these short receipts.
Ordinary native mode and short mode use separate flags, and a native clock has no due date.
Malformed or obsolete combinations are repaired only at an authorized observation.
The queue retains the earliest short date and host, and duplicate or early deliveries cannot consume another receipt.
After a successful overdue short commitment, the next eligible overdue commitment is spaced by seven days.
Only remaining short receipts can queue another `.190`; a cancelled or exhausted set stops.
Retired `.191` deliveries clear their obsolete metadata without observing, unlocking or scheduling another watch.

## Ownership, toggles and cleanup

One living registered country hosts the world clocks without becoming their actor in Event Logs.
Host replacement preserves valid pending work, invalidates observation readiness and requires a fresh permitted observation.
The completed observation reconciles existing short dates as well as newly armed ones, so a replacement host receives the earliest preserved delivery even when every pending track is already well formed.
Only exclusive short-mode receipts can contribute to that deadline; stale dates attached to native-mode rows cannot advance it.
An obsolete host delivery cannot clear a new host's queued observation.
When no programme survives, no host is invented and no recurring recovery scan is created.

Disabling a track clears its native/short pending state and prevents recording.
The shared evolution-setting transaction calls the Event 032 setting adapter only for the matching event/type, refreshing country adoption once and permitting a fresh observation when appropriate.
Previously recorded unlock history is not deleted or recorded again on re-enable.
Terminal cleanup clears Event 032's clocks only; it does not set `world_end`, start a terminal outcome or take ownership from Event 23, Event 76 or another world-end owner.
All 15 canonical terminal writes found in the reviewed runtime source invoke this cancellation beside their existing terminal subscriptions.
Already queued native events are not removed from the engine queue; their invalidated receipts make later deliveries inert.

## Files, APIs and presentation

The operation effects retain measurement, arming, recording, host and finite-job ownership.
`032_missiles_evolution_effects.txt` owns notifications, observation application, native attempts, threshold filtering and terminal clock cancellation.
`032_missiles_evolution_triggers.txt` owns recurring host gates, selected-track validity and mode integrity.
`032_missiles_evolution_events.txt` owns the five native clocks, the finite observation receiver and the one-shot payload-profile completion receiver.
The existing `.8` country receiver retains adoption, AI-profile and status-idea refresh.

External owners call `missiles_notify_evolution_change` after a settled mutation; they do not call the world measurement inside a shared payload action context.
The helper is any-scope, takes no payload, returns no acknowledgement and defaults to no scheduled work before programme initialization or after every enabled track is already recorded.
Its side effects are limited to host selection and one coalesced observation receipt.
`missiles_note_chaos_threshold_change` takes the already-updated shared meter/tier and notifies only when the threshold band changes.
The setting adapter is an explicit user-setting boundary, not a periodic observer.

These hidden clocks add no picture, icon, GUI, technology, unit, equipment or CXT content package.
Existing Event 032 evolution logs, static assets and programme controls remain their presentation consumers.

## Validation and follow-up

The actual-source native-evolution suite covers count publication, temporary lifetime, pair counting, mode integrity, finite dates, queue coalescing, duplicates, disabled/terminal state, host replacement and the actual MTTH entries.
Its native/world facts, shared logger call boundary and country-adoption event boundary are explicit limitations, not engine execution.
The original uniform-deadline helper is unsupported by the probability adapter, and the parent preserves that baseline limitation rather than manufacturing a native-before comparison.
Final probability, event graph, hook coverage and runtime evidence remain separate acceptance gates.
Future integration can add exact owner notifications where supported; it must not replace missing native callbacks with a recurring global or rolling-country watcher.
