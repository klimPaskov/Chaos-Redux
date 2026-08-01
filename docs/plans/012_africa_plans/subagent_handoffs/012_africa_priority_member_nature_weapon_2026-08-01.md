# Event 012 priority-member nature weapon handoff

## Scope

This tranche extends the existing Event 012 Rain/Drought action IDs 69 and 70 to completed priority-member packages without creating country tags, cosmetic tags, recurring world scans, or a second action ledger.

## Changed files and identifiers

- `common/script_constants/012_africa_priority_member_constants.txt` adds the fictional, bounded `africa_priority_member_nature_power` ladder and the `nature` AI weight.
- `common/script_constants/012_africa_action_constants.txt` adds `africa_natural_disaster_strength.priority_member_nature_strength_per_level`.
- `common/scripted_effects/012_africa_priority_member_effects.txt` assigns the power ladder during existing package registration and clears it during existing package cleanup. The mapping is a high-chaos gameplay value, not a cultural claim.
- `common/scripted_triggers/012_africa_triggers.txt` adds the member actor, caller-cost, and target gates and permits the existing host bridge to validate a saved member actor.
- `common/scripted_effects/012_africa_action_effects.txt` adds the explicit enemy roster refresh, player/AI member wrapper, member-side caller reserve, actor strength/severity contribution, result receipt copy, cooldown parity, and generation-safe cleanup.
- `common/decisions/012_africa_decisions.txt` adds the member roster refresh, two targeted member actions, and an AI-only cycle. All use the existing Charter icon and action IDs 69/70.
- `common/decisions/categories/012_africa_categories.txt` registers the member-only decision category so the new surface is visible without changing the host's high-chaos page.
- `localisation/english/012_african_union_l_english.yml` adds category, decision, dynamic-cost, and launch tooltip strings.
- `docs/events/012_africa/natural_disaster_weapons.md` and `docs/events/012_africa/overview.md` record the shared-host/member contract.

The follow-up AI parity pass adds authority-aware willingness to the existing `africa_priority_member_natural_disaster_ai_cycle`. Trace and low-authority packages are conservative, medium is neutral, and high or ancestral packages are progressively more willing to spend the caller reserve. The decision still uses the existing eligibility, target, cost, cooldown, host-generation, and shared-action gates.

## Runtime contract

The member decision saves the selected enemy as `africa_natural_disaster_member_action_target`, then `africa_begin_priority_member_natural_disaster_action` saves the member as global `africa_natural_disaster_action_actor` and the target as global `africa_action_target`. The current host runs `africa_begin_quoted_action_against_target`, so quote, payment, mission, outcome, event log, and cleanup remain the existing generation-safe path.

The member pays the Event 013 caller reserve from its own political power and command power. The host pays the quoted Charter action cost. A failed start refunds a member reserve if one was set and clears the host quote and both global pointers.

After a full result, the host calls the unchanged public Event 013 `call_natural_disaster = yes` API. The selected target stays exact. The member power ladder adds one bounded strength point per power level and promotes medium-or-higher package authority to regional severity, with high/ancestral authority able to reach catastrophic severity unless the host capstone already controls the result.

The action cleanup clears caller and controller reservations, member active state, global actor/target pointers, action arrays, target flags, capacities, and normal action variables. The member's 180-day cooldown is set alongside the host controller cooldown.

## Acceptance evidence

- No new African tag or cosmetic carrier was added.
- The member path uses one shared `africa_natural_disaster_enemy_targets` array and one Event 012 action record.
- The AI path uses the same target refresh and member wrapper as the player; no on_action or recurring world iteration was added.
- Event 013 source files were not modified.
- Localisation keys are in the existing Event 012 English file and retain its UTF-8 BOM.

## Remaining risks and blockers

The repository can statically inspect the new identifiers, but live-save proof is still required for at least one low-power package and one high/ancestral package, including a negative target that is at war with the member but not the host, a rejected Event 013 family, cooldown cleanup, and a host quote/payment failure rollback. The tranche does not create the requested unit models or claim completion of the 239 visual/model rows, W5 unique continent packages, the terminal World identity, live AI profiles, or the full Event 12 acceptance ledger.
