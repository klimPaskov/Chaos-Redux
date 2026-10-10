# Event 025 seizure restitution, 2026-10-07

Disposition: bounded source repair implemented, independent audit and native acceptance pending.
The acceptance basis is the user's persistent Event 025 objective requiring exclusive persistent fragments, valid rival outcomes, counterplay and cleanup, together with spec006's temporary captured-crew resources and spec014's resource, persistence and diplomacy requirements.
This repair does not accept the takeover's unrelated reward, default-enablement or completion claims.

## Repair and ownership

`chaosx_nr25_take_seized_material` keeps one targeted Boolean claim per victim, seizer and fragment slot instead of overwriting a single slot variable.
It deducts at most the existing victim crew up to `chaosx_nr25_incident.seizure_crew_limit` and accumulates an actual per-seizer detention receipt.
It cannot create captive crew from a depleted expedition.
Evidence remains bounded by the victim's available survey records.

`chaosx_nr25_demand_seizure_return` stores the answering government's country identity alongside the pending answer window.
`chaosx_nr25_seizure_return_matches_demand` requires valid independent existing governments, the pending demand and its matching seizer identity.
Acceptance and refusal consume that demand before their nested effects.
Repeated, expired, invalid or misdirected answers cannot repeat a crew grant, diplomatic effect, pressure change or report.

`chaosx_nr25_return_seized_fragments` examines exactly six stored victim-specific claims.
Each return uses the existing physical ledger and clears only a positively returned claim.
Unrelated holdings, another victim's claims and a third-party holder remain untouched.
Unfulfilled claims remain recorded.
The reported fragment count reflects actual successful transfers.
Acceptance releases only the recorded detained crews once and reports their actual count.
No reward technology, core ownership, Event 016 history, formation or unrelated equipment is created.

The new effect and trigger files belong wholly to this repair.
The incident and militarisation effects, incident constant and custody test harness were clean on entry and receive only this repair's edits.
The report localisation and overview contain concurrent unrelated changes, so only the four restitution localisation keys and the restitution overview paragraph belong to the commit.
The paired ledger Markdown describes the bounded caller contract and its limits.
The separate [continuation map](../025_source_of_truth_20261007.md) is the curator's reviewed read-time reconciliation, not a completion certificate.

## Source-executed tests

`python -B .tools/test_event025_seizure_restitution.py` passes twelve cases.
They execute the actual demand, seizure, acceptance, refusal, fragment ledger and militarisation helpers with conservative helper-local temporary cleanup.
Native opinion, threat, delayed event and timed-flag operations are observations, not successful engine executions.

The cases cover all six original slot roles, two seizures from one victim, partial returns, distinct victims, unrelated held fragments, valid refusal, repeated answers, expired or mismatched demands, invalid governments, third-party custody, integer-only legacy migration, depleted detention and crew conservation.
`python -B -m unittest discover -s .tools -p 'test_event025_*.py'` passes 74 tests against the current source.
The first all-six assertion used the wrong role-variable spelling and raised a harness `KeyError`, which was repaired to read the production `fragment_<slot>_role` key before the successful rerun.
The parchment report colour audit finds no colour-bearing report keys after the restitution text changes.
These tests do not validate native scheduling, timed-flag expiry, economics, GUI, multiplayer or persistence through a game save.

## Reference evidence

| Source read | Identity and coverage |
| --- | --- |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 125–126 | MCP section `bb6c6275c19a0ee85057eeb1e04f508b6dccf68ffefaff646276d0a128b3cdcb`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`. Targeted country flags support `@PREV` and one target suffix. |
| Installed `documentation/effects_documentation.md`, lines 4833–4852 | MCP section `538e21a9904d554de4737ee4cbf42e988513632ceb28741ea399f27e3c2babcb`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`. Meta effects construct effects from replacements. |
| Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, line 900 | MCP section `abac3e80364fcc46a40bbd56481b09ea3cfc94bee8048beec5ac48260b4681bb`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`. Country-event delay fields were read. |
| Installed `documentation/effects_documentation.md`, lines 4312–4330 and 6730–6738 | Direct read of the inclusive bounded loop and country-scope flag command. The installed flag section does not document duration argument semantics. |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 429–450 | Direct read of country-ID values, regular variable scope and conservative helper temporary-output lifetime. |
| Installed `events/WTT_china_political_power_struggle.txt`, lines 243–291 | Direct vanilla precedent for targeted country receipts, `FROM` dispatch and support/refusal replies. SHA-256 `fd087ea47db2a39b37b5384ac6c4743e3b91652084cc0aad5a00aea08d34c4dc`. |

The context bundle's omitted sources were not treated as read.
The initial file validation request incorrectly supplied snippet kind and scope with a whole-file path and was rejected by the live schema.
It was retried as an inferred whole-file check.
Trigger-file validation returns `SCRIPT_CHECK_PARTIAL`, `valid = null`, five checked commands, no findings, one unchecked argument block and one unknown-scope root.
Its documentation revision is `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
This does not establish native execution or a validated helper scope.
The earlier helper-name-only snippet returned `SCRIPT_COMMAND_UNRESOLVED` and was not used as coverage.
Effect-file validation also returns `SCRIPT_CHECK_PARTIAL` with `valid = null`, nineteen checked commands, no findings, fifteen unchecked argument blocks and one unknown-scope root against the same documentation revision.
Corrected narrow event tracing of `chaosx.nr25.173` is pending delivery at this record's creation.
No helper-expansion, native background task or standalone viewer capability was assumed.

## Limits and remaining goal work

An earlier overwritten fragment claim cannot be reconstructed from unrelated current custody.
Only the one provable integer legacy slot is migrated, and no crew detention is inferred where its receipt is absent.
The current matching-demand guard does not introduce a per-popup nonce, so separate old and new popups for the same victim/seizer pair are not distinguished beyond the current aggregate unanswered demand.
The existing evidence return is limited by the seizer's current available evidence.
This record does not certify the whole armed-action loop, its AI probability or the full Event 025 completion contract.
The dedicated decision auditor owns a read-only repair audit and will record additional findings separately.
The reward auditor owns the exact Event 016/Event 036 collision baseline and mandatory probability evidence.
GUI state evidence, all achievement scenarios, catalog reconciliation and user-supplied runtime acceptance remain open.
No gameplay fallback or simplification is introduced by this bounded repair.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents` and `chaos-redux-shared-git-commit`.
