# Event 60 Research Failure specification pack

## Design authority and current workflow

The package attributes its premise to the supplied user brief.
The original user message and claim-level acceptance record are not reproduced here, so approval of expanded mechanics remains unresolved until the implementation owner records the supporting user decision or parent acceptance.
Historical planning reviews, catalog snapshots, and package status labels do not establish approval or current implementation.
Use current [AGENTS.md](../../../AGENTS.md), [event guidance](../../../.claude/skills/chaos-redux-events/SKILL.md), [asset guidance](../../../.claude/skills/chaos-redux-event-assets/SKILL.md), and [subagent guidance](../../../.claude/skills/chaos-redux-subagents/SKILL.md) for execution.
The source design remains in the files listed below.

## Package identity

- Event ID: `60`
- Event slug: `research_failure`
- Intended repository folder: `docs/specs/060_research_failure_specs/`
- Package filename: `060_research_failure_specs.zip`
- Event type: Minor Repeatable
- Chaos level: 1
- Cluster: Scientific Research
- Reserved cluster ID: `21`, from the [shared identifier registry](../shared_identifier_registry.md). This reserves identity only and does not approve membership or activation.
- Cluster role: High member
- Source status at planning time: To Be Reworked

## Design summary

Research Failure is a severe national crisis in which one valid major country or player-controlled country loses effective scientific capacity, current research work, and a broad but safe selection of previously researched technologies.

The event treats technology as an institutional achievement that depends on trained people, working laboratories, verified standards, production knowledge, records, and repeatable methods.
Existing equipment and buildings do not vanish when a technology is regressed.
The affected country instead loses the reliable ability to reproduce, improve, verify, or replace some advanced systems until the relevant knowledge is rebuilt.

The recovery loop uses two visible values:

- **Scientific Capacity**, which represents working institutions, personnel, facilities, and coordination.
- **Archive Recovery**, which represents recovered records, verified methods, design series, calibration chains, and the ability to rediscover lost technologies efficiently.

The normal floor is two research slots.
Evolution III reduces the target to one research slot.
A valid Kruger Directorate may preserve its current slot count by accepting an emergency mandate that strengthens the Directorate at a severe political and institutional cost.
The exemption does not prevent research-speed damage, active-project loss, or technology regression.

## File index

### Source specifications

- `specs/060_research_failure_spec_part_1_core.md`
- `specs/060_research_failure_spec_part_2_technology_regression.md`
- `specs/060_research_failure_spec_part_3_reconstruction.md`
- `specs/060_research_failure_spec_part_4_evolutions_connections.md`
- `specs/060_research_failure_spec_part_5_ai_balance_edge_cases.md`
- `specs/060_research_failure_spec_part_6_presentation_assets_achievements.md`

### Design matrices and acceptance evidence

- `matrices/060_research_failure_decision_map.md`
- `matrices/060_research_failure_ai_probability_matrix.md`
- `matrices/060_research_failure_technology_registry.md`
- `matrices/060_research_failure_chaos_impact_map.md`
- `matrices/060_research_failure_acceptance_scenarios.md`

### Research and quality records

- `research/060_research_failure_research_basis.md`
- `quality/060_research_failure_source_reading_manifest.md`
- `quality/060_research_failure_design_review_and_blockers.md`
- `quality/060_research_failure_catalog_alignment_handoff.md`
- `quality/060_research_failure_package_validation.md`

### Implementation prompts

- `prompts/060_research_failure_asset_prompt.md`
- `prompts/060_research_failure_achievement_prompt.md`
- `prompts/060_research_failure_decision_mission_prompt.md`
- `prompts/060_research_failure_technology_system_prompt.md`
- `prompts/060_research_failure_coding_prompt.md`
- `prompts/060_research_failure_goal_prompt.md`

## Authority and source limits

The accepted event brief in the user request is the primary design authority for Event 60.
The supplied Chaos Redux mechanics, skills, catalogs, registries, configuration, README, and every extracted subagent definition were fully read before this pack was written.

The live Chaos Redux repository, the offline Paradox Wiki snapshot, the installed Hearts of Iron IV documentation, and the installed vanilla game files were not mounted in the original planning environment.
That prevented direct inspection of the current technology graph, exact research-state effects, production-line behavior after technology removal, and the live Event 16 Kruger API.
The specification therefore defines the required behavior and evidence gates without inventing exact engine syntax or technology identifiers.
Implementation may not replace real technology regression with a flat research penalty merely because those checks remain outstanding.
Unsafe technology families must fail closed until their graph and runtime behavior are verified.

No live specialist subagent ran during the original planning pass; the quality report records that route and the review contracts the parent applied directly.

## Package location

The installed source folder is:

```text
docs/specs/060_research_failure_specs/
```

The package contains planning files only.
It does not modify gameplay scripts, assets, localisation, or the authoritative catalog workbook.

## Open questions

- `unresolved`: the three Event 54 interaction choices in Part 4. Recommendation, shared with the Event 54 package: keep Event 54's equal random draw with no lost-technology priority, give gifted nodes no protection from later safe regression, and run Event 60's rollback before Event 54's grant inside one Scientific Research episode so a same-episode gift can only restore, never be erased.

## Changelog

### 2026-10-10 spec audit

- Starting Scientific Capacity and Archive Recovery bands rise at baseline (Capacity 35 to 45, Archive 15 to 25) and Evolution I and II, while Evolution III is unchanged. This is a Minor Repeatable event at Chaos level 1 that can hit a player more than once; starting in the three-fifths-slower band plus technology regression left the evolutions little room to escalate.
- Secondary incidents are capped at two per crisis, each at most once, and only incidents whose cause is present can fire. Seven incident types without a budget would turn a long reconstruction into popup churn.
- The README no longer repeats the original planning environment's subagent failure; the quality report keeps it. Subagent instructions use the Claude-first wording.
