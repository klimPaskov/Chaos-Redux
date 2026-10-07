# Biological native raid caller-storage patch

Date: 2026-10-07.
Disposition: implemented source declarations, frozen for independent parent validation.
Acceptance basis: parent explicitly authorized the bounded caller-storage patch following `2026-10-07_biological_raid_lifetime_audit.md` and its exact caller map.
This handoff documents implementation rather than native execution or whole-system completion.

## Changed source and frozen hashes

| File | Declarations | Insertion sites | Frozen SHA-256 |
| --- | ---: | ---: | --- |
| `common/scripted_effects/biological_battlefield_effects.txt` | 25 | 7 | `4c35b1c87c04ca027421a5d1a63f45ae1b42df29e6f65d5c9c2a3846078e7791` |
| `common/scripted_effects/biological_raid_effects.txt` | 16 | 5 | `b05ecae13e35c12b0e227114fa88206753dcb281b0d6fd448dd8f54fa9950080` |
| `common/scripted_effects/biological_sabotage_raid_effects.txt` | 19 | 4 | `f21e979a586b92519642db7e309ef098a2e2733f1d9b0ef6078831be6ee9b9bc` |
| `common/scripted_effects/biological_lifecycle_effects.txt` | 2 | 2 | `3d611e3424da6f221446810f6f4ad49e4065b1a8c066bcf7bec3989038a5d3cc` |
| `common/scripted_effects/cbrn_diplomacy_effects.txt` | 1 | 1 | `60b8c4c70a018328e64f19c8e2c5caf7cbbbfcbb99928f5c0b538b1d53278042` |

Total: 63 existing-name `set_temp_variable` declarations at 19 sites.
The exact insertion manifest is `docs/testing/2026-10-07_biological_raid_lifetime/insertion_manifest.json`.
It records each owner, original character and byte offset, before/after line, reason, field/default map, exact inserted text, and before/after file hashes.
The patch is frozen and no further source edits are planned by this worker.

## Behavior and public caller-output documentation

The declarations give returning helpers caller-owned output storage without introducing a helper, variable family, flag, target, receipt registry, wrapper, new draw, gate, payment, refund, balance value, metadata change, or callback reordering.
Native essential equipment remains the sole payload debit.
All original statements and their order remain byte-identical when the manifest's exact inserted declaration spans are removed.

The 35 residual reset declarations follow `2026-10-07_biological_raid_lifetime_caller_map.json` exactly for primary battlefield release, friendly blowback, strategic target release, strategic attacker accident, and native supply-chain sabotage.
Each of those five owners also declares its `bio_seed_dispatch_status` as missing immediately before its actual lifecycle dispatch call.
No status declaration was inserted into the shared dispatcher as a replay or state mechanism.

The owner API contract for this native path is:

- `bio_battlefield_set_payload_internal` returns required payload, consumed payload, and weaponization into resolver-owned storage.
  Its rejected-reservation consumer owns required and consumed payload locally.
- `bio_battlefield_map_engine_result_internal` returns `bio_battlefield_lifecycle_result` into the primary-release adapter's storage.
- `bio_battlefield_record_failed_attempt_evidence_internal` returns actor-match proof into resolver-owned storage before actor condemnation reads it.
- `bio_strategic_raid_select_outcome_internal` returns `bio_raid_outcome` into storage owned by the strategic resolver before selection.
  The selector already owns the nested failure/success output, so no weighted-selection body changed.
- `bio_sabotage_raid_set_agent_parameters` owns the nested parameter getter's agent, required payload, and required support fields.
  Its resolver owns those forwarded fields plus consumed payload/support, selected result, program weaponization/concealment, and failed-attempt actor-match proof.
- `bio_lifecycle_dispatch_seed` returns acceptance through storage owned by each audited raid adapter immediately before the call.
  Reset output defaults remain documented in the caller map and the audit addendum.
- `cbrn_diplomacy_classify_biological_seed_retaliation` returns `bio_seed_retaliation_status` into storage owned by the accepted seed-dispatch branch.
  Inside that classifier, the generic country classifier returns `cbrn_action_retaliation_status` into locally owned storage.

These contracts are documented in this implementation handoff, the audit, the caller map, and the insertion manifest.
Shared owner overview documentation was not edited because parent ownership limited documentation writes to the implementation handoff and evidence package.
The parent can fold the accepted contracts into the existing owner documentation after independent review.
No constants were added or changed, and no cleanup helper was added.

## Exact locations

Line numbers refer to the frozen source after insertion.

| Owner | After-line starts | Declarations by site |
| --- | --- | --- |
| `bio_battlefield_dispatch_primary_release_internal` | 265, 267, 309 | 1 result, 7 reset defaults, 1 seed-status output. |
| `bio_battlefield_attempt_friendly_blowback_internal` | 379, 402 | 9 reset defaults, 1 seed-status output. |
| `bio_battlefield_record_rejected_reservation_internal` | 469 | 2 payload outputs. |
| `bio_resolve_battlefield_dissemination` | 498 | 4 payload/weaponization/attempt-match outputs. |
| `bio_strategic_raid_dispatch_target_release_internal` | 332, 378 | 6 reset defaults, 1 seed-status output. |
| `bio_strategic_raid_dispatch_attacker_accident_internal` | 385, 408 | 7 reset defaults, 1 seed-status output. |
| `bio_resolve_strategic_raid_outcome` | 589 | 1 selected outcome. |
| `bio_sabotage_raid_set_agent_parameters` | 15 | 3 nested parameter outputs. |
| `bio_sabotage_raid_dispatch_release` | 63, 93 | 6 reset defaults, 1 seed-status output. |
| `bio_resolve_supply_chain_raid_outcome` | 162 | 9 forwarded parameter/result/program/attempt-match outputs. |
| `bio_lifecycle_dispatch_seed` | 853, 855 | 1 biological retaliation output, 1 accepted agent selector. |
| `cbrn_diplomacy_classify_biological_seed_retaliation` | 93 | 1 generic retaliation output. |

## Shared consumer preservation and follow-up

The new `bio_active_agent = bio_seed_agent` declaration is immediately before seed storage inside the existing accepted branch.
The store helper's first existing statement performs that same assignment.
All rejected paths leave any existing outer selector/cursor untouched.
No saved/global name collision was found in the audit.
For already-owned selectors on accepted spread paths, both the old store and the added declaration assign the same selected agent.
For unowned selectors, the dispatcher can retain the value long enough for its post-store detection and scheduler calls.
The selector still follows temporary lifetime, and no permanent cursor is introduced.

The new biological retaliation status declaration is immediately before the existing classifier in the accepted branch.
The classifier already initializes that output to none, so its intended value assignment remains the same.
The shared generic classifier body was not edited.
Only the biological caller's returned-status storage was changed in `cbrn_diplomacy_effects.txt`.

The eleven inventoried non-raid paired consumers remain unchanged: Africa disease seeding and laboratory accident, brilliant-scientist standard release, missiles biological payload, doomsday, facility capture, field test, connected spread, operative release, stockpile accident, and Japan campaign release.
Their caller-side reset outputs and returned dispatch-status ownership were not repaired or revalidated in this tranche.
The two dispatcher declarations are shared by those consumers, and their placement preserves rejected selectors and existing valid inputs as described above.
This source reasoning does not replace independent actual-source fixtures for their full transactions.
The exact owner list and lines remain in the caller map and audit addendum.

## Baseline and write safety

Before the first edit, copied the exact working bytes for all five source files to `docs/testing/2026-10-07_biological_raid_lifetime/before/<source path>`.
`baseline_manifest.json` records their SHA-256 hashes, byte lengths, baseline HEAD `c0f14281546a4b8f38a07349b752bfbd65e4c55d`, and the complete NUL-delimited porcelain status of the mixed working tree.
The capture contains 1,712 status entries and is deliberately not an assumption that unrelated working files belong to this patch.
All five snapshot source hashes matched the earlier audited bytes.

Every edited file was guarded against the exact before bytes and snapshot hash, prepared as a sibling temporary file, checked again for a concurrent source change, and atomically renamed into place.
Insertion removal recovered the exact original source text before writing.
No conflict guard rejected a write.
No Git staging or commit was performed.

## Validation limits and parent review

No tests or broad MCP calls were run in patch mode, as explicitly requested by the parent.
The write guards and reversible insertion accounting establish the intended patch shape, not gameplay acceptance.
The prior 28 isolated strict-frame probes remain audit evidence for the original defect and are not reported as after-patch functional proof.
The parent owns independent AST/source-preservation checks, strict-frame caller execution, seed acceptance/rejection scenarios, shared-interface coverage, and required MCP validation.
Native callback execution, actual reservation collection, outcome cardinality, outbreak protection, later lifecycle ticks, and live consumer behavior remain unproved.
No replay mechanism was added, and all original duplicate guards remain in their original order.

The strategic raid documentation gap about retired staging/refunds remains parent-owned and was not changed here.
No new substantive gameplay gap was repaired or substituted in this patch.
No gameplay fallback or simplification was introduced.
Skills used: events, native raids, subagents.
Skills created or updated: none.
This bounded implementation is ready for parent review, while the overall native warfare goal remains subject to independent validation and the recorded follow-up gaps.
