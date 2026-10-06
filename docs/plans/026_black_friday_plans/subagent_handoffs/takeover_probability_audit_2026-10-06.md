# Event 026 Black Friday probability takeover audit

Audit date: 2026-10-06.

Disposition: **Incomplete; current MCP probability conclusions remain unresolved.** The weighted routes are exposed in this child’s tool inventory, but valid source-bound inspect requests produced no result during bounded waits. No score, normalized probability, timing distribution, rank, comparison, or render is claimed from this audit.

Scope: read-only review of Event 026 option weights, the CXT price-probe decision, and the shared automatic event picker as it consumes the minor fire-once pool. No gameplay file, AI file, event catalog, workbook, or runtime source was edited. This handoff is the only file written by this audit.

## Inputs and source identity

Read AGENTS.md, the chaos-redux-subagents, chaos-redux-events, and chaos-redux-decisions-missions skills, Event 026 specification Part 5, Part 2 reservation/lifecycle, Part 8 acceptance scenarios, and the earlier probability_baseline.md and probability_final_audit.md handoffs.

The local tracked HEAD was 1e8aa914961a9f083ce544232f92b427d4fb02d7. The Event 026 event file had a working-tree addition for chaosx.nr26.3 when this handoff was finalized. Its full current local SHA-256 is AAA296D0FE93DCDD208490107669CA371B7C9DE14E54E9A93297F991F6121F2B. This is a local file hash, not an MCP source revision.

| Source | Relevant identity | Current local SHA-256 |
| --- | --- | --- |
| events/026_black_friday.txt | chaosx.nr26.2::chaosx.nr26.2.a; chaosx.nr26.3::chaosx.nr26.3.a | AAA296D0FE93DCDD208490107669CA371B7C9DE14E54E9A93297F991F6121F2B |
| common/decisions/026_black_friday_cxt_test_decisions.txt | chaosx_test_country_event026_price_probe_decision | 18EEDA72AE6AACFD89324C1259A1CFFEC6595552B8399BF5A1150D5EB2ADCE5D |
| common/scripted_effects/chaosx_settings_effects.txt | evaluate_random_event_selection_candidate; select_weighted_random_event_id | 62C7A2F13D7247543D82DBB16ACDC13AB8EE018F756EAACA07F9B8D4E288908C |
| common/scripted_effects/chaosx_logic_effects.txt | initialize_event_categories; initialize_event_chaos_level_registry; evaluate_random_event_active_pool_candidate | 7D4AE19F327AEBA7A62C98BDA9236369A319BE528752E80A9B5C6C734A5F2B81 |
| common/scripted_triggers/026_black_friday_triggers.txt | black_friday_can_reserve; black_friday_can_activate_naturally; black_friday_achievement_is_valid_sale | 8E17E5C115EB802D35D4454DFBEEA14F759A6E149AA3C1BDA5A62A27D31BDD94 |
| common/scripted_effects/026_black_friday_effects.txt | activation, dispatch, reservation, and purchase-credit effects | C87484884BB5BB7386C255038DE5BC9056826AD446928D9466D48D2AFB2D8EB0 |
| common/script_constants/026_black_friday_constants.txt | Event 26 thresholds, ratios, and dispatch modes | FAF844C23F27A8F27A5D5435FFB5BCA9162A127696A9D7460C0B96061F1C9E86 |

The source addition visible in events/026_black_friday.txt adds failure-notice event chaosx.nr26.3 with its sole option chaosx.nr26.3.a at raw ai_chance.base = 100. The existing informational event chaosx.nr26.2 retains its sole option at raw base 100. The added option is in a separate event, so it does not join the .2 option pool. No balancing target or weight change is proposed; the parent reports that the current tranche changes no weights.

## Audited surfaces and source observations

| Surface | Exact source and identifiers | Source observation | Classification |
| --- | --- | --- | --- |
| Informational event option | events/026_black_friday.txt:18-32; chaosx.nr26.2::chaosx.nr26.2.a | One local option with raw ai_chance.base = 100. The local event source contains no competing option. | Source-only; conditional option result unresolved by MCP. |
| Manual failure-notice option | events/026_black_friday.txt:35-71; chaosx.nr26.3::chaosx.nr26.3.a | The failure notice has one option with raw ai_chance.base = 100. Its parent event is sent from the human-only manual/force no-op path. | Source-only; conditional option result unresolved by MCP. |
| CXT price-probe decision | common/decisions/026_black_friday_cxt_test_decisions.txt:10-22; chaosx_test_country_event026_price_probe_decision | ai_will_do.base = 0; visibility requires tag CXT, is_ai = no, and the initialized test-country flag. This is a source score and availability gate, not a click probability. | Score-only from source; MCP result unresolved. |
| Automatic event selection consumer | common/on_actions/chaosx_on_actions_system.txt:181-192; common/scripted_effects/chaosx_settings_effects.txt:3810-3862, 3864-3923 | The daily timer sets filter all, calls select_weighted_random_event_id, then dispatches the returned ID. The picker validates candidates, scales each accepted raw event weight by 100, rounds it, sums the accepted pool, draws an integer from 1 through that total, and selects the first cumulative total reaching the roll. This is proportional sampling over a dynamic pool, not an ai_will_do score race. | Source-only algorithm; normalized Event 26 selection probability unresolved. |
| Event 26 pool registration and base weight | common/scripted_effects/chaosx_logic_effects.txt:244-283, 335-405, 516-551; common/script_constants/event_system_constants.txt:33-41; common/scripted_triggers/chaosx_settings_triggers.txt:1-30 | Event ID 26 is registered once in global.fire_once_events and included in global.all_events. Its default-enabled allowlist entry is present. Non-major event weights initialize from global.default_event_weight, which defaults to 1000, and the current stored global.event_weights[26] is what the picker reads. Settings and live weights remain external scenario state. | Bounded source input; current numeric pool and ranking unresolved. |
| Chaos and reservation validity | common/scripted_effects/chaosx_logic_effects.txt:156-184, 887-943; common/scripted_triggers/026_black_friday_triggers.txt:64-89; common/script_constants/026_black_friday_constants.txt:15-34 | Event 26 maps to internal tier 1, whose local threshold begins at 200. Reservation also requires a running event system, enabled/unfired/unreserved/inactive state, and chaos at least 200. The active-pool wrapper rejects disabled events, fired unique events, unmet chaos, and a reserved Event 26 before its weight is added. | Bounded source gate; engine eligibility unresolved. |
| Reservation and activation | common/scripted_effects/026_black_friday_effects.txt:4215-4317, 4320-4414 | Natural activation requires a reservation, Friday, chaos at least 200, enabled state, and an unfired/inactive sale. Natural reservation resolves the current timer transaction. A reservation can wait through a Friday below 200; a later eligible Friday or same-day eligible selection activates it. The ratio is chosen at activation: baseline payment ratio 5000/10000 (50% discount), or 2500/10000 (75%) at chaos 600 or higher when Evolution I is enabled. The active snapshot is retained through the sale. | Bounded source lifecycle; timing and runtime transitions unresolved. |
| Forced/manual provenance and achievement credit | common/scripted_effects/026_black_friday_effects.txt:4243-4267, 4354-4387, 5152-5183; common/scripted_triggers/026_black_friday_triggers.txt:101-128 | Force dispatch sets the force-disqualified flag and can activate without the ordinary chaos/Friday reservation path, while still requiring a running system and a non-disabled, unfired, inactive event. Ordinary manual dispatch is distinguished from natural selection and disqualifies achievement progress. Natural-sale credit also requires a human non-debug campaign and valid sale sequence; the sale-credit path therefore excludes AI, forced, manual, debug, and already-awarded credit. | Bounded source restriction; runtime credit outcomes unresolved. |

The raw ai_chance = 100 on either sole local event option is not reported here as an MCP-proven 100% result. The offline Event modding wiki describes event-option ai_chance as proportional sampling with d100 granularity. The offline AI modding wiki distinguishes this from ai_will_do, which participates in a highest-score race and may receive strategy modifiers. The installed vanilla documentation directory has no ai_chance or ai_will_do section; effects_documentation.md:5413-5430 documents random_list as weight-associated random selection. Relevant local pages read were paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:150-180, paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:26-50, and paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:357-379.

## Named scenario review

Part 5 names bf_ai_01_low_reserve_advisor through bf_ai_08_75_percent_high_chaos at docs/specs/026_black_friday_specs/026_black_friday_spec_part_5_ai_multiplayer_balance_and_exploit_controls.md:33-50. No MCP scenario rows, score traces, or ranking results returned in this audit, so all eight remain unresolved.

| Scenario ID | Source-linked observation | Candidate pool / external-factor coverage | Classification |
| --- | --- | --- | --- |
| bf_ai_01_low_reserve_advisor | Part 5 requires a sale-price advisor decision that still respects the PP reserve. | Advisor candidates, final quote, reserve, PP, strategy factors, route and availability inputs were not adapter-enumerated. | Unresolved. |
| bf_ai_02_valid_law_change | Part 5 requires valid desired laws to compete after price reduction. | Complete law pool, law gates, quote, PP reserve, strategy factors, and cooldown were not supplied to a responding adapter. | Unresolved. |
| bf_ai_03_wartime_command | Part 5 requires existing tactical logic to remain decisive during a cheaper valid command action. | Command candidates, battle/tactical state, command power, PP, cooldowns, and targets were not adapter-enumerated. | Unresolved. |
| bf_ai_04_invalid_target | Part 5 expects an invalid target to retain zero effective willingness. | Foreign-action pool and target/route validity were not supplied or evaluated. | Unresolved. |
| bf_ai_05_static_variant_pool | Event 026 source shows no normal/discounted static action variants in these event or CXT files. | Owner action variants and current eligibility were not enumerated; these source files do not establish the complete owner pool. | Bounded source observation; pool-level conclusion unresolved. |
| bf_ai_06_overlapping_discount | The sale ratio is source-visible, while owner quote composition belongs to the action adapter. | Complete action pool, modifier order, caps, final rounding, and reserve policies were not evaluated. | Unresolved. |
| bf_ai_07_sale_expiry | Source snapshots a sale at activation and has a daily expiry path. | AI re-quote timing, transaction confirmation, resources, and owner action gates were not supplied. | Bounded lifecycle source observation; action outcome unresolved. |
| bf_ai_08_75_percent_high_chaos | Source selects the 75% discount at activation when chaos is at least 600 and Evolution I is enabled. | Complete AI action pool, strategy factors, reserves, and thresholds were not swept. | Bounded source threshold; action selection unresolved. |

Related acceptance scenarios support only bounded source checks here: BF-T01 expects no Event 26 eligibility at chaos 199; BF-T02 reserves after selection at chaos 200 on Monday; BF-T03 waits until an eligible Friday; BF-T05 keeps a reservation when Friday arrives below 200; BF-T07 activates the baseline tier at 599; BF-T08 activates Evolution I at 600; BF-T09 and BF-T10 retain the activation snapshot when chaos changes during the active day. These are source-compatible state cases, not MCP timing or probability results.

BF-X18 specifies no achievement-family credit after a manual, forced, debug, or AI sale. The source trigger/effect restrictions listed above implement those exclusions in source. No campaign scenario or live-engine credit result was returned, so this audit classifies the outcome as bounded source support and runtime-unresolved.

## MCP route evidence and exact blockers

The child inventory exposed these qualified probability routes: mcp__hoi4_agent_tools__hoi4_probability_inspect, mcp__hoi4_agent_tools__hoi4_probability_evaluate, mcp__hoi4_agent_tools__hoi4_probability_sweep, mcp__hoi4_agent_tools__hoi4_probability_compare, mcp__hoi4_agent_tools__hoi4_probability_render, mcp__hoi4_agent_tools__hoi4_probability_simulate, and mcp__hoi4_agent_tools__hoi4_probability_sequence. Exposure did not establish a completed service response. No refresh=true argument was used.

The exposed probability_inspect schema accepts mod-relative source objects. Initial probes used source: { relativePath: ... } and returned the exact validation error: MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: Unrecognized key: "relativePath" at source. The retry used source: { path: ... } as specified by the local subagents skill.

A valid one-at-a-time event_option_ai_chance inspect for events/026_black_friday.txt, candidate chaosx.nr26.2.a, remained pending for about 2½ minutes and was terminated without a result, artifact, source revision, or scenario hash. The source file’s .3 event was added after that request began; no inspect was run against the finalized current .3 source because the parent directed that no further retries were needed.

A source-bound batch inspect for event_option_ai_chance on events/026_black_friday.txt and decision_ai_will_do on common/decisions/026_black_friday_cxt_test_decisions.txt, both with source: { path: ... }, stayed pending for about 3 minutes and was terminated without per-call output. The lack of per-call output means that the batch does not establish whether either adapter produced an intermediate result.

A source-bound custom_weighted_pool inspect for common/scripted_effects/chaosx_settings_effects.txt stayed pending for about 2½ minutes and was terminated without output. The earlier Event 026 handoff reported zero candidates and poolComplete = false for this adapter, but that historical result is not a current revision-bound result.

A narrow structural hoi4.event_inspect trace was attempted with a string from and returned the exact validation error: MCP error -32602: Input validation error: Invalid arguments for tool hoi4.event_inspect: Invalid input: expected object, received string at from. The corrected selector request { kind: event, eventId: chaosx.nr26.1 } remained pending for the 31-second bounded observation and was terminated without an artifact. No broad state_flow, helper expansion, or repository-wide analysis was run.

No current artifact URI, MCP source revision, scenario hash, comparison ID, or rendered evidence URI exists from these calls. The exposed event_render route was not called because the bounded event inspect returned no graph artifact to render. No probability_evaluate or probability_sweep was run because inspect supplied no accepted inputs or scenario schema. probability_compare was not run because there is no real same-scenario before artifact for the current source and the parent reports no weight change. probability_simulate was not applicable because no uncertain-input distributions or seed were declared. probability_sequence was not applicable because no complete custom-pool manifest with cadence, transitions, and terminal states was provided. probability_render had no retained current analysis ID to render.

The prior probability_baseline.md and probability_final_audit.md remain historical records, not current receipts. The 2026-09-02 final handoff’s exact event-option result covered only the one-option chaosx.nr26.2.a source; its eight-scenario result did not cover the sale-action AI pool. Its custom pool remained incomplete with zero candidates. Its MCP revisions, artifacts, and rendered outputs are preserved in that prior handoff and are not asserted as current evidence for the source hash above.

## Findings and parent follow-up

No current conclusion establishes Event 26’s normalized rank or probability in the live automatic event pool, the frequency of arrival, timing drift, action-AI dominance or starvation, rank reversal, or repetition/snowball behavior. The picker’s full runtime candidate pool depends on global.all_events, each event’s current stored weight, the filter, disabled/fired state, chaos gates, dynamic candidate-specific unavailability, and the global timer state; none was supplied as a complete current MCP scenario.

Source supports that a reserved Event 26 leaves selection through its reservation blocker without first adding a fired-history entry, while the picker continues to normalize the remaining currently valid pool. Source also sets Event 26’s stored weight marker to 1 when activation history is recorded, after which unique-event fired exclusion prevents re-entry. These are bounded source observations; no probability delta or timing distribution is proven.

The concrete follow-up is to rerun probability_inspect for the finalized .2.a and .3.a event-option surfaces, the CXT decision adapter, and the shared picker when the route returns results. Evaluate the eight Part 5 scenarios only after inspect returns accepted scenario fields, then sweep explicit numeric ranges only if a ranking or threshold question is declared. The picker scenario needs a complete active global.all_events candidate pool and state/weight inputs. The Part 5 owner-action scenarios need their full action families, final costs, reserve floors, route/target/cooldown gates, competing modifiers, and AI strategy factors. No gameplay weight fix is recommended by this audit.

Skills applied: chaos-redux-subagents, chaos-redux-events, and chaos-redux-decisions-missions. No skill was created or updated.




