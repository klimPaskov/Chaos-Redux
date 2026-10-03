# Event 021 Active-War Evolution I Probability Baseline

Audit status: incomplete baseline handoff. The live probability and event MCP calls returned no result or artifact within bounded waits, so no timing, normalized probability, ranking, dominance, starvation, or rank-reversal conclusion is MCP-certified.

The audit began before active Evolution I eligibility and decision-access changes. The current decision and trigger sources still contain the pre-change gates, and a source search found none of the proposed active review or management-ready identifiers. The shared parent-effects file did change during this audit for the existing secondary-front receipt guard and the accepted non-weighted evolution-log actor selector. That change is part of the current pre-access baseline recorded below.

Only this Markdown handoff is written by the auditor. No gameplay, AI, event, decision, mission, MTTH, constant, localisation, or runtime file was changed. No game was launched, no tests were run, and no Git index or commit operation was performed. This report is not completion of the Event 021 goal.

## Scope and acceptance basis

The accepted source design is docs/plans/021_random_civil_war_plans/event021_active_war_evolution_i_repair_addendum_2026-10-03.md, SHA-256 DF445809E442475AC3108FCD19B449334C6F1638F4FD2D36678D7141F5B113DF. Its disposition records the parent acceptance of an active-war review, genuine no-side management, source-owned receipts, and fail-closed provenance handling. The user specifically required the baseline before active eligibility or decision-access edits.

The named master design is docs/specs/021_random_civil_war_specs/021_random_civil_war_master_spec.md, SHA-256 1FA87CA057ED0AFF79C7C21B89A976153E0A8C94A1388BD0DA157EDDB5CFD1BE. Its Evolution I section distinguishes a live-war entry from a pre-fire evolved opening and expects management access when no side is viable. The existing probability scenario matrix is docs/specs/021_random_civil_war_specs/021_random_civil_war_probability_scenario_matrix.md, SHA-256 50DA56FD4DA0B9BB85BB2C741A5845F3F0C8D805C17F66D23231A906701204E0.

## Audited surfaces and current source identities

| Surface | Exact source or identifier | Current local SHA-256 | Snapshot status |
| --- | --- | --- | --- |
| Evolution I timing entry | common/mtth/021_random_civil_war_mtth.txt, random_civil_war_evolution_i_days | 7982F0768B8ED04AE7154BCFF8CBDAC33589F8F7B031CFE12353F625891881C1 | No immutable before copy in the supplied snapshot directory |
| Evolution scheduling and callback | common/scripted_effects/021_random_civil_war_parent_effects.txt, event021_parent_select_evolution_mtth_actor, event021_parent_schedule_evolution_due_date, event021_parent_process_evolution_schedule, event021_parent_apply_evolution_i | 0DBD60BF8259F6848413F84DB79F988D6D29CABB26FA09C283066A7A03E1DF61 | Supplied parent copy is stale |
| Evolution activation and capacity | common/scripted_effects/021_random_civil_war_effects.txt, event021_apply_evolution_i and event021_refresh_global_capacity | 6D9077920F2045783FFBCAC00DD20F6B3E403A3070E7E7608F13DA41BC0052D7 | No immutable before copy in the supplied snapshot directory |
| Opening-stage provenance | common/scripted_effects/021_random_civil_war_active_evolution_effects.txt, event021_capture_pending_opening_evolution_stage and event021_commit_opening_evolution_provenance | 325C414C91272A5B1DF5970ACB603F8763F778BD5AB6A73C925F1D22D4146C23 | Current source is present, but no immutable before copy was found in the supplied snapshot directory |
| Candidate traversal and current cursor order | common/scripted_effects/021_random_civil_war_dynamic_front_candidate_effects.txt, event021_parent_collect_dynamic_optional_front_candidates | C64207A9FA9EA19178243173447E2D94578D641DC2E4D8785FA013CCC7561D3E | Exact byte match to the supplied immutable candidate snapshot |
| Front-ledger validation | common/scripted_effects/021_random_civil_war_front_ledger_effects.txt, existing front-ledger validators | 64AE170001403E36EB3CE3FD4809394DDECA5DEB24F137D6E45F6AB4D7E8775E | Current source is present, but no immutable before copy was found in the supplied snapshot directory |
| Decision and mission AI willingness | common/decisions/021_random_civil_war_decisions.txt, 18 decisions and 3 missions with ai_will_do | C928B1B802B4B2CCCFA49913AF9E288571099398A0000DA1814B6E35CDE81BC1 | Pre-access source at final observation |
| Decision access triggers | common/scripted_triggers/021_random_civil_war_parent_triggers.txt, event021_country_can_manage_fronts and event021_country_can_prevent_fracture | 57BD2B2DC3169D6105380A29667A8892528B0D4DFB98A4CF37B6854B78AAFA46 | Pre-access source at final observation |
| Shared crisis and authority triggers | common/scripted_triggers/021_random_civil_war_triggers.txt, event021_country_can_manage_crisis and random_civil_war_authority_is_failing | F8123906ED70709FEE419B6BD0988186474715AF810193AA90960CC8E3AEB170 | No immutable before copy in the supplied snapshot directory |
| Decision-category visibility | common/decisions/categories/021_random_civil_war_categories.txt, event021_civil_war_crisis_category | B15A843A7D6797B2769FEB6A765BB1227347BF9985EBA40807CEDF06190766E7 | Pre-access source at final observation |
| Decision effects used by management | common/scripted_effects/021_random_civil_war_decision_effects.txt | 653D04B02509FD090E5FAF395BE489539B912E4BE0B929C1B694A7F4B6C63065 | Freeze if the parent edits this dependency |
| Central timing, capacity, anchor, and AI constants | common/script_constants/021_random_civil_war_constants.txt | FBA1DBB902F05E96C9926FFA5C21961CC671094ABC74038C503D8CB516809BEA | Freeze if the parent edits a referenced tuning value |
| Event 021 actor strategy profiles | common/ai_strategy/021_random_civil_war_ai_strategy.txt | 6ADBB93B2CD17665C4BD967368F08BC953738D81DB7A2069171241F45C309DCA | Current strategy source, no MCP analysis result |
| Event callback source | events/021_random_civil_war.txt, chaosx.nr21.11 | 0480E9EBB1FA78096A081A0B597AE8B1072B149D66C9990C5B32B1433D59685E | Event 021 callback has no option-weight race |

The supplied immutable candidate source is docs/plans/021_random_civil_war_plans/probability_snapshots/event021_candidate_traversal_after_2026-10-03/021_random_civil_war_dynamic_front_candidate_effects.txt, SHA-256 C64207A9FA9EA19178243173447E2D94578D641DC2E4D8785FA013CCC7561D3E. Its bytes exactly match the current candidate-effect source.

The supplied parent source copy in that directory is SHA-256 791B87A3DF6FF517FDBE17680D16A13248AF41F076FA3266D6F2A8AE0B90F0FA. It does not match the current parent-effects source at SHA-256 0DBD60BF8259F6848413F84DB79F988D6D29CABB26FA09C283066A7A03E1DF61, so it cannot serve as the exact before source for the next comparison.

The observed parent-effects difference includes the secondary transfer receipt initialization, the final receipt validation before start_civil_war, exact rejection cleanup through event021_parent_reject_secondary_transfer, and the evolution log change that defaults events_log_evolution_has_actor to zero before event021_select_verified_evolution_log_actor. These are current baseline facts. The decision file and the parent decision-trigger file remained at the hashes listed above, and no active Evolution I review or management-ready identifier was found at final observation.

The sibling fixture.md is about synthetic candidate traversal cases DYN-ROWS-1001, DYN-REGION-1001, DYN-REGION-1002, DYN-PACKAGE-1001, DYN-PKG-CURSOR-WRAP, and SCN-REGION-SCORE-INDEX. Its SHA-256 is D78084233392A6335B24D813C86A574110FE55B92B67A1D406852523550277F0. It is not the active-war scenario fixture and has no MCP probability scenario hash for this audit.

## MCP calls and evidence status

The live probability tool schemas were exposed. Calls below returned no result block, source revision, workspace id, diagnostic, artifact URI, or scenario hash. A caller-side timeout is recorded as no returned evidence. It does not establish that the remote service or any still-running server request was canceled.

| Tool | Narrow request | Result |
| --- | --- | --- |
| hoi4.probability_inspect | event_mean_time_to_happen on common/mtth/021_random_civil_war_mtth.txt with refresh enabled | No response or artifact after approximately five minutes of bounded waiting. The local wait was terminated. Remote completion or cancellation is unknown. |
| hoi4.probability_inspect | Same adapter and file, candidatePool limited to random_civil_war_evolution_i_days | No response or artifact within a 60-second bounded wait. |
| hoi4.probability_inspect | decision_ai_will_do on the decision file with all 18 decision identifiers | No response or artifact within a 60-second bounded wait. |
| hoi4.probability_inspect | mission_ai_will_do on the decision file with all 3 mission identifiers | No response or artifact within a 45-second bounded wait. |
| hoi4.probability_inspect | ai_strategy_factor on common/ai_strategy/021_random_civil_war_ai_strategy.txt | No response or artifact within a 45-second bounded wait. |
| hoi4.probability_evaluate | decision_ai_will_do, all 18 decisions, two explicitly partial source-flag scenarios named EV1-ACTIVE-GOVERNMENT-BASELINE-PARTIAL and EV1-ACTIVE-SETTLEMENT-PENDING-PARTIAL | No response or artifact within a 45-second bounded wait. No scenario hash was returned. |
| hoi4.probability_sweep | Same partial decision pool and scenarios, paths random_civil_war_state_authority and surrender_progress, three steps, pairwise and rank-reversal requests enabled | No response or artifact within a 45-second bounded wait. No sensitivity or threshold result was returned. |
| hoi4.event_inspect | trace for selector { kind: event, eventId: chaosx.nr21.11 }, depth 2 | No response or artifact within a 60-second bounded wait. |
| hoi4.event_render | overview for selector { kind: event, eventId: chaosx.nr21.11 }, depth 2 | No response or rendered artifact within a 60-second bounded wait. |
| hoi4.reference_context | AI context for event MTTH, ai_chance, and ai_will_do | No response or citation bundle within a 45-second bounded wait. |
| hoi4.reference_search | Offline wiki, game_doc, and script_doc search for MTTH and AI weight semantics | No response or citation artifact within a 45-second bounded wait. |
| hoi4.source_lookup | Narrow lookup for random_civil_war_evolution_i_days | No response or source artifact within a 45-second bounded wait. |

The partial evaluation fixture used only the previously documented simple fields actor, state, flags, and scopes. Its two scenario inputs were explicitly incomplete and were not accepted or hashed by the current live service. No unsupported typed variable, global-versus-country flag, controller map, candidate override, or custom-pool field was submitted.

No probability analysis id exists for hoi4.probability_render. Rendering therefore could not be requested without inventing an analysis id. hoi4.probability_compare was not run because this is a pre-patch baseline and no owner-applied after source exists. The stale supplied parent snapshot is not a safe before source. hoi4.probability_simulate was not applicable because no uncertain-input distribution was declared. hoi4.probability_sequence was not applicable because this task does not define a complete custom weighted-pool cadence, recovery, cap, cooldown, removal, reset, timer, and terminal-state manifest.

The reference context/search/read routes also produced no retrieved documentation. Their route gap is covered by direct local reads below. No MCP artifact URIs, continuation URIs, source revisions, comparison ids, or rendered evidence paths exist for this pass.

## Reference evidence

Direct local reads were used after the reference routes returned no result.

The offline Paradox wiki AI modding page, SHA-256 917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818, lines 26-36, distinguishes ai_will_do score races from event-option ai_chance probability-proportional sampling and describes MTTH factor semantics.

The offline Event modding page, SHA-256 96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D, lines 130-132 and 159-164, describes event MTTH firing and proportional option weights. Its daily event-hazard description does not establish a hazard for Event 021's current injected scalar, which is sampled once into an absolute due date by scripted effects.

The offline Data structures page, SHA-256 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4, lines 263-333, 1069-1091, and 1210-1222, covers regular and global event targets, array indexing, array scope lifetime, and array traversal.

The offline Scopes page, SHA-256 18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49, lines 663-712, was read for scope changes during array iteration.

The offline Decision modding page, SHA-256 7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162, lines 361-366, describes ai_will_do as a decision AI weight block.

The installed vanilla documentation directory was searched for MTTH, ai_will_do, and ai_chance and returned no matches. Its Script Constants section in documentation/script_concept_documentation.md, SHA-256 884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7, and common/script_constants/documentation.md, SHA-256 E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C, were read for fixed-point support and constant schemas. Those official docs do not provide AI weight or MTTH selection semantics.

The vanilla source precedent named by the accepted addendum, Hearts of Iron IV/events/LAR_Spain.txt, lines 10056-10127, SHA-256 9487E0ACBB5FDD77D6F97A582FAD24B04ACA063F1AB50C30FC56B970411B654E, uses a filtered state set for a civil-war callback. It is a structural precedent only and does not validate Event 021's nested active-war transaction or probability.

## Weighted source values and result classification

### Evolution I MTTH-backed due date

The source entry is random_civil_war_evolution_i_days. Its declared base is constant:random_civil_war_evolution_mtth.evolution_i_base_days, whose current source value is 90 days. The scheduler clamps the sampled scalar to random_civil_war_timing.evolution_minimum_days = 60 and evolution_maximum_days = 180.

The source-ordered conditional factors are authority failure at 0.75, more than 8 controlled states at 0.85, an extra active actor at 0.75, surrender_progress greater than 0.70 at 1.50, settlement phase at 1.40, and no extra active actor at 1.35. These are source terms only. No effective MTTH value or delay distribution is certified.

The scheduler selects the first eligible side in global.random_civil_war_active_theaters for the MTTH context. It evaluates the MTTH entry at due-date scheduling time, stores an absolute global due date, and fires the triggered-only event chaosx.nr21.11 when that date is reached. This is an array-order context selection and a one-time due-date calculation, not a weighted race among theaters and not evidence of a continuous event hazard. No additional MTTH sample is part of the accepted active-war repair.

Classification: source trace is score/timing-input-only. Effective timing, exact or bounded distribution, and campaign outcome are unresolved because no MCP result or complete scenario fixture returned.

### Decision ai_will_do expressions

The source-declared decision pool contains these 18 identifiers: event021_secure_arsenals, event021_defend_capital, event021_review_loyalty, event021_seize_depot, event021_open_relief_corridor, event021_offer_emergency_settlement, event021_reconstruct_administration, event021_integrate_formations, event021_set_priority_front, event021_monitor_border, event021_support_government, event021_support_opposition, event021_offer_mediation, event021_end_sponsor_commitment, event021_complete_disarmament, event021_complete_coalition_governance, event021_protect_communications, and event021_review_regional_administration. This is the complete set of decision definitions with ai_will_do in the current file. MCP poolComplete was not returned.

The shared constants are base_action = 1, base_mission = 1, priority_major = 1.5, discourage_concession = 0.75, and discourage_repression = 0.75.

| Decision | Source score terms | Baseline relevance |
| --- | --- | --- |
| event021_review_loyalty | Base 1.0, priority-major factor for command claimant, priority-major factor for government side, and discourage-repression factor when authority is failing | Visible through opening management, multifront management, or Evolution III prevention |
| event021_integrate_formations | Base 1.0, priority-major factor for multifront active, and priority-major factor for command claimant | Current visibility requires event021_country_can_manage_fronts |
| event021_set_priority_front | Base 1.0 and priority-major factor for multifront active | Current visibility requires event021_country_can_manage_fronts and the existing target/core requirements |
| event021_protect_communications | Base 1.0 and priority-major factor for capital supply risk | Current visibility includes Evolution III prevention, reconstruction, or settlement |
| event021_offer_emergency_settlement | Base 1.0, priority-major factor for negotiator profile, priority-major factor for failing authority, and discourage-concession factor for hardliner profile | Its current settlement gates are independent of the proposed no-side review |

These are raw source expressions, not calculated scores. The MCP result did not establish how the connected analyzer resolves every modifier or which decisions are available in each complete campaign state. Per chaos-redux-decisions-missions and the offline wiki, ai_will_do is a willingness score or score race. It is not a player click probability and is not presented here as a normalized selection share.

If the accepted no-side management receipt exposes event021_integrate_formations and event021_set_priority_front while random_civil_war_multifront_active remains false, their existing priority-major factors remain inactive and their score expressions fall back to base action weight, subject to any other source modifier. This creates a potential AI starvation or rank-reversal question for the no-side phase. It is not a proven defect, and the auditor selects no new weight target. The same-case MCP evaluation and compare must decide whether the existing willingness is adequate.

The three mission definitions form a separate source pool: event021_hold_the_capital_mission, event021_secure_rail_spine_mission, and event021_hold_settlement_terms_mission. Each has base_mission = 1.0. Their source factors are role and phase dependent. The capital mission has priority-major factors for government, opposition, Event 006, and same-tag roles. The rail mission has factors for reconstruction, opposition, and Event 006. Settlement terms has a factor for settlement phase. No mission rank or starvation result was returned.

### AI strategy factors and deterministic candidate scoring

common/ai_strategy/021_random_civil_war_ai_strategy.txt defines 12 role profiles. The Event 006 profile event021_independence_actor_ai applies build_army = 100, infantry production factor = 75, infrastructure build factor = 70, and avoid-starting-wars = -25 while its Event 006 and settlement gates hold. Government, claimant, mediator, sponsor, successor, and global-prevention profiles also have source-defined values in the hashed file. These strategy values influence AI behavior and are not normalized selection probabilities. Their MCP inspection and scenario evaluation are unresolved.

The existing anchor score is deterministic state scoring. event021_parent_score_anchor_state starts from 10 and adds source constants for population, civilian and military factories, infrastructure, supply node, naval base, coastal access, core status, and capital status, then clamps from 1 to 100. The state and score arrays are paired. The candidate collector selects a highest-scoring anchor and advances its route cursor through whichever validated routes were appended, in this current order: regional, command, legal, ideological. The stored region score also supports force allocation. None of these source scores is an exact actor-selection probability or a click probability.

The user instructed that these scores and cursor order remain unchanged. No score, route-order, cursor, weight, or balance value was edited or recommended for editing.

## Scenario coverage and completeness

The following IDs are handoff labels for the requested cases. They are not MCP scenario ids because no analysis response returned a scenario hash. The two partial government and settlement scenario ids in the MCP call table were submitted but produced no result.

The source-declared decision candidate pool has 18 entries and the mission pool has 3 entries. This establishes source identity coverage only. The eligible candidate subset, event-level triggers, target validity, costs, cooldowns, and external campaign state were not established by MCP.

| Requested case and handoff id | Accepted deterministic expectation | Candidate and external-input completeness |
| --- | --- | --- |
| Live baseline government, active_source_government | The due transition should attach one bounded review to the proven baseline crisis. The current baseline callback records activation and log state but has no active-war review call. | Incomplete. Need the ordered live theater array, actor and host scopes, crisis and source ids, opening-stage receipt, global Evolution I state, authority, war and force state. |
| Ordinary primary with detached siblings, active_primary_detached_siblings | Review each exact surviving source row once. Do not allocate previously detached territory or forces again. | Incomplete. Source ids, sibling rows, ownership and control, capital/remnant state, current force receipts, and the full state ledger are not expressible in the accepted partial fixture. |
| Complete human Event 006 source, active_event006_complete | A complete human package can supply a side through its existing package adapter and preserve Event 006 origin history. | Incomplete. Need package id and completeness, actor human/nonhuman identity, source id, full package territory and control, forces, and event-origin receipts. |
| Same-tag contest and no-side management, active_no_valid_side | No child and no fictitious multifront flag. Resolve a genuine no-side receipt and expose the accepted management/prevention actions. | Incomplete. Same-tag identity equality, route receipt, opening provenance, target validity, and management-ready scope are absent. |
| Generation 2 additional front inside the same crisis, active_generation_cap.same_crisis_at_2 | A matching nonnegative source generation at the cap can create an additional same-crisis front, inheriting generation 2 and the existing crisis id after all viability gates pass. | Incomplete. Requires typed source generation, source row identity, crisis id, same-crisis relation, and live row arrays. |
| Generation 2 new descendant crisis, active_generation_cap.new_descendant_at_2 | A genuinely new descendant crisis is blocked at the strict generation cap. It must not be confused with another front in the same crisis. | Incomplete. Requires distinct source and new-crisis identities, typed generation values, and the descendant-creation gate. |
| Normal active-front cap exhausted, active_capacity_skip_retry | Keep the review pending and retry after real capacity returns. Do not resolve as no-side or duplicate a log entry. | Incomplete. Requires global active-front count, normal cap, live reservations, capacity-change timing, and owner transaction state. |
| Maximum temporary envelope active, active_maximum_envelope_closed | Defer automatic reviews during the Maximum batch. After it closes, apply the ordinary cap without removing existing over-cap fronts or retaining scenario privilege. | Incomplete. Requires global batch flag, envelope cap, batch owner, reservation count, and transition timing. |
| Source successor grace, active_successor_grace | Defer until the established source grace expires while retaining recurrence and treaty history. | Incomplete. Requires source identity, successor receipt, grace deadline, current global date, and any changed source ownership. |
| Settlement pending or progressing, active_settlement_progress | Preserve the settlement opportunity and defer. Close the review when settlement completes. | Partially expressible by country flags only. Settlement phase, pending objective progress, hold-until date, signatory scopes, and global/country flag distinction remain missing. |
| Near defeat, active_near_defeat | Defer through settlement or defeat resolution and do not strip the source capital or forces. | Incomplete. Requires surrender progress, opponent identity, capital and control maps, actual force remainder, and any pending defeat/successor callback. |
| Evolution disabled, evolution_disabled | Create no active review receipt, actor, or management unlock from a disabled Evolution I. Cleanup must preserve baseline content and unrelated transactions. | Incomplete. The disable flag is global. The partial schema did not provide proven global-versus-country flag scope or the full cleanup receipt state. |
| Missing opening, source, or generation provenance, active_missing_provenance | Fail closed and leave the case unresolved. Do not infer baseline stage, source generation, or a replacement identity. | Incomplete. Requires typed absence and presence for persistent variables, source ids, crisis ids, and opening-stage receipts. |

## Findings and risk assessment

The accepted addendum's deterministic expectations are not probability results. The current source supports the following baseline findings:

- The current Evolution I application is not connected to a review of a surviving baseline war.
- event021_country_can_manage_fronts requires event021_country_can_manage_crisis plus random_civil_war_multifront_active and excludes settlement and reconstruction.
- event021_country_can_prevent_fracture requires Evolution III and excludes an active crisis.
- The current category can be visible through event021_country_can_manage_crisis, but the no-side action set still requires the accepted narrow action-level access gates.
- event021_protect_communications must use the new narrow Evolution I prevention gate only for the accepted management phase. Its current affordability, target, cost, and cleanup checks remain relevant.
- The active no-side branch must not set random_civil_war_multifront_active merely to reuse the current decision predicates.
- The current action pool has 18 source declarations, so the post-change phase must be compared against the accepted presentation budget of 3 to 5 relevant actions. The expected mission pool remains 1 to 3. Do not add a mission merely because Evolution I activated.
- Decision costs and numeric ai_will_do terms remain unchanged under the accepted repair unless the parent separately accepts a measured tuning change.

No MCP-backed dominance, starvation, rank reversal, exact availability, positive weight on an impossible candidate, repetition rate, or exploit-risk result exists. The potential base-weight-only behavior for integration and priority-front management in a no-side phase is the concrete AI risk to test after implementation. It remains unclassified beyond a source-score concern. Current mission repetition and action cooldown behavior were not engine-verified.

The anchor score and route cursor are deterministic candidate planning, not probability-proportional sampling. Current route order is regional, command, legal, ideological when each route passes its gate. Keep the score constants, highest-anchor selection, and route iteration order unchanged in the active repair.

## Required parent snapshots and follow-up

Before editing active eligibility, management access, timing helpers, or their dependencies, preserve the exact current bytes for each file the parent will change. The candidate-effects copy already exists and is an exact match. Create a fresh parent-effects copy from current SHA-256 0DBD60BF8259F6848413F84DB79F988D6D29CABB26FA09C283066A7A03E1DF61. Do not use the supplied 791B... parent copy as the before source. Recheck every hash immediately before copying because the workspace is shared.

At minimum, freeze the parent effects, active evolution effects, candidate effects, front-ledger effects, parent triggers, decision source, shared crisis triggers, and any changed capacity or AI constants. Also freeze common/scripted_effects/021_random_civil_war_effects.txt, common/decisions/categories/021_random_civil_war_categories.txt, common/scripted_effects/021_random_civil_war_decision_effects.txt, common/mtth/021_random_civil_war_mtth.txt, common/ai_strategy/021_random_civil_war_ai_strategy.txt, and events/021_random_civil_war.txt if the implementation changes any of them. Use byte-preserving snapshots and record their copied-byte SHA-256 before the parent patch.

After the complete mechanic exists, use the identical accepted scenario set for hoi4.probability_compare. The comparison should cover decision_ai_will_do on the complete 18-decision pool and mission_ai_will_do on the complete 3-mission pool separately. Reinspect the MTTH entry only if its scheduler or timing input contract changes. Evaluate and sweep only scenarios whose typed campaign inputs the live schema accepts. Keep inaccessible scenario dimensions unresolved. Render from a returned analysis id when a ranking, matrix, sensitivity, timing, or unresolved view helps review.

Keep the current region-score formula and route order unchanged. Do not convert the deterministic anchor score, cursor, or force allocation weight into a probability pool. Do not use probability_sequence unless the parent introduces a complete declared custom pool with its full cadence and state-transition contract.

The next parent decision is the accepted implementation tranche and its immutable source snapshot set. The parent still owns the AI tuning target, if any. This auditor selects no weight target and applies no fix.

## Blockers, omissions, and skills

Blocking evidence gap: the probability and event MCP routes returned no results within the bounded waits listed above. Service health and remote request completion are unknown. No exact or bounded timing, normalized option share, action ranking, candidate eligibility, or comparison is certified.

Uncertain inputs: actor and country scope, global versus country flags, current theater arrays, typed variables, source and crisis identifiers, state ownership and control, force and resource receipts, dynamic package completeness, active capacity, reservations, settlement progress, grace dates, and near-defeat state are incomplete for every requested live scenario.

Skipped analyses: probability_compare has no after source yet. Probability render has no analysis id. Simulation has no declared uncertain-input distribution. Sequence analysis has no complete custom weighted pool. Event compare has no inspect/render graph artifact and belongs after the owner patch.

Skills used: chaos-redux-subagents, chaos-redux-events, chaos-redux-mtth, chaos-redux-decisions-missions, chaos-redux-event-planning, and chaos-redux-improvement-loop. The improvement-loop skill kept this as the accepted bounded baseline handoff and prevented a duplicate expansion pass. No skill file was changed.

No changes were made to gameplay or AI weights. This handoff is an incomplete read-only baseline, not a full Event 021 audit or completion claim.
