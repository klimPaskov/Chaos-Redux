# Event 046: The Great Shuffle specification pack

This is the source design package for Chaos Redux Event 046, **The Great Shuffle**.

The event replaces **Seismic Archive** and remains a Chaos level 1 Minor Repeatable event.

It is the Medium member of the **Randomizations** cluster (ID 14), which the workbook and live registry already carry; the workbook row itself still names Seismic Archive until implementation.

## Source specifications

- `specs/046_the_great_shuffle_spec_part_1_core.md`
- `specs/046_the_great_shuffle_spec_part_2_evolutions_and_selection.md`
- `specs/046_the_great_shuffle_spec_part_3_family_catalog.md`
- `specs/046_the_great_shuffle_spec_part_4_registry_transactions_and_safety.md`
- `specs/046_the_great_shuffle_spec_part_5_reports_ai_and_multiplayer.md`
- `specs/046_the_great_shuffle_spec_part_6_chaos_clusters_and_catalog.md`
- `specs/046_the_great_shuffle_spec_part_7_achievements_assets_localisation_and_acceptance.md`

## Matrices and contracts

- `matrices/046_event_map.md`
- `matrices/046_shuffle_surface_classification_matrix.md`
- `matrices/046_shuffle_registry_schema.md`
- `matrices/046_core_family_registry_catalog.md`
- `matrices/046_owner_adapter_contract.md`
- `matrices/046_firing_transaction_state_machine.md`
- `matrices/046_range_profile_matrix.md`
- `matrices/046_report_priority_matrix.md`
- `matrices/046_probability_scenario_matrix.md`
- `matrices/046_acceptance_scenarios.md`
- `matrices/046_source_conflict_ledger.md`
- `matrices/046_source_review_manifest.md`

## Implementation prompts

- `prompts/046_the_great_shuffle_coding_prompt.md`
- `prompts/046_the_great_shuffle_goal_prompt.md`
- `prompts/046_the_great_shuffle_registry_architecture_prompt.md`
- `prompts/046_the_great_shuffle_probability_audit_prompt.md`
- `prompts/046_the_great_shuffle_asset_prompt.md`
- `prompts/046_the_great_shuffle_achievement_prompt.md`
- `prompts/046_the_great_shuffle_localisation_prompt.md`
- `prompts/046_the_great_shuffle_catalog_workbook_prompt.md`

## Quality material

- `quality/046_presentation_choice_and_scope_review.md`
- `quality/046_design_risk_register.md`
- `quality/046_spec_completion_checklist.md`
- `quality/046_package_manifest.md`

## Plans and handoffs

- [046_manual_near_completion_review.md](../../plans/046_the_great_shuffle_plans/046_manual_near_completion_review.md)
- [046_external_evidence_blockers.md](../../plans/046_the_great_shuffle_plans/046_external_evidence_blockers.md)
- [046_subagent_routing_handoff.md](../../plans/046_the_great_shuffle_plans/subagent_handoffs/046_subagent_routing_handoff.md)

## Main design decisions

Each firing is one permanent global transaction.

Values are newly generated for every valid scope and are not swapped or conserved.

Earlier firings do not affect later family rolls or ranges.

The event uses an Event 46-owned allowlist with owner-controlled adapters.

Gameplay state can be shuffled only after a complete legality contract.

Framework state, history, stable identity, settings, and one-way ledgers remain protected.

The Baseline and five evolution capabilities expand from basic country values through stores, the map, institutions, owner mechanics, and proven structural families.

Evolution V remains reachable despite the possible World Collapse event freeze.

Every successful firing creates one bounded direct Chaos entry, one Event Log entry, and one personalized report per human player.

The package also defines six achievements, one report image, achievement icon packages, the Randomizations membership, catalog reconciliation, probability scenarios, and 70 acceptance scenarios.

## Evidence status

The package's acceptance language records requested design direction, but this package contains no attributable user or parent acceptance record, so those acceptance claims remain unresolved until an explicit basis is recorded.

The unavailable repository, wiki, vanilla, workbook, MCP, runtime, asset, localisation, and testing statements below are historical package-generation evidence and do not describe current workspace or service health.

No current implementation or engine evidence is recorded in this package.

Every supplied Markdown source, catalog CSV, configuration file, and all 20 supplied subagent definitions were fully read.

The complete list, line counts, and checksums are in `matrices/046_source_review_manifest.md`.

The original planning session had no access to the mod repository, offline wiki, vanilla files, workbook, or MCP.

The package defines those required downstream inspections and does not claim implementation, workbook edits, final localisation, asset production, MCP evidence, subagent execution, or in-game testing.

No requested design domain was shortened for speed.

The runtime slot `events/046_placeholder.txt` holds only a placeholder; no part of this package is implemented.

## Open questions

- Whether Evolution V should keep its "near-universal" family coverage: at that tier a single firing rewrites almost every proven family for every country, which can erase the player's whole campaign in one popup.
  The audit kept it because World Collapse is the end state the event is built toward, but the user may prefer a ceiling below full coverage.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:
- Recorded that Randomizations is already cluster 14 with Event 46 as its Medium member, replacing the "do not infer a cluster ID" instructions.
- Removed the Domestic Unrest, Event 21 dual membership, Event 2, and Alien Invasions requirements from this package: those clusters and memberships exist and belong to their owners (Part 6, the coding, catalog, and localisation prompts, and the acceptance and probability matrices).
- Replaced `AGENTS.md` and Codex `fork_turns` wording and removed the obsolete ZIP extraction instructions.

Pass 2, design improvement:
- Rescaled the direct Chaos bands from up to `+35` per firing to up to `+10`, so a repeatable event no longer outpaces a first nuclear use (`10`) or a major war declaration (`5`) on every firing.
- Cut the report's global summary from seven counts (families, rejected families, countries, states, units, adapters, capability) to one sentence naming the domains that changed; the counts drive no decision.
