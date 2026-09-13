# Event 016 Mengele conventional incident recovery probability baseline

Date: 2026-09-08

Status: bounded read-only baseline complete for the five new private incident recovery rows. The current source has no weighted AI blocks, so no new-row score, rank, eligibility, or selection-probability claim is made. The existing Computation random-list is recorded separately as an explicit precedent, not as a same-ID baseline. No gameplay, decision, effect, AI, configuration, or runtime files were edited by this auditor, and no commit was created.

## Scope and ownership

The new weighted surface is the five-row recovery decision set in `common/decisions/016_mengele_conventional_incident_decisions.txt`: `mengele_event016_electronics_incident_recovery`, `mengele_event016_materials_incident_recovery`, `mengele_event016_rocketry_incident_recovery`, `mengele_event016_high_energy_incident_recovery`, and `mengele_event016_biomedical_incident_recovery`. The rows begin at lines 10, 52, 94, 136, and 178 and contain no `ai_will_do` blocks at this baseline freeze.

The paired deterministic effect surface is `common/scripted_effects/016_mengele_conventional_incident_effects.txt`. Its family/stage dispatcher is at lines 504-526 and cleanup dispatcher at lines 528-533. The family helpers record an incident only when the provider and stage are valid and the family has no active incident or recovery; recovery begin/cancel/finish helpers snapshot and validate the exact private receipt. No random list is present in this conventional incident effect file.

The exact fixture is [016_mengele_conventional_incident_probability_baseline_2026-09-08.json](../testing/016_mengele_conventional_incident_probability_baseline_2026-09-08.json). It preserves the five-ID added-candidate boundary, the named eleven-scenario identity, the absent-weight MCP result, and the separate two-entry Computation precedent.

## Required references read

I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-event-planning/SKILL.md`. I also consulted the offline Paradox wiki pages `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding`.

The relevant vanilla documentation consulted was `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md`, `effects_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `dynamic_variables_documentation.md`.

The source constants reviewed in `common/script_constants/016_brilliant_scientist_project_constants.txt` are the existing response profiles: technical, industrial, biological, and exotic recovery days, factory use, support equipment, trucks, fuel, manpower, and political power at lines 19-50. The existing Computation incident pressure path also uses the project capacity constants at lines 15-18. These are source inputs for the owner’s later AI patch, not auditor-selected balance targets.

## Mandatory incident inspect and absent-weight baseline

The first weighted MCP call for this tranche was `hoi4.probability_inspect` with adapter `decision_ai_will_do`, the complete five-ID candidate pool, and source `common/decisions/016_mengele_conventional_incident_decisions.txt`. MCP returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, `candidates=0`, `availableCandidates=0`, `availableAdapters=[]`, `requiredInputs=0`, and `unresolved=0`.

The inspect source revision is `2248a1c614c512dcbdd5fba89e69ae644a9efb2a354d9e5a0fff583eae77801a` and source hash is `6e7353f352d4d80421940eb5a8809ed22f2f2238e4494a6e89fd0e72c6bd7843`. The authoritative inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3df0df538c9902970bcb775c784a37ddb613902ed98f4f6ab57ab18afc3fdd3/4d1039f447572bcaf8e870f6c7c5a7d71c67c8f885a9212ba659ae6808353338/probability-inspect-6e7353f352d4.json`.

The named scenario evaluation used `E016_MENGELE_CONVENTIONAL_INCIDENTS_2026_09_08` with eleven scenario identities: `E016_MENGELE_CONVENTIONAL_INCIDENTS_VALID_OWNER_STAGE_1`, `_STAGE_2`, `_STAGE_3`, `_STAGE_4`, `_INVALID_OWNER`, `_OWN_ACTIVE`, `_RECOVERY_ACTIVE`, `_OTHER_FAMILY_ACTIVE`, `_EXACT_COST`, `_SHORTAGE`, and `_DUPLICATE_CALLBACK`. The fixture declares private owner/provider validity, stage, own and other-family active state, exact-cost and shortage alternatives, and duplicate-callback state as inputs. The five IDs were explicitly exposed in the request as a declared candidate boundary, but this does not make them live-eligible.

The evaluate call returned `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request`, the requested adapter `decision_ai_will_do`, the exact source path, the five requested IDs, and `availableAdapters=[]`. It emitted no analysis id and no probability artifact. Therefore the incident rows have no MCP score, rank, eligibility, conditional probability, dominance, starvation, or repetition result at this baseline. The named state fields remain declared test inputs only; the empty surface prevented the adapter from evaluating them.

## Separate Computation random-list precedent

The explicit precedent source is `common/scripted_effects/016_mengele_computation_incident_effects.txt`, random-list lines 193-198. Its two entries are `common/scripted_effects/016_mengele_computation_incident_effects.txt:193.entry.1`, weighted by `var:mengele_event016_computation_incident_pressure`, and `common/scripted_effects/016_mengele_computation_incident_effects.txt:193.entry.2`, weighted by `var:mengele_event016_computation_incident_complement`. The second entry is the real weighted no-op complement in the source; this is not a same-ID baseline for the new recovery decisions.

The precedent `probability_inspect` used adapter `random_list` and returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, `candidates=2`, `availableCandidates=0`, `requiredInputs=2`, and `unresolved=0`. Its source revision is `513511a40ea4cfec30d293ccc72c9de1650389209d9c642cf61eb87b10b0e3d4`, source hash is `5180295e91d11c35f89c3fe4ae6b537079d63b1329c07d9f6f85dc36278e24af`, and artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42be77e39358b85a054da1e88a43bf1563b1555f61f98b9b6415e7916688fd8b/736af158769e4e63125b6b48016d96556b4814fb2c7dadbfbb25cbb55909df99/probability-inspect-5180295e91d1.json`.

The adapter declares `selectionRule=proportional_categorical`, `normalizedProbability=true`, `rawScore=true`, `eligibility=true`, `completePoolRequired=true`, `sequence=false`, and `timeDistribution=false`. The following bounded evaluation supplied the two pressure variables explicitly and is exact only conditional on reaching this enclosing random list:

| Pressure | Complement | Incident entry raw/probability | No-op entry raw/probability |
| ---: | ---: | ---: | ---: |
| 5 | 95 | 5 / 0.05 (1/20) | 95 / 0.95 (19/20) |
| 10 | 90 | 10 / 0.10 (1/10) | 90 / 0.90 (9/10) |
| 18.75 | 81.25 | 18.75 / 0.1875 (3/16) | 81.25 / 0.8125 (13/16) |
| 24 | 76 | 24 / 0.24 (6/25) | 76 / 0.76 (19/25) |

The precedent analysis id is `probability-7644e6f8e435a05bbae897f8`, scenario hash is `29438610dc7a99e81fed9df1dc6e0168d9a04063199e19971b4287a280655409`, source revision is `ee8c8b4a91677bce731fd77be1985536f0d9ece1b76b08e03aa2fccd04f3f549`, and source hash is `5180295e91d11c35f89c3fe4ae6b537079d63b1329c07d9f6f85dc36278e24af`. The authoritative JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47b2d9a87f95416120e3c5020d77221067e7f64807add03e430362721ec9f393/d5d6bce9639b549fe9d780420cff0ab7ad542be80ac192180debb384a50df8e3/probability-7644e6f8e435a05bbae897f8.json`.

Rendered precedent evidence is preserved at the following MCP URIs:

- Ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad605df8f95c7be20a83606512630a9d0b15509f7a348a60185dacc05e1cfcf2/f9832740c4f0ae6eb3eb471132e700f97d38ec771befc7f07758fc1baf990d5d/probability-probability-7644e6f8e435a05bbae897f8-ranking.svg`.
- Ranking PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9d99d7281cbf426ecabaad9e94a9f3f5d3462df52df70c1629bbc10bda7c1204/bde6070eff814e15447301f25c6fbc35fc965be11669d731463f766e148a822d/probability-probability-7644e6f8e435a05bbae897f8-ranking.png`.
- Matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73f40451e6ae7f6f2e59ea43a57334fe81b0dc2a4472f9695a2287faa92d1c0a/55b5c53ca26a83adf5e684a02ddf0f612343255e6d088dc9000b14cc8caecf57/probability-probability-7644e6f8e435a05bbae897f8-matrix.svg`.
- Matrix PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59dee1719017d279651cf2d6994f6cce428b573790dbb9be0fb04455cc7046a4/1592eccc9c2080ed7bf4329f7d6777dc7cea5765002ea570c165c4bb961aa235/probability-probability-7644e6f8e435a05bbae897f8-matrix.png`.
- Unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/36a519f0a2bf13367a8ef04b9a944f014e39bcd4fedb37ab69ea5ed6c057c74c/probability-probability-7644e6f8e435a05bbae897f8-unresolved.svg`.
- Unresolved PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741e9e9423642ce8eb7607dbaccbbceeec8fa1c4ab1c760262892070e72be88c/75040da8fb039773dd78eab7d13efcf6cfa97e15c3ee7c5dab40b218aa0180ac/probability-probability-7644e6f8e435a05bbae897f8-unresolved.png`.

The precedent evaluation returned eight candidate rows across four pressure scenarios and two dominance diagnostics for maximum probabilities of 0.95 and 0.90. Those warnings describe conditional dominance inside the two-entry random list only. They do not establish overall incident incidence, recovery selection, timing, or campaign repetition.

## Candidate pool and external-factor completeness

- New conventional incident recovery pool: five IDs are the complete declared source boundary, but the MCP weighted pool is absent (`candidates=0`). No normalization or score race can be evaluated.
- Computation precedent pool: complete two-entry pool, with both pressure and complement variables explicitly supplied. The enclosing trigger, family/stage dispatch, provider validity, active-family flags, and recovery decision gates were not part of this random-list evaluation.
- External state for the new incident scenarios: owner/provider validity, stage 1-4, own-active, recovery-active, other-family-active, exact-cost, shortage, and duplicate-callback were declared in the fixture. Because MCP stopped at the absent weighted surface, none is certified as a runtime eligibility result.
- The owner’s planned AI uses the existing Computation recovery weight profile and exact shared response cost profiles. The planned dispatch pressure table is the existing 5/10/18.75/24 precedent and has no Exposure input. These are accepted owner inputs for the post-AI pass, not auditor-selected weights.

## Recommendations without applying them

1. After the owner attaches AI, run `hoi4.probability_inspect` first on the current five-row source and preserve the new source revision/hash. Evaluate the same `E016_MENGELE_CONVENTIONAL_INCIDENTS_2026_09_08` scenario identities and the exact five-ID candidate boundary.
2. Keep score output separate from proportional probability output. The new decision adapter may expose willingness scores, but no click probability is valid unless MCP reports a complete normalized candidate pool and a supported selection rule.
3. Reuse the existing response profile semantics and the planned 5/10/18.75/24 pressure inputs only as declared owner design. The auditor does not choose a balance target or invent a recovery weight.
4. After the owner’s AI patch, run `hoi4.probability_compare` with a true frozen pre-AI source and the exact same candidate pool and scenario identities. An addition report is not a same-ID before/after comparison and must be labelled separately.

## Skipped analyses and exact blockers

- New incident score evaluation: blocked by MCP `PROBABILITY_SURFACE_EMPTY`; no weighted block matched the current source and no artifact or analysis id was produced.
- Probability sweep: not run because there is no current weighted surface, threshold, or sensitivity to sweep.
- Simulation: not run because no uncertain input distributions or approved seed were declared.
- Sequence: not run because no complete custom pool cadence, cooldown, recovery, cap, removal, reset, timer, or terminal-state manifest exists.
- Same-ID comparison: not run because the owner has not yet attached AI; a current-vs-current or unrelated Computation comparison would violate the baseline contract.
- Structural event inspect/render: not applicable to these decision/effect rows and no event chain was in scope.
- Live HOI4 launch/gameplay validation: not performed; it belongs to the user.

## Handoff conclusion

The new five-row source is ready for the owner’s bounded AI attachment, but the truthful pre-AI result is an absent weighted surface, not a zero score or zero probability. The exact five-ID candidate boundary and eleven scenario identities are frozen in the fixture. The existing Computation random-list is fully evaluated as a separate, complete two-entry precedent: pressure 5/10/18.75/24 yields incident conditional probabilities 0.05/0.10/0.1875/0.24 against the weighted no-op complement. No balance target, AI weight, or gameplay patch was chosen by this auditor.

## Post-attachment decision evidence

The owner attached exactly five `ai_will_do = { base = constant:brilliant_scientist_project_board.ai_urgent }` rows at lines 23, 72, 121, 170, and 219 of `common/decisions/016_mengele_conventional_incident_decisions.txt`. The constant resolves to 25. No modifier or decision eligibility source was changed in this attachment.

The mandatory post-attachment decision inspect was rerun first. The requested `decision_ai_will_do` route returned `PROBABILITY_SOURCE_DISCOVERED` with zero requested candidates but five available matches and suggested `mission_ai_will_do`. The mission inspect returned `PROBABILITY_SOURCE_INSPECTED`, a complete five-candidate pool, two required inputs, zero unresolved diagnostics, source revision `002615ad2a4999540e2bd0ae7dfd99cfde23b43d798f019685b75a54d8b3b928`, and MCP source hash `bb745036a4cdcfdc8cd399d73bb37722e9cdb63e3e1004a8b8c1c5e66a01fe81`.

Inspect artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/995507145ee2a6fc148ebafa3c137aae840dc3921856e83a90447caa0f9c19e5/1957fd50bf3e945acaaec510099c1351d9e35da34abd90d2d72b04a2548c446d/probability-inspect-bb745036a4cd.json` for requested-route discovery and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67a14dae7f05d5267a0e6fc4efbe477f336fe3d5bd1f1e9602d012472cc3d84e/e296a21c799fda80643a95674e1f2cad896b583e8f36840811b8496a31418cb4/probability-inspect-bb745036a4cd.json` for the mission pool.

The exact frozen `E016_MENGELE_CONVENTIONAL_INCIDENTS_2026_09_08` eleven-scenario identity and five-ID pool evaluated successfully through `mission_ai_will_do`: analysis `probability-17c3237b326aa13c97f61098`, scenario hash `92d2d339330d8866a8e6740135c57d5f9bd02457785e519282d8cb7bcd2d3d49`, 55 candidate rows, zero unresolved rows, and zero diagnostics. Every row returned raw score 25, support `score_only`, and `conditionalProbability=null`. The adapter returned a deterministic tie order of Biomedical, Electronics, High Energy, Materials, then Rocketry in every scenario. This is exact score evidence under the explicit candidate overrides, not a live eligibility or normalized selection probability.

The authoritative decision JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f04bb6b2ae3fe6fdaca0d0a14195d958ffa79e40149d4ea985fb5b10003db6f0/5ddf2b696ffbd30849fdf715034659defd61ad4c1892655517049c35b96820d6/probability-17c3237b326aa13c97f61098.json`. Ranking, matrix, and unresolved SVG/PNG artifacts are preserved in the fixture.

An absent-to-added `probability_compare` was attempted with an inline pre-AI decision snapshot reconstructed from the frozen source by removing only the five owner-attached AI lines, the current source path as `after`, the same five IDs, and the same eleven scenario identities. The current raw file hash supplied to the after selector was `2ca8448ad530c334b4143eed719a2d048eb1afe28d9107e289bebe30ad36b881`. MCP returned `PROBABILITY_SURFACE_EMPTY` (`No weighted blocks matched this request`) with no comparison id or artifact because the before surface was intentionally unweighted. This is recorded as an absent-to-added limitation; no current-v-current or unrelated Computation comparison was substituted.

## Post-attachment conventional incident dispatch evidence

The owner added `brilliant_scientist_mengele_dispatch_conventional_incident` at `common/scripted_effects/016_mengele_conventional_incident_effects.txt:567-579`. Its random list is the complete two-entry pool at lines 572-576: `...:572.entry.1` uses `var:mengele_event016_computation_incident_pressure` to record the requested conventional incident, and `...:572.entry.2` uses the complement as a weighted no-op. The enclosing trigger is `brilliant_scientist_mengele_can_dispatch_conventional_incident`, which requires a valid private provider and stage plus the requested family’s own incident and recovery flags being clear.

The mandatory random-list inspect returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, two candidates, two required inputs, zero unresolved diagnostics, source revision `eab392797b640f3a299880ed8c04b5a4195f063043fddf21136f18bca90802a7`, and source hash `d0e0a8ff149293ba14e5e12c00c5e01310c87ae1dccb2dd9213fa76d5660783c`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbbf301039a14d2b56b862abf7420407c6490d0cba042e607211556eedf10b41/1b283aef03a9e5e67b0bf83ea5fc2191ad0fbb09c42a9e7be4c1d52f3cc877e1/probability-inspect-d0e0a8ff1492.json`.

The same eleven named incident scenarios supplied explicit pressure/complement pairs 5/95, 10/90, 18.75/81.25, and 24/76. The random-list evaluation returned analysis `probability-5c555812531bb49af182b133`, scenario hash `609017ae27c6df511c9bd2b2a67441e008c039dc2c534533cdb691f1a181ceca`, source revision `eab392797b640f3a299880ed8c04b5a4195f063043fddf21136f18bca90802a7`, source hash `d0e0a8ff149293ba14e5e12c00c5e01310c87ae1dccb2dd9213fa76d5660783c`, 22 candidate rows, complete pool, and zero unresolved rows. The adapter reports proportional categorical normalization and exact conditional probability only after the enclosing dispatch is reached.

Valid owner stage 1-4 returned incident conditional probabilities 0.05, 0.10, 0.1875, and 0.24 respectively, with complement probabilities 0.95, 0.90, 0.8125, and 0.76. Invalid owner, own-active, and recovery-active cases had both entries explicitly ineligible, pool total 0, raw values 0, and null probabilities. Other-family-active remained eligible as intended by the family-specific trigger and returned 0.10/0.90 at pressure 10. Exact-cost, shortage, and duplicate-callback fixtures also returned 0.10/0.90 because those fields are not part of the dispatch trigger; those rows do not certify payment or callback runtime behavior. Six `PROBABILITY_DOMINANT_OUTCOME` warnings identify the 0.95 or 0.90 no-op dominance in the valid/allowed cases.

The authoritative dispatch JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e72e29e7996e469427e24cb7f8cf8b3d438e688bf2d89859569826f2fccc000/11ab01c37de51aa51f3bfc4dc2cf241e448e0811702d1368f5b25446b4324c56/probability-5c555812531bb49af182b133.json`. Ranking, matrix, and unresolved SVG/PNG artifacts are preserved in the fixture.

An absent-to-added random-list `probability_compare` was attempted with an inline effect snapshot reconstructed from the frozen no-dispatch source by removing only the new conventional dispatch block, the same two-entry pool, and the same eleven scenarios. The current raw effect hash supplied to the after selector was `b26e66f7aa38faf7e34f72007b6a9b86dbd59ed992ce810639978e26eb8e97c9`. MCP returned `PROBABILITY_SURFACE_EMPTY` with no comparison id or artifact because the before source intentionally had no random-list surface. This is the exact addition boundary; no Computation source was used as a substitute.

## Causal callsite boundary

Only the Materials `self_propagating_batch_risky` callsite at `common/special_projects/projects/016_brilliant_scientist_projects.txt:202-220` and Biomedical `unlicensed_trial_risky` callsite at lines 283-301 invoke the new conventional dispatcher, and only under `brilliant_scientist_mengele_project_stage_provider_is_valid`. Their current-host else branches retain the prior public risky accident path. No native option weight, broad portfolio, or unrelated Kruger branch was included in this tranche.

## Updated completion and blockers

The five-row AI score surface is now MCP-discovered and evaluated, but remains score-only with all five rows tied at raw 25 under explicit candidate overrides. The new conventional random dispatch is a complete two-entry normalized surface with exact conditional pressure results and explicit false-eligibility probes. Both mandatory absent-to-added comparisons were attempted and blocked by `PROBABILITY_SURFACE_EMPTY` on the intentionally unweighted before snapshots; this is not a failed current-v-current comparison and no balance closure is claimed.

No sweep, simulation, sequence, timing, cooldown, repetition, terminal-state, live-game, gameplay-edit, or commit work was performed. The parent owns any balance decision and source patch; this auditor only preserved the MCP evidence and limitations.
