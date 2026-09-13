# Event 53 Specification Package Contents

This index maps every deliverable in the Event 53 planning pack. `SHA256SUMS.txt` records file-integrity hashes for the completed package.

## Entry point

| File | Purpose |
| --- | --- |
| [README.md](README.md) | Catalog identity, design promise, package map, and authoritative rules |

## Source specifications

| File | Purpose |
| --- | --- |
| [specs/01_event_identity_and_player_experience.md](specs/01_event_identity_and_player_experience.md) | Core premise, player information, choice integrity, replay role, and writing direction |
| [specs/02_target_selection_and_lifecycle.md](specs/02_target_selection_and_lifecycle.md) | Uniform target selection, persistence, control changes, extinction, succession, and lifecycle invariants |
| [specs/03_visit_pacing_and_demand_engine.md](specs/03_visit_pacing_and_demand_engine.md) | Recurring intervals, demand validity, amount scaling, payment, refusal, and industrial burdens |
| [specs/04_consequence_registry_contract.md](specs/04_consequence_registry_contract.md) | Equal package ballots, owner boundaries, pool construction, receipts, recovery, and maintenance |
| [specs/05_baseline_and_evolution_i_consequences.md](specs/05_baseline_and_evolution_i_consequences.md) | Baseline package set and Evolution I additions |
| [specs/06_evolution_ii_and_compound_consequences.md](specs/06_evolution_ii_and_compound_consequences.md) | Evolution II demands, national crises, compound packages, and prevalidation rules |
| [specs/07_evolution_iii_catastrophes.md](specs/07_evolution_iii_catastrophes.md) | World Collapse package set and no-attacker nationwide nuclear processing |
| [specs/08_system_adapters_and_attribution.md](specs/08_system_adapters_and_attribution.md) | Owner adapter contracts, neutral helper use, bookkeeping isolation, and Chaos attribution |
| [specs/09_presentation_event_logs_and_assets.md](specs/09_presentation_event_logs_and_assets.md) | Visible event family, writing direction, History, Event Details, evolutions, and report art |
| [specs/10_multiplayer_ai_and_edge_cases.md](specs/10_multiplayer_ai_and_edge_cases.md) | Multiplayer authority, player-control pause, terminal-state continuity, AI ownership, and recovery cases |
| [specs/11_balance_probability_and_acceptance.md](specs/11_balance_probability_and_acceptance.md) | Affordability goals, severity bands, exploit review, probability evidence, and completion gates |
| [specs/12_implementation_architecture.md](specs/12_implementation_architecture.md) | File map, state model, constants, helper layout, MCP work, and implementation order |

## Quality and evidence contracts

| File | Purpose |
| --- | --- |
| [quality/consequence_registry_manifest.md](quality/consequence_registry_manifest.md) | Complete 57-entry package inventory with owners, validity, severity, and readiness |
| [quality/demand_registry_manifest.md](quality/demand_registry_manifest.md) | Complete 17-entry demand inventory with applicability, scaling, bounds, and payment paths |
| [quality/adapter_contract_matrix.md](quality/adapter_contract_matrix.md) | Owner-by-owner adapter readiness, required inputs, outputs, and activation gates |
| [quality/probability_scenarios.md](quality/probability_scenarios.md) | Named MCP scenarios for uniform targeting, demands, consequences, timing, and amount sensitivity |
| [quality/validation_scenarios.md](quality/validation_scenarios.md) | Lifecycle, payment, refusal, adapter, evolution, catastrophe, presentation, and recovery tests |
| [quality/requirement_traceability_matrix.md](quality/requirement_traceability_matrix.md) | Accepted idea requirements mapped to specifications and evidence gates |
| [quality/design_scope_and_closure.md](quality/design_scope_and_closure.md) | Accepted surfaces, rejected expansion, and improvement-loop closure decision |
| [quality/source_review_manifest.md](quality/source_review_manifest.md) | Supplied-file hashes, full-reading record, research decision, and environment boundary |
| [quality/subagent_execution_status.md](quality/subagent_execution_status.md) | Subagent definition review, unavailable runtime disclosure, and later execution requirements |
| [quality/package_validation_report.md](quality/package_validation_report.md) | Final artifact inventory, consistency checks, and evidence boundary |

## Catalog handoff

| File | Purpose |
| --- | --- |
| [catalog/event_053_catalog_alignment.md](catalog/event_053_catalog_alignment.md) | Stale-row correction, authoritative XLSX workflow, field sources, and status progression |

## Parent implementation prompts

| File | Purpose |
| --- | --- |
| [prompts/goal_prompt.md](prompts/goal_prompt.md) | Compact implementation goal prompt |
| [prompts/coding_prompt.md](prompts/coding_prompt.md) | Full context-rich implementation prompt |
| [prompts/asset_prompt.md](prompts/asset_prompt.md) | Bounded five-scene generated report-art brief |

## Context-complete subagent prompts

| File | Purpose |
| --- | --- |
| [prompts/subagents/00_routing.md](prompts/subagents/00_routing.md) | Recommended routing and excluded specialist roles |
| [prompts/subagents/01_repo_explorer_prompt.md](prompts/subagents/01_repo_explorer_prompt.md) | Repository and precedent mapping prompt |
| [prompts/subagents/02_scripted_system_architect_prompt.md](prompts/subagents/02_scripted_system_architect_prompt.md) | Lifecycle, registry, adapter, and transaction architecture prompt |
| [prompts/subagents/03_ai_probability_auditor_prompt.md](prompts/subagents/03_ai_probability_auditor_prompt.md) | Read-only MCP probability audit prompt |
| [prompts/subagents/04_generated_event_art_prompt.md](prompts/subagents/04_generated_event_art_prompt.md) | Generated report-art worker prompt |
| [prompts/subagents/05_localisation_auditor_prompt.md](prompts/subagents/05_localisation_auditor_prompt.md) | Player-facing text and key-coverage audit prompt |
| [prompts/subagents/06_documentation_curator_prompt.md](prompts/subagents/06_documentation_curator_prompt.md) | Documentation reconciliation prompt |
| [prompts/subagents/07_spreadsheet_doc_worker_prompt.md](prompts/subagents/07_spreadsheet_doc_worker_prompt.md) | Authoritative workbook update and CSV export prompt |
| [prompts/subagents/08_event_completion_auditor_prompt.md](prompts/subagents/08_event_completion_auditor_prompt.md) | Final spec-versus-implementation audit prompt |
| [prompts/subagents/09_improvement_loop_closure_prompt.md](prompts/subagents/09_improvement_loop_closure_prompt.md) | Anti-bloat closure review prompt |
