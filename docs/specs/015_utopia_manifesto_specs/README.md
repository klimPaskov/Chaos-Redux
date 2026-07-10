# Event 15 Utopia Manifesto Planning Package

This package is the source design handoff for Chaos Redux Event 15, `utopia_manifesto`.

The event replaces the reserved `World Tension Subsides` entry and changes Event 15 into a Minor Fire-Once event with no cluster membership. A weak country discovers or revives a utopian manifesto. An AI country accepts it. A human player can accept or reject it. Acceptance replaces the eligible country's current generic or approved replaceable focus tree with a comprehensive Utopia tree and activates the Commonwealth Ledger mechanic.

All player-facing names in this package are working labels unless a file states otherwise. They define purpose, tone, route identity, and implementation coverage. They are not pasteable localisation.

## Package map

- `specs/` contains the source event specification.
- `matrices/` contains target selection, route, decision, idea, AI, achievement, asset, and acceptance matrices.
- `focus_graphs/` contains branch and mechanic flow diagrams.
- `research/` contains the historical design basis, bibliography, source-reading ledger, and manual improvement-loop review.
- `prompts/` contains the asset, super-event, achievement, decision, coding, and goal prompts.
- `prompts/subagents/` contains reproducible prompts for every relevant Chaos Redux project subagent.
- `handoffs/` contains implementation order, subagent orchestration, and verification blockers.
- `catalog/` contains the Event 15 catalog replacement plan.

## Design promise

The event asks whether an economically weak state can turn an old literary model into a functioning country. The resulting campaign revolves around provision, chosen or assigned work, common stores, consent, settlement, and the claim that land may be demanded only when genuine need exists. The tree supports democratic, council-socialist, technocratic, coercive, and hidden humanist interpretations. It also makes the source text's harsher features playable, including colonial claims to underused land, compulsory labor, mercenary warfare, and restricted tolerance.

The mechanic is built around four visible pressures:

1. **Need** measures material and strategic shortage.
2. **Plenty** measures the ability to provide food, housing, transport, tools, and reserves.
3. **Concord** measures consent, public confidence, and local acceptance.
4. **Choice versus Assignment** measures whether occupations and duties are selected freely or imposed by planners.

The values alter focus access, decisions, integration rules, external claims, route corruption, AI behavior, and the final state identity.

## Honest limits of this planning run

Every supplied Markdown file, TOML subagent definition, and CSV catalog was read and processed. The supplied event catalog confirms that ID 15 is reserved for rework.

The full Chaos Redux repository, offline Paradox wiki snapshot, vanilla Hearts of Iron IV installation, and project subagent execution runtime were not mounted in this environment. Repository pattern verification, exact state IDs, exact file paths inside the live mod, vanilla precedent checks, and actual subagent execution remain implementation-stage work. No result in this package claims those checks were performed.

A manual improvement-loop and anti-bloat pass is included. It follows the supplied improvement-loop and audit criteria, but it is not a substitute for the mandatory `chaosx_improvement_loop_planner` and completion-auditor runs in the implementation environment.
