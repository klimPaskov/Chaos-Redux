# Decision and mission cleanup handoff

## Scope and outcome

Inspected shared decision infrastructure and Event 001 through Event 020 decision and category surfaces only.

No Event 021 or higher decision, category, helper, or localisation surface was changed.

Patched two Event 020 category registrations and three Event 020 custom-cost localisation families.

## Changed files

`common/decisions/categories/020_black_plague_rat_categories.txt` is new.

It registers `black_plague_rat_brood_category` and `black_plague_rat_king_court_category` with the existing contamination-defense category sprite.

`localisation/english/020_black_plague_weaponization_l_english.yml` updates `black_plague_weaponization_approach_cost` and `black_plague_weaponization_delivery_cost`, then adds the matching `_blocked` and `_tooltip` keys.

`localisation/english/020_black_plague_response_l_english.yml` adds `black_plague_request_doctor_wu_access_cost_blocked` and `black_plague_request_doctor_wu_access_cost_tooltip`.

## Before and after

Before the patch, `black_plague_rat_brood_category` and `black_plague_rat_king_court_category` were decision roots with localisation and decision children but had no definitions under `common/decisions/categories/`.

After the patch, both categories are registered and use the existing `black_plague_rat_country_is_active` and `black_plague_rat_country_is_king` predicates, which already exclude retired carriers.

Before the patch, the Doctor Wu access and weaponization custom-cost displays were missing engine-resolved blocked and hover variants.

After the patch, each of those custom-cost families resolves normal, blocked, and hover localisation, with the actual materials, command power, fuel, civilian-factory commitment, and duration shown from the existing constants.

## Decision category lifecycle notes

The new Rat Nation categories disappear when the carrier retires because the reused predicates reject `black_plague_rat_country_retired` and `black_plague_rat_king_country_retired`.

The Rat Nation cleanup effect already clears its active-country flags, removes non-human ideas and unit templates, and removes the retired carrier from the global country array when it has no controlled states.

The weaponization actions remain in the shared `chaosx_disease_containment_category` and cancel when the project or selected state becomes invalid.

## Mission quality notes

The structural audit found 345 Event 001 through Event 020 timed missions.

Every audited mission contained an `available` block, a `timeout_effect`, and either an `activation` block or `selectable_mission` declaration.

Event 020’s patched Rat Nation and weaponization actions are decisions, not timed missions.

The Event 018 hidden evolution-clock missions intentionally have no normal title or description localisation because their permanently hidden category and mission visibility prevent player display.

## Cost and requirement clarity notes

Event 020 now has complete cost variants for all 49 unique custom-cost keys across 52 call sites.

The Doctor Wu request uses support equipment, motorized equipment, convoys, fuel, and a timed request.

Weaponization approach decisions use support equipment, motorized equipment, command power, fuel, factory commitment, and duration.

Weaponized delivery requires a native plague-bomb payload, support equipment, command power, fuel, factory commitment, duration, a living valid actor, a cooldown-free stockpile, and a reachable hostile human-controlled state.

## AI validity and route-lock notes

Weaponized delivery checks readiness both at the root and target-state level, validates the hostile target state again on availability and cancellation, and has a cooldown applied by the delivery effect.

Rat brood raising remains capped by `black_plague_rat_division_cap` and protected by `black_plague_rat_reinforcement_cooldown`.

No AI weights or target routing were changed.

## Issue list

### High, fixed

Event 020 Rat Nation decision categories were unregistered, leaving the category surface without its required category definitions.

### Medium, fixed

Three Event 020 custom-cost families lacked blocked and hover localisation variants, risking missing localisation and concealing the factory or duration commitment.

### Medium, deferred

161 custom-cost keys in Events 001, 005, 010, 014, and 016 lack at least one blocked or hover variant.

The required migration and verification sequence is recorded in `docs/plans/decision_system_plans/custom_cost_localisation_follow_up.md`.

### Medium, deferred

`black_plague_rat_absorb_a_weaker_brood` spends Brood Mass but calls the intentionally empty `black_plague_rat_try_absorb_adjacent_brood` helper.

The helper's one-carrier comment conflicts with the decision's territorial-absorption description, so it needs a mechanic decision rather than a cleanup-only patch.

The Event 020 design follow-up is recorded in `docs/plans/020_black_plague_plans/rat_absorption_follow_up.md`.

### Low, retained

Event 005, 014, 015, 016, and 020 deliberately split one category root across several decision files.

The category definitions are unique and the direct decision IDs do not collide, so moving these blocks would be a risky organization-only migration with no proven behaviour benefit.

## Validation

The Event 001 through Event 020 root-category audit now finds no missing category definitions.

The Event 020 custom-cost audit finds all normal, blocked, and hover localisation forms for its 49 unique cost keys.

The targeted weaponization source review confirmed its target-root, target-state, cancellation, cooldown, and payment paths use the same existing readiness predicates.

The touched English localisation files retain UTF-8 BOM encoding.

## Skipped validation

No in-game session was launched because live consumer validation belongs to the user.

No GUI inspection was needed because this patch did not change a decision-owned GUI surface.

## Remaining risks

The broad custom-cost migration and the Rat Nation absorption no-op remain unresolved and are deferred in the follow-up plan.

The cost scan did not treat Event 021 or higher as standalone cleanup targets.

## Skills used

Used `hoi4-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`.
