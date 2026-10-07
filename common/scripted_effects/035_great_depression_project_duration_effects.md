# Event 035 project work and native mission deadlines

These event-owned helpers use day counts from `global.num_days` and preserve the event's sole player-managed Severity value.
They add no scheduler, world iteration, event registration, payment, Chaos or general dynamic router.

## Quote

`great_depression_quote_center_project_duration` runs in a currently registered STATE with the paying crisis country as ROOT.
Every caller initializes temporary `great_depression_duration_quote_days = 0` and supplies `great_depression_duration_quote_type` plus `great_depression_duration_preview_delta`.
Accepted authorization supplies preview delta zero, while a state-action tooltip supplies its mapped immediate Severity change.
The helper modifies only temporary arithmetic and the caller-owned quote output.
It returns zero when registration, authority, active episode or project-type proof fails.
The quote output must be preinitialized by each caller that consumes it after return.

Structural work uses the existing central 133-day anchor and the following read-only components from `great_depression_project_duration`.

| Component | Current calculation |
| --- | --- |
| Building damage | Infrastructure, civilian-factory and military-factory damaged levels, each bounded before addition, aggregate at most six, seven days per level |
| Severity | Post-action Severity above 40, at most 60 points, half a day per point |
| Infrastructure | Four days per missing level below the reference level five |
| War | Fourteen days when the paying country is at war |
| Earlier failures | Seven days per failed project, at most three contributions without changing history |

The total is rounded after arithmetic and bounded between 133 and 245 days.
Protection quotes its separate 42-day interval.
Authorization freezes the quote as `great_depression_center_project_required_work_days` and sets certification to `max(required work - 42, 0)`.
Later condition changes cannot resize the accepted work.

Example, STATE below its funding country:

```text
set_temp_variable = { great_depression_duration_quote_type = constant:great_depression_center_project.public_works }
set_temp_variable = { great_depression_duration_preview_delta = constant:great_depression_api.zero }
set_temp_variable = { great_depression_duration_quote_days = constant:great_depression_api.zero }
great_depression_quote_center_project_duration = yes
set_variable = { great_depression_center_project_required_work_days = great_depression_duration_quote_days }
```

## Forecast and native objective

`great_depression_prepare_center_duration_tooltip` runs in COUNTRY targeted-decision context with FROM as the exact state.
It owns temporary quote storage, forwards the caller's type and preview change, and writes only the existing country tooltip cache when the quote is positive.
It never changes accepted state work or spends resources.

`great_depression_process_center_mission` runs only from the existing valid-recipient maintenance path and accepted project authorization.
It preserves the existing main-objective gate, cancels invalid site authority without failure, activates the native mission explicitly and captures state/episode immediately.
The waiting mission has the ordinary 135-day deadline and supplies no historical completion proof.

`great_depression_sync_center_project_mission` runs in the mission-owning COUNTRY.
It enters the exact stored site, validates coherent structural work and current authorization, and binds the positive authorization once.
Protection supplies neither a bound reopening context nor a shortened reopening deadline.
The bound absolute deadline is state due day plus the central seven-day grace interval.
The signed native adjustment is `deadline - global.num_days - days_mission_timeout@mission`, applied through `add_days_mission_timeout`.
It is idempotent across replay and preserves accepted pause extensions.
An expired exact contract resolves through the guarded timeout, not a restarted minimum timer.

Success requires current site authority, episode, bound authorization, its exact completed authorization, coherent work and a deadline that has not expired.
Timeout requires current context, saved expiry and neither terminal outcome flag.
Both callbacks consume their four identity fields after one resolution.
Cancellation and all-mission cleanup remove those fields without granting success or failure to another context.

## Transfer

Adoption requires coherent active work before reserving a successor slot.
Returning states reuse their exact array row even at capacity, and the bounded lookup restores the row index before stage/project mirrors are written.
No extra array, capacity, duplicated row or new work quote is created.
An exact open transfer to a foreign owner preserves accepted local work through source retirement.
Historical, closed, owned-again or wrong-source-episode records do not qualify for that preservation exception.

## Evidence boundary

The source suite executes the production quotes, actions, project processing, mission helpers and guarded callbacks with declared native primitives.
Those fixtures do not establish native scheduling, UI, scope-pointer serialization or save execution.
The mandatory event and probability evidence retains its own completeness and unresolved-input limits in the Event 035 handoffs.
