# Event 011 Secret Alliance scripted-system architecture pass

Status: promoted implementation-architecture handoff. This pass did not edit gameplay, localisation, UI, GFX, audio, spreadsheet, or event-system files.

The architecture remains the accepted engine-safety and ownership baseline. References to provisional files, outstanding wiring, or pre-implementation blockers are historical. Gameplay commit `407b9a05`, with balance frozen at `1c87d923`, establishes current behavior. Earlier decision and localisation reports are scoped historical freezes. The holistic `completion_audit.md` owns the current verdict.

Date: 2026-07-10.

## Executive decision

Implement Event 011 as one global, event-owned context with one immutable target country, a durable active-member registry, and a single target-owned event scheduler. The hidden pact is not a faction. Every reveal route calls one guarded transaction which refreshes membership, snapshots achievement facts, forms the dynamic Anti-[target] Pact from a faction template, converts hidden values into wartime state, fires the reveal presentation once, and either starts or joins one normal war against the fixed target.

The automatic opening always selects exactly three distinct AI-controlled minor founders. Evolution I accelerates a later minor recruitment; Evolution II adds a major sponsor after the three-founder transaction; Evolution III starts from the Evolution II package and advances after a shortened, playable delay. This resolves the source-pack ambiguity without weakening the user's explicit three-minor-founder requirement.

No recurring global daily, weekly, or monthly on-action belongs in this system. Broad country enumeration is limited to setup or infrequent recruitment/scenario selection. Runtime work is limited to the target, the active arrays, and narrow on-actions.

## Required references and verified precedents

The following were read before this architecture was written.

### Repository guidance

- `AGENTS.md`.
- `.agents/skills/chaos-redux-events/SKILL.md`.
- `.agents/skills/hoi4-decisions-missions/SKILL.md`.
- `.agents/skills/chaos-redux-subagents/SKILL.md`.
- `.agents/skills/hoi4-mtth/SKILL.md`.
- The complete 33-file Event 011 package under `docs/specs/011_secret_alliance_specs/`.

### Offline wiki snapshot

Core pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. System-specific pages: Faction modding and Achievement modding.

Important conclusions:

- A regular event target lasts for an effect chain and is carried into events fired by that chain. A global event target persists and must be explicitly cleared.
- Temporary variables are unscoped. Persistent scope ownership therefore uses normal variables, country flags, arrays, and event targets.
- Arrays may contain duplicate scopes. Registration must use a flag guard before `add_to_array`.
- `on_war_relation_added` is the correct hook for every new hostile country pair. `on_war` is not equivalent.
- Targeted decisions use ROOT as the decision owner and FROM as the target, and a compact `target_array` is preferable to a world-wide target list.
- `create_faction` is obsolete. Template-backed factions use `create_faction_from_template`.

### Current vanilla documentation

- `documentation/script_concept_documentation.md`, especially Collections and Script Constants.
- `documentation/script_collection_input.md` and `documentation/script_collection_operator.md`.
- `documentation/effects_documentation.md`, especially arrays, loops, event targets, `country_event`, faction effects, `add_to_war`, mission activation/removal, and variable effects.
- `documentation/triggers_documentation.md`, especially collections, arrays, event targets, war/faction state, and `has_civil_war`.
- `common/script_constants/documentation.md`.
- `common/factions/_documentation.md`.

Engine constraints confirmed from those files:

- `game:all_countries` is a built-in collection. An anonymous collection can filter it in the caller's scope, and `every_collection_element` iterates that result.
- `collection_size` comparisons are inclusive even though their syntax uses `<` and `>`; this must be commented at the call site to prevent an off-by-one rewrite.
- `for_each_scope_loop` iterates an array and changes scope to the current element.
- `random_scope_in_array` can select from a scope array and apply an additional trigger limit.
- A variable can be assigned from `mtth:entry_name`; event delays can use a prepared variable.
- `add_to_war` accepts `targeted_alliance`, `enemy`, and `hostility_reason`.
- Not every effect field accepts `constant:`. Prepare a normal or temporary variable first where the field rejects a constant.

### Verified vanilla and Chaos patterns

- Vanilla `common/on_actions/05_lar_on_actions.txt`: the Iberian Pact uses `on_war_relation_added`; its comment confirms ROOT is the attacking side, FROM the defending side, and that this hook fires for every newly hostile pair.
- Vanilla `common/decisions/FIN.txt`: `add_to_war = { targeted_alliance = ... enemy = ... hostility_reason = asked_to_join }` joins a country to an ally's existing war against the specified enemy.
- Vanilla `common/decisions/DEN.txt`: current faction creation uses `create_faction_from_template`.
- Vanilla country scorers: `common/scorers/country/generic_platonic_scorers.txt` demonstrates `target_array`, MTTH-style scores, and `get_sorted_scored_countries`/`get_highest_scored_country` support.
- Chaos `common/scripted_effects/007_fury_effects.txt`: `fury_prepare_actor_selection_weight`, `fury_add_current_country_to_actor_selection_pool`, and `fury_select_weighted_actor_candidate` are the direct precedent for integer ticket weighting plus `random_scope_in_array`.
- Chaos `common/scripted_effects/chaosx_settings_effects.txt`: `fire_event_by_temp_id_no_cluster` runs event-specific pre-fire setup before dispatch and before the normal history row is recorded.
- Chaos `common/scripted_effects/chaosx_events_log_effects.txt`: `events_log_set_default_actor_for_current_event` and `record_events_log_evolution_entry` define the actor/evolution contracts.
- Chaos `common/scripted_effects/002_zombie_outbreak_effects.txt` and `common/factions/templates/anti_zombie_league.txt`: template-backed faction creation, global leader target, member joins, and cleanup.
- Chaos `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`: the registry, selected ID/type/intensity variables, confirmation-time dispatch, and scenario-owned immutable setup.
- Chaos `common/mtth/chaosx_mtth_variables.txt`: MTTH entries can use script constants and supply values to script.
- Chaos `common/scripted_effects/chaosx_dynamic_effects.md` and `common/scripted_triggers/chaosx_dynamic_triggers.md`: reuse `uses_normal_civilian_systems`, `is_special_chaos_country`, event-pool helpers, and log helpers. Event-specific helpers remain in Event 011 files.

## Verified baseline and concurrent work warning

At the beginning of this pass, Event 011 had no live gameplay implementation. It was deliberately unavailable in these surfaces:

- `common/scripted_effects/chaosx_logic_effects.txt`: registered as fire-once but excluded by `evaluate_random_event_active_pool_candidate`, and present in the default rework-disable queue.
- `common/scripted_effects/chaosx_settings_effects.txt`: `fire_event_by_temp_id_no_cluster` set Event 011's dispatch permission to zero.
- `common/scripted_effects/chaosx_events_log_effects.txt` and scripted localisation: the event could display `N/A`/unavailable detail.
- `localisation/english/chaosx_event_names_l_english.yml`: `chaosx.event_name.11` was `Event 011 Unavailable`.

During the architecture pass, parallel uncommitted files appeared at `common/script_constants/011_secret_alliance_constants.txt` and `common/scripted_triggers/011_secret_alliance_triggers.txt`. They are provisional concurrent work, not a completed or validated baseline. This handoff keeps compatible identifiers where they are sound and explicitly lists corrections still required. Do not use the older `docs/plans/011_secret_alliance_plans/011_secret_alliance_scripted_system_architecture.md` as the implementation source of truth: it predates the complete spec and incorrectly says there is no triggerable scenario.

## Exact file map

### Event-owned gameplay

| File | Responsibility |
| --- | --- |
| `events/011_secret_alliance.txt` | `add_namespace = chaosx.nr11`; root event, pulse events, operation reports, human consent, evolution transitions, reveal, and aftermath events |
| `common/script_constants/011_secret_alliance_constants.txt` | All shared identifiers, caps, bands, weights, costs, conversions, scenario scaling, AI values, and achievement thresholds |
| `common/collections/011_secret_alliance_collections.txt` | Stable base collections of normal AI and normal human countries; caller-specific filters remain anonymous collections |
| `common/scripted_triggers/011_secret_alliance_triggers.txt` | Target, founder, member, evolution, decision, scenario, reveal, postwar, and achievement gates |
| `common/scripted_effects/011_secret_alliance_effects.txt` | Context, selection, registry, operation, evolution, reveal, war, AI, scenario, snapshot, postwar, and cleanup transactions |
| `common/mtth/011_secret_alliance_mtth.txt` | Operation interval and AI/branch weights |
| `common/on_actions/011_secret_alliance_on_actions.txt` | Narrow war, annexation, capitulation, faction-change, and peace acceleration hooks |
| `common/scorers/country/011_secret_alliance_scorers.txt` | Prospective/reveal leader ordering and optional suspect prioritisation from compact arrays |
| `common/decisions/categories/011_secret_alliance_categories.txt` | Foreign-interference, coalition-crisis, revealed-war, and aftermath category lifecycle |
| `common/decisions/011_secret_alliance_decisions.txt` | Selectors, investigations, protection, diplomacy, deception, border actions, emergency actions, war fracture, and settlement missions |
| `common/ideas/011_secret_alliance_ideas.txt` | Maintained projects, temporary burdens, operation consequences, opening conversion, and member-specific weaknesses |
| `common/dynamic_modifiers/011_secret_alliance_dynamic_modifiers.txt` | Capped country-scale operation damage and opening/war packages that genuinely need variable input |
| `common/ai_strategy/011_secret_alliance.txt` | Flag-driven generic front/production behavior; dynamic target-specific strategies are applied by effects |

### Faction and presentation wiring

| File | Responsibility |
| --- | --- |
| `common/factions/templates/011_secret_alliance_anti_target_pact.txt` | `faction_template_secret_alliance_anti_target_pact` |
| `common/factions/rules/011_secret_alliance_rules.txt` | Join/member/leadership behavior |
| `common/factions/rules/groups/011_secret_alliance_rule_groups.txt` | Faction rule groups |
| `common/factions/goals/011_secret_alliance_goals.txt` | Coalition war and possible postwar goals |
| `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt` | Faction descriptor, meter bands, suspect confidence, motive/reveal/postwar text, and scenario type/intensity detail |
| `interface/011_secret_alliance.gfx` | Stable event, decision, faction, report, super-event, and achievement sprites |
| `localisation/english/011_secret_alliance_l_english.yml` | All player-facing Event 011 text, UTF-8 with BOM |

### Shared integration surfaces

- `common/scripted_effects/chaosx_logic_effects.txt`.
- `common/scripted_effects/chaosx_settings_effects.txt`.
- `common/scripted_effects/chaosx_events_log_effects.txt`.
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`.
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`.
- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`.
- `events/chaosx_triggerable_scenarios.txt`.
- scenario scripted GUI, GUI, and scripted localisation registry files.
- `common/achievements/chaos_redux_achievements.txt` and `interface/chaosx_achievements.gfx`.
- Event Logs name, detail, evolution, actor, and weight mappings.
- `docs/events/011_secret_alliance/overview.md`, `docs/systems/triggerable_scenarios.md`, `docs/systems/custom_achievements.md`, the Event 011 asset manifest, and spreadsheet rows.

## One-context state contract

### Context invariants

1. `secret_alliance_active` means exactly one runtime context exists.
2. `event_target:secret_alliance_target` never changes during that context.
3. The target may survive a subject transition, but a fully absorbed/non-playable target ends the run; the pact never retargets the conqueror.
4. Every active member has both `secret_alliance_active_member` and one entry in `global.secret_alliance_members`.
5. No array entry is trusted without the corresponding flag and validity trigger.
6. Hidden membership is not represented by a faction.
7. `secret_alliance_reveal_in_progress` prevents recursive on-action re-entry while factions and wars are being changed.
8. Runtime cleanup and historical/achievement facts are separate.

### Persistent global event targets

Use exactly these global event targets and clear each in `secret_alliance_cleanup_runtime_context`:

| Target | Purpose |
| --- | --- |
| `secret_alliance_target` | Immutable target country |
| `secret_alliance_leader` | Prospective/current coalition leader |
| `secret_alliance_sponsor` | First major sponsor, when one exists |
| `secret_alliance_second_major` | Second major at Evolution III/scenario, when one exists |
| `secret_alliance_selected_suspect` | Human UI selection across decision chains |
| `secret_alliance_target_starting_capital` | Starting capital state until the final achievement snapshot |

Use regular event targets for `secret_alliance_weighted_candidate`, `secret_alliance_operation_actor`, `secret_alliance_operation_target`, `secret_alliance_evidence_actor`, and `secret_alliance_war_anchor`. They are chain-local and must not be treated as durable state.

### Persistent arrays

| Array | Contents and rule |
| --- | --- |
| `global.secret_alliance_members` | Current valid active members only; unique through flag-guarded registration |
| `global.secret_alliance_founders` | The original three minor founders; historical until runtime cleanup |
| `global.secret_alliance_suspects` | All countries with live suspect confidence, including innocents |
| `global.secret_alliance_visible_suspects` | Compact human decision list; rebuild from suspects, do not expose every candidate |
| `global.secret_alliance_confirmed_members` | True members confirmed by the target; add once |
| `global.secret_alliance_turned_members` | Active or historical turned channels; add once |

Do not keep a mutable reveal-snapshot array after settlement. At reveal, iterate the refreshed member array and set country snapshot flags; store counts and conclusions on the target. Those facts survive runtime-array cleanup without retaining dead scope pointers.

### Global flags and variables

Flags:

- `secret_alliance_active`, `secret_alliance_revealed`, `secret_alliance_collapsed`, `secret_alliance_settled`.
- `secret_alliance_origin_normal`, `secret_alliance_origin_scenario`.
- `secret_alliance_evolution_i`, `secret_alliance_evolution_ii`, `secret_alliance_evolution_iii`.
- `secret_alliance_operation_active`, `secret_alliance_reveal_in_progress`, `secret_alliance_cleanup_in_progress`.
- `secret_alliance_public_faction_created`, `secret_alliance_super_event_shown`.
- `secret_alliance_false_plan_accepted`, `secret_alliance_offensive_countdown_active`.

Variables:

- `global.secret_alliance_phase`.
- `global.secret_alliance_run_sequence`.
- `global.secret_alliance_member_count`, `global.secret_alliance_minor_count`, `global.secret_alliance_major_count`.
- `global.secret_alliance_cohesion`, `global.secret_alliance_readiness`, `global.secret_alliance_alertness`.
- `global.secret_alliance_doctrine`, `global.secret_alliance_current_operation_family`.
- `global.secret_alliance_operation_pulses`, `global.secret_alliance_reveal_route`.

`secret_alliance_phase` values belong in constants: inactive `0`, hidden `1`, crisis `2`, revealed war `3`, aftermath `4`. Do not replace these states with multiple numeric booleans.

### Target-country state

Flags:

- `secret_alliance_target_country`.
- `secret_alliance_response_category_unlocked`, `secret_alliance_coalition_crisis_unlocked`.
- evidence-class flags described below.
- maintained-project flags and active mission-family flags.
- run-scoped achievement qualification/disqualification flags.

Variables:

- `secret_alliance_evidence`, `secret_alliance_preparedness`, `secret_alliance_war_pressure`, `secret_alliance_coalition_resolve`.
- preparedness components: `secret_alliance_staff_security`, `secret_alliance_industrial_security`, `secret_alliance_transport_security`, `secret_alliance_border_readiness`, `secret_alliance_continuity`, `secret_alliance_allied_coordination`, `secret_alliance_known_plans`.
- mission-family active counts and stored dynamic cost variables.
- reveal snapshot counts and wartime fracture counters.

Evidence and Preparedness become visible only with Evolution II. War Pressure becomes visible with Evolution III. Coalition Resolve becomes visible after reveal. Hidden values must not appear in option tooltips, event details, suspect rows, scripted GUI values, or logs before their visibility point.

### Member-country state

Flags:

- role: `secret_alliance_active_member`, `secret_alliance_founder`, `secret_alliance_major_at_entry`, `secret_alliance_prospective_leader`.
- reveal state, mutually exclusive: `secret_alliance_member_committed`, `secret_alliance_member_delayed`, `secret_alliance_member_compromised`, `secret_alliance_turned_member`, `secret_alliance_member_withdrawn`.
- investigation: `secret_alliance_suspect`, `secret_alliance_confirmed_by_target`, `secret_alliance_publicly_named`, `secret_alliance_suspect_cleared`.
- state changes: `secret_alliance_member_removed`, `secret_alliance_turned_channel_preserved`, `secret_alliance_false_plan_source`, `secret_alliance_event_fracture_exit`.
- reveal snapshot: `secret_alliance_reveal_member_snapshot`, `secret_alliance_reveal_major_snapshot`, `secret_alliance_reveal_founder_snapshot`.

Variables:

- `secret_alliance_motive`, `secret_alliance_commitment`, `secret_alliance_recruitment_order`.
- `secret_alliance_suspect_confidence`.
- `secret_alliance_false_plan_quality`, `secret_alliance_opening_weakness`, `secret_alliance_war_exit_value`.

## Constants and MTTH contract

Keep the provisional categories that already match the spec:

- `secret_alliance_event`, `secret_alliance_motive`, `secret_alliance_doctrine`, `secret_alliance_reveal_route`.
- `secret_alliance_scenario_type`, `secret_alliance_scenario_scale`.
- `secret_alliance_starting_values`, `secret_alliance_band`, `secret_alliance_founder_weight`.
- `secret_alliance_member_change`, `secret_alliance_operation`, `secret_alliance_operation_value`.
- `secret_alliance_decision_cost`, `secret_alliance_mission`, `secret_alliance_outcome_chance`.
- `secret_alliance_reveal_conversion`, `secret_alliance_ai`, `secret_alliance_super_event`, `secret_alliance_achievement`.

Add missing enum/tuning categories before call sites stabilize:

- `secret_alliance_phase`.
- `secret_alliance_operation_family`: diplomatic isolation `1`, intelligence penetration `2`, industrial/transport sabotage `3`, political/social pressure `4`, military preparation `5`, recruitment `6`.
- `secret_alliance_evidence_class`: method `1`, communications `2`, financial `3`, diplomatic `4`, military `5`, human `6`.
- `secret_alliance_evidence_quality`: weak `1`, useful `2`, strong `3`, direct `4`.
- `secret_alliance_member_state`: committed `1`, delayed `2`, compromised `3`, turned `4`, withdrawn `5`.
- `secret_alliance_timing`: minimum/maximum pulse delay, recovery windows, Evolution III accelerated delay, public countdown, postwar check interval, and human invitation timeout.
- `secret_alliance_postwar`: outcome enums and settlement thresholds.
- `secret_alliance_scenario_registry`: ID and sort values local to Event 011 where the shared registry does not own them.

`secret_alliance_operation.pulse_days` must not be the sole fixed cadence. Use it, if retained, only as the base for `mtth:secret_alliance_operation_interval_days`.

Create these MTTH entries in `common/mtth/011_secret_alliance_mtth.txt`:

- `secret_alliance_operation_interval_days`.
- `secret_alliance_recruitment_weight`.
- `secret_alliance_dispute_weight`.
- `secret_alliance_leak_weight`.
- `secret_alliance_defection_weight`.
- `secret_alliance_doctrine_change_weight`.
- `secret_alliance_evolution_iii_accelerated_days`.
- `secret_alliance_ai_investigation_weight`, `secret_alliance_ai_protection_weight`, `secret_alliance_ai_diplomacy_weight`, `secret_alliance_ai_deception_weight`, `secret_alliance_ai_border_weight`, `secret_alliance_ai_emergency_weight`, `secret_alliance_ai_war_fracture_weight`.

The operation interval shortens with chaos, evolution, active-member count, sponsor presence, readiness, doctrine pressure, and recent target aggression. It lengthens with Preparedness, Alertness, low Cohesion, recent same-family use, sponsor distraction, and a successful target deception. Clamp the result to timing constants before passing it to `country_event = { days = secret_alliance_next_pulse_days }`.

AI decision blocks should use the repo's MTTH pattern:

```txt
ai_will_do = {
	factor = 0
	modifier = {
		set_temp_variable = { secret_alliance_ai_weight = mtth:secret_alliance_ai_investigation_weight }
		add = secret_alliance_ai_weight
	}
}
```

## Exact founder-selection contract

### Base collections

`common/collections/011_secret_alliance_collections.txt` should define only stable base filters:

- `secret_alliance_normal_ai_countries`: `game:all_countries`, exists, AI, normal civilian systems, not a special Chaos country, not capitulated, not in a civil war.
- `secret_alliance_normal_human_countries`: the same base rules with `is_ai = no` for consent routing.

Target/faction/war/member rules stay in caller-side anonymous collections because they depend on ROOT or `event_target:secret_alliance_target`.

### Eligibility triggers

Keep and complete these names in `common/scripted_triggers/011_secret_alliance_triggers.txt`:

- `secret_alliance_target_is_valid`.
- `secret_alliance_is_valid_founder_for_root`.
- `secret_alliance_has_founder_pool_for_root`.
- `secret_alliance_automatic_event_is_available`.
- `secret_alliance_is_safe_factioned_candidate`.

Founder rules:

- exists, AI, minor, independent, normal civilian system, not special Chaos, not capitulated, not in civil war;
- not the target, its subject, its overlord, its guarantee partner, faction partner, or current war enemy;
- no prior active-member flag;
- factionless, or a nonleader member of a non-target-aligned faction which can safely leave;
- if already in a faction, require no current war and apply the strong faction penalty rather than equal treatment.

The provisional trigger currently admits any nonleader faction member even while at war and omits `has_civil_war = no`. Correct both before using it.

`secret_alliance_has_founder_pool_for_root` should use an anonymous collection and `collection_size`, not a recurring `any_country` scan. The official documentation's `value > N` comparison is inclusive; comment that Event 011 intentionally uses it as “at least N.”

### Ticket weighting helpers

Use these exact effects:

- `secret_alliance_prepare_founder_selection_weight`.
- `secret_alliance_add_current_country_to_founder_ticket_pool`.
- `secret_alliance_select_weighted_founder_candidate`.
- `secret_alliance_select_exactly_three_founders`.
- `secret_alliance_rollback_failed_initialization`.

`secret_alliance_prepare_founder_selection_weight` starts with `constant:secret_alliance_founder_weight.base`, adds narrative weights for claims/cores, border or strategic reach, same continent, hostile ideology, target-created tension/threat, grievance, fear, and sponsor alignment, then multiplies by `existing_faction_penalty` for safe nonleader faction members. Round and clamp to `minimum_ticket`/`maximum_ticket`.

`secret_alliance_add_current_country_to_founder_ticket_pool` mirrors Fury: copy the integer weight into a temp remainder, add THIS to `secret_alliance_founder_ticket_pool` inside `while_loop_effect`, then clear its temp values.

`secret_alliance_select_exactly_three_founders` does not build one pool and draw three times. It runs the selection helper three times. Each successful draw immediately calls `secret_alliance_register_current_member` and sets `secret_alliance_active_member`, so the next anonymous collection excludes that country before rebuilding the ticket pool. This guarantees unique founders even though the ticket array itself contains duplicates.

After the third draw, require both `global.secret_alliance_founders^num` and the founder flag count to equal `constant:secret_alliance_event.normal_founders`. If not, call rollback before any visible event, history row, or fire-once completion. There is no replacement with invalid countries and no reduced-size opening.

### Context initialization order

`secret_alliance_prepare_random_event_fire`, in target ROOT scope:

1. Set `secret_alliance_prefire_ready = 0` as a temp variable.
2. Recheck `secret_alliance_automatic_event_is_available`.
3. Call `secret_alliance_initialize_runtime_context` to clear stale runtime state, increment run sequence, save the global target, save the starting capital state, and set normal origin.
4. Call `secret_alliance_select_exactly_three_founders`.
5. Assign motive, commitment, leader score, and doctrine.
6. Sync enabled pre-fire evolutions.
7. Apply the pre-fire package described below.
8. Seed starting values and schedule the first target-owned pulse.
9. Save the target as the Event Logs actor; hidden founders must not be exposed through the log.
10. Set `secret_alliance_prefire_ready = 1` only after every invariant passes.

The root event `chaosx.nr11.1` consumes the prepared context. It must not select founders again.

## Safe member registry

### Registration

`secret_alliance_register_current_member` is country-scoped and takes temp call inputs for founder/recruit/sponsor role. It must:

1. Re-run the appropriate validity trigger.
2. Check `NOT = { has_country_flag = secret_alliance_active_member }`.
3. Set the member flag before adding to the array.
4. Add THIS exactly once to `global.secret_alliance_members` and, when relevant, `global.secret_alliance_founders`.
5. Set major status at entry, motive, commitment, recruitment order, and reveal state.
6. Recompute counts and cohesion/readiness deltas through central value helpers.

### Refresh without mutating during iteration

Use these effects:

- `secret_alliance_refresh_member_registry`.
- `secret_alliance_mark_current_member_for_removal`.
- `secret_alliance_remove_current_member_runtime`.
- `secret_alliance_rebuild_member_registry_from_survivors`.
- `secret_alliance_recount_members`.
- `secret_alliance_reselect_leader`.

Never remove from `global.secret_alliance_members` while looping over it. Instead:

1. Clear temp arrays `secret_alliance_member_survivors` and `secret_alliance_member_removals`.
2. Iterate the live array with `for_each_scope_loop`.
3. Put valid scopes into survivors and invalid scopes into removals.
4. Iterate removals and apply member-local cleanup/loyalty outcomes.
5. Clear the live array.
6. Iterate survivors and re-add each flagged scope once.
7. Recount and reselect the leader if required.

A hidden member becomes invalid if it ceases to exist, capitulates, enters civil war, loses independence, becomes the target/target subject, joins the target faction, becomes leader of an incompatible faction, becomes a special/noncivilian Chaos country, or reaches an explicit withdrawn state. A mere unrelated faction membership does not silently invalidate it if the original safe-withdrawal contract still holds.

### Leader selection

Create `secret_alliance_reveal_leader_scorer` in the Event 011 country scorer file with `target_array = global.secret_alliance_members`. Score only valid reveal members; strongly prefer the valid sponsor, then a major, then an original founder, then strength/reach/commitment, while penalising compromised or unsafe faction state. `secret_alliance_reselect_leader` gets the sorted list, saves the first valid scope as global `secret_alliance_leader`, and clears the temporary scorer arrays. If no leader remains, collapse the hidden pact or end the reveal attempt; do not substitute the target or a static tag.

## Motives and doctrine

Use the existing numeric motive enum:

- fear, grievance, ideology, patronage, opportunism, regime survival.

`secret_alliance_assign_current_member_motive` builds a weighted motive ticket pool from facts. A bordering weak country threatened by the target weights fear; claims/cores and territorial loss weight grievance; government hostility weights ideology; a sponsor relationship weights patronage; target wealth/weakness weights opportunism; coup/civil-instability pressure weights regime survival. Every member gets exactly one primary motive.

Use these helpers:

- `secret_alliance_assign_current_member_motive`.
- `secret_alliance_select_initial_doctrine`.
- `secret_alliance_evaluate_doctrine_change`.
- `secret_alliance_calculate_motive_compatibility`.
- `secret_alliance_calculate_member_defection_pressure`.

Doctrine is one global enum: containment, punitive, regime pressure, or spoils. It weights operations, reveal pressure, war aims, and postwar outcomes. It may change only through sponsor entry, a serious failure, or a member dispute. A doctrine change applies a cooldown and produces a visible change in incident pattern without exposing the pact.

## Central values and evidence model

### Delta helpers

All value changes go through:

- `secret_alliance_change_cohesion`.
- `secret_alliance_change_readiness`.
- `secret_alliance_change_alertness`.
- `secret_alliance_change_evidence`.
- `secret_alliance_change_preparedness`.
- `secret_alliance_change_war_pressure`.
- `secret_alliance_change_resolve`.

Each reads one signed temp input named `secret_alliance_value_delta`, writes the correct scoped variable, and clamps to `constant:secret_alliance_band.value_min`/`value_max`. If a variable must be subtracted, copy it to a temp variable and multiply that temp by `-1`; do not use unary minus on a variable token.

### Evidence classes and anti-farming

Target flags:

- `secret_alliance_evidence_class_method`.
- `secret_alliance_evidence_class_communications`.
- `secret_alliance_evidence_class_financial`.
- `secret_alliance_evidence_class_diplomatic`.
- `secret_alliance_evidence_class_military`.
- `secret_alliance_evidence_class_human`.

Member/suspect clue flags should be class-and-source specific, for example `secret_alliance_clue_communications_courier` and `secret_alliance_clue_military_depot`. `secret_alliance_register_evidence` takes `secret_alliance_call_evidence_class`, `secret_alliance_call_evidence_quality`, and optional regular `secret_alliance_evidence_actor`.

It awards:

- the quality base;
- a first-class bonus when the target has not seen that class;
- a corroboration bonus when the clue links a second or later independent class to the same suspect;
- only a reduced repeat amount for a different clue in an already-known class;
- zero for the exact same clue/source pair.

It also calls `secret_alliance_change_suspect_confidence` for the actor or a deliberately generated innocent suspect. Evidence never equals membership knowledge by itself. Confirmation requires direct material, a trusted turned source, or a successful high-tier mission.

`secret_alliance_rebuild_visible_suspects` orders the live suspect array by confidence and keeps a compact display list. Human targeted decisions read `global.secret_alliance_visible_suspects`; AI reads the full suspect array directly and does not click the human selector.

### Preparedness as maintained components

`secret_alliance_recalculate_preparedness` derives the public total from the seven maintained components, with component caps and a total cap. Protection decisions activate timed ideas/projects and set expiry missions. On expiry, `secret_alliance_expire_preparedness_project` reduces or clears the component. No click creates permanent cumulative Preparedness without continuing cost.

## Operation scheduler and branch helpers

Use target-owned delayed events, not a global on-action loop.

Exact effects:

- `secret_alliance_schedule_next_operation_pulse`.
- `secret_alliance_run_operation_pulse`.
- `secret_alliance_select_operation_actor`.
- `secret_alliance_select_operation_family`.
- `secret_alliance_start_selected_operation`.
- `secret_alliance_finish_operation_full_success`.
- `secret_alliance_finish_operation_partial_success`.
- `secret_alliance_finish_operation_failure`.
- `secret_alliance_try_recruit_member`.
- `secret_alliance_resolve_recruitment_response`.
- `secret_alliance_try_member_dispute`.
- `secret_alliance_try_member_leak`.
- `secret_alliance_try_member_defection`.

Operation family effects:

- `secret_alliance_run_diplomatic_isolation_operation`.
- `secret_alliance_run_intelligence_penetration_operation`.
- `secret_alliance_run_industrial_transport_operation`.
- `secret_alliance_run_political_social_operation`.
- `secret_alliance_run_military_preparation_operation`.
- `secret_alliance_run_recruitment_operation`.

Pulse sequence:

1. Confirm fixed target and concealed state.
2. Refresh registry and values.
3. Run collapse/reveal checks.
4. Try enabled active-event evolutions.
5. If a substantial operation is already active, permit only a bounded flavor incident and reschedule.
6. Select one valid actor from the member array.
7. Select one family from MTTH/weighted doctrine/motive/recent-use factors.
8. Mark the substantial operation active and launch its event/mission.
9. Resolve into one of full/partial/failure, clear active state, apply recovery flags, and schedule the next pulse.

Only one substantial operation is active by default. Severe operations apply a longer recovery. Same-family recent-use flags penalise repetition. Permanent building damage is Evolution II+, rare, scaled to target size, and bounded. Political killings are rare, office-gated, and cannot repeat without a major state change.

Recruitment uses the same weighted candidate engine as founders but the evolution-specific validity trigger and cap. AI candidates resolve accept/refuse/leak/manipulate from motive and current values. Human candidates always receive `chaosx.nr11.150` with explicit join, refuse, leak, and expose choices; the pact waits for the answer and never treats timeout or silence as acceptance.

Disputes, leaks, and defections are distinct branches:

- dispute changes Cohesion/doctrine/operation timing and may expose a participant;
- leak creates Evidence and suspect confidence without automatically confirming the full roster;
- defection changes membership or creates a turned channel only after motive-specific terms;
- withdrawal removes the member before the reveal snapshot;
- turned membership remains active until its concrete false-plan/leak/refusal consequence occurs.

## Decision and mission architecture

### Categories and lifecycle

- `secret_alliance_foreign_interference_category`: visible from Evolution II through hidden crisis.
- `secret_alliance_coalition_crisis_category`: visible in Evolution III/prewar public crisis.
- `secret_alliance_revealed_war_category`: visible while the target is in the coalition war.
- `secret_alliance_aftermath_category`: visible only while settlement choices remain.

Baseline has no dedicated category. Category cleanup follows the `allowed`/`visible`/`available` lifecycle from the decision skill and removes activated missions explicitly at reveal, collapse, or settlement.

### Selected-suspect contract

Use:

- selector `secret_alliance_select_suspect` with `target_array = global.secret_alliance_visible_suspects`;
- `secret_alliance_set_selected_suspect`;
- `secret_alliance_clear_selected_suspect`;
- triggers `secret_alliance_has_selected_suspect`, `secret_alliance_selected_suspect_is_possible`, `_plausible`, `_likely`, `_confirmed`, and `_true_member`.

The setter clears the old country's `secret_alliance_selected_suspect` flag and the old global target, sets the new country flag, and saves global `secret_alliance_selected_suspect`. The global target is justified because selection must persist across independent decision chains and only one Event 011 context exists. It is explicitly cleared by cleanup. AI never uses the selector.

### Dynamic costs

Use:

- `secret_alliance_refresh_action_costs`.
- `secret_alliance_can_pay_investigation_cost`, `_protection_cost`, `_diplomacy_cost`, `_offensive_cost`, `_border_cost`, `_emergency_cost`, `_war_cost`.
- `secret_alliance_pay_investigation_cost`, `_protection_cost`, `_diplomacy_cost`, `_offensive_cost`, `_border_cost`, `_emergency_cost`, `_war_cost`.
- `secret_alliance_apply_action_repeat_scaling`.

The refresh effect stores normal target-country variables for PP, CP, XP, stability/war-support strain, equipment, trains, trucks, convoys, fuel, and manpower. It runs when categories open, target scale changes materially, and after a paid action. Triggers read those stored variables; payment effects copy each cost, multiply the temp copy by `-1`, and apply the resource effect. Player tooltips show the same stored values.

The provisional trigger file currently embeds literal resource thresholds in `secret_alliance_can_start_*`. Replace them with these cost triggers; literals violate the central tuning contract and can disagree with the paid amounts.

### Mission helpers and identifiers

Exact missions:

- `secret_alliance_watch_liaison_route`.
- `secret_alliance_seize_compromised_courier`.
- `secret_alliance_turn_recruited_clerk`.
- `secret_alliance_protect_defecting_envoy`.
- `secret_alliance_break_safehouse_network`.
- `secret_alliance_national_manhunt`.
- `secret_alliance_control_rumor_channel`.

Shared helpers:

- `secret_alliance_activate_mission_family`.
- `secret_alliance_increment_active_mission_count`.
- `secret_alliance_decrement_active_mission_count`.
- `secret_alliance_resolve_mission_full_success`.
- `secret_alliance_resolve_mission_partial_success`.
- `secret_alliance_resolve_mission_failure`.
- `secret_alliance_cancel_hidden_missions`.
- `secret_alliance_cancel_all_missions`.

The activation helper uses `activate_mission`/`activate_targeted_decision` only after cap and target checks. Every complete, timeout, cancel, invalid-target, reveal, collapse, and cleanup path decrements the matching active count exactly once. Use a mission-local active flag to make decrement idempotent.

### Maintained projects and border state

Protection projects are explicit: staff compartmentalisation, cipher rotation, industrial choke points, dispersed stockpiles, cabinet guard, border communications, ports/airfields, and continuity sites. Region-targeted projects save the chosen state only for their effect chain or mark the state with an Event 011 state flag plus target owner reference. Do not store one global state target for multiple simultaneous projects.

Border actions require a neighboring plausible/likely suspect. Border conflicts do not set normal hostile-war state and therefore do not call the war reveal transaction. The escalation decision that creates a normal war does.

## Evolution architecture

Exact helpers:

- `secret_alliance_sync_prefire_evolution_unlocks`.
- `secret_alliance_try_apply_evolution_i`, `_ii`, `_iii`.
- `secret_alliance_apply_evolution_i`, `_ii`, `_iii`.
- `secret_alliance_record_evolution_i`, `_ii`, `_iii`.
- `secret_alliance_schedule_accelerated_evolution_iii`.

Every `try_apply` limit must contain all of the following together:

- context is active and concealed;
- its applied flag is absent;
- required earlier evolution is applied;
- meaningful event-owned pacing gate passes;
- temp `event_id`, `event_type`, and `evolution_tier` are set;
- `is_current_evolution_enabled = yes`.

Only inside that same successful branch may the applied flag be set and the evolution log recorded. A disabled evolution never sets a hidden applied flag or creates a log entry.

### Evolution I

Active event: raises the minor cap, broadens operation/recruitment pools, and schedules stronger minor recruitment.

Pre-fire: retain exactly three minor founders and set an accelerated first-recruitment flag. Do not turn the recruited fourth member into a founder.

### Evolution II

Active event: attempt one eligible major sponsor, unlock serious operations, open Evidence/Preparedness and the response category, and seed suspects through a serious incident.

Pre-fire: retain exactly three minor founders, then add one eligible major as sponsor/member after the founder transaction. The sponsor may become prospective leader but is not a founder. Start one developed network and open the response category after a short discovery event, not silently on day one.

### Evolution III

Active event: evaluate a second major, expose War Pressure, choose public-faction/countdown or fracture pressure, and unlock preemption/ultimatum/emergency actions.

Pre-fire: initialise the Evolution II package, then schedule `mtth:secret_alliance_evolution_iii_accelerated_days`. Do not create the faction or war in the root event. The delay must permit at least one investigation/preparation response.

Evolution log actor is always the fixed target, not a hidden member. Use Event 011 fire-once type, event ID 11, and constants for stage/tier/type. This prevents the Event Logs UI from leaking a founder before reveal.

## Reveal transaction and immediate normal-war convergence

### On-action file

`common/on_actions/011_secret_alliance_on_actions.txt` should register:

- `on_war_relation_added`: always call the cheap `secret_alliance_handle_war_relation_added` gate.
- `on_annex`: call the handler only when ROOT/FROM is the target or has a member/snapshot flag.
- `on_capitulation`: same narrow gate.
- faction join/leave hooks: only flagged members/target.
- `on_peaceconference_ended`: accelerate postwar evaluation for relevant participants.

No daily/weekly/monthly world iteration.

### War-pair trigger

`secret_alliance_is_target_member_war_pair` is evaluated in on-action context and accepts either:

- ROOT active member and FROM fixed target; or
- FROM active member and ROOT fixed target.

It also requires concealed active context and no reveal guard. Save the member side as regular `secret_alliance_war_anchor`. A border conflict does not produce `on_war_relation_added`, so it does not pass this route.

### Shared transaction

Every route calls `secret_alliance_reveal_pact`. Required temp input: `secret_alliance_call_reveal_route`. Optional regular input: `secret_alliance_war_anchor` when a target war already exists.

Exact order:

1. Return immediately if already revealed or `secret_alliance_reveal_in_progress` is set.
2. Set the guard and store reveal route.
3. Refresh the member registry.
4. Resolve turned/withdrawn/invalid members.
5. Require at least the tuned minimum active membership; otherwise call hidden collapse.
6. Reselect a valid leader.
7. Call `secret_alliance_snapshot_reveal_achievements` before faction mutation.
8. Call `secret_alliance_prepare_member_reveal_states`.
9. Move safely withdrawable members out of incompatible factions.
10. Leader calls `create_faction_from_template` with `faction_template_secret_alliance_anti_target_pact` and the dynamic name key.
11. Add every remaining valid member to the leader's faction.
12. Call `secret_alliance_convert_hidden_values_to_war_state`.
13. Set revealed/public flags and close hidden-only operations/missions.
14. Fire the reveal super-event exactly once, respecting shared settings.
15. If `secret_alliance_war_anchor` exists, call `secret_alliance_join_all_members_to_existing_target_war` immediately.
16. If no war exists, start the public offensive countdown unless this route explicitly starts war in the same effect.
17. Apply dynamic AI strategies and schedule the narrow public-war status event.
18. Clear the guard.

### Immediate join contract

In a hostile-war reveal, every remaining active member joins immediately. A member's prewar `delayed` state is converted into an opening coordination/mobilisation penalty; it is not allowed to remain outside the war. `compromised` and `turned` states likewise produce concrete weaknesses after joining. A `withdrawn` country is removed before the snapshot and does not join.

`secret_alliance_join_current_member_to_existing_target_war`, in member scope, uses:

```txt
add_to_war = {
	targeted_alliance = event_target:secret_alliance_war_anchor
	enemy = event_target:secret_alliance_target
	hostility_reason = asked_to_join
}
```

The reveal guard remains set throughout the loop because each join can fire `on_war_relation_added` again. After each call, verify `has_war_with = event_target:secret_alliance_target`; a failure is an implementation error to expose in validation, not permission to create a separate fallback war.

For a pact-controlled/scenario war, create the faction, have the selected leader declare the one target war, save that leader as `secret_alliance_war_anchor`, then use the same add-to-war helper for all others while the guard is set.

## Dynamic faction identity

Template ID: `faction_template_secret_alliance_anti_target_pact`.

Name key: `secret_alliance_anti_target_pact_name`.

Primary localisation: `Anti-[secret_alliance_target.GetAdjective] Pact`.

Fallback key: `secret_alliance_anti_target_pact_name_fallback`, using `[secret_alliance_target.GetName]`.

Scripted localisation helper: `GetSecretAllianceFactionTargetDescriptor`.

The engine exposes adjective/name localisation but no documented trigger for “this adjective resolves to an empty string.” Therefore the fallback must be deterministic, not an invisible text test. Add `secret_alliance_target_requires_name_fallback` for any allowed generated/cosmetic target class known not to own a safe adjective and set `secret_alliance_faction_use_name_fallback` during context initialisation. The current target gate excludes special Chaos countries, so normal accepted targets should use the adjective path. If target eligibility is broadened, update this trigger in the same change. A static generic faction title is not an approved substitute.

## Reveal value conversion

Use `secret_alliance_convert_hidden_values_to_war_state` and subordinate helpers:

- `secret_alliance_calculate_coalition_resolve`.
- `secret_alliance_calculate_opening_coordination`.
- `secret_alliance_calculate_target_opening_defense`.
- `secret_alliance_apply_member_opening_state`.
- `secret_alliance_apply_target_opening_state`.

Central formulas use constants and capped components:

- Resolve starts from Cohesion times `resolve_cohesion_factor`, then adds public commitment and healthy sponsor contribution and subtracts fracture, turned-source, incompatible-motive, and leadership-dispute penalties.
- Opening coordination starts from Readiness times `opening_readiness_factor`, adds sponsor/known-access components, applies diminishing returns for duplicate readiness layers, and subtracts a member-count coordination burden plus false-plan/turned penalties.
- Target exposed-weakness knowledge derives from Evidence times `weakness_evidence_factor` plus a preserved false-plan bonus.
- Target opening defense derives from Preparedness times `defense_preparedness_factor` plus continuity/known-plan components.

Convert the results into bounded dynamic modifiers or distinct band packages with meaningful identity: planning/logistics/access for the coalition, mobilisation/logistics/intelligence for the target, and member-specific penalties for delayed/compromised/turned states. Do not implement the whole conversion as one generic attack/defence modifier.

A preserved turned channel must cause one actual wartime consequence: accepted false deployment, exposed depot, delayed mobilisation penalty, or public refusal/defection after entry. Merely setting a turned flag cannot qualify the achievement.

## AI architecture

### Dynamic target strategies

Static `common/ai_strategy` blocks cannot safely hardcode an arbitrary player tag. Apply target-specific strategy entries in effects while both scopes are available, using scope inversion and `id = PREV`, mirroring vanilla dynamic `add_ai_strategy` usage.

Helpers:

- `secret_alliance_apply_hidden_member_ai`.
- `secret_alliance_apply_revealed_member_ai`.
- `secret_alliance_apply_target_defense_ai`.
- `secret_alliance_remove_member_ai`.
- `secret_alliance_remove_target_ai`.

Hidden members get modest antagonize/prepare-for-war values and operation-specific priorities, never an overt maximum posture. Revealed members get strong antagonize/conquer/front values scaled by intensity, motive, reach, sponsor role, and opening state. The target gets defensive preparation appropriate to known threats. Remove every dynamic entry during member removal and cleanup.

`common/ai_strategy/011_secret_alliance.txt` should contain only generic flag-driven behavior which does not need a dynamic country ID: front execution posture, naval invasion/air/naval role ratios, convoy/logistics priority, and cautious/aggressive scenario bands.

### Decision AI

- Human selection decisions have `ai_will_do = { factor = 0 }`.
- AI selects directly from the full suspect array using confidence, evidence, cost, doctrine, and strategic access.
- AI calls the same cost/payment/result effects as the player.
- Investigation prioritises useful independent evidence classes, not the same repeatable clue.
- Protection prioritises the weakest relevant Preparedness component.
- Diplomacy matches known or estimated motive.
- Offensive action requires sufficient confidence and accepts false-accusation risk only at extreme crisis pressure.
- War fracture targets low-commitment/opportunist/grievance members first.
- Scenario AI risk tolerance scales low/medium/high/maximum but never bypasses validity or human consent.

## Triggerable scenario: Coalition Unmasked

### Shared registry additions

Use stable scenario ID `constant:triggerable_scenario_id.coalition_unmasked = 9` unless another scenario takes ID 9 before merge. Add its name sort value and shift only sort values that must remain unique.

Add `triggerable_scenarios_secret_alliance_type`, defaulting to `constant:secret_alliance_scenario_type.regional_ring`, to `initialize_triggerable_scenarios_settings`.

Extend all data-driven surfaces:

- `triggerable_scenarios_initialize_registry` ID and name-sort arrays.
- rebuild/sort/view detail mappings.
- select/cycle type controls and scripted localisation.
- `triggerable_scenario_can_launch_selected`.
- `trigger_selected_chaosx_scenario` with `trigger_secret_alliance_coalition_unmasked_scenario`.
- scenario event/confirmation text and `docs/systems/triggerable_scenarios.md`.

Confirmation reads selected type and intensity at launch time. Before any selection, snapshot them on the target as `secret_alliance_scenario_type_snapshot` and `secret_alliance_scenario_intensity_snapshot`. Also set immutable `secret_alliance_scenario_maximum_snapshot` when applicable. Later GUI changes cannot change the run or achievement eligibility.

### Type algorithms

- Regional ring: strongest weights for neighbors, same region/continent, access routes, and plausible land/naval/air reach; containment/punitive doctrine.
- Ideological front: weights governments hostile to the target's ruling ideology and compatible with the selected leader; regime-pressure doctrine.
- Great-power sponsor: select one eligible AI major first, then minors with sponsor reach/patronage; high/maximum can evaluate a second major within cap.
- Unlikely coalition: deliberately diversify ideology and motive while keeping strategic reach; start with lower Cohesion and greater fracture reserve.
- Random coalition: safe weighted selection across all valid candidates; randomise doctrine after composition.

### Intensity composition

- Low: exactly 3 minors.
- Medium: 4-6 total; a major is optional and uncommon.
- High: 1 major plus 5-7 other members when valid.
- Maximum: up to 2 majors and 8-12 total; if fewer than the requested upper band exist, use every safe candidate up to the cap and report the achieved composition.

`secret_alliance_prepare_scenario_composition` computes requested total/minor/major counts from type and intensity before the launch gate. `secret_alliance_scenario_can_launch` validates the type-specific minimum, not merely “three founders exist.” If a required major or minimum safe total is absent, disable launch with a clear reason. Never substitute an invalid or involuntary human country.

The scenario bypasses normal chaos, evolution, date, prior Event 011 history, and fire-once gates. It blocks only active context, world-end/terminal conflict, impossible pool, and unresolved human consent. The provisional scenario trigger currently blocks `secret_alliance_terminal`; remove that historical gate. A completed earlier normal run may not block the explicit scenario.

### Scenario launch transaction

1. Reset run-scoped Event 011 tracking while preserving already-earned achievement completion flags.
2. Initialise the fixed target with scenario origin.
3. Snapshot type/intensity.
4. Select the exact safe composition and collect human consent.
5. Abort before faction/war if the composition cannot be completed.
6. Set scenario starting values and equipment/logistics packages by actual composition and intensity.
7. Call the same registry, leader, faction, conversion, super-event, AI, and snapshot helpers as normal reveal.
8. Leader declares one normal target war; all other active members join that same war immediately.
9. Record the scenario identity separately. Do not write a normal automatic Event 011 history row or consume its fire-once path.

## Multiplayer consent

Normal automatic founders and automatic AI recruitment use `is_ai = yes`, guaranteeing the initial three without pausing another player or silently converting them.

Any later human candidate receives an explicit invitation event with four meaningful outcomes: join, refuse, leak, expose. The candidate is not added to any active/member/founder array until the join option executes. Refusal is final for that invitation; no timeout acceptance.

Scenario composition which includes humans uses a pending-consent array and does not create the faction or war until all invited humans accept. If any refuses, the launch is cancelled and the launcher receives the precise failure reason. Replacing the refusing human with an AI country would be an unapproved fallback and is not permitted.

Set `secret_alliance_human_consent_bypassed` only for explicit debug/forced tooling, and make it disqualify `011_secret_alliance_surrounded_not_buried`. A second human launcher cannot begin another scenario while `secret_alliance_active` is set.

## Achievements and immutable snapshots

Register all six IDs in the shared root achievement set:

- `011_secret_alliance_the_empty_chair`.
- `011_secret_alliance_every_thread`.
- `011_secret_alliance_their_man_in_the_room`.
- `011_secret_alliance_divide_the_table`.
- `011_secret_alliance_surrounded_not_buried`.
- `011_secret_alliance_two_giants_one_grave`.

### Reveal snapshot helper

`secret_alliance_snapshot_reveal_achievements` runs after member refresh and before faction mutation. It:

1. Clears prior run's transient snapshot flags.
2. Sets member/founder/major snapshot flags on every current valid member.
3. Stores reveal member and major counts on the target.
4. Stores whether every active member was confirmed and whether any false-confirmed/publicly named innocent exists.
5. Stores whether a turned channel and false plan are preserved.
6. Calculates `secret_alliance_fracture_exit_requirement` as half the reveal membership rounded up, using constants.
7. Sets `secret_alliance_public_reveal_occurred`.

### Required trackers

- Empty Chair: normal origin, no public reveal, at least one true founder confirmed, no innocent attacked/publicly named, and `secret_alliance_hidden_pact_collapsed`.
- Every Thread: `secret_alliance_all_reveal_members_confirmed`, maximum Evidence band at reveal, and no false-confirmed/publicly named innocent.
- Their Man in the Room: founder or reveal-major turned, channel preserved, false plan accepted, and `secret_alliance_false_plan_wartime_consequence` set by an actual effect.
- Divide the Table: increment `secret_alliance_event_fracture_exit_count` only for Event 011 separate terms/defection/refusal; never count capitulation/annexation. Qualify when it reaches the rounded-up requirement and the target has not lost.
- Surrounded, Not Buried: immutable Maximum scenario flag, no consent bypass, target independent, target controls the stored starting capital at outcome, survives the opening war, and coalition dissolves/settles.
- Two Giants, One Grave: two majors at reveal snapshot, target retains starting capital at final outcome, coalition defeated, and Resolve collapsed. Later changes to major status do not affect qualification.

At final outcome, convert the starting-capital state check into durable `secret_alliance_target_kept_starting_capital`, then clear its global event target during cleanup.

Keep run trackers separate from durable `achievement_011_*_completed` flags so a later manual scenario reset cannot make an already-earned achievement appear incomplete.

## Postwar architecture

Use target-owned `chaosx.nr11.190` as a low-frequency public-war status event. `secret_alliance_schedule_public_war_check` reschedules only while the fixed target has a snapshot member enemy. Narrow annex/capitulation/peace on-actions may call `secret_alliance_evaluate_postwar` early.

Exact effects:

- `secret_alliance_update_war_pressure_and_resolve`.
- `secret_alliance_try_event_fracture_exit`.
- `secret_alliance_evaluate_postwar`.
- `secret_alliance_apply_coalition_victory_outcome`.
- `secret_alliance_apply_target_victory_outcome`.
- `secret_alliance_apply_negotiated_settlement_outcome`.
- `secret_alliance_apply_sponsor_collapse_outcome`.
- `secret_alliance_apply_internal_rupture_outcome`.
- `secret_alliance_finalize_outcome`.

Outcome order is deterministic: target absorbed/coerced and doctrine goals met; target victory with low/collapsed Resolve; explicit negotiated settlement; sponsor collapse; internal rupture. Member motive, doctrine, war burden, revealed evidence, separate terms, and sponsor state decide individual settlement results.

The public faction may survive only when the chosen postwar outcome explicitly makes it a continuing regional/security bloc. Otherwise `secret_alliance_finalize_outcome` dismantles only the Event 011-owned faction after confirming `secret_alliance_public_faction_created` and the saved leader still leads that faction. It must not dismantle an unrelated successor faction.

## Idempotent cleanup

Use two layers.

### `secret_alliance_cleanup_runtime_context`

Guard with `secret_alliance_cleanup_in_progress`. If no active/runtime state exists, return safely.

Order:

1. Set guard and cancel scheduled/activated Event 011 missions and countdown flags.
2. Clear selected suspect.
3. Iterate member, founder, suspect, confirmed, and turned arrays before clearing them; call member/suspect local cleanup and remove Event 011 AI strategies/ideas.
4. Clear all runtime arrays.
5. Remove target runtime ideas, dynamic modifiers, category flags, project flags, active mission counts, and stored cost variables.
6. Remove or preserve the Event 011 faction according to the recorded postwar outcome.
7. Clear all six global event targets.
8. Clear phase, values, counts, doctrine, operation, reveal, and scenario runtime variables/flags.
9. Clear guard last.

### `secret_alliance_archive_and_finish_run`

Before runtime cleanup, store the final outcome, achievement conclusions, history/evolution/super-event facts, scenario identity, and spreadsheet/log facts. Then set a target-local run-complete flag. Do not use one permanent global `secret_alliance_terminal` to block future manual scenarios. Normal automatic repeat prevention belongs to the existing fire-once event system.

Repeated calls from peace, annexation, event options, and scenario code must produce the same final state. Cleanup must never expose unconfirmed members merely because their runtime flags are being removed.

## Event-system and Event Logs integration

Required shared edits when implementation is ready:

1. Remove Event 011 from `initialize_default_disabled_events_for_rework_queue`.
2. Replace its permanent exclusion in `evaluate_random_event_active_pool_candidate` with `ROOT = { secret_alliance_automatic_event_is_available = yes }` when `event_id = 11`.
3. In `fire_event_by_temp_id_no_cluster`, replace the ID 11 hard block with `secret_alliance_prepare_random_event_fire`; set `event_single_fire_allowed = 0` unless `secret_alliance_prefire_ready > 0`.
4. Preserve dispatch order: pre-fire context, event, fire-once handler, history record.
5. Add Event Logs default actor for ID 11 as `secret_alliance_target`, not the hidden leader.
6. Show live weight only when automatic availability passes; otherwise write the existing `-1`/`N/A` state.
7. Replace unavailable event name/detail mappings, add the three evolution previews/details, and add reveal history content without leaking hidden values.
8. Scenario launch records its scenario identity separately and does not call the normal Event 011 fire-once/history path.

## Performance budget

- Automatic eligibility: one collection-size evaluation when Event 011 is considered.
- Initial selection: three bounded world-collection passes, each building a capped ticket pool; acceptable because the event is fire-once.
- Recruitment: one infrequent collection pass only when a recruitment branch is selected and no operation is active.
- Scenario: bounded passes at explicit player launch.
- Runtime pulse: target plus active arrays only.
- On-actions: a constant-time flag/target gate before any helper.
- Decision UI: compact visible suspect array; no `any_country` in continuously evaluated player decision availability.
- AI: full suspect/member arrays only, not a world scan.

The provisional trigger file uses `any_country` for turned-channel and active-major checks. Replace those with `for_each_scope_loop`/array-derived flags and maintained counts. Avoid continuously evaluated `any_country` gates in decision categories and AI strategy enable blocks.

## Spec conflicts and resolved interpretations

| Conflict | Resolution |
| --- | --- |
| User requires exactly three valid minor founders; Evolution I spec permits four founders | Always three founders; Evolution I accelerates a fourth member as a recruit |
| User requires three minor founders; Evolution II spec permits a major founder with 2-4 minors | Select three minor founders first; add the major as sponsor/member and allow it to become leader, but not founder |
| Evolution III pre-fire could be read as immediate public war | Start with Evolution II package and a shortened MTTH delay; never instant normal-chain war |
| “Delayed entry” appears in turned-member material, but hostile-war reveal requires every active member immediately | Delayed members join the existing war immediately and receive a concrete opening penalty; withdrawn members are removed before reveal |
| Strong factionless preference versus the old handoff's strict factionless rule | Permit only safe, nonleader faction members with a strong ticket penalty and safe-withdrawal validation |
| Dynamic adjective name with country-name fallback, but engine cannot test empty localisation | Explicit fallback trigger/flag for allowed target classes; no silent generic name |
| Scenario bypasses prior event history, but provisional trigger blocks a terminal Event 011 flag | Scenario gate ignores prior completion and blocks only an active context/impossible launch/terminal world conflict |
| Older architecture says no scenario | Superseded by the complete spec; implement Coalition Unmasked with five types/four intensities |

## Provisional concurrent-file audit

The emerging `011_secret_alliance_triggers.txt` contains several good names retained above, but must not be treated as finished. Identified architecture gaps:

- founder/recruit/sponsor gates need `has_civil_war = no`;
- safe in-faction admission needs a peace/safe-withdrawal test;
- exact founder count should come from constants/collection size, not literal `3`;
- active evolution gates need `is_current_evolution_enabled` in the same successful branch;
- resource/cost thresholds must use stored dynamic costs, not literals;
- `any_country` major/turned checks must use active arrays/counts;
- scenario availability must be type/intensity specific and must not block prior Event 011 history;
- selected-suspect global-target creation/cleanup must be explicit;
- current thresholds using `>` need review where the intended band is inclusive;
- member validity needs an explicit reveal-valid variant and safe faction/war conversion checks.

The provisional constants file covers most of the required tuning families but lacks operation/evidence/member-state enums, dynamic MTTH ownership, type-specific scenario minimums, and postwar/cleanup enums.

## Implementation sequence

1. Finalise constants, collections, MTTH entries, triggers, and scorer.
2. Implement context, exact founder selection, member registry, motives/doctrine, value helpers, and rollback.
3. Wire pre-fire dispatch and automatic Event 011 availability before writing visible root-event effects.
4. Implement target pulse, operations, recruitment, disputes, leaks, defections, and active evolutions.
5. Implement Evidence/Preparedness, suspect selection, decision costs, decisions/missions, and AI equivalents.
6. Implement guarded reveal, faction template/rules/goals, value conversion, normal-war convergence, and public AI.
7. Implement scenario registry/type/intensity/consent and reuse the reveal/war helpers.
8. Implement postwar, achievements/snapshots, and two-layer cleanup.
9. Complete localisation, assets, Event Logs/details/evolutions, super-event wiring, docs, and spreadsheet alignment.
10. Run decision/mission, localisation, event-completion, and scenario/achievement audits before completion claim.

## Validation scenarios

1. Exactly three eligible founders: all three are selected once; no reduced opening.
2. Four/many eligible founders: exactly three unique minors; ticket bias is visible statistically and factionless candidates dominate without excluding safe faction members.
3. Fewer than three: Event 011 is `N/A`, no popup/history/fire-once consumption, no global target or array remains.
4. Save/reload during hidden phase: fixed target, leader, member arrays, motives, doctrine, pulse, suspects, and missions persist.
5. Founder annexed/capitulated/subjected/civil-war/faction-leader before reveal: refresh removes or loyalty-tests it without corrupting arrays.
6. Target annexed or made non-playable: run archives and cleans; it never retargets the conqueror.
7. Human candidate in multiplayer: no membership until explicit join; refuse/leak/expose outcomes work; no timeout acceptance.
8. Operation concurrency: a second substantial operation cannot start; recovery/recent-family flags prevent spam.
9. Evidence farming: the same clue/source gives no repeat Evidence; independent classes provide corroboration.
10. Preparedness expiry: maintained project cost and value disappear correctly; no permanent stacking.
11. Evolution I/II/III active: each applies and logs once only when enabled and paced.
12. Pre-fire I: three founders plus accelerated recruit. Pre-fire II: three founders plus sponsor. Pre-fire III: II package plus delayed III transition.
13. Evolutions disabled: baseline operations, hostile-war reveal, hidden collapse, and cleanup remain functional.
14. Member attacks target and target attacks member: both ROOT/FROM orientations immediately reveal.
15. Member joins an existing target war: reveal occurs on the new relation and every active member joins that same war.
16. Border conflict only: no reveal. Escalation to normal war: immediate reveal.
17. Recursive join on-actions: guard prevents duplicate faction creation, super event, and war joins.
18. Safe factioned member: leaves its old faction before joining; an unsafe leader/war state is pruned rather than dragging a third faction.
19. Turned/delayed/compromised: all active members join hard reveal; each gets the correct concrete opening state; false plan creates a wartime consequence.
20. Dynamic faction title: normal target adjective path and explicit name-fallback path both resolve.
21. Scenario type matrix: all five composition/doctrine algorithms produce valid, distinct coalitions.
22. Scenario intensity matrix: Low/Medium/High/Maximum counts, major caps, readiness/resolve/equipment/AI scale, and insufficient-pool gates.
23. Maximum scenario with fewer than upper-band candidates: every safe candidate up to cap is used and achieved count is reported; invalid/human countries are not forced.
24. Scenario after a completed normal run: launch is permitted after runtime cleanup and uses fresh run trackers.
25. Maximum snapshot: changing GUI intensity later does not qualify/disqualify the run.
26. Every Thread snapshot: removed invalid members do not count; every active reveal member and no innocent is required.
27. Divide the Table: event fracture exits count; capitulation/annexation do not.
28. Two Giants: major status is frozen at reveal and starting-capital result is frozen at settlement.
29. All five postwar outcomes: correct faction persistence/dissolution, member settlement, achievements, and cleanup.
30. Cleanup called twice from different terminal hooks: same final state, no unrelated faction/idea/AI removal, no stale global targets.
31. Large-country-count performance: no recurring world scan, bounded ticket pool, compact suspect UI, and target-owned scheduler only.

## Blockers and completion boundary

There is no architecture blocker to implementation.

Two items require explicit implementation validation rather than a design fallback:

1. Verify the exact accepted dynamic faction localisation for the allowed target set and exercise the explicit name-fallback flag. Do not replace it with a static faction title if a target class fails.
2. Verify every `add_to_war` call leaves the joining member in the anchor's existing target war. A failed join is a script defect to fix; do not create separate wars as a substitute.

This handoff deliberately makes no gameplay changes and does not claim Event 011 implementation completion.
