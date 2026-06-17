# Event 012 Africa Decision and Mission Audit Handoff

## Scope

Audited Event 012 Africa decisions and missions against:

- `docs/specs/012_africa_specs/prompts/012_africa_decision_mission_prompt.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `docs/specs/012_africa_specs/matrices/012_africa_decision_map.md`
- `docs/plans/012_africa_plans/2026-06-16_foundation_gap_improvement_addendum.md`

Required references consulted before patching:

- Offline wiki: Decision modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Idea modding, AI modding.
- Vanilla docs: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`.
- Vanilla examples: `common/decisions/AST.txt`, `common/decisions/foreign_influence.txt`, `common/decisions/SAF.txt`.
- Repo guidance: `hoi4-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-events`.

## Patch Applied

Changed file:

- `localisation/english/012_african_union_l_english.yml`

Changed localisation ids:

- `africa_send_league_aid_cost_tt`
- `africa_send_league_aid_cost_tt_blocked`
- `africa_send_league_aid_cost_tt_tooltip`
- `africa_prepare_liberation_operation_cost_tt`
- `africa_prepare_liberation_operation_cost_tt_blocked`
- `africa_prepare_liberation_operation_cost_tt_tooltip`
- `africa_complete_living_core_state_cost_tt`
- `africa_complete_living_core_state_cost_tt_blocked`
- `africa_complete_living_core_state_cost_tt_tooltip`
- `africa_open_next_historical_dossier_cost_tt`
- `africa_open_next_historical_dossier_cost_tt_blocked`
- `africa_open_next_historical_dossier_cost_tt_tooltip`
- `africa_raise_old_seat_guard_cost_tt`
- `africa_raise_old_seat_guard_cost_tt_blocked`
- `africa_raise_old_seat_guard_cost_tt_tooltip`
- `africa_unlock_bestiary_package_cost_tt`
- `africa_unlock_bestiary_package_cost_tt_blocked`
- `africa_unlock_bestiary_package_cost_tt_tooltip`

Before:

- Six `custom_cost_text` keys existed as sentence-style requirement text.
- The required `_blocked` and `_tooltip` localisation variants were missing, so the cost UI could display poorly or fall back to raw keys depending on blocked state.

After:

- The six custom cost ids now show icon-first costs matching current decision tuning:
  - League aid: 450 infantry equipment, 60 support equipment.
  - Liberation operation: 900 infantry equipment, 7000 manpower.
  - Living core: 3000 manpower.
  - Historical dossier: 80 support equipment.
  - Old-seat guard: 500 infantry equipment, 70 support equipment, 3000 manpower.
  - Bestiary package: 100 support equipment.
- Each has matching red blocked text and a tooltip describing the actual resource consumption or transfer.

## Validation

Ran:

- `rg -n "custom_cost_text = africa_.*cost_tt|africa_.*cost_tt(_blocked|_tooltip)?:" common/decisions/012_africa_decisions.txt localisation/english/012_african_union_l_english.yml`
- `xxd -l 3 localisation/english/012_african_union_l_english.yml`

Result:

- All six `custom_cost_text` ids in `common/decisions/012_africa_decisions.txt` have base, `_blocked`, and `_tooltip` localisation in `012_african_union_l_english.yml`.
- Localisation file still begins with UTF-8 BOM bytes `ef bb bf`.

Skipped:

- No full game load or parser run was performed from this subagent pass.
- No broad scripted effect, trigger, or decision redesign was attempted because the requested mode was audit plus safe small patch only.

## Issues Sorted By Severity

1. Critical: Several accepted-spec decision systems are still missing as playable surfaces.
   - Missing Diaspora Return Offices category and decisions from the prompt and UI spec.
   - Liberation War Office has only `africa_prepare_liberation_operation` at `common/decisions/012_africa_decisions.txt:358`; it lacks protect-ally, rail/port/corridor, colonial-holder, and map-objective missions.
   - Regional Integration has state survey and core completion at `common/decisions/012_africa_decisions.txt:398` and `:426`, but no timed map-objective integration missions.
   - RSA emergency has only `africa_rsa_secure_charter_supply` at `common/decisions/012_africa_decisions.txt:781`; it does not yet model side-specific survival, supply route, capital defense, or Allied pressure objectives.

2. High: The Authority Atlas selected-dossier flow is structurally present but too shallow for the accepted addendum.
   - Parent follow-up replaced immediate opening with `africa_selected_dossier_survey_mission`: the dossier only opens after the timed survey succeeds while the representative seat is controlled or Charter-protected.
   - Local office, guard, and settlement decisions now use selected-dossier triggers such as `can_africa_build_selected_dossier_local_office`, `can_africa_raise_selected_dossier_guard`, and `can_africa_settle_selected_dossier`.
   - The selected-dossier triggers check generated per-dossier flags for opened, surveyed, local-office, guard, and settlement state, so duplicate protection and lifecycle enforcement exist. The remaining gap is richer dossier-specific objectives, resistance, and subject/tag outcomes.

3. High: High-chaos package flow is incomplete relative to the catalog and accepted addendum.
   - `africa_spawn_high_chaos_actor_for_selected_package` at `common/scripted_effects/012_africa_effects.txt:522` only handles gorilla highlands, crocodile rivers, baobab senate, tidemark dominion, ananse ledger, and orisha/vodun nature courts.
   - The catalog/localisation includes chimpanzee marshes, okapi court, termite surveyors, honeyguide commons, and great herds, but those packages do not spawn actors.
   - `africa_verify_omen_reliability` at `common/decisions/012_africa_decisions.txt:679` is a positive-value timer, not the requested false-warning and disaster-risk flow.

4. Medium: Timed decisions mostly function as delayed button rewards, not missions with success and failure.
   - Most `days_remove` decisions apply rewards in `complete_effect` and have no `remove_effect`, partial success, failure, or cleanup branch.
   - This affects Congress, influence, authority docketing, liberation preparation, dossier office/guard/settlement, Bestiary reports, sponsorship, World Is One gate preparation, and RSA emergency supply.

5. Medium: Sponsor and World Is One gate checks are strong enough as gates but shallow as gameplay.
   - `can_africa_start_world_is_one_gate` at `common/scripted_triggers/012_africa_triggers.txt:243` checks the correct broad state: Africa is One, super-event done, other continent unifier readiness, regional authorities, living cores, dossiers, high-chaos packages, and sponsor preparation.
   - `africa_prepare_continent_sponsor_mission` and `africa_prepare_world_is_one_gate` at `common/decisions/012_africa_decisions.txt:734` and `:755` are still simple timers without continent target selection or sponsor-specific route work.

6. Superseded follow-up: dynamic dossier and high-chaos cleanup.
   - Parent follow-up confirmed `africa_clear_authority_atlas_progress_flags` clears generated per-dossier and per-package flags through the registered catalog arrays, and `africa_establish_union_start` calls it after catalog registration.
   - The helper also clears selected survey, direct Archive seal, macro-region, profile, high-chaos, warning, and Bestiary action state. The remaining dossier gap is depth and scenario validation, not missing reset coverage.

7. Low: AI weights exist on every reviewed decision, but targeting quality is uneven.
   - Candidate and member target arrays are valid patterns, and target triggers exclude dead/special/nonhuman invalid candidates via `is_africa_charter_league_candidate_for_prev` at `common/scripted_triggers/012_africa_triggers.txt:77`.
   - Some AI entries are flat constants and do not account for active wars, equipment strain, colonial alarm, unrest, or selected high-chaos package risk.

## Decision Category Lifecycle Notes

- `africa_continental_congress_category` at `common/decisions/012_africa_decisions.txt:9`: Visible and value-bearing. Congress and register decisions establish the layer, but Congress is a repeatable value timer with no failure or agenda tradeoff.
- `africa_charter_league_diplomacy_category` at `:53`: Target arrays are present for candidates and members. Aid/leave/fight-back support exists, but diplomacy remains thin on cooldown outcomes and target-state cleanup.
- `africa_charter_member_category` at `:211`: Member request aid, leave, and resistance war are present. This satisfies the minimum member agency surface, though leave/fight-back can use more route-lock and cooldown granularity.
- `africa_liberation_war_office_category` at `:353`: Category exists but is underbuilt. Current content is one generic operation prep decision.
- `africa_regional_integration_category` at `:391`: State-target survey and living core flow is present and uses state ownership/control checks, but accepted timed objectives and regional office work are absent.
- `africa_authority_atlas_category` at `:466`: Selected dossier, office, guard, and settlement choices exist. Per-dossier gating and mission objectives are the largest lifecycle gap.
- `africa_high_chaos_category` at `:620`: Bestiary unlock, habitat terms, omen reliability, and actor binding exist. Actor coverage and omen risk are incomplete.
- `africa_continent_sponsor_category` at `:729`: Broad gates exist. Targeted sponsor work is missing.
- `africa_rsa_civil_war_emergency_category` at `:773`: Emergency category exists with one supply decision. It needs real civil-war objectives and fail states.

## Mission Quality Notes

Current Event 012 uses timed decisions, not true mission objects. Relevant mission-like entries:

- Owner: Africa. Category: Continental Congress. Region: continental. Requirement: active Charter country. Duration: 35 days. Success: legitimacy and cohesion. Failure: none. Duplicate risk: low, but passive-store risk remains.
- Owner: Africa. Category: Charter League Diplomacy. Region: target Charter member. Requirement: member target and focus gates. Duration: 45/60 days depending on influence/docket. Success: values or integration docket. Failure: none. Duplicate risk: medium if target state changes during timer.
- Owner: Africa. Category: Liberation War Office. Region: unspecified liberation front. Requirement: mandate, command authority, equipment, manpower. Duration: 60 days. Success: Liberation Momentum. Failure: none. Duplicate risk: medium because no target objective is tied to a war/front.
- Owner: Africa. Category: Regional Integration. Region: African state target. Requirement: claim/control/ownership and survey state. Duration: instant targeted decisions. Success: paper survey or living core. Failure: none. Duplicate risk: low due state flags, but no timed objective.
- Owner: Africa. Category: Authority Atlas. Region: selected dossier, not mapped. Requirement: Atlas/focus gates and support/manpower/equipment. Duration: 45 or 75 days. Success: opens, offices, guards, or settles selected dossier. Failure: none. Duplicate risk: high due aggregate counter gating instead of per-selected-dossier gating.
- Owner: Africa. Category: High-Chaos Reports. Region: selected package or Charter member target. Requirement: Bestiary Clause and focus gates. Duration: 90 days. Success: package unlock, habitat/omen values, or actor binding. Failure: none. Duplicate risk: medium; some selected packages have no actor spawn branch.
- Owner: Africa. Category: Continental Sponsorship. Region: global/other continents. Requirement: continental thresholds. Duration: 90 days. Success: sponsor or World Is One gate flag. Failure: none. Duplicate risk: low due flags, but gameplay depth is low.
- Owner: RSA continental side. Category: RSA Civil-War Emergency. Region: South Africa. Requirement: RSA continental emergency flag. Duration: 21 days. Success: momentum and war support. Failure: none. Duplicate risk: medium as repeat support loop if timer/cooldown values are permissive.

## Cost And Requirement Clarity Notes

- Patched custom cost localisation to match current constants and HOI4 custom cost UI requirements.
- Costs are better than flat PP: equipment and manpower are used for aid, liberation, living cores, dossiers, guards, and Bestiary reports.
- Several non-cost decisions still mostly exchange time for variables and should gain map, subject, equipment, convoy, train, XP, or local-support requirements during the next implementation tranche.
- Decision constants are centralized in `common/script_constants/012_africa_constants.txt`, which is good. Avoid hardcoding future mission objective numbers inside decisions.

## AI Validity And Route-Lock Notes

- Target arrays are mostly valid: `global.africa_charter_candidate_countries`, `global.africa_charter_member_countries`, and state target `africa` follow HOI4 decision patterns.
- Candidate triggers exclude special chaos and actual nonhuman countries, helping avoid invalid Charter invitations.
- Bestiary route-lock has a safety gate through `can_africa_unlock_bestiary_clause`, but incomplete package actor handling creates route gaps after unlock.
- Sponsor/World Is One route-lock is broad and readable, but the decisions do not yet pick or validate sponsor targets.

## Localisation And Tooltip Gaps

- Patched six custom cost ids and their blocked/tooltip variants.
- Remaining tooltip gap: several long available triggers are hidden behind custom trigger tooltips, but effect text is still generic for complex systems such as World Is One, Authority Atlas settlement, Bestiary package spawn, and RSA emergency.
- No new decision ids were added, so no additional localisation ids were required in this pass.

## Cleanup And Exploit-Risk Notes

- Member aid and member request aid have resource gates, but future cooldown and target war-state checks should be reviewed for repeated equipment/manpower farming.
- Resistance war creates emergency units; current availability blocks some repeated use, but post-war cleanup and flag expiry should be audited alongside event outcomes.
- Dossier per-id flags are set but not enforced in decision availability, creating duplicate-action risk on the active dossier.
- High-chaos package unlock can advance package counts even where no actor branch exists.
- RSA emergency supply is repeatable and positive-only; add a failure/removal branch or stronger cooldown before treating it as complete.

## Concrete Recommended Fixes

1. Add per-selected-dossier scripted triggers in `common/scripted_triggers/012_africa_triggers.txt` and use them in `common/decisions/012_africa_decisions.txt` for local office, guard, and settlement availability. This should consume the existing dynamic flags from `common/scripted_effects/012_africa_effects.txt:931-1002`.
2. Expand `africa_spawn_high_chaos_actor_for_selected_package` in `common/scripted_effects/012_africa_effects.txt:522` or restrict unlock availability until each selected package has a valid actor/route. Do not let catalog entries unlock into no actor.
3. Add real timed missions or mission-like decisions with `remove_effect` for Liberation War Office, Regional Integration, Authority Atlas, High-Chaos Omen Reliability, Sponsor missions, and RSA emergency.
4. Add Diaspora Return Offices category and decisions from the prompt/spec, or record it as intentionally queued in the Event 012 implementation plan.
5. Add cleanup/reset coverage for per-dossier dynamic flags and high-chaos package flags in the existing reset/start helpers.
6. Deepen AI weights with route-aware modifiers for equipment shortage, active war, colonial alarm, high mythic volatility, and member resistance risk.

No separate broad plan was written in this pass; the accepted foundation gap improvement addendum already covers the larger missing systems. This handoff records the decision/mission-specific blockers for the parent implementation pass.

## Parent Follow-Up: 2026-06-17 Member Confidence Mission

The Charter aid/confidence gap is partially resolved. `africa_send_league_aid` targets full members through `global.africa_charter_member_countries`; `africa_send_protected_league_aid` targets protected members through `global.africa_charter_protected_countries`. Both decisions use `africa_transfer_league_aid_to_from` and start `africa_member_confidence_mission` when aid is sent to a Charter-side country that is already at war and no other confidence mission is active. The mission stores the aided country as `africa_member_confidence_target`; success requires that country to remain in the Charter relationship, avoid capitulation, and finish its war before the deadline. Failure raises Colonial Alarm and lowers League Cohesion. The target and result flags are cleaned up by Event 012 runtime teardown and establishment reset.

Remaining Charter-diplomacy gaps: confidence is still one active target at a time, there are no separate land/sea/air corridor missions, and member leave/fight-back behavior still needs more route-specific cooldown and settlement nuance.

## Parent Follow-Up: 2026-06-17 Direct Archive Seal Mission

The Authority Atlas coercive-settlement gap is partially resolved. `africa_settle_selected_dossier_direct_archive` now starts `africa_direct_archive_seal_mission`, a true timed proof crisis with visible Legitimacy, Old-Seat Legitimacy, and Restoration Debt thresholds in the Authority Atlas header. Success raises Authority and Old-Seat Legitimacy while relieving Restoration Debt. Failure marks the seal exposed, raises Restoration Debt and Colonial Alarm, lowers Legitimacy and Old-Seat Legitimacy, and fires the Counterfeit Crowns super-event surface. Mission flags are cleaned by Event 012 runtime teardown, establishment reset, and Authority Atlas progress reset.

Remaining Authority Atlas gaps: historical dossiers still need package-specific missions, local resistance events, and richer per-dossier AI prioritisation beyond the shared selected-dossier lifecycle.

## Parent Follow-Up: 2026-06-17 Omen Reliability Review Mission

The high-chaos omen-risk gap is partially resolved. `africa_verify_omen_reliability` now starts `africa_omen_reliability_review_mission` instead of immediately granting verified warnings. The mission requires Habitat Trust to meet its gate while Bestiary Alarm and Mythic Volatility stay below their caps; success sets `africa_omen_reliability_verified`, and failure raises Bestiary Alarm, Mythic Volatility, and Covenant Pressure while leaving warnings locked. The high-chaos category header shows `GetAfricaOmenReliabilityStatus`, and the threshold tooltip reads from seeded globals tied to script constants.

Remaining high-chaos gaps: warning consequences still use compliance/defiance event outcomes rather than route-specific disaster effects, and the package-side operations remain lightweight package actions rather than full country-package surfaces.

## Parent Follow-Up: 2026-06-17 Aid Corridor Mission

The Charter aid-corridor gap is partially resolved. `africa_open_member_aid_corridor` and `africa_open_protected_aid_corridor` now target warring full/member-array Charter countries and protected members through separate arrays. They require Charter General Staff, one active corridor cap, command power, support equipment, convoys, and trains; `africa_open_aid_corridor_to_from` spends those resources from the League leader, gives the target manpower and logistics stockpiles, stores `africa_aid_corridor_target`, raises Liberation Momentum, and starts `africa_aid_corridor_mission`. The mission succeeds only if the target remains in the Charter relationship, avoids capitulation, and finishes the war before the deadline; success raises League Cohesion and Regional Trust, while failure raises Colonial Alarm and lowers League Cohesion. The Charter category header surfaces `GetAfricaAidCorridorStatus`, and runtime cleanup clears the global target and per-target result flags.

Remaining Charter-diplomacy gaps: the corridor is still one active target at a time, does not distinguish land/sea/air route variants, and does not yet have target-specific local support, route-state control, or foreign interdiction events.

## Parent Follow-Up: 2026-06-17 Bestiary Warning Route Pressure

The high-chaos warning-consequence gap is partially resolved. Defiance in both holder warnings and state-holder warnings now calls `africa_apply_bestiary_warning_defiance_package_pressure`. The effect checks durable unlocked Bestiary package flags and applies small route-specific value movement: gorilla guard warnings affect Habitat Trust and Bestiary Alarm, chimpanzee scouts affect Liberation Momentum and Mythic Volatility, okapi observers affect Regional Trust and Local Sovereignty, crocodile tolls affect Authority and Bestiary Alarm, baobab records affect Old-Seat Legitimacy and Restoration Debt, termite surveyors affect Authority and Paper-Core Burden, honeyguide routes affect League Cohesion and Archive Mandate, great herd compacts affect Mythic Volatility and Colonial Alarm, tidemark tides affect Habitat Trust and Covenant Pressure, Ananse counterfeit watch affects Archive Mandate and Colonial Alarm, and nature-court covenants affect Habitat Trust and Covenant Pressure. The new effect keeps values clamped and is surfaced through `africa_bestiary_warning_package_defiance_effect_tt`.

Remaining high-chaos gaps: the warning response still does not fire package-specific event text, map disasters, or target-country penalties, and the package-side operations remain lighter than full actor-country surfaces.

## Parent Follow-Up: 2026-06-17 Sponsor Readiness Mission

The continent-sponsor readiness deadlock is resolved. `AFR_africa_is_one` requires `africa_continent_sponsor_ready`, but the old `africa_prepare_continent_sponsor_mission` required `africa_is_one_complete`, making the route internally circular. The decision now requires the Continent Sponsor Office and World Root mandate, spends convoys, support equipment, and command power, and starts `africa_continent_sponsor_readiness_mission`. The mission completes when the Continental Register, World Root mandate, required regional authorities, required living cores, minimum historical dossiers, and minimum Bestiary packages are all proven; success sets `africa_continent_sponsor_ready`, raises Legitimacy and Authority, and fires the continent-sponsor super-event surface. Failure raises Colonial Alarm and Restoration Debt. The sponsor category header now displays `GetAfricaSponsorReadinessStatus`.

Remaining sponsor/world-order gaps: cross-continent charters are still Africa-local route flags, not integrations with separate continent-unifier event systems, and World Is One certification still needs external prerequisite hooks.

## Parent Follow-Up: 2026-06-17 Continental Congress GUI First Actions

The display-only Continental Congress GUI gap is partially resolved. `africa_continental_congress_category` now attaches `africa_continental_congress_scripted_gui`. The scripted GUI defines click handlers and click-enabled triggers for four first-pass actions: Congress, Register, Dossier, and Sponsor. Each action spends PP and any required support equipment, convoys, or command power; calls the existing Event 012 helper path; and sets a timed recent-action flag to prevent repeat-click exploitation. The GUI layout now includes a warning/status line for Aid Corridor, Archive Seal, Omen Review, and Sponsor Readiness plus four visible action buttons.

Remaining GUI gaps: this is not the full accepted regional/member/dossier card interface. It does not yet include dynamic region/member card lists, per-target GUI selection, state cards, or warning drill-down panels. Decision and mission surfaces still provide those target-specific controls.

## Parent Follow-Up: 2026-06-17 Liberation Front-State Objectives

The Liberation War Office map-objective gap is partially resolved. `africa_secure_liberation_objective_state` now targets controlled African front states through decision map mode, requires an active liberation-front mission and war, spends support equipment, manpower, and command power, marks the state as secured, improves infrastructure, and advances a visible front-objective counter in the category header. `africa_liberation_front_deadline_mission` now requires border columns, rail-belt offices, and the configured number of secured front states before it can succeed. Runtime setup and teardown clear the state flags and objective counter.

Remaining Liberation War Office gaps: the objective still uses a shared front-state rule rather than named corridor sets for each regional route, and it does not yet model land/sea/air variants, local-support thresholds, foreign interdiction, or package-specific postwar settlement events.

## Parent Follow-Up: 2026-06-17 Authority Atlas Guarded Settlement

The selected-dossier lifecycle is stricter. The current code already had per-selected-dossier meta-triggers for opened, surveyed, local office, guard, and settlement state, and the office/guard/settlement decisions consume those triggers. The remaining gap was settlement availability: it required the selected dossier's local office, but not the selected dossier's guard. `can_africa_settle_selected_dossier` now requires `has_africa_selected_dossier_guard = yes`, so observer and direct Archive settlements cannot resolve an active dossier before its own old-seat guard exists.

Remaining Authority Atlas gaps: historical dossiers still share a broad mission shape and profile effects rather than having package-specific events, local resistance chains, or bespoke AI prioritisation for each dossier.

## Parent Follow-Up: 2026-06-17 Liberation Objective Retry Cleanup And Expanded Bestiary Actors

The latest decision audit finding on liberation objective retry persistence is resolved. `africa_liberation_front_deadline_mission` now calls `africa_clear_liberation_objective_progress` on cancel, success, and timeout. That helper clears `africa_liberation_objective_states_ready`, resets `africa_liberation_objective_state_count`, and removes `africa_liberation_objective_secured` from every marked state, so a failed or cancelled liberation-front mission cannot be restarted with stale secured objectives.

The Authority Atlas header now uses `GetAfricaSelectedDossierSeatName` instead of rendering `africa_selected_dossier_seat_state` directly. The scripted localisation returns the selected state name when the variable exists and `No seat selected` otherwise.

The high-chaos package actor gap is also narrowed. Chimpanzee Marshes, Okapi Court, Termite Surveyors, Honeyguide Commons, and Great Herds now map to explicit actor tags `CTL`, `OKP`, `TRM`, `HGD`, and `GHC`. Each has tag registration, country/history files, ideology and party localisation, portrait sprite ids, seat-state constants, setup-package effects, habitat-seat unlocks, nonhuman/special classification, focus-tree route access, and AI posture coverage. Their generated flag and portrait assets were delivered in `8e8d6367` and documented in `2026-06-17_012_africa_bestiary_actor_assets_handoff.md`.

Remaining decision/mission risks: liberation objective targeting remains broad and can still select loyal rear-area Charter states; narrowing it to named front corridors should be a design pass, not a silent fallback. The expanded actor target-action gap was addressed in the follow-up tranche recorded below.

## Parent Follow-Up: 2026-06-17 Country Package Audit Fix

The country-package audit found a file-scoped constant issue in the expanded Bestiary actor tranche. The CTL, OKP, TRM, HGD, and GHC seat constants are now declared in `common/scripted_effects/012_africa_effects.txt` as well as the trigger file, so spawn branches in `africa_spawn_high_chaos_actor_for_selected_package` no longer depend on constants from another file. The stale improvement-addendum note that described Honeyguide Commons and Great Herds as deferred has also been updated to reflect the implemented actor packages.

Remaining country-package risks: the expanded actors still need longer local event chains, disaster consequences, and settlement hooks before they match the older actor packages in playable depth.

## Parent Follow-Up: 2026-06-17 Expanded Bestiary Actor Target Actions

The expanded Bestiary actors now have actor-target decisions in `common/decisions/012_africa_decisions.txt`. `CTL` can be tasked with Chimpanzee Telegraph relays, `OKP` can provide Okapi shadow dossiers, `TRM` can receive a Termite Citadel engineer commission, `HGD` can open Honeyguide aid routes, and `GHC` can muster Great Herds relief columns. Each action targets the actor through `global.africa_charter_member_countries`, requires the matching opened Bestiary case, checks that the actor is an active high-chaos actor, sets an actor-side one-time flag, spends visible equipment/manpower/convoy/command/XP costs, moves Event 012 values, and increments `africa_bestiary_package_action_count`.

Remaining Bestiary risks: these actions now fire local action-report events, but they still do not have multi-step local event chains, bespoke disaster consequences, or settlement-hook outcomes.

## Parent Follow-Up: 2026-06-17 Expanded Bestiary Local Consequence Events

The five expanded actor actions now fire visible local consequence events after completion: `chaosx.nr12.40` for Chimpanzee Telegraph relays, `chaosx.nr12.41` for Okapi shadow dossiers, `chaosx.nr12.42` for Termite Citadel engineer commissions, `chaosx.nr12.43` for Honeyguide aid routes, and `chaosx.nr12.44` for Great Herds relief columns. The decisions save the targeted actor as `africa_bestiary_actor_target` before firing the event, so the event text names the actor without converting the report into a super-event or final quote package.

Remaining Bestiary risks: these are one-step action reports. They do not yet create disaster chains, map incidents, foreign-holder responses, or route-specific variant super-events.

## Parent Follow-Up: 2026-06-17 Expanded Bestiary Actor Action Cleanup

The follow-up decision audit found that the five expanded actor-side one-time flags could survive a reseed/reset while the unifier-side Bestiary action counter was cleared. `common/scripted_effects/012_africa_effects.txt` now defines `africa_clear_bestiary_actor_action_flags` and calls it from the runtime and establishment reset scans, plus the Authority Atlas progress cleanup loop when Charter member arrays still point at high-chaos actors. This clears `africa_chimpanzee_telegraph_relays_tasked`, `africa_okapi_shadow_dossiers_requested`, `africa_termite_citadel_engineers_commissioned`, `africa_honeyguide_commons_aid_routes_open`, and `africa_great_herds_relief_columns_mustered` alongside the existing Bestiary cleanup.

Remaining Bestiary risks: AI weights for the expanded actor actions are still shallow flat weights, and the timed decisions still apply costs/rewards in `complete_effect` rather than becoming true delayed missions.
