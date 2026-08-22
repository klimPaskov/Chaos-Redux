# Formable-state documentation

This directory contains the shared documentation and generated evidence for formable-country state requirements and state-puzzle consumers.

## Navigation

- [`formable_state_puzzle_system.md`](formable_state_puzzle_system.md) describes the shared state-puzzle workflow and runtime ownership boundaries.
- [`state_registry/README.md`](state_registry/README.md) is the source-of-truth index for the active-map geometry registry, schema, generated trigger contract, and consumer compiler inputs.
- [`state_puzzles/`](state_puzzles/) contains consumer manifests and generated unresolved or qualifying state-puzzle evidence grouped by formable or decision family.

## Ownership rules

The state registry README and its referenced source registry control registry schema, provenance, and generated trigger expectations.

Consumer manifests control the state candidates, qualification helpers, visibility helpers, and runtime identifiers for their own state-puzzle surfaces.

Generated images, masks, projections, and registry outputs are build artifacts and should be regenerated through the documented producers rather than edited as prose documentation.

This directory documents shared formable infrastructure; event-specific design remains in the relevant `docs/specs/`, `docs/events/`, and `docs/plans/` packages.
