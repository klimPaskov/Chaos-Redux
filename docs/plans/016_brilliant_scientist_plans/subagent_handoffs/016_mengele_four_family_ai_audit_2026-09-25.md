# Event 016 Mengele Four-Family AI Probability Audit

Date: 2026-09-25

Status: source review complete; post-patch Paleogenetics and Xenobiological Synthesis inspections succeeded, and their scenario evaluations returned partial score-only traces with unresolved final scores and ranks. A valid same-scenario compare is blocked because no immutable prepatch source path is available. Materials and Biomedical probability inspections remain unresolved.

## Scope and accepted basis

This read-only audit covers the newly authored provider decision rows `mengele_event016_materials_prototype`, `mengele_event016_biomedical_prototype`, the four `mengele_event016_paleogenetics_*` rows, and the four `mengele_event016_xenobiological_synthesis_*` rows in the four assigned decision files. The existing Materials and Biomedical Theory, Deployment, and Weaponization rows remain in `common/decisions/016_mengele_conventional_stage_decisions.txt` and are not counted as newly authored candidates in this audit.

The accepted scope is `docs/plans/016_brilliant_scientist_plans/016_final_mengele_portfolio_closure_plan_2026-09-02.md`, especially its separate private Mengele provider route and decision availability in both DLC states, together with `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`. The per-family implementation handoffs below record the source-level AI crosswalk to Kruger. These documents establish the provider boundary and the stated crosswalk. They do not set new numeric balance targets. `docs/specs/016_brilliant_scientist_specs/matrices/016_ai_behavior_matrix.md` gives broad family priorities but no numeric decision weights.

## MCP route and evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

| Attempt | Result | Evidence and limit |
| --- | --- | --- |
| `hoi4.probability_inspect`, source discovery without adapter, Materials file | `INTERNAL_ERROR`, message `Unexpected internal error` | No files scanned, candidate pool, source revision, or artifact. |
| `hoi4.probability_inspect`, source discovery without adapter, Biomedical file | `INTERNAL_ERROR`, message `Unexpected internal error` | No files scanned, candidate pool, source revision, or artifact. |
| `hoi4.probability_inspect`, source discovery without adapter, Paleogenetics file | `INTERNAL_ERROR`, message `Unexpected internal error` | No files scanned, candidate pool, source revision, or artifact. |
| `hoi4.probability_inspect`, source discovery without adapter, Xenobiological Synthesis file | `PROBABILITY_SOURCE_DISCOVERED`; suggested adapter `mission_ai_will_do`; four available candidates and four candidate-pool matches | MCP source revision `ac6a52cf5c5d57418abee0a77178c8b1dc45bc5af91785d13c92b8f0152c2c59`; MCP `sourceHash` `751411a4b934e137e32bb0727205508b7b2991d9cd8b1aef4fad36c8e7f96d0d`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63007a8aefbff3a1c3af874417ce49b01815f288b4046af4d04f778dc258622a/e82e2bc7d7027a3d20a258d2b399c6921dbeda6d932f2b3348448c7c1e84bb9/probability-inspect-751411a4b934.json`. No continuation URI was returned. |
| `hoi4.probability_inspect`, explicit `decision_ai_will_do`, all four family files | Materials, Biomedical, and Xenobiological Synthesis returned `INTERNAL_ERROR`. Paleogenetics returned `PROBABILITY_SOURCE_DISCOVERED` with `requestedAdapter=decision_ai_will_do`, `suggestedAdapter=mission_ai_will_do`, `discoveryReason=requested_adapter_empty`, zero candidates under the requested adapter, and four available candidates under `mission_ai_will_do` | Paleogenetics source revision `d964fd9baff87bdcbef013f2dd696c1495057acbd75ae647ba3b91a807d77f9b`; MCP `sourceHash` `ebf20562c0d256d6e3d2cca6429b7e4d85bdfda965ee7d99fdc5a9f6b77d3458`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/31b5c353c1f9c9363c9e97838a459f7dde9f3c718e946a2a328bacc62db8135f/10f7558ea13cebaacd2266ecef5e9edd0b94938a6b451433484bbdbcd09c3bcf/probability-inspect-ebf20562c0d2.json`. No continuation URI was returned. |
| Corrected `mission_ai_will_do` inspect, Materials file | No MCP response surfaced before the exec cell was terminated at 31 seconds | This was the first source in a serial corrected-inspect loop. The loop was stopped before Biomedical or Paleogenetics received this adapter attempt. No result, revision, or artifact is claimed. |
| `hoi4.probability_evaluate`, Xenobiological Synthesis file, `mission_ai_will_do` | Client-side 25-second bound expired with no MCP response | Three named scenarios were submitted for the four Xenobiological Synthesis rows. No analysis ID, scenario hash, scores, ranking, diagnostics, or artifact was returned. |
| `hoi4.probability_compare`, Kruger board source versus Xenobiological Synthesis source, `mission_ai_will_do` | Client-side 20-second bound expired with no MCP response | The same three scenario IDs and an eight-ID union candidate pool were submitted. No comparison ID, source revisions, scenario hash, diagnostics, or artifact was returned. This is not a successful comparison. |

The ordinary source entries are decision blocks in `common/decisions/*.txt`, but the connected inventory exposed their candidates under `mission_ai_will_do` and exposed zero Paleogenetics candidates under the requested `decision_ai_will_do` adapter. This source-type and adapter-label mismatch is unresolved. I used the adapter that the successful inventory exposed for the bounded Xenobiological evaluation and compare attempts. Neither call returned evidence. The adapter issue and timeouts prevent an engine-backed score audit for any of the four families.

The evaluation scenario set submitted was `E016_MENGELE_PROVIDER_AI_BASELINE_2026_09_25`:

| Scenario ID | Actor | Submitted state |
| --- | --- | --- |
| `E016_XENO_PEACE_HIGH_CIC` | `GER` | `has_war=false`, `num_of_civilian_factories_available_for_projects=20` |
| `E016_XENO_WAR_HIGH_CIC` | `GER` | `has_war=true`, `num_of_civilian_factories_available_for_projects=20` |
| `E016_XENO_PEACE_LOW_CIC` | `GER` | `has_war=false`, `num_of_civilian_factories_available_for_projects=0` |

The submitted evaluation candidate pool was the four Xenobiological Synthesis decision IDs listed above. The compare used those four IDs plus their four Kruger counterparts. The service returned no scenario hash for either call, so no hash is supplied here. No local substitute hash was computed.

The MCP source hashes also differ from the raw local SHA-256 values recorded below for Xenobiological Synthesis and Paleogenetics. The tool did not return its hash definition, so byte identity between those inventory artifacts and the current files is unresolved. Do not use the discovery artifacts as proof that current working-tree bytes were scored.

## Source identity recorded at initial audit

Git HEAD at inspection: `4e00548b4e36a6499cbd9586107c7ec382714203`. The four assigned decision files were untracked at this HEAD. Hashes below are SHA-256 of the current working-tree files, read after the MCP attempts.

| Source | Working-tree SHA-256 |
| --- | --- |
| `common/decisions/016_mengele_materials_stage_decisions.txt` | `A75D59F2153BBE9A7D4BDCB02105BCAA604FDC73A4E85F0A8EA82CD43F566048` |
| `common/decisions/016_mengele_biomedical_prototype_decision.txt` | `529EB153259BB5993DEC34A3DE6D8036D72508759148474D5BE54773D023B00C` |
| `common/decisions/016_mengele_paleogenetics_stage_decisions.txt` | `DD5B6DB1BD72A2A170CCE58FB88F8C9C7A926EA34A45844FB4908FAB1D4A378D` |
| `common/decisions/016_mengele_xenobiological_synthesis_stage_decisions.txt` | `8B1EB8E25C71BD722DABC750E801E9A7D4A16F94A95E8E2FF57DCB183F4EC2CD` |
| `common/decisions/016_mengele_conventional_stage_decisions.txt` | `48CD2DD6A7414320EDD8C173B8FFAFA24D9A488C7B3E4FC24A3CFD65AA8A4303` |
| `common/decisions/016_brilliant_scientist_directorate_project_board.txt` | `EE129E541E275A4C48CF6FE375E8AE2833D85529E6CE5EF74B6707282B405293` |
| `common/script_constants/016_brilliant_scientist_project_constants.txt` | `A95301ED9CBC7BB8FCB751885165F62AE5AA8C6B315EADB0C5CDAF79350CE131` |
| `common/scripted_triggers/016_mengele_paleogenetics_stage_decision_triggers.txt` | `A457BD6F889EA2EF163EA4F0D536AAB8213377737DDE496A63F2F35A8D8BCF0A` |
| `common/scripted_triggers/016_mengele_xenobiological_synthesis_stage_decision_triggers.txt` | `41596F306175804D52908601C91F0AE6239A1B57CA8A53142066238775773664` |

## Source-level Kruger comparison

The accepted portfolio closure plan keeps Mengele stage receipts private and separate from the Kruger board. The implementation handoffs state that provider AI should mirror the matching Kruger stage base and the shared wartime and cautious factors, while using provider-specific capacity triggers.

| Mengele decision | Matching Kruger decision in `016_brilliant_scientist_directorate_project_board.txt` | Base constant in both source rows |
| --- | --- | --- |
| `mengele_event016_materials_prototype` | `brilliant_scientist_fallback_materials_prototype` | `ai_high` = 10 |
| `mengele_event016_biomedical_prototype` | `brilliant_scientist_fallback_biomedical_prototype` | `ai_high` = 10 |
| `mengele_event016_paleogenetics_theory` | `brilliant_scientist_advance_paleogenetics_theory` | `ai_medium` = 5 |
| `mengele_event016_paleogenetics_prototype` | `brilliant_scientist_fallback_paleogenetics_prototype` | `ai_high` = 10 |
| `mengele_event016_paleogenetics_deployment` | `brilliant_scientist_advance_paleogenetics_deployment` | `ai_medium` = 5 |
| `mengele_event016_paleogenetics_weaponization` | `brilliant_scientist_advance_paleogenetics_weaponization` | `ai_medium` = 5 |
| `mengele_event016_xenobiological_synthesis_theory` | `brilliant_scientist_advance_xenobiological_synthesis_theory` | `ai_low` = 1 |
| `mengele_event016_xenobiological_synthesis_prototype` | `brilliant_scientist_fallback_xenobiological_synthesis_prototype` | `ai_high` = 10 |
| `mengele_event016_xenobiological_synthesis_deployment` | `brilliant_scientist_advance_xenobiological_synthesis_deployment` | `ai_low` = 1 |
| `mengele_event016_xenobiological_synthesis_weaponization` | `brilliant_scientist_advance_xenobiological_synthesis_weaponization` | `ai_low` = 1 |

The current Mengele source rows use `brilliant_scientist_project_ai.preferred_factor` on `has_war=yes` and `brilliant_scientist_project_ai.cautious_factor` on a family-private low-capacity trigger. The shared constants are `preferred_factor=2` and `cautious_factor=0.50`. The matching Kruger rows use the same base and factor constants with `brilliant_scientist_has_low_project_capacity`. Materials and Biomedical use their own private Prototype low-factory-margin predicates. These are source formula comparisons only. No raw MCP score trace or same-scenario Kruger comparison returned, so factor-value parity does not prove equivalent runtime outcomes.

## Reconciliation of historical boundary report and current source

The previous version of this handoff reported one strict Weaponization-threshold cautious trigger shared by all four stages in each family. Treat that table as a record of the earlier audit observation only; it is superseded for current-source conclusions.

For Xenobiological Synthesis, the family worker handoff says the former shared cutoff was replaced. The first-audit local source hashes were decision 8B1EB8E25C71BD722DABC750E801E9A7D4A16F94A95E8E2FF57DCB183F4EC2CD and trigger 41596F306175804D52908601C91F0AE6239A1B57CA8A53142066238775773664. The owner-patched current hashes are decision 38D5232F6099985BF1710EE372554E7A79648A333974F613D6C90D65B8EF899B and trigger 5FC76BEC30F2A2FCACF80A5643083725FD1EE7322D8F1D5A8AFFCCC84384C1E3.

For Paleogenetics, the earlier four-family report recorded decision hash DD5B6DB1BD72A2A170CCE58FB88F8C9C7A926EA34A45844FB4908FAB1D4A378D and trigger hash A457BD6F889EA2EF163EA4F0D536AAB8213377737DDE496A63F2F35A8D8BCF0A; these equal the current hashes verified in the shared checkout and listed by the provider-family auditor. Those hashes therefore do not identify a distinct prepatch version for the earlier shared-threshold claim. The earlier Paleogenetics shared-threshold observation is not bound to immutable historical source bytes and must not be treated as a verified source baseline.

The former reported boundary table applies only to that prior observation: under its reported strict family-wide checks, the lower stages received the cautious factor at both one-spare and equal-to-quote boundaries, while the Weaponization stage did not. The exact old Paleogenetics bytes cannot be recovered from the retained source artifacts. The old Xeno inventory artifact contains decision candidate discovery, not the old trigger source.

Current source and the 2026-09-25 provider-family and family-worker handoffs show four stage-specific inclusive no-spare-factory triggers for each family. Each trigger uses NOT = { available project factories > that stage quote }, so the cautious factor is active at equality and suppressed with one factory above the quote.

| Family | Stage | Current factory quote | One-spare boundary | Equal-to-quote boundary | Current trigger |
| --- | --- | ---: | --- | --- | --- |
| Paleogenetics | Theory | 1 | 2, no | 1, yes | brilliant_scientist_mengele_paleogenetics_theory_decision_no_spare_factories |
| Paleogenetics | Prototype | 2 | 3, no | 2, yes | brilliant_scientist_mengele_paleogenetics_prototype_decision_no_spare_factories |
| Paleogenetics | Deployment | 4 | 5, no | 4, yes | brilliant_scientist_mengele_paleogenetics_deployment_decision_no_spare_factories |
| Paleogenetics | Weaponization | 6 | 7, no | 6, yes | brilliant_scientist_mengele_paleogenetics_weaponization_decision_no_spare_factories |
| Xenobiological Synthesis | Theory | 1 | 2, no | 1, yes | brilliant_scientist_mengele_xenobiological_synthesis_theory_decision_no_spare_factories |
| Xenobiological Synthesis | Prototype | 2 | 3, no | 2, yes | brilliant_scientist_mengele_xenobiological_synthesis_prototype_decision_no_spare_factories |
| Xenobiological Synthesis | Deployment | 5 | 6, no | 5, yes | brilliant_scientist_mengele_xenobiological_synthesis_deployment_decision_no_spare_factories |
| Xenobiological Synthesis | Weaponization | 7 | 8, no | 7, yes | brilliant_scientist_mengele_xenobiological_synthesis_weaponization_decision_no_spare_factories |

Paleogenetics uses decision file SHA-256 DD5B6DB1BD72A2A170CCE58FB88F8C9C7A926EA34A45844FB4908FAB1D4A378D and trigger file SHA-256 A457BD6F889EA2EF163EA4F0D536AAB8213377737DDE496A63F2F35A8D8BCF0A. Xenobiological Synthesis uses decision file SHA-256 38D5232F6099985BF1710EE372554E7A79648A333974F613D6C90D65B8EF899B and trigger file SHA-256 5FC76BEC30F2A2FCACF80A5643083725FD1EE7322D8F1D5A8AFFCCC84384C1E3. The source trigger references are unchanged from the shared base and cautious AI factors; no AI base or factor was changed by these owner patches.

## Post-patch MCP inspection and evaluation

Both current decision files were inspected before their post-patch evaluations. The connected service classified these ordinary decision rows under mission_ai_will_do and returned all four stage candidates for each file.

Xenobiological Synthesis inspection returned source revision c6da05ee36ed4f27489a1dff3246a76694979763fac53fb9c4d8e076a9fd3fcb and MCP sourceHash d543d5d5b12f3a60715c07582fb3f4ce9b2b741a6516916f3f64fcef2e3f1fe3. Its artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5d4e785f6f493a49ff0db826b371c14dd8873ae94c363eb7ad7938c6a5b2f51/cb2ee1033916d94b08809fd0a68cb9991dc21005da92ca549e5023ed3705c414/probability-inspect-d543d5d5b12f.json.

Paleogenetics inspection returned source revision 1082bd199032ac306f9526055a81ff9214ee69fb225576dff47ff901af5b96ae and MCP sourceHash ebf20562c0d256d6e3d2cca6429b7e4d85bdfda965ee7d99fdc5a9f6b77d3458. Its artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5efe330dc82da16399b0a967cdd6baf17470c43748b019983b1aa0d2407ae9c/a59c5be6301100a7ab2dbd8f00f13905e2b6a4b3239578a6d2662292fd8e1f98/probability-inspect-ebf20562c0d2.json.

The first Xeno evaluation wrapper was rejected because scenarioSet.scenarios entries require a state record; the service reported that state was undefined and that has_war and num_of_civilian_factories_available_for_projects were unrecognized at the scenario entry. The corrected call put both values in state and returned PROBABILITY_ANALYZED_PARTIAL. The Paleo call used the corrected shape and also returned PROBABILITY_ANALYZED_PARTIAL.

| Family | Scenario set and IDs | Scenario hash | Analysis ID | Evaluation source revision |
| --- | --- | --- | --- | --- |
| Xenobiological Synthesis | E016_MENGELE_PROVIDER_AI_BASELINE_2026_09_25: E016_XENO_PEACE_HIGH_CIC, E016_XENO_WAR_HIGH_CIC, E016_XENO_PEACE_LOW_CIC | c83b701f15e6f6862ad8d1d3dc10b4f7c270bb32655658fb2e9a500158a46634 | probability-89d00956b13a7fee4fe4d710 | 659ec5ec6ccfd29b4158fa0b900f338aceb498fc24e93eb180bbdc5ce5dd348f |
| Paleogenetics | E016_MENGELE_PROVIDER_AI_BASELINE_2026_09_25: E016_PALEO_PEACE_HIGH_CIC, E016_PALEO_WAR_HIGH_CIC, E016_PALEO_PEACE_LOW_CIC | 513a76ec2cf22491e639c96845817df029da15bd2b017c1614defdb0ea26cafd | probability-8e57d428b70c6ead3b614bc6 | 73a1beefab7b4300cad532b321b4cb048eed58088e4a15b4fefac224c08f401e |

Each peace/high-CIC scenario used actor GER, has_war false, and 20 available project factories. Each war/high-CIC scenario used actor GER, has_war true, and 20 available project factories. Each peace/low-CIC scenario used actor GER, has_war false, and zero available project factories. The candidate pool passed for each evaluation was the four stage IDs in that family file. The evaluator marked the per-scenario four-row pool complete, but this does not establish the full country-wide decision race or a probability denominator.

The Xeno evaluation JSON artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d67751d7174f48d4641d31b00a19650b11d5e344be07705c855a5b9d61be58b0/56da0e0c08c35df15d571855f7fb99d6b8006e401048013202d95523788e5a39/probability-89d00956b13a7fee4fe4d710.json. Its ranking and unresolved views are hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93fdda216f1125b0172c71609e91763212cfd28d4a2dc853335c38bea72d0c77/2ba2c50ac186ce54fa6c969b47f18e9b8d9ef28297700269f9a6132f8e2f3b93/probability-probability-89d00956b13a7fee4fe4d710-ranking.svg and hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/692a7f8c74384c81b6229e1d9302a178e871a9f9cd836166170696622aab3f28/b5ad59e048547a3de0e51a65698adc86af18cd72a58e79ac5bb4cef8f7c99301/probability-probability-89d00956b13a7fee4fe4d710-unresolved.svg.

The Paleogenetics evaluation JSON artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af8b7f53836d254e09055836debe67f08645499e52996a05283c4e492de0849b/7b8e1d2e8254ac9ca122861cb1cd98eefbe77bf71451a5db66ecc499c9036d23/probability-8e57d428b70c6ead3b614bc6.json. Its ranking and unresolved views are hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28e8a2af5732b78b4c11934786d788f1c532373167e720ce34feb949a2bba543/4d3fede4b5b7d372f38f26ae5a97a0743b0adef825833663932944907fbb89db/probability-probability-8e57d428b70c6ead3b614bc6-ranking.svg and hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/692a7f8c74384c81b6229e1d9302a178e871a9f9cd836166170696622aab3f28/4f33d6c91dc2596e1c44f172085b31bd3ead393e9c8e69eef190d3407fc08c0a/probability-probability-8e57d428b70c6ead3b614bc6-unresolved.svg.

Both evaluations are partial score-only analyses. The base traces resolved exactly to Xeno Theory/Prototype/Deployment/Weaponization values 1/10/1/1 and Paleogenetics values 5/10/5/5. In the war/high-CIC scenarios the preferred factor resolved to 2, producing intermediate traces 2/20/2/2 and 10/20/10/10 respectively; in both peace scenarios it was false. The cautious factor token was 0.5, but its condition remained unresolved for every candidate and scenario. Final rawValue was not emitted, eligibility was unresolved, rank was null, and conditionalProbability was null.

For every candidate in every scenario, the evaluator reported unresolved custom_trigger_tooltip eligibility checks and that num_of_civilian_factories_available_for_projects could not compare the declared scenario value. Thus the scenario inputs did not prove whether the patched no-spare trigger activated at equality or one spare. The ranking SVG labels 0.00000 are placeholders accompanying unresolved candidates, not observed raw scores. The adapter identifies mission_ai_will_do as score_only, does not normalize selection probability, and reports evaluation cadence without modeling a click probability. No dominance, starvation, or rank-reversal conclusion is supported.

The current MCP sourceHash is the analyzer hash for the decision file and differs from the local raw SHA-256. The evaluation provenance links each current family-specific no-spare trigger and reports trigger source hashes matching the local current trigger SHA-256. MCP source revisions changed between inspect and evaluate; both revisions are retained above rather than treated as identical snapshots.

## Result classification, comparison blocker, and follow-up

Current per-stage trigger logic and local source hashes are exact source observations. The returned MCP base and wartime modifier traces are exact for their resolved operations. Final scores, cautious-factor activation in the named scenarios, rank, eligibility, and selection probability are unresolved. The per-file candidate pool is complete for the declared four candidates in each analysis; full game-wide candidate and external-factor coverage is not established.

A post-patch probability_compare was not run because no immutable prepatch source path is available. The installed compare contract requires nonempty before.path and after.path values with the identical saved scenario set; it rejects sourceRevision/sourceHash as substitute source identity, and an analysis or inspect artifact URI cannot replace the pre-edit source. The earlier prepatch decision files were untracked at the recorded HEAD and no immutable copies were supplied or retained. The Xeno prior SHA identifies the old bytes but not an accessible before.path; the prior Paleogenetics report has no distinct prepatch hash. Comparing the current file to itself would not yield a historical delta. The exact before source requirement is the blocker, not a reported compare success or engine pass. The earlier compare call using the Kruger board as before and Xeno as after also timed out without a response and was not a before/after patch comparison.

A probability sweep was not run because the evaluations left every candidate score, eligibility, and rank unresolved. The evaluation calls returned ranking and unresolved visual artifacts, so those are retained above; no standalone probability_render call was made. Simulation and sequence analysis do not apply to these deterministic decision score expressions.
The applicable materials reviewed were `AGENTS.md`; the eleven required offline wiki pages (`Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding`); `.agents/skills/chaos-redux-subagents/SKILL.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; `.agents/skills/chaos-redux-events/SKILL.md`; vanilla documentation `script_concept_documentation.md`, `triggers_documentation.md`, `effects_documentation.md`, and `modifiers_documentation.md`; and vanilla `common/decisions/GER.txt`, including its `ai_will_do` score and modifier examples. The wiki and vanilla references distinguish AI willingness scores from event-option probability sampling and show that score modifiers do not by themselves establish a click probability.

## Work boundary

This report is the only file written for this assignment. No gameplay or AI source was edited, staged, or committed. Hearts of Iron IV was not launched.
