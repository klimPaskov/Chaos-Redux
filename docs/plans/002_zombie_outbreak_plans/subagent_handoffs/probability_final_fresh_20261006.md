# Event 002 Final Fresh Probability Audit, 2026-10-06

Disposition: partial and unresolved; the exact source-snapshot comparison succeeded, but target-specific AI validity remains unresolved because the former typed candidate ids were consolidated into two generic actions with different adapter types and the current target scopes are not bound by the saved scenarios.

This is a read-only audit handoff for parent review.

No gameplay source, balance target, asset, index, spreadsheet, CSV, runtime, desktop, or game file was edited.

## Sources and MCP version

The current decision source is common/decisions/002_zombie_outbreak_decisions.txt, raw SHA-256 45B49A133A44474770F03C7FBFD6651C4C005F81F31D004D8B59FA5088C2422F.

The retained pre-consolidation snapshot is docs/plans/002_zombie_outbreak_plans/subagent_handoffs/probability_release_20261006_evidence/typed_baseline_current_801e2221.txt, raw SHA-256 801E222166733AA43D43A523F6D3B950BCC54EBB36ED9539731AD4D47487CDD3.

The successful comparison used the logical decision source path common/decisions/002_zombie_outbreak_decisions.txt plus snapshotPath and expectedSourceHash to bind the exact retained bytes to the decision source domain.

The focused current-source probability inspection reports source hash 3c63fdb9c41e0c7596c60f2aa5f821898eeb57af0c5aa45110a076eabe2be10e.

The broad current mission inspection found 18 mission candidates in the source and required actor, exists, has_cosmetic_tag, has_idea, is_major, is_subject, scope.any_country, scope.trigger, variable.infantry_spawn_derivative_family_id, and variable.zzz_cure.

The successful comparison reports source revision 84ad58b1e7e8b4ce917e745f21f6415b64cf824055ee41481e45298d4931cc15 and scenario hash c2afb5dd33cd814a3f1c310fd748b63a42700fce833e4a75d974f68954e884da.

The focused review-action evaluation reports source revision a2b6c673fd0c06aa1235ab222023776c0f15da8d83f79c49a7cd60313cb352b4 and the same scenario hash.

The retained scenario contract is docs/plans/002_zombie_outbreak_plans/subagent_handoffs/probability_release_20261006_evidence/typed_counterstrain_scenario_contract.json, scenario set EVENT002_TYPED_COUNTERSTRAIN_BASELINE_20261006.

The two scenarios are USA_AI_STANDALONE_INFECTED_ONLY and USA_AI_STANDALONE_ALL_EIGHT_TYPES, with actor USA and date 1936-07-01.

The adapter artifacts verify Operation Postern 1.19.2.0 (d245) and adapter version hoi4-1.19.2.v1.

The live tool inventory exposed probability inspect, evaluate, compare, and render schemas, but no separate MCP server version or health tool.

The decision references and vanilla map-only precedent retained in release_qa_20261006.md were read as carry-forward evidence; this fresh pass did not repeat the structural decision inspector.

## Candidate pools and adapter boundaries

The baseline scenario contract declares all eight pre-consolidation typed counterstrain mission ids: develop_weaponized_zombie_demonic_counterstrain, develop_weaponized_zombie_infected_counterstrain, develop_weaponized_zombie_mutant_counterstrain, develop_weaponized_zombie_necrotic_counterstrain, develop_weaponized_zombie_parasitic_counterstrain, develop_weaponized_zombie_rabid_counterstrain, develop_weaponized_zombie_undead_counterstrain, and develop_weaponized_zombie_wendigo_counterstrain.

The current source has two generic capital-target actions: review_weaponized_zombie_outbreak_profile and develop_weaponized_zombie_counterstrain.

The live mission_ai_will_do inspection of the current source with the union candidate list found only develop_weaponized_zombie_counterstrain; all eight old typed ids and review_weaponized_zombie_outbreak_profile returned CANDIDATE_NOT_FOUND for this adapter.

The live decision_ai_will_do inspection of the current source found only review_weaponized_zombie_outbreak_profile; the eight typed research ids and develop_weaponized_zombie_counterstrain returned CANDIDATE_NOT_FOUND for this adapter.

The two generic actions therefore do not form one normalized MCP selection pool; mission_ai_will_do and decision_ai_will_do are separate score-only adapters.

The entire current decision source contains more mission and decision candidates than this feature cohort, so this handoff makes no category-wide candidate-completeness claim.

## Same-scenario source comparison

The final bounded compare used mission_ai_will_do, the union of the eight old typed research ids and the two exact current generic ids, and the unchanged two-scenario contract.

The analyzer returned PROBABILITY_ANALYZED_PARTIAL, analysis id probability-516ea181c29da36887ab7f72, 18 candidate identity changes across two scenarios, zero eligible candidates in the current comparison view, zero excluded candidates, and 13 unresolved analysis items.

In each scenario, the eight old typed research candidates are reported as removed and develop_weaponized_zombie_counterstrain as added; the review id is not a mission-adapter candidate.

The current generic research action has exact raw ai_will_do score 1, but its eligibility is unresolved in both scenarios because the adapter cannot bind scope.any_country, has_idea, and scope.trigger from the saved contract.

The old typed per-profile candidateOverrides do not map to the consolidated generic research action, and the named scenarios do not provide concrete generated-country, target-country, controlled-state, or target-scope bindings.

The owner release handoff identifies a source-level reduction from 16 typed action definitions to two generic capital actions.

This compare covers only the eight old typed research candidates and the current generic mission action; it does not compare a before/after review-action candidate or prove a per-type mapping.

The comparison supplies the current generic research raw score, but it does not prove a per-type ranking, target eligibility, click probability, or before/after normalized probability delta.

The analysis classification is score-only for raw AI weights and unresolved for current generic-action eligibility.

## Current review action evaluation

The focused decision_ai_will_do inspection found review_weaponized_zombie_outbreak_profile with poolComplete true for that explicitly bounded one-action request and no required input paths.

The same named scenario ids evaluate that action at raw score 0 with eligibility true in both rows, supportLevel score_only, and no unresolved inputs.

The zero score is an AI willingness score; it is not a selection probability or evidence that the player-facing map action is unavailable.

The corresponding current mission action has raw score 1 in the comparison trace, but its eligibility remains unresolved as described above.

## Other source facts and limits

The owner handoff records the two current capital actions, eight retained profile types, 45 Political Power, 55 research days, 34 strain progress, 240 exposure days, exact-one-type readiness, and the Wendigo transformation lock.

Those gameplay values and gates are source facts, not MCP probability outputs in this audit.

The saved candidateOverrides remain explicit scenario assumptions and do not prove that the live target-country scope, profile ownership, human control, or any_country candidate set is complete.

No combined race between review decision_ai_will_do and research mission_ai_will_do was evaluated.

No probability-proportional selection share is claimed for either score-only adapter.

## Artifact evidence

| Evidence | Artifact URI |
| --- | --- |
| Current whole-file mission inspection | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/715a0b53fecfaaafa7ebe71ed35854dc29262a2602a8b946f8d5a038ec0ddf64/8254d0274bbe7de1bcb5f8539c2dd7ee96839cff249333d269a11bcf6522a007/probability-inspect-3c63fdb9c41e.json |
| Current union mission inspection | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/685722752c0a086ce3571508e7dc9329379bef7dd6569657f2f5a3414ba3783b/fafc9d4a6449029e48599eaed8a1731042568053a40922223d52662f4a631962/probability-inspect-3c63fdb9c41e.json |
| Current union decision inspection | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/457d3a47e4be75639edcc51cef8d52ebe26e0127abf1a6564b0409eacd5e02f9/adf2dab523abbf77e7ce20a5ee8ae84dd3d2114c2c2299f889fc260671b41714/probability-inspect-3c63fdb9c41e.json |
| Focused review-action inspection | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf5360185926cc4f31888c78563507463ceb03516c711065378658cc204593c6/7a3c58dede0a1bf3837979a65886b74082970eb502acdfb25281b2f51f23da99/probability-inspect-3c63fdb9c41e.json |
| Same-scenario comparison JSON | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d8670f73515cd5fae087db9848cd7ba1ff5a58274b2179dbadb273ceaad3fb1/3116c9a95b26c9102e7cc61403f6477c381a3045386a4040705903498755d090/probability-516ea181c29da36887ab7f72.json |
| Comparison PNG | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30b962c2af7f30c31d895feab7273c454abc2b85a1c3c18552e4a32c76ecfd82/b1039723501b1a629fc4568fa10df4dbaa990b960e5dffed63a3f559b34880fa/probability-probability-516ea181c29da36887ab7f72-comparison.png |
| Unresolved PNG | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98e9059c3c95c8b58d3bec9ace71ec096241178677f391a15e9c96a555fd1a8/ac5c7f175bae9db6c41c755de01d5c5b6984217b0669ba9ebc34d320820b0e1f/probability-probability-516ea181c29da36887ab7f72-unresolved.png |
| Current review evaluation JSON | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d449b533e39efe3ff444c33dfe220a23624ea713ee567388601d21eb25cbedeb/a5f0087fcc01d70208893a24595535025b66bc5595339af068b1d0dcd4e57ab0/probability-4a5ee8bb5228ca9141b5dad7.json |
| Review ranking PNG from explicit probability_render | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0510d970a75fe06a3b54da547232c142a6b51c7de97f880bd237cbdc0eb629b/54a045d73737c84122a9193b33464b18e6809897d5f3871824e626672635db4a/probability-probability-4a5ee8bb5228ca9141b5dad7-ranking.png |

The final comparison JSON was retrieved through verified byte ranges and SHA-256 checked against its artifact URI.

The explicit probability_render request for the union comparison returned PROBABILITY_ANALYSIS_STALE because the workspace revision advanced from 84ad58b1e7e8b4ce917e745f21f6415b64cf824055ee41481e45298d4931cc15 to a2b6c673fd0c06aa1235ab222023776c0f15da8d83f79c49a7cd60313cb352b4; the original compare call emitted the linked comparison and unresolved images.

The focused review-action probability_render completed at the same source revision as its evaluation and is linked above.

## Blockers, omissions, and recommendations

An initial comparison with the eight old ids alone returned PROBABILITY_SURFACE_EMPTY after consolidation because none of those ids exists in the current source.

An inlineClausewitz baseline attempt also returned PROBABILITY_SURFACE_EMPTY because the connected analyzer binds inline input under a proposed/inline-probability-source.txt path rather than the decision source domain.

The supported snapshotPath and expectedSourceHash form parsed the retained baseline after the exact candidate union was supplied.

No additional probability retry is needed for this adapter mismatch; the adjusted union comparison is the final same-scenario result.

Keep the current review score at 0 and research score at 1 unless the owner selects a different AI willingness target; this audit does not recommend a numeric change.

Do not use the current generic research score to infer per-type availability or AI selection until the owner can bind the consolidated target scope and active profile type in a supported scenario contract.

Keep decision_ai_will_do and mission_ai_will_do results separate, and do not claim a single category-wide normalized share across them.

## Skills and work boundary

Read and applied .agents/skills/chaos-redux-subagents/SKILL.md, .agents/skills/chaos-redux-events/SKILL.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, and .agents/skills/chaos-redux-mtth/SKILL.md as relevant.

No skills were changed, no tests or game launch were performed, and no commit was created.
