# Event 006 current probability audit (2026-08-29)

Status: **UNRESOLVED — current HOI4 probability and structural MCP routes are unavailable.** This is a read-only audit of the current source snapshot and accepted Event 006 specifications. No gameplay, AI, event, focus, decision, mission, strategy, MTTH, localisation, workbook, or runtime files were edited.

## Scope and authority

The audited surface is Event 006, Independence Wave, including automatic package allocation, root and support-event `ai_chance`, decision and mission `ai_will_do`, national-focus `ai_will_do`, advisor `ai_will_do`, AI strategy factors, formable-congress success/failure selection, SCN-008 ranking and target selection, and evolution MTTH timing.

The current design authority is `docs\plans\006_independence_wave_plans\006_source_of_truth_map.md`, `docs\specs\006_independence_wave_specs\README.md`, and the seven accepted specification parts under `docs\specs\006_independence_wave_specs\specs\`.

The current implementation-facing event authority is `docs\events\006_independence_wave\overview.md`. It records Event 006 as **HOLD / PARTIAL**, with 32 content-attested selectable packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows, including eight adapter-only rows that remain fail-closed.

The current source authority retains the automatic ladder `3/4/5/7/10`, with World Collapse also targeting `10`, and keeps the public Event 006 report as the first player-facing entry point.

I read `AGENTS.md`, `.agents\skills\chaos-redux-subagents\SKILL.md`, `.agents\skills\chaos-redux-events\SKILL.md`, `.agents\skills\chaos-redux-mtth\SKILL.md`, and `.agents\skills\chaos-redux-decisions-missions\SKILL.md`.

I also consulted the required offline Paradox wiki pages in `paradox_wiki\`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, AI focuses, and National focus modding.

I consulted the relevant vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\`, including `script_concept_documentation.md`, `triggers_documentation.md`, `effects_documentation.md`, `modifiers_documentation.md`, `script_math_functions.md`, and `script_collection_input.md`.

## Required MCP pass and exact blocker

The required first call was attempted against the current Event 006 root/support event source with the probability adapter route:

```text
tools.mcp__hoi4_agent_tools__hoi4_probability_inspect({
  adapter: "event_option_ai_chance",
  source: { paths: ["events/006_independence_wave.txt", "events/006_independence_wave_support_events.txt"] },
  refresh: true
})
```

The exact result was `TypeError: tools.mcp__hoi4_agent_tools__hoi4_probability_inspect is not a function`.

The same runtime has no callable entries matching probability, `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.focus_inspect`, or `hoi4.focus_render` in its exposed tool catalog. The repository still configures the server at `[mcp_servers.hoi4_agent_tools]` in `.codex\config.toml` with command `hoi4-agent-tools.cmd`, so this is an MCP tool-exposure/transport blocker rather than a source absence.

Because the mandatory inspect call is unavailable, no current `probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_render`, `probability_sequence`, or `probability_simulate` call could be made. No current MCP artifact URI, MCP source revision, scenario hash, comparison ID, ranking render, timing render, or unresolved render was produced in this audit.

The failed route is recorded here instead of substituting hand arithmetic or a source-only claim for engine evidence.

## Current source inventory and local fingerprints

The following local SHA-256 fingerprints identify the source snapshot inspected on 2026-08-29. They are not MCP source revisions.

| Surface | Source file | Current local SHA-256 | Weighted identifiers observed |
| --- | --- | --- | --- |
| Root event and report | `events\006_independence_wave.txt` | `81464DEF1BAF372B9A126BFA95C78E585C7D0C2E51786C5BC75E82822764BA22` | `chaosx.nr6.1`, `.2`, `.300`–`.308`, `chaosx.triggerable_scenarios.8`, `.80`; 11 `ai_chance` blocks |
| Merged support events | `events\006_independence_wave_support_events.txt` | `F8DB738666DC14003DC3240DD027DA3DDD8EC3F67EE85465B9C8F580B4265021` | `chaosx.nr6.36`–`.40`, `.360`–`.364`, and package support IDs; 136 `ai_chance` blocks |
| Automatic allocator | `common\scripted_effects\006_independence_wave_effects.txt` | `39361582082EF535F661FC6C6D2CAF9D0B15B9741E5CC468E07AA11F04706894` | `independence_wave_select_one_automatic_package` at line 3287; one outer 14-entry `random_list` at line 3494 |
| Allocation scoring | `common\scripted_effects\006_independence_wave_package_planner_effects.txt` | `A89D48568A05F125CB1157FD60DD83EA806CC356D0FFEFF4621270A2DBCFEB87` | `independence_wave_calculate_candidate_allocation_weight` at line 585 |
| Regional package pools | `common\scripted_effects\006_independence_wave_package_region_effects_registry.txt` | `2C309B2400D987B93C45159699A1A936FD4FECF7D3E883978E288E854A941728` | 14 regional `random_list`s, 126 package weight entries, 14 selector blocks |
| Formable selection | `common\scripted_effects\006_independence_wave_formable_registry_effects.txt` | `7BFF28B86CBF0FCA20EE88A379C08765FDC5664D8696CE4F651862E5D66CD23D` | `independence_wave_formable_resolve_congress` at line 2481; two-entry success/failure `random_list` at line 2485 |
| SCN-008 registry | `common\scripted_effects\006_independence_wave_scenario_effects.txt` | `BA7AC7622F1F97674C4487A169C91AB861E1BE56D0DE1C54388CCE062535041D` | `independence_wave_scenario_rebuild_ranked_registry` at line 165; 138 ranked package IDs; deterministic order, not a probability pool |
| Evolution scheduler | `common\scripted_effects\006_independence_wave_evolution_effects.txt` | `CC75B8B6BC4EB2BA834610C1A43E15D405ACF0289280A62263C1C5AADCDAC142` | `independence_wave_schedule_next_evolution_check` calls `mtth:independence_wave_evolution_interval` at line 692 |
| Merged evolution MTTH | `common\mtth\chaosx_mtth_variables.txt` | `91988D433884C49DC4E8D98F3F7CBF0E9ECAE218E3EC147539425466CCA4BA33` | `independence_wave_evolution_interval` at line 233 |
| Core decision scores | `common\decisions\006_independence_wave_decisions.txt` | `86A4177F318D4574B3CF972CDED7DC581AF3B1F67285FD88AED7643A00B8BDE3` | 77 `ai_will_do` blocks |
| Shared decision scores | `common\decisions\006_independence_wave_shared_decisions.txt` | `1F5787C3C2BB3A92E9C914CF1148270A0BD7E96556FF49DC7EC6C3A8BC8F682C` | 14 `ai_will_do` blocks |
| Focus selection | `common\national_focus\006_independence_wave_focus.txt` | `86A6A9BE8132F9DF53DFA58733A776B55BF24CA91F8E4A169296953D360D832C` | 227 `ai_will_do` blocks |
| IW-043/IW-058 focus overlays | `common\national_focus\006_independence_wave_iw043_iw058_focus.txt` | `FF73C22B4269F02CA831ABA89C7EDE443861A5260317DDD4F40DD0FD57E5A30F` | 48 `ai_will_do` blocks |
| IW-093/IW-098 focus overlays | `common\national_focus\006_independence_wave_iw093_iw098_focus.txt` | `91646A32C32D8CD6D9E29357BBF580FFACB82B52F06AF386A03491132A5AD807` | 43 `ai_will_do` blocks |
| Advisor selection | `common\characters\006_independence_wave_characters_registry.txt` | `1567E9AB52B43AEA47ADB200A600BAD4516E2675DAA9CCA01FABCF23D10C15D6` | 21 advisor `ai_will_do` blocks |
| AI strategy factors | `common\ai_strategy\006_independence_wave_ai_strategy_registry.txt` | `FEDDA4765DCC6DD54EEA3C7D5CE2C994D8359ACB1B233F9F6987C493FE4319CA` | 738 `ai_strategy` entries |
| Shared tuning constants | `common\script_constants\006_independence_wave_constants_registry.txt` | `B882BF3A86C0E38677F1E8FADC5B315FADDF27BC6F9854A2CF6628E65EAB6210` | allocator, decision AI, evolution MTTH, formable risk, registry, ladder, and scenario constants |

A source census over the Event-006-named files in `events\`, `common\decisions\`, `common\national_focus\`, `common\characters\`, `common\scripted_effects\`, and `common\ai_strategy\` found 147 `ai_chance` blocks, 1,123 `ai_will_do` blocks, 16 `random_list` blocks, and 738 `ai_strategy` entries. This census is exact for the local text snapshot but is not engine evidence and does not imply that every block is simultaneously selectable.

The decision-file portion of the census covers these exact sources: `006_independence_wave_balkan_decisions.txt`, `006_independence_wave_bashkiria_mari_decisions.txt`, `006_independence_wave_decisions.txt`, `006_independence_wave_far_eastern_decisions.txt`, `006_independence_wave_form01_02_04_decisions.txt`, `006_independence_wave_form03_decisions.txt`, `006_independence_wave_form05_decisions.txt`, `006_independence_wave_form48_decisions.txt`, `006_independence_wave_formable_decisions.txt`, `006_independence_wave_frontier_decisions.txt`, `006_independence_wave_iberian_decisions.txt`, `006_independence_wave_iw043_iw058_decisions.txt`, `006_independence_wave_iw093_iw098_decisions.txt`, `006_independence_wave_karelia_crimea_decisions.txt`, `006_independence_wave_mediterranean_decisions.txt`, `006_independence_wave_minor_overlay_decisions_registry.txt`, `006_independence_wave_pacific_decisions.txt`, `006_independence_wave_rhineland_bavaria_saar_decisions.txt`, `006_independence_wave_scotland_wales_decisions.txt`, `006_independence_wave_shared_decisions.txt`, `006_independence_wave_siberian_decisions.txt`, `006_independence_wave_transcaucasus_decisions.txt`, `006_independence_wave_wallonia_frisia_decisions.txt`, and `006_independence_wave_western_decisions.txt`.

## Source-only value and modifier traces

The following are source-level traces only. They are not normalized selection probabilities, click probabilities, timing distributions, or balance proofs.

### Automatic allocator

`independence_wave_calculate_candidate_allocation_weight` initializes a candidate at zero and only enters the scoring branch after `has_independence_wave_runtime_package_content_attestation_for_execution_id = yes` and the chaos-band eligibility check pass.

The base score is `100` from `constant:independence_wave_allocation_weight.base`.

The visible additive modifiers are `+100` for a valid breakaway sponsorship record, `+25` for a registered tag, `+30` for a new region, and `+20` for a new host.

The visible repeat-memory modifiers are `-80` for a prior package, `-25` for a prior region, and `-20` for a prior host.

The visible evolution and chaos modifiers include a low-opening-confidence penalty of `20`, a high-opening-confidence bonus of `15`, a `+15` Replicable Independence supported-region bonus, a `-35` low-chaos signature penalty, a `+45` high-chaos-only bonus, dormant package additions of `+30`, `+25`, and `+35` by depth, Armed Birth additions of `+20` for industrial and frontier archetypes, Sovereign Congress additions of `+15` regional and `+30` signature, and Open Sovereignty additions of `+55` high-chaos and `+40` formable-route packages.

At World Collapse, eligible candidates with an earliest band of Totalen Chaos receive the `1.35` `world_collapse_rarity` multiplier, and the attested result is floored at `1` by the source constant.

The outer selector has 14 regional entries, while the selector boundary statically seeds 144 per-package weight variables and the regional registry contains 126 package weight entries. These counts are different source layers and must not be treated as one complete candidate denominator without an MCP pool expansion.

### Event option `ai_chance`

Root options in `events\006_independence_wave.txt` use the shared `independence_wave_decision_ai` scale for the `.301`–`.304` route events, with base values of `very_low = 2`, `low = 5`, `standard = 10`, `high = 25`, and `urgent = 100` where the block is present.

The shared modifiers are `modifier_half = 0.5`, `modifier_double = 2`, and `modifier_major = 5`.

The support-event registry adds 136 source `ai_chance` blocks, including evolution incident factors declared as `40`, `45`, `55`, or `60` for the named `.360`–`.364` option pairs. A source option’s score is not a guarantee that its trigger is true or that it is in the active candidate pool.

The offline event and AI references define `ai_chance` as proportional among currently visible options, with a default of `1` when absent and a d100-style effective floor. Current option validity and normalization were not engine-inspected.

### Decisions, missions, focuses, and advisors

The source has 784 decision/mission `ai_will_do` blocks across 25 Event-006 decision files, 318 focus `ai_will_do` blocks across the generic and two overlay focus files, and 21 advisor `ai_will_do` blocks in the character registry.

These are willingness/score races, not probability-proportional event-option pools. The source values use the shared decision scale and package-specific constants, with modifiers gated by visibility, availability, route, war, host threat, capital control, resources, cooldown, target validity, and lifecycle flags.

The accepted route specification explicitly requires invalid routes to be hidden, bypassed, or weighted to zero, and it states that the route table values are source-level design weights before engine normalization. No current MCP trace proved that every impossible or dead route reaches zero in each candidate pool.

### AI strategy factors

`common\ai_strategy\006_independence_wave_ai_strategy_registry.txt` contains 738 strategy entries covering build, production, infrastructure, defence, host restraint, emergency, patron, league, and package-specific priorities.

The source values are additive or negative strategy factors applied to AI scores and can affect focus, research, production, war, and target choices. They are not a normalized selection denominator, and no current strategy adapter was callable.

### Formable congress selection

`independence_wave_formable_resolve_congress` first calls `independence_wave_formable_calculate_failure_risk`, checks `can_independence_wave_formable_pass_congress_vote`, and then samples the two source branches `independence_wave_formable_success_weight` and `independence_wave_formable_failure_weight`.

The source risk bases are `15`, `25`, `40`, and `55` for low through severe tiers, with `+15` per opposed member, `+5` per observer, `-10` per controlled anchor, `-5` per surplus consent, `+10` for military settlement, and `+15` for the hidden high-chaos proclamation. The result clamps failure to `5`–`85`, and success is `100 - failure`.

The two-entry branch pool is structurally visible in source, but the risk tier, member and observer counts, controlled anchors, consents, method, and transaction gate are state inputs, so no campaign formation probability is claimed.

### Evolution MTTH

`independence_wave_evolution_interval` has a base of `300` days, with source factors `1.15` for Gathering Storm, `1` for Rising Chaos, `0.85` for Chaos Tier, `0.7` for Totalen Chaos, `0.55` for World Collapse, `1.25` for a thin network, and `0.8` for a dense network at 15 living origins.

The caller clamps the resulting `mtth:` value to `90`–`720` days before scheduling the next check. A timing distribution still requires a complete state schedule, active-incident cadence, and engine evaluation; no current timing result is available.

### SCN-008 ranked registry and target selection

`independence_wave_scenario_rebuild_ranked_registry` appends 138 package IDs in deterministic priority order, then `independence_wave_scenario_attempt_ranked_packages` attempts the bounded registry and records rejected rows.

SCN-008 is therefore a deterministic ranking and reservation surface for package admission, not a single probability-proportional random list. Scenario target setup separately uses bounded `random_country` and `random_neighbor_country` calls for patrons and war targets, with host reservation, existence, faction, ideology, adjacency, and failed-declaration rollback as external state.

## Scenario contract and completeness

The scenario IDs below are retained as required controls from the accepted Event 006 probability handoff. They are controls to rerun after MCP recovery, not current results, scenario hashes, or current source receipts.

| Surface and control | Intended complete inputs | Current completeness | Classification on 2026-08-29 |
| --- | --- | --- | --- |
| `E6_ALLOCATOR_LADDER_2026_08_24`: `ALLOC_UNIFORM_COMPLETE`, `ALLOC_CALM_3`, `ALLOC_RISING_5` | Complete 14-entry outer region pool, nested package weights, attestation, host capacity, anchors, prior-wave memory, Event 005 collision, chaos/evolution flags, target counts `3/4/5/7/10` | Outer 14 branch shape is source-visible, but nested weights and live host/collision/attestation state are incomplete | **Unresolved**; no current ranking, dominance, starvation, or exact draw probability |
| `E6_ROOT_OPTION_MATRIX_2026_08_24`: `E6_CORE_EMPTY_CURRENT_2026_08_24`, `E6_SHARED_DECISION_EMERGENCY_2026_08_24`, `E6_SHARED_DECISION_PROVISIONAL_2026_08_24` | Complete visible option set, trigger validity, route state, resources, host/league/patron state, and sender/target scopes | 11 root blocks and 136 support blocks are source-visible, but active candidates and external factors were not MCP-expanded | **Unresolved**; no current option normalization |
| `E6_KUB_MISSION_MATRIX_2026_08_24` and `E6_TAT_MISSION_MATRIX_2026_08_24` | Complete mission/decision candidates, costs, caps, host threat, war, capital control, and target validity | Source files exist, but no current mission adapter or scenario evaluation was callable | **Unresolved**; no current score race |
| `E6_FOCUS_ROUTE_RACE_2026_08_24`: `FOCUS_OPEN_CALM`, `FOCUS_HOST_CRISIS`, `FOCUS_ROUTE_LOCKED`, `FOCUS_NO_VALID_ROUTE` | Complete focus candidate graph, prerequisites, availability/bypass, route flags, strategy factors, and country state | 318 focus score blocks are source-visible, but no current focus inspection or probability route was callable | **Unresolved**; no current focus ranking or zero-route proof |
| `E6_EVOLUTION_MTTH_MATRIX_2026_08_24` | Complete active incident, chaos tier, network count, schedule cadence, terminal state, and clamp path | MTTH source and caller are visible, but no engine timing evaluation or cadence trace was callable | **Unresolved**; no current timing distribution |
| `SCN-008` eight modes by Low/Medium/High/Maximum | Complete 138 ranked rows, host reservations, overlap resolution, blocked-row reasons, intensity package, scenario type, and target-reservation transitions | Source rank order and mode cardinality are visible, but live row validity and target transitions were not MCP-inspected | **Unresolved**; no current all-32-cell execution or target ranking |
| Formable congress two-branch pool | Complete risk tier, opposed/observer counts, anchors, consents, method, transaction gate, and total branch weights | Two branch names and formula are source-visible, but state inputs were not evaluated | **Unresolved**; no campaign formation probability |

The candidate-pool status for every row is incomplete for quantitative purposes. The current source-level 32/29/40/161 admission boundary is a static authority, not a substitute for a complete runtime pool in a named MCP scenario.

External factors not available to this audit include current country existence and control, host survival, state anchors, Event 005 collision state, living tags, Event 006 origin flags, package content-attestation flags, previous wave arrays, chaos tier, opening confidence, network count, route flags, resources, mission caps, cooldowns, league membership, patron reach, target reservations, failed war declarations, and terminal campaign flags.

## Findings and result classifications

The source census and local hashes are **exact source observations** for this snapshot.

The allocator and formable formulas are **score-only source traces** until the engine supplies a complete candidate pool and modifier evaluation.

The old named controls remain **unresolved current scenarios** because their prior receipts were generated against older source revisions and cannot be relabeled after the current source drift.

No current conclusion is made about dominance, starvation, rank reversal, repetition, timing drift, excessive repetition, or unsafe snowball behavior.

No current positive-weight impossible-choice finding is asserted because source eligibility and engine-visible candidate normalization were not available through MCP.

The source contains explicit fail-closed gates and minimum floors, but their interaction with all package rows, host capacity, collision state, and nested random lists remains unproven.

The differing static layers of 144 seeded package variables, 126 regional package entries, 138 SCN-008 ranked rows, 193 selectable rows, and 32 currently content-attested packages are a review boundary, not evidence of a defect by themselves. They require one current adapter expansion that explains each layer and records rejected rows.

The source uses a single public Event 006 entry event `chaosx.nr6.1` with `is_triggered_only = yes`; no automatic MTTH for the root report was found. Evolution timing is a separate active-incident MTTH path and must not be conflated with public wave-firing probability.

The accepted specification distinguishes event-option probability, AI willingness score races, deterministic SCN-008 ranking, random target selection, and MTTH timing. Any future report must preserve those distinctions.

## Historical MCP receipts retained for traceability only

The following artifacts are copied from the prior 2026-08-27 handoff and are not current evidence because the source hashes and/or revisions have changed.

The historical workspace was `mod_chaos_redux_ea3b2d67c2c0`.

The historical root `event_option_ai_chance` inspect used source revision `69c8a8272a3833a9d2572014de194a973be3ebf64ec9bfeb989faed10f025df6` and source hash `a08206c27f0e0da5cfd56e3e6e985b067d7b528ba1f6e4b3898369346b238cd2`, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7fe874b36f58c12c4800313e9205f0f3729069edc140ee5fdd1823264db7eaf/6665d56de258cb0f6e0dce33d3d186440150dad083c398cb815ecbb4e304ec74/probability-inspect-a08206c27f0e0.json`.

The historical root option evaluation used analysis `probability-21ecef2ef00a9848c2101687`, scenario hash `509f3bf047bf951e9ca0c5d5cad28068e9f8be60440685cc2df06baacb70fa30`, and artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41672d50cc42614955ad64eb5ed280867f51e7d65da58dff9f6762e7cbb6d13b/c3db11608f627df722ff00347396812d7829f2ca074f227e0282602c0a9f3d16/probability-21ecef2ef00a9848c2101687.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a9bd51a40fff8263f9188ebc4ba1dd50359064d7a6c07d866905cddfa7a80ce/920444f64f80360abdca21b596dd0c335498d2af727d919dfa282cf844f64bb2/probability-probability-21ecef2ef00a9848c2101687-ranking.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38838b1831e77eb6343d8d1a2b7fa7eb9fbff4fbab74749fe362f780278f481a/d5def5068eaaabccb219b9d18ebc7790c4be54789371456ef23cb8e4de1ccdc5/probability-probability-21ecef2ef00a9848c2101687-unresolved.svg`.

The historical automatic allocator inspect used source revision `2375381d0e0468efccef10c185078eeba27ce904e1052220b39cef5d8758f447`, source hash `5b551b7eed1e6c673d519870075f8cb057e0c521e5bb3b28585df8506f71c29a`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/daee059af43c24af47f40bf108fcdd1c32d3d799ad8d36c5e633a4633ad18679/654f3990ddc34c4a8c72313a6a16dc6929151a867992c70589da2a34763fc48b/probability-inspect-5b551b7eed1e.json`.

The historical formable inspect used source hash `355bf8134c4151ef3265293666e291f16461997ad73bebb53053dbaab01ac05d` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a50d304bd304a621e064e7a785dd7372ec427113d1afd4adbf1462314e73aa80/c50a5735e1d07b32de3f027023d08eddad4bf51ca6ebb1f5da104c93cce8ebd1/probability-inspect-355bf8134c41.json`.

The historical formable synthetic evaluation was analysis `probability-96ce0b313e1c5d9bec8312c7`, scenario hash `93d7db3a8e9c997b1911313f31f58e42db3107b885dfedfd00d1bd62ab3ebaa3`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e008c643c96364e99cff12f03ed2c13e655a64aae2572f3d0409004c4cda423b/5fb39ba0f9609847d65ba88c9003fd077b8f4ae147d98fdf60a574cad5b560cc/probability-96ce0b313e1c5d9bec8312c7.json`; its exact 1/2 result applied only to a synthetic 1-and-1 branch fixture.

The historical strategy discovery artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43aca06d5c3833b9f939906398346c2a889590e3dc29e17960490801716e3551/291a9b75f2871d660f965be5d2ef5c375ffc8163306f21ce0171a43ada1de3c1/probability-inspect-a35190937fed.json`, with historical source hash `a35190937fed7a0e7a3e156244ad0dbac468bdc2c0c05366da6cce0d3d482396` and `discoveryReason=no_weighted_surfaces`. It did not prove the current 738 strategy entries or their target validity.

The historical evolution discovery artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/071073d01b60814f26e86ca47ef4bd080930003201a2f651549dd23a59f7ca0b/5ee9b942aef03481620662115738fb396355122bd4dbe37a9d3501a003f40c30/probability-inspect-8632297cf059.json`, with historical source hash `8632297cf059164892a537ff3a987cddd0406c020e98234331014d42b4b8f8a2` and zero matched weighted surfaces. It did not prove the current merged MTTH caller or timing.

## Recommended owner follow-up

Restore the callable `hoi4-agent-tools` probability and structural routes in the current runtime and preserve the exact tool error above as the transport blocker until the route is repaired.

Rerun `hoi4.probability_inspect` first for every current source hash, then run the named allocator, root/support-event, decision/mission, focus, formable, evolution, and SCN-008 controls with complete candidate pools and declared external factors.

For the allocator, the rerun must expose all 14 outer region entries, the nested package entries, the 32 admitted package boundary, the 161 unattested rows, host capacity, anchor uniqueness, prior-wave arrays, Event 005 collision, and rejection reasons before reporting percentages.

For event options, decisions, missions, focuses, and advisors, the rerun must distinguish visible/available candidate sets from score traces and include route, resource, lifecycle, target, and strategy factors.

For SCN-008, rerun all eight player-facing modes at Low, Medium, High, and Maximum, preserving separate Universal Belligerence target rules and result rows, host reservations, blocked-candidate reasons, and intensity state transitions.

For evolution, rerun the MTTH matrix with explicit chaos tier, network count, active-incident cadence, clamp path, horizon, and terminal state inputs, and render timing evidence.

After any owner-applied weight or validity patch, run `hoi4.probability_compare` against the same named scenarios and preserve the before/after comparison ID. This auditor must remain read-only and must not choose tuning targets or apply fixes.

## Skipped analyses and remaining uncertainty

`hoi4.probability_evaluate` was skipped because the required inspect adapter function is not callable in this runtime.

`hoi4.probability_sweep` was skipped because no current adapter or baseline scenario result exists.

`hoi4.probability_compare` was skipped because no current before/after owner patch exists and the required MCP route is unavailable.

`hoi4.probability_render` was skipped because no current ranking, matrix, timing, sequence, comparison, or unresolved artifact exists to render.

`hoi4.probability_simulate` was skipped because no explicitly declared uncertain-input model was authorized and the route is unavailable.

`hoi4.probability_sequence` was skipped because no complete custom pool with cadence, state transitions, and terminal states was declared and the route is unavailable.

The attempted `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.focus_inspect`, and `hoi4.focus_render` routes each returned the same `TypeError: tools.mcp__hoi4_agent_tools__<method> is not a function` failure, so the matching structural MCP evidence is absent.

No hand-calculated probability, normalized denominator, sampled timing, rank reversal, dominance, starvation, repetition, or balance conclusion is substituted for the unavailable MCP evidence.

The current audit is therefore delivered as a source-fingerprinted, score-versus-probability boundary report with all live weighted conclusions unresolved.

No gameplay simplification or fallback was applied.
