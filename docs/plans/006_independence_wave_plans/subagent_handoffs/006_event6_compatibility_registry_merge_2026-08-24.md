# Event 006 compatibility registry merge — 2026-08-24

## Scope

This source-layout pass removes three tiny Event 006 compatibility files without changing any executable identifier, trigger result, effect body, or load-order dependency.

## Merged sources

- `common/scripted_triggers/006_independence_wave_crisis_triggers.txt` was folded into `common/scripted_triggers/006_independence_wave_compatibility_triggers.txt`.
- `common/scripted_triggers/006_independence_wave_vanilla_formable_compatibility_triggers.txt` was folded into `common/scripted_triggers/006_independence_wave_compatibility_triggers.txt`.
- `common/scripted_effects/006_independence_wave_crisis_effects.txt` was folded into `common/scripted_effects/006_independence_wave_compatibility_effects.txt`.

The compatibility trigger registry now owns the dormant adapter predicates, hard-disabled retired-crisis predicates, and the two negative CHU/ASY vanilla-formable guards. The compatibility effect registry now owns the dormant adapter cleanup wrappers and the eleven empty retired-crisis stubs.

## Preservation checks

- `can_independence_wave_open_crisis` and every retired pressure, barrier, and cost helper remain `always = no`.
- Every retired crisis effect remains an empty block; no pressure, cost, cooldown, queue, history, or early Event 006 request can be recreated by a stale call.
- `can_access_vanilla_chu_formable_shortcuts` and `can_access_vanilla_asy_formable_shortcuts` remain exact negative guards for IW-043 and IW-058 only.
- The current allocator validator was updated to read the compatibility registries and to exempt the merged compatibility effect registry from retired-helper call scanning.
- `python -B .tools/audit_event6_allocator.py` passes with the existing 149-publisher, 126-automatic, 138-scenario-ranked, 40-adapter, 32-attestation, 29-group, and 3/4/5/7/10 ladder evidence.

This is a source-only file-count reduction. It does not widen Event 006 package admission, change automatic allocation, alter the no-pre-event player-facing boundary, or provide live parser/runtime evidence.
