# Event 021 manual-scenario ticket uniqueness repair

Disposition: implemented for source-level country uniqueness. Probability comparison and runtime scenario validation remain unresolved.

## Acceptance basis and behavior

The Event 021 manual-scenario contract builds a unique eligible-country count, draws countries into a selected-country array, then freezes each selected target once for preflight and commit. The user requires Maximum to commit every eligible normal human country and all scenario target selection to remain dynamic. No country may be selected twice into that unique target set.

Before this repair, the draw removed exactly `individual_crisis_targeting.load_zero_tickets` tickets after selecting a country. A candidate whose adjusted ticket count exceeded that shared value could remain in the pool and be selected again during a multi-country draw. The draw budget itself is based on unique eligible-country count, so duplicate selection could consume a requested slot without adding a new country.

The success branch now calls `event021_parent_remove_scenario_target_tickets`. That helper scans the current ticket-array length from the end, removes every row whose country scope equals the selected-country target, and returns before the selected-country count increments. Initial weights, load adjustments, intensity shares, and Maximum's direct all-eligible path are unchanged. Removal work follows the actual current ticket-array size and has no new fixed ticket-count or country-count limit.

## Changed files and identifiers

- `common/scripted_effects/021_random_civil_war_parent_effects.txt`: added `event021_parent_remove_scenario_target_tickets` and replaced the fixed-count four-ticket deletion in the manual scenario draw success branch.
- `common/scripted_effects/021_random_civil_war_parent_effects.md`: documented the helper's array-based bound, input event target, selected-country uniqueness behavior, and probability-validation limitation.

The pre-edit parent-effects source was captured at `docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_parent_effects_current_worktree_capture_2026-09-26.txt`, SHA-256 `B9D5002AF433C4CBC33D2BE3641B63239D3ABCC0DBDA5E030E09D8DB8D599A3C`. The post-edit parent-effects source SHA-256 is `6D736B9413913F1C232DDDC8302F6F7D7C53143D52A01FA1A53D15DDCE3E15DF`.

## Weighted-logic evidence and limits

The pre-edit direct `hoi4.probability_inspect` used `custom_weighted_pool` on the exact parent-effects source and returned `PROBABILITY_SOURCE_INSPECTED` at source revision `ea4669159bc268bcacb07b26a88c4b151990475a45248e401b6d1d6fd5936617`, source hash `6bd965bf376ee70c602e9fcd4f6d0e805be135d7ce10c2ed493c04566070c513`, with `poolComplete=false`, zero candidates, and zero available candidates. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4cdae552a308846be0508861140f802cde624097fcfd0fb285c40c4598abad31/87eef4d593b895e9670c84cd6053075617b99cfa5bc8d5b7a8b039c4fd3aec49/probability-inspect-6bd965bf376e.json`.

The post-edit direct `hoi4.probability_inspect` again returned `PROBABILITY_SOURCE_INSPECTED`, now at source revision `18b4807db5579a6dc63c42d11525e6ef3998e5ccbf5d57465c94f13ff02d04d6`, source hash `65cbdeafa54f422789e4491a22b40b80a2fc977a3e9636f65ad980ef7f7b8df0`, with `poolComplete=false`, zero candidates, and zero available candidates. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0bb8c34fec2a189564f2a6af83bea99232bde144606d99f04785f8116d7d3cb2/f0138dc3936b26811507e58b04eb8aeda2e8496ffe5f7379b2354a5d6eb0e9b1/probability-inspect-65cbdeafa54f.json`.

The baseline handoff is `docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_manual_scenario_probability_baseline_2026-09-26.md`. It names the required scenarios, explains why the installed adapter cannot model the live `every_country` candidate pool, load-derived tickets, eligibility gates, and Event 006 package/anchor receipts, and does not claim any probabilities or balance approval. A separate read-only probability-auditor pass is requested for the same-scenario post-change comparison. Until a valid comparison completes, the probability delta remains unresolved and this fix is not probability-certified.

The current `hoi4.event_inspect` trace for `chaosx.nr21.15` returned `EVENT_INSPECTED_PARTIAL`, revision `60d7bb069cf4775966ed1d430b161f4789d7de3f3784d2498cfa95def6ac54b8`, zero blocking diagnostics, and zero helper projections because the focused route deferred workspace-wide helpers. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ea6160fc1b313a6563a3ada36f43ec86fbde1b7b3b372a4cbfcb67ccd567c32/10179fe65b7135f16091917ab6569885e8e20cda06767a8d63b9d2bb3af41967/event-trace-60d7bb069cf4.json`. This event view does not validate the new scripted-effect loop.

## Remaining tests and risks

The manual scenario route still needs an in-game validation with one eligible country, several eligible countries with uneven ticket counts, a multi-country selection budget, the Event 006 package path, and each non-Maximum intensity. Verify the selected-country array, requested/preflight/committed counts, no duplicate target, and cleanup after both successful and skipped plans. Measure the loop under the largest supported multiplayer-human target set. Maximum remains a separate all-eligible path and was not changed.

The full Event 021 dynamic-front and actor-slot migration remains incomplete. This repair removes one fixed ticket-removal count only; it does not resolve the named secondary front slots or per-crisis front caps documented in the active dynamic-front architecture handoff.
