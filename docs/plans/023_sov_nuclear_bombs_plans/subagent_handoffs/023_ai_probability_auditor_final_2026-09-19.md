# Event 23 AI and probability auditor handoff

Audit date: 2026-09-19.

Role: chaosx_ai_probability_auditor.

Status: read-only audit complete for the current weighted surfaces, with campaign-level conclusions unresolved wherever the MCP adapter could not bind the required nested Clausewitz state.

No gameplay, AI, event, decision, mission, trigger, effect, constant, localisation, or runtime file was edited by this audit.

## Scope and provenance

The audited repository was C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.

The audit covered the relevant Event 23 specifications, the current constants, MTTH entries, events, decisions and missions, scripted triggers and effects, on actions, the decision map, and the three previous AI probability handoffs.

The offline Paradox wiki snapshot and the installed vanilla documentation under C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation were consulted for weighted event options, MTTH, decisions and missions, scopes, variables, event targets, random lists, and AI willingness semantics.

The relevant repository skills used were chaos-redux-subagents, chaos-redux-events, chaos-redux-mtth, chaos-redux-decisions-missions, and chaos-redux-event-planning.

At audit completion, these Event 23 gameplay files were already modified in the shared worktree and were not authored by this audit: common/decisions/023_sov_nuclear_bombs_decisions.txt, common/script_constants/023_sov_nuclear_bombs_constants.txt, common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt, common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt, common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt, and events/023_soviet_nukes.txt.

The pre-existing Event 23 worktree delta was 280 insertions and 42 removals across those six files, so this handoff pins evidence to the current working-tree snapshot rather than treating the previous handoff revisions as current.

## Current source inventory

The following local SHA-256 values and line counts were captured from the current working tree at the end of the audit.

| Source file | Lines | Bytes | Local SHA-256 |
| --- | ---: | ---: | --- |
| common/script_constants/023_sov_nuclear_bombs_constants.txt | 612 | 12882 | 87EE45C6DE751F4E4D4A9E0354853BFB92676CE0C93DC880FA6797BB5FB0F030 |
| common/mtth/023_sov_nuclear_bombs_mtth.txt | 46 | 4088 | DCB60B1AE6F08C09B0E3D22E9E2442432EB424E3ED2BB103517F0DF3BBD1DE09 |
| events/023_soviet_nukes.txt | 533 | 21593 | 199883D4CBC129505CC2A8AFCF1F6FA6BACC03E0BF6FB621F40EC8BB376F0296 |
| common/decisions/023_sov_nuclear_bombs_decisions.txt | 1378 | 108201 | 2162528AF73639C71F076F6B29B39C2657003D84DA671D23B568103244772DF2 |
| common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt | 2974 | 153517 | 024F58FC1680E1FC60AD893DF22476AF1CB55CF406AD9AAD463DBEB182F08D22 |
| common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt | 1673 | 97160 | 9146D8F6BE3FD59206874077210E83F56554FBB339FC524179241CDAD88ECB9A |
| common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt | 1042 | 46044 | 3F0E4BEF6A7503FC1208CD9FAB5A8A438B9EB23A3F1041B327EE1150722AAD29 |
| common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt | 317 | 18103 | 3D13AA513F4DAD3DD82E6372509E6F86F401BB1B0EBBC86DD3977D0FE906F319 |
| common/on_actions/023_sov_nuclear_bombs_on_actions.txt | 169 | 6296 | 4AD96A8F3BA51610924DC350782B4F82FDE28AEE04DE311774C0A0DCE22A60AF |
| common/decisions/categories/023_sov_nuclear_bombs_categories.txt | 19 | 849 | 73E522E12687D2E0D0C62450806930E0BED033F08EA0F827E55E5E9E4882F011 |

## MCP adapter discovery

All weighted-surface work began with hoi4.probability_inspect.

The source-less opening probe returned MCP error -32602 because the adapter requires a source; the source-bound discovery immediately succeeded and no conclusion was based on the failed probe.

Current source-bound discovery results were:

| Surface | Adapter | Discovery result | Artifact URI | MCP source revision | MCP source hash |
| --- | --- | --- | --- | --- | --- |
| Event 23 event options, with the six coercion candidates supplied | event_option_ai_chance | 32 available candidates, six supplied candidates matched | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b01628da6763149f2d5661efbfb0ba8b47a3a8e13c8bf09e66e8298b42ca1c12/d13c9e93d2c55d9ba79caf1d632a5a4af4c24ffd204ababf2f5c1653866a3daf/probability-inspect-d6ee9bbed985.json | 00446e3ecc5f33ccfcc4392cd88b25007296f7ed05bca863a47b36cd46013e65 | d6ee9bbed9850c7e069b589b6964c81f7c254e14ea8641a7f8d88418f7915b11 |
| Event 23 decisions and missions | mission_ai_will_do | 81 available candidates, full source candidate pool matched | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67a37fa297bd4c323a23fd515ccfbce55ebe9b5040919864649c6951cf2bb5f1/a6059e71e41f241c4ba83b3e6423dffdbd87bfb1f898d7d8dda2ae9f6aa15711/probability-inspect-ab318c242dc6.json | c18dfc2c72ad7451730cba87f4b20072ca086b02e864f7ea1d3397fd18a49e90 | 99cf9964015debe87eb5e86b8e45aea19e0d0ecc38ee9ef14d57b3fb91da93c1 |
| Event 23 test random_list | random_list | three available entries, three supplied entries matched | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/92a5ae7d1af1cb2da3e88924c8fc1d4d0d8a008c030ed7e29cd2361cd6c9a45e/37c9d58d54f1769e82f1cb0b59181790d83508839e9d185167c05ea128da14c2/probability-inspect-225efb1424e1.json | 4d18fe68daaed6b694382d4f48d995327c06a0c7f545fd2a96d72f011b132411 | 225efb1424e1d0490a7871a4bceeffa3b5ed9f77c8dd469876ccf94700a15452 |
| Event 23 evolution MTTH | event_mean_time_to_happen | no indexed candidates and no available MTTH adapter | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efa1daf683e9b03185a41678a5ea3400a5d834f6ba712fd3656a1dc23cdb572b/a69ef1d0b2046f53fd7245d50d365c6be0e7a296fde16a1298a55f53adbcccc9/probability-inspect-89b364cff8d7.json | 4d18fe68daaed6b694382d4f48d995327c06a0c7f545fd2a96d72f011b132411 | 89b364cff8d70ba8114832f89e206c5a9f69ec8c28635880207ea785515f596c |
| Event 23 AI strategy factor candidate | ai_strategy_factor | no candidates and no available AI strategy adapter for the requested source | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/968d02b48b53400e04ff1ef89bb155646f07872278b7c6f380805d709a4801ae/c70b14f15887d078a61a7487132457eca194175e76cf19e24ee995298c465f0c/probability-inspect-805834e62664.json | 5e8b78423498fff93939e43bf5557ebb148151e903335b4a3aa8fefaac3b2f94 | 805834e62664744fbd660b99f7e343af4742244676db7673abe3224a905a654e |

The random_list adapter verified Operation Postern 1.19.2.0 (d245) and the observed launcher version was Operation Postern v1.19.2.0.a729 (d245).

## Candidate pools and fixture completeness

The Event 23 event-option source has multiple independent categorical pools, so the 32 discovered options were not treated as one global normalized race.

The doctrine pool was complete at four candidates: chaosx.nr23.2.party, chaosx.nr23.2.military, chaosx.nr23.2.scientific_safety, and chaosx.nr23.2.dispersed_commands.

The phase-navigation pool was complete at six candidates: chaosx.nr23.100.a, chaosx.nr23.100.custody, chaosx.nr23.100.production, chaosx.nr23.100.test, chaosx.nr23.100.coercion, and chaosx.nr23.100.retaliation.

The coercion response pool was complete at six candidates: chaosx.nr23.120.a, chaosx.nr23.120.b, chaosx.nr23.120.c, chaosx.nr23.120.refuse, chaosx.nr23.120.e, and chaosx.nr23.120.f.

The stand-down response pool was complete at two candidates: chaosx.nr23.163.a and chaosx.nr23.163.b.

The Event 23 test random_list pool was complete at three entries: common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:765.entry.1, common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:765.entry.2, and common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:765.entry.3.

The mission adapter request supplied all 81 candidates exposed by the current inspector.

The 12 target-aware score subset was complete as a requested subset, but it was not a complete global state-target selection pool.

Every scenario used state: {} and flags: [] because the accepted MCP scenario schema does not bind the required ROOT, THIS, PREV, FROM, saved event targets, country/state scopes, country variables, global variables, technologies, wars, ownership, controller, fuel, airbase, distance, and faction relations from the Event 23 source.

The named below, at, and above receipt cases and target delivery cases therefore name the intended state but do not claim that the nested values were applied by the adapter.

## Source constants and structural gates

The current evolution thresholds are chaos I 400, chaos II 600, chaos III 800, chaos IV 1000, major_exchange_chaos 800, first_use_chaos 1000, first_use_min_strategic_loss 3, and world_gate_major_count 2 in common/script_constants/023_sov_nuclear_bombs_constants.txt:28-40.

The current AI constants are doctrine 1.00, doctrine_reform 0.35, doctrine_reform_option 0.25, command 1.00, collapse 1.00, demonstration 0.80, moratorium 0.90, wartime_factor 1.25, severe_loss_factor 1.50, restraint_factor 1.35, capital_target_factor 1.80, air_base_target_factor 1.35, industrial_target_factor 1.25, assigned_site_factor 1.55, transferred_custody_factor 1.75, reactor_site_factor 1.45, major_target_factor 2.00, remote_site_factor 1.20, standdown_acceptance 0.70, and standdown_refusal 0.30 in common/script_constants/023_sov_nuclear_bombs_constants.txt:237-259.

The test random-list weights are 70, 20, and 10 in common/script_constants/023_sov_nuclear_bombs_constants.txt:301-303.

The evolution MTTH source bases are 180, 240, 300, and 360 days for Evolutions I-IV in common/script_constants/023_sov_nuclear_bombs_constants.txt:477-480.

The current MTTH factors include public acceleration 0.75, serious-crisis acceleration 0.65, war acceleration 0.85, major-exchange acceleration 0.60, collapse acceleration 0.70, low-integrity delay 1.35, moratorium delay 1.50, reciprocal-restraint delay 1.25, and stable-command delay 1.10 in common/script_constants/023_sov_nuclear_bombs_constants.txt:489-497.

The delivery route requires atomic_research, nukes, strategic_bomber1 or the By Blood Alone large-airframe route, more than zero deployed strategic bombers, fuel at least 1000, and an owned controlled airbase with level above the configured floor in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:67-101.

The exact state delivery endpoint revalidates the owner or controller, impassable status, the launcher route, an owned controlled airbase, and distance strictly less than 1000 in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:104-132.

Because fuel uses NOT = { has_fuel < 1000 }, fuel exactly 1000 is accepted by the source gate, while distance exactly 1000 fails the strict distance < 1000 check.

The major-exchange receipt threshold is 2 in common/script_constants/023_sov_nuclear_bombs_constants.txt:431.

The source receipt recorder stores actor and target IDs for the first pair, increments to two only when the candidate pair differs in actor or target, and calls sov_nuclear_bombs_open_major_exchange only for the second distinct ordered pair in common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:119-174.

The receipt gate then requires Evolution III, chaos at least 800, major detonation confirmation, major exchange active, receipt count at least 2, and another nuclear major in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:302-324.

The broader major-exchange world gate can open on the first confirmed major receipt or confirmed enemy nuclear use, while the nonterminal exchange super-event requires the second distinct pair.

The severe first-use source gate requires Evolution IV, chaos at least 1000, war, strategic losses at least 3, capital threat, front collapse, reserve exhaustion, enemy use or verified launch preparation, no atomic moratorium, no Soviet major-first-use flag, a delivery route, readiness at least 75, integrity at least 20, and a nuclear-major action target in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:347-368.

The prepared-strike chain separately rejects release_orders_suspended in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:772-793, but the severe_first_use_gate itself does not test release_orders_suspended.

The limited-strike validity helper allows Evolution II and a non-major target with readiness at least 25, integrity at least 40, an exact selected-state route, a valid command target, and war with the target in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:718-732.

The major-strike validity helper requires Evolution III, an exact selected-state route, readiness at least 25, integrity at least 20, and a valid nuclear-major target in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:734-746.

The breakaway delivery helper requires a selected registered state, a non-Soviet holder with atomic_research and nukes, the holder delivery route, and exact endpoint access in common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:953-968.

## Current probability evaluations

### Test random_list: exact conditional result

Analysis ID: probability-9e4a9b1c3382ca78d5599cb3.

Source revision: 4d18fe68daaed6b694382d4f48d995327c06a0c7f545fd2a96d72f011b132411.

Source hash: 225efb1424e1d0490a7871a4bceeffa3b5ed9f77c8dd469876ccf94700a15452.

Scenario hash: c34ee2621ae2bd295a71ad4b3a777b47dda3c7b86a1d62c0554643d164d875b3.

JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9bddcaf53251266010670102fabb6aef049ac373218779f0995e24b08e84905f/a1aa2c0db8bfb16d821e49fbfccc57f96d6c6379d46350956e81fb39a50b7c44/probability-9e4a9b1c3382ca78d5599cb3.json.

Rendered ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af71acf116153e31df61d9adf5066284e957808d14a84042b1c5d921b0d37541/5343567c501eb71bed8e4cc999d1d1bae9a8c5601beea86489d71e909cd28430/probability-probability-9e4a9b1c3382ca78d5599cb3-ranking.svg.

Rendered matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e849f4369628b753056fa802b56302976ea37669fed3e9192c639ef5550e4530/ead85bc454ea7187a38a3f0d5283106d8a54067f02b3bb23777c8ae27bc2b941/probability-probability-9e4a9b1c3382ca78d5599cb3-matrix.svg.

Rendered unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/4b5836f0d89928db5d686a0e6113896efad67176bafa5b9e5a6eaab569dfe59a/probability-probability-9e4a9b1c3382ca78d5599cb3-unresolved.svg.

For every one of P23_TEST_PROOF_SECURE, P23_TEST_CONCEALED_WEAK_COMMAND, P23_TEST_PUBLIC_PREPARED, and P23_TEST_INVALID_SITE, the complete three-entry pool was eligible and the exact conditional values were 70/100 = 0.7, 20/100 = 0.2, and 10/100 = 0.1.

Classification: exact conditional probability for the random_list execution only.

The invalid-site scenario still produces 70/20/10 because the supplied random_list source does not include the outer test-site availability chain; no overall probability of reaching the roll or accepting the site is claimed.

### Doctrine event options

Analysis ID: probability-c248374c5587a83dbe567707.

Source revision: 56cf63bbd7b20127ce95b2f9e2e235dec1b3e51125d6498bd5b3dfd596606e37.

Source hash: d6ee9bbed9850c7e069b589b6964c81f7c254e14ea8641a7f8d88418f7915b11.

Scenario hash: 1ddcffb81f6f475362834d83dfe28e365ba5df3cb4026cc649e1cca38f6d5d23.

The four-option pool was evaluated over P23_BASELINE_EVOLUTION_ENABLED, P23_BASELINE_EVOLUTION_DISABLED, P23_FIRST_USE_TIER_800_BLOCKED, P23_FIRST_USE_TIER_1000_STABLE_BLOCKED, and P23_FIRST_USE_TIER_1000_SEVERE_RARE.

The result was PROBABILITY_ANALYZED_PARTIAL with 20 candidate rows, four unresolved rows, and one diagnostic stating that the scientific-safety test-failure modifier was not active in any supplied scenario.

Rendered ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19ea09a74a7640c35ef1b5c536b7068fff3d7b685822a9541e54a9d1d3bb8e58/bf48cc2e993b604fc5335aadb54b7a62d9b3cd135c2346af112bfdd2f982da11/probability-probability-c248374c5587a83dbe567707-ranking.svg.

Rendered matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eed2486517104926769bf0da648f5e016917e0d2360f0997585a6c5dbcdc919b/9b276b3b8b351ab01ad1df38b541739b134fcd89aeafabf238495f0db0bd787e/probability-probability-c248374c5587a83dbe567707-matrix.svg.

Rendered unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aecc785a69f86b0866200b6854aa7e2f195b89289ba59fd4d63f8c7c8d6d0283/16a5638081e80c260defa9001b3518d17a9df6b16272764cf68e17fac4915097/probability-probability-c248374c5587a83dbe567707-unresolved.svg.

Classification: bounded score and partial normalized result only; the four unresolved rows prevent an exact doctrine-choice probability.

### Phase navigation options and disabled evolution cases

Analysis ID: probability-791bdf395f0a439d8cc125e1.

Source revision: 9d192e1b8954490a4c990364a1f99f357696ed80fa78e3883875b2dfc3730c3c.

Source hash: d6ee9bbed9850c7e069b589b6964c81f7c254e14ea8641a7f8d88418f7915b11.

Scenario hash: bbfb6bbabccc624b49c35b27dc94793099017de522c92a41114396380dd01e05.

The six-option pool was evaluated over P23_BASELINE_EVOLUTION_ENABLED, P23_BASELINE_EVOLUTION_DISABLED, P23_COERCE_MINOR_MAJOR_EXCLUSION, P23_COERCE_MAJOR_TARGET_EXCLUSION, P23_FIRST_USE_STANDDOWN_BLOCKED, P23_MAJOR_EXCHANGE_RECEIPT_BELOW, P23_MAJOR_EXCHANGE_RECEIPT_AT, and P23_MAJOR_EXCHANGE_RECEIPT_ABOVE.

The result was PROBABILITY_ANALYZED_PARTIAL with 48 candidate rows, 11 unresolved rows, and 14 diagnostics.

The adapter reported chaosx.nr23.100.a as dominant in all eight supplied fixtures and reported the other five navigation options as never eligible in the empty fixtures.

This is not a campaign-level dominance result because the navigation options are gated by phase and nested flags that were not bound; it is evidence that the adapter cannot prove those gates or a fallback from the supplied fixtures.

Rendered ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d0baefcd5456b9765ec10e8122506c8a16ac10444966a7d81ef428f61ab7071/74feb00c7e932e77d5ac21c11756ec78d0534e8aec8deddf38723162b62e9f6e/probability-probability-791bdf395f0a439d8cc125e1-ranking.svg.

Rendered matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5bcd5cbd56c368023163cb094cd123a5ad6b8fd26dc76eae3e4a0e91121da51/71a7fc9ae5a86f86e7805203501019df2b9e8a0542a4713e267d039ad72f853f/probability-probability-791bdf395f0a439d8cc125e1-matrix.svg.

Rendered unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64d36262728efe127b192d366e250c18fba46c8902499919947810acb9a8d508/bbe3a6fbc6f588f5032a42ce8d086fd6deefb041b0aa49c35c1b672a46387a75/probability-probability-791bdf395f0a439d8cc125e1-unresolved.svg.

Classification: bounded partial event-option result; no disabled-evolution probability is proven.

### Coercion response options, including minor and major exclusions

Analysis ID: probability-c69b7cd84aca8e79193c078c.

Source revision: 2a7f2e00ce76706beb5c16fb1fe9c899ef57d2e6afbd9768198b5e455b34845b.

Source hash: d6ee9bbed9850c7e069b589b6964c81f7c254e14ea8641a7f8d88418f7915b11.

Scenario hash: 6966ef3a966028bb9219da34e4a09d9d238ebad91d0267587cf24bd2b15fb305.

The complete six-option pool was evaluated over P23_COERCE_ISOLATED_LOSING_MINOR, P23_COERCE_PROTECTED_STABLE_MINOR, P23_COERCE_UNTESTED_SECRET, P23_COERCE_EMPTY_THREATS, P23_COERCE_MINOR_MAJOR_EXCLUSION, and P23_COERCE_MAJOR_TARGET_EXCLUSION.

The source bases are 35 for accepted, 25 for partial, 20 for delayed, 20 for refusal, 10 for exposed, and 10 for foreign support at events/023_soviet_nukes.txt:257-316.

The result was PROBABILITY_ANALYZED_PARTIAL with 36 candidate rows, 33 unresolved rows, and 14 diagnostics.

The diagnostics include EVENT_OPTION_FALLBACK_NOT_PROVEN, every coercion option never eligible across the six empty fixtures, and chaosx.nr23.120.a reported as dominant across all six supplied fixtures.

Classification: unresolved and not a normalized coercion probability.

The positive source bases are not a click probability because option triggers, target validity, war relation, demand state, faction relation, settlement state, and event-target response validity are incomplete in the fixture.

Rendered ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8b9e8bc8e3aaf862582dcb1ae02cd9c7a4c8c431f691bc819d63ccf10c47c3a/de4bd93ef522716b88f065252641a75ae90466727f4b0f895090cd0cd7896eb3/probability-probability-c69b7cd84aca8e79193c078c-ranking.svg.

Rendered matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/926942e73648ce228354ee2f5a4d6d58e0f7509b8738cc374ae86701068043b1/f5547c75c8e702269bdbee807ab14d62778a3954e75f01a517e1ca60fe36525f/probability-probability-c69b7cd84aca8e79193c078c-matrix.svg.

Rendered unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/add4491edfe1ab803237226f587f18ced2c89c770be5e9d8cb56be2edc3f4a19/1836d9fef4be8a39c121fcc066eb3cd5cd36b37ffc98e08206b70415728538ef/probability-probability-c69b7cd84aca8e79193c078c-unresolved.svg.

### Stand-down response

Analysis ID: probability-7b58ef44253030e9a889e3a0.

Source revision: 9d192e1b8954490a4c990364a1f99f357696ed80fa78e3883875b2dfc3730c3c.

Source hash: d6ee9bbed9850c7e069b589b6964c81f7c254e14ea8641a7f8d88418f7915b11.

Scenario hash: 4200099cdff9b6043a8ebfffed9104c573e120224775a630779484cfb4adc531.

The two-option pool was evaluated over P23_FIRST_USE_STANDDOWN_BLOCKED, P23_MAJOR_EXCHANGE_RECEIPT_BELOW, P23_MAJOR_EXCHANGE_RECEIPT_AT, and P23_MAJOR_EXCHANGE_RECEIPT_ABOVE.

The source bases are constant:sov_nuclear_bombs_ai.standdown_acceptance, currently 0.70, and constant:sov_nuclear_bombs_ai.standdown_refusal, currently 0.30, in events/023_soviet_nukes.txt:464-480.

The result was PROBABILITY_ANALYZED_PARTIAL with eight rows and one unresolved item.

Classification: bounded partial option score only; nested standdown actor, hotline, nonce, and release-order state prevent an exact response probability.

### First-use authorization scenarios

Analysis ID: probability-eb4cfa2c0acec21a09929966.

Source revision: 02a4516a479653ea44ca8aa0b0af1a70ec9feccb80bb5436fede7080fbd41a2e.

Source hash: ab318c242dc6cc7618b18117c5910cdec86be7754679f44164a6d1ee2cd4c0a0.

Scenario hash: 3bc54bae0a84b2ef96d718dc1c8fe6bd51a9e9a4dd66da9331d83c77de57ca8e.

The singleton candidate sov_nuclear_bombs_give_final_authorization was evaluated over P23_FIRST_USE_TIER_800_BLOCKED, P23_FIRST_USE_TIER_1000_STABLE_BLOCKED, P23_FIRST_USE_TIER_1000_SEVERE_RARE, and P23_FIRST_USE_STANDDOWN_BLOCKED.

The source score is base 0.10, multiplied by severe_loss_factor 1.50 only when event_can_authorize_first_use is true, and multiplied by 0.00 before Evolution III in common/decisions/023_sov_nuclear_bombs_decisions.txt:613-625.

The result was PROBABILITY_ANALYZED_PARTIAL with four rows and 12 unresolved items, including the severe-loss modifier not being active in any empty fixture.

Classification: score-only and unresolved, not a first-use probability or timing distribution.

Rendered unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93b91d865e6d8bf7c998e1139803dd82a995bd14a88ebbd5d64fda233daafa6a/e2d13a13a338782dfadad442e5a979b1acf7260ec993ec25aa18819f5004ad85/probability-probability-eb4cfa2c0acec21a09929966-unresolved.svg.

### Breakaway route stages

Analysis ID: probability-6745fcda8b0a5d2dc572268a.

Source revision: 02a4516a479653ea44ca8aa0b0af1a70ec9feccb80bb5436fede7080fbd41a2e.

Source hash: ab318c242dc6cc7618b18117c5910cdec86be7754679f44164a6d1ee2cd4c0a0.

Scenario hash: 01d9d97a40945c8f9c86dafaaa9b09f2bd97dc6ebfba55fe84ecb7f5cc3d0ed1.

The three-stage pool was evaluated over P23_BREAKAWAY_CUSTODY_STAGE, P23_BREAKAWAY_TECHNICAL_STAGE, P23_BREAKAWAY_COMMAND_STAGE, P23_BREAKAWAY_DELIVERY_STAGE, P23_BREAKAWAY_OPERATIONAL_STAGE, and P23_BREAKAWAY_RETURN_STAGE.

The source candidates are sov_nuclear_bombs_breakaway_technical_access_mission, sov_nuclear_bombs_breakaway_command_formation_mission, and sov_nuclear_bombs_breakaway_delivery_integration_mission.

The result was PROBABILITY_ANALYZED with 18 rows, zero unresolved items, and three never-eligible diagnostics because all three definitions intentionally declare available = { always = no }.

The source timeout values are 180, 240, and 180 days and the source AI score is 0.20 for each stage in common/decisions/023_sov_nuclear_bombs_decisions.txt:1293-1342.

Classification: exact source score and never-eligible mission status under the supplied adapter model, but not a selection probability, timing distribution, or sequence result.

Rendered ranking SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35b7519b08619df6380fd6e38bc6c4e044f7bd4340c56cf0af5c3c6b15d01473/dacbca652849b314073f9effc31e78bc4e9f2f1e4bc8ecc1fb66f6e5f2790503/probability-probability-6745fcda8b0a5d2dc572268a-ranking.svg.

Rendered matrix SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dea7d5751dc648ee5496372b4c308343105bb2df6c58faf24a0f16cf4fdb5809/2ee10a14e8be2eb5c9ff8e9a0a68f273292738889dee39ecef5e2452b94ccf65/probability-probability-6745fcda8b0a5d2dc572268a-matrix.svg.

### Target and site delivery feasibility

Analysis ID: probability-4f52e72b81d39eadfe6c9ca6.

Source revision: c9dafc0932de72656039c206dd2ab5a3d2a25308b46293e0c21355861b7cd3e5.

Source hash: ab318c242dc6cc7618b18117c5910cdec86be7754679f44164a6d1ee2cd4c0a0.

Scenario hash: bc4b6dd3d60198213f65e238b3376de5c7c1a74940cecf6f223db7ba60190481.

The 12-candidate requested target subset was evaluated over P23_TARGET_WARTIME_REAL_DISPUTE, P23_TARGET_MAJOR_EXCLUSION, P23_TARGET_BREAKAWAY_CUSTODY, P23_TARGET_SITE_ROUTE_FUEL_BELOW, P23_TARGET_SITE_ROUTE_FUEL_AT, P23_TARGET_SITE_ROUTE_DISTANCE_ABOVE, and P23_TARGET_SITE_VALID.

The result was PROBABILITY_ANALYZED_PARTIAL with 84 rows, 32 unresolved items, and two modifier diagnostics.

Classification: unresolved target score race; the subset is complete for the requested comparison but not a normalized global target pool.

The target-aware source scores are:

| Candidate | Base | Important modifiers |
| --- | ---: | --- |
| sov_nuclear_bombs_operational_command | 1.00 | wartime 1.25, zero before Evolution I, capital 1.80, airbase 1.35, industrial 1.25 |
| sov_nuclear_bombs_collapse_command | 1.00 | wartime 1.40, transferred custody 1.75 |
| sov_nuclear_bombs_harden_storage_site | 1.00 | war 1.80, assigned site 1.55, capital 1.80, airbase 1.35, industrial 1.25 |
| sov_nuclear_bombs_disperse_reserve_package | 0.90 | war 1.60, remote site 1.20, airbase 1.35 |
| sov_nuclear_bombs_expand_fissile_production | 1.10 | reactor entitlement 1.80, reactor site 1.45, industrial 1.25 |
| sov_nuclear_bombs_survey_remote_test_state | 1.30 | test failure 1.40, remote site 1.20, airbase 1.35 |
| sov_nuclear_bombs_select_coercion_target | 1.00 | war 1.30, capital 1.80, airbase 1.35, industrial 1.25 |
| sov_nuclear_bombs_redirect_strike_state | 0.20 | capital 1.80, airbase 1.35, industrial 1.25 |
| sov_nuclear_bombs_select_retaliation_target | 1.30 | capital 1.80, airbase 1.35, nuclear-major 2.00 |
| sov_nuclear_bombs_select_disputed_depot | 1.50 | transferred custody 1.75, capital 1.80 |
| sov_nuclear_bombs_select_dismantlement_site | 0.70 | assigned site 1.55, industrial 1.25 |
| sov_nuclear_bombs_breakaway_request_return | 1.00 | transferred custody 1.75, capital 1.80 |

The source validity layer excludes impossible, missing, dismantled, impassable, ownerless, controller-invalid, same-country, subject, capitulated, non-war, non-major, unregistered, no-infrastructure, no-route, and no-event-target cases as applicable to each decision.

The MCP did not bind those nested conditions, so target dominance, target starvation, and rank reversal remain unresolved.

Rendered unresolved SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e445b7ff00b83d1287b4b7bcd4cb5f07141f2d36d93c4f2acdae55c7fd7fa39d/d0127364eeffe642da0e77bd35da8291c0d2f1674d361fc32af938b75e3256d4/probability-probability-4f52e72b81d39eadfe6c9ca6-unresolved.svg.

### Full decision and mission pool

Analysis ID: probability-c3c6addf1693a8a3701e4aba.

Source revision: ee2dff92c6e85a975a18be8689656dff8fcd22d39c214fb18d757e7d6a5903d1.

Source hash: 99cf9964015debe87eb5e86b8e45aea19e0d0ecc38ee9ef14d57b3fb91da93c1.

Scenario hash: 43cc29c25913f932e82651bbd1ad9eef8806121ad3f6c21f35b9b6fcde2c4896.

The complete 81-candidate mission pool was evaluated over P23_BASELINE_EVOLUTION_ENABLED, P23_BASELINE_EVOLUTION_DISABLED, P23_FIRST_USE_TIER_800_BLOCKED, P23_FIRST_USE_TIER_1000_STABLE_BLOCKED, P23_FIRST_USE_TIER_1000_SEVERE_RARE, P23_FIRST_USE_STANDDOWN_BLOCKED, P23_BREAKAWAY_TECHNICAL_STAGE, and P23_TARGET_SITE_VALID.

The result was PROBABILITY_ANALYZED_PARTIAL with 648 candidate rows, 239 unresolved items, and 75 diagnostics.

The mission adapter is score-only for this source and does not claim normalized selection probability or a native time distribution.

Classification: score-only partial evidence.

The important current mission scores are device assembly 0.80, delivery crews 0.70, command exercise 0.60, proof test 0.80, ultimatum response 1.00, strike preparation 0.40, retaliation window 0.60, rail corridor security 0.70, breakaway technical access 0.20, breakaway command formation 0.20, breakaway delivery integration 0.20, joint custody transfer 0.70, and dismantlement inspection 0.80.

No normalized mission selection probability, starvation claim, or timing claim is made from these scores.

### Major-exchange receipt threshold report option

Analysis ID: probability-2450bec28d12925071347b02.

Source revision: e84753dd9e08b6b13fc3de142d30d4903720531e5317b58a2b806a9c9bdb7182.

Source hash: d6ee9bbed9850c7e069b589b6964c81f7c254e14ea8641a7f8d88418f7915b11.

Scenario hash: 88a1ee27aa42d1e13a476e6c374db37b9c84e349f9d96ce8b5efbe017044a964.

The singleton chaosx.nr23.150.a report option was evaluated over P23_MAJOR_EXCHANGE_RECEIPT_BELOW, P23_MAJOR_EXCHANGE_RECEIPT_AT, and P23_MAJOR_EXCHANGE_RECEIPT_ABOVE.

The adapter returned a complete one-option result with the singleton at 1.0 in all three rows.

Classification: exact only for the downstream one-option report race, not evidence that the receipt gate opened at any of the three threshold cases.

The actual below, at, and above gate remains source-only because the receipt count is a global variable and the gate is upstream of this event.

## Comparison controls

These are same-source controls, not before-and-after balance claims, because no owner patch was applied during this audit.

The random-list control used sourceHash 225efb1424e1d0490a7871a4bceeffa3b5ed9f77c8dd469876ccf94700a15452, scenarioHash 9613742d3ab6aa46f396dfa9349fc4e46a5b26eee7bb446d0184b8e4dad5f47e, analysis ID probability-232f80b747e7848e7c17f176, comparisonChanges 0, and JSON artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b4d737b78503f42c73308ccae721edc204b9d84b0c1ce7e7049cfa3bbdc6a17d/2c2eff20f102cab38bc780f2ec1cba020a19f2fd6a0fbd3c68da35241fda5ce6/probability-232f80b747e7848e7c17f176.json.

The random-list comparison SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/82b6902e4cddb91d32bf54d9fd1e9158dda340e14773a7a3e97c2453c3f2c7f5/probability-probability-232f80b747e7848e7c17f176-comparison.svg.

The coercion control used sourceHash d6ee9bbed9850c7e069b589b6964c81f7c254e14ea8641a7f8d88418f7915b11, scenarioHash 6a65d0c24a9217af7cf1fc821b866a7a7d89f06e8d9f1e457fa00a383c321254, analysis ID probability-bed65cc02c3984e3289f900b, comparisonChanges 0, 33 unresolved rows, and JSON artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e195979ab96fa40d9e6766b32398ade6748ca0b1547f372698da066619d4592d/3d82a45b739f56c8ad56e0e55c64edf495830a8ebbaf5c8a71b1c9e57a649ac2/probability-bed65cc02c3984e3289f900b.json.

The breakaway control used sourceHash 99cf9964015debe87eb5e86b8e45aea19e0d0ecc38ee9ef14d57b3fb91da93c1, scenarioHash 80eba409d8dd656de32b26690e3ea385b7a6ba59b9f24bd56ae4de1f19e12a7d, analysis ID probability-a30d1b07c4373120c8a2fc5a, comparisonChanges 0, and JSON artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c93ab64f28c1de1c2fd227e73d677a336bf5c2424d49379b25f62e185ce0bcbf/8b6195bd484b59c29012f31df4b5a39e2bd24de97b8b63095d033d468286f5f4/probability-a30d1b07c4373120c8a2fc5a.json.

The breakaway comparison SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/8f4f19193a9b4d0bcda9c0f4d9553a3a400ec2416d43baf29fd117fd950452f1/probability-probability-a30d1b07c4373120c8a2fc5a-comparison.svg.

## Structural Event 23 MCP evidence

Current hoi4.event_inspect lint used selector kind event, eventId chaosx.nr23.1, revision 7b46ce0f0b41b7a70558a7f9c2a50810d919f49edff91f4121893ac789909dce, graphHash 21d2f98403cc858ac4c982cd0242b16412709762716c01b466a8152daaa04e0e, and artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a23f4dbdfa4d4bd40654b619ff17df7c718af6142d9d22aa010d5960701c8d38/0945465ab1a2c245fc2bc0155bbc9325d57f5c79055a1cd9e79acfb3872e64be/event-lint-7b46ce0f0b41.json.

The structural lint was partial because the large workspace deferred helper projections and lifecycle passes, and the workspace-wide counts included 8756 unresolved nodes and 2198 diagnostics with zero blocking diagnostics.

Current hoi4.event_render options used the same revision 7b46ce0f0b41b7a70558a7f9c2a50810d919f49edff91f4121893ac789909dce and graphHash 21d2f98403cc858ac4c982cd0242b16412709762716c01b466a8152daaa04e0e.

The structural render manifest is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9927c72d490793222b3b365920af94beabde0284dab64edb73aa71daa0cb586/e9d6f0b8a870730b7b34bcf7f72c98aad3c8e6c1a9c99caf8d15176b1c51ccf1/event-options-7b46ce0f0b41-manifest.json.

The structural render JSON is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2ce8094c556db908aadbc32b5576cc8e4f932fa562f04a85d1caf3c06f07fd0/9c59284081c04074c1a909f2cc68754344fde28a4ce378c956ba902f581e1f25/event-options-7b46ce0f0b41.json.

The structural render SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ecdeb0cab78f89a572096ffd76fa4cc9b76b7a04974a4dd54ac3def1a847dcb/edfb673abe9c3850d52b8a94c76d9bd7103ad649ed1b5068b446cbafeb7f193e/event-options-7b46ce0f0b41.svg.

## Audit findings

### AI validity and gating

The source validity layer is substantially gated: actor validity, active ledger, disabled-evolution flags, sequential evolution flags, route prerequisites, exact endpoint access, owner/controller relations, war relations, nuclear-major status, subject and capitulation exclusions, no-active-project checks, reservation checks, custody doctrine selection, settlement state, moratorium state, release suspension, and event-target state are all represented in the inspected source.

MCP did not prove those gates under a native Event 23 fixture because the nested scopes and variables were not bound.

### Dominance and starvation

The only probability dominance warnings came from empty-fixture gated event-option surfaces: phase acknowledgement was dominant in all eight navigation fixtures, and coercion accepted was dominant in all six coercion fixtures.

Those warnings are adapter diagnostics, not campaign behavior, because the same artifacts also report the gated options never eligible and unresolved.

The coercion pool has no proven unconditional fallback, so a malformed or missing response target can produce a no-option or forced-resolution surface; this remains an unresolved integration risk that needs a bound fixture.

The phase-navigation pool has a base-100 acknowledgement option and five base-0 gated route options, so stale phase flags or missing route state could starve route transitions; this is source risk, not a proven runtime outcome.

### Rank reversal and target bias

The source has several multiplicative target factors that can reverse ranks across capital, airbase, industrial, assigned-site, transferred-custody, reactor-site, remote-site, major-target, wartime, crisis, doctrine, and readiness states.

The probability_sweep route could not run, and the target fixtures did not bind state candidates or FROM scopes, so no rank reversal, target dominance, or target starvation claim is exact.

### First-use and exploit risk

The final authorization score is correctly zeroed before Evolution III at the decision score layer and receives the severe-loss multiplier only when the severe first-use gate is true.

The source has a semantic gap that requires owner review: an Evolution II limited strike against a non-major target can set sov_nuclear_bombs_soviet_first_use_recorded, but the severe first-use gate only blocks sov_nuclear_bombs_soviet_major_first_use_recorded.

If the intended rule is that any Soviet combat use consumes the first-use opportunity, a non-major limited strike can leave the later major first-use gate open once the Evolution IV conditions are met.

The severe first-use helper also does not independently test sov_nuclear_bombs_release_orders_suspended, although prepared_strike_chain_is_valid and retaliation_authorization_is_valid do reject suspended release orders.

The MCP could not bind P23_FIRST_USE_STANDDOWN_BLOCKED, so this is a source-level exploit-risk finding rather than an engine-proven path.

### Major-exchange receipt risk

The recorder prevents repeating the same ordered actor-target pair from increasing the receipt count, but the source rule is pair distinctness rather than an explicit distinct-country set.

If the design means two different major countries rather than two different ordered receipts, the current OR comparison should be reviewed by the owner in common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:153-169 and the on-action candidate-ID assignments in common/on_actions/023_sov_nuclear_bombs_on_actions.txt:123-160.

The requested below, at, and above threshold cases are unresolved in MCP because no global receipt-count fixture was accepted.

### Repetition, cadence, and snowball risk

The random test roll itself has no repetition defect in its exact conditional pool, but its enclosing action cadence, cooldown, recovery, and terminal handling were not part of the random_list adapter request.

The mission adapter reports no native time distribution and the sequence route was not run, so repetition, cooldown, cap, reset, re-entry, and terminal-state safety remain unresolved for the full Event 23 lifecycle.

The breakaway route has explicit 180/240/180-day stage timers and explicit stage flags, but no MCP sequence evidence proves that cancellation, cleanup, re-entry, or terminal collapse states cannot repeat or bypass a stage.

## Scenario coverage and classifications

P23_BASELINE_EVOLUTION_ENABLED was included in doctrine, phase navigation, and full mission evaluations and remains partial or score-only because the actor, phase, and evolution flags were not bound.

P23_BASELINE_EVOLUTION_DISABLED was included in doctrine, phase navigation, and full mission evaluations and remains unresolved because disabled-evolution flags and scheduled MTTH state were not bound.

P23_COERCE_ISOLATED_LOSING_MINOR, P23_COERCE_PROTECTED_STABLE_MINOR, P23_COERCE_UNTESTED_SECRET, and P23_COERCE_EMPTY_THREATS were included in the complete coercion race and are unresolved nested-trigger cases.

P23_COERCE_MINOR_MAJOR_EXCLUSION and P23_COERCE_MAJOR_TARGET_EXCLUSION were included in phase navigation, coercion, and same-source coercion comparison controls; no major-exclusion probability is claimed.

P23_FIRST_USE_TIER_800_BLOCKED, P23_FIRST_USE_TIER_1000_STABLE_BLOCKED, and P23_FIRST_USE_TIER_1000_SEVERE_RARE were included in doctrine, first-use authorization, and full mission evaluations; the result is score-only or partial, with no first-use probability claim.

P23_FIRST_USE_STANDDOWN_BLOCKED was included in stand-down, first-use authorization, phase navigation, and full mission evaluations; nested release suspension and event-target state remain unresolved.

P23_MAJOR_EXCHANGE_RECEIPT_BELOW, P23_MAJOR_EXCHANGE_RECEIPT_AT, and P23_MAJOR_EXCHANGE_RECEIPT_ABOVE were included in phase navigation, stand-down, receipt-report, and sweep attempts; only the downstream singleton report option was exact, and the upstream receipt gate was unresolved.

P23_TEST_PROOF_SECURE, P23_TEST_CONCEALED_WEAK_COMMAND, P23_TEST_PUBLIC_PREPARED, and P23_TEST_INVALID_SITE were included in the exact random-list evaluation, which proves only the conditional 70/20/10 execution result.

P23_BREAKAWAY_CUSTODY_STAGE, P23_BREAKAWAY_TECHNICAL_STAGE, P23_BREAKAWAY_COMMAND_STAGE, P23_BREAKAWAY_DELIVERY_STAGE, P23_BREAKAWAY_OPERATIONAL_STAGE, and P23_BREAKAWAY_RETURN_STAGE were included in the three-stage mission evaluation and comparison control; all three mission definitions were never eligible because their native mission availability is always no.

P23_TARGET_WARTIME_REAL_DISPUTE, P23_TARGET_MAJOR_EXCLUSION, P23_TARGET_BREAKAWAY_CUSTODY, P23_TARGET_SITE_ROUTE_FUEL_BELOW, P23_TARGET_SITE_ROUTE_FUEL_AT, P23_TARGET_SITE_ROUTE_DISTANCE_ABOVE, and P23_TARGET_SITE_VALID were included in the 12-candidate target subset; nested state and route feasibility remained unresolved.

## Recommended owner fixes, without application

1. Add a native machine-readable Event 23 scenario fixture that binds ROOT, THIS, PREV, FROM, saved event targets, event-target country/state scopes, global and country variables, flags, technologies, wars, owner/controller, subject, capitulation, faction, airbase, bomber, fuel, distance, and major receipt identity.

2. Re-run the exact named scenario sets after the fixture exists, with numeric alternatives for readiness 25/50/75, integrity 20/40/75, chaos 800/1000, strategic losses 2/3/5, receipt count 1/2/3, fuel 999/1000, and distance 999/1000.

3. Decide whether first-use consumption is general combat use or major-target use, then align sov_nuclear_bombs_event_severe_first_use_gate, sov_nuclear_bombs_event_can_authorize_first_use, sov_nuclear_bombs_event_has_valid_limited_strike_target, and the action-recording flags in common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt.

4. Decide whether the receipt threshold means two distinct ordered receipts or two distinct major-country participants, then bind and test the actor-target identity recorder in common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt and common/on_actions/023_sov_nuclear_bombs_on_actions.txt.

5. Make stand-down rejection explicit in the first-use authorization path if the severe first-use helper is intended to be independently safe, rather than relying only on prepared_strike_chain_is_valid.

6. Provide an explicit coercion fallback or prove the event-target response path cannot enter the event with every option gated, then re-run the six-option race and comparison.

7. Supply a complete mission lifecycle manifest for activation, timeout, cancellation, cleanup, cooldown, recovery, cap, removal, reset, re-entry, and terminal states before using probability_sequence or claiming repetition safety.

8. After any owner-applied weighted patch, run hoi4.probability_compare with the same candidate pools and the same named scenarios; the same-source controls in this handoff are not a substitute for that before-and-after pass.

## Skipped analyses and exact blockers

The event_mean_time_to_happen evaluation returned PROBABILITY_SURFACE_EMPTY with no weighted blocks matched and no available MTTH adapter, so no exact or bounded evolution timing distribution is claimed.

The corrected probability_sweep call returned PROBABILITY_SWEEP_RANGE_REQUIRED with details scenarioId P23_TEST_PROOF_SECURE and path state.sov_nuclear_bombs_readiness because every sweep path requires a declared scenario range, numeric alternatives, or an accepted numeric state value.

An earlier sweep attempt using the stale line-760 random-list identifier returned PROBABILITY_SURFACE_EMPTY because the current indexed entries are at line 765; no conclusion uses that failed attempt.

probability_simulate was not run because the user did not declare uncertain-input distributions, correlations, seed, sample count, or sampling method.

probability_sequence was not run because no complete custom weighted-pool manifest declares cadence, cooldown, recovery, cap, removal, reset, timer changes, terminal states, and state transitions, and the mission adapter reports sequence false.

The requested AI-strategy factor source returned no candidates and no available adapter, so there is no Event 23 strategy-factor probability evidence.

The structural Event 23 inspect and render were partial because the large workspace deferred helper and lifecycle projections and exposed workspace-wide unresolved nodes and diagnostics; the direct Event 23 graph had zero blocking diagnostics.

## Final handoff classification

Exact: only the conditional Event 23 test random_list result, 70/20/10 for a complete eligible three-entry pool, and the downstream singleton receipt-report option.

Bounded: source bases, modifier traces, hard validity gates, route thresholds, receipt threshold logic, mission stage durations, and the current same-source comparison controls.

Score-only: the 81-candidate mission surface, breakaway mission scores, first-use authorization score, and the target-aware decision scores.

Unresolved: campaign-level doctrine, coercion, phase navigation, stand-down, evolution-disabled behavior, MTTH timing, threshold crossing, target/site feasibility, rank reversals, starvation, repetition safety, and AI-strategy factors.

No gameplay patch, weight change, or tuning decision was applied by this auditor.
