# Event 006 allocator probability audit — 2026-08-30

## Scope and disposition

This is a read-only probability audit of the consolidated Event 006 automatic allocator `random_list` in `common/scripted_effects/006_independence_wave_effects.txt:3501`. No weighted value, candidate gate, route, or gameplay source was changed. The whole-event disposition remains HOLD / PARTIAL, and this audit does not establish live release behavior or campaign balance.

## MCP inspection

The required first pass used `hoi4.probability_inspect` with the `random_list` adapter. The source contains a complete 14-entry outer region pool, with no unsupported construct or unresolved expression in the declared list. The inspect result was `PROBABILITY_SOURCE_INSPECTED` with `poolComplete=true`, 14 candidates, and 0 unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27bf7da70dbee56f04f7ffc6348f88d19406c411a2ba04db9458c4db28335a69/98cb75f379bb4b20009dd0980ad5de8e6a47f42676531e53bcc0744e129f8e81/probability-inspect-6baf0f47d8c4.json`.

The inspected source revision was `843ed9a9d73fab1de87cf1ab6132ce9a7a6f946cfa442b20ed6805a151f9ee2f` and source hash `6baf0f47d8c45bfbe1391245e89570ab519526acfa202a7cb924cd4dcd8da291`.

## Named evaluation

The complete 14-entry pool was evaluated under the explicitly empty fixture set `E006_ALLOCATOR_EMPTY_FIXTURE_2026_08_30` with these five named scenarios: `CALM_EMPTY`, `GATHERING_EMPTY`, `RISING_EMPTY`, `TOTALEN_EMPTY`, and `WORLD_COLLAPSE_EMPTY`. Horizon was one day; outputs requested JSON, ranking, and unresolved views; metrics were `raw_value` and `conditional_probability`.

The evaluator returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-905de4e9ea1e4789b6308f58`, 70 candidate/scenario rows, 14 unresolved items, 0 diagnostics, and validation that explicitly surfaced the unresolved/bounded state. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed470a2dc9d1b7a594e44de803e9a7535e59b1d0f5070bf74aad3bb92301b5c1/4063711d4bf41386855e758da7b6ad5da62c3e6e482975998673b66c3fe69892/probability-905de4e9ea1e4789b6308f58.json`.

The evaluation source revision was `92137190baa8cf20595a29e72ae283d1c132327f6f6c96b279168ec70cf3626d`, source hash `6baf0f47d8c45bfbe1391245e89570ab519526acfa202a7cb924cd4dcd8da291`, and scenario hash `7c28997e505f5b1708b0c2b531760721438be1e570a08fee67a416dc1fac29f6`.

The same evaluation returned ranking evidence at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/04d117a5cc9575d399aa755dcde6f1d6b945019c2f79a64ee9c02e3a9082213d/32144972b10e4414a72029d10328bb2fd54fad3a633d2d0b006e9c037db3d1ab/probability-probability-905de4e9ea1e4789b6308f58-ranking.svg` and unresolved evidence at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/7e943735b0deed3e13f35df90ebec5ee10b85700621f8a181ae0019b22ba3758/probability-probability-905de4e9ea1e4789b6308f58-unresolved.svg`.

## Interpretation and limits

The candidate pool is structurally complete for the outer region list, but the empty fixtures do not provide typed country, anchor, host, reservation, package, chaos-band, or dynamic regional-weight state. The 14 unresolved items therefore prevent exact normalized selection probabilities and do not prove eligibility, starvation, dominance, or campaign timing. The result is classified as partial/bounded MCP evidence only.

The five exact automatic target bands remain governed by the source constants and allocator validator (`3/4/5/7/10`, with World Collapse at 10). The evaluator does not replace the source contract or the focused static ladder, reservation, capacity, and SCN-008 checks.

No sweep, simulation, sequence, or comparison was run. There was no accepted before/after weighted patch to compare, and no declared numeric scenario ranges or complete campaign state existed for a threshold or sensitivity pass. No AI or balance claim is made.

## Focused validation

The current allocator, country API, strict flag-family, FORM-16, GUI semantic, and SCN-008 scenario validators passed independently. Their counts and fail-closed package boundary remain recorded in the completion and source-of-truth handoffs.

Live HOI4 execution, save/load, country-release receipts, and user-facing decision or event validation remain outside agent scope.

## Remaining blocker

The required custom `chaosx_ai_probability_auditor` route is not callable in this runtime. This direct MCP pass is retained as structural/partial evidence and must not be promoted to a quantitative balance or exact-probability claim.

No simplification, fallback, gate relaxation, invented identity, or weighted-source edit was made.
