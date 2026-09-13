# Gods of Africa specification package

> Superseded-package notice, 2026-09-05: this standalone package is retained as historical planning provenance and is not the current source of truth. Its accepted Event 012 ownership and subsystem design are represented by `docs/specs/012_africa_specs/` and the current implementation-facing document `docs/events/012_africa/gods_of_africa.md`; its old intended destination and unperformed-environment statements remain historical. No files are deleted by this cleanup.

## Disposition

This package is superseded by the accepted Event 012 specification package and current Event 012 subsystem documentation. Its internal prompts, quality gates, catalog handoff, and implementation map remain useful historical evidence, but they must not be used to reopen duplicate implementation work or to treat the former Event 070 catalog request as current approval.

## Package identity

This package specifies **Gods of Africa** as a persistent subsystem owned by Event `012`, **Africa Is One**.

Event `070` remains available for a different event idea. Nothing in this package assigns an event weight, event classification, cluster membership, or `chaosx.nr70.*` namespace to Gods of Africa.

The historical intended repository destination recorded by this package was:

```text
docs/specs/012_africa_is_one_specs/gods_of_africa/
```

## Core design decisions

- The system begins only after Africa Is One has fired, the African unifier exists, Evolution I is active, and the consolidation delay has elapsed.
- Every valid major country and player-controlled country receives an independent relationship with Africa and the Gods.
- **Gods of Africa Strength** is one global public value.
- **Wrath of the Gods** is one public value tracked separately for each participant.
- The exact friendship calculation remains hidden.
- Each participant can have only one active demand at a time.
- Material tribute is transferred to the African unifier.
- Demand size follows target capacity, African need, Wrath, Strength, Chaos, and Event 012 evolution state.
- Punishment severity is capped by Strength. Wrath alone can never unlock the strongest punishment.
- Routine tribute calls stay inside Event 012's owner-managed runtime and do not enter the normal random-event picker.
- The player-facing surface uses an ordinary decision category, one active demand mission, and a compact two-value display by default.
- A full scripted GUI is reserved for a later implementation decision if the normal category cannot present the system clearly.
- The doctrine is fictional. It does not combine real African religious traditions into one invented historical pantheon.

## Package contents

### Source specification

- `specs/012_gods_of_africa_full_spec.md`
- `specs/012_gods_of_africa_technical_architecture.md`
- `specs/012_gods_of_africa_decisions_missions_ui.md`
- `specs/012_gods_of_africa_focus_integration.md`
- `specs/012_gods_of_africa_assets_presentation.md`

### Implementation and catalog handoffs

- `implementation/012_gods_of_africa_implementation_map.md`
- `handoffs/012_gods_of_africa_catalog_alignment.md`
- `handoffs/012_gods_of_africa_subagent_routing_and_blocker.md`

### Quality and review

- `quality/012_gods_of_africa_acceptance_matrix.md`
- `quality/012_gods_of_africa_ai_probability_scenarios.md`
- `quality/012_gods_of_africa_parent_improvement_review.md`
- `quality/012_gods_of_africa_source_reading_manifest.md`
- `quality/012_gods_of_africa_package_validation.md`
- `PACKAGE_MANIFEST.md`

### Research

- `research/012_gods_of_africa_research_notes.md`
- `research/012_gods_of_africa_bibliography.md`

### Reusable prompts

- `prompts/012_gods_of_africa_coding_prompt.md`
- `prompts/012_gods_of_africa_goal_prompt.md`
- `prompts/012_gods_of_africa_decision_mission_prompt.md`
- `prompts/012_gods_of_africa_focus_prompt.md`
- `prompts/012_gods_of_africa_asset_prompt.md`
- `prompts/012_gods_of_africa_super_event_prompt.md`
- `prompts/012_gods_of_africa_completion_audit_prompt.md`

## Evidence status

Every source file supplied with this task was read in full, including all three CSV catalogs and all twenty extracted subagent definitions.

The live Chaos Redux repository, the authoritative XLSX event catalog, the offline Paradox wiki snapshot, installed vanilla files, and vanilla documentation were not mounted in the original planning environment. That statement is historical; current source, wiki, vanilla, and MCP evidence is recorded by the accepted Event 012 documentation and dated handoffs.

The configured custom-subagent route was discovered, but the outer Codex tunnel returned an HTTP 404 during the original planning invocation. No claim in this package treats a manual role review as an executed custom-subagent report; current Event 012 documentation records the available read-only MCP artifacts and the dedicated probability-auditor limitation separately.

## Design completion statement

The gameplay design was fully specified without a smaller fallback version at the time of this package. Runtime inspection, source implementation, generated-art production, probability evaluation, GUI rendering, catalog workbook edits, and live-game validation were outside that planning package; current implementation and evidence dispositions are recorded by the replacement documents.
