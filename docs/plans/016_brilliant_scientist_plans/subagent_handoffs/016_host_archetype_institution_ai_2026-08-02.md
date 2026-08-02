# Event 016 host-archetype institution AI continuation

Date: 2026-08-02

## Scope

This bounded continuation connects the existing mutually exclusive host-archetype flags to the four initial Directorate institutional-form decisions. It adds no event, project, route, meter, asset, or model.

## Changed files

- `common/decisions/016_brilliant_scientist_directorate_institutions.txt`
  - Public Science Council receives the university and refugee archetype weights.
  - Compartmentalized Military Office receives the militarized and threatened archetype weights.
  - Private Industrial Concession receives the industrial and colonial archetype weights.
  - Exile Scholar Network receives the refugee and colonial archetype weights.
- `docs/events/016_brilliant_scientist/systems/directorate.md`
  - Documents the new AI preference layer and its presentation-only scope.

## Contract

The effects remain the existing institution blocks and their existing costs, factory burdens, flags, dynamic modifiers, and Directorate meter changes. Archetype weights are applied only after the mutually exclusive host flag has been assigned at appointment or ordinary transfer. Human choice is unchanged. No country-wide iteration, new resource store, hidden meter exposure, or duplicate route is introduced.

## Validation

- Confirmed all six `brilliant_scientist_host_flavor_ai` keys used by the decision blocks are declared in `common/script_constants/016_brilliant_scientist_host_flavor_constants.txt`.
- Confirmed each new modifier is inside the corresponding existing `ai_will_do` block and is guarded by one of the mutually exclusive host-archetype flags.
- Confirmed the project-force equipment file was restored to its audited helper-gated form; no inline static gate expansion is part of this tranche.
- Hearts of Iron IV was not launched. Live AI selection evidence remains user-owned.

## Simplifications and blockers

No fallback, placeholder, or model was introduced. The archetype continues to be a finite presentation and AI preference layer rather than a separate country-specific event chain; broader country flavour, quantitative balance evidence, and live consumer validation remain outside this handoff.
