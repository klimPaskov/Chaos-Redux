# Subagent Execution Order

## Operating rule

All project custom subagents use `fork_context=false`. Every prompt must contain the system slug, paths, accepted source package, current implementation commit, exact tranche, user constraints, previous handoff disposition, permitted write scope, and the allocated scenario id after it has been verified.

The parent agent remains responsible for integration and completion claims.

## Tranche 0

### Documentation curator

Use after local source inspection.

Prompt scope:

- reconcile expanded source pack, current docs, current internal event and scenario ids, and live code behavior
- create source-of-truth map
- mark stale docs and old prompts
- record plan dispositions

Allowed writes:

- documentation and plan files only

### Scripted system architect

Use after engine proof tasks.

Prompt scope:

- propose Air Winter helper map
- propose Fallout request and transition helper map
- propose constants and lifecycle
- identify duplicated current Air logic
- define cleanup and migration

Allowed writes:

- narrow helper architecture plan first
- no gameplay patch until parent accepts the helper map

## Tranche 1

### Scripted system architect

Prompt scope:

- implement or audit state phase helpers, constants, triggers, aggregation, and mapmode support logic
- keep one monthly state pass
- document helpers and call sites

Required handoff:

- files changed
- helpers
- constants
- lifecycle
- mapmode call sites
- validation

### Documentation curator

Update current-state ledger and Air docs after parent integration.

## Tranche 2

### Decision and mission auditor

Prompt scope:

- winter response category
- costs beyond political power
- state targeting
- mission timing
- cleanup
- AI
- exploit risk

It may patch small local decision defects.

### Localisation auditor

Prompt scope:

- phase names and descriptions
- mapmode tooltip
- decision requirements
- dynamic values
- treaty text
- no generic apocalypse prose

It may patch local text and dynamic localisation defects.

### Scripted system architect

Recheck treaty caching, building damage, category damage, and shared Deaths calls.

## Tranches 3 and 4

### Scripted system architect

Prompt scope:

- Fallout request coordinator
- state machine
- event targets
- batch cursors
- abort and recovery
- player reservation
- diplomacy cleanup helper boundaries

### Country package auditor

Prompt scope:

- rewrite foundation
- tag and state validity
- capital and controller safety
- player continuity
- minimal internal test package validity

Do not ask this subagent to create new countries from scratch.

### Documentation curator

Reconcile old normal super-event documentation and record the new transition source of truth.

### Completion auditor

Audit only the implemented transition and rewrite foundation. Do not treat missing regional country content as a defect before its planned tranche, but record any foundation that would prevent later content.

## Tranche 5

### Decision and mission auditor

Prompt scope:

- scenario registry lifecycle
- confirmation and launch gate
- intensity behavior
- countdown cleanup
- duplicate launch protection

### Completion auditor

Compare the allocated manual Fallout scenario against exact province sweep, seven-day delay, blackout, and rewrite requirements.

## Tranche 6 and each regional wave

### Country package auditor

One bounded region or package group per prompt.

Provide:

- selected matrix rows
- source tags
- state groups
- leaders
- assets
- focus ids
- exact package status

Audit and patch only small local defects.

### Focus tree auditor

One bounded archetype or region per prompt.

Audit:

- archetype branch
- regional overlay
- country memory branch
- branch depth
- AI
- icons
- decisions
- route locks
- reward impact

### Decision and mission auditor

Audit country survival, expansion, reconstruction, and faction decision families.

### Localisation auditor

Audit country identity, focus, decision, tooltip, and scripted localisation.

### Asset subagents

Route by asset type:

- sourced real leaders and historical flags to `chaosx_asset_source_researcher`
- fictional flags, portraits, report art, and UI art to `chaosx_generated_event_art`
- focus, idea, decision, achievement, and small animated icons to `chaosx_icon_artist`

Every asset prompt includes exact names, sizes, source mode, final paths, sprite names, and blocked conditions.

## Finalization

### Spreadsheet worker

Use only after final in-game wording exists.

Prompt scope:

- event and scenario catalog rows
- exact player-facing mirror fields
- implementation status
- no invented wording

### Documentation curator

Create final source-of-truth map, plan disposition table, and resume or completion packet.

### Event completion auditor

Compare:

- all accepted specs
- all accepted addenda
- implementation
- assets
- localisation
- AI
- docs
- spreadsheet
- validation evidence

### Improvement-loop planner

Use only when a new implemented layer exposes a large design gap not covered by the accepted source pack. Do not create another addendum while a previous one remains unresolved.

At near completion, request closure. Additional broad expansion is not automatically useful because the source pack already received a manual closure pass.

## Handoff folder

All implementation subagent handoffs belong under:

`docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/`

Each patch handoff lists:

- files changed
- identifiers
- behavior before and after
- meaningful validation
- skipped validation and reason
- remaining risks
- parent follow-up
