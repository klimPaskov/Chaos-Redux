# Event 009 White Peace Probability Audit

Audit date: 2026-10-05.

Status: the read-only source audit and scenario fixture are complete. The MCP probability, structural event, reference-read, and source-lookup calls returned no analysis artifacts because the connected calls timed out after 600 seconds. No exact, bounded, sampled, score-only, or timing result was returned by the probability analyzer. The audit is incomplete for balance sign-off.

## Scope and files

I read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, the three parent-named Event 009 design files, `docs/plans/009_white_peace_plans/subagent_handoffs/009_documentation_curator_2026_10_05.md`, and `docs/plans/009_white_peace_plans/agent_decisions_2026-10-05.md`. I also read the relevant offline wiki pages and installed-game documentation listed below.

| Surface | Source and identifiers | What is being weighted |
| --- | --- | --- |
| Automatic event selection | `common/scripted_effects/chaosx_settings_effects.txt::evaluate_random_event_selection_candidate`, `select_weighted_random_event_id`; `common/scripted_effects/chaosx_logic_effects.txt::get_event_weight`, `evaluate_event_pool_candidate_unavailability`; `common/on_actions/chaosx_on_actions_system.txt` | The shared picker iterates `global.all_events`, rejects invalid candidates, and selects from scaled event weights. Event 9 is registered as repeatable at `chaosx_logic_effects.txt:288`. |
| Event 9 dynamic cap and availability | `common/scripted_effects/009_white_peace_effects.txt::count_white_peace_minor_candidates`, `determine_white_peace_stage`, `count_white_peace_major_candidates`, `calculate_white_peace_dynamic_cap` | The source converts war and candidate pressure, repeatable cap state, stage state, and a recent-broad-settlement flag into the Event 9 cap and availability variables. |
| Stage branch selection | `common/scripted_effects/009_white_peace_effects.txt::select_white_peace_branch` | Three stage-specific `random_list` blocks choose single, multi, major, or broad effects after Event 9 has already been selected. |
| Pair scoring and target selection | `common/scripted_effects/009_white_peace_effects.txt::score_white_peace_pair`, `add_current_white_peace_primary_to_weighted_pool`, `select_weighted_white_peace_primary_candidate`, `add_current_white_peace_partner_to_weighted_pool`, `select_weighted_white_peace_partner_for_current_primary`, `select_white_peace_primary_pair`; `common/scripted_triggers/009_white_peace_triggers.txt` | Pair scores are represented by repeated scope entries and selected with `random_scope_in_array`. Country and pair gates determine which candidates enter those arrays. |
| Forced and automatic entry | `events/009_white_peace.txt::chaosx.nr9.1` | The hidden root is triggered-only. The automatic event system calls it after weighted selection. A forced launch may enter without a prepared pair context. |
| Event options and MTTH | `events/009_white_peace.txt` | No `ai_chance`, `ai_will_do`, `mean_time_to_happen`, or `mtth:` token appears in the Event 009 event, effects, triggers, or constants files. The report events have one acknowledgement option. |

The event pool, event cap, branch list, and target-pair list are separate selection surfaces. The event weight is a raw pool weight. It is not an AI willingness score or an event-option click chance. A complete conditional event chance would require every live `global.all_events` candidate, each candidate’s eligibility and current weight, and the current timer and settings state. The branch lists are conditional on Event 9 already being selected. The pair selector is conditional on the chosen branch and the complete live war-participant pool.

## Named scenarios and declared inputs

The exact scenario set submitted to baseline evaluations, sweeps, and post-patch comparisons is [white_peace_probability_scenarios_2026-10-05.json](white_peace_probability_scenarios_2026-10-05.json), SHA-256 `280C9F2120093E71E0EEDAD002441417DFCF14AA97EBA109911E28B663126AE5`. It contains five stable scenario IDs.

| Scenario ID | Declared world | Pool and external-factor completeness |
| --- | --- | --- |
| `WP009_19360101_FORCED_USA_ITA_ETH_MAJOR_LOCKED` | USA recipient on 1936-01-01; Italy and Ethiopia are the only stated war pair; base stage; Italy major and Ethiopia minor; both independent, faction-free, normal, protected-flag-free, not capitulated, below the surrender threshold, and holding their own capitals. The user reports that the forced launch produced no report and skip reason 3, `major_locked`. | The single war pair is complete as a declared synthetic input. Country relationships, capital control, the event arrays, and other trigger bindings were not resolved by MCP. The global all-event selection pool is explicitly incomplete. The skip reason is a user-supplied observation, not an MCP result. |
| `WP009_19360101_ELIGIBLE_LUX_BEL_MINOR_PAIR` | Synthetic base-stage world with one six-month-old isolated LUX–BEL minor war, home-controlled capitals, no recent memory, and no protection flags. | Complete only as a declared one-pair case. It is not a live campaign observation. The all-event pool is incomplete, and the adapter did not confirm the country-scope and relationship bindings. |
| `WP009_STAGE1_6_WARS_4_SAFE_MINOR_PAIRS` | Synthetic aggregate input with six active wars and four safe minor pairs. | Counts are declared, but no typed roster for those war pairs was supplied. Pair-selection completeness is unresolved, and the global event pool is incomplete. |
| `WP009_STAGE2_10_WARS_6_SAFE_PAIRS_1_MAJOR` | Synthetic aggregate input with ten active wars, six safe minor pairs, and one major candidate. | Counts are declared, but no typed roster or accepted evolution-gate binding was supplied. Pair selection is incomplete and the global event pool is incomplete. |
| `WP009_STAGE3_12_WARS_8_SAFE_PAIRS` | Synthetic aggregate input with twelve active wars, eight safe minor pairs, and one major candidate. | Counts are declared, but no typed roster or accepted evolution-gate binding was supplied. Pair selection is incomplete and the global event pool is incomplete. |

The scenario file was preserved unchanged for possible same-scenario comparison. Its outer shape uses the known `id` and `scenarios` envelope with `actor`, top-level `date`, `state`, `flags`, and `scopes`. The connected tools returned no scenario hash or accepted nested schema. Descriptive fields such as the declared war-pair roster and alias labels must therefore be treated as scenario assumptions, not proof that the adapter bound every Clausewitz trigger or scope. No uncertain-input distribution, seed, scheduled state transition, or cadence was declared.

The current evolution gates read `global.chaos_meter_value` against tier minima 200, 400, and 600 and reject each stage when its matching `events_log_disabled_evolution_9_9_<stage>` global flag is set. The logic is in `common/scripted_triggers/chaosx_settings_triggers.txt::is_current_evolution_enabled` and `has_reached_current_evolution_tier`, with thresholds in `common/script_constants/chaos_meter_constants.txt::chaos_meter_tier_range`. The original five-scenario fixture did not include those gate inputs. The companion [white_peace_probability_evolution_gate_scenarios_2026-10-05.json](white_peace_probability_evolution_gate_scenarios_2026-10-05.json), SHA-256 `0318DB90F063F0E01BB28C8951C883F971AF1B349958A39E8540F8EFC7FEEB99`, preserves the original five scenario objects and adds Stage I–III gate-on cases plus all-disabled, Stage I disabled at a later stage, Stage II disabled with stale unlock history, and Stage III disabled with stale unlock history. These seven cases are a future re-audit fixture only. They were not submitted to MCP, and their aggregate candidate inputs remain incomplete.

## MCP evidence

The valid limited reference-context result identified workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned installed `effects_documentation.md` random-list lines 5413–5432 at revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and offline `Effects - Hearts of Iron 4 Wiki.md` random-effects lines 4504–4571 at revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`. That context response omitted nine sources. A targeted reference search returned the installed random-list and random-scope sections and offline Event Modding sections for triggering, event effects, and on-action integration, but the search response still omitted sixteen results. A higher-limit context request, six targeted `reference_read` calls, a targeted trigger search, and a bounded `source_lookup` retry all timed out after 600 seconds. The first source-lookup request was rejected because `maxDefinitions` exceeded the route limit of 3. I read the relevant local reference files directly and record their local SHA-256 values below. No MCP reference-read artifact is claimed.

| Tool and surface | Request | Result |
| --- | --- | --- |
| `hoi4.probability_inspect` | Adapter `event_mean_time_to_happen`, source `events/009_white_peace.txt`. | `timed out awaiting tools/call after 600s`. No source revision, source hash, artifact, or MTTH adapter result. |
| `hoi4.probability_inspect` | Adapter `custom_weighted_pool`, source `common/scripted_effects/chaosx_settings_effects.txt` and `common/scripted_effects/chaosx_logic_effects.txt`. | Both calls timed out after 600 seconds. The all-event pool and dynamic Event 9 weight were not inspected by MCP. |
| `hoi4.probability_inspect` | Adapters `random_list` and `custom_weighted_pool`, source `common/scripted_effects/009_white_peace_effects.txt`. These were submitted before the owner edits, when the runtime file matched the saved baseline copy. | Both calls timed out after 600 seconds. No candidate list, weight trace, source revision, or artifact. |
| `hoi4.probability_evaluate` | Baseline adapters `random_list` and `custom_weighted_pool`, source `docs/plans/009_white_peace_plans/evidence_2026_10_05/baseline/009_white_peace_effects.txt`, the saved five-scenario set, raw-value and conditional-probability metrics. | Both calls timed out after 600 seconds. No score, ranking, conditional probability, scenario hash, revision, or artifact. |
| `hoi4.probability_sweep` | Baseline adapters `custom_weighted_pool` and `random_list`, the same saved source and scenario set, paths `state.active_war_count`, `state.safe_minor_pair_count`, and `state.white_peace_stage`, five steps, pairwise and rank-reversal search. | Both calls timed out after 600 seconds. No threshold, sensitivity, or rank-reversal output. |
| `hoi4.probability_compare` | Custom-pool compare from the saved baseline effect path to `common/scripted_effects/009_white_peace_effects.txt`, random-list compare on the same paths, and custom-pool compare from the saved baseline trigger path to `common/scripted_triggers/009_white_peace_triggers.txt`. All used the same five-scenario set. | All three calls timed out after 600 seconds. No comparison IDs, source revisions, scenario hashes, artifacts, or numeric deltas. The owner then applied a further evolution-gate change, so the current final source has no returned comparison result. |
| `hoi4.event_inspect` and `hoi4.event_render` | Read-only downstream trace of selector `{kind:"event",eventId:"chaosx.nr9.1"}` and reachability render, before owner edits. | Both timed out after 600 seconds. No graph, render, revision, or artifact. |
| `hoi4.probability_render` | Not called. | No evaluation or comparison returned an `analysisId`, so there was no valid analysis resource to render. |
| `hoi4.probability_simulate` | Not called. | No uncertain-input distribution or seed was declared. |
| `hoi4.probability_sequence` | Not called. | No complete source-linked pool manifest with cadence, transitions, and terminal state was available. |
| Service version and health | Tool catalog checked for HOI4 health/version routes. | No HOI4 service health or version route was exposed. No service-version or health claim is made. |

No MCP artifact URI, probability source revision, scenario hash, comparison ID, or rendered evidence path exists for this audit. The local source hashes below are file receipts, not MCP source revisions.

## Source findings

### Base-stage forced launch and skip reason

In the baseline, `events/009_white_peace.txt::chaosx.nr9.1` is hidden and triggered-only. It calls `prepare_white_peace_runtime_context` when the context or targets are absent, then calls `fire_white_peace_report_event` only when the context is ready and both selected targets exist. The base branch permits only a minor-versus-minor pair. The supplied Italy–Ethiopia case has a safe major–minor relationship but no eligible base-stage minor pair or unlocked major candidate. `count_white_peace_major_candidates` records an otherwise-safe major pair as locked before Stage II, and `calculate_white_peace_dynamic_cap` assigns skip reason `major_locked = 3` when no other eligible pair exists. The baseline forced root can therefore exit without a report, matching the user’s supplied observation.

The baseline already had a `major_locked` availability string for the event/settings detail surface at `common/scripted_localisation/chaosx_scripted_localisation_settings.txt:782-783` and `localisation/english/chaosx_gui_l_english.yml:483`. The hidden forced root did not dispatch that explanation.

The current final owner source now calls `dispatch_white_peace_unavailable_report` for a human recipient when no settlement was applied. It sends `chaosx.nr9.6`, whose scripted localisation selects the explicit `major_locked` explanation. The final trigger source also requires `can_white_peace_conflict_be_isolated`, which rejects either selected participant having an additional enemy country. This narrows the candidate pool to isolated pair conflicts. These are current source observations only. The structural MCP pass timed out, and the current final source was not compared successfully.

The accepted decision record says Stages I and III can still settle several separate isolated wars. It also records that the current branch gates follow the Event Settings evolution contract and that stored unlock flags cannot bypass a disabled stage. `set_white_peace_evolution_gates` checks `is_current_evolution_enabled` for tiers 1, 2, and 3 after resetting the enable flags. `is_current_evolution_enabled` requires both the Chaos tier minimum and the absence of the matching disabled-evolution flag. The original stage scenarios do not fully declare these inputs, so their stage outcomes remain unresolved under the final source.

### Weight, stage, and target mechanics

The exact source tuning values include base environmental cap 125, valid-pair floor 120, environmental maximum 1500, active-war pressure 90 capped at 540, safe-minor-pair pressure 85 capped at 595, minor-only-pair pressure 60 capped at 240, and clutter steps 125, 175, and 225. Stage multipliers are 0.78, 0.55, and 0.38. Branch weights are 100 for the base single branch, 70/30 for Stage I, 60/25/15 for Stage II, and 50/25/15/10 for Stage III. These are source constants, not measured scenario scores or probabilities.

The dynamic cap reads the repeatable event cap divided by the default event weight, applies the stage multiplier and recent-broad penalty, rounds, then clamps the result to at least 120. That final lower clamp can flatten the intended repeat-decay or evolution reduction at low pre-clamp values. This is a source-level sensitivity concern. The required sweep did not return, so its effect on live event selection is unresolved.

The active-war proxy counts normal war countries after excluding special, nonhuman, and explicitly protected actors. Other participants who fail the target trigger because they are subjects, in civil war, near capitulation, recently settled, or faction members can still contribute to the active-war proxy. A safe pair is separately required for availability. This means ineligible wars may raise the environmental cap when another safe pair exists. This is a source-level pressure concern, not a measured rank reversal or balance finding.

Pair scoring adds the configured factors for minor status, no-major-war context, war age, independence, faction status, and safe capitals, with a major penalty and a minimum floor. The selection code appends each primary and partner scope once per score point, then picks a random scope from the array. This is a custom weighted sampler, not an AI willingness score or an engine `random_list`.

The saved baseline did not isolate each conflict, so a primary with many eligible enemies could have accumulated enough repeated entries to reach the engine’s 1000-iteration loop limit. The current final trigger restricts each primary to one isolated eligible enemy. The parent’s final-source review bounds that one-pair score at 150, so the baseline saturation concern does not apply to the current isolated-pair source. This is a source-level bound, not a measured probability or ranking. No normalized pair share, starvation, or dominance result was returned.

The country and pair gates require existence, normal civilian systems, active war, controlled states, surrender progress below 0.50, safe capital control, no capitulation, civil war, subject status, faction membership, special/nonhuman role, protection flags, recent-country memory, recent pair memory, direct belligerency, and stage-appropriate minor or major status. The final owner gate additionally requires the conflict to be isolated. The scenario adapter did not prove any of these external scope predicates.

### AI validity, repetition, and effect-cost alignment

Event 9 has no AI acceptance race. Each displayed report has one acknowledgement option, and the source contains no Event 009 `ai_chance`, `ai_will_do`, or MTTH entry. AI outcomes depend on eligibility, target scoring, the branch random list, and the shared automatic event pool.

Source memory durations are 180 days for recent-country protection, 360 days for recent-pair memory, 540 days for recent major-country memory, and 720 days for recent broad settlement. The event is repeatable and relies on the shared event timer, recovered weight, and repeatable cap. A complete cadence/state-transition manifest was not declared, so no sequence or repetition probability was measured.

Source effect constants set Chaos reductions to -1 for one minor pair, a cap of -3 for multi-minor settlement, -2 for a major settlement, and a broad cap of -3. The source establishes those values, but the MCP calls returned no cause-versus-cost, repeat-firing, exploit-risk, or dominance evidence. No balance sign-off is made.

## Concrete owner recommendations

- Keep the invalid forced-entry path explicit. The current source dispatches the localized unavailable report; confirm that the report reaches the forced-event recipient in the live session.
- Run the same five named scenarios through `probability_inspect`, `probability_evaluate`, and `probability_sweep` after the adapter becomes reachable. Include the current `is_current_evolution_enabled` tier gates and the isolated-war candidate closure in any typed scenario data the accepted schema supports.
- Re-run `probability_compare` against the saved baseline paths and the current final paths using the same scenario set. The current final evolution-gate and isolated-conflict edits have no returned comparison result.
- Sweep the 120-point post-multiplier floor, eligible versus ineligible war pressure, and current evolution gates before changing any tuning constants. The isolated-pair gate removes the baseline multi-enemy path that could have reached the 1000-ticket construction limit. Recheck that bound if future source changes permit more than one eligible enemy per primary.
- Keep the global `all_events` candidate pool incomplete in the report until every event candidate, weight, validity gate, timer filter, and external setting is represented. Do not claim an exact automatic event chance from Event 9’s weight alone.

No source or tuning change was applied by this auditor. No selected target was calculated by hand in place of the MCP analyzer.

## Reference citations and local revisions

The offline references were read directly because the MCP `reference_read` route timed out. Their local SHA-256 values identify the files reviewed in this workspace.

| Reference | Sections read | Local revision |
| --- | --- | --- |
| `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` | Triggering 117–150, event effect firing 192–229, `ai_chance` and event-option guidance 159–177, on-action integration 703–852. | `96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D` |
| `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md` | MTTH, `ai_will_do` score-race, and `ai_chance` proportional choice distinctions at 25–45. | `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | Random effects and `random_list` weights at 4504–4571. | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | `random_scope_in_array` and loop limits around 1218–1225. | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | `is_major`, war, faction, subject, surrender-progress, war-length, and capital-controller trigger entries. | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| Installed `documentation/effects_documentation.md` | `country_event` 2943–2959, `random_list` 5413–5432, and `random_scope_in_array` 5558–5573. | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Installed `documentation/triggers_documentation.md` | War 5024–5060, capital control 5381, faction 5686–5695, major 5881, subject 6276, surrender 7640, and war-length 7704–7711. | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |

The limited MCP context returned installed `random_list` source ID `443f582ff7608109d67f72cd410f3008aa3175f6e1a1463b51644545d0927a89`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and the offline `Effects` section at revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`. The targeted reference search returned additional source IDs for `random_scope_in_array` and Event Modding. Their `reference_read` calls timed out, so no detailed MCP reference-read evidence is claimed.

## Source snapshot receipts and remaining uncertainty

The owner-preserved baseline files are under `docs/plans/009_white_peace_plans/evidence_2026_10_05/baseline/`. Their SHA-256 values are:

| Baseline path | SHA-256 |
| --- | --- |
| `009_white_peace.txt` | `FA594B92D0F19F8E2FB548FA3B31F4916C5AF7D8AEABABC01203E62216838A25` |
| `009_white_peace_effects.txt` | `B210CB1CB5F7110DBD6DF3C44FF2FE8D1A74AE16E37EB1851DEC9DDC58468094` |
| `009_white_peace_triggers.txt` | `3B894E5A8958829FAB81D2F1DB0897904E7DB6717CED39B979908B88E8DD3130` |
| `009_white_peace_constants.txt` | `B05FA7363D842CC61A54DCAFB012B6BBADFE428F67E9107B553663FEFE6B5903` |

The final stage gate also depends on these shared source files, read after the owner follow-up:

| Gate source | Relevant identifiers | SHA-256 |
| --- | --- | --- |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | `has_disabled_current_evolution`, `is_current_evolution_enabled`, `has_reached_current_evolution_tier`, lines 38–81. | `9942DC608ADB7285F3856D2B5DC0BAF3FE2E3FCAF0232A0D54CD168F1B4D1989` |
| `common/script_constants/chaos_meter_constants.txt` | `chaos_meter_tier_range.tier_1.min`, `tier_2.min`, and `tier_3.min`, lines 20–22. | `3AFC88033DE79F3ABB0D173C82AAEF6130FBF0846CD012A575CA00B73BDE1B4A` |

The first post-patch source state used in compare requests had hashes `72932A503DF518F019474EC859ECFF08CA22117E1F1B5041CD1253503B5AC4DF` for the event file, `F6B0295595FF90B5945CE69B12ECE122087F718437043B40305D5D093CFD3622` for effects, and `04F5359539E65E5A01C2EC87AD5E07151CC3B121D8278EA7FEE3B8ED8D8CBFE9` for triggers. Those compare requests produced no result. The owner subsequently made the evolution-gate change, so the current final source is newer than that attempted comparison.

Current final SHA-256 values are `E1D284F8BE3FAB8E1083FC6A0F0ED573E48A64BE54D6D86468F7F40BAE74B1FB` for `events/009_white_peace.txt`, `3F270AF72823F6E44C48CEF860A738138E2A64AF8E2443784EED797271C6E2E3` for `common/scripted_effects/009_white_peace_effects.txt`, `1EFC4A398A478233BE2EA589BF0926602A96D78C6A544A4A5B527AB0FF5B1564` for `common/scripted_triggers/009_white_peace_triggers.txt`, and `EA135B39035057E6D9B211005C024FC0EA14146C23C83398E561E28ECE186409` for `common/script_constants/009_white_peace_constants.txt`. The constants diff removes the non-weight achievement field `white_peace_achievement.broad_pairs_required`; the weight, cap, stage, and branch tuning values are unchanged in the current diff.

The current final effects source clears the three evolution-enable flags during context reset, recomputes them through `is_current_evolution_enabled`, requires matching enable gates for stored stage flags and pressure thresholds, and zeroes the related branch weights when a gate is disabled. This behavior was read after the comparison calls timed out. The original preserved scenario set does not establish the helper’s internal tier bindings, so those stage cases remain incomplete even as declared inputs. The companion gate fixture adds the source-backed tier and disabled-flag cases, but it has no MCP evaluation or comparison result.

No MCP probability result proves event-weight ranking, normalized selection chance, branch shares, pair shares, timing, repeat starvation, dominance, rank reversal, or exploit safety. The user-supplied forced-event observation is the only live result in scope. No live game was launched, no user logs were requested, and this auditor made no gameplay or source edits. Only the scenario fixture and this handoff were created by this auditor.

