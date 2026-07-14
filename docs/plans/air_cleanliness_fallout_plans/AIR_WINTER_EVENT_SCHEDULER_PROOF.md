# Air Winter Event Scheduler Proof

## Implemented surface

`air_winter_schedule_phase_event` is defined in
`common/scripted_effects/air_cleanliness_winter_event_effects.txt`. The only
live call is inside `air_winter_update_state`, after the monthly state damage,
population, phase modifier, and disease work. The host already reaches that
state effect through its single unfiltered `every_state` pass. No country loop,
state loop, or on-action entry was added for winter events.

The scheduler records one country flag for each escalation phase. The first
qualifying state in the host's state iteration selects that country's phase event.
Later states cannot select another event for the same phase. The scheduler
checks the current phase on every monthly state pass, so a phase entry blocked
by the country cooldown remains eligible after the cooldown expires. A timed
46-day country cooldown is one day longer than the longest 45-day delayed
result. Recovery entries require a real phase decrease and use a persistent
country count limited by
`constant:air_winter_event_runtime.recovery_arc_cap`.

## Deterministic event selection

The selected event number is stored in the temporary variable
`air_winter_selected_event_id`. Every selectable number comes from the typed
`air_winter_event_id` script constant table. Presentation class, state
category, local shelter, and transition direction select the number through an
ordered `if` chain. No random effect, random list, MTTH roll, or unordered
country search is used.

An unclassified presentation state cannot select a phase or recovery event.
Every reviewed class has an explicit route, including the boreal and
equatorial phase-2 food route and the highland phase-1 route. The country phase
gate is written only after an event number has been selected. A missing route
therefore leaves the phase eligible for another classified state instead of
silently assigning a fallback event.

The event is fired with a `meta_effect` that injects the selected integer into
`chaosx.fallout.[AIR_WINTER_EVENT_ID]`. The installed vanilla
`effects_documentation.md` defines `meta_effect` for any scope and explicitly
lists `OWNER` as a supported target. Its example injects a country token and a
numeric value into executable effect text. Current vanilla also uses variable
localisation replacement inside `meta_effect` in
`common/scripted_effects/CZE_scripted_effects.txt` to select numbered ideas.
The winter scheduler follows that documented pattern with an event number.

## Event target lifetime

Before firing an event, the scheduler saves the calling state as the regular
event target `air_winter_event_state` and its owner as
`air_winter_event_country`. The offline Data structures page states that a
regular event target carries into events fired in the effect chain. Its own
example saves a state target and fires a country event ten days later. The same
page states that a child event inherits the target for the entire event chain.

This is the required basis for the delayed result blocks. Every delayed result
is scheduled from an event option while the regular state target is live. The
target therefore survives into that result without using a global event target
that another country could overwrite. The installed
`effects_documentation.md` also documents `country_event` delays in hours,
days, and months. Delay constants are copied into temporary variables before
the event `days` field. The timed country-flag surface is more restrictive, so
the scheduler uses the file-scoped literal
`@AIR_WINTER_EVENT_COUNTRY_COOLDOWN_DAYS`. Its value is mirrored by
`constant:air_winter_event_runtime.country_cooldown_days` and must be updated
with that tuning entry.

Every event validates both regular targets before it opens. The state must
still be valid and owned by the saved country. Delayed result blocks also
require one of their own pending branch flags. When an initial choice creates
a delayed branch, the state stores its original country in
`air_winter_pending_event_owner`. Monthly reconciliation cancels that branch
if the state changes owner or the branch ledger becomes incomplete. This keeps
a transferred state from receiving a result selected by its former owner.

The offline Data structures reference documents that a regular variable can
store a country database ID and can later be used as a target with the `var:`
prefix. Vanilla `events/NSB_Soviet.txt` uses the same ownership form in
`is_owned_by = var:SOV.SOV_nationalist_country`. The Air Winter state variable
uses `is_owned_by = var:air_winter_pending_event_owner` in the same way.

## AI and cleanup

Every player-choice block has explicit AI weights with state or country
modifiers. AI countries resolve the ordinary country events without a player
popup. Result blocks expose only the option that matches the stored chain flag
or deterministic state outcome.

`air_winter_event_clear_state_memory` cancels pending branches and clears
lasting state event memory during an explicit state reset. It does not clear
country memory because one state reset must not reopen events for every other
state owned by that country. `air_winter_event_clear_country_memory` clears
phase gates, the timed cooldown, and the recovery counter only when invoked in
country scope. `air_winter_reset_country` owns that country-scoped cleanup.
Completed delayed blocks clear their own pending flag and stored owner as soon
as the result resolves.

## Validation boundary

Static review proves the documented meta effect syntax, regular event target
lifetime, delayed event syntax, ownership guards, branch cancellation,
single-iterator call site, unique event IDs, and one-to-one localisation
coverage. A live game session has not yet proved the generated `country_event`
text or delayed target chain in this tranche.
The installed documentation also does not promise that `every_state` order is
numeric state-ID order. The scheduler only requires the iterator order to stay
stable for an unchanged database, which still needs a repeated runtime trace.
Those runtime proofs remain required before this event scheduler can be
treated as release-ready.
