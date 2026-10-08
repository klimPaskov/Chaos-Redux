# Two remaining biological seed callers: bounded source checks

Date: 2026-10-08.
Disposition: implemented independent bounded source tests and handoff, with 67 passing cases.
Acceptance basis: the parent applied 17 declarations in two existing helpers and assigned independent tests against the exact archives and insertion manifest.
The parent retained gameplay, MCP integration, final review, index, and commit ownership.
This review covers only `missiles_dispatch_biological_payload` and `bio_lifecycle_seed_selected_spread_target` plus their actual reset contract.
It does not establish full eleven-caller coverage or native biological correctness.

## Owned files and execution

- `docs/testing/2026-10-08_bio_remaining_callers_source_tests.js`: new bounded actual-source suite.
- `docs/testing/2026-10-08_bio_remaining_callers_source_results.json`: final working-run captures, source hashes, scoped fingerprints, references, and limitations.
- This handoff: source preservation, behavior findings, evidence boundaries, and parent follow-up.

Command: `node docs/testing/2026-10-08_bio_remaining_callers_source_tests.js`.
Final result: `passed_bounded_two_biological_callers`, 67 cases, zero failures.
All raw loaded inputs remained stable from capture to the end of that run.
No gameplay, historical test suite, shared VM/parser, helper documentation, constants, Git index, commit, extracted tree, game, logs, or MCP artifacts were edited by this agent.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, including the conservative temporary-output lifetime and explicit ownership requirements.

## Source preservation and scoped dependencies

The archive root is `docs/testing/2026-10-08_bio_remaining_callers/`.
Its insertion manifest names eight default fields before each caller's reset and one missile receipt field before the actual `var:missiles_operation_impact_state` dispatch scope.
The test verifies the raw before/after hashes, finds each insertion anchor inside its exact owner, checks the contiguous preceding declarations against the manifest's field/default AST, and removes precisely those three byte spans from the after archive.
The recovered bytes equal the complete raw before archive byte for byte and parse to the original statement structure and order.
The count is exactly 17 declarations across three sites.
None initializes `bio_active_agent`, and no blanket active-agent reset is introduced.

Both current owned helper texts equal their frozen after texts under CRLF-to-LF conversion only, and their unique definition ASTs also match.
Whole-file current equality is deliberately not required for the mixed missile file.
The current actual reset AST equals the archived before reset and has SHA-256 `1cd764ae145be2fad3c63f8038407480133988d2bced75286d47a34251da9384`.
The 35 referenced constant fields are derived from the actual two owner/reset bodies and the explicit four-agent/three-guidance fixture inputs.
Their sorted token-and-field AST fingerprint is `33a3f1fa5d3bcc47ace1b497fe3569e5e05e0f163163c65e7c6f241ee7444376`.
It covers biological route/source/result/proof/math fields, spread clamps and cross-border evidence, the no-retaliation default, missile result/positive-amount guard/payload requirement, all four agents, and the three tested guidance outcomes.
It excludes unrelated missile evolution categories rather than requiring their content in this patch.
The only dynamic token construction exercised by these owners is the actual spread meta actor-variable selector, whose integer agent expansion is recorded in each spread trace.
It constructs a stored actor pointer name, not a constant token.

The unchanged Event 026 parser and `BaseVM` are imported from `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js`, SHA-256 `b048592fb35b86ae2dd915aec0cda54896f7d2f1c1d3a2e358bd2fe3b2e8ccf7`.
They retain the conservative helper-return rule that discards newly created temporary scalars while preserving writes to inherited caller storage.
Actor 7, victim 9, source state 100, and target state 101 have separate regular-variable stores.
Temporary values remain unscoped.
The earlier `2026-10-07_biological_raid_lifetime_source_tests.js` was read for extension patterns but never imported, run, or changed by this review.

## Tested boundaries and results

| Coverage | Cases | Meaningful result |
| --- | --- | --- |
| Raw archives and exactly 17 declarations | 1 | Three recorded blocks reconstruct both complete originals and preserve both current owned helper bodies. |
| Actual reset, scoped constants, unchanged VM | 1 | Reset identity and 35 field definitions remain pinned without importing unrelated mixed-file work. |
| Both caller reset prefixes, before/after | 1 | Each new eight-field allocation survives the actual returning reset. Before storage is absent and the neutral weaponization value reads zero. After weaponization is retained as one and the other seven declared defaults remain zero. |
| Missile four agents × on-target/degraded/site-accident × accepted/rejected receipt | 24 | Actual source supplies the exact target state, actor, victim, agent, strategic route, deliberate source, guidance-mapped result, four supplied proofs, required quantity one, and consumed quantity one. Before an accepted receipt disappears and the operation remains rejected. After only an accepted receipt marks completed. |
| Missile verified-debit flag and positive quantity | 3 | Missing verified flag, zero quantity, and negative quantity skip dispatch and retain rejected result. |
| Spread four agents × actor present/missing × cross-border true/false × accepted/rejected receipt | 32 | Actual record calculations, actor meta pointer lookup, target/controller binding, eight defaults, cursor, source/target pointers, success history and mission gates agree with each declared fixture. |
| Spread lower/upper clamp inputs | 2 | Actual source clamps low intensity/exposure/evidence to 1/0.002/0 and high inputs to 35/0.20/100. |
| Existing mission counter and inactive mission, accepted/rejected | 2 | Accepted active mission increments an existing five to six. Rejection retains five. Inactive mission never creates a counter. |
| Raw run stability | 1 | Every loaded file retains the bytes used by that final run, including the mixed missile file. |

The missile baseline reproduces 12 accepted fixture receipts being dropped at dispatcher return and leaving saved `missiles_operation_delivery_result` rejected zero.
The patched owner retains that receipt through the nested state-scoped call and saves completed four in those 12 accepted cases.
All 12 rejected fixture cases remain rejected before and after.
The receipt stub uses the normal inherited `BaseVM.run` frame rather than bypassing helper-return cleanup.

The spread source calculates seed intensity 20 from 80 × 0.25 and exposed share 0.15 from 0.6 × 0.25 in the matrix fixtures.
Evidence stays 98 without cross-border status and becomes capped 100 after the existing five-point cross-border addition.
Condemnation override remains the supplied 17.
Actor proof is supplied one only when the source state stores the matching agent's actor pointer to existing fixture country 7, otherwise it is missing zero.
Victim scope is the target's fixture controller 9 and victim proof is supplied one.
Spread route/source/result remain connected-spread/spread/spread, with payload proof, use-history proof, batch proof, required amount, consumed amount, concealment, and force-detection defaults zero.
Both callers also retain zero reads for unused base intensity, base exposed share, base evidence, base condemnation, friendly-spread risk, and no-retaliation status.

For spread, the receipt was already declared immediately before dispatch in the original owner, so the test does not invent a new before/after loss for that field.
Under the explicit accepted receipt fixture, target connected-spread history and active-mission counter behavior are the same before and after.
The measurable caller packet change is retained weaponization one and declared zero defaults after reset.
The source agent cursor and both spread state targets remain unchanged.
`bio_outbound_spread_history` is set for every attempted spread, including rejected receipts.
It is an existing attempt marker and does not prove a successful spread.
The achievement callback is captured once per attempt rather than interpreted as an awarded achievement.

## Negative dependency probe

A separate nonwriting probe changes `bio_lifecycle_math.one` from one to two in the test's in-memory constants read.
The scoped constant fingerprint case fails as intended.
The probe disables the result writer, does not modify source or accepted result bytes, and demonstrates rejection of changed exercised input definitions.
The preserved raw archive and current-owner checks remain stricter than this one input probe.

## Raw source identities

| Source | Archived raw before | Archived raw after |
| --- | --- | --- |
| `common/scripted_effects/032_missiles_operations_effects.txt` | `0ce202634f2e78686253483096df2ff76e31a003bcc4e564fae950c255172e2c` | `501f284c7b315776b5b2bfe4a2f422e07d61e68c0ad80f1e3b6c771da7f11c75` |
| `common/scripted_effects/biological_lifecycle_effects.txt` | `9bf1e04826fdde8c745e946af3230b6534707f457777637bda84e0c2f6105450` | `bafa99015ee34357a41aeee1741f715c1b61fe4d299d24cee0c2628fdc6aee11` |

Final tested missile full-file raw SHA-256: `aae2d5d7ab3a3993e266cc1afb6e0cd292974acd8a6362eb17e473fa3f47b08e`.
Its owned biological caller AST SHA-256 is `8a55092655a03af130aebbda14452903e17ebc8e3dbb9aac582d228d626409ef`, matching the frozen after archive.
The lifecycle full-file raw SHA-256 remains its frozen after hash, with owned spread AST SHA-256 `34cd0a6414b62f746ba549a020ccb98204470c0f97e0432b06a80c5af8c6f1c4`.
The missile peer changed unrelated source between earlier test runs and subsequent reads, so the final suite was refreshed once and frozen with its actual run identity.
The test claims end-of-run stability, not whole mixed-file immutability across concurrent work.

Raw loaded constant files are `biological_lifecycle_constants.txt` at `5da904d0c59c1d7051d590223632f33b7dbf576d75765814c3badb3bb54c7c13`, `032_missiles_constants.txt` at `28c66b9d5543126c40bdef4cc717d4229307d7f4c0c79e1ccd17d132b85b837f`, and `cbrn_diplomacy_constants.txt` at `911527dea01211332d1ca1b112c83df6619999631cb80a04f16c44f6ac4af70b`.
The result JSON retains those raw identities plus every archive, manifest, and shared VM identity.

- Test SHA-256: `afc080d9826b6c39efd80656f0ce7e9dcec2f1ea2708b6ddcc79fb796472f6c7`.
- Result SHA-256: `a93f58a81a11380cf2bbd21aa3ef66704b5e85d3ba69711f33ae96f056627362`.

## References, limitations, and parent follow-up

The offline variable lifetime sections at `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:435-443` were read directly, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:7820-7827` documents `set_temp_variable`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Installed command support does not by itself prove native scripted-call return behavior, so the frame model remains explicitly conservative source evidence.
No MCP route health or engine-validation result is claimed by this test assignment.

Actual execution covers only the two owned caller bodies, the reset body, supported Clausewitz variable/scope/control operations, and the spread meta selector.
The seed dispatcher is an explicit accepted/rejected fixture that captures the entire seed input packet and supplies only a dispatch-status return.
Acceptance is fixture-controlled even when actor proof is missing, which tests caller forwarding and response to a returned receipt rather than native authorization or seed validity.
The real dispatcher, route/agent profile arithmetic, exposure, episode slots, incubation, condemnation, attribution, policy, actual achievements, native outcome selection, missile operation preparation, custody receipts, debit/refund/payment behavior, and lifecycle effects are not executed or certified.
No balance target, probability distribution, or native transaction is tested.
The selected spread owner is invoked directly with supplied target, response, profile and source-state inputs, so random target selection and spread chance are outside coverage.
The scope pointers and controller existence are bounded fixtures, and no persistence across events or saves is established.

The assigned two-caller source test package is complete.
No gameplay simplification or fallback was introduced by this reviewer.
The parent retains independent review, MCP/source integration, documentation reconciliation, remaining caller disposition, and final isolated candidate-tree checks before commit.
