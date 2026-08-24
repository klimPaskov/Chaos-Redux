# Event 014 Cannibalism weighted-AI and probability audit

Date: 2026-08-24

Owner: `event014_probability_audit_20260824`

Mode: read-only audit. No gameplay, event, focus, decision, mission, AI, technology, doctrine, GUI, localisation, or runtime source was edited. This handoff is the only file authored by this pass.

## Executive result

The current MCP probability service did not return a fresh Event 014 probability inspection. Both the broad source inspection and the narrower `event_option_ai_chance` inspection ended with `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; timed out awaiting tools/call after 180s`. The timeout is a tooling blocker, not a balance result.

Cached contract evidence is retained below, but the current working tree has source-snapshot drift in `common/scripted_effects/014_cannibalism_effects.txt` and `common/national_focus/014_cannibalism_focus.txt`, and the prior broad event artifact used a different event snapshot hash. Cached exact values are therefore marked conditional/cached and are not promoted as current-engine proof unless the current source hash matches the receipt.

The audit proves the distinction between deterministic score races, AI willingness scores, event-option scores, true `random_list` probabilities, MTTH timing scores, and deterministic spread cadence. It does not prove campaign frequencies for host selection, convergence, reinfection, terminal routes, decisions, missions, focuses, or AI strategies.

The most important owner actions are to refresh the MCP artifacts against the current source, expose complete deterministic candidate/score manifests to the analyzer, resolve the empty mission adapter, and either remove or wire the unused Evolution III MTTH declaration. No balance target or gameplay weight patch is recommended from this incomplete evidence.

## Workspace, references, and source snapshot

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Game target in the contracts: Operation Postern `1.19.2.0` (`d245`).

The required root `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `chaos-redux-events`, `chaos-redux-mtth`, `chaos-redux-focus-trees`, and `chaos-redux-decisions-missions` instructions were read. The required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, and national focus modding were consulted. The relevant vanilla documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including effects, modifiers, triggers, script concepts, dynamic variables, script math, and AI/decision behavior where available.

Current working-tree SHA-256 values:

| Source | Current SHA-256 | Contract or prior-artifact status |
| --- | --- | --- |
| `events/014_cannibalism.txt` | `0377739AC3D8BA119520DFC3803E44C61BFCD9A730A184DA447BDF7B1A5A8737` | Matches the local probability-contract snapshot; prior broad probability report cited `6077762438709f5883ccf90488f0b635a776a7079b7fb9071ddc6b43654641b3`, so prior event evaluations still require refresh. |
| `common/scripted_effects/014_cannibalism_effects.txt` | `6736D352684352C601F684021CDA8DDF70F65F6EC2639D09A7C7ED26E80046DC` | Differs from contract hash `469becf19e11468238f4b19e03583e0f8ec4cd44b76a82c869f03390fb6843d5`; current file has concurrent uncommitted changes outside this audit. |
| `common/scripted_triggers/014_cannibalism_triggers.txt` | `7590020DFA1B49B1765584463B979021B50EEB186AEF3BA9450B9BD1E273F25E` | Matches contract. |
| `common/mtth/014_cannibalism_mtth.txt` | `9C43B60C5D15E3EB6E5AC4C975B713302197B32CC3739B7A2AC3857E5512E84C` | Matches contract. |
| `common/decisions/014_cannibalism_decisions.txt` | `5D33DD1CE78DCC5BAE9E089181CF93D60F13AFE9F52AD5920E89EFDD5A9CFC65` | Matches contract. |
| `common/national_focus/014_cannibalism_focus.txt` | `00AB448346CE80746511E4281960677F454DBC47050AC44496EA020A7051A3E7` | Differs from the prior focus MCP snapshot (`2413e679ae5fcd4e281baf327d1fc51c9c083cf30ffc1e1f9d44470326d8bfbe`). Current uncommitted changes are Wendigo focus layout coordinates; focus probability artifacts are stale for this working tree. |
| `common/ai_strategy/014_cannibalism_warlords.txt` | `44113B630915D1EA6FF6783AE0627503BE4C6A5952371B8F94C9E315C5C9FED3` | Matches contract. |
| `common/script_constants/014_cannibalism_constants.txt` | `9ACA3CD6B767E6BCB249F1DFC73826EB87D18561865FBCB715407CCE46E8A6AD` | Matches contract. |
| `common/on_actions/014_cannibalism_on_actions.txt` | `3C107D32A9AEA742E2818CD314A4DA40FCBC14122D1BD8EC47B4B32720BC972B` | Matches contract. |

The exact audited source surfaces are `events/014_cannibalism.txt`, `common/scripted_effects/014_cannibalism_effects.txt`, `common/scripted_triggers/014_cannibalism_triggers.txt`, `common/mtth/014_cannibalism_mtth.txt`, `common/decisions/014_cannibalism_decisions.txt`, `common/national_focus/014_cannibalism_focus.txt`, `common/ai_strategy/014_cannibalism_warlords.txt`, `common/script_constants/014_cannibalism_constants.txt`, `common/on_actions/014_cannibalism_on_actions.txt`, `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`, `common/scripted_guis/014_cannibalism_scripted_gui.txt`, and the probability contracts under `docs/plans/014_cannibalism_plans/probability_contracts/`.

## MCP provenance and structural results

The required first probability call was attempted before the rest of the audit:

1. `hoi4.probability_inspect`, `workspaceId=mod_chaos_redux_ea3b2d67c2c0`, source `events/014_cannibalism.txt`, `refresh=true`: timed out after 180 seconds.
2. Narrow retry, adapter `event_option_ai_chance`, same source, `refresh=false`: timed out after 180 seconds.

The current structural Event MCP route did return a partial scan:

- `hoi4.event_inspect`, `mode=scan`, selector `file/events/014_cannibalism.txt`, `refresh=false`: `EVENT_INSPECTED_PARTIAL`, revision `4de24027e9ca18748b8dbb1f29292852eb5cd86b4befc20fb4a7c9b5ef47492a`, graph hash `3ff1b2b93e7bb0f80e2e00397f8fc67de9c44a4a969d43f031a26620ef2fe734`, artifact [event-scan-4de24027e9ca.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4488e993ebf5276aca21ec64b25c9d026bd26d97fd4436fa654c1c72d31d176f/aaf3d83d8bcb2e3a4b0933e3546e45640269d96cb680bca91221ed483fdda214/event-scan-4de24027e9ca.json). The scan reported `MCP_INLINE_FILES_TRUNCATED`; helper projections and lifecycle analysis were deferred, so it is structural partial evidence only.
- `hoi4.event_inspect`, `mode=trace`, selector `event/chaosx.nr14.1`, `refresh=false`: same partial revision/graph, artifact [event-trace-4de24027e9ca.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c587838bd6f52b819d3aa220d45bfcd11f5b71dec670de192946e5b41f4b372e/1c017ee7c53ae3b387b8f899c783c9719f43700456b685aa78b0afc41f03d76b/event-trace-4de24027e9ca.json). It is not a complete reachability proof.
- `hoi4.event_render`, `view=overview`, selector `event/chaosx.nr14.1`, `refresh=false`: timed out after 180 seconds.
- `hoi4.focus_inspect`, `treeId=cannibalism_unified_focus_tree`, `relativePath=common/national_focus/014_cannibalism_focus.txt`, `mode=national`: timed out after 180 seconds.
- `hoi4.focus_render`, same tree/path, `mode=national`: timed out after 180 seconds.

Cached contract and prior-audit artifacts retained for review:

- Deterministic selector/custom-pool inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7113f1b2aeb4c5e416d97f989fabed2142635f729244733f8e5da5644bb5c9d/a678dd5aa1c2bcfb5be56ea0becf5f2b5471fb39d30627635c017a0591eb18c5/probability-inspect-a2195480e458.json`; `poolComplete=false`, candidates `0`, unsupported `every_country`, `every_state`, `for_each_scope_loop`, `find_highest_in_array`, event-target persistence, scripted triggers, and dynamic effect side effects.
- MTTH inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed92883c79b0b9849d1052ad073589de9e5a1e81ece26b6e413fa7669967cc90/7273d43ba19227cf546aa9c01b9805f99fdd437d6f629813faaced0e388d155d/probability-inspect-a1950692f970.json`; status `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason=no_weighted_surfaces`.
- Decision inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc29dd5799af8e3871aba086353b4ade20c10bfc172915352d11cbcda03e5652/574b534bf02f4fb134835d619bc1ed51ecdc81fca8621e562f18e3f2d59220bb/probability-inspect-f0e56bfe94bb.json`; 95 candidates, 32 required inputs, `poolComplete=false`.
- Mission inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/884a3936fe58851b7ab983f77c53881241b88f735487f38058ff7a839457e63b/938f2a706ad596ecf778eb3508c9c253def1e0df6ae32f0ea46c942874fac6ed/probability-inspect-f0e56bfe94bb.json`; requested `mission_ai_will_do` was empty, with `decision_ai_will_do` suggested.
- AI-strategy inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f9b360bd13cf61f9ac0fdd41f53b0d1352df14146a09f19f664e35d7385f158/627558277a60af17dbafc95a9223c4458d2ae65e8ac127f9f677dd998db93cec/probability-inspect-02bd4b54a3b6.json`; `no_weighted_surfaces`, zero candidates.
- Synthetic sequence probe: analysis `probability-959793529f480f0842ef5cd5`, source revision `ed391ce84cbf7cbe73df82d7212a4fe7995e7f9e077717f0f92d46306a282855`, source hash `62c5a67dd4490a4699d85d1508543e29d5f21f9a68e35e11fbd1f14c6057de0a`, one candidate, horizon one day, samples 100, seed 14014, no transitions; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86df5076a6cb23b9ae20e9c945fcd230f1d0492c51bd69e3d14060b86f151f2a/3bcf87893dde2bad849c7eebcd9717bfeb0dc693443014eee7d9e215b3a0ce36/probability-959793529f480f0842ef5cd5`, sequence render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/087b0325aaa04d9778f092a41f5f827bbd5e5f59e455e5c822f395e472e4dfbd/6e20d65560f5aa333e3b49352073599cf394d3ee8b8d4deda04128aac38bbdbe/probability-probability-959793529f480f0842ef5cd5-sequence.svg`. This is a manifest parser probe, not a campaign sequence result.

`hoi4.probability_evaluate`, `hoi4.probability_sweep`, and `hoi4.probability_render` were used by the prior audit and their retained evidence is listed below. No fresh call was attempted after the explicit timeout stop. `hoi4.probability_compare` was not applicable because no owner patch exists. `hoi4.probability_simulate` was not applicable because no uncertain-input distributions, correlations, or approved seeds were declared. The source-linked queue is not a complete sequence manifest; the one-candidate probe above does not prove source cadence or transitions.

## Named scenarios and completeness

The declared scenario ids are:

| Scenario id | Intended state | Candidate pool and external-factor completeness | Classification |
| --- | --- | --- | --- |
| `E014_ELIGIBLE_WARTIME_COUNTRY` | Active ordinary wartime country with a valid origin state | Host/state scripted predicates and complete country enumeration unavailable to the adapter | Bounded/partial |
| `E014_ISOLATED_CONVOY_DEPENDENT` | Isolated theater, convoy pressure, damaged supply, remote army | Convoy/supply predicates and external map state unresolved | Bounded/partial |
| `E014_OCCUPIED_CASUALTY_HEAVY` | Occupied states, heavy casualties, low manpower, damaged logistics | Ratio/occupation loops unresolved | Bounded/partial |
| `E014_PLAYER_HOST_SAFETY` | Human country eligible as host or player-controlled Warlord | `.30` event pool was complete in the prior run; current receipt is stale event-snapshot evidence | Cached/bounded |
| `E014_WARLORD_ORIGIN_ISLAND` | Island-origin Warlord | Focus pool supplied in prior run; current focus hash differs and origin factor was unresolved | Score-only/partial |
| `E014_WARLORD_ORIGIN_SIEGE` | Siege-origin Warlord | Same focus/origin limitations | Score-only/partial |
| `E014_WARLORD_ORIGIN_MARCH` | March-origin Warlord | Same focus/origin limitations | Score-only/partial |
| `E014_UNIFIED_ROUTE` | Unified Hannibal route before terminal lock | `.81` four-option pool complete conditional on valid reveal/target; current cached receipt is stale | Cached conditional score |
| `E014_WENDIGO_ROUTE` | Wendigo route before/after transformation lock | `.81` route gates and target state external; cached receipt is stale | Cached conditional score |
| `E014_CHAOS_BELOW_1000` | Unified route below ordinary terminal threshold | Focus terminal gates unresolved; current focus artifacts stale | Score-only/partial |
| `E014_CHAOS_AT_OR_ABOVE_1000` | Unified/Wendigo route at or above terminal threshold | Terminal route gates and focus candidates unresolved | Score-only/partial |
| `E014_CONTAINMENT_OPEN` | Open emergency containment/recovery route | `.60` costs and target state unresolved | Bounded/partial |
| `E014_REINFECTION` | External reinfection/spread route with live target | `.61` event target, generation, and queue lifecycle unresolved | Bounded/partial |

Event-specific prior scenario sets include `E014_CAPTURE_COOPERATION_BASELINE_2026_08_24`, `E014_EVENT_30_PLAYER_SAFETY_2026_08_24`, `E014_EVENT_81_UNIFIED_ROUTE`, `E014_EVENT_81_DEMOCRATIC_ROUTE`, `E014_EVENT_80_CAPTURE_OUTCOMES_2026_08_24`, `E014_EVENT_71_WARLORD_SUBMISSION_RESISTANCE_2026_08_24`, `E014_EVENT_60_CONTAINMENT_BASELINES_2026_08_24`, `E014_EVENT_61_CONTAINMENT_REINFECTION_2026_08_24`, and `E014_WARLORD_PERSONALITY_POOL_2026_08_24`. The focus sweep set was `E014_FOCUS_SWEEP_NAMED_SCENARIOS_2026_08_24`.

## Weighted and probability surfaces

### Dynamic host, state, Warlord, convergence, and Wendigo selectors

Sources: `common/scripted_effects/014_cannibalism_effects.txt:1112-1497`, `:4520-4644`, `:11894-12042`, and `:18385-18601`; triggers in `common/scripted_triggers/014_cannibalism_triggers.txt:2781-3144`, `:3612-3650`, and `:5273-5370`.

These are deterministic score races, not probability-proportional pools.

- `cannibalism_select_first_host` enumerates every country satisfying `cannibalism_can_be_origin`, scores the current host, uses `find_highest_in_array`, and takes the first source-array tie. The host score starts at 2 and includes player +2, war-duration +1/+3/+5, stability +2/+3 or high-stability -2, low war support +1, casualty-ratio +2/+4/+6 at `.025/.075/.15`, manpower-ratio +2/+3 at `.015/.005`, isolation +3, damaged supply +3, remote army +4, convoy losses +2 plus threat +2/+4, external hunger, occupation +2, large occupation adding the same `occupied_state` +2 again at three or more non-core controlled states, large army +1, and Chaos tier +1 through +5. The result is rounded and clamped to 1..32.
- `cannibalism_select_highest_risk_state` enumerates controlled states satisfying `cannibalism_state_is_valid_origin` and no active cell, scores army presence, island/remote location, infrastructure, damaged port, port, supply node, occupation, prison/camp, population density, and capital penalty, then takes the first maximum. No probability is implied.
- `cannibalism_select_warlord_candidate_state` scans `global.cannibalism_node_states`, requires `cannibalism_state_can_emerge_as_warlord`, and scores node strength plus population divided by 50 and capped at 40, then adds island +12, siege +10, or march +8. Strict-greater replacement means the first node wins ties.
- `cannibalism_prepare_warlord_creation_context` uses deterministic origin precedence island, siege, march and region precedence Middle East, Europe, Asia, Africa, North America, South America, Oceania. Name selection after the region branch is the only random stage in this identity path.
- `cannibalism_select_unification_host` scores viable Warlords with base 10, human +1000, controlled states *5, divisions *2, controlled population *4 per million, Larder/alignment/network terms, port/supply/rail terms, leverage/manipulation terms, and a non-island capital-isolation penalty of -20. Human candidates are evaluated first; AI candidates are considered only when no human candidate exists. Equal scores use lower country id.
- `cannibalism_select_wendigo_merge_host` uses `every_country` with `cannibalism_is_valid_wendigo_merge_host`, human candidates first, then AI only if no human exists. The score is base 10, human +10000, divisions *10, states *6, controlled population *5 per million, clamped to 10..100000, with lower country id as the tie-break.
- `cannibalism_select_next_initial_wendigo_anchor` scans valid controlled states of the selected merge host, requires no anchor/cooldown/recovery, owner/controller identity, usable Larder, and population at least 500K, then scores base 10, capital +10000, population /100, coast +20, naval base +25, supply node +30, and rail +15. It takes the first strict maximum and repeats until three initial anchors or no candidate. Each successful anchor consumes exactly 250K population; live anchors cap at six.

The custom-pool contract returned zero candidates and `poolComplete=false` because these loops, event targets, scripted triggers, and side effects are not represented by the adapter. No exact candidate dominance, starvation, rank reversal, or selection probability is certified. The duplicated use of `occupied_state` for both the first occupied state and the `large_occupation` threshold is a tuning-review item, not a proven defect; if the second +2 is intentional it should be named separately in the contract.

### Event `ai_chance` scores

`events/014_cannibalism.txt` contains 40 options and 32 `ai_chance` blocks. `ai_chance` is an event-option score/probability-proportional-to-size mechanism over currently eligible options; it is not a country-wide campaign frequency.

| Event | Current score trace and gates | Result |
| --- | --- | --- |
| `chaosx.nr14.2` | Three options, raw bases 55/30/15. Democratic/high-integrity and authoritarian/low-integrity/stability modifiers are conditional. | Raw ordering only; no normalized current result because route state was unresolved. |
| `chaosx.nr14.20` | Three options, raw bases 45/40/15. Open/concealment/exploitation and integrity factors can stack. | Prior evaluation had two unresolved route factors; no current normalized result. |
| `chaosx.nr14.21` | Three options, raw bases 40/45/15. Open/concealment/exploitation, democratic, ritual-appropriation, and integrity factors can stack. | Prior evaluation had two unresolved route factors; no current normalized result. |
| `chaosx.nr14.30` | `.30.a` base 100; `.30.b` base 0 and trigger `is_ai = no`. | Prior cached run returned `.30.a=100`, `.30.b=0` for AI/player-safety probes. This is intended player-safety gating, but the receipt is from an older event snapshot. |
| `chaosx.nr14.60` | Humane 60, hard 30, unanswered 10; first two require payment triggers, government factors apply. | Prior run partial because route costs/gates were unresolved. |
| `chaosx.nr14.61` | Open 55, conceal 30, exploit 15; reinfection/new-actor flags and integrity/government/stability factors apply. | Prior run partial with three unresolved rows. |
| `chaosx.nr14.71` | Submission 40, surrender 15, autonomy 25, resistance 20, challenge 5; route/preparation/alignment/division factors stack. | Prior five-option run left 17 scripted gate/factor rows unresolved; no route conclusion. |
| `chaosx.nr14.80` | Anti-decapitation `.80.f` is conditional critical 100; ordinary outcomes are high/medium/medium/medium/low with urgency factors. | Six-option root pool was incomplete; diagnostic `EVENT_OPTION_FALLBACK_NOT_PROVEN`. The nested `.80.d` pool is separately listed below. |
| `chaosx.nr14.81` | Four options base 60/30/10/30, democratic `.81.a` urgency factor, fascist `.81.c` urgency factor. | Prior complete conditional score rows were `[60,30,25,30]` for fascist/unified and `[150,30,10,30]` for democratic, but current fresh proof is blocked. |

The prior `.30` analysis id was `probability-2df314e43b00d261998c992a`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3497244d5e893f90c1751bf0df87d8f2ba713b2414bf8c9027aeec344f958c7/72a5b4ae8afdb7fbb07b0da936c80f3badf4b2fa71afbdcbe581a7ee6a49762f/probability-2df314e43b00d261998c992a.json`. The prior `.71` analysis id was `probability-1d14632fdbd4dd8a015a6df1`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71f6a5b46a4c9e3089fde71a085ab7e412afbbc2e578c691fdbc36d388eeac84/6c59dbc02ff88452d0d654779b2d7e52eee8b434ddf3f368da857d57e12b3059/probability-1d14632fdbd4dd8a015a6df1.json`. The prior `.80` id was `probability-9fb40ab560bec82e6ba0acf3`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8412266e4466a061ba5843d503c5caa25275e32ba18ba1d36b9326bb50c69c77/2bc220aa0a81339ab3b5eb135974adf3083a1c01c4b0a6d6d7ee269818e78cae/probability-9fb40ab560bec82e6ba0acf3.json`. The `.81` prior ids were `probability-0c4c89f992a9709b4b69d2ab`, `probability-e018952d4ea96793487da5eb`, and combined `probability-621c764abee3b7442440c14a`; artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69b323d0b99652a5b45bf695645d4d4ff8b375d17a8815e136c9b87e1ddb6043/b31c2750b141a1d0223803439629876c77d48d5b3940746a73549a74fc08ae01/probability-0c4c89f992a9709b4b69d2ab.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1afc1ba0396122ff1f2bf84bc58db9ee157dcdd23f60035577aa63e8a6143774/78a295708cf13c935c244f84a2d65de8055709b70c30d2429515399868a8ea9d/probability-e018952d4ea96793487da5eb.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ffd49f6d9537e808284579adbb0b2dc81a64a39bbb785bb5fca32b158d3fd27/7c2ee2a08212b8ce43824c63943c7c0ff96ed8ed8e7976292bcc10a8fafe330b/probability-621c764abee3b7442440c14a.json`. These cached receipts retain scenario hashes but are tied to the prior source snapshot.

### True random pools

- `chaosx.nr14.80.d` at `events/014_cannibalism.txt:770-778` has two entries with effective weights 85 and 15. The cached MCP analysis `probability-66c8d75f2f1936727a2f0895` (scenario hash `631fa3859f4a9725b74e84d3c322205a11093cc5858560365209c9a6caebe3ae`) reported conditional `17/20` cooperation and `3/20` escape. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1794b3a229866f6541ba76e20a785f37a8f09c55a619c9127ab8eb283bba925/51f094aa6a3d33c6c233f2b2b460ffaa5d54d0456227d3b946d7fb648b1878b3/probability-66c8d75f2f1936727a2f0895.json`. This is conditional on reaching `.80.d`; it is not the chance of reaching event 80 or choosing option d. The source snapshot in the prior report differs from the current event hash, so rerun is required before treating this as current exact proof.
- Regional Warlord names at `common/scripted_effects/014_cannibalism_effects.txt:4648-4709` use seven deterministic region branches, each with four equal entries. The cached result was `1/4` per name within a selected region. The prior personality analysis `probability-139bd3d79b8c3148b17916c2` (scenario hash `b460ea46f698da1fed0023358123dab9e652c691b2576004ebf79823141f619b`) reported `1/6` for each of six personalities; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b5e534e1a274029ae69e4d35cd643d610a04d32bf4a4da084c520650d02a52f/b8aabec558afe333dbbd970fe22978a7072bc1d54b96fc28f96d401278c67de6/probability-139bd3d79b8c3148b17916c2.json`, ranking render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78d81fc0306e7af0b709bdf38c1595dbbc72f18306273d58597b90183c2d28dd/10b96ace229678fd979e25e939ed7010d51024f3f7bb737c2b47e22b1e5c03a9/probability-139bd3d79b8c3148b17916c2-ranking.svg`. These cached exact receipts are tied to the older effects snapshot and must be refreshed against the current file.

### MTTH and target-score surfaces

`common/mtth/014_cannibalism_mtth.txt:10-225` declares Evolution I, II, and III timing entries plus unified and Wendigo target decision scores. The evolution base is 90 days, with runtime clamping to 21..240 days in the Evolution I/II scheduler. Modifiers are source-ordered and include exploitation, severe hunger/cohesion, critical cell/network reach, foreign spread, Warlord count, open emergency, high integrity, local victory due date, consumed population, connected routes, and Chaos tiers.

`cannibalism_unified_target_decision_weight` and `cannibalism_wendigo_target_decision_weight` are additive/multiplicative target scores consumed by targeted decisions, not timing probabilities. Invalid targets receive an invalid factor; contamination, distant reachability, overextension, cold-front, post-lock population, and coalition-capital factors remain scope-sensitive.

The current scheduler calls `mtth:cannibalism_evolution_i_days` and `mtth:cannibalism_evolution_ii_days` at `common/scripted_effects/014_cannibalism_effects.txt:2997-3091`. `cannibalism_evolution_iii_days` is declared at `common/mtth/014_cannibalism_mtth.txt:188-225` but no call site exists; `cannibalism_try_schedule_evolution_iii` uses convergence gates, warning dates, and hard timing constants instead. This is a source/contract contradiction requiring owner resolution. It is not an exact timing or campaign-probability result.

Cached MTTH inspection returned `no_weighted_surfaces`; no exact days distribution, cumulative chance, or rank reversal is certified.

### Decisions and missions

`common/decisions/014_cannibalism_decisions.txt` contains 95 `ai_will_do` entries across containment, international response, Warlord command, unified Larder/war machine/global campaign, terminal, Wendigo command, counterwar, and mission surfaces. They are willingness scores and target races, not click probabilities. The adapter found 95 candidates but 32 required inputs and an incomplete pool.

The target-score decisions use dynamic `factor = 0` plus `modifier { ... add = <MTTH target score> }` at the unified and Wendigo target operations. This is a valid score-construction pattern under the AI/MTTH rules, but it leaves the score unresolved when target scope, cost, reachability, event targets, or scripted target predicates are not typed by MCP.

Fourteen mission lifecycle entries are declared in the source, including compact vigilance, supply corridor, rotation, investigation, prison, island, network, stop-unification, stop-transformation, unified command/Larder/war-machine/counterwar, and Wendigo terminal hunt. The requested `mission_ai_will_do` adapter discovered no candidates and suggested the decision adapter. Mission activation, timeout, objective progress, operation receipts, cleanup, and auto-start paths are therefore unresolved.

### Focus selection

`common/national_focus/014_cannibalism_focus.txt` contains three trees:

- `cannibalism_unified_focus_tree`: 108 `ai_will_do` entries.
- `cannibalism_warlord_focus_tree`: 68 `ai_will_do` entries.
- `cannibalism_wendigo_focus_tree`: 28 `ai_will_do` entries.

The prior focus candidate pools were 108, 68, and 28 respectively. Prior evaluate ids were `probability-5082fd895998e40511f8331b`, `probability-5b5b64a920031d06333b58c0`, and `probability-646105a362ee7052695dd079`; artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/45b13dad8ecdcb8b9aabbfaa70d9a1716614ead6b67263aea2e660f3c04eb24d/348be99d3ae843205d63e4e203ac2fbd487a2c8dd81cf2d1ba604ee79f3271cf/probability-5082fd895998e40511f8331b.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b95186ba51e8b7a1505a2011498b433f9980147b19a1a3966546caf9c1b3b53/d17fff770b4ed0941fed961e9771a08dcfdc7111ac35e7dbcae47c311195d562/probability-5b5b64a920031d06333b58c0.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb3e098fa3a5575e4773cf288d44b1e16491b6cd8b0b78aff7f66e85a50d66da/7d3134066b8f9ef83343d56496f4ffd4190478093f67b9443d77e805cacfcd11/probability-646105a362ee7052695dd079.json`; prior sweep id was `probability-99042c8a8d406dc94d858c46`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cabd2111fcedd2ee558ec8be398f8d577fd92a8d3d8b76d191b3e7438d7d5cad/36a8baaffb61a3bdeb3cc9a85220b21eea5a412a7ac64b80514aa2e981c82e8a/probability-99042c8a8d406dc94d858c46.json`, with ranking, matrix, sensitivity, threshold, and unresolved renders in its artifact bundle. Those runs were partial: 209 unified rows, 141 Warlord rows, and 79 Wendigo rows were unresolved. The current focus source hash differs, so no focus rank or sensitivity claim is current-certified.

Focus `ai_will_do` is an AI priority/score race. It is not a probability that a focus is clicked. Candidate availability, prerequisites, bypasses, terminal/reveal flags, route factors, Warlord origin factors, and strategy-plan multipliers must remain in the candidate pool.

### AI strategies, research, and doctrine

`common/ai_strategy/014_cannibalism_warlords.txt` has four deterministic profiles: common, island, siege, and march. The common profile uses fixed intensities 220 army/template, 180 infantry, and 160 support; island uses convoy ratio 35, one convoy factory, screen ratio 20, naval base 120; siege uses artillery 190, bunker 170, arms factory 120; march uses motorized 190, infrastructure 160, and spare units 130. `abort_when_not_enabled = yes` removes the profile when the Warlord/origin flags no longer apply. These are intensities, not selection probabilities; the adapter returned no weighted surfaces.

`common/ai_focuses/chaosx_ai_focuses.txt` contains only empty generic `biowarfare_tech` and `chemical_warfare_tech` category blocks. No Event 014-specific research or doctrine AI-weight block was found. The prior technology inspection returned zero candidates and `no_weighted_surfaces`; no doctrine probability claim is made because no Event 014 doctrine surface exists and the current required probability service is unavailable.

### Spread, reinfection, convergence, and terminal timing

Spread dispatch is deterministic. The declared route delays/strengths are retreat 24/34, prisoner transfer 32/45, convoy 38/40, volunteer return 28/32, occupation turnover 20/48, deliberate seed 30/55, conquest 14/60, and survivor 35/28. Enqueue writes nine aligned global arrays, validates source/target/generation context, sets due date `global.date + delay`, opens `.60`, and later resolves `.61` or `.62`; terminal rows are arrived, contained, or invalidated and are compacted. Pulse cadence is first 7 days, baseline 14, ritual 10, network/convergence 7; automatic route cooldown is 45 days and foreign re-enable is 90 days.

The synthetic one-candidate sequence probe is complete only as a manifest parser test. It does not execute source effects, queue producers, generation guards, recovery/cooldown, target invalidation, compaction, or terminal transitions. No reinfection recurrence, route frequency, time-to-terminal, convergence-host frequency, repetition, or snowball frequency is certified.

## Risk findings

### Dominance and starvation

- The only cached AI-zero branch is `.30.b`, intentionally gated to human countries; `.30.a` consequently dominates the AI pool. This is route protection, not a proven defect.
- In unified and Wendigo host selectors, human-first passes and the +1000/+10000 human bonuses create deterministic human dominance whenever a valid human exists. This is intentional-looking player safety but is not a probability result.
- Democratic `.81.a` receives the strongest cached conditional score because its urgency factor raises 60 to 150. The cached normalized rows were conditional score normalizations, not campaign frequencies, and the current event artifact requires refresh.
- No other option, focus, decision, mission, Warlord origin, or terminal candidate is MCP-certified starved. Adapter `NEVER_ELIGIBLE`/unresolved diagnostics cannot prove dead runtime candidates.

### Rank reversal, repetition, and exploit risk

- The prior focus sweep requested thresholds and rank reversals and produced partial sensitivity/threshold artifacts, but unresolved rows and the current focus hash prevent certification.
- No deterministic selector rank reversal can be analyzed as probability without complete candidate arrays, computed scores, external factors, and tie-break metadata.
- Flat four-way name pools and six-way personality pools have no internal dominance or starvation when all branches are present, subject to the stale-effects caveat.
- The spread queue has declared cooldown, generation, invalidation, compaction, and caps, but the MCP could not execute the stateful lifecycle. Repetition, recovery starvation, stale-row exploit, and terminal snowball risk remain unresolved rather than disproved.

### Invalid, duplicated, and contradictory surfaces

- `cannibalism_score_current_host` adds the same `occupied_state` constant once for any occupied state and again at `large_occupation >= 3`. Verify that the second +2 is intended; otherwise introduce a distinct named large-occupation component in the owner patch.
- The source declares `cannibalism_evolution_iii_days` but the runtime scheduler never calls it. Either wire the MTTH entry into the intended scheduler or remove/mark the declaration and contract row; do not tune its factors while it is unused.
- `.80` root option fallback is not proven when the captured-Warlord event target is missing or invalid. The adapter emitted `EVENT_OPTION_FALLBACK_NOT_PROVEN`; the owner should provide a complete target-gated candidate manifest and explicit invalid-target behavior before claiming capture-outcome dominance.
- The current source uses `every_country` for Wendigo merge-host enumeration while the selector contract describes an actor registry. Confirm that the trigger guarantees only valid active Wendigo actors are included and align the analyzer contract with the implementation.
- No positive weight on an impossible/dead choice is MCP-proven. All such conclusions remain unresolved until scripted availability, target validity, bypass, event-target, and route gates are typed.

## Owner priorities and required follow-up

1. After concurrent source changes settle, rerun `hoi4.probability_inspect` first for every affected adapter against the current hashes. Re-evaluate the named event scenarios and focus sweep; preserve scenario hashes and revisions.
2. Add an analyzer-readable deterministic selector manifest for host, state, Warlord origin, unification, Wendigo merge, and anchor races containing the complete eligible pool, score components, source order, lower-id/first-match tie break, and event-target/generation validity. Do not replace these deterministic selectors with random pools.
3. Type the scripted route/cost/target predicates for `.20`, `.21`, `.60`, `.61`, `.71`, `.80`, focus route factors, and the two MTTH-backed target scores. Include external government, stability, integrity, casualty/manpower, occupation, supply, convoy, event-target, actor-generation, and terminal state inputs.
4. Define an adapter-compatible mission score contract or explicitly route mission score review through complete decision candidates, including activation, timeout, objective, operation receipts, auto-start, cleanup, cooldown, and terminal states.
5. Resolve `cannibalism_evolution_iii_days` unused-vs-runtime scheduling contradiction and then compare timing under the same named scenarios.
6. Re-run `hoi4.probability_sweep` for host/decision/focus thresholds and rank reversals only after candidate pools are complete. Use `hoi4.probability_compare` only after an owner-applied patch, with the same scenario ids, pools, diagnostics, and source revisions before and after.
7. Do not use the synthetic sequence probe, raw AI scores, or static source formulas as campaign probabilities.

## Skipped analyses and exact blockers

- Fresh probability inspection: two calls timed out after 180 seconds; all current normalized probability conclusions are unresolved.
- Fresh evaluate/sweep/render: stopped after the mandatory inspect timeout per parent instruction; prior cached IDs and artifact URIs are retained but source-drift caveats apply.
- Before/after compare: no owner-applied patch or before/after source pair exists.
- Seeded simulation: no explicitly declared uncertain input distributions, correlations, or approved seeds.
- Source-linked sequence: no complete adapter-supported manifest for route producers, cadence, recovery, cooldown, invalidation, compaction, reset, and terminal transitions; only the one-candidate parser probe exists.
- Event render: timeout after 180 seconds; event inspect is partial with inline inventory truncation and deferred helper/lifecycle passes.
- Focus inspect/render: both timeout after 180 seconds; prior focus artifacts are tied to a different source hash.
- Technology/doctrine: no Event 014-specific research or doctrine weighted surface exists; no doctrine adapter conclusion is claimed.

## Handoff classification

Current source formulas and candidate counts are `source review` only. Cached MCP receipts for `.30`, `.81`, capture cooperation, names, personality, and focus sweep are `conditional/cached` and require source-hash refresh. MTTH and AI-strategy inspections are `score-only/no weighted surface`. Decision and mission inspections are `bounded/unresolved` because their candidate pools and inputs are incomplete. Dynamic host/state/origin/convergence/Wendigo selectors and spread lifecycle are `unresolved` for probability. No gameplay patch was chosen or applied.
