# Condemnation cost scaling and cost row closure

Disposition: implemented in the current shared source for the approved 2026-09-20 Condemnation cost and presentation tranche. No commit was made because the parent owns the shared worktree.

Acceptance basis: the user's 2026-09-20 cost requirements and `docs/specs/condemnation_system_specs/specs/condemnation_impact_system_spec.md`. The accepted design requires a 0–1000 score, a multiplier of `1 + score / 500`, whole equipment amounts rounded up, a score-linked 5–15% inspection burden for 180 days, unchanged disclosure rates, exact displayed and debited payments, and separate target and participant ownership paths.

## Changed source and identifiers

The cost helpers are in `common/scripted_triggers/condemnation_sanctions_triggers.txt`. `condemnation_prepare_cost_multiplier` clamps the selected score to 0 through 1000 and produces the shared fixed-point multiplier. `condemnation_prepare_scaled_integer_cost` rounds positive equipment, convoy, and experience payments up to the next whole unit when necessary. `condemnation_prepare_scaled_fraction_cost` preserves fuel precision. `condemnation_prepare_inspection_consumer_goods` produces the score-linked inspection increment.

`common/scripted_effects/condemnation_response_effects.txt` now copies the score-linked inspection increment into the normal variable used by `condemnation_inspection_score_burden`, refreshes that modifier through the existing inspection pulse, and clears the variable when inspections end. Response payment effects use the same integer and fraction helpers as their visible rows. Refusing inspections removes the dynamic modifier, the base idea, and the stored increment.

`common/scripted_effects/condemnation_sanctions_effects.txt` now subtracts the displayed fixed-point fuel share directly in `condemnation_pay_fuel_fraction`. The previous helper multiplied the displayed share by current fuel ratio, which made the debit smaller than the row whenever the country was below full fuel. Participant enforcement, escalation, carve-out, breach, tightening, and shield effects retain their selected target score before calculating their payment.

`common/script_constants/condemnation_sanctions_constants.txt` owns the score clamp, multiplier divisor, integer step, inspection minimum, midpoint, per-score increment, and maximum. The dynamic modifier in `common/dynamic_modifiers/condemnation_sanctions_dynamic_modifiers.txt` adds the score-linked increment on top of the existing 5% inspection idea.

`common/scripted_localisation/condemnation_response_costs.txt` and `localisation/english/condemnation_response_costs_l_english.yml` provide 18 icon-first cost rows. `localisation/english/condemnation_sanctions_l_english.yml` removes player-facing payment prose from effect tooltips, describes recovery through current conduct, and explains the 5–15% inspection range. `docs/systems/cbrn_warfare/condemnation/condemnation_sanctions.md` documents the formula, matrix, ownership, and boundary behavior.

The compensation decision now keeps the living-victim requirement in its requirement tooltip while invoking the shared affordability predicate separately. Command reform likewise uses the shared affordability predicate directly. Neither requirement tooltip repeats spendable resource names or amounts already shown by the cost row.

Skills applied: `chaos-redux-decisions-missions` for shared affordability, one-debit, icon-row, and cognitive-load rules, and `chaos-redux-scripted-gui` for the mandatory native decision-window inspect/render evidence. No skill file was changed; the existing guidance already covers this workflow.

## Exact score and rounding evidence

The shared formula is `m = 1 + clamp(score, 0, 1000) / 500`. Integer amounts use `ceil(base amount x m)` and the fuel amount is a fixed-point share of capacity that is subtracted from `fuel_ratio` by the same value shown in the row.

| Input score | Clamped score | Multiplier | Compensation row | Inspection burden |
| --- | ---: | ---: | --- | ---: |
| Below range: `-1` | `0` | `1x` | `20` convoys, `500` infantry equipment, `12%` fuel | `+5%` Consumer Goods |
| Exact lower boundary: `0` | `0` | `1x` | `20` convoys, `500` infantry equipment, `12%` fuel | `+5%` Consumer Goods |
| Exact midpoint: `500` | `500` | `2x` | `40` convoys, `1000` infantry equipment, `24%` fuel | `+10%` Consumer Goods |
| Exact upper boundary: `1000` | `1000` | `3x` | `60` convoys, `1500` infantry equipment, `36%` fuel | `+15%` Consumer Goods |
| Above range: `1001` | `1000` | `3x` | `60` convoys, `1500` infantry equipment, `36%` fuel | `+15%` Consumer Goods |

The adjacent rounding checks also hold: score `499` yields `ceil(20 x 1.998) = 40` convoys and `ceil(500 x 1.998) = 999` equipment; score `501` yields `ceil(20 x 2.002) = 41` convoys and `ceil(500 x 2.002) = 1001` equipment. Exact multiples at 0, 500, and 1000 remain unchanged by the ceiling step.

## Ownership and boundary behavior

Target response decisions calculate their quote in the acting country scope, so the target country pays against its own `condemnation_total`. The compensation, inspections, stockpile, site, observer, command, defiance, and evasion effects remain target-country effects.

Participant decisions run with the acting participant as `ROOT` and the selected condemned country as `FROM`. `condemnation_set_target_cost_score` sets the target score before both `available` and `custom_cost_trigger`. Participant scripted localisation reads the same `FROM.condemnation_total`, and the completed participant effects recalculate the selected target score before debiting the participant. The participant is therefore the payer and the selected target owns the score used for the quote.

Below-range scores clamp to zero, exact 0 uses 1x, exact 500 uses 2x, exact 1000 uses 3x, and above-range scores clamp to 1000. If a selected target has no score variable, the participant quote falls back to zero and 1x. A future native raid country-event bridge must preserve this actor-country and selected-target ownership path; this handoff deliberately does not add a condemnation-specific raid special case while the raid owners repair the native scope bridge.

## Complete concealment and response matrix

The matrix was checked against the current decisions, response effects, and localization. Existing consequences remain attached to each action.

| Action | Owner and payment | Existing outcome retained |
| --- | --- | --- |
| Accept international inspections | Target; no payment | 180-day inspection idea, dynamic `+5%` to `+15%` Consumer Goods, `-15%` Encryption, and `10%` hidden-evidence disclosure per targeted pulse. |
| Destroy chemical stockpiles | Target; no payment | Removes 75% of every supported chemical agent and legacy cylinder stock, sets the chemical stockpile restriction for 365 days, and advances the compliance state. |
| Destroy biological stockpiles | Target; no payment | Removes 75% of anthrax, plague, tularemia, smallpox, and weaponized-zombie bomb stock, sets the biological stockpile restriction for 365 days, and advances the compliance state. |
| Dismantle restricted sites | Target; no payment | Clears supported restricted-site flags, records destroyed and dismantled site history, and advances the compliance state. |
| Pay victim compensation | Target; scaled convoys, infantry equipment, and fuel | Pays the last valid victim, records the compensation opinion, applies the 180-day settlement burden, and advances the compliance state. |
| Issue non-use pledge | Target; no payment | Starts the 365-day pledge, applies its war-support effect, schedules verification, and retains pledge-break handling. |
| Allow foreign observers | Target; scaled convoys | Starts the 180-day observer idea, applies the detection penalty, and discloses 5% of hidden evidence per targeted pulse. |
| Reform unconventional command | Target; scaled army, air, and navy experience | Records permanent reform, applies the 270-day transition burden, and advances the compliance state. |
| Refuse inspections | Target; no payment | Cancels inspections and observers, blocks decay for 180 days, and adds the public blocked-inspection coverup source. |
| Domestic propaganda campaign | Target; no payment | Applies its stability, war-support, and Consumer Goods effects for 180 days and marks defiance. |
| Emergency autarky | Target; scaled fuel | Directly debits the shown fuel share and retains local-resource, Consumer Goods, factory-output, and relief effects for 180 days. |
| Forced extraction | Target; no payment | Retains the immediate stability loss and the 180-day resource and production-efficiency effects. |
| Substitute materials | Target; no payment | Retains the 180-day resource and production-efficiency effects. |
| Military rationing | Target; no payment | Retains the 180-day fuel-use and factory-output effects. |
| Pressure subject supply | Target; no payment | Requires a subject and retains the immediate stability, local-resource, and pressure effects for 180 days. |
| Controlled shipping | Target; scaled convoys and fuel | Directly debits both displayed payments and retains the 180-day convoy-efficiency and factory-output effects. |
| Hardline mobilization | Target; no payment | Retains the 180-day war-support and stability effects without reducing material pressure. |
| Black-market arms | Target; scaled convoys and fuel | Directly debits the shown payments, grants the existing infantry and support equipment, and retains the 120-day route, pressure, burden, and exposure effects. |
| False manifests | Target; scaled convoys | Retains the 120-day route, escort-efficiency, pressure, and exposure effects. |
| Neutral intermediaries | Target; scaled convoys | Retains the 120-day route, infantry-equipment gain, license-cost, pressure, and exposure effects. |
| Subject front | Target; no payment | Retains the subject requirement, stability loss, 120-day route, local-resource gain, pressure, and exposure effects. |
| Covert fuel route | Target; scaled convoys | Retains the 120-day route, fuel gain, military-fuel-use effect, pressure, and exposure effects. The fuel gain remains separate from the payment debit. |
| Reflag merchant shipping | Target; scaled convoys | Retains the 120-day escort-efficiency, pressure, and exposure effects. |
| Stolen production license | Target; scaled convoys | Retains the 120-day production-efficiency, pressure, and exposure effects. |
| Smuggled laboratory | Target; scaled convoys and support equipment | Retains the 120-day research, pressure, and exposure effects. |
| Join arms embargo | Participant; scaled convoys and fuel from the selected target's score | Creates the arms sanction pair and retains native-embargo registration, relation restrictions, recall, burden, and AI-strategy integration. |
| Escalate strategic, total, or pariah embargo | Participant; scaled convoys and fuel from the selected target's score | Replaces the pair tier and retains native claim ownership, burden replacement, fatigue, relation restrictions, and cleanup. |
| Abstain | Participant; no payment | Retains the review record, victim and participant opinion consequences, and AI abstention path. |
| Humanitarian carve-out | Participant; scaled convoys from the selected target's score | Retains relief, expiry, pair bookkeeping, and participant burden refresh. |
| Quiet breach | Participant; scaled convoys, infantry equipment, and fuel from the selected target's score | Retains target and participant pressure, exposure, 120-day duration, discovery, coverup condemnation, and diplomatic damage. |
| Tighten enforcement | Participant; scaled convoys from the selected target's score | Retains quiet-breach removal, enforcement burden, counter-relief, expiry, and burden refresh. |
| Shield ally | Participant; scaled convoys from the selected target's score | Retains shield relief, opinion support, fatigue, expiry, and cleanup. |
| Withdraw sanctions | Participant; no payment | Retains bilateral cleanup, burden removal, relation-rule cleanup, and preservation of independently owned embargoes. |

Every paid action has at most three spendable types. The largest rows are compensation, command reform, and quiet breach, each with three icon slots. No visible cost row spells out a resource name; the 18 rows in `condemnation_response_costs_l_english.yml` use convoy, infantry equipment, support equipment, fuel, and service-experience text icons.

## Lifecycle and cognitive-load audit

The target category has one posture selector and three curated views. Human players see one of compliance, defiance, or evasion at a time; AI keeps the existing direct evaluation path. The current compliance view can expose eight primary response decisions, the defiance view can expose nine, and the evasion view can expose eight. The participant category contains ten decision types. This exceeds the decisions-and-missions skill's six-action density guideline and remains a P2 design issue for a later phase or subcategory split; it is outside this approved cost-row patch and was not silently redesigned.

Visible player values now have direct significance. The score is a bounded public pressure measure that drives the quote and the inspection burden. The tier gates actions. The cost row is the only upfront payment display, and the effect tooltip explains the action outcome and duration. The response panel says `Recovery` and explains which conduct helps condemnation ease; it contains no player-facing `decay credit` or `compliance credit` terminology. Cost rows are compact and contain one to three icons, while requirements remain in the requirement tooltip or native blocked state.

There are no separate missions or timed objectives in this cost surface. Timed ideas and flags are the lifecycle carriers: inspections, observers, compensation, command reform, defiance programs, and evasion routes have explicit durations, and the existing pulse and cleanup paths refresh or remove their modifiers. The native decision list can still become dense at high tiers, as recorded above.

## AI, route, cleanup, and exploit audit

No AI weights were changed in this tranche. Target decisions retain their existing profile, ideology, severity, tier, war, and industry modifiers. Participant decisions retain zero base AI weight because the existing participant recalculation owns the AI route. The target and participant trigger checks use the same scaled quote as the row and the debit, so missing fuel is tested against the exact fixed-point fraction rather than merely checking positive fuel.

The source audit found no second payment debit in the completion tooltips. Paid decisions use `cost = 0`, a custom affordability trigger, an icon-first custom row, and one hidden effect debit on completion. Fuel debits now subtract the fixed displayed fraction directly. Existing native embargo ownership arrays, relation-rule cleanup, fatigue, burden, timed flags, and dynamic inspection modifier removal remain in place. No free paid-action loop was added; route flags and active-pair checks continue to gate repeat use.

The raid scope blocker remains open. Native raid `actor_effects` currently use a raid-instance `ROOT`, while the condemnation source helper expects a country actor `ROOT`. The raid owners are designing a country-event bridge. Condemnation-specific raid special casing was intentionally not added. The post-bridge test must cover a country-event root, a target score below 0, exactly 0, exactly 500, exactly 1000, and above 1000, with the participant paying against the selected target score.

## MCP and validation evidence

The mandatory GUI read-only route succeeded for the native engine-owned decision window. `hoi4.gui_inspect` used scenario `COND_NATIVE_DECISION_TAB_20260920`, CXT, formal censure, score 500, full fuel, and compliance view. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1fab810ce9db7fac21aea94913c6f2954d13defc11dca0ce3b6ae2ea09c0d60/5984716ed0770a491e25d41365781c719a23b0f39e927226c98b67acaea50947/gui-inspect.b9d848f0ae36459f.json`. It parsed the source graph without blocking diagnostics but reported the known engine-owned `countrydecisionview` offline-render limitations: the native container clipped from 550x1080 to 0x0, several native elements have non-positive offline sizes, and a button-state effect is not executed by the renderer.

`hoi4.gui_render` used the same matching scenario, 1920x1080 at UI scale 1, and normal, disabled, long-text, and missing-localisation states. Artifact examples: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/8741ba8dada2439257e2133d5f5e78894d79670584e7a092ca56075a5640e2e7/countrydecisionview-full.png` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b6c2920b0b248811d6bf4e66dc75e3cda2bcf4bec9cf82147c85870faa0bb51/3db43b6b4da10db5a40eca957f11bb8c3d7e1580c3954afdf2eec3405488ce44/countrydecisionview-layout.json`. The renderer returned `GUI_RENDERED`, five variants, four requested states, and no blocking validation result. It repeated the native clipping and unsupported-effect diagnostics, so the result is evidence of the shared vanilla container rather than a visual approval of the decision row itself. No shared GUI rewrite was attempted.

The weighted route was exposed through `hoi4_probability_inspect` and `hoi4_probability_evaluate`, but no decision-specific inspector was exposed. Final source inspection used adapter `decision_ai_will_do` on `common/decisions/condemnation_sanctions_decisions.txt`; it found 36 candidates and 20 required inputs with zero unresolved inputs in the source scan. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e31d7fd04f70f157fd886fb8ffa04e570508e4bc327508008e8cc61182ab0439/2b3c07e4653dac97a097cd4fb56c6084568818f516265fccba83c50bd2fff430/probability-inspect-c73922aaee3d.json`.

Final `hoi4_probability_evaluate` used the accepted flat scenario schema with scenario set `COND_PROB_FINAL_20260920` and scenario `formal_censure_resource_ready`. It returned `PROBABILITY_ANALYZED_PARTIAL`, 36 candidates, 696 unresolved items, and 28 diagnostics because the offline scenario cannot bind the full country, target, and route state. Analysis id: `probability-9a49525fe6a1cefd2f96b70e`. Source revision: `cc1f6fe97d83eed786446be950ec9ca299fcfdff1e211fcdb1dca79c8382b33e`. Source hash: `c73922aaee3d4db932bbf7e83bb6bfc2866077fcf8379225a896916ca566aa88`. Scenario hash: `855f2014893640f121ca584a30c41cf174a06ea2a04d19c1c022f512d7e05f3a`. Authoritative artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e6e85eea0854c6dc4f141ab8796b3e3a84b8660a4d5b496eeb60690588de960/0b8306c2d57e2e538d25070fbe57781974dbceef5615173ae20332033431b153/probability-9a49525fe6a1cefd2f96b70e.json`. The ranking and unresolved artifacts were emitted with the same analysis. No AI balance change was made, so no before/after probability comparison is claimed; a threshold sweep was also skipped because the candidate pool and runtime state are incomplete and the requested patch did not change any weight.

The custom `chaosx_ai_probability_auditor` subagent route was not exposed in the callable tool set, so the direct MCP weighted inspection and partial evaluation are the available evidence and not a substitute for the parent's auditor route. The initial invalid GUI scenario call was corrected after the MCP reported that `scenario.state` must be a string and `scenario.flags` a record; the final inspect and render used the corrected schema.

Source checks included the score boundary calculation above, one-to-one custom cost key coverage for all 18 decision cost keys, icon-slot counting with a maximum of three, review of each paid and concealment action's trigger and completion effect, UTF-8 BOM checks for the two touched English localization files, and searches confirming no player-facing `decay credit`, `compliance credit`, or `recovery support` text remains in the condemnation localization. No game was launched and no logs were requested. Live gameplay and post-bridge country-event-root behavior remain for the user and parent integration pass.

## Remaining issues and recommended follow-up

The action-category density remains above the six-action guideline in all three target views and in the participant category. Add a phase or second selector in a later accepted UI pass, with the same native/custom cost rows and effects preserved.

The obsolete cost-status helpers in `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt` still contain static cost checks and `fuel_k > 0`, but the audit found no current interface consumer for those orphan names. A shared UI owner should either remove those dead helpers or route them through the new dynamic cost localisers before exposing them again.

The old internal variables and constant group named `condemnation_decay_credit` and `condemnation_compliance_credit` remain in gameplay bookkeeping for compatibility. They do not appear in the player-facing condemnation localization. A later bookkeeping cleanup can rename them after checking every source and save compatibility path.

No separate implementation plan was written because all requested cost and row changes were applied within the approved source surface. This handoff is the review record; the only queued design follow-up is the action-density/UI pass described above.
