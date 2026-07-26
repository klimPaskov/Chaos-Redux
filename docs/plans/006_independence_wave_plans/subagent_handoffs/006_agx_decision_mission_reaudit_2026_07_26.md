# Event 006 AGX decision and mission re-audit

Date: 2026-07-26.

Scope: fresh read-only review after commits `8c15baa17`, `c9337fd94`, and `79663734e`.

Reviewed surface: the AGX Frisian waterline category, water-board record and government decisions, the North Sea Coastal Conference, the focus-to-decision gate, shared cost helpers, AGX cleanup, and directly linked localisation and AI weights.

## Bounded verdict

**HOLD — one High lifecycle and route-lock defect remains in the new North Sea conference lane.**

The mandate gate itself is correctly wired and its normal lifecycle is coherent.

`independence_wave_agx_mandate_north_sea_coastal_conference_focus` sets `independence_wave_agx_north_sea_conference_authorized`, the paid `independence_wave_agx_convene_north_sea_coastal_conference` consumes that flag as a visibility requirement, its successful completion sets `independence_wave_agx_north_sea_conference_complete`, and `independence_wave_agx_prepare_low_countries_dossier_focus` requires that completion flag.

No gameplay, focus, localisation, GUI, or asset source was edited in this review.

## Issues sorted by severity

### High — conference can finish after its route and eligibility gate have become invalid

`common\decisions\006_independence_wave_wallonia_frisia_decisions.txt`, `independence_wave_agx_convene_north_sea_coastal_conference`, verifies package identity, stable waterline, recognition, network membership, Low Countries candidacy, `independence_wave_agx_north_sea_conference_authorized`, no client lock, and no earlier completion in `visible`.

The active 300-day timer's `cancel_trigger` checks only package identity, stable waterline, and capital control.

Per the consulted decision reference, a regular decision's `visible` block does not cancel an already active timer unless its conditions are repeated in `cancel_trigger` or `cancel_if_not_visible = yes` is used with an appropriate cancellation effect.

An AGX player can therefore start the conference while eligible and subsequently take the patron-client lock, lose network membership or Low Countries candidacy, or fall below the recognition threshold while it is active.

The timer can still run to `remove_effect`, set `independence_wave_agx_north_sea_conference_complete`, grant the regional-conference reward, and unlock the dossier focus despite the route no longer allowing the action.

Recommended narrow repair: extend the conference `cancel_trigger` with the continuing public eligibility conditions, at minimum `has_country_flag = independence_wave_agx_north_sea_conference_authorized`, `has_country_flag = independence_wave_network_member`, `has_country_flag = independence_wave_low_countries_federation_candidate`, `is_independence_wave_recognized_or_later = yes`, and `NOT = { has_country_flag = independence_wave_client_route_locked }`.

The intended cancellation result needs an owner decision: either use the existing failure package for a lapsed mandate, or add a bounded no-reward cancellation tooltip and effect that makes the lost mandate explicit.

### Medium — conference factory commitment is understated in its visible cost string

The same conference uses `modifier = { civilian_factory_use = constant:independence_wave_decision_cost.civilian_factory_major }`, which reserves three civilian factories during its timer.

Its cost trigger `can_pay_independence_wave_strategic_cost` requires more than the shared standard threshold of two available civilian factories, so it becomes available only with three, matching the three-factory modifier.

`independence_wave_cost_strategic` in `localisation\english\006_independence_wave_decisions_l_english.yml` says that it requires the standard two-factory quantity.

The player-facing text is therefore one factory lower than both the active commitment and the availability boundary for this decision.

Recommended narrow repair: give `independence_wave_agx_convene_north_sea_coastal_conference` a conference-specific custom-cost localisation key that shows the major three-factory commitment, including its `_tooltip` and `_blocked` variants, or deliberately align the modifier and gate to the existing strategic-cost contract.

### Low — availability and cancellation requirements lack custom player-facing trigger tooltips

The AGX waterline decisions, water-board government decisions, mandate focus, and conference use readable descriptions and custom cost text, but no `custom_trigger_tooltip` wraps their route, capital, former-host, active-project, or conference-foundation requirements.

The missing details include the fact that a living former host must be at peace for `independence_wave_agx_reconcile_water_board_records`, that one package project may be active, and that the mandate focus is the only source of conference authorisation.

Recommended narrow repair: add short named tooltips to the affected `available` blocks and to `has_independence_wave_agx_north_sea_conference_foundation` at its focus consumer, without exposing raw scripted-trigger names.

## Decision category lifecycle

`independence_wave_agx_waterline_category` is package-visible only for AGX and contains one automatic crisis mission plus nine finite project, government, or conference decisions.

`independence_wave_setup_iw_007_frisia` initializes Waterline Integrity at 25 and Coastal Security at 20, refreshes the exposed-waterline idea, enables the shared focus framework and eligible political routes, then sets `independence_wave_iw_007_setup_complete` only after its setup validation succeeds.

The `independence_wave_agx_hold_the_waterline` mission activates only after that setup flag. Its 540-day timer succeeds through its stable-waterline cancellation branch, fails on expiry or capital loss, and does not appear again after either terminal flag is set.

All four founding projects are finite through their completion flags. The active-project scripted trigger serializes them with the water-board, government, and conference actions, preventing simultaneous project rewards or civilian-factory stacking.

The three government decisions are mutually exclusive in practice through `has_independence_wave_agx_route_government`, and their installation helpers remove competing government ideas before setting the selected government flag.

The AGX package cleanup removes the mission and every category decision, clears both waterline variables, removes AGX ideas, and clears all known project, government, conference, mandate, focus, and formable-preparation flags, including `independence_wave_agx_north_sea_conference_authorized`.

## Mission quality notes

| Mission | Owner | Category and region | Requirement and duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `independence_wave_agx_hold_the_waterline` | AGX after validated IW-007 setup | `independence_wave_agx_waterline_category`; Friesland waterline | Bring Integrity to 60 and Security to 55 before `independence_wave_nwe_package_duration.agx_waterline_crisis` (540 days), while retaining the capital | Stable values set `independence_wave_agx_waterline_crisis_resolved`; expiry or capital loss sets the failed flag, lowers both measures, and applies the founding-failure package | Low; activation and both terminal flags prevent a second crisis mission |

The mission is an active objective rather than a passive stockpile test: it requires choosing and completing waterline, harbor, rail, guard, or focus work under a real deadline.

Its long duration is proportionate to an opening national crisis, and the project family has materially different cost profiles and meter gains.

## Costs and requirement clarity

The reviewed choices are not a flat political-power store.

Pump inspection and constitutional/labor government use command power, manpower, and temporary factory use; harbor and rail work use command power plus a convoy-or-train alternative; dike guards use manpower, Army Experience, infantry equipment, and support equipment; water-board records use the strategic diplomatic transport package; and the conference also sacrifices Stability and War Support.

All reviewed values come from `common\script_constants\006_independence_wave_decision_constants.txt` and `common\script_constants\006_independence_wave_wallonia_frisia_constants.txt` rather than local magic numbers.

The shared custom-cost strings explain the material families but are prose-first rather than the preferred icon-first presentation. The conference's specific three-factory discrepancy is the actionable clarity defect above.

## AI validity and route-lock notes

Every AGX action has a non-zero `ai_will_do` base. The four opening projects are urgent or high, former-host records are suppressed while the waterline is unstable, and the conference has a standard base with a constitutional-route multiplier.

Availability handles material, capital, current-project, former-host-war, and current route checks before an AI can select the action.

The focus chain makes the intended conference lifecycle reachable only after waterline stabilization, route-government installation, succession settlement, network access, and the mandate focus.

The only route-lock failure found is active-timer invalidation for the conference, documented as the High issue. No dead-country target or invalid targeted-decision risk exists on this AGX package surface because the reviewed decisions are not targeted decisions.

`hoi4.focus_inspect` returned the read-only structural artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e63589060aa85ac74913e53b7bd0daf0063c04775c551292f57be2625cd000c/3b31c83204d20eb288b2db3aa04e0e9d58f52029934ad992eeb732fbf1cd8c51/focus-inspect.6fc9b4cccfc792df.json`.

It retained existing tree-wide layout warnings outside this bounded decision review and did not supply a focused AGX AI scenario evaluation. No decision-owned scripted GUI is linked to this category, so `hoi4.gui_inspect` and `hoi4.gui_render` were not applicable.

## Localisation, cleanup, and exploit-risk notes

All reviewed AGX decision, mission, focus, effect-tooltip, and mandate keys resolve in `localisation\english\006_independence_wave_wallonia_frisia_l_english.yml`.

The mandate tooltip correctly states that authorisation does not waive the conference's strategic cost or duration.

The focus and decision flags are consistently named, and the new authorization flag has exactly one normal setter, one gameplay consumer, and one package-cleanup clearer.

Finite completion flags, the serialized active-project trigger, capped waterline variables, one-time focus reward flags, and package cleanup prevent equipment, factory, unit, or conference-reward farming in the reviewed lane.

The High invalidation defect can still grant a one-time regional reward after a closed route; it is a route-bypass issue, not a repeatable reward loop.

## DM-58 context only

This AGX review did not reopen DM-58.

`006_event_completion_audit_v7_addendum_2026_07_26.md` and `006_dm58_preflight_scope_post_repair_2026_07_26.md` retain a source-level PASS for `5dcb2c8de`'s candidate-scope repair.

They also retain the separate unproved distinct-owner feasibility and missing three-distinct-owner success, failure, rollback, and AI-resource evidence.

## Validation and boundary

Meaningful validation consisted of tracing every AGX decision and mission from setup, through availability, cost helper, timer result or cancellation, focus setter or consumer, cleanup, and localisation; reviewing the three specified overlay commits; checking all references to `independence_wave_agx_north_sea_conference_authorized`; and running the read-only focus inspection noted above.

Skipped meaningful validation: no live game or scenario execution was run because this subagent may not launch Hearts of Iron IV, and no focused probability evaluation was available from the MCP for this Clausewitz source selector.

No plan handoff was written because the required remedies are small, local decision lifecycle and localisation changes.

## Whole-event limitations

This bounded finding does not change the Event 006 whole-event **HOLD**.

The authoritative v6/v7 records still leave broader runtime package coverage, focus-layout diagnostics, compatible-country coverage, formables, SCN-008, super-event and asset acceptance, achievement proof, AI/balance matrices, and the remaining DM-58 feasibility evidence unresolved.
