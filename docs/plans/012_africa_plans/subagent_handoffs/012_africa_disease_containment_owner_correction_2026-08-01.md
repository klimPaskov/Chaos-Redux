# Event 012 disease-containment owner correction

## Scope

This bounded tranche hardens the existing Event 012 achievement recorder for `africa_disease_made_and_unmade`. It does not add a new action, tag, model, unit, on-action scan, or disease system.

## Source change

`common/scripted_effects/012_africa_achievement_effects.txt` now increments `global.africa_achievement_disease_outbreaks_contained` only when `global.africa_achievement_active_disease_outbreaks` is greater than zero. The same guarded branch decrements one active outbreak. A full `contain_emergent_disease` result against a research site without a previously recorded weaponisation failure therefore remains a gameplay result but cannot create a false achievement proof.

## Existing owner path preserved

`africa_achievement_record_full_action` still opens the disease branch for containment, countermeasure, and weaponisation actions. `africa_achievement_record_action_outcome` still records an outbreak only on the declared weaponisation failure path. The completion trigger still requires the branch, route, outbreak, zero active outbreaks, at least one contained outbreak, and the countermeasure, plus its existing terminal disqualifiers.

## Validation

- The only callsite for `africa_achievement_record_disease_outbreak_contained` remains the full-result path for `contain_emergent_disease`.
- No new tag, model, recurring world iteration, or proxy achievement owner was introduced.
- The Event 012 overview and final completion audit now record the active-ledger guard and its remaining live-proof boundary.

## Remaining boundary

Live positive, failure, host-transfer, and cleanup scenarios remain open for the full 44-achievement acceptance pass. This correction narrows one owner; it does not claim the achievement package complete.
