# Missile site scoring repair probability audit

Audit date: 2026-09-13. This is a read-only audit of the State-local industrial eligibility and strategic-region intersection in `missiles_score_site_candidate` and its downstream `missiles_select_best_site` and `missiles_assign_site_strategic_region` helpers.

No gameplay source was edited by this audit, and no source was staged or committed. The owner-applied source receipt is [root_source_edits.json](../root_source_edits.json).

## Scope and source identity

The audited source is `common/scripted_effects/032_missiles_effects.txt`. The preserved prepatch snapshot is `baseline/032_missiles_effects.txt` with SHA-256 `35D8C85E0C6FD7B7E1826135968AD5B2A2E1982D41CE6FB1D8D7CA7B52650903`, and the owner-reported postpatch source SHA-256 is `457e2e8fb8aed64bafc585fa74b0b324ae8db226d89edd6b0615fbed85f51111`.

The owner receipt records three reversible edits: the State industrial gate now ORs `arms_factory`, `industrial_complex`, and `dockyard` against the documented zero value before adding the unchanged `missiles_site_score.industrial_access` value of 8; the region probe now uses one `strategic_region` selector plus State-scope `is_in_array` membership; and the adjacent comment describes that legal intersection.

`missiles_select_best_site` iterates eligible owned States, calls the scorer, and replaces the saved target only on strict `>`. This is a deterministic maximum score race with first traversal order retained on ties. It is not probability-proportional sampling, so the adapter's normalized projection must not be described as a native site-selection chance.

## Required references

The offline wiki pages consulted were `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, `Data structures - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `AI modding - Hearts of Iron 4 Wiki.md`, and the relevant state/building pages.

The vanilla documentation consulted was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, `effects_documentation.md`, `script_collection_input.md`, `script_collection_operator.md`, and `script_concept_documentation.md`. The vanilla precedent `common/scripted_effects/ITA_scripted_effects.txt` uses an OR of `industrial_complex > 0`, `arms_factory > 0`, and `dockyard > 0` for industrial access.

The trigger documentation states that `building_count_trigger` supports `STATE` and `COUNTRY` scopes and includes all three building keys. The offline trigger page states that `any_state_in` accepts exactly one category from `array`, `continent`, `ai_area`, or `strategic_region`, which is the source of the paired24 diagnostic for the former dual-category selector. The same page documents `is_in_array` as the State membership test used by the owner patch.

## Native MCP discovery

The mandatory native `hoi4.probability_inspect` call used adapter `custom_weighted_pool`, source `common/scripted_effects/032_missiles_effects.txt`, identifier `missiles_score_site_candidate`, and workspace `mod_chaos_redux_ea3b2d67c2c0` before and after the owner patch.

The prepatch inspection returned `PROBABILITY_SOURCE_INSPECTED` with zero candidates, zero available candidates, `poolComplete=false`, and zero unresolved diagnostics. Its source revision was `d5381746d11109335c44af125c8bc8d90dbb09c34cc4005e0ade36553313331b`, source hash was `c63d821d83b6a1f961a5b13476c8dd440a6357f1cc624cd323212075afd6a7dd`, and its artifact is recorded in [missiles_site_probability_native_inspect.json](missiles_site_probability_native_inspect.json).

The postpatch inspection returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=identifier_not_found`, zero candidates, zero available candidates, and no native pool. Its source revision was `2dfbba640636946c697e195cb466dd9979859f3332b694d09796a2c3b7064949`, source hash was `8bf2d2fb378b58ed3057fe0130bb26e1d9835ba632410439e07854115de8a0e3`, and its artifact is recorded beside the prepatch artifact.

The custom adapter does not execute Clausewitz effects or infer the `every_owned_state` loop, so this native result leaves the actual runtime candidate pool unresolved. The adapter requires a complete declared pool; the following five-state manifests satisfy completeness only within their declared projection.

## Scenario and projection contract

The exact candidate pool is `site_factory_none`, `site_military_only`, `site_civilian_only`, `site_dockyard_only`, and `site_existing_core_infrastructure`. The named scenario set is `event032_missiles_site_factory_gate_scenarios_20260913` with scenario hash `9773f5a64705c398e3d385d62e24dd4f0de85a8b00af867eb535e60abb353925`.

`MISSILES_SITE_FACTORY_NONE`, `MISSILES_SITE_FACTORY_MILITARY_ONLY`, `MISSILES_SITE_FACTORY_CIVILIAN_ONLY`, and `MISSILES_SITE_FACTORY_DOCKYARD_ONLY` hold the common validity, ownership, infrastructure, and other scorer inputs equal and vary only the stated one-building State-local field. `MISSILES_SITE_EXISTING_CORE_INFRASTRUCTURE` supplies the representative existing rocket site, core, and infrastructure profile with no factory. Each State also declares `country_num_of_factories` to expose the former Country-only trigger, but neither manifest references that aggregate in its score expression.

Both manifests use a +100000 adapter-only offset because the source baseline is negative. The offset preserves all score differences and ranking arithmetic and is not a gameplay value. The prepatch manifest leaves the local factory fields out of the gate, while the postpatch manifest uses `(arms_factory + industrial_complex + dockyard) * 8`; that expression is exactly equivalent to the source OR for the three named mutually exclusive one-building scenarios. A State containing multiple factory types would receive one source bonus but would be counted more than once by this projection, so that combined case is outside the proof and remains a projection limitation.

The manifests, scenario set, and machine-readable evidence are [missiles_site_manifest_before.json](missiles_site_manifest_before.json), [missiles_site_manifest_after.json](missiles_site_manifest_after.json), [missiles_site_scenarios.json](missiles_site_scenarios.json), [missiles_site_probability_baseline_evaluate.json](missiles_site_probability_baseline_evaluate.json), [missiles_site_probability_after_evaluate.json](missiles_site_probability_after_evaluate.json), and [missiles_site_probability_compare.json](missiles_site_probability_compare.json).

## Baseline projection

The baseline `hoi4.probability_inspect` of the declared prepatch manifest accepted five candidates and the complete five-state projection. The exact baseline `hoi4.probability_evaluate` used the scenario hash above, horizon one day, 25 candidate rows, zero unresolved diagnostics, and analysis id `probability-e6012690be70ccfd0561885d`.

The three ordinary candidates scored 30 after the diagnostic offset in every scenario, and the existing/core/infrastructure representative scored 1070. In source arithmetic these correspond to ordinary score `-99970` and representative score `-98930`. The factory scenarios therefore produced no local score distinction before the patch, even when a State had one military factory, one civilian factory, or one dockyard.

The baseline rendered JSON, ranking, matrix, waterfall, and unresolved artifact references are preserved in [missiles_site_probability_baseline_evaluate.json](missiles_site_probability_baseline_evaluate.json) and the parent-copied [missile_probability_baseline.json](../missile_probability_baseline.json). The rendered normalized shares are adapter diagnostics over this fixture and must not be read as runtime site-selection probabilities; tied ordinary rows also received adapter ordering that does not establish the runtime strict-`>` tie winner.

## Postpatch comparison

The postpatch `hoi4.probability_evaluate` used the identical candidate pool, scenario set, scenario hash, horizon, and five-state projection, with analysis id `probability-d1c97286e5c3fe23df95042b`. It returned 25 rows, zero unresolved diagnostics, and no changed common factors.

The mandatory same-scenario `hoi4.probability_compare` used the two declared manifests and returned `PROBABILITY_ANALYZED`, comparison analysis id `probability-70e5f22e3d72a5f285fe6135`, 15 changed rows, zero regressions, `adapterChanged=false`, and `assumptionsChanged=false`.

For `MISSILES_SITE_FACTORY_MILITARY_ONLY`, `site_military_only` changed from 30 to 38, a raw score delta of +8. `MISSILES_SITE_FACTORY_CIVILIAN_ONLY` and `MISSILES_SITE_FACTORY_DOCKYARD_ONLY` show the same +8 delta for their respective local candidate. `MISSILES_SITE_FACTORY_NONE` and `MISSILES_SITE_EXISTING_CORE_INFRASTRUCTURE` are unchanged, and the representative existing/core/infrastructure candidate remains the highest score in every named scenario.

The adapter projection consequently moves the factory-bearing candidate above the tied ordinary 30-score candidates while preserving the representative's rank. The 15 changed rows include the offsetting changes that any normalized fixture diagnostic necessarily assigns to other rows; those values are recorded in the compare JSON solely for reproducibility and are not native probabilities. The comparison has no AST path attribution because it compares synthetic manifests; `root_source_edits.json` is the source-of-truth mapping to the three owner edits.

## Findings and limits

The baseline industrial eligibility was invalid for the State-local scorer because `num_of_factories` is documented as Country-only and means a Country aggregate. The owner patch's three State building predicates match the documented State-capable building trigger and the vanilla OR precedent, preserving the existing industrial-access value of 8 and all other constants and arithmetic.

The paired24 selector diagnostic is adjacent to `missiles_assign_site_strategic_region`, where the former `any_state_in` combined `array` and `strategic_region`, two mutually exclusive selector categories. The owner repair keeps `strategic_region` as the sole `any_state_in` category and applies `is_in_array={array=ROOT.missiles_region_probe_states value=THIS}` inside the State scope, preserving the intended intersection. Parent source validation found effective strategic-region IDs exactly 1 through 304 with no gaps or duplicates and no mod strategic-region override, matching the missile map bounds.

The evidence supports a local tie break and raw score correction in the named projection. It does not prove the full world candidate pool, live engine execution, combined factory-type behavior, or a normalized selection chance. It also does not establish broad balance, starvation, or campaign dominance beyond the representative fixture, whose +1040 raw lead over an ordinary site remains unchanged.

No repetition, cadence, cooldown, recovery, cap, removal, reset, or terminal-state analysis was applicable because the audited helper is a direct per-call score race and no complete dynamic sequence was declared. Seeded simulation was skipped because no uncertain inputs or sampling process were declared. A prepatch sweep was attempted and returned the exact adapter blocker `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request`; no postpatch sweep was required because the constants and ranking dimensions were unchanged.

## Handoff

Owner patch recommendation is satisfied in `common/scripted_effects/032_missiles_effects.txt`: use State-local OR eligibility for the single +8 industrial-access bonus and the legal one-category region selector plus State array membership. No tuning target was selected. The remaining unresolved item is native MCP binding to the scripted helper and the full `every_owned_state` candidate pool; the five-state raw-score compare is the bounded evidence available for the named scenarios.
