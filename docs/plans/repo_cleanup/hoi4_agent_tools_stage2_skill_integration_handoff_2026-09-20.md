# HOI4 Agent Tools Stage 2 skill integration handoff

Status: implemented as a documentation patch; live Stage 2 integration remains pending.

## Basis and boundaries

The parent requested a narrow, non-gameplay maintenance pass for the five-stage integration. The separate `C:\Users\klimp\Documents\Projects\hoi4-agent-tools-stage2-qualify` checkout resolves to `b34f042`; its `CHANGELOG.md`, `docs/helper-expansion.md`, and `docs/jobs.md` describe candidate 3.1.0 behavior and state that it is not published or installed. The dispatch says the public package remains 3.0.9. This pass did not verify a new live server, alter the product checkout, restart Codex, interrupt a process, or claim Stage 2 MCP availability.

The offline Paradox wiki core pages and vanilla `script_concept_documentation.md`, `effects_documentation.md`, and `triggers_documentation.md` were consulted before editing. No HOI4 script syntax or gameplay was changed.

## Changed files

| File | Disposition and reason |
| --- | --- |
| `AGENTS.md` | Implemented: one MCP paragraph distinguishes Stage 2's version-gated candidate capabilities from the installed routes and preserves mandatory domain evidence. The parent expressly requested AGENTS wording in this bounded scope. |
| `.agents/skills/chaos-redux-subagents/SKILL.md` | Implemented: the existing routing owner now defines conditional task/job use, page evidence, and handoff boundaries once the server and client are verified. No central MCP skill was created. |
| `.agents/skills/chaos-redux-events/SKILL.md` | Implemented: the released 3.0.9 focused-analysis rule is versioned, and the Stage 2 paged helper route is described as opt-in, bounded source evidence rather than lifecycle or runtime proof. |

No `.codex/agents/*.toml` was changed: existing domain roles already require the owning skills and mandatory MCP evidence, so copying the conditional job contract into each role would create drift. Other owner skills, including focus, decisions, GUI, MTTH, and asset guidance, were left unchanged because the common routing gate covers the new transport behavior and their domain checks remain valid. No new skill was created.

## Checks

- Confirmed the three edited canonical files were clean before this pass and reviewed their focused diff afterward; unrelated dirty gameplay, audio, reports, and documentation files were left untouched.
- Ran `python -B .tools/sync/sync_claude_agents.py`: 20 agents unchanged; all 17 skill mirrors remained existing junctions; `.mcp.json` unchanged. Other runtime agent generators were unnecessary because no canonical TOML changed.
- Ran `skill-creator`'s `quick_validate.py` on both edited skills; both passed.
- Checked Stage 2 candidate documentation against the wording: helper pages are opt-in for event and technology inspection; `finished` differs from `complete`; native tasks require negotiation; ordinary calls remain valid; `hoi4.job_inspect` and `hoi4.job_cancel` are control operations; completed jobs can contain tool-level errors.

## Remaining integration work

- Publish and install the qualified Stage 2 package through the parent-owned release path, then verify the actual live package version, service health, exposed schemas, and client task negotiation. The candidate checkout and public 3.0.9 status do not establish live availability.
- Run a bounded event and technology helper-page example on the installed route, retaining revision, continuation, coverage, and unresolved findings; run a representative persistent read job and inspect its final result. Verify cancellation behavior only against an explicitly selected safe job. Record exact blockers if routes are absent.
- Keep the existing focus, event, technology, probability, GUI, and map inspect/render/compare/scenario obligations when jobs are used. The parent must review any later domain-specific evidence and update profiles with mechanic-specific facts.

No gameplay simplifications or omitted requested file edits were made. Stage 2 live MCP validation is pending because this task was limited to documentation and dispatch did not establish an installed Stage 2 server.
