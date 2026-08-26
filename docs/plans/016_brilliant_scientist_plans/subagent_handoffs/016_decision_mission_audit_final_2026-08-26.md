# Event 016 final decision and mission audit

Date: 2026-08-26.

Status: Read-only source and MCP audit for the parent agent. No gameplay, localisation, decision, mission, raid, scripted GUI, or balance source was changed by this audit, and no commit was created.

## Scope and evidence boundary

The audit covers the Event 016 alien landing and D’Rhondan contact surfaces, D’Rhondan country decisions, hosted Directorate facilities, institutions, foreign and project-board decisions, containment responses, Directorate missions, Kruger-State decisions and missions, native Portal Warfare raids, scripted effects and triggers, script constants, localisation, and the Event 016 Directorate GUI.

The main source surfaces are `common/decisions/016_alien_infantry_landing_decisions.txt`, `common/decisions/016_dhrondan_contact_decisions.txt`, `common/decisions/016_dhrondan_country_decisions.txt`, `common/decisions/016_brilliant_scientist_containment_decisions.txt`, `common/decisions/016_brilliant_scientist_directorate_facilities.txt`, `common/decisions/016_brilliant_scientist_directorate_foreign.txt`, `common/decisions/016_brilliant_scientist_directorate_institutions.txt`, `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, `common/decisions/016_brilliant_scientist_directorate_synthesis.txt`, `common/decisions/016_brilliant_scientist_evolution_missions.txt`, the `016_brilliant_scientist_kruger_state_*` decision files, `common/raids/016_brilliant_scientist_portal_raids.txt`, and their Event 016 scripted effects, triggers, constants, and English localisation.

The current branch is `master` at `659895db2` (`docs: close current Event 016 improvement delta`). The requested baseline commit `18f7c7d67` and its descendants were reviewed; the descendants after that baseline are documentation or unrelated Event 006/famine changes. Event 016 gameplay source files in the inspected scope were clean in the worktree.

Required offline wiki pages were consulted from `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding. Vanilla documentation and precedents consulted include `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `common/raids/_documentation.md`, and the SOV paranoia scripted decision-category GUI precedent at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/SOV_paranoia_system_scripted_gui.txt` with its interface layout.

## Severity-ordered issue list

### P1 source gap: real Event 016 decisions exceed the four-spendable-cost ceiling

The accepted decisions-and-missions rules cap a gameplay-changing decision at four distinct spendable cost types. The current source exceeds that ceiling in several Event 016 families.

The hosted containment decisions in `common/decisions/016_brilliant_scientist_containment_decisions.txt:20-448` use a native Political Power `cost` and debit additional resources in `complete_effect`. `brilliant_scientist_arrest_kruger` has Political Power, Support Equipment, Infantry Equipment, manpower, and Army Experience, for five types. `brilliant_scientist_shutdown_directorate` has Political Power, Support Equipment, Motorized Equipment, trains, and fuel, for five types. `brilliant_scientist_ratify_sovereign_charter` has Political Power, convoys, trains, Motorized Equipment, and Support Equipment, for five types. `brilliant_scientist_launch_military_seizure` has Political Power, Support Equipment, Infantry Equipment, Motorized Equipment, fuel, manpower, and Army Experience, for seven types. `brilliant_scientist_exile_kruger` and `brilliant_scientist_request_foreign_containment` are four types, while release and concession are within the limit.

The three synthesis decisions in `common/decisions/016_brilliant_scientist_directorate_synthesis.txt:16-288` exceed the same limit when their factory commitments are counted as the real `civilian_factory_use` cost. `brilliant_scientist_prepare_high_speed_materials_trial` uses Political Power, Air Experience, Support Equipment, Motorized Equipment, fuel, manpower, and three civilian factories. `brilliant_scientist_establish_portal_calibration_network` uses Political Power, Support Equipment, Motorized Equipment, fuel, manpower, and two civilian factories. `brilliant_scientist_convene_cross_domain_review` uses Political Power, Support Equipment, Motorized Equipment, fuel, manpower, and two civilian factories.

The project-board stage families in `common/decisions/016_brilliant_scientist_directorate_project_board.txt:838-3154` are more severe. The 15 family portfolios use separate theory, deployment, and weaponization decisions. Deployment and weaponization stages consume Political Power, civilian factories, military factories, Support Equipment, trucks, trains, fuel, and manpower, with some families also consuming Army, Air, or Navy Experience. This is eight to eleven spendable types per stage before considering non-consumed strategic-resource access. The shared payment logic is visible at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:7-44` and the gates at `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:123-1681`.

The 15 project incident response decisions in `common/decisions/016_brilliant_scientist_directorate_project_board.txt:3597-4566` also use Political Power, a civilian-factory commitment, Support Equipment, trucks, fuel, and manpower, for six types. The payment helpers are `brilliant_scientist_pay_technical_incident_response`, `brilliant_scientist_pay_industrial_incident_response`, `brilliant_scientist_pay_biological_incident_response`, and `brilliant_scientist_pay_exotic_incident_response` at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1567-1635`.

Kruger-State project-batch decisions have the same problem. `brilliant_scientist_krg_pay_project_batch_cost` at `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt:60-65` spends Support Equipment, Motorized Equipment, fuel, and manpower, while its callers add a Political Power `cost`. Representative callers are `brilliant_scientist_krg_run_bounded_clone_growth_cycle` at `common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt:65-89`, `brilliant_scientist_krg_fabricate_alien_laser_batch` at `common/decisions/016_brilliant_scientist_kruger_state_canonical_and_exotic_decisions.txt:39-62`, and `brilliant_scientist_krg_fabricate_portal_transit_batch` at `common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt:213-241`. Each is five distinct spendables when the native Political Power cost is included.

Disposition: this is an implementation/design blocker for completion of the decision audit, not a balance preference. The parent should reduce each affected visible action to at most four spendable types or split the mechanic into separately understandable actions while preserving the accepted core intent.

### P1 source gap: hidden or non-icon cost presentation accompanies the over-budget actions

The affected actions expose only the Political Power value through native `cost` in the decision definition, while physical costs are debited in `complete_effect` or a helper. Their availability tooltips are not a replacement for an icon-first cost row.

Containment has no `custom_cost_text` in `common/decisions/016_brilliant_scientist_containment_decisions.txt`. Its requirement strings at `localisation/english/016_brilliant_scientist_containment_l_english.yml:20-26` spell out `Support Equipment`, `Infantry Equipment`, `manpower`, `Army Experience`, trucks, trains, fuel, and convoys as prose with no corresponding texticons.

The project-stage cost keys at `localisation/english/016_brilliant_scientist_projects_l_english.yml:18-...` likewise use strings such as `3 civilian factories, 2 military factories, 600 Support Equipment, 80 trucks, 8 trains, 500 fuel, 1400 manpower, 90 Political Power, access to 5 units of relevant strategic resources`. No texticons are present in those cost strings, and non-consumed strategic-resource access is mixed into the spendable-cost sentence.

The incident cost keys at `localisation/english/016_brilliant_scientist_projects_l_english.yml:571-574` are entirely literal resource-name prose. The synthesis keys at `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml:270-279` provide only one icon-like token, `£political_power`, which does not match the Event 016 usage of the standard `£pol_power` token, and leave all other spendables as literal names.

Disposition: the cost rows and blocked tooltips need an owner-applied redesign after the four-type decisions are chosen. Every remaining spendable must use the correct texticon, and non-consumed requirements such as strategic-resource access, facility validity, or factory availability must be separated from consumed costs.

### P2 queued: Portal beachhead active-state lifecycle has no consumer

`brilliant_scientist_portal_raid_establish_beachhead` at `common/scripted_effects/016_brilliant_scientist_raid_effects.txt:53-77` sets `brilliant_scientist_portal_beachhead_active` and `brilliant_scientist_portal_raid_breach_recorded`, changes the selected province controller, and creates the fixed Portal Breach Cadre. A repository-wide search found no Event 016 consumer that clears, expires, or transitions `brilliant_scientist_portal_beachhead_active`.

The separate state flags `brilliant_scientist_portal_raid_breach_recorded`, `brilliant_scientist_portal_raid_targeted`, `brilliant_scientist_portal_facility_extracted`, and `brilliant_scientist_portal_factory_extracted` can remain permanent history if that policy is accepted. The active beachhead flag needs an explicit transient-versus-permanent policy before it is used as a target lock or containment state.

Disposition: queued for a named Portal containment, spread, or beachhead owner. No new owner or cleanup system was invented during this audit.

### P2 queued: primary facility defense mission has no cancellation cleanup or refund contract

`brilliant_scientist_krg_primary_facility_defense_mission` at `common/decisions/016_brilliant_scientist_kruger_state_foundation_decisions.txt:544-572` has a 120-day timeout and a target-validating `cancel_trigger`, but no `cancel_effect`. Its start decision at `:513-542` pays the light material helper before activating the mission. If the primary facility or ownership becomes invalid, the mission is cancelled with no source cleanup and no refund. There is no active flag to clear, so the missing cleanup is not a proven stale-flag defect, but the sunk-cost behavior is not explicit in the mission tooltip.

Disposition: queued design decision. Either make the material commitment explicitly non-refundable in the player-facing tooltip and accepted design, or add a guarded cancellation refund/receipt contract. `brilliant_scientist_krg_maintenance_audit_mission` at `:699-727` does have cancellation cleanup and a distinct 180-day deadline.

### P2 blocked: required probability-auditor route and current decision/mission inspectors are unavailable

No callable `chaosx_ai_probability_auditor` is present in the tool inventory. The direct `mcp__hoi4_agent_tools__hoi4_probability_inspect` attempt against `common/decisions/016_dhrondan_contact_decisions.txt` timed out after 180 seconds for the decision AI route and the default route, with no artifact returned. Earlier direct routes for the D’Rhondan decisions and missions returned `PROBABILITY_SURFACE_EMPTY` when no supported decision/mission weighted surface was exposed. Therefore no current `probability_compare` pass is claimed.

No `hoi4.decision_inspect` or mission-specific inspector was exposed. Source review covers triggers, effects, target legality, timers, cleanup, and AI declarations, but it is not equivalent to an engine-backed decision/mission inspection.

Disposition: MCP evidence blocker only. Re-run the named auditor and compare the same rebellion, landing, expedition, Directorate, and Portal scenarios when the route is callable.

### P3 blocked: current GUI inspect failed after a corrected request; current GUI render is partial

The Event-owned GUI is `kruger_directorate_container`, attached by `brilliant_scientist_directorate_category` in `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt` and defined in `common/scripted_guis/016_brilliant_scientist_directorate_scripted_gui.txt` with layout `interface/016_brilliant_scientist_directorate.gui`.

The first current `hoi4.gui_inspect` request was rejected immediately with `GUI_SCENARIO_ID_DUPLICATE` because `event016_directorate_compact_current` was supplied both as the primary scenario and in `relatedScenarios`. The corrected request used unique IDs for the compact, expanded, and pressure scenarios, ran for approximately 125 seconds across bounded waits, and returned `INTERNAL_ERROR` with `Unexpected internal error`, `artifactCount: 0`, and no artifact or diagnostics.

The current `hoi4.gui_render` request completed with `GUI_RENDERED`, one artifact, and status `ok`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce/ab7035b380c130ddaa18ccdde154830bce7336e2def0b71154216d9367df4371/kruger_directorate_container-full.svg`. Reported SHA256 is `efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce`, size 727134 bytes. The response included `[MCP_RESPONSE_TRUNCATED]` with `actualBytes: 39776` and `maxBytes: 32768`; the full artifact was retained by the MCP workspace.

Historical inspect evidence from the GUI-worker attestation reports 22 Event 016 elements, with 194 modelled, 5 approximated, 7 ignored, 2 missing, 2 unsupported, and 7 unresolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7773e9a94e5f46dcfcc13649534f130b179fac8695618fa59744986158b4374a/7291dbc76ab889d8485f4de2b4b8aec4cf4f3bd86f9ca15ab64a2f8f04d962a4/gui-inspect.017d249c791c0735.json`. This historical result is not substituted for the failed current inspect.

Source review of the GUI found a 500x360 root with compact and full panels, one portrait/profile region, four visible meters, role/control text, footer, and open/close controls. It has no gameplay-changing buttons or spendable costs. No `hoi4.gui_rewrite` was used because this was an audit-only task.

## Resolved or source-supported findings

The alien landing path is structurally complete at source level after the country-owned registry correction in `common/scripted_effects/016_alien_infantry_api_effects.txt:301-327`. `alien_infantry_call_landing` at `common/decisions/016_alien_infantry_landing_decisions.txt:9-84` uses a state target, valid controlled/passable-state gates, a 2,000 Alien Laser Weapons reserve, and the seven-day `alien_infantry_landing_mission` at `:86-101`. The reservation helper refunds one proven reserve on cancellation/loss, clears the target and duration, and guards duplicate materialization.

The alien landing cooldown ladder is constant-backed at 30 days by default and 24, 18, or 12 days with accepted network, guarded-descent, or near-space upgrades. The owner-target registry correction is source-resolved, but dynamic two-provider transfer, duplicate registration, state loss, D’Rhondan capture, release, and Event 019 deferred-transfer behavior remain unproved without live or engine acceptance evidence.

The D’Rhondan contact category at `common/decisions/016_dhrondan_contact_decisions.txt:9-155` exposes a status row, mutually exclusive Kruger and Mengele expedition authorizations, the Honor Accord, and hidden route-specific missions. Each expedition spends 50 Political Power plus 500 fuel, uses a 180-day mission, has route-specific locks and cleanup, and does not cross-mutate the other envoy path. The rebellion pulse is country-scoped, lasts 90 days, and is gated by at least six arrivals, 30 Pact Strain, and 600 global Chaos; the accepted 10/20/40 branch math was evaluated by a bounded probability call but is not a current post-anchor probability comparison.

The D’Rhondan sovereignty category at `common/decisions/016_dhrondan_country_decisions.txt:9-198` uses state or country targets with revalidation at resolution. Reclamation has a 30-day native decision timer, a 90-day repeat cooldown, and a 365-day wargoal. Enclave support uses a 30-day timer and per-state completion marker. Postwar integration uses a 60-day timer and cancels if war resumes. The Two-World Compact validates an independent, non-warring, non-subject partner and owns an explicit invalidation path for the saved diplomatic target.

The native Portal pair in `common/raids/016_brilliant_scientist_portal_raids.txt:34-516` is structurally bounded. `brilliant_scientist_portal_facility_raid` targets a hostile controlled state with state-level industrial or strategic installations. `brilliant_scientist_portal_special_project_facility_raid` targets an exact tagged provincial facility. Both require weaponization technology, the fixed `Quantum Transit Raiders` template, at least six `portal_raider` battalions, 60 Teleportation Equipment, and 10 Command Power. Both use seven preparation days, a 30-day target re-enable time, native cancellation/expiry, and four outcome levels. Successful outcomes destroy the assigned source formation, preventing a free-unit loop. The state-target critical outcome intentionally calls the state extraction helper twice to match the `up to two` localization; this is not treated as an exploit.

The DHR landing, contact, sovereignty, and Portal cost rows that are already icon-first remain within four spendable types: landing uses one Alien Laser Weapons type with `£GFX_alien_laser_weapon_equipment_medium`; each expedition uses Political Power and fuel with `£pol_power` and `£fuel_texticon`; Honor Accord and DHR sovereignty actions use Political Power; Portal raids use Command Power and Teleportation Equipment with `£command_power` and `£teleportation_equipment_1_text_icon`.

No broad world iteration was found in the audited Event 016 decision/effect paths. State, country, event-target, and native raid contexts are used instead of a new world polling loop.

## Category lifecycle and cognitive-load notes

`alien_infantry_landing_category` has one player action and one hidden mission. It is within the six-action and active-mission limits, and its category and decision text explain reserve, timeout, refund, presence, strain, and cooldown.

`dhrondan_contact_category` has one non-actionable status row, two mutually exclusive expedition actions, one accord action, two route missions, and one rebellion mission. Its route and transaction locks prevent simultaneous Kruger/Mengele authorization. The mission count is acceptable, but current MCP cannot prove the rendered category row or blocked-state layout.

`dhrondan_sovereignty_category` has four primary actions, with target requirements separated from Political Power cost and with per-state completion markers. It stays within the visible-action limit.

`brilliant_scientist_raids` has two native raid actions and no custom scripted GUI. Preparation, reservation, target selection, and outcome history are owned by the native raid surface.

`brilliant_scientist_directorate_category` is declared once at `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt:9-22` but is appended by facilities, foreign, institutions, project-board, synthesis, containment, and evolution files. The category itself only gates current host or sovereign status and has `visible_when_empty = yes`; phase/route filtering is delegated to every individual decision. The constituent source contains dozens of visible decision IDs, including 45 project-stage decisions, 15 incident responses, containment responses, synthesis actions, and institutional/facility actions. This may be acceptable only if the individual gates reliably reduce each runtime phase to six or fewer primary actions. No decision-specific MCP listing was available to prove that scenario count.

The Directorate scripted GUI presents four meters, a portrait/profile frame, role/control state, and a footer. It does not show a raw unexplained value dump in source, but current inspect failure leaves visual fidelity and blocked-state presentation unverified.

The over-budget cost rows materially increase cognitive load even where the category is phase-gated. A player must remember factories, equipment, transport, fuel, manpower, experience, Political Power, and sometimes strategic-resource access from prose or hidden helper effects. The affected stage and containment designs do not meet the accepted four-cost presentation rule.

## Mission quality audit

| ID | Owner/category/region | Requirement and duration | Success/expiry | Failure or cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `alien_infantry_landing_mission` | Landing country, `alien_infantry_landing_category`, selected controlled state | Valid pending reserve and selected state; 7 days | One locked landing cohort, presence/strain receipt, cooldown, and registry insertion | Invalid control or reservation cancels and refunds one proven reserve | Pending flag, target pointer, and one-cohort guard |
| `dhrondan_kruger_expedition_mission` | Host country, `dhrondan_contact_category`, D’Rhondan route | Live Kruger route, envoy craft, no pact/transaction lock; 180 days | Audience/pact route and canonical-role restoration | Route failure clears obligation, role suspension, duration, and pending state | Route, obligation, expedition, and transaction locks |
| `dhrondan_mengele_expedition_mission` | Mengele-directorate country, contact category, D’Rhondan route | Independent Mengele route and envoy craft; 180 days | Independent audience/pact route | Failure clears its own route without mutating Kruger | Separate route and expedition flags |
| `dhrondan_rebellion_pulse_mission` | Pact host country, contact category, country-wide pulse | Pact, six arrivals, 30 strain, 600 Chaos; 90 days | 10/20/40 tier resolution in `dhrondan_resolve_rebellion_pulse` | Eligibility loss cancels; timeout has no `cancel_effect`, but no mission-specific transient state is set | One active mission and `dhrondan_rebellion_triggered` |
| `brilliant_scientist_sovereignty_deadline_mission` | Current host, Directorate category, hosted sovereignty board | `brilliant_scientist_sovereignty_deadline_active`; variable-backed duration | Timeout marks the deadline expired | Cancellation calls `brilliant_scientist_cancel_sovereignty_deadline` | Deadline active/resolved flags |
| `brilliant_scientist_loyalty_review_mission` | Current host, Directorate institutions, country-wide review | Security section and paid review request; 45 days | Snapshot-based loyalty resolution and cleanup | Host loss clears `brilliant_scientist_security_action_in_progress` | Security action and review-request flags |
| `brilliant_scientist_krg_primary_facility_defense_mission` | Kruger State, foundation category, primary facility state | Valid owned/controlled primary facility; 120 days | Defense completion flag and Army Experience | Target loss cancels without `cancel_effect` or refund contract | No active mission flag is left, but paid sunk cost is ambiguous |
| `brilliant_scientist_krg_maintenance_audit_mission` | Kruger State, foundation category, primary facility/project-force context | Maintenance action and operational evidence; 180 days | Completed audit and runtime package rebuild | Cancellation clears active/objective state; timeout calls success or fail helper | Active flag and objective flags are explicitly cleared |
| `brilliant_scientist_krg_transit_breach_closure_mission` | Kruger State, portal/temporal category, terminal context | Closure route and operational evidence; 90 days | Breach closed and stability receipt | Cancellation clears active/objective state; timeout calls success or fail helper | Active flag, objective flags, and closed marker |
| `brilliant_scientist_krg_temporal_stabilization_supervision_mission` | Kruger State, portal/temporal category, temporal target context | Pending stabilization and strategic factory capacity; 120 days | Stabilization completion and pending-state cleanup | Civil-war/invalid route cancels or calls temporal rescue failure helper | Supervision active, pending, and post-rescue flags |
| `brilliant_scientist_krg_singularity_disarmament_hold_mission` | Kruger State, terminal category, singularity programme | Global weapons dismantled and no terminal/fallout lock; 180 days | Durable hold completion and threat-source refresh | Terminal/arming/fallout invalidation clears active hold | Active and completion flags plus terminal commitment flags |
| `brilliant_scientist_portal_facility_raid` / `brilliant_scientist_portal_special_project_facility_raid` | Native `brilliant_scientist_raids`, hostile state/province target | War, control, destination, technology, six raiders, 60 equipment, 10 Command Power; 7-day preparation | Native failure/limited/success/critical result; successful levels establish breach and extract targets | Native cancellation, expiry, history, and 30-day re-enable | Native operation lock and source division destruction |

The 15 Directorate project incident missions are family-specific and use constant-backed technical, industrial, biological, or exotic response deadlines of 60, 90, 120, or 150 days. Their responses use active/resolved flags, a dedicated cancel tooltip, and family-specific failure cleanup, but their six-type cost design remains the P1 issue above.

## Cost and requirement clarity audit

| Surface | Representative identifiers | Spendable types found | Icon/visibility result | Disposition |
| --- | --- | --- | --- | --- |
| Alien landing | `alien_infantry_call_landing` | 1 | Correct Alien Laser Weapons texticon in category, description, requirement, and effect keys | Source-supported |
| D’Rhondan expeditions | `dhrondan_send_kruger_to_dhronda`, `dhrondan_send_mengele_to_dhronda` | 2 | `£pol_power` and `£fuel_texticon` are visible in descriptions and effect text | Source-supported |
| Portal raids | Two native raid types | 2 | Native Command Power and Teleportation Equipment costs are defined; outcome text is localized | Source-supported, outcome probability still unproved |
| Directorate facilities/foreign | Campus, prototype works, secondary lab, relocation, joint lab | Usually 3-4 including Political Power | Physical costs are mostly hidden in available checks/effects; individual cost text audit is still needed | Queued after global cost reduction |
| Containment | Arrest, shutdown, charter, military seizure | 5, 5, 5, and 7 respectively | Native row shows Political Power; requirements are literal-name prose with no texticons | P1 redesign |
| Synthesis | High-speed trial, portal calibration, cross-domain review | 7, 6, and 6 including factory commitments | `£political_power` plus literal names; no icon coverage for other spends | P1 redesign |
| Project stages | All 15 families, deployment and weaponization | 8-11 depending family and experience spends | Literal prose cost keys and mixed consumed/non-consumed requirements | P1 redesign |
| Project incidents | Technical, industrial, biological, exotic response families | 6 each including factory commitment | Literal prose cost keys with no texticons | P1 redesign |
| Kruger-State batches | `brilliant_scientist_krg_pay_project_batch_cost` callers | 5 including Political Power | Helper costs are hidden in complete effects and call-site tooltips | P1 redesign |

Requirement text generally revalidates live state, route, target, peace, facility, and capacity conditions. The exact gap is that consumed costs and non-consumed requirements are often mixed in one prose tooltip, while the native decision cost row does not expose the helper debit.

## AI validity and route locks

Alien landing AI scores only valid state targets and is gated by contact, reserve, pending, cooldown, and world-end checks. The D’Rhondan expedition routes use deterministic Kruger-first selection when both routes are available; this is safe and avoids duplicate payment but is not probability-proven as a balance choice.

D’Rhondan sovereignty AI uses the same target validation as the player path. Compact partner validation rejects dead, subject, warring, NAP, and existing-compact targets. Portal raid AI zeroes invalid actors and targets and applies Kruger-host, Kruger-State, major-target, capital, and facility factors after native readiness/target checks.

Kruger-State decision triggers use `brilliant_scientist_krg_decisions_are_active`, route-specific focus/technology flags, live stockpile gates, and explicit retry/capacity flags. The project-batch and foreign-operation helpers are reusable, but their cost visibility and probability behavior remain unproven by the unavailable custom auditor.

No invalid dead-country target, impossible border route, or broad world iteration was proven in the reviewed DHR/landing/Portal paths. Engine-level target acceptance remains unavailable for the decision and mission surfaces.

## Localisation and tooltip gaps

Event 016 DHR landing/contact/country and Portal localisation keys are present and generally explain thresholds, consequences, timers, and route identity. The rebellion mission text exposes the six-arrival, Pact Strain, Chaos, and 10/20/40 outcome thresholds.

The primary localisation gap is cost presentation, not missing identifiers. Containment, project, incident, and synthesis cost keys use literal resource names, omit required texticons, or use the nonstandard `£political_power` token. The project-stage cost strings also combine consumed values with strategic-resource access requirements and factory commitments in long comma-separated prose.

The current Directorate GUI source has dynamic labels for Mandate, Dependence, Exposure, and Capacity, plus role/control text. Historical MCP metadata reported missing font glyphs and ignored tooltip fields in the offline renderer; these are renderer fidelity limitations, not proof of missing source localisation. Fresh inspect did not complete.

## Cleanup and exploit-risk notes

Alien reservation cleanup is guarded and idempotent around one recorded 2,000-weapon reserve. Kruger and Mengele cleanup are route-specific. The compact offer owns explicit invalidation and global-target cleanup. DHR state decisions use per-state markers and revalidate before effect application.

Portal success destroys the source formation, and facility extraction checks destination capacity before removing the selected source facility. No free-unit loop, free-equipment loop, core spam, or cooldown bypass was proven in the reviewed source.

The unresolved Portal active beachhead marker is the material stale-state risk. The primary-facility-defense mission has an explicit cancellation/refund ambiguity. The new over-budget cost findings are player-clarity and balance-contract risks rather than proven duplication exploits.

Correction for the concurrent route-consumer tranche: the five D’Rhondan focus support flags are consumed by existing decisions/triggers and are not dead flags. `dhrondan_alien_components_standardized` and `dhrondan_orbital_office_reassembled` feed paid-landing AI, `dhrondan_laboratory_route_complete` feeds enclave-supply gates and weights, `dhrondan_predictive_warfare_perfected` feeds reclamation gates and weights, and `dhrondan_access_map_exchange_ready` gates Covenant compact offers. The authoritative consumer table is in `016_focus_tree_audit_final_2026-08-26.md`; no duplicate decisions are needed.

## MCP evidence and exact limits

Event state-flow inspection for `chaosx.nr16.47` returned `EVENT_INSPECTED_PARTIAL` with revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94eaa4862016956958bae29a2fba697a0e3f1efd857ff96c4fbb3381c76ccb38/cf509287edc5293ffdfebfa2f78ddcd1972b2ee23764f5d60435b01fa7a2b23b/event-state_flow-f588a2607444.json`. The partial result reported `MCP_INLINE_FILES_TRUNCATED` and unresolved large-workspace nodes; it supports event-chain structure but cannot prove runtime variable/array scope.

The bounded probability evaluation for the D’Rhondan rebellion branch returned the accepted LOW/MEDIUM/HIGH 10/90, 20/80, and 40/60 arithmetic. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e6b12c1c58d429149c8cfd862db1eb27fa2828abe9b019d28f7742f5b3bc5d5/4f8da02cda90ddb1005a32456c01c0b3f80491073478574d0c2381ef2d085338/probability-ce533f32be4dd0efbce3f9f8.json`. This proves branch arithmetic only and is not a fresh `chaosx_ai_probability_auditor` compare.

The current GUI render artifact and exact inspect errors are recorded in the P3 blocker above. The historical GUI inspect artifact is retained as context only. No GUI rewrite was attempted.

## Concrete recommended fixes

1. Assign an owner to reduce containment, synthesis, project-stage, incident-response, and Kruger-State project-batch decisions to at most four distinct spendable types, preserving factory commitments only where the accepted design explicitly needs them.

2. Add icon-first cost localisation for every remaining spendable and separate non-consumed target, technology, route, peace, facility, capacity, and strategic-resource requirements into custom trigger tooltips. Replace `£political_power` with the repository-standard Political Power texticon where applicable.

3. Decide and document whether `brilliant_scientist_portal_beachhead_active` is transient. Add a named Portal containment/spread transition or keep it as permanent history only after target-lock semantics are explicitly specified.

4. Decide whether primary-facility-defense material is sunk on target invalidation. If it is refundable, add a guarded receipt/refund path; if not, state the non-refundable commitment in the decision and mission localisation.

5. Run `chaosx_ai_probability_auditor` with the same named landing, expedition, rebellion, Directorate, and Portal scenarios, then perform a `probability_compare` pass. Direct route timeout or `PROBABILITY_SURFACE_EMPTY` must not be presented as equivalent evidence.

6. Re-run `hoi4.gui_inspect` and `hoi4.gui_render` for compact/full, hover, disabled, warning, and long-text states after the current MCP route is responsive. Current render success with a truncation diagnostic is useful artifact evidence but not a clean inspect/render acceptance pair.

7. Keep or assign the five D’Rhondan focus support flags rather than adding duplicate consumer decisions without an accepted design owner.

## Validation and completion boundary

Meaningful validation completed: required offline wiki and vanilla documentation review, vanilla scripted GUI precedent review, source-level decision/category/mission/raid inspection, static cost-count and texticon audit, target/route/AI/cleanup review, exact localisation-key review for the audited surfaces, bounded Event 016 state-flow inspection, bounded rebellion probability arithmetic, and current GUI inspect/render attempts with exact errors and artifacts recorded.

Skipped meaningful validation: live HOI4 execution, savegame playtest, current decision/mission-specific MCP inspection because no route was exposed, fresh custom probability-auditor/compare execution because the auditor was unavailable and direct inspection timed out, and GUI rewrite/post-change comparison because this task forbids source patches.

No source edits or gameplay commits were made by this audit. The handoff is evidence-only and does not claim in-game completion. Completion remains blocked by the over-budget/hidden cost designs, the Portal active-beachhead lifecycle decision, the primary-facility-defense cancellation/refund contract, unavailable decision/mission/probability MCP routes, and the failed current GUI inspect.

Handoff path: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_decision_mission_audit_final_2026-08-26.md`.
