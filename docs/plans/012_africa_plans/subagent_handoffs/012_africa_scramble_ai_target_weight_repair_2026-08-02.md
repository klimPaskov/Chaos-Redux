# Event 012 Scramble AI target-weight repair

Date: 2026-08-02

Status: implemented as a narrow AI-only response and target-selection repair; live scenario evidence remains open.

## Scope

This tranche owns only the existing Scramble response event and the Action 81 AI target dispatch. It does not add tags, models, world-package identities, recurring scans, or a second participant store.

## Changes

- `events/012_africa_world_order.txt` now halves the AI chance for the ultimatum response when the participant fails `africa_ai_scramble_expedition_materially_ready`, and doubles it when the same material gate passes. The human option remains available as a deliberate bluff or pressure choice.
- `common/scripted_triggers/012_africa_ai_profile_triggers.txt` now requires the shared material gate before Action 81 reports a valid expedition-planning target to AI.
- `common/scripted_effects/012_africa_ai_profile_effects.txt` applies the same gate when selecting the concrete Action 81 participant target, preventing a stale or weak planner from consuming the AI action quote.

The final war declaration remains fail-closed in `africa_scramble_launch_expedition_if_unresolved`; this tranche aligns AI willingness and target dispatch with that existing validator instead of changing the player-facing war path.

## Validation

- The material helper remains single-definition and now has consumers in the pre-response classifier, final launch loop, response AI chance, Action 81 availability, and Action 81 target selection.
- Changed source files were checked for balanced braces and unsupported comparison operators.
- No HOI4 executable or live save was launched.

## Remaining risk

The source still needs campaign evidence for rank ordering, coalition-cap starvation, naval distance, and material depletion between response and launch. Those are acceptance checks, not a reason to invent new participant stores or tags here.
