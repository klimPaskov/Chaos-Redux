# Event 012 Strength Chaos normalization audit

Disposition: the accepted source correction is present in the parent’s AFTER snapshot and its bounded source arithmetic is reviewed; MCP probability classification and source before/after comparison remain unresolved because every narrow probability inspection stayed pending without a tool result.

Audit date: 2026-10-08.

Scope: the single deterministic helper `gods_of_africa_refresh_strength` in `common/scripted_effects/012_africa_gods_effects.txt`. The accepted correction is the parent decision supplied in this task: divide the global Chaos meter by `constant:chaos_meter_tier_range.tier_final.min`, multiply by `constant:gods_of_africa_strength.component_max`, retain the Evolution II/III bonuses, the 10% component share, the existing clamp, other weights, smoothing, and punishment gates, and remove the obsolete `chaos_divisor`.

## Sources and immutable snapshots

- BEFORE manifest: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/012_africa_plans/subagent_handoffs/012_gods_strength_chaos_2026-10-08_evidence/before/manifest.json`. All four declared snapshot hashes were independently checked against their bytes.
- AFTER manifest: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/012_africa_plans/subagent_handoffs/012_gods_strength_chaos_2026-10-08_evidence/after/manifest.json`. All four snapshot hashes and all four current logical source hashes match.
- `common/scripted_effects/012_africa_gods_effects.txt`: BEFORE `a8345ffd8135137f90e0e87da15067f16607a43578fe4e9f69d3a3abb7511092`; AFTER `4d456c03921a25281857364e136f784c066602ebbde6b126bd3f04a166c28105`. The old helper reads the meter, divides by `chaos_divisor = 1`, adds the evolution bonuses, and clamps at lines 714–719. The AFTER helper uses the final-tier minimum and component maximum at lines 714–721, then preserves the weighted addition and divisor at lines 722–739.
- `common/script_constants/012_africa_gods_constants.txt`: BEFORE `be9f4d3cd489b86d6dca14b213d8d02fd48b42020228dd209f0f8098a14d563e`; AFTER `6bd87f107439f05533583f204de323b1170a75baefe9e8dfa18bec79e9167876`. The AFTER constants retain Evolution II `15`, Evolution III `25`, component range `0..100`, Chaos share `10`, and weighted divisor `100` at lines 348–355; the obsolete `chaos_divisor` entry is absent.
- `common/script_constants/chaos_meter_constants.txt`: BEFORE and AFTER `3afc88033de79f3abb0d173c82aaef6130fbf0846cd012a575ca00b73bde1b4a`. Tiers are `0..199`, `200..399`, `400..599`, `600..799`, `800..999`, and final tier minimum `1000` with no maximum at lines 19–26.
- `common/scripted_triggers/012_africa_gods_triggers.txt`: BEFORE and AFTER `9db29e9384743ee26e476b69fb46e83ebe076e3475023917866de6f6dba2e2b2`.
- The auditor’s `strength_helper_before.txt` and `strength_helper_after.txt` are exact byte slices of only the named helper from the corresponding full-file snapshots. Their SHA-256 hashes are `b928b86a1758fc66c11130270606cd5216883a536ee7443c93ba9f6c4f66f402` and `396dfa52f7176deb4feb72707e9370dc2aa2eb8e382bdb2e9711bfcf0a953282`. These are thin projections only; they do not claim helper-closure or whole-workspace coverage. The original full-file manifests remain linked above.

## MCP probability evidence

Automatic adapter discovery was requested with the exact candidate annotation `candidatePool: ["gods_of_africa_refresh_strength"]`; no adapter was forced and no custom-pool manifest was supplied. The annotation is complete for the single named helper, but it does not describe a selection pool, so probability candidate-pool completeness and normalization are not applicable at this helper boundary.

- `hoi4.probability_inspect` call 1 used `source: { path: "common/scripted_effects/012_africa_gods_effects.txt" }` and the exact helper candidate. It yielded no result after bounded polling and was stopped. No adapter, artifact URI, revision, or scenario hash was returned.
- `hoi4.probability_inspect` call 2 retried the immutable BEFORE projection using the logical source path, `snapshotPath: "docs/plans/012_africa_plans/subagent_handoffs/012_gods_strength_chaos_probability_2026-10-08_evidence/strength_helper_before.txt"`, `expectedSourceHash: "b928b86a1758fc66c11130270606cd5216883a536ee7443c93ba9f6c4f66f402"`, and the same exact candidate. It yielded no result after one bounded poll and was stopped.
- `hoi4.probability_inspect` call 3 used the corresponding AFTER projection and `expectedSourceHash: "396dfa52f7176deb4feb72707e9370dc2aa2eb8e382bdb2e9711bfcf0a953282"` with the same candidate. It also yielded no result after one bounded poll and was stopped.
- These are pending/no-result outcomes, not proof that the service is unhealthy or that an adapter explicitly returned unsupported. The connected probability route exposes `scenarioSet` as an opaque required value for `hoi4.probability_compare`; no inspection response supplied a recognized adapter or a schema-backed scenario set.
- `hoi4.probability_compare` was not submitted because a valid identical scenario set and recognized adapter were unavailable. Guessing the scenario envelope or casting this helper as a stochastic selection would violate the scenario contract. No comparison ID, MCP scenario hash, probability artifact URI, or rendered probability evidence exists.
- `hoi4.probability_evaluate` and `hoi4.probability_sweep` were not run because the inspected surface has no returned probability adapter or candidate race. `hoi4.probability_simulate` and `hoi4.probability_sequence` were not run because there are no declared uncertain inputs or a custom stochastic pool. `hoi4.probability_render` was not run because no retained probability analysis ID or renderable MCP result exists.
- The exact requests and pending outcomes are recorded in `012_gods_strength_chaos_probability_2026-10-08_evidence/mcp_probability_trace.md`. MCP analysis artifacts and rendered evidence paths: none returned.

## Source arithmetic and parent model

The BEFORE component formula is `clamp(chaos / 1 + 15*EII + 25*EIII, 0, 100)`. The AFTER formula is `clamp((chaos / 1000) * 100 + 15*EII + 25*EIII, 0, 100)`. The direct Chaos contribution to the weighted target is `component * 10 / 100`; it is at most `10` points.

The parent-supplied `source_model_after.json` at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/012_africa_plans/subagent_handoffs/012_gods_strength_chaos_2026-10-08_evidence/source_model_after.json` has SHA-256 `f5d1062cfabce1d017231437d76d2851bd76eec34e7f057e9ab121ebd9d31752`. It labels itself `bounded_source_model`, sets `engineEvaluation` to `false`, records 22 passing source groups with zero failures, and includes the relevant `012_GODS_STRENGTH_CHAOS_component_curve` group with 56 rows, maximum contribution `10`, and endpoint `1000`. This is the parent’s production-node arithmetic evidence; I did not reproduce its model or interpret it as engine execution.

The 56 source-model cases use meter values `0, 100, 199, 200, 399, 400, 599, 600, 799, 800, 999, 1000, 1001, 1200` across four flag contexts: no evolution flags, Evolution II only, Evolution III only, and both flags. Their local audit identifiers are the complete cross-product `SM012-C<meter>-<none|EII|EIII|EII+III>`; these labels are not MCP scenario IDs or hashes.

No date, seed, cadence, terminal state, or scheduled transition applies to these deterministic source-model cases; only the meter value and the two evolution flags vary.

| Chaos | BEFORE component/share in all four contexts | AFTER none | AFTER EII | AFTER EIII only | AFTER EII+III |
|---:|---:|---:|---:|---:|---:|
| 100 | 100 / 10 | 10 / 1 | 25 / 2.5 | 35 / 3.5 | 50 / 5 |
| 200 | 100 / 10 | 20 / 2 | 35 / 3.5 | 45 / 4.5 | 60 / 6 |
| 400 | 100 / 10 | 40 / 4 | 55 / 5.5 | 65 / 6.5 | 80 / 8 |
| 600 | 100 / 10 | 60 / 6 | 75 / 7.5 | 85 / 8.5 | 100 / 10 |
| 800 | 100 / 10 | 80 / 8 | 95 / 9.5 | 100 / 10 | 100 / 10 |
| 1000 | 100 / 10 | 100 / 10 | 100 / 10 | 100 / 10 | 100 / 10 |
| 1001 | 100 / 10 | 100 / 10 | 100 / 10 | 100 / 10 | 100 / 10 |
| 1200 | 100 / 10 | 100 / 10 | 100 / 10 | 100 / 10 | 100 / 10 |

At Chaos `0`, the model retains the nominal Evolution II and III additions exactly: components/shares are `15/1.5`, `25/2.5`, and `40/4` for EII, EIII-only, and both flags. Bonuses are added before the component clamp, so their effective marginal value decreases when the component reaches `100`.

The AFTER curve is monotone and linear before its cap, with score slope `0.01` per Chaos point. The component first caps at Chaos `1000` with no evolution bonus, `850` with EII only, `750` with EIII only, and `600` with both bonuses. Values `1001` and `1200` are valid final-tier normalization stress inputs because the shared final tier has no maximum; this does not prove the live campaign meter can reach `1200`.

## Score, probability, gates, and risk

This helper calculates one deterministic component of a weighted score. It does not conduct a score race, generate an `ai_will_do` willingness value, sample a probability-proportional pool, or define an MTTH/timing distribution. A 10% component share is not a 10% click or selection probability.

The other component weights remain `25/20/20/15/10` alongside Chaos `10`, and the target still divides by `100` (`012_africa_gods_constants.txt`, lines 71–76 and 355). The helper then applies its existing capital-loss and surrender penalties, clamps its target, and either writes an immediate target or moves stored Strength toward it by the configured smoothing step (`012_africa_gods_effects.txt`, lines 739–796). Consequently, the table is exact for the isolated component/share only; the full Strength value also depends on five other components, penalties, stored Strength, and smoothing state.

The catastrophe gate remains in `gods_of_africa_extreme_gate_is_open` (`012_africa_gods_triggers.txt`, lines 724–749): Chaos at least `800`, host Strength at least `80`, and participant Wrath at least `90` are still required, along with Evolution III, current host/generation, the Last Sentence flag, non-capitulation, no recent extreme punishment, at least three demand failures, and at least two offenses. The corresponding constants are unchanged at `012_africa_gods_constants.txt`, lines 101–108, and the trigger source hash is byte-identical before and after.

At the Chaos gate value `800`, the direct weighted component is `8` with no evolution, `9.5` with either single evolution flag, and `10` with both; the BEFORE value is `10` in each context. This can lower the pre-smoothing target by up to `2` points at that meter value, but does not change the gate predicates. No resulting change to full Strength, catastrophe availability, or decision willingness is claimed.

Dominance, starvation, rank reversal, repeated selection, and stochastic exploit risk are not defined at this scalar helper boundary. Downstream decision candidate rankings, AI willingness scores, and their rank reversals were deliberately not expanded into the nine-decision audit requested to remain out of scope. The component is recalculated from the global meter and remains capped at `100` and `10` weighted points; the surrounding helper’s smoothing and penalties remain separate influences.

## Documentation evidence

- Offline wiki Effects, `divide_variable` entry at line 712: `hoi4.reference_search` and `hoi4.reference_read`, section id `47711a12db514f388775ce71bc3d80274aeba998b1e56405e18f744e57c183f9`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`; source file SHA-256 matches that revision.
- Offline wiki AI modding, `ai_will_do` arithmetic example at lines 38–73: section id `710fd4775bf6f71143eb238bb639d7ecf829e664aa0b8213fa2a24de2b32846e`, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`. The example shows score composition; it does not establish a click probability.
- Installed `effects_documentation.md`, `divide_temp_variable` lines 3587–3594 (section id `7a26e33ee99b2605de12e0182bfd4f2e1a2341a62fbe58a1ce277b7fc4e1ec1f`), `clamp_temp_variable` lines 2681–2694 (id `6789583b685dbcc6c230eb70d204504a152416f9bfdf4ff7c35c923b8fd52b93`), and `multiply_temp_variable` lines 5012–5018 (id `9d96cdc695031689479a49ee97cf92cbffd4fba3991dadcc516299fecd1f07c4`); all share revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Installed `script_concept_documentation.md`, Script Constants lines 216–222: section id `c859ab9d6a857bfc830f89b36b004514b78ee454e001a80238e1f7b355ccd0`, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`; installed `common/script_constants/documentation.md`, constants schema lines 1–34: section id `48deec564822a81f6806514736148c344258acac56db7e9989998ed30dd26b68`, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.

The HOI4 reference routes were exposed and targeted offline wiki/game-document sections were read. No web wiki was used.

## Recommendations and remaining limits

No additional gameplay fix is recommended within this accepted correction: the normalization uses the shared endpoint, preserves both evolution additions and the 10% weight, reaches the component maximum at Chaos `1000`, and keeps the existing catastrophe gates. The parent model’s source arithmetic supports these points, but the MCP probability conclusion remains unresolved.

Do not describe these component values as click probabilities or as a full Strength simulation. An MCP source comparison requires a recognized adapter and its accepted scenario contract or a supported deterministic-score route. Native numeric consumption remains separate engine evidence. Until then, the probability delta, downstream decision ranking changes, and runtime reachability of the `1200` input remain unresolved.

Skipped structural event inspection/render: this bounded surface is one scripted helper, not an event-chain graph audit. No MTTH, AI decision candidate pool, random selection, strategy factor, uncertain input, custom pool cadence, or timing sequence was analyzed.

Skill used: `chaos-redux-subagents`. No gameplay, AI, event, or other source file was edited by the auditor; no game was launched and no Git action was taken.
