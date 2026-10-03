# Stored-state scope guidance handoff

Status: implemented within the parent-granted skill-maintenance scope, pending parent review and isolated commit.
Authorization: the parent requested one reusable STATE-versus-COUNTRY correction and this exact handoff path.
No gameplay implementation or validation is claimed.

## Owned change

Only `.agents/skills/chaos-redux-events/SKILL.md` received a skill edit.
The owned content is the four-sentence paragraph at lines 494–497, immediately after `#### Country activation and ROOT` and before `Entering another country scope does not rebind ROOT.`
The existing skill already owns country activation and callback scope guidance, so no new skill or routing change is needed.

Before: no paragraph distinguished a stored STATE pointer from COUNTRY-only existence checks at this location.
The existing callback and transaction ownership guidance remained in place.

After, exact owned paragraph:

```text
Stored state pointers refer to persistent map objects, so do not use COUNTRY-only `exists = yes` inside a STATE scope.
Validate the intended state with an appropriate documented native STATE predicate or registered state marker such as `has_state_flag`, together with its expected state ID using the documented identity semantics.
`scope_exists` is always true for variable scopes and does not validate the stored pointer.
Retain `exists = yes` checks in actual COUNTRY scopes, including a state's owner, controller, or stored country pointer.
```

This does not prescribe a speculative state-existence API, remove legitimate country checks, or put event-specific context into the skill.
Expected identity is deliberately stated without equating a state's internal object ID with its file ID.
AGENTS.md section 1.15 requires an object-specific check, and its country-existence examples remain applicable to actual country pointers.
No AGENTS.md or subagent routing update is required.

## References read directly

Installed reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`.
SHA-256: `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`, matching the parent-supplied revision.

- Lines 2708–2716, `exists`: supported scope COUNTRY and current-country existence semantics.
- Lines 4827–4840, `has_state_flag`: supported scope STATE and registered flag syntax.
- Lines 7450–7471, `scope_exists`: variable scopes are always valid, including the explicit `var:my_var` example.
- Lines 7561–7569, `state`: supported scope STATE and state-ID checking semantics.

Offline reference: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`.
SHA-256: `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`, matching the parent-supplied revision.
Read lines 425–450 for database-object variables, `var:` scope syntax, persistent regular variables, and scoping.
Read lines 1667–1674 for the distinction between internal state object ID and file state ID.

Offline reference: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`.
SHA-256: `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`.
Read lines 32–41, 245–274, 329–335, and 737–756.
The relevant dual-scope table distinguishes numeric state scope, country scope, COUNTRY-valued `owner` and `controller`, and type-dependent variable scope.

Required instructions read fully: `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `C:/Users/klimp/.codex/skills/.system/skill-creator/SKILL.md`.

## MCP evidence and limits

The connected tool inventory exposes `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, and `hoi4.source_lookup` in this session.
The live `hoi4.reference_context` call returned `status = ok`, `code = OK`, workspace `mod_chaos_redux_ea3b2d67c2c0`, no blockers, and the matching installed-trigger and Data structures revisions.
Its limited event-surface bundle omitted some broader sources, including Scopes, so it is not proof of complete event-reference coverage.
The pertinent Scopes sections were read directly as listed above.
Targeted `hoi4.reference_search` calls for `exists`, `has_state_flag`, and `scope_exists`, plus revision-bound `hoi4.reference_read` calls for installed-trigger lines 2708, 4827, 7450, and 7561, did not deliver results during the worker's bounded wait.
The pending read-only orchestration cells were terminated before final delivery.
This is a search/read retrieval gap, not an absent namespace or proof that the server is wholly unavailable, because the context route succeeded.
The exact local sections and hashes above supply the documentation evidence for this correction.
Local source review and reference retrieval are documentation evidence, not engine execution or live-game validation.
No server was launched, no resource handshake was attempted, and no missing capability was invented.

## Validation and preservation

Ran `python -X utf8 C:/Users/klimp/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/chaos-redux-events`.
Result: exit 0, `Skill is valid!`.
Manual review confirms the paragraph captures only the documented syntax and scope distinction and preserves country checks.

Skill bytes before this worker's patch: SHA-256 `9FC79849CBDCFD8AEA8BEAE63CF6D4AE2985B8B1E03463E802B25A2FD7AEC12D`.
Skill bytes after this worker's patch: SHA-256 `5EFC1CF17534F01A5367929328412C2B2D86E14AE623B8D7973D677D769D61E6`.
The complete in-memory before/after comparison removed the owned paragraph and found identical existing text apart from one blank separator at original line 493 changing from CRLF to LF during `apply_patch`.
Restoring only that separator in the comparison reproduces the original bytes exactly, so existing mixed-work paragraphs and their other line endings are preserved.
The parent should isolate only the paragraph insertion and this handoff for its later commit, excluding the separator normalization if desired.

The existing callback ownership guidance, identified by the parent as committed in `464841023d34ba11dd39d42d36accb5c62c00959`, was not rewritten.
That commit attribution was supplied by the parent and was not independently inspected because this assignment forbids Git operations.
Existing option-audit and history-ownership additions were preserved without assuming ownership of their staged or unstaged state.
No Git, staging, config, generator, mirror, other-skill, gameplay, asset, localisation, workbook, game, or log work was performed.

## Parent handoff

Review the four-sentence insertion and commit only the finished owned hunk plus this handoff through the parent's isolated-index workflow.
Skills used: skill-creator, chaos-redux-events, and chaos-redux-subagents.
Skills updated: chaos-redux-events only.
Skills created: none.
Other skills and AGENTS.md: unchanged.
No implementation simplification was made, and engine validation is outside this documentation-only assignment.
Completed: the owned skill paragraph, official skill validation, preservation comparison, and this handoff.
Blocked evidence: targeted MCP search/read delivery remained unresolved and is not claimed as completed.
Remaining authority: the parent reviews and performs the later isolated commit.
