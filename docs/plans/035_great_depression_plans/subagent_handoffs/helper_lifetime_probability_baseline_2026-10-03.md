# Event 35 Helper Output Lifetime Probability Baseline

Status: baseline source review complete, required native probability analysis unresolved because the connected inspect calls timed out or returned an internal error.

This is a read-only baseline handoff for the Event 35 temporary-output lifetime patch. The parent owns the four call-site initializations and the later same-scenario comparison.

## Scope and ownership

The two weighted surfaces are `great_depression_score_independent_target` and `great_depression_score_center_candidate` in the preserved Event 35 effects snapshot.

The other two tracked outputs, `great_depression_center_registration_failed` and `great_depression_deepening_value`, are control-flow and gameplay outputs rather than probability weights.

No gameplay, AI, event, focus, decision, mission, technology, doctrine, GUI, localisation, constants, or existing scenario fixture file was changed by this audit. No files were staged or committed.

The only new files are this handoff and the report-only [helper lifetime baseline fixture](../audit_inputs/helper_lifetime_2026_10_03/helper_lifetime_baseline_fixture.json). The fixture is not an MCP `scenarioSet` schema and was not submitted as one.

## Source identities

The immutable before-source is `docs/plans/035_great_depression_plans/audit_inputs/helper_lifetime_2026_10_03/035_great_depression_effects_before.txt`, copied from `common/scripted_effects/035_great_depression_effects.txt`.

Its verified SHA-256 is `3B065E7FC529FA4E8A98B7CAF60656ECC2FD22970944B966329986B85D1B1403`.

The actual interim effects hash captured by the parent before the two weighted caller additions was `6DA8BF85559ACD08FD6E36ACDBE886C88DB006D90031C876531FCB684BA8987C`. My earlier report incorrectly copied the trigger-hash suffix into this historical effects hash. The value is corrected using the parent's explicit capture, not a rehash of the current file. It is a historical interim identity and was not used as the immutable baseline.

The effects source after the lifetime patch and before the later reclosure patch had SHA-256 `B9E01DE3EB2CC97FA31E73188745AF77A1EEF28F07D86AC51AC0346385AA28A9`, independently rechecked with `Get-FileHash` and `certutil`. Its bytes are now also preserved as `audit_inputs/reclosure_2026_10_03/035_great_depression_effects_before.txt`. This identifies that captured state rather than any later working-file state.

The supporting source `common/script_constants/035_great_depression_constants.txt` had SHA-256 `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7`.

The supporting source `common/scripted_triggers/035_great_depression_triggers.txt` has SHA-256 `FE2DC15DC22EA0D8F9336C7120412B1DA66CF7F7348D43E7EE1D7A72BC1566CA`, rechecked with both `Get-FileHash` and `certutil`.

The v2 candidate fixture `docs/plans/035_great_depression_plans/audit_inputs/center_owner_2026_10_03/scenarios_v2.json` has SHA-256 `F348094B23CD57F16C067DB32C5C7F4BD2E6CE780145E3C6B4808346743C63C3`.

The v3 candidate fixture `docs/plans/035_great_depression_plans/audit_inputs/center_owner_2026_10_03/scenarios_v3.json` has SHA-256 `2C92489F1C2764C729096B2FF88505A3E8F653D204E6F92F76B1627B4134BF66`.

The report-only lifetime fixture has SHA-256 `8B921CD7205797D1314E3BF778328AEBA1911E6DE9E13498366E1286524E1E84`.

## Source and documentation evidence

The preserved effects snapshot defines the candidate score at lines 1322-1350, the independent target score at lines 1355-1489, the weighted target selector at lines 1495-1522, initial center registration at lines 1525-1748, new-crisis initialization at line 3178 and the registration-failure consumer around lines 3337-3345, and the deepening amount helper and consumer at lines 3396-3474.

The source helper-output calls are `great_depression_select_independent_target` to `great_depression_score_independent_target`, `great_depression_register_initial_centers` to `great_depression_score_center_candidate`, `great_depression_initialize_new_crisis` to `great_depression_register_initial_centers`, and `great_depression_deepen_active_crisis` to `great_depression_resolve_deepening_amount`.

The relevant gate definitions are `great_depression_new_center_state_is_permitted` at line 60 and `great_depression_is_valid_independent_target` at line 123 of `common/scripted_triggers/035_great_depression_triggers.txt`.

The independent target weights are in `great_depression_independent_target_weight` at lines 1111-1138 of the constants file. The center score coefficients are in `great_depression_scaling` at lines 1179-1209.

I read `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Variable types, lines 435-442. Line 440 says temporary variables created in scripted effects or triggers may fail to remain visible to the caller, while a temporary variable initialized before the helper call carries through and is modified.

I read `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `set_temp_variable`, lines 7820-7826. The installed documentation defines the effect and its supported scope, but does not independently establish the scripted-helper return-lifetime behavior stated in the wiki.

The local wiki file SHA-256 is `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`. The installed effects-documentation file SHA-256 is `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.

The connected `hoi4.reference_context` request for the Event 35 helper-output rule ended with `timed out awaiting tools/call after 600s`. I read the pertinent offline files directly and retained their exact paths, sections, line spans, and hashes above.

The parent reports a separate targeted `hoi4.reference_search` request for `set_temp_variable` in `game_doc`, with `limit = 1`, is still pending on cell 22. I did not poll, duplicate, or restart that parent handle. It remains pending and has not supplied citation output to this handoff.

The required repo skills read in full were `chaos-redux-subagents`, `chaos-redux-events`, and `chaos-redux-event-planning`. The event-planning skill applies because the source matrix names the required scenario families and states full-pool and rank expectations.

## Baseline source findings

### Independent target weight

`great_depression_score_independent_target` creates `great_depression_independent_target_weight` inside the callee. `great_depression_select_independent_target` calls it for each valid country, then immediately reads that output as the `for_loop_effect.end` value used to append entries to `great_depression_independent_target_pool`.

The conservative call-frame model discards that callee-created temporary scalar on return because the selector does not preinitialize caller-owned storage at this call boundary. The exact engine result of reading the absent scalar is unresolved. I do not claim that it becomes zero, that the pool is empty, or that any specific country receives a selection probability.

The source formula starts from the constant `base = 10`, adds `major = 8` for a major and `player = 12` for a human-controlled country, and uses usable civilian and military factory factors of `1` and `0.5` with caps of `18` and `12`.

Other named source modifiers are high trade dependence `+8`, low stability `+10`, recent industrial expansion `+8`, severe supply disruption `+10`, war exhaustion `+8`, rough Event 34 landing `+10`, previous episode `-8`, recent episode `-24`, recent major industrial state loss `+2` per factory up to `16`, strong reform `-12`, and hollow recovery `+12`.

The helper rounds and clamps the resulting weight to the configured range from `1` to `64`. These are source constants, not analyzer-computed candidate weights.

The selector's source-level mechanism expands a candidate weight into repeated array entries and then chooses with `random_scope_in_array`. This is a weighted ticket-pool mechanism, not an `ai_will_do` willingness score and not a decision click probability. An exact conditional selection probability requires a complete valid-country pool, all candidate weight inputs, and a successful MCP analysis.

The validity trigger requires a viable economy and either major status or human control. It excludes active Event 35, active or frozen Event 34, pending transition, incompatible economic state, active refire safeguard, and stale active-registry entries. The complete TGT candidate set and external factors are not supplied for this baseline.

### Depression Center score

`great_depression_score_center_candidate` creates `great_depression_center_candidate_score` in the callee. `great_depression_register_initial_centers` calls it for each eligible state and then compares that output with caller-owned `great_depression_center_best_score`. The baseline call does not preinitialize the output in the caller frame.

The conservative call-frame model discards the candidate score at helper return, so the caller's comparison input is unavailable under this model. The source defines a deterministic highest-score candidate race with a state-ID tie break. It does not define a probability-proportional selection or an AI willingness score.

The score coefficients read from the constants file are `4` for industrial capacity, `2` for infrastructure, `1` for population, `-16` for a capital, and `-10` for adjacency to an existing Great Depression Center. The source reads civilian factories, military factories, dockyards, infrastructure, population, capital status, and center adjacency.

The selector's candidate gates also require the candidate to be owned, controlled, and core to the receiving country, passable, above the minimum population, industrialized, not already registered, and permitted by `great_depression_new_center_state_is_permitted`.

The result class for this selector is score-only if the analyzer returns a numeric trace. No baseline score, ranking, tie resolution, or rank reversal was returned by MCP, so the measured baseline remains unresolved.

### Other two output boundaries

`great_depression_register_initial_centers` initializes `great_depression_center_registration_failed` inside the callee, then `great_depression_initialize_new_crisis` reads it after return to choose abort versus continue. The caller has no preinitialized temporary output in the preserved baseline.

`great_depression_resolve_deepening_amount` initializes and modifies `great_depression_deepening_value` inside the callee, then `great_depression_deepen_active_crisis` consumes it for persistent severity and trend updates. The caller has no preinitialized temporary output in the preserved baseline.

These are control-flow and gameplay-output lifetime findings, not probability results. Their exact engine effect after return is unresolved by this audit.

## Scenario inputs and completeness

The independent target scenario family is `TGT-01` through `TGT-10`, named in `docs/specs/035_great_depression_specs/035_great_depression_ai_probability_matrix.md`, lines 38-40, and specified in `docs/specs/035_great_depression_specs/035_great_depression_spec_part_9_ai_probability_balance.md`, lines 343-352.

| Scenario | Required candidate pool | External-factor completeness | Scenario purpose |
| --- | --- | --- | --- |
| `TGT-01` | Full valid-country pool required, not supplied | Incomplete | Several stable majors and one player non-major |
| `TGT-02` | Full pool required, not supplied | Incomplete | One country has active Event 35 and must be ineligible |
| `TGT-03` | Full pool required, not supplied | Incomplete | One country has active Event 34 and must be ineligible |
| `TGT-04` | Full pool and safeguard state required, not supplied | Incomplete | A recently recovered country should rank below comparable untouched candidates |
| `TGT-05` | Full pool and exact industrial-loss history required, not supplied | Incomplete | Recent major industrial loss should increase relative vulnerability |
| `TGT-06` | Full pool and prior episode/reform history required, not supplied | Incomplete | Strong reform lowers weight while hollow recovery raises it after its safeguard |
| `TGT-07` | Complete singleton pool required, not supplied | Incomplete | One valid country remains |
| `TGT-08` | Complete empty pool required, not supplied | Incomplete | No valid country remains and no call should be queued |
| `TGT-09` | Full multiplayer player and major pool required, not supplied | Incomplete | Several player countries with no hidden local-player dominance |
| `TGT-10` | Complete cluster actor and member pool required, not supplied | Incomplete | Negative Economy cluster anchor retains its actor without rerolling |

The TGT matrix requires a full valid-country pool but does not provide candidate identities or a complete scenario fixture. Candidate-pool completeness and external-factor completeness are therefore unresolved for every TGT scenario. I do not state an exact probability or a dominance, starvation, or rank result for any TGT scenario.

The earlier `docs/plans/035_great_depression_plans/035_great_depression_completion_report_2026-08-31.md`, lines 216-220, records historical TGT inspect artifact `probability-inspect-564f67ae2e4d.json`, comparison analysis `probability-04588e59754999011203a599`, and scenario hash `6197357e6d72b69b2f494b2b83fa34d49b1dea3f86b24b293c96e6ec872f86e2`. It reports ten scenarios, 150 rows, and zero unresolved inputs, while explicitly classifying those results as historical evidence. I did not reuse them as this baseline because the scenario payload and matching source revision were not supplied, and the new inspect attempts returned no current analysis artifact.

The center v2 fixture contains seven named scenarios with complete candidate pools under its `bindingContract`. Its pool counts are two for `CTR35-ROOT-ACTOR`, `CTR35-ROOT-DIFFERENT`, `CTR35-FOREIGN-ROOT-NEIGHBOR`, `CTR35-NO-CENTER-NEIGHBOR`, `CTR35-CAPITAL`, and `CTR35-NEGATIVE-TIE`, and one for `CTR35-TINY-CAPITAL`.

The center v3 fixture preserves those seven cases and adds `CTR35-FORBIDDEN-PRIMARY+validother`, `CTR35-RESERVED-OTHER-EPISODE+validother`, `CTR35-ALL-RESERVED-OR-FORBIDDEN`, and `CTR35-FROZEN-FORBIDDEN-CLEARED-LIVE`. Each added fixture declares two candidate states.

| Scenario | v2 pool | v3 pool | External-factor completeness in the fixture |
| --- | ---: | ---: | --- |
| `CTR35-ROOT-ACTOR` | 2 | 2 | Complete within each fixture contract; MCP field mapping unresolved |
| `CTR35-ROOT-DIFFERENT` | 2 | 2 | Complete within each fixture contract; MCP field mapping unresolved |
| `CTR35-FOREIGN-ROOT-NEIGHBOR` | 2 | 2 | Complete within each fixture contract; MCP field mapping unresolved |
| `CTR35-NO-CENTER-NEIGHBOR` | 2 | 2 | Complete within each fixture contract; MCP field mapping unresolved |
| `CTR35-CAPITAL` | 2 | 2 | Complete within each fixture contract; MCP field mapping unresolved |
| `CTR35-TINY-CAPITAL` | 1 | 1 | Complete within each fixture contract; MCP field mapping unresolved |
| `CTR35-NEGATIVE-TIE` | 2 | 2 | Complete within each fixture contract; MCP field mapping unresolved |
| `CTR35-FORBIDDEN-PRIMARY+validother` | Not present | 2 | Complete in v3, including state-permission inputs; MCP field mapping unresolved |
| `CTR35-RESERVED-OTHER-EPISODE+validother` | Not present | 2 | Complete in v3, including center and episode registry inputs; MCP field mapping unresolved |
| `CTR35-ALL-RESERVED-OR-FORBIDDEN` | Not present | 2 | Complete in v3, including state-permission and episode inputs; MCP field mapping unresolved |
| `CTR35-FROZEN-FORBIDDEN-CLEARED-LIVE` | Not present | 2 | Complete in v3, including frozen Event 34 and live-permission inputs; MCP field mapping unresolved |

The v2 contract declares owner, controller, core membership, passability, population, industrial getters, capital status, center flag, registry membership, adjacency, and the complete actor center registry for its original cases. The v3 contract explicitly adds live Event 34 conversion-prohibition state and center episode metadata across its scenario records, along with the complete actor registry.

Candidate-pool and external-factor completeness are complete within each corresponding fixture contract. Whether those fields can be expressed in the connected MCP scenario schema is unresolved because the inspect route returned no accepted schema or artifact. No native ranking or score trace is claimed.

The earlier `scenarios.json` in the same folder was not used. It has no populated candidate-pool rows, while v2 and v3 provide the explicit complete fixtures requested for this audit.

## MCP evidence and blockers

The connected workspace ID was `mod_chaos_redux_ea3b2d67c2c0`. `list_mcp_resource_templates({server: "hoi4_agent_tools"})` returned the artifact template `hoi4-agent://workspace/{workspaceId}/artifact/{sha256}/{provenanceHash}/{name}` with byte-range selectors. No probability artifact was returned, so there is no artifact URI to retrieve.

The live exposed `hoi4.probability_inspect` schema accepts `source`, optional `adapter`, optional `candidatePool`, `refresh`, and `workspaceId`. The evaluate and sweep schemas expose `scenarioSet` as an untyped field, so their accepted nested scenario fields were not established by tool metadata alone.

The required first inspect used the frozen before-source path with no adapter selector. It ended with the exact tool error `timed out awaiting tools/call after 600s`.

The narrower independent-target inspect used the same frozen path with adapter `custom_weighted_pool` and no candidate-pool claim. It ended with the same exact 600-second timeout.

The fixture-bounded center inspect used the frozen path and the complete candidate IDs `1` and `2`. It returned `code = INTERNAL_ERROR`, `status = error`, `artifactCount = 0`, and blocker message `Unexpected internal error` for workspace `mod_chaos_redux_ea3b2d67c2c0`.

No inspect call produced an analysis ID, source revision, analyzer source hash, scenario hash, candidate trace, or artifact URI. No renderable analysis exists.

`hoi4.probability_evaluate` and `hoi4.probability_sweep` were not called because inspect did not return an accepted adapter, scenario schema, or analyzer source result. No exact or bounded MCP trace, threshold sweep, sensitivity result, rank reversal, ranking, normalized probability, or timing result is available.

`hoi4.probability_render` was not called because there is no analysis ID. `hoi4.probability_simulate` was not needed because no uncertain-input distributions were declared. `hoi4.probability_sequence` was not applicable because this is not a complete cadence-and-transition custom pool. `hoi4.probability_compare` was not run in this before-only handoff and is reserved for the parent-owned post-patch audit using the same named scenarios and immutable before-source.

The broader `hoi4.event_inspect` and `hoi4.event_render` chain analysis was outside this bounded helper-output baseline. No event-chain or unrelated Event 35 audit expansion was performed.

## Results and risk classification

The independent target surface is `unresolved` for candidate weights after helper return, ranking, exact selection probability, target dominance, starvation, rank reversal, and repetition risk. The source-only finding is that the weight output is created in the callee and read after return by ticket construction.

The center candidate surface is `score-only` by source design and `unresolved` for measured score values and ordering because the required MCP inspect failed. It has no click probability or normalized selection probability.

The registration-failure and deepening outputs are `unresolved` for native return behavior. Source confirms that callers rely on temporary outputs first created inside callees.

AI candidate validity is source-reviewed through the named trigger gates. MCP did not prove runtime availability, complete candidate coverage, or that impossible candidates are excluded in a live campaign.

Dominance, starvation, rank reversal, repeated-selection frequency, exploit risk, and timing drift are not determined by this baseline. There is no MCP evidence to support those balance conclusions.

For identical complete inputs, the parent-requested caller-preinitialization patch should leave the helper formulas, constants, gates, candidate identities, and center state-ID tie break unchanged. The intended score outputs before and after should therefore be equal when the helper output is retained. This is the intended comparison target, not a measured before/after result.

## Recommended owner changes at baseline

In `common/scripted_effects/035_great_depression_effects.txt`, initialize `great_depression_independent_target_weight` in the caller-owned country frame immediately before `great_depression_score_independent_target` is called inside `great_depression_select_independent_target`.

Initialize `great_depression_center_candidate_score` in the caller-owned state frame immediately before `great_depression_score_center_candidate` is called inside `great_depression_register_initial_centers`.

Initialize `great_depression_center_registration_failed` in `great_depression_initialize_new_crisis` immediately before `great_depression_register_initial_centers` is called.

Initialize `great_depression_deepening_value` in `great_depression_deepen_active_crisis` immediately before `great_depression_resolve_deepening_amount` is called.

The parent owns these four source edits. The changes should only establish caller-owned output storage and preserve the current helper formulas, constants, eligibility, candidate IDs, selection logic, and tie-breaks.

## Owner status after the preserved baseline

The frozen before-source remains the baseline for the two weighted outputs. The current working file now preinitializes `great_depression_independent_target_weight` to `constant:great_depression_api.zero` at line 1499 before `great_depression_score_independent_target`, then reads the output at line 1503.

The current working file preinitializes `great_depression_center_candidate_score` to `constant:great_depression_scaling.invalid_center_candidate_score` at line 1687 before `great_depression_score_center_candidate`, then reads the output in the best-score comparison at line 1694.

The parent reports, and the current file confirms, that the third output is caller-preinitialized fail-closed to `constant:great_depression_api.one` at line 3340 before `great_depression_register_initial_centers`. The fourth output is caller-preinitialized to `constant:great_depression_api.zero` at line 3439 before `great_depression_resolve_deepening_amount`. These current edits do not change the preserved baseline snapshot.

The parent also reports a separate cross-owner output-lifetime audit in `common/scripted_effects/035_great_depression_external_adapters.txt`. A read-only check of the current file confirms caller-owned zero initialization for `famine_pressure_request_result` before `famine_request_event_pressure`, `migration_pressure_request_result` before `migration_request_event_pressure`, and `famine_occupation_context_proven` before `famine_resolve_occupation_profile`. The observed current lines are 48-51, 75-78, and 85-88. The current file hash is `5B6862AA9BF510DC08524634E626F459FD7DFCB6984B2C200D2ED2AD71FB7EA7`.

The parent states that these external-adapter changes are in the 035 external file only and make no owner-code changes. I verified the current initialization statements but did not create or inspect an immutable before-source for that external file, so its before/after lifetime audit remains parent-owned.

All four direct Event 35 call-site outputs are now caller-preinitialized in the current source. No source edits were made by this auditor.

## Post-patch handoff requirements

The post-patch probability comparison for the current after-source is documented in `docs/plans/035_great_depression_plans/subagent_handoffs/helper_lifetime_probability_compare_2026-10-03.md`. It uses the exact immutable before-source above and the actual after-source path when the connected MCP route accepts the existing scenario inputs.

The center comparison should preserve the complete CTR35 v2/v3 candidate fixtures and classify returned results as score/rank evidence, never as click probabilities. The independent-target comparison needs a complete TGT candidate pool before any exact normalized selection probability can be claimed.

If the connected inspect route remains unavailable, preserve the exact error and leave MCP balance conclusions unresolved. Do not compare the current source to itself or use source review as analyzer evidence.
