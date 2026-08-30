# Event 31 Random Terror probability baseline handoff

## Audit status

This is a read-only baseline audit of Event 31 Random Terror, with fixed identity `chaosx.nr31.1`, Minor Repeatable, Chaos level 1, and the five evolutions Organized Cells, Transnational Terror Network, Territorial Insurgency, The Jihadist International, and The Final Jihad.

No gameplay, AI, event, focus, decision, mission, scripted effect, scripted trigger, localisation, country, GUI, asset, or runtime file was patched.

No Event 31 GUI was created or audited as an owned GUI surface, the 3D pipeline was not used, and Internal Fracture was not registered.

The evidence classes in the scenario matrix are used literally: exact means a complete pool and fully resolved factors, bounded means a complete known pool with explicit external bounds, sampled means seeded simulation under declared assumptions, score-only means relative ordering without normalized probability, and unresolved means a missing pool, route, schema, or external state.

The completed MCP pass did not reach named scenario evaluation, sweeps, simulation, sequence analysis, comparison, or rendering before the requested stop. Therefore no exact selection probability or balance completion claim is made below.

## Immediate baseline verdict

The source baseline contains three confirmed implementation defects that materially invalidate the accepted Event 31 pacing and settings contracts.

1. `random_terror_resolve_evolution` resolves the highest eligible evolution in one call, and `random_terror_run_global_wave` calls it at the start of every global wave.
2. The accepted 90, 120, 150, 180, and 210-day campaign-sensitive evolution pacing has no observed scheduler or MTTH-backed path in the Event 31 source.
3. The resolver checks `random_terror_evolution_N_disabled`, while the shared Event Details toggle writes `events_log_disabled_evolution_31_31_N`, so disabled evolutions are not reliably disabled by the shared control.

The False Revelation trigger contains the expected gate, but there is no observed automatic eligibility scheduler. `random_terror_begin_false_revelation` is reached from `random_terror_commit_revelation_transaction`, and the transaction helper has no external call in the completed repository call-graph search. The focus and decision paths call `random_terror_actor_accelerate_revelation`, which only sets a request or gate-failed flag and does not itself begin the terminal branch.

## Repository surfaces reviewed

The direct Event 31 weighted and state surfaces reviewed were `events/031_terrorist_attack.txt`, `common/scripted_effects/031_random_terror_effects.txt`, `common/scripted_triggers/031_random_terror_triggers.txt`, `common/script_constants/031_random_terror_constants.txt`, `common/decisions/031_random_terror_decisions.txt`, `common/decisions/031_random_terror_missions.txt`, `common/decisions/categories/031_random_terror_categories.txt`, `common/national_focus/031_random_terror_focus.txt`, `common/on_actions/031_random_terror_cxt_on_actions.txt`, and `common/ideas/031_random_terror_ideas.txt`.

Shared surfaces reviewed for cross-system behavior were `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_triggers/chaosx_settings_triggers.txt`, the Event 14 interaction paths, the shared Event Details registry, relevant Chaos Redux on-actions, and the Event 31 country and carrier definitions.

The required Event 31 specifications and matrix were read, including `031_random_terror_ai_scenario_matrix.md`, Parts 1 through 13, the complete-spec copy, the source audit, research notes, improvement review, country package matrix, decision and mission matrix, and the related prompts and manifest.

The required local repository guidance, Chaos Redux event, MTTH, focus-tree, decision and mission, event-planning, and subagent skills were read before the audit.

The required offline Paradox wiki pages were consulted from `paradox_wiki/`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, National focus modding, and AI modding.

The installed vanilla documentation was consulted from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including the script concept, effects, triggers, modifiers, dynamic variables, localisation objects, localisation formatter, and script math documentation.

Vanilla event option `ai_chance`, vanilla `ai_will_do` decision and focus patterns, and the Chaos Redux Event 14 cannibalism event, decisions, scripted effects, triggers, and AI interaction paths were used as structural precedents.

## MCP evidence ledger

The MCP workspace returned by the completed calls was `mod_chaos_redux_ea3b2d67c2c0`.

| Route | Exact request result | Artifact, revision, or blocker | Classification |
| --- | --- | --- | --- |
| `hoi4.probability_inspect` with `{source:{event_id:"chaosx.nr31.1"}}` | Rejected with `Unrecognized key "event_id" at source`. | The source schema requires an object path selector. | Exact schema blocker for that request form. |
| `hoi4.probability_inspect` with `{source:"events/031_terrorist_attack.txt"}` | Rejected with `expected object, received string at source`. | The source schema does not accept a source string. | Exact schema blocker for that request form. |
| `hoi4.probability_inspect` with `{}` | Returned `PROBABILITY_ADAPTERS_LISTED`, with 11 listed adapters, `availableAdapters: []`, and zero candidates. | No artifact was produced. | Exact discovery result, not Event 31 evidence. |
| `hoi4.probability_inspect` with `source.path = events/031_terrorist_attack.txt` | Returned `PROBABILITY_SOURCE_DISCOVERED`, suggested `event_option_ai_chance`, scanned the requested file, and found 15 matching candidates. | Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86edeeb21472f076c0879fdca8d9cedf85a15dba365c461870ebe86a3e498a18/8119fe4933a1d543f394ccf667ee14d05b5329dea65e4585957f18fca64551f0/probability-inspect-6dc5c6a76c7d.json`. Artifact SHA-256: `86edeeb21472f076c0879fdca8d9cedf85a15dba365c461870ebe86a3e498a18`. Source revision: `0e3a90634d4e6b1f62262aec02bd1ab60167df69d923ac9b1f4ba3fb43934cee`. Source hash: `6dc5c6a76c7d0a77b925807f6a476bdaacb69f4f94f429bcd73eefb628dcf378`. | Exact source discovery and candidate-pool discovery only. |
| `hoi4.probability_inspect` with `source.path = common/ideas/031_random_terror_ideas.txt` | Returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`. | Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18e8212b02ff7828a1c3c2b4812a97ebc6221c4178d4282a5095d318f6b7abb3/29943c296acece80c4c7248697744e00273e38a7de0f044d7b1dc4656e148fd1/probability-inspect-575604ec03ac.json`. Source revision: `6548740135864c966f65717ee6cc4ff5fb66bca54fb7daa705a77452470991c3`. Source hash: `575604ec03ac70944372330000f9eac9ec98d81f629777bda81ff8d69111f362`. | Exact no-weighted-surface result for the ideas file. |
| Source-specific `hoi4.probability_inspect` attempts for decisions, missions, categories, focus, effects, triggers, constants, on-actions, and country sources | Returned `INTERNAL_ERROR`, `filesScanned: []`, and `Unexpected internal error` in the completed calls. | No probability artifacts were produced for those sources. | Exact MCP blocker. All affected conclusions remain unresolved. |
| `hoi4.event_inspect` with the initial `{id:"chaosx.nr31.1"}` selector | Rejected because the selector requires `selector.kind`. | Exact selector-schema blocker. | Exact schema blocker for that request form. |
| `hoi4.event_inspect` with `{kind:"event",id:"chaosx.nr31.1"}` | Rejected because the event selector requires `selector.eventId`. | Exact selector-schema blocker. | Exact schema blocker for that request form. |
| `hoi4.event_inspect` with `{kind:"event",eventId:"chaosx.nr31.1"}`, scan mode, helper expansion, and depth 8 | Returned `EVENT_INSPECTED_PARTIAL`. The workspace scan reported 9,706 events, 15,119 options, 1,115 entries, 38,223 edges, 30,078 state accesses, 2,207 issues, 2,208 diagnostics, and 2 blocking diagnostics. The scan was cut after 64 of 363 files by `MCP_INLINE_FILES_TRUNCATED`. | Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/837a3bbe7f901c15966b7421e2d211d4ce571b04aece67d8eea578b6719bc0b7/0bad8f7c90c95dd0d69abd43501a422334c4b9403348700bbdb641a32bacf872/event-scan-ce33d5ee346e.json`. Artifact SHA-256: `837a3bbe7f901c15966b7421e2d211d4ce571b04aece67d8eea578b6719bc0b7`. Revision: `ce33d5ee346e83cd752f9a7ea7b893351b5ef03e4debec28c8db99693b2bba24`. Graph hash: `2f3ba39c43b523de2bc480492d1c58d30bbcd53e697695fa02fa37e36bce64bc`. The unclosed source block reported in the artifact is in unrelated `mod:common/on_actions/016...`; it is not attributed to Event 31. | Partial structural evidence only. |
| `hoi4.focus_inspect` with `common/national_focus/031_random_terror_focus.txt` and with tree ID `random_terror_actor_focus_tree` | Returned `SCAN_BYTE_LIMIT` with `Scan exceeds configured byte limit`. | No focus artifact was produced. | Exact MCP blocker. Focus AI and route rankings are unresolved. |
| `hoi4.probability_evaluate` for P01-P10, W01-W08, evolution, actor-route, and identity-pair cases | Not completed before the requested stop. | No evaluate artifact, scenario hash, ranking, waterfall, timing, or probability trace is available. | Exact incomplete-route blocker. |
| `hoi4.probability_sweep` for legitimacy, capital deadline, reserves, hub importance, intelligence, evidence, and foreign access | Not completed before the requested stop. | No sweep artifact or rank-reversal result is available. | Exact incomplete-route blocker. |
| `hoi4.probability_compare` | Not completed before the requested stop. No owner patch or approved candidate balance profile exists for a before-and-after comparison. | No comparison ID or artifact is available. | Exact incomplete-route blocker. |
| `hoi4.probability_simulate` | Not completed before the requested stop. No uncertain-input distribution was declared for a seeded sample. | No seed, sample count, confidence interval, or simulation artifact exists. | Exact incomplete-route blocker. |
| `hoi4.probability_sequence` | Not completed before the requested stop. The Maximum scenario manifest required by the matrix was not supplied to the analyzer. | No sequence artifact, state trace, or terminal-state result exists. | Exact incomplete-route blocker. |
| `hoi4.event_render`, `hoi4.focus_render`, and `hoi4.probability_render` | Not completed before the requested stop. | No rendered evidence path or URI is available for these routes. | Exact incomplete-route blocker. |

The structural Event 31 scan also reported 2,206 dangling option warnings among its global diagnostics. Because the scan was global and partial, those warnings are not assigned to Event 31 without a narrow artifact proving ownership.

## Observed weighted surfaces

### Event options

The successful Event 31 event-source inspection found this complete 15-candidate pool for `event_option_ai_chance`:

`chaosx.news.310.a`, `chaosx.news.311.a`, `chaosx.news.312.a`, `chaosx.news.313.a`, `chaosx.news.314.a`, `chaosx.news.315.a`, `chaosx.nr31.2.a`, `chaosx.nr31.3.a`, `chaosx.nr31.4.a`, `chaosx.nr31.5.a`, `chaosx.nr31.6.a`, `chaosx.nr31.7.a`, `chaosx.nr31.8.a`, `chaosx.nr31.90.a`, and `chaosx.nr31.91.a`.

The nine country report and terminal-related options in `events/031_terrorist_attack.txt` use `ai_chance = { base = 100 }`.

The six news options do not define `ai_chance` in the inspected source.

The raw `100` values are exact source observations. They are not a global Event 31 firing probability, and no normalized choice probability was produced by MCP.

### Incident random list

`random_terror_apply_incident` in `common/scripted_effects/031_random_terror_effects.txt` supplies a complete 24-entry random-list pool before state-context normalization.

| Incident family | Raw source weight |
| --- | ---: |
| civilian attack | 16 |
| transport disruption | 12 |
| depot sabotage | 10 |
| port convoy attack | 8 |
| official assassination attempt | 7 |
| hostage crisis | 7 |
| security site attack | 12 |
| propaganda surge | 10 |
| arms theft | 8 |
| sponsor evidence | 6 |
| smuggling corridor | 6 |
| training area | 5 |
| copycat | 5 |
| failed raid | 5 |
| intelligence breakthrough | 4 |
| defection | 4 |
| relief strain | 5 |
| military defection | 4 |
| capital infiltration | 5 |
| rival organization | 4 |
| community rejection | 5 |
| joint operation | 4 |
| sponsor exposure | 4 |
| cannibal clash | 2 |

The list has positive raw weight for naval, rail, capital, military-defection, corridor, sponsor, and Event 14 interaction families before the state-specific validity checks. The effect later changes some invalid selections to `civilian_attack`, `security_site_attack`, or `defection`.

This fallback preserves a nonzero draw path for an invalid family and changes the effective distribution rather than removing the invalid candidate before normalization. The exact context-conditioned probability is unresolved because the random-list adapter call failed before producing an artifact.

The source records substantive Muslim opposition through `random_terror_muslim_community_opposition_recorded` when `community_rejection` is selected. No real extremist names, symbols, sacred hostile material, religion-based baseline target factor, or identity-based recruitment factor was introduced by this audit.

### Targeted-raid outcomes

`random_terror_resolve_targeted_raid_outcome` selects from a complete five-entry outcome pool after resolving a high, medium, or low public risk band.

| Risk band | Clean | Costly | Partial | Failure | Abusive failure |
| --- | ---: | ---: | ---: | ---: | ---: |
| High | 65 | 20 | 10 | 4 | 1 |
| Medium | 35 | 30 | 22 | 10 | 3 |
| Low | 10 | 15 | 25 | 35 | 15 |

The high band is selected from high response legitimacy and low activity, while the low band is selected from armed activity or very low legitimacy. These are exact raw weights and source gates, not normalized probabilities. No MCP outcome evaluation or seeded simulation was completed.

### Global Jihad pattern and intensity

`random_terror_resolve_scenario_profile` uses four patterns when `random_pattern` is requested, each with raw weight 25: Dispersed Networks, Border Corridors, Capital Uprisings, and Territorial Fronts.

Intensity branches are deterministic source profiles rather than an AI score race. The observed low, medium, high, and maximum anchors are respectively 4, 7, 10, and 15 country targets, 4, 8, 12, and 18 state targets, 1, 3, 5, and 8 actors, and pressure anchors 35, 50, 65, and 80.

The corresponding network reach anchors are 45, 60, 75, and 90, unity anchors are 25, 45, 65, and 85, readiness anchors are 10, 25, 50, and 75, and response-capacity anchors are 2, 3, 4, and 5.

The raw equal pattern weights and deterministic intensity values are exact source observations. Their scenario-conditioned probabilities and setup validity were not evaluated by MCP.

### Government decisions, missions, and focus AI

`common/decisions/031_random_terror_decisions.txt` contains the Event 31 government decision category and many `ai_will_do` blocks. `common/decisions/031_random_terror_missions.txt` contains the eight required mission surfaces: contain wave, protect transport, break corridor, prevent capital, retake, restore civil authority, hostage deadline, and stop uprising.

The decision and mission candidate pools were not returned by a successful probability inspection. Their source scores are therefore not promoted to normalized probabilities.

`random_terror_actor_focus_tree` is defined in `common/national_focus/031_random_terror_focus.txt`, but the mandatory focus inspection stopped at `SCAN_BYTE_LIMIT`. The focus route score race, invalid-route zeroing, rank reversals, and following-focus behavior are unresolved.

The matrix requires Shadow Council, War Directorate, and Ideological Secretariat to be compared as a score race. No exact focus route ranking was produced.

### Evolution selection and pacing

There is no Event 31 `mean_time_to_happen` block in the inspected Event 31 event, decision, mission, focus, effect, or trigger sources.

`random_terror_resolve_evolution` initializes `random_terror_resolved_evolution` to zero, checks the Chaos thresholds in order, and overwrites it through Evolution V when every prior stage is eligible. It then sets the global stage and unlocks only the final resolved stage in the current call.

`random_terror_run_global_wave` calls `random_terror_resolve_evolution` immediately at line 797 before target selection. This makes the highest eligible evolution available at the next wave rather than applying the accepted campaign-sensitive 90, 120, 150, 180, or 210-day timing anchors.

The observed evolution thresholds are 200, 400, 600, 800, and 1000 Chaos for Evolutions I through V, with World End at 1000. Threshold source facts are exact. Evolution timing distribution, campaign modifiers, and delayed transition probability are unresolved.

## Named core scenarios P01-P10

Every row below is retained from `031_random_terror_ai_scenario_matrix.md`. The source observations are separated from MCP probability evidence.

| Scenario | Required behavior and surfaces | Completed evidence | Classification |
| --- | --- | --- | --- |
| `P01_stable_peace_state` | Stable government, peace, one active urban state, high legitimacy, good intelligence, and adequate reserves. Compare target choice, government decisions, incident pool, and territorial spawn. Response cell, intelligence, victim support, and protection should outrank coercive surge. | The event option pool is flat at raw 100, the incident list has the fixed raw family weights, and invalid incident families are normalized after selection. No named scenario evaluation, sweep, comparison, or spawn probability was completed. | Unresolved overall. Raw source observations are exact. |
| `P02_unstable_wartime_authoritarian` | Low stability, war, poor intelligence, strong army, weak legitimacy, and several fronts. Capital and security surge should rise, victim support should remain nonzero, and abusive risk should be higher than P01 without draining all fronts. | The raid source selects a lower public risk band from armed activity or very low legitimacy and exposes the low-band raw outcome weights. No wartime decision score, capital deadline sweep, reserve trace, or seeded sample was completed. | Unresolved overall. Raid gates and weights are exact source evidence only. |
| `P03_occupied_resistance_context` | Occupied states, resistance, supply strain, and one active network. Transport and local-control responses should matter without treating an occupied population as one organization. | Dynamic country and state target pools, transport validity, and decision AI were not returned by MCP. No identity or occupation-conditioned score evaluation was completed. | Unresolved. |
| `P04_successful_response` | Protection, victim support, high legitimacy, an intelligence breakthrough, and one weakened cell. Clean success and closure should rise while severe incidents and spread fall. | The source records intelligence breakthrough, reduces activity, applies recovery effects for clean and costly outcomes, and keeps the incident list fixed before normalization. No before-and-after or recurrence comparison was completed. | Unresolved overall. Source transition facts are exact. |
| `P05_transnational_safe_haven` | Weak host, three affected countries, a sponsor, two corridors, and high reach. Matched corridor and safe-haven actions should dominate while distant attacks remain bounded. | The source contains corridor, sponsor evidence, sponsor exposure, network reach, and Global Jihad profile values. No network candidate pool, foreign AI score, sensitivity sweep, or sampled result was completed. | Unresolved. |
| `P06_territorial_spawn` | Pressure above severe, Lost Local Control, defectors, equipment, viable parent, and a carrier. A connected valid spawn should follow resources and not leave the parent empty or create a free oversized army. | The source calls `random_terror_try_spawn_actor` after Lost Local Control and uses `random_terror_state_is_valid_target` and viable-parent checks. The required event, map, carrier, force-fill, and bounded spawn evaluation routes were not completed. | Unresolved. |
| `P07_muslim_government_against_jihadist` | Evolution IV actor, Muslim-majority government, and strong local religious rejection. Ordinary target score must equal the non-Muslim pair, actor priority must activate, and rejection must reduce unity and recruitment. | The source has a fictional Evolution IV path and a community rejection effect that records Muslim community opposition and reduces International Unity. No paired MCP comparison or recruitment score was completed. | Unresolved overall. Source opposition path is exact. |
| `P08_cannibal_border` | Event 31 and Event 14 actors share a border and each has another enemy. Alliance must remain zero, practical rivalry can rise, and both actors must preserve survival fronts. | The Event 31 source includes `cannibal_clash` with raw weight 2 and records a clash that reduces Network Reach. No Event 14 strategy or diplomacy comparison was completed. | Unresolved. |
| `P09_major_intervention` | Capable major, threatened ally, access, and low domestic pressure. Intelligence and aid should rise, while direct intervention remains conditional on access and threat. | Relevant decision and foreign-access candidate pools were not returned by MCP. No capacity/access sweep or comparison was completed. | Unresolved. |
| `P10_maximum_scenario` | Global Jihad Maximum, several actors, widespread cells, Final Jihad active, and Chaos below and above 1000 variants. Strategic fronts, capital defense, coalition action, and the World End gate must remain coordinated. | The source has maximum deterministic anchors, a four-pattern random list, Evolution V enabling `random_terror_false_revelation_enabled`, and a World End trigger at Chaos 1000. No complete sequence manifest, simulation, scenario setup evaluation, or terminal comparison was completed. | Unresolved overall. Source gates and profile anchors are exact. |

## World-end cases W01-W08

The following results retain the matrix IDs and expected outcomes. They do not claim that the analyzer evaluated the cases.

| Case | Declared inputs and expected result | Source evidence | Classification |
| --- | --- | --- | --- |
| `W01` | Chaos 999, Evolution V yes, high territory, wide crises, high unity, branch enabled. Expected hard block. | `random_terror_can_begin_false_revelation` requires Chaos greater than or equal to `chaos_world_end`, which is 1000. The below-gate block is exact source evidence. | Bounded source gate, unresolved complete scenario. |
| `W02` | Chaos 1000 or more, Evolution V no, high territory, wide crises, high unity, branch enabled. Expected hard block. | The trigger requires `random_terror_evolution_5_unlocked` and `random_terror_false_revelation_enabled`. | Bounded source gate, unresolved complete scenario. |
| `W03` | Chaos 1000 or more, Evolution V yes, low territory, wide crises, high unity, branch enabled. Expected block by territory. | The trigger requires Territorial Control greater than the territorial gate of 60 and territorial state count greater than the capital gate of 2. | Bounded source gate, unresolved complete scenario. |
| `W04` | Chaos 1000 or more, Evolution V yes, high territory, narrow crisis spread, high unity, branch enabled. Expected block by crisis spread. | The trigger requires crisis state count greater than the capital gate of 2. | Bounded source gate, unresolved complete scenario. |
| `W05` | Chaos 1000 or more, Evolution V yes, high territory, wide crises, low unity, branch enabled. Expected block or slow path with falling readiness. | The trigger requires International Unity greater than the unity gate of 70. The source also has terminal counteroffensive losses to readiness and unity. No readiness cadence or lapse evaluation was completed. | Bounded source gate, unresolved timing and lapse behavior. |
| `W06` | Chaos 1000 or more, Evolution V yes, high territory, wide crises, high unity, branch disabled. Expected hard block. | The trigger requires `random_terror_false_revelation_enabled`, but no automatic eligibility scheduler was found. | Bounded source gate, unresolved route reachability. |
| `W07` | All readiness conditions high. Expected delayed candidate, not instant. | The begin effect schedules `chaosx.nr31.95` after `world_end_delay_days` once it is reached, but the completed call graph found no external call to the transaction commit helper that reaches begin. | Exact source reachability finding, unresolved automatic behavior. |
| `W08` | Chaos 1000 or more, Evolution V yes, territory and unity falling, restored countries, branch enabled. Expected readiness decline and candidate lapse. | The source contains counteroffensive reductions, but no automatic eligibility scheduler or readiness-candidate lapse evaluator was found. | Exact missing-scheduler finding, unresolved complete scenario. |

## Five evolution slow, fast, and blocked cases

These are the five exact evolution rows in the matrix.

| Evolution | Slow case | Fast case | Hard block | Baseline result |
| --- | --- | --- | --- | --- |
| Organized Cells | One isolated cell repeatedly contained. | Several countries with surviving cells and coordinated waves. | Evolution disabled. | The resolver can set Evolution I as soon as Chaos is at least 200 during the next global wave, subject to its mismatched disabled flag. No slow or fast MTTH evidence exists. |
| Transnational Terror Network | No sponsor, no border link, and low Network Reach. | Several regions, a safe haven, a sponsor, and surviving organized cells. | Organized Cells disabled or required content missing. | The resolver can jump to Evolution II in the same call after Evolution I is resolved and Chaos is at least 400. No reach or active-country timing evidence exists. |
| Territorial Insurgency | No Lost Local Control state and no viable carrier. | Several armed states, defections, and captured equipment. | No valid territory or evolution disabled. | The source invokes actor spawning after Lost Local Control and can resolve Evolution III in the same threshold pass. Map validity and force probabilities are unresolved. |
| The Jihadist International | No compatible actor, low authority, and strong rivalry. | Several compatible actors, high authority, and territorial victories. | Evolution disabled. | Evolution IV is threshold-resolved at Chaos 800 after earlier stages in one call. The source contains community opposition content, but actor compatibility and leadership ranking were not evaluated. |
| The Final Jihad | Low unity, rival wars, and actors losing territory. | High unity, a dominant leader, capitals, and a wide network. | Evolution IV unavailable or disabled. | Evolution V is threshold-resolved at Chaos 1000 after earlier stages in one call and sets both `random_terror_final_jihad_active` and `random_terror_false_revelation_enabled`. No 210-day timing, leadership, or sequence evidence exists. |

The required pacing anchors are approximately 90, 120, 150, 180, and 210 days after eligibility. The current resolver has no observed delayed stage scheduler and therefore cannot support those timing expectations.

## Actor-route cases

The focus matrix requires the following six route cases. The expected winner is a score-race expectation, not a click probability.

| Actor-route case | Shadow Council | War Directorate | Ideological Secretariat | Expected route | Baseline result |
| --- | --- | --- | --- | --- | --- |
| One isolated state, strong parent, foreign cells | Very high | Low | Medium | Shadow Council | Focus inspection blocked by `SCAN_BYTE_LIMIT`, so rank and invalid-route zeroing are unresolved. |
| Four connected states, regular defectors, adequate supply | Medium | Very high | Medium | War Directorate | No focus probability or score trace. |
| Strong recruitment, charismatic fictional leader, low conventional equipment | Medium | Low | High | Ideological Secretariat | No focus probability or score trace. |
| Criminal-political actor with sponsor and weak doctrine | High or sponsor economy | Medium | Low | Shadow Council or mixed route | No sponsor-factor or route comparison. |
| Evolution IV-compatible actor seeking faction leadership | Medium | Medium | High | Ideological Secretariat or jihadist route | Evolution IV actor gate is source-visible, but route selection and faction-leadership ranking are unresolved. |
| Actor under immediate parent offensive | Medium | High if resources exist | Low to medium | War Directorate or survival path | No reserve, offensive deadline, or focus score trace. |

The matrix requires invalid route conditions to be zero before normalization. That requirement was not proven by MCP.

## Identity-sensitive paired cases

The required pairs hold every non-identity input constant and vary only the named identity field. No MCP paired evaluation or compare artifact was completed. The static source review of the inspected Event 31 target, recruitment, and actor eligibility paths found no positive baseline factor keyed to religion, ethnicity, nationality, refugee status, or ordinary ideology. This is source evidence only and does not replace paired probability evidence.

| Pair ID | Only allowed difference | Required result | Completed result |
| --- | --- | --- | --- |
| `PAIR_MUSLIM_NON_MUSLIM_STABLE` | Muslim-majority religious-demographic registry versus non-Muslim registry. | Equal ordinary target and recruitment scores. | No positive religion factor was observed in the reviewed source. Paired MCP compare is unresolved. |
| `PAIR_ETHNICITY_ONLY_STABLE` | Ethnicity registry only. | Equal ordinary target and recruitment scores. | No positive ethnicity factor was observed in the reviewed source. Paired MCP compare is unresolved. |
| `PAIR_NATIONALITY_ONLY_STABLE` | Nationality registry only. | Equal ordinary target and recruitment scores. | No positive nationality factor was observed in the reviewed source. Paired MCP compare is unresolved. |
| `PAIR_REFUGEE_HOST_NONHOST_STABLE` | Refugee count or hosting status only. | Equal before real relief or route conditions. | No positive refugee factor was observed in the reviewed source. Paired MCP compare is unresolved. |
| `PAIR_DEMOCRATIC_AUTHORITARIAN_STABLE` | Ordinary ideology only, with stability and response capacity held equal. | Equal ordinary target and recruitment scores. | No positive ordinary-ideology factor was observed in the reviewed source. Paired MCP compare is unresolved. |
| `PAIR_RECENCY_CONTROL` | Recently targeted state versus otherwise identical state. | Only cooldown recency lowers the recently targeted candidate. | The source contains target reservation and state cooldown flags, but no paired MCP result. |
| `PAIR_CORRIDOR_CONTROL` | Adjacent to an active corridor versus not adjacent, with all other inputs equal. | Corridor access alone raises the adjacent candidate. | Corridor state flags and Network Reach are source-visible, but no paired MCP result exists. |

Evolution IV is the only stage that unlocks the fictional jihadist branch. Muslim communities, governments, and soldiers have opposition paths in the source design, including community rejection and unity reduction. Religion, ethnicity, nationality, refugee status, and ordinary ideology are not valid positive baseline target or recruitment factors.

## Territorial spawning, readiness, coalition, and defeat

The source invokes `random_terror_try_spawn_actor` after a state reaches Lost Local Control and checks state validity, viable parent conditions, and carrier availability through Event 31 scripted triggers and effects.

The source constants define local, regional, transnational, jihadist, and final actor division anchors of 4, 8, 12, 15, and 20, with a per-state cap of 2 and an overall cap of 30. These are raw setup anchors and not proof that force size follows population, equipment, supply, defections, or sponsorship in all scenarios.

No map inspection, event render, country spawn evaluation, carrier-consumption trace, force-fill probability, or bounded territorial evidence was completed. P06 and all territorial force cases therefore remain unresolved.

Global Jihad launch validity checks include no World End, no duplicate active setup, no setup-in-progress, an eligible scenario selection or manual request, a free country carrier or existing actor, and at least one eligible wave target. Scenario profile setup selects intensity and pattern, but the complete actor, parent, state overlap, capital, force, region-diversity, coalition, and cleanup pool was not returned by MCP.

The Event 14 interaction is source-visible through the `cannibal_clash` incident family and Event 31’s no-ally design requirement, but no strategy-factor or diplomacy adapter evidence proves alliance zero, rivalry dominance, or survival-front preservation.

`random_terror_can_defeat_actor` has source gates for non-final actor loss of territory or authority, final-actor defeat after False Revelation denial, and capitulation. No defeat or surrender sequence evaluation was completed, so cleanup, merger, subordinate handling, and terminal defeat remain unresolved.

## Confirmed exploit and failure risks

1. Immediate threshold crossing can skip the accepted evolution pacing and expose higher evolution pools in the first subsequent global wave.
2. A single threshold pass can resolve all eligible evolution stages, including Evolution IV and Evolution V, instead of staging them over campaign-sensitive intervals.
3. The resolver’s disabled flag names do not match Event Details, so a user-disabled evolution can still be selected by the resolver.
4. Evolution V sets `random_terror_false_revelation_enabled` as part of immediate evolution resolution, while no automatic eligibility scheduler was found for the terminal branch.
5. The False Revelation request flags set by focus or decision acceleration have no observed consumer that reaches the transaction commit helper.
6. Positive raw incident weights for context-invalid families are selected before fallback normalization, which can distort the intended state-conditioned pool and create repetition of the civic fallback.
7. Fixed raw event option values must not be read as a global event probability. The analyzer found the event candidates, but no event-level sampling or firing cadence probability was evaluated.
8. Decision, mission, focus, foreign intervention, coalition, target, and territorial conclusions can suffer dominance, starvation, rank reversal, or repetition, but the required MCP traces are absent and no such risk is asserted as proven.
9. Maximum Global Jihad has no completed sequence evidence for carrier limits, actor removal, cooldown, duplicate prevention, setup rollback, or terminal gate order.
10. Identity-neutrality is supported by reviewed source terms but remains unproven as a paired normalized score until the analyzer can evaluate identical non-identity inputs.

## Owner-action recommendations

These are recommendations for the gameplay owners. None was applied by this audit.

1. Replace the one-call highest-threshold evolution resolver with a campaign-sensitive scheduler that advances one eligible evolution at a time and records the 90, 120, 150, 180, and 210-day timing anchors through explicit state and cadence.
2. Make the resolver consume the shared Event Details flag contract `events_log_disabled_evolution_31_31_N`, while preserving baseline progression when an evolution is disabled and preventing only its dependent content.
3. Add an automatic False Revelation eligibility scheduler that evaluates the existing gate, creates a delayed candidate, consumes a valid transaction, and schedules the terminal event only after the transaction commits.
4. Give the False Revelation request and transaction flags one complete caller and consumer path, and add a lapse path for falling readiness, territory, unity, crisis spread, or restored countries.
5. Filter invalid incident candidates before random-list normalization, or expose a complete context-conditioned pool to the probability adapter, so invalid naval, rail, capital, military, sponsor, corridor, and Event 14 entries do not distort the civic incident distribution.
6. Preserve identity neutrality in target and recruitment logic, and add the paired Muslim/non-Muslim, ethnicity, nationality, refugee, and ordinary-ideology cases as permanent probability regression scenarios.
7. Supply complete candidate pools and external-factor manifests for government decisions, missions, focus routes, target countries, target states, actor routes, intervention, territorial spawning, and coalition strategy before choosing any balance target.
8. Supply the required Maximum scenario sequence manifest with setup order, carrier limits, actor removals, evolution state, intensity, type, cooldowns, terminal gate, and duplicate prevention before using `hoi4.probability_sequence`.
9. After an owner-applied patch, rerun `hoi4.probability_compare` with the same P01-P10, W01-W08, five evolution, actor-route, and paired identity cases. No new balance targets should be selected from this incomplete baseline.

## Skipped analyses, blockers, and uncertainty

The following analyses remain incomplete by explicit route result or by the requested stop: named probability evaluation, threshold and sensitivity sweeps, rank-reversal sweeps, before-and-after or candidate comparison, seeded simulation, custom-pool sequence analysis, probability renders, event render, focus render, map evidence, decision and mission adapter evidence, focus adapter evidence, AI strategy-factor evidence, country spawn evidence, and complete terminal-state evidence.

The exact blockers are recorded in the MCP evidence ledger above. The most consequential blockers are the repeated source-specific `INTERNAL_ERROR`, the focus `SCAN_BYTE_LIMIT`, the global partial event scan with `MCP_INLINE_FILES_TRUNCATED`, and the absence of completed evaluate, sweep, compare, simulate, sequence, and render artifacts.

Source-level observations are exact where they quote a file, identifier, raw weight, trigger, or effect path. They are not exact runtime probabilities. All scenario, identity-pair, score-race, target-choice, recruitment, territorial, coalition, defeat, and terminal timing conclusions that lack a successful MCP trace remain unresolved.

There are no approved fallbacks or simplifications in the gameplay scope. The only deliverable from this audit is this documentation handoff, and no gameplay patch was made.
