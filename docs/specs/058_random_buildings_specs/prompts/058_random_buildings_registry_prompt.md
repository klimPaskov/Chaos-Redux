# Scripted-system architecture prompt for Event 58 Random Buildings

Use this prompt with `chaosx_scripted_system_architect` after the repository exploration pass.

Spawn with `fork_context=false`.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, the complete Event 58 specification package, the repository explorer handoff, the offline wiki pages for data structures, triggers, effects, scopes, event targets, and on-actions, installed vanilla documentation, and the exact live Event 58, building, facility, camp, map, and event-log source files named by the parent.

## Goal

Design and, when parent scope permits, implement the smallest reusable Event 58 provider architecture that supports:

- baseline state buildings
- Evolution I expanded state buildings
- Evolution II province packages
- Evolution III exceptional structures
- future owner registration without root-event rewrites
- independent state rolls
- risk-band selection and safer-only fallback
- current capacity checks
- atomic placement and owner callback
- stable display families
- per-transaction result accounting
- owner-controlled responsibility and cleanup

The registry belongs to Event 58 unless an already existing neutral cross-system provider contract clearly fits. Do not place event lifecycle, evolution, UI, or owner-specific validation into `chaosx_dynamic_effects` or `chaosx_dynamic_triggers` merely to make it look shared.

## Required architecture output

For every proposed helper or registry surface, state:

- exact name
- owner file
- scope
- inputs
- outputs
- defaults
- side effects
- persistent or temporary state
- event targets
- direct call sites
- cleanup
- failure behavior
- documentation path

Define the provider row contract for:

- stable entry ID
- owner system
- eligible layer
- risk band
- relative weight
- global availability
- state validity
- province-target resolution where relevant
- capacity
- placement
- post-placement initialization
- responsibility resolver
- uniqueness scope
- display family
- structure-exists proof where achievements need it
- cleanup owner

Malformed or incomplete providers must fail closed without breaking other entries.

## Transaction requirements

- Freeze the loaded land-state membership once per firing.
- Revalidate candidates immediately before mutation.
- Require the provider to prove callback readiness before mutation. A failed attempt may reroll only after proving that it left no partial building, facility, marker, ledger, or responsibility state.
- Process baseline, Evolution I, Evolution II, and Evolution III in that order.
- Allow one result per state per active state or province layer.
- Allow a province package to affect several valid provinces while counting as one state result.
- Use a limited world budget for Evolution III.
- Prevent two exceptional structures in one state during one firing.
- Keep the zero-result preflight from consuming event history, timer, repeatable cap, or Chaos.
- Keep direct hidden-resolver calls from creating a second registered transaction.
- Clear temporary arrays, targets, and counters after reports and achievements.
- Do not add a recurring whole-world on-action.

## Owner adapters

Inspect and map real adapters for ordinary buildings, camps and repression, reactors and facilities, railways, supply hubs, and any current Chaos Redux custom buildings.

A special structure is complete only when its owner initialization succeeds. When rollback is unsafe, the provider must use a prevalidated path that cannot fail after mutation or remain blocked. Event 58 must not duplicate deaths, condemnation, evidence, project completion, technology grants, or owner event history.

Use the shared country classifiers only where an individual provider needs them. Do not add another event-local special-country registry.

## Dynamic values

Centralize thresholds, risk-band targets, exceptional budget, retry limits, display family IDs, and one-shot Chaos milestones in Event 58 script constants or the verified local tuning pattern.

Do not scatter magic numbers across event, effects, triggers, logs, achievements, and localisation.

## Evidence and handoff

Use event, map, and probability MCP inspection as required by the owner skills. Do not guess unsupported building or province operations.

Return either a bounded implementation or an architecture plan. List files, helpers, constants, call sites, provider entries mapped, owner APIs, unsupported fields, map blockers, validation, and remaining parent work.
