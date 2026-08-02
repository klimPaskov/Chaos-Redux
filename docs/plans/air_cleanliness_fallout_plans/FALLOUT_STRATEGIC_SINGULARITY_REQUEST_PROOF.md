# Fallout strategic-singularity request proof

Status: statically integrated, dormant at the world-end boundary, and not runtime accepted.

## Scope

This proof records the source-aware bridge between the Brilliant Scientist strategic-singularity terminal and the Fallout request coordinator. The bridge uses the existing strategic-singularity source enum and does not create a second Fallout request path, a second coordinator, or an ordinary super-event route.

## Request intake

`common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` prepares the strategic-singularity terminal, records its pre-lock consequence receipt, saves the initiating country as `fallout_request_actor_input`, and submits `fallout_request_source_input = constant:fallout_request_source.strategic_singularity` to `fallout_request_aftermath`.

`fallout_explicit_terminal_request_is_valid` in `common/scripted_triggers/fallout_consolidated_triggers.txt` accepts the strategic-singularity source as an explicit terminal request. That shared validator requires the world-end ledger to be free and the terminal to be enabled, but it does not require Air Contamination to reach 100 percent or impose a Chaos value above 1000. Any upstream Brilliant Scientist scenario eligibility remains a separate terminal rule and is not a Fallout request threshold.

`common/scripted_effects/fallout_consolidated_effects.txt` remains the only request coordinator. It records the source, intensity, request date, coordinator, and actor target in the single idempotent envelope. Repeated calls are rejected by `fallout_request_ledger_is_free` rather than creating another request.

## Rejection recovery

When a pending strategic-singularity request fails the shared validation gate, `fallout_clear_pending_request_envelope` calls `brilliant_scientist_recover_rejected_singularity_fallout_request` through the saved actor target before clearing the envelope. The Brilliant Scientist effect clears its submitted marker, records a rejected receipt, increments its retry counter, and schedules the existing retry event. No Fallout transition flag is set by this rejection path.

## Lock finalization

When the host-owned Fallout coordinator reaches the snapshot-ready lock, it sets the normal Fallout transition flags and schedules the blackout phase. If the source is strategic singularity and the initiating actor target is still present, the lock calls `brilliant_scientist_finalize_singularity_after_fallout_lock` in that country scope. That effect verifies the existing singularity finalization gate before setting the Brilliant Scientist world-end identity and queuing its dedicated dramatic presentation. The Fallout blackout and rewrite remain the owning transition surface.

## Separation from other terminal sources

The source-aware calls are guarded by `fallout_request_source_is_strategic_singularity`. Manual, Air Contamination, chemical, biological, mixed, and Final Silence requests do not enter the Brilliant Scientist recovery or finalization effects. Zombie ids, files, assets, audio, sprites, and paths are not referenced.

## Static checks

- The Fallout namespace remains owned by `events/fallout_world_end_events.txt`.
- The strategic-singularity source enum is declared in `common/script_constants/fallout_consolidated_constants.txt`.
- The source trigger and explicit-terminal validator are defined in `common/scripted_triggers/fallout_consolidated_triggers.txt`.
- The request envelope and lock bridge are defined in `common/scripted_effects/fallout_consolidated_effects.txt`.
- The Brilliant Scientist recovery and finalization effects are defined in `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt`.
- No setter for either Fallout scheduler activation flag was added.
- No public manual scenario row was added.

## Runtime boundary

No Hearts of Iron IV session was launched. Host authority, save recovery, event-target persistence, blackout input capture, multiplayer behavior, and the Brilliant Scientist presentation queue remain runtime evidence gaps. This proof does not claim completion of the Fallout transition, successor allocation, or the 660-block living-world floor.
