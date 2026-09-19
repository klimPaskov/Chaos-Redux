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

## Post-handoff concurrent source drift and fresh MCP evidence (2026-09-19)

This addendum is the latest read-only snapshot and supersedes only claims that depend on mutable Event 23 source after commit 3d24d1824. The preceding body preserves the earlier pinned artifacts. Event 23 gameplay files were modified concurrently in the shared worktree and were not authored, patched, or staged by this auditor.

### Final local source snapshot

The final local read-only capture immediately before this addendum was:

| Source | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| common/script_constants/023_sov_nuclear_bombs_constants.txt | 634 | 13660 | 7973DF753CF75632F56F8BFD7CA4D5340A20B1DB060D59702927D95AC94DA886 |
| common/mtth/023_sov_nuclear_bombs_mtth.txt | 46 | 4088 | DCB60B1AE6F08C09B0E3D22E9E2442432EB424E3ED2BB103517F0DF3BBD1DE09 |
| events/023_soviet_nukes.txt | 571 | 23208 | C5FF20CED5EC19B63AB7DF5E8E86E11D432C77AECF57A0C4D48C3F3DD3B61AA2 |
| common/decisions/023_sov_nuclear_bombs_decisions.txt | 1378 | 108209 | FE78EAC200DD2E44AB21DFC8915F9294F363BBB7B97D91E6AD9DE416ADA9DB31 |
| common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt | 3060 | 160070 | E5DB039D7B7F08F8B3964B81A51A87D0A85EA88FA69D9C40D68C2DD048B80378 |
| common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt | 1703 | 99092 | 2FED7AF708EAB9550445583EB844E9D322F19BB05D4CEC416F09FC6EEDBCF38C |
| common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt | 1089 | 47669 | 1D5BF567BE43DA1472FAFC1E25B21F29672E1F2519ACE8DFCC8499310EB414E6 |
| common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt | 327 | 18586 | D9A450F181AE826BD21D788FEE2C933E04363E4329274014603BDCC9546A2D7B |
| common/scripted_triggers/023_sov_nuclear_bombs_achievement_triggers.txt | 186 | 11135 | 21E27EEF51A6E601788D97C47EF3AEE3DE776385DADBD81FF163B454E281F6F1 |
| common/on_actions/023_sov_nuclear_bombs_on_actions.txt | 183 | 6928 | A9F571052879001F383CB95BE85F8690AADCD3CDEFA7D7A1B0C552AD28EF6AA2 |
| docs/events/023_sov_nuclear_bombs.md | 196 | 71722 | FA6496BF342EE9919974336DC9BD62B84C37B0C3384F6C6D366B719629B06575 |

The current local test pool is indexed at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:798` and has four dynamic entries, not the earlier three-entry 70/20/10 pool. The current base constants are success 60, partial 20, failure 12, and accident 8, with conditional modifiers for instrumentation, concealment, evacuation, integrity, and readiness. The old 70/20/10 result remains exact only for the pre-drift source snapshot and its four named test fixtures; it must not be reported as the current normalized result.

The current receipt gate requires Evolution III, chaos at least 800, major detonation confirmation, major exchange active, a global major receipt count at least `major_receipt_minimum = 2`, the answered flag, and another nuclear major. The runtime recorder only reaches the second receipt when the observed actor and target IDs are reciprocal. These are source facts and not an engine-proven probability because the required global variables, flags, country identities, and nested scopes were not bindable in the fixture schema.

### Fresh probability evidence and artifact provenance

All calls below used the mandatory read-only `hoi4.probability_inspect` first for the relevant adapter or source, followed by `hoi4.probability_evaluate` and same-source `hoi4.probability_compare` where the adapter bound. Rendered ranking, matrix, unresolved, and comparison artifacts are listed so the parent can retrieve the evidence directly.

Test random outcomes, adapter `random_list`, source `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:798`: inspect returned source revision `85372c9a198c54a19d4c320a8c4aa484287a31df90e361253319df52975e4351`, source hash `5b2af7f2cfaebc8b93928d61083300c9e1d0fce73bc9260baead7f6eab4b01e5`, four candidates, and inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a921dc3c20e40eb387c6b921bd53dfec231479dec40c951697023a9fcb123760/b5719da07474cae4c4d63ef60f2063a505bf6c59006a900231c2de7a0ad52796/probability-inspect-5b2af7f2cfaebc8b93928d61083300c9e1d0fce73bc9260baead7f6eab4b01e5.json`. The evaluate scenario set was `event023_test_random_outcomes_postdrift_20260919` with `P23_TEST_PROOF_SECURE`, `P23_TEST_CONCEALED_WEAK_COMMAND`, `P23_TEST_PUBLIC_PREPARED`, and `P23_TEST_INVALID_SITE`; it returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-741a3ac377a5e05ded4d3225`, scenario hash `b5226ec0652efcd3c9af10c2251e041b9b329f91a3c25af4907b4f6b40384157`, 16 rows, 4 unresolved, and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4edf25bc8fee1073d1a4679c0fb9dac9cc268dcac3d594c9c4d6a36fc7588b3d/72c2dbbca5360469292266b04b12af373ffe08330d5c7ed1b32ac6b825a099a6/probability-741a3ac377a5e05ded4d3225.json`. Its ranking, matrix, and unresolved renders are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d05f709ca701a3c6a897eadd4e7922409760774710b174e1366077a44d0a027f/80bc8b3646ad2da4848dcc1d00e596f0977bab7aa9f6041d9954f74fc364d5c6/probability-probability-741a3ac377a5e05ded4d3225-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f09f77aea66c0239c47ce155e1d5e0be3bd29a94bb76bdf260fbc5fa197fc5a2/201c16ae1753e8ecee902eb56d49d7a195faa640f9b7323f51d644282eeb2a7e/probability-probability-741a3ac377a5e05ded4d3225-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42ddc597e635f062174c57623bf4fa79f78ac1a36caeb3d6df40aa2f28f64018/b0070b422b1a1a3f5e8dfd2736b8bac80deb0559cc5296c42643bac959c12e3b/probability-probability-741a3ac377a5e05ded4d3225-unresolved.svg`. All four dynamic weight variables were unresolved, so no current normalized 70/20/10 probability is proven. The same-source compare analysis `probability-170bfe676d73457a4e00be1`, with the same revision, source hash, scenario hash, 16 rows, 4 unresolved, and zero comparison changes, is in `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8f28b2dd8ab96cf877a77cabc9ef0d8ca8adf5af6f174bc7922be8675e0758ac/0ff0185822e1210620c86e261d21dfa56d1a85f61e28d38c21b78f2e9d3e8938/probability-170b0fe676d73457a4e00be1.json`, with comparison render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/536e107f503ffb6c905a149708e076344ad5182183025e4914ddcfe298cb4652/probability-probability-170b0fe676d73457a4e00be1-comparison.svg`.

Phase navigation and baseline or exclusion scenarios used source `chaosx.nr23.100`, adapter `event_option_ai_chance`, and candidates `chaosx.nr23.100.a`, `.c`, `.custody`, `.production`, `.test`, `.coercion`, and `.retaliation` as indexed by the MCP pool. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7cddb7a3dc3676fbc03ee2498772e18e54102a10b860c66790f16169c895c86d/f83c29815818a93f441d4fb94d12e4a07ede42a8d0707d959026a6ab56af048f/probability-inspect-c8fd77570c22.json`; source revision `96a6f50fbb71544f347ebc62f4d46894c75132e60db336f9aec93a5406b787a4`, source hash `c8fd77570c22afe1de7c59fdb77785644336d40d1d96972c5f0c87c1d677a4a4`. The evaluate set `event023_phase_navigation_current_20260919` covered `P23_BASELINE_EVOLUTION_ENABLED`, `P23_BASELINE_EVOLUTION_DISABLED`, `P23_COERCE_MINOR_MAJOR_EXCLUSION`, `P23_COERCE_MAJOR_TARGET_EXCLUSION`, `P23_FIRST_USE_STANDDOWN_BLOCKED`, `P23_MAJOR_EXCHANGE_RECEIPT_BELOW`, `P23_MAJOR_EXCHANGE_RECEIPT_AT`, and `P23_MAJOR_EXCHANGE_RECEIPT_ABOVE`; analysis `probability-060011086e82f184cce2357b`, scenario hash `f6325ff8aac2f77f6ac5f50590251675e9680ca757db07c906b0e357eec5b7bd`, returned partial with 48 rows, 11 unresolved, 14 diagnostics, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71fbb92e6f004a56a278a600c0313aeda0fe2f637ca4a98939daa52bb0a0f831/1869af638592386e433300b1dc2d4fb12bfd9ddf33f69a254fefb407e18950b7/probability-060011086e82f184cce2357b.json`, ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02e66e0064aefdd4e5ae2c4c5ed95d7ffb42c7f248abb430552a97b9d0110250/b7b8f75bdcb163c43b7b734f347d97c11b78f4034bdeed40da8721e2d99eca67/probability-probability-060011086e82f184cce2357b-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5bcd5cbd56c368023163cb094cd123a5ad6b8fd26dc76eae3e4a0e91121da51/0c3e8aaab71d5994e71ab4fa901f3e2a6622a8f76df631fd1bc2d36392211d6a/probability-probability-060011086e82f184cce2357b-matrix.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64d36262728efe127b192d366e250c18fba46c8902499919947810acb9a8d508/e768970aae426772b7d222cfe219a8dd5b75b9bb84a01aa4a49b477edde08ab0/probability-probability-060011086e82f184cce2357b-unresolved.svg`. The same-source compare is analysis `probability-6d044f1e3be18264aab7d549`, same source and scenario hashes, 48 rows, 11 unresolved, 14 diagnostics, zero comparison changes, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3f8d2ced40ecfd06b173d1a9b03ab4499139c7f6b3b1e5ab21bb9fdea6b264a/7912a70fab6760cdde21d2dabd8c2789ba29f15a0de1b318b4910b89c9190368/probability-6d044f1e3be18264aab7d549.json`, comparison `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/af8ce9d6ff2e239355413b1976184f55c78584d0bd6645e0d89f88cc6bd93015/probability-probability-6d044f1e3be18264aab7d549-comparison.svg`. All eight phase scenarios showed `.a` as dominant and the other options never eligible under the empty fixtures; this is a fixture-bound score outcome, not campaign probability or proof that exclusions work.

Coercion used source `chaosx.nr23.120`, adapter `event_option_ai_chance`, and candidates `.a`, `.b`, `.c`, `.refuse`, `.e`, and `.f`. Inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b7350c85e96de198979b7c13024de118f607620467ada08565384267c1cf08e6/c7275fd3bb9fdec372f7adb9674fccfa3cd67a0fc07b16e4ed377155ac4493ae/probability-inspect-d6ee9bbed985.json`, source revision `42588438320875d8283d06b32fd6c958b91fe8424f64afc28848d301d58e3f38`, source hash `d6ee9bbed9850c7e069b589b6964c81f7c254e14ea8641a7f8d88418f7915b11`. The evaluate set `event023_coercion_current_20260919` covered `P23_COERCE_ISOLATED_LOSING_MINOR`, `P23_COERCE_PROTECTED_STABLE_MINOR`, `P23_COERCE_UNTESTED_SECRET`, `P23_COERCE_EMPTY_THREATS`, `P23_COERCE_MINOR_MAJOR_EXCLUSION`, and `P23_COERCE_MAJOR_TARGET_EXCLUSION`; analysis `probability-4edee2e65dd20b8553e2799f`, scenario hash `71ae5e23118365f14b81858fcd7beccef2f953342006678623dd99dce0769d2f`, returned partial with 36 rows, 33 unresolved, and 14 diagnostics, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91c357cfd1de0623c8497ad6d1191a2b1bf91b7ec58a70b4cadb694a29ad9c3e/d3974becc9fd5bb54fc7e2509c587cc339f0c74f7991a76d45c100d00d0945af/probability-4edee2e65dd20b8553e2799f.json`, ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/020597d8091d1023c068f978db032bcb06aac690bcad73f4c54190a46e305477/3bfd67c641acb891950e39d4e9f40ea4cc7ddd7cfd4a4b3effc648216562147a/probability-probability-4edee2e65dd20b8553e2799f-ranking.svg`, matrix `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/926942e73648ce228354ee2f5a4d6d58e0f7509b8738cc374ae86701068043b1/6c83a3712f642da2b62c20589dd836b1469f8bebd5a0879815e37140426a0bb3/probability-probability-4edee2e65dd20b8553e2799f-matrix.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/add4491edfe1ab803237226f587f18ced2c89c770be5e9d8cb56be2edc3f4a19/87071efa2b204bc8f767143bd52f1ee462680b9f588c3b74ec3fb4efbc6653d6/probability-probability-4edee2e65dd20b8553e2799f-unresolved.svg`. Same-source compare analysis `probability-5fd299269415f054b962c4e4`, same source and scenario hashes, 36 rows, 33 unresolved, 14 diagnostics, zero comparison changes, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/09c30a6ef8cdffaac9339ce2fa318163373d7bbf5da315a6edd01b76f0981348/22334338daf85db3e0bf2008cbafe18bac4d2d9f3649cca9286c0544fb05e3ab/probability-5fd299269415f054b962c4e4.json`, comparison `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/7308c19899aa9d5680c50d97861a75d2f330a10f7121878bd2807226b5bceadd/probability-probability-5fd299269415f054b962c4e4-comparison.svg`. The `.a` option was dominant and all options were never eligible under empty fixtures, so minor and major exclusion behavior is unresolved rather than proven.

First-use authorization used the singleton mission `sov_nuclear_bombs_give_final_authorization`, adapter `mission_ai_will_do`, source revision `206a070b3e7ecdb733fd8f1093acfc467b8ad80a176d88c9deee241fe629d4df`, source hash `f85397565290163e432048a5034a0dd604bcaeb918a1f94232dff24c04517e1d`, and inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07f1b5d2e21cf73874319479f052fa0ff2717f9e5f4a44c5b7ad79005c49b22b/355885e577fbdea542e5bcd15d10b9b51d3b05ec176a4ccaa88e6f3e1187a263/probability-inspect-f85397565290.json`. The evaluate set `event023_first_use_authorization_current_20260919` covered `P23_FIRST_USE_TIER_800_BLOCKED`, `P23_FIRST_USE_TIER_1000_STABLE_BLOCKED`, `P23_FIRST_USE_TIER_1000_SEVERE_RARE`, and `P23_FIRST_USE_STANDDOWN_BLOCKED`; analysis `probability-5ed3d0299fbcee9c5bde94b0`, scenario hash `72b58706ee0287d6d5896b2fff10c40bc4fa07d77a13b3c8e2d8dba9a0a54483`, returned partial with 4 rows and 12 unresolved, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79b84307b2aa9ef9cf53a76c05f21824a2aca3306108a03a274384892bb76aa3/b53d2f5de3a8f1777a67d54c6b5d18bd085522ce7596bf0fb1a10401b3dd855c/probability-5ed3d0299fbcee9c5bde94b0.json`, ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99adc22b888278ad3deec510c8887dc867fe6cabce5b639f118fa6243a4f2935/1eecad3fc7518f5ba7b50356d22d36adc6e4495354130bcf6343caa49c9ffebf/probability-probability-5ed3d0299fbcee9c5bde94b0-ranking.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93b91d865e6d8bf7c998e1139803dd82a995bd14a88ebbd5d64fda233daafa6a/0d1dacafd656314b4e5d2760ccdaa9d551e9437fc079be19629ac103edf777/probability-probability-5ed3d0299fbcee9c5bde94b0-unresolved.svg`. Source base is 0.10, severe-loss factor 1.50 only when the nested first-use gate binds, and 0 before Evolution III; no first-use probability is claimed.

Stand-down and report receipt options used source `chaosx.nr23.163`, adapter `event_option_ai_chance`, candidates `.a` and `.b`, inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/daa7867383556c6523af9a99da4513da1322f3adbe56efdd8fd45f913ba77ec4/e33c16335550ad5254b3e6d3bf37ef501df28460f7142154c16bf09ae828154a/probability-inspect-818f8aef957a.json`, and inspect source revision `c8fe4364fd35534335d511791db7bbc24c3398e1e8f6ff194dc49af465736616`, source hash `818f8aef957ab0687648215009217e4e464c84760cd1eb2f1270f0de3c02af49`. Evaluate set `event023_standdown_receipt_current_20260919` covered `P23_FIRST_USE_STANDDOWN_BLOCKED`, `P23_MAJOR_EXCHANGE_RECEIPT_BELOW`, `P23_MAJOR_EXCHANGE_RECEIPT_AT`, and `P23_MAJOR_EXCHANGE_RECEIPT_ABOVE`; analysis `probability-80f4450d110ee6aca2e35958`, source revision `fee0fad499e4be418c10002c166440fff814400a79d02aac293adaf33fba1a6`, source hash `1e296d04b6298ce5258eae09fa60c5f64caeaf284776f3e893d7064741a7915c`, scenario hash `27e2d1d15f09237d52287167f5147df23780545ef8679fe127a9a539e27eccb7`, partial with 8 rows and 1 unresolved, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb098e9cb0bb65b671a68005ae6785b2197a9f00b237998edb077e65aa5bc824/45924d208639c70119ab1791d843d537389865ed7707a29c877cf4d228fd0045/probability-probability-80f4450d110ee6aca2e35958-unresolved.svg`, and ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b9b4afd774089453819ab745790a74b319c66725e24cb46d3e0f0a662c5f6a8/1709b2f9174eb619cab8cae18f7cd3e59f2a335b2246b118c54c55f6bad2e047/probability-probability-80f4450d110ee6aca2e35958-ranking.svg`. The same-source compare analysis `probability-d789ff5e232cef8ab8038941`, scenario hash unchanged, partial with 8 rows and 2 unresolved, zero comparison changes, is JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ceb4fa00a18d6e3b07d3252b43b5d8131b2e5bfe214d3698f68d08cc1063d7b/2e618b1f786f9a53be5a85b56a91eb384f06328851661c0613c56f87c90accca/probability-d789ff5e232cef8ab8038941.json`, comparison `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/72759f7692a724632b9664d045443484b3e16ad115f0dc2769b0785ff94c3c1b/probability-probability-d789ff5e232cef8ab8038941-comparison.svg`. The report singleton `chaosx.nr23.150.a` was separately evaluated over receipt below, at, and above; analysis `probability-228c69e0afadef473360871f`, scenario hash `57bb9e394a48100d0d85a8f42e3bb20af3db6cce1480cc427fe4de84627c6208`, complete 3 rows with 0 unresolved and singleton conditional 1.0, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d489da926ba1bdc291bd9562cad18b8d1baeae6dc529d0faf7a9cfb889c9bf8/81a3f567264078981642c7d2bce1f96e3f9caba4abec11f66d26bd5d37295011/probability-228c69e0afadef473360871f.json`, ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e95fabc3593c479378dadb75614f0481fd7ae74f15e8363e8f1ef528bf9c74d/2d2dee61f8bc088e9fea8febc169c58edea12630848276c9edd381416575b3e8/probability-probability-228c69e0afadef473360871f-ranking.svg`. That exact 1.0 is only the downstream report selection conditional on the report surface, not the upstream receipt-gate probability.

Breakaway stages used the complete declared pool `sov_nuclear_bombs_breakaway_technical_access_mission`, `sov_nuclear_bombs_breakaway_command_formation_mission`, and `sov_nuclear_bombs_breakaway_delivery_integration_mission`, adapter `mission_ai_will_do`, inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d265befb526c45715f9c1c48c79c503ec46d51da6fc56b23babfe86824bdec00/05329bfd1c4a88c1be59bc875713f3683e0b32ceb0d724905ffd674363646f44/probability-inspect-f85397565290.json`, source revision `206a070b3e7ecdb733fd8f1093acfc467b8ad80a176d88c9deee241fe629d4df`, source hash `f85397565290163e432048a5034a0dd604bcaeb918a1f94232dff24c04517e1d`. The evaluate set `event023_breakaway_stages_current_20260919` covered `P23_BREAKAWAY_CUSTODY_STAGE`, `P23_BREAKAWAY_TECHNICAL_STAGE`, `P23_BREAKAWAY_COMMAND_STAGE`, `P23_BREAKAWAY_DELIVERY_STAGE`, `P23_BREAKAWAY_OPERATIONAL_STAGE`, and `P23_BREAKAWAY_RETURN_STAGE`; analysis `probability-318d957ab1cc7c8b831bf11a`, scenario hash `a72afbf3e54514a0c998df3b1e278b57e02933e070b7e0b6139962bdf0831865`, complete with 18 rows, 0 unresolved, and 3 diagnostics. All three missions were never eligible because native availability is `always = no`; this is exact availability evidence, not a sequence probability. JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90b90079e423a222e1c1cb4df2dd00cc6d1d9497c420800a0fdb15dca1805e14/8fe9745a429cd71a4266fa665927666bf9cbe2a468e9460ae9e2152c858650d2/probability-318d957ab1cc7c8b831bf11a.json`, ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/718084650cb8e9f4aa647d9214ba8a47c1f074b9c6c07f8d7559cc69e23767e5/8752e8c56acf9cb62a739f3d34ce7fe603dd6a90267d459d6ffad5bd74c016ea/probability-probability-318d957ab1cc7c8b831bf11a-ranking.svg`, same-source compare `probability-958f11bee5a16473bbd0227d` JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/086af0bc8b60df7a1fd89e7fdfcf6b8de1b37d88aad9ac612e7526a19d4f1ed2/06a672b7cb7e62114ebdd2a22eb96034cbe518fc65c604be99fe86f22329abc7/probability-958f11bee5a16473bbd0227d.json`, comparison `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/fc390071b10fbf51a187bb514ad33f5bade3fd1060eccd24779d030cecc7f957/probability-probability-958f11bee5a16473bbd0227d-comparison.svg`.

Target and site feasibility used the 12-candidate `mission_ai_will_do` pool rooted at `sov_nuclear_bombs_operational_command`: operational command, collapse command, harden storage, disperse reserve, expand fissile production, survey remote test state, select coercion target, redirect strike state, select retaliation target, select disputed depot, select dismantlement site, and breakaway request return. Inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/150162e0a6bea7804bb2268b56a9884ba9979ac455c91e2fdb4028c97b0239eb/d976b57341a42248496b3876cee91d7c8e8cffb2f3a06ab53e816bf5a2123f04/probability-inspect-f85397565290.json`, source revision `733c94b0a181328d9fe25db43459a1b32160228f493df2d07faea469d127ba51`, source hash `f85397565290163e432048a5034a0dd604bcaeb918a1f94232dff24c04517e1d`. The evaluate set `event023_target_site_current_20260919` covered `P23_TARGET_WARTIME_REAL_DISPUTE`, `P23_TARGET_MAJOR_EXCLUSION`, `P23_TARGET_BREAKAWAY_CUSTODY`, `P23_TARGET_SITE_ROUTE_FUEL_BELOW`, `P23_TARGET_SITE_ROUTE_FUEL_AT`, `P23_TARGET_SITE_ROUTE_DISTANCE_ABOVE`, and `P23_TARGET_SITE_VALID`; analysis `probability-8496fa1df9b40faff544dcf9`, scenario hash `4d37b87a9a684eedd978cefa0816c0351e27d5b8fba847a82fad2758395ba37a`, partial with 84 rows, 32 unresolved, and two diagnostics, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0eeee1ad275da0ebd5d754477ab981d97482d87be6e0fafb30f4ab61dbfbd8c0/caadbe1a977eb0b8d0776df5fc0626524c230fd9450fee688a539cabc2908bdb/probability-8496fa1df9b40faff544dcf9.json`, ranking `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5a90c376d1f367fda44f13fbb2e3f3f5d27c6a3b635011097381389a062c75e/56af2453bb9f020f77c5c9ea1c262500752e2d035b38e01d70315191f5ab10b6/probability-probability-8496fa1df9b40faff544dcf9-ranking.svg`, unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e445b7ff00b83d1287b4b7bcd4cb5f07141f2d36d93c4f2acdae55c7fd7fa39d/d7e70c81ced439786b405dbd5a3369bfd9952d53b9fedcf9761bbda13d87acdf/probability-probability-8496fa1df9b40faff544dcf9-unresolved.svg`, and same-source compare analysis `probability-4f56744027cd835ec5ce2512`, same source and scenario hashes, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/377887346e16366cf84808d182cde2aaf3888b48888dd116a8015839fe1109dc/1ddba8f4d3fd210bbba48a5744631b2a6b23eb81648ffc4f6e022f1296dfef30/probability-4f56744027cd835ec5ce2512.json`, comparison `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/ffb832489c73a31ccd973a0bc5cab7dd324a1ad5c3c1e2ef369112c1b5f78fda/probability-probability-4f56744027cd835ec5ce2512-comparison.svg`. Fuel, distance, country ownership/controller, target validity, event-target identity, and site-state conditions remained unresolved.

### Structural MCP evidence

The matching read-only `hoi4.event_inspect` for `chaosx.nr23.1` returned `EVENT_INSPECTED_PARTIAL`, revision `c339bab29c33e06f15e9de16f28345205de654dd06b8497c2363f74d52ca2928`, graph hash `3ae9667f068b3c09812c980244c3d9cf28f67f19b8d66f3d549ee8db5a310ca5`, 9745 events, 15176 options, 38399 edges, 2198 diagnostics, and zero blocking diagnostics, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f661482de969b942de8152505b832a7b29971d07838e8b62d923bb27ad652ab/d49f618048a2bb5032f78051bf1146ca6db8d4e3235a3099d47275eb2113f8c1/event-lint-c339bab29c33.json`. The matching `hoi4.event_render` was partial because the workspace exceeded the render node budget; its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b32f0bc6211ae56a215b3d7419abe5e83918f500e24de6a557363c9b3682bd86/72d41c667233d0f1e0f6f5b8522fb8efec55a0826087b193df0bb6a740437010/event-options-c339bab29c33-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e25e98e40df21ec108d74431f1a0716c0c0982facca8dd33f468d26457169cc5/15c06517e514f259180cd9739cf2198926146a2ac58278207f061cf4d66be08d/event-options-c339bab29c33.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42b101807ed54a3adebc082b1cfeabbd2397ed9e2778f1edcc43cfeb427603a0/623b2527eda242401c5da6fd3b70b57016a061fcd27e7cceafdddd1f4a7c5f4f/event-options-c339bab29c33.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cde8a733a47ef273f2ab2fb03c1a7a74eb3cd52e0b35386116422fc5308467ab/8bf1d39475f43ab5231b43f161ee98822ee2e4599a9398006a422af94caac3ac/event-options-c339bab29c33.png`.

### Updated conclusions

Exact: the downstream singleton receipt-report option is conditionally 1.0 on its already-bound report surface; the current four-entry test random list is structurally exact as a proportional categorical pool but its dynamic weights are unresolved under the supplied fixtures. The pre-drift three-entry 70/20/10 evaluation is exact only for its pinned historical source and must not be generalized to the current four-entry implementation.

Bounded or score-only: source bases and modifier traces, hard gate expressions, receipt threshold and reciprocal-ID logic, route threshold expressions, native mission availability, mission stage definitions, and same-source comparison controls. A score race is not a click probability, and a singleton conditional result is not an upstream gate probability.

Unresolved: normalized current test-outcome probabilities, coercion acceptance or refusal probabilities, evolution-enabled versus disabled phase selection, first-use authorization probability, stand-down acceptance probability under release suspension, upstream major-exchange receipt probability below/at/above the distinct-major threshold, target and site delivery feasibility, breakaway timing or sequence probabilities, MTTH timing distributions, rank reversals, starvation, repetition, and snowball risk. The MCP fixture route did not bind nested ROOT/THIS/PREV/FROM scopes, country and state ownership/controller, event targets, global flags and variables, technology and war state, fuel, airbase, distance, or dynamic temp variables.

The empty-fixture dominance diagnostics for phase navigation and coercion are not campaign findings. They show that `.a` is the only candidate the adapter could resolve in those incomplete fixtures and that other options were never eligible; they do not prove major exclusions, fallback safety, or choice dominance in a real campaign.

### Skipped analyses and exact blockers in this refresh

The requested sensitivity sweep was attempted with `state.sov_nuclear_bombs_readiness` and returned `PROBABILITY_SWEEP_RANGE_REQUIRED`; details identified scenario `P23_BASELINE_EVOLUTION_ENABLED` because no numeric range, alternatives, or accepted numeric state value was supplied. No rank-reversal conclusion is drawn.

`event_mean_time_to_happen` returned `PROBABILITY_SURFACE_EMPTY` with no matched MTTH adapter or indexed weighted block. MTTH source review therefore remains source-only and timing remains unresolved.

`probability_simulate` was not run because no uncertain-input distributions, correlations, seed, sample count, or sampling method were declared. `probability_sequence` was not run because no complete custom-pool cadence, cooldown, recovery, cap, removal, reset, timer transition, and terminal-state manifest was declared.

The AI-strategy-factor route returned no candidates and no available adapter. The event structural render remained partial because the workspace exceeded the route's node budget. The MCP source index and shared worktree moved during the audit, so every artifact above is pinned to its recorded revision and hash rather than being silently relabeled as the final local file state.

An explicit follow-up `hoi4.probability_render` for analysis `probability-741a3ac377a5e05ded4d3225` returned `PROBABILITY_ANALYSIS_NOT_CACHED` because the analysis ID was produced by a different MCP server process. The evaluate-generated ranking, matrix, unresolved, and JSON artifacts listed above remain the available rendered evidence; no replacement source-only render was treated as equivalent.

### Recommended owner fixes without application

Provide declared native fixtures or adapter support for nested country, state, event-target, global-variable, and dynamic-variable binding before making any normalized probability or rank-reversal claim. Re-run the current four-entry test pool with explicit resolved weights and compare it against the pre-drift three-entry baseline using the same four test scenario IDs. Add explicit receipt fixtures for count 1, count 2 reciprocal majors, count 2 non-reciprocal majors, and count above threshold, including `sov_nuclear_bombs_major_exchange_answered`. Add a direct severe-first-use fixture with `release_orders_suspended` true and false, and bind the delivery route, target owner/controller, fuel, airbase, distance, readiness, integrity, and strategic-loss state. Declare the breakaway cadence and terminal-state contract before using sequence analysis. These are audit recommendations only; no gameplay or weight changes were applied.
