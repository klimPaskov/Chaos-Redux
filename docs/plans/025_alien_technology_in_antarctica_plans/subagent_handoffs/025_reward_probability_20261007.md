# Event025/Event016/Event036 reward probability baseline, 2026-10-07

Disposition: incomplete for probability and structural conclusions. This is a read-only current-source audit with exact MCP inspection artifacts where calls returned. Probability evaluation, sweep, event graph, technology graph, and rendering evidence remain unresolved because the required live calls timed out or were still pending at handoff authoring. Source review is recorded as bounded evidence and does not replace those routes.

## Scope and authority

Audited reward surfaces are the Event016 neutral custom technology owner API, the Event025 winner-reward ledger and winner-settlement overlap input, and the Event036 legacy jet reward and overlap-conversion seam.

Accepted design inputs are specs 006 Outcomes, Rewards, and Aftermath and 014 Acceptance Criteria in docs/specs/025_alien_technology_in_antarctica_specs/specs/. The current human instruction is the authority for exact collision semantics: aircraft/propulsion field labels do not establish an exact shared payload ID. The 2026-10-04 D8 entry records a prior implementation decision, but its broad-field overlap classification is contradicted by the current human correction and by the audited payload IDs.

The parent retains Event025 seizure and restitution work locally. This audit did not inspect or propose changes to those branches.

No gameplay, AI, technology, localisation, workbook, Git index, or runtime file was edited. The only writes are this handoff and byte-exact current-source snapshots under evidence_20261007_reward/source_snapshot/. HOI4 was not launched. No tests were added or run.

## Current conclusion

The Event016 owner API has the required base, upgrade, Integration tier order when its request permits base selection. Event025 currently requests base selection. The Event036 overlap-conversion request sets allow_base to zero, which skips all still-missing base families before trying an upgrade and Integration.

The current source does not prove an exact Event025/Event036 payload collision. Event036 grants jet_fighter1, jet_fighter2, and 200 jet_fighter_equipment_2. The Event016 pool has no matching jet technology or equipment ID. In particular, alien_infantry and alien_predictive_warfare map to the broad propulsion field, but their consumers are land infantry equipment and land tactics. Portal, Temporal, and other candidate families also do not share the Event036 jet IDs.

The ledger labels a match between the broad aircraft and propulsion fields as exact. That field comparison can reject a valid Event016 base, suppress the Event036 jet reward, and relabel an unrelated upgrade or Integration outcome as a conversion. The exact positive collision scenario therefore has no current candidate. A genuine aviation owner extension remains a parent decision, not an accepted design or an applied fix.

No exact normalized selection probability is claimed. The completed probability inspection found the 18 random_list entries across two separate pools, but poolComplete was false and all 18 dynamic weight inputs were required. The named evaluation and sweep calls timed out. Equal source weights remain score-only evidence.

## Audited weighted surfaces

| Surface | Source location and role | Pool |
| --- | --- | --- |
| Event016 base selection | common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt, chaosx_grant_random_custom_operational_technology, random_list at line 553 | Seven independently gated base-family entries, candidate IDs ending 553.entry.1 through 553.entry.7 |
| Event016 external reward upgrades | The same file, chaosx_grant_external_alien_recovery_reward, random_list at line 782 | Eleven independently gated upgrade/control entries, candidate IDs ending 782.entry.1 through 782.entry.11 |
| Event036 event options | events/036_alien_spacecraft.txt, country event chaosx.nr36.2 | Three options each declare ai_chance base 100. Their triggers are intended to select the legacy jet delivery, converted reward, or pending fallback. The MCP inspect for this option pool timed out, so no normalized option result is claimed. |

There is no random selection inside the reward helper for an Event025 winner other than the two owner API random lists. No MTTH entry or MTTH-backed AI score participates in these reward calls. Event firing timing, focus choice, decision AI, and unrelated Event025 AI surfaces were not included in this bounded reward baseline.

## Exact candidate IDs and source-declared validity

The candidate IDs returned by the API source inventory identify two separate random lists. The seven base weights are initialized to zero and set to constant:chaosx_custom_technology_tuning.random_candidate_weight, currently 1, when chaosx_custom_operational_technology_is_unowned passes. The eleven upgrade weights are initialized to zero and set to the same constant when chaosx_custom_technology_upgrade_is_eligible passes. The trigger requires the selected operational base, an unowned upgrade, and a compatible xenobiological control channel where applicable.

| Base candidate ID | Selector | Existing Event016 technology | Current payload or consumer | Current public field | Event036 exact jet-ID match |
| --- | --- | --- | --- | --- | --- |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:553.entry.1 | portal | brilliant_scientist_portal_warfare_tech | teleportation_equipment_1 and portal_raider land formation | spatial | none |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:553.entry.2 | clone | brilliant_scientist_clone_formations_tech | existing clone equipment and land formation package | biological | none |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:553.entry.3 | robot | brilliant_scientist_robot_formations_tech | autonomous robot equipment and land formation package | computation | none |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:553.entry.4 | paleogenetic | brilliant_scientist_paleogenetic_formations_tech | existing paleogenetic land package | biological | none |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:553.entry.5 | xenobiological | brilliant_scientist_xenobiological_formations_tech | existing xenobiological land package | biological | none |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:553.entry.6 | alien_infantry | brilliant_scientist_alien_infantry_tech | alien_laser_weapon_equipment_1; alien_infantry is type infantry, category army, landing-only and untrainable | propulsion | none |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:553.entry.7 | temporal | brilliant_scientist_temporal_guard_tech | temporal_guard_equipment_1 and temporal_guard land formation | temporal | none |

| Upgrade candidate ID | Selector | Existing technology | Current consumer or effect | Candidate gate |
| --- | --- | --- | --- | --- |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.1 | portal_weaponization | brilliant_scientist_portal_warfare_weaponization_tech | strengthens portal_raider | Portal base present and upgrade unowned |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.2 | clone_weaponization | brilliant_scientist_clone_formations_weaponization_tech | selects existing clone refinement | Clone base present and upgrade unowned |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.3 | robot_weaponization | brilliant_scientist_robot_formations_weaponization_tech | strengthens autonomous_robot | Robot base present and upgrade unowned |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.4 | paleogenetic_weaponization | brilliant_scientist_paleogenetic_formations_weaponization_tech | strengthens paleogenetic formation | Paleogenetic base present and upgrade unowned |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.5 | xenobiological_weaponization | brilliant_scientist_xenobiological_formations_weaponization_tech | strengthens xenobiological formation | Xenobiological base present and upgrade unowned |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.6 | alien_predictive_warfare_weaponization | brilliant_scientist_alien_predictive_warfare_tech | enables two land-combat tactics and depends on alien_infantry tech | Alien Infantry base present and upgrade unowned |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.7 | temporal_weaponization | brilliant_scientist_temporal_guard_weaponization_tech | strengthens temporal_guard | Temporal base present and upgrade unowned |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.8 | xeno_chemical_control | brilliant_scientist_xeno_chemical_control_tech | occupies chemical control channel | Xenobiological base present, this control unowned, alternate controls clear |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.9 | xeno_neural_control | brilliant_scientist_xeno_neural_control_tech | occupies neural control channel | Xenobiological base present, this control unowned, alternate controls clear |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.10 | xeno_machine_control | brilliant_scientist_xeno_machine_control_tech | occupies machine control channel | Xenobiological base present, this control unowned, alternate controls clear |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:782.entry.11 | xeno_researched_control | brilliant_scientist_xeno_researched_control_tech | occupies researched-control channel | Xenobiological base present, this control unowned, alternate controls clear |

The owner selectors and raw weights are source evidence, not normalized probabilities. The inspected list IDs are grouped by their random_list parent. The 18 entries are never treated as one 18-way pool.

## Tier order, modifiers, and delivered-source receipts

The owner API first applies its per-source duplicate guard. It then calls the base random helper when allow_base is absent or positive. A successful base result records tier 1 and a public field. If no base is applied, the API prepares the eleven-candidate compatible-upgrade pool. A successful upgrade records tier 2. If no upgrade is applied, it applies brilliant_scientist_alien_systems_integration at tier 3, or adds the existing integration_reinforcement_stability constant, currently 0.02, when the idea is already present.

Each eligible member in either active pool receives the same raw weight, constant:chaosx_custom_technology_tuning.random_candidate_weight = 1. There are no candidate-specific weight modifiers, strategy factors, date factors, or MTTH modifiers in these two random_list blocks. Equal raw weights do not establish equal normalized shares unless the active pool and every weight input are complete.

The public source values are source_antarctic_race = 25 and source_alien_spacecraft = 36. Operational receipts encode selector × provenance_stride + source in chaosx_custom_technology_operational_provenance. Upgrade receipts use the separate chaosx_custom_technology_upgrade_provenance array and encode both the prerequisite family receipt and selected upgrade receipt. The current stride is 1,000,000. Event025 and Event036 each have a source-specific consumed flag, so one successful owner-API reward per source is permitted for the same country while same-source repeats are blocked.

Integration has no family or upgrade selector receipt. Its evidence is the source-specific consumed marker and ledger result/tier. Event036's legacy jet option bypasses the owner API entirely. The resolver can record Event036 and expose a legacy_reward_allowed flag before option A actually grants the jets. Option A later sets brilliant_scientist_alien_spacecraft_recovered after granting jet_fighter1, jet_fighter2, and 200 jet_fighter_equipment_2. The family flag is therefore not itself a delivered-payload receipt.

### Temporary caller-output lifetime

The owner API's external result outputs are caller-initialized by the Event025 ledger preparer. The random base output chaosx_custom_technology_random_grant_applied is also initialized before the nested base helper call.

The upgrade branch calls chaosx_grant_custom_technology_upgrade and then reads chaosx_custom_technology_upgrade_applied inside each random_list option. The external owner API initializes chaosx_external_alien_recovery_upgrade_applied but does not initialize the nested helper output chaosx_custom_technology_upgrade_applied before the call. The nested grant initializes and sets that temporary itself. Under the project's conservative temporary-output lifetime rule, the caller-owned output storage is missing. This is a bounded source-contract defect. Whether the live engine preserves the new nested temporary in this exact call chain is unresolved without the required runtime/analyzer evidence.

If the output is cleaned on return, a valid upgrade could be granted while the outer owner fails to observe its marker and enters the Integration branch. That can misreport the result and may apply both an upgrade and Integration for one source. The owner should initialize the consumed temporary output in its caller frame before each nested upgrade grant, or use an output with a documented durable lifetime. No code was changed.

## Exact overlap and caller mismatch

Event036 option A grants jet_fighter1, jet_fighter2, and 200 jet_fighter_equipment_2. The current Event016 candidate IDs do not include those technology or equipment IDs. Portal grants teleportation equipment and a land raider consumer. Temporal grants a temporal_guard land consumer. Alien Infantry grants alien_laser_weapon_equipment_1 and an infantry land consumer. Predictive Warfare depends on that land base and enables land tactics. A special_project_specialization label or a public field name is not a shared payload identity.

The current owner field mapper returns spatial for Portal, computation for Robot, propulsion for Alien Infantry and Predictive Warfare, temporal for Temporal, biological for the biological families and controls, and integrated for the capstone. It does not return aircraft for any of the seven base families or eleven upgrades.

The Event025 overlap trigger accepts Event025 field aircraft or propulsion. The Event036 resolver treats either of those Event025 labels as belonging to the same flight/propulsion/weapons overlap group when Event036 itself has aircraft or propulsion. The Event025 winner-settlement caller also derives a positive overlap from Event036 aircraft-family flags or the legacy recovered flag. These are field-family comparisons, not exact technology, equipment, or payload ID comparisons.

The legacy Event036 resolver sets its aircraft-family marker and legacy-reward permission before the player or AI option grants the jets. Event025 winner settlement reads the family marker as sufficient overlap even when the actual legacy delivery receipt has not been set. Therefore a pending Event036 option can affect Event025 base filtering before Event036 delivered any jet package.

With Event025 first, a base Alien Infantry result or Alien Predictive Warfare upgrade is marked propulsion. The later Event036 jet reward then enters the conversion branch, requests allow_base = 0, and can select any currently eligible Event016 upgrade or Integration. It can suppress the jet package and label an unrelated land upgrade as an overlap conversion. This is the named land_alien_family_then_jet_aircraft_negative_control. It is a bounded source-level false positive, not an exact collision.

With Event036 first, the winner-settlement caller currently sets overlap from the aircraft-family marker and the owner excludes only the Alien Infantry base weight. No current API payload matches the jets, so that candidate exclusion is unsupported by exact identity. The remaining base candidates remain source-valid. If only Alien Infantry is missing, the broad false match empties the base pool and permits a premature upgrade or Integration fallback.

The current Event025 request explicitly allows a base. The Event036 overlap-conversion request explicitly sets allow_base = 0. That skips all missing bases, not only a proven duplicate family. This conflicts with the current user instruction to prefer a missing valid base, then a compatible upgrade, then Integration. No balance target or replacement weight is selected here.

## Named scenario results and completeness

All named scenarios below use the complete source-declared seven-base set and eleven-upgrade set as two separate candidate pools. For each row, source-defined weights and state assumptions are recorded. MCP candidate-pool and external-factor completeness remain unresolved unless a successful analyzer result is cited. The prior October 3 scenario contract is preserved as historical evidence, not silently rewritten.

| Scenario ID | Declared inputs and source trace | Candidate-pool and external-factor completeness | Classification and result |
| --- | --- | --- | --- |
| no_owned_bases | All seven bases missing, no base-qualified upgrade, no Event025 or Event036 receipt, no overlap and no Integration idea. Every eligible base has raw weight 1. | The seven source IDs and all required base weight paths are identified. MCP poolComplete and external-state closure were not returned. | Base tier precedes upgrades and Integration is source-exact conditional on invocation. Conditional selection probabilities are unresolved. |
| one_owned_base | Historical fixture keeps Portal owned, the other six bases missing, Portal weaponization eligible and the other ten upgrades owned. | Six base entries and one upgrade entry are source-declared. MCP completeness and the ownership/control fixture are unconfirmed. | A valid base pool remains ahead of the upgrade pool. No normalized share or ranking is claimed. |
| all_bases_owned_upgrade_available | All seven bases owned, only Portal weaponization eligible, other ten upgrades owned, Integration absent. | Base weights are source-declared zero. Upgrade pool has one declared positive entry and ten zero entries. MCP poolComplete is unresolved. | Upgrade tier is selected before Integration under the declared state. Probability unresolved. |
| all_bases_and_upgrades_owned | All seven bases and eleven upgrades owned, Integration absent as in the historical fixture. | Both source pools have zero eligible weight by declared ownership. The Integration-idea state is explicit in the historical fixture, not an MCP-observed state. | The source has an Integration fallback when no upgrade is applied. Whether the all-zero random_list state reaches that fallback was not verified by the timed-out analyzer, so the result is bounded source flow and the actual outcome remains unresolved. If the idea already exists, the source branch adds its existing stability reinforcement. |
| repeated_event025_receipt | Event025 ledger receipt and Event025 source-consumed marker already exist. The resolver exposes the stored result and does not request the owner API again. | No selection pool is active. The source-specific receipt gates are source-reviewed; event graph MCP coverage timed out. | One-call-per-source is source-exact. Runtime repetition evidence is unresolved. |
| event036_first | Event036 legacy jet package is declared delivered before Event025 winner settlement. Current caller also treats the Event036 aircraft-family marker as overlap. | Current broad source filtering leaves six base candidates by setting the Alien Infantry weight to zero. Under exact payload identity no Event016 candidate matches the delivered jet IDs, so the exact-identity pool would retain all seven. MCP pool completeness is unresolved. | Current-source candidate suppression is bounded and unsupported by exact identity. No normalized share is claimed. |
| event025_first | Preserve the historical conditional Portal-first fixture. Current source maps Portal to spatial, so Event036's jet package is not an exact overlap and remains the legacy result. The old fixture's broad aircraft label is retained only in the October 3 document. | This is conditional on Portal already having been selected. The first-draw probability and whole event-order distribution are not established by this trace. | Bounded conditional source path. No unconditional Portal probability or sequence result is claimed. |
| land_alien_family_then_jet_aircraft_negative_control | Event025 conditionally delivered Alien Infantry or its Predictive Warfare upgrade, followed by Event036 jets. The land IDs and jet IDs differ. | This is a negative-control branch, not a full random draw. The conditional probability of the initial alien-family result is unresolved. | Current field grouping falsely classifies this as overlap. Exact shared payload is absent in the inspected current source set. |
| same_payload_true_collision_if_any | Compare the full current Event016 selector outputs with Event036 jet tech/equipment IDs. | The current pool has no exact matching ID, so there is no positive collision candidate or complete positive fixture. | Not applicable to the current code. Any new aviation owner family or refinement needs parent acceptance and a new scenario. |

Historical fixtures overlap_aircraft_other_bases_missing, overlap_propulsion_other_bases_missing, and overlap_both_other_bases_missing remain unchanged in 025_reward_probability_baseline_20261003_evidence/scenario_contract.md. Their field-based positive claims are not reused as proof of exact overlap. The historical event025_first fixture that labels Portal as aircraft is retained as a false-positive historical input because the current source maps Portal to spatial.

## Validity, dominance, starvation, repetition, and exploit risk

Candidate validity: source triggers reject owned base technologies and matching operational/grant receipts. Upgrade eligibility requires its base, the upgrade to be unowned, and mutually exclusive xenobiological controls to be compatible. This is bounded source evidence. The required probability and technology graph calls did not verify engine eligibility, external DLC behavior, or a complete runtime source closure.

Dominance: all eligible candidates in each list use raw weight 1. No source-authored candidate has a larger weight. This is score-only evidence. No normalized dominance claim is made because MCP did not report a complete pool.

Starvation: the Event036 broad overlap request can suppress the whole base tier with allow_base = 0. The Event025 overlap filter also zeroes the Alien Infantry base candidate without proving an exact match. If that is the only missing family, it is starved and fallback advances to upgrades or Integration.

Rank reversal and sensitivity: no analyzer result was returned. The uniform raw weight constant scales all eligible members together, so source alone supplies no candidate-specific rank difference. Sweep evidence is unresolved.

Repetition: Event025 records its result before the API request and subsequent resolver calls expose the stored record. API consumption is tracked independently for Event025 and Event036. The Event036 legacy jet option has no explicit ledger delivery-consumed marker after its direct stockpile grant, and legacy_reward_allowed is not visibly consumed in option A. Whether its scheduler guarantees a single display was not confirmed by event MCP, so duplicate Event036 legacy delivery remains an unresolved conditional risk.

Replacement tier semantics: the API stores result type, tier, field, overlap, and source. The provenance arrays can encode the selected selector and source, but the public ledger result does not directly return the selected selector. In an Event036 conversion, the caller can pass the earlier broad field into the owner API, causing an unrelated upgrade or Integration to inherit that field. A conversion flag can therefore reflect the broad overlap input rather than a proven shared payload.

Side-effect boundary: the owner API grants only the existing Event016 hidden technology packages and Integration idea/reinforcement through the neutral owner surface. The audited reward helper contains no direct country ownership transfer, state ownership change, character recruitment, Kruger history grant, division spawn, or stockpile grant. It calls the existing Event016 runtime reconciliation, which may restore the owning package's templates/provider consumers. Event036 option A separately grants its intended jet technologies and 200 jet equipment. These are source facts, not in-game runtime proof.

## Recommendations, not applied

1. Replace field-label overlap checks with a country-scoped exact delivered-payload receipt comparison. Compare stable owner selectors and canonical technology/equipment IDs. Keep presentation fields separate from collision identity.
2. In the current candidate set, treat Event036 jet delivery as non-overlapping. Keep all seven missing Event016 bases eligible after Event036 until a parent-approved owner extension adds a genuine matching aviation or propulsion payload.
3. Preserve the requested base-first, eligible-upgrade, Integration order. Event025 already sends allow_base = 1. Review the Event036 conversion request at chaosx_alien_recovery_ledger_resolve_event036 because allow_base = 0 skips every missing base, not only an exact duplicate.
4. Gate Event025 overlap on a delivered Event036 jet receipt. The resolver's aircraft-family marker and legacy-reward permission precede the actual option A grant and do not prove payload delivery.
5. Initialize chaosx_custom_technology_upgrade_applied in the caller frame before each nested upgrade helper call, or return a separately initialized caller-owned output. This follows the documented temporary-output lifetime contract and prevents an applied upgrade from being mistaken for an empty pool.
6. Persist or reconstruct the exact selected family/upgrade and actual delivery source in the ledger. Do not derive the replacement field from the prior broad field. Keep the Integration result distinct from an aircraft-specific upgrade.
7. If a true cross-event aviation collision remains a design requirement, review the proposed append-only aviation owner family and refinement in 025_exact_aircraft_overlap_contract_20261003.md. That package, its vanilla jet exception, and any refinement values remain unresolved until the parent accepts them. No weight or balance value is proposed by this audit.
8. Add or prove a one-shot delivery receipt for the direct Event036 legacy jet option before relying on its permission flag as a duplicate guard.

## Live MCP evidence and exact blockers

Workspace ID: mod_chaos_redux_ea3b2d67c2c0.

### Live tool schema snapshot

The live probability tool declarations were read from the connected tool inventory before the calls. The shared adapter enum is event_mean_time_to_happen, event_option_ai_chance, decision_ai_will_do, mission_ai_will_do, national_focus_ai_will_do, technology_ai_will_do, doctrine_ai_will_do, direct_random, random_list, ai_strategy_factor, and custom_weighted_pool.

| Tool | Accepted request fields observed in the live schema |
| --- | --- |
| hoi4.probability_inspect | adapter, candidatePool, customPoolManifest, refresh, source, workspaceId |
| hoi4.probability_evaluate | adapter, candidatePool, customPoolManifest, diagnosticThresholds, horizonDays, metrics, outputs, refresh, scenarioSet, source, workspaceId. scenarioSet is required. |
| hoi4.probability_sweep | adapter, candidatePool, diagnosticThresholds, horizonDays, metrics, outputs, refresh, scenarioSet, source, sweep, workspaceId. sweep requires paths and accepts steps, pairwise, findRankReversals. |
| hoi4.probability_compare | adapter, before, after, beforeManifest, afterManifest, candidatePool, diagnosticThresholds, horizonDays, outputs, refresh, scenarioSet, workspaceId |
| hoi4.probability_render | analysisId, expectedScenarioHash, filter, includeHtml, outputs, workspaceId. analysisId and outputs are required. |
| hoi4.probability_simulate | adapter, candidatePool, confidenceLevel, diagnosticThresholds, horizonDays, metrics, outputs, refresh, samples, samplingMethod, scenarioSet, seed, source, workspaceId |
| hoi4.probability_sequence | customPoolManifest, diagnosticThresholds, horizonDays, maxSteps, outputs, samples, confidenceLevel, scenarioSet, seed, workspaceId. customPoolManifest, horizonDays, and scenarioSet are required. |
| hoi4.event_inspect | mode, selector, direction, maxDepth, maxEdges, maxNodes, expandHelpers, refresh, workspaceId, plus mode-specific inputs. |
| hoi4.event_render | view, selector, direction, maxDepth, maxNodes, expandHelpers, includeHtml, refresh, workspaceId. |
| hoi4.tech_inspect | mode, technologyId, targetId, targetKind, direction, maxDepth, maxNodes, includeSubTechnologies, refresh, workspaceId, plus mode-specific inputs. |
| hoi4.tech_render | view, technologyId, targetId, categoryId, folderId, scenario, maxNodes, includeHtml, refresh, workspaceId. |
| hoi4.source_lookup | path, line, view, includeReferences, maxLines, workspaceId, and optional structure/keyPath inputs. The live validator capped maxLines at 80. |
| hoi4.script_validate | path or source/kind/scope inputs, documentation, limit, workspaceId. A file-path check infers command kinds and scopes. The live validator capped limit at 32. |
| hoi4.reference_context | surface, question, limit, workspaceId. The live validator capped question at 160 characters. |
| hoi4.reference_search | query, sources, limit, workspaceId. |
| hoi4.reference_read | id, revision, source, startLine, startColumn, maxLines, workspaceId. |

The probability source validator identified source as an object requiring one of identifier, path, inline Clausewitz source, or virtual patch. A path-only source object was accepted. The initial freeform source.query request and the no-source adapter request were rejected by validation and were corrected before classifying route health.

| Tool | Result |
| --- | --- |
| hoi4.probability_inspect, custom_weighted_pool, Event025 ledger source | Returned PROBABILITY_SOURCE_INSPECTED with zero candidates, zero unresolved inputs, source hash f6b6cdd946cb3fde1149439411ea1e17b29dae0a4782dc607985607f97fd2577, source revision 01f4c18e7220a274dafae6f485e15df0a0f5eb287e94d4d8ab4c553a35f105d3, artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e6652ffc78f899406fe93f27bc436355f03b24c7ea061177d23e00d0b847be1/82e4e55f0186582581bfa204cd603a87e2793ab4ef0d78fada2b8b2a8f4f5611/probability-inspect-f6b6cdd946cb.json. Event025 itself has no detected random_list candidate in that source. |
| hoi4.probability_inspect, source discovery for Event016 API | Returned PROBABILITY_SOURCE_DISCOVERED, suggested random_list, 18 available entries across the two owner lists, source hash c81eab16ac54d7f29ad0a164070228b6daaa422a7e59ce93189bbc2a7a63ea45, source revision 68d717d5d35720bf7c99e360bd5824f8adf101231edcde14eb80354515af5e08, artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08276cd89ab460af260a610a6714169fed3c8a4360427be0088edff6c86cfe69/2b1a3687eb3a14b88acb7476f5c2ef45444d41baf31e1b95cd0c8a2d646a1bb6/probability-inspect-c81eab16ac54.json. |
| hoi4.probability_inspect, random_list on Event016 API | Returned PROBABILITY_SOURCE_INSPECTED with candidates 18, poolComplete false, 18 required weight input paths, one unresolved item, same MCP source hash, source revision 8644f56a540efb3572da3412185501689240be664a82a09f4536f543ad601885, artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4fcb9e3c84ebc8aab6a0f06afede78f72d747f5de1dfdcfeb1c7ab52bdb23b1/1bcd8fc09cc8075ada77689f370c8f4dd0030289faf8f11ec041ac4057613807/probability-inspect-c81eab16ac54.json. The 18 required inputs are the seven chaosx_custom_technology_random_weight_* variables and eleven chaosx_external_alien_recovery_upgrade_weight_* variables listed by this artifact. |
| hoi4.probability_inspect, Event036 option source discovery and exact chaosx.nr36.2 event_option_ai_chance retry | Both calls timed out awaiting tools/call after 600 seconds. No Event036 option pool completeness, source revision, or artifact resulted. |
| hoi4.probability_inspect, separate seven-base and eleven-upgrade pools | Both focused calls timed out after 600 seconds. A cached no-refresh seven-base retry also timed out after 600 seconds. The combined inventory remains non-normalizable. |
| hoi4.probability_evaluate, no_owned_bases | The seven-candidate base pool evaluation timed out after 600 seconds. A narrower retry using the named base helper and JSON-only output also timed out after 600 seconds. No scenario hash, analysis ID, ranking, or normalized share resulted. |
| hoi4.probability_sweep | The five-step uniform candidate-weight sensitivity call timed out after 600 seconds. A narrower three-step JSON-only retry against the named base helper returned no result during the final short observation and was left unresolved. No threshold or rank-reversal result is claimed. |
| hoi4.probability_compare | Not run. This is a baseline with no owner-applied source patch or accepted candidate implementation. The October 3 baseline contains no analyzer result to compare, and its broad-field fixtures remain historical inputs. |
| hoi4.probability_render | Not run because no probability evaluation or comparison returned an analysisId. There is no renderable ranking, matrix, sensitivity, comparison, or unresolved artifact. |
| hoi4.probability_simulate | Not run because no uncertain input distribution or seed was declared. |
| hoi4.probability_sequence | Not run because no complete custom-pool manifest with cadence, state transitions, recovery, caps, cooldowns, removals, resets, timers, and terminal states was supplied. Event-order scenarios remain bounded conditional traces, not a sequence model. |
| hoi4.event_inspect and hoi4.event_render | Broad and narrowed Event025/Event036 calls timed out after 600 seconds. No event graph revision, render URI, or structural coverage result was returned. |
| hoi4.tech_inspect and hoi4.tech_render | Four targeted technology traces and a single-technology retry, followed by three technology renders and a single-technology retry, timed out after 600 seconds. No technology graph revision or rendered URI was returned. |
| hoi4.source_lookup | Successful source-location results identify the Event016 owner API at lines 674–827, MCP revision c7642a0568a871b0ea1d13e4b49ff221787ec210a1844c007af0c78a794f9345; Event025 winner caller at lines 3829–3882 and Event036 resolver at lines 386–541, revision 1a44f0a4fe6809f81cda0fd58888a6d525de9412b3767d3850f8136e932262c2; Event036 event chaosx.nr36.2 at lines 38–86, revision 8a069c1e5049b5f1356f651580963c6afa9dba88b3a039db153d06d61194b243; alien_infantry technology at lines 186–193, revision b12d4b5a514b7cf7e5f02bad09ecad041ed0b3a4363b1100d1fb29d6c2465f4f; Event025 broad overlap trigger at lines 76–92 and Event016 upgrade eligibility trigger at lines 246–333, revision ef923c3f757bd7f21c81c8e415912e9d07eb8df9c98a95a07cd876164b4ed91c. These are source-location receipts, not engine execution. |
| hoi4.script_validate | The first four-file request was rejected because limit exceeded 32. The path-only retry at limit 32 timed out for the Event016 API effects file. The API triggers, Event025 ledger effects, and Event025 ledger triggers returned SCRIPT_CHECK_PARTIAL with valid = null, validation.passed = false, parametersChecked = false, no findings, and unchecked argument blocks (49, 239, and 230 respectively). The documented game-source revision was 9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b. These partial checks do not establish script validity or parameter semantics. |
| Standalone Technology Tree Viewer | No matching viewer tool or executable was exposed in the checked live tool inventory, repository, or installed HOI4 directory. The repo skill also says the 3D model pipeline package does not provide this unrelated viewer. Availability elsewhere is unverified and is recorded as a package gap. |

No connected server version/health result or task negotiation was available in the tool inventory. No job, helper-expansion, native MCP task, or game-launch route was used. Exposed schemas were inspected for probability inspect/evaluate/sweep/compare/render/simulate/sequence, event inspect/render, technology inspect/render, reference context/search/read, source lookup, and script validation.

The initial source query using source.query was rejected as an invalid source key. The valid current source form is source.path. A reference-context AI question over 160 characters was rejected, then a shorter question succeeded. A source lookup request with maxLines 120 was rejected because the live maximum is 80, then the narrower 80-line lookup succeeded. These were corrected request-shape limits, not route-health evidence.

## Reference evidence

| Reference | Section | Live revision |
| --- | --- | --- |
| Installed game documentation, C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md | random_list, lines 5413–5432; set_technology, lines 7805–7819 | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af |
| Offline wiki, paradox_wiki\Effects - Hearts of Iron 4 Wiki.md | Random effects and proportional random_list weights, lines 4504–4571 | 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c |
| Offline wiki, paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md | random_list, line 894 | 18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49 |
| Offline wiki, paradox_wiki\Technology modding - Hearts of Iron 4 Wiki.md | Technologies, enabling objects, hidden technology examples, lines 61–80, 146–171, 172–214 | c5428838db20c4c812c66aff82cbafc58db3b73453c30436bce0d97436170bee |
| Offline wiki, paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md | Temporary variable lifetime and nested scripted effect/trigger caveat, lines 435–443 | 62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4 |

The installed documentation describes random_list weights as scope variables and the effect selected by associated weight. The offline Effects page states that the option's chance is its weight divided by the total active weight. That rule supports no exact selection share until the complete active pool and all external weight inputs are confirmed.

## Frozen current raw source identities

Each source was copied byte-for-byte under C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\docs\plans\025_alien_technology_in_antarctica_plans\evidence_20261007_reward\source_snapshot\ preserving its repository-relative path. At copy time, the source hash before copy, source hash after copy, and snapshot hash matched for every row.

| Repository-relative source | Bytes | Frozen snapshot SHA-256 |
| --- | ---: | --- |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt | 61311 | 67993F2CB733C0DE4B8B2EC96AC55CE68BCBC65EF0ED79F08F9E4A6F66B0F604 |
| common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.md | 18310 | A1A044288C74BC91734453C0A5EED1F8209B49C9DA6E5C2CAEEA394DF6ACBAFD |
| common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt | 19964 | EDE44BE51D047929E45DE9EDBF59D5064C98983E5A914C46F0D7FC31B58AA19B |
| common/script_constants/016_brilliant_scientist_custom_technology_constants.txt | 2785 | ACDACB5CE819989AD30DE13A4520F532A798490C27FEB575B048F1D5D6DBF5AB |
| common/technologies/016_brilliant_scientist_project_technologies.txt | 10706 | 60BF2225FA86B235EE30898A9B1D19383D6D89AF72613764FD1A72D75AE7548E |
| common/technologies/016_brilliant_scientist_project_force_technologies.txt | 8395 | 8B0129A6B71FFCB5AD5D4EF354329D3ED10B18919D0849922A52763049F3F1D0 |
| common/units/016_brilliant_scientist_project_forces.txt | 19688 | FD0DF90E8C27DB087E7DF09BA8E325F3AE887A80B673677179D0FD5403489357 |
| common/units/equipment/016_brilliant_scientist_project_force_equipment.txt | 33392 | 4687027A01DBC8CD1BEE2EA0A872EC418FA85628EF2C554857A2C6320285A2E0 |
| events/025_alien_technology_in_antarctica.txt | 84403 | 6E5993A3E8C83267AF49517B3119F5F5E187B156A7BA9AA7BB1FD1413BF9C95E |
| common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt | 59164 | AFE0086F5ACF1F05677E0711C3B875E862D85753C8E793B0F35D93B56549568D |
| common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.md | 10886 | 8D2585D353EE4A3066479403A88A063CB819A8418E44C1CD90606EC740AB33BE |
| common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt | 80184 | DB50893535A6C3DDAA3490F9851A438D4159B01BC061EB3A78EADE19176EC1FD |
| common/script_constants/025_alien_technology_in_antarctica_constants.txt | 29135 | A5746329E1A4B012CCDD1C275B6DB8D295F5B0EE93F8482068638090C580202B |
| common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt | 240930 | 920022325FF9FABF32A7957F4FFAF60C67E8623940A4DAACB5B98FE0D63AB0ED |
| events/036_alien_spacecraft.txt | 2972 | 6531D27F883458F3D5E874CBEF1C01A197D23D101C57CAA2FC38D35567A69C73 |

At the final identity check, all current gameplay source files still matched their frozen bytes. The ledger Markdown had changed after the snapshot: snapshot SHA-256 8D2585D353EE4A3066479403A88A063CB819A8418E44C1CD90606EC740AB33BE, current SHA-256 14FF28F5CCB32E292DF3E9A55E2207926091B0FED7DCD5C9BFEC5D9CBE7E9AD9. The visible current edit is in the seizure-return documentation owned by the parent. The current reward-bridge paragraph still defines overlap by broad field labels. The byte-exact snapshot was preserved without overwrite.

The 2026-10-03 frozen API hash was 4AA4CB9BAE94A76B8F33A5EA37F76E3C1AB040168FB688C7B9CD4A3C9EB6D3E1. The current API effects and constants have changed since that baseline. The API trigger and Event016 technology/unit sources listed above retain the historical raw hashes. The current Event025 ledger and settlement sources also differ from the October 3 snapshots. These are raw-byte identities, not MCP source revisions.

## Remaining uncertainty and handoff

The audit is not complete for probability claims. No candidate received an MCP-confirmed normalized share, the named evaluation and sweep have no returned scenario hash, and the named event/technology views have no returned structural artifacts. All selection probabilities, rank reversals, timing distributions, and in-game outcomes remain unresolved.

The parent can review the full source identities and exact selectors in the snapshot tree. A later owner patch or accepted aviation extension requires a fresh probability baseline and compare pass with the same explicit scenario IDs, retaining every old false-positive fixture as historical evidence. The probability auditor remains read-only and does not select weights or approve the owner extension.

Skills read and applied: chaos-redux-subagents, chaos-redux-events, chaos-redux-mtth, and chaos-redux-event-planning. No skill was created or updated.
