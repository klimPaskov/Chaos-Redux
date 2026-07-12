# Event 014 Focus-Closure Remediation Addendum

Date: 2026-07-12

Status: accepted, implemented, audited, and promoted into the Event 014 source specifications on 2026-07-13.

Disposition: H-01, H-02, H-03, and M-01 are implemented. The final country-package audit reports P0/P1/P2/P3 all at zero. The final focus audit reports no P0 or P1 and identifies only this documentation promotion plus the bounded P3 pre-lock AI behavior recorded in the source specs. All 21 final closure assets are present.

Audit source: docs/plans/014_cannibalism_plans/subagent_handoffs/event014_focus_tree_reaudit_2026-07-12.md

## Outcome

This addendum closes the four findings from the final Event 014 focus re-audit without adding another focus branch, country route, lore package, scripted GUI, or passive world scan.

The bounded implementation is:

1. one reusable country-target scoring contract with a unified profile and a route-aware Wendigo profile;
2. four terminal-hunt decision surfaces: launch, mission, press, and defender break;
3. two additional selectable Wendigo operations: receipt-gated Pack muster and inherited winter-cell activation;
4. three staged Pack upgrades, four inherited origin-template upgrades, and two inherited-commander stages folded into the existing 28-focus Wendigo overlay;
5. an exact normalization or explicit exception for every non-round authored value in the two focus-constant files cited by H-03; and
6. six new decision DDS files, one unique file for each new selectable or mission decision.

The previous closure addendum at docs/plans/014_cannibalism_plans/improvement_loop/2026-07-12_event014_post_implementation_closure_addendum.md is implemented:

- constituent technology union is live; and
- all 39 unified decision IDs have their own registered decision icons.

Those two items are not reopened here. Their final implementation facts are reconciled into the Event 014 source-of-truth documentation with this closure tranche.

## Finding disposition

| Audit finding | Required closure | Bounded implementation in this addendum |
|---|---|---|
| H-01 | Real reusable target scoring and route-aware AI consumers | Two country scorers, shared factor triggers/constants, two decision-weight MTTH entries, six unified decision consumers, Wendigo pre-lock priority, and Wendigo post-lock global-war priority |
| H-02 | A paid target-aware terminal-hunt family | Exactly four IDs: launch, mission, press, and defender break, with one persistent target, timer, success, failure, counterplay, AI, and full cleanup |
| H-03 | Round authored tuning or explicit formula/engine exceptions | Exact normalization table for both cited focus-constant files plus a narrow exception ledger for semantic counts and multiplier encodings |
| M-01 | Deeper Wendigo progression | No new focuses: receipt-gated recruitment, three Pack stages, four inherited origin upgrades, two commander stages, one inherited-cell operation, and the terminal hunt are attached to existing focus rewards |

## Non-negotiable boundaries

- The original live ZZZ country remains the transformed country. No replacement tag, reconstructed OOB, replacement Pack template, or identity swap is permitted.
- The Wendigo Pack remains a 16-battalion locked template. Upgrades add support structure only; they do not replace its battalions or open normal queue recruitment.
- Every population-funded muster uses cannibalism_prepare_consumption_context, checks cannibalism_population_loss_applied against the exact request, and records the population loss once through the canonical Event 014 Deaths-backed transaction.
- Enemy-death receipts are permission tokens only. They never create manpower, population, equipment, Larder, units, or Deaths entries.
- The receipt muster still pays exact controlled usable-state population, Larder, infantry equipment, and support equipment.
- No new on_daily, on_weekly, on_monthly, or equivalent whole-world on-action is allowed. Enemy-loss receipt sampling runs only from the existing Event 014 pulse and only across current enemies of the one live Wendigo actor.
- The final focus may complete the terminal route, but only cannibalism_process_wendigo_transformation_pulse may call cannibalism_complete_wendigo_terminal_lock and set world_end.
- Broken anchors and the existing counterwar remain meaningful before the pulse applies the final lock.
- Player-facing content may use Hannibal Lecter only after cannibalism_reveal_complete.
- No ancient-general, Carthaginian, Punic, or classical framing is permitted.
- No text may claim to represent living Indigenous traditions. The transformed route remains the mod's fictional Event 2/Event 14 entity.
- No fallback icon, shared icon, generic substitute, or transform-only duplicate art is accepted for the six new decisions.

## H-01: reusable country-target scoring

### Architecture

Add the following dedicated files:

- common/script_constants/014_cannibalism_target_score_constants.txt
- common/scripted_triggers/014_cannibalism_target_scoring_triggers.txt
- common/scripted_effects/014_cannibalism_target_scoring_effects.txt
- common/scorers/country/014_cannibalism_target_scorers.txt

Update:

- common/mtth/014_cannibalism_mtth.txt
- common/decisions/014_cannibalism_unified_decisions.txt
- common/decisions/014_cannibalism_wendigo_decisions.txt
- common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt
- common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt
- common/scripted_effects/014_cannibalism_unified_focus_effects.txt
- common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt
- common/scripted_effects/014_cannibalism_super_event_effects.txt
- localisation/english/014_cannibalism_l_english.yml
- docs/events/014_cannibalism.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_9_ai_balance_and_integrations.md
- docs/specs/014_cannibalism_specs/matrices/ai_strategy_matrix.md

The scorer file is the ordered-country consumer. The MTTH entries are the targeted-decision consumer. Both must use the same scripted predicates and script constants; no decision may carry its own unrelated major-only or at-war-only substitute.

### Exact scorer and MTTH identifiers

Country scorers:

- cannibalism_unified_target_scorer
- cannibalism_wendigo_target_scorer

Decision-weight MTTH entries:

- cannibalism_unified_target_decision_weight
- cannibalism_wendigo_target_decision_weight

The Wendigo scorer is one profile with stage-aware modifiers:

- before cannibalism_wendigo_transformation_locked, it prefers current enemies with cold fronts and high usable population;
- after the pulse applies the terminal lock, it prefers remaining high-population countries, faction leaders, coalition capitals, and major population centers.

The scorer scope contract must be documented in the new scorer file:

- scorer target/default scope: candidate country;
- scorer FROM: initiating unified or Wendigo actor;
- targeted-decision ROOT: initiating actor;
- targeted-decision FROM: candidate country.

Target-only factor predicates are shared directly. Relationship predicates receive mirrored scorer and targeted-decision wrappers so ROOT/FROM reversal is explicit rather than implicit.

### Exact trigger identifiers

Hard eligibility:

- cannibalism_target_country_has_usable_population
- cannibalism_target_country_is_ordinary_human_target
- cannibalism_target_country_has_physical_route_from_actor
- cannibalism_unified_scored_target_is_valid
- cannibalism_wendigo_scored_target_is_valid

Positive factors:

- cannibalism_target_has_high_population_center
- cannibalism_target_has_very_high_population_center
- cannibalism_target_has_weak_supply
- cannibalism_target_has_existing_cells
- cannibalism_target_has_prison_route
- cannibalism_target_has_port_route
- cannibalism_target_has_low_stability
- cannibalism_target_has_rail_or_naval_route
- cannibalism_target_is_coalition_leader
- cannibalism_target_has_cold_front
- cannibalism_target_is_postlock_population_or_capital_priority

Relationship and actor-state factors:

- cannibalism_scored_target_is_current_enemy
- cannibalism_scored_target_is_adjacent_to_actor
- cannibalism_scoring_actor_is_overextended
- cannibalism_scoring_actor_has_mature_distant_logistics

The target validity predicates must exclude rather than merely down-weight:

- the actor itself;
- allies, faction members, and subjects of the actor;
- capitulated or non-existing countries;
- Event 014 cannibal countries that cannot be valid hostile targets;
- actual nonhuman countries other than the live transformed ZZZ actor;
- countries with no controlled state that is outside cannibalism_state_is_unusable_larder;
- countries whose only population is wasteland, consumed, irreversibly contaminated, or below the existing minimum consumable population;
- targets with no current war, land adjacency, inherited active-cell route, or permitted rail/naval corridor;
- targets already protected by the existing per-operation target lock; and
- a second terminal-hunt target while one hunt is active.

Physical reach is true only through one of these proved routes:

- current war;
- direct country adjacency;
- an inherited active Event 014 cell in the target;
- both sides possessing a usable port while the actor has cannibalism_unified_global_naval_corridors_open, inherited island knowledge, or the Wendigo winter network; or
- post-lock global-war reach for an otherwise usable human population target.

There is no reach rule based only on being a major.

### Exact score constants

Define category cannibalism_target_score in common/script_constants/014_cannibalism_target_score_constants.txt:

| Key | Value | Meaning |
|---|---:|---|
| base | 100 | Score of a valid ordinary target before factors |
| invalid | 0 | Defensive zero for any target that escapes the target trigger |
| high_population_state_k | 1000 | One controlled usable state with at least one million people |
| very_high_population_state_k | 5000 | One controlled usable state with at least five million people |
| high_population_add | 30 | High-population bonus |
| very_high_population_add | 60 | Very-high-population bonus; use instead of, not in addition to, high |
| weak_supply_add | 25 | Low infrastructure, missing supply node, or documented supply pressure |
| existing_cell_add | 35 | At least one active Event 014 cell |
| prison_route_add | 20 | At least one usable prison/camp route |
| port_route_add | 20 | At least one usable controlled naval base |
| low_stability_threshold | 0.40 | Low-stability threshold |
| low_stability_add | 25 | Low-stability bonus |
| adjacency_add | 40 | Direct land-neighbor bonus |
| rail_or_naval_route_add | 25 | Proved rail or naval route bonus |
| coalition_leader_add | 50 | Faction leader or recorded coalition/defeat-contributor command hub |
| current_enemy_add | 30 | Current-war continuity bonus |
| cold_front_add | 50 | Wendigo pre-lock cold-front bonus |
| postlock_population_add | 75 | Wendigo post-lock population-center bonus |
| postlock_capital_add | 75 | Wendigo post-lock faction/coalition capital bonus |
| partial_contamination_factor | 0.50 | Some contaminated states, but at least one usable population state remains |
| distant_reachable_factor | 0.50 | Reachable only through a proved distant route |
| overextension_enemy_count | 3 | Actor enemy-count threshold |
| overextension_factor | 0.25 | Penalty before mature logistics |
| mature_network_reach | 85 | Existing mature network threshold |
| medium_score | 175 | Middle AI-strategy band |
| high_score | 275 | High AI-strategy band |

Very-high population replaces high population so one state does not receive both bonuses. Prison, port, rail, cell, and coalition factors may stack because they describe distinct route advantages.

Cold-front evidence is bounded to live engine evidence:

- num_units_on_climate@cold_climate above zero for the target; or
- a controlled state with the live winter-temperature disruption used by the natural-disaster system.

It must not be guessed from culture, ethnicity, or a hand-authored country list.

Overextension applies when the actor has at least three active enemies and lacks both mature Network Reach and the appropriate global/distant logistics flag. It is a score penalty, not a permanent target ban. An actually unreachable target remains excluded.

### Exact scorer consumers

Add these reusable effects:

- cannibalism_get_unified_scored_targets
- cannibalism_get_wendigo_scored_targets
- cannibalism_unified_apply_scored_campaign_priorities
- cannibalism_wendigo_apply_scored_enemy_priorities
- cannibalism_wendigo_apply_scored_terminal_priorities

The get effects use get_sorted_scored_countries_temp with:

- cannibalism_scored_target_countries
- cannibalism_scored_target_values

Both are temporary arrays and must be cleared before and after use. No persistent global target-score cache is allowed.

The unified consumer replaces the current major/current-war shortcuts for exactly these six targeted decisions:

1. cannibalism_unified_seed_major_enemy_army
2. cannibalism_unified_prepare_global_campaign
3. cannibalism_unified_issue_terror_ultimatum
4. cannibalism_unified_provoke_border_incident
5. cannibalism_unified_destroy_coalition_hub
6. cannibalism_unified_collapse_enemy_front

Each ai_will_do block starts at zero and adds mtth:cannibalism_unified_target_decision_weight. Existing affordability and route-open checks remain hard gates. Border incidents remain adjacent-only, coalition-hub and front-collapse actions remain current-enemy-only, and the shared score orders candidates inside those valid pools.

CBL_read_the_continental_weakness continues to set cannibalism_unified_dynamic_campaign_scoring_open, but its completion effect must also call cannibalism_unified_apply_scored_campaign_priorities. The flag is no longer allowed to change only planning_speed.

The Wendigo consumer replaces cannibalism_wendigo_focus_prioritize_current_enemies. It assigns conquer, antagonize, and front_unit_request bands from the scorer:

- below medium_score: low route constants;
- medium_score through high_score exclusive: medium route constants;
- high_score or greater: high route constants.

Add these keys to the existing cannibalism_wendigo_ai category:

- prelock_target_low = 150
- prelock_target_medium = 250
- prelock_target_high = 400
- postlock_target_low = 1000
- postlock_target_medium = 2000
- postlock_target_high = 3000

cannibalism_activate_terminal_global_war keeps the ordinary Hannibal branch unchanged. In the Wendigo branch it must:

1. reject countries that fail cannibalism_wendigo_scored_target_is_valid;
2. obtain the post-lock score;
3. add score-banded conquer, antagonize, and front-unit strategies; and
4. create/declare the global war only against a valid usable target.

Empty wasteland and actual nonhuman countries do not receive a token low score and do not receive a terminal war goal.

### Localisation corrections

Update these existing keys so the text and live behavior match:

- CBL_read_the_continental_weakness_desc
- CBL_read_the_continental_weakness_tt
- ZZZ_wendigo_hunt_every_remaining_capital_desc
- ZZZ_wendigo_hunt_every_remaining_capital_tt
- ZZZ_wendigo_the_world_beneath_winter_desc
- ZZZ_wendigo_the_world_beneath_winter_tt

Add:

- cannibalism_unified_target_scoring_tt
- cannibalism_wendigo_prelock_target_scoring_tt
- cannibalism_wendigo_postlock_target_scoring_tt
- cannibalism_target_unreachable_tt
- cannibalism_target_unusable_population_tt

Player-facing text must describe population, cells, supply, prisons, ports, physical routes, stability, coalition command, cold fronts, and overextension. It must not mention score variables, caps, implementation history, or that a previous tooltip was inaccurate.

## H-02: paid terminal-hunt family

### Exact decision IDs and icons

Add exactly four terminal-hunt surfaces:

| Decision ID | Scope/category | Unique icon file |
|---|---|---|
| cannibalism_wendigo_launch_terminal_hunt | Targeted country decision in cannibalism_wendigo_command_category | gfx/interface/decisions/014_cannibalism/decision_cannibalism_wendigo_launch_terminal_hunt.dds |
| cannibalism_wendigo_terminal_hunt_mission | Activated actor mission in cannibalism_wendigo_command_category | gfx/interface/decisions/014_cannibalism/decision_cannibalism_wendigo_terminal_hunt_mission.dds |
| cannibalism_wendigo_press_terminal_hunt | Actor decision while the mission is active | gfx/interface/decisions/014_cannibalism/decision_cannibalism_wendigo_press_terminal_hunt.dds |
| cannibalism_break_wendigo_terminal_hunt | Defender decision in cannibalism_wendigo_counterwar_category | gfx/interface/decisions/014_cannibalism/decision_cannibalism_break_wendigo_terminal_hunt.dds |

Register one sprite per ID in interface/014_cannibalism.gfx using GFX_decision_<decision_id>.

The mission icon is not exempt from the unique-icon rule.

### Open and target rules

cannibalism_wendigo_launch_terminal_hunt is visible only when:

- cannibalism_wendigo_terminal_hunt_open is set by ZZZ_wendigo_hunt_every_remaining_capital;
- the actor satisfies cannibalism_wendigo_command_is_open;
- the route is not broken or locked;
- the countdown is active;
- no terminal hunt is active; and
- the launch cooldown is absent.

Its target must:

- satisfy cannibalism_wendigo_scored_target_is_valid;
- be at war with the actor before the terminal lock;
- have a usable capital/population objective;
- not be the current hunt target of another active mission; and
- not carry cannibalism_wendigo_terminal_hunt_target_lock.

The pre-lock hunt does not declare a free war and does not bypass normal diplomacy.

### Constants

Add category cannibalism_wendigo_terminal_hunt to common/script_constants/014_cannibalism_wendigo_constants.txt:

| Key | Value |
|---|---:|
| launch_larder | 400 |
| launch_command | 50 |
| launch_command_gate | 49.99 |
| launch_infantry | 750 |
| launch_infantry_gate | 749 |
| launch_support | 150 |
| launch_support_gate | 149 |
| mission_days | 120 |
| starting_pressure | 25 |
| pressure_goal | 100 |
| press_larder | 200 |
| press_command | 25 |
| press_command_gate | 24.99 |
| press_infantry | 250 |
| press_infantry_gate | 249 |
| press_support | 50 |
| press_support_gate | 49 |
| press_fuel | 500 |
| press_pressure | 25 |
| press_cooldown_days | 30 |
| defender_manpower | 10000 |
| defender_manpower_gate | 9999 |
| defender_command | 30 |
| defender_command_gate | 29.99 |
| defender_infantry | 500 |
| defender_infantry_gate | 499 |
| defender_support | 100 |
| defender_support_gate | 99 |
| defender_counterpressure | 25 |
| counterpressure_goal | 100 |
| success_progress | 5 |
| failure_progress | 10 |
| success_cooldown_days | 90 |
| failure_cooldown_days | 120 |
| target_lock_days | 120 |

Because days_mission_timeout is not documented to accept script-constant tokens, define @CANNIBALISM_WENDIGO_TERMINAL_HUNT_MISSION_DAYS = 120 at the top of common/decisions/014_cannibalism_wendigo_decisions.txt and use it only for the mission field. Keep mission_days in the script constants for tooltips, due-date variables, and validation. The two values must remain equal.

### Persistent state

Global event target:

- cannibalism_wendigo_terminal_hunt_target

Actor flags:

- cannibalism_wendigo_terminal_hunt_active
- cannibalism_wendigo_terminal_hunt_press_cooldown
- cannibalism_wendigo_terminal_hunt_launch_cooldown

Target flags:

- cannibalism_wendigo_terminal_hunt_defender
- cannibalism_wendigo_terminal_hunt_target_lock

Actor variables:

- cannibalism_wendigo_terminal_hunt_pressure
- cannibalism_wendigo_terminal_hunt_counterpressure
- cannibalism_wendigo_terminal_hunt_start_date
- cannibalism_wendigo_terminal_hunt_due_date
- cannibalism_wendigo_terminal_hunts_completed
- cannibalism_wendigo_terminal_hunts_failed

The global target is justified because the mission survives the launch effect chain. Only one original-ZZZ Wendigo actor and one hunt may exist. Every terminal path must clear it.

### Exact effects and lifecycle

Add:

- cannibalism_wendigo_start_terminal_hunt
- cannibalism_wendigo_press_active_terminal_hunt
- cannibalism_defender_break_active_terminal_hunt
- cannibalism_wendigo_terminal_hunt_has_succeeded
- cannibalism_wendigo_terminal_hunt_has_failed
- cannibalism_resolve_wendigo_terminal_hunt_success
- cannibalism_resolve_wendigo_terminal_hunt_failure
- cannibalism_clear_wendigo_terminal_hunt_runtime

Launch:

1. revalidate target and all four launch resources at click time;
2. pay Larder, Command Power, infantry equipment, and support equipment;
3. save the target as cannibalism_wendigo_terminal_hunt_target;
4. set actor/defender flags and the target lock;
5. set pressure to 25 and counterpressure to zero;
6. store start and due dates;
7. activate cannibalism_wendigo_terminal_hunt_mission; and
8. apply the scored high-priority AI strategy to this target.

Press:

1. require an active valid target;
2. require the press cooldown to be absent;
3. pay Larder, Command Power, infantry equipment, support equipment, and fuel;
4. add 25 pressure and clamp it at 100; and
5. apply a 30-day press cooldown.

Pressing never creates units, equipment, manpower, population, war goals, or receipts.

Defender break:

1. remains visible to the flagged defender even if no transformation anchor is currently reachable;
2. requires the defender to exist, remain at war, control its capital, and pay manpower, Command Power, infantry equipment, and support equipment;
3. adds 25 counterpressure and clamps it at 100;
4. records the defender through cannibalism_record_current_country_as_defeat_contributor; and
5. does not directly destroy an anchor or manufacture a mission success.

This decision supplements, rather than replaces, the existing identify/assault/disrupt/break-site counterwar. Breaking anchors can still fail the hunt by breaking the whole route.

Mission success is:

- the target has capitulated; or
- the actor controls the target capital and hunt pressure has reached 100.

Mission failure is any of:

- the mission times out;
- counterpressure reaches 100;
- the transformation route breaks;
- the actor loses every live anchor;
- actor or target ceases to exist;
- the target is no longer at war with the actor before success; or
- the target becomes invalid/unusable before success.

Success:

- increments cannibalism_wendigo_terminal_hunts_completed by one;
- adds exactly 5 transformation progress and clamps it;
- applies the normal target lock/cooldown;
- does not set world_end;
- does not award a second winter-victory or enemy-death receipt if capitulation already did so; and
- clears all active hunt runtime.

Failure:

- increments cannibalism_wendigo_terminal_hunts_failed by one;
- subtracts exactly 10 transformation progress and clamps it;
- applies the longer launch cooldown;
- leaves the existing anchor counterplay intact; and
- clears all active hunt runtime.

Cleanup must remove the mission when called externally, remove the active defender flag and any active hunt modifier, clear all hunt variables except lifetime completed/failed counters, and clear cannibalism_wendigo_terminal_hunt_target. On ordinary success or failure, the timed cannibalism_wendigo_terminal_hunt_target_lock remains until its original expiry so the same country cannot be relaunched immediately. Route break, terminal lock, actor removal, and Event 014 global cleanup also clear that timed lock.

Call cleanup from:

- success;
- failure;
- timeout;
- cannibalism_break_wendigo_transformation_route;
- cannibalism_complete_wendigo_terminal_lock;
- actor capitulation/removal;
- Event 014 global cleanup; and
- any lifecycle reconciliation that invalidates the original-ZZZ actor.

At terminal lock, an unresolved pre-lock hunt is cleared before scored post-lock global-war strategies are assigned. The lock itself remains pulse-only.

### AI

- Launch uses mtth:cannibalism_wendigo_target_decision_weight.
- AI launch factor is zero unless it can pay every launch cost and retain at least the existing minimum Larder after payment.
- AI prefers a current enemy at medium/high score, a target whose capital is already threatened, and a target with inherited cells.
- AI press factor is high only when the target capital is controlled or hunt pressure is at least 50 and all resources can be paid.
- AI stops pressing when anchors are below the countdown minimum or Larder is below the countdown minimum.
- Defender AI uses the break decision when counterpressure is below 100, its capital is controlled, and it can pay without dropping below the existing manpower/equipment safety gates.

### Localisation

For every decision add the base key, _desc, _cost_text, and _effect_tt. Also add:

- cannibalism_wendigo_terminal_hunt_success_tt
- cannibalism_wendigo_terminal_hunt_failure_tt
- cannibalism_wendigo_terminal_hunt_target_tt
- cannibalism_wendigo_terminal_hunt_pressure_tt
- cannibalism_wendigo_terminal_hunt_counterpressure_tt

Descriptions must state the target, timer, paid resources, capital/pressure success, defender counterpressure, timeout/route-break failure, and absence of free formations.

## M-01: deeper Wendigo progression inside the existing tree

### A. Bounded enemy-death receipts

Add the following variables:

Actor:

- cannibalism_wendigo_enemy_death_receipts

Per current enemy:

- cannibalism_wendigo_enemy_casualties_snapshot
- cannibalism_wendigo_enemy_death_remainder
- cannibalism_wendigo_enemy_death_receipts_issued

Flags:

- cannibalism_wendigo_enemy_death_receipts_open
- cannibalism_wendigo_receipt_muster_open

Add category cannibalism_wendigo_enemy_death_receipt:

| Key | Value | Contract |
|---|---:|---|
| casualties_per_receipt | 50000 | New enemy military casualty delta required for one receipt |
| per_enemy_cap | 2 | Maximum receipts from one enemy country |
| pool_cap | 5 | Maximum unspent receipts held |
| muster_receipt_cost | 1 | Semantic receipt count |
| muster_population_k | 100 | Exact controlled usable-state population payment |
| muster_minimum_population_k | 105 | Click-time reserve gate |
| muster_larder | 200 | Larder payment |
| muster_infantry | 500 | Infantry-equipment payment |
| muster_infantry_gate | 499 | Availability gate |
| muster_support | 100 | Support-equipment payment |
| muster_support_gate | 99 | Availability gate |
| muster_pack_batch | 1 | One empty Pack; semantic unit count |
| muster_manpower_factor | 0.50 | Population-to-reinforcement-pool formula |
| muster_cooldown_days | 30 | Actor cooldown |

Add effects:

- cannibalism_initialize_wendigo_enemy_death_receipts
- cannibalism_process_wendigo_enemy_death_receipts
- cannibalism_process_current_wendigo_enemy_death_delta
- cannibalism_muster_wendigo_pack_from_enemy_death_receipt_effect

Receipt sampling rules:

1. ZZZ_wendigo_count_the_winter_victories opens receipts and snapshots current casualties for every current enemy. Existing losses are not retroactive.
2. The existing Event 014 pulse calls cannibalism_process_wendigo_enemy_death_receipts only for the live pre-lock Wendigo actor.
3. The helper loops every_enemy_country, never every_country.
4. A newly encountered enemy receives a snapshot first and no receipt on that first sample.
5. Later samples subtract the saved exact casualties value, add only positive deltas to that enemy's remainder, and update the snapshot.
6. Each full 50,000 casualties may issue one receipt, subject to the per-enemy cap of two and held-pool cap of five.
7. The threshold amount is subtracted from the remainder for every issued receipt. A casualty counter reset clears the stale remainder and resets the snapshot; it never creates a negative or compensating receipt.
8. The receipt logic reads casualties only. It does not call a Deaths effect or modify any Deaths total.

The engine casualties variable is total military casualties suffered by that enemy. Localisation must say recorded new losses while the target was an active enemy; it must not claim every loss was personally inflicted by the Wendigo actor.

The Chaos Meter/Deaths system remains the canonical military-death accounting surface. Receipt bookkeeping never counts those deaths again.

### B. Receipt-gated Pack muster

Add one state-targeted decision:

- ID: cannibalism_muster_wendigo_pack_from_enemy_death_receipt
- icon: gfx/interface/decisions/014_cannibalism/decision_cannibalism_muster_wendigo_pack_from_enemy_death_receipt.dds
- sprite: GFX_decision_cannibalism_muster_wendigo_pack_from_enemy_death_receipt

It requires both receipt and muster focus flags, one receipt, Pack capacity, no actor cooldown, a live anchor, an unbroken recruitment site, and a controlled usable state with at least 105K population.

The effect order is mandatory:

1. save the selected state as cannibalism_consumption_target_state;
2. request exactly 100,000 people with recruitment context;
3. require result applied and cannibalism_population_loss_applied equal to 100,000;
4. pay one receipt, 200 Larder, 500 infantry equipment, and 100 support equipment;
5. convert only the applied population loss through the 0.50 manpower factor;
6. create one Wendigo Pack with start_equipment_factor = 0 and start_manpower_factor = 0;
7. increment the existing cannibalism_wendigo_trained_pack_count and respect the existing Pack capacity;
8. apply the existing state recruitment cooldown and a 30-day actor cooldown.

The receipt is a gate and discount against the ordinary 160K/240-Larder two-Pack batch. It is not a population or manpower substitute.

Refactor the existing spawn helper into:

- cannibalism_spawn_empty_wendigo_pack_batch

It accepts a temporary batch input and always uses the current zero equipment/manpower start factors. The existing train decision passes its existing batch of two. The receipt muster passes one. Neither caller may unlock normal queue recruitment.

### C. Three Pack stages

Add flags:

- cannibalism_wendigo_pack_stage_drilled
- cannibalism_wendigo_pack_stage_hunting
- cannibalism_wendigo_pack_stage_frozen_larder

Add idempotent effects:

- cannibalism_wendigo_apply_pack_stage_drilled
- cannibalism_wendigo_apply_pack_stage_hunting
- cannibalism_wendigo_apply_pack_stage_frozen_larder

Attach them to:

| Existing focus | Stage | Exact structural change |
|---|---|---|
| ZZZ_wendigo_drill_the_original_pack | Drilled | Add recon support to Wendigo Pack |
| ZZZ_wendigo_expand_the_hunting_packs | Hunting | Add engineer support to Wendigo Pack |
| ZZZ_wendigo_army_of_the_frozen_larder | Frozen Larder | Add logistics_company support to Wendigo Pack |

Use add_units_to_division_template and the stage flag to prevent duplicate support companies. Do not add or remove any of the 16 wendigo_zombies battalions. Existing and later Packs inherit the upgraded template and must draw the added support manpower/equipment through normal reinforcement.

### D. Four inherited origin variants

Add flags:

- cannibalism_wendigo_origin_variants_open
- cannibalism_wendigo_origin_island_winterbound
- cannibalism_wendigo_origin_siege_winterbound
- cannibalism_wendigo_origin_march_winterbound
- cannibalism_wendigo_origin_prison_winterbound

Add:

- cannibalism_wendigo_apply_inherited_origin_variants

ZZZ_wendigo_all_inheritances_intact calls the helper once. It upgrades only templates whose inherited knowledge flag exists:

| Inherited flag | Existing locked template | One-time support addition |
|---|---|---|
| cannibalism_unified_origin_island_knowledge | Island Reavers | recon |
| cannibalism_unified_origin_siege_knowledge | Siege Eaters | artillery |
| cannibalism_unified_origin_march_knowledge | March Predation Column | logistics_company |
| cannibalism_unified_origin_prison_knowledge | Lockhouse Column | engineer |

These are the supernatural winter-bound variants promised by the route. They retain the existing template names and units, add no free equipment or manpower, remain locked, and continue to be raised only through the paid Event 014 recruitment helper.

If an inherited flag or template is absent, that variant is skipped. No generic replacement variant is created.

### E. Two inherited-commander stages

Add unit-leader traits to common/country_leader/014_cannibalism_traits.txt:

- cannibalism_wendigo_bound_captain
- cannibalism_wendigo_winter_hunt_captain

Add category cannibalism_wendigo_captain:

| Key | Value |
|---|---:|
| bound_attack | 0.05 |
| bound_supply | -0.05 |
| winter_attack | 0.10 |
| winter_speed | 0.05 |
| winter_recovery | 0.10 |
| winter_attrition | -0.15 |

Add flags:

- cannibalism_wendigo_captain_stage_bound
- cannibalism_wendigo_captain_stage_winter_hunt

Add effects:

- cannibalism_wendigo_bind_inherited_warlord_captains
- cannibalism_wendigo_refresh_inherited_commander_stage

ZZZ_wendigo_retain_the_warlord_captains applies the bound trait to every existing army leader who has cannibalism_host_commander or cannibalism_bound_servant. It does not create a commander and does not affect Hannibal.

ZZZ_wendigo_all_inheritances_intact opens the second stage. The refresh helper replaces bound with winter-hunt only after cannibalism_wendigo_winter_victories reaches the existing minimum. It runs on focus completion and from the existing Wendigo pulse so focus order cannot strand the upgrade.

No commander receives both stage traits.

### F. Inherited winter-cell operation

Add one targeted country decision:

- ID: cannibalism_activate_inherited_winter_cell
- icon: gfx/interface/decisions/014_cannibalism/decision_cannibalism_activate_inherited_winter_cell.dds
- sprite: GFX_decision_cannibalism_activate_inherited_winter_cell

Add flags:

- cannibalism_wendigo_inherited_cell_operations_open
- cannibalism_wendigo_inherited_cell_target

Add country array:

- cannibalism_wendigo_active_cell_targets

Add effects/triggers/modifier:

- cannibalism_wendigo_is_valid_inherited_cell_target
- cannibalism_wendigo_can_pay_inherited_cell_cost
- cannibalism_activate_inherited_winter_cell_effect
- cannibalism_clear_wendigo_inherited_cell_runtime
- dynamic modifier cannibalism_wendigo_inherited_cell_pressure

Add category cannibalism_wendigo_inherited_cell:

| Key | Value |
|---|---:|
| larder | 150 |
| command | 25 |
| command_gate | 24.99 |
| support | 100 |
| support_gate | 99 |
| duration_days | 60 |
| target_lock_days | 90 |
| hunt_pressure | 20 |

ZZZ_wendigo_keep_the_foreign_cells opens the decision.

A valid target must be an ordinary human current enemy with at least one active Event 014 cell and a usable population state. The target also passes the Wendigo scorer. The effect pays all costs, applies a 60-day supply/planning/organization disruption, adds the target to the active-cell array, and sets a 90-day target lock.

If the target is also cannibalism_wendigo_terminal_hunt_target, the operation adds 20 hunt pressure once and clamps it. It does not create a cell, population loss, Larder, equipment, a unit, or a war goal.

Inherited origin knowledge affects target reach/score, not free output:

- island knowledge validates proved port routes;
- siege knowledge raises capital/supply-pressure targets;
- march knowledge validates proved rail routes;
- prison knowledge raises prison-route targets.

Cleanup loops the registered active-cell array; it never scans every country.

### G. Exact existing-focus rewiring

No focus is added, removed, moved, or renamed.

| Existing focus | Required added behavior |
|---|---|
| ZZZ_wendigo_open_the_winter_hunt | Open/use the scored pre-lock Wendigo target profile |
| ZZZ_wendigo_count_the_winter_victories | Initialize and open bounded enemy-death receipts |
| ZZZ_wendigo_drill_the_original_pack | Apply Pack stage 1 |
| ZZZ_wendigo_open_the_pack_musters | Open receipt-gated muster in addition to existing paid training |
| ZZZ_wendigo_expand_the_hunting_packs | Apply Pack stage 2 |
| ZZZ_wendigo_army_of_the_frozen_larder | Apply Pack stage 3 |
| ZZZ_wendigo_retain_the_warlord_captains | Apply inherited commander stage 1 |
| ZZZ_wendigo_keep_the_foreign_cells | Open inherited winter-cell activation |
| ZZZ_wendigo_all_inheritances_intact | Apply available origin variants and open commander stage 2 |
| ZZZ_wendigo_hunt_every_remaining_capital | Open the four terminal-hunt surfaces and scored current-enemy priorities |
| ZZZ_wendigo_the_world_beneath_winter | Keep terminal hunt/route open and refresh scored priorities; do not lock |

Existing direct Command Power, Political Power, stability, war-support, authority, Frenzy, anchor, research, building, and capacity rewards remain only after H-03 normalization and the balance gates below.

### H. Route-break and lock cleanup

Extend cannibalism_break_wendigo_transformation_route to:

- clear active terminal-hunt runtime;
- clear inherited winter-cell runtime;
- clear receipt collection/muster flags and pool;
- clear terminal-hunt and receipt cooldowns;
- close new Pack recruitment operations; and
- leave the original ZZZ country, current units, locked templates, paid population history, Larder history, origin upgrades, and inherited commander traits intact.

Update cannibalism_wendigo_command_is_open and all new operation triggers to reject cannibalism_wendigo_transformation_broken.

Extend cannibalism_complete_wendigo_terminal_lock to:

- clear pre-lock hunt, cell, and receipt runtime before global-war strategy assignment;
- keep Pack/origin/commander structural upgrades;
- apply the scored post-lock target profile; and
- remain callable only from cannibalism_process_wendigo_transformation_pulse.

## H-03: exact focus-tuning normalization

### Warlord operating-order modifiers

In common/script_constants/014_cannibalism_warlord_focus_constants.txt, change:

| Key | Current | Required |
|---|---:|---:|
| burden_army_attack | 0.12 | 0.15 |
| burden_army_organization | -0.12 | -0.15 |
| council_planning | 0.12 | 0.15 |
| confederacy_speed | 0.12 | 0.15 |
| confederacy_organization_regain | 0.18 | 0.20 |
| confederacy_defence | 0.08 | 0.10 |
| rapid_organization_regain | 0.18 | 0.20 |
| rapid_attack | 0.12 | 0.15 |
| mobile_speed | 0.12 | 0.15 |
| discipline_organization_regain | 0.12 | 0.15 |
| alignment_organization | 0.12 | 0.15 |
| alignment_reinforce_rate | 0.04 | 0.05 |
| alignment_supply_consumption | -0.12 | -0.15 |
| manipulation_political_power | 0.12 | 0.15 |
| manipulation_efficiency_gain | 0.12 | 0.15 |
| manipulation_speed | 0.06 | 0.05 |
| defiance_attack | 0.18 | 0.20 |
| defiance_organization | 0.12 | 0.15 |
| defiance_political_power | -0.08 | -0.10 |

All other operating-order percentages already represent multiples of five percentage points or explicit closed-state sentinels.

### Warlord contract values

Change:

| Keys | Current sequence | Required sequence |
|---|---|---|
| recruit_experience_small / medium / large / elite | 0.03 / 0.05 / 0.08 / 0.12 | 0.05 / 0.10 / 0.15 / 0.20 |
| recruitment_cooldown_reduction_small / medium / large | 3 / 7 / 10 | 5 / 10 / 15 |
| recruitment_cooldown_minimum | 7 | 10 |
| prisoner_ledger_alignment_gain | 2 | 5 |
| provincial_integrity_gain | 2 | 5 |
| managed_frenzy_relief | -2 | -5 |
| rapid_frenzy_gain | 2 | 5 |
| council_frenzy_relief | -2 | -5 |
| operation_alignment_gain_small / medium | 2 / 4 | 5 / 10 |
| operation_network_reach_gain | 1 | 5 |
| officer_corruption_stability | -0.01 | -0.05 |
| island_convoy_recovery | 2 | 5 |
| march_train_recovery | 1 | 5 |

### Wendigo focus values

In common/script_constants/014_cannibalism_wendigo_focus_constants.txt, change:

| Keys | Current sequence | Required sequence |
|---|---|---|
| authority_small / medium / large | 1 / 2 / 3 | 5 / 10 / 15 |
| frenzy_medium | 4 | 5 |
| stability_small / medium | 0.02 / 0.04 | 0.05 / 0.05 |
| war_support_small / medium | 0.03 / 0.05 | 0.05 / 0.05 |

Keep pack_capacity_small = 2 and pack_capacity_large = 4 as explicit formula-derived count exceptions. They are not percentages or meter deltas: both are exact multiples of the existing two-Pack paid batch, and cannibalism_rebuild_wendigo_anchor_runtime combines them with the base and per-anchor capacity formula. Changing them to 5/10 would break that formula and sharply increase empty-formation capacity.

### Explicit exception ledger

The following non-five values are accepted only for these reasons and must receive comments beside their definitions:

| File/key | Reason |
|---|---|
| cannibalism_warlord_contract.major_victory_count_increment = 1 | Distinct-victory counter, not a tuned magnitude |
| cannibalism_warlord_contract.state_exhaustion_action_increment = 1 | One completed action recorded exactly once |
| cannibalism_warlord_contract.independent_capital_fort_levels = 2 | Engine building-level count |
| cannibalism_warlord_contract.defiance_resistance_fort_levels = 1 | Engine building-level count |
| cannibalism_wendigo_focus.pack_capacity_small = 2 | One existing two-Pack batch |
| cannibalism_wendigo_focus.pack_capacity_large = 4 | Two existing two-Pack batches |
| cannibalism_wendigo_focus.building_level = 1 | Engine building-level count |
| cannibalism_wendigo_focus.shared_building_slot = 1 | Engine shared-slot count |
| cannibalism_wendigo_focus.research_uses = 1 | Engine research-bonus use count |
| cannibalism_wendigo_focus.ai_branch_factor = 1.25 | Encodes a 25% AI factor |
| cannibalism_wendigo_focus.ai_war_factor = 1.50 | Encodes a 50% AI factor |
| cannibalism_wendigo_focus.ai_low_authority_factor = 1.40 | Encodes a 40% AI factor |
| cannibalism_wendigo_focus.ai_low_network_factor = 1.35 | Encodes a 35% AI factor |
| cannibalism_wendigo_focus.ai_countdown_factor = 2.00 | Encodes a 100% AI factor |
| cannibalism_wendigo_focus.ai_terminal_factor = 4.00 | Encodes a 300% AI factor |

The encoded percentages are all multiples of five. Closed-state values such as -1.00 and -1000 are engine sentinels and not authored incremental tuning.

No other arbitrary non-round value in the two cited files is accepted.

## Asset and localisation ledger

### Frozen six-icon ledger

| Row | Decision ID | DDS filename |
|---:|---|---|
| 1 | cannibalism_wendigo_launch_terminal_hunt | decision_cannibalism_wendigo_launch_terminal_hunt.dds |
| 2 | cannibalism_wendigo_terminal_hunt_mission | decision_cannibalism_wendigo_terminal_hunt_mission.dds |
| 3 | cannibalism_wendigo_press_terminal_hunt | decision_cannibalism_wendigo_press_terminal_hunt.dds |
| 4 | cannibalism_break_wendigo_terminal_hunt | decision_cannibalism_break_wendigo_terminal_hunt.dds |
| 5 | cannibalism_muster_wendigo_pack_from_enemy_death_receipt | decision_cannibalism_muster_wendigo_pack_from_enemy_death_receipt.dds |
| 6 | cannibalism_activate_inherited_winter_cell | decision_cannibalism_activate_inherited_winter_cell.dds |

All six live under gfx/interface/decisions/014_cannibalism/ and are registered in interface/014_cannibalism.gfx. Their compositions must be recognizably different at decision scale:

- launch: marked capital and converging winter routes;
- mission: timed pursuit/encirclement;
- press: committed columns closing inward;
- defender break: severed pursuit line and defended capital;
- receipt muster: ledger token, controlled population source, and empty Pack muster;
- inherited cell: concealed cell linked to a frozen route.

Do not reuse one image under six filenames. Do not use any existing decision DDS as the final source.

Update:

- docs/specs/014_cannibalism_specs/matrices/asset_inventory_matrix.md
- docs/plans/014_cannibalism_plans/014_live_asset_gap_map.md
- docs/plans/014_cannibalism_plans/014_remaining_static_asset_ledger.md

Asset production must use chaos-redux-event-assets. If any animation is proposed later, it is outside this closure and requires chaos-redux-frame-animation; these six decisions require static icons only.

### Localisation surfaces

Update existing Wendigo focus descriptions/tooltips for all focus rewires in the table above.

Add localisation for:

- six decision names;
- six descriptions;
- six cost texts;
- six effect tooltips;
- terminal-hunt success/failure/pressure/target tooltips;
- enemy-death receipt count and muster contract;
- the three Pack-stage flags/tooltips;
- four origin-variant state descriptions;
- two commander traits;
- inherited winter-cell pressure;
- the three scoring tooltips; and
- route-break cleanup.

All localisation stays in localisation/english/014_cannibalism_l_english.yml as UTF-8 with BOM, uses keys without :0, and speaks as if the feature has always existed.

The public name Hannibal Lecter is allowed only on post-reveal surfaces whose visibility is gated by cannibalism_reveal_complete.

## Balance gates

Implementation is not accepted until these gates are demonstrated:

### Target scoring

- A reachable high-population, low-stability neighbor with a cell outranks a distant major with no usable route.
- A coalition leader receives a meaningful bonus but cannot outrank a hard-invalid target.
- A fully contaminated/wasteland/nonhuman target is absent, not merely assigned a low positive score.
- Before mature logistics, the fourth simultaneous front is materially de-prioritized.
- Pre-lock Wendigo AI prefers a cold high-population current enemy.
- Post-lock Wendigo AI prefers remaining population centers and coalition capitals rather than assigning every country the same value.

### Hunt costs and outcomes

- One launch plus three presses costs 1000 Larder, 125 Command Power, 1500 infantry equipment, 300 support equipment, and 1500 fuel before any unrelated costs.
- A defender can reach 100 counterpressure only by paying four full defender operations.
- Launch/press cannot run with insufficient stockpiles.
- A successful hunt adds only 5 transformation progress and cannot itself lock the route.
- A failed hunt removes 10 progress and creates a longer cooldown.
- Anchor destruction can still break the route during the mission.

### Receipt muster

- The five-receipt held cap and two-receipt per-enemy cap prevent casualty-scale runaway.
- One receipt muster produces one empty Pack, not the ordinary two-Pack batch.
- The state loses exactly 100K population, the Deaths ledger receives that population loss once, and the actor also loses 200 Larder, 500 infantry equipment, and 100 support equipment.
- The receipt itself never changes manpower or Deaths.
- The existing Pack capacity and recruitment-site counterplay remain binding.

### Focus normalization

- The normalized warlord operating-order choices remain distinct and no modifier accidentally changes sign.
- The normalized recruitment-experience/cooldown ladders remain monotonic.
- The Wendigo focus route can reach the existing 80 Authority gate through intended play but does not receive authority outside completed focus rewards.
- Total direct stability from the Wendigo overlay remains 15 percentage points.
- Total direct war support from the five current call sites remains 25 percentage points.
- The 2/4 Pack-capacity exceptions continue to represent one/two paid batches.

### Structural upgrades

- Pack support stages increase reinforcement demand and never create support equipment.
- Origin upgrades occur only for inherited origins and never create a missing generic variant.
- Commander stages affect only inherited host commanders/bound servants and never create leaders.
- Route break closes new recruitment/hunt/cell operations while preserving the live country and already-paid formations.

## Validation scenarios

### Scenario 1: unified target matrix

Create or inspect at least eight simultaneous candidate countries: neighbor, current enemy, major, low-stability country, cell country, prison/port country, contaminated country, and unreachable island. Confirm validity, score order, and all six decision AI weights.

### Scenario 2: unified overextension

Compare the same reachable target at two active enemies and four active enemies, first without mature logistics and then with Network Reach 85 plus the correct route flag. Confirm the penalty appears and then clears.

### Scenario 3: Wendigo pre-lock score

Provide two valid enemies: one cold/high-population and one warm/low-population major. Confirm the first receives the higher decision and AI-strategy priority.

### Scenario 4: Wendigo post-lock score

Allow the pulse to lock, then compare a coalition capital/high-population target with a small reachable target. Confirm different global-war AI bands and no strategies/war goals for invalid nonhuman or wasteland targets.

### Scenario 5: hunt success by capitulation

Launch, pay all costs, capitulate the target before timeout, and confirm one success, one cleanup, no duplicate winter victory/receipt, and no direct world_end.

### Scenario 6: hunt success by capital pressure

Launch, pay three presses, control the target capital, and confirm success at pressure 100. Confirm every press cost and cooldown.

### Scenario 7: defender break

Pay four defender operations while holding the capital. Confirm counterpressure 100 resolves failure, records the contributor, applies the long cooldown, and clears the global target.

### Scenario 8: route break during hunt

Destroy the final anchor during an active hunt. Confirm transformation break, mission removal, target cleanup, receipt/cell closure, and preservation of original ZZZ identity and existing formations.

### Scenario 9: pulse-only final lock

Complete The World Beneath Winter and leave all gates satisfied. Confirm the focus does not set world_end. Confirm only the next valid transformation pulse clears pre-lock runtime, applies the locked idea/leader trait, and starts scored global war.

### Scenario 10: casualty receipt initialization

Open receipts against an enemy with prior casualties. Confirm the first snapshot gives zero receipts. Add fewer than 50,000 new casualties, then cross the threshold, and confirm exactly one receipt with the correct remainder.

### Scenario 11: receipt caps and reset

Cross multiple thresholds for one enemy and several enemies. Confirm per-enemy two and held-pool five. Simulate a lower casualty counter and confirm no negative or free receipt.

### Scenario 12: exact receipt muster

Use a controlled usable anchor state with sufficient population and all resource costs. Confirm exact state loss, exact Deaths record, exact resource payments, one empty Pack, capacity increment, and both cooldowns. Repeat each failed prerequisite and confirm no partial payment or population loss.

### Scenario 13: Pack stage idempotence

Complete each Pack focus once, rebuild/reload runtime helpers, and confirm exactly one recon, engineer, and logistics support addition with all 16 Wendigo battalions unchanged.

### Scenario 14: origin variants

Test island-only, siege-only, march-only, prison-only, multiple-origin, and no-origin inheritance. Confirm only corresponding existing locked templates gain their one support addition.

### Scenario 15: commander stages

Test focus order with winter victories before and after All Inheritances Intact. Confirm all and only inherited host commanders/bound servants move from bound to winter-hunt exactly once.

### Scenario 16: inherited cell and hunt interaction

Activate a real inherited cell against a non-hunt enemy and against the active hunt target. Confirm all costs, timed target modifier, registered cleanup, and the one-time 20 pressure interaction only for the hunt target.

### Scenario 17: focus tuning

Compare each affected warlord order and both full Wendigo routes before acceptance. Confirm signs, total stability/war support, Authority gate timing, Pack-cap formula, AI focus order, and no unintended duplicate reward.

### Scenario 18: assets/localisation

Confirm all six decision IDs resolve to six different registered DDS files and every visible decision/mission/focus/trait/modifier has aligned English localisation.

### Scenario 19: reveal and cultural boundary

Inspect every new visible surface before and after cannibalism_reveal_complete. Confirm no pre-reveal Hannibal Lecter name, no ancient/classical framing, and no claims about living Indigenous traditions.

### Scenario 20: lifecycle cleanup

Exercise success, timeout, defender failure, target capitulation, actor capitulation, route break, terminal lock, and global Event 014 cleanup. Confirm no stale global hunt target, mission, flag, modifier, registered cell target, receipt snapshot, or temporary score array.

## Implementation acceptance checklist

H-01 is closed only when:

- both scorer IDs exist and return ordered candidates;
- hard-invalid targets are absent;
- all stated spec factors are represented;
- all six unified targeted decisions consume the shared decision weight;
- CBL_read_the_continental_weakness changes target selection, not only planning speed;
- pre-lock and post-lock Wendigo AI values differ by score;
- global Wendigo war excludes impossible targets; and
- localisation accurately names the live factors.

H-02 is closed only when:

- all four hunt IDs are live;
- every launch/press/break cost is actually paid;
- one persistent target survives the mission and is always cleared;
- success, timeout, defender counterpressure, and route-break failure all work;
- defender counterplay is visible even without a reachable anchor;
- AI can choose and operate the family without overspending;
- no hunt effect grants units/population/equipment/manpower; and
- final lock remains pulse-only.

H-03 is closed only when:

- every required value in the normalization tables is changed;
- every retained non-five value appears in the exception ledger with its reason;
- no arbitrary non-round authored value remains in either cited file; and
- focus route balance gates pass.

M-01 is closed only when:

- receipt sampling is bounded and non-retroactive;
- receipt muster pays exact real population and stockpile resources;
- Pack stages are structural, idempotent, and keep the 16-battalion lock;
- inherited origins upgrade only their live templates;
- inherited commanders receive both stages without new characters;
- inherited cells create a real paid operation;
- terminal hunt is a real active loop;
- exact Deaths accounting, anchor counterplay, original ZZZ identity, and pulse-only lock are preserved; and
- every new selectable/mission decision has its own icon.

Final audit routing for this tranche was:

- chaosx_focus_tree_auditor
- chaosx_decision_mission_auditor
- chaosx_localisation_auditor
- chaosx_event_completion_auditor
- chaosx_country_package_auditor for original-ZZZ identity, unit/template, technology, and commander preservation.

Any audit finding is implementation work, not a documentation-only note.

## Documentation reconciliation

The verified implementation facts are reconciled in:

- docs/events/014_cannibalism.md
- Event 014 spec parts 5, 6, 8, 9, 10, and 12
- focus_route_matrix.md
- decision_mission_matrix.md
- ai_strategy_matrix.md
- asset_inventory_matrix.md
- idea_lifecycle_matrix.md
- package_status.md
- package_validation.md
- PACKAGE_MANIFEST.md
- the three live asset ledgers named above
- the previous closure addendum's implemented technology-union and 39-icon status.

The source specs must describe the accepted live behavior. This working addendum remains in plans and is not itself a substitute for source-of-truth promotion.

## Simplifications, omissions, and blockers

No design simplification or fallback was used for this addendum. H-01, H-02, H-03, and M-01 are implemented. The final country-package audit reports no findings. The final focus audit reports no P0 or P1, with documentation promotion completed here and the bounded P3 AI behavior documented in the source specifications.

The casualty receipt uses the engine's exact read-only casualties counter for active enemies. Because that counter represents all military casualties suffered by the target, player-facing text must not attribute every recorded loss to the Wendigo actor. This is an explicit engine-semantic boundary, not permission to estimate, generate, or double-count deaths.

If any required support subunit, scorer context, MTTH scope, mission field, or target lifecycle behaves differently under the current engine documentation, stop that implementation surface and resolve it against vanilla documentation and a vanilla precedent. Do not substitute an unapproved fallback.

## References consulted

Offline Paradox wiki snapshot:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- National focus modding

Vanilla documentation:

- documentation/script_concept_documentation.md
- documentation/effects_documentation.md
- documentation/triggers_documentation.md
- documentation/dynamic_variables_documentation.md
- documentation/collection_input_documentation.md
- documentation/collection_operator_documentation.md
- documentation/script_math_functions_documentation.md
- documentation/localisation_formatter_documentation.md
- documentation/localisation_objects_documentation.md
- common/script_constants/documentation.md
- common/on_actions/_documentation.md

Vanilla precedents:

- common/scorers/country/generic_operation_target_scorer.txt
- common/scorers/country/operative_mission_scorer.txt
- common/decisions/INS.txt persistent target and cleanup sequence
- common/decisions/PRC.txt activated mission success/failure sequence
- common/scripted_effects/00_scripted_effects.txt scorer retrieval

Chaos Redux live precedents:

- common/on_actions/014_cannibalism_on_actions.txt
- common/scripted_effects/014_cannibalism_unified_decision_effects.txt
- common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt
- common/scripted_effects/014_cannibalism_wendigo_effects.txt
- common/scripted_effects/014_cannibalism_super_event_effects.txt
- common/scripted_triggers/014_cannibalism_triggers.txt
- common/scripted_triggers/014_cannibalism_integration_triggers.txt
- common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt
- common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt
- common/national_focus/014_cannibalism_wendigo_focus.txt
- common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt
- common/script_constants/014_cannibalism_warlord_focus_constants.txt
- common/script_constants/014_cannibalism_wendigo_focus_constants.txt
- common/script_constants/014_cannibalism_wendigo_constants.txt
- common/country_leader/014_cannibalism_traits.txt
- history/units/ZZZ_weaponized_1936.txt
