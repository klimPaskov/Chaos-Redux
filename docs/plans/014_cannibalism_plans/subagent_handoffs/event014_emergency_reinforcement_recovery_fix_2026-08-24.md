# Event 014 emergency reinforcement recovery fix

## Scope and ownership

This handoff covers the narrow gameplay correction for `cannibalism_emergency_reinforcement`. It changes only the workshop-recovery guard in `common/scripted_effects/014_cannibalism_effects.txt`; the decision and Event 014 English localisation already carry the explicit readiness-only wording in the current branch. No AI weights, cost constants, category density, missions, scripted GUI files, assets, or unrelated decisions were changed in this tranche.

## Transaction path

- Entry decision: `cannibalism_emergency_reinforcement` in `common/decisions/014_cannibalism_decisions.txt`.
- Readiness trigger retained unchanged: `cannibalism_warlord_can_pay_emergency_reinforcement_cost` in `common/scripted_triggers/014_cannibalism_triggers.txt`. It checks the command route, emergency flag, Larder threshold, and infantry/support equipment reserve with `has_equipment`; the reserve is not a spend effect.
- Transaction helper: `cannibalism_execute_warlord_recruitment_transaction` in `common/scripted_effects/014_cannibalism_effects.txt`.
- Event 014 localisation keys already present in `localisation/english/014_cannibalism_l_english.yml`: `cannibalism_emergency_reinforcement_desc`, `cannibalism_emergency_reinforcement_requirements_tt`, `cannibalism_emergency_reinforcement_cost_text`, and `cannibalism_emergency_reinforcement_effect_tt`.

## Before and after

Before this fix, the transaction consumed the configured Deaths-ledger population and Larder and restored manpower, but any active `cannibalism_warlord_workshop_conversion_open` flag also granted the workshop infantry-equipment recovery amount. That contradicted the emergency action's no-equipment contract and could create equipment while the tooltip described a manpower-only action.

After this fix, the workshop recovery block requires `cannibalism_warlord_workshop_conversion_open` and explicitly rejects `cannibalism_recruitment_template.emergency_reinforcement`. Emergency reinforcement therefore consumes the configured Deaths population and Larder, restores manpower, applies its existing survival-order relief, and generates neither a unit nor equipment. The equipment reserve remains a readiness-only requirement and is explicitly described as checked but not consumed.

## Exact patch

In `cannibalism_execute_warlord_recruitment_transaction`, the `add_equipment_to_stockpile` branch is now gated by:

```text
has_country_flag = cannibalism_warlord_workshop_conversion_open
NOT = {
    check_variable = {
        cannibalism_warlord_recruitment_template = constant:cannibalism_recruitment_template.emergency_reinforcement
    }
}
```

The normal workshop recovery route remains unchanged for non-emergency recruitment templates. The existing emergency manpower and Deaths-ledger transaction blocks remain unchanged.

## Validation and evidence

- Source inspection confirmed the emergency decision uses `cannibalism_emergency_reinforcement_requirements_tt` through `custom_trigger_tooltip` and retains `custom_cost_trigger` with the same readiness trigger.
- Source inspection confirmed the readiness trigger still uses Larder and `has_equipment` checks without an equipment-removal effect.
- Source inspection confirmed the transaction still calls `cannibalism_pay_current_warlord_larder_cost`, computes `cannibalism_warlord_recruitment_manpower`, and calls `add_manpower` before the guarded workshop branch.
- Narrow staged-diff review must show only the added emergency exclusion in the effect file and this handoff. The shared effect file has unrelated concurrent worktree/index changes; those were preserved and excluded from this commit.
- Localisation BOM was checked as UTF-8 with BOM before handoff.
- No probability/AI audit was required because this patch does not alter a weight or probability surface. No GUI MCP call was required because no GUI surface changed. Live HOI4 execution was not performed; runtime review remains with the parent/user.

## Remaining review items

The parent should review this one-line route separation together with concurrent edits in `014_cannibalism_effects.txt` before integration. No broader Event 014 balance, mission, GUI, or asset conclusions are implied by this narrow fix.

