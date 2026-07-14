# Event 015 Utopia Manifesto decision implementation handoff

## Status and ownership

The Event 015 decision surface is implemented across the following decision-subagent-owned files:

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/decisions/categories/015_utopia_manifesto_categories.txt`
- `common/scripted_effects/015_utopia_manifesto_decision_effects.txt`
- `common/script_constants/015_utopia_manifesto_decision_constants.txt`

This handoff is the fifth owned file. No other gameplay, localisation, interface, asset, event, focus, identity, on-action, or spreadsheet file was edited by this subagent. The work has not been staged or committed; the parent agent owns final integration, review, audit, and commit.

The implementation contains 9 decision categories, 97 player/AI decisions, and 31 timed missions. It covers the accepted decision and mission matrices from first survey through post-formation institutional maintenance. Every launch decision has an explicit `ai_will_do` block. Missions use dynamic variable durations and explicit activation, cancellation, completion, and timeout behavior.

## Implementation outcome

- The Ledger is an actual resource-and-proof system: survey, accounts, stores, reserve pressure, callings, property, districts, and the island all feed existing Event 015 kernel helpers.
- Every project consumes political, material, manpower, stability, experience, command, or institutional capacity appropriate to its subject. The store system is not political-power-only.
- Project lengths are computed by the shared duration wrapper and stored in ordinary variables before `days_mission_timeout` is read.
- State projects use targeted state decisions and state flags. Necessary Ground, stewardship, and League diplomacy use targeted country decisions and the kernel's array-backed scope contracts.
- No decision grants free cores, claims, owned states, divisions, or equipment. Coercive Necessary Ground advances through the existing case/enforcement contract rather than direct territorial effects.
- No daily, weekly, monthly, or world-iteration on action was added.
- Guardians route failures now have playable consequences and paid correction paths: Productive Tenure failure creates the data scandal; district failure creates the assignment revolt; neither clears itself for free.
- Formation is split into a long proof mission and a separate proclamation. The proclamation uses the route-aware identity dispatcher as its only formation writer call.

## Category surface

| Category | Purpose |
| --- | --- |
| `utopia_manifesto_ledger_category` | Survey, accounts, stores, reserve, callings, second trade, short day, and property transition |
| `utopia_manifesto_district_category` | State survey, district role, construction, and charter |
| `utopia_manifesto_island_category` | Geography selection and staged island project |
| `utopia_manifesto_necessary_ground_category` | Target selection, domestic alternatives, active case, bilateral offer, enforcement, and renunciation |
| `utopia_manifesto_stewardship_category` | Provision, route restoration, charter, status, autonomy, return, integration, and revolt cleanup |
| `utopia_manifesto_league_category` | League initialization, aid, technical missions, reserve compact, membership, legitimacy, defense, sponsorship, and expulsion |
| `utopia_manifesto_defense_category` | Store guard, citizen watch, engineers, auxiliary contract, and demobilization |
| `utopia_manifesto_governance_category` | Constitutional correction and route-specific repair actions, including the two Guardians incidents |
| `utopia_manifesto_formation_category` | Proof mission, route-aware proclamation, and three post-formation actions |

## Mapped-family coverage

| Accepted family | Implemented identifiers and behavior | Event hooks |
| --- | --- | --- |
| National survey and accounts | `decision_utopia_count_houses_and_hands`, `mission_utopia_count_houses_and_hands`, `decision_utopia_recount_the_country`, `decision_utopia_publish_the_accounts`; survey success/failure, repeat recount, and timed account-publication cooldown | `.3` |
| Common stores and reserve | `decision_utopia_establish_capital_store`, `mission_utopia_establish_capital_store`, `decision_utopia_fill_seasonal_reserve`, `mission_utopia_fill_seasonal_reserve`, `decision_utopia_rotate_old_stores`, `decision_utopia_release_emergency_stores`, `decision_utopia_two_years_against_hunger`, `mission_utopia_two_years_against_hunger`; paid rolling reserve, emergency withdrawal, and two-year proof | `.5`, `.30`, `.31`, `.32` |
| Six Callings | Six selectors: provisioning, workshops, civic works, learning and care, maritime and settlement, defense and watches. Four response methods: `decision_utopia_issue_open_call`, `decision_utopia_guarantee_placement`, `decision_utopia_set_assignment_quota`, `decision_utopia_emergency_calling_levy`; shared `mission_utopia_fill_unpopular_calling` | `.6`, `.20`, `.21`, `.22` |
| Second trade and short day | `decision_utopia_learn_second_trade`, `mission_utopia_learn_second_trade`, `decision_utopia_suspend_the_short_day`, `mission_utopia_short_day_suspension`; explicit success and terminal cleanup | `.23` |
| Property transition | `decision_utopia_register_public_land`, `mission_utopia_register_public_land`; estate-to-land-trust, factory-to-worker-council, Productive Tenure, and idle-grant revocation project decisions; shared `mission_utopia_property_transition` | route proofs; Productive Tenure failure feeds `.91` correction surface |
| District survey and roles | `decision_utopia_survey_district_site`, `mission_utopia_survey_district_site`; market garden, industrial housing, rail junction, and refugee municipality roles; `mission_utopia_build_garden_district`; `decision_utopia_complete_district_charter`; `mission_utopia_complete_district_charter` | `.40`, `.41`, `.42`, `.43` |
| Island geography | `decision_utopia_prepare_national_island_variant`; existing island capital, coastal refuge, and Inland Island selectors; paid site, harbor or inland terminal, capital provision ring, open fortification or closed gates; `mission_utopia_build_island_stage`; `decision_utopia_make_an_island`; `mission_utopia_make_an_island` | `.44` for Inland Island; route/geography proof for other variants |
| Necessary Ground target and case setup | `decision_utopia_select_necessary_ground_target`, `decision_utopia_clear_necessary_ground_target`, `decision_utopia_survey_domestic_alternatives`, `mission_utopia_survey_domestic_alternatives`, `decision_utopia_draft_need_case`, `decision_utopia_select_need_case_state`, `mission_utopia_need_case_expiry` | `.8`, `.50`, `.51`, `.53`, `.54` |
| Bilateral Necessary Ground methods | Purchase, long supply contract, lease, joint administration, associate municipality, `mission_utopia_wait_for_need_answer`, revised offer, ultimatum, enforcement, direct renunciation, lease conversion, and joint-administration conversion | `.52`, `.55`, `.200`, `.201`, `.202`, `.203`, `.204` |
| Stewardship | Confirmation, emergency provision and mission, route restoration and mission, local charter, Assigned Colony, charter period and mission, status vote, autonomy, return, long integration and mission, and paid revolt cleanup | `.9`, `.60`, `.61`, `.62`, `.63`, `.64` |
| League of Places | Initialization, surplus abroad, technical mission and mission, reserve compact and answer mission, League invitation and answer mission, legitimacy proof mission, reconstruction brigade pool, mutual defense council, sponsorship, and exploitative-member expulsion | `.70`, `.71`, `.72`, `.73`, `.74`, `.210`, `.211` |
| Defense and paid growth | Store guard and mission, citizen watch and mission, engineer companies and mission, one-time paid auxiliary contract, paid demobilization and mission | `.80`, `.81`, `.82`, `.83`, `.84` |
| Route governance | Constitutional correction and mission; household referendum, Calling councils, forecast, service register, and sunset-clause corrections | `.90`, `.91`, `.92`, `.93`, `.94`, `.95` |
| Guardians incidents | `decision_utopia_publish_corrected_tenure_tables` is the sole paid clear for `utopia_manifesto_data_scandal`; `decision_utopia_negotiate_district_appeals` is the sole paid clear for `utopia_manifesto_assignment_revolt` | `.91` / `.93` correction narrative |
| Formation and maintenance | `decision_utopia_prove_the_commonwealth`, `mission_utopia_prove_the_commonwealth`, `decision_utopia_proclaim_the_commonwealth`; one-time paid institution, defense, and charter post-formation actions | route-aware identity events and regional proclamation contract |

## Centralized tuning

`common/script_constants/015_utopia_manifesto_decision_constants.txt` contains 135 entries in ten groups:

| Constant group | Entries | Owns |
| --- | ---: | --- |
| `utopia_manifesto_decision_cost` | 33 | Political power, manpower, equipment, trains, convoys, experience, command power, stability, and war-support costs |
| `utopia_manifesto_decision_duration` | 31 | Base and maximum mission durations, war/country-size additions, Ledger reductions, incident delay, and timed-flag cooldowns |
| `utopia_manifesto_decision_change` | 9 | Ledger, reserve, support, cohesion, and project step deltas |
| `utopia_manifesto_decision_value` | 10 | Neutral/default values, counters, offers, provisions, and duration multipliers |
| `utopia_manifesto_decision_threshold` | 7 | State, country, integrity, reserve, and formation thresholds |
| `utopia_manifesto_decision_ai` | 29 | All AI base factors and route/situation modifiers |
| `utopia_manifesto_decision_building` | 2 | District building levels |
| `utopia_manifesto_decision_property_project` | 4 | Property-project enumeration |
| `utopia_manifesto_decision_district_role` | 4 | District-role enumeration |
| `utopia_manifesto_decision_island_stage` | 6 | Island stage enumeration |

The only file-scoped numeric constants are fields that require parse-time literals rather than dynamic `constant:` tokens:

- `@utopia_decision_cooldown_medium` and `@utopia_decision_cooldown_long` are used only by `days_re_enable`. Timed country flags load the equivalent script constant into a temporary variable before passing it to `days =`.
- The nine `@utopia_manifesto_category_priority_*` values are used only by the static category `priority` field.

All gameplay costs, deltas, thresholds, enum values, duration arithmetic, AI factors, and mission timeouts in the owned decision and helper files use script constants. Structural booleans and the engine's structural zero/one forms remain literal where appropriate.

## Mission lifecycle and cleanup

| Mission | Activation/runtime owner | Completion | Cancellation and timeout cleanup |
| --- | --- | --- | --- |
| `mission_utopia_count_houses_and_hands` | `utopia_manifesto_survey_active` | `utopia_manifesto_complete_national_survey` | `utopia_manifesto_fail_national_survey` clears active state and records failure |
| `mission_utopia_establish_capital_store` | `utopia_manifesto_capital_store_project_active` | `utopia_manifesto_complete_capital_store` | `utopia_manifesto_fail_store_project` clears store project runtime |
| `mission_utopia_fill_seasonal_reserve` | `utopia_manifesto_seasonal_reserve_active` | `utopia_manifesto_complete_seasonal_reserve` | Store failure helper clears runtime and records the failed route |
| `mission_utopia_two_years_against_hunger` | `utopia_manifesto_two_year_reserve_active` | `utopia_manifesto_complete_two_year_reserve` | `utopia_manifesto_fail_two_year_reserve` clears active state and writes partial/failure proof |
| `mission_utopia_fill_unpopular_calling` | `utopia_manifesto_calling_mission_active` | `utopia_manifesto_resolve_calling_mission` | `utopia_manifesto_fail_calling_mission` clears the current Calling runtime |
| `mission_utopia_learn_second_trade` | `utopia_manifesto_second_trade_active` | Clears active state and records training completion | Cancel and timeout both clear active state and record failure |
| `mission_utopia_short_day_suspension` | `utopia_manifesto_short_day_suspended` | Clears suspension and records the completed shift | Cancel and timeout clear the suspension and record failure |
| `mission_utopia_register_public_land` | `utopia_manifesto_property_register_active` | Clears active state and records the register | Cancel and timeout clear active state and record register failure |
| `mission_utopia_property_transition` | Country `utopia_manifesto_property_project_active`; selected state carries the property-project flag | `utopia_manifesto_complete_property_transition` clears country/state runtime | `utopia_manifesto_fail_property_transition` clears runtime; Productive Tenure failure also sets `utopia_manifesto_data_scandal` |
| `mission_utopia_survey_district_site` | Country `utopia_manifesto_district_survey_active`; selected state carries survey state | `utopia_manifesto_complete_district_survey` | `utopia_manifesto_fail_district_project` clears country/state runtime; Guardians failure also sets `utopia_manifesto_assignment_revolt` |
| `mission_utopia_build_garden_district` | Country `utopia_manifesto_district_build_active`; selected state carries role/project state | `utopia_manifesto_complete_district_build` | District failure helper clears country/state runtime and records the route failure |
| `mission_utopia_complete_district_charter` | Country `utopia_manifesto_district_charter_active`; selected state carries charter state | `utopia_manifesto_complete_district_charter` | District failure helper clears country/state runtime |
| `mission_utopia_build_island_stage` | Country `utopia_manifesto_island_project_stage_active`; project state carries stage state | `utopia_manifesto_complete_island_stage` | `utopia_manifesto_fail_island_stage` clears country/state stage runtime |
| `mission_utopia_make_an_island` | `utopia_manifesto_make_island_mission_active` | `utopia_manifesto_complete_make_island` | `utopia_manifesto_fail_make_island` clears active state and writes failure proof |
| `mission_utopia_survey_domestic_alternatives` | `utopia_manifesto_domestic_alternative_survey_active` | `utopia_manifesto_resolve_domestic_alternative_survey` | Failure helper clears active state and records inadequate preparation |
| `mission_utopia_need_case_expiry` | `utopia_manifesto_need_case_active`; duration is the kernel case expiry variable | Finishes after the case is cleared and removes any response-active flag | Cancel expires the active case; timeout fires `.54`, expires the case, clears response state through the case contract, and clears the selected country target |
| `mission_utopia_wait_for_need_answer` | `utopia_manifesto_case_response_active`; target must still be the selected country | Clears response state; a counteroffer also fires `.52` | Cancel clears response state; timeout clears response state and records refusal without inventing territorial effects |
| `mission_utopia_emergency_provision` | `utopia_manifesto_stewardship_provision_active` | `utopia_manifesto_complete_stewardship_provision` | Cancel/timeout fail the project; invalidated obligation also triggers stewardship revolt cleanup |
| `mission_utopia_restore_stewardship_route` | `utopia_manifesto_stewardship_route_active` | `utopia_manifesto_complete_stewardship_route` | `utopia_manifesto_fail_stewardship_project` clears all stewardship project-active flags |
| `mission_utopia_hold_charter_period` | `utopia_manifesto_stewardship_charter_period_active` | Records the completed charter period and refreshes proof | Cancel/timeout fail the project and trigger the revolt contract where the obligation survives |
| `mission_utopia_long_integration` | `utopia_manifesto_stewardship_integration_active` | Records peaceful-case evidence before `utopia_manifesto_integrate_stewardship` clears the central target/case runtime | Cancel/timeout fail the project and trigger the revolt contract; no stale active-case pointer remains |
| `mission_utopia_technical_mission` | Root `utopia_manifesto_technical_mission_active`; target `utopia_manifesto_technical_mission_host` | Both root and target flags clear after resolution | Both flags clear on cancel and timeout |
| `mission_utopia_reserve_compact_answer` | Root `utopia_manifesto_reserve_compact_pending`; target `utopia_manifesto_reserve_compact_invited` | Clears both transient flags; accepted compact refreshes League achievement proof | Cancel clears both; timeout clears both and records target refusal |
| `mission_utopia_league_invitation_answer` | Root `utopia_manifesto_league_invitation_pending`; target `utopia_manifesto_league_invited` | Clears both transient flags and refreshes League achievement proof | Cancel clears both; timeout clears both and records target refusal. Historical member/refusal arrays remain intentionally persistent |
| `mission_utopia_prove_league_not_mask` | `utopia_manifesto_league_legitimacy_mission_active` | Completes legitimacy proof | Failure helper clears active state and records League failure |
| `mission_utopia_guard_the_common_stores` | `utopia_manifesto_store_guard_mission_active` | Records completed store defense | Failure helper clears active state and records store-defense failure |
| `mission_utopia_raise_a_citizen_watch` | `utopia_manifesto_citizen_watch_training_active` | Records trained citizen watch | Cancel/timeout clear training and record understrength/wasted-training proof |
| `mission_utopia_form_engineer_companies` | `utopia_manifesto_engineer_company_training_active` | Records formed engineers and defense proof | Cancel/timeout clear training and record limited-cadre outcome |
| `mission_utopia_end_the_auxiliary_contract` | `utopia_manifesto_auxiliary_demobilization_active` | Clears contract/dependency and records successful demobilization | Cancel/timeout clear demobilization-active state, leave the underlying contract active, and set the betrayal/failure outcome |
| `mission_utopia_constitutional_correction` | `utopia_manifesto_constitutional_correction_active` | A route correction decision calls the common completion helper and removes the mission | Cancel/timeout call the common failure helper and clear active correction state |
| `mission_utopia_prove_the_commonwealth` | `utopia_manifesto_formation_proof_mission_active` | Refreshes canonical proof and records full or partial formation evidence | Cancel/timeout clear active proof state and set failure proof; they do not form the country |

## Target and state lifecycle

### Necessary Ground

1. `decision_utopia_select_necessary_ground_target` calls `utopia_manifesto_save_from_as_selected_country_target`. The kernel clears any prior target, saves the selected country's ID, inserts that scope into `utopia_manifesto_selected_country_targets`, and marks the foreign country with `utopia_manifesto_selected_country_target`.
2. `decision_utopia_draft_need_case` calls `utopia_manifesto_open_need_case_against_from`. The kernel enforces one active case, writes the target ID/family/stage/method/expiry and integrity/support counters, inserts the target into `utopia_manifesto_active_case_targets`, and marks it with `utopia_manifesto_active_case_target`.
3. `decision_utopia_select_need_case_state` calls `utopia_manifesto_set_from_state_as_case_state`. The kernel clears any prior case state, writes the state ID, inserts it into `utopia_manifesto_active_case_states`, and marks it with `utopia_manifesto_active_case_state`.
4. Offer decisions write exactly one active offer family, call `utopia_manifesto_record_case_offer`, set `utopia_manifesto_case_response_active`, and activate the answer mission. Bilateral events use the existing accept/refuse/counteroffer helpers; the mission always clears the response-active flag at its terminal path.
5. A consensual settlement calls `utopia_manifesto_start_stewardship_from_active_case`; the target and state remain live while provision, route, charter, vote, autonomy/return, or integration are evaluated.
6. Return and integration record external-case proof before the kernel clears stewardship variables, target/state arrays, foreign flags, case IDs, and case runtime. Revolt copies the target to `utopia_manifesto_stewardship_revolt_target` before the same central cleanup. Expiry/renunciation also use the central case cleanup rather than removing individual pointers ad hoc.
7. `decision_utopia_clear_necessary_ground_target` is available only outside active response/stewardship states and calls the central selected-target cleanup.

### State projects

- Property, district, and island selectors set both a country-side active flag and a state-side project/stage flag.
- Their common completion/failure helpers iterate the owned state arrays/flags and clear the active state marker at every terminal path.
- The state role or completed-project proof remains only where it is historical formation evidence; active/survey/construction markers do not persist.

### League targets

- Technical-mission host, reserve-compact invite, and League-invitation pending flags are transient and clear on success, cancellation, and timeout.
- League member, refusal, sponsor, aid, reserve-contributor, defense-partner, and exit arrays/flags are historical/runtime network state owned by the central League kernel and intentionally survive a single answer mission.
- `utopia_manifesto_clear_league_runtime` remains the terminal cleanup owner for all League arrays, foreign flags, counters, and external-network state.

## Canonical formation behavior

Formation has one deliberate call path:

1. `decision_utopia_prove_the_commonwealth` starts the dynamically timed proof mission.
2. `mission_utopia_prove_the_commonwealth` calls `utopia_manifesto_complete_formation_proof`, which only refreshes formation proof and writes `utopia_manifesto_formation_proven` or partial proof. It does not form or rename the country.
3. `decision_utopia_proclaim_the_commonwealth` rechecks `utopia_manifesto_can_form_current_route` and calls only `utopia_manifesto_form_current_route_identity = yes`.
4. The identity dispatcher is therefore the sole decision-owned formation call and remains responsible for route identity plus the central `utopia_manifesto_complete_formation` writer. The decision file does not call `utopia_manifesto_complete_formation` directly.
5. Successful proclamation records crisis-recovery evidence, then marks the formation transition complete when the central formed flag exists.
6. Post-formation institution, defense, and charter decisions are paid, one-time actions and refresh relevant proofs. None is a second formation writer.

## Event-hook map

| Event | Decision/mission use |
| --- | --- |
| `chaosx.nr15.3` | National survey completion |
| `.5` | Capital store completion |
| `.6` | First Calling shortage |
| `.8` | First external Necessary Ground case |
| `.9` | First stewardship obligation |
| `.20`, `.22` | Calling method/failure outcomes |
| `.21` | Surplus-gift route |
| `.23` | Second-trade outcome |
| `.30`, `.31`, `.32` | Seasonal/two-year reserve route outcomes |
| `.40`, `.41`, `.42`, `.43` | District role/charter/failure outcomes |
| `.44` | Inland Island |
| `.50` | Necessary Ground state selection |
| `.51` | Domestic-alternative result |
| `.52` | Revised/counter offer |
| `.53` | First local petition |
| `.54` | Case expiry |
| `.55` | Enforcement |
| `.60`, `.61`, `.62`, `.63`, `.64` | Provision, Assigned Colony, charter, status vote, and stewardship failure/revolt |
| `.70`, `.71`, `.72`, `.73`, `.74` | League invitation, reserve compact, sponsor, expulsion, and legitimacy failure |
| `.80`, `.81`, `.82`, `.83`, `.84` | Store guard, watch/engineers, auxiliary hire, auxiliary incident/demobilization, and failed demobilization |
| `.90`, `.91`, `.92`, `.93`, `.94`, `.95` | Correction failure and five route/incident correction outcomes |
| `.200`, `.201`, `.202`, `.203`, `.204` | Purchase/long supply, lease, joint administration, association, and ultimatum bilateral handling |
| `.210`, `.211` | League invitation and reserve-compact bilateral handling |

All 51 distinct event references in the decision file resolve to definitions in the repository at handoff time.

## Guardians incidents

- `utopia_manifesto_fail_property_transition` checks the selected property-project enum. A failed Productive Tenure project sets `utopia_manifesto_data_scandal`.
- `utopia_manifesto_fail_district_project` checks the active Guardians route. A failed district project sets `utopia_manifesto_assignment_revolt`.
- `utopia_manifesto_data_scandal` clears only through the paid `decision_utopia_publish_corrected_tenure_tables`, which calls `utopia_manifesto_resolve_data_scandal` and records a resolved flag.
- `utopia_manifesto_assignment_revolt` clears only through the paid `decision_utopia_negotiate_district_appeals`, which calls `utopia_manifesto_resolve_assignment_revolt` and records a resolved flag.
- Both resolution helpers refresh Ledger/formation state after applying their paid institutional correction. There is no silent or automatic clear.

## Achievement and proof recorder dependencies

### Recorder calls owned by this decision implementation

- Emergency store release and completed stewardship provision call `utopia_manifesto_record_achievement_common_use_financed_provision`.
- Non-emergency assignment quota calls `utopia_manifesto_record_achievement_assignment_overreach`.
- Direct renunciation of a resolved Need sets the obsolete-case evidence and calls `utopia_manifesto_record_achievement_obsolete_case_renunciation` before central case cleanup.
- Long integration calls `utopia_manifesto_record_achievement_peaceful_case_resolution` before integration clears the active target.
- Autonomy/return calls `utopia_manifesto_record_stewardship_return_achievement_evidence`, which sets retained-autonomy evidence and calls both peaceful-case and status-vote recorders before central cleanup.
- Reserve compact, League invitation, and mutual-defense completion refresh `utopia_manifesto_refresh_achievement_league_proofs`.
- Auxiliary contract success calls `utopia_manifesto_record_achievement_auxiliaries_hired` as a conduct disqualifier.
- Constitutional correction completion and successful proclamation call `utopia_manifesto_record_achievement_crisis_recovery`.

### External call sites still owned by event/identity/integration work

- The `.51` domestic-substitution event option must call `utopia_manifesto_record_achievement_peaceful_case_resolution` before `utopia_manifesto_renounce_active_need_case`, because the latter clears the case pointer.
- The `.54.a` expiry/obsolete-case option must call `utopia_manifesto_record_achievement_obsolete_case_renunciation` after it establishes obsolete-case evidence and before the case is cleared.
- District role outcomes in `.40` through `.43` must call `utopia_manifesto_refresh_achievement_planned_district_proof` after their country-side role flags are written.
- `utopia_manifesto_record_achievement_callings_sustained` still needs a genuine long-duration Calling challenge owner. No accepted decision-matrix row established such a long challenge, so this subagent did not manufacture a one-click substitute.
- War, annexation, stronger-attacker, closed-major-war, reserve-under-war, inland-supply-under-war, early-coast, and unrelated territorial lifecycle recording belongs to parent-owned on-actions/identity integration. This decision implementation deliberately does not duplicate those recorders.

### Exposed reserve, inland, defense, and League state

- Reserve: `utopia_manifesto_two_year_reserve_complete`, `utopia_manifesto_two_year_reserve_partial`, central `utopia_reserve_score`, and the existing reserve-band flags.
- Inland Island: `utopia_manifesto_achievement_inland_island_path`, `utopia_manifesto_inland_terminal_complete`, `utopia_manifesto_island_project_complete`, and event-owned `utopia_manifesto_inland_island_rail_ring`.
- Store/watch/engineers: `utopia_manifesto_store_guard_complete`, `utopia_manifesto_store_guard_failed`, `utopia_manifesto_citizen_watch_trained`, `utopia_manifesto_citizen_watch_understrength`, `utopia_manifesto_citizen_watch_training_wasted`, `utopia_manifesto_engineer_companies_formed`, `utopia_manifesto_engineer_defense`, and `utopia_manifesto_engineer_cadres_limited`.
- Auxiliary conduct: contract-active/dependency, hired, demobilized, failed-demobilization, and betrayal flags; hire also writes the explicit achievement disqualifier through the recorder.
- League: central member, aid, reserve, defense, refusal, exit, and external-network counters; foreign member/reserve-contributor/defense-partner flags; decision-owned compact/invitation/defense outcomes call the League proof refresher.

## Validation evidence

- The owned decision file contains 97 decisions and 31 missions. All 97 decisions have explicit AI blocks. All 31 missions have activation, variable timeout, cancel trigger, cancel effect, and completion/timeout behavior.
- All `utopia_manifesto_* = yes/no` scripted calls from the owned files resolve to repository definitions at handoff time.
- All 51 referenced Event 015 event IDs resolve to existing event definitions.
- The proclamation decision has exactly one formation call: `utopia_manifesto_form_current_route_identity`. There is no direct decision call to `utopia_manifesto_complete_formation`.
- Targeted League answer missions clear their root and target transient flags on all terminal paths. Central case/stewardship helpers own case target cleanup; property, district, and island helpers own state project cleanup.
- The implementation contains no direct core, claim, ownership, annexation, unit-creation, or equipment-grant shortcut.
- Tunable gameplay numerics in the owned decision and helper surfaces resolve through script constants, except the explicitly documented parse-time static fields.

## Simplifications, omissions, and blockers

No fallback or simplification was used in the owned decision implementation. All accepted decision and mission families were implemented, including paid Guardians incident correction, all geography variants, all Necessary Ground methods, League and defense branches, route correction, canonical formation, and post-formation actions.

The achievement event call sites listed above are cross-owner integration dependencies, not substitute behavior in the decision implementation. Localisation, event text, focus/event identity wiring, assets, event-log/details/spreadsheet alignment, and the final audit are parent/other-subagent surfaces and must be complete before the overall Event 015 goal can be claimed complete.

## Skills and references used

- `chaos-redux-subagents` for ownership boundaries and handoff obligations.
- `hoi4-decisions-missions` for targeted-decision, mission-lifecycle, dynamic-duration, AI, and cleanup rules.
- Required offline Paradox wiki core pages, relevant vanilla documentation, and vanilla decision/mission precedents were consulted before editing. No online Paradox wiki was used.

