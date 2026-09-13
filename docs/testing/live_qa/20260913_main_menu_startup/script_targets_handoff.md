# Startup script target and temporary-variable repair

Status: assigned source repairs implemented; parent probability comparison and startup retest pending.
Parent owns launch/retest and final acceptance; no game process or computer control was used by this worker.

## Files and behavior

- `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`: removed 23 unsupported temporary clears after exact identifier tracing; corrected scoped reads of those same unscoped scratch variables.
- `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`: removed the opening-reactor scratch clear; wrapped the persistent global operational-ledger comparison in `check_variable`.
- `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`: preserved owned-and-controlled criteria with `any_owned_state` plus `is_controlled_by = PREV`, removed effect-only `limit` from `any_country`, and corrected scalar owner/controller comparisons.
- `common/scripted_effects/021_random_civil_war_parent_effects.txt`: corrected the two aligned temporary-array declarations, two owned-state game-variable checks, misplaced remnant effect, two leader-presence checks and variable-target annexation; removed three trailing local target clears; guarded the current-state reserve call with its existing fresh normal pointer.
- `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md`: documents temporary lifetime and nested custody reads.

## Exact scratch lifecycle proof

`script_targets_temp_references.txt` inventories every full identifier read/write across common, events and localisation before the patch.
`script_targets_temp_callers.txt` inventories owning helper callers and immediate continuation.
Reconciliation scratch consists of physical_custody_total, accounted_total and soviet_usable_devices (all prefixed sov_nuclear_bombs_).
Each is overwritten before computation and copied into persistent global outputs before the former clear.
Operationalized_amount and native_custody_delta are initialized from the selected site before nested holder ledger/native-stockpile effects.
Transfer_operational, transfer_assigned, transfer_reserved and transfer_total are initialized before any actor attribution; native_transfer_delta is initialized separately in both mutually exclusive holder/SOV branches.
Holder_devices is initialized before old-holder debit and new-holder credit.
Native_return_delta is initialized immediately before native debit.
Disposition_operational, disposition_assigned, disposition_reserved, disposition_transferred and disposition_total are initialized independently at entry to both terminal disposition operations; neither calls the other, and their only nested reconciliation helper uses a disjoint scratch set.
Opening_reactors_remaining is initialized from entitlement before all queue checks; its callers consume persistent pending flags and counters.
No full identifier has an absence-sentinel reader or a delayed-event reader.
The global usable-device output shares a suffix with local scratch but was preserved with its global namespace intact.

## Local event-target lifecycle proof

`script_targets_event_references.txt` inventories exact targets and includes imported writer files.
Ordinary_cleanup_host is saved at operation entry and Ordinary_cleanup_actor at each admitted actor before annexation; all reads are within that operation and no continuation reads them.
Secondary_next_source is saved before the successful commit branch reads it; its nested secondary-front attempt and later .7 event do not read this target before another save.
Current_state has three reserve call sites: connected expansion saves it immediately; ordinary anchor selection already guards its normal pointer; the Event006 branch now uses the same guard after the normal pointer is cleared at planning entry.
The shared reserve helper therefore cannot consume a stale local target when a new anchor was not published.
The three imported liberation_candidate targets are always overwritten by the exact 32 admitted Event006 package publishers before this caller reads them.
`script_targets_adapter_overwrite_proof.txt` maps every allowlisted package to its actual registered country tag and existing state definition.
Each loader uses every_possible_country (including dormant tags), the exact static anchor, and the anchor owner to overwrite the three targets.
Dynamic dispatch preserves zero-padded package names and draws only the adapter allowlist; there are no absent-country publications in this bounded set.
The obsolete clears can therefore be removed without changing a shared Event006 contract.

## Constants, call sites and cleanup

No tuning constants or numeric probabilities changed.
Existing ledger constants and the normal current-state pointer provide the required values and validity.
The annexation uses a fresh real local country target immediately before the native annex effect; it expires with the chain and has no external readers.
No new generic helper or global target router was introduced.
Selected actor/anchor validity repair is documented separately by `selected_actor_lifecycle_handoff.md`.

## MCP and validation limits

Event 021 and Event 023 inspect/render calls returned EVENT_INSPECTED_PARTIAL / EVENT_RENDERED_PARTIAL at revision 4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d.
The server explicitly deferred workspace helper projections and lifecycle passes; this is partial event graph evidence, not engine proof of the scratch contracts.
The Event023 trace artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0fbb4bb4c40f4b46e99b3a29fea796faaa1bcdc687dd15ee089c82ac18a2e594/d01dd3ae07f620825bc428391f763a71b1a39e1028571b108be2b4121a498a9c/event-trace-4bccb6ec7fe1.json.
The Event023 render manifest is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5b8184c2d24c5d406a16228d4f27bb4d17231135af50310719f42ff3e932e99/72a41ddb4cd0d8afbcf7a2d3f636c9eff9496fae4e00ca1458b465ffe3e99496/event-targets-4bccb6ec7fe1-manifest.json.
Comparison against the baseline revision returned EVENT_REVISION_NOT_CACHED, and comparison using the trace report URI returned EVENT_GRAPH_ARTIFACT_INVALID.
The startup log retest remains parent-owned.
Original source bytes are retained under baseline/scripts with their relative paths.

## Remaining work and uncertainty

The scenario selected-target validity gate and exposure profile has_stability repair were released and implemented as recorded below.
The selected actor/anchor worker completed its separate contract and evidence.
No simplification or substitute target has been used.
Skills used: chaos-redux-events, chaos-redux-subagents and chaos-redux-debug-playtest; no skill was modified.

The same exact-identifier audit also covered return_operational, return_transferred, return_total, recorded_owner_dismantled and recorded_owner_missing in the touched custody helpers.
They are temporary-only, set before use, with no outside readers; their PREV prefixes were removed and the three ineffective clear_variable return-scratch calls were removed.

The final in-memory proposedSources baseline comparison remained pending for several minutes and was terminated at the parent's instruction to avoid indefinite MCP tooling before launch; no comparison result was claimed.
Selected actor/anchor implementation is complete: see selected_actor_lifecycle_handoff.md and selected_actor_lifecycle_mcp_evidence.json.
Task-specific static contract results are in script_targets_validation.json.

## Final held repair release

The parent released the two held syntax/validity repairs after the root probability auditor returned its concrete baseline and tool limits.
The scenario picker uses a caller-country success flag set through PREV only by the successful random-scope body, reset each draw and after the loop.
The existing failure branch remains unchanged; stale target presence alone cannot dispatch a failed draw.
The exposure mediator comparison uses `has_stability` with its unchanged constant and strict greater-than threshold.
Immediate prepatch bytes for the held edits are at `docs/testing/live_qa/20260913_main_menu_startup/baseline/scripts_held_021/common/scripted_effects/021_random_civil_war_parent_effects.txt`.
Original full-tranche baseline bytes are at `docs/testing/live_qa/20260913_main_menu_startup/baseline/scripts/common/scripted_effects/021_random_civil_war_parent_effects.txt`.
Final source bytes remain at the corresponding live repository path.
Named scenario `scenario_draw_success`: nonempty eligible ticket pool, budget one; dispatch the actual drawn country once using the unchanged ticket distribution and removal count.
Named scenario `scenario_draw_failure_after_success`: a preceding draw left a local target, but the next draw has no eligible candidate; cleared success flag must route to the existing budget-consuming failure branch without redispatch or ticket removal.
Named scenario `exposure_mediator_below_equal_above`: stability below, equal to and above constant:event021_ai.exposure_mediator_stability; only above satisfies the unchanged strict comparison, assuming preceding profile branches are false.
Root retains mandatory same-scenario probability_compare and startup retest ownership.
All assigned source repairs are implemented; final engine and comparison acceptance remain with the parent.
