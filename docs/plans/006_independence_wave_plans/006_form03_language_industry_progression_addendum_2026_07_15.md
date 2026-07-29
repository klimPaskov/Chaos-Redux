# Event 6 FORM-03 post-charter progression addendum

Date: 2026-07-15
Status: accepted and source-implemented; live validation and route-readiness evidence remain queued
Scope: `FORM-03`, the `LCX` Confederation of the Low Countries carried by `AFX` or `AGX`
Working labels in this document are not final localisation.

Current disposition (2026-07-29): the `.300-.308` event chain, FORM-03 focus,
decision, idea, modifier, report-art, localisation, and runtime consumers are
implemented in the current tree. The remaining work is bounded validation of
formation reachability, carrier/package admission, save/load, AI, and live
outcomes; this addendum is no longer pending implementation.

## 1. Decision and acceptance status

`FORM-03` already has a valid formation transaction. It must not be redesigned as an annexation formable. The missing requirement is meaningful post-formation play for the registry row's accepted `federal language settlement and industrial integration` obligation.

This addendum defines that play as the **Charter of Languages and Works**, a visible post-charter system with two public values:

- `Federal Accommodation`, stored in `independence_wave_form03_federal_accommodation`
- `Industrial Integration`, stored in `independence_wave_form03_industrial_integration`

Both values run from 0 to 100. Full ratification requires at least 70 in both, a resolved constitutional status for every sovereign associate, and a real federal language scope. The carrier earns progress through timed decisions, missions, member votes, civilian-factory commitments, transport equipment, command attention, and state projects. It cannot finish by waiting or by spending political power.

The static implementation attestation and the runtime outcome are deliberately separate:

- `independence_wave_form03_progression_attested` certifies that the full source package is installed and audited. Add it to the pre-formation readiness contract only after every surface in this addendum exists.
- `independence_wave_form03_post_charter_complete` records that a particular LCX carrier achieved the full settlement in play.

The formation gate must never require the runtime completion flag. Doing so would require a post-formation result before formation and would make the route impossible.

## 2. Locked invariants

The implementation must preserve all of these accepted facts:

1. `LCX` is the Confederation of the Low Countries, not vanilla Benelux and not an ethnic Greater Netherlands.
2. Only `AFX` and `AGX` can carry the `LCX` cosmetic identity.
3. The carrier capital remains state 34 for an `AFX` carrier or state 36 for an `AGX` carrier.
4. A consenting non-carrier `AFX` or `AGX` founding anchor may be integrated through the existing transaction.
5. `BEL`, `HOL`, and `LUX` retain their tags, capitals, focuses, cores, states, armies, diplomacy, and sovereignty.
6. States 6, 7, 8, 35, 977, and 980 are never transferred or cored by this progression.
7. State 36 is a coarse game state. Player-facing text must not imply that every resident is Frisian.
8. Brussels may host a conference scene. It is not made the LCX capital while Belgium owns it.
9. The route remains constitutional or league Development Compact based. Patron-client and radical routes do not gain a hidden bypass.
10. No daily, weekly, or monthly all-country on action is added.
11. Failure after formation does not run the pre-commit identity rollback. LCX has already formed by that point.
12. No free units, instant cores, free factories, passive point generation, or political-power store is introduced.

## 3. Research basis and limits

### 3.1 Accepted Event 6 sources

This addendum implements rather than replaces the accepted sources under `docs/specs/006_independence_wave_specs/`, especially:

- `specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`
- `specs/006_independence_wave_spec_part_4_focus_tree_architecture.md`
- `specs/006_independence_wave_spec_part_5_country_packages.md`
- `specs/006_independence_wave_spec_part_6_formables_and_league.md`
- `specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`
- `matrices/006_formable_family_registry.csv`
- `matrices/006_decision_mission_map.csv`
- `matrices/006_idea_lifecycle_matrix.csv`
- `matrices/006_regional_overlay_matrix.csv`
- `matrices/006_ai_strategy_matrix.csv`
- `matrices/006_wave_tuning_model.csv`
- `research/006_research_resolution_matrix.csv`

The current identity, package, and audit handoffs remain binding. In particular, `006_form01_04_identity_research_2026_07_15.md`, `006_form03_audit_2026_07_15.md`, and `006_wallonia_frisia_package_handoff.md` fix the identity, state policy, and package anchors used here.

### 3.2 Historical anchors

- The official Benelux history records a 1943 monetary agreement, a 1944 customs agreement, and the later customs union. This supports a near-period counterfactual built around manifests, monetary clearing, tariffs, and technical coordination. It does not support annexing the three sovereign states. See [History of the Benelux](https://www.benelux.int/en/information-for-citizens/benelux-union/about-us/history/) and the [2019 Benelux summit declaration](https://www.benelux.int/files/9415/5427/7383/20190402_Decl_Benelux_Summit_EN_Final.pdf).
- Belgium's official history identifies language legislation and later federalisation as central responses to linguistic and regional conflict. The modern division into language communities and economic regions is a later institutional analogy, not a structure to project unchanged into the 1930s. See [Formation of the federal state](https://www.belgium.be/en/about_belgium/country/history/belgium_from_1830/formation_federal_state) and [The federal state](https://www.belgium.be/en/about_belgium/government/federale_staat).
- The Walloon public infrastructure service records that the state and Liège created the Port Autonome de Liège in 1937. It also describes ports as interfaces between water, rail, and road. This is a period-appropriate institutional anchor for a Sambre-Meuse public works board. See [Ports autonomes](https://infrastructures.wallonie.be/en/entreprises--non-marchand/nos-thematiques/voies-deau/gestion-du-domaine/organisation-territoriale/ports-autonomes.html).
- Official Walloon material describes the Sambre and Meuse waterways as a connected economic corridor linked to major North Sea ports. Modern tonnage is not used for tuning. The durable geographic relationship supports the corridor design. See [Voies navigables](https://www.wallonie.be/fr/vivre-en-wallonie/mobilite-et-infrastructures/voies-navigables).
- Official Friesland material identifies long-running water management and the Woudagemaal's operation since 1920. This supports a waterway standards and pumping-board project. See [Friesland and water](https://www.friesland.nl/nl/ontdek/waterland).
- Current Dutch and Frisian government material confirms the continuing public significance of West Frisian. It is used only to avoid erasing the language. It is not evidence for an exact alternate 1930s federal service code. See [Using Frisian](https://www.rijksoverheid.nl/vraag-en-antwoord/erkende-talen/wanneer-fries-gebruiken) and [Culture, language and education](https://www.fryslan.frl/cultuur-taal-en-onderwijs).

### 3.3 Vanilla structural precedents

- `common/ideas/belgium.txt`, `common/national_focus/belgium.txt`, and `events/WUW_Belgium.txt` show a staged language issue expressed through focuses, events, and idea swaps.
- `common/decisions/BUL.txt` shows timed civilian-factory commitments and partner investment decisions. It is a structural precedent for visible joint projects.
- `common/decisions/HOL.txt` and `events/MTG_Netherlands.txt` provide a Low Countries congress precedent. Their annexation and core grants are an explicit anti-precedent for FORM-03.

The implementation must continue to follow the offline wiki and official vanilla documentation consulted for data structures, scopes, events, decisions, missions, ideas, focuses, AI, script constants, variables, event targets, and dynamic values.

## 4. Public state model

### 4.1 Script constants

Create `common/script_constants/006_independence_wave_form03_constants.txt` with these categories and values. The names are exact implementation identifiers.

| Category | Keys and values |
|---|---|
| `independence_wave_form03_value` | `minimum = 0`, `maximum = 100`, `initial_accommodation = 15`, `initial_integration = 15`, `provisional = 25`, `compromise = 50`, `ratified = 70`, `consolidated = 85` |
| `independence_wave_form03_phase` | `none = 0`, `provisional = 1`, `drafting = 2`, `ratification = 3`, `complete = 4`, `compromise = 5`, `rupture = 6` |
| `independence_wave_form03_language_model` | `none = 0`, `parallel_services = 1`, `territorial_administration = 2`, `working_register = 3` |
| `independence_wave_form03_outcome` | `none = 0`, `full_compact = 1`, `charter_without_works = 2`, `industrial_directorate = 3`, `dual_compromise = 4`, `charter_rupture = 5` |
| `independence_wave_form03_delta` | `parallel_services = 25`, `territorial_administration = 20`, `working_register = 10`, `parallel_examinations = 20`, `working_examinations = 15`, `parallel_language_codes = 15`, `territorial_language_codes = 20`, `working_language_codes = 10`, `federal_appeals = 15`, `protected_service_extension = 20`, `anchor_works = 25`, `shared_manifests = 15`, `associate_corridor = 20`, `compact_technical_mission = 10`, `project_cancellation = -10`, `ratification_failure = -15`, `repair = 20` |
| `independence_wave_form03_league` | `technical_mission_reserve_cost = -20`, `technical_mission_cancel_refund = 10`, `technical_mission_minimum_reserve = 80`, `contribution_gain = 10`, `confidence_gain = 5`, `failure_loss = -10` |
| `independence_wave_form03_modifier` | `provisional_stability = -0.05`, `provisional_consumer_goods = 0.03`, `provisional_factory = -0.05`, `full_stability = 0.05`, `full_consumer_goods = -0.03`, `full_efficiency_gain = 0.05`, `full_trade = 0.10`, `language_compromise_stability = 0.03`, `language_compromise_consumer_goods = 0.05`, `industrial_directorate_factory = 0.08`, `industrial_directorate_stability = -0.08`, `dual_compromise_consumer_goods = 0.02`, `rupture_stability = -0.10`, `rupture_consumer_goods = 0.05`, `rupture_factory = -0.05`, `sambre_resources = 0.10`, `sambre_local_supplies = 0.10`, `sambre_infrastructure_speed = 0.15`, `frisian_local_supplies = 0.10`, `frisian_infrastructure_speed = 0.15`, `associate_local_supplies = 0.10`, `associate_infrastructure_speed = 0.10` |

Reuse the existing shared decision durations and costs rather than copying them. The relevant sources are `independence_wave_decision_duration`, `independence_wave_decision_cost`, `independence_wave_decision_effect`, and `independence_wave_decision_ai`.

### 4.2 Variables

| Variable | Scope | Purpose |
|---|---|---|
| `independence_wave_form03_federal_accommodation` | carrier | Public 0 to 100 constitutional progress |
| `independence_wave_form03_industrial_integration` | carrier | Public 0 to 100 industrial progress |
| `independence_wave_form03_charter_phase` | carrier | Current phase enum |
| `independence_wave_form03_language_model` | carrier | Selected language model enum |
| `independence_wave_form03_charter_outcome` | carrier | Current outcome enum |
| `independence_wave_form03_ratification_start_date` | carrier | Audit and cooldown date |
| `independence_wave_form03_last_repair_date` | carrier | Repair cadence audit |

The two public values are clamped by `independence_wave_form03_change_accommodation` and `independence_wave_form03_change_industrial_integration`. Callers provide temporary deltas named `independence_wave_form03_accommodation_delta` and `independence_wave_form03_integration_delta`. Temporary variables are never scoped.

### 4.3 Carrier flags

Use flags for boolean state:

- `independence_wave_form03_progression_attested`
- `independence_wave_form03_post_charter_active`
- `independence_wave_form03_language_convention_unlocked`
- `independence_wave_form03_language_convention_complete`
- `independence_wave_form03_industrial_board_unlocked`
- `independence_wave_form03_sambre_meuse_project_complete`
- `independence_wave_form03_frisian_waterway_project_complete`
- `independence_wave_form03_manifests_project_complete`
- `independence_wave_form03_compact_technical_mission_complete`
- `independence_wave_form03_sovereign_corridor_invitations_sent`
- `independence_wave_form03_ratification_window_open`
- `independence_wave_form03_post_charter_complete`
- `independence_wave_form03_post_charter_compromise`
- `independence_wave_form03_post_charter_failed`
- `independence_wave_form03_language_repair_used`
- `independence_wave_form03_industrial_repair_used`
- `independence_wave_form03_compact_reserve_committed`
- `independence_wave_form03_cleanup_in_progress`

Completed project flags are one-shot proof. Progress is not inferred from a passive count of flags.

### 4.4 Sovereign associate flags

These live only on `BEL`, `HOL`, or `LUX` when that country has `independence_wave_form03_autonomous_member`:

- `independence_wave_form03_full_accession_requested`
- `independence_wave_form03_limited_associate`
- `independence_wave_form03_language_vote_pending`
- `independence_wave_form03_language_guarantees_ratified`
- `independence_wave_form03_language_guarantees_withheld`
- `independence_wave_form03_corridor_invitation_pending`
- `independence_wave_form03_industrial_terms_ratified`
- `independence_wave_form03_industrial_terms_withheld`
- `independence_wave_form03_corridor_project_complete`
- `independence_wave_form03_withdrawal_recorded`

`independence_wave_form03_withdrawal_recorded` is a lifecycle tombstone. It survives member withdrawal, blocks rejoining the same LCX lifecycle, and clears only during carrier cleanup. This prevents a join, collect, withdraw, and rejoin loop.

Late accession after a full compact never clears the carrier's completed flag. The new member remains pending or limited until it performs its own accession work.

### 4.5 Exact scripted API

Extend the existing FORM-03 effect and trigger files with the following exact public helpers. Action-specific implementation may remain private inside the decision file, but these shared calls and predicates should not be duplicated.

| Effect ID | Contract |
|---|---|
| `independence_wave_form03_start_post_charter_progression` | Initializes the two values and provisional lifecycle only after full outer commit |
| `independence_wave_form03_change_accommodation` | Applies the temporary accommodation delta and clamps 0 to 100 |
| `independence_wave_form03_change_industrial_integration` | Applies the temporary integration delta and clamps 0 to 100 |
| `independence_wave_form03_select_language_model` | Stores one model, applies its structural value transaction, and dispatches member status votes |
| `independence_wave_form03_dispatch_constitutional_status_votes` | Sends the full, limited, or withhold choice to unresolved exact sovereign members |
| `independence_wave_form03_initialize_late_autonomous_member` | Routes a new member to the correct drafting or post-ratification accession event without rescanning countries |
| `independence_wave_form03_record_member_language_ratification` | Resolves one member's constitutional work and updates the carrier once |
| `independence_wave_form03_record_member_corridor_completion` | Resolves one member-selected corridor and updates the carrier once |
| `independence_wave_form03_apply_member_settlement_to_host` | Applies bounded deltas only when the member is the carrier's actual former host |
| `independence_wave_form03_apply_development_compact_technical_mission` | Commits and settles the reserve plus own-record transaction |
| `independence_wave_form03_refresh_charter_idea` | Enforces the one-at-a-time idea lifecycle |
| `independence_wave_form03_resolve_full_ratification` | Sets the complete outcome and durable transactions |
| `independence_wave_form03_resolve_ratification_timeout` | Selects the exact compromise or rupture outcome from stored values and member state |
| `independence_wave_form03_reopen_charter_progression` | Converts rupture into a bounded repairable compromise state |
| `independence_wave_form03_leave_autonomous_membership` | Removes one member's participation while preserving the withdrawal tombstone |
| `independence_wave_form03_reconcile_member_mirrors` | Rebuilds carrier BEL, HOL, and LUX mirror flags from exact country state |
| `independence_wave_form03_cleanup_post_charter_progression` | Performs guarded legal and accounting cleanup before existing FORM-03 cleanup |

| Trigger ID | Scope and contract |
|---|---|
| `has_independence_wave_form03_post_charter_progression` | Carrier has full LCX commit and active progression |
| `has_independence_wave_form03_active_language_action` | Carrier action lock |
| `has_independence_wave_form03_active_state_works` | Carrier state-works lock |
| `has_independence_wave_form03_active_industrial_administration` | Carrier non-state industrial lock |
| `has_independence_wave_form03_resolved_constitutional_status` | Member is fully ratified, limited, or explicitly withholding |
| `has_independence_wave_form03_all_constitutional_statuses_resolved` | Every living autonomous member has one resolved status and no pending full vote |
| `has_independence_wave_form03_federal_language_scope` | Carrier holds both anchors or has at least one sovereign language signatory |
| `has_independence_wave_form03_full_ratification_gate` | Both values meet threshold, member statuses resolve, and language scope is real |
| `is_independence_wave_form03_sovereign_associate` | Exact eligible BEL, HOL, or LUX member connected to the active carrier |
| `is_independence_wave_form03_associate_corridor_state` | Exact member-owned and controlled state in the bounded target set |
| `can_pay_independence_wave_form03_sambre_meuse_project_cost` | Safe civilian, train, and command-power surplus |
| `can_pay_independence_wave_form03_frisian_waterway_project_cost` | Safe civilian, train, convoy, and command-power surplus |
| `can_pay_independence_wave_form03_compact_technical_mission_cost` | Development Compact route, league membership, civilian capacity, and reserve floor |
| `can_pay_independence_wave_form03_repair_industrial_cost` | Safe civilian, train, and command-power surplus for repair |
| `can_independence_wave_form03_implement_member_language_guarantees` | Pending full member can fund its own language work |
| `can_independence_wave_form03_fund_associate_corridor_share` | Resolved member can fund one legal target and has not completed a corridor |
| `can_independence_wave_form03_withdraw_from_autonomous_membership` | Living member may leave once and has no active member action |

## 5. Runtime state machine

| Phase | Entry | Player work | Exit |
|---|---|---|---|
| Provisional | Outer formable transaction fully commits `LCX` | Read the opening event and reveal the focus branch | First FORM-03 focus |
| Drafting | Charter convention or works board opens | Select a language model, implement services, complete works, invite associates | Both values reach at least 50 and associate status is resolved |
| Ratification | Convergence focus activates the ratification mission | Raise both values to 70 and satisfy the federal language scope | Player ratifies or timer expires |
| Complete | Full gate is met and mission is selected | Late members use accession actions | Remains durable until origin cleanup |
| Compromise | Timer finds one or both values between 50 and 69 | Repair the missing pillar and resubmit | Full gate or another failure |
| Rupture | Timer finds either value below 50 or a foundational accession unresolved after material loss | Serve a 360-day reopening action, repair both pillars, resubmit | Compromise or complete |

`independence_wave_form03_start_post_charter_progression` runs exactly once from the successful branch of `independence_wave_formable_commit_selected_family`, after that outer transaction sets `independence_wave_formable_active` and `independence_wave_formable_committed` and applies the normal commit outcome. Its family check must be `constant:independence_wave_formable_family.low_countries_federation`. It initializes both values to 15, sets phase `provisional`, installs the provisional idea, sets the active flag, calls `mark_focus_tree_layout_dirty = yes`, and fires `chaosx.nr6.300`.

It must not run from the identity adapter or from `independence_wave_formable_integration_adapter_3`. This preserves the existing rollback if either adapter fails and ensures that `is_independence_wave_form03_active_carrier` is already true when the opening event and focus refresh execute.

## 6. Focus branch

Add a six-focus child branch below `independence_wave_establish_integration_commission` in `common/national_focus/006_independence_wave_focus.txt`.

| Focus ID | Position | Cost | Function |
|---|---:|---:|---|
| `independence_wave_form03_open_charter_convention` | x 52, y 16 | `@independence_wave_focus_short` | First focus. `allow_branch` and `available` require `is_independence_wave_form03_active_carrier`. Unlocks the convention decision |
| `independence_wave_form03_define_public_service_guarantees` | x 51, y 17 | `@independence_wave_focus_standard` | Requires the opening focus. Unlocks language implementation actions |
| `independence_wave_form03_establish_delta_works_board` | x 53, y 17 | `@independence_wave_focus_standard` | Requires the opening focus. Unlocks industrial projects |
| `independence_wave_form03_build_federal_appeals_and_examinations` | x 51, y 18 | `@independence_wave_focus_standard` | Requires public service guarantees. Unlocks the model-specific second constitutional action |
| `independence_wave_form03_harmonize_corridor_standards` | x 53, y 18 | `@independence_wave_focus_standard` | Requires the works board. Unlocks manifests, associate corridors, and Development Compact technical work |
| `independence_wave_form03_submit_low_countries_compact` | x 52, y 19 | `@independence_wave_focus_long` | Uses two prerequisite blocks so the two y 18 focuses are both required. Requires both values at least 50 and `has_independence_wave_form03_all_constitutional_statuses_resolved`. Activates the ratification mission |

Only the first focus needs `allow_branch`. Child visibility inherits it. The formation start effect must call `mark_focus_tree_layout_dirty` because the offline focus reference confirms that `allow_branch` otherwise refreshes only when the tree loads.

Focus rewards only unlock actions, advance the phase, or activate the final mission. They do not grant free factories, equipment, value points, or generic stat bundles.

## 7. Carrier decisions and mission

All entries remain in `independence_wave_form03_low_countries_category`. At most one language action, one state works action, and one administrative industrial action may run at the same time. Scripted triggers enforce those three locks.

| Decision or mission ID | Type and time | Real cost | Exact result |
|---|---|---|---|
| `independence_wave_form03_convene_language_convention` | Timed decision, 180 days | 1 civilian factory, administration standard | Fires `chaosx.nr6.301` on completion. Cancellation loses 10 accommodation |
| `independence_wave_form03_open_multilingual_service_examinations` | Timed decision, 150 days | 1 civilian factory, administration standard | Adds 20 accommodation for parallel services or 15 for the working register. Adds 10 capacity only for the parallel model |
| `independence_wave_form03_publish_member_language_codes` | Timed decision, 120 days | Administration light | Adds 15, 20, or 10 accommodation according to the selected model. Adds 5 legitimacy for parallel or territorial models |
| `independence_wave_form03_establish_federal_language_appeals` | Timed decision, 180 days | 1 civilian factory, administration standard | Territorial model only. Adds 15 accommodation and reduces instability by 5 |
| `independence_wave_form03_extend_protected_local_services` | Timed decision, 180 days | 1 civilian factory, administration standard, 5% stability | Working-register model only. Adds 20 accommodation. This is the model's deliberate repair cost |
| `independence_wave_form03_reconnect_sambre_meuse_corridor` | Timed state works decision, 180 days | 3 civilian factories, 20 trains, 20 command power | Requires carrier ownership and control of state 34. Adds 25 integration, applies the state 34 modifier, and queues one non-instant infrastructure level if valid |
| `independence_wave_form03_coordinate_frisian_waterway_standards` | Timed state works decision, 180 days | 3 civilian factories, 10 trains, 5 convoys, 20 command power | Requires carrier ownership and control of state 36. Adds 25 integration, applies the state 36 modifier, and queues one non-instant infrastructure level if valid |
| `independence_wave_form03_standardize_rail_and_customs_manifests` | Timed decision, 180 days | 1 civilian factory, diplomatic standard | Adds 15 integration. It standardizes schedules and manifests without creating a customs annexation |
| `independence_wave_form03_request_development_compact_technical_mission` | Timed decision, 180 days | 1 civilian factory, administration light, 20 league reserve committed at selection | Development Compact only. Adds 10 integration and 10 capacity. Adds 10 own league contribution and 5 own confidence. Adds 5 cohesion and 5 common cause |
| `independence_wave_form03_invite_sovereign_corridor_partners` | Timed decision, 180 days | 1 civilian factory, diplomatic standard | Sends `chaosx.nr6.303` only to eligible autonomous `BEL`, `HOL`, and `LUX` members that have not answered |
| `independence_wave_form03_ratify_confederal_charter` | Selectable mission, 360 days | No extra payment beyond the convergence focus and completed work | Activated by effect. `available` is the full ratification gate. Selection resolves full compact. Timeout resolves compromise or rupture |
| `independence_wave_form03_resubmit_confederal_charter` | Timed decision, 180 days | Diplomatic standard | Any repairable compromise, including a reopened rupture. Requires the full gate. Resolves full compact without repeating one-shot projects |
| `independence_wave_form03_reopen_charter_talks` | Timed decision, 360 days | Strategic cost, 3 civilian factories | Rupture only. Restores each value to a minimum of 50, clears one-cycle repair locks, clears rupture, sets a repairable compromise, and refreshes the correct asymmetric or dual idea |
| `independence_wave_form03_repair_language_settlement` | Timed decision, 180 days | 1 civilian factory, administration standard | Once per failure cycle and only below 70. Adds 20 accommodation |
| `independence_wave_form03_repair_industrial_compact` | Timed decision, 240 days | 3 civilian factories, 20 trains, 20 command power | Once per failure cycle and only below 70. Adds 20 integration |
| `independence_wave_form03_implement_member_language_guarantees` | Sovereign-member timed decision, 180 days | 1 civilian factory, administration light | Pending full member implements the selected model locally, records one constitutional ratification, and reports to the carrier |
| `independence_wave_form03_fund_associate_corridor_share` | Sovereign-member targeted decision, 180 days | 1 civilian factory, diplomatic light | Member chooses one legal owned and controlled state, completes one corridor share, and reports 20 integration once |
| `independence_wave_form03_withdraw_from_autonomous_membership` | Sovereign-member timed decision, 120 days | Diplomatic standard | Leaves the association once, preserves the withdrawal tombstone, and reconciles carrier mirrors without changing sovereignty |

Specific cost triggers and payment effects belong in the FORM-03 trigger and effect files. They must use the existing shared cost constants, including the named duration, factory, train, convoy, command-power, and stability keys. Every equipment payment checks a safe surplus before the decision can start. Civilian factories are committed through decision modifiers for the full timer, while equipment, command power, stability, and league reserve are debited at selection.

The ratification entry must use `days_mission_timeout = constant:independence_wave_decision_duration.integration`, `activation` for the still-valid active-carrier state, `available` for the full gate, and `activate_mission` from the convergence focus. It must not rely on a dormant decision becoming visible by polling.

The Development Compact decision requires a shared reserve of at least 80 before committing 20. This leaves the existing danger floor of 60 intact. Cancellation returns 10 and treats the other 10 as committed technical work. The reserve transaction happens at selection, so another league action cannot spend the same reserve.

## 8. Language models and member ratification

`chaosx.nr6.301` offers three structural models after the convention has consumed its time and resources.

| Working option | Immediate structural effect | Follow-up actions | Political result |
|---|---:|---|---|
| Parallel federal services | +25 accommodation | Examinations and language codes | Highest service duplication, strongest common guarantees, modest initial capacity burden |
| Territorial administration with federal appeal | +20 accommodation | Language codes and appeal board | Strong regional administration and a federal remedy, lower central uniformity |
| One working register with protected local services | +10 accommodation | Examinations, language codes, protected-service extension | Fastest administrative consolidation, but it cannot reach full settlement without a costly protection extension |

These are not three generic modifier choices. Each stores a different enum, changes the available actions, changes their value deltas, and produces a different compromise idea if ratification times out.

After a model is selected, every unresolved exact `BEL`, `HOL`, and `LUX` scope receives `chaosx.nr6.302` if it is an autonomous member. The event is the request point. Its three choices are full constitutional accession, limited economic association, or explicit withholding. Full accession sets `independence_wave_form03_full_accession_requested` and `independence_wave_form03_language_vote_pending`. Limited association sets its limited flag. Withholding sets `independence_wave_form03_language_guarantees_withheld`. This removes any circular requirement to request full accession before receiving the request event.

A pending full member must then perform `independence_wave_form03_implement_member_language_guarantees`, a 180-day decision using 1 civilian factory and administration light. Completion clears the pending flag and records `independence_wave_form03_language_guarantees_ratified` exactly once.

A member may choose limited economic association. It retains sovereignty and autonomous membership but receives `independence_wave_form03_limited_associate`. It does not block the carrier's universal settlement and does not count as a constitutional signatory.

Extend the existing `independence_wave_form03_join_active_carrier_as_autonomous_member` effect with `independence_wave_form03_initialize_late_autonomous_member`. A member joining before model selection waits for the normal `.302` dispatch. A member joining after model selection but before full ratification receives `.302` immediately. A member joining after full ratification receives `.304`, and full accession creates its own pending work without clearing the carrier's completion flag. If sovereign corridor invitations were already sent, the same immediate chain also exposes `.303` to that member. No country scan or repeated carrier-wide invitation is used.

`has_independence_wave_form03_resolved_constitutional_status` is true only for full ratification, limited association, or explicit withholding. A pending full request is unresolved. The carrier-level full ratification trigger requires:

1. Accommodation at least 70.
2. Every living autonomous member has one resolved constitutional status and no pending full request.
3. A real federal language scope exists. This means either the carrier owns and controls both states 34 and 36, or at least one sovereign autonomous member has implemented the language guarantees.

This prevents a one-anchor carrier with only limited economic associates from claiming a federal language settlement.

## 9. Sovereign industrial participation

`chaosx.nr6.303` invites each eligible sovereign associate to a corridor protocol. Acceptance only unlocks work in that member's scope. It does not let the carrier spend, build, transfer, core, or change law inside the member.

The member action `independence_wave_form03_fund_associate_corridor_share` is a state-targeted 180-day decision. It uses 1 civilian factory and diplomatic light. The target must be owned and controlled by the member and must be one of:

- `BEL`: state 6 or 977
- `HOL`: state 7 or 35
- `LUX`: state 8

Completion applies `independence_wave_form03_associate_corridor_modifier` to that chosen state, queues one non-instant infrastructure level if a valid level remains, records the member's industrial ratification, and adds 20 industrial integration to the active carrier exactly once for that member.

State 980 is not included. The accepted identity handoff leaves Ardennes as a later staged question rather than an automatic LCX corridor surface.

The permanent dynamic modifier is the invariant project consequence. A queued infrastructure level is an additional cap-safe physical extension when the state can accept one. This is not a fallback outcome. No industrial project grants an instant factory or building slot.

## 10. Territorial industrial modifiers

Create `common/dynamic_modifiers/006_independence_wave_form03_state_modifiers.txt` with only three applied modifiers:

| Modifier ID | Scope gate | Modifiers |
|---|---|---|
| `independence_wave_form03_sambre_meuse_corridor_modifier` | State 34 while owned by the active carrier | `local_resources_factor = 0.10`, `local_supplies = 0.10`, `state_production_speed_infrastructure_factor = 0.15` |
| `independence_wave_form03_frisian_waterway_modifier` | State 36 while owned by the active carrier | `local_supplies = 0.10`, `state_production_speed_infrastructure_factor = 0.15` |
| `independence_wave_form03_associate_corridor_modifier` | Registered member target while its owner retains industrial ratification | `local_supplies = 0.10`, `state_production_speed_infrastructure_factor = 0.10` |

This bounded use of dynamic modifiers is justified because country ideas cannot express state 34, state 36, or a member-selected sovereign corridor. At most five exact Low Countries states can carry the modifiers, and no world scan maintains them. The modifiers represent the durable operating value of the completed corridor. They avoid fractional building-slot bonuses that could round into reward dust.

When the original carrier is `AFX`, the state 34 project sets `independence_wave_afx_continuity_delta = constant:independence_wave_nwe_package_pressure.standard_gain` and calls `independence_wave_change_afx_industrial_continuity`. When the original carrier is `AGX`, the state 36 project sets both `independence_wave_agx_waterline_delta` and `independence_wave_agx_coastal_security_delta` to `constant:independence_wave_nwe_package_pressure.standard_gain` and calls `independence_wave_change_agx_waterline_security`. An absorbed non-carrier package is not reinitialized and its ended-origin values are not recreated.

## 11. Events

Reserve the currently unused `chaosx.nr6.300` through `chaosx.nr6.308` block in `events/006_independence_wave.txt`. Re-run an ID collision scan immediately before implementation.

| Event ID | Scope | Purpose |
|---|---|---|
| `chaosx.nr6.300` | carrier | Public opening report for the provisional charter and two values |
| `chaosx.nr6.301` | carrier | Language convention model choice |
| `chaosx.nr6.302` | sovereign associate | Full constitutional accession invitation and limited-association option |
| `chaosx.nr6.303` | sovereign associate | Corridor protocol invitation |
| `chaosx.nr6.304` | late sovereign associate | Post-ratification accession terms. Full accession creates pending work without revoking carrier completion |
| `chaosx.nr6.305` | carrier | Member ratification or withdrawal report with dynamic member name |
| `chaosx.nr6.306` | carrier | Full compact ratification outcome |
| `chaosx.nr6.307` | carrier | Dynamic compromise outcome selected from the stored outcome enum |
| `chaosx.nr6.308` | carrier | Charter rupture and reopening terms |

No global event target is needed. The carrier is always exact `AFX` or `AGX`, and sovereign members are exact `BEL`, `HOL`, or `LUX`. Fixed scoped effects can record the result safely. Regular event targets may be used only inside the immediate invitation chain for displayed names.

## 12. Idea lifecycle

Create `common/ideas/006_independence_wave_form03_ideas.txt`. Exactly one FORM-03 idea may be active at a time. `independence_wave_form03_refresh_charter_idea` removes every variant before adding the correct one.

| Idea ID | Condition | Modifiers |
|---|---|---|
| `independence_wave_form03_provisional_charter` | Provisional, drafting, or ratification | -5% stability factor, +3% consumer goods, -5% factory output |
| `independence_wave_form03_charter_without_works` | Accommodation at least 70, integration below 70 | +3% stability factor, +5% consumer goods |
| `independence_wave_form03_industrial_directorate` | Integration at least 70, accommodation below 70 | +8% factory output, -8% stability factor |
| `independence_wave_form03_dual_compromise` | Both values from 50 through 69 | +2% consumer goods |
| `independence_wave_form03_ratified_confederation` | Full compact | +5% stability factor, -3% consumer goods, +5% production efficiency gain, +10% trade opinion |
| `independence_wave_form03_charter_rupture` | Either value below 50 at timeout | -10% stability factor, +5% consumer goods, -5% factory output |

Use the exact supported keys `stability_factor`, `consumer_goods_factor`, `industrial_capacity_factory`, `production_factory_efficiency_gain_factor`, and `trade_opinion_factor`. Their values must be sourced from the new script constants. The FORM-03 lifecycle adds only one simultaneous national spirit and does not replace the existing AFX or AGX package lifecycle or route idea.

## 13. Five-value, host, league, and network transactions

### 13.1 Carrier values

Use the existing public value effects and the shared `independence_wave_value` constants. The following are deliberate, event-sized changes rather than a reward on every button:

| Resolution | Legitimacy | Recognition | Capacity | Security | Instability |
|---|---:|---:|---:|---:|---:|
| Parallel services selected | +10 | +5 | -5 | 0 | 0 |
| Territorial administration selected | +10 | 0 | +5 | 0 | -5 |
| Working register selected | -5 | 0 | +10 | 0 | +10 |
| Either anchor works project completes | 0 | 0 | +10 | +5 | -5 |
| Full compact ratified | +10 | +10 | +10 | 0 | -10 |
| Charter rupture | -15 | -10 | 0 | 0 | +15 |

Project-level accommodation and integration deltas remain in their dedicated variables. Do not mirror every small increase into the five-value system.

### 13.2 Former host

The existing carrier's `independence_wave_former_host` is the only former-host ledger this progression may modify.

- If that exact former host becomes a sovereign member and implements language guarantees, apply hostility -10, property dispute -10, population dispute -15, and border progress +10.
- If that exact former host completes a corridor share, apply obligations -10, property dispute -10, and border progress +10.
- If that exact former host withholds full accession during the ratification window, apply hostility +10, population dispute +10, and host domestic pressure +10.

Use the shared `independence_wave_decision_effect.bilateral_*` constants. Initialize all eight `independence_wave_decision_*` host delta temporaries to `constant:independence_wave_value.minimum`, then set only the named hostility, obligations, property, population, border-progress, or host-pressure deltas and call `independence_wave_decision_apply_host_deltas`. This synchronizes the existing ledger without stale temporary inputs. Do not invent a second former-host variable for the absorbed non-carrier AFX or AGX origin.

### 13.3 League

The Development Compact technical mission is available only when:

- the carrier is an Independence Wave league member
- the global route is `constant:independence_wave_league_route.development_compact`
- shared reserve is at least 80
- no other FORM-03 compact mission is active

On success, use `independence_wave_change_own_league_record` for the carrier's contribution and confidence. Apply global cohesion +5, common cause +5, patron capture 0, and no direct aggregate confidence delta. The own-record effect recalculates aggregate confidence and avoids double counting.

The own-record call sets `independence_wave_member_contribution_delta` and `independence_wave_member_confidence_delta`. The global call initializes `independence_wave_league_cohesion_delta`, `independence_wave_league_common_cause_delta`, `independence_wave_league_patron_capture_delta`, `independence_wave_league_shared_reserve_delta`, and `independence_wave_league_member_confidence_delta`, then calls `independence_wave_change_league_values`. Reserve selection, cancellation refund, success, and rupture each use that single accounting surface. The direct aggregate confidence delta stays at `constant:independence_wave_value.minimum` whenever the own record changes.

If the charter ruptures after compact money was used, apply cohesion -10, common cause -10, and own confidence -10. Do not automatically force a league crisis. Existing league thresholds remain authoritative.

### 13.4 Network

A sovereign associate corridor completion gives the completing member +10 network standing if it is an active Event 6 country. `BEL`, `HOL`, or `LUX` that are not Event 6-origin countries do not receive fabricated Event 6 values. The carrier receives no extra network points beyond the industrial integration already earned.

## 14. AI contract

### 14.1 Carrier focus AI

- Opening charter focus: urgent.
- Language branch: urgent for the constitutional route, high for Development Compact.
- Works branch: urgent for Development Compact, high for the constitutional route.
- Convergence focus: blocked below 50 in either value, urgent once both are at least 50.

### 14.2 Language choice AI

- Parallel services gets the strongest weight for constitutional AI at `constant:independence_wave_recognition_band.treaty_backed` recognition and at least `constant:independence_wave_capacity_band.institutional` capacity.
- Territorial administration gets the strongest weight when both states 34 and 36 are present or at least two sovereign members seek full accession.
- The working register is an emergency compromise. It gets a high weight only during war, instability at `constant:independence_wave_instability_band.severe`, or capacity below `constant:independence_wave_capacity_band.institutional`. It must never be the generic default.

### 14.3 Project AI

- A state works project requires at least one unreserved civilian factory after its three-factory commitment.
- AI does not start both state works projects at once unless enough civilian factories remain for ordinary construction.
- War multiplies major works weight by `constant:independence_wave_focus_ai.war_avoid_factor` but does not block a human player.
- Loss of ownership or control of the target state cancels the project and applies the one-time -10 integration cancellation delta.
- AFX-origin AI prioritizes state 34 while industrial continuity is unstable.
- AGX-origin AI prioritizes state 36 while the waterline or coastal security is unstable.
- Development Compact AI may use the technical mission only at the 80 reserve floor. It cannot spend the league below the existing danger floor.
- AI must retain the existing safe train, convoy, manpower, and command-power reserves.

### 14.4 Sovereign member AI

- Full accession weight rises with opinion at `constant:independence_wave_decision_gate.diplomatic_acceptance_opinion`, democratic government, peace with the carrier, and carrier recognition at `constant:independence_wave_recognition_band.treaty_backed`.
- Limited association weight rises when the member lacks spare civilian factories or has unsettled relations but is not hostile.
- Withholding weight rises during war with the carrier, capital loss, or negative opinion.
- Corridor participation requires one spare civilian factory after commitment, a controlled eligible state, and the diplomatic material reserve.
- Human `BEL`, `HOL`, and `LUX` always receive an explicit choice. AI outcomes never overwrite a human member.

## 15. Failure, compromise, recovery, and withdrawal

### 15.1 Ratification resolution

`independence_wave_form03_resolve_ratification_timeout` uses the stored values and membership flags:

| Condition | Outcome |
|---|---|
| Both values at least 70 and full gate met | Full compact |
| Accommodation at least 70, integration from 50 through 69 | Charter without works |
| Integration at least 70, accommodation from 50 through 69 | Industrial directorate |
| Both values from 50 through 69 | Dual compromise |
| Either value below 50 or foundational full accession unresolved after a member loss | Charter rupture |

Compromise retains LCX and opens bounded repair work. Rupture retains LCX with a severe idea and a 360-day reopening action. Completing the reopening action clears rupture, sets the repairable compromise state, refreshes the idea from the restored values, and exposes the same full-gate resubmission action. No outcome silently converts to a generic formable.

### 15.2 Withdrawal

`independence_wave_form03_withdraw_from_autonomous_membership` is a 120-day sovereign-member decision with diplomatic standard cost. It calls `independence_wave_form03_leave_autonomous_membership`, clears that member's active participation flags, retains `independence_wave_form03_withdrawal_recorded`, and recalculates the existing carrier mirror flags. `can_independence_wave_form03_join_as_autonomous_member` must reject the tombstone until carrier cleanup. Re-accession after a formal withdrawal is not available in this lifecycle.

Withdrawal during drafting or ratification applies -10 accommodation, -10 integration, -10 legitimacy, and -10 to the withdrawing member's own league confidence when that member has an Event 6 league record. A non-Event 6 BEL, HOL, or LUX member receives no fabricated league value. The loss is recorded once through `independence_wave_form03_withdrawal_recorded`.

It never transfers a state, creates a war, changes a subject relation, or removes the member's sovereign tag.

### 15.3 No post-formation transactional rollback

Physical construction already completed remains on the map after compromise, rupture, withdrawal, or later origin cleanup. Charter dynamic modifiers and legal flags are removable. Buildings are not erased as if the work never happened.

The existing `independence_wave_form03_rollback_identity` remains restricted to a failed formation transaction before integration commit.

## 16. Cleanup contract

Create `independence_wave_form03_cleanup_post_charter_progression` and call it at the start of `independence_wave_form03_cleanup_runtime`.

Required order:

1. Set `independence_wave_form03_cleanup_in_progress`.
2. If Development Compact reserve is committed to an unfinished mission, return the 10-point cancellation refund exactly once.
3. Remove the active ratification mission and every FORM-03 timed decision. All cancel effects must check the cleanup flag and do nothing during cleanup.
4. Remove every FORM-03 idea variant.
5. Remove the state 34 and state 36 dynamic modifiers.
6. In exact `BEL`, `HOL`, and `LUX` scopes, remove associate corridor modifiers from states 6, 977, 7, 35, and 8 where present, then clear all associate progression flags.
7. Clear the two public values, phase, model, outcome, dates, project flags, repair flags, reserve flag, active flag, and progression attestation.
8. Clear the cleanup guard last.

Extend `independence_wave_form03_clear_autonomous_member_state` with every new associate flag. Existing cosmetic-tag removal, global identity cleanup, package readiness cleanup, and member mirror cleanup remain in `independence_wave_form03_cleanup_runtime`.

No cleanup path fires a timeout outcome, member-withdrawal penalty, or project cancellation penalty.

## 17. Presentation, localisation, and art

### 17.1 Visible values without a new scripted GUI

Expand `independence_wave_form03_low_countries_category` with:

- active-carrier and pending-member visibility
- `visible_when_empty = yes` while progression is active
- a category description showing both numeric values, their bands, the charter phase, and unresolved member status

Create `common/scripted_localisation/006_independence_wave_form03_scripted_localisation.txt` with:

- `GetIndependenceWaveForm03AccommodationBand`
- `GetIndependenceWaveForm03IntegrationBand`
- `GetIndependenceWaveForm03PhaseText`
- `GetIndependenceWaveForm03LanguageModelText`
- `GetIndependenceWaveForm03MemberStatusText`
- `GetIndependenceWaveForm03OutcomeText`

On a sovereign-member screen, the scripted localisation resolves the live carrier through exact `AFX` and `AGX` checks before displaying the carrier's two values. It must not read nonexistent member-local copies or create a global carrier pointer.

A bespoke scripted GUI is not warranted. Two exact values and a phase fit legibly in the category description, and the existing animated FORM eligibility seal already owns discovery and proclamation feedback. A new animation would duplicate that function and reduce numeric clarity. Static, distinct art is the stronger choice for this progression.

### 17.2 Localisation file and direction

Create `localisation/english/006_independence_wave_form03_l_english.yml` with UTF-8 BOM. It owns:

- category name and dynamic description
- all six focus names, descriptions, and effect tooltips
- every decision and mission name, description, cost text where a shared key does not fit, and effect tooltip
- all six idea names and descriptions
- `chaosx.nr6.300` through `.308` event text and options
- value bands, phase names, language models, member statuses, and outcomes
- modifier localisation for all three state dynamic modifiers

Writing direction:

- Treat the charter as an alternate constitutional bargain, not a prediction of later Belgian federal structures.
- Name Dutch, French, West Frisian, and German-speaking service rights only where participating communities make them relevant.
- Never imply that state 36 is uniformly Frisian.
- Describe `BEL`, `HOL`, and `LUX` as sovereign associates that can ratify, limit, or leave their participation.
- Describe actual costs, time, member vetoes, works burdens, and failure risks.
- Never mention caps, implementation history, reworks, fallbacks, or registry checks in player-facing text.

### 17.3 Asset package

After parent acceptance, route production through `chaos-redux-event-assets` under the already accepted Event 6 asset families. Do not create duplicate asset-family rows for this subsystem.

| Accepted asset family | FORM-03 deliverable | Size and path | Sprite family |
|---|---|---|---|
| `ASSET-048` regional report variants | Charter convention report scene | 210x176, `gfx/event_pictures/006_independence_wave/` | `GFX_report_event_006_form03_charter_convention` |
| `ASSET-018` regional formable focuses | Six adapted FORM-03 focus icons | 94x86, `gfx/interface/goals/006_independence_wave/form03/` | `GFX_goal_independence_wave_form03_*` plus shine sprites |
| `ASSET-026` founding identity stages | Six charter idea stages | 64x64, `gfx/interface/ideas/006_independence_wave/form03/` | `GFX_idea_independence_wave_form03_*` |
| `ASSET-038` integration missions | Distinct adapted language, works, member vote, ratification, repair, and withdrawal decisions | 32x32, `gfx/interface/decisions/006_independence_wave/form03/` | `GFX_decision_independence_wave_form03_*` |

Create `interface/006_independence_wave_form03.gfx` for these sprites and register the report image in `interface/006_independence_wave_event_pictures.gfx`.

The report scene should show a multilingual constitutional table joined to engineering and transport plans, with no readable generated text. The six focus icons must distinguish the opening convention, public-service guarantees, the delta works board, appeals and examinations, corridor standards, and ratification. Idea stages must visibly progress from loose papers to a settled charter and works seal. Every decision receives distinct adapted art within coherent language, works, member, ratification, repair, and withdrawal subfamilies. Decision icons must remain readable at 32x32.

Create an asset manifest at `docs/assets/006_independence_wave/low_countries_form03_progression/manifest.md` with source, processed PNG, DDS, sprite, usage, and provenance records. The existing LCX flag manifest remains separate.

No new animated asset is specified. If a later accepted design adds animation, it must use `chaos-redux-frame-animation` and real source frames.

## 18. Exact source touchpoints

| File | Required implementation |
|---|---|
| `common/script_constants/006_independence_wave_form03_constants.txt` | New values, enums, deltas, league reserve, and modifier tuning |
| `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` | Call the FORM-03 start effect only from the successful outer commit branch after active and committed flags are set |
| `common/scripted_effects/006_independence_wave_form03_effects.txt` | Start, value changes, model, project, member, host, league, ratification, recovery, withdrawal, lifecycle, and cleanup effects |
| `common/scripted_triggers/006_independence_wave_form03_triggers.txt` | Progress gates, membership resolution, language scope, resource costs, action locks, target-state gates, full ratification, and AI safety |
| `common/decisions/006_independence_wave_form03_decisions.txt` | All carrier and sovereign member decisions plus the ratification mission |
| `common/decisions/categories/006_independence_wave_form03_categories.txt` | Post-charter carrier and member visibility, dynamic description, visible-when-empty behavior |
| `common/national_focus/006_independence_wave_focus.txt` | Six-focus branch at x 51 to 53, y 16 to 19 |
| `common/ideas/006_independence_wave_form03_ideas.txt` | Six mutually exclusive lifecycle ideas |
| `common/dynamic_modifiers/006_independence_wave_form03_state_modifiers.txt` | Three bounded state modifiers |
| `events/006_independence_wave.txt` | Event block `.300` through `.308` |
| `common/scripted_localisation/006_independence_wave_form03_scripted_localisation.txt` | Value, phase, model, member, and outcome text selectors |
| `localisation/english/006_independence_wave_form03_l_english.yml` | Final player-facing localisation, UTF-8 BOM |
| `interface/006_independence_wave_form03.gfx` | New focus, idea, and decision sprites |
| `interface/006_independence_wave_event_pictures.gfx` | FORM-03 report sprite |
| `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt` | Preserve package lifecycles and expose the existing AFX or AGX project-value hooks only |
| `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt` | Reuse stable continuity and waterline checks in project AI |
| `docs/events/006_independence_wave/systems/formable_registry.md` | Document post-charter state machine and runtime completion flag |
| `docs/events/006_independence_wave/northern_western_europe_packages.md` | Document AFX and AGX interaction with LCX projects |
| `docs/events/006_independence_wave/overview.md` | Document events, decisions, focus branch, member behavior, and failure outcomes |
| `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv` | Mark the accepted progression implemented only after audit |
| `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` | Register the FORM-03 action family after parent accepts identifier rows |
| `docs/specs/006_independence_wave_specs/matrices/006_idea_lifecycle_matrix.csv` | Register the one-at-a-time charter lifecycle |
| `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv` | Keep existing families 018, 026, 038, and 048 authoritative. Record child deliverables in the asset manifest rather than adding duplicate family rows |
| `docs/assets/006_independence_wave/low_countries_form03_progression/manifest.md` | Source, processed, DDS, sprite, usage, and provenance records for the accepted child assets |

`docs/spreadsheets/chaos_redux_events_catalog.xlsx` has only the broad Event 6 details and evolution fields. FORM-03 has no dedicated workbook field. Do not edit row 7 merely to insert this subsystem. Reconcile the row only if implementation changes the top-level in-game Event 6 detail or evolution wording.

## 19. Validation scenarios

The implementation is not complete until all scenarios below have evidence.

1. `AFX` carrier and consenting `AGX` anchor form LCX. Only state 36 transfers and cores through the existing transaction.
2. `AGX` carrier and consenting `AFX` anchor form LCX. Only state 34 transfers and cores through the existing transaction.
3. `AFX` plus a consenting eligible Belgian delegation forms LCX without transferring a Belgian state.
4. `AGX` plus a consenting eligible Belgian delegation forms LCX without transferring a Belgian state.
5. Progress starts only after the outer transaction sets `independence_wave_formable_active` and `independence_wave_formable_committed`, and never from either adapter or a failed transaction.
6. The six-focus branch is hidden before formation and appears after the layout-dirty call.
7. Starting values are exactly 15 and 15 and remain clamped from 0 to 100.
8. Each language model exposes only its authored follow-up actions and reaches its stated value total.
9. A one-anchor carrier cannot satisfy the full language scope with only limited associates.
10. A two-anchor carrier can satisfy the federal language scope without annexing a sovereign member.
11. A full sovereign member must spend its own time and resources to implement language guarantees.
12. Human `BEL`, `HOL`, and `LUX` can select full accession, limited association, explicit withholding, corridor participation, refusal, and withdrawal without AI overwrite.
13. The state 34 project cannot start without carrier ownership and control of state 34.
14. The state 36 project cannot start without carrier ownership and control of state 36.
15. Loss of a project state cancels once, applies one cancellation loss, and never duplicates payment or progress.
16. Associate corridor targets are limited to states 6, 977, 7, 35, and 8 in the correct member scope.
17. No associate project transfers, cores, or changes ownership of its target.
18. A max-infrastructure target still receives the invariant project modifier and no invalid construction order.
19. Development Compact reserve cannot be committed below 80, debits 20 once, and returns 10 once on cancellation.
20. League contribution and confidence update the carrier's own record without double changing aggregate confidence.
21. Constitutional non-league LCX can complete through domestic and sovereign-member projects.
22. Full ratification requires both values at least 70 and resolved membership.
23. Language-high and industry-low timeout produces `charter_without_works`.
24. Industry-high and language-low timeout produces `industrial_directorate`.
25. Both values from 50 through 69 produce `dual_compromise`.
26. Either value below 50 produces `charter_rupture` and does not drop LCX.
27. Repair and resubmission can reach full compact without repeating one-shot anchor projects.
28. Late sovereign accession reaches the correct status and corridor terms without a country scan, cannot revoke an already completed compact, and does not repeat the carrier-wide invitation.
29. Withdrawal clears only the leaving member, applies its penalties exactly once, retains the lifecycle tombstone, and prevents rejoin exploitation.
30. Former-host deltas apply only when the carrier's actual saved former host is the participating member.
31. AFX-origin state 34 work changes the existing AFX continuity mechanic. AGX-origin state 36 work changes the existing AGX waterline mechanic.
32. Exactly one FORM-03 idea is active in every phase and no idea survives cleanup.
33. Origin cleanup removes missions, decisions, legal modifiers, variables, flags, member state, and reserved league funds without firing timeout or cancellation penalties.
34. Physical infrastructure already built remains after legal cleanup.
35. No on-action scans all countries. All member dispatch uses exact carrier and member tags or activated decisions.
36. AI keeps safe civilian, train, convoy, manpower, command-power, and league-reserve margins.
37. Player-facing text never calls state 36 uniformly Frisian and never describes BEL, HOL, or LUX as annexed.
38. Final localisation keys exist with UTF-8 BOM, and event, focus, decision, idea, docs, and registry wording agree.
39. FORM-03 progression attestation remains absent until every implementation and audit surface passes.

## 20. Unresolved facts and design decisions

These questions must remain explicit. They do not justify invented content.

1. The exact 1930s public-service status of West Frisian and German-speaking communities needs package-specific archival research. Until then, final text must present an alternate negotiated guarantee rather than claim an enacted historical template.
2. The current Belgian founding eligibility is specifically the `BEL_flanders` cosmetic delegation. Whether it may speak for all Belgian institutions is unresolved. The progression must describe only the participating delegation and sovereign member terms.
3. State 36 cannot represent a precise ethnolinguistic boundary. No mechanic or localisation may treat it as one.
4. A voluntary post-formation dissolution and cosmetic-tag reversion has no accepted capital, membership, flag, or historical package. This addendum does not add a dissolve button. Such a route needs a separate accepted identity decision.
5. The integrated non-carrier AFX or AGX origin loses its own former-host runtime through the existing end-origin transaction. This addendum does not synthesize a second host ledger.
6. Final event prose, option labels, and asset compositions remain production work. Working labels here are not final localisation.
7. Event IDs `.300` through `.308` are currently free, but implementation must re-scan after concurrent Event 6 work lands.

None of these questions blocks the authored two-value progression. They constrain claims and prevent unsafe scope expansion.

## 21. Implementation order and completion gate

1. Accept this addendum and fold any design changes into the Event 6 source specification.
2. Add constants, triggers, effects, ideas, and state modifiers.
3. Wire the start hook and cleanup before exposing decisions.
4. Add decisions, mission, events, and exact member dispatch.
5. Add the six-focus branch and layout refresh.
6. Produce and wire final localisation and static assets.
7. Update system, package, event, and matrix documentation.
8. Run a decision and mission audit, focus-tree audit, localisation audit, country-package audit, and Event 6 completion audit.
9. Set `independence_wave_form03_progression_attested` in the readiness effect only after the audits pass.
10. Mark FORM-03's post-formation progression implemented only after the validation matrix above has evidence.

## 22. Simplifications, omissions, and fallbacks

No fallback progression, copied route, territorial annexation, passive checklist, placeholder asset, or free reward path is proposed.

This is a documentation-only addendum. Gameplay, localisation, assets, matrices, and the workbook remain unchanged in this tranche. The unresolved dissolution route and exact period language-law research are disclosed design boundaries, not silent substitutes.
