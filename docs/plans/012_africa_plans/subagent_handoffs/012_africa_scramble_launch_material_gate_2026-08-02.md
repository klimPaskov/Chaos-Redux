# Event 012 Scramble expedition launch material gate

Date: 2026-08-02

Status: Implemented source correction; live acceptance remains open.

## Scope

The Scramble pre-response classifier already used `africa_ai_scramble_expedition_materially_ready`, which requires a deployable army, available manpower, and a controlled coastal naval base. The final `africa_scramble_launch_expedition_if_unresolved` loop did not repeat that predicate before declaring the intervention war, so a participant that acquired the planner flag through a later response could still be selected without the material package.

## Change

`common/scripted_effects/012_africa_world_order_effects.txt` now requires `africa_ai_scramble_expedition_materially_ready = yes` in the final coalition-member selection limit. The existing coalition cap, capitulation, war, and declaration legality checks remain unchanged. No new country tag, roster store, or expedition fallback was introduced.

## Validation

- The readiness helper is defined once in `common/scripted_triggers/012_africa_ai_profile_triggers.txt` and is now consumed by both the pre-response classifier and the final launch loop.
- The launch loop still grants expedition material and starts the existing `topple_government` war only after the gated participant is selected.
- The change is limited to the Event 012 world-order effect and this handoff; unrelated worktree edits are not part of the tranche.

## Remaining acceptance

Live coalition ranking, naval/deployable strength scenarios, target retry behavior, and aftermath acceptance still require campaign proof. This correction does not close W5, model, audio, native-language, external-package, or achievement acceptance blockers.
