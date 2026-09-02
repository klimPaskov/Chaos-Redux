# Event 016 containment decision probability baseline

Date: 2026-09-02

Owner: `chaosx_ai_probability_auditor` (read-only)

Status: final bounded source comparison complete; raw-score deltas are zero where finite, but decision eligibility remains partial and unresolved.

This handoff is bounded to the eight containment decisions and is not an Event 016 completion claim.

The binding design source is `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.

## Scope and source retention

The retained before source is the exact decision blob from commit `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`:

`common/decisions/016_brilliant_scientist_containment_decisions.txt`

The source object passed to MCP used `path` plus the `git show` bytes and was not an analysis ID.

The before decision blob ID is `ac2d60d20e10d1ada83cd13574d7cd0898ef82ef`.

The working-copy decision SHA-256 at baseline was `4902789a99d92529b65ad8d10758afac3623899e2e91aaa054a9de6ec43dc92a`.

The working-copy decision, containment trigger, and containment constant files had no semantic content diff from the retained commit under `git diff --ignore-space-at-eol`; their working-copy SHA-256 values were `4902789a99d92529b65ad8d10758afac3623899e2e91aaa054a9de6ec43dc92a`, `808da14d9777f07404ea0005c64ecf9103d41cbe135a4e5a1f00d7869bc9a6b3`, and `a22d840d15ce99aa9674730e93ffb2cbc429537e70762271877488e188792c00` respectively.

The retained commit blob IDs for the context files are `536ad478578ebd90ad9691240227d1e4ec7759a2` for `common/scripted_triggers/016_brilliant_scientist_containment_triggers.txt` and `7be1512c255f960522ba45c41b2c44e149ff0db7` for `common/script_constants/016_brilliant_scientist_containment_constants.txt`.

The helper provenance exposed by the adapter also reaches `common/scripted_triggers/016_brilliant_scientist_triggers.txt`, whose reported source hash was `ef9b7964617cb6b73cf5bc230fd31751081a0ffc21cca999575dbb45f3853636`.

No gameplay, localisation, specification, asset, workbook, runtime, or weight file was edited by this audit.

## Weighted surface and adapter

The eight candidates are:

`brilliant_scientist_release_kruger`, `brilliant_scientist_exile_kruger`, `brilliant_scientist_arrest_kruger`, `brilliant_scientist_shutdown_directorate`, `brilliant_scientist_ratify_sovereign_charter`, `brilliant_scientist_launch_military_seizure`, `brilliant_scientist_request_foreign_containment`, and `brilliant_scientist_concede_institutional_authority`.

The first mandatory inspect request used the requested `decision_ai_will_do` adapter and returned `requested_adapter_empty` with zero candidates while suggesting `mission_ai_will_do`.

That route result is retained as a capability finding, not as baseline evidence: [probability-inspect-cc69f458d41e](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be584fb1cd1e0ad0bd68acc70bc0d0b0c6352f2c8b914145597d38b8a31fc924/fb74140aedf7128bf87362303756dfcdb68697643794c8271bcb621adcde25a3/probability-inspect-cc69f458d41e.json).

The matching `mission_ai_will_do` inspect succeeded with eight candidates and `poolComplete=true`: [probability-inspect-cc69f458d41e](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42ad7b74fae7f7f7881d69cb84607ddedf680f6bb9cf6a7fe188df746d1e3204/25937d4d42781876284bb72e4c73e0b943f2875d2d4b21f331f9a41dc3bc8eda/probability-inspect-cc69f458d41e.json).

Inspect source hash: `cc69f458d41ebeaa18afac0683fb51301e02e86e890729bdc1cc6ecc32138874`.

Inspect source revision: `7be18c3bdb9c5b43e9375f3367d8acf2ca89ccdb3549f7bd064d9bd5ca57df82`.

The adapter reported six required inputs and no inspect-time unresolved items.

The adapter capability is score-only: it supports raw `ai_will_do` scores and ranks, but does not model normalized decision selection probabilities or a time distribution.

## Exact baseline scenario family

Scenario set ID: `E016_CONTAINMENT_COST_CLOSURE_2026_09_02`.

The exact recovered scenario object is retained as [E016_CONTAINMENT_COST_CLOSURE_2026_09_02.scenarios.json](E016_CONTAINMENT_COST_CLOSURE_2026_09_02.scenarios.json). Its local SHA-256 is `8bba36e6fdf9ca86b74e7e38a2b811c9766c317b702da70bb1c6597ef6f28278`, and it contains all 17 named scenario bodies used by the comparison.

The exact named scenario IDs were:

`E016_CONTAINMENT_LOW_AUTHORITY_PEACEFUL_PUBLIC_HOST`, `E016_CONTAINMENT_HIGH_INDEPENDENT_DANGEROUS_HOST`, `E016_CONTAINMENT_DEMOCRATIC_FACTION_HOST`, `E016_CONTAINMENT_WARTIME_MILITARY_RESPONSE`, `E016_CONTAINMENT_VALID_CHARTER_TERRITORY`, `E016_CONTAINMENT_PROVEN_SAME_TAG_CAPTURE_NON_KRG`, `E016_CONTAINMENT_EXACT_NEW_BOUNDARY`, `E016_CONTAINMENT_ONE_BELOW_EXILE_CONVOYS`, `E016_CONTAINMENT_ONE_BELOW_ARREST_SUPPORT`, `E016_CONTAINMENT_ONE_BELOW_SHUTDOWN_TRUCKS`, `E016_CONTAINMENT_ONE_BELOW_CHARTER_SUPPORT`, `E016_CONTAINMENT_ONE_BELOW_MILITARY_RIFLES`, `E016_CONTAINMENT_ONE_BELOW_FOREIGN_CP`, `E016_CONTAINMENT_ONE_BELOW_CONCESSION_SUPPORT`, `E016_CONTAINMENT_ACTIVE_ACTION`, `E016_CONTAINMENT_CLOSED_BOARD`, and `E016_CONTAINMENT_WORLD_END`.

The fixture dimensions covered low-authority peaceful public hosting, high independent capacity with a dangerous project posture, democratic faction membership, wartime military response, valid charter territory, a proven same-tag capture retaining a non-KRG original host tag, the exact proposed anchor boundary, one below each proposed physical or operational anchor, an active action, a closed board, and the world-end terminal state.

The public contexts declared a democratic government, public compact, public-science context, and a non-KRG actor `ABC`.

The dangerous and wartime contexts declared the secret directorate and strategic-security context where applicable, with high independent capacity and project counts.

The same-tag fixture used actor `ABC`, not KRG, and declared `original_tag = ABC`, `brilliant_scientist_institutional_capture_proven`, `brilliant_scientist_same_tag_takeover`, and `brilliant_scientist_original_host_non_krg` markers.

The proposed anchor boundary fixtures were declared as one below `20` convoys for exile, `600` support equipment for arrest, `200` trucks for shutdown, `600` support equipment for charter, `6000` rifles for military seizure, `20` command power for foreign containment, and `300` support equipment for concession.

The candidate pool was explicitly complete at inspect and evaluation level, but scenario state did not bind every custom helper and typed numeric variable in the adapter’s expected form.

The adapter therefore left the unresolved availability and helper chains visible and did not turn the fixtures into an exact in-engine affordability or click-eligibility claim.

## Baseline evaluation

The before-edit evaluation used `mission_ai_will_do`, the retained source object, all eight candidates, and all 17 named scenarios.

Analysis ID: `probability-65461ff54d419584271d2512`.

Scenario hash: `4a4611db1bd408349d42d455c9c29e22440c1219348239df5198126e05359312`.

Source hash: `cc69f458d41ebeaa18afac0683fb51301e02e86e890729bdc1cc6ecc32138874`.

Source revision: `7be18c3bdb9c5b43e9375f3367d8acf2ca89ccdb3549f7bd064d9bd5ca57df82`.

Result: `PROBABILITY_ANALYZED_PARTIAL`.

Evaluated cells: 136 (8 candidates x 17 scenarios).

Pool completeness: true.

Unresolved items: 28.

Diagnostics: 1.

Support level: `score_only`.

Authoritative JSON: [probability-65461ff54d419584271d2512](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b46be82ddf4a18ef2d8f061a25d69ecc99383905c876489e7e632ea304ded655/1f0fab90df4aae4e9e62d62b2f6b8ea57134cec2a5045222db91c3fc9dfadcdd/probability-65461ff54d419584271d2512.json).

Rendered evidence: [ranking](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f287abd316b674d1362d8665c40c869fb18dd229de0b69fd6d6f8098b9e2815a/445f00083b897301fdcfb26e1b8922d2c9f53afa97addc70484d3e76f5924b4d/probability-probability-65461ff54d419584271d2512-ranking.svg), [matrix](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66cec60c7fcbd15455d869630131d837549fe4ef7ad2bf0dc0a80113f58e449e/6891bf9a9eebf5222d50896339e5cf1858f4faecd314911bc52cb7701c5e72a8/probability-probability-65461ff54d419584271d2512-matrix.svg), and [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbe1088ddb93202c48aec6b6203e27bbc550f9ec9df5061ef61fc9411b97b59a/5de07d47c73a454ac647b76f36afdc92f2702d546020bf50fad5a6f51447a808/probability-probability-65461ff54d419584271d2512-unresolved.svg).

The comparison view emitted by the evaluate operation is [comparison](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/440f9d75bea980977e69123155ff0fcee15787bb80601a25cb40ca71111f0fd0/probability-probability-65461ff54d419584271d2512-comparison.svg); it is not a before/after comparison and must not be read as one.

## Baseline score evidence

Only two candidates resolved to finite raw scores in every supplied fixture because custom trigger and helper state remained unresolved.

The finite scores were:

| Scenario family | `brilliant_scientist_ratify_sovereign_charter` | `brilliant_scientist_request_foreign_containment` | Classification |
| --- | ---: | ---: | --- |
| Low-authority peaceful public host | 72 | 9.6 | score-only; all other candidates unresolved |
| High-independent dangerous host | 36 | 4.8 | score-only; all other candidates unresolved |
| Democratic faction host | 72 | 28.8 | score-only; all other candidates unresolved |
| Wartime military response | 36 | 4.8 | score-only; all other candidates unresolved |
| Valid charter territory | 72 | 9.6 | score-only; all other candidates unresolved |
| Proven same-tag capture, non-KRG tag | 72 | 9.6 | score-only; root/helper semantics unresolved |
| Exact new boundary | 72 | 9.6 | score-only; costs are not part of `ai_will_do` score arithmetic |
| Each one-below payment fixture | 72 or 36 | 9.6, 4.8, or 28.8 according to government/war/faction flags | score-only; affordability not proven |
| Active action, closed board, and world-end | 72 | 9.6 | score-only; visibility/cancel state is outside score arithmetic |

The exact per-ID one-below fixtures are retained in the authoritative JSON under the scenario IDs above; the score pattern is unchanged from the ordinary context unless the fixture also changes government, war, or faction flags.

The finite traces show the source bases and factors being applied in source order.

For charter, the low-authority public fixture resolved `12 x 3 x 2 = 72` from the high base, response-charter factor, and democratic factor.

For foreign containment, the public non-faction fixture resolved `12 x 2 x 0.4 = 9.6`, the democratic faction fixture resolved `12 x 3 x 2 x 0.4 = 28.8`, and the wartime or secret fixture resolved `12 x 0.4 = 4.8` where no democratic or faction preference applied.

The other candidates retain their source bases and factor constants, but their custom trigger tooltips and helper chains remained unresolved, so no exact raw score or rank is claimed for them.

One diagnostic reported that the concession `strong_factor` was not active in any supplied scenario.

## Source cost and modifier baseline

The before source retains these political-power costs: release `25`, exile `40`, arrest `55`, shutdown `65`, charter `75`, military seizure `85`, foreign containment `65`, and concession `50`.

The before source also retains multiple physical or operational gates and spends rather than one anchor per action.

| Decision | Existing physical/operational gates and spends in retained source | Parent’s candidate anchor for the cost closure |
| --- | --- | --- |
| Release | no physical anchor | no anchor |
| Exile | 10 convoys, 5 trains, 100 support equipment | 20 convoys |
| Arrest | 400 support equipment, 1500 infantry equipment, 12000 manpower, 15 army experience | 600 support equipment |
| Shutdown | 300 support equipment, 150 trucks, 10 trains, 1000 fuel | 200 trucks |
| Charter | 20 convoys, 15 trains, 250 trucks, 300 support equipment | 600 support equipment |
| Military seizure | 700 support equipment, 3000 rifles, 300 trucks, 2500 fuel, 25000 manpower, 30 army experience | 6000 rifles |
| Foreign containment | 25 convoys, 350 support equipment, 20 command power | 20 command power |
| Concession | 200 support equipment, 10 trains | 300 support equipment |

The retained decision source applies light, medium, or heavy consumer-goods burden and also applies factory-efficiency penalties through file-scoped modifiers.

The parent’s planned cost patch consolidates each action to at most four axes: political power, one physical or operational anchor, upfront stability, and consumer-goods burden.

The planned patch removes factory-efficiency burden and other deductions or requirements, uses inclusive affordability at the named boundary, and moves player-facing cost text to `custom_cost` with matching political-power AI hints.

Those cost, timer, receipt, visibility, and cancellation changes are not part of `mission_ai_will_do` arithmetic and require separate source/eligibility or structural proof.

## Findings and limits

The candidate pool is complete for the eight named decisions, but the probability adapter’s decision route is empty and its matching mission route is explicitly score-only.

No normalized selection probability is available or claimed because the adapter documents no decision-selection denominator.

No timing distribution, repetition rate, starvation rate, or click probability is inferred from the scores.

The current baseline has no proven dominance or rank reversal across the unresolved candidates.

The finite score ordering is only a partial ranking over the two candidates whose helper chains resolved.

The adapter surfaced unresolved `custom_trigger_tooltip` blocks and helper chains involving `brilliant_scientist_is_current_host`, institutional capture, coercive-risk thresholds, dependence, independent capacity, government control, warned incidents, captured domains, and character presence.

The direct scenario state fields did not satisfy every typed variable declaration expected by the helper evaluator, so the exact low/high threshold and resource-boundary eligibility remains unresolved.

Active action, closed board, world-end, native timed decision cancellation, and own-receipt checks are visibility/cancel semantics, not AI score semantics.

No source-only result is being substituted for those engine-level checks.

## Final bounded source comparison

The final comparison used `hoi4.probability_compare` with adapter `mission_ai_will_do`, the eight-candidate pool above, `before` as the exact decision source from commit `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`, `after` as the frozen current decision source, and the retained fixture with the exact scenario hash `4a4611db1bd408349d42d455c9c29e22440c1219348239df5198126e05359312`.

The final compare analysis ID is `probability-3940462a3287d0e28d957172` with status `PROBABILITY_ANALYZED_PARTIAL`.

The adapter remained `mission_ai_will_do` on game version `Operation Postern 1.19.2.0 (d245)`, with `poolComplete=true`, 17 scenarios, and 136 candidate cells.

The final after-source hash is `0c734710ee13f7fba7bd85874497e8fce93aad149ef24e7711d0fee64191069b`, and the reported after-source revision is `8b501cf7bf1164649f3cfd6bb7e9de01f864dce166b8e6603b2c1391b75eacea`.

The compare recorded 136 scenario changes, all attributed to `added eligibility:hidden_trigger:unresolved:` at each decision's `available.hidden_trigger` path after the shared `can_pay_containment_<action>` checks were added.

No nonzero raw-score delta and no nonzero rank delta were reported. The finite score formulas therefore show no weighted AI change, but the newly introduced payment helper calls are not bound by the scenario's typed helper inputs, so the result does not prove live selection eligibility or affordability.

The compare's aggregated unresolved count is 44, and the rendered after-scenario summaries leave all eight candidates unresolved in every named fixture. This is an adapter input-binding limitation, not evidence that all decisions are impossible in-game.

One informational diagnostic remains: the concession `strong_factor` was not active in any of the 17 fixtures.

Authoritative JSON: [probability-3940462a3287d0e28d957172](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce09405f2f9ea301464c07b8416b987eb0ef7344cf72d6536a1d302582a41c5b/a45a0d49956fe8bc686954ef400c36fa969d48ef7598cece8ae40e668f1cba80/probability-3940462a3287d0e28d957172.json).

Rendered evidence: [ranking](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1724d5e3a362221319ac8585ea47b76d7d50fb4922185761fe0e4af0309304dc/45a6eb7da4e2363ac6c9c09130b853532559c089183d454193d6f578a6ca8cb7/probability-probability-3940462a3287d0e28d957172-ranking.svg), [matrix](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66cec60c7fcbd15455d869630131d837549fe4ef7ad2bf0dc0a80113f58e449e/3e15aa5e9f73e81c0913b7797607f39c066ae00ec423de6fa849b4813ccf8f91/probability-probability-3940462a3287d0e28d957172-matrix.svg), [comparison](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8674bfab364d829c732d033ec16f35ec423c525b21b1a80a5f995a9099f497b/b0d35ac87a0e42a974f7f837f6d4448d9f7b78a46f34dcd5c5ab402671cd937b/probability-probability-3940462a3287d0e28d957172-comparison.svg), and [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e62f9c41131abdd28152865f3e097a191d9ba654537ef54d32a02a24dca7ef74/9cae857f92811efd1a124fec24a3dce43d3d83e50624eda141d748d1a59953b0/probability-probability-3940462a3287d0e28d957172-unresolved.svg).

The source patch retains all PP, stability, consumer-goods, and timer values requested by the parent, and the eight AI formula blocks were not numerically edited. The compare does not evaluate custom-cost display, native timed-action settlement, stale-receipt cancellation, or GUI visibility, so those remain structural/engine checks outside this weighted score result.

The baseline fixture intentionally carries several mutually exclusive response flags at once so source factors can be compared in a common score matrix. Those simultaneous flags are artificial score fixtures and must not be treated as normal-board eligibility or as a claim that all response modes coexist in a live country.

## Skipped analyses

`probability_sweep` was not run because no balance target or AI score change was requested and the adapter is score-only.

`probability_simulate` and `probability_sequence` were not run because no random distribution or complete custom weighted pool applies.

No event graph call, game launch, or log collection was performed.

The outputs authored by this audit are this handoff and the retained scenario fixture linked above; no gameplay or balance source was edited.

## References and skills

The required offline Paradox wiki pages were consulted for decision syntax, triggers, effects, modifiers, scopes, event targets, localisation, on actions, and AI behavior.

Vanilla documentation consulted included `documentation/triggers_documentation.md`, `documentation/effects_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, and `common/decisions/_documentation.md`.

Skills used: `chaos-redux-subagents`, `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-mtth`.

No skill was created or updated.
