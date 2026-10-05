# Event 015 Probability and AI Release Audit

Status: source review and same-scenario comparisons were attempted after the parent’s final-source signal.
The selector’s declared synthetic-pool comparison completed.
Event-option and focus analyses are partial because the scenario pool does not establish the complete live campaign candidate set.
Event and decision evaluations later rendered stale after the workspace revision moved.
No gameplay source was edited.

## Audited source surfaces

The principal current source hashes at comparison capture were:

| Surface | Current source | SHA-256 |
|---|---|---|
| Event options, opening, incidents, and reports | `events/015_utopia_manifesto.txt` | `55a18a9102a81810291b2b4af55bd1349fa4301b88f1f309889872bd271464a8` |
| Candidate selector and pulse scheduling | `common/scripted_effects/015_utopia_manifesto_effects.txt` | `0e05dafecbbf2364716febb1c19fd6be069f201c43abe9320c53623b367f1eb2` |
| Candidate eligibility and approved-light gate | `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | `0f545614ec86dba0f5f587db0f44e0b7a222a250e94430344c6785db893fabda` |
| Main decisions and affordability gates | `common/decisions/015_utopia_manifesto_decisions.txt` | `be3fd76dee2516fe9241ba47b1f8d52942c763800c868be8caca24a742a9ed1f` |
| Prefire evolution decision | `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` | `26e51a0a525cd785b02a20e4ef59fe13505f22d110a40dbaa21485c6822859ed` |
| Evolution-consumption decisions | `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` | `e09f6c99f55bc1ff7f9bb05b97ebebb39a103b7008b5ab3c6a56aaa93b3a858c` |
| Decision effects | `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | `493f0a110ca95508f0932114ec36e37f7f7bc6a0428a58b5e4d3702c5b2b0d92` |
| Shared Event 015 scripted effects at comparison capture | `common/scripted_effects/015_utopia_manifesto_effects.txt` | `0e05dafecbbf2364716febb1c19fd6be069f201c43abe9320c53623b367f1eb2` |
| Focus tree | `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `9dce3a0805f6087f30e37885a7eeca1912e39932b01504d0b19e1e3a1b0bfaff` |
| MTTH entries | `common/mtth/015_utopia_manifesto_mtth.txt` | `af4b8bdb27c94fa0163fcdbb96eae0ee0e5d14acf67ac148389820c4d4bb9b11` |
| Event 015 AI strategy entries | `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` | `7d23dc491c21103ed85ab5c7eeb2f9941dce26299aa26ed483d35212c4880caa` |
| Advisor definitions | `common/characters/015_utopia_manifesto_characters.txt` | `42b7a3dd5edb484a48978efb09c0d0b0212e35698139f7f61aaf09eb43bb9c6f` |
| Narrative AI and MTTH constants | `common/script_constants/015_utopia_manifesto_narrative_constants.txt` | `dcb61c2e6805c5329df89ac1d71d9bbce489c2b841e862988b3338dce44b00ed` |
| Candidate ticket score and class constants | `common/script_constants/015_utopia_manifesto_constants.txt` | `4abd55f04279be24d59dd51ff1eebdd798103db12751ad6e856357c0921f134a` |

Before-source snapshots used for the comparisons were retained at `.tools/tmp/015_probability_2026-10-05/events015-before-pulsefix.txt` (SHA-256 `ea643723cd03bbe5864596be77fae5251f07c56d10820238fdaf09a98235049c`), `.tools/tmp/015_probability_2026-10-05/candidate-selector-before/common__scripted_effects__015_utopia_manifesto_effects.txt` (`7a1487ff35e14c780d7425ee34fbaa26e86902e7be36e6b2fbda57832709e361`), `.tools/tmp/015_probability_2026-10-05/candidate-selector-before/common__scripted_effects__chaosx_settings_effects.txt` (`7c09c09a0898b46f3f342ab300c1d68ea57277295f99f790c17148716a6f837f`), and `.tools/tmp/015_probability_2026-10-05/focus-before-head/common__national_focus__015_utopia_manifesto_focus_tree.txt` (`6d0a079b9740eaccf1018e8e8e1034e4c1165cf32d9d3b915dad7465013ab775`).
Main decision affordability was compared from `docs/plans/015_utopia_manifesto_plans/probability_snapshots/unit_growth_pre_fee_reduction_2026-10-05/common/decisions/015_utopia_manifesto_decisions.txt` (SHA-256 `633128029848ec42bb65bdb48df3b6d0e3a73b7ddc051a4835d91bf6926b8dd7`).
Its accompanying snapshots preserve the then-current decision effects, main effects, triggers, decision constants, and English cost copy; shared helpers are read from the current workspace by the MCP analyzer, so these are not a full historical workspace snapshot.

## Scenarios and completeness

All comparisons used the strict 27-scenario fixture at `docs/plans/015_utopia_manifesto_plans/probability_evidence_2026-10-05/exactscenario.json`, file SHA-256 `1c21994b7b7627ad0cbe272b1938c5ef2e935bb309ca03cd3bc22b29c4d3ac49`.
MCP normalized scenario hash: `de2b78f8a6af4c7af23c250f4d5dbf5c12ea6ba5fa6608e86dea894be2f4edca`.
Scenario-set id: `015_utopia_probability_release_2026_10_05`.

The selector before/after custom-pool manifests are preserved at `docs/plans/015_utopia_manifesto_plans/probability_evidence_2026-10-05/selector_pool_manifests.json`, SHA-256 `5167ae9e6c48a3f0eb67e1b87395e79e72ee27f013225019cd3378a27d1f145f`.

The declared core fixtures are `015_minor_peacetime_1936`, `015_war_shortages`, and `015_constrained_route`, with isolated variants `015_constrained_route_voluntary`, `015_constrained_route_council`, `015_constrained_route_closed`, and `015_constrained_route_humanist`.
`015_namedlight_approval_unmapped` exercises the approved-light candidate gate, and `015_opening_already_presented` exercises repeat-opening suppression.
These are synthetic inputs, not save observations.
The two-country minor pool is complete only within its explicitly declared fixture and its ticket weights are declared model values, not campaign measurements.

Eighteen additional scenarios test below/equal/above ordinary full-price quote boundaries for six decision bundles: `refugee_municipality`, `close_the_gates`, `issue_need_ultimatum`, `enforce_need_case`, `impose_assigned_administration`, and `begin_long_integration`.
Full-price ratio `10000` is an explicit fixture input.
**The four unit-growth fee changes do not have dedicated below/equal/above boundary scenarios in this 27-case set.** Do not treat the six existing bundles as affordability proof for Citizen Watch, Engineer Companies, Auxiliary Contracts, or Post-formation Reinforce.

External campaign state remains incomplete for event pools, focus prerequisites and bypasses, AI strategy plans, country-specific decisions, and stored targets.
No save data was supplied or modeled.
Candidate overrides and synthetic state flags are assumptions for bounded tests; they do not prove live availability.

## MCP workflow and retained evidence

The connected `hoi4-agent-tools` probability schemas were verified from the live tool metadata.
The installed local package was version 3.8.1; its `schemas/probability.js` source hash is `de7aeb8fcfebfdfc7df6ce48e01808c64d371d590932916dc456cb8d7c73df20`, and `docs/probability.md` hash is `a392933e376396fe135e25711f513fe3b0f5f09d03847455c1a95948fed030c8`.
Its source-selector contract supports a workspace-relative preserved snapshot path, logical game path, and exact expected SHA-256.
Its documentation states that decision scores are not normalized probabilities, focus requires a complete candidate pool, and candidate overrides remain scenario assumptions.

Initial read-only `hoi4.probability_inspect` calls were made for the Event 015 event file, MTTH entry, prefire and main decision sources, focus tree, AI strategy entries, and advisor weights.
The initial event-source and main-decision calls were wrapper-terminated before a result was available.
Retained calls for the MTTH, prefire decision, focus, AI strategy, advisor, and event-option adapter returned the exact MCP error `tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by timed out awaiting tools/call after 600s`.
No inspect artifact or source revision came from those calls.

After the owner’s final-source signal, the following one-time `hoi4.probability_compare` calls were submitted with `refresh:false` and the same 27-scenario set: the selector’s before/after custom-pool manifests; event `ai_chance` from the preserved event snapshot to the current event source; native event MTTH on the same event source; main decision AI/affordability source from the preserved unit-growth snapshot to current; and national-focus AI from the exact Git-HEAD snapshot to current.
The calls completed, but the inline response for the five-call batch was truncated by the execution envelope before all per-route summaries and artifact references could be retained.
The selector and event outputs were recovered below.
The missing decision and native-MTTH response summaries remain unresolved in this handoff; do not claim their scores or timing were compared successfully.

For `custom_weighted_pool`, analysis id `probability-603a45f10367a6f22fd46566` returned `PROBABILITY_ANALYZED`, scenario hash `de2b78f8a6af4c7af23c250f4d5dbf5c12ea6ba5fa6608e86dea894be2f4edca`, 27 scenarios, 3 comparison changes, 0 unresolved items, 4 eligible candidate/scenario rows, and 104 excluded candidate/scenario rows.
The model’s total count is 108 candidate/scenario rows.
Two diagnostic warnings say the synthetic human-generic and approved-light candidates are never eligible in the supplied scenarios.
This proves only the declared manifest model.
It does not prove live selector weights, candidate completeness, or the approved-light route’s campaign eligibility.

The selector authoritative JSON is [MCP resource `probability-603a45f10367a6f22fd46566.json`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90a61eb8493053f3c6944cd901cad93ddcc9e91eb5c49aeffe5d1e52aecfa67c/87f436b9ea36bd551e5a498e554a926b786d993a148fcf7b3e42fda20d117409/probability-603a45f10367a6f22fd46566.json).
Its returned matrix and comparison views are [matrix SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1de0c140d97cc2c92a368525e08eca58357a77de41a39c6011cfba409e158d50/bcc965455dc9e65bafe3e33e11546817b409a11fbed94131ad87b83cdcfbf21b/probability-probability-603a45f10367a6f22fd46566-matrix.png) and [comparison PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb9ae8a0920741c845fabb3e17eeaea3275420551f998376f9e11bb568e98bbd/49c6b3fedddd0e3da53a9211c1dad3aa19242f3845b5c4edf8da43aa6a843891/probability-probability-603a45f10367a6f22fd46566-comparison.png).
The authoritative JSON SHA-256 is `90a61eb8493053f3c6944cd901cad93ddcc9e91eb5c49aeffe5d1e52aecfa67c`; the PNG hashes are recorded in the resource links.

For the event-option comparison, id `probability-a91e41e8faf0b76a6455c751` returned `PROBABILITY_ANALYZED_PARTIAL` for the same 27 scenarios.
Its authoritative JSON resource is approximately 75 MB: [event comparison JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3adba179072d1303a4b9794fcf49acec82cfcfd65fcb075766a39015b68e2f16/ba8d0d2665c059bc6523782b91fff3682af9a8954c95882491de86f10da576aa/probability-a91e41e8faf0b76a6455c751.json).
It was not downloaded or opened.
A subsequent compact `hoi4.probability_render` request returned `PROBABILITY_ANALYSIS_STALE`; its retained metadata reports 7,938 candidates across 27 scenarios, 7,353 eligible and 542 excluded candidate/scenario rows, 708 unresolved items and 77 unresolved candidates, and zero comparison changes.
Because the rendered result was marked stale after the comparison, those counts are historical artifact metadata only, not current-source proof.
The stale render reports source revision `2177afb467bfd5f982f7a512ffa06e1a613ecdf47…`; it produced no valid fresh ranking or comparison view.

The focus comparison reported 124 focus candidates and explicitly warned `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`; the 27 synthetic scenarios do not enumerate all prerequisite, bypass, focus-strategy, and external-factor state.
The retained result reported 708 unresolved or bounded items.
No exact focus-selection probability is available.
Its comparison analysis id and linked artifact were not retained in the truncated batch response.

Bounded follow-up `probability_evaluate` calls used the five declared scenarios `015_minor_peacetime_1936`, `015_war_shortages`, `015_constrained_route`, `015_namedlight_approval_unmapped`, and `015_opening_already_presented`.
Their normalized scenario hash is `5206e353236439432dba6d8e9c5508e848fbef69e829eb9b2adf8e6c767fae9e`.

For the opening option pair, analysis id `probability-0a0a1eb64781caefb88992cb` returned `PROBABILITY_ANALYZED_PARTIAL` for 5 scenarios and 10 candidate/scenario rows, with 5 eligible rows, 5 excluded rows, and 14 unresolved items.
The analyzer reported `chaosx.nr15.1.a` at the configured 1.0 dominance threshold in all five scenarios and `chaosx.nr15.1.b` never eligible.
This is conditional option-pool evidence only; it says nothing about whether the event fires.
The authoritative JSON is [opening option evaluation](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8379fd63f9817083e998efcaba1e3465d2a5bc4b210fc1b10592b5a11c9b2ea/068f3842c66d926f7494a6f2aa657b1b87b544cb84321451bc9e240ba966a812/probability-0a0a1eb64781caefb88992cb.json), SHA-256 `a8379fd63f9817083e998efcaba1e3465d2a5bc4b210fc1b10592b5a11c9b2ea`, size 153,180 bytes.
The analyzer also returned [unresolved SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38b502cd71bed8226bbe98bd128d94170a7069746645679c8092843b4678159f/e79a2c9fd95ca03dfa2cb01b61494a7e5141a30473115e3cb545f87f392dbab2/probability-probability-0a0a1eb64781caefb88992cb-unresolved.svg).
A later render of this evaluation returned `PROBABILITY_ANALYSIS_STALE` with zero fresh visual resources.

For the four growth decision scores, analysis id `probability-c62d5f7332649a413cfd7c32` returned `PROBABILITY_ANALYZED_PARTIAL` for 5 scenarios and 20 candidate/scenario rows.
It found zero eligible rows and 30 unresolved items; all four selected decision candidates were never eligible across this scenario subset.
This means the test state did not reach the decisions and cannot establish either score rank or affordability.
Its authoritative evaluation JSON, later marked stale by render, is [growth decision evaluation](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4f548c79fc0c123743fc34a50ee7a2bfb333b5392910f3af613736c780ec1d7/3375815288ccfe1c5241b2b629581a6c4f70ea00f387b2139bed86716fc91d9e/probability-c62d5f7332649a413cfd7c32.json), SHA-256 `c4f548c79fc0c123743fc34a50ee7a2bfb333b5392910f3af613736c780ec1d7`, size 663,671 bytes.
No available-growth ranking is claimed.

For a bounded focus score sample, analysis id `probability-b553749f46ab58ee714edd76` returned `PROBABILITY_ANALYZED_PARTIAL` for 15 candidate/scenario rows, 10 eligible rows, 5 excluded rows, and 17 unresolved items.
`utopia_manifesto_the_country_as_a_question` was never eligible in this five-scenario subset.
The selected three-focus sample is not a complete focus pool.
Its JSON is [focus score evaluation](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4cfd9a11c28a4e558e40a7b53a75d6404c65208033f7bc58845db2d101f24f4/bf417ce4c4d5bee401cc4a6527880cdffe9233545058c9551a53d1fdd1c7c0a7/probability-b553749f46ab58ee714edd76.json); its rendered views include [ranking PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/31cf546664398b05b4c00824741a15e7b099bdc8debe0c4708cf06155611c79f/faa285cef8e415d43529a433738d32c27ba9100713b9f85fbc4fb1881cecadb7/probability-probability-b553749f46ab58ee714edd76-ranking.png) and [waterfall PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50e074937d61dbcf8f8a38c8843537e5deb06f78954584bf173b547d1bed34fd/30a92033e009bebe516b9bd99d3aec1058e299a0805bad208b68cc4010e79d2b/probability-probability-b553749f46ab58ee714edd76-waterfall.png).
These present scores for that small declared sample only.

The `probability_evaluate` and `probability_sweep` requests for `utopia_manifesto_incident_interval` against `common/mtth/015_utopia_manifesto_mtth.txt` both returned `PROBABILITY_SURFACE_EMPTY`, with `availableAdapters: []` and `candidatePool: []`.
This exact blocker shows that the installed probability parser does not recognize this `mtth:` helper entry from the MTTH source file.
No timing distribution, cumulative chance, or sensitivity result is available from MCP.

Probability simulation was skipped because no uncertain-input distributions were declared.
Sequence analysis was skipped because the selector manifest models a single draw, with no recurrence, cooldown, recovery, or state transitions.

A focus sweep on `variable.utopia_need` was submitted across five sweep points and the same three-focus candidate subset used in the evaluation.
It returned `PROBABILITY_ANALYZED_PARTIAL`, 15 candidate/scenario rows, 10 eligible, 5 excluded, and 17 unresolved items.
The artifact is [focus sensitivity sweep JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2adb2475af700c7385a771da0c5d0b4715b48aa2af821ac4259b1ddf86e854ed/cdf73a2f1464efd1fc3b0c7546602a1fa5788cc6dad178fc8d4b2ce7f1cf2289/probability-2f0a01246994931f2a87ecfe.json); its scenario hash is `66e282d799fa30693a6e505991265202391f11cbc6b5ecf1f68eddfa12bb5d84`, with 17 unresolved items.
The sweep is bounded to the three selected focuses; it does not prove a route-wide reversal, starvation, or priority result.
Its sensitivity view is [sensitivity PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c9f4d7deafbc056ce1c8e68b039be8608464c55fadc7441e4f41da8753e1a72/a2a10ce3e331f10b4ac78e7b9989070484b9e88cdec2a197952eb307aa7af4d8/probability-probability-2f0a01246994931f2a87ecfe-sensitivity.png).

The sweep requested `findRankReversals: true`, but the compact result exposed no reversal count; no claim that there were zero reversals is supported.

Structural `hoi4.event_inspect` and `hoi4.event_render` for `chaosx.nr15.1`, and `hoi4.focus_inspect` and `hoi4.focus_render` for `utopia_manifesto_tree`, each timed out after 600 seconds without an artifact, revision, graph, or render.
`hoi4.reference_context` for AI completed and identified the offline AI wiki and installed AI-strategy documentation.
The later bounded reference-search/read calls did not return before their wrappers were terminated, so the relevant local documentation sections were read directly.

## Findings by probability surface

**Candidate selector.** `utopia_manifesto_prepare_candidate_weight` starts at 10, adjusts the ticket weight from country conditions, and clamps it to 1–60.
The source’s `for_loop_effect` uses an end-exclusive upper bound; the intended number of tickets is therefore the resulting weight.
The caller selects the first non-empty priority class: player generic, AI generic, then approved-light AI.
Lower-priority candidates receive no draw while a higher class is non-empty.
Selection within the chosen array is a weighted-ticket draw (`random_scope_in_array`), not a decision/focus AI score race.
Numeric selector weights for classes 1 and 2 were not changed.
The class-3 candidate gate is now deliberately fail-closed at `common/scripted_triggers/015_utopia_manifesto_triggers.txt:87-89` because the approval flag has no producer and the original-tree identity was not captured for safe return.
This blocks the approved-light synthetic candidate in the after manifest.
Preserve the gate until the approval/capture/return mapping exists; then test the complete class-3 pool and teardown condition under the same scenarios.

The source ticket constants in `common/script_constants/015_utopia_manifesto_constants.txt` are base 10; adds of 15 for weak factories, 10 for small state, 5 for low research, 10 for weak infrastructure, 5 for secure capital, 5 for independence, 5 for no faction, 10 for coastal/island context, 10 for inland-island context, 10 for migration pressure, 10 for housing pressure, and 5 for trade pressure; penalties of 10 for defensive war, 15 for subject status, 5 for occupation, 10 for subject network, 5 for a major guarantor, and 10 for recent industrial growth; then rounding and a clamp to 1–60.


The opening event now records `utopia_manifesto_opening_presented` at `events/015_utopia_manifesto.txt:29`; the selector rejects repeat openings.
It captures the actor’s original generic tree receipt before loading the Event 015 tree and restores generic only when its receipt exists and Event 015 still owns the current tree.
A country that has since received a foreign tree is preserved.
The pulse uses actor-once flags and the interval helper; it can emit at most one ordered incident per pulse.
These mechanisms alter eligibility/cadence, not the numeric AI score values.

**Event `ai_chance`.** The file contains 289 option-level `ai_chance` blocks.
The opening `.1` local option pair has `.1.a` at `certain = 100` and `.1.b` at `disabled = 0`, with `is_ai=no` on `.1.b`.
Narrative constants range from `disabled = 0` through `certain = 100`; named intermediate weights include 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, and 75.
Narrative factors include `avoid = 0.25`, `continuity = 2.00`, and `war_pressure = 4.00`.
These are option weights normalized only within a complete local event option pool, not the probability that the event fires.
No exact full-file option probabilities are claimed.
The submitted full-file analysis was partial and later stale, with many options unresolved under the synthetic campaign fixture.
Event firing cadence, outer event selection, player popups, and external option triggers are not part of a local `ai_chance` normalization.

**Decision and mission AI.** The main decision file has 105 `ai_will_do` blocks; the prefire evolution file has 1; the evolution-consumption file has 15.
Their values are willingness scores, not click probabilities.
Current AI base constants range from `never = 0` to `automatic = 100`, with intermediate values 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 18, 20, 30, and 50.
Modifier factors range from 0.1 to 5.
Source-side edits changed cost and affordability conditions but did not change numeric AI weights, per the decision owner.
The four growth decisions are `decision_utopia_raise_a_citizen_watch`, `decision_utopia_form_engineer_companies`, `decision_utopia_hire_auxiliary_contracts`, and `decision_utopia_reinforce_post_formation_defense`.
Their original four dynamic formation debits remain.
Auxiliary Contracts also requires the combined support-equipment stock for its formation debit plus the 50-unit support gift to the selected partner.
The other six boundary-tested bundles are listed above.
The current fixture omits boundary cases for all four changed growth decisions, and the decision AI compare summary was not retained, so affordability changes remain unverified by a scenario trace.

**Focus AI.** The focus tree contains 124 focuses and 124 `ai_will_do` blocks.
Selection is a random-score race among currently available focuses after AI strategy factors; numeric focus AI weights were not changed.
The fixture leaves `focus.external_factors_complete` false, and does not provide a complete live eligible pool.
The 124-candidate comparison is score-oriented and explicitly incomplete; no rank, starvation, dominance, or selection-probability conclusion is made.

**MTTH and timing.** `common/mtth/015_utopia_manifesto_mtth.txt` has six country-scope entries: the incident interval and five evolution intervals.
The incident’s base is 120 days and the evolution bases are 150, 210, 270, 330, and 390 days.
Source modifiers use factors for war (0.75), severe Need (0.75), low Plenty (0.75), low Concord (0.80), high Assignment (0.85), constitutional crisis (0.65), and formed Commonwealth (1.25), applied only where each entry declares them.
The effect assigns `mtth:utopia_manifesto_incident_interval` to a temporary delay and schedules a delayed country event; this is computed scheduled cadence, not native event `mean_time_to_happen`.
No exact cumulative timing is claimed because no successful bounded MTTH trace was recovered.
The submitted native-event MTTH compare response was among the truncated batch results; its result is unresolved here.

**AI strategy and advisors.** `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` contains 32 `ai_strategy` assignments.
Strategy values include `avoid_starting_wars`, `build_building`, `build_army`, and `send_volunteers_desire`; the source package’s AI-strategy probability adapter parses only research and focus strategy forms and does not extract all Event 015 strategy types.
Their combined rank and interaction with engine/mod factors remain unresolved.
Sixteen advisors use the same shared base factor `1.00`, with route-specific availability.
No advisor-specific probability adapter was exposed; flat advisor scores and rank against other recruitable advisors are unverified.

Event 015 strategy constants in `common/ai_strategy/015_utopia_manifesto_ai_strategy.txt` are low 30, moderate 60, high 100, war caution -100, war moderate -60, war restraint -160, war crisis -220, and war escalation +60.
The `avoid_starting_wars` modifiers combine with engine and other mod strategy factors, so these values are not standalone campaign weights.

## Reference evidence

The offline `AI modding - Hearts of Iron 4 Wiki.md` snapshot SHA-256 is `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818` (AI weighting and strategy sections at lines 26-37, 74-115, and 1212-1238).
The offline `Event modding - Hearts of Iron 4 Wiki.md` hash is `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` (event timing and `ai_chance` at lines 130-161).
The offline `Decision modding - Hearts of Iron 4 Wiki.md` hash is `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` (decision score behavior at lines 357-385).
The offline `National focus modding - Hearts of Iron 4 Wiki.md` hash is `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203` (focus selection at lines 604-630).
No web wiki was used.

Installed vanilla `common/ai_strategy/_documentation.md` hash `70f5d755ae7ed4060e49cc64a393d1a0dc5611b3acc8abc6dfb4538781c915a1` was read at lines 197-210 (`avoid_starting_wars`) and 447-460 (`build_building`).
Installed effect/dynamic-variable docs were also checked directly.
The installed documentation does not provide a complete guide to the focus `ai_will_do` score race, event option normalization, or decision AI ordering, so the offline wiki and source adapter limits remain material.

## Conclusions and recommended follow-up

Do not tune the positive AI weights from the present run.
The selector’s class priority is intentional but starves lower classes by design; the modeled approved-light pool is correctly blocked by the current fail-closed gate.
Event option probabilities, focus AI rankings, and decision availability require complete candidate and external-factor state before a campaign balance claim is possible.
The near-flat advisor base factor warrants a separate candidate-pool comparison if advisor selection is intended to be meaningfully prioritized.

The next probability pass should add below/equal/above affordability fixtures for each of the four growth decisions using their current full-price quoted costs, model the combined Auxiliary support gate, and retain the same IDs for before/after source snapshots.
A separate source/trigger-level decision inspection is needed because `decision_ai_will_do` reports scores and does not model custom-cost availability.

After the comparison and bounded evaluations, the shared-effect source advanced from comparison-time SHA `0e05dafecbbf2364716febb1c19fd6be069f201c43abe9320c53623b367f1eb2` to final observed SHA `3e55ff988d0762e4674b586fe05b51f0e39c5a9f7f76d6db4f4ee2f4afb185f3` at 23:41 UTC.
The event file remained `55a18a9102a81810291b2b4af55bd1349fa4301b88f1f309889872bd271464a8`.
The parent identified the shared-effect delta as a weight-neutral manual BATCH feedback-routing change; the final helper-source hash is recorded separately because it postdates the probability artifacts.
The final helper revision therefore has no same-revision probability artifact.
Recheck if its diff changes a weighted option's eligibility or weight expression.

No probability weights, prerequisites, or costs were changed by this auditor.
Audit conclusion: **incomplete for release-balance sign-off** because key MCP inspect routes timed out, decision and MTTH compare summaries were lost in the bounded output, the event artifact is partial/stale, focus and event candidate pools are incomplete, and the four new growth-cost boundary cases are absent.

Skills applied: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-planning`, and `chaos-redux-improvement-loop`.
No skill was created or changed.
