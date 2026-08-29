# Event 033 Acid Rain, Part 11, integrations, migration, and save safety

## Event-system registration

The existing repository registers Event 33 as repeatable. The rework must:

- remove `33` from `global.repeatable_events`
- add `33` to `global.major_events`
- register Chaos level 2 in the event availability surface
- keep one-time fired state after accepted formation
- use the normal Major weight and reset path for independent firing
- use mixed Major cluster pacing when queued through Natural Disasters
- update Event Details type, status, cluster, severity, and evolution rows

Do not leave Event 33 in both type arrays during migration.

## Air Cleanliness integration

### Dedicated source

Add a stable Acid Rain source to the Air Contamination source ledger. Reusing the broad natural aerosol row would hide the user-required Event 33 lifetime contribution and make the 15-point cap hard to audit.

The source records:

- current Event 33 atmospheric pressure estimate
- lifetime actual additions
- last actual addition
- first and latest activity dates
- post-event pressure decay

The Event 33 GUI displays lifetime actual additions. The Air Cleanliness source details display the source ledger values.

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

### Current source pressure

Increase the source pressure estimate by actual Event 33 additions. While active, allow a small monthly pressure decay only if the event is in a weak regional state. After acute dissipation, decay the pressure estimate by a constant monthly amount until zero. This pressure decay does not directly subtract global Air Contamination. Global recovery remains owned by the normal Air Cleanliness system.

Clamp displayed current Event 33 pressure to the current global contamination value when required by the source-ledger presentation contract.

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

The integration should read a shared protection score or documented component API. It must not count the same stockpile twice or create a second competing mask inventory.

Event 33 permanent projects represent broad civilian infrastructure and organization. Existing CBRN assets can improve their effectiveness or reduce urgent-action costs. They do not automatically grant four Event 33 project tiers.

## Humanitarian integration

Use existing source-owned registration for:

- disaster pressure from tier-2 or tier-3 aftermath
- infrastructure and supply pressure
- contaminated-water pressure when qualified
- displacement pressure from major evacuation
- famine or disease risk when shared systems accept the state conditions

Event 33 owns only its source registration and removal. The Humanitarian system owns aid, refugee, famine, disease, and secondary crisis behavior.

Source IDs must distinguish Event 33 from Event 13 and Air Winter pressure so one cleanup cannot remove another event's burden.

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

## Famine, disease, and migration hooks

Event 33 can increase conditions that the shared systems already evaluate:

- contaminated food and water
- isolated supply routes
- damaged infrastructure
- displacement from severe evacuation
- prolonged global exposure

The implementation should register those pressures and let their owners resolve outcomes. Do not hard-code a second famine, disease, or migration engine inside Event 33.

## Current prototype removal

The existing prototype contains:

- `events/033_acid_rain.txt`
- `common/scripted_effects/033_acid_rain_effects.txt`
- `common/decisions/033_acid_rain_decisions.txt`
- `common/decisions/categories/033_acid_rain_categories.txt`
- `common/dynamic_modifiers/033_acid_rain_dynamic_modifiers.txt`
- `common/on_actions/033_acid_rain_on_actions.txt`
- `common/scripted_guis/033_acid_rain_scripted_guis.txt`
- `localisation/english/033_acid_rain_l_english.yml`
- prototype bindings in `interface/chaosx_decisions.gui`

Replace the runtime. Do not extend the daily nested country and owned-state scan.

Remove or migrate:

- old `acid_rain` global flag
- old continent variable and continent array
- old acid-cloud timer values
- old `chaosx_acid_rain_timeout` mission
- old `chaosx_acid_clouds_timeout` mission
- old `acid_clouds_state` and `acid_rain_state` prototype modifiers
- old one-image-per-continent GUI state
- prototype localisation that claims deaths without any real state-population removal
- any interpretation of `local_manpower` or recruitable-population penalties as civilian deaths

## Old-save migration

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

Implementation completion updates:

- event catalog workbook source
- cluster catalog workbook source
- Event 33 system documentation
- event-system type documentation
- event-cluster documentation
- Air Contamination source-ledger documentation
- Deaths cause documentation if a new cause is added
- super-event and audio catalogue
- asset manifest
- achievement registry documentation
- generated API documentation if new public helpers are introduced
