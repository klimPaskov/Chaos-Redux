# Event 056: The Navy

This package is the source planning handoff for Chaos Redux Event 56.

The installed package path is:

```text
docs/specs/056_the_navy_specs/
```

## Design authority and current workflow

The package attributes its premise to the supplied user brief.
The original user message and claim-level acceptance record are not reproduced here, so approval of expanded mechanics remains unresolved until the implementation owner records the supporting user decision or parent acceptance.
Historical planning reviews, catalog snapshots, and package status labels do not establish approval or current implementation.
Use current [AGENTS.md](../../../AGENTS.md), [event guidance](../../../.claude/skills/chaos-redux-events/SKILL.md), [asset guidance](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), and [subagent guidance](../../../.claude/skills/chaos-redux-subagents/SKILL.md) for execution.
The source design remains in the files listed below.

## Specification order

1. `specs/056_the_navy_spec_part_1_core.md`
2. `specs/056_the_navy_spec_part_2_eligibility_and_commissioning.md`
3. `specs/056_the_navy_spec_part_3_fleet_package_catalog.md`
4. `specs/056_the_navy_spec_part_4_repeats_and_evolutions.md`
5. `specs/056_the_navy_spec_part_5_ai_clusters_and_connections.md`
6. `specs/056_the_navy_spec_part_6_chaos_balance_and_performance.md`
7. `specs/056_the_navy_spec_part_7_presentation_assets_and_achievements.md`
8. `specs/056_the_navy_spec_part_8_acceptance_criteria.md`

## Implementation prompts

- `prompts/056_the_navy_asset_prompt.md`
- `prompts/056_the_navy_achievement_prompt.md`
- `prompts/056_the_navy_commissioning_prompt.md`
- `prompts/056_the_navy_coding_prompt.md`
- `prompts/056_the_navy_goal_prompt.md`

## Quality and handoff notes

- `quality/source_reading_ledger.md`
- `quality/catalog_alignment_brief.md`
- `quality/ai_probability_scenario_matrix.md`
- `quality/spec_coverage_matrix.md`
- `quality/improvement_loop_self_review.md`
- `quality/subagent_runtime_blocker.md`

## Source authority

The user-provided Event 56 brief is the event-design authority for this pack. The supplied project mechanics, skills, catalogs, configuration, and subagent definitions govern compatibility and quality.

The supplied CSV catalogs are export snapshots. They are historical evidence for catalog state during the original planning pass and must not be edited as source files. Event and cluster catalog changes belong in the authoritative XLSX workbook during implementation, followed by the repository exporter.

## Planning boundary

This package defines the full event design and implementation acceptance criteria. It does not claim that gameplay code, final localisation, final artwork, achievements, cluster registrations, or catalog workbook updates have already been implemented.

## Changelog

### 2026-10-10 spec audit

- The Famine connection now states the useful direction as well as the forbidden one: a convoy or escort package can break an island blockade famine through Famine's existing convoy and escort test, with no new Event 56 effect. The AI prefers Full Commissioning for such a package when an owned state is under blockade famine, so the AI uses the gift where it matters most.
- Subagent instructions use the Claude-first wording; historical runtime-blocker notes in `quality/` are unchanged records.
