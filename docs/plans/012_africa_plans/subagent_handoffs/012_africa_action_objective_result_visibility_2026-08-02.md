# Event 012 action objective result visibility handoff — 2026-08-02

## Scope

The shared 102-row action contract already stored a row-specific objective on the quote and active mission, but the result event was created before cleanup copied that value to the result snapshot. This tranche keeps that existing value visible through the mission description and the result detail without creating a second action store or changing action resolution.

## Changed files and identifiers

- `common/scripted_effects/012_africa_action_effects.txt`: `africa_resolve_action` snapshots `africa_active_action_objective` before creating `chaosx.nr12.220`, and `africa_cleanup_action` repeats the idempotent snapshot before clearing the active record.
- `common/scripted_localisation/012_africa_charter_gui_scripted_localisation.txt`: `GetAfricaCharterActionObjectiveName` reads the immutable active objective when called from a mission target; the existing active-objective branches remain target-scoped and no duplicate lookup is introduced.
- `common/scripted_localisation/012_africa_scripted_localisation.txt`: `GetAfricaLastActionObjectiveName` maps the completed action objective to the existing objective labels.
- `localisation/english/012_african_union_l_english.yml`: short, medium, long, and epic mission descriptions expose the objective; `chaosx.nr12.220.d` exposes the same objective in the result event.
- `docs/events/012_africa/action_duration_objective_contract.md`: records the active-mission and post-cleanup result path.

## Behaviour

The quote, payment, mission timer, outcome roll, and cleanup kernels are unchanged. A completed action result now reports whether it resolves by peace or deadline, awaits a response, watches target validity, prepares a war, holds a review window, clears a terminal gate, or has no timed review. Cancellation retains the same snapshot for later history, but intentionally does not open a second result popup. Missing state remains the existing neutral `No timed review` label.

## Validation

- Static brace and quote scan on all changed Clausewitz/scripted-localisation files: balanced.
- Event 012 localisation key scan: the new scripted-localisation methods resolve only to existing objective labels.
- No country tags, models, entities, world scans, recurring on_actions, or action IDs were added.
- Live Hearts of Iron IV execution and GUI rendering remain user-owned validation.

## Remaining risks

The objective lookup is presentation-only and does not prove the mission's live outcome. The existing mission availability and result kernels remain authoritative.
