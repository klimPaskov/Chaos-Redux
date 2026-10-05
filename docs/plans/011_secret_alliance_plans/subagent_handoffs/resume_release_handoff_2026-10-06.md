# Event 011 release repair handoff, 2026-10-06

## Status

The authorized Event 011 source repairs are applied, but the release remains incomplete because current event and GUI inspection artifacts are unavailable, post-gate probability certification did not return, and the permanent asset source manifest is missing. The parent performs the isolated focused commit after reviewing the shared tree.

Acceptance basis: the parent’s explicit Event 011 release direction authorizes the cost bundle repairs, per-resource cost colors, separate Stability eligibility copy, forced-entry feedback, and relevance gates. The parent also accepted retaining the seven-action mapped-border Evolution II case where both distinct paid operations remain meaningful.

No game was launched. No desktop was controlled, no spreadsheet or CSV was opened or edited, and no stage, reset, stash, checkout, clean, or commit action was performed.

## Changed Event 011 paths and behavior

| Path | Identifiers or change |
| --- | --- |
| `common/decisions/011_secret_alliance_decisions.txt` | Eleven over-budget decision instances now use four or fewer spendable types. Special political-power and Border Escalation War Support checks share named affordability helpers. The four relevance gates below apply to this decision file. |
| `common/scripted_effects/011_secret_alliance_effects.txt` | Removed the obsolete Convoy affordability check from `secret_alliance_run_available_ai_protection`; its outer helper still checks the shared protection bundle, and the port action still checks and pays Fuel. Initialized the caller-owned Black Friday quote output before invoking the shared quote helper. Owner-side entry failures route through the shared feedback helper. |
| `common/scripted_triggers/011_secret_alliance_triggers.txt` | Added exact dynamic quote checks for Partial Dossier, Name Member, Expose Sponsor, Coalition Case, diplomacy Command Power, and border-escalation War Support. Existing diplomacy helpers call the named Command Power check. |
| `common/scripted_localisation/011_secret_alliance_cost_display.txt` | Added 20 country-scope per-resource getters for ready and deficient inline or hover amounts. |
| `common/scripted_localisation/011_secret_alliance_gui_scripted_localisation.txt` | Retained the compact cohesion and readiness band getters and required status fallback. Current rendered GUI evidence is still unavailable. |
| `events/011_secret_alliance.txt` | Entry `.1` checks active context before initialization and assigns one specific failure reason for invalid target, missing country, active chain, or unavailable route. Scenario composition failure routes through the shared feedback hook. No `.204` event remains. |
| `localisation/english/011_secret_alliance_l_english.yml` | Added the per-resource cost colors and 40% Stability floor key, updated 12 relevant requirement tooltips, renamed `chaosx.nr11.3.t` to “Orders from Unknown Hands,” and added the mapped-route interception requirement. |
| `docs/events/011_secret_alliance/overview.md` | Reconciled the prior historical claims and current release evidence limits. |
| `docs/plans/011_secret_alliance_plans/agent_decisions_2026-10-05.md` | Records source choices, dispositions, evidence, and blockers. |
| `docs/plans/011_secret_alliance_plans/catalog_changes_pending.md` | Records accepted-and-queued catalog wording because XLSX and CSV edits are out of scope. |
| `docs/plans/011_secret_alliance_plans/probability_snapshots/before_2026-10-05/011_secret_alliance_decisions.txt` | Byte-exact copy of the pre-repair Git HEAD decision source. Its blob is `b1c9be23c84c0a34a3f7b66d5fe69b7d625c727e`, matching HEAD `1b79965f46cd1e9babfc223575d18112dbaafefe`. |

`secret_alliance_has_dynamic_partial_dossier_political_power_cost`, `secret_alliance_has_dynamic_name_member_political_power_cost`, `secret_alliance_has_dynamic_expose_sponsor_political_power_cost`, `secret_alliance_has_dynamic_coalition_case_political_power_cost`, `secret_alliance_has_dynamic_diplomacy_command_power_cost`, and `secret_alliance_has_dynamic_border_escalation_war_support_cost` are the new trigger identifiers. The first five use the same cached amount as their displayed and debited fees. The border-escalation helper uses the same variable as its War Support payment. Diplomatic cost requirements state the minimum Stability separately from the fee.

## Cost bundles before and after

| Decision | Before | After |
| --- | --- | --- |
| `secret_alliance_protect_ports_and_airfields` | Command Power, Army Experience, Support Equipment, Fuel, Convoys | Command Power, Army Experience, Support Equipment, Fuel |
| `secret_alliance_run_controlled_shipment` | Command Power, Army Experience, Support Equipment, Trains, Trucks | Command Power, Army Experience, Support Equipment, Trucks |
| `secret_alliance_sabotage_forward_depot` | Command Power, Army Experience, Support Equipment, Trains, Fuel | Command Power, Army Experience, Support Equipment, Fuel |
| `secret_alliance_seize_courier_aircraft_or_vessel` | Command Power, Army Experience, Support Equipment, Trains, Fuel, Convoys | Command Power, Army Experience, Support Equipment, Fuel |
| `secret_alliance_begin_limited_border_conflict` | Command Power, Army Experience, Support Equipment, Trains, Manpower | Command Power, Army Experience, Support Equipment, Manpower |
| `secret_alliance_emergency_mobilization` | Command Power, Support Equipment, Manpower, Fuel, Stability | Command Power, Support Equipment, Manpower, Stability |
| `secret_alliance_fortify_exposed_approaches` | Command Power, Support Equipment, Manpower, Fuel, Stability, Trains | Command Power, Support Equipment, Stability, Trains |
| `secret_alliance_recall_overseas_assets` | Command Power, Support Equipment, Manpower, Fuel, Stability, Convoys | Command Power, Support Equipment, Stability, Convoys |
| `secret_alliance_preempt_coalition` | Command Power, Support Equipment, Manpower, Fuel, Stability, War Support | Command Power, Support Equipment, Stability, War Support |
| `secret_alliance_seek_defensive_alliance` | Command Power, Support Equipment, Manpower, Fuel, Stability | Command Power, Support Equipment, Manpower, Stability |
| `secret_alliance_evacuate_critical_leadership` | Command Power, Support Equipment, Manpower, Fuel, Stability, Trains | Command Power, Support Equipment, Stability, Trains |

The source contains six over-budget Evolution III decisions, because Emergency Mobilization and Seek a Defensive Alliance share one cost profile, while Preempt the Coalition is separate. The final private warning remains three costs: Political Power, Command Power, and Stability. Railway supply and divisions remain border-conflict requirements rather than payments.

The 31 cost localization families cover 54 decision instances. Each family has a base, `_blocked`, and `_tooltip` key. Twenty getters select forty ready or deficient component keys. `_blocked` aliases the base row so a failed unrelated gate cannot make affordable fees appear unaffordable. Static nested-key expansion confirmed no more than three inline amounts and no more than four spendable types in the full hover bundle. The localization auditor confirmed the icons, formats, aliases, and UTF-8 BOM.

The decision audit confirmed that gates, displayed cached fees, and debits agree for all eleven listed actions. The emergency split-payment helpers charge the same four-cost bundles. The limited border-conflict package is charged only after the border war begins. The AI port-protection branch no longer checks a Convoy reserve that the player action does not spend. No amount, scale, sale ratio, outcome amount, or numeric AI weight changed in the cost repair.

At the start of `secret_alliance_refresh_dynamic_costs`, the caller initializes `black_friday_price_payable` to the shared zero constant before passing the output through `black_friday_price_table_quote`. This follows the Event 026 quote-helper contract, which documents the value as caller-owned. It does not change any ordinary amount, price ratio, scale, or AI weight.

## Decision-list relevance and accepted density exception

`secret_alliance_compartmentalize_staff_plans` now appears after an intelligence operation, matching the accepted Event 011 decision matrix’s “Intelligence clue” route. `secret_alliance_intercept_survey_team` now appears only after mapped routes exist, matching the accepted matrix’s mapped-route requirement and preserving the earlier reconnaissance action as its setup phase.

`secret_alliance_offer_separate_terms` now appears only for a selected active enemy member that has not capitulated. `secret_alliance_demand_sponsor_accountability` now appears only for an unused selected major sponsor that has capitulated. These requirements are mutually exclusive for the same selected target.

Source predicate review reduced the original ordinary military Evolution II combination from eight simultaneous rows to six. After `chaosx.nr11.8.a` maps routes without preparing a crossing, seven rows can still appear because reconnaissance remains useful for opening a new state-specific crossing while interception acts against the mapped route. On 2026-10-06, the parent accepted that contextual seven-action case because suppressing either operation would remove a meaningful choice; no further visibility gate or category was added. The revealed-war combination falls from seven to at most six. These are source-predicate findings, not MCP scenario evaluations, and the current decision-list render is unavailable.

## Other source repairs and prose

`chaosx.nr11.21.a` pays its displayed Command Power cost, then starts a National Manhunt only when a mission slot is free. Without a free slot, the containment response still resolves. The `.201` scenario composition notice is queued only when the safe eligible pool is strictly smaller than the requested roster; filling the roster exactly does not report an exhausted pool. The notice displays achieved member and major counts.

The super-event slot 73 retains the five route-specific descriptions. The forced-route text no longer attributes all player-forced reveals to a dossier, and the fractured text no longer invents an exact count of delayed delegations. The reveal helper has one world-news dispatch after a successful transaction. Six Event 011 achievements and all three Event Details evolution entries remain wired.

The shared feedback helper receives `no_target`, `no_country`, `already_active`, or `unavailable` for owner-side entry failures. Its receipt is set before reporting, so the dispatcher’s generic callback cannot produce a duplicate popup. The report/news colour audit was rerun after the final localization edits and returned `total keys with colour: 0`.

## Parent-authorized shared localization keys

The following six keys in `localisation/english/chaosx_gui_l_english.yml` were changed by the parent, not by this Event011 owner pass. Their surrounding file and other uncommitted content remain parent-owned.

| Key suffix | Before | Current |
| --- | --- | --- |
| `secret_alliance_target` | `no valid Secret Alliance target.` | `no eligible country can be selected.` |
| `secret_alliance_active` | `a Secret Alliance is already active.` | `a related operation is already under way.` |
| `secret_alliance_postwar` | `the postwar bloc is already active.` | `the current settlement is still active.` |
| `secret_alliance_launch` | `a Secret Alliance launch is already in progress.` | `an earlier response is still being prepared.` |
| `secret_alliance_callbacks` | `the Secret Alliance cannot yet establish a viable opening.` | `earlier events are still awaiting resolution.` |
| `secret_alliance_founders` | `no valid Secret Alliance founders are available.` | `too few suitable governments are available.` |

## Popup and asset evidence

The parent reviewed the 1890x910 Event011 QA sheet at `C:/Users/klimp/Videos/chaos_redux_trailer/records/qa/evt011_sheet.jpg` through a 1100px downscaled image and reviewed the 950x740 crop of `evt011_pop00.png`. The captured title, body, and buttons were clear, but the capture uses the old opening title and does not verify the revised title rendering. The five `evt011_pop00.png` through `evt011_pop04.png` images contain one Event011 popup, three unrelated vanilla reports, and one map view. The shared `docs/content_dump/teaser_screenshots.md:211` keeps the old title as a caption for the historical `307_secret_alliance_same_mistake_three_times.png` image, not as a current localization value. No desktop or game was opened during this task.

Runtime Event011 report, news, interface, decision, idea, achievement, warning-animation, super-event, and audio assets remain registered in their engine-facing files. The Event 011 overview records 57 runtime DDS targets, 38 transparent assets, six achievement triplets, eight warning-animation frames, and a static fallback as historical validator results. No current source-asset crosswalk was independently rebuilt. `docs/assets/011_secret_alliance/` and its source/processed PNG manifest are absent, so source provenance and derivation evidence remain incomplete. The parent checked `git log --all -- docs/assets/011_secret_alliance` and found no recoverable repository history for that workspace. No asset was created or changed in this repair.

Super-event source and audio research remain in `docs/super_events/011_secret_alliance/research.md`. The runtime reveal art is `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds`, the registered sprite is `GFX_super_event_011_secret_alliance_public_reveal`, and the reveal uses slot 73 with audio ID 43. The final WAV is documented as 86.101746 seconds at 44.1 kHz.

## References and MCP evidence

The byte-exact pre-repair decisions file is preserved under `docs/plans/011_secret_alliance_plans/probability_snapshots/before_2026-10-05/`. Its Git blob matches HEAD and its SHA-256 is `872CF65B501FBC684AB9BD9A929A5C5BDE71405AC291A36AD7853DBB8E99FC55`.

The last current decision-source lookup before the post-gate comparison attempt was complete at source-location revision `4829d290bbf4ae803820d2be80669b15deeb7baadae71f4cd3f92db408c4562a`, Git blob `087be84ba6b7ecb59ba612548d79dea9b5ce1768`, and raw SHA-256 `29F2218C5987F21FC8F18FC3D7498E3FE94E39EECD6AF816F755733EDB1FB59`.

The parent’s final caller-output initialization is in `common/scripted_effects/011_secret_alliance_effects.txt`, now Git blob `771756198171a376263972d657a3ff3b3dd30593` and raw SHA-256 `6B9FCAD39303391705CD3D3A85D7EBAB86149B3C5581D581B2126BA60B5B6C51`. The shared Event 026 helper documents the output as caller-owned at `common/scripted_effects/026_black_friday_price_table_effects.txt:27-33`, and the native-table caller initializes the same temp output at `:1404-1412`.

The latest successful probability comparison predates the final visibility gates. It used adapter `decision_ai_will_do`, the exact HEAD decision content inline as `before`, `common/decisions/011_secret_alliance_decisions.txt` as `after.path`, and scenario `E011_AI_TARGET_E2_HIGH_EVIDENCE_PREPAREDNESS` at 1938.1.1 with Active, Evolution II, and response-category flags, Evidence 100, and Preparedness 87. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-cf520b9df5de0c81ef39bd77`, scenario hash `f8b16118b1a4283f4d791140d1cd83693ddf58579154bfcd72ee391436a0c626`, 61 candidates, 2 eligible, 34 excluded, 25 unresolved, 415 unresolved items, and 45 diagnostics. It is score-only and does not model normalized selection probability. The tool’s later render marked that analysis stale and returned no visual resources.

The one post-gate comparison attempt used the same exact inline HEAD source, current decision path, adapter, and scenario. It remained pending after about 52 seconds and was terminated without status, source revision, analysis ID, scenario hash, or artifact. No retry followed. The comparison predates the parent’s later caller-output initialization as well. Static normalized source comparison reports unchanged 61 decision `ai_will_do` blocks, 18 event `ai_chance` blocks, and 12 `random_list` blocks. Probability certification remains blocked, including the changed candidate gates and quote flow.

An earlier path-based comparison attempt pointed `before.path` at the preserved snapshot under `docs/plans` and returned `PROBABILITY_SURFACE_EMPTY` with no adapter or candidates. That result reflects the documentation path not being indexed as a weighted decision surface, not a verified server outage; the subsequent inline-before comparison is the partial artifact described above.

The weighted audit also identified one unverified random-boundary candidate at `secret_alliance_resolve_weighted_counter_network_action`: `set_temp_variable_to_random` uses `min = 1` and `max = secret_alliance_outcome_total`, while installed effects documentation defines the range as `[min, max)`. The existing full, partial, and failure cutoffs appear to leave the last integer outcome outside the random range. The source audit did not calculate a campaign probability, and no weight or probability logic was changed.

Current `hoi4.event_inspect` and event-render paths returned no Event011 graph or reachability artifacts. The Event011 GUI worker’s current `hoi4.gui_inspect` and `hoi4.gui_render` requests remained pending beyond 60 seconds. Source review confirms the selected country name still feeds a fixed-size 136×18 text box, so long-name clipping remains a visual blocker. The user owns live-game validation.

In one initial bounded probe I mistakenly passed `refresh=true` to event roots, event reachability, decision inspect, and probability inspect despite the parent’s no-refresh instruction. All four produced no response within 50 seconds and no artifacts. I did not repeat refresh or broad-flow calls. The connected tool list exposed event, decision, GUI, probability, reference, source lookup, and script validation schemas, but no separate HOI4 health/status route.

The offline Localisation wiki sections `193-214`, `221-242`, and `656-683` have SHA-256 `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064`. They cover number colors, texticons, and `defined_text` selection. Installed `common/script_constants/documentation.md:1-8` has SHA-256 `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` and documents the `constant:` prefix. Offline Data structures line 440 (SHA-256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`) explains temporary-variable lifetime across helper calls. Installed `effects_documentation.md:7820-7840` (SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`) documents `set_temp_variable`. The installed set-temp-random section at `:7842-7855` and offline Effects wiki line 707 establish the half-open random range.

The current source check for the three cost-helper trigger bodies returned `SCRIPT_CHECK_PARTIAL`. The validator recognized `set_temp_variable`, `NOT`, `has_political_power`, `command_power`, and `has_war_support` in country scope but left the three native `set_temp_variable` argument blocks unchecked. This does not certify equality boundaries or runtime debit behavior.

## Remaining blockers and queued work

1. Current Event011 event-graph, decision-scenario, and GUI visual artifacts are unavailable. Source review is not engine validation.
2. The 136×18 selected-lead label and 94px suspect-card names need current-source long-text GUI renders. The previous source handoff at `event011_gui_text_fit_2026-10-05.md` records the exact window and failure calls.
3. The post-gate probability comparison did not return. Probability and AI selection certification remain incomplete.
4. Accepted participant limit: the hostile-war exception preserves valid nonleader faction followers already fighting the target. Existing faction leaders remain outside the valid-member/reveal-leader roster because the current transaction does not transfer an existing faction leader. A safe leader-transfer or coexisting-faction anchor route is a future proposal, not a required participant class in this release.
5. The permanent Event011 source-asset workspace and provenance manifest are missing. Historical runtime counts are not a current row-level source-to-consumer audit.
6. Spreadsheet catalog wording remains accepted and queued in `catalog_changes_pending.md` because XLSX and CSV edits are out of scope.

The accepted faction-leader participant limit and the mapped-border density exception are explicit scope dispositions, not hidden simplifications. No unapproved fallback was introduced. No files were staged or committed.
