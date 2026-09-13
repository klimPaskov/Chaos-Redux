# Repression ledger GUI interaction and selected-site cost audit

## Scope and disposition

This is a bounded, read-only audit of repression_ledger_window, its existing category launcher, and the selected-site cost path.

The source hash observed at this audit is 3C320877508906C9F380D5D471BE4DDD003C0F061C5C4A24EDF990B8D900C45C for interface/camp_repression_ledger.gui.

The parent applied the user-authorized compact layout directly after the earlier writer transaction rolled back, and the current selected-site cost implementation is present in its quote helpers and localisation; I did not edit runtime source, localisation, skills, or any unrelated document.

Disposition: the source patch, quote helpers, and parent-owned current native evidence are implemented. The three source findings in this report concerning biological activation, evidence branching, and expansion affordability are resolved. The bounded L1/L3/L5/L6 source arithmetic review finds the accepted slopes conservative for the fixed mission outcomes. Parent follow-up restored the six fixed AI political-power hints after MCP baseline inspection; the specialist's same-scenario decision and mission comparisons found zero score changes and no unresolved inputs. No GUI source blocker remains. This subagent did not rerender.

The earlier REWRITE_SOURCE_STALE and REWRITE_POST_VALIDATION_FAILED results are historical writer evidence, not a current completion gate; the post-write index failure named GFX_button_148x34 and GFX_closebutton.

## Evidence and verification boundary

The required offline Paradox wiki pages, vanilla documentation, the scripted GUI skill, the decisions and missions skill, and the relevant vanilla and Chaos Redux precedents were consulted before this review.

The revised compact reference is reference_compact.png in this directory, with the reviewed scalar proposal in reviewed_layout.patch.

The current source layout contract reported by the parent is a 396 by 460 selected card, selected name at (20,14) with a 356 by 52 bound, subtype at (20,68), live capacity and all-cause cumulative deaths at (20,98) with a 356 by 40 bound, six conditional 180 by 96 decorative backgrounds at x = 14/202 and y = 146/248/350, native buttons at x = 30/218 and y = 156/258/360, and centred cost bounds at x = 30/218 and y = 196/298/400 with 148 by 40 bounds.

The Situation strain surface is now 348 pixels wide with symmetric 24-pixel inner insets and 300-pixel paired columns in the current source description.

Earlier exact native renders were successful fixture renders with generatedScenarios.enabled = false, states = [normal], and a 1920 by 1080, uiScale 1 resolution, but they predate the current source hash and cannot prove the current layout or cost text.

The current parent-owned evidence is organized as follows: final_review contains the normal and matrix cases; final_long contains the highcost and long cases; final_situation contains the full native Situation pages; final_scroll contains the corrected bottom-scroll output; final_category contains the full native category output; and final_pages/policy_directives and final_pages/accountability contain the per-page outputs. The parent viewed these full-size renders and confirmed that visible buttons remain in the click-region evidence. This subagent did not independently rerender or certify every current PNG. The current validator output still includes tool-model limitations around scripted GUI visibility and unsupported or ignored click/scroll fields, so those diagnostics are not treated as a blanket visual pass.

All findings below distinguish source or fixture proof from executed-game behavior; live engine behavior and real mouse-wheel or scrollbar operation were not run by this subagent.

## Issues sorted by severity

1. Resolved in current source: biological activation intentionally does not create an immediate death receipt. camp_rework_apply_biological_escalation_in_action_state changes the ongoing site profile and registers the active site; the monthly loss pipeline records a receipt when actual ongoing losses occur. The player-facing tooltip describes ongoing civilian losses. A runtime or narrow engine trace remains useful to confirm the first monthly receipt and exactly-once behavior, but no immediate casualty should be invented from the action path.

2. Resolved in current source: the selected evidence action now branches on the shallow/deep evidence threshold, while its wrapper continues to require valid enemy proximity. The contradictory NOT is_valid_camp_enemy_proximity_state predicate was removed. The immediate evidence-destruction burst and the existing success/failure effects remain; the current tooltip and native output should still be checked against the threshold wording.

3. Resolved by parent follow-up: the six custom-cost actions have fixed ai_hint_pp_cost metadata at the former nominal values of 30 PP for each labor action, 60 PP for restricted methods, 25 PP for evidence, 45 PP for inspection, and 60 PP for dismantlement. Actual payment still uses the selected-state quote. The specialist's decision and mission comparisons cover the same four L1/L5 adequate-funds and shortfall scenarios and found no score changes; see site_cost_ai_audit.md and ai_hint_evidence for the explicit eligibility overrides and PP-saving simulation limit.

4. Resolved in current source and separate from selected-site quotes: the active countrywide expansion GUI gate and GetCampExpandBlockedSummary now check political power, manpower, support equipment, and trains, matching camp_rework_expand_labor_in_action_state. Command power and infantry equipment remain only on the activation guard where the wrapper and visible requirements use them. No hidden active-expansion resource gate remains in the reviewed source.

5. Resolved for this bounded balance review: multi-level quotes grow while the generic labor result is fixed, and the supplied L1/L3/L5/L6 arithmetic shows the accepted slopes remain conservative. L5 is the standard upper bound for the shared concentration/extermination camp family, while L6 is retained as a conservative cross-family presence case; combinations above that, such as Gulag level 4 or L10, are synthetic stress cases and are not presented as normal sites. The generic labor mission remains 150 days with a fixed start benefit of +3 labor output, a success benefit of +7 labor output plus one infrastructure level or a 365-day forced-labor modifier, and a fixed 0.35 percent death burst capped at 220. The quotes do not use deaths as a price input.

6. Low, parent-owned evidence: the compact source addresses the earlier baseline cost-box overflow, panel compression, and asymmetric insets. The parent viewed the current Situation, category, long-name, and bottom-scroll native outputs in the corrected evidence folders and confirmed visible buttons in the click-region evidence. This subagent did not rerender; validator-only unsupported-field diagnostics remain separate from the visual review.

## Cost and effect audit

The quote helper is in common/scripted_triggers/camp_repression_site_cost_triggers.txt:5-153, payments are in common/scripted_effects/camp_repression_site_cost_effects.txt:5-97, and the level constants are in common/script_constants/camp_repression_site_cost_constants.txt.

L is the selected state's combined concentration, extermination, and Gulag building level total with a minimum of one, so territory population is not being misused as detainee capacity.

The source-evaluated arithmetic in site_cost_arithmetic_scenarios.json covers the required size bands. L1 is labor 12 PP, 8 motorized, 1 train, and 12 support with reserves of 2 motorized, 1 train, and 3 support; L3 is 16 PP, 24 motorized, 3 trains, and 36 support with reserves of 6, 1, and 9; L5 is 20 PP, 40 motorized, 5 trains, and 60 support with reserves of 10, 2, and 15; and L6 is 22 PP, 48 motorized, 6 trains, and 72 support with reserves of 12, 2, and 18. Every supplied case reports exact affordability, one-unit-short rejection, debit equal to quote, and reserve save and clear in the small source evaluator; this is source or fixture proof, not a HOI4 engine run.

The building definitions bound concentration and extermination at level 5 within their shared chaosx_camp_network family and keep the Gulag network at a separate level 1 cap. Accordingly, L5 is the normal single-family ceiling used for this review, while L6 is a conservative cross-family presence case for cost headroom. Higher combinations such as Gulag level 4 or L10 are synthetic stress inputs and should not drive ordinary balance targets.

Against the fixed 150-day labor lifecycle, the L1 quote is a reasonable low entry price because the order still consumes a free project factory, requires the retained reserve, adds +2 overstretch and +2 resistance, and pays for logistics before the fixed +3 start and +7 completion labor-output benefits. At L3, L5, and L6 the same reward is purchased with 24/40/48 motorized, 3/5/6 trains, and 36/60/72 support plus the corresponding reserve, so the linear slope makes larger sites progressively less attractive without changing the outcome or charging by deaths. No further discount is supported by this audit.

Inspection scales from 13 PP at L1 to 19, 25, and 28 PP at L3, L5, and L6 for a 180-day administrative action that freezes expansion while granting reform, visibility, and observer exposure. Dismantlement scales from 18 PP, 350 manpower, and 5 support at L1 to 24/550/15, 30/750/25, and 33/850/30 for the 365-day permanent closure and cleanup. Evidence scales from 12 PP, 150 manpower, 3 command power, and 3 support at L1 to 16/250/5/9, 20/350/7/15, and 22/400/8/18, while retaining the immediate capped evidence-destruction burst and threshold-controlled outcome. These are four spendable types at most, and none uses casualties to determine price.

The bounded conclusion is to retain the current coefficients through the normal L5 band and the conservative L6 cross-family check. The lower L1 prices address the former flat logistical burden, while the fixed labor benefit and escalating equipment, manpower, and command-power requirements prevent larger sites from becoming a free repeatable action. Runtime throughput and player-economy context remain user-owned validation, but the source arithmetic shows no paid-outcome mismatch or cost coefficient that requires another change here.

| Selected action | Level-one quote | Actual lifecycle and outcome | Verdict |
| --- | --- | --- | --- |
| Labor Works | 12 PP, 8 motorized, 1 train, 12 support paid on order; retain 2 motorized, 1 train, and 3 support in stock | The selected wrapper pays once, enters the payload-only labor start, and activates generic_labor_project_cycle for 150 days; start gives +3 labor output, +2 overstretch, and +2 resistance, while completion gives the fixed success result or the fixed failure result | Reasonable and far below the former flat 120 truck, 18 train, and 180 support burden at L1; the L3/L5/L6 matrix shows the fixed reward is not being handed out cheaply at larger sites |
| Inspect | 13 PP | Pays once, applies the 180-day inspection flag and burden, freezes expansion, and grants reform, visibility, and observer exposure; no immediate death pulse | Reasonable for an administrative action with a clear 180-day opportunity cost |
| Dismantle | 18 PP, 350 manpower, 5 support | Pays once, starts the 365-day selected dismantlement mission, and on completion removes camp buildings and modifiers, carries evidence, unregisters the inactive site, clears ownership markers, and credits reform | Conservative for a permanent closure; no reason to inflate it to match a death toll |
| Destroy Records | 12 PP, 150 manpower, 3 command power, 3 support | Pays once, applies the 1.25 percent evidence-destruction burst capped at 150, then enters the threshold-controlled success or failure evidence branch | Four spendable types are acceptable; enemy proximity remains the wrapper requirement and shallow/deep evidence remains the branch threshold |
| Chemical or Biological Order | 23 PP plus the existing tier payload | Pays the administrative quote once; chemical uses the shared CBRN civilian-death receipt, while biological registers the active site and its monthly tier multiplier and deliberately leaves immediate casualty receipt to the ongoing-loss pipeline | PP is a reasonable administrative fee because the payload remains the principal material cost; confirm the first monthly biological receipt in runtime or a narrow engine trace |

The quote slopes are labor PP 10 + 2L, motorized 8L, trains L, support 12L, inspection PP 10 + 3L, dismantlement PP 15 + 3L, manpower 250 + 100L, support 5L, evidence PP 10 + 2L, manpower 100 + 50L, command power 2 + L, support 3L, and restricted PP 20 + 3L.

The selected labor affordability predicate uses inclusive greater_than_or_equals checks for political power, the paid equipment, and the retained reserve, and the payment effect subtracts exactly the paid quote once; a level-one order therefore requires at least 10 motorized, 2 trains, and 15 support before payment and leaves the 2, 1, and 3 reserve units in stock.

The generic labor completion and cancellation trigger checks the same retained reserve with inclusive equality, and cleanup clears only the reserve variables after completion or cancellation; the selected route calls the payload-only start and does not call the legacy flat camp_rework_consume_labor_project_resources helper.

The generic dispatcher pays once at common/scripted_effects/camp_repression_action_dispatcher_effects.txt:135-165 before activating the labor mission and at :184-248 before inspection, evidence, or dismantlement; the scripted GUI route calls the matching wrapper once at common/scripted_effects/camp_repression_rework_effects.txt:3899-4113.

The decision cost rows use the new decision-scoped quote getters in localisation/english/camp_repression_site_cost_l_english.yml, and each spendable value uses the matching political power, manpower, command power, motorized, train, support, or restricted-payload texticon.

The countrywide guard action remains four flat spendable types, quota relief remains one political-power cost, and activation or expansion remain separate countrywide packages; these values were not folded into selected-state quotes.

## Interaction preservation and GUI review

The scripted GUI click map retains camp_gui_*_click actions for the existing action ids at common/scripted_guis/camp_repression_ledger_scripted_gui.txt:131-139, and camp_rework_route_country_specific_action still dispatches each id to its existing wrapper.

The pool and site dynamic lists retain camp_ui_pool_list and camp_ui_site_list, their array bindings, change-scope behavior, row buttons, selected markers, and row text bindings.

The six selected-site buttons retain their button text, tooltip keys, availability predicates, effects, sounds, and click regions; the compact geometry moves the button and adjacent cost bounds only.

The cost labels remain transparent presentation controls, and decorative backgrounds remain conditional so labels do not become additional click targets at source level.

The category launcher, close action, tab markers, panel visibility flags, selected-row variables, and empty-state branches remain unchanged in the reviewed source.

The source and reference support five navigation actions, up to six selected-site orders, six scroll rows in the 300 by 312 viewport, and the supplied bottom-scroll fixture selecting the final row; this is source or fixture proof, not executed mouse input.

The displayed selected-site values now have explicit significance: selected site name and subtype identify the target, capacity is live site capacity, the death line is all-cause cumulative state deaths, and the quote rows distinguish paid labor from the retained reserve in the labor tooltip.

## Decision lifecycle, mission, AI, and cleanup notes

The generic labor mission owner is the acting country and its region is the selected state; requirements are responsible control, an active valid site, the construction or extraction target condition, a free project factory, and the retained reserve, and duplicate starts are blocked by generic_labor_project_active.

The generic labor mission runs for standard_action_days = 150, completes on timeout, and cancels when control, site validity, project target, factory capacity, or retained reserve fails; success and failure both run the existing cleanup and death receipt paths.

The selected dismantlement mission owns the selected state through camp_gui_dismantlement_state_id, runs for 365 days, cancels on control or site-loss failure, and completes through the existing building, evidence, registration, custody, and ownership cleanup.

No scripted GUI AI weights changed, and both scripted GUI definitions remain player-only; no AI probability analysis was run for unchanged weights.

The action dispatcher records the existing cooldown after a routed action and clears transient action-state variables, while labor reserve variables clear at mission terminal paths; no new free-equipment, free-unit, war-goal, core, or cooldown loop was found in the selected payment path.

## Required final checks and remaining uncertainty

The parent reports that exact matching situation_warning, policy_directives, and accountability scenarios from scenarios.json were rendered with generatedScenarios.enabled = false, states = [normal], and 1920 by 1080 uiScale 1, with full-size PNG, cropped PNG, layout, validation, and provenance copied under final_review and final_long. This subagent did not rerender.

Those parent-owned renders are the evidence to inspect for centred navigation, symmetric Situation columns, 396 by 460 card bounds, no overlap or clipping in the 148 by 40 cost boxes, preserved row reachability, and click regions that exclude decorative cost labels; retain any actual visible warning rather than declaring a blanket pass from validator output.

The source-evaluated L1/L3/L5/L6 matrix matches the same camp_rework_prepare_site_cost_quote values used by the affordability trigger and payment effect, including exact stock equality and reserve save and clear. The parent-owned native evidence should retain that quote presentation and the countrywide expansion row matching its active payment gate; no additional coefficient change is indicated by this audit.

The biological action has no immediate death receipt by design; a focused runtime or narrow engine trace may confirm that the first monthly receipt records actual ongoing losses exactly once, but the selected-site cost audit cannot establish runtime timing from source alone.

The evidence action’s source branch is coherent after the predicate removal; parent review should retain the native tooltip wording for enemy proximity and the shallow/deep evidence threshold, with no further source change indicated by this audit.

The six custom-cost actions' saving hints and specialist comparison are complete in the parent follow-up. This decision auditor did not itself run that weighted analysis; the separate specialist owns the comparison evidence.

Live engine throughput, economy context, and monthly biological timing remain user-owned validation boundaries. The arithmetic artifact is not a substitute for an executed game, and no gameplay balance claim beyond the bounded quote comparison is made here.

No gameplay weights, probabilities, countrywide costs, restricted payload inventory, or unrelated GUI surfaces were changed by this subagent, and no commit was created.
