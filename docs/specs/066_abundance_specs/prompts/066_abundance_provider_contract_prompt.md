# Event 066 Abundance Provider Contract Prompt

Use `chaosx_scripted_system_architect` with `fork_context=false` for the reusable scripted architecture and bounded implementation work described here.

## Task

Design and implement the provider contract for Event 66 Abundance.
The accepted source specs are under `docs/specs/066_abundance_specs/`.
Read every specification part, especially:

- `specs/066_abundance_spec_part_2_dynamic_value_space.md`
- `specs/066_abundance_spec_part_3_choice_generation.md`
- `specs/066_abundance_spec_part_4_abundance_application.md`
- `research/066_abundance_value_provider_coverage_matrix.md`

Read and follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, the current scripted-system rules, the offline wiki pages and vanilla documentation required by the touched script surfaces, and the existing dynamic effects and triggers registries.

## Architecture requirement

HOI4 does not provide safe general reflection over every numeric variable and mechanic.
Implement an extensible owner-registration contract.
Event 66 must not maintain a small central list of values.
Each owner package publishes the semantic values it controls through stable providers or dynamic family providers.

A provider must support:

1. Idempotent registration with stable numeric identity and schema version.
2. Read-only candidate enumeration in country scope.
3. Availability checks for DLC, mechanic ownership, reveal state, route state, targets, and current lifecycle.
4. Spoiler-safe short and full display identities.
5. Current value or stage reporting where available.
6. Harm, rarity, strangeness, source class, deduplication family, and hard conflict metadata.
7. An owner-controlled abundance application callback.
8. AI evaluation facts that are consumed only after four cards are generated.
9. Idempotent result receipts with complete, partial, rejected, persistence, and recovery states.
10. Save-safe stored candidate identities and migration behavior.

## Owner boundary

Enumeration must never activate the owner mechanic, mark another event fired, mutate a ledger, create a target, or change gameplay.
Application must return to the owner system.
Event 66 cannot directly set foreign crisis variables, global totals, source ledgers, population, deaths, contamination, condemnation, famine, migration, occupation, equipment families, or country-specific balances.

Global systems enter only through owner-defined country contribution operations.
Hidden values stay unavailable or use an owner-supplied cover name.
Raw helper variables, indexes, sequence values, proofs, and debug counters are excluded.

## Candidate and card storage

Provide a bounded data model for four cards with up to three atomic candidates each.
Store provider identity, candidate sub-identity, target proof when required, display selector identity, current snapshot, harm class, source class, deduplication family, hard conflicts, strength profile, and application receipt identity.

Card order and contents must survive save and load.
Reopening the popup or rebuilding localisation cannot reroll.
Parallel arrays or another proven Clausewitz pattern may be used, but the model must be documented and auditable.

## Dynamic dispatch

Use stable scripted effects, scripted triggers, script constants, event targets, meta effects, and scripted localisation where they are supported by the current engine and local precedent.
Do not invent unsupported dynamic calls.
Fail closed when a provider identity or callback is missing.

Keep Event 66 orchestration in event-owned files unless another unrelated caller proves that a helper belongs in the neutral shared registry.
Any new neutral shared helper requires a contract update in the matching Markdown registry and a call-site audit.

## Required outputs

- provider registry source and tuning constants
- Event 66 owner gateway and dispatch helpers
- example core providers and owner adapter pattern
- provider authoring documentation with purpose, scope, inputs, outputs, defaults, side effects, and examples
- provider schema and migration notes
- coverage inventory disposition table
- candidate and card storage diagram
- result receipt contract
- debug rejection reason map
- bounded validation for missing, duplicated, stale, and malformed providers
- handoff under `docs/plans/066_abundance_plans/subagent_handoffs/`

## Restrictions

Do not add a periodic whole-world scan.
Do not add a custom GUI.
Do not patch unrelated owner systems merely to inflate coverage.
Do not claim universal coverage until the repository-wide value inventory has a disposition for every row.
Do not hide missing providers behind generic Political Power, equipment, or factory fallbacks.
Do not alter AI generation based on utility.

Report blocked provider families and the exact engine or ownership reason.
