# Event 029 Riches Found — AI probability baseline

Status: baseline audit only. This report is incomplete and unresolved because the required HOI4 MCP probability and structural routes were not callable in this session. No gameplay, AI, event, focus, decision, mission, technology, localisation, or runtime source was changed. The only created artifact is this report and its parent folder.

Audit date: 2026-08-29.

## 1. Mandatory MCP route and evidence status

The first required call was attempted before source analysis:

```text
mcp__hoi4_agent_tools__hoi4_probability_inspect({})
```

The exact blocker returned was:

```text
BLOCKED: callable tool mcp__hoi4_agent_tools__hoi4_probability_inspect is not present in the current tool inventory.
```

The callable inventory also did not expose `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, or `hoi4.probability_render`. The matching read-only structural routes `hoi4.event_inspect` and `hoi4.event_render` were unavailable as well.

The repository still contains a registration for the `hoi4_agent_tools` server in `.codex\config.toml`, but registration did not make the required functions callable in this session. No MCP adapter revision, scenario hash, artifact URI, comparison id, or rendered evidence URI exists for this audit. No source-only calculation is treated as a replacement for the missing engine evidence.

Consequences:

- No engine-exact or engine-bounded probability, score, timing, threshold, rank, or target result was produced.
- No `probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_simulate`, or `probability_sequence` call could be made.
- No `probability_render` output exists.
- All named Event 029 scenario conclusions below are `unresolved` unless explicitly described as an exact source observation.
- The source observations below identify what the parent agent must expose to the MCP adapter; they do not claim campaign balance.

## 2. Reviewed sources and scope

The accepted scenario matrix and the rest of the Event 029 design package were read from:

- `docs\specs\029_riches_found_specs\029_riches_found_ai_probability_scenarios.md`
- `docs\specs\029_riches_found_specs\029_riches_found_acceptance_criteria.md`
- `docs\specs\029_riches_found_specs\029_riches_found_coding_prompt.md`
- `docs\specs\029_riches_found_specs\029_riches_found_goal_prompt.md`
- `docs\specs\029_riches_found_specs\029_riches_found_spec_part_1_core_loop.md`
- `docs\specs\029_riches_found_specs\029_riches_found_spec_part_2_baseline_progression.md`
- `docs\specs\029_riches_found_specs\029_riches_found_spec_part_3_decisions_missions_foreign_interference.md`
- `docs\specs\029_riches_found_specs\029_riches_found_spec_part_4_evolutions.md`
- `docs\specs\029_riches_found_specs\029_riches_found_spec_part_5_ai_balance_interactions.md`
- `docs\specs\029_riches_found_specs\029_riches_found_spec_part_6_assets_localisation_achievements.md`
- `docs\specs\029_riches_found_specs\029_riches_found_catalog_alignment.md`
- `docs\specs\029_riches_found_specs\029_riches_found_research_notes.md`
- `docs\specs\029_riches_found_specs\029_riches_found_source_review_manifest.md`
- `docs\specs\029_riches_found_specs\029_riches_found_decision_mission_prompt.md`
- `docs\specs\029_riches_found_specs\029_riches_found_achievement_prompt.md`
- `docs\specs\029_riches_found_specs\029_riches_found_asset_prompt.md`

The required offline references were consulted in `paradox_wiki\`, including `AI modding - Hearts of Iron 4 Wiki.md`, `Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, and `Idea modding - Hearts of Iron 4 Wiki.md`.

The required vanilla documentation was consulted under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\`, including `effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`. Relevant vanilla precedents included `random_country` with an explicit `limit`, weighted `random_list`, event `ai_chance` blocks with base and modifiers, and event MTTH blocks.

Event 018 Resources Found was inspected only to prevent cross-contamination. Its `018_resources_found_*` implementation is not Event 029 evidence and was not used as a substitute for missing Event 029 surfaces.

## 3. Current Event 029 weighted and selection surfaces

The following audit identifiers are assigned in this report because the current source does not define the planned `RF_*` implementation identifiers.

| Audit surface | Exact current source | Exact source observation | Candidate-pool completeness | External-factor completeness | Result classification |
|---|---|---|---|---|---|
| `RF_EVENT_029_GLOBAL_POOL` | `common\scripted_effects\chaosx_logic_effects.txt:274-347,349-398,822-...`; `common\scripted_effects\chaosx_settings_effects.txt:4329-4442,1744` | Event ID `29` is registered in `global.repeatable_events`, therefore included in `global.all_events`; the default event weight and cap initialize to `1000`; the active-pool check can reject disabled candidates; the weighted selector scales valid event weight by `100`, rolls from `1` through the summed scaled total, and selects by cumulative weight. | `INCOMPLETE`: the runtime member set depends on disabled flags, event state, settings filter, required chaos, and other candidate validity. | `UNAVAILABLE`: no MCP adapter could expose the runtime pool or settings. | `UNRESOLVED`; source trace only, not a selection probability. |
| `RF_EVENT_029_DEFAULT_AVAILABILITY` | `common\scripted_effects\chaosx_logic_effects.txt:349-363`; `common\scripted_triggers\chaosx_settings_triggers.txt:10-33` | The initialization pass adds every event not returned by `event_log_event_is_reworked_default_enabled` to `global.disabled_events`; the allowlist contains Event 018 but not Event 029. Event 029 is therefore default-disabled under the current shared initialization path. | `INCOMPLETE`: the static registration is visible, but the live disabled state and settings overrides were not supplied to an adapter. | `UNAVAILABLE`. | `UNRESOLVED` for runtime selection; the default-disabled source state is an exact source observation, not a balance conclusion. |
| `RF_EVENT_029_RECIPIENT_RANDOM_COUNTRY` | `events\029_riches_found.txt:22-34` | `chaosx.nr29.1` is `is_triggered_only` and invokes `random_country` with no visible `limit`, then fires `chaosx.nr29.2` after one day. No ordinary-country, valid-state, Event 018 exclusion, existing-mine exclusion, country weight, or state suitability rule is encoded in this file. | `INCOMPLETE/UNBOUNDED`: the accepted pool cannot be reconstructed from the current source; implicit engine behavior is unknown without the route. | `UNAVAILABLE`: controller, occupier, state ownership/control, special-country, civil-war, faction, war, and mine-state inputs are not declared to an adapter. | `UNRESOLVED`; no exact recipient probability may be stated. |
| `RF_EVENT_029_OPTION_ACKNOWLEDGEMENT` | `events\029_riches_found.txt:38-51` | `chaosx.nr29.2` has exactly one option, `chaosx.nr29.2.a`, with `ai_chance = { base = 100 }`. There is no `ai_will_do` and no competing option. The option sends `chaosx.news.31` after three days and grants `2000` political power. | `COMPLETE` only for the source-visible one-option AI option pool; this does not complete the recipient or mine pool. | `UNAVAILABLE` for engine confirmation; no external modifier is encoded. | `UNRESOLVED` for engine evidence. The source weight is a degenerate proportional `ai_chance` input, not an `ai_will_do` willingness score and not a human click probability. |
| `RF_EVENT_029_REPEATABLE_RECOVERY` | `common\scripted_effects\chaosx_logic_effects.txt:987-1083,1114-1181`; `common\script_constants\event_system_constants.txt:39-42` | The shared defaults are `event_weight = 1000`, `recovery_rate = 20`, and `reduce_cap_factor = 0.5`. On a repeatable fire, the cap is multiplied by `0.5` and the event weight is cleared; the recovery routine replaces a weight of `1` with one recovery step and otherwise adds one recovery step up to the cap. The visible source calls recovery from global minor/major pacing handlers, not from an Event 029-specific monthly hook. | `INCOMPLETE`: cadence, settings overrides, firing context, and all other repeatable candidates were not supplied. | `UNAVAILABLE`: no timeline adapter or state-transition engine result. | `UNRESOLVED`; exact source constants and branches are known, but timing distribution is not. |

The Event 029 news event in `events\_chaosx_news.txt:428-442` is not a separate weighted surface: it has one news option and is reached by the Event 029 option effect. It was not counted as an independent AI race.

The current Event 029 source contains no Event 029-specific `ai_will_do`, `mean_time_to_happen`, `random_list`, foreign target score, raid target score, decision score, mission score, research score, doctrine score, evolution MTTH, or incident pool. Absence is recorded as `ABSENT`, not as an engine-proven zero weight.

## 4. Score versus probability interpretation

The offline AI modding reference distinguishes the relevant engine surfaces:

- `ai_will_do` is a willingness score used in a highest-score race, with later AI strategy modifiers capable of multiplying the score.
- `ai_chance` is a probability-proportional-to-weight option race; weights need not sum to `100`.
- A weighted random list or the shared Event Log selector is also a proportional sampling surface, with the denominator defined by the complete valid candidate pool.
- MTTH is a timing distribution controlled by a base and modifiers; it is not an option click score.

Event 029 currently exposes only a single `ai_chance` option and the shared event-ID proportional selector. It exposes no current `ai_will_do` score race. The `base = 100` option value cannot be used to infer the probability of the event being selected, the probability of a country receiving it, the probability of a state being selected, or a player's click behavior. Those denominators and behaviors are either absent from source or unavailable through MCP.

## 5. Named scenario coverage

The table records every named scenario from `docs\specs\029_riches_found_specs\029_riches_found_ai_probability_scenarios.md`. `ABSENT` means the Event 029 candidate surface has not been implemented; it does not mean every candidate has effective weight zero. `INCOMPLETE` means a shared source mechanism exists but the complete live candidate pool is not available. `UNAVAILABLE` means the required external inputs or engine route were not exposed. Every actual result in this table is therefore `UNRESOLVED`.

### Surface A — Initial policy choice

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_POLICY_01_STABLE_DEMOCRACY` | Public Development leads; State Extraction or regulated Concession follows; Militarized Mine and Predatory Extraction remain behind plausible alternatives, with Predatory negligible. | No probability evaluation; no Event 029 policy candidate pool exists in source. | `ABSENT` | `UNAVAILABLE`: legitimacy, ideology, order, policy, war, and mine state not adapter inputs. | `UNRESOLVED` |
| `RF_POLICY_02_AUTHORITARIAN_MAJOR_AT_WAR` | State Extraction leads; Militarized Mine follows; aligned Concession and Public Development remain viable; Predatory becomes material only under the intended desperation and government context. | No probability evaluation; no Event 029 policy score surface exists in source. | `ABSENT` | `UNAVAILABLE`: authoritarian government, major status, war, receipts, desperation, and strategy factors not encoded. | `UNRESOLVED` |
| `RF_POLICY_03_POOR_MINOR` | Limited Concession or infrastructure-for-access leads; slow Public Development follows; exclusive concession must not dominate when limited access is valid. | No probability evaluation; no country-scale or concession pool exists in source. | `ABSENT` | `UNAVAILABLE`: poor/minor scale, access, foreign offers, infrastructure, and valid target set not encoded. | `UNRESOLVED` |
| `RF_POLICY_04_COLONIAL_OCCUPIER` | Militarized/local settlement leads for short expected occupation; State Extraction follows; long-term controllers should value local sharing more than short-term predation. | No probability evaluation; no occupier policy surface exists in source. | `ABSENT` | `UNAVAILABLE`: occupation duration, controller, legitimacy, local sharing, and resistance inputs not encoded. | `UNRESOLVED` |

### Surface B — Development choice

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_DEV_01_INLAND_DEEP_REEF` | Rail Spur leads; Drain/Reinforce follows; Housing/Processing and Development Fund remain useful; Port/Convoy is invalid and Drive Deeper is not allowed to dominate. | No probability evaluation; no Event 029 development candidate pool exists in source. | `ABSENT` | `UNAVAILABLE`: inland geography, transport, reef/depth, order, prerequisites, and costs not encoded. | `UNRESOLVED` |
| `RF_DEV_02_ISLAND_GEMSTONE` | Port/Convoy leads; Processing or secure assay follows; Housing remains plausible; Rail is zero unless a real route exists; Drive Deeper stays low with weak order. | No probability evaluation; no state development score surface exists in source. | `ABSENT` | `UNAVAILABLE`: island access, route validity, gemstone type, order, and prerequisite state not encoded. | `UNRESOLVED` |
| `RF_DEV_03_COLLAPSE_WARNING` | Drain/Reinforce leads; temporary closure/repair and transport restoration follow; Housing and Processing trail; Drive Deeper is zero or near-zero. | No probability evaluation; no collapse development or temporary-closure surface exists in source. | `ABSENT` | `UNAVAILABLE`: collapse severity, infrastructure damage, workforce, transport, and closure state not encoded. | `UNRESOLVED` |

### Surface C — Revenue choice

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_REV_01_HIGH_LEGITIMACY_DEMOCRACY` | Citizens' Dividend or Stabilization Fund leads; Earmark Local Revenue and Worker/Community Sharing remain strong; Centralize and Patronage trail. | No probability evaluation; no Event 029 revenue candidate pool exists in source. | `ABSENT` | `UNAVAILABLE`: legitimacy, ideology, reserve, revenue, and sharing policy not encoded. | `UNRESOLVED` |
| `RF_REV_02_WARTIME_FINANCIAL_CRISIS` | Centralize leads; Stabilization withdrawal is valid only with reserve; reduced local settlement and Dividend remain alternatives; Patronage is contextual. | No probability evaluation; no wartime revenue score surface exists in source. | `ABSENT` | `UNAVAILABLE`: war, stockpile, reserve validity, government, and emergency strategy not encoded. | `UNRESOLVED` |
| `RF_REV_03_LOW_LEGITIMACY_NON_CORE` | Earmark Local Revenue leads; Worker/Community Sharing follows; Dividend and Stabilization remain viable; Centralize falls as resistance and legitimacy pressure rise. | No probability evaluation; no legitimacy-sensitive revenue surface exists in source. | `ABSENT` | `UNAVAILABLE`: non-core status, resistance, legitimacy pressure, and local revenue state not encoded. | `UNRESOLVED` |

### Surface D — Foreign concession target

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_FOREIGN_01_NEAR_ALLIED_MAJOR` | A nearby allied industrial major with access and good relations outranks a distant neutral. | No probability evaluation; no Event 029 foreign target pool exists in source. | `ABSENT` | `UNAVAILABLE`: distance, border/port access, industry, relations, faction, ideology, invitation, and rival status not encoded. | `UNRESOLVED` |
| `RF_FOREIGN_02_DISTANT_NAVAL_POWER` | A distant naval power can rank for a coastal/island mine with convoys and strategic interest, but should rank poorly for inland mines without transit. | No probability evaluation; no access- or convoy-sensitive target scoring exists in source. | `ABSENT` | `UNAVAILABLE`: coast/island, convoy, transit, naval reach, strategic interest, and target validity not encoded. | `UNRESOLVED` |
| `RF_FOREIGN_03_HOSTILE_RIVAL` | A hostile rival is zero or near-zero for a cooperative concession; sabotage/coercive action is a separate route if valid. | No probability evaluation; no cooperative concession or separate coercive target route exists in source. | `ABSENT` | `UNAVAILABLE`: hostility, relations, rival status, route type, and target validity not encoded. | `UNRESOLVED` |
| `RF_FOREIGN_04_EXISTING_EXCLUSIVE_CONCESSION` | New exclusive candidates are invalid; only compatible limited technical/repair assistance may remain. | No probability evaluation; no existing-concession exclusion or compatible-assistance pool exists in source. | `ABSENT` | `UNAVAILABLE`: concession ownership, exclusivity, compatibility, repair need, and access not encoded. | `UNRESOLVED` |

### Surface E — Security and raid response

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_SEC_01_CIVILIAN_CRIME` | Mine Police leads; camp/admin/licensing follows; Private Guards remain possible; Army Cordon and Arm Workers trail; Clear Barricades is invalid. | No probability evaluation; no Event 029 security choice pool exists in source. | `ABSENT` | `UNAVAILABLE`: crime severity, order, civilian status, guards, and action validity not encoded. | `UNRESOLVED` |
| `RF_SEC_02_ARMED_RAID_WARTIME` | Army Cordon leads; Escort/route defense follows; Mine Police and Private Guards remain viable; Truce depends on actor; Arm Workers trail. | No probability evaluation; no raid response or actor target pool exists in source. | `ABSENT` | `UNAVAILABLE`: raid actor, war, route, military capacity, and truce validity not encoded. | `UNRESOLVED` |
| `RF_SEC_03_WORKER_CLAIM_WAR` | Negotiate Truce or Claims Court leads; Mine Police follows; Army Cordon, Clear Barricades, and Private Guards remain contextual; military/fascist context may reverse the middle. | No probability evaluation; no worker-claim security surface exists in source. | `ABSENT` | `UNAVAILABLE`: worker claim, war, ideology, government, military capacity, and actor validity not encoded. | `UNRESOLVED` |
| `RF_SEC_04_PRIVATE_ENCLAVE` | Disarm Private Forces or buyout leads; Replace Administration follows; Army Cordon remains possible; accepting the enclave is weak and dependent on context. | No probability evaluation; no private-enclave target/action pool exists in source. | `ABSENT` | `UNAVAILABLE`: enclave ownership, foreign backing, dependence, force, and buyout validity not encoded. | `UNRESOLVED` |

### Surface F — Evolution I timing

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_EVO1_01_MANAGED_MINE` | With chaos `600`, moderate pressure, high legitimacy/order, public/state policy, and stabilization, the base timing is longer and can be effectively starved. | No MTTH evaluation; Event 029 has no evolution-I MTTH source. | `ABSENT` | `UNAVAILABLE`: chaos meter, pressure, legitimacy, order, policy, stabilization, cadence, and terminal state not encoded. | `UNRESOLVED` |
| `RF_EVO1_02_CAPTURED_CONCESSION` | With chaos `600`, high pressure, low legitimacy, exclusive concession, private guards, and failed audit, timing is shorter and usually precedes a full year. | No MTTH evaluation; no captured-concession evolution source exists. | `ABSENT` | `UNAVAILABLE`: controller transfer, concession, guards, failed audit, pressure, and date cadence not encoded. | `UNRESOLVED` |
| `RF_EVO1_03_MULTIPLE_MINES` | With chaos `600` and three mines, the most corrupt/dependent mine should lead; mines should not all evolve on the same day. | No multi-mine timing evaluation; no Event 029 mine registry or aggregate MTTH source exists. | `ABSENT` | `UNAVAILABLE`: complete mine registry, aggregate dependence, per-mine pressure, and independent timers not encoded. | `UNRESOLVED` |

### Surface G — Evolution II timing

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_EVO2_01_HIGH_PRESSURE_GEMSTONE` | With chaos `800`, high pressure, gemstone, guards, theft, and low order, timing is clearly shorter. | No MTTH evaluation; no Event 029 evolution-II MTTH source exists. | `ABSENT` | `UNAVAILABLE`: chaos, gemstone, guards, theft, pressure, order, and timing cadence not encoded. | `UNRESOLVED` |
| `RF_EVO2_02_SHARED_REVENUE_CONTROLLED_ACCESS` | With chaos `800`, moderate pressure, trusted sharing, high order, and controlled shifts, timing is longer or capable of remaining inactive. | No MTTH evaluation; no controlled-access evolution source exists. | `ABSENT` | `UNAVAILABLE`: sharing, order, shifts, pressure, containment, and terminal suppression not encoded. | `UNRESOLVED` |
| `RF_EVO2_03_CLOSED_MINE` | With chaos `800`, temporary closure, no workforce, and no shipments, evolution is blocked or heavily suppressed until reopening or a concealed incident. | No MTTH evaluation; no closure/workforce/shipments gates exist in Event 029 source. | `ABSENT` | `UNAVAILABLE`: closure, workforce, shipments, concealed incident, reopen transition, and cadence not encoded. | `UNRESOLVED` |

### Surface H — Evolution III timing

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_EVO3_01_AGGRESSIVE_DEEP_MINE` | With chaos `1000`, high pressure, repeated deepening, high development, recent deaths, and an opened unstable deep, timing is shorter. | No MTTH evaluation; no Event 029 evolution-III MTTH source exists. | `ABSENT` | `UNAVAILABLE`: chaos, deepening count, development, deaths, deep state, pressure, and timer cadence not encoded. | `UNRESOLVED` |
| `RF_EVO3_02_PARTIALLY_SEALED` | With chaos `1000`, moderate pressure, a deep seal, strong integrity, and no violence, timing is longer or blocked. | No MTTH evaluation; no sealed-deep evolution source exists. | `ABSENT` | `UNAVAILABLE`: seal state, integrity, violence, pressure, and containment terminal state not encoded. | `UNRESOLVED` |
| `RF_EVO3_03_GOLD_DISEASE_MASS_VIOLENCE` | With chaos `1000`, Gold Disease, massacre/collapse, and high deep pressure, timing accelerates materially but is not instantaneous solely because a death transaction occurred. | No MTTH evaluation; no Gold Disease or deep-pressure implementation exists. | `ABSENT` | `UNAVAILABLE`: disease stage, violence, collapse, deep pressure, deliberate trigger, and timing cadence not encoded. | `UNRESOLVED` |

### Surface I — Gold Disease choices

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_GOLD_01_STABLE_HIGH_LEGITIMACY` | Revenue sharing leads; Controlled Access follows; temporary closure and sealing remain viable; Quarantine, Military Control, and continued extraction trail. | No probability evaluation; no Gold Disease option pool exists in source. | `ABSENT` | `UNAVAILABLE`: disease state, legitimacy, order, extraction, workforce, and containment availability not encoded. | `UNRESOLVED` |
| `RF_GOLD_02_AUTHORITARIAN_WARTIME` | Military/control or Controlled Access leads; Workforce Replacement follows; sealing and quarantine remain viable; revenue sharing and temporary closure depend on context. | No probability evaluation; no authoritarian Gold Disease score surface exists in source. | `ABSENT` | `UNAVAILABLE`: authoritarianism, war, force, workforce, access control, and disease stage not encoded. | `UNRESOLVED` |
| `RF_GOLD_03_COLLAPSE_IMMINENT` | Temporary closure leads; evacuation and sealing follow; quarantine and sharing remain possible; continued extraction is invalid except for an explicit desperation override. | No probability evaluation; no collapse/emergency Gold Disease pool exists in source. | `ABSENT` | `UNAVAILABLE`: collapse severity, evacuation, seal validity, desperation override, and extraction state not encoded. | `UNRESOLVED` |

### Surface J — Demons Beneath the Mine choices

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_DEMON_01_STABLE_DEMOCRACY_PEACE` | Scientific or Religious investigation leads; Evacuation and Permanent Seal follow; exploitation requires evidence; Occult, Military Purge, and Agreement remain negligible or invalid as specified. | No probability evaluation; no supernatural option pool exists in source. | `ABSENT` | `UNAVAILABLE`: ideology, peace, evidence, hostile group, supernatural state, and action validity not encoded. | `UNRESOLVED` |
| `RF_DEMON_02_COLLAPSING_AUTHORITARIAN_WAR` | Controlled Exploitation or Military Purge leads; Agreement is material only with high dependence/desperation; investigation and sealing remain contextual. | No probability evaluation; no authoritarian supernatural route exists in source. | `ABSENT` | `UNAVAILABLE`: war, collapse, authoritarianism, dependence, force, evidence, and agreement validity not encoded. | `UNRESOLVED` |
| `RF_DEMON_03_EVACUATION_COMPLETE` | Permanent Seal leads; bound-terms containment and controlled upper workings remain possible; Agreement is low; Military Purge is invalid if no hostile group remains. | No probability evaluation; no evacuation-complete target/action pool exists in source. | `ABSENT` | `UNAVAILABLE`: evacuation, hostile-group validity, seal integrity, containment, and upper-workings state not encoded. | `UNRESOLVED` |

### Surface K — Gilded Sovereignty choices

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_GILDED_01_WEALTHY_REFORMIST` | Buy Back or Recognize Local Board leads; Revoke and Share remain viable; Violent Nationalize and Let Govern trail. | No probability evaluation; no Gilded Sovereignty option pool exists in source. | `ABSENT` | `UNAVAILABLE`: wealth, reformism, foreign backing, board status, force, damage, and legitimacy not encoded. | `UNRESOLVED` |
| `RF_GILDED_02_WEAK_DEPENDENT_STATE` | Share or Let Govern leads; Recognize follows; Buy Back, Revoke, and Violent Nationalize are weaker. | No probability evaluation; no dependent-state route exists in source. | `ABSENT` | `UNAVAILABLE`: dependency, fiscal capacity, board, foreign backing, force, and legitimacy not encoded. | `UNRESOLVED` |
| `RF_GILDED_03_MILITARY_MAJOR` | Revoke or Violent Nationalize leads; Buy Back follows; Share, Recognize, and Let Govern trail; the violent route must account for damage, deaths, foreign backing, and force. | No probability evaluation; no military-major Gilded Sovereignty surface exists in source. | `ABSENT` | `UNAVAILABLE`: major status, military capacity, damage, deaths, foreign backing, and route costs not encoded. | `UNRESOLVED` |

### Surface L — Bottomless Account choices

| Scenario ID | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_ACCOUNT_01_STABLE_STATE` | Close/Bind leads; Pay Material and Spend Authority remain viable; Accept Predatory is negligible. | No probability evaluation; no Bottomless Account option pool exists in source. | `ABSENT` | `UNAVAILABLE`: stability, account state, material reserve, authority, and breach risk not encoded. | `UNRESOLVED` |
| `RF_ACCOUNT_02_DESPERATE_WAR_STATE` | Pay Material or Accept Predatory leads; Spend Authority follows; Bind and Close trail; predation is bounded by benefit and breach risk. | No probability evaluation; no wartime account score surface exists in source. | `ABSENT` | `UNAVAILABLE`: war desperation, benefit, breach risk, stockpile, and government context not encoded. | `UNRESOLVED` |
| `RF_ACCOUNT_03_LOW_STABILITY_HIGH_DEPENDENCE` | Spend Authority or Accept Predatory can lead for a personalist authoritarian; Pay Material follows if stockpile exists; Bind and Close trail. A democracy with the same numbers should rank Close/Bind higher. | No probability evaluation; no dependence- and ideology-sensitive account surface exists in source. | `ABSENT` | `UNAVAILABLE`: stability, dependence, personalism, ideology, stockpile, and breach risk not encoded. | `UNRESOLVED` |

### Surfaces M and N — Incident pools and repeat-recipient/state selection

| Scenario or surface identifier | Accepted expectation, not observed | Actual/MCP result | Pool | External factors | Class |
|---|---|---|---|---|---|
| `RF_INCIDENT_POOLS` (Surface M; no individual scenario id) | Claims, rush, development setbacks, corruption, foreign interference, raids, collapse severity, Gold Disease, supernatural incidents, and contract outcomes need complete valid pools; common low severity must not starve plausible major outcomes; cooldowns, memory, managed flavor, and pressure response must be explicit. | No incident random list or Event 029 incident effect exists in source. | `ABSENT` | `UNAVAILABLE`: incident state, target validity, cooldown, memory, pressure, and terminal-state inputs not encoded. | `UNRESOLVED` |
| `RF_REPEATABLE_RECIPIENT_STATE_POOL` (Surface N; no individual scenario id) | All valid ordinary countries with a suitable state should have equal country weight; country scale, ideology, faction, mine count, and player control should not alter country selection; no suitable state should yield zero or N/A; state suitability is a separate race. | Current source uses unfiltered `random_country` and has no state candidate or suitability surface. | `INCOMPLETE/UNBOUNDED` | `UNAVAILABLE`: ordinary-country filter, owned/controlled state pair, exclusions, existing mine registry, and state suitability not encoded. | `UNRESOLVED` |

## 6. Named-role coverage

The named roles are covered below even where the scenario matrix has no separate role-only scenario id.

| Role or axis | Scenario ids and design surfaces | Current source status | Pool/factor result | Class |
|---|---|---|---|---|
| Controllers | All policy, development, revenue, security, evolution, Gold Disease, Demons, Gilded Sovereignty, and Bottomless Account scenarios. | Only the unfiltered `random_country` recipient path exists; no controller/state-bound mine state or AI score exists. | Candidate pools absent; controller state unavailable. | `UNRESOLVED` |
| Occupiers | `RF_POLICY_04_COLONIAL_OCCUPIER`, `RF_SEC_04_PRIVATE_ENCLAVE`, occupation/recapture/annexation/release acceptance cases. | No occupier, occupation-duration, legitimacy, controller reconciliation, or local-settlement weighting exists in Event 029 source. | Pools absent; occupation and transfer factors unavailable. | `UNRESOLVED` |
| Concession seekers | `RF_FOREIGN_01_NEAR_ALLIED_MAJOR` through `RF_FOREIGN_04_EXISTING_EXCLUSIVE_CONCESSION`, plus `RF_EVO1_02_CAPTURED_CONCESSION`. | No foreign target score, concession validity, exclusive-concession exclusion, or technical/repair route exists. | Target pool absent; distance, access, relations, faction, industry, and rival factors unavailable. | `UNRESOLVED` |
| Neighbors | Surface D foreign interference, neighbor transit/labor/joint-security/smuggling/armed-pressure behavior, and `RF_FOREIGN_*` context. | No neighbor candidate target, transit gate, or interference random list exists. | Neighbor pool absent; border, access, relations, and route-type factors unavailable. | `UNRESOLVED` |
| Raiders | `RF_SEC_02_ARMED_RAID_WARTIME` and Surface M raid incidents. | No raid target selection, raid severity, escort, truce, or route-defense score exists. | Raid pool absent; actor, war, route, and target-validity factors unavailable. | `UNRESOLVED` |
| Country scale | `RF_POLICY_02_AUTHORITARIAN_MAJOR_AT_WAR`, `RF_POLICY_03_POOR_MINOR`, `RF_FOREIGN_01`, `RF_FOREIGN_02`, `RF_GILDED_03`, and `RF_ACCOUNT_02`. | No major/minor/poor/industrial country weighting or score modifier exists. | Pools absent; country scale and industrial capacity unavailable. | `UNRESOLVED` |
| Ideologies | Policy scenarios plus `RF_REV_01`, `RF_GOLD_01`, `RF_DEMON_01`, `RF_DEMON_02`, `RF_GILDED_*`, and `RF_ACCOUNT_03`. | No ideology, government, personalist, democratic, authoritarian, military, fascist, or religious strategy factor exists. | Pools absent; ideology and government inputs unavailable. | `UNRESOLVED` |
| Wartime desperation | `RF_POLICY_02`, `RF_REV_02`, `RF_SEC_02`, `RF_GOLD_02`, `RF_DEMON_02`, and `RF_ACCOUNT_02`. | No desperation, war, stockpile, breach-risk, military-capacity, or emergency override surface exists. | Pools absent; scheduled war and reserve factors unavailable. | `UNRESOLVED` |
| Multiple-mine holders | `RF_EVO1_03_MULTIPLE_MINES`, Surface N, `RF_TEST_TRANSFER_06_MULTI_MINE`, and `RF_TEST_REPEAT_02_SAME_COUNTRY`. | No Event 029 mine registry, per-mine timer, aggregate dependence, or same-country/new-state exclusion exists. | Pool absent/incomplete; mine count and per-mine state unavailable. | `UNRESOLVED` |

No `ai_will_do` score-only result was produced for any role. The role expectations above remain design expectations, not measured ranking evidence.

## 7. Base trace, validity, and risk findings

### Shared event-pool trace

The exact source path currently reads as follows:

```text
Event 29 is appended to global.repeatable_events.
    -> repeatable event ids are appended to global.all_events.
    -> the chaos registry gives Event 29 required tier 0 by default.
    -> initialization gives non-major events default weight/cap 1000.
    -> the default rework queue adds Event 29 to global.disabled_events because id 29 is absent from the default-enabled allowlist.
    -> the active-pool candidate check can reject the disabled event.
    -> if valid, the selector reads the current event weight, scales it by 100, and samples against the sum of all valid global.all_events candidates.
    -> after a repeatable fire, the cap is multiplied by 0.5 and the weight is cleared; shared pacing later recovers it by the configured rate toward the reduced cap.
```

This is a source control-flow trace, not an exact probability. The denominator, settings filter, live disabled state, competing event weights, pacing cadence, and engine scope are incomplete.

### Validity findings

- The accepted Event 029 recipient requires an ordinary existing country and at least one valid owned-and-controlled state, with exclusions for special countries, civil-war shells, temporary carriers, Event 018 sites, and existing Event 029 mines. `events\029_riches_found.txt:30` contains no visible `limit` or equivalent validation.
- No state candidate or state suitability weighting exists in the current Event 029 source.
- No controller reconciliation, occupation transfer, recapture, annexation, release, civil-war, or multiple-mine state exists in the current Event 029 source.
- No Event 029 policy, development, revenue, foreign, security, raid, incident, Gold Disease, supernatural, Gilded Sovereignty, or Bottomless Account candidate pool exists in the current Event 029 source.
- The accepted design specifies an exact `1000` political-power grant, while `events\029_riches_found.txt:50` currently grants `2000`. This is a source/spec discrepancy for the parent to resolve; it is not a balance target selected by this audit.

### Dominance, starvation, rank reversal, repetition, and exploit risk

- Dominance: no planned candidate ranking was measured because the planned pools are absent and `probability_evaluate` is unavailable.
- Starvation: Event 029 is deterministically placed in the shared default-disabled queue by the current source initialization. This is consistent with the accepted “disabled until full rework” gate, but no re-enable scenario was available to test whether it can participate correctly.
- Rank reversal: no threshold or sensitivity sweep was possible, so no rank reversal is proven or disproven.
- Repetition: Event 29 is registered as repeatable and the shared cap/recovery path is present, but there is no visible Event 029 per-country, per-state, new-mine, or same-country/new-state memory. Repeat-recipient and duplicate-mine behavior therefore remains an unverified source risk, not an engine-proven exploit.
- Invalid positive weights: no Event 029-specific positive weights are present for impossible options because those options are not implemented. The unfiltered recipient path leaves target validity unresolved rather than proving invalid recipients are selected.
- Snowball risk: the current `2000` political-power reward is double the accepted design amount, but the live trigger cadence and recipient pool are unavailable. The magnitude is a source/spec discrepancy and a parent review item, not a completed balance conclusion.
- Hidden state: shared disabled flags, event weights, caps, settings overrides, firing history, global pacing, and candidate validity all affect the current event-ID pool and were not available to MCP.

## 8. Threshold and sweep status

No `hoi4.probability_sweep` call could be made, so there is no threshold artifact, sensitivity matrix, rank-reversal result, or rendered sweep.

The following are exact source observations only:

- Event 029 is registered with shared required chaos tier `0`; this is not an implementation of the accepted evolution thresholds `600`, `800`, and `1000`.
- The shared default event weight and initial cap are `1000`.
- The shared repeatable cap reduction factor is `0.5`.
- The shared recovery step is `20`.
- Valid event weights are scaled by `100` and rounded before the shared proportional roll.
- A scaled candidate below `1` is invalidated as a zero-weight candidate.

These knobs cannot establish scenario timing, event selection probability, or rank order without the complete candidate pool and runtime state. No claim is made that the shared recovery branch is equivalent to the accepted Event 029 monthly cadence; the visible source calls it from global event-pacing handlers and no Event 029-specific cadence is present.

## 9. Bounded patch/compare plan for the parent agent

This is a bounded follow-up plan, not a patch and not a balance target selection.

1. Complete the owner implementation for the accepted Event 029 surfaces while keeping Event 018 separate. At minimum, expose stable identifiers for the global event pool, recipient country pool, state suitability pool, initial policy, development, revenue, foreign target, security/raid, Evolution I/II/III MTTH, Gold Disease, Demons Beneath the Mine, Gilded Sovereignty, Bottomless Account, incident pools, and multi-mine registry.
2. In `events\029_riches_found.txt`, replace the unfiltered recipient path with the accepted ordinary-country plus valid-owned-and-controlled-state contract, and add the required target/exclusion memory. Resolve the `2000` versus accepted `1000` political-power discrepancy under owner review rather than changing it in this audit.
3. In `common\scripted_effects\chaosx_logic_effects.txt` and `common\scripted_triggers\chaosx_settings_triggers.txt`, preserve the shared registration contract but verify the final Event 029 enablement gate, disabled-state behavior, per-event validity, and recovery cadence after the complete Event 029 implementation exists.
4. Centralize any new Event 029 tuning values in the owner-selected `common\script_constants\` surface and place Evolution I/II/III MTTH variables in the owner-selected `common\mtth\` surface, following `chaos-redux-mtth`. The auditor must not choose numeric weights or thresholds.
5. After implementation, run `hoi4.probability_inspect` first for each stable surface and record the adapter revision, source revision, scenario hash, complete candidate pool, availability gates, costs, modifiers, scheduled state changes, cadence, and terminal states.
6. Run `hoi4.probability_evaluate` for all scenario ids in Section 5, including explicit controller, occupier, concession-seeker, neighbor, raider, country-scale, ideology, wartime-desperation, and multiple-mine inputs. Use `score-only` only for genuine `ai_will_do` outputs; use proportional probability for complete `ai_chance` or random-list pools; use timing classification for MTTH.
7. Run `hoi4.probability_sweep` over pressure, legitimacy, order, development, occupation duration, war desperation, relations, access, convoy availability, and mine count. Sweep the accepted chaos thresholds `600`, `800`, and `1000` only after the corresponding source gates exist. Record any dominance, starvation, threshold crossing, or rank reversal without converting scores into click probabilities.
8. Use `hoi4.probability_simulate` only for explicitly declared uncertain inputs and preserve the seed, sample count, uncertainty declaration, and sampled classification. Use `hoi4.probability_sequence` only after the complete custom incident/mine pool, cadence, recovery, cooldown, reset, removal, and terminal transitions are declared.
9. Use `hoi4.probability_render` for ranking tables, target matrices, timing distributions, threshold sensitivity, incident-pool composition, and multi-mine sequence views that improve review. Use `hoi4.probability_compare` after an owner-applied patch with the same scenario ids, candidate pools, state declarations, and external factors as the baseline. Do not compare a changed pool to an undeclared pool.
10. Use `hoi4.event_inspect` and `hoi4.event_render` for the completed chain and verify that the rendered structure agrees with the probability adapter's event, option, target, evolution, and terminal-state identifiers.

The required post-patch comparison set is the full `RF_POLICY_*`, `RF_DEV_*`, `RF_REV_*`, `RF_FOREIGN_*`, `RF_SEC_*`, `RF_EVO1_*`, `RF_EVO2_*`, `RF_EVO3_*`, `RF_GOLD_*`, `RF_DEMON_*`, `RF_GILDED_*`, and `RF_ACCOUNT_*` list above, plus the Surface M incident-pool and Surface N repeat-recipient/state-pool inspections. The auditor should preserve each comparison id and rendered evidence URI for the parent review.

## 10. Skipped analyses and remaining uncertainty

- Probability inspection was attempted first and blocked by the exact missing callable reported in Section 1.
- Probability evaluation, threshold sweeps, simulations, custom sequences, comparisons, and renders were skipped because their required routes were not callable.
- Structural Event 029 inspection and rendering were skipped because `hoi4.event_inspect` and `hoi4.event_render` were not callable.
- No live game or runtime validation was performed.
- The `RF_TEST_*` acceptance scenarios were not executed; they remain owner/runtime validation inputs.
- No exact selection probability exists for the Event 029 global event, recipient country, state, policy, foreign target, security action, incident, or evolution timing.
- No dominance, starvation, rank-reversal, repetition, or exploit result for the planned candidate pools can be engine-proven from this baseline.
- The default-disabled Event 029 state, shared weight/cap/recovery constants, unfiltered `random_country`, one-option `ai_chance`, and `2000` political-power effect are exact source observations only.

This report is a read-only baseline handoff. Event 029 Riches Found AI probability auditing is incomplete and unresolved, and no completion or balance claim is made.
