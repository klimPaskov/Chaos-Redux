# Event 021 probability audit — 2026-10-06

Disposition: incomplete read-only audit. The decision source was discovered and the existing emergency-terms comparison returned a partial result, but the four-scenario score evaluation timed out and the event-option inspection timed out. No numeric score ranking, selection probability, or balance conclusion is certified by this handoff.

## Scope and source files

- Decision ai_will_do: common/decisions/021_random_civil_war_adaptation_decisions.txt, three decisions: event021_adapt_campaign, event021_expose_intervention, and event021_mass_mobilization (source lines 4–67).
- Decision availability, costs, and phase gating: common/scripted_triggers/021_random_civil_war_adaptation_triggers.txt (lines 2–92).
- Decision and event-option tuning: common/script_constants/021_random_civil_war_regional_constants.txt (lines 2–26).
- Event ai_chance: events/021_random_civil_war_adaptation_events.txt, event chaosx.nr21_adaptation.1, options chaosx.nr21_adaptation.1.a, .1.b, and .1.c (lines 4–43).
- Authority failure is random_civil_war_authority_is_failing in common/scripted_triggers/021_random_civil_war_triggers.txt (lines 339–348); it compares random_civil_war_state_authority to constant:random_civil_war_authority.collapse_maximum, whose source value is 14 in common/script_constants/021_random_civil_war_constants.txt:219.
- The rail-validity helper used by the supply option is event021_secure_rail_mission_target_valid in common/scripted_triggers/021_random_civil_war_parent_triggers.txt:1186–1193.
- Existing emergency-terms comparison target: event021_offer_emergency_settlement in common/decisions/021_random_civil_war_decisions.txt:223–305, with tuning in common/script_constants/021_random_civil_war_constants.txt:596–699 and offer readiness/blocking helpers in common/scripted_triggers/021_random_civil_war_parent_triggers.txt.

The parent reports that final balance review removed the mass-mobilization command-power gate and payment while leaving every AI weight unchanged. The successful adaptation-file inspection predates that eligibility edit, so its hash does not certify final decision availability. The named fixtures supplied command power 100, above the prior gate, but their analysis did not return.

## MCP evidence and source revisions

The successful read-only hoi4.probability_inspect for decision_ai_will_do discovered three candidates in the adaptation decision file, with poolComplete = false, availableCandidates = 0, and four required inputs: command_power, has_political_power, scope.has_equipment, and variable.army_experience. All three candidates require scenarios. The adapter reports selectionRule = score_only, rawScore = true, and normalizedProbability = false. It does not model a decision click probability.

- Workspace: mod_chaos_redux_ea3b2d67c2c0.
- Source revision: 866ba025c5fe9ce020dc5d00d8a585923ac34e42e476a1e9d0135718d2e696c0.
- Analyzer source hash: a16e2e3cbf592675fda37dbb40ac08a887bb4531e2f94837bf53bca1245ebb65.
- Candidate-file hash reported in candidate provenance: 8a8f18424060a8dc20e094adbc56b591aaa31b26486efe58a530190db72287f2.
- Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bfc200087f840df646d0a62478e5734ea28856ef67f4abf378e7ac224ea38a3/92ee21bd4f82557313c8245c7ff6b7bc506cd278b400f50e828faf2a4ad6c1ba/probability-inspect-a16e2e3cbf59.json.

The separate hoi4.probability_inspect for event_option_ai_chance on events/021_random_civil_war_adaptation_events.txt returned the exact blocker: tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; caused by timed out awaiting tools/call after 600s. It produced no artifact, source revision, source hash, candidate count, or analyzer-backed option eligibility. I did not retry it.

A named four-scenario hoi4.probability_evaluate request for the three discovered decision IDs returned the exact blocker: tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_evaluate; caused by timed out awaiting tools/call after 600s. It produced no analysis artifact or score rows. The one authority-threshold sweep request had not returned when this handoff was written; its threshold and rank-reversal conclusion remains open.

The matching hoi4.event_inspect lint request was started with a file selector for the event source. The parent then directed that no further structural event queries were needed because the parent was handling the final narrow event render and comparison. This subagent stopped the pending lint request without receiving an artifact. No event structural coverage is claimed here.

## Named scenarios and completeness

The submitted scenarioSet ID was EVENT021_ADAPTATION_GOV_RAIL_CLAIMANT_PLAINS_FAILING_MOUNTAIN_EVENT006_PLAINS_2026_10_06. It contained four scenarios with actor CXT, flat scenario state, flags, and a ROOT scope state. The input matrix is preserved in 2026-10-06_probability_evidence/scenario_matrix.json. It records values sent to the evaluator, not values accepted or certified by the MCP analyzer.

- GOV_RAIL: government-side and Evolution II flags, a front-action-used flag, 30 army experience, authority 0, command power 100, political power 100, rifles 3000, support equipment 500, and plains terrain.
- CLAIMANT_PLAINS: opposition-side and Evolution II flags, an arsenal-action-used flag, the same resource values, and plains terrain.
- FAILING_MOUNTAIN: government-side and Evolution II flags, a capital-action-used flag, the supplied foreign-intervention marker, authority 15, the same resource values, and mountain terrain.
- EVENT006_PLAINS: opposition-side, Evolution II, and Event 006 adapter-complete flags, a front-action-used flag, authority 15, the same resource values, and plains terrain.

The fixtures do not prove hidden helper state. For example, the rail decision helper requires a stored target state that exists, is owned and controlled by the crisis country, belongs to its opening-core array, and retains valid supply or infrastructure. A country flag alone does not establish that pointer and map state. The foreign-intervention availability helper also needs the live sponsor and target state. Phase and response-slot eligibility, current event stage, settlement/reconstruction exclusions, affordability, and terminal locks were not confirmed by the timed-out evaluation. The adapter therefore proved no scenario outcome for these candidate gates.

Candidate-pool completeness differs by surface. The new decision file contains the three IDs above, but its inspector result says poolComplete = false. The existing Event 021 decisions file has a prior inspection with 18 candidates and poolComplete = false; the combined category pool across both files and any other loaded sources was not certified. Because the adapter is score-only, no normalized probability was requested or inferred. The event file visibly contains three option blocks, but its analyzer candidate pool and trigger-qualified membership remain unresolved because inspection timed out.

## Source traces and result classifications

The following are source facts only; no total score products were calculated by hand.

| Candidate | Base and conditional source modifiers |
| --- | --- |
| event021_adapt_campaign | Base event021_regional_response.ai_base = 1; ai_urgent = 2 when random_civil_war_authority_is_failing is true. |
| event021_mass_mobilization | Base ai_base = 1; ai_preferred = 3 when authority is failing; ai_urgent = 2 for the opposition side. |
| event021_expose_intervention | Base ai_base = 1; ai_preferred = 3 when authority is failing; ai_urgent = 2 when the recorded sponsor is major. |
| chaosx.nr21_adaptation.1.a supply option | Base ai_base = 1; ai_preferred = 3 for the government side and independently for a valid rail mission target. |
| chaosx.nr21_adaptation.1.b defense option | Its option trigger is mountain or urban; base ai_base = 1; ai_preferred = 3 on mountain terrain; ai_urgent = 2 when authority is failing. |
| chaosx.nr21_adaptation.1.c columns option | Base ai_base = 1; ai_preferred = 3 for the opposition side and independently for the Event 006 adapter-complete flag; ai_urgent = 2 on plains. |

The shared adaptation constants are ai_base = 1, ai_preferred = 3, and ai_urgent = 2. These values are centralized. The decision modifiers are willingness scores, not click probabilities. The event-option modifiers are weights for proportional sampling, but no scenario probability is certified because the required option inspection timed out.

The defense option's source trigger excludes plains. Thus the source expectation is that defense is unavailable in CLAIMANT_PLAINS and EVENT006_PLAINS; this is not an analyzer-proven zero or an exact option probability. Mountain/urban scope semantics also remain unconfirmed by MCP in this pass.

The prior read-only inspection of common/decisions/021_random_civil_war_decisions.txt found 18 existing decision candidates, poolComplete = false, and required inputs command_power, has_army_experience, has_manpower, has_political_power, scope.any_of_scopes, and scope.has_equipment.

- Prior source revision: 2c36eaadc8bbc6823ea29ed78be8c12fd99ab4545f65f8e4fd88ff94e7bbd235.
- Prior analyzer source hash: 946fd00348474f35a2b843190c8e58d294c6c4842e9fa80faecbca481b638618.
- Candidate-file hash in that inspection: 0201a1e3c88197de973b39ce49ad4c3fa1712ae9724cec0e9c358a93edc300eb, matching the local SHA-256 of the current emergency-terms source and the bytes at HEAD when checked.
- Prior artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/33f8f072575c3fc80118358129813c0e63c08e547b8c140b326049e557186a90/80b1ec77a96f4e24f0c5e79efc4101a7e9ee583b218d7de9372bc56c9b40a486/probability-inspect-946fd0034847.json.

## Emergency-terms compare

One hoi4.probability_compare attempt used the same four scenario IDs, decision_ai_will_do, candidate event021_offer_emergency_settlement, and the existing decision file as both before and after. The local file was byte-identical to HEAD when checked, and its raw candidate-file hash matched the prior inspection. The comparison returned PROBABILITY_ANALYZED_PARTIAL, but it is unresolved evidence rather than accepted score certification:

- Analysis/comparison ID: probability-153ef582240bdf5ff4d2c10f.
- Source hash: 946fd00348474f35a2b843190c8e58d294c6c4842e9fa80faecbca481b638618.
- Source revision: 56f327939c0a996aaa92f9454c3318328ecc6a52942947c0ff46ecc970587445.
- Scenario hash: 29f8925d5cacc89e5fcfed943fa518d3ed068c071770292ed7b010f6583c4a99.
- Result: four supplied scenario rows, zero eligible, four excluded, 13 unresolved, and comparisonChanges = 0.
- Diagnostic: PROBABILITY_OUTCOME_NEVER_ELIGIBLE for event021_offer_emergency_settlement across the supplied scenarios; modifiers for the cohesive zero gate, hardliner holdout, holding ground, lost ground, major-negotiator profile, and mediation were not active in those fixtures.

This result does not show that emergency terms are never eligible in a campaign. It shows that the supplied fixtures did not establish readiness, valid sides, the live country scopes, settlement costs, or the state and player-control gates. Because every row was excluded and 13 inputs stayed unresolved, the comparison proves no numeric score delta. The source identity and comparisonChanges = 0 support only that the same unchanged decision source was compared on both sides.

The comparison operation emitted JSON and unresolved/comparison visuals:

- JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e81980d6fdf458e865480a54ad5c384b79a2a2b05d024dbf4ae2d652056cccb0/8ec3fcf592e9e8c100aa751ff796796d7252e8ca297167a9adb4511975b64726/probability-153ef582240bdf5ff4d2c10f.json.
- Comparison SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/c8b5cbb2ac1373bfe114c803b51c99cbeec2533e7e43aacf2117f6e076c9de41/probability-probability-153ef582240bdf5ff4d2c10f-comparison.svg.
- Comparison PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1fd8e11d21dd2414c85f7412d454fa53b5b857ed9fb09593caa20f6277f498f/49c72e30c5a0f10fc73acd0c9405b1940594cf7c70f380c1950596b65406aa93/probability-probability-153ef582240bdf5ff4d2c10f-comparison.png.
- Unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb8944f792a08bfdc7228333b437a8554da873aec0f04aa68e5fa49681740231/ba654c1aeabbc7b07740b39e41734261096108cf45c7bb7a931e4bf3bebe4c74/probability-probability-153ef582240bdf5ff4d2c10f-unresolved.svg.
- Unresolved PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ae19c2cc6e04562aed791633a084acbc7c63031f1343547d4c2f8797f765aa4/d1928da0582c5b546693179d3d7422ccb31e6db6281156157c2a11758564def1/probability-probability-153ef582240bdf5ff4d2c10f-unresolved.png.

No score table or ranking is claimed from this comparison. A separate hoi4.probability_render follow-up did not return before it was stopped; the comparison artifacts above are the only retained render evidence.

## Balance, validity, and risks

The source uses conditional modifiers rather than a single flat weight, and the inspected adaptation decision IDs do not contain literal repeated constants for their AI priorities. No decision selection probability is modeled by the adapter. The old and new files do not form a complete category pool in the returned inspections, so dominance, starvation, rank reversal, and competition against the rest of the category remain unresolved.

The action gates visibly constrain the adaptation decision lifecycle: campaign adaptation is once per crisis and affordable; mobilization requires the prior adaptation, a high-chaos stage, affordability, and an unused marker; sponsor exposure is government-side, intervention-bound, affordable, and once per live intervention. The event comment describes one optional report per side per crisis, the event is triggered-only, and each option consumes the pending receipt through its effect. These are source-level repetition safeguards; no probability_sequence analysis was applicable because these are not declared custom weighted pools with a full cadence/state manifest.

No positive-weight-on-impossible-choice, starvation, snowball, or exploit conclusion is analyzer-certified. Availability is explicitly separate from score, the hidden helper state was incomplete, and the event-option MCP route timed out. No balance target or numeric tuning change is recommended from this incomplete evidence.

## References and skill guidance

The reference-context route returned these revision-bound citations:

- Installed game country decision documentation, C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md:1–46, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019.
- Offline wiki Decision modding AI section, paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:357–374, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
- Offline wiki Event modding options section, paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:151–179, revision 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d.
- Offline wiki AI modding MTTH section was read directly from paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:26–36; the targeted reference_search call did not return, so no MCP revision is available for that local read.
- The installed decision documentation establishes decision scope and availability evaluation, while the offline wiki distinguishes decision ai_will_do scores from proportional event-option ai_chance. Both references show that these are different weighted surfaces.

The hoi4.reference_context event bundle omitted detailed Effects and Triggers sections. The hoi4.reference_search request did not return within the bounded wait, and no hoi4.reference_read artifact was captured. Relevant source helpers were read directly from the named local files. Skills read: chaos-redux-subagents, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-mtth, and chaos-redux-event-planning.

## Recommended follow-up

1. After the analyzer route is responsive, inspect events/021_random_civil_war_adaptation_events.txt with event_option_ai_chance, then evaluate all three options under the four named scenarios with explicit terrain and all option-trigger state. Sweep the authority-failure and terrain boundaries, and retain the analyzer's qualified candidate set before reporting any proportional selection probability.
2. Reinspect the final adaptation-decision source after the parent’s affordability edit. Evaluate GOV_RAIL, CLAIMANT_PLAINS, FAILING_MOUNTAIN, and EVENT006_PLAINS with accepted target, scope, campaign-phase, resource, and flag bindings, then sweep the authority threshold and render score/unresolved views.
3. Inspect the whole active Event 021 decision category across the existing and adaptation files. Include every available decision candidate before making a global score-race, dominance, or starvation claim.
4. Keep emergency-terms score evidence unresolved until a scenario can satisfy event021_settlement_offer_ready, event021_settlement_offer_blocked = no, the country/side and cost gates, the relevant profile state, and any live mediation scope. Then repeat a before/after compare only if a real source change is being checked.
5. Parent owns final-source eligibility validation and commit. This handoff performs no gameplay edits, no staging, and no commit.
