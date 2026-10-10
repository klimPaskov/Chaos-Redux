# Event 039 retirement transaction closeout, 2026-10-07

Disposition: bounded implementation and source validation complete, Event 039 and native acceptance incomplete.
Acceptance basis: the active user goal requires exact character authorization, protected-character preservation, duplicate prevention, rollback, cleanup and outcome-only Chaos accounting.
The previous goal turn made progress by committing the launch scope correction `04f15a662`.
Current implementation and subsequent commits were inspected before this repair, including the later ruler, inheritance, country and terminal work.

## Implemented behavior

The opening murder, foreign ruler murder and First Knife capture call `murder_mystery_retire_selected_leader`.
The caller's target ID and generation, exact owner and victim, disposition and protection are frozen before ruler resolution.
The helper requires an installed successor receipt, proves that the sitting ruler differs from the victim, and revalidates the frozen selection before consumption.
The consume API scans the bounded registry without writes, requires exactly one matching ID, and then checks generation, unused state, disposition, role, protection, owner and subject identity.
Named subjects use CHARACTER identity and generic-office subjects use their COUNTRY sentinel in separate branches.
Only an actual row mutation publishes `murder_mystery_target_consumption_committed`.
An existing tombstone flag cannot authorize retirement or compensation.
After native retirement, the victim must leave the recorded owner's roster and the verified successor must remain recruited before a committed removal receipt is published.
If retirement leaves the victim recruited, rollback restores only this transaction's exact consumed row.
A missing victim retains its tombstone if another postcondition fails.
The synchronous recursion guard and private rollback inputs clear at normal exit, and selection cleanup clears public result receipts.
Generic capture and office-casualty outcomes also require fresh consumption before accounting.
The opening's mapped Chaos consequence moved from preparation into the successful opening commit, retaining its existing amount and history reason.

Changed gameplay files are `common/scripted_effects/039_murder_mystery_character_effects.txt`, `039_murder_mystery_runtime_effects.txt` and `039_murder_mystery_integration_effects.txt`.
The helper API document and `docs/events/039_murder_mystery.md` describe the new contract.
No new event, scenario, country, portrait, equipment or asset identifier was introduced.
This tranche changes no AI weight, MTTH, random-selection weight or tuning constant.

## Validation and findings

`run_fixture.py` executes six current effect bodies and seven trigger dependencies from actual source under declared native mocks.
All 41 permanent cases pass, including distinct caller/owner/ROOT, protected and owner-managed rejection, generation mismatch, exact rollback, public-selector overwrite, recursion, temporary-variable lifetime, generic sentinels, used-row transitions and duplicate-ID rejection before mutation.
The first run exposed missing consume-time owner, subject and role checks, which were added and rerun.
The independent completion auditor then reproduced a confusion between old tombstone status and fresh consumption.
The separate receipt corrected that defect, and the reproductions are permanent cases.
The auditor independently passed all 41 cases and three additional index/identity cases on the final hashes in `subagent_handoffs/retirement_transaction_review_2026_10_07.md`.
`results.json` records the current physical source hashes and confirms stable bytes throughout execution.
The parent reviewed the fixture's parser boundary, scope rules, native mocks, temporary call-frame cleanup, mutation hooks and independent outcome assertions.

The installed native references establish CHARACTER-scoped retirement and COUNTRY-scoped roster enumeration.
The parent read installed `documentation/effects_documentation.md:6427-6435` at revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, offline `Effects - Hearts of Iron 4 Wiki.md:3815` at revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, and offline `Data structures - Hearts of Iron 4 Wiki.md:263-269,444-480` at revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Vanilla `events/Britain.txt:269-275` promotes a successor before retiring the prior ruler, with file SHA-256 `83741f44f61f18c1bb2731612042878866093e8ba8e701c8ef0ab7a769494f28`.
Additional exact native and wiki citations are retained in the fixture and audit handoffs.

Live MCP `script_validate` supports the declared native retirement and typed identity scopes, with parameters and runtime behavior outside its proof.
Whole-helper validation remains partial because scripted helpers and native argument blocks are unresolved or unchecked, and its omitted findings do not count as covered.
The parent's initial bounded event inspection and narrower retry returned `JOB_WORKER_EXIT`.
The scope render at four nodes timed out after 600 seconds, and the one-node retry also timed out.
The corrected compare request over the three HEAD source overlays, with one-node bounds, timed out after 600 seconds.
That comparison was explicitly current-to-HEAD and did not return a semantic delta.
The auditor's separate render selected zero nodes and cannot establish event or helper coverage.
No MCP event-graph success, live execution, save/reload or Part 18 completion is claimed.

## Remaining scope and deviations

No gameplay simplification or asset substitution was introduced by this transaction repair.
The fixture's native operations are mocks, and complete opening/foreign/capture accounting and successor installation remain outside its execution boundary.
Registry rollback does not undo the predecessor caller's already-installed successor or restore its former political state.
Historical host authorization, the unverified static-Chamberlain attachment, grounded institutional presentation, country viability and rollback, weighted audits, supplied-operation receipts, achievement fidelity, terminal aftermath, assets and the wider Part 18 cases remain unfinished or unverified.
The ENG source audit proposes a guarded, already-recruited Churchill candidate for further implementation review and does not authorize stealing or recruiting an absent identity.
The catalog mismatch was repaired separately in commit `b77059d1d`, including eight workbook cells and their exporter-produced records.
The earlier use of Intelligence ID 20 before workbook reservation is recorded as a reservation-order deviation in the catalog reconciliation note.

Skills used are `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-shared-git-commit` and `xlsx` for the separate catalog tranche.
The reusable distinction between validator status and fresh mutation receipts was added to the events skill through the skill maintainer.
No game process was launched.
