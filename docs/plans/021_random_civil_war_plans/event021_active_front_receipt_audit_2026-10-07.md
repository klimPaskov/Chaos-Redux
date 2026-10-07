# Event 021 active-front receipt and calendar audit, 2026-10-07

Disposition: integer receipt repair implemented; source-backed regression evidence available, with native execution and whole-event acceptance still open.
Acceptance basis: the full Event 021 goal requires proved front receipts, whole force allocation, cleanup and dynamic scaling; the accepted active-war Evolution I addendum requires exact state spans before mutation.
This pass does not change actor eligibility, target weights, AI scores, generation limits, resource budgets, timers, or the public `Needs Testing` status.

## Repair and meaningful evidence

`event021_parent_validate_active_front_row_integers` rejects fractional values in sixteen government-owned row fields before the existing validator can publish transaction readiness.
The fields are front and source IDs, generation, actor type, archetype, goal, route, relationship, four package identity fields, status, division count, state offset, and state count.
The helper uses scratch modulo-one checks without rounding saved data, repairing receipts, imposing an additional numeric cap, or touching scope pointers and fractional asset shares.
Its caller owns and initializes the in/out validity scalar, so a later passing row cannot erase a failure.
Private loop index and break variables prevent this helper from borrowing another loop's control.

`.tools/test_event021_active_front_receipt.py` executes the production validator and its new helper with separate scoped saved state, temporary scalar storage, and temporary arrays.
It discards helper-created storage at return and retains caller-preinitialized outputs.
The pre-repair committed validator accepts a malformed receipt containing two 1.5-state spans whose total remains three states and whose anchors are inside the fractional intervals.
The same regression rejects that receipt after the repair.
The fixture checks every integer column at increments of 0.0001 and 0.5, legitimate integer IDs above 10,000, unchanged fractional asset shares, readiness revocation, ownership and control loss, duplicated IDs and states, misaligned columns, bad anchors, noncontiguous or incomplete spans, capacity exhaustion, and isolation from inherited loop control.
These fixtures do not certify native country creation, force transfer, allocation rounding, map traversal, or rollback.

The calendar regression discovers every `021*.txt` engine surface under `common/` and `events/`, rather than checking only the original five effect files.
It verifies all 44 current date additions use a caller-owned converted day offset, including the active-war Evolution I retry.
The initial 41-site date-unit repair is commit `015a7820a22727a72cc567ea54abd2abed35f303`; the later shared-helper integration is `17f9ac0d0`.
There is no direct whole-day addition to an encoded date among the 44 current deadline additions covered by this audit.

## References and MCP coverage

Installed `documentation/effects_documentation.md`, lines 4986–4998 (`modulo_temp_variable`) and 4279–4295 (`for_each_loop`), revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, establish supported kinds and loop-control syntax.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, line 572, lines 435–442 and 1216–1237, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, cover modulo, conservative helper output lifetime and array iteration.
Installed `common/ai_strategy/USA.txt`, lines 534–550, SHA-256 `17b5f96282381f5e7341e60f1f974be9d6835fe8ddcbcdbf26679941023df819`, is the native scratch-modulo precedent read for this change.
The live whole-file `hoi4.script_validate` route returned `SCRIPT_CHECK_PARTIAL`: 740 commands checked, no reported findings, 352 native argument blocks unchecked, and 33 effect roots with unknown inferred scope, for the pre-repair file request.
An explicit COUNTRY-scope loop excerpt likewise returned partial evidence because the native loop argument block was unchecked.
This is not parameter certification or native execution proof.
The integer-helper source lookup returned a paged and cached definition, so its excerpt alone is not final-source certification.
Final leaf-command and focused event-lint results are recorded separately when the outstanding calls return.

## Whole-goal limits

The independent scripted-system architect returned four further active-war defects: missing caller storage for forwarded candidate arrays, missing caller storage for the measured remnant array, incomplete live-remnant proof between sequential mutation attempts, and incomplete restoration of borrowed transaction globals.
Their repair is accepted and queued under the full goal, after this finished integer-validation tranche; this report does not classify them as solved.
No gameplay simplification, art substitution, numeric cap, allocation shortcut, or timing fallback is introduced by this repair.
The previously approved relation-only external-war fallback is unchanged.
This report does not close the prior Event 006 styled-portrait dependency, workbook alignment, complete numerical probability scenarios, matching MCP rendering and comparison, native scenario performance, or live acceptance requirements.
No game session was launched and no clean live error log is claimed.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
