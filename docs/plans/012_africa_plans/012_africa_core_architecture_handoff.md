# Event 12 Africa core architecture handoff

Status: implementation contract, not a completion claim. This handoff records the host preflight, persistent state, relationship state machine, action-family runtime, lifecycle hooks, cleanup, and shared-system touchpoints for Event 12. It does not replace the accepted specifications or the decision matrix.

## 1. Accepted boundaries

- Event 12 is the tier-4 Minor Fire-Once entry `chaosx.nr12.1`. It is the required Severe member of the repeatable Formables cluster, stable cluster ID 6. The cluster unlocks at tier 3; the member itself remains unavailable below tier 4.
- Selection is automatic, weighted, African-rooted, and has no human-player preference. If no eligible host exists, nothing is committed and Event 12 remains unfired.
- The opening is protection first. Host selection, a first proof, and protection work precede a Charter, constitutional route, integration, continent formation, or world-order action.
- The selected country remains the host across ordinary tag and cosmetic-tag changes. Its original host identity must also remain separately recorded for achievements and history.
- Relationship state, clauses, confidence, and visible cooperation are authoritative. Opinion is never an integration trigger. Members can refuse, remain autonomous, leave, resist, join a rival bloc, or reach an occupied settlement.
- The seven routes remain Charter Federalism, Continental Republic, Council of Crowns, People's Union, Military Continentalism, Continental Confederation, and the gated Ancestral Covenant/high-chaos route.
- Logged evolutions are I at tier 4, II at tier 5, and III at tier 6. The requested fourth layer is post-unification world-order play, not a duplicate tier-6 evolution row.
- `Africa is one` accepts integrated, autonomous-federal, loyal confederal/chartered, allied restored, and explicitly exempted relationships when their constitutional obligations are settled. It is not an annex-everything check.
- South Africa joining the Allied framework requires its specified civil-war settlement. No branch may bypass that condition.
- There is no Event 12 triggerable scenario. There are no blanket continent-wide cores or war goals.
- No Event 12 `on_daily`, `on_weekly`, `on_monthly`, or equivalent whole-world recurring hook is permitted. A one-shot prefire scan is permitted; a bounded host-owned delayed callback is permitted.
- A missing engine capability is a blocker to raise with the user. Do not silently substitute a weaker decision, static cost, generic host, or legacy faction implementation.

## 2. Host preflight and commit barrier

The live preflight split is sound in principle: `africa_prepare_random_event_fire` performs a one-shot candidate scan, stores the winner as the regular event target `africa_prefire_host`, and the shared dispatcher fires `.1` in that scope. The regular target is correct for this stage because the event is fired from the same effect chain.

The required sequence is:

1. `evaluate_random_event_active_pool_candidate` rejects Event 12 unless tier, cluster, event settings, fire-once state, and `africa_automatic_event_is_available` all pass.
2. `africa_prepare_random_event_fire` clears every temporary preflight array/value, performs one explicit `every_country` scan, and adds only countries satisfying `africa_is_eligible_host`.
3. Candidate weighting is read-only. It may inspect independence, autonomy, colonial war, existing African support, size, surrender progress, neighbours, and isolation, but must not set candidate flags, change diplomacy, or initialize Event 12.
4. The weighted result is saved as regular `africa_prefire_host`; it is revalidated immediately before dispatch. Empty or invalid results leave `africa_prefire_ready = 0`, do not mark Event 12 fired, and do not create a host.
5. `chaosx.nr12.1` must commit in `immediate`, not in the visible option. The dispatcher performs its fire-once bookkeeping after dispatch; initialization therefore cannot depend on a later human click. The option is narrative-only.
6. The idempotent commit effect `africa_initialize_selected_host` revalidates eligibility, saves `africa_host` with `save_global_event_target_as`, sets the active/origin flags, initializes the host ledger, records the original playbook and identity, and schedules only the bounded first-contact callback.
7. The event-log actor mapping must resolve the selected host during that same committed fire. Only after commit can first-proof or Charter content become available.

Commit invariants:

- `africa_event_active`, `africa_unifier_host`, and global `event_target:africa_host` must either all exist and agree or all be absent. Add an `africa_host_commit_completed` country flag and reject a second commit.
- Preserve `africa_origin_host_id`, `africa_origin_host_playbook`, and `africa_host_generation`. Ordinary tag changes do not alter the origin fields. `africa_host_generation` starts at one and increments only during an explicit ownership transfer.
- `africa_baseline_active` cannot be used as proof that initialization completed unless the global host target and commit flag also pass.
- The prefire target is transient and must never be treated as the campaign owner after `.1`. All later content resolves through global `africa_host` plus host-generation checks.
- The current weighted duplicate-scope array technique is acceptable only in this one-shot preflight. It must remain capped by the configured weight bounds and must not be reused in a pulse.

### Explicit host transfer

Tag changes are not transfers. Capitulation is not automatically a transfer. If the host is annexed, ceases to exist, or loses the accepted African-rooted host condition permanently, the lifecycle hook must open an explicit transfer resolution rather than silently picking a generic country.

`africa_begin_host_transfer` should freeze the old host ledger during the valid annex/capitulation callback, copy it to temporary global staging arrays, preserve the origin-host fields, and invalidate outstanding callbacks by incrementing the generation. A valid successor must be an existing chartered/autonomous-federal/integrated country with a mapped overlay and an explicit constitutional or crisis result selecting it. `africa_complete_host_transfer` copies the ledger, updates member reverse links, saves the new global `africa_host`, clears staging, and records the transfer. If no valid successor exists, the system remains in an explicit suspended-host crisis; it must not invent a host or discard obligations.

## 3. State ownership contract

| Scope | Authoritative state | Rule |
| --- | --- | --- |
| Global | `africa_event_active`, `africa_event_resolved`, `africa_is_one`, terminal world-order flags, evolution-history flags, global `africa_host`, temporary host-transfer staging | Global state answers only campaign ownership/history questions. Do not mirror every host variable globally. |
| Host country | route, evolution, host playbook/depth/overlay/support class, Authority, Reach, Burden, Colonial Pressure, supporting measures, caps, action counters, relationship/active-action/project/regional arrays | This is the campaign ledger. A host transfer copies it atomically. |
| Member country | relationship enum, Confidence, host generation, accession-clause flags, obligation flags, integration prerequisites, regional ID, active action ID/generation/status, failure/history flags | Boolean facts use flags. Multi-state facts use enums/variables. |
| State | project ID/status, regional ID, owning action generation, founder/beneficiary reverse arrays, consent/settlement flags | State projects must be discoverable without a world scan. |
| Temporary | candidate weights, computed costs/durations, selected outcome, local loop indexes, transient event targets | Temporary variables are never scope-qualified and never carry delayed state. |

Canonical host arrays should be distinct and deduplicated:

- `africa_relationship_countries`: every country with an Event 12 relationship record.
- `africa_protected_countries`, `africa_associate_countries`, `africa_chartered_countries`, `africa_autonomous_federal_countries`, `africa_integrated_countries`, `africa_resistant_countries`, `africa_leaving_countries`, `africa_rival_bloc_countries`, and `africa_occupied_settlement_countries`: current-state indexes maintained only by the transition effect.
- `africa_active_action_targets`, `africa_active_dossiers`, `africa_living_core_projects`, `africa_active_congress_regions`, `africa_active_obligations`, and `africa_warning_ledger`: bounded work registries.
- Nine regional readiness values must be host-owned, one per accepted overlay. Do not infer regional readiness from a global country scan.

The existing `africa_selected_targets` working roster must not double as the scripted-GUI cursor. The human UI has exactly one selected country at a time, using the Event 15 precedent:

- host variable `africa_selected_country_id`;
- one-entry host array `africa_selected_country_targets`;
- target flag `africa_selected_country_target`;
- `africa_clear_selected_country_target` and `africa_save_from_as_selected_country_target` effects.

Scripted GUI cannot create event targets, so it must use this ID/array/flag contract. AI never depends on this cursor; it scores a bounded eligible target array and calls the same action-start effect.

### Event-target rules

- `africa_prefire_host`: regular event target, prefire chain only.
- `africa_host`: global event target, campaign owner. It must be explicitly cleared at terminal cleanup or replaced during an atomic host transfer.
- `africa_action_target`, `africa_action_secondary_target`, `africa_action_state`, and `africa_action_region`: regular targets only for a single immediate chain.
- Delayed missions/events store target scope in owner arrays plus persistent target flags, action ID, action generation, and host generation. Do not rely on a regular event target surviving a delay.
- Annex callbacks snapshot reverse arrays before clearing them, following the Event 19 cleanup lesson.

## 4. Member relationship state machine

`africa_relationship_state` is the one authoritative ten-state enum. The public entry remains `africa_apply_relationship_transition`; it takes temporary `africa_requested_relationship_state` in member scope. It must be expanded into a validate, unregister, mutate, register, and reconcile transaction.

The complete permitted graph from the accepted diagram is:

- Outside -> Protected, Associate, Rival Bloc, Occupied Settlement.
- Protected -> Associate, Outside, Resistant.
- Associate -> Chartered, Outside, Resistant.
- Chartered -> Autonomous Federal, Integrated Region, Leaving, Resistant.
- Autonomous Federal -> Integrated Region, Leaving, Resistant.
- Integrated Region -> Autonomous Federal, Resistant, or terminal identity cleanup.
- Resistant -> Chartered, Leaving, Rival Bloc, Occupied Settlement.
- Leaving -> Outside, Associate, Rival Bloc, Occupied Settlement.
- Rival Bloc -> Associate, Autonomous Federal, Outside, Occupied Settlement.
- Occupied Settlement -> Integrated Region, Autonomous Federal, Resistant, Outside.

The live helper currently covers only a subset of these edges and only appends to `africa_relationship_countries`. Before decisions depend on it, add the missing accepted edges and the transaction below:

1. Validate the current state, requested edge, current host generation, confidence/consent/route requirements, action capacity, and target existence. Positive opinion is never a validator.
2. Snapshot old state and lifetime evidence. Cancel or resolve actions that are incompatible with the requested state before changing it.
3. Remove the member from the old host state array and clear only state-specific temporary flags. Preserve unrelated clauses, historical proof, and achievement evidence.
4. Set the new enum exactly once. Add the member to `africa_relationship_countries` if absent and to exactly one current-state array.
5. Apply transition-specific clause/obligation changes, update Confidence, recompute host counts/caps/representation/burden, and queue the exact follow-up event.
6. Clear temporary inputs and leave a success result for the caller. A rejected edge changes no persistent state and spends no resources.

Direct integration remains gated by negotiated consent, representation, administrative dossier, transport connection, local settlement, security settlement where required, confidence, route compatibility, and manageable Burden. Occupation never skips those gates. `grant_core_recognition` is a final constitutional review, not a generic core loop.

The Charter relationship enum remains authoritative even if a vanilla faction is later created. Protected and associate countries need not be faction members. Faction join/leave callbacks may reconcile chartered or federal defence obligations, but faction membership can never promote a relationship by itself.

## 5. Parameterized action runtime

All 102 matrix rows use one runtime contract. Do not implement 102 unrelated effects.

### Stable profile and execution kernels

Create `africa_action_id` constants for the matrix row order, 1 through 102. The corrected `africa_action_family` constants are the 14 acceptance families; military is an execution channel, not a fifteenth content family.

Use these execution kernels:

- `instant_bilateral`: immediate guarantee, recognition, clause, treaty, or capstone transaction with cooldown.
- `offer_response`: owner sends a bounded offer; target response, timeout, and withdrawal share one record.
- `timed_country`: country-targeted mission with full, partial, failure, timeout, and cancellation callbacks.
- `state_project`: state/corridor/construction project with founder and beneficiary reverse links.
- `regional_settlement`: congress, claims, restoration, representation, or multi-member constitutional settlement.
- `war_escalation`: deployment, preparation, intervention, blockade, secession, or continent-war state tied to exact wars and participants.
- `special_project`: fictional research, containment, or capped unit creation; no repeat-farming and no real-world pathogen instructions.
- `formation_terminal`: regional/continental/world identity transaction with a preflight and commit barrier.
- `governance_review`: constitutional crisis, sunset, election, succession, loyalty, ratification, or postwar review.

Every decision/event sets a stable action ID and calls the shared sequence:

1. `africa_prepare_action_profile`: load family, kernel, phase, route mask, relationship mask, cost components, duration band, caps, success/partial/failure callbacks, cleanup mode, and AI scoring inputs from constants/profile data.
2. `africa_validate_action`: validate owner, target, host generation, phase, route, relationship, capacity, contradictory offers, exact resources, and anti-farming/cooldown flags.
3. `africa_begin_action`: recompute and clamp dynamic costs, debit once, allocate a monotonically increasing action generation, increment the host active count, create reverse links, and activate the mission/response. Player and AI call this same effect.
4. `africa_resolve_action`: accept only the matching action and host generations; select full, partial, failure, or explicit cancellation; call the matrix-specific payload; then call cleanup.
5. `africa_cleanup_action`: idempotently remove mission/decision state, reverse links, access/deployment/project modifiers, temporary target flags, and active counters. Refunds occur only where the matrix explicitly defines one.

Persistent delayed fields belong on the owner/target: `africa_active_action_id`, `africa_active_action_generation`, `africa_active_action_family`, `africa_active_action_status`, `africa_active_action_host_generation`, and profile-specific stored cost/outcome snapshots. Temporary computed values must never be referenced by a delayed event.

Dynamic costs must use actual equipment, convoys, trains, fuel, manpower, civilian capacity, command/intelligence capacity, access, distance, target scale, route, risk, and obligations named by the matrix. Political power may be one component but cannot turn the system into a PP shop. Costs and durations use centralized constants and must be shown through matching tooltips; start revalidates the displayed values to prevent stale UI. Targeted-decision `target_trigger` runs frequently, so its `target_array` must remain bounded and prefiltered.

### Complete 102-row family map

The numbers below are the decision-matrix row order and become `africa_action_id` values.

**Protection — `africa_action_family.protection`, rows 1-10.** Default kernel is `timed_country`; 1 and 7 use `instant_bilateral`, 4/5/9 use `war_escalation`, and 8 uses `state_project`.

1. `guarantee_sovereignty`
2. `open_aid_corridor`
3. `dispatch_charter_mission`
4. `deploy_volunteers`
5. `intervene_against_coloniser`
6. `evacuate_leaders_archives`
7. `recognise_provisional_government`
8. `secure_border_sanctuary`
9. `break_blockade`
10. `emergency_relief_column`

This family owns first-proof reliability, protection confidence, broken-guarantee memory, rescue/corridor reverse links, and war-end cleanup.

**Accession — `africa_action_family.accession`, rows 11-20.** Rows 11-18 use `offer_response`; 19 uses `timed_country`; 20 is `instant_bilateral` followed mandatorily by `governance_review`.

11. `offer_defence_charter`
12. `offer_development_charter`
13. `offer_federal_charter`
14. `offer_crown_charter`
15. `offer_peoples_charter`
16. `offer_security_charter`
17. `offer_sacred_ecological_compact`
18. `renegotiate_accession_clauses`
19. `hold_accession_referendum`
20. `admit_member_in_emergency`

This family owns one active offer per target, a clause ledger, target consent, response deadlines, mutually exclusive constitutional drafts, and the mandatory postwar review after emergency admission.

**Regional congress — `africa_action_family.regional_congress`, rows 21-30.** The family uses `regional_settlement`; 28/29 add timed support records and 30 may escalate through `war_escalation` only after the settlement path is exhausted.

21. `convene_regional_congress`
22. `settle_overlapping_claims`
23. `create_regional_charter`
24. `form_regional_federation`
25. `restore_historical_polity`
26. `approve_direct_integration_schedule`
27. `guarantee_regional_representation`
28. `fund_congress_security`
29. `invite_diaspora_delegates`
30. `enforce_congress_settlement`

This family owns one active congress per regional overlay, delegates/claimants, settlement version, opt-outs, and a commit barrier for releases or formations.

**Integration — `africa_action_family.integration`, rows 31-40.** Rows 31-37 use `timed_country` or `state_project`; 38 is an `instant_bilateral` capstone after long prerequisites; 39 combines `war_escalation` with a mandatory sunset `governance_review`; 40 is `regional_settlement`.

31. `build_administrative_bridge`
32. `connect_member_capitals`
33. `standardise_customs`
34. `integrate_security_services`
35. `harmonise_officer_corps`
36. `negotiate_autonomy_statute`
37. `launch_local_settlement_programme`
38. `grant_core_recognition`
39. `impose_emergency_administration`
40. `federalise_restored_polities`

This family owns integration-stage prerequisites, reversible autonomy, representation and minority protections, and no direct outside-to-integrated transition.

**Economy — `africa_action_family.economy`, rows 41-50.** Construction rows use `state_project`; policy/institution rows use `timed_country`; the long industrial plan is a staged regional project, never one monolithic timer.

41. `survey_continental_resources`
42. `build_regional_rail_spine`
43. `expand_river_transport`
44. `modernise_continental_port`
45. `create_local_processing_chain`
46. `continental_procurement_contract`
47. `food_security_reserve`
48. `resource_sovereignty_review`
49. `charter_development_fund`
50. `continental_industrial_plan`

This family owns capacity reservations, named corridors/projects, regional contributions, maintenance/suspension, and ecological clauses. No free factories or generic continent modifier substitutes for the projects.

**Diaspora — `africa_action_family.diaspora`, rows 51-58.** Use `instant_bilateral` for opening the registry, `state_project` for housing, and `timed_country` for transport, missions, bonds, representation, and rescue.

51. `open_voluntary_return_registry`
52. `charter_passage_programme`
53. `build_returnee_housing`
54. `invite_afro_american_technical_mission`
55. `veterans_and_volunteers_programme`
56. `diaspora_investment_bonds`
57. `citizenship_and_representation_convention`
58. `diaspora_emergency_evacuation`

This family owns voluntary consent, transport manifests, settlement capacity/trust, one-time veteran cohorts, bond maturity/default state, and local-citizen representation safeguards.

**Rival blocs — `africa_action_family.rival_bloc`, rows 59-66.** Use `timed_country` for networks/negotiation/exit, `governance_review` for suspension and leadership, and `war_escalation` only for an actual secession war.

59. `monitor_rival_bloc`
60. `offer_rival_arbitration`
61. `support_rival_member_defection`
62. `counter_foreign_patronage`
63. `prepare_member_exit_terms`
64. `suspend_disloyal_member`
65. `emergency_leadership_vote`
66. `contain_regional_secession_war`

This family treats a rival bloc as a legitimate African alternative. Peaceful equal-status merger and negotiated exit remain valid outcomes; annexation is not the default cleanup.

**High chaos — `africa_action_family.high_chaos`, rows 67-76.** Diplomacy uses `offer_response`; disaster/disease work uses bounded `timed_country`, `state_project`, or `special_project`; special units are capped `special_project` records.

67. `consult_oracle_network`
68. `bargain_with_the_green`
69. `petition_the_rain`
70. `defy_the_drought`
71. `contain_emergent_disease`
72. `research_disease_countermeasure`
73. `weaponise_fictional_pathogen`
74. `awaken_stone_cohort`
75. `train_gorilla_heavy_infantry`
76. `organise_pan_sappers`

This family remains locked until its accepted chaos/route/actor gates pass. Reuse `call_natural_disaster` and existing disease lifecycle/containment APIs where applicable. Row 73 remains abstract, fictional, consequence-heavy game scripting with no real pathogen procedure. Rows 74-76 need one-time site or capped replacement ledgers, not free-unit loops.

**Scramble response — `africa_action_family.scramble`, rows 77-84.** Diplomatic/economic work uses `timed_country` or `offer_response`; mobilisation and intervention use `war_escalation`; the conference uses `regional_settlement` with global delegates bounded to an explicit list.

77. `seek_international_recognition`
78. `prepare_anti_sanctions_network`
79. `answer_foreign_ultimatum`
80. `mobilise_continental_defence`
81. `disrupt_expedition_planning`
82. `offer_base_withdrawal_treaty`
83. `call_global_anti_colonial_conference`
84. `break_intervention_coalition`

This family owns one crisis/coalition identifier, exact participants, ultimatum deadline, mobilisation state, and demobilisation or war conversion. It must never discover participants through a recurring world scan.

**World order — `africa_action_family.world_order`, rows 85-92.** Sponsorship uses staged `timed_country`; union/identity actions use `formation_terminal`; war uses `war_escalation`; settlement/epilogue uses `governance_review`.

85. `sponsor_continent_unifier`
86. `mediate_continent_union`
87. `prepare_continental_war`
88. `force_continent_submission`
89. `form_dynamic_two_continent_union`
90. `declare_the_world_is_one`
91. `administer_world_regions`
92. `contain_terminal_high_chaos`

This family preserves continent identities and regional systems until a validated formation commit. Terminal cleanup snapshots achievements/history first and shuts incompatible systems explicitly; it does not silently delete surviving high-chaos actors.

**Constitutional route crises — `africa_action_family.constitutional_crisis`, rows 93-99.** All use `governance_review`, parameterized by active route, involved members/regions, crisis severity, and the exact sunset/cancellation condition.

93. `convene_federal_deadlock_conference`
94. `conduct_first_continental_election`
95. `arbitrate_continental_succession`
96. `balance_food_and_industrial_plan`
97. `review_victorious_commander_loyalty`
98. `ratify_confederal_emergency_action`
99. `review_covenant_obligation`

These are required route pressures, not flavour. Each can alter leadership, sovereignty, cohesion, confidence, or route viability and must clean up if the route or subject disappears.

**Post-unification governance — `africa_action_family.post_unification`, row 100.** Use `governance_review`.

100. `hold_postwar_constitutional_review`

This is mandatory after unresolved wartime institutions or emergency admission and pauses during renewed terminal war rather than completing invisibly.

**Host opening — `africa_action_family.host_opening`, row 101.** Use `timed_country` tied to the remembered first-proof target and failure generation.

101. `recover_failed_host_proof`

The recovery cannot erase the original failure, repeat the same impossible target, or grant a normal early mandate after a second failure.

**Regional congress and restorations — `africa_action_family.regional_restorations`, row 102.** Use `regional_settlement` plus `formation_terminal` only when a country release/package activation is actually required.

102. `promote_priority_member_package`

Promotion requires viable territory/autonomy, local support, a functioning institution, distinct strategic/economic play, and an unresolved relationship question. It activates one of the accepted priority packages; it does not bulk-create tags.

## 6. Release, faction, and shared-system contracts

- Rows 25 and 102 and any territorial restoration must use the shared liberation release coordinator in `common/scripted_effects/chaosx_liberation_release_effects.txt`: begin, allocate/reserve, validate, lock, execute, finalize, commit, or rollback. Event 12 supplies candidate/package data and applies the Event 12 relationship only after a verified release. It must not bypass the coordinator with an independent ownership-transfer loop.
- Reuse `call_natural_disaster` from `common/scripted_effects/chaosx_dynamic_effects.txt` for compatible Rain/Drought/disaster calls. If a new genuinely shared dynamic helper is needed, add it there and document it in `chaosx_dynamic_effects.md` in the same future change.
- A Charter military faction is a derived interoperability surface, never the relationship source of truth. If current-version faction templates are used, create them under `common/factions/templates/`, with rules/goals in the corresponding `common/factions/rules/` and `common/factions/goals/` paths. Create the faction only after the Charter formation result, not during host opening.
- The official current faction system and the vanilla Baltic precedent use `create_faction_from_template`. The vanilla precedent contains a DLC/legacy branch; Event 12 must not copy that fallback without explicit user approval. Confirm the mod's supported ownership behavior before wiring the template.

## 7. Lifecycle hooks and bounded scheduling

Create only `common/on_actions/012_africa_on_actions.txt` for Event 12 callbacks. Every body begins with `has_global_flag = africa_event_active` and then checks whether ROOT/FROM/the changed state is the host, a registered relationship country, an active action target, or a reverse-linked project. No body uses `every_country` or `any_country` as a repair scan.

Safe hooks and official scopes:

- `on_war_relation_added`: ROOT attacker, FROM defender. Start/reconcile exact protection, intervention, secession, Scramble, or world-war records.
- `on_war` and `on_peace`: refresh only registered participant actions; cancel war-only preparation and demobilise through explicit resolution.
- `on_capitulation`: ROOT capitulated, FROM winner. Snapshot host/member/action state and schedule the defined result.
- `on_annex`: ROOT winner, FROM annexed. Snapshot reverse links before cleanup; invoke host transfer if FROM is the host; remove or migrate only exact member/project records.
- `on_peaceconference_ended`: ROOT winner, FROM loser. Reconcile exact affected war and territorial projects; do not infer all settlements globally.
- `on_state_control_changed`: use the documented `FROM.FROM` changed-state scope and act only when that state carries an Event 12 reverse link/project flag.
- `on_government_change`: revalidate route/host/member constitutional compatibility without changing relationship state from opinion or ideology alone.
- `on_join_faction` and `on_leave_faction`: ROOT joining/leaving country, FROM faction leader. Reconcile only derived defence obligations and rival-patron state.
- `on_subject_annexed`, `on_subject_free`, and `on_subject_autonomy_level_change`: ROOT subject, FROM overlord. Reconcile sovereignty, release, and accession state.
- `on_puppet`, `on_release_as_free`, and `on_release_as_puppet`: update only exact release/relationship records created by a verified action.

Do not add Event 12 work to `common/on_actions/chaosx_on_actions_system.txt`. Decisions and missions provide their own clocks. If a later asynchronous ledger proves it needs reconciliation that hooks cannot supply, use a hidden host country event such as `chaosx.nr12.900`, guarded by one `africa_host_pulse_scheduled` flag, rescheduled only while the exact host and Event 12 are active, and iterating only bounded host arrays. This is the Event 19 country-pulse pattern, not permission for a world pulse.

## 8. Cleanup contract

Cleanup is explicit and idempotent.

- Action cleanup: verify action and host generations, snapshot the matrix result, call the exact cancellation payload, remove access/units/project modifiers/target flags/reverse links, decrement the active count once, and clear the action record. `remove_mission` does not run completion or timeout effects, so call cleanup before removing it.
- Relationship change: cancel or convert incompatible offers/missions before unregistering the old state; maintain exactly one relationship-state array after the transition.
- Annex/country destruction: snapshot arrays while the callback scopes are valid, then transfer, fail, or cancel each exact record. Never rely on a regular event target in a delayed retry.
- Route change: finish safe committed work, cancel route-exclusive drafts/crises with their defined consequences, and preserve general protection/economic obligations where still valid.
- Host transfer: stage, copy, update reverse links/generation, save the new global target, then clear staging and the old owner flag.
- Event dissolution or terminal world identity: first snapshot event-log/evolution/achievement evidence and permanent map results. Then remove Event 12 decisions, missions, temporary ideas/modifiers/access/guarantees created by the system, selected-target flags, reverse links, action records, work arrays, and the global host target. Preserve permanent constitutional results and recorded history.

Use lifetime evidence flags/arrays for broken guarantees, coercion, peaceful exits, clause breaches, host origin, first-proof result, promotion, and terminal resolution. Do not clear evidence before achievements and log history consume it.

## 9. Exact future file ownership and shared touchpoints

Event-owned implementation files:

- `events/012_african_union.txt`: entry commit, first-proof chain, callbacks, outcomes, evolutions.
- `common/script_constants/012_africa_constants.txt`: shared state enums/caps; add host/action status and generation constants.
- `common/script_constants/012_africa_action_constants.txt`: 102 stable action IDs, cost/duration/profile coefficients.
- `common/scripted_triggers/012_africa_triggers.txt`: host, relationship, route, action, target, and completion gates.
- `common/scripted_effects/012_africa_effects.txt`: host commit/transfer, relationship transaction, value/cap reconciliation.
- `common/scripted_effects/012_africa_action_effects.txt`: profile loader, validation, start, resolve, cleanup, and AI target scoring.
- `common/decisions/categories/012_africa_categories.txt` and `common/decisions/012_africa_decisions.txt`: bounded categories, targeted decisions, missions, and AI.
- `common/on_actions/012_africa_on_actions.txt`: the non-recurring lifecycle hooks above.
- `common/factions/templates/012_africa_faction_templates.txt`, `common/factions/rules/012_africa_faction_rules.txt`, and `common/factions/goals/012_africa_faction_goals.txt`: only if the accepted current faction system is wired.

Narrow shared edits that are safe and required:

- `common/scripted_effects/chaosx_logic_effects.txt`: use `constant:africa_event.id` in event registration; keep the existing active-pool availability gate.
- `common/scripted_effects/chaosx_settings_effects.txt`: keep only Event 12 prefire/host dispatch in `fire_event_by_temp_id_no_cluster`; no Event 12 gameplay belongs here.
- `common/scripted_triggers/chaosx_settings_triggers.txt`: include `constant:africa_event.id` in the normal-event settings classifier.
- `common/script_constants/event_cluster_constants.txt`: set `event_cluster_formables.unlock_tier` to tier 3.
- `common/scripted_effects/chaosx_event_cluster_effects.txt`: retain Event 12 as Formables required, tier 4, Severe, using constants. Do not make the fire-once member repeatable.
- `docs/systems/event_clusters.md`: replace the reserved Formables description and record tier-3 cluster/tier-4 member behavior.
- `common/scripted_effects/chaosx_events_log_effects.txt` plus Event Details/evolution localisation and GUI registries: map Event 12 actor to committed `africa_host`, and register the three logged evolutions.

At the time of the final review, the live active-pool gate, settings classifier, Formables member tier/danger, and `.1` immediate host commit are already correct. The Formables unlock constant and cluster documentation still need alignment.

## 10. Engine uncertainties that must be resolved before dependent content

1. Verify that the dispatcher executes a country event's `immediate` block before shared fire-once history capture. If not, the dispatcher needs an explicit commit acknowledgement before marking Event 12 fired.
2. Verify global event-target and country-array behavior when the host is annexed. The transfer design must be tested in `on_annex`/`on_capitulation`; do not assume an annexed owner retains readable arrays after the callback.
3. Verify which decision duration and dynamic-cost fields accept variables or `constant:` values. If a field rejects them, stop and agree on the UI/runtime representation; do not silently turn a dynamic mission into a static timer or PP cost.
4. Verify country `target_array` behavior for the intended AI decisions and keep it bounded, because `target_trigger` is evaluated frequently. Do not use `state_target = any` for continent-wide discovery.
5. Verify current faction-template availability and ownership/DLC behavior before choosing template creation. No legacy `create_faction` fallback is authorized.
6. Verify annexed-country removal from arrays and duplicate-scope behavior for every persistent registry. All add effects must test non-membership; cleanup must tolerate an already missing scope.
7. Verify the exact scripted-GUI country-selection effect path. The UI must use ID/array/flag storage and cannot call `save_event_target_as`.

## 11. Evidence and precedents inspected

- Entire Event 12 source package: manifest/README, nine specification parts, five diagrams, four acceptance/revision handoffs, decision/AI/host/polity/priority/achievement/focus/asset matrices and notes, prompts, and research/sensitivity records, with the decision matrix treated as the 102-row action authority.
- Offline wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Faction modding.
- Vanilla documentation: decision, on-action, effects, triggers, script concept/script constants, dynamic variables, collections, AI strategy, and current faction documentation.
- Vanilla precedents: `common/decisions/AUS.txt` for bounded `target_array`, timed cancellation, completion/removal separation, and AI; `common/decisions/BALTIC.txt` plus `common/factions/_documentation.md` for faction-template creation and its ownership caveat.
- Chaos Redux precedents: Event 15 selected-country ID/array/flag contract and lifecycle hooks; Event 6 plus `chaosx_liberation_release_effects.txt` for frozen release-plan validation/commit/rollback; Event 19 for host-owned pulses and annex cleanup; `chaosx_dynamic_effects.txt/.md` for shared disaster dispatch; dispatcher, cluster, settings, log, and Event 12 live files.

Validation performed for this handoff: the decision matrix has 102 ordered data rows; the map above accounts for rows 1-102 exactly once across the corrected 14 acceptance families; the relationship graph includes all ten accepted states; and the proposed hooks contain no recurring whole-world on-action.

## 12. Remaining risks and simplifications

This is an architecture handoff, so gameplay, localisation, AI profiles, assets, workbook rows, Event Details, evolutions, and the 102 action implementations remain incomplete. No gameplay simplification or fallback is authorized here. The material risks are host-annex transfer semantics, dynamic decision-field support, current faction-template ownership behavior, and the amount of per-action outcome data still to implement and audit.
