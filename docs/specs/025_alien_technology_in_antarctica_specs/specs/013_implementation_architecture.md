# Implementation architecture

## Architecture purpose

Event 025 is one event-owned system with shared adapters for technology grants, event logs, global presentation, and consequences.

It should not duplicate the Event 016 technology system, Event 036 alien reward logic, shared Deaths ledger, shared event log, shared super-event framework, or generic decision utilities.

## Expected file map

The live repository decides exact filenames after inspection. The intended ownership is:

```text
events/025_alien_technology_in_antarctica.txt
common/decisions/025_alien_technology_in_antarctica_decisions.txt
common/decisions/categories/025_alien_technology_in_antarctica_categories.txt
common/ideas/025_alien_technology_in_antarctica_ideas.txt
common/dynamic_modifiers/025_alien_technology_in_antarctica_dynamic_modifiers.txt
common/script_constants/025_alien_technology_in_antarctica_constants.txt
common/scripted_effects/025_alien_technology_in_antarctica_effects.txt
common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt
common/on_actions/025_alien_technology_in_antarctica_on_actions.txt
common/scripted_guis/025_alien_technology_in_antarctica_scripted_guis.txt
interface/025_alien_technology_in_antarctica.gui
interface/025_alien_technology_in_antarctica.gfx
localisation/english/025_alien_technology_in_antarctica_l_english.yml
common/scripted_localisation/025_alien_technology_in_antarctica_scripted_localisation.txt
docs/events/025_alien_technology_in_antarctica/
```

Shared files are touched only for registration, generic adapters, Event Details, super-event slot mapping, achievements, and catalog alignment.

## Event ID plan

Canonical entry:

- `chaosx.nr25.1`

Suggested event families:

| Range | Role |
| --- | --- |
| `.1` | Global major-event entry and initialization |
| `.2` to `.9` | Human invitation, observer response, entry closure |
| `.10` to `.29` | Mobilization and route incidents |
| `.30` to `.49` | Crossing and outpost incidents |
| `.50` to `.79` | Survey, fragment, intelligence, and rescue reports |
| `.80` to `.99` | Final recovery and winner resolution |
| `.100` to `.129` | Evolution I incidents |
| `.130` to `.159` | Evolution II incidents |
| `.160` to `.189` | Evolution III incidents |
| `.190` to `.219` | Evolution IV incidents |
| `.220` to `.259` | Evolution V and aftermath incidents |
| `.260` to `.279` | Event 036 arbitration and cross-event reports |
| `.280` to `.299` | Cleanup, invalidation, and hidden maintenance events |

The implementation may adjust ranges after checking existing IDs. It must keep the event namespace coherent and documented.

## Registration

The implementation must update the major-event category array in `initialize_event_categories` or the current live equivalent.

Required registration work:

- Event 25 in the major-event array
- Event 25 name selectors
- debug name selectors
- Event Details row
- default enabled allowlist only after full implementation is ready
- event-list validity and `N/A` state when no valid setup can be built
- super-event mapping
- achievement registry

Event 25 remains outside active cluster membership.

## Initialization flow

The entry event performs one bounded initialization transaction.

Required order:

1. validate that no active Event 025 race exists
2. create the global race identity and phase
3. initialize participant arrays and sequence counter
4. count and invite every current human-controlled country
5. score and select the bounded AI roster
6. initialize crash-sector hidden state
7. initialize evolution state that applies at first firing
8. initialize shared Event 016 and Event 036 reward ledger adapters
9. show the opening super-event
10. send participant or observer entry events
11. schedule the bounded entry-window closure

No participant should act before its country ledger is initialized.

## Participant registry

Use aligned global arrays or the current shared bounded-registry pattern.

Required participant fields:

- stable participant country scope or UID
- participant sequence
- human or AI
- active, withdrawn, invalid, or resolved state
- entry secrecy state
- route family
- gateway group
- current phase
- Expedition Progress
- Logistics Readiness
- Exposure Risk or Dependence
- outpost state
- outpost integrity
- survey certainty
- fragment ownership count and category proof
- current mission family
- next pulse date or scheduled pulse state
- posture for AI
- public incident state

Arrays must remain aligned after withdrawal and invalidation. Prefer marking inactive entries over removing rows while an active loop may hold an index.

## Country-owned state

Country-scoped flags and variables are appropriate for private expedition values and GUI access.

Suggested public naming follows the event-owned context without unnecessary project prefixes:

- `antarctic_expedition_participant`
- `antarctic_expedition_observer`
- `antarctic_expedition_phase`
- `antarctic_expedition_progress`
- `antarctic_logistics_readiness`
- `antarctic_exposure_risk`
- `antarctic_alien_dependence`
- `antarctic_route_family`
- `antarctic_gateway_group`
- `antarctic_outpost_state`
- `antarctic_outpost_integrity`
- `antarctic_survey_certainty`
- `antarctic_selected_rival_id`
- `antarctic_fragment_*`
- `antarctic_hostile_action_*`

Final names should match live repository conventions and avoid collisions.

## Global state

Suggested global concepts:

- race active
- current global phase
- primary core claimed
- winner
- participant count
- active participant count
- crash-sector weights and selected primary sector
- evolution unlock and recorded state
- first outpost report sent
- first fragment report sent
- first public clash report sent
- global repeated-alien-recovery count

Use flags for boolean state and variables for counts or enums.

## Event targets

Use regular event targets for one effect chain and global event targets only when persistent scope storage is necessary.

Likely persistent targets:

- current winner during resolution and report sequence
- selected rival for a human GUI only when a country ID variable is insufficient
- current fragment transfer recipient during a bounded transfer chain

Every global target needs explicit cleanup.

Do not use one global selected rival for all players.

## Constants

Centralize tuning in script constants.

Required groups:

- participant caps
- pulse interval bands
- entry window duration
- route burden values
- gateway modifiers
- visible value floors and caps
- phase thresholds
- survey and fragment gains
- mission durations
- action cooldowns
- costs and reserve floors
- AI participation factors
- AI action factors
- evolution MTTH and modifiers
- casualty bands
- opinion and tension effects
- reward tier thresholds
- Dependence thresholds and accident factors

Do not scatter duplicate magic numbers across events, decisions, GUI, and AI.

Duration fields that reject constants should receive a variable assigned from the constant before use, or use the verified local engine pattern.

## Bounded pulse model

The event needs a scheduled pulse to progress active expeditions and AI choices.

The pulse must iterate only over the stored participant registry.

Preferred cadence:

- every 10 to 15 days during the active race
- slower or event-driven aftermath updates after resolution

The pulse handles:

- mission and route state refresh
- bounded passive progress or decay
- weather and incident opportunities
- AI action selection
- invalid participant cleanup
- race-resolution checks
- evolution pacing checks

It must not use `on_daily`, `on_weekly`, or `on_monthly` over every country.

An event-owned scheduled event or narrow on-action is preferred.

## Randomness model

Randomness should choose among valid outcomes after deterministic eligibility is built.

Examples:

- crash sector
- weather setback
- survivor profile
- fragment category
- incident severity
- Event 016 technology reward

Every pool must fail closed when empty. Do not substitute a different family merely because one target became invalid unless the spec defines that fallback.

## Dynamic helper families

### Participant helpers

- initialize country ledger
- register participant
- mark withdrawn
- invalidate participant
- rebuild active participant view
- resolve country from participant UID

### Value helpers

- change progress with clamp
- change readiness with clamp
- change exposure with clamp
- change dependence with clamp
- refresh idea or dynamic modifier state

### Route helpers

- evaluate gateway access
- calculate route burden
- debit route commitment
- interrupt route
- restore route

### Mission helpers

- launch mission
- resolve success
- resolve partial success
- resolve failure
- cancel active mission

### Rival helpers

- select rival
- validate selected rival
- apply evidence state
- pay hostile action
- apply defense
- clear stale target

### Fragment helpers

- grant category
- transfer category
- remove category
- calculate fragment tier
- rebuild fragment display

### Winner helpers

- evaluate final recovery validity
- compare same-day finalists
- declare winner once
- apply winner reward
- apply losing rewards
- close race

### Aftermath helpers

- select policy
- refresh Dependence state
- schedule accident
- contain
- transfer custody
- destroy or seal material

## Shared Event 016 helper extension

The implementation should inspect the current external technology helpers.

When the existing random base helper can return an empty result, add one reusable duplicate-safe helper in the Event 016 or shared custom-technology owner file.

It must not be implemented as an Event 025 private copy.

The helper needs documented inputs, outputs, defaults, side effects, and examples in `chaosx_dynamic_effects.md` or the current owner documentation.

## Event 036 shared ledger

Use a small shared scripted helper family owned by the alien-recovery integration layer.

Required contracts:

- record Event 025 field and tier
- record Event 036 aircraft tier
- test exact overlap
- select upgrade conversion
- record conversion used
- return broad public field for localisation

The shared ledger should not depend on Event 036 being implemented at the time Event 025 is completed. Unknown or unavailable Event 036 state resolves safely.

## Decisions and missions

All event-owned categories belong in the Event 025 decision files.

The ordinary decision category contains:

- board entry action
- urgent mission indicators
- observer or withdrawal status where needed

Most active actions are presented on the board and call the same scripted effects used by AI.

Action costs use no more than four spendable types.

## Ideas and dynamic modifiers

Use few staged ideas.

Likely ideas:

- Expedition Commitment, temporary and removed after closure
- Alien Recovery Program lifecycle, winner only
- Alien Systems Integration capstone, rare

Route burden, outpost state, and Dependence may fit dynamic modifiers when the player needs visible combined effects.

Do not create one permanent idea for every phase or fragment.

## Evolution architecture

Each evolution has:

- global enabled check
- minimum Chaos tier
- eligibility state
- MTTH or first-firing entry
- one recorded milestone
- behavior flag
- event-log context
- clean disabled path

Entry during an active race must preserve ordinary phase and country ledgers.

Entry before Event 25 fires changes initialization and opening intensity.

Evolution V may create country-specific Dependence progression after the global evolution milestone. Those country stages are ordinary aftermath progression unless a later stage is deliberately registered as another evolution type.

## Event log integration

History:

- one Event 25 opening row
- no row for every participant action

Evolution log:

- one row per enabled evolution milestone
- actor only when the recorded milestone belongs to one country

Event Details:

- premise
- current public phase
- participant count
- public evolution state
- winner after resolution

Name mappings and actor sanitizing follow the shared Event Logs owner file.

## Super-event architecture

The opening uses an unused verified slot.

Implementation requirements:

- visibility flag
- image selector
- title, description, quote, and button selectors
- unique audio ID
- settings-aware volume wrappers
- `play_current_super_event_sound = yes`
- cleanup or close behavior

Do not choose a slot before inspecting the live registry.

## Achievements

Use the single root achievement registry.

Keep Event 025 achievements grouped together with stable IDs. Add tracking flags and counters in event-owned helpers. Keep binary asset paths in the engine-required achievement root.

## GUI architecture

The board is an event-owned independent window with a participant-country context.

Button triggers and effects call named event-owned helpers. Decorative layers remain transparent to input.

The GUI worker owns layout, state presentation, click regions, and MCP evidence. The parent owns costs, effects, AI, balance, and final integration.

## Localisation architecture

Expected surfaces:

- event localisation
- decision and mission localisation
- board localisation
- scripted localisation for values, phases, selected rivals, sectors, fragment fields, and reward fields
- Event Details localisation
- event name and debug mappings
- achievement localisation
- super-event localisation

All English localisation uses UTF-8 with BOM according to repository rules.

## Asset architecture

Non-portrait assets use event-scoped folders.

The asset workers create source, PNG, DDS, contact sheet, manifest, and handoff outputs. The parent wires non-portrait sprites and runtime consumers.

No runtime file points into `docs/assets/`.

## Invalidation and cleanup

The cleanup helper must cover:

- country deletion or annexation
- withdrawal
- route invalidation
- participant capitulation
- winner resolution
- all-participant failure
- evolution disable state
- external terminal state
- save reload

It must:

- cancel missions
- clear selected rivals
- release temporary commitments
- remove obsolete decisions
- preserve historical and achievement state
- preserve fragment ownership where appropriate
- avoid repeated reward application

## Documentation and catalog

Implementation updates:

- event doc
- system doc for Expedition Board and reward arbitration
- asset provenance and crosswalk
- super-event research note
- achievement doc
- Event 016 shared-helper documentation when extended
- Event 036 integration documentation
- authoritative event-catalog XLSX

After workbook update run the repository exporter. Do not edit CSV snapshots directly.

## MCP requirements

Event chain:

- `hoi4.event_inspect`
- `hoi4.event_render`
- `hoi4.event_compare`

GUI:

- `hoi4.gui_inspect`
- `hoi4.gui_render`
- `hoi4.gui_rewrite`
- post-change compare

Technology:

- `hoi4.tech_inspect`
- `hoi4.tech_render`
- `hoi4.tech_compare`

Probability:

- `hoi4.probability_inspect`
- scenario evaluation
- baseline and post-patch compare
- timing or sensitivity render when useful

Missing MCP routes remain explicit blockers for the affected evidence. Source-only review is not equivalent.

## Repository and vanilla references

Before source implementation the agent must inspect:

- required offline Paradox wiki pages
- relevant vanilla documentation
- vanilla event, decision, GUI, special-project, technology, and super-event precedents
- existing Chaos Redux major events
- existing bounded registries
- Event 016 custom technology owner files
- Event 036 current files or reservation state
- current super-event slots
- current GUI window patterns

The planning package cannot substitute for those local engine references.
