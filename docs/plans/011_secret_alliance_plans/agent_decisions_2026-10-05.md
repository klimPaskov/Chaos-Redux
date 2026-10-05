# Event 011 Release Repair Decisions — 2026-10-05

Status: source repairs implemented; release incomplete pending current event and GUI evidence, weighted-logic certification, and asset provenance.

Acceptance basis: the parent’s explicit Event 011 release direction for this task authorizes the source repair, the four-cost ceiling, the three-value inline cost limit, and owner-side forced-failure feedback through the shared reporting hook.

The accepted Event 011 specifications and decision/mission matrix remain the design source; this record documents implementation choices within that accepted scope and does not promote new mechanics into the source specifications.

## Cost bundle repairs

The shared country-scale cost values, evidence scaling, Black Friday quote refresh, AI weights, and consequence amounts remain unchanged.

Every action below now consumes no more than four distinct resource types, and each custom inline cost row displays no more than three amounts while its native hover text lists the full bundle.

| Decision | Before | Current bundle | Reason |
| --- | --- | --- | --- |
| Protect Ports and Airfields | Command Power, Army Experience, support equipment, fuel, convoys | Command Power, Army Experience, support equipment, fuel | The access-point project retains its operational fuel cost without also charging a separate shipping reserve. |
| Run a Controlled Shipment | Command Power, Army Experience, support equipment, trains, trucks | Command Power, Army Experience, support equipment, trucks | The shipment uses road transport and no longer pays the general train charge. |
| Sabotage a Forward Depot | Command Power, Army Experience, support equipment, trains, fuel | Command Power, Army Experience, support equipment, fuel | The depot operation retains its fuel use without a second transport charge. |
| Seize a Courier Aircraft or Vessel | Command Power, Army Experience, support equipment, trains, fuel, convoys | Command Power, Army Experience, support equipment, fuel | The shared interception action uses fuel across either target type and does not add separate rail and convoy payments. |
| Begin a Limited Border Conflict | Command Power, Army Experience, support equipment, trains, manpower | Command Power, Army Experience, support equipment, manpower | Railway supply and divisions in both named states remain requirements; the action no longer bills trains in addition to manpower. |
| Emergency Mobilization | Command Power, support equipment, manpower, fuel, Stability | Command Power, support equipment, manpower, Stability | Domestic mobilization retains the manpower and readiness burden without adding a fifth fuel fee. |
| Fortify Exposed Approaches | Command Power, support equipment, manpower, fuel, Stability, trains | Command Power, support equipment, Stability, trains | The action pays for command, field equipment, political strain, and rail movement without also charging manpower and fuel. |
| Recall Overseas Assets | Command Power, support equipment, manpower, fuel, Stability, convoys | Command Power, support equipment, Stability, convoys | The action pays for command, field equipment, political strain, and sea transport without also charging manpower and fuel. |
| Preempt the Coalition | Command Power, support equipment, manpower, fuel, Stability, War Support | Command Power, support equipment, Stability, War Support | Preemption retains its separate Evidence-scaled War Support cost and Stability strain without manpower and fuel charges. |
| Seek a Defensive Alliance | Command Power, support equipment, manpower, fuel, Stability | Command Power, support equipment, manpower, Stability | The diplomatic emergency retains its command, personnel, equipment, and Stability burden without a fifth fuel fee. |
| Evacuate Critical Leadership | Command Power, support equipment, manpower, fuel, Stability, trains | Command Power, support equipment, Stability, trains | The evacuation retains its command, field equipment, Stability, and rail movement costs without separate manpower and fuel charges. |

The source inventory contains six overbudget crisis decisions rather than five: the base emergency bundle is reused by both Emergency Mobilization and Seek a Defensive Alliance, while Preempt the Coalition adds its separate Evidence-scaled War Support payment.

The full decision list has no native `cost =` value on these actions; each uses `custom_cost_text`, a matching affordability trigger, and one manually debited payment path.

The previous Stability affordability paths did not all test the exact quoted fee; investigation, intermediary, public-dossier, and emergency actions now compare current Stability against the same cached quote used by their display and debit, while existing minimum-Stability requirements remain separate gates.

Preempt the Coalition retains its conditional false-case Stability penalty and now states that risk in the effect tooltip; it remains the same Stability cost type, not an additional fifth resource.

The limited-border-conflict decision now uses the same no-trains cost gate as its payment, while rail supply and the presence of divisions remain exact-state requirements.

## Cost-row color state

The 31 Event011 cost localization families now use 20 resource-specific scripted getters for their ready and deficient amounts. Their 40 English result keys retain the existing texticons and amount precision, while each resource number is green only when its matching inclusive affordability trigger passes and red when it does not. All `_blocked` keys alias the same resource-coloured base row, so an unrelated route or capacity requirement no longer paints affordable costs red. Hover rows use the same getters for any fourth spendable cost.

The shared political-power, diplomacy command-power, border-escalation War Support, and additional dossier political-power checks are named scripted triggers. The applicable availability and custom-cost blocks call the same checks, and the separate 40% Stability floor remains an eligibility requirement rather than a Stability fee.

The applicable diplomatic requirement tooltips now state that separate floor using `secret_alliance_decision_gate.diplomacy_stability` directly. Their displayed Stability cost remains a separate payment, so the requirement text no longer obscures the difference between a minimum reserve and the amount spent.

The decision inventory still contains 54 custom-cost decision instances across the 31 localization families. The source audit expands nested cost macros and confirms no inline row exceeds three amounts, no hover bundle exceeds four, and each family has base, `_blocked`, and `_tooltip` keys. No cost amount, spendable resource type, scale, sale ratio, or numeric AI weight changed in this display repair.

## AI cost-gate alignment

`secret_alliance_run_available_ai_protection` no longer requires Convoys before applying the ports-and-airfields action. The player decision and its payment use Command Power, Army Experience, Support Equipment, and Fuel; the obsolete Convoy check did not match either surface. Its parent AI response gate still checks the shared protection costs, and its branch checks the Fuel add-on that the effect pays.

## Decision-list relevance gates

The source audit found eight Evolution II rows visible together and seven revealed-war rows visible together in the named predicates. The parent directed phase and irrelevance gates that keep all meaningful actions reachable.

`secret_alliance_compartmentalize_staff_plans` now appears after an intelligence operation, matching the accepted Part 3 decision matrix’s “Intelligence clue” requirement. `secret_alliance_intercept_survey_team` now appears after `secret_alliance_conduct_border_reconnaissance_raid` maps the route, matching the accepted matrix’s requirement to launch the interception against mapped routes. Both decisions remain available in their intended stages.

`secret_alliance_offer_separate_terms` is shown only for the selected active enemy member that has not capitulated. `secret_alliance_demand_sponsor_accountability` is shown only for an unused, capitulated major sponsor. Those target states are mutually exclusive, so the two revealed-war diplomacy choices no longer occupy rows together when one is irrelevant.

These visibility gates change candidate eligibility while leaving every `ai_will_do` numeric block unchanged. Source re-audit confirms that the ordinary military Evolution II case drops from eight visible rows to six, and the revealed-war case drops from seven to at most six. Following incident `.8.a`, the mapped-route state still presents seven meaningful choices because reconnaissance opens a new state-specific crossing while interception acts against mapped routes. The parent accepted that one contextual density exception on 2026-10-06 to preserve both distinct paid operations; the decision skill’s action budget guides readability and does not require deletion or extra categories solely to hit the number. The current GUI row rendering remains unverified.

The latest probability comparison attempt after these gates remained pending for about 52 seconds and returned no artifact. The preceding matched comparison was partial and unresolved; final post-gate weighted evidence remains blocked. No cost, payment, numeric weight, outcome, or action effect changed for this list repair.

## Accepted hostile-war faction-leader constraint

The hostile-war path captures the attacking pact member as `secret_alliance_war_anchor`, then refreshes members through `secret_alliance_is_valid_member`. The active-hostile-war exception preserves nonleader faction followers already fighting the target. Existing faction leaders remain outside the valid-member roster because reveal preparation moves followers and does not disband or transfer another faction's leader. The parent accepted this as the safe current participant boundary on 2026-10-06. This release does not claim to preserve a faction-leader anchor as a pact member. A separately designed safe leader transfer or coexisting-faction anchor remains a future proposal and is not a required live participant class.

## Forced-entry feedback

Event 011 routes owner-side prefire and entry failures through the existing `chaosx_report_forced_event_failure` helper with specific `no_target`, `no_country`, `already_active`, or `unavailable` reasons.

The shared helper sets `chaosx_manual_event_failure_shown` before displaying the one report, so the dispatcher’s later generic failure callback cannot produce a duplicate popup.

The temporary owner-specific `chaosx.nr11.204` event has been removed after its callback was replaced by the shared hook.

## Counter-network panel text

The Event011-owned panel keeps its accepted 500×250 layout and click geometry.

The phase heading drops its redundant `COUNTER-NETWORK:` prefix, the selected lead uses the country name without a grammatical suffix, and the footer uses compact operation and hidden-state labels inside its existing text boxes.

`GetSecretAllianceGuiStatus` retains its required recent-operation fallback outside the concealed-state conditions.

The fresh `hoi4.gui_inspect` and `hoi4.gui_render` routes did not return for the current text revision; the prior GUI handoff remains historical visual evidence and does not certify these shortened strings.

The opening report title `chaosx.nr11.3.t` now reads “Orders from Unknown Hands.” It names the forged orders and altered schedules described by the report rather than describing their repetition informally.

## Validation and remaining evidence

`python .tools/report_colour_audit.py --event 011` reported zero colour keys.

The `.201` delayed composition notice is queued only when `secret_alliance_scenario_safe_total_pool_snapshot` is strictly less than the requested roster; filling the available roster exactly does not claim that the safe pool was exhausted. Its text reports the achieved member and major counts (`common/scripted_effects/011_secret_alliance_effects.txt:8450-8458`; `localisation/english/011_secret_alliance_l_english.yml:113-115`).

The parent reviewed the Event011 QA sheet at `C:/Users/klimp/Videos/chaos_redux_trailer/records/qa/evt011_sheet.jpg` through its 1100px downscaled image and reviewed the 950×740 crop of `evt011_pop00.png`. The sheet and crop show the original opening title “The Same Mistake Three Times”; the title was changed afterward, so no screenshot verifies its revised rendering. The five popup images are `evt011_pop00.png` through `evt011_pop04.png`: pop00 is Event011, pop01–03 are unrelated vanilla reports, and pop04 is a map view. Existing 960×540 `_view.png` copies are historical source evidence only.

The source-level cost inventory found 31 cost localization families across 54 decision instances. Nested localization expansion confirms at most three inline amounts and four spendable types in each complete hover row.

The current entry feedback, cost gates, payment effects, and 71 decision name/description pairs have been reviewed from source; the localization audit found no banned visible implementation terms or update-history wording.

Current event-chain and GUI-render artifacts remain unavailable. The latest decision-weight comparison returned `PROBABILITY_ANALYZED_PARTIAL` for a decision source whose raw hash matched the file before the final visibility-gate patch; unresolved eligibility, an incomplete candidate fixture, and a stale render leave probability certification open. The visibility-gate patch has no post-change comparison.

## Reference and MCP evidence

Offline wiki references read: `Decision modding - Hearts of Iron 4 Wiki.md:284-336` (revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`) for custom cost row naming and manual debit; `Triggers - Hearts of Iron 4 Wiki.md:2320-2358` (revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`) for dynamically built `meta_trigger` text; and `Event modding - Hearts of Iron 4 Wiki.md:151-185` (revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`) for event-option and AI chance behavior.

The offline `Localisation - Hearts of Iron 4 Wiki.md:193-214, 221-242, 656-683` (SHA-256 `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064`) documents number colouring, texticons, and current-scope `defined_text` selection. The installed script-constant schema at `common/script_constants/documentation.md:1-8` (SHA-256 `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C`) confirms scoped constants use the `constant:` prefix. The installed vanilla example `common/scripted_localisation/WUW_GER_scripted_loc.txt` (SHA-256 `82233D7BB8362D933182C7DA345606089A67B92ADEDB764C37A942E1E2F67683`) and the existing Event007 component-colour implementation at `common/scripted_localisation/007_fury_cost_display.txt` (SHA-256 `C68A8F354A75A8F7BF138905FF9FAFB21EC25D1EED1C7933DFD9229AE7008B15`) are the `defined_text` and per-resource ready/blocked display precedents for Event011.

The Data structures target section was read locally at `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:303-328` (SHA-256 `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`) after `reference_read` returned `REFERENCE_REVISION_STALE` for the indexed section; `hoi4.reference_search` identified regular targets and `has_event_target` separately.

Installed-game documentation read: `common/decisions/_documentation.md:1-48` (SHA-256/revision `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`) for decision scope and availability; `documentation/triggers_documentation.md:6404-6423` (revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`) for supported `meta_trigger` scopes; `documentation/dynamic_variables_documentation.md:435-438` (revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`) for `has_stability` units; and `documentation/effects_documentation.md:2173-2181`, `7820-7827`, and `5012-5018` (revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`) for `add_stability`, `set_temp_variable`, and `multiply_temp_variable`.

Vanilla precedent: `hoi4.source_lookup` located `game:common/decisions/AFG.txt:458-543`, owner `AFG_cross_border_target_state`, at revision `06b629264c53467c4de7cbfb7e661e5b9827be3eac9e9c074a0a0171470bc441`. The inspected Afghanistan decision pairs a custom cost trigger and text key with a hidden manual `add_command_power` debit.

Latest decision-source lookup before the final comparison attempt returned `complete=true`, revision `4829d290bbf4ae803820d2be80669b15deeb7baadae71f4cd3f92db408c4562a`, current Git blob `087be84ba6b7ecb59ba612548d79dea9b5ce1768`, and raw SHA-256 `29F2218C5987F21FC8F18FC3D7498E3FE94E39EECD6AF816F755733EDB1FB59`. The latest post-gate probability compare remained pending and returned no result.

The required `script_validate` requests returned `SCRIPT_CHECK_PARTIAL`: native command kinds and country scope were recognized for the new political-power, diplomacy command-power, and War Support affordability bodies, while three `set_temp_variable` argument blocks remained unchecked. Earlier checks also left native argument blocks and owner-defined payment helpers unresolved. This is syntax coverage only and does not verify equality boundaries or engine payment behavior.

Current event-chain structure and GUI visual evidence remain blocked: the narrow event roots/reachability probes produced no response within 50 seconds; the Event011 source auditor’s structural inspect/render produced no artifacts; and the current `secret_alliance_counter_network_container` `hoi4.gui_inspect`/`hoi4.gui_render` requests remained pending past 60 seconds. The decision inspector’s earlier inventory timed out after 600 seconds, and a no-scenario request returned the schema error that declared scenarios are required.

In one initial bounded probe I mistakenly passed `refresh=true` to the event roots, event reachability, decision inspect, and probability inspect calls despite the parent’s no-refresh instruction. All four produced no response within 50 seconds and returned no artifacts; I did not repeat refresh or broad-flow calls. The connected tool list exposed the event, decision, probability, GUI, reference, source lookup, and script-validation schemas but no separate HOI4 health/status route.

The latest decision-weight comparison returned `PROBABILITY_ANALYZED_PARTIAL` for the pre-final-visibility-gate decision source. Its raw decision-source SHA-256 matched the file at that time, but it reported 415 unresolved items and 45 diagnostics, was score-only, and a later render marked the analysis stale with zero visual resources. The final four visibility gates were applied afterward and have no matching comparison artifact. The full weighted certification remains blocked. The exact comparison details, candidate coverage, all other weighted surfaces, and the half-open random-range finding are preserved in the final release handoff.

## Caller-owned dynamic price result

The dynamic cost refresh consumes `black_friday_price_payable` after `black_friday_price_table_quote` returns.
It initializes that temporary result in the consuming refresh effect before invoking the quote helper.
This guarantees the existing cached fees survive the helper return, as required by the shared quote contract and the offline Data structures wiki at line 440 (SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`).
The installed `set_temp_variable` effect documentation and the existing shared quote implementation supply the native syntax and precedent.
No ordinary amount, sale ratio, resource type, AI numeric weight or outcome is changed.
This is an owner-applied lifetime correction, not an observed free-fee runtime claim.
The prior probability artifacts do not prove this corrected quote flow; exact-price live fixtures remain required.
