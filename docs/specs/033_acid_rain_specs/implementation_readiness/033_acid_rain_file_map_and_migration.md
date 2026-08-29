# Event 033 Acid Rain file map and implementation handoff

## Repository context

The current repository already contains a prototype Event 33 implementation. It selects one of seven regions, applies a broad cloud modifier, applies an acute rain modifier to one random state and neighbors, advances through timeout missions, and runs a daily country and owned-state damage scan.

The rework replaces that runtime. Existing namespace and asset identifiers can be retained only after collision and reference inspection.

## Proposed file ownership

### Core script

| Path | Responsibility |
| --- | --- |
| `common/script_constants/033_acid_rain_constants.txt` | All timing, chance, mortality, damage, cost, cap, and Chaos values |
| `common/scripted_triggers/033_acid_rain_triggers.txt` | Eligibility, region mapping, project affordability, front state, exposure, and achievement predicates |
| `common/scripted_effects/033_acid_rain_effects.txt` | Initialization, registry, fronts, coverage, exact state-population transactions, pulses, contamination, control transfer, dissipation, cleanup, and migration |
| `common/dynamic_modifiers/033_acid_rain_dynamic_modifiers.txt` | Acute bands, severe cells, global layer, aftermath tiers, emergency and recovery modifiers |
| `events/033_acid_rain.txt` | Formation dispatcher and bounded visible reports |

### Decisions and interface

| Path | Responsibility |
| --- | --- |
| `common/decisions/categories/033_acid_rain_categories.txt` | Category visibility, picture selection, and phase container |
| `common/decisions/033_acid_rain_decisions.txt` | Four permanent projects, urgent actions, evacuations, recovery, and AI |
| `common/scripted_guis/033_acid_rain_scripted_guis.txt` | Read-only GUI data binding and safe controls |
| `interface/033_acid_rain.gui` | Dedicated window layout |
| `interface/033_acid_rain.gfx` | Event-specific sprites and frame sequences |
| `localisation/english/033_acid_rain_l_english.yml` | Final audited localization |

### Shared-system edits

| Surface | Required edit |
| --- | --- |
| Major event registry | Add 33, remove repeatable registration |
| Event availability | Chaos level 2 and validity trigger |
| Evolution registry | Add three cumulative stages |
| Event Details | Add type, cluster, stage, counters, history, achievements |
| Natural Disasters cluster | Add sixth member and mixed Major pacing |
| Air Contamination source ledger | Add Acid Rain source and display row |
| Deaths cause ledger | Add dedicated cause only if layout and API accept it |
| Humanitarian source registry | Add Event 33 source identifiers |
| CBRN civilian protection | Expose or consume documented shared score |
| Achievements | Register ten Event 33 achievements |
| Super-event registry | Register formation presentation and sound |
| Audio catalogue | Add final source and converted paths |
| Asset manifest | Register every source and DDS output |

## Suggested internal helper groups

### Registry and schema

- prepare schema
- build eligible states
- map state to stable region
- initialize countries
- initialize front slots
- reconcile active save
- cleanup stale prototype state

### Front operations

- enter region
- choose visit quota
- build footprint
- drift footprint
- select next region
- reveal warning
- move front
- split front
- close front slot

### Exposure operations

- begin ordinary episode
- apply ordinary opening and sustained loss
- apply severe opening and sustained loss
- apply global transition and sustained loss
- add building pressure
- spend building pressure
- update acute modifier
- close acute exposure and calculate aftermath

### Air operations

- calculate weekly request
- clamp lifetime and ceiling
- apply central delta
- record actual addition
- update source pressure

### National operations

- recalculate Preparedness
- calculate cost band
- debit and record commitment
- complete or cancel project
- refresh urgent actions
- migrate state responsibility
- close national category

### History and acceptance

- append event history
- record evolution activation
- record direct Chaos receipt
- update achievements
- dispatch cooldown reports
- close event history

Final helper names should follow repository conventions. Public helpers need documented input, scope, output, and cleanup contracts.

## Implementation order

### Work package 1, source and registry

- align workbook source and docs
- register Event 33 as Major level 2
- add constants and schema
- build region and state eligibility tests

Exit proof:

- event can build and print the frozen registry without starting weather
- every valid state maps once

### Work package 2, one-front engine

- front slot 1
- initial footprint
- drift
- warning
- movement
- exact coverage
- correction and dissipation ladder

Exit proof:

- observer test reaches every state and closes without damage systems

### Work package 3, losses and aftermath

- exposure episodes and receipts
- exact state population removal through `apply_exact_state_civilian_population_loss`
- proof that pre-pulse population minus post-pulse population equals the helper's applied loss
- Deaths registration and Event 33 counters using the same applied loss
- explicit rejection of `local_manpower` or recruitable-population modifiers as mortality
- building pressure
- acute and aftermath modifiers
- control transfer

Exit proof:

- totals reconcile after save, reload, and state transfer

### Work package 4, national actions

- Preparedness components
- cost bands and commitment ledger
- permanent projects
- urgent actions and evacuation
- recovery actions
- AI rules

Exit proof:

- exact-cost and one-below-cost tests pass for every variant

### Work package 5, Air Cleanliness

- dedicated source ID
- central clamp path
- GUI lifetime counter
- post-event pressure decay

Exit proof:

- randomized cap suite has zero violation

### Work package 6, evolutions

- Severe Storm Cells
- Multiple Weather Fronts
- Global Acid Rain

Exit proof:

- each stage works from pre-fire and active-transition entry
- each stage survives reload

### Work package 7, presentation

- reports
- custom GUI
- frame animations
- super-event image and audio
- localization

Exit proof:

- three resolutions, multiplayer, source, and license checks pass

### Work package 8, cluster and history

- sixth Natural Disasters member
- mixed Major pacing
- reservation and cancellation
- Event Details and achievements

Exit proof:

- independent and cluster firing pass without double pacing

### Work package 9, migration and final audit

- prototype active and completed migrations
- remove daily on-action
- documentation and catalog export
- completion and improvement-loop audits

Exit proof:

- all Part 12 gates pass

## Prototype replacement details

### Replace entirely

- daily Event 33 on-action damage scan
- old timeout missions
- old continent completion array as endpoint
- old random state plus neighbors footprint
- old mortality claims that do not remove state population
- any use of `local_manpower` or recruitable-population penalties as a death implementation
- old one-region GUI swap
- old repeatable registration

### Preserve only after audit

- `chaosx.nr33` namespace
- existing report or news image if art review accepts it
- localization key roots that do not encode old behavior
- event ID and any stable external reference to Event 33

## Migration transaction

Implement migration before deleting old variable reads.

1. detect old state and new schema absence
2. store old current region and completion facts
3. build new registry
4. migrate acute states from old acute modifier
5. migrate visited-region history separately
6. create new one-front state or preserve completed status
7. write migration receipt
8. remove old missions, flags, arrays, and modifiers
9. disable old on-action path
10. save and reload test

After one stable release and documented compatibility policy, old migration reads can be archived in a later cleanup. Do not remove them in the same change that first introduces migration.

## Tool requirements

Implementation must use:

- repository search and reference tracing before editing shared registries
- scripted-system architecture review
- decision and mission audit
- probability inspection for every weighted list
- AI probability auditor
- GUI inspection at supported resolutions
- frame-animation validation
- generated-art validation
- localization audit
- debug and playtest skill
- event completion audit
- documentation curator
- improvement-loop planner near completion

## Handoff evidence

The final implementation handoff should contain:

- changed-file list
- new and removed helper list
- registry and ID map
- balance constant diff
- probability reports
- performance profile
- save migration evidence
- exact-cost test evidence
- Air cap test evidence
- GUI screenshots at three resolutions
- asset manifest
- quote and audio source record
- achievement test record
- catalog export validation
- open issue list with severity
