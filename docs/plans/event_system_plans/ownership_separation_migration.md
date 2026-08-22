# Shared event-system ownership separation migration plan

Date: 2026-07-29

Status: deferred design plan only. No gameplay, GUI, localisation, or registry file is changed by this document.

## Why this plan exists

The current shared event system is functional but ownership is concentrated across a small number of large scripted-effect files. The repository cleanup evidence shows that settings-aware dispatch, random-event preparation and accounting, and Event Log storage and rebuilds are cross-linked through those files and their GUI consumers. That concentration makes a later event-specific change harder to review and increases the chance that a local cleanup will break a shared contract.

This is a warranted future migration candidate, not permission to move code during the current documentation cleanup. The migration must preserve behavior and must be staged behind explicit contract evidence.

## Current ownership evidence

| Surface | Current owner or consumer | Evidence and boundary |
| --- | --- | --- |
| Shared settings and manual firing | `common/scripted_effects/chaosx_settings_effects.txt`, `common/scripted_guis/chaosx_scripted_gui_settings.txt` | Event 017 documents automatic, manual, Event Details, and cluster dispatch reaching the shared pre-fire route in `chaosx_settings_effects.txt`. The settings GUI owns digit entry, apply, clear, and last-fired display actions. |
| Random-event preparation, selection, and fired accounting | `common/scripted_effects/chaosx_logic_effects.txt` plus event-specific preparation helpers | Event 017 delegates weighted context preparation to the shared route and calls `random_faction_prepare_runtime_context`; Event 018 documents the generic dispatcher calling `resources_found_prepare_random_event_fire` before dispatch. The exact helper and accounting call graph must be inventoried before any extraction. |
| Event history, Event Details registry, and derived rebuilds | `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, `common/scripted_guis/chaosx_scripted_gui_events_log.txt` | `docs/systems/event_system/events_log_evolutions_and_clusters.md` lists the parallel history, evolution, cluster, and event-detail arrays and their rebuild entry points. Event 017 records sequence-bound secondary actors and exact event-result binding through this shared surface. |
| Cross-system dispatch context | `common/scripted_effects/chaosx_settings_effects.txt`, `common/scripted_effects/chaosx_logic_effects.txt`, event files, and GUI callers | Event 006 documents a settings-aware FIFO, event-log payload `6002`, and preservation of an already visible super-event. These are shared contracts, not safe local implementation details. |
| GUI scope contracts | `common/scripted_guis/chaosx_scripted_gui_settings.txt`, `common/scripted_guis/chaosx_scripted_gui_events_log.txt`, and interface files | The cleanup audit intentionally preserves `event_target:` usage and selected-row/detail state. GUI event-target patterns are valid and must not be migrated as part of ownership separation. |

## Frozen contracts

The following contracts are frozen before any code move:

- Event IDs, roots, type arrays, cluster arrays, evolution arrays, and registration order remain unchanged.
- Event 006 context, payload `6002`, source and result actor binding, and the settings-aware FIFO remain unchanged.
- `last_fired` values and their visible settings GUI semantics remain unchanged, including clear and overwrite behavior.
- Event Log history, Event Details, evolution, and cluster array shapes remain unchanged, including index alignment and secondary-actor arrays.
- Existing `event_target:` GUI and selected-row/detail-state conventions remain unchanged.
- Settings toggles, automatic-selection gates, manual firing, Event Details firing, and cluster firing retain their current trigger and cleanup behavior.
- No new whole-world `on_daily`, `on_weekly`, or `on_monthly` loop is introduced as a migration shortcut.

## Phased migration

### Phase 0: contract inventory and freeze

Build a call-graph ledger for every definition and caller in the three owner files, the two shared scripted-GUI files, the event-log scripted localisation file, and the shared event documentation. Record input scopes, global and country arrays, temporary variables, regular and global event targets, cleanup effects, and loader order. Do not edit gameplay files in this phase.

The ledger must include every Event 001-020 consumer and the shared-system references from Event 021 onward that are in scope only because they touch registration, settings, scenarios, or Event Log infrastructure.

### Phase 1: settings facade and dispatch adapter

Introduce a dedicated settings-dispatch owner only after Phase 0 proves the loader and call order. Keep compatibility wrappers at the existing helper names so event files and the GUI do not change in the first migration commit.

The adapter must preserve automatic timer dispatch, manual settings dispatch, Event Details dispatch, cluster dispatch, pre-fire preparation, settings gates, FIFO ordering, audio or super-event interlocks, and `last_fired` updates. No event ID or registration array is rewritten.

### Phase 2: random selection and accounting boundary

Separate weighted candidate preparation, selection, fire-once or repeatable accounting, cooldowns, and post-fire callbacks from settings presentation. Event-specific preparation helpers remain event-owned; only the generic selection and accounting contract is moved.

The first extraction must retain the existing helper names through wrappers and must prove that Event 006, Event 017, Event 018, and all default-enabled shared consumers receive the same context scopes and target pointers.

### Phase 3: Event Log storage and rebuild boundary

Separate history writes and exact sequence binding from Event Details registry setup and derived-view rebuilds. Keep the current parallel-array schemas and all index-preserving copy and sanitation behavior.

The Event Log GUI and scripted localisation remain consumers of the stable facade. Do not move or rename GUI `event_target:` contracts, selected-row variables, secondary-actor arrays, or evolution and cluster selectors during this phase.

### Phase 4: validation, deprecation, and cleanup

Run static definition-and-caller scans, array-length and index-alignment checks, targeted Event Log and settings inspections, and read-only scenario traces for Event 006, Event 017, and Event 018. Compare pre- and post-migration contracts for automatic, manual, Event Details, cluster, and triggerable-scenario dispatch.

Only after the parent accepts the evidence may compatibility wrappers be marked for later removal. Wrapper removal is a separate plan with its own parser/load and parent-owned live validation gate; it is not implied by this document.

## Acceptance gates

The migration is not accepted if any helper has an unresolved caller, any parallel array changes length or order, any Event 006 context or `6002` payload changes, any `last_fired` value changes, any Event Log result binds to a different history sequence, or any GUI selected-row/detail target becomes invalid.

The migration is not accepted if a settings toggle, Event Details preview, cluster member, or triggerable scenario silently bypasses the adapter. A failed gate requires restoring the previous owner file through the compatibility wrappers and recording the failed evidence.

## Non-overlap and ownership

This plan covers future shared event-system architecture only. It does not replace Event 006's implementation plan, Event 017 or Event 018 event plans, `docs/systems/event_system/events_log_evolutions_and_clusters.md`, the current settings or Event Log GUI contracts, or the shared-helper cleanup handoff. Those documents remain the current behavioral authorities until a parent-approved migration tranche produces newer evidence.

## Parent decisions required before implementation

1. Confirm that the current concentration warrants a dedicated shared-system migration after the event-specific cleanup is stable.
2. Approve the Phase 0 contract ledger scope and the owner-file split proposed by the evidence, rather than assuming a particular new filename.
3. Decide whether compatibility wrappers may remain indefinitely for stable public helper names or must receive a later removal milestone.
4. Decide the parent-owned live-validation scenarios required before wrapper removal.

## Current disposition

No phase is started. The plan is queued as a deferred architecture candidate with behavior-preservation gates and no authorized gameplay edits.
