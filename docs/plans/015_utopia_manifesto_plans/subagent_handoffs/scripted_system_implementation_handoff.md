# Event 15 Scripted-System Implementation Handoff

## Status and ownership

The Event 15 helper kernel is implemented in the following parent-owned, uncommitted files:

- `common/script_constants/015_utopia_manifesto_constants.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`

No gameplay file outside those three files was edited by the scripted-system subagent. The parent agent owns final integration, review, and commit.

The implementation used the `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, and `chaos-redux-mtth` skills. The required offline wiki core pages and the relevant vanilla documentation for effects, triggers, script constants, event targets, events, decisions, focuses, AI, scopes, localisation, and on actions were consulted before implementation.

## Implemented kernel

### Conservative candidate selection

- `utopia_manifesto_automatic_event_is_available` exposes whether at least one automatic candidate exists.
- `utopia_manifesto_prepare_random_event_fire` builds three ordered weighted ticket pools and selects one actor.
- Selection outputs:
  - temporary `utopia_manifesto_prefire_ready`, set to `1` only after successful selection;
  - temporary `utopia_manifesto_prefire_candidate_class`;
  - regular event target `utopia_manifesto_prefire_actor`, for the current firing chain;
  - global event target `utopia_manifesto_latest_actor`, retained as the latest historical actor for log integration.
- Class priority is human generic, AI generic, then approved registry. Class 3 is intentionally empty until an approved registry is supplied; it has no generic fallback.
- Absolute automatic gates exclude majors, terminal identities, protected packages, mature/non-generic trees, civil wars, offensive wars, unsafe capitals, faction leaders, heavy industry, subject empires, and extensive occupation.
- Subjects are admitted only when they have no subjects of their own, low occupation, a secure capital, and a valid ordinary overlord relationship.
- `utopia_manifesto_manual_event_is_available`, `utopia_manifesto_manual_override_boundary_is_safe`, and `utopia_manifesto_strong_manual_override_boundary_is_safe` provide explicit manual boundaries without weakening automatic selection.
- `utopia_manifesto_refresh_candidate_unavailability_reason` writes one primary diagnostic reason flag or `utopia_manifesto_candidate_available`.

### Four-value Ledger and callings

The only public Ledger values are:

- `utopia_need`
- `utopia_plenty`
- `utopia_concord`
- `utopia_assignment`

Each value is initialized dynamically, clamped, assigned one of five bands, and accompanied by source breakdown variables. Reserve strength has six bands. The retired consent/surplus/overreach/vocation/foreign-suspicion model does not appear in the kernel.

Public Ledger effects:

- `utopia_manifesto_initialize_ledger`
- `utopia_manifesto_refresh_ledger`
- `utopia_manifesto_apply_prepared_ledger_delta`

`utopia_manifesto_apply_prepared_ledger_delta` accepts temporary inputs `utopia_manifesto_need_delta`, `utopia_manifesto_plenty_delta`, `utopia_manifesto_concord_delta`, and `utopia_manifesto_assignment_delta`; omitted inputs default to zero. It records the last delta and refreshes all bands.

Six calling families and their methods are centralized under script-constant enums. Public calling effects are:

- `utopia_manifesto_initialize_callings`
- `utopia_manifesto_refresh_calling_state`
- `utopia_manifesto_apply_prepared_calling_change`

The prepared calling effect accepts temporary `utopia_manifesto_calling_family_input`, `utopia_manifesto_calling_severity_delta`, and optional `utopia_manifesto_calling_method_input`.

### Routes, geography, and decision phase

Canonical route setters are:

- `utopia_manifesto_set_consent_of_households_route`
- `utopia_manifesto_set_common_table_route`
- `utopia_manifesto_set_guardians_of_measure_route`
- `utopia_manifesto_set_closed_island_route`
- `utopia_manifesto_set_joke_understood_route`

The first four permit a route change only from unresolved state, idempotently to the same route, or during an active constitutional crisis. Joke Understood uses `utopia_manifesto_can_reveal_joke_understood`; it supports unresolved revelation or a humane crisis correction from Consent, Common Table, or Guardians when exact-obedience/coercive conduct has not been adopted.

`utopia_manifesto_prepare_island_variant` writes exactly one of:

- `utopia_manifesto_geography_existing_island`
- `utopia_manifesto_geography_coastal_island`
- `utopia_manifesto_geography_inland_island`

It prioritizes an island capital, then a coastline, then the Inland Island variant. The corresponding enum is stored in `utopia_manifesto_geography_variant`.

`utopia_manifesto_set_decision_phase` accepts temporary `utopia_manifesto_decision_phase_input`, clamps it to the declared enum, and advances monotonically. Separate unlock effects exist for calling, reserve, district, Necessary Ground, stewardship, league, and formation decisions.

### Focus-facing proof API

The focus tree may rely on these public triggers:

- `utopia_manifesto_need_is_high`
- `utopia_manifesto_plenty_is_low`
- `utopia_manifesto_concord_is_low`
- `utopia_manifesto_can_adopt_short_workday`
- `utopia_manifesto_can_secure_two_year_reserve`
- `utopia_manifesto_has_exportable_surplus`
- `utopia_manifesto_island_project_proof_met`
- `utopia_manifesto_has_valid_auxiliary_source`
- `utopia_manifesto_has_valid_escalation_case`
- `utopia_manifesto_has_eligible_league_partner`
- `utopia_manifesto_has_defense_compact_partner`
- `utopia_manifesto_has_meaningful_external_network`
- `utopia_manifesto_can_take_coercive_need_fork`
- `utopia_manifesto_has_resolved_first_need_case`
- `utopia_manifesto_has_valid_associate_network`
- `utopia_manifesto_has_stewardship_obligation`
- `utopia_manifesto_stewardship_charter_period_met`
- `utopia_manifesto_stewardship_status_vote_ready`
- `utopia_manifesto_can_reveal_joke_understood`
- `utopia_manifesto_super_event_network_threshold_met`

`utopia_manifesto_island_project_proof_met` requires a built project, secure capital, prepared geography, and material proof or a secure reserve. It does not consume its own completion flag.

### Necessary Ground and stewardship API

Target selection is array-backed and scope-safe:

- `utopia_manifesto_save_from_as_selected_country_target`
- `utopia_manifesto_clear_selected_country_target`
- `utopia_manifesto_selected_country_target_is_valid`
- `utopia_manifesto_from_is_selected_country_target`

The one-active-case narrative API is:

- `utopia_manifesto_open_need_case_against_from`
- `utopia_manifesto_set_from_state_as_case_state`
- `utopia_manifesto_prepare_case_integrity`
- `utopia_manifesto_apply_prepared_case_local_support_delta`
- `utopia_manifesto_record_case_offer`
- `utopia_manifesto_record_case_counteroffer`
- `utopia_manifesto_accept_case_settlement`
- `utopia_manifesto_refuse_case_settlement`
- `utopia_manifesto_issue_case_ultimatum`
- `utopia_manifesto_enforce_active_need_case`
- `utopia_manifesto_renounce_active_need_case`
- `utopia_manifesto_expire_active_need_case`
- `utopia_manifesto_clear_active_need_case`

Important input contracts:

- Open case: `FROM` is the selected country; optional temporary `utopia_manifesto_case_family_input` and `utopia_manifesto_case_expiry_days_input`.
- Set state: `FROM` is a state controlled by the active case target and not a ROOT core.
- Support delta: temporary `utopia_manifesto_case_local_support_delta`.
- Case method: temporary `utopia_manifesto_case_method_input` before the relevant outcome.
- Offer/counteroffer: optional temporary `utopia_manifesto_case_offer_input`.

Stewardship API:

- `utopia_manifesto_start_stewardship_from_active_case`
- `utopia_manifesto_record_stewardship_provision`
- `utopia_manifesto_record_stewardship_charter`
- `utopia_manifesto_record_stewardship_vote`
- `utopia_manifesto_refresh_stewardship_proof`
- `utopia_manifesto_return_stewardship`
- `utopia_manifesto_integrate_stewardship`
- `utopia_manifesto_trigger_stewardship_revolt`
- `utopia_manifesto_clear_stewardship_runtime`

Provision and vote effects accept temporary `utopia_manifesto_stewardship_provision_input` and `utopia_manifesto_stewardship_vote_support_input`, both defaulting to one. Consensual completion writes the external-case, first-associate, autonomy, and consensual-partner proofs used by formation logic.

### League API

League state is array-backed and idempotently cleaned. Public effects are:

- `utopia_manifesto_initialize_league`
- `utopia_manifesto_invite_from_to_league`
- `utopia_manifesto_add_from_as_league_member`
- `utopia_manifesto_remove_from_league`
- `utopia_manifesto_record_from_league_refusal`
- `utopia_manifesto_record_from_league_aid`
- `utopia_manifesto_record_from_league_reserve_contribution`
- `utopia_manifesto_record_from_league_defense_consultation`
- `utopia_manifesto_record_from_league_sponsor`
- `utopia_manifesto_record_from_league_exit`
- `utopia_manifesto_record_league_failure`
- `utopia_manifesto_apply_prepared_league_cohesion_delta`
- `utopia_manifesto_refresh_league_state`
- `utopia_manifesto_clear_league_runtime`

All country-specific operations use `FROM`. Cohesion change uses temporary `utopia_manifesto_league_cohesion_delta`. Refresh derives `utopia_manifesto_first_associate_recognized`, `utopia_manifesto_small_places_compact`, and `utopia_manifesto_regional_commonwealth` from the network thresholds.

### Formation API

- `utopia_manifesto_refresh_formation_proof` computes the route-specific proof and writes `utopia_manifesto_formation_proof_met` plus `utopia_manifesto_formation_proof_route`.
- `utopia_manifesto_can_form_current_route` exposes the proof as a trigger.
- `utopia_manifesto_complete_formation` is the canonical final writer. It rechecks proof, sets `utopia_manifesto_commonwealth_formed` and `utopia_manifesto_commonwealth_of_places`, and prepares the regional proclamation when the network threshold is met.

Formation consumes the exact focus capstone flags:

- `utopia_manifesto_route_capstone_consent`
- `utopia_manifesto_route_capstone_common_table`
- `utopia_manifesto_route_capstone_guardians`
- `utopia_manifesto_route_capstone_closed_island`
- `utopia_manifesto_route_capstone_joke`

It also consumes the island-project, first-external-case, stewardship, growth, humane/coercive conduct, partner, league, and external-network proof flags declared in the focus/event specifications.

### Settings-aware evolutions

The five exact evolutions are Glosses in the Margin, Necessary Shores, Cities of One Measure, Nowhere Made Law, and Perfect Island.

Prefire behavior:

1. Candidate selection calls `utopia_manifesto_evaluate_prefire_evolutions` in the selected actor scope.
2. That effect rechecks the live evolution setting and persists five actor-country prefire flags.
3. Acceptance calls `utopia_manifesto_consume_prefire_evolution_state`, translating only enabled prefire flags into actor setting-enabled flags.
4. Active evaluation requires those persisted setting-enabled flags and rechecks the current global setting/tier before exposing an evolution as available.
5. `utopia_manifesto_log_prepared_evolution` rechecks the current setting before recording. Disabled stages are not recorded.

Public scheduling/delivery API:

- `utopia_manifesto_evaluate_active_evolutions`
- `utopia_manifesto_schedule_prepared_evolution`
- `utopia_manifesto_validate_scheduled_evolution`
- `utopia_manifesto_clear_scheduled_evolution`
- `utopia_manifesto_apply_glosses_in_the_margin_evolution`
- `utopia_manifesto_apply_necessary_shores_evolution`
- `utopia_manifesto_apply_cities_of_one_measure_evolution`
- `utopia_manifesto_apply_nowhere_made_law_evolution`
- `utopia_manifesto_apply_perfect_island_evolution`

Scheduling accepts temporary `utopia_manifesto_evolution_to_schedule` and optional temporary `utopia_manifesto_evolution_delay_days`. Validation clears a pending evolution whose setting has been disabled and writes diagnostic `utopia_manifesto_evolution_disabled_before_delivery`.

Event-log context uses `events_log_evolution_event_id`, `events_log_evolution_type`, `events_log_evolution_stage`, `events_log_evolution_tier`, `events_log_evolution_actor`, and `events_log_evolution_has_actor`. The actor target is saved and consumed in the same logging effect chain.

### Paid growth

- `utopia_manifesto_refresh_dynamic_costs` computes per-state, per-tier military and institutional costs.
- `utopia_manifesto_can_pay_military_growth` and `utopia_manifesto_can_pay_institutional_growth` expose affordability.
- `utopia_manifesto_apply_paid_military_growth` and `utopia_manifesto_apply_paid_institutional_growth` charge the computed resources and apply the outcome.

All four accept optional temporary `utopia_manifesto_growth_tier_input`, defaulting to one and clamped to one through three. Military growth pays manpower, army experience, infantry equipment, and support equipment before creating capped Household Guard units. Institutional growth pays manpower, political power, and support equipment before applying Ledger benefits. Failed payment sets a diagnostic flag and applies no partial outcome.

### Cleanup

- `utopia_manifesto_clear_all_runtime_state` clears selected targets, the active case, stewardship, league arrays/foreign flags, evolution scheduling, decision unlocks, callings, growth counters/proofs, formation proof/final state, Ledger state, routes, geography, and outcome proofs.
- `utopia_manifesto_enter_disable_safe_state` removes acceptance state, performs the full cleanup, and sets `utopia_manifesto_kernel_disabled`.
- `utopia_manifesto_reject_manifesto` writes rejection and performs the same cleanup.

The global `utopia_manifesto_latest_actor` target is deliberately retained as historical log state until the next successful selection overwrites it.

The engine-created Household Guard division template cannot be safely removed through this kernel. Its `utopia_manifesto_paid_guard_template_created` marker is therefore deliberately retained during cleanup to prevent duplicate template creation if the system is later reactivated. Growth counters and proof flags are cleared, so the retained template is inert.

## Required parent integration

### Formation writer is not yet called

At the time of this handoff, `utopia_manifesto_complete_formation` is the sole writer of `utopia_manifesto_commonwealth_formed`, but no Event 15 event, decision, or focus calls it. The focus tree and regional proclamation event consume that flag. The parent must wire the effect to the successful formation-proof/proclamation transition or establish another deliberate canonical writer.

### Evolution delivery edge

`chaosx.nr15.150` validates a pending stage before scheduling and on each actor pulse. Kernel apply/log effects also recheck the live setting, so disabled stages are not recorded. The delayed event triggers `chaosx.nr15.100` through `.104`, however, currently test only acceptance and local availability. If a setting changes after scheduling and before delivery with no intervening actor pulse, the narrative window can still open, although its stage will not be logged. The parent should add a delivery-time live-setting gate if the window itself must be suppressed.

Do not rely on a regular event target across the delay. The current kernel logs an actor target immediately within the delivery effect chain and is safe on that point.

### Exact unresolved helper-call snapshot

The final cross-file audit found 20 unresolved calls outside the kernel. These are not kernel contracts and were left for their current owners.

Decision file, owned by the decision implementer, who confirmed the recovered draft is being replaced and these calls will be removed or locally defined:

- `common/decisions/015_utopia_manifesto_decisions.txt:54` — `utopia_manifesto_has_storehouse_project_room`
- `common/decisions/015_utopia_manifesto_decisions.txt:63` — `utopia_manifesto_can_pay_storehouse_project`
- `common/decisions/015_utopia_manifesto_decisions.txt:64` — `utopia_manifesto_has_storehouse_project_room`
- `common/decisions/015_utopia_manifesto_decisions.txt:70` — `utopia_manifesto_can_pay_storehouse_project`
- `common/decisions/015_utopia_manifesto_decisions.txt:71` — `utopia_manifesto_has_storehouse_project_room`
- `common/decisions/015_utopia_manifesto_decisions.txt:519` — `utopia_manifesto_has_integration_project_room`
- `common/decisions/015_utopia_manifesto_decisions.txt:528` — `utopia_manifesto_can_pay_integration_project`
- `common/decisions/015_utopia_manifesto_decisions.txt:529` — `utopia_manifesto_has_integration_project_room`
- `common/decisions/015_utopia_manifesto_decisions.txt:535` — `utopia_manifesto_can_pay_integration_project`
- `common/decisions/015_utopia_manifesto_decisions.txt:536` — `utopia_manifesto_has_integration_project_room`
- `common/decisions/015_utopia_manifesto_decisions.txt:710` — `utopia_manifesto_clear_league_aid_targets`

Retired GUI/scripted-localisation calls, owned by the parent and intentionally not restored because they belong to the obsolete meter/action API:

- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt:17` — `utopia_manifesto_apply_petitions_decision`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt:20` — `utopia_manifesto_apply_storehouse_audit_decision`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt:23` — `utopia_manifesto_start_renunciation_vote_mission`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt:43` — `utopia_manifesto_overreach_high`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt:44` — `utopia_manifesto_foreign_suspicion_high`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt:45` — `utopia_manifesto_is_marked_bounds`
- `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt:75` — `utopia_manifesto_can_pay_renunciation_vote`
- `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt:77` — `utopia_manifesto_need_crisis`
- `common/scripted_localisation/015_utopia_manifesto_scripted_localisation.txt:78` — `utopia_manifesto_overreach_high`

`utopia_manifesto_emit_regional_proclamation` is resolved by `common/scripted_effects/015_utopia_manifesto_super_event_effects.txt` and is no longer an unresolved call.

## Validation evidence

- The three kernel files have balanced braces after final cleanup changes.
- The helper kernel defines 198 scripted effects/triggers with no duplicate names inside the owned files.
- All 204 internal helper calls resolve to an owned definition; no internal call is missing.
- All 359 `constant:` references resolve to one of 265 declared Event 15 constants; 195 distinct constants are consumed.
- The owned files contain neither unsupported `<=`/`>=` operators nor retired public-meter tokens.
- The only project-wide duplicate `utopia_manifesto_*` top-level name observed during the snapshot was `utopia_manifesto_ledger_category`, defined both in the active decisions draft and the separate category file. This is outside kernel ownership and should disappear when the decision draft replacement lands.
- Optional Event Chain Viewer lint completed only as a partial whole-project inspection because two sources were skipped and the report contained broad project noise. It did not provide a clean targeted pass and is not treated as completion proof. Artifact: `hoi4-agent://workspace/chaos_redux/artifact/0d0b44caa5b5d819be93f083e22c720bb6be6bac9a24cfa23df09c6d3686c271/381a534f64a9d74642765b001a4dc17753b15f6689dee2806dbc545c1d319eb7/event-lint-b462dc50ad57.json`.

## Simplifications, omissions, and blockers

- No fallback candidate class was introduced. Approved-registry class 3 remains intentionally empty until a real registry is approved.
- No daily, weekly, monthly, or other world-iteration on action was added.
- No gameplay surface outside the constants/triggers/effects kernel was edited.
- The formation call-site and delivery-time evolution-window gate remain parent integration items described above.
- The 20 external unresolved-call locations are owned by the decision implementer or parent and are listed exactly above.
- The Household Guard template remains inert but physically present after terminal cleanup because no safe template-removal contract was introduced.

