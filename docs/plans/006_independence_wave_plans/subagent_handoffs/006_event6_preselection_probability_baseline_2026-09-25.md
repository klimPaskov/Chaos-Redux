# Event 006 host-preselection probability baseline

## Disposition

**Baseline source inspection is complete; campaign probability conclusions remain unresolved.** This is a read-only baseline for the planned host-preselection eligibility change, not a balance recommendation or a post-change comparison.

The immutable source supplied to the weighted MCP inspections came from `git show 278ecf1a4939b7d473a7ce35a770a0efd3fe884d:<path>`, not from the edited working copies. The requested Git object resolves to commit `278ecf1a4939b7d473a7ce35a770a0efd3fe884d` (`2026-09-25T18:36:09+03:00`). Its committed blobs for all three inspected weighted files are identical to their blobs at the inspected `HEAD`, `6ef677cb25b6a1a5406f34118791fc5a7be704da`:

| Baseline source | Git blob at baseline and HEAD | Working-tree status |
| --- | --- | --- |
| `common/scripted_effects/006_independence_wave_effects.txt` | `29a676007716457d85a79cc5dd8a4f18dfea7f0d` | Edited; not used as baseline input |
| `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` | `6a833b6050165fda853a5c04eff3021ce6eff319` | Committed bytes match baseline |
| `common/scripted_effects/006_independence_wave_package_planner_effects.txt` | `55eacd856e50f5d07104c15413dd795a6129641a` | Edited; not used as baseline input |

The MCP accepts immutable source through `source.inlineClausewitz`; each weighted source excerpt was extracted from the requested Git commit before it was sent. MCP `sourceRevision` values below are analyzer content revisions, not Git commit identifiers. The uncommitted host-preselection edits were not submitted as baseline source.

## Audited surfaces and source facts

| Surface | Immutable source and identifiers | Baseline source finding |
| --- | --- | --- |
| Outer automatic regional draw | `common/scripted_effects/006_independence_wave_effects.txt:3399-3429,3431-3657,3660-3715`; `independence_wave_prepare_all_automatic_weights`, `independence_wave_select_one_automatic_package`, `independence_wave_allocate_automatic_packages` | Fourteen regional totals feed one `random_list`. The selector repeats while the selected count is below the frozen target and the attempt count is below `maximum_attempts`; it fails closed if the exact count is not reached. |
| Nested regional package draws | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`; `independence_wave_select_region_01_automatic_package` through `_14_automatic_package` | There are fourteen separate nested `random_list` pools with 126 package-weight entries total. They are not one 126-entry categorical pool. Per-region counts are 9, 9, 8, 8, 12, 12, 5, 3, 7, 7, 5, 13, 19, and 9. |
| Candidate score and eligibility | `common/scripted_effects/006_independence_wave_package_planner_effects.txt:585-803`; `independence_wave_calculate_candidate_allocation_weight` | The score starts at zero and receives its base and conditional modifiers only when runtime package-content attestation and the earliest-chaos-band gate pass. An attested candidate below the configured minimum is raised to the minimum. The `can_plan_independence_wave_package_iw_NNN` gates and their state-dependent inputs are computed outside this score helper. |
| Accepted count ladder | `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md:25-40`; `docs/specs/006_independence_wave_specs/matrices/006_wave_tuning_model.csv:1-7` | Calm World 3, Gathering Storm 4, Rising Chaos 5, Chaos Tier 7, Totalen Chaos 10, World Collapse 10. World Collapse retains the 10-package count while changing package/route/force/ambition and danger pressure. |
| Event 005 joint call context | `common/scripted_effects/005_006_liberations_collision_effects.txt:1240-1316` | Event 005 reserves its opening republic footprint before Event 006 allocation in the shared joint plan. Event 006 therefore draws against shared country, anchor, state, and reservation data. |

The nested registry inspection found these source ranges for the fourteen distinct pools: region 01 `:368-379`, 02 `:614-625`, 03 `:786-796`, 04 `:974-984`, 05 `:1222-1236`, 06 `:1487-1501`, 07 `:1630-1637`, 08 `:1733-1738`, 09 `:2120-2129`, 10 `:2423-2432`, 11 `:2648-2655`, 12 `:3282-3297`, 13 `:4141-4162`, and 14 `:4724-4735`.

The accepted host covenant requires hosts and protected-state conflicts to be resolved before candidate selection (`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md:109-143`). In the baseline allocator, candidate selection begins before a selected package reserves its host state. The previous continuation handoff identifies this source-contract gap at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_allocator_audit_continuation_2026-09-25.md:63-75`. This audit measures no probability change for the planned preselection because its eligibility effects depend on an unrepresented host/map fixture.

## MCP routes, schema, and artifacts

The probability adapter was `random_list`, version `hoi4-1.19.2.v1`, with selection rule `proportional_categorical`. The inspection artifact schema is `probability-inspection.v2`. The analyzer requires a complete active pool and resolved numeric weights to report normalized probabilities. Its sequence capability is unsupported for this adapter.

`hoi4.probability_inspect` was run first on the immutable outer draw source, then on the complete immutable regional registry, and on the immutable candidate-score helper. `hoi4.probability_evaluate` used the complete fourteen-entry outer candidate pool in the explicit input-gap diagnostic below. It returned a partial analysis with all fourteen region weights unresolved. The evaluate artifact also emitted ranking, matrix, and unresolved render resources, but those resources contain no numeric ranking or probabilities because every candidate weight is unresolved.

| MCP result | Status, source provenance, and coverage | Artifact |
| --- | --- | --- |
| Outer `probability_inspect` | `PROBABILITY_SOURCE_INSPECTED`; source hash `acfacfbb1b94e0241221532e651d1b6898cbc30acff3a96e23dea53d24c7f3f2`; MCP source revision `c1e7440e6000b0169c9d067bb112e495b560d5d97a1972227c485cfeff48a7cd`; 14 candidates and 14 required regional-total inputs discovered | [Inspect JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b612b0beddf820da1337d723dd4238fbd29b21cd787a2c8be635044e6c4346de/cfb7b61432d140115ecd9680c828edac67612d1af2a779668576b8da1f6d4f52/probability-inspect-acfacfbb1b94.json) |
| Registry `probability_inspect` | `PROBABILITY_SOURCE_INSPECTED`; source hash `30dfe6314a5ee5fc20f3a28df966e63eac1c7d64166a5ffa0dcaff23b9717318`; MCP source revision `9e1fff80f20ec841106991b0664b582098fcc09257d509c25e03971da3cb32c6`; 126 entries across fourteen pools; `poolComplete=false`, 126 required inputs, one unresolved adapter limitation | [Inspect JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ffc119ab3e450d7ce8cbf53a3b88ba41cde094a53cd7c231bcdaa8adb4c54c14/902e4e16923659cd6bf5a9bb9fd33486893e6c5df23fbc2dafe7394c25523070/probability-inspect-30dfe6314a5e.json) |
| Candidate-score helper `probability_inspect` | `PROBABILITY_SOURCE_DISCOVERED`; source hash `83f6a0370e3b3353f2dd267e95c636b5d28d9721c99d6a442b164cfe9a4e80e5`; MCP source revision `6bbb5e39008df6a303b024c1ac1bd38d417e0fdd4fc11d398ac8c81adf8a3c89`; requested `random_list` adapter found no weighted block in this helper excerpt (`no_weighted_surfaces`) | [Inspect JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81e23982e871f434c0f1218cd68c8cae3b27eea7fdc0d6ae87fe6a40f3b30511/914f757f7c4618b64fc4104cb1c24825e9dc7de003f88587427588f013e1848b/probability-inspect-83f6a0370e3b.json) |
| Outer `probability_evaluate` | `PROBABILITY_ANALYZED_PARTIAL`; analysis `probability-571a3ba80be8d65d0370c10a`; source hash `acfacfbb1b94e0241221532e651d1b6898cbc30acff3a96e23dea53d24c7f3f2`; MCP source revision `8b754bef72b27007ec361709914c38065f1b01c2cea30990bff014f3c15526c8`; scenario hash `5af364fa5681ad4d2adc414a504740ddf94db7c12e96ff662a0bd1a35360bf1d`; 14 candidates, 14 unresolved, no numeric ranking | [Analysis JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/359fd1643b97c3e35355ca291bf430c9bf0cf2a349a327e1356f160f8bed81e2/e6044675c89480a7f82a912b0e444177fb9dc98c3740860ba574275fbef22a69/probability-571a3ba80be8d65d0370c10a.json) |
| Evaluate-produced views | These views are attached to the partial analysis with fourteen unresolved weights, so they do not constitute numeric ranking, matrix, or probability evidence | [Ranking SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7686d0ec986ca1b6f6ab47ecf5be2d6a20ca324a19719a6c038cbbd21cac1b6/ed16302c9484a21f51cb9d0483f5f9012c8bdc5d5ca642485e166906a713d5ca/probability-probability-571a3ba80be8d65d0370c10a-ranking.svg), [matrix SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb82348e00a8a5b3a4460776d68a7265653902127409e97b2200fac0a89e1ce4/5cb9517f6a56d2d8d230cfca7601918b4a9f9fc062c91818f70806f4b9412728/probability-probability-571a3ba80be8d65d0370c10a-matrix.svg), [unresolved SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/671c7a4a2028118484a8bdc423adf600b2022755af26439b78383782799a37f2/probability-probability-571a3ba80be8d65d0370c10a-unresolved.svg) |

The remaining evaluate-generated PNG views are [ranking](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a2c0e9a1ee629459e3ba0bf1c8363d67d2041a7792e03efe4c97076102516462/69ae127a33abf1b4009fb7b9469891244d31592f6b931ea95e8bee66394134ca/probability-probability-571a3ba80be8d65d0370c10a-ranking.png), [matrix](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b866eaedbe5ecbe0d18d14585dafe2558723da0ea146e9527e37e586cb61f54/268b88d4bc38c1e0e9549566d8445cd4fa6615372c3f8b9afd3028c292799187/probability-probability-571a3ba80be8d65d0370c10a-matrix.png), and [unresolved](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/443748d25cfe2d3c7c73f1357d1647f95e14a3a02a6d877b89d4c6a07af3fc50/8b15f59a59756b5134e81f3510586026fd9b4c23867f3233fed0176da697464d/probability-probability-571a3ba80be8d65d0370c10a-unresolved.png).

An explicit `hoi4.probability_render` request returned `PROBABILITY_ANALYSIS_STALE`, with analysis revision `8b754bef72b27007ec361709914c38065f1b01c2cea30990bff014f3c15526c8` and current workspace revision `02ca236673c7720f2291af2ae29b1907745b7ecb210963aea2efcf441093e4dc`. The evaluate-produced artifacts above remain linked evidence; the stale render call produced no new view. Direct retrieval of the analysis JSON resource failed with `MCP error -32603: Artifact provenance manifest is unavailable`, including metadata-manifest retrieval. The structured evaluate response is available, but the JSON resource could not be independently reopened.

## Scenario definition and input completeness

The only submitted scenario is deliberately an input-gap diagnostic, not a campaign state or compare-ready baseline fixture:

```json
{
  "scenarioSet": {
    "id": "E006_PRESELECTION_BASELINE_INPUT_GAP_DIAGNOSTIC",
    "scenarios": [
      {
        "id": "E006_OUTER_REGION_TOTALS_UNBOUND",
        "actor": "country_scope",
        "state": {},
        "flags": [],
        "scopes": {}
      }
    ]
  },
  "adapter": "random_list",
  "candidatePool": [
    "independence_wave_region_01_total_weight",
    "independence_wave_region_02_total_weight",
    "independence_wave_region_03_total_weight",
    "independence_wave_region_04_total_weight",
    "independence_wave_region_05_total_weight",
    "independence_wave_region_06_total_weight",
    "independence_wave_region_07_total_weight",
    "independence_wave_region_08_total_weight",
    "independence_wave_region_09_total_weight",
    "independence_wave_region_10_total_weight",
    "independence_wave_region_11_total_weight",
    "independence_wave_region_12_total_weight",
    "independence_wave_region_13_total_weight",
    "independence_wave_region_14_total_weight"
  ]
}
```

This source-level outer candidate pool is complete at fourteen entries, but its effective weights are not complete. The evaluator required all fourteen regional totals and returned all fourteen unresolved. The inner registry inventory has 126 dynamic package-weight inputs split among fourteen categorical pools and is marked `poolComplete=false`; it cannot be normalized as one pool.

The probability scenario schema accepts a flat primitive `state` map, string flags, and declared scopes. It does not bind Clausewitz numeric temporary variables or compound scripted-trigger evaluations, and it has no typed fixture for current candidate arrays, living/registered tag state, host ownership/control/capital, protected-state reservations, prior selections, or the Event 005 reserved footprint. These are required inputs to the package `can_plan_*` gates, score modifiers, region totals, and collision eligibility. The analyzer therefore cannot represent any of the six accepted chaos-band states as a complete selection scenario, nor distinguish the standalone and Event 005 joint collision contexts without inventing data.

No scenario with the six accepted target counts (3, 4, 5, 7, 10, 10) or either collision context was submitted. The diagnostic scenario hash must not be reused as a campaign scenario in a future comparison. No compare-ready `scenarioSet` can be supplied under the inspected schema; the parent must first obtain a supported typed world/host/candidate fixture route.

## Score evidence versus probability evidence

The source defines the following score terms in `independence_wave_calculate_candidate_allocation_weight` and the relevant entries in `common/script_constants/006_independence_wave_constants_registry.txt`. These are source-level score components, not an MCP-computed candidate trace and not selection probabilities.

| Conditional score term | Source value |
| --- | ---: |
| Base | +100 |
| Sponsored candidate; registered tag | +100; +25 |
| New selected region; new selected host | +30; +20 |
| Previously selected package; previous-wave region; previous-wave host | −80; −25; −20 |
| Replicable-independence supported-region recovery when prior-region penalty applies | +15 |
| Signature package below the high-chaos threshold; high-chaos-only package when open | −35; +45 |
| Replicable opening confidence below threshold; at or above high threshold | −20; +15 |
| Dormant-nations registered; regional; signature package | +30; +25; +35 |
| Armed-birth industrial; frontier package | +20; +20 |
| Sovereign-congress regional; signature package | +15; +30 |
| Open-sovereignty high-chaos; formable/route-only package | +55; +40 |
| World Collapse for a package whose earliest band is Totalen Chaos | multiply accumulated score by 1.35 |
| Minimum after valid attestation and band gate | 1 |

Multiple terms may apply together, and eligibility or prior allocations can change between draws. The score values above must not be arithmetically combined into a purported effective score without the scenario's trigger, scope, flag, event-target, and array state. A `random_list` samples proportionally from the resolved nonzero weights in its own active pool; the outer regional draw and later nested package draw are separate proportional draws. This is not an `ai_will_do` willingness score, a player click chance, or a direct probability for receiving a package across the repeated allocation loop.

## Findings by required risk class

| Risk class | Baseline result | Classification |
| --- | --- | --- |
| Candidate-pool completeness | Outer syntax pool has all 14 region entries, but all 14 computed totals are unresolved. Nested source has 126 entries in 14 distinct lists; analyzer marks the aggregate incomplete because it cannot normalize multiple pools together. | Exact source inventory; probability unresolved |
| Candidate validity and impossible/dead/blocked choices | Runtime content attestation, earliest-band gate, per-package `can_plan_*` eligibility, tag status, map ownership/control, and protected-state conflict affect admission. Their complete scenario state was unavailable. | Unresolved |
| Region/package ranking and normalized probability | No numeric weight vector was supplied or produced. | Unresolved |
| Dominance, starvation, or rank reversal | The source includes region, host, prior-package, prior-region, prior-host, evolution, and band modifiers. No valid score trace or complete active pool was available to compare candidates. | Unresolved |
| Repetition and allocation shortfall | The source reruns selection as reservations mutate plan arrays and stops at the exact target or attempt cap. Pool exhaustion or attempt exhaustion fails the exact-count contribution. No sequence simulation is supported by this adapter or this fixture. | Source behavior exact; repetition and shortfall rates unresolved |
| Host-preselection change effect | The baseline selects a candidate before that selected package reserves a host state. The planned eligibility change depends on host preselection and protected-state collision data not representable to the analyzer. | Source ordering exact; probability delta unresolved |
| Standalone versus Event 005 joint collision | The joint path allocates Event 005 first, then invokes Event 006 with the shared plan. The required reserved anchors, countries, states, and host state are unavailable as typed inputs. | Call order exact; odds and collision outcomes unresolved |
| Snowball/exploit risk | Repeated allocations and protection/eligibility checks are visible in source, but no complete-map and state-transition scenario was executable. | Unresolved |

The tuning model's target counts define allocation length, not the weight vector for a draw. Keeping World Collapse at 10 is an accepted count constraint and does not establish its package odds. No numeric target, weight edit, admission change, or balance conclusion is authorized by this baseline.

## Skipped analyses and exact blockers

- `hoi4.probability_sweep` was attempted on the pinned outer excerpt and diagnostic scenario, but returned `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request`. It produced no sweep evidence or artifact. No threshold values or numeric alternatives were invented to force a sensitivity result.
- No seeded simulation was run because the user supplied no uncertain-input distributions or seed, and no unresolved candidate scores can be sampled meaningfully.
- No sequence analysis was run because `random_list` sequence support is false in the inspected adapter, the nested full pool and cadence/state-transition fixture are unavailable, and repeated draws change selection state.
- No `hoi4.probability_compare` was run because this deliverable is the pre-patch baseline and no authorized after-source was supplied. The diagnostic scenario is not a valid campaign scenario for reuse.
- A direct `hoi4.probability_render` request could not render the cached analysis because MCP marked it stale after the workspace revision changed. Evaluate-produced ranking, matrix, and unresolved artifacts are retained above, but they do not resolve the weights.
- The aggregate registry inspect reports `MULTIPLE_CATEGORICAL_POOLS` and requires selecting an individual pool before normalization. The score-helper inspect independently reports `no_weighted_surfaces` because that isolated helper contains no `random_list` block for the adapter to evaluate.
- The nested candidate weights, all fourteen outer total weights, effect-derived host/collision eligibility, target validity, and external map state remain unresolved. No source-only arithmetic or memory was substituted for probability evidence.

The additional structural `hoi4.event_inspect` and `hoi4.event_render` calls were scoped to `chaosx.nr6.1` in the current workspace. They returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, revision `56768c99247c326e71307f4cdcf1093228db1cd5ea1e096d52b5e8deaf49ef59`, graph hash `38bf2a838e569c36fa58186c04afc2e9c09f855d5b02748939397fac7dca0d73`, with a focused boundary, zero projected helpers, and unresolved helper/lifecycle coverage. These structural artifacts are current-workspace context, not immutable baseline probability evidence: [event trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a09608b512ebe740822d3c2feef9bdf98abed7533f2f93c018df94a02ae52eaa/c64afdf7c121b4898ce2456cbc91b3ab8c06883c013282a75da39ef24c4958cd/event-trace-56768c99247c.json), [render manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a5c9f7ab514a9cae8e9ca007956832c589c8d441742f82b1a7561068b55d02d/9e99f266a1c5563aa6f7daca9bde32cd99d9e5f0ec8cc3cea1145149f0e782b0/event-neighborhood-56768c99247c-manifest.json), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40e7b9bb0613ff00bb47d5963d4d4d229da70ab5563bf8662affc2dfcc9f41fc/8ed3347d68bd02369c412f334b9ad3e33f46020e527db121690e79723829bbbf/event-neighborhood-56768c99247c.svg), [PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/855a35b2b53292f7bf0b375744e13ab6b6d469463a229e99af22052b8804cd34/c1284639f83bc1192272f8b51dce2eb51e375ddf125f13eb5eee444dcc391f0b/event-neighborhood-56768c99247c.png).

## Parent follow-up

First obtain an analyzer-supported fixture contract for the active package pool, current host ownership/capital/control, protected-state reservations, candidate arrays, Event 005 reservation footprint, and repeated-allocation state. Then define the six accepted chaos-band cases and the standalone and joint collision cases once with complete candidate pools and external factors; preserve those exact scenario IDs for the authorized post-patch `hoi4.probability_compare`.

Until those inputs are representable, report the host-preselection probability delta, ranking changes, dominance/starvation, rank reversals, repeat rates, and collision odds as unresolved. No numeric weight or balance fix is recommended from this evidence.

## Instructions and scope record

Applied `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.codex/agents/chaosx_ai_probability_auditor.toml`. Consulted the relevant offline wiki random-list pages and vanilla `documentation/effects_documentation.md` for proportional random-list semantics. No skill or gameplay source was changed. No tests or Hearts of Iron IV process were run.

## After-preselection source and compare addendum

### After-source snapshot

The after-source snapshot was read from the current workspace at Git `HEAD` `6abe7b9cf52e1e19dccfb1d74e7227e73dc9bb8c`. The three files' committed `HEAD` blobs still match the immutable baseline blobs; the two preselection implementation files differ only in their uncommitted worktree content. Raw Git object hashes for the current worktree bytes are recorded separately from MCP source hashes because these hash schemes cover different representations.

| After source path | Baseline Git blob | After worktree raw Git object | MCP inspect result and source hash | MCP revision and artifact |
| --- | --- | --- | --- | --- |
| `common/scripted_effects/006_independence_wave_effects.txt` | `29a676007716457d85a79cc5dd8a4f18dfea7f0d` | `9e363184f8bada77bc316a8e3922b367ea6cd854` | `PROBABILITY_SOURCE_INSPECTED`; outer syntax pool complete with 14 candidates and 14 required regional-total inputs. `unresolved=0` is discovery coverage, not a resolved scenario trace. MCP source hash `800416aa4370f500c2799e3cf8abb3cb310da3127c80e4ad01bad8e8f533c4b9`. | MCP source revision `e81a658d4f4c75652b4c60d44b55a87c3826bb98f4d8c925d7ed3b3cf09e6a50`; [inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43510e2103b175e420147b1156b1d6e588ad45bf241811d0f7ff4c630b0d8048/f227daf7459242a2f068f4f76f91f38fdffdfcc040c26d12272788fc43b92645/probability-inspect-800416aa4370.json) |
| `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` | `6a833b6050165fda853a5c04eff3021ce6eff319` | `6a833b6050165fda853a5c04eff3021ce6eff319` | `PROBABILITY_SOURCE_INSPECTED`; 126 entries in fourteen distinct pools, `poolComplete=false`, 126 required inputs, one unresolved multiple-pool limitation. MCP source hash `17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6`. | MCP source revision `9e2a7f1e34449c4d10e468361e6857608cd1326a18dedc5009406240af50da3a`; [inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a782b1eb8b75e36af0abf642d7ec0ad7f53d9f88f47ae77c1028a5fefbee99d5/65114480d299b2863f0c6559acb7a77a276b28caa95a0049e5aa51958fa90ab0/probability-inspect-17e35c209602.json) |
| `common/scripted_effects/006_independence_wave_package_planner_effects.txt` | `55eacd856e50f5d07104c15413dd795a6129641a` | `d3c1a9b7b8174aaf9477a0d4d7d67d795edd9d07` | `PROBABILITY_SOURCE_DISCOVERED`; requested `random_list` adapter found no weighted block in the planner helper file (`no_weighted_surfaces`), so its eligibility/host-collection logic cannot be scored independently by this adapter. MCP source hash `6aed5bf35bcea2f7a1571b149a0905ccd5466dba8cc4ac1a7f2648afd463ce95`. | MCP source revision `9e2a7f1e34449c4d10e468361e6857608cd1326a18dedc5009406240af50da3a`; [inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78c999d831615acbb5a766105d5a88af2f7bf954ef6bf0d0d82e30aaaceed578/40b1c94687520e5269bd995ff5f0ca4f6fdaa185d220e15bca94fcffab7e8cc1/probability-inspect-6aed5bf35bce.json) |

The inspected source diff adds `independence_wave_preselect_automatic_hosts = yes` after the plan contribution begins and before the first allocation draw in `006_independence_wave_effects.txt:3660-3687`. The planner adds a preselection collection/reservation pass and changes compact/extended optional-state expansion to reject hosts outside the preselected set in `006_independence_wave_package_planner_effects.txt:135-263,532-589,715-724,949-964`. No weight constants were changed in the reviewed diff. These are source facts only; the eligibility effect on normalized selection remains unresolved.

The per-file MCP source revisions differ because the workspace index advanced while the three current paths were inspected. The source hashes and raw Git object hashes above identify the inputs actually inspected; they do not establish that the three MCP artifacts share one atomic index revision.

### Scenario and compare result

The request refers to six named count-band and Event 005 collision scenarios from the baseline handoff, but that handoff defines no such six scenario IDs or fixtures. It names only `E006_PRESELECTION_BASELINE_INPUT_GAP_DIAGNOSTIC` with scenario `E006_OUTER_REGION_TOTALS_UNBOUND`, state `{}`, flags `[]`, and scopes `{}`; the handoff explicitly says this diagnostic is not a campaign scenario and must not be reused as one. No six-scenario compare was run, and no scenario IDs were invented.

One compare probe used only that already-declared diagnostic scenario, the complete fourteen-entry outer region-weight candidate pool, and `before`/`after` objects with the same mod-relative source path plus `inlineClausewitz` excerpts taken from the immutable baseline commit and current worktree respectively. This is not the requested six-scenario comparison and is not campaign probability evidence.

The exact `hoi4.probability_compare` response was `status=error`, `code=PROBABILITY_SURFACE_EMPTY`, message `No weighted blocks matched this request`, `artifactCount=0`, no blockers beyond that code, no diagnostics, and no comparison ID or artifacts. The only submitted scenario ID was `E006_OUTER_REGION_TOTALS_UNBOUND`, under set ID `E006_PRESELECTION_BASELINE_INPUT_GAP_DIAGNOSTIC`; the baseline evaluate's prior scenario hash was `5af364fa5681ad4d2adc414a504740ddf94db7c12e96ff662a0bd1a35360bf1d`, and the compare response returned no scenario hash. Because the analyzer matched no weighted block, the call does not confirm that its baseline source shape was accepted for comparison.

The requested six-scenario compare is blocked before valid execution for two recorded reasons. First, the baseline handoff contains no six scenario IDs or typed state fixtures to reuse. Second, the installed subagent workflow requires nonempty `before.path` and `after.path`; the only workspace path resolves to the current after-source, while the historical baseline is available as a Git revision and inline source, not as a separate MCP path. The attempted path-plus-inline diagnostic compare returned `PROBABILITY_SURFACE_EMPTY` rather than a usable comparison. A flat primitive scenario map cannot represent the required Clausewitz candidate arrays, host ownership/control/capital, protected-state collisions, or Event 005 reservation footprint.

No compare artifact, normalized odds, ranking delta, rank reversal, starvation, repetition rate, collision probability, or numeric balance conclusion is available. No `probability_evaluate`, `probability_sweep`, or render was run for the absent six-case scenario set. Keep those results unresolved until the parent supplies the missing named scenario set and an analyzer-supported baseline source path/fixture contract.
