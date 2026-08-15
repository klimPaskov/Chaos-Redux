# IW-033 / IW-041 decision and founding-mission audit

Date: 2026-08-05

Mode: read-only audit.

Scope: `IW-033` Karelia and `IW-041` Crimean Tatar State decisions, founding missions, shared decision costs, local triggers and effects, cleanup, AI strategy, package constants, and directly referenced localisation.

No gameplay, AI, GUI, or localisation source was changed.

## Current owner-patch status (2026-08-05)

The owner patch is recorded in `006_documentation_curator_iw033_iw041_owner_patch_reconciliation_current_2026_08_05.md`. It removes the founding missions from the active-project predicate, makes stable-ledger mission success require a route government, passes the shared reserve and member-confidence helper inputs, requires a live League phase before the network action can consume its one-shot flag, removes the former-host decision and clears `independence_wave_kc_host_settled` during cleanup, makes former-host settlement idempotent, and adds capital-loss cancellation to every government route. The source defect list below is retained as a pre-owner-patch baseline and no longer describes those current code paths. The owner later promoted IW-033 and IW-041 into the central content-attestation registry; the parent-waived Level 2 focus breadth limitation and package-specific probability/runtime evidence remain separate bounded findings.

## Later owner-AI reserve-floor tranche (2026-08-05)

The owner-AI handoff `006_iw033_iw041_owner_ai_reserve_floor_patch_2026_08_05.md` adds executable `ai_will_do` behavior to the regular IW-033/IW-041 and combined host/network decisions. Selection waits for foundation settlement, prefers the lower regional ledger, and applies zero-weight post-spend floors for command power, manpower, infantry equipment, support equipment, trains, convoys, fuel, and major security actions through the centralized `independence_wave_karelia_crimea_ai_floor` table and reusable package triggers. The audit's pre-owner AI observations remain historical; same-scenario MCP comparison, normalized selection, balance, and live runtime evidence remain pending.

## Pre-owner-patch result (superseded)

**HOLD.** Both founding missions are structurally unable to complete because the active-project lock counts the mission itself as an active project.

The regional-network reward also writes two temporary variable names that its shared helper never consumes.

The package should not be admitted until at least those two defects and the mission completion race are repaired.

## Issue list, ordered by severity

### Critical — the founding mission deadlocks every required action

`has_independence_wave_karelia_crimea_active_project` in `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt:162` includes both `has_active_mission = independence_wave_kar_hold_statehood_foundation` and `has_active_mission = independence_wave_cri_hold_statehood_foundation`.

Every project, government action, former-host settlement, durable-state action, and network action in `common/decisions/006_independence_wave_karelia_crimea_decisions.txt` requires `NOT = { has_independence_wave_karelia_crimea_active_project = yes }`.

The founding missions activate on package setup and last 210 days, so their own presence makes every action that can raise ledgers or install a government unavailable until the mission ends.

The mission then times out or cancels into `independence_wave_kc_apply_failure`.

The matching Transylvania and Montenegro active-project triggers list only active timed decisions and do not include their founding missions.

Recommended repair: remove both founding-mission checks from `has_independence_wave_karelia_crimea_active_project`, retaining the one-timed-decision-at-a-time checks.

### High — the network decision silently omits two promised rewards

`independence_wave_kc_reward_network` in `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt:432` sets `independence_wave_league_reserve_delta` and `independence_wave_league_confidence_delta`.

`independence_wave_change_league_values` consumes `independence_wave_league_shared_reserve_delta` and `independence_wave_league_member_confidence_delta` in `common/scripted_effects/006_independence_wave_effects.txt:2867`.

Consequently the one-shot network action can change cohesion and common cause but cannot grant its intended shared-reserve or member-confidence rewards.

Its localisation promises all three results through `independence_wave_kc_network_effect_tt` in `localisation/english/006_independence_wave_karelia_crimea_l_english.yml:112`.

Recommended repair: rename the two local temporary variables to the helper's exact `shared_reserve` and `member_confidence` input names, then use a focused before/after helper trace.

### High — stable ledgers can fail the mission before a government is installed

Each mission's `cancel_trigger` in `common/decisions/006_independence_wave_karelia_crimea_decisions.txt:19-25` and `:41-47` cancels when its ledger trigger becomes true, independently of the government requirement.

The `cancel_effect` only calls `independence_wave_kc_resolve_foundation`, which succeeds only when stable ledgers, a route government, package receipts, and capital control are all present.

If the final ledger-improving project completes before the player finishes a government action, the mission cancels and records foundation failure rather than remaining active to the 210-day deadline.

Recommended repair: make the success-cancel branch require both stable ledgers and `has_independence_wave_karelia_crimea_route_government = yes`.

Keep invalid package or capital-loss cancellation separate, so that stabilising ledgers without a government leaves time to install one rather than imposing an undocumented ordering trap.

### Medium — a foundation failure leaves spending actions visible with no recovery path

`independence_wave_kc_foundation_failed` prevents mission reactivation but is not used to hide or remove the remaining package actions.

After failure, projects and government decisions can still consume their one-time resources, but durable sovereignty and network actions require `independence_wave_founding_settlement_complete`, which failure never sets.

No event, decision, or mission outside this package references the failed or crisis-escalated flag as a recovery receipt.

Recommended repair: either remove or hide unfinished foundation actions when failure resolves, or add an explicit, costed recovery path that clears failure and reactivates the founding mission.

### Medium — cleanup leaves the former-host settlement state and decision outside its package reset

The two package cleanup effects remove all listed local actions but omit `independence_wave_kc_negotiate_former_host` in `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt:556-635`.

They also do not clear `independence_wave_kc_host_settled`.

The latter flag gates both the former-host settlement's visibility and the KAR/CRI host-restraint AI strategies.

An origin reset can therefore inherit a settlement receipt from an earlier incarnation and skip the intended diplomatic stage and restraint layer.

Recommended repair: remove the former-host decision during both package cleanups and clear `independence_wave_kc_host_settled` beside the other KC lifecycle flags.

### Medium — government actions can resolve after the capital falls

The eight timed government decisions at `common/decisions/006_independence_wave_karelia_crimea_decisions.txt:197-307` check capital control only in `available`.

None has a `cancel_trigger` or `cancel_effect`, and their government-install effects do not recheck capital control.

An action begun while the capital is held can still change politics, party names, leaders, ideas, and route flags after its capital is occupied.

Recommended repair: add the same package-invalid or capital-lost cancellation contract used by the projects, with a deliberate cancellation outcome rather than a free government change under occupation.

### Medium — the one-shot network reward may spend before league values are live

The network decision only requires `independence_wave_network_member` and `independence_wave_league_route_available`.

`independence_wave_change_league_values` applies changes only during specified live league phases in `common/scripted_effects/006_independence_wave_effects.txt:2872-2894`.

If a carrier opens the corridor before those phases, it consumes its one-shot flag while the global league deltas are a no-op.

Recommended repair: add the shared live-league-phase requirement to the decision's availability, or retain and apply its deltas when the league activates.

### Medium — foundation success and the paid settlement both apply the former-host delta bundle

`independence_wave_kc_resolve_foundation` invokes `independence_wave_kc_apply_former_host_settlement` on success at `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt:316-340`.

The separately paid `independence_wave_kc_negotiate_former_host` invokes the same bundle and is not blocked by foundation settlement.

This is not repeatable farming because the paid action sets `independence_wave_kc_host_settled`, but it stacks the same relationship changes once automatically and once through the stated paid project.

Recommended repair: confirm that this two-stage settlement is intentional and expose its distinct receipts, or guard the automatic application with the former-host-settlement flag.

### Medium — local custom-cost feedback is incomplete and malformed

The eight package-specific `custom_cost_text` families lack their implicit `_blocked` and `_tooltip` localisation companions.

The eight visible cost strings in `localisation/english/006_independence_wave_karelia_crimea_l_english.yml:93-100` contain the malformed `U+00C2 U+00A3` sequence instead of the single HOI4 text-icon marker.

This removes dependable blocked-cost feedback for railhead, security, commission, transit, survey, return, screening, and customs actions.

The paired localisation audit records all sixteen missing companion keys and the exact code-point evidence in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw033_iw041_localisation_audit_2026_08_05.md`.

Recommended repair: provide dynamic constant-backed normal, blocked, and hover text for every local cost family, using the proper command-power, train, convoy, equipment, manpower, and fuel icons.

### Low — shared cost requirements demand an undisclosed strict surplus

The shared administration, diplomatic, security, and strategic cost triggers use strict `>` checks in `common/scripted_triggers/006_independence_wave_decision_triggers.txt:227-280`, while their payment effects subtract exactly the displayed value.

For example, the former-host decision cannot start at exactly 20 command power and 10 trains or convoys even though the player-facing cost says that it commits those exact amounts.

This may be intentional safety reserve design, but the cost text should say “requires more than” or the requirements should allow an exact payment.

## Decision category lifecycle

1. Package release marks setup complete and activates the appropriate 210-day founding mission in `independence_wave_karelia_crimea_category`.

2. The player should execute projects, then a focus-unlocked government action, then allow mission success to set the founding-settlement receipt.

3. The current active-project predicate blocks step 2 for the entire mission duration.

4. On a successful mission, the carrier receives large shared progress, durable-state focus progress, an automatic former-host relationship change, and `independence_wave_founding_settlement_complete`.

5. Durable sovereignty and the network corridor then become available under their route, ledger, capital, material, and membership conditions.

6. On timeout, invalid cancellation, or premature stable-ledger cancellation, the mission applies the central failure bundle and raises the next crisis tier.

7. Origin cleanup removes the missions and most decisions, ideas, ledger variables, and route/project flags, but currently omits the former-host action and settlement flag.

The category has no dedicated scripted GUI, so no decision-owned GUI inspection or render applied.

## Founding-mission quality notes

| Mission | Owner / category / region | Requirement and duration | Success / failure | Duplicate and lifecycle risk |
| --- | --- | --- | --- | --- |
| `independence_wave_kar_hold_statehood_foundation` | KAR / `independence_wave_karelia_crimea_category` / state 146 | KAR package and IW-033 setup, unfinished status, 210 days | Needs both Karelian ledgers at 65, route government, shared package and force receipts, and capital control; otherwise the standard failure bundle | Separate identifier and no duplicate definition found, but its own active state blocks every requirement-producing decision and its ledger cancellation can fail prematurely. |
| `independence_wave_cri_hold_statehood_foundation` | CRI / same category / state 137 | CRI package and IW-041 setup, unfinished status, 210 days | Needs both Crimean ledgers at 65, route government, shared package and force receipts, and capital control; otherwise the standard failure bundle | Separate identifier and no duplicate definition found, with the same deadlock and premature-cancellation defects. |

`available = { always = no }` is appropriate for a passive mission, but the category and mission localisation do not disclose the exact ledgers, current values, 65 threshold, capital requirement, government receipt, or one-project limit.

## Cost and requirement clarity

The package uses varied, concrete local costs rather than a flat political-power exchange.

- Karelia spends command power plus trains for railheads and transit, infantry and support equipment for the Ski Guard, and manpower for the Language Commission.
- Crimea spends command power plus manpower for survey and return work, infantry and support equipment for screening, and convoys plus fuel for Black Sea customs.
- Former-host, government, durable-state, and network actions use shared administration, diplomatic, security, and strategic cost bundles.

The durations are centralised in package constants at 30, 45, 60, and 210 days.

The concrete resource variety is sound, and one-time action flags prevent repeated equipment or ledger farming once the active-project defect is fixed.

The remaining player-facing requirement gaps are capital control, alive and peaceful former host, route choice, ledger thresholds, settlement status, live league phase, and the one-active-project rule.

## AI validity and route locks

KAR and CRI have symmetric survival, former-host restraint, and settled-state strategies in `common/ai_strategy/006_independence_wave_karelia_crimea.txt`.

The former-host decision correctly verifies a living saved host, peace, package status, and capital control both at start and cancellation.

The transit action correctly requires its saved former host and peacetime condition, and the network action requires membership plus the league focus route.

The host-restraint AI layer becomes invalid after the stale `independence_wave_kc_host_settled` cleanup state, as described above.

Balance-sensitive decision and mission scores were routed to `chaosx_ai_probability_auditor` with peacetime, wartime, former-host, and post-foundation scenarios.

The baseline decision inspection discovered only the two durable-sovereignty candidates, with 11 required inputs and an incomplete runtime pool.

The mission inspection discovered 20 candidates with 14 required inputs and an incomplete runtime pool.

An explicit two-mission control evaluated both founding missions as unavailable because their `available = { always = no }` contract is passive, with the same raw AI score of 120 and no normalized selection probability.

No named peacetime, wartime, former-host, or post-foundation score result is valid yet.

The probability adapter cannot resolve the compound scoped conditions in this package from the accepted typed state declarations, including command power, equipment, capital scope, active missions, active decisions, and route flags.

Treat the static strategy values as source evidence only, not balance validation, until the adapter accepts a complete typed scenario contract.

## Localisation and tooltip gaps

In addition to the cost feedback defect, the two mission descriptions use abstract references to the “opening force,” “stable authority,” and unspecified ledgers.

The failure, route, and host-settlement tooltips do not enumerate their material state changes.

`independence_wave_cri_services_effect_tt` exposes implementation language about a “free formation loop,” and `independence_wave_kc_route_effect_tt` names a “shared Event 006 ledger.”

The paired localisation handoff contains the complete key list, party-name mismatch, country naming policy question, and dynamic ledger recommendation.

## Cleanup and exploit-risk notes

The one-project limit and one-time action flags are a useful anti-farming contract, but the mission-inclusive active-project test makes them a total lock instead.

There is no free-unit, core, or war-goal loop in the local effects.

The recoveryless post-failure state can consume resources on decisions that can no longer reach durable-state rewards.

Former-host settlement is not repeatable but can stack with the automatic foundation settlement bundle.

The omitted former-host cleanup creates a cross-origin stale-route and stale-AI risk.

## MCP and validation evidence

Required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, event, decision, idea, and AI modding were consulted.

Vanilla decision and mission documentation and `common/decisions/BALTIC.txt` were consulted for mission activation, cancellation, timeout, and removal precedent.

The installed HOI4 MCP exposes no dedicated decision or mission inspect, render, or lint transport.

This is an exact transport limitation, so source review is not treated as equivalent decision-list or mission visual evidence.

No dedicated decision-owned scripted GUI exists in this package, so `hoi4.gui_inspect` and `hoi4.gui_render` do not apply.

The mandatory probability-auditor baseline completed through the available MCP route.

- Decision inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ecbfcf6b1cb96ae9777e9c92a0e5e2511a7af1028b67aa82ee4671e6e5e8f6a/1fc932e40d5db921a42bc4e46ebc9b6976517f0ed2b339ebbefbcfd436b6acec/probability-inspect-43d279a452b6.json`.

- Mission inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f942eb575167ba8a736a99bc806ff9e8a55824c5cc75698c1cb828f096d6af19/5da46b4ca20a25e4aa1348bcded149566c4568a40a7e5b23fae89e033d6b7685/probability-inspect-43d279a452b6.json`.

- Passive-foundation-mission control artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17ce1193b3e072a9ca6aac4e925144408f1b9c9f9eee804111be6640c3b424cd/160ad97e7826b77a68983c231f885b23ce2cfaff9f632c27ab0db792917e6346/probability-3a00d1428faf8d5f4cc14ccb.json`.

- Empty-state durable-decision probe artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b6380e4c37ea036deb07854bdf37e0ae3f00a390f4568c36fcbd7be1f92594f/21eb806c5287d1c95ee1eea0f3efd83534e02e5167402ab46528faf4021f4276/probability-9e9058b7b57bf3be7b1b078e.json`.

The exact blocker for the requested named scenarios is unresolved compound typed state in the probability adapter, rather than the absence of `hoi4.probability_inspect` itself.

Meaningful source validation traced each mission's activation, cancellation, timeout, and resolution path; every local action's active-project gate; the network reward helper input names; both package cleanup lists; and shared cost and league-phase contracts.

Static identifier searches found no duplicate local decision or mission definitions.

Skipped validation: no game launch was performed, consistent with repository rules, and no dedicated decision/mission MCP transport is installed.

## Changed files and handoff status

Changed file: this audit handoff only.

Changed gameplay, mission, decision, scripted-GUI, AI, or localisation identifiers: none.

No source patch was made because this assignment was explicitly read-only.

No plan handoff was written because the defects are narrow corrections to an existing package rather than a proposed new decision system.

## Recommended patch order

1. Remove the two founding missions from `has_independence_wave_karelia_crimea_active_project`.

2. Correct the two network helper input variable names.

3. Reshape the mission cancellation success condition so ledger stability and a route government arrive together.

4. Add former-host action and flag cleanup, then cancellation for the eight government actions.

5. Decide the post-failure recovery policy and the league-phase delivery policy before enabling those one-shot routes.

6. Repair local custom-cost localisation and add concise trigger tooltips and dynamic ledger visibility.

7. After an owner patch, rerun the same probability scenarios through `chaosx_ai_probability_auditor` and use `hoi4.probability_compare` against its baseline artifacts.
