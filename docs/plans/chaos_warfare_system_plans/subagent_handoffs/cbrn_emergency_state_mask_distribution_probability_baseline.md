# `cbrn_emergency_state_mask_distribution` Probability Baseline

Status: baseline captured before the parent edit; the MCP evaluation is partial and does not establish target eligibility or a click probability.

## Audited surface and source identity

The only audited weighted surface is `cbrn_emergency_state_mask_distribution` in `common/decisions/cbrn_protection_decisions.txt`, under `cbrn_civil_defence_category`, source lines 259–285 at capture.

The local Git revision was `e4c197bba88a5f6c748eb5ede0c062700e83e769`; the local SHA-256 of the decision file was `7c029e52c4344b8503cde7257cc4d8d27ee9992e659666751e374ca70fa60a2b`.

MCP inspection reported source revision `68fd5a9e1a5ff4764ef7e8fa4b58095923a14cefc0cab41e82b05479c5d243a1` and source hash `9981b52f2d2f96f5aa2546cb52fed7de41eef9093cc49e0fc0e1b4aaee4ad3ae`; evaluation reported the same source hash but source revision `a76d6ac48f2ace9c10db31394d4c5fb06007afcf8a07ca27aad70a27d213c8b0`. The discrepancy between MCP revisions is retained as unresolved provenance; the local Git revision and file SHA were unchanged during capture.

Referenced weighted inputs are `cbrn_protection_ai.base_response = 8`, `alert_factor = 5`, `contaminated_state_factor = 3`, and `capital_factor = 3` in `common/script_constants/cbrn_system_constants.txt` (SHA-256 `3dae2d3ab97cccb78f0164dca1854ee0801cee04f68f1ed83146e0d1f1a6971f`). Availability helpers include `cbrn_country_has_any_mask_stock` and `cbrn_state_can_receive_emergency_masks` in `common/scripted_triggers/cbrn_protection_triggers.txt` (SHA-256 `3babc4ee62585c5ff450acf09fab91abd141f3dc2bd49047f8edcf071e3b1443`) and `cbrn_state_has_chemical_contamination` in `common/scripted_triggers/cbrn_triggers.txt` (SHA-256 `892391b2ec11cb022f885cc69e21ad9c48c616f62b4747425ffb9155434caf4a`).

## MCP evidence

`hoi4.probability_inspect` selected adapter `decision_ai_will_do`, discovered one candidate, required inputs `FROM` and `has_equipment`, and reported `poolComplete: false`, `availableCandidates: 0`, and no unresolved items before a scenario was declared. Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/352e5464569bb35533aa7244385bda6324090d876aab4ed8c1ed462f033384af/04b6301593b7112e3fdc25763dc1807379187126266fab43a5bc542bd02f4910/probability-inspect-9981b52f2d2f.json`.

`hoi4.probability_evaluate` used scenario set `cbrn_emergency_state_mask_distribution_baseline_2026-09-25`, scenario hash `6edad30d3de7b147eeef0e91fdd533a75610998d99fc2199a8df6c8c92a67e1e`, and analysis id `probability-d5d2be324e5a83077ac589e1`. The exact submitted call fixture is [cbrn_emergency_state_mask_distribution_baseline_fixture.json](cbrn_emergency_state_mask_distribution_baseline_fixture.json).

Evaluation reported adapter `decision_ai_will_do`, adapter version `hoi4-1.19.2.v1`, game version `Operation Postern 1.19.2.0 (d245)`, source hash `9981b52f2d2f96f5aa2546cb52fed7de41eef9093cc49e0fc0e1b4aaee4ad3ae`, source revision `a76d6ac48f2ace9c10db31394d4c5fb06007afcf8a07ca27aad70a27d213c8b0`, and eight named scenarios. Result code was `PROBABILITY_ANALYZED_PARTIAL`; analysis status was `partial`; the adapter declares `selectionRule: score_only`, `rawScore: true`, `normalizedProbability: false`, `sequence: false`, and `timeDistribution: false`.

Evaluation JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4cd20072800fd511ff3a3c3f396107dad6cccb384f522e0868ff2ee4d17665b8/ffe36cb7e44f26cc7faf3b5fde5b50847f293971eeac4d8756cb49b778527921/probability-d5d2be324e5a83077ac589e1.json`.

The evaluation emitted ranking SVG and PNG resources at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9f5862684fb845e2b6d4633a237c5e3390a5222147a4c56e14898055a9cdb6d/a300b4606c413a5cec28b94733041c26667d61f098251c6a912c223d6b11b1d8/probability-probability-d5d2be324e5a83077ac589e1-ranking.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28e1b365058840ddd1b55cd089b52f9388c7462eeeae104e0fec5fcb1243d39f/a0347d2b355d2a4120cdca747f899b742932f6508cb8c9688b3785e5cf1bfdb2/probability-probability-d5d2be324e5a83077ac589e1-ranking.png`; unresolved SVG and PNG resources are at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b87273495a4c2442f0f35f4d743d77249a1a6bbed238140c7e93e4a856e56758/fc1048909b7ce10562dd558c47f123f76c82e75110e80aa3ef36acfcd71d2861/probability-probability-d5d2be324e5a83077ac589e1-unresolved.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b532f7b066ef9fc0e3597c9b7c8f4206c6012096181fb2602790f69b5530d3b2/5410e69804bbb2728c203cbcc9c8b31875802313bc1367c18bf2c10e75442480/probability-probability-d5d2be324e5a83077ac589e1-unresolved.png`.

## Scenario results and limits

The base weight is exactly 8 in the MCP trace; the alert, contamination, and capital multipliers are 5, 3, and 3 in the referenced script constants. The available trace showed the alert multiplier inactive and the contamination and capital checks unresolved, so no effective score was established. MCP diagnosed that the alert factor was not active in any of the eight supplied scenarios.

Every scenario retained unresolved eligibility. MCP specifically reported that `has_equipment` was not declared as the scoped/compound trigger; target resolution `FROM` was unresolved; the target lacked declared `is_controlled_by = ROOT` and `state_population_k`; and nested helpers lacked `has_variable`, numeric `cbrn_chemical_contamination`, numeric `cbrn_civilian_mask_effective_coverage`, and `is_capital` inputs. Do not infer the decision is eligible or ineligible from these traces.

The `stock-none`, `stock-exact`, and `stock-above` fixture cases supplied only `has_equipment: false/true/true`; exact stock quantity could not be expressed, and the latter two cases are identical for the analyzer. The `eligible-alert` and `stale-alert` cases both supplied the same target alert flag and no distinct eligibility state; the adapter did not activate the alert multiplier in any supplied case. They are labels preserved for the parent’s matching comparison, not resolved eligibility tests.

The `pp-below`, `pp-exact`, and `pp-above` cases supplied `political_power` values 9, 10, and 11. The decision’s native political-power cost is 10, but the inspector did not list political power as an adapter input and the evaluation did not resolve full decision affordability; these cases do not prove selectable status below, at, or above cost.

The declared `candidatePool` contains only this named decision. The adapter does not model a complete state-target or decision-selection race as a normalized probability, so it supplies no click probability, rank reversal, or global category denominator. Result classification is `score-only` for adapter capability and `unresolved` for effective score and eligibility. Starvation, repetition, cadence, and sequence risks remain unresolved because sequence analysis is unsupported and the state-target pool is incomplete.

## Follow-up and recommendations

No AI-weight or prerequisite change is recommended from this baseline. Preserve the `ai_will_do` base and modifiers during a display-only cost edit, and run `hoi4.probability_compare` against the same fixture after the parent change. The comparison should confirm whether the edit touched any score inputs; if it changes actual payment or eligibility, provide a supported state fixture for equipment stock, target ownership, population, contamination, distribution coverage, capital status, and political power rather than treating the current partial result as proof.

`hoi4.probability_sweep` and a separate `hoi4.probability_render` call were not run because the parent asked to stop further MCP retries after the partial evaluation; the evaluation itself emitted ranking and unresolved views. `hoi4.probability_compare` is pending the parent’s post-edit source. Simulation and sequence analysis were not used because uncertain inputs were not declared and the adapter reports sequence unsupported.

## Guidance consulted

Read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-decisions-missions/SKILL.md`. Opened the required offline Paradox wiki core pages and reviewed the decision AI and AI-modifier sections of `Decision modding - Hearts of Iron 4 Wiki.md` and `AI modding - Hearts of Iron 4 Wiki.md`. Consulted the vanilla `triggers_documentation.md` entry for `has_equipment`; it is a country-scope trigger, while the connected probability adapter still requires an explicit scenario-bound representation.

No gameplay, AI, localisation, runtime, or other implementation files were edited.
