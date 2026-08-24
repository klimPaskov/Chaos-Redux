# Event 014 Cannibalism Probability and Weighted-AI Final Audit v4

Date: 2026-08-24

Owner: `event014_probability_audit_v4`

Mode: read-only audit; no gameplay, AI, event, focus, decision, mission, technology, GUI, localisation, or runtime source was changed by this pass.

## Executive result

The MCP pass proves several exact conditional selections and identifies the remaining weighted surfaces that cannot be certified because the adapter does not understand the scripted construct or the MCP service timed out.

The exact results are the capture sub-pool at 85/15, the regional-name pools at 1/4 each, the Warlord personality pool at 1/6 each, Event 014 `.30` at 1/0 for AI/player safety, and Event 014 `.81` at 12/29, 6/29, 5/29, 6/29 for a fascist route and 15/22, 3/22, 1/22, 3/22 for a democratic route.

Those exact values are conditional on the supplied candidate pools and typed scenario gates; they are not campaign-wide frequencies.

Focus, decision, mission, MTTH, AI-strategy, host/state/origin, spread, convergence, reinfection, and terminal-route conclusions remain score-only, bounded, partial, or unresolved unless explicitly marked exact below.

No balance patch is recommended from incomplete evidence.

If an owner applies any weight, factor, prerequisite, candidate-pool, route-gate, cadence, or timing change, the owner must request a second pass with `hoi4.probability_compare` using the same named scenarios and the same complete candidate pools.

## Required references and source surfaces

The required `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, and `chaos-redux-event-planning` instructions were read before this audit.

The offline Paradox wiki core pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding were consulted.

The vanilla documentation in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` was consulted for triggers, effects, modifiers, script concepts, and weighted/MTTH behavior.

The audited Chaos Redux sources are:

- `events/014_cannibalism.txt`
- `common/mtth/014_cannibalism_mtth.txt`
- `common/on_actions/014_cannibalism_on_actions.txt`
- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`
- `common/script_constants/014_cannibalism_constants.txt`
- `common/decisions/014_cannibalism_decisions.txt`
- `common/national_focus/014_cannibalism_focus.txt`
- `common/ai_strategy/014_cannibalism_warlords.txt`
- `common/scripted_guis/014_cannibalism_scripted_gui.txt`

The relevant Event 014 specifications and matrices are under `docs/specs/014_cannibalism_specs/`, including `specs/014_cannibalism_spec_part_9_ai_balance_and_integrations.md`, `ai_strategy_matrix.md`, `decision_mission_matrix.md`, `event_map_and_state_machine.md`, and `focus_route_matrix.md`.

## MCP provenance and operational status

The workspace used for the evidence is `mod_chaos_redux_ea3b2d67c2c0`.

The game target reported by the probability adapter is Operation Postern `1.19.2.0` with target revision `d245`.

The complete Event 014 source hash reported by the event probability artifacts is `6077762438709f5883ccf90488f0b635a776a7079b7fb9071ddc6b43654641b3`.

The event evaluation source revision used by the cached results is `8b35768e3f344792ab495d4adb31980f9a2888cedf6054f98a5e855015bc1b12`.

The focus-tree inspect artifacts use source revision `b8ec7075df481a85864a28acd1a960931820fd37229aa237dd736e8c8b2af671` and source hash `2413e679ae5fcd4e281baf327d1fc51c9c083cf30ffc1e1f9d44470326d8bfbe`.

The random-list artifacts carry their complete source revisions and hashes in their JSON; the final transcript retained the artifact identifiers but not every full revision string.

`hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, and `hoi4.probability_render` were used for the cached evidence.

`hoi4.probability_compare` was not run because no owner-applied candidate patch exists.

`hoi4.probability_simulate` was not run because the source supplies no explicit uncertain input distributions and no approved seeds/correlations for the unresolved scripted predicates.

`hoi4.probability_sequence` was not run because no complete source-linked manifest declares cadence, cooldown, recovery, removal, reset, cap, and terminal state transitions for a custom pool.

Fresh calls made near the end of the audit to `hoi4.probability_inspect`, `hoi4.event_render`, and `hoi4.gui_inspect` all failed with `timed out awaiting tools/call after 180s`.

The timeout is an MCP service blocker, not evidence that the affected surface is valid or invalid.

## Named scenarios

The named scenario contract used for the pass is:

| Scenario id | Declared state and purpose | Candidate/external-factor completeness | Classification |
| --- | --- | --- | --- |
| `E014_ELIGIBLE_WARTIME_COUNTRY` | Active ordinary wartime country with a valid origin state. | Candidate pool supplied for focus/event roots; country-state scripted predicates are only partly typed. | Bounded/partial |
| `E014_ISOLATED_CONVOY_DEPENDENT` | Isolated theater, convoy pressure, damaged supply, and remote army. | Candidate pool supplied where the adapter supports it; convoy/supply scripted triggers are not fully typed. | Bounded/partial |
| `E014_OCCUPIED_CASUALTY_HEAVY` | Occupied states, high casualty ratio, low manpower, and damaged logistics. | Candidate pool supplied where supported; occupation/casualty ratio inputs are not fully typed for deterministic selectors. | Bounded/partial |
| `E014_PLAYER_HOST_SAFETY` | Human country eligible as a host or player-controlled Warlord. | Event `.30` pool complete; host scorer itself is deterministic and not normalized by MCP. | Exact for `.30`; score-only for host scorer |
| `E014_WARLORD_ORIGIN_ISLAND` | Island-origin Warlord with island flags and convoy route. | Warlord focus pool complete; origin factor remains untyped in focus evaluation. | Score-only/partial |
| `E014_WARLORD_ORIGIN_SIEGE` | Siege-commune Warlord with siege-origin flags. | Warlord focus pool complete; origin factor remains untyped in focus evaluation. | Score-only/partial |
| `E014_WARLORD_ORIGIN_MARCH` | March-host Warlord with march-origin flags. | Warlord focus pool complete; origin factor remains untyped in focus evaluation. | Score-only/partial |
| `E014_UNIFIED_ROUTE` | Revealed unified Hannibal route before terminal lock. | Event `.81` four-option pool complete; route/event-target gates are supplied as external scenario state. | Exact conditional for `.81`; route-wide result unresolved |
| `E014_WENDIGO_ROUTE` | Revealed Wendigo Hannibal route before and after transformation lock. | Event `.81` four-option pool complete; transformation flags and target validity are external. | Exact conditional for `.81`; route-wide result unresolved |
| `E014_CHAOS_BELOW_1000` | Unified route with Chaos below the ordinary terminal threshold. | Focus pool supplied; Chaos threshold gate is not resolved for every focus row. | Score-only/partial |
| `E014_CHAOS_AT_OR_ABOVE_1000` | Unified route with Chaos at or above the ordinary/Wendigo terminal threshold. | Focus pool supplied; terminal eligibility and route flags remain partially unresolved. | Score-only/partial |
| `E014_CONTAINMENT_OPEN` | Open emergency/containment policy with active recovery operations. | Event `.60` pool supplied; cost and route triggers are partly unresolved. | Bounded/partial |
| `E014_REINFECTION` | External reinfection/spread route with a live spread target. | Event `.61` pool supplied; spread target and event-target lifecycle are partly unresolved. | Bounded/partial |

The focus sweep used the named wartime, isolation, occupation, and chaos scenarios above in scenario set `E014_FOCUS_SWEEP_NAMED_SCENARIOS_2026_08_24`.

The event and random-list evaluations used source-specific scenario sets named in the artifact JSON, including `E014_CAPTURE_COOPERATION_BASELINE_2026_08_24`, `E014_EVENT_30_PLAYER_SAFETY_2026_08_24`, `E014_EVENT_81_UNIFIED_ROUTE`, `E014_EVENT_81_DEMOCRATIC_ROUTE`, `E014_EVENT_80_CAPTURE_OUTCOMES_2026_08_24`, `E014_EVENT_71_WARLORD_SUBMISSION_RESISTANCE_2026_08_24`, `E014_EVENT_60_CONTAINMENT_BASELINES_2026_08_24`, `E014_EVENT_61_CONTAINMENT_REINFECTION_2026_08_24`, and `E014_WARLORD_PERSONALITY_POOL_2026_08_24`.

## Research and technology selection

The Event 014 source tree contains no Event 014-specific `research` AI pool, technology-selection `ai_will_do`, or doctrine-selection weight.

`common/ai_focuses/chaosx_ai_focuses.txt` contains only empty generic `biowarfare_tech` and `chemical_warfare_tech` category blocks and no Event 014, CBL, Warlord, or Wendigo identifiers.

The required technology probability inspection was nevertheless run against that file with adapter `technology_ai_will_do`.

The inspection returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason:no_weighted_surfaces`, zero candidates, zero required inputs, and no available technology adapter candidates.

Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9e780c302635ddc56cfd5dba4bac1cda8f750f4277f80a037adbebb9c8f94f8/788ab8f2e57b3f56af02a220ffc04c52ba24e24d03cac68a21015cafe1175db1/probability-inspect-47750f225b5b.json`.

The inspected source revision is `4d5badb57b316b4e9fb6197b797498480a24abc609db783ede882ea099e82876` and source hash is `47750f225b5beabb821b65ae742892b2bbd553372c5695dc937093a8f5781662`.

The matching `hoi4.tech_inspect` folders pass returned `TECH_INSPECTED_PARTIAL`, revision `674a4b57ad5962e342b90f7e0c14c7f2229ac3df5879082bedce2d43fceb86e3`, graph hash `79529f538313929694d6c14d491e06d2ab7bae3d01e785d8e09d72078ac01eb2`, and an inline-inventory truncation diagnostic.

Its authoritative folders artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/55b3a017bf72a9cf513cbde40ccc082e19966c519a77f57b277a36b38417dec7/2aca3b02dc41ea8de39f80a305a04ddbcd38dc02e268a62374fe85fe39bf25a5/technology-folders-674a4b57ad59.json`.

The matching `hoi4.tech_render` summary returned `TECH_RENDERED_PARTIAL` with helper projections deferred for the large vanilla workspace.

The rendered JSON, SVG, and PNG artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/97d616efc5dc926d565a420c0c524bf27bb2e9f167dcc6079a57c89be4b40428/93d65f51266e331aca8d9682fe744503afdf11d973daa584d74948a52288d400/technology-summary-674a4b57ad59.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/180f059b95b105bb8548a22dd80a1bc37400afff8840219dee8e1e22396b08f4/2de0b27643b413a587a3da684d0e9f42dda10154e7df57f2eb05b45291ccb617/technology-summary-674a4b57ad59.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d698e43a5fbe3e2fdae5326eff47cb1052ed5d8568276634b6ce8a03287161b/62fea1f250085204b01a6c3021111de64b9d92e1217a87f39ecc85f9029a7188/technology-summary-674a4b57ad59.png`.

Conclusion: Event 014 has no research or doctrine weighted surface to balance; generic research-category and vanilla technology evidence is recorded only to prove the absence of an Event 014-specific pool.

The doctrine probability-inspect attempt was intentionally aborted when the parent requested an immediate interim handoff, so no doctrine-adapter result is claimed; source review still found no Event 014 doctrine-selection block.

## Exact probability evidence

### Hidden capture cooperation pool

Source: `events/014_cannibalism.txt:770`, nested under `chaosx.nr14.80.d`.

The supplied pool is complete with two entries and total weight 100.

`CANNIBALISM_CAPTURE_COOPERATION_WEIGHT = 85` produces exact conditional probability `0.85`.

`CANNIBALISM_CAPTURE_ESCAPE_WEIGHT = 15` produces exact conditional probability `0.15`.

The evaluation is `probability-66c8d75f2f1936727a2f0895` with scenario hash `631fa3859f4a9725b74e84d3c322205a11093cc5858560365209c9a6caebe3ae`.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1794b3a229866f6541ba76e20a785f37a8f09c55a619c9127ab8eb283bba925/51f094aa6a3d33c6c233f2b2b460ffaa5d54d0456227d3b946d7fb648b1878b3/probability-66c8d75f2f1936727a2f0895.json`.

The ranking child artifact was produced by the same MCP analysis; its full child URI was not returned in the final transcript.

The matrix child artifact was produced by the same MCP analysis; its full child URI was not returned in the final transcript.

The ranking and matrix renders are retained by the MCP artifact bundle; the abbreviated child path above is included because the service did not return the full child URI in the final transcript.

### Warlord regional-name pools

Source: `common/scripted_effects/014_cannibalism_effects.txt:4648`, `4657`, `4666`, `4675`, `4684`, `4693`, and `4701`.

Each regional pool has four complete entries with weight one, and each evaluation returned exact conditional probability `1/4` for every entry.

The latest inspect artifact for the Europe pool is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9f8689a9adc0985efbf1c298dbfbdfaecbcaacd437affa2b17a10b77176c30ee/9f7fdbe99e0413b7a20ea46d59501438aca19b6e14b6de2d85a4db00acf1c559/probability-inspect-a2195480e458.json`.

The region evaluations are `probability-fc81d6deb5429c53d3176f3f`, `probability-2e8b6fff8f0cefad5f56a0dd`, `probability-d6ad6aa7b83d990bbfa0d78d`, `probability-6138be13c12bfce4ec4ec175`, `probability-1f26cb5b29386dbbedc8401b`, `probability-3eeabf88d532ac51ed7b45c1`, and `probability-a7bd9ad03ac6f4415447c128` for Europe, Asia, Africa, Middle East, North America, South America, and Oceania respectively.

The seven region scenario hashes are retained in the seven JSON artifacts; only their prefixes were available in the final transcript.

No dominance, starvation, or repetition risk is present inside any one of these flat four-way pools.

### Warlord personality pool

Source: `common/scripted_effects/014_cannibalism_effects.txt:4711`.

The six-entry pool is complete and all entries have equal weight, producing exact conditional probability `1/6` for each personality.

The evaluation is `probability-139bd3d79b8c3148b17916c2` with scenario hash `b460ea46f698da1fed0023358123dab9e652c691b2576004ebf79823141f619b`.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b5e534e1a274029ae69e4d35cd643d610a04d32bf4a4da084c520650d02a52f/b8aabec558afe333dbbd970fe22978a7072bc1d54b96fc28f96d401278c67de6/probability-139bd3d79b8c3148b17916c2.json`.

Rendered ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78d81fc0306e7af0b709bdf38c1595dbbc72f18306273d58597b90183c2d28dd/10b96ace229678fd979e25e939ed7010d51024f3f7bb737c2b47e22b1e5c03a9/probability-139bd3d79b8c3148b17916c2-ranking.svg`.

The personality matrix child artifact was produced by the same MCP render; its full child URI was not returned in the final transcript.

The flat pool has no dominance or starvation risk, subject to the caller always reaching this pool with all six entries available.

## Event option probability surfaces

The complete-source event inspect discovered 40 option `ai_chance` blocks and 32 options containing `ai_chance` syntax after deterministic options are excluded.

The broad inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9737ca9bda2c24d11807ba943b75d7fd083504b7af705d9160906df1d69059da/037312b503ec1052845f6aa56edd64f44cf540adb2a3dd3f5239323cd778d26c/probability-inspect-607776243870.json`.

The broad event pool is not complete for normalized probabilities because the source contains event-target and scripted-trigger gates that are not all typed by the adapter.

### Opening policy and evolution responses

`chaosx.nr14.2` has options `.2.a`, `.2.b`, and `.2.c` with base weights from `cannibalism_policy_effect` and government, command-integrity, stability, and route modifiers.

The empty-state evaluation proved the raw base ordering `a = 55`, `b = 30`, `c = 15` but left government, meter, and stability factors unresolved, so no normalized option probability is claimed.

The named democratic/fascist state evaluation resolved the democratic factor on `.2.a` and the authoritarian factor on `.2.b` and `.2.c`, but meter and stability remained unresolved.

This surface is bounded modifier evidence, not an exact probability.

`chaosx.nr14.20` and `chaosx.nr14.21` were evaluated in ordinary-wartime, isolated-convoy, and occupied/casualty-heavy route scenarios with complete three-option candidate pools.

The adapter returned partial results with two unresolved scripted route factors for each root, including clean, concealment, exploitation, and disfavored-route predicates.

No normalized probability or route dominance claim is valid for `.20` or `.21` until those predicates are typed.

### Player host safety

`chaosx.nr14.30` has `.30.a` for remaining in place and `.30.b` for the human-only country switch.

The evaluation is `probability-2df314e43b00d261998c992a` in `E014_EVENT_30_PLAYER_SAFETY_2026_08_24`; the JSON artifact retains the complete scenario hash.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3497244d5e893f90c1751bf0df87d8f2ba713b2414bf8c9027aeec344f958c7/72a5b4ae8afdb7fbb07b0da936c80f3badf4b2fa71afbdcbe581a7ee6a49762f/probability-2df314e43b00d261998c992a.json`.

The complete two-option pool returned `.30.a = 100` and `.30.b = 0` for the AI decision scenario, with `.30.b` ineligible because `is_ai = no` is false.

The player-host scenario returned `.30.a = 100` and `.30.b = 0` as an eligible-but-zero AI weight, while the player can still see the option through the human trigger.

This proves no AI host-switch hazard; `.30.a` dominance and `.30.b` starvation are intentional route protection rather than a balance defect.

### Warlord submission and resistance

`chaosx.nr14.71` contains five options for retain-command submission, surrender, autonomy, resistance, and challenge.

The complete five-option root evaluation is `probability-1d14632fdbd4dd8a015a6df1`; the JSON artifact retains the complete scenario hash.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/71f6a5b46a4c9e3089fde71a085ab7e412afbbc2e578c691fdbc36d388eeac84/6c59dbc02ff88452d0d654779b2d7e52eee8b434ddf3f368da857d57e12b3059/probability-1d14632fdbd4dd8a015a6df1.json`.

The aligned-submission, defiant-resistance, and player-host scenarios left 17 scripted gate/factor rows unresolved.

Options `.71.a`, `.71.b`, and `.71.e` were not proven eligible because `cannibalism_current_warlord_can_submit_without_displacing_player` and `cannibalism_current_warlord_can_challenge_active_unifier` are not typed by the adapter.

The `.71.c` autonomy and `.71.d` resistance traces are also not normalized because route flags, alignment, division strength, and external target validity are incomplete.

No conclusion about which Warlord origin is more likely to submit, resist, or challenge is certified.

### Capture outcomes and hidden cooperation

`chaosx.nr14.80` contains the anti-decapitation escape option and five ordinary captured-Warlord outcomes.

The evaluation is `probability-9fb40ab560bec82e6ba0acf3` in the player-host, occupied/casualty-heavy, and high-chaos scenarios; the JSON artifact retains the complete scenario hash.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8412266e4466a061ba5843d503c5caa25275e32ba18ba1d36b9326bb50c69c77/2bc220aa0a81339ab3b5eb135974adf3083a1c01c4b0a6d6d7ee269818e78cae/probability-9fb40ab560bec82e6ba0acf3.json`.

The supplied six-option root pool was partial because all options were gated by the captured-Warlord event target and no unconditional fallback was proven.

The adapter diagnostic is `EVENT_OPTION_FALLBACK_NOT_PROVEN`.

The separate nested random pool at `.80.d` is exact 85/15 as reported above once `.80.d` is reached.

### Unified and Wendigo captured-Hannibal outcomes

`chaosx.nr14.81` has a complete four-option pool and is the strongest route-comparison evidence in this audit.

The fascist/unified scenario evaluation is `probability-0c4c89f992a9709b4b69d2ab`; the JSON artifact retains the complete scenario hash.

Its exact weights are `.81.a = 60`, `.81.b = 30`, `.81.c = 25`, and `.81.d = 30`, for conditional probabilities `12/29`, `6/29`, `5/29`, and `6/29`.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69b323d0b99652a5b45bf695645d4d4ff8b375d17a8815e136c9b87e1ddb6043/b31c2750b141a1d0223803439629876c77d48d5b3940746a73549a74fc08ae01/probability-0c4c89f992a9709b4b69d2ab.json`.

The democratic scenario evaluation is `probability-e018952d4ea96793487da5eb`; the JSON artifact retains the complete scenario hash.

Its exact weights are `.81.a = 150`, `.81.b = 30`, `.81.c = 10`, and `.81.d = 30`, for conditional probabilities `15/22`, `3/22`, `1/22`, and `3/22`.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1afc1ba0396122ff1f2bf84bc58db9ee157dcdd23f60035577aa63e8a6143774/78a295708cf13c935c244f84a2d65de8055709b70c30d2429515399868a8ea9d/probability-e018952d4ea96793487da5eb.json`.

The four-scenario combined run `probability-621c764abee3b7442440c14a` covered Wendigo, democratic, Chaos below 1000, and Chaos at or above 1000 with a complete four-option pool and zero unresolved option rows.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ffd49f6d9537e808284579adbb0b2dc81a64a39bbb785bb5fca32b158d3fd27/7c2ee2a08212b8ce43824c63943c7c0ff96ed8ed8e7976292bcc10a8fafe330b/probability-621c764abee3b7442440c14a.json`.

The exact `.81` values are conditional on the event having reached its valid reveal and captured-Hannibal target; they do not establish the probability of reaching unified versus Wendigo routes or of crossing Chaos 1000.

The government modifier creates a large but source-intended rank shift toward `.81.a` on democratic countries.

## Dynamic host, state, origin, spread, convergence, and terminal selectors

The prefire host selection is defined in `common/scripted_effects/014_cannibalism_effects.txt:1112-1365`.

The host score includes player safety, war duration, stability, war support, casualty ratio, manpower ratio, isolation, damaged supply, remote army, convoy pressure, external hunger, occupation count, army size, Chaos tiers, and a final clamp.

The eligible pool is `every_country` with `cannibalism_can_be_origin = yes`.

The state score at `:1367` includes army presence, island/remote position, infrastructure, damaged port, port, supply node, occupation, prison/camp, external hunger, and population density.

Warlord origin selection at `:4520` uses deterministic origin-specific branches for island, siege, and march.

Unified host selection at `:11893` uses a deterministic scored array with human preference, alignment, spread, ports, supply, rail, capital, leverage, manipulation, isolation, and a stable tie-break.

Wendigo merge-host selection at `:18373-18455` uses deterministic score accumulation with human preference, divisions, controlled states, controlled population, clamping, and lowest-id tie-breaking.

Wendigo anchor selection at `:18461-18568` scores capital, population, coast, naval base, supply node, and rail and selects the highest valid state.

The `custom_weighted_pool` inspector was started for the host, state, Warlord-origin, unified-host, Wendigo-merge-host, and Wendigo-anchor surfaces.

Each returned `poolComplete = false`, zero candidates, and no usable normalized pool because `find_highest_in_array`, deterministic arrays, event-target pointers, and loop-built candidate scopes are not represented by the adapter.

The exact MCP diagnostic is `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason:no_weighted_surfaces` for the MTTH/strategy requests and zero-candidate custom-pool discovery for deterministic selectors.

These selectors are score races with deterministic selection order, not probability-proportional samples.

No exact probability, seeded frequency, dominance, starvation, or rank-reversal claim is valid for them.

The owner should not convert these deterministic selectors to random pools merely to make the adapter happy.

If quantitative review is required, the owner should expose a read-only analyzer manifest containing the complete eligible candidate set, each computed score, the stable tie-break rule, and the scenario state.

## Focus selection and focus-route evidence

The structural focus surfaces are `cannibalism_warlord_focus_tree`, `cannibalism_unified_focus_tree`, and `cannibalism_wendigo_focus_tree` in `common/national_focus/014_cannibalism_focus.txt`.

The complete candidate pools supplied to the probability adapter were 68 Warlord focuses, 108 unified focuses, and 28 Wendigo focuses.

Unified inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/645cda143b4f8a8a215d7a47c23740dacd53af9bfd2ad46e9bbe46000ebe2dc8/694af333ebe09f563157ee63d6874ab196616c9bc379725627b73ca92af814df/probability-inspect-2413e679ae5f.json`.

Warlord inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0a0140cc31ef5bb94d7fa01825f9bd2b7786601fc31dec89db191b04a88141c/783e5fe23a2163371178624e2133b4dc721dbbd5e6f66be30a16bccb0e579ae9/probability-inspect-2413e679ae5f.json`.

Wendigo inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/339e0cda24ac48305140475bda031a0c40a84629ac93cb291526aafe414b3a78/00d65034edfaf9a8d1587a888edb7c03416dedfd03563640bb6a07c3f60463af/probability-inspect-2413e679ae5f.json`.

The unified evaluation `probability-5082fd895998e40511f8331b` used five named wartime, isolation, occupation, and Chaos scenarios and 540 data rows from 108 focuses across five scenarios; the JSON artifact retains the complete scenario hash.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/45b13dad8ecdcb8b9aabbfaa70d9a1716614ead6b67263aea2e660f3c04eb24d/348be99d3ae843205d63e4e203ac2fbd487a2c8dd81cf2d1ba604ee79f3271cf/probability-5082fd895998e40511f8331b.json`.

The Warlord evaluation `probability-5b5b64a920031d06333b58c0` used island, siege, and march origin scenarios and 204 data rows from 68 focuses across three scenarios; the JSON artifact retains the complete scenario hash.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b95186ba51e8b7a1505a2011498b433f9980147b19a1a3966546caf9c1b3b53/d17fff770b4ed0941fed961e9771a08dcfdc7111ac35e7dbcae47c311195d562/probability-5b5b64a920031d06333b58c0.json`.

The Wendigo evaluation `probability-646105a362ee7052695dd079` used unified-route, Wendigo-route, and high-Chaos scenarios and 84 data rows from 28 focuses across three scenarios; the JSON artifact retains the complete scenario hash.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb3e098fa3a5575e4773cf288d44b1e16491b6cd8b0b78aff7f66e85a50d66da/7d3134066b8f9ef83343d56496f4ffd4190478093f67b9443d77e805cacfcd11/probability-646105a362ee7052695dd079.json`.

The focus evaluations were `PROBABILITY_ANALYZED_PARTIAL` because 209 unified rows, 141 Warlord rows, and 79 Wendigo rows contained unresolved route, origin, terminal, or helper factors.

Examples include `NEVER_ELIGIBLE` terminal/reveal focuses in states without typed route flags, and Warlord origin focuses whose `warlord_origin_factor` was supplied as an untyped string state.

Focus scores are AI willingness/priority scores and are not click probabilities.

The focus sweep `probability-99042c8a8d406dc94d858c46` used `cannibalism_larder`, `cannibalism_world_hostility`, and `cannibalism_frenzy` paths at six sweep points with rank-reversal and pairwise requests.

The sweep returned partial results with 209 unresolved rows but did produce ranking, matrix, sensitivity, threshold, and unresolved artifacts.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cabd2111fcedd2ee558ec8be398f8d577fd92a8d3d8b76d191b3e7438d7d5cad/36a8baaffb61a3bdeb3cc9a85220b21eea5a412a7ac64b80514aa2e981c82e8a/probability-99042c8a8d406dc94d858c46.json`.

The focus-sweep ranking child artifact was produced under the same analysis ID; its full child URI was not returned in the final transcript.

The focus-sweep matrix child artifact was produced under the same analysis ID; its full child URI was not returned in the final transcript.

The focus-sweep sensitivity child artifact was produced under the same analysis ID; its full child URI was not returned in the final transcript.

The focus-sweep threshold child artifact was produced under the same analysis ID; its full child URI was not returned in the final transcript.

The sweep artifacts are review evidence, not a complete rank-reversal certification because unresolved rows can change the live candidate set.

The structural focus renders completed without blocking diagnostics for all three trees, although the unified layout reported 18 layout detours and one vanilla localisation warning.

Unified focus HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d7f8dedc1d0fdf3264341acf249f184bb5066426b427c0d0b227091d0efbfd7/99e342e66cd7c3b1598b5d435de3a97a3fb2c33a22462ce77d03ded3268f9be0/cannibalism_unified_focus_tree.focus.html`.

Warlord focus HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/309685252c4c928a5a7a82e3b5dea2e1ad54a8c594db21dab4a5c8d775e7ca07/541445b5d6290fe3d1380af5ea2f379ecb796c5b74610a4e6e35f21f68575ae4/cannibalism_warlord_focus_tree.focus.html`.

Wendigo focus HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9288b9bab68f6f2de2f996c6c392e7172c58ef85287c1af410c423be3f3704d5/a38dcd9584b000a3dd3267b5ed05488ee5fea57250ef973d094a99c7d7b9bd31/cannibalism_wendigo_focus_tree.focus.html`.

## MTTH and evolution timing

The MTTH source is `common/mtth/014_cannibalism_mtth.txt`.

The entries are `cannibalism_evolution_i_days`, `cannibalism_evolution_ii_days`, `cannibalism_evolution_iii_days`, `cannibalism_unified_target_decision_weight`, and `cannibalism_wendigo_target_decision_weight`.

The evolution entries include exploitation, severe hunger, critical cell strength, foreign spread, open emergency, high integrity, containment due date, Warlord count, network reach, consumed population, connected routes, and Chaos-tier modifiers.

The two target-decision entries use invalid-target factors plus population, supply, cells, prison, port, stability, rail/naval, coalition, enemy, adjacency, contamination, distant-route, overextension, cold-front, post-lock population, and post-lock capital factors.

`hoi4.probability_inspect` with `event_mean_time_to_happen` returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason:no_weighted_surfaces`, zero candidates, and no usable adapter for the file.

A line-scoped refresh attempt also timed out after 180 seconds.

Therefore no effective MTTH days, cumulative chance, timing distribution, rank reversal, or threshold claim is made.

The six unified targeted decisions and the Wendigo targeted decisions remain unresolved as quantitative weighted pools because the adapter cannot bind the MTTH entry to the targeted `FROM` scope and scripted predicates.

The owner should expose typed target-score inputs or an analyzer manifest before requesting a timing/target comparison.

## Decision and mission AI scores

The source is `common/decisions/014_cannibalism_decisions.txt`.

The source parser found 95 `ai_will_do` blocks, including operational decisions, maintained mission entries, and read-only tracker entries.

The broad prior MCP discovery artifact reported 95 candidates, `poolComplete = false`, 32 required inputs, and no normalized result: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a96791ee01aeda97abe575041d783d754beb67e74fd8809509500/9d8828873c26b9a83e1be6df65856969f29e39154c7824a97d08232faab24cca/probability-inspect-7094c91933c5.json`.

The current complete-pool refresh with all 95 ids and a three-id targeted refresh both timed out at 180 seconds.


The complete source-discovered 95-id `ai_will_do` candidate list supplied for the failed refresh is:

```text
cannibalism_end_terror_exploitation
cannibalism_joint_suppression_operation
cannibalism_interdict_likely_convergence_host
cannibalism_blockade_island_host
cannibalism_land_against_island_host
cannibalism_rescue_island_host_survivors
cannibalism_identify_and_bury_victims
cannibalism_rebuild_feeding_state_institutions
cannibalism_complete_memorial_and_inspection_site
cannibalism_ratify_international_inspection_compact
cannibalism_emergency_ration_audit
cannibalism_restore_supply_corridor
cannibalism_rotate_compromised_formations
cannibalism_forensic_recovery_teams
cannibalism_search_missing_burial_party
cannibalism_protect_burial_and_medical_details
cannibalism_public_court_martial
cannibalism_conditional_amnesty
cannibalism_seal_transfer_records
cannibalism_authorize_terror_battalion
cannibalism_feed_selected_prisoners
cannibalism_replace_compromised_officer_chain
cannibalism_infiltrate_ritual_cell
cannibalism_break_ritual_economy
cannibalism_reconnoiter_silent_island
cannibalism_liberate_feeding_state
cannibalism_prepare_network_submission
cannibalism_prepare_network_resistance
cannibalism_humane_route_screening
cannibalism_seal_inbound_route
cannibalism_unified_absorb_warlord
cannibalism_unified_appoint_governor
cannibalism_unified_purge_rival
cannibalism_unified_issue_continental_command
cannibalism_unified_centralize_larder
cannibalism_unified_convert_captured_workshop
cannibalism_unified_abandon_exhausted_frontier
cannibalism_unified_designate_feeding_capital
cannibalism_unified_rapid_consumption
cannibalism_unified_managed_consumption
cannibalism_unified_mobile_consumption
cannibalism_unified_battlefield_consumption
cannibalism_unified_establish_air_program_foundation
cannibalism_unified_create_cannibal_legion
cannibalism_unified_surge_cannibal_legion
cannibalism_unified_recruit_island_reavers
cannibalism_unified_recruit_siege_eaters
cannibalism_unified_recruit_march_predation_column
cannibalism_unified_raise_bone_guard
cannibalism_unified_launch_continental_hunt
cannibalism_unified_collapse_enemy_front
cannibalism_unified_launch_naval_hunt
cannibalism_unified_process_convoy_harvest
cannibalism_unified_build_silent_anchorage
cannibalism_unified_launch_air_interdiction
cannibalism_unified_seed_major_enemy_army
cannibalism_unified_prepare_global_campaign
cannibalism_unified_issue_terror_ultimatum
cannibalism_unified_provoke_border_incident
cannibalism_unified_integrate_postwar_state
cannibalism_unified_destroy_coalition_hub
cannibalism_unified_convert_counterwar_pressure
cannibalism_unified_begin_terminal_mobilization
cannibalism_unified_terminal_consume_controlled_state
cannibalism_consume_controlled_state
cannibalism_raise_scavenger_warband
cannibalism_raise_feast_cohort
cannibalism_raise_origin_specialist
cannibalism_raise_bone_guard
cannibalism_raise_network_cadre
cannibalism_emergency_reinforcement
cannibalism_seed_foreign_formation
cannibalism_intensify_feeding_district
cannibalism_abandon_exhausted_state
cannibalism_align_local_ranks
cannibalism_synchronize_warlord_attack
cannibalism_island_ambush_convoys
cannibalism_siege_ambush_relief_column
cannibalism_march_raid_supply_depot
cannibalism_designate_transformation_anchor
cannibalism_fortify_transformation_anchor
cannibalism_consume_transformation_anchor_population
cannibalism_train_additional_wendigo_packs
cannibalism_freeze_supply_corridor
cannibalism_accelerate_transformation_countdown
cannibalism_stabilize_transformation_countdown
cannibalism_wendigo_launch_terminal_hunt
cannibalism_wendigo_press_terminal_hunt
cannibalism_muster_wendigo_pack_from_enemy_death_receipt
cannibalism_activate_inherited_winter_cell
cannibalism_identify_transformation_anchor
cannibalism_assault_transformation_anchor
cannibalism_disrupt_transformation_logistics
cannibalism_break_wendigo_recruitment_site
cannibalism_break_wendigo_terminal_hunt
```

The mission adapter returned `requestedAdapter: mission_ai_will_do`, `suggestedAdapter: decision_ai_will_do`, `discoveryReason: requested_adapter_empty`, zero mission candidates, and 95 available source candidates.

No mission score or decision score is certified by current MCP probability evidence.

The decision surface includes early containment, international response, Warlord command, unified Larder/War Machine/global campaign, terminal mobilization, and Wendigo command/counterwar families.

The source and decision matrix show route, cost, target validity, cooldown, cap, equipment, manpower, supply, population, and generation gates, but static source review is not a substitute for the required probability pass.

The owner should either provide mission-adapter support or split mission entries into a declared decision-compatible score pool with explicit candidate completeness.

## AI strategies

The source is `common/ai_strategy/014_cannibalism_warlords.txt`.

The four profiles are `cannibalism_warlord_common_profile`, `cannibalism_warlord_island_profile`, `cannibalism_warlord_siege_profile`, and `cannibalism_warlord_march_profile`.

The profiles use `build_army`, equipment production factors, template priority, role ratios, convoy and screen ratios, naval-base building, artillery, bunkers, arms factories, motorized production, infrastructure, and spare-unit factors.

`hoi4.probability_inspect` with `ai_strategy_factor` returned `PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason:no_weighted_surfaces`, zero candidates, and no available probability adapter.

These values are strategy intensities, not direct selection probabilities.

No dominance, starvation, repetition, or strategy rank-reversal conclusion is certified.

## Random lists not yet certifiable

The full scripted-effects scan found 42 nested random-list entries but `poolComplete = false` because it combined multiple unrelated pools.

The line-specific regional and personality pools above were complete and exact.

The dynamic pools at `common/scripted_effects/014_cannibalism_effects.txt:6161`, `6197`, and `6239` were inspected in an earlier cached pass as two-entry, three-entry, and three-entry pools with complete candidate counts and zero unresolved source inputs at inspection time.

The current refresh attempts for line 6161 timed out at 180 seconds, so no exact normalized values or rendered artifacts from those dynamic weights are promoted here.

Those pools are the audit-success/failure, forensic full/partial/failure, and missing-burial-party full/partial/failure outcomes.

Their weights depend on open-emergency, concealment, command-integrity, and event-target feeding-program state.

They require scenario evaluations before any probability or repetition claim can be made.

## Spread, reinfection, convergence, and terminal routes

Spread and reinfection are wired through `common/on_actions/014_cannibalism_on_actions.txt`, the spread queue helpers in `common/scripted_effects/014_cannibalism_effects.txt`, and events `.60`, `.61`, and `.62`.

The on-action path is lifecycle- and generation-aware and does not use a world-wide daily iteration, but queue cadence, route replacement, and target invalidation are not represented as a normalized MCP probability pool.

Event `.60` containment scenarios returned partial results with 20 unresolved rows in `probability-53f3063dd71386156cf469fc`.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19461590cef1c6486f03bdedf10654437b9926bccfc2670dbf62bcee478f3006/6dfe7cc1084919417b2c70333df507b596a110fd4643b0f4e64258901fe2f95c/probability-53f3063dd71386156cf469fc.json`.

Event `.61` reinfection scenarios returned partial results with three unresolved rows in `probability-925ebf20da754347e06b7d7c`.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5c8098046d057ebe306b93664f5bcf0d9a120ca79100226ca78785e7b7bb500/f0b9f28acaecdc555f21b599732ac15ff7e98a8ca9a2c9283fd0c95933a36f6e/probability-925ebf20da754347e06b7d7c.json`.

Event `.62` is deterministic and has no `ai_chance` pool.

Convergence and terminal route selectors use the deterministic host/state score helpers and targeted decisions described above.

The ordinary terminal route requires a unified country, terminal route flag, all operational packages, no existing world end, Chaos above 1000, Network Reach at least 92, controlled states above 35, consumed population at least 25,000K, and Larder at least 750.

The Wendigo terminal route requires the transformed Hannibal country, locked transformation, no existing world end, and Chaos above 1000.

The exact reach probability, time-to-terminal, reinfection recurrence, and convergence-host frequency remain unresolved because the MCP adapter cannot evaluate the stateful event-target queue and deterministic array selectors.

No seeded simulation or sequence analysis is justified without a manifest declaring pulse cadence, recovery/cooldown, queue removal, generation reset, host replacement, and terminal transitions.

## Structural event and GUI evidence

`hoi4.event_inspect` completed a partial workspace scan for Event 014 with revision `2ff7afa1197ed490fdb459863f83602ebc90056b7a21d375ea6aba5d60e94775` and graph hash `e6c6235d6f921a68432087240c6fdb3282af5b5cf000bcff7eeed0e2a070c1c7`.

The event artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4630f01878c901d900ccd8293c187c19fa9f05aa4c571d1ac2ecadf17dc84329/2fc5e990934aea42a0a941b6057b48c4a9fd61ccedf2baf3916f022fac9e9438/event-scan-2ff7afa1197ed.json`.

The scan reported `MCP_INLINE_FILES_TRUNCATED` and deferred event analysis, so no full event reachability or terminal proof is claimed.

The required `hoi4.event_render` unresolved view was attempted after the scan and timed out after 180 seconds.

The dedicated Event 014 GUI windows are `cannibalism_early_header_window`, `cannibalism_network_window`, `cannibalism_warlord_command_window`, `cannibalism_revealed_command_window`, and `cannibalism_wendigo_command_window`.

The required `hoi4.gui_inspect` call for `cannibalism_early_header_window` with scenario `event014_probability_audit_v4` timed out after 180 seconds.

Existing decision-audit evidence also records an MCP artifact-storage failure and an earlier GUI-render timeout for the same windows.

No GUI probability or visual-selection claim is made.

## Findings by risk type

### Dominance

Exact dominance is proven only for `.30.a` in the AI/player safety scenario because `.30.b` is human-only and has zero AI weight.

The democratic `.81.a` increase is a quantified government-factor shift, not an unbounded dominance defect.

No focus, decision, mission, host, or terminal dominance claim is valid while candidate gates remain unresolved.

### Starvation

The hidden capture escape entry is not starved inside the nested random pool because it has exact weight 15/100.

The `.30.b` AI-zero result is intentional player-only gating.

No other option, focus, decision, mission, Warlord origin, or route is certified starved.

### Rank reversal

The focus sweep requested rank-reversal analysis and rendered sensitivity/threshold views, but unresolved rows prevent complete certification.

No custom deterministic selector or MTTH rank reversal was analyzable by the current adapter.

### Repetition and snowball risk

The flat random pools have no internal repeated-entry bias beyond their declared equal weights.

No cadence-level repetition, recovery starvation, cap bypass, or snowball frequency claim is valid without the missing sequence manifest and state transitions.

The deterministic host and terminal selectors can snowball by score accumulation in principle, but this is a design-risk hypothesis, not MCP-proven probability evidence.

### Invalid or dead candidates

The focus and event evaluations reported `NEVER_ELIGIBLE` or unresolved route rows for terminal, reveal, origin, event-target, and scripted-helper gates.

The adapter did not prove that every dead candidate is excluded at runtime, so no source patch is prescribed solely from those diagnostics.

## Owner patch recommendations, without applying them

No gameplay weight patch is required by the exact evidence in this audit.

If quantitative coverage is required, the owner should consider the following analyzer-facing or narrowly scoped source improvements and then rerun the same scenarios.

- Expose deterministic host/state/origin/convergence/Wendigo candidate arrays to the probability analyzer with a complete candidate set, computed score, eligibility reason, and stable tie-break metadata.
- Type the scripted route predicates used by `.20`, `.21`, `.60`, `.61`, `.71`, `.80`, focus gates, and the two target-decision MTTH entries, including event-target existence and generation values.
- Add an adapter-compatible mission score surface or explicitly declare that mission AI uses the decision adapter and provide a complete candidate map.
- Add an adapter-compatible AI-strategy factor surface for the four Warlord profiles if quantitative strategy comparison is required.
- Publish a sequence manifest for spread/reinfection, deterministic host replacement, recovery cooldowns, terminal locks, and queue cleanup before requesting simulation or sequence analysis.

The owner must apply any accepted source patch first.

After each owner patch, rerun `hoi4.probability_inspect` and `hoi4.probability_evaluate` for the affected adapter, rerun the existing focus sweep or an equivalent named sweep, and run `hoi4.probability_compare` with the exact same scenario set, candidate pool, source revision pair, and diagnostic thresholds.

The compare must report score traces separately from normalized probabilities and must retain before/after artifact URIs and scenario hashes.

## Skipped analyses and blockers

No before/after comparison was run because there is no owner-applied before/after patch.

No seeded simulation was run because uncertain external inputs and approved correlations/seeds were not declared.

No sequence analysis was run because cadence, cooldown, recovery, reset, removal, and terminal manifests are incomplete.

No exact MTTH timing was run because the MTTH adapter returned `no_weighted_surfaces` and the source-line refresh timed out.

No exact decision or mission probability was run because the decision refresh and mission adapter returned no usable complete pool, followed by 180-second service timeouts.

No exact AI-strategy probability was run because the strategy adapter returned `no_weighted_surfaces` with zero candidates.

No exact host/state/origin/convergence/Wendigo selector probability was run because the custom-pool adapter returned zero candidates for deterministic array selectors.

No full event or GUI render was completed because the final `event_render` and `gui_inspect` calls timed out after 180 seconds.

These are unresolved analyses, not simplifications of the gameplay system.

## Handoff conclusion

The exact nested random pools and the exact `.30` and `.81` event option results are safe to carry forward as conditional MCP evidence.

The focus pass proves candidate-pool coverage and produces useful score/sensitivity artifacts, but unresolved route rows prevent probability certification.

The host, state, origin, convergence, spread, reinfection, terminal, MTTH, decision, mission, and AI-strategy surfaces require an owner-supported analyzer representation or a recovered MCP service before balance claims can be made.

No gameplay changes were made, no gameplay commit is required from this read-only audit, and any owner patch must be followed by a same-scenario `probability_compare` pass.
