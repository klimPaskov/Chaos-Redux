# Event 006 Decision and Mission Map Handoff

## Scope and status

This handoff covers the dedicated Event 006 decision layer only. The source map in `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` contains exactly 59 rows; the implementation contains exactly 59 decisions or missions, one `# DM-XX` marker for every row, 59 name keys, 59 description keys, and 59 `ai_will_do` blocks.

The local decision surface is implemented without a political-power store, passive resource drip, daily/weekly/monthly country sweep, fallback formable tag, or repeatable free-unit reward. Parent-owned shared consumers listed below remain required before Event 006 as a whole can be called complete. The twelve stable decision sprites were already registered with final DDS assets by the Event 006 gameplay-icon tranche.

## Files changed by this subagent

- `common/decisions/006_independence_wave_decisions.txt`
- `common/decisions/categories/006_independence_wave_categories.txt`
- `common/script_constants/006_independence_wave_decision_constants.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_decision_mission_map_handoff.md`

No shared gameplay file, GFX file, asset, focus file, event file, on-action file, or spreadsheet was edited in this subtask. No commit was created.

## Manual 59-row matrix audit

| ID | Implemented action | Manual implementation audit |
|---|---|---|
| DM-01 | `independence_wave_secure_provisional_capital` | Auto-starting 75-day live capital-garrison mission; capital loss, inadequate assigned divisions, or origin end cancels it; success and failure write different founding values. |
| DM-02 | `independence_wave_establish_revenue_service` | Selectable 150-day founding mission with administration cost and civilian-factory burden; opens revenue tools or produces a salary crisis. |
| DM-03 | `independence_wave_register_population` | Auto-starting 150-day census mission with factory burden and an administration payment on success; capital loss or severe instability fails it. |
| DM-04 | `independence_wave_hold_first_assembly` | Selectable constitutional-route mission with administration cost, live legitimacy/capital gates, success route flag, and failure faction pressure. |
| DM-05 | `independence_wave_confirm_traditional_authority` | Selectable traditional-route mission with suitability/unlock gates, administration cost, success route flag, and refusal outcome. |
| DM-06 | `independence_wave_recruit_local_civil_servants` | One-shot 75-day administration project; pays manpower/command/factory capacity and raises domestic capacity with low patron exposure. |
| DM-07 | `independence_wave_recall_exile_administrators` | One-shot 75-day diplomatic project; consumes a transport channel and trades patron exposure for capacity and recognition. |
| DM-08 | `independence_wave_retain_former_host_officials` | One-shot 45-day host-linked project; requires a living former host, pays vetting/administration cost, and records host influence and domestic backlash. |
| DM-09 | `independence_wave_create_provincial_compacts` | State-targeted 120-day project with administration cost, autonomy/control tradeoffs, and generation-safe per-state completion markers. |
| DM-10 | `independence_wave_establish_treasury_and_currency` | Selectable 240-day treasury mission; pays administration/factory burden, creates economic infrastructure on success, or records inflation failure. |
| DM-11 | `independence_wave_send_diplomatic_mission` | Country-capital-targeted 75-day mission with transport/command cost, recognition/refusal branches, one-active-action gate, and target cooldown. |
| DM-12 | `independence_wave_request_former_host_recognition` | Former-host-targeted 120-day negotiation with material diplomatic stake and accepted/refused settlement branches; cancels on host death or origin end. |
| DM-13 | `independence_wave_seek_regional_guarantee` | Patron-capital-targeted 120-day action; pays diplomatic materials, can obtain a real guarantee and recognition, and has a major target cooldown. |
| DM-14 | `independence_wave_accept_arms_limit_recognition` | One-shot treaty decision; accepts a live offer, grants recognition, records backlash, and applies a 720-day arms-limit flag through a duration variable. |
| DM-15 | `independence_wave_build_permanent_foreign_service` | Selectable 300-day recognized-state mission with administration/factory burden; success opens the permanent service and failure records overrun/patron staffing. |
| DM-16 | `independence_wave_coordinate_recognition_campaign` | Network-targeted 180-day shared campaign; pays diplomatic capacity and changes target recognition plus sender/league standing with a target cooldown. |
| DM-17 | `independence_wave_integrate_militias` | Selectable 180-day security mission; consumes manpower, equipment, support equipment, and army experience; integrates the pool or creates a warlord crisis. |
| DM-18 | `independence_wave_secure_depot` | State-targeted 120-day depot operation with real security materials, control checks, and generation-safe state markers. |
| DM-19 | `independence_wave_recall_defecting_officers` | One-shot 45-day security action with command/equipment cost and officer, organization, infiltration, and instability consequences. |
| DM-20 | `independence_wave_form_border_guards` | Selectable 180-day security mission with manpower/equipment cost; creates border-readiness state or an abuse/autonomy failure. |
| DM-21 | `independence_wave_open_volunteer_corridor` | Patron-capital-targeted 120-day corridor with transport, fuel, and diplomatic costs; registers a bounded patron channel and cancels if the route becomes hostile. |
| DM-22 | `independence_wave_raise_emergency_units` | One-shot severe-threat decision. It first spends the major security package, then creates exactly two understrength divisions from the already researched Event 006 template under fixed unit id 60022, plus one capital fort. DM-23 or origin cleanup deletes only id 60022 with `disband = yes`. |
| DM-23 | `independence_wave_professionalize_army` | Selectable 360-day mission with major security cost; establishes a durable professionalization tier or records militia resistance/cost overrun, and demobilizes DM-22 formations on success. |
| DM-24 | `independence_wave_offer_ceasefire_line` | Former-host-targeted 75-day negotiation with diplomatic stake and acceptance/refusal branches; a successful offer executes real white peace when applicable. |
| DM-25 | `independence_wave_divide_state_property` | One-shot former-host-targeted 180-day negotiation; pays administration resources and updates the property/obligation ledger and bilateral settlement. |
| DM-26 | `independence_wave_negotiate_citizenship_and_return` | One-shot former-host-targeted 240-day negotiation; pays administration resources and updates population movement, tension, and instability ledgers. |
| DM-27 | `independence_wave_accept_limited_claims` | One-shot host-offer decision; pays diplomatic cost, records claim renunciation and recognized separation, and applies the intended legitimacy/ambition tradeoff. |
| DM-28 | `independence_wave_demand_recognition_by_force` | Former-host-targeted 120-day ultimatum with strategic cost and strength gates; produces recognition or a reclamation-conflict opening. |
| DM-29 | `independence_wave_offer_association_or_reunion` | Former-host-targeted 240-day vote/negotiation; on voluntary reunion it invokes decision cleanup and shared origin end before host annexation. |
| DM-30 | `independence_wave_prepare_reclamation_defense` | Selectable 75-day emergency mission with major security cost, fort/readiness success, surprise failure, and cancellation when threat ends or host war begins. |
| DM-31 | `independence_wave_accept_arms_mission` | Patron-targeted 75-day mission; the sponsor sends real infantry/support equipment and the action registers a bounded patron influence/aid channel. |
| DM-32 | `independence_wave_accept_industrial_credits` | Patron-targeted 240-day project with administration/factory burden, infrastructure/industry output, debt/concession state, and generation-safe target marker. |
| DM-33 | `independence_wave_invite_security_advisers` | Patron-targeted 120-day mission; pays diplomatic materials, adds a security channel, and creates actionable interference evidence and patron exposure. |
| DM-34 | `independence_wave_grant_base_or_transit_rights` | One-shot patron-targeted long treaty; pays strategic cost, applies a 720-day rights flag through a duration variable, grants a real guarantee, and records concession/backlash. |
| DM-35 | `independence_wave_balance_patrons` | Repeatable 240-day mission requiring two channels; every repeat escalates from diplomatic-standard to an added administration-light cost and uses a 365-day cooldown. |
| DM-36 | `independence_wave_buy_out_concession` | One-shot patron-targeted 240-day buyout with strategic cost; clears the concession and materially reduces the selected patron's influence. |
| DM-37 | `independence_wave_expose_foreign_interference` | Risky patron-targeted 45-day action; evidence and legitimacy select success/scandal branches, with real recognition/aid/security consequences and target cooldown. |
| DM-38 | `independence_wave_choose_client_future` | One-shot route decision; requires a dominant patron and strategic commitment, locks the patron-client route, and closes incompatible autonomy choices. |
| DM-39 | `independence_wave_recognize_new_independence_wave_country` | Instant Event-6-country-targeted recognition with diplomatic cost and 180-day cooldown; raises target recognition and both network standings, and angers only a living former host. |
| DM-40 | `independence_wave_send_civil_service_cadres` | Network-targeted 120-day mission with administration/factory burden; transfers capacity/instability value to the target and standing to the sender. |
| DM-41 | `independence_wave_contribute_emergency_reserve` | Repeatable instant league contribution; consumes exactly one currently safe surplus channel (equipment, trains, convoys, or fuel), records the contribution, and has a 180-day cooldown. |
| DM-42 | `independence_wave_request_collective_recognition` | League/network-targeted 180-day campaign with diplomatic/factory burden; success raises recognition/confidence and target standing, while valid cancellation applies cohesion loss. |
| DM-43 | `independence_wave_request_border_arbitration` | League-member-targeted 120-day case with diplomatic cost, settlement/refusal branches, league standing effects, and a 365-day cooldown. |
| DM-44 | `independence_wave_rescue_threatened_member` | Threatened-member-targeted 75-day crisis; immediately sends real equipment and a guarantee, rewards survival/peace, and applies abandonment penalties only while the requester remains active. |
| DM-45 | `independence_wave_convene_founding_congress` | Selectable 300-day congress contribution with strategic/factory cost; registers a founder, advances the shared league state machine, or calls shared congress failure. |
| DM-46 | `independence_wave_adopt_charter_pillar` | Sequential paid vote action. Five uses set the five charter pillars; the fifth maps the focus proposal flag to the matching shared league-route constant and proclaims the formal league. |
| DM-47 | `independence_wave_challenge_league_leadership` | Selectable 120-day vote mission with strategic cost, standing/contribution comparison, leader-scope update, confidence/cohesion effects, and crisis lockout. |
| DM-48 | `independence_wave_survey_claimed_districts` | State-targeted 120-day survey with administration/factory burden; records local support and generation-safe ambition-state results. |
| DM-49 | `independence_wave_sponsor_plebiscite` | Surveyed-state-targeted 240-day operation with strategic cost; local support drives transfer/claim/scandal outcomes and generation-safe state settlement markers. |
| DM-50 | `independence_wave_negotiate_transfer` | Surveyed-state-targeted 180-day bilateral mission with strategic compensation; resolves peaceful transfer or host pressure and records a generation-safe state result. |
| DM-51 | `independence_wave_prepare_border_ultimatum` | Surveyed-state-targeted 120-day crisis with combined strategic and major-security cost; transfer/refusal logic can create a dynamic state-specific `take_state_focus` wargoal through `meta_effect`. |
| DM-52 | `independence_wave_integrate_settled_district` | Controlled-state-targeted 360-day integration with administration/security/factory burden; grants a core, infrastructure, and generation-safe integration marker. |
| DM-53 | `independence_wave_discover_regional_identity` | One-shot 120-day family-gated discovery project with administration/factory burden; reveals the selected family requirements and records foreign alarm through values. |
| DM-54 | `independence_wave_convene_formation_congress` | Selectable 360-day formation mission with strategic/factory cost and legitimacy/recognition/capacity gates; records congress consent or failure. |
| DM-55 | `independence_wave_proclaim_military_union` | One-shot military/radical proclamation with strategic plus major-security cost. It publishes a selected-family commit request and deliberately does not invent a fallback tag. Shared registry consumption is mandatory. |
| DM-56 | `independence_wave_integrate_member_region` | Formable-state-targeted 540-day integration with administration/security/factory burden; grants a core and infrastructure and uses generation-safe one-time state markers. |
| DM-57 | `independence_wave_sponsor_another_breakaway` | Evolution-5 state-targeted 180-day covert operation with diplomatic, security, and factory costs; publishes a bounded sponsored-state record for the next wave plan. |
| DM-58 | `independence_wave_coordinate_reclamation_fronts` | Selectable 180-day radical-league mission with strategic/security/reserve gates; marks every registered member ready, consumes reserve/cohesion, or enters league crisis on failure. |
| DM-59 | `independence_wave_transform_league_charter` | Selectable irreversible 180-day leader/founder vote with strategic cost; sets the radical league route, removes low-standing non-radical members, and records the danger milestone. |

## Passive/checklist and free-unit audit

- DM-01 and DM-03 are the only automatically activated missions. DM-01 is a live capital-control and assigned-division objective; DM-03 continuously occupies a civilian factory and fails on capital loss or severe instability. Neither is a focus-completion checklist or a passive resource generator.
- All other timed missions are player-selectable or targeted, pay a material/administrative/diplomatic/security package, and have success, timeout, cancellation, or target invalidation behavior.
- DM-22 is the only decision-layer `create_unit` call. It is `fire_only_once`, severe-threat gated, pays 10,000 manpower, 1,000 infantry equipment, 200 support equipment, and major army experience before creating two 70%-manpower/65%-equipment formations. The fixed create-unit id has one matching `delete_unit` path on professionalization and origin cleanup. There is no repeatable free-unit loop.
- DM-31 and DM-44 move equipment that already exists in a sponsor/member stockpile through `send_equipment`; DM-41 removes one real surplus resource channel. No action manufactures a repeatable stockpile reward.

## DM-55 selected-formable commit contract

`independence_wave_decision_request_selected_formable_commit` performs no tag fallback. When DM-55 is paid and completed it sets, on the acting country:

- country flag `independence_wave_formable_commit_pending`
- variable `independence_wave_formable_commit_request_date = global.date`

The shared package/formable registry must consume this request only after resolving its already selected family. Its transaction must:

1. Revalidate family selection, family territory, congress consent, route, and the current origin generation.
2. Apply the family-specific tag or cosmetic tag, claims/cores, member consent/annexation, capital, name, and flag transaction.
3. Set `independence_wave_formable_active` on the surviving country so DM-56 becomes available.
4. Clear `independence_wave_formable_commit_pending` and `independence_wave_formable_commit_request_date` on success, rejection, cancellation, or stale generation.
5. Retire obsolete pre-formation operations without clearing the post-formation/formable unlocks needed by DM-56. The full `independence_wave_cleanup_decision_layer` is an origin-end cleanup and should not be used wholesale unless the consumer deliberately re-establishes the surviving post-formation state.
6. Record failure consequences rather than substituting any generic tag if the family transaction cannot be completed.

Current shared dependency: a package/formable selector must set `independence_wave_formable_family_selected` and retain its family-specific identifier. The focus layer's `independence_wave_formable_family_registered` flag is not, by itself, the selected-family contract used by DM-53 through DM-55.

## DM-57 sponsored-state output contract

On successful completion, the targeted state is added once to `global.independence_wave_sponsored_breakaway_states` and receives:

- state flag `independence_wave_dm57_sponsorship_active`
- scope variable `independence_wave_sponsoring_country = ROOT`
- variable `independence_wave_sponsorship_generation = ROOT.independence_wave_generation_id`
- variable increment `independence_wave_sponsored_opening_strength += constant:independence_wave_decision_gate.sponsorship_opening_strength`
- variable `independence_wave_sponsored_route = constant:independence_wave_government_route.radical_sovereignty`

The shared wave planner must consume this array before candidate scoring is frozen. For every entry it must validate the state, sponsor scope, and sponsor generation; add the opening-strength and radical-route biases to that exact candidate; then remove the array entry and clear the state flag and all four state variables on consumption, rejection, stale generation, or invalidation. It must not silently substitute another state.

## Required parent/root wiring

1. Resolved by the parent: `independence_wave_end_active_origin` calls `independence_wave_cleanup_decision_layer = yes` while the country is still scoped and before league/network/patron unregister calls or `independence_wave_active_origin` is cleared. Generation reset uses the same cleanup, including demobilization of DM-22 unit id 60022.
2. Preserve `independence_wave_force_package_applied`, `independence_wave_anchor_state`, `independence_wave_force_profile`, the generated force template, and `GetIndependenceWaveForceTemplateName` after opening setup. DM-22 refuses to activate without the real package and persisted anchor; there is no fallback template.
3. Implement the DM-55 selected-family consumer exactly as specified above.
4. Implement the DM-57 sponsored-state planner consumer and full stale-entry cleanup exactly as specified above.
5. The shared reclamation/claim planner must consume `independence_wave_reclamation_front_ready` on registered league members plus global flag `independence_wave_reclamation_fronts_coordinated`, issue only compatible synchronized ultimatums/wars, and clear all ready/global state when resolved, rejected, dissolved, or stale.
6. The shared league layer must enforce a single live founding congress globally, not merely one per country, and must clear/rebuild league leader/congress leader pointers, five charter flags, `independence_wave_radical_charter_active`, `independence_wave_reclamation_fronts_coordinated`, and member readiness flags on league reset/dissolution.
7. The focus layer must set the ten unlock flags consumed here and one of the five charter proposal flags before DM-46's final vote. Those identifiers are listed below.
8. Evolution 5 must set global flag `independence_wave_evolution_5_open_sovereignty_enabled`; without it DM-57 through DM-59 remain correctly locked.
9. Resolved dependency: `interface/006_independence_wave.gfx` defines all twelve stable sprite ids listed below, and every referenced DDS is tracked under `gfx/interface/decisions/006_independence_wave/`.

## Focus and league flag dependencies

Decision unlock flags:

- `independence_wave_unlock_first_assembly`
- `independence_wave_unlock_traditional_authority`
- `independence_wave_unlock_foreign_service`
- `independence_wave_unlock_professional_army`
- `independence_wave_unlock_forced_host_recognition`
- `independence_wave_unlock_patron_client_route`
- `independence_wave_unlock_league_congress`
- `independence_wave_unlock_border_ambitions`
- `independence_wave_unlock_formable_discovery`
- `independence_wave_unlock_high_chaos_actions`

DM-46 proposal flags:

- `independence_wave_charter_proposal_defensive_congress`
- `independence_wave_charter_proposal_development_compact`
- `independence_wave_charter_proposal_sovereign_equality`
- `independence_wave_charter_proposal_armed_liberation`
- `independence_wave_charter_proposal_radical_revisionist`

The fifth DM-46 pillar maps the selected proposal to the matching `independence_wave_league_route.*` value, calls `independence_wave_proclaim_formal_league`, and clears all five proposal flags. There is no default route.

## Localisation and sprite dependencies

The English file contains all 118 decision name/description keys, all 11 category titles and descriptions, and all dynamic cost strings. The final file must remain UTF-8 with BOM.

Required stable sprites:

- `GFX_decision_independence_wave_recognition_actions`
- `GFX_decision_independence_wave_government_actions`
- `GFX_decision_independence_wave_army_integration_actions`
- `GFX_decision_independence_wave_depot_border_actions`
- `GFX_decision_independence_wave_former_host_negotiations`
- `GFX_decision_independence_wave_patron_aid`
- `GFX_decision_independence_wave_patron_balancing`
- `GFX_decision_independence_wave_network_aid`
- `GFX_decision_independence_wave_league_votes`
- `GFX_decision_independence_wave_border_arbitration`
- `GFX_decision_independence_wave_formable_proclamation`
- `GFX_decision_independence_wave_integration_missions`

## Meaningful validation evidence

- Exact source/implementation cardinality: 59 CSV rows, 59 decision blocks, 59 `# DM-XX` markers, 59 names, 59 descriptions, and 59 AI blocks.
- Timed-operation teardown audit: every decision containing `days_remove` or `days_mission_timeout` has explicit origin-end cancellation; cancellation penalties are guarded so origin teardown does not create false league/founding failures.
- Per-state repeat-safety audit: DM-09, DM-18, DM-32, DM-48, DM-49, DM-50, DM-51, DM-52, and DM-56 pair their state marker with the acting origin generation.
- Dynamic tuning audit: 165 distinct `constant:` references resolve; the gameplay decision/effect/trigger/category files contain no numeric gameplay literals.
- Resource integrity audit: exactly one `create_unit` call and one matching id-filtered `delete_unit` call exist in this decision layer; sponsor aid and league reserve actions consume real source resources.
- Localisation coverage audit: all 140 required name/description/category keys resolve, and no `:0` keys are present.

## Simplifications, omissions, and blockers

No fallback or deliberately weaker substitute was used inside the owned decision files. Root cleanup and the twelve-sprite contract are resolved. The decision layer is not independently shippable until the parent-owned DM-55, DM-57, DM-58, and global league lock/reset contracts above are implemented. The remaining items are integration blockers, not optional polish, and Event 006 should remain incomplete if any one of them is absent.
