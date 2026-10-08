# Event 006 package-incident appointment and shown-report lifecycle

The 65 package pairs retain 130 report events and 260 choices.
Each pair has an A appointment after the founding posture and a B appointment scheduled by either valid A answer.
Shared tuning remains 45 days for A and 150 days for B.
Every original picture, option, cost, reward and AI expression remains unchanged.
No new event ID, asset, country, portrait, decision category or periodic world hook is introduced.

Scheduling selects the existing package event ID, records the current origin generation and writes the due date once.
The appointment remains registered even while that slot's earlier report is shown.
Dispatch requires a known package and a registered current-generation appointment with a stored due date and no delivered, resolved or shown receipt.
Remaining game hours are the stored date difference multiplied by the shared date-unit scale and clamped to zero.
Meta construction injects the native numeric event ID and remaining hours.
Closing a previous report never restarts the original delay; an unknown package creates no appointment.

A and B have independent shown locks and normal-variable snapshots of shown generation and package.
Valid immediate delivery captures these before publishing delivered, and replacement delivery cannot overwrite a shown slot.
Every effect-time answer requires an active current origin, matching appointment generation, delivered/unresolved state and matching shown generation/package.
An old A answer cannot resolve new A or schedule new B; an old B answer cannot spend resources or reward a replacement origin.
Option visibility is evaluated when the popup opens, so click-time proof remains the authority.

Origin cleanup clears generation-local appointments and answers while preserving an outstanding shown slot and snapshots.
Only the corresponding native after handler releases that shown proof.
It closes independently of reply authority, then may wake an already-registered current appointment against its original due date.
Old B closure leaves current A untouched; resolved answers cannot redispatch.
The documented default thirteen-day timeout chooses the first option and follows normal after closure.
Current 45/150-day appointments constrain natural cross-generation overlap; no native exploit is claimed observed.

A due delayed callback for the same package may fulfill a currently authorized appointment after the slot becomes free.
It captures current shown proof at that delivery and does not carry an immutable historical scalar generation.
The enforced write lifetime protects the ordinary outstanding-popup lifecycle.
An arbitrarily forced replay of a closed handler after its slot is reused cannot be distinguished by these country scalars and is not claimed safe as a public API.
The close helpers are native after entries, not repeatable debug actions.

| API | Country-scope inputs and outputs | Defaults and side effects |
| --- | --- | --- |
| `independence_wave_schedule_package_incident_a/b` | Current active package/generation; A resolved for B | Registers a known package once and writes its original date. No rewards. |
| `independence_wave_package_incident_select_a/b_event` | Current package ID; caller-created temporary `independence_wave_package_incident_event_id` output | Caller initializes zero; unknown packages leave zero. Original 130 mappings only, with no country mutation. |
| `independence_wave_package_incident_queue_a/b_appointment` | Registered current appointment, stored date, free shown slot | Initializes selector output, computes hours and queues the authorized report. No new due date or reset. |
| `independence_wave_package_incident_capture_a/b_shown` | Event immediate with valid delivery proof | Captures normal generation/package and publishes shown/delivered once. |
| `can_resolve_independence_wave_package_incident_a/b` | Exact shown and current appointment proof | Pure boolean; rejects stale or resolved answers. |
| `independence_wave_package_incident_close_a/b_shown` | Sole native after entry for the shown slot | Releases only that slot and conditionally dispatches an existing appointment. No costs or rewards. |
| `independence_wave_clear_package_incident_runtime` | Origin reset/end | Clears live state while retaining outstanding popup proof. |

```text
independence_wave_schedule_package_incident_a = yes
immediate = { hidden_effect = { independence_wave_package_incident_capture_a_shown = yes } }
after = { independence_wave_package_incident_close_a_shown = yes }
```

Regression evidence retains all 130 mappings and byte-identical 260 option bodies.
Cases cover current/stale proof, duplicate delivery/closure before slot reuse, independent old-B/current-A slots, unknown packages and remaining-date dispatch.
Closure thirteen days into a replacement A appointment retains 32 days, and a valid A answer retains B's 150-day delay.
The model declares active-origin facts and a documented date converter; it does not execute native popup timing, economy or arbitrary event-instance replay.
The independent architect handoff and MCP coverage limits remain in the October 8 source review.

Existing report pictures and option labels are retained in the event file with their existing sprite/DDS consumers.
Entry event, event log, evolutions, scenario and catalog strings are unchanged by this lifecycle repair.
Future validation should settle native timeout/after order and delivery through origin transitions before changing timing.
Extensions must preserve exact appointments, shown lifetimes, original country content and ownership-limited cleanup.
