# Event 016 settlement-outcome host flavour handoff

Date: 2026-08-02

Mode: parent-owned bounded presentation continuation. No models or gameplay effects were added.

## Scope

The ten resolved settlement outcomes in `chaosx.nr16.31` already selected a causal result and appended the recorded Evolution IV sovereignty policy. They now also append `GetBrilliantScientistHostFlavorClause`, preserving the host's university, industrial, militarized, threatened, colonial, refugee, or default institutional context when the settlement resolves.

Covered outcomes: release, exile, confinement, shutdown, foreign defection, laboratory uprising, Kruger State rebellion, charter, institutional takeover, and non-country crisis.

## Invariants

- `chaosx.nr16.31` keeps its existing outcome-selection triggers, option, country formation, territory, character, receipt, and policy effects.
- The appended clause is presentation-only and does not alter containment strength, transfer, state ownership, production, technology, AI weighting, event-log state, or aftermath scheduling.
- The policy clause remains present after the host clause, so the recorded Evolution IV commitment remains visible.

## Changed files

- `localisation/english/016_brilliant_scientist_containment_l_english.yml`
- `docs/events/016_brilliant_scientist/overview.md`
- `docs/events/016_brilliant_scientist/systems/super_events_and_aftermath.md`
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`

## Validation and boundary

The localisation file retains its UTF-8 BOM. Existing focused Event Inspector coverage for the containment chain remains applicable because only description text changed. Broader country-specific chains, quantitative balance evidence, live acceptance, and all seven Event 016-specific 3D packages remain open.
