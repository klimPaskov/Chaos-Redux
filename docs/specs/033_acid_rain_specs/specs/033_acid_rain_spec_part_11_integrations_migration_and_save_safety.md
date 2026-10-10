# Event 033 Acid Rain, Part 11, integrations, migration, and save safety

Status: `implemented` in source for registration, the Air source, Deaths, CBRN civilian protection, the Humanitarian addition path, control transfer, prototype migration and terminal interruption.
Source-specific Humanitarian retirement is `unresolved` (README open question 1).
Save and reload, multiplayer determinism and migration of real old saves are user live checks.
This part owns the Air cap invariant.

## Event-system registration

Event 33 is registered as:

- a member of `global.major_events` and of no repeatable or fire-once list
- a Chaos level 2 event in the availability surface
- one-time fired after accepted formation
- an ordinary Major for independent firing, with the normal weight and reset path
- a mixed-pacing member when queued through Natural Disasters
- a Major, level 2, Natural Disasters, Severe entry with three evolution rows in Event Details

## Air Cleanliness integration

### Dedicated source

Acid Rain owns Air source id `5` (`acid_rain_air.source_id`) in the shared source ledger, separate from the natural aerosol row, so its lifetime contribution and 15-point cap stay auditable.
The shared ledger stores the source's lifetime accepted additions and its current share of global contamination, and the Air Cleanliness system owns how that share recovers.
The Event 33 interface shows only the lifetime addition; the Air Cleanliness source details show the ledger row.

### Hard-cap formula

For every requested positive Event 33 addition:

1. `lifetime_remaining = max(0, 1500 - event_lifetime_added_bp)`
2. `ceiling_remaining = max(0, 5000 - global_air_contamination_bp)`
3. `clamped_request = min(request_bp, lifetime_remaining, ceiling_remaining)`
4. if `clamped_request <= 0`, add nothing
5. call the central Air Contamination mutation helper with the Acid Rain source ID
6. read the actual applied positive delta after central clamping
7. add only that actual delta to Event 33 lifetime additions
8. update Event 33 current pressure and source ledger from the same actual delta

Never increase the lifetime counter before the central helper returns its actual delta.

If another system pushes global contamination above 5000 bp after Event 33 has added contamination, do not remove Event 33's past contribution. Future Event 33 requests add zero until the global value falls below 5000 bp.

### Formation and weekly request

Formation requests `75 bp`, then the weekly pulse builds a request from stored state:

| Component | Request addition |
| --- | --- |
| Active world share below 2 percent | `+4 bp` |
| Active share 2 to below 5 percent | `+8 bp` |
| Active share 5 to below 10 percent | `+12 bp` |
| Active share 10 percent or higher | `+16 bp` |
| Average Weak intensity | `+4 bp` |
| Average Standard intensity | `+8 bp` |
| Average Strong intensity | `+12 bp` |
| Average Extreme intensity | `+16 bp` |
| Each active severe cell | `+3 bp`, capped at `+9 bp` |
| Multiple-front atmospheric split | `+4 bp` |
| Global layer | `+10 bp` |

Clamp an active weekly request between `8 bp` and `45 bp` before the two hard caps. A week with no active acute weather requests zero.

### Current source share

Event 33 keeps no pressure estimate of its own.
It mirrors the shared ledger's current Acid Rain share into `global.acid_rain_air_current_bp`, and the global-phase dissipation penalty reads that mirror.
Global recovery, and with it the shrinking current share, belongs to the Air Cleanliness system; Event 33 never subtracts contamination.

### Chaos ownership

The central Air Cleanliness helper converts actual global contamination change into its normal Chaos effect. Event 33 does not add another Chaos point for the same percentage increase.

## Deaths integration

Call `apply_exact_state_civilian_population_loss` for every positive Event 33 mortality pulse and use one accepted cause ID as defined in Part 4. Store `state_civilian_population_loss_applied`, confirm that the state's real civilian population fell by that value, and register the same value once. The Deaths system owns its normal Chaos conversion and UI history. `local_manpower`, recruitable-population penalties, generic manpower loss, unit attrition, and Event 33 counters remain non-authoritative and cannot substitute for population removal.

Required reconciliation:

- country responsibility changes
- state controller changes
- protected population floor
- state population already reduced by another event on the same day
- loading a pulse after loss application but before report scheduling

Use a generation, state, exposure type, episode, and pulse-date receipt so a repeated scheduler call cannot apply the same loss twice. Commit the receipt in the same effect chain as the population transaction and its counters.

## CBRN civilian-protection integration

Event 33 can reuse compatible national protection facts from the existing CBRN civilian system:

- gas masks and filters
- protective clothing
- decontamination equipment
- emergency medical capacity
- warning systems
- shelters

The implemented integration reads `cbrn_civilian_mask_effective_coverage` to lower the mortality protection multiplier (Part 4), and the AI reads the strong-protection CBRN triggers to lower, never zero, the Medical project priority.
It never counts the same stockpile twice or creates a second mask inventory.
Event 33 projects represent broad civilian infrastructure and organization; CBRN assets do not grant project tiers.

## Humanitarian integration

Event 33 registers three kinds of proven consequence with the famine owner through `famine_adapt_acid_rain_state`: each exact positive pulse loss, a state's first tier-2 or tier-3 aftermath, and a finished evacuation of a state of at least 500,000 people (amounts in Part 4).
Each request carries source id 33, the Acid Rain death reason, the current generation and a per-transaction revision, so it stays distinct from Event 013 and Air Winter requests.
Under the famine owner's current contract an accepted request adds a daily-decaying food shock and renews the 60-day disaster food context, which does not stack and expires on its own.
A tier is marked registered only after the famine owner accepts it, so a rejected request can retry.
The famine system owns food security, relief, famine mortality and any later famine survivor flight; Event 33 owns only its requests.
Whether recovery must additionally retire Acid Rain's share is README open question 1.

## Natural Disasters integration

Event 33 is a separate Major system, not an Event 13 family. It can call shared disaster, Deaths, Air, and Humanitarian interfaces, but it does not call the Event 13 public disaster generator for its main rain pulses.

When Event 13 and Event 33 affect the same state:

- preserve separate card and aftermath ownership
- combine actual state modifiers through accepted dynamic-modifier rules
- deduplicate shared Humanitarian sources
- keep Event 13 natural aerosol pressure separate from Acid Rain source additions
- avoid two opening-casualty shocks on the same scripted day when a shared safety scheduler can stagger them

## Occupation and control changes

When an active or aftermath state changes controller:

1. update the state responsible-country record
2. decrement old country active, warning, or aftermath counts
3. increment new country counts
4. move state-targeted decisions and pending reports
5. preserve touched, episode, deaths, damage, and achievement history
6. preserve evacuation completion and remaining duration
7. refresh both countries' category visibility

Use the narrow state-control on-action. Do not scan all active states after every control change.

## Famine, migration and other system links

- Famine: through the Humanitarian requests above; damaged transport and poisoned water reach the player as Food Security changes on the famine surface.
- Migration: Event 33 creates no migration cohort, because evacuation protects people in place and is recorded as disaster pressure; displacement reaches migration only when famine itself proves survivor flight through `migration_accept_famine_survivor_request`.
- Condemnation: none, because the rain has no responsible actor.
- Camps, CBRN warfare and fallout: no direct link beyond the shared Deaths ledger, the Air ledger and CBRN civilian protection above.

Event 33 never hard-codes a second famine, disease or migration engine.

## Prototype retirement

Status: `implemented`.
The continent prototype's daily all-country and all-owned-state scan, timeout missions, continent completion array, one-image-per-continent GUI swap, repeatable registration and modifier-only death claims are gone from the active runtime.
The two old missions `chaosx_acid_rain_timeout` and `chaosx_acid_clouds_timeout` remain only as inert shells that cancel themselves, so old saves can unload them; `acid_rain_migrate_legacy_runtime` removes their records.

## Old-save migration

Status: `implemented` through `acid_rain_migrate_legacy_runtime` and the `acid_rain_migration` constants; migration of real old saves is a user live check.

### Save where the prototype never fired

- clear stale unowned prototype variables if present
- register the new Major event state
- do not mark Event 33 fired

### Save where the prototype is active

1. set the migration lock and new schema
2. build the frozen eligible-state registry
3. read the old current region ID
4. mark states with the old acute `acid_rain_state` modifier as touched and active
5. treat old `acid_clouds_state` as visited-region or warning evidence, not automatic acute state coverage
6. create one new Standard-intensity front in the old current region
7. seed its active footprint with migrated acute states, then fill to the minimum target if needed
8. preserve old visited-region history without marking every state in those regions touched
9. remove old missions, on-action ownership, and prototype modifiers only after new receipts exist
10. start future exact state-population mortality without backfilling deaths the prototype never applied
11. show one migration summary only in debug or patch notes, not as a second formation super-event

### Save where the prototype completed

If old completion state proves all seven prototype regions were processed and the event is no longer active, preserve Event 33 as fired and complete. Do not reactivate it to enforce the new state-coverage rule retroactively.

### Ambiguous save

If prototype active flags exist but no valid current region or acute state can be recovered, fail closed into controlled dissipation and preserve the fired state. Do not randomly start a new front after an unprovable partial event.

## Save and load safety

Persist:

- schema and phase
- frozen state registry and counts
- touched receipts
- all front records and arrays
- next scheduled dates
- severe and superstorm episode IDs
- country projects and resource commitments
- state episode and opening-shock receipts
- deaths, prevented deaths, damage, contamination, and achievement facts
- dissipation check index

On load:

- do not reroll regions, quotas, movement dates, severe cells, or third-front results
- validate array alignment and stable IDs
- repair only missing derived values
- never rebuild history from current modifiers when stored receipts exist
- if an active array is missing, run one bounded reconciliation under a global lock

## World-end and terminal transitions

If another system commits a terminal world transition:

- call Event 33 acute cleanup through its public cleanup helper
- stop future contamination requests
- preserve already added contamination unless the terminal system owns a documented atmospheric rewrite
- preserve Deaths history
- close or transfer projects according to the terminal system's country rewrite contract
- release cluster reservation
- mark Event 33 termination reason in history

Event 33 cannot block a terminal transition by waiting for complete state coverage.

## Multiplayer determinism

- global random draws happen in one host-authoritative effect chain
- front slots process in stable numeric order
- state tie-breakers use stable state ID after equal weights
- GUI clicks are read-only
- project decisions mutate only the acting country and stored global counters
- save reload does not reroll any accepted draw

## Documentation updates

The catalog workbook and exports, the event overview, the event-cluster documentation, the Air source-ledger documentation, the Deaths reason table and the audio catalogue already describe the implemented event.
Any later behavior change updates the overview and, for catalog-visible wording, the workbook before its exports.

## Accepted implementation decisions, 2026-10-04

Acceptance basis: agent decisions recorded in `docs/plans/033_acid_rain_plans/agent_decisions_2026-10-04.md`, taken on 2026-10-04 under the full design authority the user granted for Event 033; each item is implemented in source and its live-game confirmation is a separate gate.

- Humanitarian adapter (D5, D14): `famine_adapt_acid_rain_state` is a minimal append to the famine-owned `common/scripted_effects/famine_adapter_effects.txt` and its documentation table, mirroring the Event 013 natural-disaster adapter with Acid Rain request identities. Its generic additive pressure endpoint does not establish a reversible source-33 ledger or recovery retirement. Cleanup must touch only Acid Rain contributions through a supported owner interface, and that implementation dependency remains unresolved in the October 7 consequence-acceptance reconciliation.
- Shared exact-loss helper (D1): `apply_exact_state_civilian_population_loss` removes population first, reads back the observed decrease and records it in Deaths once; the twelve shared callers declare their outputs before each call.
- Save safety (D9, D19): registries are created at their bound before indexed writes, and the region index rebuilds itself when it is missing or belongs to another generation, so a save made before the index existed continues safely.
- Event Details navigation (D18) uses only the shared Event Log entry points (`open_events_log_events_tab`, `get_event_type`, `events_log_add_event_details_entry`) and changes no shared file.
- Weekly Air request (D30): the "Active world share" is the share of valid states under acute rain now (ordinary front targets, active severe-cell states outside them, or every valid state under the global layer), which reads Gate 9's "stored coverage" through this table; the request runs in the regional and global phases, averages the open fronts' intensity (Standard under the global layer), counts active severe cells and superstorms in the capped adder, and its due day advances from the previous due day; the first weekly request is due one week after the formation request (D36).
