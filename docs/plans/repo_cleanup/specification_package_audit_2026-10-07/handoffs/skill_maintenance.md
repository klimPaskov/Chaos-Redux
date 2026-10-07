# Specification audit skill maintenance

## Scope and disposition

Disposition: implemented reusable skill corrections within the parent-authorized documentation audit.
This handoff does not establish approval or implementation of event design, identifier reservations, or gameplay.
Only the two assigned skill files and this handoff were edited.
Existing unstaged edits in the subagents skill were preserved; no staging, commit, generated-runtime synchronization, gameplay edit, or AGENTS.md edit was performed.

## Changed skills and rationale

| Skill | Exact change | Recurring failure prevented |
| --- | --- | --- |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | Three evidence bullets under Documentation curation agents. | Historical archive hashes and dated QA results mistaken for current checkout validation; duplicate compilations maintained as independent authority; mutable workflow copies and dated capability reports treated as current instructions. |
| `.agents/skills/chaos-redux-event-planning/SKILL.md` | Source authority and shared identifiers subsection after Required reading. | Extending a duplicate or historical source without identifying authority; independent package allocations colliding with runtime IDs or other proposals; public-only inventories missing hidden entries; conflating scenario namespaces or sort values. |

The planning rule requires occupancy checks against active packages and reservations, implemented registries/constants including hidden entries, and the canonical workbook.
It distinguishes event, manual scenario, world-end registry, cluster, and display/sort namespaces.
Proposed reservations must be recorded centrally with namespace, owner, status, and evidence before consumers use them.
Reservations do not establish design acceptance or runtime registration, and implemented IDs remain stable while colliding proposals are remapped with their references.

No skill was created.
Other skills were left unchanged.
The existing fork-context rule already uses `fork_turns="none"`; the curation addition makes checking active prompt copies explicit without changing runtime spawning or role ownership.
No AGENTS.md routing change or generated agent-definition change is needed.

## Grounding evidence

- `AGENTS.md`, Specs and Plans, Skill Maintenance, and spreadsheet source/export rules: acceptance and implementation are separate evidence; existing skills are preferred; the XLSX is the canonical catalog source.
- `.agents/skills/chaos-redux-subagents/SKILL.md`, Fork context rule and Documentation curation agents: current Codex no-inheritance argument and established curator authority.
- `.agents/skills/chaos-redux-event-planning/SKILL.md`, Required reading, Specification shape, and Output rules: existing design baseline, canonical part structure, and package authority conventions.
- `docs/plans/repo_cleanup/specification_package_audit_2026-10-07/brief.md`, Audit contract: historical versus current inventory scope, owner-skill links, reference-safe duplicate consolidation, and current capability discovery.
- `docs/plans/repo_cleanup/specification_package_audit_2026-10-07/handoffs/055_060.md`, Dispositions and Validation: all 27 combined-copy bodies checked against separate sources; original ZIP receipt preserved; obsolete active spawn arguments corrected; current inventories refreshed separately from historical receipts.
- `docs/specs/057_the_black_market_specs/PACKAGE_MANIFEST.md`: explicitly retained original supplied-ZIP bytes and hashes after checkout edits.
- `docs/specs/060_research_failure_specs/quality/060_research_failure_package_validation.md`: original environment failures and review claims labeled historical, with current health and checkout validation excluded.
- `docs/specs/031_random_terror_specs/031_random_terror_complete_spec.md`: successor pointer to canonical numbered parts rather than another editable compilation.
- `docs/specs/031_random_terror_specs/031_random_terror_manifest.json`: a proposed manual scenario identifier differs from the implemented ID for the same named scenario in `common/script_constants/chaosx_triggerable_scenarios_constants.txt`.
- `common/script_constants/world_end_scenario_registry_constants.txt`: distinct world-end IDs and hidden/public visibility definitions show why a public catalog is insufficient for runtime occupancy.
- `common/scripted_effects/chaosx_event_cluster_effects.txt`: shared cluster initialization and definition registry establish the runtime allocation surface.

The parent supplied the repeated cross-package collision finding and the intended central ledger path.
This subtask does not claim to have re-audited all ID occupancy or the workbook contents; the new skill requires that check for future allocations.
No engine syntax or behavior was changed or asserted, so engine-reference and MCP domain validation were outside this skill-only scope.

## Preserved before-source evidence

Before editing, both current skill files were copied byte-for-byte under `C:/Users/klimp/AppData/Local/Temp/chaos-redux-specs-audit-yijvocg9/skill_before/`, preserving their repository-relative paths.

| Relative path | Pre-edit SHA-256 |
| --- | --- |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | `338848510239626FE63A81C117FA96C9228AEA0D211BC86B992F0B432B0F35FC` |
| `.agents/skills/chaos-redux-event-planning/SKILL.md` | `798800DAED7178A659C51811384F71F5F15D0C34FBF2C9443D03C596931F4A2A` |

## Validation and parent follow-up

Both skills passed `C:/Users/klimp/.codex/skills/.system/skill-creator/scripts/quick_validate.py`.
Each working skill was compared with its saved current-file baseline using `git diff --no-index`; the subtask diff contains only the documented additions and preserves the pre-existing edit.
The frontmatter, existing routing rules, and unrelated sections remain unchanged.
The rules add no event-specific IDs, design context, or temporary audit history to either skill.

Dependency: the parent must finish `docs/specs/shared_identifier_registry.md` before final integration, or update the planning skill reference if the ledger path changes.
That ledger did not exist at the time of this subtask's validation.
No requested skill guidance was simplified or omitted.
The optional Windows mapped-section troubleshooting note was not inserted because neither owned section has a suitable troubleshooting home.
During shared audits, `rg --no-mmap` avoids ripgrep's mapped-file interference; when a concurrent mapped-section write failure occurs, let the reader release the file and retry the narrow write instead of deleting and replacing the file.
That operational note remains in this handoff pending a suitable reusable troubleshooting owner.
