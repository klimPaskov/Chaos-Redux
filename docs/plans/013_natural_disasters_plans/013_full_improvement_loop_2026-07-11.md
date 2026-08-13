# Event 013 full improvement loop, remaining work after the 2026-07-11 tranche

> Disposition, 2026-07-11: implementation tranches 1-4 and source-of-truth tranche 6 are folded into the live Event 013 files and accepted specs. Tranche 5 completed the static, data, asset, audio, workbook, and balance passes; its live-engine scenario matrix remains queued because the repository has no deterministic headless HOI4 harness. The exact evidence and remaining queue are in `013_implementation_validation_notes.md` and `013_event_completion_final_audit.md`.

## Purpose

This file is the implementation plan for the accepted Event 013 gaps that remain after the current parent tranche. It does not reopen completed architecture, warning-cost, route, geography, queue, cluster, presentation, or asset work.

All names in this plan are script identifiers or working labels. They are not final player-facing localisation.

The source specifications under `docs/specs/013_natural_disasters_specs/` remain authoritative. If this plan is accepted, any design clarification in it must be promoted into the relevant source specification before gameplay implementation is called complete.

## Outcome

Event 013 can be considered implementation-complete only when:

- delayed reports describe the recorded impact instead of a generic family assumption
- Evolution II upgrades unresolved serious aftermath cards already in play
- the abnormal GUI presents selectable physical route markers and discrete timeline points, then routes the player back to the normal aftermath decisions
- Skyfall Crisis contains causal skyfire hail and ocean-impact tsunami routes
- the accepted runtime matrix has evidence for queues, calls, clusters, scenarios, transfer, recovery, GUI, achievements, and super events
- documentation and workbook status describe only verified behavior

## Completed prerequisite tranche

The following surfaces are inputs to this plan, not remaining implementation tasks. They still require the runtime proof listed later.

| Completed or in-flight prerequisite | Contract now available to remaining work |
| --- | --- |
| Physical geography, origin, and basin registries | Family eligibility, initiating context, path basin, and physical follow-up targets use hard data rather than permissive target guesses. |
| Exhaustive random-family preflight | A valid family cannot be rejected only because a bounded random draw missed it. |
| Exact delayed-job wake and direct history ownership | Far-future jobs retain their exact due date and a direct root call can own its one Event 013 history row. |
| Queue context snapshots | Delayed jobs carry aligned family, severity, fine follow-up route, sequence, due date, and state scope through processing and control transfer. |
| Exact evolution override API | Cluster and manual callers can request a precise permitted Event 013 evolution instead of inheriting the current maximum stage. |
| Fine follow-up route persistence | The state stores a route distinct from the compact mechanical chain class. Physical routes re-enter the Event 013 API without creating a second history row. Route labels and queued report route snapshots exist. |
| Warning causality correction | Preparation choices mitigate a matching independently resolved hazard. They do not select the hazard. |
| Eight severity-scaled warning cost profiles | All 75 preparation decisions use the air, naval/coast, command/rail, civilian shutdown, shelter/medical, transport, fuel/convoy, or field-research profile with matched affordability and AI gates. |
| Family-group disruption modifiers | Persistent impact disruption is no longer represented by one interchangeable modifier. |
| Dynamic category art | The decision category reflects the highest-priority visible disaster family. |
| Cluster 5 exact member context | The five logical Event 013 members retain preflight state, target country, family, and exact evolution variant through the pending queue. |
| Abnormal GUI path controls | Previous segment, next segment, and locate-state controls operate on the selected sequence. Fine route data is copied into GUI view arrays. |
| Event 099 bridge and related integrations | Event 099 is a narrow Event 013 sandstorm bridge. Event 046 remains inert and Event 051 overlap guards remain in place. |
| Super-event scope cleanup | The persistent presentation target is generation-safe and cleared after display. |
| Event 013 audio correction | The Event 013 super-event audio package is unique and the selected replacement is documented. |

Do not duplicate these systems. Patch a prerequisite only when its focused audit or runtime scenario proves a defect.

## Remaining blockers and implementation order

| Order | Remaining blocker | Completion dependency |
| ---: | --- | --- |
| 1 | Truthful report composition | Uses completed queue identity snapshots and fine routes. |
| 2 | Evolution II active-card synchronization | Uses the existing aftermath ledger and exact evolution API. |
| 3 | Skyfall causal variants | Uses the geography, basin, origin, fine-route, and physical subcall contracts. |
| 4 | Physical abnormal-map markers and decision routing | Uses stabilized route, origin, basin, timeline, and Skyfall data. |
| 5 | Runtime and balance proof | Runs after the four gameplay and GUI blockers are closed. |
| 6 | Documentation and workbook reconciliation | Runs after implementation facts and runtime evidence exist. |

The order is intentional. The GUI should display final route facts, not provisional data that changes during later Skyfall work.

## Tranche 1: truthful delayed reports

### Accepted gap

The 25 report events have distinct family art and prose, and the queue now snapshots family, severity, and fine route. Their base descriptions can still assert damage or a secondary hazard that did not resolve. Appending the exact fine-route label does not make the preceding assertion true.

### Implementation contract

Keep one report event per family. Compose each description from a stable family observation followed by scoped clauses sourced from the queued impact snapshot.

Required report facts:

- family
- affected state
- severity
- recorded deaths
- each damage-system flag that actually resolved
- warning action and outcome, when present
- fine follow-up route and its due date, when scheduled
- linked physical target, when the follow-up leaves the source state
- recovery phase or unresolved recovery need
- sequence id and segment id for snapshot identity

Extend the aligned country job arrays rather than reading mutable live state at report-delivery time. The enqueue, pop, transfer, clear, and invalid-job paths must carry every added field in the same order.

Recommended helper surfaces:

- `natural_disaster_snapshot_report_outcome`
- `GetNaturalDisasterReportSeverityClause`
- `GetNaturalDisasterReportDamageClause`
- `GetNaturalDisasterReportHumanClause`
- `GetNaturalDisasterReportWarningClause`
- `GetNaturalDisasterReportFollowupClause`
- `GetNaturalDisasterReportRecoveryClause`

The existing `GetNaturalDisasterReportFollowupRoute` remains the route-name resolver. It should be called by the follow-up clause, not used as the only dynamic sentence.

### Report truth rules

- Family base prose may state the observed physical event.
- Damage prose appears only for damage flags captured by that job.
- A report must not state an aftershock, famine, disease, tsunami, ash, fire, or other route unless the captured fine route matches it.
- A physical follow-up clause names its actual destination only when a valid target was scheduled.
- A skipped physical chain is described as no scheduled follow-up. It must not keep a visible route promise that cannot execute.
- Death values come from the captured impact result. Later deaths from a matured chain belong to that chain's own impact record, not the earlier report.
- Report options acknowledge the report and update unread state only. They do not apply hidden gameplay consequences.

### Files

- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `events/013_natural_disasters.txt`
- `localisation/english/013_natural_disasters_l_english.yml`
- `docs/events/013_natural_disasters/overview.md`

### Acceptance cases

1. The same earthquake report is tested with aftershock, seismic landslide, urban fire, and no schedulable physical target.
2. The same flood report is tested with disease, crop loss, refugee pressure, and flash flood.
3. Warning actions that match and do not match the resolved route produce different warning clauses without changing the route.
4. A queued report survives control transfer with the original family, deaths, damage, and route snapshot.
5. Two impacts in the same state before the first report arrives retain separate sequence and segment facts.

## Tranche 2: Evolution II active-card synchronization

### Accepted gap

Evolution II must upgrade open aftermath cards and allow new chain risks for unresolved serious disasters. The exact evolution override API controls new calls. It does not mutate cards that were opened at an earlier stage.

### Bounded ledger

Add a global bounded array of state scopes for open Event 013 aftermath cards. Keep the existing country-scoped `natural_disaster_active_states` arrays as responsibility indexes.

Maintain the global ledger at:

- aftermath-card activation
- card closure
- terminal failure or supersession
- invalid-state pruning
- responsibility transfer

Registration and removal must be idempotent. Transfer changes the responsible country array but does not duplicate the global state entry.

Do not use `on_daily`, `on_weekly`, `on_monthly`, or any world-country scan. Synchronization runs only when a stage is first recorded and through narrow recovery or card-entry safety checks.

### State helper

Add one idempotent state-scoped helper, working name `natural_disaster_sync_open_card_to_evolution_ii`.

Eligibility:

- the card is open
- the recorded card evolution is below Evolution II
- severity is serious enough for a chain under the source spec
- the card has not completed or failed its relevant follow-up window
- the state and responsible country are still valid

Effects:

- raise the card evolution monotonically to Evolution II
- preserve family, sequence, segment, warning result, damage, deaths, progress, and any existing fine route
- if no fine route exists, resolve one from the family and physical geography contract
- schedule the route only after a valid target is confirmed
- apply the Evolution II recovery-pressure adjustment once
- refresh the family-group disruption and visible card data once
- activate the matching chain mission when the follow-up is live
- set an explicit synchronization flag so repeated safety calls cannot duplicate cost, damage, missions, reports, or history

Do not reroll an existing route. Do not replay the original impact. Do not add an Event 013 history row. Do not turn an ordinary open card into an abnormal family when Evolution III opens.

### Evolution logging decision

The source spec permits an unfired Event 013 to open at the current higher evolution. Document this as the Event 013 pre-fire pacing exception. A normal active progression records each newly reached stage once. If runtime evidence shows repeated same-stage logging, repair the flag transition. Do not add MTTH pacing unless the source spec is amended and the `chaos-redux-mtth` skill is used.

### Files

- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- the narrow existing evolution-recording call site
- `localisation/english/013_natural_disasters_l_english.yml` only if visible card wording changes
- `docs/events/013_natural_disasters/overview.md`

### Acceptance cases

1. A severe Evolution I card with no route receives one valid route and one matching mission when Evolution II opens.
2. A card with an existing route retains that route and due date.
3. A resolved, closed, or failed card is not reopened.
4. Repeating the synchronization helper has no additional effect.
5. A transferred card upgrades under its current responsible country.
6. Evolution III opens future abnormal families without relabeling ordinary open cards.

## Tranche 3: causal Skyfall Crisis variants

### Accepted gap

Skyfall Crisis promises meteor impact, meteor shower, skyfire hail, ocean impact, and abnormal ash when chained. The current family pool does not model skyfire hail or a real meteor-origin ocean-to-tsunami route.

### Scope boundary

Do not add a twenty-sixth disaster family. Skyfire hail is a meteor-shower-linked physical follow-up. Ocean impact is an origin-medium and basin context that produces a delayed tsunami path. Abnormal ash remains a consequence of a resolved dust-veil or eruption route, not an unrelated primary draw.

### New causal data

Add centralized enum values for:

- origin medium: land impact, atmospheric fragmentation, ocean impact
- fine route: skyfire hail
- Skyfall variant: local land impact, severe land chain, meteor shower, skyfire chain, ocean impact chain

Persist the origin medium and variant through sequence planning, scheduled state data, abnormal history, GUI view arrays, reports, and cleanup.

### Skyfire hail route

When an eligible meteor-shower sequence resolves the skyfire route:

1. keep meteor shower as the sequence origin family
2. select a geography-valid hailstorm target from the same path context
3. dispatch a no-history hailstorm physical subcall with meteor origin context
4. apply the fine route `skyfire_hail`
5. allow its damage to create the accepted fire pressure only through the normal warning and chain mechanics

The hail segment must have a distinct path marker and report clause. It must not be a renamed ordinary hailstorm selected independently from the Skyfall pool.

### Ocean impact route

HOI4 state scope cannot represent a sea province as the impact state. Use the accepted hard tsunami basin registry and a coastal proxy only as the recorded observation or nearest coast.

1. choose and lock a tsunami basin
2. record origin medium as ocean impact
3. do not apply land-crater damage or crater recovery to the coastal proxy
4. schedule the first valid coastal tsunami segment within the locked basin
5. schedule later basin-valid coastal arrivals through the existing sequence contract
6. keep one Event 013 history row for the Skyfall sequence
7. expose the ocean origin and each arrival in the abnormal history and report snapshots
8. gate the delayed-tsunami super event on an actual scheduled ocean chain, not a generic coastal meteor chance

If no valid coast exists in the locked basin, reject that variant during preflight and select another valid Skyfall variant before any player-facing promise is created. This is validation, not a fallback substitution.

### Intensity matrix

| Intensity | Skyfall contract |
| --- | --- |
| Low | Local land impact with normal warning, report, and recovery. |
| Medium | Larger land-impact sequence and regional falloff. |
| High | Severe land impacts with wildfire or dust-veil chains. |
| Maximum | Meteor shower, skyfire hail, ocean impact, delayed tsunami, and abnormal ash routes become eligible. |

The manual scenario can bypass ordinary evolution prerequisites, but intensity still owns abnormal access. All outcomes remain non-terminal.

### Files

- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `common/scripted_triggers/013_natural_disasters_geography_triggers.txt`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `common/decisions/013_natural_disasters_decisions.txt` only if scenario visibility or tooltips need the resolved variant
- `localisation/english/013_natural_disasters_l_english.yml`
- existing Event 013 super-event gate and documentation files

### Acceptance cases

1. Low Skyfall cannot produce an abnormal route.
2. Maximum Skyfall can produce each of the five accepted causal roles.
3. Skyfire hail has meteor origin, hail physical damage, and no second Event 013 history row.
4. Ocean impact produces no land crater on its coastal proxy.
5. Every delayed tsunami arrival remains inside its locked basin and uses valid coastal targets.
6. Abnormal ash appears only after a valid dust-veil or eruption cause.
7. The Skyfall and delayed-tsunami super-event gates each fire only at their accepted moment.

## Tranche 4: complete the physical abnormal map

### Accepted gap after path controls

The GUI can cycle previous and next segments, locate the selected state with `goto_state`, and display route data. The map still uses fixed decorative marker positions, the timeline remains a text line, and no marker routes the player into the normal aftermath decision surface.

### Spatial route view

Retain the urgency list as the entry and archive view. For a selected abnormal sequence, build a sequence-only path view sorted by segment number.

Add aligned view facts for each visible marker:

- state scope
- segment number
- family and origin family
- origin medium
- path basin
- schedule or impact date
- path status
- fine follow-up route
- chain target and due date
- report date
- recovery phase and reassessment date
- record result and history status

The path view must never mix markers from unrelated sequence ids.

### Marker contract

Provide up to five selectable marker buttons for the visible sequence window. Each marker:

- uses a coordinate selected from a documented basin or domain layout table
- distinguishes forecast, warning, next hit, confirmed impact, follow-up, recovery, and closed history
- has a hover tooltip with state, segment, arrival, family, and route
- selects the record on click
- enables locate-state only for a real state scope
- retains the same data and coordinates in static animation mode

Coordinates are presentation data. They must be centralized and documented. A single fixed marker drawn over a decorative map does not satisfy the physical-route contract.

### Timeline contract

Replace the single text-only timeline with discrete selectable points for the facts that exist:

- forecast or warning
- scheduled impact
- confirmed impact and report
- follow-up due date
- reassessment
- super-event moment when applicable

Each point changes the selected marker or shows its scoped tooltip. Do not create a point for an absent milestone.

### Normal decision routing

Gameplay costs and effects remain in `common/decisions/013_natural_disasters_decisions.txt`.

The GUI action must:

1. store the selected state in the existing country selection variable
2. close the scripted GUI
3. make only that state's normal warning, recovery, relief, or chain decisions the relevant target set
4. leave AI behavior entirely on the normal decision and mission path

Do not duplicate a preparation or recovery effect inside scripted GUI code.

### History and observer rules

- history mode is read-only
- a closed record can be located but cannot expose live decisions
- two countries observing the same global sequence build independent country view arrays
- a country cannot receive action routing for a state it does not currently own or control unless the existing foreign-relief contract explicitly permits it
- repeated hits in one state remain separate segments when their sequence or segment identity differs

### Files

- `interface/013_natural_disasters.gui`
- `common/scripted_guis/013_natural_disasters_scripted_gui.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `localisation/english/013_natural_disasters_l_english.yml`
- `docs/events/013_natural_disasters/overview.md`
- `docs/assets/013_natural_disasters/gfx_handoff.md`

No replacement art is required. Reuse the completed animated layers, static fallbacks, marker sprites, card frames, and recovery assets.

### Acceptance cases

1. A rupture path with five segments shows five selectable markers in segment order.
2. Next and previous path controls wrap within the selected sequence only.
3. Locate-state focuses the selected real state.
4. A live marker routes to that state's normal decisions without duplicating effects.
5. History mode remains read-only.
6. Static mode preserves marker position and meaning.
7. Two overlapping abnormal sequences do not mix marker data.
8. Two observers can inspect the same sequence without overwriting each other's selection.
9. Skyfire hail and ocean-impact tsunami use their distinct origin and route markers.

## Tranche 5: focused runtime and balance proof

Static validation is not completion evidence for Event 013. Record results in `docs/plans/013_natural_disasters_plans/013_implementation_validation_notes.md` and keep affected workbook rows at `Needs Testing` until their cases pass.

### Queue and API scenarios

1. Baseline delayed warning and impact with no same-day collapse.
2. Far-future job due date with an earlier job inserted later.
3. Direct console root call with exactly one history row.
4. Accepted then rejected public calls in one effect chain.
5. Rejected then accepted public calls in one effect chain.
6. Selected-state then selected-country calls in one effect chain.
7. Partial multi-hit success with correct resolved output.
8. The dynamic indexed-scope queue worker with more than one job.
9. Control transfer while warning, report, follow-up, and recovery jobs are queued.

### Route and warning scenarios

1. Every fine route reaches its compact chain class or physical family as documented.
2. Every physical route preflights a valid target before it becomes visible.
3. Changing among the three warning decisions for one scheduled family does not change the resolved fine route.
4. A matched preparation reduces the matching consequence.
5. A non-matched preparation preserves its own useful protection without suppressing an unrelated route.
6. All 75 decisions verify affordability, paid cost, visible cost, severity scaling, expiry, and AI gate.
7. The nine family-group disruption profiles apply and clear on the right families.

### Evolution, cluster, and scenario scenarios

1. Baseline and Evolutions I, II, and III.
2. An open-card Evolution II upgrade, existing-route preservation, and idempotence.
3. All five Cluster 5 logical roles at their relevant tiers.
4. Two overlapping cluster launches with exact target and evolution context.
5. Every Disaster Barrage type at Low and Maximum.
6. Medium and High boundary checks for sequence size and abnormal access.
7. Skyfall causal cases from Tranche 3.
8. Event 046 inactivity, Event 051 overlap exclusion, and the Event 099 to Event 013 bridge.

### Report, GUI, recovery, and achievement scenarios

1. Report truth cases from Tranche 1.
2. Overlapping abnormal paths and same-state repeated records.
3. Dormant archive, history mode, static mode, marker routing, and two observers.
4. Full, partial, failed, cancelled, expired, and cleaned recovery at every capacity band.
5. Foreign relief in transit during responsibility transfer.
6. All ten achievement unlock routes and their disqualifiers.
7. Each super-event gate, display generation, audio identity, and target cleanup.

### Balance review

Inspect actual tuning values and outcomes for:

- dense compared with sparse states at the same severity
- war-damaged compared with intact infrastructure
- weak compared with strong countries paying warning costs
- warning matched compared with unmatched and unprepared outcomes
- Evolution II aggregate regional deaths and building damage
- Evolution III and Maximum Skyfall aggregate deaths, damage, and recovery load
- AI preparation and recovery choices under low resources and multiple concurrent cards
- news throttling under repeated small Evolution II hits

Balance findings must change constants, weights, or effects when outcomes miss the accepted bands. A prose assertion that balance looks reasonable is not evidence.

## Tranche 6: source-of-truth and workbook closure

After implementation and runtime proof:

1. Promote accepted clarifications from this plan into the relevant Event 013 source specs.
2. Update `docs/events/013_natural_disasters/overview.md` with the verified report, active-card, Skyfall, and physical-map behavior.
3. Update `docs/systems/event_clusters.md` with verified five-role dispatch behavior.
4. Update Event 013 super-event documentation only for gates that passed their scenarios.
5. Update `docs/assets/013_natural_disasters/gfx_handoff.md` with final marker and timeline wiring. Do not request replacement art.
6. Reconcile Event, Scenarios, and Clusters rows in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` using the `xlsx` skill.
7. Keep wording in workbook detail fields exactly aligned with final in-game localisation.
8. Mark rows `Implemented` only when their matching runtime scenarios have evidence.
9. Resolve or supersede the 2026-07-11 gap inventory and implementation handoffs with explicit disposition notes.

Run the Event 013 completion, decision and mission, localisation, and spreadsheet audits again before the final completion claim.

## Stop conditions

Stop and request user direction if completion would require:

- a new disaster family
- a new world-end branch
- a new country or focus-tree package
- a second independent disaster controller
- replacement of completed assets with a fallback
- a world-iterating daily, weekly, or monthly on action
- removal of accepted route, marker, report, scenario, cluster, achievement, or super-event behavior
- a substitute for unsupported GUI behavior rather than the accepted interaction

## Simplifications and omissions

No simplification or fallback is authorized by this plan. The four implementation tranches cover every remaining accepted-spec gameplay and GUI blocker identified after the parent tranche. Runtime proof and documentation reconciliation remain mandatory completion work.

## Skills used to produce this plan

- `chaos-redux-improvement-loop`
- `chaos-redux-event-planning`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-super-events`
