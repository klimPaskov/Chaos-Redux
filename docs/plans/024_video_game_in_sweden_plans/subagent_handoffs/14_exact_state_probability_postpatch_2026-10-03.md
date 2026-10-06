# Event 24 Postpatch AI Probability Audit

Audit date: 2026-10-03.

Workspace: C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux.

Status: incomplete. The source patch is reviewed against immutable BEFORE and AFTER copies. Child-local HOI4 tools were not callable. Parent probability_inspect and probability_compare calls were dispatched but each timed out after 600 seconds. No engine probability result or numerical balance signoff is available.

This handoff is read-only with respect to gameplay. It records the owner-applied exact-comparator and reassessment-affordability patch, source inventories, scenario assumptions, the missing child-local MCP route, unresolved conclusions, and separate owner follow-ups. This audit created only the seven immutable copies in the POSTPATCH snapshot folder and this handoff. No gameplay, AI, event, decision, trigger, effect, constant, localisation, asset, workbook, skill, or live-game file was edited by this audit. No commit was made.

## Scope and accepted evidence

The accepted source documents read in full for this audit were:

- docs/specs/024_video_game_in_sweden_specs/024_video_game_in_sweden_ai_probability_scenarios.md
- docs/specs/024_video_game_in_sweden_specs/024_video_game_in_sweden_decision_map.md
- docs/specs/024_video_game_in_sweden_specs/024_video_game_in_sweden_spec_part_1_core.md
- docs/specs/024_video_game_in_sweden_specs/024_video_game_in_sweden_spec_part_2_evolutions.md
- docs/plans/024_video_game_in_sweden_plans/subagent_handoffs/13_exact_state_probability_baseline_2026-10-03.md

The audited weighted surfaces are the three opening options in chaosx.nr24.2, three route-report options in chaosx.nr24.20, fourteen incident response options in chaosx.nr24.30, three reassessment options in chaosx.nr24.50, seven native random-list incident families in video_game_in_sweden_roll_incident, and all eighteen decision ai_will_do entries in video_game_in_sweden_program_category.

The preserved accepted scenario IDs are P24_FINAL_OPENING_MATRIX with P24-O1 through P24-O4, P24-C1 through P24-C7, P24-D1 through P24-D5, and P24-I1 through P24-I5. No new scenario IDs were created.

## Immutable source identities and comparison binding

The AFTER copies below were copied once before probability requests and SHA-256 checked against the source bytes at capture time. They were not recopied. All later comparison references in this handoff mean these frozen files, never subsequent live source.

The decision source files are byte-identical across the two snapshots. Their phase-helper changes are located in separate scripted-trigger and scripted-effect files. No decision_ai_will_do compare result is claimed to include those helper changes. Such dependency coverage remains unresolved unless the parent confirms a supported source-binding method for the decision definitions and their helper files.

| Weighted source or identity cross-check | Immutable BEFORE path and SHA-256 | Immutable AFTER path and SHA-256 | Capture result |
| --- | --- | --- | --- |
| events/024_hearts_of_iron.txt | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_hearts_of_iron.txt, 5f628f1c1718fea7fc9171e46c3a2530101a3749ecfedc9ca288e3212f862420 | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_hearts_of_iron.txt, 05c9f3eda8ac693e16d4d309dee0c0ebafb1e2e3fd96106ecbe279db6b8bb9dc | Match at capture, 34,233 bytes |
| common/decisions/024_video_game_in_sweden_decisions.txt | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden_decisions.txt, dc1ea5273d6f22cfe8361c8d8ba176d344fc4ba98865f62a2145455d694f7f30 | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_video_game_in_sweden_decisions.txt, dc1ea5273d6f22cfe8361c8d8ba176d344fc4ba98865f62a2145455d694f7f30 | Byte-identical BEFORE and AFTER, 38,595 bytes |
| common/scripted_effects/024_video_game_in_sweden_effects.txt | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden_effects.txt, 9336e28c7eca010c16b24242926a85e633a5083a2f8c049269aeec587c4c9622 | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_video_game_in_sweden_effects.txt, e8354f2c9c1e4c3abf759b03730c8f906d75103959d93c31ffa7cc16f765d7f3 | Match at capture, 122,630 bytes |
| common/scripted_triggers/024_video_game_in_sweden_triggers.txt | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden_triggers.txt, 875b061004f7122c0599825409d9345b532ea38b38ac1addcc19c11965bf58e5 | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_video_game_in_sweden_triggers.txt, b960aa50ab2f8c40fe1a988278f4058e72dbd0ba47678384a87bd6a0c67c1751 | Match at capture, 29,541 bytes |
| common/script_constants/024_video_game_in_sweden_constants.txt | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden_constants.txt, 622621c00d24cf036cf3fec3f1f82949db6d92b3af4701af396bef4e132d632c | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_video_game_in_sweden_constants.txt, 622621c00d24cf036cf3fec3f1f82949db6d92b3af4701af396bef4e132d632c | Byte-identical BEFORE and AFTER, 14,364 bytes |
| common/ideas/024_hearts_of_iron_ideas.txt | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_hearts_of_iron_ideas.txt, 04e14b1b74d5ec5fd862f45d9eaa16524c6316d6e986856618b9eb603e7af97c | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_hearts_of_iron_ideas.txt, 04e14b1b74d5ec5fd862f45d9eaa16524c6316d6e986856618b9eb603e7af97c | Byte-identical BEFORE and AFTER, 3,756 bytes |
| common/scripted_localisation/024_video_game_in_sweden.txt | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_video_game_in_sweden.txt, 5844548f94a997a80db45d8950a3848dd6b589a73037e137f9dcef5cbeb0acbf | docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_video_game_in_sweden.txt, 5844548f94a997a80db45d8950a3848dd6b589a73037e137f9dcef5cbeb0acbf | Byte-identical BEFORE and AFTER, 11,117 bytes |

The weighted comparison inputs are therefore frozen as follows: events/024_hearts_of_iron.txt, common/scripted_effects/024_video_game_in_sweden_effects.txt, and common/scripted_triggers/024_video_game_in_sweden_triggers.txt from the PRE and POST snapshot folders. Decisions and constants are identical across the two snapshots. The owner reports that baselinepre_cleanup exact copies also exist for the later lifecycle edits. Those files are outside this comparison.

After the snapshot confirmation, the parent reported additional nonweighted lifecycle changes in the live scripts: .90 runs maintenance only while program_active, close_program is idempotent through program_closed, the RealityCheck Stockholm check adds AND inside NOT to reject either loss, and the 365-day condition uses NOT flag days < 365 with the existing flag check. The parent reports no AI weight, incident weight, or candidate-pool changes in that cleanup. These later live files were not read, rehashed, copied over, or compared here. No result in this handoff includes those later changes.

The parent later reported civil-war and commander changes in the current live chaosx.nr24.99 path and stated that they do not change weights. A read-only search of the frozen Event24 AFTER event, effect, trigger, and decision copies found no chaosx.nr24.99 identifier. These reported later changes are outside the captured source identity and were not independently reviewed.

## Live MCP route status and exact comparison blocker

Subsequent parent relay: the parent dispatched probability_inspect through its live route for adapter event_option_ai_chance, the three chaosx.nr24.20 candidates, the frozen POST event path, refresh enabled, and workspace mod_chaos_redux_ea3b2d67c2c0. The request is awaiting a result in parent cell65. This child cannot access that cell and has received no inspect artifact or result.

The parent identified docs/testing/runtime_repairs/20260913_cxt_history_followup/facility_probability_corrected/scenarios.json as a generic custom-pool fixture. A read-only parse of that file confirmed schemaVersion 1.0, top-level id and scenarios, and scenario entries shaped as id, label, and state with named state facts. It contains 31 facility scenarios and its SHA-256 is 5ad132cf47dfacb40cad570d3f483ce33a275d6c1cebe17b8abc27011bacc5d3. The state object has no numeric index-like keys. It confirms custom-pool envelope shape only and does not prove native Event24 variable binding, host flags, or option eligibility.

The parent proposed a bounded chaosx.nr24.30 comparison using the same 13 conditional response points before and after, with named scenario facts for phase, route, current_incident, and last_incident. The generic custom-pool fixture confirms outer envelope shape only. It does not establish that event_option_ai_chance binds these state facts to native Event24 variables. No new scenario IDs or numeric array indices should be introduced. Native binding, host validity, flags, and response eligibility remain unresolved unless the adapter proves them and returns poolComplete. In particular, P24-I3 current_incident = 6 covers the workplace response point only. current_incident = 7 for the party response remains a separate unresolved trace. P24-I5 current_incident = 0 is a before-draw point and does not prove response-option coverage. No .30 compare result has been returned to this child.

Parent-side relay update received after this handoff was first written: a fresh hoi4.reference_search for flagdays, hoi4.event_inspect lint for root24, and hoi4.event_render options for chaosx.nr24.20 each timed out awaiting tools/call after 600 seconds. No artifact URI was returned for those requests. The parent reports that no valid probability_compare has run because the inspect timeout left the scenario fixture contract or request schema unavailable. The parent will try schema discovery through its route. The compare remains outstanding.

Final parent relay for the postpatch inspect: the parent dispatched adapter event_option_ai_chance for chaosx.nr24.20.a, .20.b, and .20.c, using the frozen AFTER events/024_hearts_of_iron.txt path, refresh enabled, and workspace mod_chaos_redux_ea3b2d67c2c0. It timed out awaiting tools/call after 600 seconds. No artifact, source revision, candidate rows, poolComplete, scenario hash, or raw inspect data was returned.

Final parent relay for the postpatch comparison: the parent dispatched event_option_ai_chance for the complete fourteen-option chaosx.nr24.30 pool, using the frozen PRE and POST events/024_hearts_of_iron.txt paths and a bounded P24-I1 through P24-I5 envelope probe with thirteen conditional response points. It timed out awaiting tools/call after 600 seconds. No artifact, revision, poolComplete, scenario hash, candidate IDs, or raw comparison data was returned. Native variable binding and P24-I5 before-draw response coverage were unconfirmed before the call, so no numerical claim follows. The parent did not dispatch numeric compares for .50, decisions, or random-list helpers. Those surfaces remain unresolved.

The relayed .30 compare used BEFORE path docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_hearts_of_iron.txt and AFTER path docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_hearts_of_iron.txt. Its declared candidatePool was chaosx.nr24.30.terrain_a, chaosx.nr24.30.terrain_b, chaosx.nr24.30.supply_a, chaosx.nr24.30.supply_b, chaosx.nr24.30.enemy_a, chaosx.nr24.30.enemy_b, chaosx.nr24.30.template_a, chaosx.nr24.30.template_b, chaosx.nr24.30.diplomatic_a, chaosx.nr24.30.diplomatic_b, chaosx.nr24.30.workplace_a, chaosx.nr24.30.workplace_b, chaosx.nr24.30.party_a, and chaosx.nr24.30.party_b.

The relayed .20 inspect used AFTER path docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_hearts_of_iron.txt and candidatePool chaosx.nr24.20.a, chaosx.nr24.20.b, and chaosx.nr24.20.c, with refresh enabled and workspace mod_chaos_redux_ea3b2d67c2c0. It timed out before returning result identifiers or candidate data.

The child-local tool registry was checked before requests. It exposes no callable mcp__hoi4_agent_tools probability, event, reference, or source-lookup route and therefore exposes no live schema in this child context. The only child-local registry names containing hoi4 at this check were Blender-specific authoring tools. The parent now reports that its probability inspect and compare routes are callable. No parent-side server health, server version, connected workspace ID, or probability tool schema was returned to this child.

The required first postpatch probability_inspect lookup was attempted before any source probability interpretation. It failed locally because mcp__hoi4_agent_tools__hoi4_probability_inspect was absent from the live tool registry. No request reached an MCP server.

The mandatory probability_compare was attempted before any further inspect retry, using nonempty before.path and after.path values for the frozen event source:

- BEFORE: docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_exact_state/024_hearts_of_iron.txt
- AFTER: docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/024_hearts_of_iron.txt

The client returned TypeError: tools[name] is not a function because mcp__hoi4_agent_tools__hoi4_probability_compare is absent from the live tool registry. The attempt failed before schema validation or server dispatch. A valid identical scenarioSet could not be supplied or checked because the live schema is unavailable. The comparison status is BLOCKED and NOT DISPATCHED. There is no comparisonId, analysisId, scenarioHash, sourceRevision, unresolved-row artifact, or rendered URI from this turn.

The same child-local registry check found no probability_evaluate, probability_sweep, probability_render, event_inspect, event_render, reference_context, reference_search, reference_read, or source_lookup routes. They were not dispatched by this child. The previous handoff records 600-second service timeouts for some older requests. This turn did not time out. The direct child dispatch blocker was the missing callable route in this child context, not absence of a route in the parent's environment.

Historical MCP context from the predecessor handoff only:

- Prior workspace ID: mod_chaos_redux_ea3b2d67c2c0.
- Prior opening artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f67017802db38f3033f13c7da9155822c60531c6a14b23fded978d1f2370fda7/2c77c3ee1582b4997563595f327f82e7b135bd12bbad5dfe8fcacd85f7952c09/probability-cb60cb3ec67ba407e5c9dec4.json.
- Prior decision-inspect artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6586c8819613196ac2c29345e39353cb6799c6a626201fdca2f87539c95a189/b9c23bef38b88d6c6e6ef6cf9f5bd97e7326017f85e1b5f22e31c91dee24ce13/probability-inspect-d07e33ab2f93.json.

Those artifacts do not bind to the immutable 2026-10-03 PRE and POST source hashes and are not accepted as this comparison. No fresh MCP artifact, revision, scenario hash, comparison ID, or render exists for the current patch.

## Verified source delta

The frozen PRE to POST source diff contains 79 explicit compare = equals additions to check_variable tests: 17 in events/024_hearts_of_iron.txt, 39 in common/scripted_effects/024_video_game_in_sweden_effects.txt, and 23 in common/scripted_triggers/024_video_game_in_sweden_triggers.txt. The changes repair phase, route, incident-family, and zero or one sentinel identity tests. Deliberate numeric threshold comparisons were not changed.

In chaosx.nr24.50.c, events/024_hearts_of_iron.txt now requires both video_game_in_sweden_can_restrict_use = yes and video_game_in_sweden_can_pay_restriction = yes. The matching restriction affordability trigger already exists in common/scripted_triggers/024_video_game_in_sweden_triggers.txt and the normal restriction decision uses it. This is an availability change, not a numerical weight change.

The three source diffs contain no changed ai_chance bases, ai_chance factors, ai_will_do bases, ai_will_do factors, random-list weights, or script constants. The decisions and constants source files are byte-identical between BEFORE and AFTER. Source inspection therefore confirms the comparator and affordability delta, but cannot confirm engine evaluation, pool completeness, or scenario rankings.

The targeted scan found no ai_strategy_factor token in the five frozen weighted gameplay source files.

## Weighted surface inventory and raw traces

The values below are source bases and named modifiers from the frozen source and predecessor inventory. They are not evaluated scores, normalized shares, or balance conclusions.

| Surface | Source candidates | Base values and raw modifiers | Candidate and external-factor completeness |
| --- | --- | --- | --- |
| Opening options, chaosx.nr24.2 | chaosx.nr24.2.a Controlled Staff Trial, .2.b Civilian Commercial Release, .2.c Competitive Officer League | Bases 4.0, 3.0, 2.0. Named factors include peace 1.8, low stability 0.5, commercial stability 1.5, wartime commercial 0.4, wartime officer 2.0, low army experience 1.4, supply crisis 0.25, and severe-crisis factors 8.0, 0.0, 0.25 in route order. | Three definitions are present. Runtime eligibility, host binding, event targets, and complete external factors are unknown to MCP. |
| Route report, chaosx.nr24.20 | chaosx.nr24.20.a, .20.b, .20.c | Each base is 1. The triggers compare the route enum to controlled, commercial, or officer using explicit equality. | Three definitions are present. The accepted O scenarios describe the pre-route opening. No separate accepted post-route report fixture is specified. |
| Incident response, chaosx.nr24.30 | terrain_a, terrain_b, supply_a, supply_b, enemy_a, enemy_b, template_a, template_b, diplomatic_a, diplomatic_b, workplace_a, workplace_b, party_a, party_b under chaosx.nr24.30 | All bases are 1. Named factors are supply-crisis overconfidence 0.25, enemy red-team 2.0, enemy supply 0.2, template separate-policy 1.8, template supply 0.25, workplace protected-shifts 1.8, workplace war 0.2, party democratic 1.7, and party supply 0.2. | Fourteen definitions are present. Exact incident identity is explicit in the frozen AFTER source. Other trigger state and event-option pool completeness are unknown to MCP. |
| Reassessment, chaosx.nr24.50 | chaosx.nr24.50.a, .50.b, .50.c | Bases 3.5, 2.0, and 4.0. Named factors include the Reality Audit supply factor 2.0, the Dual-Track stability factor 1.6, and route-specific factors. No factor was multiplied by hand. | Three definitions are present. The .50.c affordability gate is now explicit. Live eligibility and affordability remain unevaluated. |
| Incident selection, video_game_in_sweden_roll_incident | video_game_in_sweden_incident_terrain_weight, _supply_weight, _enemy_weight, _template_weight, _diplomatic_weight, _workplace_weight, and _party_weight | Native random_list bases are 2.0, 3.0, 2.0, 2.0, 2.0, 2.0, and 2.0 in that order. The effect loads each from video_game_in_sweden_incident.*_weight constants and applies state-dependent logic before drawing. | Seven family definitions are present. Current family validity, cooldown state, cadence, and the dynamically positive pool are unknown to MCP. |
| Decision category, video_game_in_sweden_program_category | All eighteen IDs listed in the next table | ai_will_do base scores are listed below. Modifier traces are score components and are not click probabilities. | Eighteen weighted definitions are present. Exact phase tests are explicit after the patch. Runtime availability, host state, affordability, target validity, and category pool completeness are unknown to MCP. |

The eighteen decision ai_will_do bases are:

| Decision ID | Raw base score |
| --- | --- |
| video_game_controlled_exercise | 1 |
| video_game_logistics_module | 2 |
| video_game_expand_access | 1 |
| video_game_conclude_trial | conclude_low_value = 4 |
| video_game_rules_revision | 1 |
| video_game_field_validation | validation_caution = 2.5 |
| video_game_red_team | red_team_caution = 2 |
| video_game_officer_league | 1 |
| video_game_national_league | 1 |
| video_game_protect_shifts | 1 |
| video_game_preparedness_clubs | 1 |
| video_game_foreign_licenses | foreign_interest = 2 |
| video_game_separate_policy | 2 |
| video_game_begin_reality_audit | audit_crisis = 3.5 |
| video_game_narrow_reality_audit | audit_crisis = 3.5 |
| video_game_dual_track | 2 |
| video_game_restrict_use | restrict_crisis = 4 |
| video_game_trust_model | trust_safe = 1.5 |

Decision modifier traces retained from the frozen source inventory:

- P24-D1: Logistics Module has supply factor 2.0 and peace factor 0.3, plus route factors.
- P24-D2: Field Validation has supply factor 0.0, low-stability factor 0.5, and mismatch factor 3.0.
- P24-D3: National League has war factor 2.5, low-war-support factor 2.0, and supply factor 0.35. Protect Shifts has war factor 3.0 and distraction factor 2.0.
- P24-D4: Foreign Licensing has foreign-interest base 2.0 and war factor 0.2, plus route factors. The decision source has no direct blockade or usable-convoy-route predicate.
- P24-D5: Conclude Trial has peace factor 1.8 and war factor 0.4.
- P24-C5 and P24-C7: Reality Audit has supply factor 2.0 and low-stability factor 0.5. Dual-Track has stable factor 1.8, red-team factor 1.5, and supply factor 0.5. Restriction has crisis factor 2.0 and peace factor 0.1. Trust the Model has crisis and low-stability factors 0.0, plus war factor 1.5.

The option pools use ai_chance. Their normalized option share, if available, would be conditional on the event firing and on the complete set of options eligible at that event. Decision ai_will_do entries are willingness scores in the decision race and do not state a click probability. The native random_list uses positive eligible family weights for a probability-proportional draw. These three mechanisms are kept distinct.

## Named scenario points and completeness

The source candidate definitions are complete at the file inventory level for the six requested surfaces. MCP poolComplete was not returned for any of them. Runtime eligible candidates and external factors are therefore incomplete or unknown in every scenario. The source inventory is not evidence of an exact normalized pool.

| Scenario set | Frozen source surface and candidate pool | Declared point retained from the accepted matrix or predecessor | Missing state and external factors |
| --- | --- | --- | --- |
| P24_FINAL_OPENING_MATRIX, P24-O1 through P24-O4 | chaosx.nr24.2, three opening options | Before route selection: phase 1, route 0, current incident 0, last incident 0. O1 is calm democratic peace. O2 is calm democratic rearmament. O3 is militarized wartime Sweden. O4 is emergency defense. | Exact numeric stability, experience, supply, fuel, host scope, Stockholm control, event flags, and external modifiers were not supplied. |
| P24-O1 through P24-O4 for chaosx.nr24.20 | Three route-report definitions exist, but the accepted O cases concern the opening choice | No separate post-choice report state is defined. The source route identities are 1, 2, and 3. | No report-specific fixture was constructed. Rebinding the pre-choice O scenarios to post-choice state would be an unsupported assumption. |
| P24-C1 | Evolution I option context, outside chaosx.nr24.50 | Phase 2, route 1, current incident 0, last incident 0. Stable democratic Evolution I. Route 1 is an explicit audit assumption. | Exact stability, host binding, affordability, field and red-team flags remain missing. |
| P24-C2 | Evolution I option context, outside chaosx.nr24.50 | Phase 2, route 3, current incident 0, last incident 0. Militarized wartime Evolution I. Route 3 is an explicit audit assumption. | War, experience, supply, validation, route flags, and option eligibility remain unbound. |
| P24-C3 | Evolution II option context | Phase 3, route 2, current incident 0, last incident 0. Strong industry and high tension. Route 2 is an explicit audit assumption. | Industry, public reach, stability, and policy-separation state remain unbound. |
| P24-C4 | Evolution II option context | Phase 3, route 2, current incident 0, last incident 0. Factory and stability crisis. Route 2 is an explicit audit assumption. | The scenario has no numeric stability point. Relevant source cutoffs are 0.20, 0.35, and 0.50. |
| P24-C5 | chaosx.nr24.50 and the Evolution III decision pool | Phase 4, route 1, current incident 0, last incident 2. Supply failure and lost core. Route 1 and the previous supply incident are explicit audit assumptions. | The matrix does not distinguish a historical supply-crisis flag from a current supply gap. A current gap blocks Reality Audit. Fuel, trains, host, and restriction affordability remain unresolved. |
| P24-C6 | chaosx.nr24.50 and the Evolution III decision pool | Phase 4, route 3, current incident 0, last incident 0. Stable high-Chaos militarized Sweden. Route 3 is an explicit audit assumption. | Numeric stability, supply reserves, active war goal, Chaos tier, and route flags remain unbound. |
| P24-C7 | chaosx.nr24.50 and the Evolution III decision pool | Phase 4, route 1, current incident 0, last incident 0. Near capitulation. Route 1 is an explicit audit assumption. | The matrix does not specify surrender progress. The maximum-risk route uses a strict cutoff below 0.75. The restriction payment floor may also invalidate .50.c. |
| P24-D1 | All eighteen decisions | Phase 1, route 1, current incident 0, last incident 0. Logistics action under train shortage. | The accepted state must separate an existing crisis flag from current stock. A current shortage below the three-train gap threshold conflicts with the four-train Logistics cost. |
| P24-D2 | All eighteen decisions | Phase 2, route 1, current incident 0, last incident 1. Field Validation after mismatch. | Divisions, supplied regions, equipment, fuel, trains, and mismatch flags remain unbound. |
| P24-D3 | All eighteen decisions | Phase 3, route 2, current incident 0, last incident 0. National League during total mobilization. | Factory output, war-production pressure, stability, and decision availability inputs remain unbound. |
| P24-D4 | All eighteen decisions | Phase 3, route 2, current incident 0, last incident 0. Foreign Licensing while blockaded. | Convoy stock and access, valid partners, autonomy, and recipient scope remain unbound. Source inspection found no direct blockade or usable-route gate. |
| P24-D5 | All eighteen decisions | Phase 1, route 1, current incident 0, last incident 0. Conclude Trial ignored baseline. | Program age must meet the 120-day review condition, reliance must be below 50, and no mission may be active. Exact host and flags remain unbound. |
| P24-I1 | Seven-family random_list and conditional .30 response | Random-list state phase 2, route 1, current incident 0, last incident 0. Conditional response current incident 1. Terrain mismatch. | War or exercise state, recent terrain validation, host, cooldown, and scheduled changes remain unbound. |
| P24-I2 | Seven-family random_list and conditional .30 response | Random-list state phase 2, route 1, current incident 0, last incident 0. Conditional response current incident 2. Supply mismatch. | Current stocks, war state, and whether the supply-crisis flag is historical or current remain unbound. |
| P24-I3 | Seven-family random_list and conditional .30 response | Random-list state phase 3, route 2, current incident 0, last incident 0. Conditional workplace response current incident 6. Party response current incident 7 requires its own trace. | Public reach, league state, party appropriation, host, and previous-family state remain unbound. |
| P24-I4 | Seven-family random_list and conditional .30 response | Random-list state phase 4, route 1, current incident 0, last incident 0. Conditional response current incident 5. Diplomatic category error. | A meaningful living diplomacy target and active diplomacy flag are not specified. |
| P24-I5 | Seven-family random_list | Random-list state phase 2, route 1, current incident 0, last incident 2. Recent supply family is an explicit audit assumption. | The matrix says one family fired recently but does not name it. Other current validity and cooldown facts remain unbound. |

Dates, Swedish host and event-target bindings, state control, scope types, flags, cooldown transitions, exact stocks, and scheduled state changes were not MCP-validated. No JSON scenario fixture was written because no live scenario schema was available. The numeric phase, route, and incident enums are audit fixture assumptions from the predecessor inventory, not new design values.

## Bounded findings and result classification

| Finding | Classification | Evidence and limit |
| --- | --- | --- |
| Seventy-nine omitted enum or sentinel comparisons now specify equals. | Exact source delta | Snapshot diff counts are 17 event, 39 effect, and 23 trigger additions. Runtime semantics were not engine-validated. |
| Exact phase and route tests no longer use the documented inclusive default. Exact incident-family, last-family, and sentinel checks are explicit. | Bounded | The offline Data structures page says omitted compare defaults to greater_than_or_equals. The installed documentation lists compare tokens but does not state the default. No MCP or game result was obtained. |
| chaosx.nr24.50.c requires the restriction affordability helper. | Exact source delta, bounded runtime effect | The frozen event source contains the new predicate. Actual resource availability and option selection were not evaluated. |
| Raw ai_chance and random-list values and decision ai_will_do bases. | Score-only source inventory | No hand multiplication or normalized probability claim is made. |
| Event option shares, random-list probabilities, decision rankings, dominance, starvation, or rank reversals. | Unresolved | No probability inspect, evaluate, sweep, or compare result exists. MCP poolComplete, unresolved inputs, and scenario hashes are absent. |
| Incident repetition rate and dynamic eligible-family completeness. | Unresolved | The exact last-family and zero-sentinel source tests are repaired. Runtime cadence, positive pool, event order, and cooldown transitions were not analyzed. |
| Positive scores on impossible, dead, hidden, blocked, or route-incompatible candidates. | Unresolved except for bounded source gates | Route and phase identities are explicit in the snapshot. Host, target, affordability, and event-gate evaluation are unavailable. |
| Evolution MTTH timing distributions. | Not present in the five frozen weighted gameplay sources, no timing result | Targeted source scan found no mtth: or mean_time_to_happen. The event timing path in the predecessor review uses day counters. P24-E1A through P24-E3B were not evaluated. |

The affordability gate can leave a collapse scenario with no affordable reassessment option. .50.a requires the Reality Audit start and payment predicates. .50.b requires Dual-Track validity and payment. .50.c now requires restriction validity and affordability. The predecessor source inventory states that restriction affordability has a 30 political-power floor plus stability and war-support floors of 0.04. No engine scenario tested whether one option remains available during collapse. This is a bounded starvation risk, not a measured result.

P24-C5 remains input-ambiguous. A current campaign supply gap blocks Reality Audit, while the scenario expectation ranks Reality Audit first after supply failure. The scenario must say whether the incident reflects an earlier supply crisis with current reserves recovered or an active current gap.

P24-D1 has a related state ambiguity. A live train shortage that crosses the current supply-gap threshold can conflict with the four-train Logistics cost. The fixture needs to distinguish shortage history from current available stock.

P24-D4 remains unresolved because source inspection found no direct blockade or usable-convoy-route predicate on Foreign Licensing. Convoy access, valid partner, subject autonomy, and recipient scope were not evaluated.

No dominance, starvation, rank-reversal, repetition, snowball, exploit, or balance conclusion is signed off numerically. The exact-source fixes make those future scenario comparisons more meaningful, but source changes alone do not establish an improved ordering.

## Owner follow-up, separate from this comparison

The restriction emergency route needs a separate resource-safe design patch. Keep the accepted goal that restriction is the emergency resolution route during collapse, and resolve how it remains available when the existing affordability floor disables every recovery choice without permitting silent partial payment. The affected identifiers are chaosx.nr24.50.c, video_game_in_sweden_can_pay_restriction, video_game_in_sweden_can_restrict_use, video_game_in_sweden_pay_restriction, and video_game_in_sweden_start_restriction. The relevant files are events/024_hearts_of_iron.txt, common/scripted_triggers/024_video_game_in_sweden_triggers.txt, common/scripted_effects/024_video_game_in_sweden_effects.txt, and common/decisions/024_video_game_in_sweden_decisions.txt.

That work requires a fresh baseline after current lifecycle cleanup, an owner-applied patch, and a new probability_compare using the same named crisis scenarios. Keep P24-C5 and P24-C7 in the core comparison and include the complete three-option .50 pool. Use P24-C1 through P24-C7 only for their applicable scenario surfaces. Do not reuse this handoff as that baseline and do not include the later patch in the current comparison.

Also resolve the P24-C5 supply-state distinction and declare the P24-D1 stockpile point and P24-D4 blockade, convoy, partner, autonomy, and scope inputs before the next valid probability evaluation. No numerical weight or threshold target is recommended here.

## Owner-planned baseline controlled-exercise effect adjustment

After the 79-comparator AFTER snapshot, the owner preserved additional current pre-debrief snapshots before a separate effect-only repair. The verified files are:

| Snapshot | Bytes | SHA-256 |
| --- | --- | --- |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_baseline_debrief/024_video_game_in_sweden_effects.txt | 122,484 | c33505451dfdacd23f56975478b1241adf694069f749bcf4c7ceb03dc490170c |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_baseline_debrief/024_video_game_in_sweden.txt | 11,117 | 5844548f94a997a80db45d8950a3848dd6b589a73037e137f9dcef5cbeb0acbf |
| docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_pre_baseline_debrief/024_hearts_of_iron_l_english.yml | 43,141 | 4f102147d2934a10b3371d860c532bafabc128efd767bb0a08fefe54d5dc6b5f |

The pre-debrief effects snapshot shows video_game_in_sweden_do_controlled_exercise at lines 781-790 applies the configured first reliance gain of 3, then the repeat gain of 1. The frozen constants source already has video_game_in_sweden_reliance.controlled_debrief_loss = 4 at post_exact_state/024_video_game_in_sweden_constants.txt:121, and the named loss is unused in the pre-debrief effects snapshot. This confirms the owner-described input values at source level. It does not verify the planned effect edit or campaign trajectory.

The owner plans to apply controlled_debrief_loss after either exercise gain, producing the owner-stated net Reliance changes of -1 for the first exercise and -3 for repeats. The owner states the three existing resource costs, availability gates, and AI weights will remain the same, with no extra modifier, asset, or localisation change. This is a planned effect adjustment, not a numerical AI-weight edit. It is not present in the immutable pre-debrief snapshot and is outside the frozen 79-comparator comparison.

The owner-stated route is Officer start 62, rail review to 57, then controlled exercises to 56, 53, 50, and 47, allowing ordinary closure below 50 at Chaos 0 without an evolution. This trajectory is not a probability result or a runtime validation. Future timing and reliance-sensitive choices remain unbalanced and unvalidated. No comparison or numerical signoff for this effect adjustment is claimed.

The seven POST exact-state copies were rehashed after the new pre-debrief captures and still match the identities in the frozen source table above. The 79-comparator comparison remains bound only to post_exact_state. The additional current effect and localisation snapshots do not change that comparison.

## Reference evidence

The required reference MCP routes are absent from the child-local tool registry. The relevant local documentation sections were read directly:

- paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:566-609. SHA-256 and prior MCP source revision: 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4. This section documents the check_variable compare choices and the omitted default greater_than_or_equals.
- paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:571-586. SHA-256 and prior MCP source revision: abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06. This section lists the comparison types and trigger syntax.
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:2110-2131. SHA-256 and prior MCP source revision: 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29. This section lists equals, not_equals, strict comparisons, supported scopes, and examples. It does not state the omitted-comparator default.

The prior successful reference-context call returned source headings only and no artifact URI. The prior reference-read and source-lookup calls timed out as recorded in handoff 13. No new reference artifact or source lookup was obtained.

## Skipped analyses and blockers

- probability_inspect was the required first audit request. The child route was absent. The parent .20 request reached its route and timed out after 600 seconds with no artifact.
- probability_compare was attempted before any further child inspect retry. The child route was absent. The parent .30 request reached its route and timed out after 600 seconds with no artifact, so no before/after numeric comparison exists.
- probability_evaluate and probability_sweep were unavailable. No exact or bounded modifier trace, threshold result, or rank reversal was returned.
- probability_render was unavailable and no analysisId existed. No ranking, matrix, sensitivity, comparison, or unresolved view URI exists.
- event_inspect and event_render were unavailable. No structural event-chain artifact or render path exists.
- probability_simulate was not justified because the accepted scenarios provide no declared distributions, correlations, or seed contract. Its route was also absent.
- probability_sequence was not applicable to the native random_list. No complete custom-pool manifest declares cadence, transitions, recovery, caps, cooldowns, removals, resets, timers, and terminal states. Its route was absent.
- P24-F1 through P24-F5 foreign-response scenarios were outside handoff 13 exact-state comparison scope and were not re-audited.
- P24-E1A through P24-E3B evolution timing scenarios were not analyzed because no MTTH-backed surface was found in the frozen weighted sources. No timing distribution is reported.
- No in-game simulation or live game was run. No tests were added or run.

## Files, skills, and handoff status

Files created for this audit: docs/plans/024_video_game_in_sweden_plans/subagent_handoffs/14_exact_state_probability_postpatch_2026-10-03.md and the seven immutable copies in docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-03_post_exact_state/.

Skills read: chaos-redux-subagents, chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-mtth.

Handoff disposition: incomplete. The immutable AFTER copies bind the requested patch comparison inputs. Parent inspect and .30 compare calls both timed out after 600 seconds without artifacts. Native Event24 variable binding and P24-I5 response coverage remain unresolved. The .50, decision, and random-list compares remain undispatched. No numerical balance signoff is provided.
