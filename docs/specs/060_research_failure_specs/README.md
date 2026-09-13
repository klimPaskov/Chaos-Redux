# Event 60 Research Failure specification pack

## Package identity

- Event ID: `60`
- Event slug: `research_failure`
- Intended repository folder: `docs/specs/060_research_failure_specs/`
- Package filename: `060_research_failure_specs.zip`
- Event type: Minor Repeatable
- Chaos level: 1
- Cluster: Scientific Research
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

The live Chaos Redux repository, the offline Paradox Wiki snapshot, the installed Hearts of Iron IV documentation, and the installed vanilla game files were not mounted in this environment.
That prevented direct inspection of the current technology graph, exact research-state effects, production-line behavior after technology removal, and the live Event 16 Kruger API.
The specification therefore defines the required behavior and evidence gates without inventing exact engine syntax or technology identifiers.
Implementation may not replace real technology regression with a flat research penalty merely because those checks remain outstanding.
Unsafe technology families must fail closed until their graph and runtime behavior are verified.

The configured Codex subagent bridge was also unreachable in this session and returned an HTTP 404 response during discovery.
No live specialist subagent is claimed to have run.
The parent planning pass applied the written review contracts of the improvement-loop planner, scripted-system architect, decision and mission auditor, probability auditor, asset rules, localisation rules, and event completion auditor directly.
The failed subagent route is recorded in the quality report.

## Extraction

Extract the ZIP at the repository root so that this folder lands at:

```text
docs/specs/060_research_failure_specs/
```

The package contains planning files only.
It does not modify gameplay scripts, assets, localisation, or the authoritative catalog workbook.
