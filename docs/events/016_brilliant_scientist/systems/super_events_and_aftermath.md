# Event 016 super-events, world threat, terminal routes, and defeat aftermath

## Purpose

This system turns Event 16 from a local scientific appointment into campaign-scale presentation only after the campaign has supplied matching evidence.

It owns exactly six visible super-event packages, an event-driven Kruger world-threat source, local and regional defeat legacies, a qualifying global-crisis settlement, Laboratory World, and the Strategic Singularity handoff into Fallout.

Event 16 remains outside event clusters.

## Six-package presentation contract

| Visible ID | Package | Runtime gate |
| ---: | --- | --- |
| `90` | International recognition | Evolution II chronology, a public anchor, an international anchor, and the configured recognition score |
| `91` | Kruger State formation | An active sovereign Kruger State with at least two controlled states and a real project-force, advanced-project, or nonterminal Singularity asset |
| `92` | Global Kruger threat | A scored combination of territory, industry, deployed or weaponized project families, opponents, aggressive reach, and strategic escalation |
| `93` | Laboratory World | The conquest commitment, terminal map audit, global administration, subject integration, major-opposition defeat, chaos above the shared final threshold, and no incompatible terminal state |
| `94` | Strategic Singularity | A fully armed and connected device whose source-aware Fallout request has acquired the shared world-end lock |
| `95` | Qualifying defeat | Defeat after the persistent threat ledger reaches the configured global-crisis qualification score |

The queue in `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` serializes these packages against the shared `super_event_visible` flag.

If another super-event is visible, the Event 16 package remains in aligned ID and actor arrays and retries through hidden event `chaosx.nr16.300`.

When dispatch succeeds, the queue writes the visible ID, selects the matching scripted localisation, picture, and final audio ID, and plays the settings-aware super-event audio for human countries.

## International recognition

Evolution II by itself cannot fire recognition.

The host must retain Kruger, have a public anchor such as established reputation, an exposed research advantage, or a publicly failed assassination, and have an international anchor such as a joint laboratory, repeated foreign operations, or several high-interest foreign actors.

Prototype depth, portfolio depth, public reputation, exposed research advantage, foreign activity, assassination exposure, and joint-laboratory history contribute to the shared recognition score.

The fired flag and date prevent duplicate presentation while preserving the recognition history for later event-log and achievement checks.

## Event-driven world threat

`brilliant_scientist_refresh_world_threat_source` is called by relevant project, decision, focus, war, and territory transitions.

It does not introduce a recurring daily, weekly, or monthly world scan.

Each refresh records current and peak states, factories, deployed project families, weaponized families, opponents, major status, and late Singularity construction.

It also marks every currently controlled state as historical Kruger territory, which later allows inspection and reconstruction to follow actual control history.

The shared world-threat source activates only after the Kruger State has a real territorial and industrial base, aggressive reach, a sufficient threat score, and either several project armies, extensive weaponization, or an armed-program history.

A durable settlement, verified global dismantlement, defeat, capitulation, or world end clears the active source without erasing peak history.

### Active-day history

On activation, the country records `brilliant_scientist_world_threat_start_num_days` from `global.num_days` for the current interval.
The first `brilliant_scientist_world_threat_start_date` and reveal date remain calendar-history values; they are never subtracted to calculate elapsed days.
`brilliant_scientist_refresh_world_threat_duration` rebuilds `brilliant_scientist_world_threat_duration_days` from positive `brilliant_scientist_world_threat_accumulated_active_days` plus the positive current day difference only while the country threat flag is active.
A missing start or negative difference contributes zero, and refreshing twice does not accumulate the same interval twice.

Every source-clear boundary calls `brilliant_scientist_close_world_threat_interval` before clearing the active flag.
That helper stores the rebuilt total, records the end date and day, and clears the current start-day receipt before returning.
Repeated or nested close calls therefore contribute nothing further.
Reactivation opens a fresh interval without discarding completed active time, so inactive gaps never count.
Both Laboratory World and the source-aware Singularity finalizer close the interval and clear the country threat flag as well as the shared source flag.

## Defeat scale

Defeat qualification uses duration, major-power status, opponent counts, deployed project families, weaponization, late Singularity construction, peak territory, and peak industry.

A local defeat produces one project-causal archive legacy for the former host or actual victor.

A regional defeat produces a news event and a persistent countermeasure-sharing or nationalized-archive settlement.

A qualifying global-threat defeat opens the four-part custodian system and visible super-event `95`.

The defeated country's classification is permanent: capitulation followed by annexation cannot dispatch a second aftermath package.
Local and regional recipients each hold a distinct pending archive receipt, set before their event is delivered.
The chosen option clears that receipt before granting its original reward and permanent outcome, so a duplicate already-delivered popup cannot award the other choice.
Preparation rejects both outstanding and completed packages without erasing their history.

Remnant flags derive from actual deployment history or still-fielded project formations; biological remnants require deployed or weaponized biological history, and a Singularity remnant requires late-construction history.

The system does not create every remnant in every campaign.

## Qualifying defeat custodian

The actual capitulation or annexation victor becomes the global aftermath custodian.

The custodian receives four categories: treaty, inspection, reconstruction, and project remnants.

The archive, regional-settlement, and each project-remnant hearing append a custodian-policy clause selected from the current government. Democratic custodians are asked to publish evidence and hear affected communities; communist custodians frame the inheritance as a public industrial trust; fascist custodians prioritize classification and command; non-aligned and unusual custodians must negotiate a doctrine while the settlement is still being built. The containment settlement reports additionally retain the host-archetype clause beside the recorded sovereignty policy, so each resolved `.31` outcome keeps its institutional context. The clauses are descriptive only and do not replace the existing ideology-weighted AI, decision gates, legal outcomes, or remnant receipts.

All twenty-two decisions use event-owned icons, political costs, exact factory occupancy, equipment where relevant, and bounded durations.

Timed decisions cancel when the settlement closes, and state-targeted work also cancels if the selected state ceases to be fully controlled.

### Treaty

The custodian founds a scientific commission, exchanges countermeasures, drafts personhood and asylum articles, and writes the Singularity convention.

Ratification requires the configured treaty progress and certified inspections.

The final compact preserves a research institution while carrying a continuing production burden.

### Inspection and dismantlement

The custodian must register at least one controlled historical Kruger laboratory state, inventory the project armies, secure the command archives, and resolve every project-causal remnant hearing.

The explicit registered-facility receipt prevents remnant progress from substituting for a physical inspection.

Certification removes every Event 16 project formation and runtime military package from a still-existing defeated Kruger country, closes recruitment, records dismantled project families, removes biological deployment modifiers, disarms the Singularity, and permanently blocks both terminal routes.

Completed-project and deployment history remains available for the event log, achievements, and postwar text.

### Reconstruction

State rebuilding is available only in fully controlled historical Kruger territory or a state with an Event 16 facility or laboratory-corridor history.

Each state can be rebuilt once and consumes trucks, trains, support equipment, political authority, six civilian factories, and time before adding one infrastructure level and one civilian factory.

Survivor clinics and the memorial archive provide alternative concrete reconstruction work.

Closing the board requires three completed reconstruction receipts and creates the lasting reconstruction institution.

### Project-causal remnants

Clone, machine, paleogenetic, xenobiological, portal, temporal, biological, alien, and Singularity hearings each offer two mutually exclusive legal dispositions.

Each choice writes a persistent history flag, adds a distinct lifecycle idea, increments inspection progress once, and closes only its own remnant family.

The remnant category resolves automatically when every family that actually exists has received a disposition.

## Settlement completion

The aftermath completes only after treaty ratification, inspection certification, reconstruction closure, and all actual remnant hearings.

Completion clears the active custodian targets and categories while preserving dates, institutions, legal outcomes, defeated-state identity, and project history.

The separate Kruger State durable-settlement certificate requires completed disarmament throughout its audit timer.
It cancels when its eligibility is lost, and its final helper repeats the same condition independently of UI cancellation.
The durable-settlement receipt is written before administration is awarded, preventing repeated certification or post-terminal settlement rewards.

## Laboratory World

Laboratory World uses world-end scenario reservation `11` and visible package `93`.

The conquest commitment is mutually exclusive with the Singularity commitment.

The terminal gate requires Evolution IV chronology, the enabled shared scenario, a completed and passed terminal map audit, sufficient actual map control, global administration, subject integration, defeated major opposition, and global chaos above `constant:chaos_meter_tier_range.tier_final.plus`.

Only after those requirements are true does the route set the normal world-end state, record the Laboratory World scenario, stop incompatible Event 16 systems, and present the super-event.

## Strategic Singularity and Fallout

Strategic Singularity uses world-end scenario reservation `12` and visible package `94`.

Preparation may begin before the world-end threshold, but execution requires Evolution IV chronology, all required components, an armed device, a live command network, fail-deadly authority, an enabled chaos meter, no active disarmament, a free Fallout request ledger, and no incompatible world end.

Arming continuation, fail-deadly authorization, and final commitment recheck the current owned-and-controlled qualifying facilities rather than relying solely on a past audit flag.
The shared final gate preserves the special capitulation-failsafe path; it does not import ordinary decision availability as a blanket non-capitulation requirement.

At execution, Event 16 computes the deficit between the current chaos value and `constant:chaos_meter_tier_range.tier_final.plus`, raises chaos through the documented Singularity source, records deaths, contamination, condemnation, and detonation history, and submits a maximum-intensity source-aware Fallout request.

Event 16 does not seize `world_end` directly from Fallout.

The shared Fallout request lock validates and owns the world-end transition, then calls `brilliant_scientist_finalize_singularity_after_fallout_lock`, which records the Event 16 terminal result and presents package `94`.

This sequence allows the device to fire from any starting chaos tier while still respecting the shared world-end threshold and Fallout pipeline.

## Main implementation files

- `common/script_constants/016_brilliant_scientist_super_event_constants.txt`
- `common/script_constants/016_brilliant_scientist_aftermath_constants.txt`
- `common/scripted_triggers/016_brilliant_scientist_super_event_triggers.txt`
- `common/scripted_triggers/016_brilliant_scientist_aftermath_triggers.txt`
- `common/scripted_triggers/016_brilliant_scientist_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_aftermath_effects.txt`
- `common/decisions/016_brilliant_scientist_aftermath_decisions.txt`
- `common/decisions/categories/016_brilliant_scientist_aftermath_categories.txt`
- `common/ideas/016_brilliant_scientist_aftermath_ideas.txt`
- `common/on_actions/016_brilliant_scientist_project_on_actions.txt`
- `events/016_brilliant_scientist_super_events.txt`
- `events/016_brilliant_scientist_aftermath_events.txt`
- `localisation/english/016_brilliant_scientist_super_events_l_english.yml`
- `localisation/english/016_brilliant_scientist_aftermath_l_english.yml`

## Visual and audio wiring

The six `457x328` super-event DDS files live under `gfx/super_events/016_brilliant_scientist/` and are registered by `interface/016_brilliant_scientist_super_events.gfx`.

Their source, processed, decoded-DDS, provenance, and validation evidence lives under `docs/assets/016_brilliant_scientist/`.

The six final WAV files live under `sound/016_brilliant_scientist/`, with shared sound, music, scripted-localisation, and settings-aware playback mappings for visible IDs `90` through `95`.

The twenty-two aftermath decision sprites and four category sprites are registered by `interface/016_brilliant_scientist_aftermath_decisions.gfx`.

Their exact runtime paths and visual meanings are listed in `docs/assets/016_brilliant_scientist/aftermath_decision_icon_contract.md`.

The archive and project-remnant hearings `chaosx.nr16.301`, `.303`, and `.310` through `.318` use scripted picture selection. `GetBrilliantScientistAftermathRemnantPicture` routes clone or machine, biological or paleogenetic or xenobiological, portal or temporal, and alien or singularity remnants to four reviewed `210x176` documentary report cards. Prototype-only and unresolved remnant records retain `GFX_report_event_016_brilliant_scientist_aftermath_remnant`, while the regional settlement `.303` keeps the shared archive card because it is not tied to one project family. The legal choices, receipts, and inspection progress are unchanged by this presentation routing.

## Closure evidence and remaining implementation

The 2026-09-02 terminal postpatch handoff under `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_terminal_postpatch_review_2026-09-02.md` records the once-only archive and certificate traces and all eleven frozen duration boundary cases.
Its MCP artifacts capture the current event consumers, but the historical comparison returned `EVENT_REVISION_NOT_CACHED`; the arithmetic checks are source regressions, not engine execution.
Command and power infrastructure still require the separately tracked physical site/role/quantity implementation before the whole terminal system can be accepted.
No icon or sprite is added by these lifecycle guards; the existing terminal decision icons, aftermath report cards, and six presentation packages remain their consumers.

## Future extensions

The settlement can later support diplomatic participation by additional coalition members, but only through a reviewed design that preserves one authoritative custodian and prevents duplicate rewards.

The remnant ideas can later feed unrelated biological, alien, portal, or temporal event chains when those systems expose stable integration hooks.

A future map overlay could show registered and reconstructed laboratory states, but it should reuse the existing state flags rather than create a second recovery ledger.

Any future return of Kruger must use the preserved clone, machine, temporal, or alien evidence and cannot create a duplicate Warren Kruger identity.
