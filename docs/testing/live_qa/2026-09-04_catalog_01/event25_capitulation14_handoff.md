# Event 025 capitulation trigger alias repair handoff

Status: implemented and source-ready for parent integration.

This bounded repair addresses the 34 `is_capitulated` parser records at 19 unique source locations reported by `docs/testing/live_qa/2026-09-04_catalog_01/logs/launch_13/logs/error.log`.

## Scope and changed files

The repair changed only the invalid trigger alias in the three assigned files.

- `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt` contains 4 replacements.
- `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt` contains 14 replacements.
- `common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt` contains 1 replacement.

Every replacement changes `is_capitulated` to the supported country trigger spelling `has_capitulated` while retaining the existing `= yes` value.

The affected helpers are `chaosx_alien_recovery_ledger_event025_owner_target_is_valid`, `chaosx_nr25_ai_candidate_available`, `chaosx_nr25_target_participant_valid`, `chaosx_nr25_scheduler_participant_valid`, `chaosx_alien_recovery_ledger_cleanup_invalid_targets`, `chaosx_alien_recovery_ledger_assign_fragment_slot_1` through `chaosx_alien_recovery_ledger_assign_fragment_slot_6`, and `chaosx_nr25_run_bounded_pulse`.

The ledger cleanup group covers the recorded owner and fragment-owner validity checks, and the six fragment-slot helpers retain their existing previous-owner checks.

## Behavior and semantics

Vanilla trigger documentation confirms that `has_capitulated` is a country-scoped boolean trigger and is used as `has_capitulated = yes`; `is_capitulated` is not a supported trigger type.

The four negative validity gates remain negative as `NOT = { has_capitulated = yes }`, so capitulated countries continue to be rejected as event-target owners or participants.

The bounded-pulse invalid-participant limit remains a positive `has_capitulated = yes` test, so capitulated participants continue to be invalidated and cleaned up.

No scope changes, event-target changes, constants, flags, resource gates, helper names, caller conditions, or unrelated source edits were made.

## Backup evidence

The exact immediate pre-patch files were copied to `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event25_capitulation14/` with their relative source paths preserved.

The verified pre-patch backup hashes were:

- `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt`: 40,556 bytes, SHA-256 `983D131CB63ACAF296BF36ACE79EB6C1B11ED1B8C249D2804EFE6C111BB6AD44`.
- `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt`: 55,024 bytes, SHA-256 `94FD609544ADE75E101584A4E29D20B14B774A8D8488FB30E6AA3651831AD500`.
- `common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt`: 175,130 bytes, SHA-256 `A522391281531D1A8E5513EB6EC7DA8A21979BCEA26CF23F2525400E9D61B616`.

## Validation evidence

The source audit found exactly 19 assigned occurrences before patching and no other `is_capitulated` occurrences in the assigned files after patching.

The post-patch inventory contains exactly 19 `has_capitulated` occurrences at the same helper locations, and the inverse token substitution reconstructs the backed-up source text, demonstrating that the patch was alias-only.

The parent verified launch14 parser acceptance with zero `is_capitulated` diagnostics and stable hashes for all three source files during launch14.

This launch14 result proves parser acceptance for this alias repair only; it does not prove campaign behavior or a complete event/helper lifecycle pass.

## Event MCP evidence and limits

The required narrow read-only event inspection and unresolved render were run for `chaosx.nr25.1`.

Both returned partial results against revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8` with graph hash `c6850dd8ad35035c9a83ff251c3df14e4e6123af303e2037d032ccbf5ea51b2e`.

The event inspection returned `EVENT_INSPECTED_PARTIAL` with 0 helper nodes, deferred workspace-wide helper and lifecycle projections, and `MCP_INLINE_FILES_TRUNCATED` diagnostics; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a27c2d1c3f31257992ace27c27116691b91ead2db01a69cf64193f9def67cfa9/7140fe555d48d7d58083e356a62f9639c2a6625e24f4e27bd4e8c94f771c1325/event-lint-1102e50fad94.json`.

The unresolved render returned `EVENT_RENDERED_PARTIAL` with layout hash `065a1869db8966704a35c5a762b300aef85fb49a23b9b6683c0362704f6b0ca8` and manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41b31a16bb70568ddec79dd6badb0af8dcfe49d8512593fcbcab45fd258db208/05c6319f914bf6951d2e1cab3cbcc6cd9060f6b81554dcc672e8abf28af255cf/event-unresolved-1102e50fad94-manifest.json`.

The event MCP route is focused on event and on-action sources and did not index the three assigned scripted trigger/effect files, so these artifacts provide narrow event linkage evidence only.

No helper registration, helper parser, or helper lifecycle pass is claimed from this partial MCP route.

## Weighted-surface assessment

The occurrence in `chaosx_nr25_ai_candidate_available` is an eligibility gate only.

The repair changes no AI weight, `ai_chance`, MTTH, random-list weight, decision score, focus weight, research weight, or strategy factor.

Therefore a probability-auditor baseline and probability comparison are not required for this alias-only repair.

## Remaining limits and parent actions

No game launch or commit was performed by this worker.

Parent launch14 parser acceptance is recorded above, while campaign validation remains outside this handoff.

Other launch13 Event 025 diagnostics, including unrelated `clear_event_target`, `has_active_mission`, and candidate-helper issues, were outside this exact `is_capitulated` scope and were not changed here.

No simplification or fallback was used within the assigned alias-repair scope.

Skills applied were `chaos-redux-subagents` and `chaos-redux-events`.
