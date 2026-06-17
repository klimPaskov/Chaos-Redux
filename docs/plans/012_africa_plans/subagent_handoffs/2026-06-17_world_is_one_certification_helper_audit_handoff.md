# Event 012 World Is One Certification Helper Audit

## Files changed

- `common/decisions/012_africa_decisions.txt`

## Gameplay surface changed

- Decision: `africa_certify_continent_unifiers_for_world_is_one`
- Helper call preserved: `africa_certify_continent_unifiers_for_world_is_one = yes`
- Requirement trigger preserved: `can_africa_certify_continent_unifiers_for_world_is_one = yes`

## Before

The certification decision declared `custom_cost_text = africa_certify_continent_unifiers_for_world_is_one_cost_tt`, but the convoy, support equipment, command power, and army experience checks were only inside `available`. That blocked the decision, but it did not provide the sibling `custom_cost_trigger` expected by the HOI4 decision cost pattern and used by vanilla for blocked/unblocked custom cost text.

## After

The route/readiness gate remains in `available`, while the resource gate now lives in a sibling `custom_cost_trigger` using the existing tooltip key and checks:

- `convoy_1 > constant:africa_force.continent_unifier_certification_convoys`
- `support_equipment > constant:africa_force.continent_unifier_certification_support_equipment`
- `command_power > constant:africa_decision.continent_unifier_certification_command_power_gate`
- `has_army_experience > constant:africa_decision.continent_unifier_certification_army_xp_gate`

The effect, constants, flags, achievement checks, and terminal gate logic were not redesigned.

Parent follow-up, 2026-06-17: the `complete_effect` now repeats the same resource gates before spending convoys, support equipment, command power, and army experience. Since HOI4 decision `complete_effect` runs when the decision is selected, this is a same-selection defensive guard that keeps the script effect aligned with the custom cost trigger.

## Why this is bounded

The patch only changes the decision UI/cost gating structure for the newly added certification decision. It does not alter the World Is One route prerequisites, readiness flags, cost amounts, AI weight, terminal effect, achievements, or localisation keys.

## Validation

- Re-read the edited decision block with line numbers and confirmed the route gate remains in `available`, with exactly one sibling `custom_cost_trigger` and one matching `custom_cost_text`.
- Ran `git diff --check -- common/decisions/012_africa_decisions.txt`; no whitespace errors were reported.

## Remaining issues and risks

- The broader Event 012 implementation intentionally uses `all_continent_unifiers_world_end_ready` as an Event 012 certification compatibility flag, not as proof from separate external continent-unifier event systems.
- `common/decisions/012_africa_decisions.txt` is currently untracked in the dirty worktree, so normal `git diff` does not show this narrow patch against HEAD.
