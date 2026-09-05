# Event catalog skill schema alignment handoff

## Documentation review, 2026-09-05

Disposition: unresolved.
Historical skill-edit record. Its thirteen-column Events contract and slot-level Cluster Memberships ownership remain distinct from the fourteen-column spreadsheet handoff. Current workbook reconciliation is outside this documentation task. The original unavailable-skill statement confuses the registered chaosx_skill_maintainer subagent with a skill. Current routing uses that canonical subagent and the owning skill-creator guidance, without inferring that the earlier session exposed the agent.
See the [shared-plan review](../../repo_cleanup/subagent_handoffs/2026-09-05_shared_plan_dispositions.md) for the source ledger, cross-document conflicts, and evidence limits.

## Retained record

## Scope

Updated only reusable skill guidance for the current Chaos Redux event catalog workbook schema.

No gameplay, localisation, workbook, CSV export, generated-agent, or asset files were edited.

## Changed skill files

- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/xlsx/SKILL.md`

## Reusable rule

The one-row-per-event `Events` sheet contains `ID`, `Event Name`, `Details`, `Evo I`, `Evo II`, `Evo III`, `Evo IV`, `Evo V`, `World-End Scenario`, `Type`, `Chaos level`, `Cluster ID`, and `Status`, with no scalar `Member Severity` field.

When one event belongs to several distinct clusters, its `Cluster ID` cell stores the distinct cluster IDs as a comma-separated list.

Exact membership slots, including intentional repeated event-cluster slots, and slot-level severity belong in `Cluster Memberships`.

The `Clusters` sheet aggregates aligned member IDs and member severities, so repeated membership slots must not be silently deduplicated.

## Validation

The full `AGENTS.md`, both changed skill files, and the official `skill-creator` guidance were read before editing.

The offline Paradox Wiki core pages required by `AGENTS.md` were consulted before editing.

The skill validator passed for both changed skill folders with no scaffold or frontmatter errors under `python -X utf8`; the default Windows invocation could not decode the existing UTF-8 source with its cp1252 default.

Targeted searches confirm that the obsolete `Events`-sheet `Member Severity` guidance is removed and the three-sheet catalog boundary is stated in both skills.

The repository-provided `chaosx_skill_maintainer` skill was unavailable in the loaded skill catalog, so the official `skill-creator` guidance was used as the maintenance fallback.

No HOI4 MCP route was needed because this patch changes reusable documentation guidance only and does not document a live MCP-backed surface.
