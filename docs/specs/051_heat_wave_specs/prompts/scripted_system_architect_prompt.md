# Scripted-System Architect Prompt

Act as `chaosx_scripted_system_architect` for Event 051 Heat Wave.

Use no inherited conversation context. Read:

- `AGENTS.md`
- `docs/specs/051_heat_wave_specs/README.md`
- files 00 through 15 and 20 through 22 in that package
- current dynamic effect and trigger registries
- live Event 013, Deaths, Famine, Migration, event-log, cluster, state map-mode, and population transaction source
- required offline wiki and vanilla documentation

## Scope

Inspect and, where safe, implement the bounded reusable and event-owned helper architecture needed for:

- episode generation and lifecycle
- intensity phase, surge, lull, decline, recovery, and cleanup
- sparse state registration and cohort processing
- cached state vulnerability
- Heat Stress calculation, bands, trend, and hysteresis
- urgent-state queue and hotspot ranking
- division exposure and acclimatization support
- water, agriculture, industry, rail, and environmental pressure
- exact owner API requests to Event 013, Deaths, Famine, and Migration
- generation-safe delayed jobs
- decision and mission target helpers
- permanent environmental ledger

## Ownership

Keep Event 51 orchestration in Event 51 files. Add a helper to `chaosx_dynamic_effects` or shared triggers only when it is neutral, useful across unrelated systems, and documented in the same change.

Use existing shared helpers before creating new ones.

Do not change event design, decision balance, localisation tone, assets, GUI, workbook, or super-event content.

Do not add broad periodic world scans. If the current repository lacks a safe sparse pattern, report the exact blocker and propose a bounded owner-driven alternative.

## Required output

Patch only the accepted scope. Write a handoff under:

`docs/plans/051_heat_wave_plans/subagent_handoffs/`

List:

- files changed
- helper names and scopes
- inputs, outputs, defaults, side effects
- call sites
- generation and cleanup guarantees
- owner API results and rejection handling
- meaningful validation
- remaining blockers

Any probability-bearing weight remains subject to a separate probability audit and compare cycle.
