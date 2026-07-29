# Fallout Blackout GUI Proof

## Scope

This proof covers the Fallout-owned blackout surface in `interface/fallout_world_end.gui`, `common/scripted_guis/fallout_world_end_scripted_gui.txt`, `common/scripted_localisation/fallout_world_end_scripted_localisation.txt`, and the coordinator effects in `common/scripted_effects/fallout_world_end_effects.txt`.

The surface is not a super-event. The ordinary super-event GUI and event picture slots are not used for the transition.

## Static presentation proof

- `fallout_world_end_blackout_window` is a parentless independent `containerWindowType` with `fullScreen = yes`, percentage sizing, a zero origin, and clipping disabled. This is the documented root shape for a scripted GUI binding.
- `GFX_fallout_blackout_tile` is a Fallout-owned opaque DDS under `gfx/interface/fallout_world_end/`.
- `fallout_world_end_click_blocker` is a non-transparent `buttonType` scaled to the same full-screen coverage as the blackout tile. It has no scripted click effect, so it cannot advance a phase or alter the rewrite.
- The centered text box reads `fallout_world_end_blackout_display`, which delegates to `GetFalloutWorldEndBlackoutText`.
- The localisation selector maps the authoritative transition phases to the eight authored beats. The final map-return text is shown only at `fallout_transition_phase.map_return`.
- The scripted GUI is player-context only, rejects AI, and is visible only while `fallout_transition_active` is set.

## Processing and authority proof

`fallout_lock_transition` is the only entry path that sets the transition active flag and it saves `fallout_transition_coordinator` before scheduling phase event `chaosx.fallout.1001`. Every phase event requires the current synchronized human coordinator and the active generation-bound phase. The coordinator advances one phase after its current receipts are durable, marks the GUI dirty, and schedules the next phase after the documented three-hour beat interval.

New request intake clears any stale `fallout_transition_coordinator` target before writing the pending envelope and pauses Air Cleanliness immediately. The designated coordinator reconciliation pulse then claims the single request target, so a previous owner cannot block a fresh request for one date. This coordinator is a synchronized human selection, not a proven literal Paradox lobby-host identity. A rejected pending envelope releases the temporary Air pause before ordinary operation resumes.

The designated Fallout coordinator also owns request validation, snapshot reconstruction, state grading, population loss, physical collapse, diplomacy reset, successor allocation, numerical survival commit, player continuation, and map return. Save reconciliation calls `fallout_world_end_migrate_save`, reschedules an unissued current phase, and never creates a second transition generation.

Dedicated Fallout blackout audio is dispatched separately from the GUI. It uses the existing super-event audio setting only as a volume and playback preference. No super-event event, quote, button, or picture slot is used.

## Engine references and boundary

The offline Interface Modding page documents `fullscreen`, independent windows, `buttonType`, `alwaystransparent`, sprite scaling, and centered text. The offline Scripted GUI Modding page documents independent container assignment, `player_context`, visibility, and dirty updates. The installed vanilla `interface/frontend_friends_view.gui` uses an `event_trap` element for popup exclusivity. This Fallout surface now uses the documented independent container route and declares a full-screen non-transparent button.

Static review can prove the documented container binding, declared full-screen geometry, the non-transparent input-consuming control, phase text mapping, synchronized human-coordinator gate, generation checks, save-recovery calls, and dedicated audio path. It cannot prove literal Paradox lobby-host identity, click interception, z-order against every DLC window, keyboard capture, pause behavior, save persistence, multiplayer presentation, or performance in a live session. HOI4 was not launched by request, so those remain explicit runtime blockers rather than passing claims.

The read-only GUI inspector returned `GUI_INSPECTED` for `fallout_world_end_blackout_window`, and the renderer returned `GUI_RENDERED` for 1920 by 1080 and 2560 by 1440 offline representations after the container rewrite. The workspace-wide validation result remains false because unrelated source and GUI diagnostics exceed the inspector ceiling. These artifacts are structural evidence only and do not replace live input or multiplayer proof.
