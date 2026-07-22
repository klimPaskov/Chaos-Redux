# Fallout The Bad Batch chain proof

Status: implemented as a dormant reviewed-candidate tranche. It is not
countable toward the 660 block release floor and it does not set a scheduler
activation flag.

## Ownership and identity

- Namespace: `chaosx.fallout`
- Event suffixes: `204` through `216`
- Candidate id: `204`
- Transaction key: `710008`
- Candidate route: `7108`
- Event Log history id: `9113`
- Phase: `fallout_event_phase.first_winter_year`
- Cooldown family: food security
- Target type: state
- Visible budget cost: `1`
- Human events: `204`, `206`, `207`, `208`, `209`, and `214`
- Hidden AI events: `205`, `210`, `211`, `212`, `213`, and `215`
- Authenticated cleanup: `216`

All gameplay belongs to the Fallout event file and Fallout scheduler. The
chain does not reference zombie ids, files, assets, audio, sprites, or paths.

## Discovery and greenhouse provenance

The candidate producer selects the lowest valid owned state with a current
Fallout identity row, a durable resource row, a produced Air Winter snapshot,
Air Winter Adaptation above `24`, and Air Winter Reclamation above `20`.
Country Food must be at least `24`, and at least one branch must be payable.
The affordability gate is an OR across Destroy, Plant, Isolate, and Share, so
Medicine is not required merely to discover the chain.

Seed-memory flags qualify when they prove a surviving working seed program.
The greenhouse route is generation bound. During pretransition capture,
`fallout_world_end_effects.txt` copies the live
`air_winter_greenhouse_refuge` receipt into
`fallout_pretransition_air_winter_greenhouse_provenance_recorded` and
`fallout_pretransition_air_winter_greenhouse_generation`. The candidate checks
that the copied generation equals the current Fallout transition generation.
Snapshot rebuild clears the receipt before recapture. A generic food,
shelter, reclamation, or building value cannot substitute for the receipt.

## Four branch contract

Event `204` exposes Destroy, Plant, Isolate, and Share. The branches cost
Medicine plus Scrap, Food, Filters, and Recognition respectively. The cost is
paid only after the delayed scheduler row and ordinary receipt both commit.
The country payment flag prevents a second charge.

The accepted opening freezes country Food, Medicine, Scrap, Filters, Shelter,
and Recognition, together with the target state's Air Winter Exposure,
Adaptation, Reclamation, Food reserve, Shelter capacity, and Water security.
It also freezes cause memory, provenance kind, selected branch, result, target,
generation, and issue day. Outcome is calculated once at commit and is not
rerolled by the delayed result or callback.

The viability formula is stored in script constants and uses Adaptation at
35 percent, Reclamation at 30 percent, Food reserve at 20 percent, Shelter
capacity at 15 percent, and Exposure as a 20 percent penalty. The result is
clamped to `0` through `100`. Branch thresholds use the frozen result and the
reviewed resource bands for success, partial success, and failure.

## Delayed result, callback, and failure

The result is scheduled ten days after the accepted opening. Human events
`206` through `209` and hidden AI events `210` through `213` consume the same
issued delayed receipt. Each outcome writes a distinct state memory, changes
survival resources, applies the branch modifier, updates Cohesion through the
single Fallout helper, and clamps the state ledger.

Each failure band requests one exact target-state civilian population loss of
`0.0035` of the current state population through the shared Deaths pipeline.
The minimum remaining population is `100`. The callback never repeats the
loss.

Hidden AI starts each payable branch at the same base score, adds the frozen
success or partial band, applies the current government archetype, cause,
recognition, food, and war adjustments, then selects the highest score. The
selection checks branches in Destroy, Plant, Isolate, Share order and replaces
only on a strictly higher score, so exact ties resolve to the lowest stable
branch identity. An unaffordable branch is assigned an invalid score and is
never used as an unpaid fallback.

The callback is delayed ninety days after the result. Events `214` and `215`
apply the stored outcome without a second roll, write the durable cultivar,
controlled-plot, shared-trial, or failed-review memory, and prepare the exact
cleanup receipt. Event `216` releases result and callback cleanup only after
the issued cleanup token is authenticated. Transaction debris is cleared while
state branch, outcome, cause, provenance, and result memories remain.

## Event Log and localisation

History `9113` owns fifteen payloads, twelve branch and outcome rows, and
three callback rows. The selector is in
`common/scripted_localisation/fallout_world_end_bad_batch_event_log_scripted_localisation.txt`.
Event Log name and detail routing is registered in
`common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` and
`common/scripted_effects/chaosx_events_log_effects.txt`.

Player-facing text names greenhouse trays, filtered trial beds, ash roads,
partner growers, shelter engineers, and food ledgers. It does not present
mutation as an ordinary radiation effect. The dedicated pilot text is written
as a regional food and quarantine story. Full country-memory and government
archetype variants remain a queued expansion surface under the improvement
addendum and do not earn release-floor credit here.

## Asset proof

The dedicated fictional altered-ecology report package is under
`docs/assets/fallout_bad_batch/` with source PNG, processed preview, prompt
provenance, manifest, and GFX handoff. The runtime DDS is
`gfx/event_pictures/fallout_bad_batch/report_event_fallout_bad_batch.dds`.
Sprite `GFX_report_event_fallout_bad_batch` is registered in
`interface/fallout_world_end.gfx` and is referenced by all human opening,
result, and callback events in this chain. No zombie art or path is reused.

## Asset and UI inventory

The human report card uses `GFX_report_event_fallout_bad_batch`, defined in
`interface/fallout_world_end.gfx` and stored at
`gfx/event_pictures/fallout_bad_batch/report_event_fallout_bad_batch.dds`.
The branch options use text and resource tooltips only. No new focus, idea,
decision, mapmode, scripted GUI, flag, portrait, or audio sprite is required
by this chain. The full-screen Fallout blackout remains owned by the separate
blackout surface and is not reused as an ordinary event picture.

## Review boundary

Static review covers unique ids, effect and trigger balance, aligned candidate
arrays, greenhouse generation handoff, branch cost receipts, delayed tokens,
history payloads, localisation keys, dynamic modifier consumers, and DDS
facts. No HOI4 process was launched. Event issuance, popup display, exact
ten-day and ninety-day timing, save recovery, multiplayer behavior, dynamic
modifier presentation, and normal-map visibility remain unobserved engine
surfaces. The scheduler remains dormant and the release-floor count remains
`0 of 660`.
