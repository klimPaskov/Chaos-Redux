# Event 012 B4 Scramble material-readiness gate

Status: implemented as a narrow AI-classification patch; live scenario and probability-surface evidence remain open.

## Gameplay changes

- Added `africa_ai_scramble_material` constants for minimum expedition army size, available manpower, and the controlled coastal naval-base floor (the trigger requires a level above zero).
- Added `africa_ai_scramble_expedition_materially_ready` in `common/scripted_triggers/012_africa_ai_profile_triggers.txt`.
- `africa_ai_classify_scramble_response` now assigns `power_expedition_coalition` only when the actor is an AI faction leader with colonial interest and passes the material gate.
- Actors that fail the gate continue through the existing withdrawal, sanctions, recognition, or opportunist classification branches; the shared quoted action validator remains the final launch authority.

## Acceptance alignment

The classifier now considers a concrete capability footprint instead of ranking every colonial faction leader as expedition-capable. This does not create a new action path, bypass costs, or alter target validation. It uses existing country/state triggers and centralised constants, and it does not add tags, models, or player-facing strings.

## Validation and remaining risk

Static checks should confirm the trigger has one definition and one classifier callsite, the three constants are referenced, and no unsupported operators or new country identities were added. A live acceptance pass still needs one materially incapable colonial faction leader, one capable faction leader, and one non-leader interest actor to confirm classification and downstream action ranking. The strategy-plan probability adapter remains unresolved.
