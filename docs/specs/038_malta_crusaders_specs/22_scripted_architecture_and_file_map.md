# Scripted architecture and implementation file map

## Ownership principle

Event 38 owns its lifecycle, actors, state collections, values, orders, relics, principalities, routes, hidden transitions, and terminal orchestration.

Shared systems own global ledgers and reusable contracts. Event 38 calls their public APIs and publishes stable facts.

## Proposed source files

Exact names should follow current repository conventions after exploration.

### Events

```text
events/038_malta_crusaders_events.txt
```

Contains the `chaosx.nr38.*` namespace, player-facing events, reports, hidden events, and delayed handoffs. Large terminal or hidden event families can remain in the same namespace and split files only if current event loading permits a clean event-owned split.

### Script constants

```text
common/script_constants/038_malta_crusaders_constants.txt
```

Groups:

- event and scenario IDs
- value thresholds
- setup package levels
- force budget bands
- order IDs
- relic status IDs
- principality type IDs
- duration and cooldown bands
- AI tuning
- Chaos outcomes
- Holy World proof and pulse tuning
- Atlantis comparison and force tuning

Use `constant:category.key` where supported. Fields that reject constants use variables assigned from constants.

### Scripted triggers

Suggested files:

```text
common/scripted_triggers/038_malta_crusaders_triggers.txt
common/scripted_triggers/038_malta_crusaders_map_triggers.txt
common/scripted_triggers/038_malta_crusaders_unit_provider_triggers.txt
common/scripted_triggers/038_malta_crusaders_terminal_triggers.txt
```

Public trigger families:

- event availability
- Malta actor validity
- opening state validity
- package validity
- order and demand validity
- principality region and actor validity
- Papal supremacy
- continent proof
- Teutonic eligibility
- Atlantis eligibility
- scenario launch eligibility
- provider family eligibility
- player-facing custom trigger tooltips

Every trigger is read-only and fails closed when proof is incomplete.

### Scripted effects

Suggested files:

```text
common/scripted_effects/038_malta_crusaders_setup_effects.txt
common/scripted_effects/038_malta_crusaders_core_effects.txt
common/scripted_effects/038_malta_crusaders_order_effects.txt
common/scripted_effects/038_malta_crusaders_principality_effects.txt
common/scripted_effects/038_malta_crusaders_relic_effects.txt
common/scripted_effects/038_malta_crusaders_unit_provider_effects.txt
common/scripted_effects/038_malta_crusaders_hidden_route_effects.txt
common/scripted_effects/038_malta_crusaders_holy_world_effects.txt
common/scripted_effects/038_malta_crusaders_cleanup_effects.txt
```

Keep event-specific orchestration out of `chaosx_dynamic_effects.txt`. Add a shared helper there only when callers cross event or subsystem boundaries, and update its Markdown contract in the same change.

### State collections

Use the current collection or registry pattern for exact Event 38 state groups. Suggested file:

```text
common/collections/038_malta_crusaders_state_collections.txt
```

If the engine surface uses scripted triggers or arrays instead, follow current repository precedent and keep one owner source of truth.

### Decisions

```text
common/decisions/038_malta_crusaders_decisions.txt
common/decisions/categories/038_malta_crusaders_categories.txt
```

All Event 38 categories stay in these files unless a verified engine constraint requires another placement.

### Ideas and modifiers

```text
common/ideas/038_malta_crusaders_ideas.txt
common/dynamic_modifiers/038_malta_crusaders_dynamic_modifiers.txt
common/opinion_modifiers/038_malta_crusaders_opinion_modifiers.txt
```

Use dynamic modifiers for values and region-dependent effects when suitable. National spirits need complete lifecycles.

### Focus tree

```text
common/national_focus/038_malta_crusaders_focus.txt
common/focus_inlay_windows/038_malta_crusaders_inlay.txt
```

The inlay file is optional and should exist only if a small read-only focus summary is approved. The main Crusade Council is a separate event-owned GUI.

### AI

```text
common/ai_strategy/038_malta_crusaders_ai_strategy.txt
common/ai_focuses/ or current project equivalent
common/ai_templates/038_malta_crusaders_ai_templates.txt
```

Exact AI file types follow installed vanilla and repository precedents.

### Countries and history

Depending on tag reuse and transformations:

```text
common/countries/...
common/country_tags/...
history/countries/...
history/states/... only when verified and necessary
common/characters/038_malta_crusaders_characters.txt
```

Do not overwrite vanilla country history broadly when an event-time transformation can preserve compatibility.

### Units and equipment

```text
common/units/038_malta_crusaders_units.txt
common/units/equipment/038_malta_crusaders_equipment.txt
common/technologies/038_malta_crusaders_technologies.txt
common/technology_tags/... where needed
common/script_enums.txt
```

Technology or doctrine files require MCP inspection, render, and compare.

### On actions

```text
common/on_actions/038_malta_crusaders_on_actions.txt
```

Use event-owned bounded hooks. Do not add whole-world daily, weekly, or monthly processing.

### Scripted GUI and interface

```text
common/scripted_guis/038_malta_crusaders_scripted_guis.txt
interface/038_malta_crusaders.gui
interface/038_malta_crusaders.gfx
```

The event UI worker owns bounded layout work after the gameplay helper contract is accepted.

### Localisation

```text
localisation/english/038_malta_crusaders_l_english.yml
common/scripted_localisation/038_malta_crusaders_scripted_localisation.txt
```

Additional languages are outside this specification unless the project requires them in the same goal.

### GFX and assets

Event-scoped folders:

```text
gfx/event_pictures/038_malta_crusaders/
gfx/interface/ideas/038_malta_crusaders/
gfx/interface/goals/038_malta_crusaders/
gfx/interface/decisions/038_malta_crusaders/
gfx/interface/038_malta_crusaders/
gfx/models/038_malta_crusaders/
gfx/entities/038_malta_crusaders/
sound/038_malta_crusaders/
```

Flags remain in engine flag roots with tag and cosmetic-tag filenames. Achievement files remain in the achievement root.

### Documentation

```text
docs/events/038_malta_crusaders/
docs/plans/038_malta_crusaders_plans/
docs/super_events/038_malta_crusaders_super_event_research.md
docs/testing/... event-specific acceptance notes
```

Accepted source design stays in this spec folder.

## Core public effects

Suggested owner APIs:

```text
malta_crusaders_initialize_registry
malta_crusaders_prepare_opening_transaction
malta_crusaders_validate_opening_transaction
malta_crusaders_commit_opening_transaction
malta_crusaders_rollback_opening_transaction
malta_crusaders_initialize_country_package
malta_crusaders_refresh_public_values
malta_crusaders_queue_order_demand
malta_crusaders_resolve_order_demand
malta_crusaders_create_principality
malta_crusaders_transfer_relic_custody
malta_crusaders_apply_prefire_package
malta_crusaders_activate_evolution
malta_crusaders_form_teutonic_order
malta_crusaders_activate_atlantis
malta_crusaders_prepare_holy_world
malta_crusaders_activate_holy_world
malta_crusaders_launch_manual_scenario
malta_crusaders_cleanup_actor
```

Names are working API labels. Final names must be descriptive and consistent with repository style.

## Transaction outputs

Major transactions should return explicit results and proofs.

### Opening

```text
malta_crusaders_opening_result
malta_crusaders_opening_reject_reason
malta_crusaders_opening_transaction_id
malta_crusaders_opening_package_level
malta_crusaders_opening_state_count
malta_crusaders_opening_displaced_owner_count
```

### Principality

```text
malta_crusaders_principality_result
malta_crusaders_principality_reject_reason
malta_crusaders_principality_generation
malta_crusaders_principality_actor
malta_crusaders_principality_region
```

### Holy World

```text
malta_crusaders_holy_world_result
malta_crusaders_holy_world_reject_reason
malta_crusaders_holy_world_actor
malta_crusaders_holy_world_continent
malta_crusaders_holy_world_target_count
```

Public temporary inputs clear before return. Result and proof outputs remain long enough for the caller to read.

## Event targets

Use regular event targets for one event chain. Use global event targets only for durable cross-chain actors that cannot be represented safely by country variables or arrays.

Potential durable targets:

- current Event 38 actor
- current Pope
- selected principality actor
- selected order headquarters
- current relic custodian
- Holy World actor

Every global target needs explicit clear and invalidation logic. Do not use global targets merely for convenience.

## Variables and flags

### Flags for booleans

Use flags for true or false state:

- event fired
- route chosen
- evolution active
- Holy World ready
- Teutonic formed
- Atlantis formed
- manual setup active

Do not use numeric variables that only store 0 or 1.

### Variables for quantities

Use variables for:

- Authority, Cohesion, Legitimacy
- generation numbers
- package level
- elapsed timer
- selected ID values
- counts
- dynamic cost and strength calculations

### Temporary variables

Temporary variables have no scope. Do not prefix them with `ROOT`, `PREV`, or another scope token.

## Meta effects and dynamic selection

Meta effects can select:

- package-specific setup effects
- order-specific effects
- principality-specific creation effects
- equipment tokens
- regional campaign effects

Use them when the engine field does not accept a dynamic token. Keep the possible generated text bounded and validated.

## Shared dynamic helpers

Reuse:

- `calculate_economy_scaled_factory_grant`
- `union_compatible_researched_technologies_from_donor`
- `apply_state_population_loss_without_recruitable_manpower_gain`
- `apply_exact_state_civilian_population_loss`
- stockpile debit helpers
- `refresh_world_threat_state`
- `call_natural_disaster` only when accepted

Do not duplicate them.

## Chaos and event-log calls

The event uses current shared effects for:

- event registration and firing
- History row
- evolution row
- Chaos history
- world-end branch registry
- triggerable scenario registry
- super-event audio and visibility

Inspect current exact APIs before coding. This pack does not freeze outdated helper names beyond the documented public effects.

## Unit provider file ownership

Event 38 owns every custom unit provider callback. The shared unit-family registry reads published owner data. It does not gain an Event 38-specific central switch.

Provider setup is idempotent and CXT registered.

## Map MCP workflow

Before state edits or registry finalization:

1. `hoi4.map_inspect` the target states, owners, adjacency, ports, rail, supply, regions, and islands
2. render or inspect connected map data
3. build the exact collection manifest
4. use `hoi4.map_rewrite` only for accepted map source changes
5. compare after changes

If the route is unavailable, exact map implementation is blocked. Public-wiki IDs are not equivalent evidence.

## GUI MCP workflow

For the Crusade Council:

1. inspect owning GUI and linked scripted GUI
2. render all states and supported resolutions
3. inspect hierarchy and click regions
4. apply bounded GUI rewrite
5. render the same states and resolutions after change
6. compare and fix every visible defect

Source-only review cannot replace this evidence.

## Focus and technology MCP workflow

Use:

- focus inspect
- focus render
- focus rewrite where needed
- technology inspect
- technology render
- technology compare

Every output must be reviewed by the parent implementation agent.

## Documentation contracts

Any new shared helper updates its matching Markdown registry. Event-owned helpers are documented in Event 38 system docs. Every script file begins with an overview comment.

## Implementation order

1. repository exploration and collision audit
2. exact map registry
3. constants and owner state
4. release transaction
5. Malta package
6. custom unit providers
7. council values and decisions
8. focus tree
9. principalities
10. evolutions
11. hidden routes
12. Holy World and scenario
13. assets and super-events
14. event logs, cluster, scenario, workbook, and docs
15. audits and final reconciliation
