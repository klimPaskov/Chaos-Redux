# Event 011 Secret Alliance specification package

This package expands Event 011 into a full source design for a hidden anti-player diplomatic and covert operations system.

## Package structure

- `specs/011_secret_alliance_spec.md` is the core source specification.
- `specs/011_secret_alliance_mechanics.md` defines pact selection, stage values, reveal rules, escalation, and cleanup.
- `specs/011_secret_alliance_decisions_missions.md` defines the player response category, missions, border operations, costs, and action families.
- `specs/011_secret_alliance_ai_balance_localisation.md` defines AI behavior, balance guardrails, effect strength, and text direction.
- `matrices/011_secret_alliance_decision_map.md` contains decision and mission mapping.
- `matrices/011_secret_alliance_ai_matrix.md` contains actor behavior mapping.
- `matrices/011_secret_alliance_asset_matrix.md` contains asset coverage.
- `focus_graphs/011_secret_alliance_progression_map.md` contains a route sketch for event progression.
- `research/011_secret_alliance_research_notes.md` records historical inspiration sources.
- `prompts/` contains implementation, asset, achievement, super-event, decision and mission, and goal prompts.
- `handoffs/011_secret_alliance_subagent_routing.md` maps the provided project subagent definitions to the implementation pass.
- `inspection/011_secret_alliance_source_reading_manifest.md` records the source files read for this planning pass.

All text in the spec is direction and design unless it explicitly says it is an internal working label. Player-facing localisation should be written during implementation from these directions.
