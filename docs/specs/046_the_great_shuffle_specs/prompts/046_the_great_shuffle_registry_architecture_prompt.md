# Event 046 scripted-system architecture prompt

Use `chaosx_scripted_system_architect` with a context-complete prompt and no inherited conversation context to design and, where parent-authorized, implement the Event 046 randomization framework.

Read:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaosx_dynamic_effects.md`
- `chaosx_dynamic_triggers.md`
- every Event 046 source spec
- `matrices/046_shuffle_surface_classification_matrix.md`
- `matrices/046_shuffle_registry_schema.md`
- `matrices/046_owner_adapter_contract.md`
- `matrices/046_firing_transaction_state_machine.md`
- `matrices/046_range_profile_matrix.md`
- `matrices/046_acceptance_scenarios.md`

Before source work, read the required offline wiki pages and current vanilla documentation for variables, arrays, random lists, effects, triggers, event targets, scope iteration, state population, equipment stockpiles, buildings, research progress, production, units, commanders, diplomacy, save persistence, and meta effects.

Inspect current Chaos Redux event registration, evolution, Event Log, Chaos history, population transaction, special-country classification, owner registries, sparse processing, and save-repair precedents.

## Architecture goals

Create one Event 46-owned allowlist registry.

Do not scan arbitrary memory or variables.

Give every family a stable owner, version, capability, scope source, validity contract, result type, dynamic range, distribution, compatibility group, dependency bundle, planning method, setter, reconciliation, report contract, direct Chaos class, recovery, cleanup, and tests.

Keep owner-specific orchestration in owner files.

Only add a helper to the shared dynamic registry when it is genuinely neutral and has unrelated callers.

Document every new public helper in the matching reference file.

## Transaction goals

Map the state machine from Idle through Closing.

Prove that every selected family's complete result set is fixed before its first write.

Choose a result-storage method supported by the live engine that can handle country, state, unit, commander, production, pair, and owner scopes without permanent save bloat.

Prove exact save and load recovery.

Use logical family atomicity.

Do not claim general rollback when the engine cannot provide it.

A family that fails before commit remains untouched.

A family that begins commit must finish the immutable plan idempotently.

No reroll can occur after planning.

## Required hard cases

Design and prove:

- baseline family selection and quotas
- compatibility and dependency bundles
- zero-scope and malformed-family rejection
- duplicate-start lock
- one-member cluster non-duplication
- World Collapse reachability under both possible freeze orders
- population absolute rewrite for increases and decreases with no Deaths, migration, or unintended reserve-manpower effect
- generic source suppression for Event 46-owned ideology and other setter side effects
- owner adapter registration and veto
- exact report before and after values
- direct Chaos compression once per transaction
- cleanup of every per-scope plan and source marker
- practical one-shot world processing without a periodic whole-world on-action

## Protected state audit

Produce a write-path audit for every protected domain in Part 4 and the classification matrix.

The audit must include Chaos, Deaths, Air Cleanliness, Condemnation, famine, migration, camps, event weights, timers, histories, enable state, evolution state, clusters, scenarios, Event Log arrays, world-end state, settings, debug state, achievements, stable IDs, object identities, provider registries, and lifecycle event targets.

A numeric type is not evidence that the value is safe.

## Output and handoff

Use the parent-provided allowed file list.

Do not redesign Event 46, add decisions, add a GUI, add a super-event, or expose new player counters.

When making a bounded patch, write a handoff under `docs/plans/046_the_great_shuffle_plans/subagent_handoffs/` listing changed files, family IDs, helpers, call sites, before and after behavior, meaningful validation, skipped evidence, and remaining blockers.

When the architecture needs a broader unapproved change, write a plan and stop.

Do not weaken the accepted design with hardcoded family lists, old-value scaling, compensation, restored values, generic fallbacks, or periodic world scans.
