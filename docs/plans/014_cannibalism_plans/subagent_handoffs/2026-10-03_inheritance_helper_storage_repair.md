# Event014 bounded inheritance helper storage repair

Date: 2026-10-03.
Owner: patch-capable `chaosx_scripted_system_architect`.
Disposition: implemented bounded source fix for E014-FINAL-01, ready for parent review.
Acceptance basis: the parent's explicit bounded helper-output lifetime repair instruction.
Event014-wide completion, final commit and runtime acceptance remain parent-owned.
No commit or index change was made.

## Delivered changes

Changed engine source: `common/scripted_effects/014_cannibalism_effects.txt`.
Added owner API document: `docs/events/014_cannibalism/inheritance_storage_contract.md`.
Added this handoff and its same-named evidence folder.
`events/014_cannibalism.txt` has no owned escaped-output consumer and is unchanged.

The source patch adds 107 scalar storage assignments across thirteen existing helper definitions and fourteen storage groups, plus output API comments.
All additions allocate output storage in the consuming or forwarding caller itself before nested helpers and donor country scopes.
No initialization helper is introduced.
The three inheritance owners allocate all sixteen donor outputs and ten player-ledger outputs at frame entry.
Later ordinary absorption and primary-donor Wendigo absorption own their nested runtime-migration return.
The runtime migrator owns the spread-migration return.
Spread migration, validation, rebuild, reveal, terminal integration and annex-release paths own their consumed validation/context/return values.
Initial-anchor registration owns the consumption result and actual population loss, and consumption preparation owns the five parameter outputs it forwards into the state helper.
The canonical exact-state population helper already had caller-owned applied-loss/result storage and is unchanged.

All existing inputs, cursor definitions, donor target binding, regular saved variables, origin priority, route rewards, Larder transfer/clamps, both-human Larder zero override, and source eligibility predicates are preserved.
Unused rebuild source-state-loaded output, unused creation/registration results and submission-wrapper results are not hoisted.
No flags become permanent numeric variables and no scoped temporary token is introduced.
No weights, costs, selection scores, AI, GUI, assets, localisation, Larder scaling or Network data helpers are changed.
Provider 523 from parent commit `4c582411` is byte-preserved.

## Exact changed helper hunks

The immutable before source and insertion-only patch are in `evidence/014_cannibalism_effects.before.txt` and `evidence/source_lifetime.patch`.
`storage_boundaries.json` lists every added variable, its default and exact inserted lines.
These source lines refer to this delivered snapshot, before any later parent edit.

| Caller definition | Before line | After line | Added scalar allocations |
| --- | --- | --- | --- |
| `cannibalism_create_unified_country_from_selected_host` | 12393 | 12432 | 26 |
| `cannibalism_absorb_current_warlord_into_unified_host` | 12583 | 12652 | 27 |
| `cannibalism_create_wendigo_unification_from_selected_hosts` | 18813 | 18916 | 26 |
| `cannibalism_absorb_primary_warlord_donor_into_wendigo` | 18738 | 18839 | 1 |
| `cannibalism_migrate_runtime_references_to_unified_country` | 12238 | 12275 | 1 |
| `cannibalism_migrate_spread_entries_between_countries` | 11278 | 11306 | 2 |
| `cannibalism_validate_spread_queue` | 9743 | 9754 | 6 |
| `cannibalism_rebuild_spread_pending_ledgers` | 9967 | 9985 | 7 |
| `cannibalism_execute_evolution_iii_reveal` | 12538 | 12604 | 2 |
| `cannibalism_integrate_terminal_ai_warlords` | 11543 | 11574 | 1 |
| `cannibalism_begin_current_warlord_slot_release` | 5591 | 5600 | 1 |
| `cannibalism_prepare_consumption_context` | 3981 | 3984 | 5 |
| `cannibalism_register_current_wendigo_anchor` | 18489 | 18587 | 2 |

There are also documentation-only API comments immediately before the existing capture, achievement-capture and spread-migration definitions.
Exact insertion anchors, including those comments:

| Before insertion line | After insertion line | Added physical lines |
| --- | --- | --- |
| 377 | 377 | 3 |
| 3985 | 3988 | 6 |
| 5592 | 5601 | 2 |
| 9745 | 9756 | 7 |
| 9968 | 9986 | 8 |
| 11278 | 11304 | 2 |
| 11280 | 11308 | 3 |
| 11544 | 11575 | 2 |
| 12042 | 12075 | 4 |
| 12244 | 12281 | 2 |
| 12395 | 12434 | 27 |
| 12539 | 12605 | 3 |
| 12585 | 12654 | 29 |
| 18491 | 18589 | 3 |
| 18739 | 18840 | 2 |
| 18815 | 18918 | 27 |

Before source SHA-256: `1751eee6c2a9de6770b6aadae2d6f18010ef84ea85bf17e6003fc4773a2fe302`.
Delivered source SHA-256: `f045bfea8c075818f1cfd3959bc92f02d4708186eb5718834fe8f3305f79e563`.
`file_facts.json` records the unchanged event file hash and the exact helper locations.

## Helper map and lifecycle contract

The owner document contains the complete sixteen-output capture table, donor inputs, country scope, zero defaults, temporary-only capture side effects and full inline usage example.
It also specifies ten achievement-transfer outputs, spread/runtime results, consumed context fields, five consumption-parameter outputs and exact-population return defaults.
Call names, scopes, values and output meanings remain the existing API.
Caller frames retain storage across helper returns and temporary values remain unscoped.
A forwarding frame initializes the result before its nested helper, and its own outer consumer initializes that result before invoking the forwarding frame.
The existing Wendigo wrapper already owned its forwarded result and the reveal consumer now also owns it.
No generic helper extraction or dynamic-registry extension is needed because allocating storage in an initializer helper would repeat the defect.

Constants and tuning: no constant definitions or tuning tables changed.
Zero is the required output-storage initial value and the existing `cannibalism_consumption_result.invalid_scope` constant supplies the anchor failure default.
Event targets: no new target or persistence mechanism added.
Existing regular donor/destination/row/consumption pointers keep their current lifecycle.
Cleanup: no new flag, variable, target cleanup or recurring action added.
Temporary storage ends with its owning effect frame and immediate return values are not cleared early.
Migration: inline preallocation replaces implicit callee-owned output storage, with the original helper calls and consumers retained.

## Meaningful validation

The one-off `evidence/check_storage_contract.py` reuses the final completion audit's lexical block reader without running that audit or introducing a test framework.
Run from the repository root with `python docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_inheritance_helper_storage_repair/evidence/check_storage_contract.py`.
`source_contract_checks.json` records 67 passing bounded source checks and the final source hashes.

The checks use source-defined assignments and defaults, then discard temporary names first created inside a returning helper.
They preserve scoped donor state separately from temporary output storage.
The pre-repair source fails capture-output ownership as a negative control.
Opening CBL creation, later warlord absorption and original-ZZZ merge each retain all sixteen fields with distinct nonzero regular donor values, under each of the three origin alternatives.
All three transaction owners retain ten human achievement-ledger outputs with nonzero source-defined counters.
The two-human branch's source-defined post-capture override zeroes only inherited Larder and preserves route/identity snapshots.
Nested migration failure and success are projected across both helper return boundaries.
Anchor consumption retains a nonzero actual population result and the source-defined applied status.
The selected-host actor/global equality predicate accepts matching generations and rejects a mismatched generation in the bounded source projection.
The population request predicate rejects equal and older request IDs, preserving the original duplicate-request branch.
Transfer, annex, population and equipment call counts are unchanged, and every original source line retains its exact bytes, including existing mixed newline styles.
No additional native population or equipment call is introduced.

These are bounded actual-source storage projections and source preservation checks.
They do not execute the entire queue validator, complete opening/absorption transactions, native scope behavior, annex callbacks, equipment transfer, technology union or population/deaths accounting.
They do not prove in-game duplicate-transfer absence or multiplayer preservation.
MCP and native runtime acceptance are explicitly unresolved.

## References and MCP blockers

Live schemas were verified for `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and event inspect/render/compare.
`hoi4.script_validate` is absent from the exposed tool list.
Connected server health/version and client task negotiation are unconfirmed, so no helper expansion, jobs or native tasks were requested.

A two-source `set_temp_variable` search and narrow event inspection returned no status/artifact within a 45,000ms client observation window.
The first event query used undefined `chaosx.nr14.50` and supplies no event coverage.
The corrected existing warlord-response event `.71` query, bounded to one node and one edge with helper expansion disabled, also returned no status/artifact within 45,000ms.
These are client nonresponse observations and no server timeout, failure or cancellation status is invented.
`mcp_route_evidence.json` and `corrected_event_route_evidence.json` retain requests, exposed schemas and exact limitations.
Prior corrected narrow reference-context/search/read/source-lookup and event inspect/render/compare observations are in the final audit's evidence directory.
The parent's existing 600-second load timeouts remain inherited evidence, and no broad load query or additional expensive retry was used here.
The earlier four-node options render at revision `e9e470262f1ea057b06851d06c768e7e69517688395c2427a2d534af5005edff` remains partial with zero indexed helpers and cannot certify this repair.
Required event/helper inspect/render/compare coverage remains blocked by absent returned source-linked results.

Local reference evidence retains exact absolute Windows paths, line spans and SHA-256 revisions in `reference_excerpts.json`.
The main lifetime reference is offline `Data structures - Hearts of Iron 4 Wiki.md:438-450`, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Installed effects documentation `set_temp_variable:7820-7839` supports the syntax and any-scope assignment.
The vanilla CHI example at lines 803-820 demonstrates unscoped temporary storage used after country scope changes, without proving scripted-helper return ownership.
Existing shared dynamic effects/docs and relevant wiki effects/scopes and installed script-constants sections were consulted.
No source-only reference or projected test is presented as engine evidence.

## Remaining limitations and parent actions

The bounded storage source fix is finished, with no mechanic simplification or replacement.
Final source review and commit remain with the parent, as explicitly requested.
The destination-validity trigger currently lacks an actor/global generation equality check, so this repair cannot claim rejection of every stale destination or recycled source incarnation.
The selected opening host equality gate and spread exact-generation metadata comparisons are preserved, and wider source-gate design remains outside this task.
Scored selection helpers and their return storage remain outside the parent's lifetime-storage boundary because changing them affects selection behavior and requires the owning probability workflow.
Full native event/helper closure, annex callbacks, population/deaths and equipment idempotence, technology union, and both-human multiplayer acceptance are not established by these source probes.
No game was launched, runtime logs searched or user runtime advice issued.
The parent can proceed with its separately planned Larder/data helper edits in the shared effects file after reviewing this exact snapshot.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or updated because the existing helper-output lifetime rule already covers this repair.
