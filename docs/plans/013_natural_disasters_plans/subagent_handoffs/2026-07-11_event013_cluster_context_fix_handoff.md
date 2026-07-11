# Event 013 pending cluster context fix handoff

Date: 2026-07-11

Mode: bounded gameplay patch. No commit was created.

## Files changed

- `common/scripted_effects/chaosx_event_cluster_effects.txt`
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-07-11_event013_cluster_context_fix_handoff.md`

The existing `economy_positive` cluster edits in the shared scripted-effects file were preserved unchanged.

## Gameplay surface changed

The event-cluster pending queue now preserves the exact Event 013 runtime context for every queued Natural Disasters member, including members appended behind an already active cluster queue.

The firing-order pipeline carries the original one-based member slot through random ordering in:

- `temp_event_cluster_order_candidate_batch_index_entries`
- `temp_event_cluster_firing_order_batch_index_entries`

The persistent pending queue now keeps six aligned rows:

- `event_cluster_pending_member_event_id_entries`
- `event_cluster_pending_member_batch_index_entries`
- `event_cluster_pending_member_event013_state_entries`
- `event_cluster_pending_member_event013_target_country_entries`
- `event_cluster_pending_member_event013_family_entries`
- `event_cluster_pending_member_event013_variant_entries`

Every ordered non-Event013 member receives zero sentinel entries in the four Event013 context arrays. This keeps all pending arrays aligned for mixed and overlapping cluster batches.

The file-local structural constants are `@event_cluster_event013_context_sentinel`, `@event_cluster_event013_baseline_first_slot`, `@event_cluster_event013_evolution_i_slot`, `@event_cluster_event013_evolution_ii_slot`, and `@event_cluster_event013_evolution_iii_slot`.

## Event 013 role mapping

`event_cluster_get_event013_member_variant` maps the Natural Disasters source slots as follows:

| Batch-relative slot | Requested Event 013 variant |
| --- | --- |
| 1 | Baseline, stage 0 |
| 2 | Baseline, stage 0 |
| 3 | Evolution I |
| 4 | Evolution II |
| 5 | Evolution III |

The requested stage is capped to `natural_disaster_current_evolution` after the normal evolution enable checks. Invalid Natural Disasters slots fail runtime preparation instead of becoming a baseline substitute.

## Before and after behavior

Before this patch, only event IDs survived in `event_cluster_pending_member_event_id_entries`. Event 013 consumed the one regular preflight target only when `event_cluster_current_member_sequence` equaled the absolute queue position one. A Natural Disasters batch appended behind another active batch therefore lost its state and family when the originating effect chain ended. Its later member could enter `random_valid` targeting.

After this patch:

1. Random firing order preserves the original logical member slot even when duplicate Event 013 IDs exchange positions.
2. `event_cluster_prepare_event013_pending_contexts` runs synchronous Event 013 preflight for every fired Event 013 row before the cluster is recorded or queued.
3. Preflight receives the capped role stage through `natural_disaster_call_evolution_override_supplied` and `natural_disaster_call_evolution_override`.
4. The exact state, target country, family, and variant are copied out of the regular preflight targets immediately. The temporary state family marker is cleared after capture.
5. Any Event 013 row without a proved exact context sets `event_cluster_runtime_ready` to zero. The cluster is not recorded, marked fired, or queued.
6. The delayed callback reads all context from the same pending row before incrementing the absolute traversal index.
7. State and country scopes are recovered with separate numeric proof variables. The Event 013 call runs only after both recoveries succeed.
8. The call uses `natural_disaster_target_mode.caller_provided` with exact state and country proofs. There is no Event 013 `random_valid` branch in the cluster member dispatcher.
9. Queue cleanup clears every aligned pending array together.

The absolute `event_cluster_pending_member_index` remains only as the queue cursor. It no longer decides the Natural Disasters logical role or authorizes a stale regular event target.

## New and changed helpers

- `event_cluster_clear_order_candidates`
- `event_cluster_add_fired_order_candidate`
- `event_cluster_append_order_candidates_by_score`
- `build_event_cluster_firing_order`
- `event_cluster_initialize_pending_context_rows`
- `event_cluster_get_event013_member_variant`
- `event_cluster_prepare_event013_pending_contexts`
- `event_cluster_prepare_runtime_context`
- `event_cluster_queue_ordered_fired_members`
- `event_cluster_fire_next_pending_member`
- `fire_event_cluster_member_by_temp_id`
- `event_cluster_clear_pending_member_queue`

## Safety and scope boundaries

- Target discovery still uses `natural_disaster_prepare_random_event_fire`, including Event 013 physical geography and target validation.
- Preflight remains locked to the cluster-firing country. No world target, substitute country, substitute state, or widened geography was added.
- A target that becomes invalid before its delayed member fires fails through the exact caller-provided Event 013 validation. It is not rerolled.
- The patch does not change Event 013 effects, triggers, constants, localisation, GUI, history arrays, cluster detail rows, or the event catalog workbook.
- The patch does not alter the unrelated `economy_positive` cluster registration, membership, availability, or cooldown changes already present in the file.

## Validation performed

- Script nesting scan finished at depth zero and never entered a negative depth.
- Static queue audit found exactly one append block for each of the six pending arrays inside `event_cluster_queue_ordered_fired_members`.
- Static sentinel audit found exactly one per-row initializer for each Event 013 context array.
- The delayed callback checks all five context-array lengths against the event-ID array before reading a row.
- `event_cluster_current_member_sequence` has no remaining read or assignment. Its only occurrence is cleanup for prior runtime state.
- The Event 013 cluster dispatcher contains only `caller_provided` target mode and both exact target proofs.
- The source-slot mapping preserves 1 and 2 as baseline, 3 as Evolution I, 4 as Evolution II, and 5 as Evolution III before the normal unlocked-stage cap.
- Diff review confirmed that the pre-existing `economy_positive` hunks remain present.

## Integration dependency and remaining runtime proof

The parent-owned Event 013 API tranche must implement and reset these two public temp inputs:

- `natural_disaster_call_evolution_override_supplied`
- `natural_disaster_call_evolution_override`

The cluster patch already supplies them during both preflight and final call. Until the Event 013 API consumes the inputs, the queued variant value persists correctly but cannot control Event 013 evolution resolution.

A live overlapping-queue scenario remains required after that API input lands. The proof should start another cluster queue, append Natural Disasters before it drains, then confirm that the Event 013 row uses its stored batch slot, exact state, exact country, exact family, and exact variant. It should also confirm that a deliberately invalidated stored state fails closed without selecting another target.

## Simplifications, omissions, and blockers

No fallback or gameplay simplification was introduced. The bounded cluster-context patch is complete. Full mechanical variant enforcement depends on the parent-owned Event 013 evolution-override input described above, and live engine validation remains pending for the integrated tranche.
