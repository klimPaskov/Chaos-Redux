# Event 006 AGX conference decision re-audit v12

Audit date: 2026-07-26.

Scope: `independence_wave_agx_convene_north_sea_coastal_conference` and its direct Event 006 decision localisation and helper references.

## Verdict

The lifecycle and factory-cost defects reported by the older v10 admission audit are resolved in post-`187115bd1` source.

This audit found one remaining low-severity player-facing defect and patched it: the availability tooltip exposed raw scripted-helper conditions instead of explaining the strategic payment, capital-control, and single-project requirements.

No broader Event 006 system, focus, asset, map, scripted GUI, or helper design was changed.

## Issue list, sorted by severity

1. Resolved, low severity: the decision's `available` block displayed raw helper-trigger names for `can_pay_independence_wave_strategic_cost` and `has_independence_wave_agx_active_package_project`, plus an unlabelled nested capital-control trigger.

No unresolved high- or medium-severity defects were found within this decision scope.

## Changed files and identifiers

- `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`
  - Updated `independence_wave_agx_convene_north_sea_coastal_conference`.
  - Replaced the three raw `available` predicates with `custom_override_tooltip` wrappers that preserve exactly the existing predicates.
- `localisation/english/006_independence_wave_decisions_l_english.yml`
  - Added `independence_wave_agx_coastal_conference_capital_control_tt`.
  - Added `independence_wave_agx_coastal_conference_no_active_project_tt`.

## Before and after behavior

Before this patch, the conference was correctly blocked when strategic resources, capital control, or project exclusivity were missing, but the decision tooltip could surface internal helper identifiers.

After this patch, the same conditions gate the decision with readable player-facing lines: the existing dedicated strategic-cost tooltip, `Keep the capital under Frisian control.`, and `No other Frisian founding project may be active.`

The patch does not change the cost, duration, reward, AI weight, cancellation criteria, or cleanup behavior.

## Decision category lifecycle notes

The decision belongs to `independence_wave_agx_waterline_category` and becomes visible only for a live AGX package with a stable waterline, recognized founding phase, network membership, Low Countries candidacy, focus authorization, an unlocked client route, and no completed conference.

It starts a 300-day strategic project, reserves three civilian factories through its modifier, spends the strategic material package immediately, and blocks every other AGX package project through `has_independence_wave_agx_active_package_project`.

The `187115bd1` lifecycle repair makes the active project cancel when any visible prerequisite becomes invalid, including recognition, network membership, candidacy, authorization, client-route validity, waterline stability, package identity, or capital control.

Normal resolution sets `independence_wave_agx_north_sea_conference_complete` and calls `independence_wave_nwe_reward_regional_conference`.

Cancellation applies the existing founding-project failure effect only while the AGX package still exists, so invalidated projects cannot grant the conference reward.

`independence_wave_cleanup_iw_007_frisia` removes the decision and clears its authorization and completion flags on package teardown.

## Mission quality notes

No mission is owned by this conference decision.

The category's separate waterline mission is outside the requested conference-decision surface, so no mission duration, success, failure, or duplicate assessment was changed here.

## Cost and requirement clarity notes

The current `can_pay_independence_wave_strategic_cost` gate requires more than two available civilian factories, which is the minimum three required by the conference's `civilian_factory_major = 3` reservation.

The dedicated `independence_wave_cost_agx_coastal_conference` cost, tooltip, and blocked keys accurately state the three-factory condition and the stability, war-support, command-power, and convoy-or-train commitment.

The availability text now names the remaining two non-material requirements without exposing raw trigger syntax.

## AI validity and route-lock notes

The AGX-only visibility gate and client-route lock prevent use by an invalid package or patron-client route.

The AI uses the existing standard strategic weight, doubled for constitutional or popular-council routes, and can only evaluate the decision while the same visibility and availability gates are true.

No target scope, dead-country target, or route bypass exists on this decision.

## Localisation and tooltip notes

The dedicated major-factory cost localisation introduced by `187115bd1` is present in normal, tooltip, and blocked forms.

This audit added the two missing availability-tooltip keys listed above.

The localisation file remains UTF-8 with BOM.

## Cleanup and exploit-risk notes

The decision is one-time through `independence_wave_agx_north_sea_conference_complete` and cannot be rerun for repeated network rewards.

The active-project helper includes the conference itself, preventing overlapping AGX project timers.

Cancellation repeats every substantive completion prerequisite and routes live-package failure to the existing project-failure effect, preventing reward resolution after a route, recognition, or authorization loss.

No equipment farming, free-unit loop, war-goal spam, core spam, or cooldown abuse was found in this narrow decision.

## Meaningful validation

- Re-read the offline Decision modding, Triggers, Effects, Localisation, Data structures, Scopes, Modifiers, On actions, Event modding, Idea modding, and AI modding references, plus vanilla `common/decisions/_documentation.md`, current vanilla decision examples, and vanilla trigger documentation for `custom_override_tooltip`.
- Ran a targeted static contract check that confirmed all three readable availability wrappers, all post-`187115bd1` cancellation gates, the dedicated AGX three-factory cost key family, and UTF-8 BOM localisation.
- Reviewed `has_independence_wave_agx_active_package_project`, `can_pay_independence_wave_strategic_cost`, `independence_wave_decision_pay_strategic`, `independence_wave_nwe_reward_regional_conference`, and `independence_wave_cleanup_iw_007_frisia` for predicate, cost, reward, and teardown alignment.

## Skipped meaningful validation

No Hearts of Iron IV process, save/load, AI campaign, or live decision-timer execution was run.

No scripted-GUI inspection was needed because this decision has no decision-owned scripted GUI surface.

## Remaining issues and parent follow-up

No remaining concrete defect was found in the AGX conference decision, its direct localisation, or its direct helpers.

The parent-wide Event 006 blockers remain outside this task, including the shared-focus geometry HOLD, the nine-group exact-ten capacity boundary, and live runtime validation.

No additional plan handoff was written because this patch is local and does not require a broader mechanic decision.
