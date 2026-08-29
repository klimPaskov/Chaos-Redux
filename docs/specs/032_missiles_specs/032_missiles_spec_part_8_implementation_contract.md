# Event 32 specification, part 8: Implementation contract

## Implementation ownership

Event 32 should use event-owned files for its private runtime and shared files only for established framework integration.

Recommended event-owned files:

- `events/032_missile_crisis.txt`
- `common/script_constants/032_missiles_constants.txt`
- `common/scripted_effects/032_missiles_effects.txt`
- `common/scripted_triggers/032_missiles_triggers.txt`
- `common/on_actions/032_missiles_on_actions.txt` only for narrow exact hooks
- `common/ideas/032_missiles_ideas.txt`
- `common/dynamic_modifiers/032_missiles_dynamic_modifiers.txt`
- `common/decisions/032_missiles_decisions.txt`
- `common/decisions/categories/032_missiles_categories.txt`
- `common/raids/032_missiles_raids.txt` when the native raid adapter is used
- `common/opinion_modifiers/032_missiles_opinion_modifiers.txt`
- event-owned GFX files
- event-owned localisation files
- `docs/events/032_missiles.md`

Shared framework touchpoints include:

- random-event category registration
- reworked-event default enable allowlist
- event name and debug selectors
- Event Logs history and Event Details
- evolution log catalog and selectors
- triggerable scenario registry
- shared CBRN consequence adapters
- shared Deaths reason enum or adapter
- shared dynamic effect or trigger registry only when the helper becomes genuinely reusable
- authoritative event catalog workbook

## Namespace and IDs

Keep:

- namespace `chaosx.nr32`
- entry event `chaosx.nr32.1`

The current country report ID `chaosx.nr32.2` can remain the first-recipient report.

Allocate stable subevent ranges before implementation.

Recommended ranges:

| Range | Use |
| --- | --- |
| `.1` to `.9` | entry, reports, first news bridge |
| `.10` to `.29` | baseline setup and repeat reports |
| `.30` to `.49` | strike results and accidents |
| `.50` to `.69` | Saturation and Unreliable reports |
| `.70` to `.89` | Special Warheads reports |
| `.90` to `.119` | Rogue Launch Commands incidents |
| `.120` to `.149` | Automatic Retaliation warnings and chain results |
| `.150` to `.169` | capture, civil war, succession, and cleanup |
| `.170` to `.189` | scenario result and setup failure |
| `.190` to `.199` | debug-only or reserved |

The final mapping can differ, but it must be documented and collision-free.

## Core scripted APIs

### Recipient validation

Recommended trigger:

`missiles_is_valid_recipient`

Inputs:

- current country scope

Outputs:

- boolean
- stable reject reason through a temporary result when called from setup

The trigger should delegate special-country profile checks to narrow helpers.

### Program initialization

Recommended effect:

`missiles_initialize_or_advance_program`

Inputs:

- current country
- firing context
- first or repeat flag
- scenario context
- package scale

Outputs:

- accepted result
- normalized technology stage
- reserve delta
- site result
- report type
- debug receipt

Side effects:

- changes one country only
- creates or advances program
- does not record the global Event 32 history row

### Technology adapter

Recommended effect family:

- `missiles_normalize_technology_stage`
- `missiles_grant_next_technology_step`
- `missiles_apply_mature_program_package`

The technology adapter must be isolated from reserve, site, and report code.

### Reserve helpers

Recommended effect and trigger family:

- `missiles_add_reserve`
- `missiles_remove_reserve`
- `missiles_can_pay_reserve`
- `missiles_reserve_operation_missiles`
- `missiles_refund_operation_missiles`
- `missiles_transfer_captured_reserve`
- `missiles_destroy_reserve`

Every transaction returns the exact applied amount.

### Site helpers

Recommended family:

- `missiles_build_site_candidate_pool`
- `missiles_score_site_candidate`
- `missiles_select_site`
- `missiles_create_site`
- `missiles_upgrade_site`
- `missiles_damage_site`
- `missiles_repair_site`
- `missiles_capture_site`
- `missiles_scuttle_site`
- `missiles_cleanup_site`
- `missiles_refresh_site_modifier`

### Operation helpers

Recommended family:

- `missiles_preflight_operation`
- `missiles_create_operation_receipt`
- `missiles_reserve_operation_resources`
- `missiles_commit_operation`
- `missiles_abort_operation`
- `missiles_resolve_operation`
- `missiles_cleanup_operation`

### Damage helpers

Recommended family:

- `missiles_calculate_conventional_damage`
- `missiles_apply_conventional_damage`
- `missiles_calculate_civilian_loss`
- `missiles_register_incident_deaths`
- `missiles_apply_site_target_damage`

Special payloads call shared owning-system effects.

### Incident helpers

Recommended family:

- `missiles_allocate_incident_id`
- `missiles_record_incident`
- `missiles_close_incident`
- `missiles_create_warning`
- `missiles_process_warning`
- `missiles_can_add_retaliation_generation`
- `missiles_link_retaliation_incident`
- `missiles_close_root_chain`

### Succession helpers

Recommended family:

- `missiles_preflight_country_split`
- `missiles_split_program_after_civil_war`
- `missiles_transfer_inherited_site`
- `missiles_cleanup_removed_country`

These helpers require frozen state and country packages from the caller.

## Constants

All tuning belongs in `common/script_constants/032_missiles_constants.txt` or a clearly justified shared tuning file.

Recommended constant groups:

- program stage IDs
- recipient profile IDs
- reserve package values
- reserve caps
- readiness bands
- command-control bands
- guidance factors
- site levels
- site capacity
- site hardening
- site security
- site count thresholds
- site scoring
- operation profile IDs
- target profile IDs
- payload IDs
- preparation duration
- cooldowns
- reserve costs
- readiness costs
- command-control costs
- conventional damage
- death scaling
- evolution IDs
- evolution MTTH
- evolution threshold factors
- rogue incident IDs
- warning states
- retaliation posture IDs
- chain caps
- scenario profile IDs
- scenario intensity scaling
- AI profile IDs
- AI weights
- chaos deltas
- log type IDs
- stable reject reasons

Do not use file-scoped `@` constants for values consumed across event, decision, trigger, effect, localisation, and scenario files.

## Flags and variables

Use flags for true or false state.

Potential country flags:

- program initialized
- first report seen
- mature line reached
- saturation adopted
- payload integration flags
- site crisis active
- rogue crisis active
- warning active
- scenario origin
- achievement disqualifiers

Potential country variables:

- normalized stage
- reserve
- reserved reserve
- readiness
- command control
- active site count
- current operation ID
- current incident ID
- selected target ID
- retaliation posture
- root warning ID
- AI profile

Potential state variables:

- site owner ID
- site level
- capacity
- hardening
- security
- damage
- local reserve share or capture estimate
- operation ID
- incident ID

Use temporary variables for one-call calculations. Do not scope temporary variables with `ROOT.` or `PREV.`.

## Event targets and persistent records

Regular event targets are suitable for one immediate report chain.

Persistent concurrent operations, sites, and retaliation incidents should use:

- numeric country IDs
- state IDs
- arrays
- variables
- stable incident IDs
- global event targets only when one unique pointer is sufficient and cleanup is guaranteed

Do not reuse one global event target for several simultaneous operations.

Every global event target must have a named cleanup point.

## Event dispatch

The global entry can use a one-time country loop because Event 32 explicitly affects every valid existing country.

It must not add:

- `on_daily`
- `on_weekly`
- `on_monthly`
- another recurring all-country on-action

without separate user approval.

The setup can be split into delayed deterministic chunks if required. The final result must remain atomic at the Event 32 history and repeatable-weight level.

## Prepared operation state machine

Recommended states:

1. none
2. selecting
3. resources reserved
4. preparing
5. ready
6. committed
7. resolving
8. completed
9. aborted
10. invalidated

Every state transition has:

- one entry effect
- one exit effect
- resource rule
- site receipt rule
- target validity rule
- visible decision set
- cleanup rule

The implementation must reject impossible transitions.

## Incident state machine

Recommended states:

1. created
2. evidence pending
3. warning active
4. response preparing
5. response committed
6. consequences applied
7. closed

Rogue incidents may use an additional crisis state, but they should still close through the shared incident cleanup.

## Evolution runtime

Each evolution needs:

- global unlock flag
- enabled gate
- eligibility trigger
- pending-job flag
- MTTH or delayed evaluation
- recorded flag
- evolution context
- log call
- behavior helper
- cleanup or disable behavior

Disabled evolutions must not set pending or recorded flags.

When an evolution is disabled after it was active, the project-wide toggle contract should decide whether existing state is suspended or retained. Event 32 should follow the current evolution-toggle precedent and document the result.

## Native raid adapter

Before implementation:

- inspect installed raid documentation
- inspect at least one vanilla rocket-site or nuclear raid
- inspect current Chaos Redux CBRN raids
- verify starting-point behavior
- verify target-state and target-province variables
- verify equipment and nuke consumption
- verify AI availability
- verify DLC gates
- verify outcome effects
- verify map icons and visuals

The native adapter is accepted only when it can prove:

- exact launch state
- exact target state
- exact reserve receipt
- exact payload receipt
- exact outcome
- actor and victim
- cleanup
- AI route

## Scripted strike adapter

If native raids cannot satisfy parity, implement the scripted adapter as a full supported route.

It may use decisions and delayed events, but it must not become a weaker decorative substitute.

Required parity:

- target selection
- preparation
- reserve payment
- site capacity
- cooldown
- guidance failure
- damage
- deaths
- payload
- diplomacy
- AI
- logs
- incident chain

The adapter should expose the same operation API so later systems do not care which presentation route is active.

## Shared CBRN adapters

Before adding any new Event 32 payload helper, inspect existing chemical, biological, nuclear, thermonuclear, Condemnation, Air Cleanliness, and Deaths entry points.

If the exact reusable route exists, call it.

If a route is missing, add it to the owning shared system and document:

- purpose
- scope
- inputs
- outputs
- defaults
- side effects
- usage example

Do not put shared chemical exposure logic inside `032_missiles_effects.txt`.

## AI implementation

AI target and incident weights require:

- complete candidate pools
- centralized weights
- named scenarios
- baseline auditor pass
- owner patch
- `hoi4.probability_compare`
- final scenario evidence

AI decisions should use the same ability and payment triggers as player decisions.

The human selected-target variable must not block AI from seeing all valid targets.

## Localisation

Recommended files:

- `localisation/english/032_missiles_l_english.yml`
- `common/scripted_localisation/032_missiles_scripted_localisation.txt`
- shared event-name and Event Logs selectors
- shared scenario scripted localisation
- shared GUI localisation where the decision category needs labels

All visible text must be final implementation wording written from the direction in part 7.

Requirements:

- UTF-8 with BOM
- no `:0`
- no raw internal variable names
- no paste of specification labels without review
- dynamic target, state, reserve, readiness, control, payload, and posture text
- cost texticons
- precise blocked reasons
- concise value tooltips
- Event Details wording aligned with workbook

## GFX and assets

Register stable sprite names before final art production.

Recommended naming direction:

- `GFX_032_missiles_report`
- `GFX_032_missiles_news`
- `GFX_032_missiles_category_picture`
- event-owned decision, mission, idea, state-modifier, raid, texticon, and achievement names

Exact names should be recorded in the asset manifest and kept stable.

## Achievements

Achievements remain grouped under the root-only Chaos Redux achievement registry.

Implementation requires:

- stable IDs
- tracking flags and variables
- disqualifiers
- final localisation
- triplet icons
- docs
- route hooks
- scenario-origin rules
- full test cases

## Triggerable scenario

SCN-015 requires:

- constants
- registry entry
- sort value
- five profile types
- four intensity stops
- launch eligibility
- confirmation flow
- launch effect
- profile and intensity scripted localisation
- scenario result or failure report
- idempotence
- bypass cleanup
- docs
- workbook row
- CSV regeneration

The next public ID must be re-audited before source is patched.

## Event Logs

Required shared changes:

- event name mapping
- debug name mapping
- history details
- event-detail premise
- five evolution catalog rows
- five evolution name and detail selectors
- actor behavior
- enabled state
- fired count and weight display
- `N/A` when no valid recipient exists
- one history row per global firing

## Documentation

Required permanent documentation:

- `docs/events/032_missiles.md`
- API notes for any shared helper
- scenario documentation
- updated cross-event docs when a bridge changes
- asset coverage and provenance after temporary-workspace cleanup
- achievement list
- probability evidence references
- test matrix
- completion report

## Workbook

Update only:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Required Event 32 fields:

- final status
- chaos level
- event detail
- five evolution details
- cluster remains blank
- manual scenario reference if the workbook schema supports it
- implementation notes appropriate for player-facing fields

Required scenario fields:

- SCN-015 ID and name
- source event
- profile labels and details
- intensity details
- status

Then run:

`python .tools/export_event_catalog_csv.py`

Do not edit the exported CSV files directly.

## Migration from legacy Event 32

The current legacy source grants two technologies and two rocket-site levels.

Migration requirements:

- preserve namespace and entry ID
- preserve Event 16 reaction behavior
- replace capital-first and random-state site selection
- replace blanket two-tech grant with normalized one-step progression
- replace generic bomber picture with final Event 32 art
- replace generic country report text
- prevent old and new site logic from running together
- seed new program variables when an existing save-facing legacy site is detected only if the project supports migration
- document whether the rework requires a new campaign

The implementation agent must follow the repository rule on save compatibility and should not invent a silent migration that cannot be proven.

## Performance budget

The system should meet these design limits:

- one global recipient transaction per Event 32 firing
- no recurring global country scan
- one prepared operation per ordinary country by default
- one active rogue crisis per country
- one active warning per country per root incident
- global active-incident cap
- retaliation generation cap
- bounded drift-state pool
- bounded barrage failure rolls
- one-shot delayed recovery
- exact cleanup after country or state change
- no GUI polling beyond ordinary decision and scripted-localisation evaluation

## Required MCP evidence during implementation

### Event chain

- `hoi4.event_inspect`
- `hoi4.event_render`
- `hoi4.event_compare`

### Technology

- `hoi4.tech_inspect`
- `hoi4.tech_render`
- `hoi4.tech_compare`

### Probability

- `hoi4.probability_inspect`
- scenario-specific evaluate, sweep, simulation, comparison, and render

### GUI

A full event-owned scripted GUI is not planned. Use GUI tools only if implementation changes a shared category or target presentation that falls within their supported scope.

## Required subagent sequence

Recommended sequence:

1. parent and repository explorer map current source where needed
2. scripted-system architect reviews APIs, constants, receipts, and incident queue
3. parent implements baseline program and operation pipeline
4. decision and mission auditor reviews actions, costs, cleanup, and exploits
5. AI probability auditor establishes baseline scenarios
6. parent patches AI and weighted outcomes
7. AI probability auditor compares final source
8. asset workers create bounded art
9. localisation auditor reviews all visible text
10. spreadsheet worker updates the authoritative workbook
11. improvement-loop planner returns addendum or closure
12. parent resolves that result
13. event completion auditor compares full specs to implementation
14. parent writes concrete completion report

All project subagents use `fork_context=false`.

## Explicit implementation boundaries

Do not add any of these without a new accepted design:

- country package
- national focus tree
- faction
- formable nation
- leader or portrait
- flag
- custom unit
- custom 3D model
- animated sprite
- dedicated event-owned scripted GUI
- event-owned super event
- event-owned campaign terminal branch
- new chemical or biological agent
- free nuclear or thermonuclear stockpile
- generic all-country periodic scanner

These boundaries protect implementation depth from unnecessary expansion.
