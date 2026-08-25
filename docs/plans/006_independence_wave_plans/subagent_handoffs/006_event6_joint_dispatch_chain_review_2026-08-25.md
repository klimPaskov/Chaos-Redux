# Event 006 joint dispatch chain review — 2026-08-25

## Scope

This review checked whether a committed Event 005 + Event 006 Liberations plan needs an additional direct call to the Event 006 root event.

## Source evidence

- `common/scripted_effects/005_006_liberations_collision_effects.txt` commits the joint transaction and sets `independence_wave_joint_presentation_pending` only after `liberation_release_commit_plan` reaches the committed phase.
- `common/scripted_effects/chaosx_event_cluster_effects.txt` registers the Liberations members as numeric event IDs `6` and `5`, prepares the joint plan, queues the ordered member IDs, and schedules `chaosx.event_clusters.2` for delayed delivery.
- `common/scripted_effects/chaosx_settings_effects.txt` resolves a queued numeric member ID through `fire_event_by_temp_id_no_cluster`, whose default `meta_effect` dispatches `country_event = { id = chaosx.nr[EVENT_ID].1 }`. Therefore member `6` already resolves to `chaosx.nr6.1` and member `5` to `chaosx.nr5.1`.
- `events/006_independence_wave.txt` keeps `chaosx.nr6.1` as the hidden root. It consumes the committed joint receipt and opens `chaosx.nr6.2`; otherwise it runs the standalone allocator and opens the report only after a committed standalone plan.

## Decision

No gameplay patch was applied. Adding `country_event = { id = chaosx.nr6.1 }` to the joint preparation effect would duplicate the existing queued delivery and could race the Event 005 member. The current chain is source-complete for root-event dispatch.

## Validation

- `python -B .tools/audit_event6_allocator.py` passed: 149 publishers, 126 automatic/high-chaos selectable packages, 40 runtime adapters, 32 attested packages, and the retired pre-event crisis surface.
- `python -B .tools/audit_event6_flags.py --strict` passed: 102 registered tags, 102 complete flag families, 0 incomplete families.

## Remaining runtime evidence

The HOI4 event inspector returned a partial artifact for `chaosx.nr6.1` with unresolved graph nodes and blocking diagnostics in the broad repository scan. That tooling result does not justify changing the source dispatch chain; live game validation remains outside the agent scope.
