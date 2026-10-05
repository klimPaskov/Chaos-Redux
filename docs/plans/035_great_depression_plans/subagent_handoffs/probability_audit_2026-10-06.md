# Event 035 AI and probability audit — 2026-10-06

## Status

This is an incomplete read-only audit of the Event 035 decision AI, incident pools, evolution pacing, and requested report/news event options.

The HOI4 MCP probability routes are exposed, but the decision and event-option source inspections timed out after 600 seconds, and no scenario evaluation completed for those surfaces.

The random-list source inspection completed and exposed its full source inventory, but it could not evaluate a complete runtime pool because the file contains multiple categorical pools and 128 unresolved external inputs.

The MTTH source inspection completed and reported no native event-mean-time-to-happen weighted surface for Event 035's dynamic delay entries.

No current AI score, selection probability, incident ranking, evolution timing distribution, rank reversal, starvation, dominance, or exploit result is asserted from this audit.

## Audited surfaces

| Surface | Exact source identifiers | Classification |
| --- | --- | --- |
| Conference AI and supplier eligibility | <code>great_depression_global_recovery_conference</code> and <code>great_depression_join_global_recovery_conference</code> in <code>common/decisions/035_great_depression_decisions.txt</code> | Source score formula available; scenario scores and selection race unresolved |
| Conference supplier quotes | <code>great_depression_event34_supplier_adapter</code> and <code>great_depression_global_recovery_conference</code> in <code>common/scripted_effects/035_great_depression_effects.txt</code> and <code>common/scripted_effects/035_great_depression_decision_effects.txt</code> | Source-only before/after gate review; no MCP comparison |
| Random incident selection | <code>great_depression_run_due_incident_pool</code>, <code>great_depression_incident_run_baseline_pool</code>, <code>great_depression_incident_run_contagion_pool</code>, <code>great_depression_incident_run_social_pool</code>, and <code>great_depression_incident_select_social_extreme_outcome</code> in <code>common/scripted_effects/035_great_depression_incident_effects.txt</code> | Source inventory complete; runtime pool and conditional probabilities unresolved |
| Evolution activation delays | <code>great_depression_financial_contagion_activation_interval</code>, <code>great_depression_social_collapse_activation_interval</code>, <code>great_depression_second_great_depression_activation_interval</code> in <code>common/mtth/035_great_depression_mtth.txt</code>, consumed by <code>great_depression_try_evolution_activation</code> in <code>common/scripted_effects/035_great_depression_effects.txt</code> | Source delay logic reviewed; timing distribution unresolved |
| Event option weights | <code>chaosx.nr35.2</code>, <code>chaosx.nr35.14</code>, <code>chaosx.nr35.15</code>, and <code>chaosx.nr35.22</code> in <code>events/035_great_depression.txt</code> | Source tokens reviewed; event-option MCP evidence unresolved |

The broader AI probability matrix surfaces for target selection, doctrines, ordinary recovery actions, contagion partner choice, breakdown outcomes, Evolution III conversion, blocs, and conference choice remain outside this bounded tranche.

## MCP evidence

All successful MCP calls used workspace <code>mod_chaos_redux_ea3b2d67c2c0</code>.

The probability-inspection artifact verified HOI4 version <code>Operation Postern v1.19.2.0.a729 (d245)</code> and probability-tool version <code>3.8.1</code>.

| Tool and source | Result and preserved evidence |
| --- | --- |
| <code>hoi4.probability_inspect</code>, adapter <code>decision_ai_will_do</code>, source <code>common/decisions/035_great_depression_decisions.txt</code> | The corrected source form was <code>{path: ...}</code>. The call timed out with <code>timed out awaiting tools/call after 600s</code>. It returned no artifact, source revision, candidate inventory, score trace, or scenario hash. |
| <code>hoi4.probability_inspect</code>, adapter <code>random_list</code>, source <code>common/scripted_effects/035_great_depression_incident_effects.txt</code> | Returned <code>PROBABILITY_SOURCE_INSPECTED</code>. Artifact URI: <code>hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48f165295b4638c6c372e7b51e96fd8e99fb51d34896421d7f15630333e6dd24/b8ed6f2e04c982c5f09d312e7f41863ac765d1dba36a5aa0ad0e6a5f72cb40c2/probability-inspect-9dfdbe9330a9.json</code>. Source revision: <code>32b195e30b3b82726384e1c04f90e4a132eeacab8397667d2d69aa0494052386</code>. Aggregate source hash: <code>9dfdbe9330a92d184f59e5f5d2aad531b46570fefb6b49daaefaa5d8aae207e3</code>. Candidate-file provenance hash: <code>7da1108b02bc4dce6eb1188e66a5bedc8b6d3cb9787a5dd190b1967f0aa2e969</code>. The artifact was retrieved in byte ranges, reconstructed to 932,691 bytes, and its SHA-256 matched the artifact URI. |
| <code>hoi4.probability_inspect</code>, adapter <code>event_mean_time_to_happen</code>, source <code>common/mtth/035_great_depression_mtth.txt</code> | Returned <code>PROBABILITY_SOURCE_DISCOVERED</code> with <code>discoveryReason = no_weighted_surfaces</code>, zero candidates, and zero unresolved inputs. Artifact URI: <code>hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2141a62b80a3694177971897aefe09ad50334bb608d5ff45cf81d2cb0de38fb8/26353f61c8c51315ec9d41b86be0d8050c8466369c841d6bec8027f290d9f562/probability-inspect-9059f0f856e9.json</code>. Source revision: <code>42b95ed1b8f1b51519c4a160d0f0d1ff060149a45e9a65a75241e4b8441289ad</code>. Source hash: <code>9059f0f856e99d1ce99ddfe33dd3f23581fd1820a302c925a6162ec60e4edd45</code>. |
| <code>hoi4.probability_inspect</code>, adapter <code>event_option_ai_chance</code>, source <code>events/035_great_depression.txt</code> | The call timed out with <code>timed out awaiting tools/call after 600s</code>. It returned no artifact, source revision, scenario hash, option ranking, or normalized chance. |
| <code>hoi4.event_inspect</code>, mode <code>trace</code>, selector <code>{kind: event, eventId: chaosx.nr35.2}</code> | A bounded query with depth 1, 4 nodes, 8 edges, helper expansion disabled, and no refresh produced no result after about 93 seconds and was terminated. No graph revision or artifact was returned. |
| <code>hoi4.event_render</code>, view <code>options</code>, selector <code>{kind: event, eventId: chaosx.nr35.2}</code> | A bounded query with depth 1, 4 nodes, and helper expansion disabled produced no result after about 31 seconds and was terminated. No render artifact was returned. |

The probability-inspection summary for the random-list file reports 63 candidates, zero candidates available without a scenario, 128 required inputs, one unresolved input, and <code>poolComplete = false</code>.

Its unsupported diagnostic is <code>MULTIPLE_CATEGORICAL_POOLS</code>: it requires one event-option or random-list pool to be selected before normalized probabilities can be requested.

The selected adapter documents eligibility, raw scores, and normalized probabilities for a complete pool, but does not provide sequence or time-distribution conversion.

The candidate artifact lists the full required-input set, including country variables, global arrays, event targets, state scopes, and dynamic target conditions.

The MCP result did not provide base-weight modifier traces, an evaluated ranking, or a named scenario result.

### Scenario coverage

| Scenario ID | Intended decision or timing case | Candidate pool and external factors | Result |
| --- | --- | --- | --- |
| <code>supplier_no_quote</code> | Industrial Boom supplier can see an open conference but has no Event 35 quote | The candidate pool is incomplete because decision-source inspection timed out. Conference episode and stage, supplier registration, cost-variable readiness, action lock, available political power, fuel, convoys, civilian factories, participant room, and AI profile are not analyzer-bound. | Unresolved; source gate predicts unavailable before quote initialization, but no MCP scenario was evaluated. |
| <code>supplier_quoted_affordable</code> | Registered supplier has a complete quote and all required resources | The same candidate and conference-state inputs are missing from the probability result. | Unresolved; current source contains quote-refresh calls, but no scenario comparison verified the outcome. |
| <code>supplier_short_one_resource</code> | Supplier has a complete quote but is short on one required resource | The exact resource shortage must be one of political power, fuel, convoy equipment, or civilian factories available for projects; no typed input or full AI selection pool was accepted. | Unresolved; source gate predicts unavailable, with no score or selection result. |
| <code>supplier_withdrawn</code> | Supplier withdrew from current-world commitments | The withdrawal episode ID must be compared with the active global episode ID; the decision pool and AI score trace remain unavailable. | Unresolved; source gate predicts unavailable while the withdrawal ID matches the active episode. |
| <code>EVO-01</code>–<code>EVO-08</code> | Evolution I–III timing, Event 34 inheritance, and disabled evolution | The matrix's named states were read, but the native event-MTTH adapter found no weighted surface in the custom delay file. Scheduled state transitions and current episode settings were not modeled. | Unresolved; no timing value, median, tail, or activation probability was evaluated. |
| <code>K-09</code> historical set | Incident-pool balance across severity and evolution contexts | Prior 2026-09-05 handoff declared an audit-only custom pool with 59 entries, 84 scenarios, and 4,956 candidate-scenario rows. | Historical custom-pool model only; not current-source or runtime random-list probability evidence. |

The historical K-09 analysis ID was <code>probability-00c43d73f98109724cc77856</code> with scenario hash <code>8ebb73c646d4ae42bd3f897b569440f533e376a67a6fd73dcdeb9cc6ee34b100</code>, source revision <code>4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945</code>, and source hash <code>a35e848d0bba357b565a11c7b5b77b4e8d99a370c63cf7d8e40020939517458a</code>.

That prior handoff reported only the expected fail-closed no-incident outcomes in <code>K09-GATE-NO-TARGET</code> and <code>K09-GATE-NO-PARTNER</code>; it explicitly states that the custom manifest is not a normalized runtime probability receipt for the Clausewitz random lists.

Its ranking, matrix, and unresolved-view artifacts are recorded in <code>docs/plans/035_great_depression_plans/subagent_handoffs/k09_incident_pool_audit_2026-09-05.md</code> and must not be treated as a current render or current-source result.

## Decision AI and supplier eligibility

The conference join surface is <code>great_depression_join_global_recovery_conference</code> in <code>common/decisions/035_great_depression_decisions.txt</code>.

Its target surface admits an active crisis, an exposed partner, a prior global contributor, or a country with <code>industrial_boom_active</code> when the recovery conference is open and the economy is viable.

Its availability separately requires a complete quote, an open action slot, participant room, open global commitments, and enough political power, fuel, convoy equipment, and civilian factories available for projects.

The quote-readiness trigger requires all ten cost variables: factor, civilian, political power, manpower, fuel, trains, convoys, support equipment, stability, and war support.

The source AI weight starts at <code>constant:great_depression_ai_weight.standard</code> (6), adds priority (16) for a coherent active crisis, elevated (10) for a major, strong (8) for either relief-coalition or financial-stabilizer profiles, and standard (6) for a global contribution.

The source AI block multiplies by zero for a conference stage that is not ready or a liquidation-gambler profile.

It does not visibly mirror the availability checks for cost readiness, resource affordability, participant room, or <code>great_depression_global_commitments_are_open</code>.

This is a source-level positive-score-on-blocked-choice risk for <code>supplier_withdrawn</code> and <code>supplier_short_one_resource</code>, not a confirmed AI selection defect; the probability route did not return a score trace, and engine screening of unavailable decisions remains unresolved.

The adjacent convening decision <code>great_depression_global_recovery_conference</code> starts at blocked weight 0 and adds profile, stage, major, and affordability modifiers; its source weight block was not changed in the current edits.

### Current quote change against the Git baseline

The immutable pre-change source baseline is Git commit <code>786a48834a81beddefcd5cefbfad834ce5b07ed6</code>.

Before that commit's later workspace edits, <code>great_depression_event34_supplier_adapter</code> did not call the quote refresh, and the conference-opening effect refreshed the contributor array but not registered Industrial Boom suppliers.

The current <code>common/scripted_effects/035_great_depression_effects.txt</code> calls <code>great_depression_refresh_costs</code> in <code>great_depression_event34_supplier_adapter</code> at line 6798.

The current <code>common/scripted_effects/035_great_depression_decision_effects.txt</code> also iterates <code>global.great_depression_global_supplier_risk_countries</code> and refreshes each extant supplier's quote when the conference opens at lines 1381–1388.

Those edits address the source path that left a registered supplier without the variables required by <code>great_depression_costs_are_ready</code>.

They change quote readiness and eligibility, not an <code>ai_will_do</code> constant or modifier.

## Incident-pool source and cadence

The current source artifact groups the 63 random-list entries into eight separate lists:

| Pool | Candidate count | Source entry identifiers |
| --- | ---: | --- |
| Due-incident router | 4 | <code>035_great_depression_incident_effects.txt:1045.entry.1</code>–<code>:1045.entry.4</code> |
| Baseline incident pool | 11 | <code>035_great_depression_incident_effects.txt:435.entry.1</code>–<code>:435.entry.11</code> |
| Contagion incident pool | 12 | <code>035_great_depression_incident_effects.txt:528.entry.1</code>–<code>:528.entry.12</code> |
| Social pool, first branch | 7 | <code>035_great_depression_incident_effects.txt:739.entry.1</code>–<code>:739.entry.7</code> |
| Social pool, second branch | 7 | <code>035_great_depression_incident_effects.txt:783.entry.1</code>–<code>:783.entry.7</code> |
| Social pool, third branch | 7 | <code>035_great_depression_incident_effects.txt:829.entry.1</code>–<code>:829.entry.7</code> |
| Social pool, fourth branch | 7 | <code>035_great_depression_incident_effects.txt:877.entry.1</code>–<code>:877.entry.7</code> |
| Social extreme-outcome pool | 8 | <code>035_great_depression_incident_effects.txt:1079.entry.1</code>–<code>:1079.entry.8</code> |

The incident constants provide pool-router bases 6, 5, and 6; incident-class bases common 20, uncommon 14, rare 9, major 5, severe 2, positive 8, and no-incident 3; and class factors disabled 0, low 0.5, high 1.5, and severe 2.

Those are source constants only; the MCP did not produce effective weights after eligibility gates or modifier traces.

The adapter found target and cooldown dependencies including active episode, Severity, Evolution floor, last incident kind and pool, project failures, valid state/center/project targets, partners, organized social actors, and shared random-civil-war scopes.

Because the file contains eight categorical lists, their entries must be evaluated as separate complete pools; adding them together would not yield a valid selection probability.

The current timing constants are 21 days for the baseline due interval, 14 days when Financial Contagion or Social Collapse is active, 7 days for no-op retries, 42 days for family cooldowns, 14 days for the active pressure window, and a 48-receipt history cap.

The 2026-09-05 custom K-09 manifest modeled one 21-day categorical cadence; the current source has an additional 14-day evolution interval and 7-day retry path.

Its old repetition and timing conclusions therefore do not cover the current conditional cadence and are not current-source sequence evidence.

## Evolution pacing source

The source base delays are 120 days for Financial Contagion, 140 days for Social Collapse, and 180 days for The Second Great Depression.

Financial Contagion multiplies its delay by 0.65 at high Severity, 0.70 under low stability, 0.80 for a faction, subject, or Event 34 supplier link, 1.25 for an improving trend, and 1.15 when none of those strong links applies.

Social Collapse uses factors 0.65 for high Severity, 0.70 for sustained extreme social pressure, 1.35 when all Depression Centers have reopened, and 1.20 above the high-stability floor.

The Second Great Depression uses factors 0.65 for high Severity, 0.75 for organized-actor proof, 0.80 for attributable contagion, 0.70 for a major with at least three active crises, and 1.35 for a non-major improving origin with fewer than two active crises.

<code>great_depression_try_evolution_activation</code> computes each MTTH value when its due-day variable is absent, stores <code>global.num_days + delay</code>, and later checks whether the stored due day has arrived.

State changes after that initial scheduling do not update the already-stored deadline.

The due variables clear at activation and in reset, abort, and recovery cleanup paths, but no disable-time clear appears in the reviewed source.

While an evolution is disabled, <code>is_current_evolution_enabled</code> blocks scheduling and activation; if it can be re-enabled during the same crisis after a stored due date has passed, the next enabled pulse can activate it immediately.

That is a conditional source-level timing risk for an unmodeled disable/re-enable case, not a result for <code>EVO-08</code>, which only specifies that an evolution remains disabled.

## AI validity, dominance, starvation, repetition, and exploit risk

Decision <code>ai_will_do</code> values are willingness scores in a selection race; they are not probabilities proportional to the sum of weights.

Event-option <code>ai_chance</code> and random-list weights use proportional selection semantics, but neither pool was scenario-evaluated in this pass.

No current numeric decision ranking, supplier rank reversal, incident dominance, valid-path starvation, or event-option chance was returned.

No current exploit or repetition rate was established; only the source cadence and the conditional stored-deadline behavior above were verified from files.

The historical K-09 custom-pool result reported no unexpected dominance across its declared scenarios, but it is not evidence for the current random-list source or cadence.

The parent reports nine source tests passed; this auditor did not run tests or launch the game.

## Recommended follow-up

Keep the current quote refresh in <code>great_depression_event34_supplier_adapter</code> and the conference-opening walk over <code>global.great_depression_global_supplier_risk_countries</code>.

When the decision probability route responds, evaluate the four named supplier scenarios with the same conference stage, supplier registration, cost quote, resource availability, participant-room, withdrawal episode, and AI-profile inputs.

Check whether unavailable decisions are excluded before AI score selection; if not, add a zero factor in <code>great_depression_join_global_recovery_conference</code> that mirrors closed commitments, unavailable cost, and no-room gates.

Re-run the incident audit as one scenario set per random-list identifier, with each full source pool, all state/relationship bindings, last-kind cooldown, and conditional 21/14/7-day cadence declared.

Clarify whether evolution deadlines freeze while disabled or are cleared and recalculated; add the disable/re-enable case to the timing scenarios if that setting transition is supported.

Do not claim the parent quote change has passed a probability comparison; the current decision-weight source is byte-identical to the pre-change decision file, while only helper effects changed, so comparing the decision file to itself would not test quote eligibility.

## Comparison and rendering disposition

<code>hoi4.probability_compare</code> was not run and has no comparison ID.

The baseline decision-weight source at commit <code>786a48834a81beddefcd5cefbfad834ce5b07ed6</code> and the current decision-weight file are byte-identical; the changed surfaces are quote-refresh effects, not AI-weight definitions.

The probability inspection call needed to establish a complete decision scenario failed by the 600-second timeout, and the random-list inspection explicitly reported multiple categorical pools and incomplete external inputs.

Calling compare on the unchanged decision source would be a self-comparison and would not measure the effect-driven availability change.

<code>hoi4.probability_evaluate</code> and <code>hoi4.probability_sweep</code> were not run because no accepted complete candidate pool and scenario inputs were available.

<code>hoi4.probability_simulate</code> was not run because no uncertain-input distributions were declared.

<code>hoi4.probability_sequence</code> was not run because the random-list adapter reports <code>sequence = false</code> and the current complete cadence and transitions were not declared in a manifest.

<code>hoi4.probability_render</code> was not run because no current analysis ID or scenario result exists.

<code>hoi4.event_inspect</code> lint/trace and <code>hoi4.event_compare</code> for <code>chaosx.nr35.14</code>, <code>chaosx.nr35.15</code>, and <code>chaosx.nr35.22</code> were not attempted after the bounded <code>.2</code> trace produced no artifact; the parent requested that no further broad calls be made.

## Reference sources read

The offline wiki's Decision modding AI section states that a decision requires <code>ai_will_do</code> and that the block is an MTTH-style score formula.

The offline wiki's AI modding section distinguishes the common highest-random-score <code>ai_will_do</code> selection race from event-option <code>ai_chance</code> proportional sampling.

The offline wiki's Effects and Scopes sections state that <code>random_list</code> uses proportional weights within its candidate list.

The installed vanilla Country Decisions documentation separates decision visibility from current availability, and the installed effects documentation describes <code>random_list</code> as choosing an effect based on its associated weight.

| Reference | Local path and line span | Revision |
| --- | --- | --- |
| Decision modding — AI | <code>C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md</code>, lines 357–374 | <code>7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162</code> |
| AI modding — MTTH blocks and selection semantics | <code>C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md</code>, lines 26–37 | <code>917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818</code> |
| Effects — random effects | <code>C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md</code>, lines 4504–4558 | <code>997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c</code> |
| Scopes — random_list | <code>C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md</code>, line 894 | <code>18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49</code> |
| Installed Country Decisions documentation | <code>C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md</code>, lines 1–46 | <code>5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019</code> |
| Installed effects documentation — random_list | <code>C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md</code>, lines 5413–5432 | <code>2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af</code> |

The audit read <code>AGENTS.md</code> and the skills <code>.agents/skills/chaos-redux-subagents/SKILL.md</code>, <code>chaos-redux-mtth/SKILL.md</code>, <code>chaos-redux-decisions-missions/SKILL.md</code>, <code>chaos-redux-events/SKILL.md</code>, and <code>chaos-redux-event-planning/SKILL.md</code>.

## Pre-change evidence and files

Exact pre-change bytes were extracted directly from commit <code>786a48834a81beddefcd5cefbfad834ce5b07ed6</code> into <code>docs\plans\035_great_depression_plans\subagent_handoffs\evidence\035_probability_audit_2026-10-06\before\</code>.

| Source | Baseline raw SHA-256 | Current raw SHA-256 | Relationship |
| --- | --- | --- | --- |
| <code>common/scripted_effects/035_great_depression_effects.txt</code> | <code>7eaf0b885a1ebabd7d13ddba459a341ad67b82975e24d61ee40dfee273458d59</code> | <code>6d015ff2382e05fc1c4b0cee2cbf36a8f0a6c4f1c6d75f55d66de3e08db20e78</code> | Changed; includes supplier quote initialization and announcement/report scheduling |
| <code>common/scripted_effects/035_great_depression_decision_effects.txt</code> | <code>73d771b09b1c1a697f632a199de712f1ef9c69b2c5c2e0afd1bf7286107a1cc8</code> | <code>b419d96cef3bc9fe2f51d0d71f6e046c324174c18c6af3f5704bccf31f8bede0</code> | Changed; includes refresh for registered suppliers on conference opening |
| <code>common/decisions/035_great_depression_decisions.txt</code> | <code>e307823fbde9732a1dcc5187916335db8207a8a1174ffd4d7e3b6154e300dcb7</code> | <code>e307823fbde9732a1dcc5187916335db8207a8a1174ffd4d7e3b6154e300dcb7</code> | Byte-identical; no AI-weight change |
| <code>common/scripted_triggers/035_great_depression_decision_surface_triggers.txt</code> | <code>6647a403c26b7962f567316daf991a8952baf5feedf3436e03c251c7bc60f28c</code> | <code>6647a403c26b7962f567316daf991a8952baf5feedf3436e03c251c7bc60f28c</code> | Byte-identical |
| <code>common/script_constants/035_great_depression_constants.txt</code> | <code>7c799446f570dc1ca403c0ae62ed79d8f70d0f5b033220935e8dc24f1d2fd1df</code> | <code>7c799446f570dc1ca403c0ae62ed79d8f70d0f5b033220935e8dc24f1d2fd1df</code> | Byte-identical |
| <code>events/035_great_depression.txt</code> | <code>fadd54aa5e97608a2bffa8d5ee1c12d3afb8466311693556319e61dd1b8ff9dc</code> | <code>fadd54aa5e97608a2bffa8d5ee1c12d3afb8466311693556319e61dd1b8ff9dc</code> | Byte-identical; event option weights are unchanged |

The current localisation file hash is <code>ba2bc7a2b266c9131901ee54854706dd2bdde62000eb67bb04405ec6abeb5444</code>; its wording edits do not alter a weight.

The only files written by this auditor are this handoff and the byte-exact evidence copies in the bounded <code>before</code> folder.

No gameplay source, event source, AI weight, spreadsheet, or test file was edited, and no commit was created.
