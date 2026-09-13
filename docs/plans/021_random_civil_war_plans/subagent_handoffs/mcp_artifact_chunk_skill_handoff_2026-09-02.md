# MCP artifact chunk skill handoff

## Files changed

- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `docs/plans/021_random_civil_war_plans/subagent_handoffs/mcp_artifact_chunk_skill_handoff_2026-09-02.md`

## Short diff

Added a reusable paragraph to the existing `MCP evidence in handoffs` subsection covering untrusted stringified-JSON resource envelopes, encoding/type inspection, small `?offset=<bytes>&length=<bytes>` reads, `continuationURI` tails, range and metadata preservation, invalid-character and truncation checks, per-chunk decoding, ordered reconstruction, and declared-type validation before display. It explicitly forbids printing base64 and substituting artifact regeneration for retrieval recovery.

## Scope and validation

No gameplay, runtime, configuration, generated-agent, or server files were changed.

No further MCP calls were made; the guidance uses only the observed `read_mcp_resource` tool and artifact-template continuation contract supplied for this maintenance task.

The official skill validator was run against `.agents/skills/chaos-redux-subagents` and returned `Skill is valid!`.

No commit was created, as requested.
