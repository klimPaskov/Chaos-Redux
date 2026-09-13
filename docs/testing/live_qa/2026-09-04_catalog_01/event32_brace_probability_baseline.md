# Event 032 brace repair probability baseline

Audit date: 2026-09-05 (Europe/Kiev).

Status: baseline captured before the owner applies the parser repair; this is a read-only audit and contains no gameplay source changes.

## Scope and conclusion

The audited weighted surface is `missiles_score_target_country_candidate` in `common/scripted_effects/032_missiles_operations_effects.txt`.

The exact source repair is one closing brace (`}`) between source lines 1635 and 1636, immediately after `any_controlled_state = { missiles_operation_target_has_strategic_value = yes }` and immediately before `add_to_temp_variable = { missiles_target_candidate_score = constant:missiles_target_score.strategic_depth }`.

The brace closes the strategic-depth `limit` block. It does not alter any weight, condition, candidate, or effect value.

The pre-repair file snapshot is SHA-256 `FAE1419206A62C6C89559A2383115ECA1961CEF26E33960A8956A544AE670FCD`; the file has 5174 lines at capture time.

The source helper is a deterministic score race, not a probability-proportional pool. `missiles_select_best_target_country` initializes the best score to `constant:missiles_target_score.baseline`, loops `global.enabled_countries_list`, filters with `missiles_ordinary_target_is_valid`, calls this helper, and keeps a candidate only when its score is strictly greater than the current best. The source therefore supports a score-only conclusion; the conditional probabilities below are explicitly an audit-only categorical projection and are not gameplay click or target-selection probabilities.

## Source evidence

The candidate helper begins at `common/scripted_effects/032_missiles_operations_effects.txt:1600`.

Before the missing close, the relevant source is:

```text
		if = {
			limit = {
			ROOT = {
				OR = {
					check_variable = { var = missiles_ai_profile value = constant:missiles_ai_profile.saturation_offender compare = equals }
					check_variable = { var = missiles_ai_profile value = constant:missiles_ai_profile.counterforce_guardian compare = equals }
				}
			}
			any_controlled_state = { missiles_operation_target_has_strategic_value = yes }
			add_to_temp_variable = { missiles_target_candidate_score = constant:missiles_target_score.strategic_depth }
		}
```

The required insertion is:

```text
			any_controlled_state = { missiles_operation_target_has_strategic_value = yes }
		}
			add_to_temp_variable = { missiles_target_candidate_score = constant:missiles_target_score.strategic_depth }
```

The candidate validity source is `common/scripted_triggers/032_missiles_triggers.txt:236-252`.

`missiles_target_is_valid` requires an existing country different from `ROOT`, a war with `ROOT`, at least one non-impassable controlled state, and no subject relationship to `ROOT`.

`missiles_ordinary_target_is_valid` adds `NOT = { is_in_faction_with = ROOT }`, so a faction partner has no positive ordinary-target selection probability even if its score expression is positive.

The score constants are in `common/script_constants/032_missiles_constants.txt:1006-1025`: baseline `-100000`, major `180`, factory step `4`, controlled-state step `5`, active war `45`, first-use pressure `30`, evidence pressure `35`, strategic depth `25`, and profile value `100`; island and resistance adjustments are `-20` and `-30` in the same constant family.

The source score components represented by the audit projection are profile value, major-country bonus, factories, controlled states, active war, evidence pressure, first-use pressure, island adjustment, resistance adjustment, and the strategic-depth term gated by the `saturation_offender` or `counterforce_guardian` ROOT profile plus `any_controlled_state` strategic value.

## Required references consulted

The repository instructions and `AGENTS.md` were read before the audit.

The relevant Chaos Redux skills read were `.agents/skills/chaos-redux-subagents/SKILL.md` and `.agents/skills/chaos-redux-events/SKILL.md`.

The required offline wiki pages read were `Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.

The relevant vanilla documentation read was `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `triggers_documentation.md`, `script_collection_operator.md`, `script_collection_input.md`, and `script_concept_documentation.md`.

The exact diagnosis document read was `docs/testing/live_qa/2026-09-04_catalog_01/event32_helper_parser_analysis.md`.

The Event 032 AI and probability sources read were `docs/specs/032_missiles_specs/032_missiles_probability_scenario_matrix.md`, `docs/specs/032_missiles_specs/032_missiles_spec_part_6_ai_and_probability.md`, and `docs/plans/032_missiles_plans/subagent_handoffs/032_ai_probability_audit_2026-09-01.md`.

## MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

The mandatory first call was `hoi4.probability_inspect` with adapter `custom_weighted_pool`, source identifier `missiles_score_target_country_candidate`, and path `common/scripted_effects/032_missiles_operations_effects.txt`.

That call returned `PROBABILITY_SOURCE_DISCOVERED` with source revision `c14556322e5d93806e6e53981d4490550229900e4efb7e49006c486044dcb6c4`, normalized source hash `06ec1e7f1e576664bf4a39982744d8d8a5c2f28d5804ddb2f6ee68cc7a9900db`, `candidates=0`, `availableCandidates=19`, and no unresolved required inputs.

The 19 available candidates are random-list entries at `common/scripted_effects/032_missiles_operations_effects.txt:2485.entry.1` through `.19`; they are not the target-country score race, and no native custom-pool adapter bound to the named helper.

The authoritative native inspection artifact is [`probability-inspect-06ec1e7f1e57.json`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a2e7bf15aab3399adae1b34a45b937fe52915a61ce35ed3090da00f762e144c/917331c26199b3ea57c081ee0a4e1b248d85ceb6c5516929d2056efe2b37ab6a/probability-inspect-06ec1e7f1e57.json).

Because the native adapter could not bind this helper, an audit-only custom manifest was inspected with `hoi4.probability_inspect` to preserve the score components and run bounded named scenarios without claiming runtime coverage.

The manifest id is `event032_target_country_score_projection_prepatch_20260905`.

The manifest inspection returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, `candidates=3`, `requiredInputs=0`, source revision `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`, and manifest source hash `c58504e110acd71f7830898f791bbb3085813e91108a38fdd569925da97ae766`.

The authoritative manifest artifact is [`probability-inspect-c58504e110ac.json`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84d325af70439e3d914abbeac354a0bed4a58bc499add3e4c023e181fe894bcd/6ec9f212bf3de1fff18d38d31ea8b4e55f5b276f35134ba0b3eafd7375006788/probability-inspect-c58504e110ac.json).

The manifest candidate pool is complete for the declared projection and contains `enemy_major_frontline`, `enemy_minor_distant`, and `ally_faction_partner`.

The manifest state declares all score constants and candidate eligibility inputs used by the scenarios, including `root_strategic_profile`, `major_strategic_depth`, `minor_strategic_depth`, and ordinary-target eligibility for each candidate.

## Named scenarios and completeness

The scenario set id is `event032_target_country_score_projection_scenarios_prepatch_20260905`; its scenario hash from `hoi4.probability_evaluate` is `7943900e81a301c804b7cd64fda52af6e4e23d056f2c01907888857b0f7ae89d`.

Every scenario supplied the complete three-candidate manifest pool and all manifest state inputs.

| Scenario | Strategic depth/profile state | Eligibility state | Projection pool | Live external factors |
| --- | --- | --- | --- | --- |
| `E32_TGT_C_STRATEGIC_TRUE_BOTH_ELIGIBLE` | ROOT strategic profile on; major strategic-depth trigger true | major and minor valid; ally invalid | complete, 3 declared candidates | incomplete: dynamic enabled-country list, actual scope/trigger evaluation, tie order, and operation preflight are external |
| `E32_TGT_C_STRATEGIC_FALSE_BOTH_ELIGIBLE` | ROOT strategic profile on; strategic-depth trigger false | major and minor valid; ally invalid | complete, 3 declared candidates | incomplete: same live factors |
| `E32_TGT_C_STRATEGIC_TRUE_MAJOR_INELIGIBLE` | ROOT strategic profile on; major strategic-depth trigger true | major invalid; minor valid; ally invalid | complete, 3 declared candidates | incomplete: same live factors |
| `E32_TGT_C_STRATEGIC_FALSE_ALL_INELIGIBLE` | ROOT strategic profile on; strategic-depth trigger false | all three invalid | complete, 3 declared candidates | incomplete: fallback behavior is outside this projection |
| `E32_TGT_C_STRATEGIC_TRUE_ROOT_PROFILE_OFF` | ROOT strategic profile off; major strategic-depth trigger true | major and minor valid; ally invalid | complete, 3 declared candidates | incomplete: same live factors |

The projection has no declared cadence transitions, seed, timer history, cooldown, recovery, cap, removal, reset, or terminal state because the named helper is a synchronous score race.

The source path still has unresolved external factors for exact gameplay selection: the contents and iteration order of `global.enabled_countries_list`, actual country scope transitions, the runtime results of `missiles_ordinary_target_is_valid`, candidate state counts and buildings, war/faction/subject status, profile flags, and the fallback `random_country` route in `missiles_ensure_selected_target` when no scored target is found.

## Baseline score results

The `hoi4.probability_evaluate` call used adapter `custom_weighted_pool`, the complete declared pool, the five named scenarios, metrics `raw_value` and `conditional_probability`, horizon one day, and outputs `json`, `ranking`, `matrix`, `waterfall`, and `unresolved`.

The analysis returned `PROBABILITY_ANALYZED`, analysis id `probability-dd6b49e969d5e286cef56791`, analysis source revision `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`, analysis source hash `797a63197ad25d2a888514e8a1374ac1c79f1585814ebad3c9c2efcc1191174b`, and the scenario hash above.

The score and projected normalization results are:

| Scenario | Candidate | Eligibility | Raw score in declared projection | Rank | Conditional probability in declared categorical projection | Classification |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `E32_TGT_C_STRATEGIC_TRUE_BOTH_ELIGIBLE` | `enemy_major_frontline` | true | 410 | 1 | 410/581 = 0.705679862306368330 | exact projection; source semantics score-only |
| `E32_TGT_C_STRATEGIC_TRUE_BOTH_ELIGIBLE` | `enemy_minor_distant` | true | 171 | 2 | 171/581 = 0.294320137693631669 | exact projection; source semantics score-only |
| `E32_TGT_C_STRATEGIC_TRUE_BOTH_ELIGIBLE` | `ally_faction_partner` | false | 100 | — | 0 | exact eligibility result; not a runtime odds claim |
| `E32_TGT_C_STRATEGIC_FALSE_BOTH_ELIGIBLE` | `enemy_major_frontline` | true | 385 | 1 | 385/556 = 0.692446043165467625 | exact projection; source semantics score-only |
| `E32_TGT_C_STRATEGIC_FALSE_BOTH_ELIGIBLE` | `enemy_minor_distant` | true | 171 | 2 | 171/556 = 0.307553956834532374 | exact projection; source semantics score-only |
| `E32_TGT_C_STRATEGIC_FALSE_BOTH_ELIGIBLE` | `ally_faction_partner` | false | 100 | — | 0 | exact eligibility result; not a runtime odds claim |
| `E32_TGT_C_STRATEGIC_TRUE_MAJOR_INELIGIBLE` | `enemy_major_frontline` | false | 410 | — | 0 | exact projection eligibility; no candidate race for this row |
| `E32_TGT_C_STRATEGIC_TRUE_MAJOR_INELIGIBLE` | `enemy_minor_distant` | true | 171 | 1 | 1 | exact projection; source semantics selects the only eligible candidate |
| `E32_TGT_C_STRATEGIC_TRUE_MAJOR_INELIGIBLE` | `ally_faction_partner` | false | 100 | — | 0 | exact eligibility result; not a runtime odds claim |
| `E32_TGT_C_STRATEGIC_FALSE_ALL_INELIGIBLE` | `enemy_major_frontline` | false | 385 | — | 0 | exact projection; no normalized pool |
| `E32_TGT_C_STRATEGIC_FALSE_ALL_INELIGIBLE` | `enemy_minor_distant` | false | 171 | — | 0 | exact projection; no normalized pool |
| `E32_TGT_C_STRATEGIC_FALSE_ALL_INELIGIBLE` | `ally_faction_partner` | false | 100 | — | 0 | exact projection; no normalized pool |
| `E32_TGT_C_STRATEGIC_TRUE_ROOT_PROFILE_OFF` | `enemy_major_frontline` | true | 385 | 1 | 385/556 = 0.692446043165467625 | exact projection; confirms profile gate |
| `E32_TGT_C_STRATEGIC_TRUE_ROOT_PROFILE_OFF` | `enemy_minor_distant` | true | 171 | 2 | 171/556 = 0.307553956834532374 | exact projection; confirms profile gate |
| `E32_TGT_C_STRATEGIC_TRUE_ROOT_PROFILE_OFF` | `ally_faction_partner` | false | 100 | — | 0 | exact eligibility result; not a runtime odds claim |

The strategic-depth term contributes 25 to the major candidate only when both the ROOT profile gate and the candidate `any_controlled_state` trigger are true in the declared projection.

The major candidate remains rank 1 in both eligible scenarios with or without the strategic-depth term, so these bounded cases show no rank reversal.

Turning the ROOT strategic profile off removes the term even when the candidate strategic-depth trigger is true, matching the source gate.

The MCP emitted design warnings for the one-candidate scenario (`PROBABILITY_DOMINANT_OUTCOME`) and for the never-eligible `ally_faction_partner` (`PROBABILITY_OUTCOME_NEVER_ELIGIBLE`); both are expected consequences of the named eligibility cases, not tuning conclusions.

The authoritative evaluation JSON is [`probability-dd6b49e969d5e286cef56791.json`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11d658012603b2e9e51ea64a1693f72cabb306d2c376d3566c3d0a781717995a/c8a9a4cb208d24d44e4fc6104c93f63d5d6bd27f2eeb49b135171f1f1998f1e6/probability-dd6b49e969d5e286cef56791.json).

Rendered MCP evidence from the evaluation is available as the ranking [`PNG`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/062b92e330be8ded66daf473cc9ce8061ee5709eefebe96b22d4dfa104fac4b1/ab721762ad8b62952f88aa04ec04a4ff8c97d036758b3572c2793c9dd86854b9/probability-probability-dd6b49e969d5e286cef56791-ranking.png), matrix [`PNG`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca2005d118ff803e755ab6f5f2b1b302189e1a85dc63cebf03e3c722d36902b9/bf2919f6dcd603dbca6b561a61802b73fb74059a45108f57953b0a755fc02497/probability-probability-dd6b49e969d5e286cef56791-matrix.png), waterfall [`PNG`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30e705195442d455fc8aa773f9286b06c9a96c84be413a897fe592fbe7e2d535/4ac4c9ed54da2cc7fca5ebdbe15d7d1680415ba60e5c09b1ff6c21da6e807f4f/probability-probability-dd6b49e969d5e286cef56791-waterfall.png), and unresolved [`PNG`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741e9e9423642ce8eb7607dbaccbbceeec8fa1c4ab1c760262892070e72be88c/90a94899e6c72c14f7ee189ac3a8c59ac6c4f9cbfc5c7aacb0e3e8f08db2390e/probability-probability-dd6b49e969d5e286cef56791-unresolved.png).

## Structural event MCP evidence

The required `hoi4.event_inspect` lint call used selector `{kind: event, eventId: chaosx.nr32.1}`, both directions, helper expansion, depth 2, and bounded node/edge limits.

It returned `EVENT_INSPECTED_PARTIAL` against cached revision `1102e50fad94d2051bd32d8a7cd64c3429a191f53e98c50d02aeb60327e1dae8`, graph hash `c6850dd8ad35035c9a83ff251c3df14e4e6123af303e2037d032ccbf5ea51b2e`, `helpers=0`, `issues=2199`, and `blockingDiagnostics=1`.

The authoritative lint artifact is [`event-lint-1102e50fad94.json`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42b22d07332e4b1e6a4ae21a358b989d89c6cda0293ad11c67aaab9242298c04/3c6d73d389a3002615183ec2f1990aa394d48395f2b363033d3b622a5438542c/event-lint-1102e50fad94.json).

The required `hoi4.event_render` call used the same selector and bounds with view `unresolved`.

It returned `EVENT_RENDERED_PARTIAL` against the same cached revision and graph hash.

The rendered unresolved artifacts are [`event-unresolved-1102e50fad94.json`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/149bb64ff6af53a5b72b09cd3b1ad23e0a3590504388abc8d984a2e50c8c885c/8adc9a3de4b77e82832ded676ad7eebbc30f49b97c4cee18fb8f129feca7435e/event-unresolved-1102e50fad94.json), [`SVG`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/545920b4b70e76103cbfc1f95100f5781a13853e577afc30acf507bb131272ca/ea9849ced48f47ef33d1ba5c3a48a95265aa1715c77372a3fe477be60d5ea452/event-unresolved-1102e50fad94.svg), and [`PNG`](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27a01d2c1d45ee7c50658f873fc0c8d51f23679147ae43cbbec74756c2557b8b/dcec68979c36277643521476590a645cd772233bf7a7b3433cf904f5f211125bb94/event-unresolved-1102e50fad94.png).

The structural MCP view is partial and cached at an older source revision, so it is evidence of the known unresolved parser state and not a current post-repair validation.

## Blockers and skipped analyses

`hoi4.probability_sweep` was attempted with the named helper and the same scenarios, but the native source surface returned `PROBABILITY_SURFACE_EMPTY` because no custom weighted block matched and only the 19 unrelated random-list entries were discoverable.

The custom audit manifest cannot be passed to `probability_sweep` through the installed route: direct manifest input is rejected at `source`, wrapped manifest input is rejected as an unrecognized key, and a cached manifest identifier returns `PROBABILITY_SURFACE_EMPTY`.

Therefore threshold, sensitivity, and exhaustive rank-reversal conclusions are unresolved beyond the five explicitly evaluated points.

`hoi4.probability_render` was attempted for analysis id `probability-dd6b49e969d5e286cef56791` and the matching scenario hash, but returned `PROBABILITY_ANALYSIS_NOT_CACHED` because rendering requires an analysis id produced by the same MCP server process; the evaluation call itself emitted authoritative ranking, matrix, waterfall, and unresolved resources, which are linked above.

`hoi4.probability_compare` was pending the observed one-brace source change at baseline capture and is recorded below against the same named scenarios.

`hoi4.probability_simulate` was skipped because the named helper is deterministic and no uncertain inputs or seed were declared.

`hoi4.probability_sequence` was skipped because the helper has no complete declared cadence, transition, cooldown, or terminal-state contract.

No live game was launched.

## Findings and owner recommendations

The parser defect is structural and localized: insert one `}` at the exact boundary above.

The score formula is unchanged by that repair, and the bounded synthetic projection shows the expected strategic-depth delta of 25 only under the two source gates.

The positive ally profile score is harmless in the ordinary selector because the faction-partner eligibility trigger is false; it must not be converted into a positive runtime target probability.

The all-ineligible scenario has a zero normalized projection pool; the source then reaches the separate fallback path in `missiles_ensure_selected_target`, so the overall target outcome remains unresolved until that path and the live candidate list are included in a complete scenario.

After applying the brace, rerun `hoi4.probability_inspect` for the exact helper and source path, then run `hoi4.probability_compare` with the same scenario id, candidate pool, and external-factor declarations.

If the native custom-pool adapter remains unavailable, preserve the exact `PROBABILITY_SURFACE_EMPTY` or discovery diagnostic and keep the conclusion score-only; do not infer a gameplay selection probability from the audit projection.

The parent should also rerun the bounded `hoi4.event_inspect` lint and unresolved `hoi4.event_render` against the post-repair source revision to verify that the following helper declarations are visible.

No gameplay weights, conditions, candidate validity rules, or tuning values are recommended for change by this baseline.

## Post-repair native reinspection and compare

The observed current source has SHA-256 `49E0BC2BC87DB597C6BCA7D52B4B72EA90372F2599E926E29AB01637AAE5961B`.

The brace author is unknown. The parent’s hash guard detected the source drift before any parent write, and `event32_brace_observed/provenance.json` records that current source minus exactly one brace reconstructs the prepatch baseline hash.

The post-repair read-only `hoi4.probability_inspect` call used the same helper identifier and source path and returned `PROBABILITY_SOURCE_DISCOVERED` with source revision `e97002abcf41dad3ccd29cd8266858164bc8a7383770ff4c6e7a444c5d24a3b3`, source hash `2900fbbdff58bc4a6adf6dcc8d920874d9b819957c994eb0c14cda34c4a206fd`, `candidates=0`, and `availableCandidates=19`.

The 19 discovered entries remain unrelated `random_list` entries at `common/scripted_effects/032_missiles_operations_effects.txt:2486.entry.1` through `.19`; the named helper is still not bound to a native `custom_weighted_pool` adapter.

The required same-scenario `hoi4.probability_compare` call used adapter `custom_weighted_pool`, actual current helper source for both before and after route inputs, candidate pool `enemy_major_frontline`, `enemy_minor_distant`, and `ally_faction_partner`, and the original five scenario ids.

It returned `PROBABILITY_SURFACE_EMPTY` with no comparison artifact or probability delta because no weighted block matched the named helper; the only available adapter was the unrelated 19-entry `random_list` surface.

This post-repair compare is therefore unresolved for native runtime probability, while the source-level repair provenance remains an observed single-brace change of unknown authorship.
