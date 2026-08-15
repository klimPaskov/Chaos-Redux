# Event 006 reconquest achievement host guard (2026-08-12)

## Change

`independence_wave_achievement_break_reconquest_is_complete` now requires `has_independence_wave_living_former_host = yes` before it dereferences `var:independence_wave_former_host`.

## Reason

The companion peaceful-host proof already required the living-host guard. The reconquest proof had the same former-host scope dereference but relied only on the defender/survivor flags. The explicit guard keeps the proof fail-closed if cleanup, host death, or an invalid origin leaves those flags without a live former-host target.

## Scope and validation

Valid reconquest runs are unchanged because the host must exist for the reconquest relationship and war-resolution proof. The change affects only an invalid or stale host-target state.

The achievement source audit remains 16/16 definitions, 16/16 proof triggers, 16/16 localisation triplets, and 16/16 icon triplets. Current Event 006 static allocator/scenario/flag/GUI/tag audits remain the shared receipts.

Current `hoi4.event_inspect` is blocked before scanning by `ARTIFACT_MANIFEST_INVALID` / `Artifact provenance manifest is invalid` for workspace `mod_chaos_redux_ea3b2d67c2c0`; no live unlock or save/load claim follows.
