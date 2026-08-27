# Event 020 decision and mission audit handoff

## Scope and result


The human Black Plague entries remain inside `chaosx_disease_containment_category`.

No dedicated Black Plague disease category was created or retained.

`black_plague_rat_brood_category` and `black_plague_rat_king_court_category` remain separate country-specific Rat and Rat King surfaces rather than human disease-board categories.

No decision-owned scripted GUI was changed, so `hoi4.gui_inspect` and `hoi4.gui_render` were not applicable.

## Changed files and identifiers

- `common/scripted_triggers/020_black_plague_shared_response_triggers.txt`: `black_plague_shared_can_armored_clearance`, `black_plague_shared_can_air_reconnaissance`, and `black_plague_shared_can_liberate_and_quarantine` now require an ordinary selectable response state with rat-occupation history.
- `common/script_constants/020_black_plague_shared_response_constants.txt`: the large and metropolitan scaled material gates now match the actual 1.5x and 2x payment calculated by `black_plague_begin_shared_state_action`.
- `common/decisions/020_black_plague_weaponization_decisions.txt`: `black_plague_weaponization_safety_first`, `black_plague_weaponization_military_acceleration`, `black_plague_weaponization_dual_use`, and `black_plague_weaponization_defensive_conversion` are mutually exclusive while a choice is running and cancel if the project can no longer continue.
- `common/decisions/020_black_plague_weaponization_decisions.txt`: `black_plague_weaponization_deliver_payload` now targets `any_state`, blocks a second active delivery, and cancels when its actor or target becomes invalid.
- `common/scripted_triggers/020_black_plague_weaponization_triggers.txt`: `black_plague_weaponization_approach_can_continue` and `black_plague_weaponization_delivery_actor_is_valid` were added as narrow lifecycle gates.
- `common/scripted_triggers/020_black_plague_weaponization_triggers.txt`: `black_plague_weaponization_target_state_is_valid` now requires a reachable enemy controller at war with ROOT and uses the existing ordinary exposure receiver gate, allowing a completed payload to seed clear or cured enemy states.
- `common/scripted_effects/020_black_plague_weaponization_effects.txt`: `black_plague_weaponization_choose_safety_first`, `black_plague_weaponization_choose_military_acceleration`, `black_plague_weaponization_choose_dual_use`, `black_plague_weaponization_choose_defensive_conversion`, and `black_plague_weaponization_deliver_to_state` now put their trigger checks inside `if = { limit = { ... } }` before executing effects.
- `localisation/english/020_black_plague_response_l_english.yml`: the three reclaimed-rat action descriptions now describe their actual post-liberation target state.
- `localisation/english/020_black_plague_weaponization_l_english.yml`: `black_plague_weaponization_deliver_payload_desc` now describes the enemy-state target without falsely requiring an already established outbreak.

## Before and after behaviour

The three shared anti-rat actions previously required `black_plague_shared_rat_state_can_start_action` while their decisions only targeted `any_controlled_state`, making a state transferred to a Rat controller unselectable by the responding country.

They now become available after the existing pulse restores a recaptured Rat state to its prior crisis phase and records `black_plague_liberated_rat_state`.



The shared response gate could accept 61 support equipment for a large state even though the begin effect charged 90, and could accept 91 for a metropolitan state even though it charged 120.

The gate now requires strictly more than the actual 90 or 120 support-equipment charge, with matching motorized and fuel values.

Weapon approach decisions could be activated in parallel and their scripted effects called scripted triggers directly as effects.

Only one approach can now be active, and each resolver first evaluates the existing availability trigger inside an effect-side `limit`.

Weapon delivery previously selected an actor-controlled established state and therefore could not deliver a payload against an enemy or reintroduce the disease after the actor's own outbreak ended.

It now selects a human enemy state at war with the actor and relies on `black_plague_apply_exposure`, which already performs the clear or cured to threatened transition for weaponized provenance.

## Decision-category lifecycle notes

The response and shared response state decisions use the existing selected-state board contract for human players and the AI target path for AI countries.

Their completion sets a pending action on ROOT, begins the state action, resolves through `remove_effect`, and invokes the existing cancel effect when the state becomes unusable.

The repaired anti-rat actions now follow that same lifecycle after a state is retaken instead of trying to run on a foreign Rat-held state through an incompatible target type.

Weapon approach selection is exclusive during its thirty-day timer, then marks one approach and pays the chosen cost only if the project remains active.

Weapon delivery consumes real stockpile, support equipment, command power, fuel, factory time, and a fourteen-day timer only after its completion guard still finds a valid enemy target.


## Mission quality notes

No `mission`, `mission_timeout`, or mission-specific field appears in the audited Event 020 decision files.

The timed items are decisions using `days_remove`, so mission owner, duration, success, failure, and duplicate-risk fields are not applicable to this scope.

The decision timer lifecycles above were checked instead.

## Cost and requirement clarity notes

The actual large and metropolitan shared-response material quotes are now protected by matching availability gates.

`black_plague_shared_action_cost` still describes a population-scaled material cost without displaying the selected state's exact quote.

The next UI pass should add scoped scripted localisation for the current selected state's support-equipment, motorized-equipment, and fuel totals rather than exposing a generic price sentence.

Weapon choices and delivery have real equipment, command-power, fuel, factory-time, and timer gates.

Rat King terminal preparation and immune-blood decisions remain unusually flat resource exchanges, as recorded below.

## AI validity and route-lock notes

Weapon payload targets now require an existing enemy controller at war with ROOT and `black_plague_state_can_receive_exposure = yes`, which excludes invalid, impassable, non-human, and Rat-controller targets through the shared exposure gate.

The four weapon approaches cannot be selected simultaneously by the AI, and their existing approach-specific AI modifiers remain unchanged.


No dead-country target or closed-route bypass was found in the repaired response or weaponization paths.

## Localisation, icons, and GUI notes

All decision-facing name, description, custom cost text, and custom effect tooltip keys referenced by the four audited decision files resolve in English localisation.

All non-vanilla decision icons referenced by those files resolve in the interface GFX definitions, including the five weaponization sprites in `interface/020_black_plague_weaponization.gfx`.

The two touched localisation files retain UTF-8 BOMs and have no duplicate keys.

No custom decision-owned scripted GUI surface exists in this audit scope, so there is no GUI render artifact or fidelity finding.

## Cleanup and exploit-risk notes

The new weapon-delivery cancel trigger and completion guard prevent a stale target from consuming equipment or applying a strike after control, war, or state eligibility changes during its timer.

The approach resolvers now safely do nothing when their project has ended or a different approach has completed first.

`black_plague_rat_king_send_the_royal_strike` remains a high-priority design gap because it has no map, enemy, or mission target, gives Brood Mass, and writes `black_plague_rat_royal_strike_recent`, which has no reader or expiry.

`black_plague_rat_king_mark_terminal_preparation` remains a high-priority exploit risk because it adds ten global preparation every thirty days without spending the Sentience or Cohesion that its localisation describes as an investment.

`black_plague_rat_harden_the_immune_blood` also grants permanent immunity and the Dominion idea without a Rat-pool cost or an availability gate beyond not already being immune.

## Remaining issues sorted by severity

1. High: Implement the Rat King Royal Strike as a real targeted operation with a legal enemy target, a meaningful outcome, a timed cooldown, and cleanup of `black_plague_rat_royal_strike_recent`.
2. High: Charge and clamp the stated Sentience and Cohesion investment for `black_plague_rat_king_mark_terminal_preparation`, or redesign its availability and progression so the action cannot farm terminal preparation for free.
3. Medium: `black_plague_shared_can_strike_royal_node` has no matching decision call site, leaving a declared royal-node counterplay action unreachable.
4. Medium: Give `black_plague_rat_harden_the_immune_blood` a Rat-pool or comparable opportunity cost and explain its one-time consequence in the decision surface.
5. Low: Display the exact population-scaled shared-response quote through dynamic localisation rather than only the generic `black_plague_shared_action_cost` text.

Items 1, 2, and 4 alter the Rat progression economy and need parent-owned design decisions rather than another narrow patch.

## Validation and evidence

Read the offline Paradox wiki snapshot for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, and AI before source inspection.

Read the applicable vanilla effects, triggers, script-constants documentation, and vanilla decision precedents, including `has_decision` mutual-exclusion examples.

Confirmed that all audited decision localisation and custom GFX references resolve, and confirmed that the touched localisation files have BOMs with no duplicate keys.


The focused HOI4 MCP event lint produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f43de795c14adccb8997c40973607732e42e39006ce941e69cf57b7a74a3aefe/179163c204b8b0f8d75f834dc1fb9756621cf40a69982c920261589a3c971dfd/event-lint-b9117f0642fd.json`.

Its fidelity is partial because the workspace-wide helper projections and lifecycle passes were deferred by the tool's large-workspace boundary, and it reported no blocking diagnostic for the focused query.

No Hearts of Iron IV session was launched, in accordance with repository policy.

## Recommended next owner actions

The parent should decide whether to accept a Rat King operation redesign for the three high-priority Rat economy issues, then create a bounded plan for that progression work.

The parent should also decide whether the uncalled `black_plague_shared_can_strike_royal_node` action is required by the accepted Event 020 matrix before adding a corresponding shared-category decision.

This handoff is the required plan handoff path for the broader Rat-operation follow-up.
