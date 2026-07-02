# Event 011 Secret Alliance Scripted System Architect Handoff

## Files Changed

Parent integration note: the final integrated Event 011 implementation promotes the three founder targets and the public leader target to global event targets so later decisions, reveal checks, cleanup, achievements, and localisation can safely reference them across event chains. The notes below describe the architect handoff as originally delivered before that parent integration pass.

- `common/script_constants/011_secret_alliance_constants.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/scripted_system_architect_event_011_handoff.md`

No event, decision, localisation, GUI, asset, achievement, audio, or shared dirty files were edited.

## Helper Names and Behavior

### Constants

- `secret_alliance_event`: event id and evolution type.
- `secret_alliance_requirement`: founder count, active member floor, and map-control gates.
- `secret_alliance_role`: numeric role ids for Convener, Financier, Provocateur, Patron, Recruit, and Broker.
- `secret_alliance_phase`: lifecycle ids from inactive through aftermath and collapsed.
- `secret_alliance_evolution_stage`: baseline and Evo I, II, III stage ids.
- `secret_alliance_meter`: shared 0 to 100 meter floor, bands, and cap.
- `secret_alliance_opening_value`: opening values for secrecy, cohesion, readiness, suspicion, evidence, counter-readiness, leverage, and member confidence.
- `secret_alliance_delta`: reusable meter changes, reveal changes, and AI pulse values.
- `secret_alliance_member_cap`: baseline and evolution member caps.
- `secret_alliance_selection_weight`: weighted founder/member pool entries and penalties.
- `secret_alliance_selection_threshold`: fixed-point opinion and target weakness gates.
- `secret_alliance_evolution_threshold`: member, readiness, cohesion, suspicion, and evidence gates.
- `secret_alliance_reveal_threshold`: public reveal and self-reveal gates.
- `secret_alliance_ai_weight`: AI tuning scaffold for later decisions.

### Triggers

- `secret_alliance_can_be_target`: validates a target country and requires enough valid founder candidates.
- `secret_alliance_target_has_active_pact`: checks active Event 011 target state and saved target.
- `secret_alliance_is_valid_founder_for_root_target`: candidate country gate with `ROOT` as target. Requires an independent diplomatic actor and excludes the target, target faction, target subjects, all other subjects, direct target war, capitulated countries, special chaos countries, nonhuman countries, world-end state, existing members, and local diplomacy locks.
- `secret_alliance_is_valid_member_candidate_for_root_target`: founder gate plus member cap check.
- `secret_alliance_member_is_live_for_root_target`: live member validity gate.
- `secret_alliance_member_should_leave_for_root_target`: removal reason gate.
- `secret_alliance_has_live_members`, `secret_alliance_has_minimum_pre_reveal_members`: member-count gates.
- `secret_alliance_can_publicly_reveal`, `secret_alliance_can_self_reveal`: reveal gates.
- `secret_alliance_can_unlock_evolution_i`, `secret_alliance_can_unlock_evolution_ii`, `secret_alliance_can_unlock_evolution_iii`: active pact evolution gates.
- `secret_alliance_ai_can_use_counterplay`, `secret_alliance_ai_should_prepare_for_war`: AI-safe target-side helper gates.

### Effects

- `secret_alliance_initialize_values`, `secret_alliance_clamp_values`: initialize and clamp pact and target meters.
- `secret_alliance_add_secrecy`, `secret_alliance_add_cohesion`, `secret_alliance_add_readiness`, `secret_alliance_add_suspicion`, `secret_alliance_add_evidence`, `secret_alliance_add_counter_readiness`, `secret_alliance_add_leverage`, `secret_alliance_add_member_confidence`: bounded value adjusters. Callers set `secret_alliance_value_delta` before calling.
- `secret_alliance_prepare_founder_candidate_weight`, `secret_alliance_add_current_country_to_founder_pool`, `secret_alliance_prepare_founder_pool`, `secret_alliance_select_three_founders`: weighted founder selection. Selected founders are tracked in a temporary array while choosing roles so a country cannot receive two founder slots.
- `secret_alliance_prepare_member_candidate_pool`: weighted post-opening recruitment pool. This is separate from the founder pool because an active target should no longer satisfy the opening-only target gate.
- `secret_alliance_initialize_pact`: target-scope opening helper. Saves `secret_alliance_target`, clears and builds member/founder arrays, initializes values, selects three founders, assigns roles, and calculates member cap. Sets `secret_alliance_context_ready = 1` only when three founders were selected.
- `secret_alliance_register_member_from_current_scope`: adds current country to `global.secret_alliance_members`, sets member flag, count, confidence, and default role.
- `secret_alliance_assign_founder_roles`: assigns Convener, Financier, and Provocateur using the selected founder event targets.
- `secret_alliance_calculate_member_cap`: calculates target variable `secret_alliance_member_cap`.
- `secret_alliance_try_invite_member`: weighted capped recruit selection and registration.
- `secret_alliance_refresh_member_validity`: rebuilds the live member array and clears stale member state for invalid members without mutating the source array during iteration.
- `secret_alliance_clear_current_member_state`: clears member, founder, role, suspect, confirmed, public-leader, and blocked-faction state from the current country.
- `secret_alliance_member_leave_pact`: calls current-member cleanup and removes the country from Event 011 member/founder arrays.
- `secret_alliance_collapse_pact_if_invalid`: collapses a pre-reveal pact with too few members.
- `secret_alliance_reveal_pact_publicly`: marks the pact public, confirms live members, lowers secrecy, raises readiness, and moves phase to public.
- `secret_alliance_prepare_public_leader`, `secret_alliance_form_anti_target_faction`: picks the Convener or a live member as public leader, creates `secret_alliance_anti_target_pact` when the leader is not already in a faction, and adds unfactioned live members.
- `secret_alliance_pull_live_members_into_reveal_war`: joins live members to the war side of `event_target:secret_alliance_war_reveal_member` against `ROOT`.
- `secret_alliance_reveal_pact_by_war`: target-scope war reveal helper. Requires `secret_alliance_war_reveal_member` to be saved by the caller, then runs public reveal, marks war reveal, forms the faction, and calls all-live-member war join.
- `secret_alliance_apply_baseline_package`: target-scope baseline helper that refreshes phase and member cap without writing an evolution log entry.
- `secret_alliance_unlock_evolution_i`, `secret_alliance_unlock_evolution_ii`, `secret_alliance_unlock_evolution_iii`, `secret_alliance_check_evolution_unlocks`: event-log aware Evo I, II, and III helpers.
- `secret_alliance_apply_ai_counterplay_pulse`: simple AI-safe evidence and counter-readiness pulse.

## Call Sites Changed

None. Owned scope forbids editing `events/011_secret_alliance.txt`, decisions, localisation, GUI, assets, achievements, and audio.

Expected parent call sites:

- Event opening: call `secret_alliance_initialize_pact = yes` in target scope and proceed only when `secret_alliance_context_ready > 0`.
- Invitation pulse: call `secret_alliance_refresh_member_validity = yes`, then `secret_alliance_try_invite_member = yes`.
- Evolution controller: call `secret_alliance_check_evolution_unlocks = yes`.
- Investigation and decision results: set `secret_alliance_value_delta`, then call the matching bounded meter helper.
- War reveal detector: in target scope, save the first member at war with the target as `secret_alliance_war_reveal_member`, then call `secret_alliance_reveal_pact_by_war = yes`.
- Public exposure decision: call `secret_alliance_reveal_pact_publicly = yes`.
- AI target pulse: call `secret_alliance_apply_ai_counterplay_pulse = yes` from an existing Event 011 pacing event or decision, not from a new global on-action.

## Constants and Tuning Table Plan

The constants file centralizes:

- target and founder requirements
- role ids
- phase ids
- meter bands
- opening values
- delta ladder
- member caps
- founder/member weighting
- reveal thresholds
- evolution thresholds
- AI tuning anchors

No file-scoped `@` constants were added because the helper layer does not set timed flags or timed ideas.

## Event Target and Cleanup Plan

- `secret_alliance_initialize_pact` saves the target as global event target `secret_alliance_target`.
- Founders were originally handed off as regular event targets; the parent integration pass now saves `secret_alliance_founder_convener`, `secret_alliance_founder_financier`, and `secret_alliance_founder_provocateur` as global event targets and clears them during resolution cleanup.
- Persistent membership uses arrays and country flags, not long-lived regular event targets.
- `secret_alliance_prepare_public_leader` now saves the current public leader as a global event target for reveal, war, faction, localisation, and cleanup paths.
- War reveal requires the caller to save `secret_alliance_war_reveal_member`.
- `secret_alliance_collapse_pact_if_invalid` clears the global target on pre-reveal collapse.

## Migration Plan

1. Add Event 011 opening script and call `secret_alliance_initialize_pact`.
2. Use `secret_alliance_context_ready` to block firing or show `N/A` in event-list weighting when founders cannot be selected.
3. Replace inline meter math in Event 011 events, decisions, missions, and GUI buttons with the bounded value helpers.
4. Replace inline member cleanup with `secret_alliance_refresh_member_validity` and `secret_alliance_member_leave_pact`.
5. Call reveal helpers from public exposure, self-reveal, and war-detection paths.
6. Wire decision and GUI target selectors against `global.secret_alliance_members`, `secret_alliance_member_suspected`, and `secret_alliance_member_confirmed`.

## Validation

- Checked touched helper scripts for unsupported comparison operators.
- Checked touched helper scripts for remaining temporary work labels.
- Checked touched helper files for `secret_alliance_` helper and constant references.

## Blockers and Uncertainty

- Parent integration added localisation and scripted localisation wiring for the Anti-[target country] Pact.
- Founder/member selection deliberately requires independent diplomatic actors. Subject countries are treated as invalid signatories because the public pact, faction, and war-reveal package rely on sovereign diplomatic agency rather than overlord-mediated diplomacy.
- Existing shared world-threat state has aggregate/source flags but no country-scoped `is_world_threat_actor` trigger. Special chaos and nonhuman exclusions are used where available. If a future event creates a normal-looking country that is a world-threat actor, the shared classifier should be extended outside this Event 011-only patch.
- War reveal requires the caller to identify and save `secret_alliance_war_reveal_member`. The helper does not scan the world from a daily or weekly global on-action.
- Parent integration keeps faction formation conservative when the selected public leader is already in a faction and routes reveal pressure through the public crisis and war helpers.
- Parent integration wired the reveal super-event, image, researched text, and licensed audio package.

## Parent Follow-Up

- Parent integration added Event 011 event, decision, localisation, idea, GUI, super-event, audio, achievement, and audit surfaces after this architect handoff.
