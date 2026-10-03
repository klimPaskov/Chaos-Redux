# Event 025 physical-custody transaction tranche

Disposition: implemented for the bounded transaction layer; accepted policy caller wiring remains queued.
Acceptance basis: the user's complete Event 025 request explicitly requires exclusive persistent fragments and Evolution V transfer/destruction, consistent with specs/006 and the section 8 and 23 acceptance gates.
This is a parent-reviewed source tranche, not a returned independent architect handoff or an Event 025 completion pass.

## Implemented transaction behavior

Historical winner identity is separate from physical core custody.
Public field acquisition cannot overwrite a living owner or recover a permanently destroyed fragment.
Every ownership mutation rebuilds both country fragment counts and six aligned owner/role rows.
The two acquisition callbacks no longer add a second count after ledger reconciliation.
Transfer validates both recipient identity proofs and giver-specific consent, preserves existing recipient fragments, moves all sender-held material without cloning it, consumes permission, and clears the input selection.
Destruction retires only the caller's material and does not revoke researched technology or historical winner receipts.
Invalid physical targets are cleaned through six slots without erasing historical reward state or scanning the world.

## Changed surfaces

- Physical-custody and fragment helper blocks in `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt`.
- Fragment input and custody proof blocks in `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt`.
- The two fragment-acquisition success callbacks in `common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt`.
- The paired ledger contract document and `.tools/test_event025_custody.py`.

Other uncommitted reward-bridge and Event 036 overlap hunks in these mixed files are not part of this tranche.
They remain pending owner-API review and baseline/post-patch weighted evidence.

## Validation

Eight source-execution tests cover six-slot exclusivity, repeated acquisition, invalid integer/role inputs, consent consumption, existing recipient material, missing/wrong consent, wrong recipient ID, subject/capitulated/annexed recipient, war, self-transfer, corrupt role, repeated transfer, permanent destruction, preserved history, invalid-owner cleanup, aligned projections, and acquisition caller count integrity.
The pre-existing 25 recovery/lifecycle/evolution callback tests must also remain passing.
The test interpreter explicitly does not emulate scheduling, rendering, diplomacy, external technologies, multiplayer, or save/reload.

Installed `documentation/effects_documentation.md` meta_effect lines 4833–4852 and for-loop documentation previously retained by the parent support the bounded substitution/loop pattern.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` targeted flags lines 112–125 and global event targets lines 267–285 were read directly.
The vanilla `common/scripted_effects/CZE_scripted_effects.txt` meta-effect examples at lines 442–470 were inspected as structure precedents.
Source SHA-256 revisions: effects documentation `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`; Data structures wiki `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`; vanilla CZE effects `cb5ee5136b5759efe4caaaace23189964fce57af18558d0ac535336ea93319c6`.
MCP reference_read of the exact meta-effect section timed out after 600 seconds; the narrower four-line retry also timed out after 600 seconds.
Mandatory MCP event, technology, probability and GUI evidence remains incomplete and is not replaced by these source tests.

## Remaining work and omissions

Neither transfer nor destroy is a finished playable policy route yet.
The current policy executor does not consume these transactions, and recipient permission UI, route/preparedness checks, costs, cooldowns, Dependence transfer, diplomatic effects, and confirmation/result text remain required.
The pending reward-bridge edits, Event 016 missing-base-first ordering, exact aircraft/propulsion family mapping, and Event 036 direct holder seam remain outside this tranche.
No simplification or fallback is accepted through this handoff.
