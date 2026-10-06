# Event003 weighted release evidence

Status: bounded source review complete; probability evidence remains unresolved.

I made no gameplay, AI, event, focus, decision, mission, effect, trigger, strategy, localisation, or spreadsheet changes, and I did not commit.

The parent’s latest instruction says the numeric AI weights are unchanged and a probability comparison is not required without a weight edit; I therefore did not run `hoi4.probability_compare`.

The current decision source hash below was supplied by the parent as frozen and verified locally before this report was written.

All source observations are bound to the reviewed hashes in the table; the event and scripted-effects files changed again before the final identity check, and those later bytes were not reviewed.

## MCP status

The live probability tools are exposed, but my six current-source `hoi4.probability_inspect` requests for `event_option_ai_chance`, `decision_ai_will_do`, `national_focus_ai_will_do`, `ai_strategy_factor`, `random_list`, and `direct_random` returned no result or tool-level error before the parent asked me to stop waiting.

I made one single-source retry for `event_option_ai_chance` on `events/003_the_holy_realm.txt`; it also returned no result or error and I terminated its wait under the parent’s instruction to avoid another long MCP wait.

No `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, `hoi4.probability_render`, or sequence/simulation call completed in this release review.

No analysis ID, MCP source revision, scenario hash, comparison ID, artifact URI, or rendered evidence is available, so I make no probability, score-trace, ranking, timing, dominance, starvation, or rank-reversal claim.

The parent reported that a separate focus inspector succeeded, but its artifact and revision were not passed to this probability handoff; I did not receive event trace/render evidence or make another structural MCP request.

## Source identities

| Surface | Reviewed source SHA-256 | Frozen 2026-10-05 source SHA-256 | On-disk hash at close |
| --- | --- | --- | --- |
| `events/003_the_holy_realm.txt` | `5DCEDB956D5A2A6309F460C4134FEBACBF0A38F6BD46A679600FBDA7FE8BA629` | `DA715562A72AECFCBE54744B07958C045B55E032E5CC9F83CEC43B0365737D0B` | `149D693B96F008FA7977DF3A1CFC179D47A772C727BF57C76C968C50A65E0E16` (not reviewed) |
| `common/decisions/003_holy_realm_decisions.txt` | `88DAE2B720A330214A3858623AC41010B2FBDAB10D0402CDE833AAB6D5B54C04` | `41D5F00ED33E8BE4457762054F6A9F7589D9EA4621B4890445292748107DAA5C` | same as reviewed |
| `common/national_focus/003_holy_realm.txt` | `29C3BD371CFC53912C1F3C72BDD00CEFB2262BD6303EE7195DE5750E244278D9` | `2FC00143958DD042884832F922055C00AC859EEBEFC19DD4D1DD2146ACFBD7AD` | same as reviewed |
| `common/scripted_effects/003_holy_realm_effects.txt` | `8F0D3732FA23A15A59288A445FA84759194C94C07C78B6FF0F0F5A016E8BEDA4` | `E2DB87896575D046683C1579C774912237414B73F35FFF549208F0A543A7A4E3` | `EC66BD83349BCE11B3DEA1DFD4C15008777A6BFBDB228C4DB08CDFD9C73CD710` (not reviewed) |
| `common/scripted_triggers/003_holy_realm_triggers.txt` | `E0E7F8151B468911022F761FBA6F63FA76C674694D86C793FEBCA4906EF32964` | `6257489D3ED69EB2EAC7A367F51121F17F6A2BD8CB16E2E6C6D2914F646DEAD1` | same as reviewed |
| `common/script_constants/003_holy_realm_constants.txt` | `F23AD9391B47AF234B2FBB58DA461BCEE23295EA9B2B618A853DCFAF9EB0EB59` | `A11E2834F0CFEF0FFE778F268FAA9C291649CCB1450AFA3047D6ED97F0FC740C` | same as reviewed |
| `common/on_actions/003_holy_realm_on_actions.txt` | `9DB90ED70C61553CB4EF7973BD8E24A5F58F7D7C2DEF0E714A1994077C60DC36` | `E8B352B154606038CA059186CD43E0575B09BE16C858AFA2C5D466FC370970EA` | same as reviewed |

The frozen copies are under `docs/plans/003_holy_realm_plans/source_snapshots/release_qa_20261005/`.

There is no frozen `common/ai_strategy/003_holy_realm.txt` copy in that directory, so I cannot identify a valid before source for strategy-factor comparison.

## Declared scenarios and evidence completeness

The IDs below preserve the earlier baseline labels and add the release-specific cases requested by the parent; none was submitted to the MCP analyzer, so none has an analyzer scenario hash.

| Scenario ID | Source-derived assumptions | Candidate and external-factor coverage | Result class |
| --- | --- | --- | --- |
| `usa_1936_entry` | 1936-01-01 USA campaign entry with no existing `holy_realm_exists` flag | TIB/BHU/NEP existence, host eligibility, on-action dispatch, and AI/player control are not runtime-observed | unresolved |
| `usa_1936_two_months` | 1936-03-01 follow-up with an assumed active THR host after the refuge chain | Host route, choices, later flags, variables, focus completions, decisions, strategy activation, and war state are incomplete | unresolved |
| `tib_host_setup` | TIB exists, passes `can_host_holy_realm_refuge`, and `holy_realm_exists` is unset | The TIB-priority branch is source-defined; recipient automation and entry dispatch are not observed | unresolved |
| `teaching_bhumi_3`, `teaching_bhumi_6`, `teaching_bhumi_10` | THR begins at the named `bodhisattva_bhumi` value with the teaching system unlocked | Slot count, other decision candidates, pending event callbacks, PP, sale quote, focus route, legitimacy, and final-doctrine state are incomplete | unresolved |
| `sale_25_actual_fee` | A 25 percent sale ratio is assumed for the named native PP costs | The active sale sequence, table refresh state, quote quantum, live affordability, concurrent sale changes, and available decision pool were not analyzer-resolved | unresolved |
| `sanctuary_capital_missing`, `sanctuary_current_capital_secured` | THR has completed the named `THR_buddha_mandate` prerequisites; scenarios vary current-capital control and recent-fall state | Other completed/available focuses, bypasses, strategy plan, and route state are incomplete | unresolved |
| `final_silence_999`, `final_silence_1000`, `final_silence_1001` | The global chaos meter is assumed to be 999, 1000, or 1001 | Final-doctrine balance, focus prerequisites, availability, strategy factors, and other candidates are incomplete | unresolved |

## Source findings

At reviewed event hash `5DCEDB956D5A2A6309F460C4134FEBACBF0A38F6BD46A679600FBDA7FE8BA629`, `events/003_the_holy_realm.txt` has 47 explicit `ai_chance` blocks, matching the frozen file, and no `mean_time_to_happen` entry.

The event file’s different close hash means the reviewed event counts and option details below must not be treated as verified for the latest on-disk bytes.

The `chaosx.nr3.1` root now checks only that `holy_realm_exists` is absent, selects the host, and sends a no-target fallback event when the host selector returns no target (`events/003_the_holy_realm.txt:26-60`).

The reviewed host effect prefers eligible TIB and otherwise calls `random_country` with `can_host_holy_realm_refuge` (`common/scripted_effects/003_holy_realm_effects.txt:2575-2588`), while the reviewed trigger admits TIB or BHU/NEP in the TIB-absent branch (`common/scripted_triggers/003_holy_realm_triggers.txt:12-42`).

On the `nr3.1` route, a player-controlled host receives `chaosx.nr3.2` after one day, while the AI-host branch forms THR directly and schedules `chaosx.nr3.4` after twenty days (`events/003_the_holy_realm.txt:36-58`).

The four `nr3.2` candidates are `.a` base 0, `.b` base 100 with a factor of 2 for TIB/original TIB, `.c` base 0, and `.e` base 1 with factor 0 for AI, factor 15 when global chaos exceeds 700, and factor 2 after 1940-12-31 (`events/003_the_holy_realm.txt:86-175`).

Because the normal AI-host branch bypasses `nr3.2` in this source path, those option weights do not govern that branch; other event callers were not traced, so overall reachability remains unresolved.

The linked decision `THR_hold_dharma_teaching` has `ai_will_do = { factor = 2 }`, charges the native `global.black_friday_price_pp_25` quote, and invokes a four-entry random list after six hours (`common/decisions/003_holy_realm_decisions.txt:943-973`).

That list is source-complete: weight 35 selects `chaosx.nr3.110`, 25 selects `.111`, 25 selects `.112`, and 15 selects `.113` (`common/decisions/003_holy_realm_decisions.txt:962-967`).

Each of those four events has two local options without an explicit `ai_chance`; the offline Event modding page says an unset option uses the default weight of 1, but no MCP result confirms how the installed probability adapter resolves these pools (`events/003_the_holy_realm.txt:1696-1854`; `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:157-161`).

At the reviewed event hash, `chaosx.nr3.74` is another incomplete explicit-weight pool: option `.a` has no `ai_chance`, while `.b` has base 30 and modifiers that set it to zero when the final doctrine leans final or final-silence pressure exceeds 59 (`events/003_the_holy_realm.txt:661-712`).

Options `chaosx.nr3.110.b` and `chaosx.nr3.111.b` grant the new 5 PP teaching outcomes and both advance the Bhumi helper (`events/003_the_holy_realm.txt:1720-1729` and `1758-1767`).

The reviewed advancement helper increments Bhumi only below its maximum of 10 and uses strict `>` milestone checks; it grants 50 PP above floor 3, 75 PP plus 15 command power above floor 6, and stability above floor 8, with one-time country-flag guards present (`common/scripted_effects/003_holy_realm_effects.txt:983-1040`; `common/script_constants/003_holy_realm_constants.txt:219-232`).

Those one-time guards are absent from the frozen helper, so the frozen source could repeat the milestone payouts after later teaching completions; the reviewed helper prevents repeating those milestone rewards.

The parent explicitly accepts `THR_hold_dharma_teaching` remaining available at Bhumi 10 as intentional teaching activity: the increment stops at the cap, success is still recorded, and milestone payouts are one-time.

That parent intent is not a probability result; the amount charged under the assumed sale ratio and the joint selection of the random-list outcome and its two-option event remain MCP-unresolved.

The new `holy_realm_bhumi_advancement_available` trigger permits an unset Bhumi variable or a value below the configured maximum (`common/scripted_triggers/003_holy_realm_triggers.txt:76-85`).

It now gates `THR_bodhisattva_mission_refuge_circuit`, `THR_bodhisattva_mission_white_scarf_envoys`, `THR_bodhisattva_mission_wounded_border`, `THR_bodhisattva_hold_teachings_for_refugees`, and `THR_bodhisattva_teach_foreign_officers` (`common/decisions/003_holy_realm_decisions.txt:975-1080` and `2172-2245`).

Their `ai_will_do` source lines are unchanged versus the frozen decision source; the current decision file has 113 such blocks and the frozen copy also has 113.

The source scores for `THR_bodhisattva_mission_refuge_circuit`, `THR_bodhisattva_mission_white_scarf_envoys`, and `THR_bodhisattva_mission_wounded_border` remain 2, 1.5, and 1; refugee teaching and foreign-officer teaching remain 1.2 and 0.8; `THR_hold_dharma_teaching` remains 2, `THR_bodhisattva_invite_foreign_pilgrims` remains 1, and `THR_register_outer_valleys` remains 2; these are willingness scores, not click probabilities.

`THR_bodhisattva_invite_foreign_pilgrims` consumes `bodhisattva_pilgrim_cost = 155` and has a source AI score of 1 (`common/script_constants/003_holy_realm_constants.txt:145`; `common/decisions/003_holy_realm_decisions.txt:2353-2389`).

The separately named `THR_register_outer_valleys` uses `submitted_admin_cost = 125` and grants 25 PP (`common/script_constants/003_holy_realm_constants.txt:124`; `common/decisions/003_holy_realm_decisions.txt:1655-1685`), so a scenario that calls this a 155-cost registration does not match the current source identifier.

The shared price quote applies `global.black_friday_discount_ratio`, rounds positive quotes up to their configured quantum, keeps the result no higher than the ordinary price, and writes the resulting payable cost (`common/scripted_effects/026_black_friday_price_table_effects.txt:32-81` and `3177-3183`).

No MCP result established the 25 percent sale’s actual PP charge, whether the sale state was active for AI, or the relationship between that charge and the 25 PP outer-valleys reward.

The current `THR_buddha_mandate` focus adds the `holy_realm_capital_sanctuary_secured` availability trigger; its frozen copy did not have this gate (`common/national_focus/003_holy_realm.txt:1057-1082`; frozen focus snapshot: lines 1051-1076).

The trigger checks that the current capital is controlled by ROOT and that `holy_realm_capital_sanctuary_recently_fallen` is absent (`common/scripted_triggers/003_holy_realm_triggers.txt:95-100`).

`THR_buddha_mandate` has no explicit `ai_will_do`, so the offline National focus page’s default score of 1 is the only source-level score rule available here; no complete available-focus pool or independent score race was evaluated (`paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:604-623`).

Final Silence’s configured gate remains 1000 in current and frozen constants (`common/script_constants/003_holy_realm_constants.txt:75`).

At exactly 1000 the strict `>` modifiers remain false; they become true above 1000 in `THR_throne_without_body` (base `@holy_realm_ai_final_entry_factor`, plus its route/chaos modifiers) and `THR_bop_expand_silence_cells` (base 0.4, multiplied by 4 only when the final balance leans final) (`common/national_focus/003_holy_realm.txt:1855-1897`; `common/decisions/003_holy_realm_decisions.txt:3620-3654`).

These facts establish the source condition boundary only; other route prerequisites, strategy modifiers, active focus/decision candidates, and ranking were not analyzed by MCP.

The reviewed strategy file contains 14 named packages and 19 `ai_strategy` directives (`common/ai_strategy/003_holy_realm.txt`, SHA-256 `05013995D0729FAA412785869F31A52B00F3FD5937BDF0F42C755ADED394FBE3`), but the frozen snapshot directory contains no matching strategy source.

Its raw directives are `holy_realm_refuge_defence` (avoid war 150, defend ally borders in Asia 100), `holy_realm_himalayan_consolidation` (avoid war -20), `holy_realm_expansionist_mandala` (build army 80, avoid war 30), `holy_realm_expansionist_forced_integration` (avoid war -35), `holy_realm_peaceful_power_growth` (build army 60, infrastructure 80), `holy_realm_mandate_intervention` (volunteer desire 80), `holy_realm_renunciation_restraint` (avoid war 200, volunteer desire 30), `holy_realm_peacekeeper_route` (volunteer desire 120, avoid war 90), `holy_realm_coercive_route` (avoid war -50), `holy_realm_final_doctrine_restraint_until_gate` (avoid war 120), `holy_realm_foreign_contain_tibet` (antagonize TIB 100), `holy_realm_foreign_contain_bhutan` (antagonize BHU 100), `holy_realm_foreign_contain_nepal` (antagonize NEP 100), and `holy_realm_foreign_emergency_response` (defend ally borders 150).

Those strategy values are directives, not normalized probabilities; package activation triggers and external strategy-plan modifiers were not evaluated.

## Evidence references and remaining blockers

The offline wiki sections read directly were `AI modding - Hearts of Iron 4 Wiki.md:26-36,74-80`, `Event modding - Hearts of Iron 4 Wiki.md:157-161`, `Decision modding - Hearts of Iron 4 Wiki.md:361-373`, and `National focus modding - Hearts of Iron 4 Wiki.md:604-635`.

The installed vanilla documentation read directly was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:5372-5379,5413-5428`, covering `random_country` and weighted `random_list` syntax.

The HOI4 `reference_context`, `reference_search`, and `reference_read` routes were not used in this bounded release pass because the parent directed me not to wait on additional long MCP requests; the local offline pages above were read directly instead.

No probability candidate-pool completeness, modifier trace, normalized event share, decision rank, focus independent-score race, strategy factor trace, threshold sweep, or comparison result is available.

Recommended next evidence step is one short successful `probability_inspect` per affected adapter followed by named scenario evaluation once the service returns promptly; retain the current source hashes above and use the frozen `.before` files for any later requested comparison.

No AI-weight change is recommended by this source-only pass.
