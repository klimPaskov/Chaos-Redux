# 086 World Claims

**Full specification draft and implementation handoff.** Catalog: Minor Repeatable, Chaos level 1, Formables Low only, To Be Reworked. This is a planning package, not installed runtime content or a completed engine-validation report.

This repository package lives at `docs/specs/086_world_claims_specs/`.
Implementation working notes and specialist evidence belong under `docs/plans/086_world_claims_plans/`.

## Main specification

| Part | Subject |
| --- | --- |
| [1](086_world_claims_spec_part_1_core.md) | Core idea, universal opening and campaign loop |
| [2](086_world_claims_spec_part_2_frontiers.md) | Owned-territory frontier, connected rings, repeat behavior |
| [3](086_world_claims_spec_part_3_evolutions.md) | All five Evolutions and profile persistence |
| [4](086_world_claims_spec_part_4_integration.md) | Claimant-specific Compliance, sustained integration and earned cores |
| [5](086_world_claims_spec_part_5_dynamic_ambitions.md) | Dynamic ambition discovery, adoption, formation and successors |
| [6](086_world_claims_spec_part_6_geographic_campaigns.md) | Geographic campaign examples and unscripted shapes |
| [7](086_world_claims_spec_part_7_decisions_and_missions.md) | Integration projects, assurances and proclamations |
| [8](086_world_claims_spec_part_8_rivals_and_changed_countries.md) | Rival claims, subjects, civil wars, releases and country continuity |
| [9](086_world_claims_spec_part_9_names_flags_and_native_formables.md) | Greater-state identities, flags and native-formable precedence |
| [10](086_world_claims_spec_part_10_endgames_and_world_pressure.md) | Continental/global outcomes and bounded Chaos contributions |
| [11](086_world_claims_spec_part_11_presentation_and_assets.md) | Exact-state UI, reports, assets and writing direction |
| [12](086_world_claims_spec_part_12_ai_and_campaign_balance.md) | AI behavior, pacing, fairness and performance |
| [13](086_world_claims_spec_part_13_achievement_design.md) | Eight achievement concepts |

## Numbers and implementation contracts

Read [canonical tuning](086_world_claims_tuning.md), [engine gates](086_world_claims_engine_contracts.md), [decision/mission matrix](086_world_claims_decision_mission_matrix.md), [country continuity matrix](086_world_claims_country_package_matrix.md), [AI scenarios](086_world_claims_ai_scenario_matrix.md), [achievement matrix](086_world_claims_achievement_matrix.md), and [implementation handoff](086_world_claims_implementation_handoff.md).

Geographic and identity details are in [the geographic registry contract](geography_and_identity/geographic_registry_contract.md) and [the identity/flag contract](geography_and_identity/identity_and_flag_contract.md). Production directions are in [asset briefs](086_world_claims_asset_briefs.md). Read the user requirement crosswalk in [traceability](source_review/requirements_traceability.md).

The user's stage thresholds, Compliance values, catalog identity and universal frontier rule remain fixed. Exact outer allowances, holding times, formation requirements, costs, missions, Chaos contributions and achievement conditions are proposed design expansion. They are not playtested balance.

## Ready implementation prompts

Use [coding](086_world_claims_coding_prompt.md), [assets](086_world_claims_asset_prompt.md), [decisions and missions](086_world_claims_decision_mission_prompt.md), [achievements](086_world_claims_achievement_prompt.md), and the [copy-paste `/goal`](086_world_claims_goal_prompt.md). The goal is checked against the required 3,500–4,000-character range.

Specialist assignments are in the [bounded subagent handoffs](086_world_claims_subagent_handoffs.md).

## Review and validation status

[All 60 engine acceptance scenarios](validation/acceptance_matrix.md) remain explicitly marked pending. [The parent review](validation/parent_design_review.md) records design interpretations and unresolved gates. The original planning delivery records forty passing [abstract tests](validation/abstract_contract_tests.py) in its [dated results](validation/abstract_test_results.json). They test a limited logical model and do not prove native Compliance isolation, hooks, exact continuity, GUI behavior or multiplayer support.

Run the abstract examples from the repository root with:

```text
python docs/specs/086_world_claims_specs/validation/abstract_contract_tests.py
```

The most important engine gates are claimant-specific Compliance, exact uninterrupted control/Compliance history, sparse persistence and country epochs, native-provider compatibility, and prepared exact-state display coverage. Runtime files, final assets, UI reference images, exact installed-state mappings, the complete geographic identity inventory, and in-game validation are not produced by this package.

## Source-reading disclosure

The 22 September draft read its 42 supplied files and six repository files; installed game files, the full offline wiki, the workbook and provider implementations were only partly inspected, and no specialist or HOI4 tool ran.
The [source audit](source_review/source_reading_audit.md) and [hash manifest](source_review/source_manifest.json) keep that provenance.

Names, flags and map pieces are prepared engine-compatible resources selected from dynamic territorial results, not images or GUI nodes created during play.

## Revision log

### 2026-10-10 spec audit

- Removed the obsolete planning-package structure check (`validation/package_check_report.json`) and refreshed `package_manifest.json` for the current files.
- Replaced Codex-specific `collaboration.spawn_agent` and `fork_turns` wording in the coding prompt with the repository's subagent routing, and condensed the source-reading disclosure.
- Pass 2 review retained the design: claims follow owned frontiers, integration uses native Compliance, and each Evolution changes reach, starting Compliance or core timing rather than adding a new meter.
