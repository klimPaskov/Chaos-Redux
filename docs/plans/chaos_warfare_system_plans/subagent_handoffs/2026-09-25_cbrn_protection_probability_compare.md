# CBRN Protection Decision Probability Compare Handoff

Date: 2026-09-25.
Status: Post-edit evaluation is partial; the same-fixture compare is blocked by a stale pre-edit source hash.
Disposition: unresolved pending an evaluator route that can address both source snapshots.

## Audited surface

The weighted surface is the mission_ai_will_do score for cbrn_recondition_old_masks, cbrn_convert_civilian_mask_industry, cbrn_simplify_filters_for_mass_issue, and cbrn_export_protective_equipment in common/decisions/cbrn_protection_decisions.txt.

The parent edit removes each native PP cost, adds ai_hint_pp_cost values of 10, 30, 20, and 15 respectively, gates availability on the corresponding PP threshold, and debits PP in each decision's complete_effect helper. This handoff is read-only; no gameplay files were changed.

The local source review covered common/decisions/cbrn_protection_decisions.txt, common/scripted_triggers/cbrn_protection_triggers.txt, common/scripted_effects/cbrn_protection_decision_effects.txt, and common/script_constants/cbrn_system_constants.txt. The four ai_will_do blocks are unchanged in the source diff. The custom cost helpers add PP gates and immediate PP debits, while ai_hint_pp_cost supplies the AI's reservation hint for custom PP spending.

## MCP evidence

The required first hoi4.probability_inspect call used adapter mission_ai_will_do, source {path:"common/decisions/cbrn_protection_decisions.txt"}, the exact four-id candidate pool, and refresh=true. It returned PROBABILITY_SOURCE_INSPECTED, poolComplete=true, four candidates, six required input groups, zero unresolved inspection items, and availableCandidates=0 in the inspection view. That last field is not a scenario eligibility result because no scenario state is supplied to inspect.

This turn's inspect reported source revision 3ef8643dac1801e6f039300d8eaa8b97ea975ca88039bf5c46a7028dc94241e4 and MCP source hash 71c6265420ba03a7c8f94283b249c2a56d898d4688227ccd32ba5a5faf357d3a. The inspect artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b75de4da13de986db2d6c5b52047fb323a40e3db76ec89dccaedab941c48cb4/76e0a254e3000ffe2f9753f09335a200b8af7aa1a47fe77989f102ecc8ad042f/probability-inspect-71c6265420ba.json (artifact SHA-256 3b75de4da13de986db2d6c5b52047fb323a40e3db76ec89dccaedab941c48cb4).

The post-edit hoi4.probability_evaluate used the exact fixture docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-25_cbrn_protection_probability_scenarios.json and the exact same four-id candidate pool. The fixture SHA-256 recorded by the baseline handoff is 64acbe863a6daa9173f954a1ce48fbfdbc5d9f07b4809deb4c5e026120d64274. The scenario hash from this evaluation is 1edc53b2709f2906d65c6c21639c585fec6e94573862b64687f4159326c34992.

The evaluation returned PROBABILITY_ANALYZED_PARTIAL, analysisStatus=partial, 14 scenarios, 56 candidate-scenario rows, 24 unresolved items, zero diagnostics, and six visual resources. Its source revision was b26af07d75fbf09cfa48f47f4730750ffddb2563fb4e4d3f4e1f8b0129638b79, with MCP source hash 71c6265420ba03a7c8f94283b249c2a56d898d4688227ccd32ba5a5faf357d3a.

The authoritative evaluation JSON artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88bbc768023666a63abc1214bdec65f2d58420c804e805b43dcbcac6c99378a8/75a03dfa5cf6de87fc13a05f9591a8ab2921b5dcb5bafecad6f87bca265ef27c/probability-1fc403cd1c81753fed73dad7.json (artifact SHA-256 88bbc768023666a63abc1214bdec65f2d58420c804e805b43dcbcac6c99378a8). Evaluation rendering returned ranking SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88a4491e7eda9d7c4751aa1d129246cfb47083a2179a97aa61edc2e29426cb33/a358b3323fa07a2d8d2e3a7ecde30219b2cd8d6d12eeab02c468b29fb26d00dd/probability-probability-1fc403cd1c81753fed73dad7-ranking.svg, ranking PNG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad0cb8caa3b73af5b2215ff569c60fd346f320aa266b65ad260378f61b1675a0/8005b402a7f8aec6582047df255ec4d226bb43f30c2a37b6b515d99557b3fc7f/probability-probability-1fc403cd1c81753fed73dad7-ranking.png, waterfall SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ca3f21c251209acee4ef263309a2bb7b413ba56e5bfef846e744625d45716f4/0bfb8eefb3aea05d6b2f4ece42b521aee4da7f441f49b4de66a2ccfdcc3d91ee/probability-probability-1fc403cd1c81753fed73dad7-waterfall.svg, waterfall PNG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10fcf0d14e9966d30850a370de6138411cbf2b1696bd511f7f67b20c8be2b1cd/204d97ac5c10a886f5825d417d12a34c90e9a46e43113124916e23b73e8066ee/probability-probability-1fc403cd1c81753fed73dad7-waterfall.png, unresolved SVG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a364999f13adbd720e759aa42d2b1dae439628dd4df82ba46fbd313ee12282f/89943914cde59b75714999337bbf04f839f881af83d53f9402d2c97d999e41fa/probability-probability-1fc403cd1c81753fed73dad7-unresolved.svg, and unresolved PNG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/422c83fd14e5d4b4efe2a95742d594270de8755a87d3c2b3d19caebfd132c58a/e7ac2f3a96922fd4c7e92fe4910dd94dafde7e9eb6597844f5e488dabac37b37/probability-probability-1fc403cd1c81753fed73dad7-unresolved.png.

The MCP tool response exposed scenario counts and artifact links inline, but not the candidate score rows or individual unresolved traces. No per-scenario numerical score or resolved eligibility claim is copied here. A separate hoi4.probability_render request for analysis id probability-1fc403cd1c81753fed73dad7 and the same scenario hash returned PROBABILITY_ANALYSIS_NOT_CACHED with blocker “Render requires an analysis ID produced by this server process”; it returned no additional artifact.

One same-fixture hoi4.probability_compare was attempted with adapter mission_ai_will_do, the same candidate pool and fixture, before.expectedSourceHash=19d2547ba34b6c8439bac578820bd49828c4fb6ee8a5d194c82403f98cd70dcf, and after.expectedSourceHash=71c6265420ba03a7c8f94283b249c2a56d898d4688227ccd32ba5a5faf357d3a. MCP returned PROBABILITY_SOURCE_STALE, “Probability source hash is stale”, expected old hash 19d2547ba34b6c8439bac578820bd49828c4fb6ee8a5d194c82403f98cd70dcf, actual indexed source hash 51f615f58e6ada5e778ff6d031c78d9994f8d1e0dbaa728e162315e0b162ca63, and no compare artifacts. The actual indexed hash matches the current local decision file SHA-256. The old expected hash is the captured pre-edit local file SHA-256 from the baseline handoff. The compare therefore did not establish a before-and-after result.

The current MCP source hash 71c6265420ba03a7c8f94283b249c2a56d898d4688227ccd32ba5a5faf357d3a is the hash reported by inspect/evaluate metadata, while the current local file SHA-256 is 51f615f58e6ada5e778ff6d031c78d9994f8d1e0dbaa728e162315e0b162ca63. This turn's inspect revision 3ef8643dac1801e6f039300d8eaa8b97ea975ca88039bf5c46a7028dc94241e4 differs from the parent-provided post-edit inspect revision 3af48c034c6f47d3bead19b92151aa4514b4c52cd0336c5baa96d586cf37a008, but both report MCP source hash 71c6265420ba03a7c8f94283b249c2a56d898d4688227ccd32ba5a5faf357d3a. The evaluator reported a third source revision b26af07d75fbf09cfa48f47f4730750ffddb2563fb4e4d3f4e1f8b0129638b79 for that same MCP source hash.

After this MCP comparison, the parent removed redundant zero-valued native `cost` fields from the hospital and shelter decisions in the same source file without changing these four `ai_will_do` blocks. The final local file SHA-256 for that later cleanup is `bdcddee979de76de95e50d9828bd594df849c1e2203f08d64e049af80e6add1f`; the `51f615...` hash above identifies the payment-patch snapshot that the comparison actually inspected.

## Scenario coverage and result classification

The named scenario ids were recondition_pp_below_support50_factories1, recondition_pp_exact_support50_factories1, recondition_pp_above_support50_factories1, convert_pp_below_support250_factories3, convert_pp_exact_support250_factories3, convert_pp_above_support250_factories3, simplify_pp_below_support150_factories2, simplify_pp_exact_support150_factories2, simplify_pp_above_support150_factories2, export_pp_below_reserve1500_factories1, export_pp_exact_reserve1500_factories1, export_pp_above_reserve1500_factories1, export_stock_below_reserve1500, and export_stock_above_reserve1500.

The fixture brackets the intended PP amounts at 9/10/11, 29/30/31, 19/20/21, and 14/15/16. It also probes support-equipment and civilian-factory boundaries for the three national procurement decisions, and masks at 1,499/1,500/1,501 for export. Candidate pool completeness is exact for the four requested ids; it is not the game's full decision-choice denominator. mission_ai_will_do reports raw willingness scores and does not normalize them into click probabilities or model a decision timing distribution.

External-factor coverage remains incomplete. Flat primitive state cannot bind the source's compound scripted triggers, check_variable conditions, equipment checks, technology, and all target validity conditions as engine-native typed state. Export also requires an eligible target relationship, and the fixture's FROM=ITA mask stock alone does not prove that target eligibility. The evaluation's 24 unresolved items mean the fixture did not produce a full set of exact scenario eligibility and score traces.

Result classifications:
- Inspect: exact discovery that the requested four-id pool is complete for this request and that the selected source exposes the mission_ai_will_do adapter.
- Post-edit evaluation: score-only adapter analysis, partial as a whole, with 24 unresolved items; individual numeric traces are not claimed in this report.
- Post-edit compare: unresolved because the captured pre-edit hash is stale against the current indexed source.
- Click probability, timing, and full-category ranking: unresolved and outside what this score-only adapter proves.

## Source-level weights and risk findings

The local source and the unchanged common/script_constants/cbrn_system_constants.txt hash confirm that the four ai_will_do formulae remain the pre-edit formulae. Their constants recorded in the baseline handoff are base_procurement=1, low_stock_factor=3, industrial_reserve_factor=2, chemical_enemy_factor=4, mass_civil_defence_factor=3, at_war_factor=1.50, export_surplus_factor=1.50, and export_shortage_factor=0.

The source-level formulas are:
- cbrn_recondition_old_masks: base_procurement, multiplied by low_stock_factor when the country needs imported masks and industrial_reserve_factor for the industrial-reserve profile.
- cbrn_convert_civilian_mask_industry: the same factors plus chemical_enemy_factor when an enemy has used chemical weapons.
- cbrn_simplify_filters_for_mass_issue: base_procurement, multiplied by mass_civil_defence_factor, at_war_factor, and low_stock_factor when their triggers apply.
- cbrn_export_protective_equipment: base_procurement, multiplied by export_surplus_factor when export stock is available and export_shortage_factor when the country needs imported masks.

These are source-level score expressions, not MCP-resolved scenario values. The export shortage factor of zero can suppress export willingness when the shortage trigger is true, including at the 1,500-mask boundary if its additional filter-condition, stock, and factory predicates also hold. The fixture omits the filter-condition probe for export, so that boundary remains unresolved. No exact dominance, starvation, or rank-reversal result is proven.

## Recommendations, skipped analyses, and limits

Keep the four existing ai_will_do expressions unchanged until a same-source-snapshot comparison is available. Do not infer that ai_hint_pp_cost changes the willingness score; the offline decision-modding reference describes it as an AI PP reservation hint for custom costs, while ai_will_do is a separate score race.

Resolve the pre-edit source-hash blocker before claiming a post-edit score comparison. The compare's stale error is consistent with the baseline handoff's earlier stale-source evaluation, which reported no numerical pre-edit baseline. If a later route can address an immutable pre-edit snapshot, rerun the same named fixture and candidate pool, then sweep PP, stock, factory, and shortage boundaries. Prioritize the export row's exact 1,500-mask shortage predicate when those typed inputs can be bound.

hoi4.probability_sweep was skipped because the parent explicitly directed finishing after the single same-fixture compare returned stale; no thresholds or rank reversals are MCP-proven. hoi4.probability_simulate is inapplicable because the fixture declares no uncertain input distributions. hoi4.probability_sequence is inapplicable because these are decision willingness scores, not a declared custom weighted pool with cadence and state transitions. A second compare or source refresh was not run.

## References read

Offline wiki pages: Data structures - Hearts of Iron 4 Wiki.md, Triggers - Hearts of Iron 4 Wiki.md, Effects - Hearts of Iron 4 Wiki.md, Modifiers - Hearts of Iron 4 Wiki.md, Localisation - Hearts of Iron 4 Wiki.md, Scopes - Hearts of Iron 4 Wiki.md, On actions - Hearts of Iron 4 Wiki.md, Event modding - Hearts of Iron 4 Wiki.md, Decision modding - Hearts of Iron 4 Wiki.md, Idea modding - Hearts of Iron 4 Wiki.md, and AI modding - Hearts of Iron 4 Wiki.md.

Vanilla documentation read: C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md, effects_documentation.md, modifiers_documentation.md, and script_concept_documentation.md. The vanilla decision reference notes has_political_power and add_political_power; the offline decision page documents native decision costs, custom-cost payment, ai_hint_pp_cost, and AI willingness score semantics.

Repo skills read: .agents/skills/chaos-redux-subagents/SKILL.md and .agents/skills/chaos-redux-decisions-missions/SKILL.md. No skill was created or updated.
