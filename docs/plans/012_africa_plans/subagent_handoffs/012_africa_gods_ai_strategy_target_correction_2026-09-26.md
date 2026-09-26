# Event 012 Gods AI strategy target correction — 2026-09-26

Disposition: **source correction implemented; quantitative verification unresolved**. The strategy syntax now targets decision spending explicitly. Existing numeric priorities and army-build values are unchanged.

## Source basis and change

The active user goal requires a working AI route. The offline `AI modding` reference specifies that `pp_spend_priority` requires an `id` target and lists `decision` as a base-game target; vanilla `RAJ.txt` uses `id = decision` for that strategy. Event 012's host and participant policy actions are decisions, so `decision` is the matching category. No other target category or numeric value was changed.

The owner added `id = decision` to the five existing `pp_spend_priority` entries in `common/ai_strategy/012_africa_gods_ai_strategy.txt`. The host values remain 20/35/25 and participant values remain 10/-10; the existing `force_build_armies` values also remain 150/250/200/200. The file's overview now describes the decision-spending target.

## Before source and scenario fixture

The exact pre-change file is preserved at `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_ai_strategy_prechange_2026-09-26.txt`, raw SHA-256 `512983a8803d903907f9427b3d3b7b33a201be904280d869c988587e5161af3f`. The baseline probability inspector reported source revision `bdb611c21e0621ff225092b14b945e7c35003666b2c0dc2e4d215aa76f4e5deb`, canonical source hash `763acf72df105a6ac8708867519b41f92aff481e9b1fd800dfd515e473d540ca`, `discoveryReason=no_weighted_surfaces`, and zero candidates. Evaluating the saved scenario set returned `PROBABILITY_SURFACE_EMPTY` with no analysis ID.

The saved scenario fixture is `docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_ai_strategy_scenarios_2026-09-26.json`. It uses only the live supported `id`, `actor`, flat primitive `state`, `flags`, and `scopes` fields. Host cases use the real vanilla tag `ETH`, the source-backed `gods_of_africa_active` flag, and doctrine values 1/2/3; participant cases use `GER` with the source-backed participant/defiance flags. The evaluator accepted this structure but found no pre-change strategy candidates.

## After source inspection

After the five IDs were added, `hoi4.probability_inspect` returned source revision `2a84205d0ae6181681d9365bd1bb9a9f515ce8c91d63858b4bec72cd388a8d11`, canonical source hash `a3c4be103db94d5c3a07a7c267874f36c7ff62f6e40735b512521892a6a124e8`, `discoveryReason=no_weighted_surfaces`, and zero candidates. Evaluating the identical scenario fixture again returned `PROBABILITY_SURFACE_EMPTY` with no analysis ID. Thus the file now follows vanilla's required `id` syntax, but the installed adapter still does not recognize this source as a weighted surface.

The `chaosx_ai_probability_auditor` ran `hoi4.probability_compare` using the immutable before snapshot, the current source path, and the exact saved scenario set. It returned `PROBABILITY_SURFACE_EMPTY`, `candidatePool=[]`, `availableAdapters=[]`, and no comparison ID or artifact. The before and after evaluations also returned `PROBABILITY_SURFACE_EMPTY`; no after-source candidate was available to compare. The source correction therefore remains quantitatively unverified, and unchanged raw values are not probability or balance evidence.

## Remaining limits

This correction does not establish actual in-campaign strategy activation or relative decision-selection odds. The current decision, mission, focus, and event-option pools still have incomplete candidates or required inputs, and the full Gods goal also retains its separate event lifecycle, scenario, presentation, and user-owned live-game acceptance gates. No gameplay test or autonomous game launch was performed.
