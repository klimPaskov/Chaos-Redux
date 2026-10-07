# Independent chemical caller-storage source checks

Date: 2026-10-07.
Disposition: implemented bounded source tests, passed and frozen for parent review.
Acceptance basis: parent requested independent tests of the chemical architect's frozen caller-storage patch.
Ownership: the test, its result JSON, and this handoff only.
No biological source, chemical source, shared VM, existing tests, shared documents, Git index, or commits were changed.

## Files and run

- `docs/testing/2026-10-07_chemical_raid_lifetime_source_tests.js`, SHA-256 `262e684c6ca70fad462e82563c441999ba69adb979e42d791dd960fd7548a33a`.
- `docs/testing/2026-10-07_chemical_raid_lifetime_source_results.json`, SHA-256 `d5b7fe0b3451465f56adeda6719a98653e5a0bd5562905b4b88c31bc587ebad4`.
- This implementation handoff.

Command: `node docs/testing/2026-10-07_chemical_raid_lifetime_source_tests.js`.
Result: 18 tests passed, zero failures.
The results retain every source hash, per-test before/after observations, named fixture boundary, and precision limit.
No source defect was confirmed by these bounded tests.

## Evidence covered

The test reads the frozen source and insertion manifests, original action-lifetime insertion map, raw before/after archives, and the exact current source.
All 206 scalar declarations and the one temporary-array initializer were removed by their recorded byte spans.
The resulting bytes equal the archived before bytes exactly for all eight inventoried source files, and their parsed ASTs equal the original ASTs.
Live working source equals archived after source under newline normalization only.
The evidence-root `.gitattributes` explicitly protects the raw before and after archives with `-text`.

This preserves the original statements, values, helper calls, scopes, weighted bodies, native reservation fields, and duplicate guards.
No source-preservation assertion uses HEAD as a substitute for the actual mixed working baseline.

| Regression probe | Archived before | Repaired source |
| --- | --- | --- |
| Three full-record owners | Zero public packet fields retained after the returning producer | All 60 fields retained. Land and exact-state doomsday reset defaults checked individually, including the two mask-only multiplier defaults. Air reservation runs its actual returning chain. |
| Land agent/class, severity and payload getters | Returned values dropped | Chlorine class, cylinder severity and exact 40-unit cylinder requirement retained from their actual helpers. |
| Air reservation | Public/forwarded fields lost | Actual successful agent classifier, result selector, consumption/dose getter and reservation resolver retain result, release proof, reservation proof, and positive native-consumption record. |
| Eighteen existing route/class/exact-agent outputs | Existing allocation preserved | Actual profile helper returns retain all eighteen slots using the unchanged exposure caller prefix. |
| Six protection weights for each of four classes | All six weight outputs dropped, fixture effective score zero | All six retained. With respiratory zero and other layers 100, actual calculator gives scores 45, 90, 75 and 55 for choking, blister, nerve and incapacitating classes. These are return-regression observations, not a balance recommendation. |
| Accepted dispatcher called twice | Two captured history applications and lost private outputs | One application, retained source context 102, evidence floor 75 and fixture civilian-death result 25. Original supplied-proof guard survives return. |
| Rejected, unpaid or unbound record | Not a claimed repaired native scenario | Actual dispatcher gate produces zero sink applications for each explicit case and leaves missing dispatch proof. |
| Failed-attempt dispatcher called twice on a supplied resolved record | Two captured attempt rows, evidence remains 50, attribution output lost | One row, evidence advances to 70, probable attribution 2 retained, and actual attempt outputs 20 evidence points, 35 floor and 8 condemnation base survive. |
| Doomsday target getter | Count and target array lost on return | Two supplied exact state pointers and count two retained. |
| Doomsday stock and condemnation getters | Returned arsenal and condemnation lost | Four real-source 3-unit remaining-stock debits, then four assumed already-native-reserved units recorded without being debited again. Total recorded arsenal 16 survives, batch condemnation and proportional quarter share survive. |
| Chemical doomsday event bridge | Returned status lost, no captured news | With a declared successful release sink fixture, retained returned status allows exactly one captured conditional news call. |

The regular actor, state and victim dictionaries remain separate from unscoped temporary storage.
The existing strict helper cleanup implementation from Event 026 is imported unchanged and drops temporary scalars/arrays first created inside each returning helper.
The new test extends only task-specific command adapters for scopes, clamp/round, persistent state mutation, and captured native sinks.
It does not introduce another general interpreter or report framework.

## Neighboring and uncommitted work

The original exposure file and entirely untracked payload-reservation file remain byte-identical to their captured working baselines.
The original protection source was already dirty and retains its previous allocations exactly after removing only the six weight declarations.
The preservation check covers the existing eighteen exposure-profile outputs, six generic protection outputs, and two payload authorization metadata outputs without claiming them as this chemical patch's work.

The test captures and uses `cbrn_exposure_effects.txt`, `cbrn_protection_effects.txt`, and `cbrn_payload_reservation_effects.txt` as working dependencies.
The last file has no HEAD/index entry in the supplied baseline manifest.
Successful local tests therefore do not prove a committed checkout contains that dependency.
The parent must decide which existing dirty/untracked dependencies belong to the integrated commit and validate that committed consumer set separately.
No staging was performed here.
Missile and camp owners remain unchanged and untested by this suite.

## Explicit fixture and coverage limits

Full-record tests execute the actual allocation/reset/reservation prefixes within the consuming owner frame, rather than complete native land/air/doomsday outcome transactions.
The real action agent-validity and class-match triggers execute on the supplied record.
Exact target eligibility and actor identity remain declared context fixtures.
The failed-attempt case explicitly supplies a resolved, positive native-consumption record and zero release-efficiency result to isolate its private return and duplicate guard.
This is not a native payment observation.

The dispatcher guard, supplied proof assignment, private declarations, source/context getter, evidence-floor getter, and first civilian-death branch of the actual state-consequence helper execute from parsed source.
The population/death sink returns a fixed fixture 25, while unit damage, shock, condemnation and record/history applications are captured sinks.
The rest of state consequences is deliberately excluded from that private-output probe.
It does not certify real deaths, disruption, contamination, medical saturation, balance, or all record columns.

Doomsday collection uses two supplied eligible state pointers, without a real ownership/policy search.
The real arsenal getter mutates a concrete fixture stockpile, and the real batch/share getters calculate forwarding values.
Complete four-agent, multi-state remainder allocation and full release acceptance are not executed here.
The event bridge release producer is a named successful sink fixture whose return follows conservative caller lifetime.
Its news count proves the new event-owned status boundary, not actual catastrophe/news execution.

Meta event scheduling is captured, not executed by the engine.
No random-result or random-dose branches are evaluated because the air forwarding case uses native success.
The source tests are not probability evidence.
Nineteen unrelated constants finer than five decimal places are not loaded into the existing five-decimal VM, and all selected tested helpers pass without requesting one.
An attempted reference to such an unsupported constant would fail rather than invent a value.

Early test runs found fixture issues with ID literals, bridge scope bindings, shorthand array parsing, and a release sink's missing frame cleanup.
Those fixture issues were corrected in the owned test file, and no gameplay patch was made to satisfy the test.
The final results reflect the frozen test and current source hashes.

The parent owns MCP before/after evidence, broader transaction/protection validation, documentation integration, commit composition, and final completion claims.
Native execution remains unproved.
No game launch, logs, MCP call, payment/refund invention, gameplay fallback, or simplification was introduced.
