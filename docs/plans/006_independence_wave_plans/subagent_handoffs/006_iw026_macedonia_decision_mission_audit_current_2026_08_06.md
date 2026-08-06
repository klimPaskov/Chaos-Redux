# IW-026 Macedonia decision and mission audit — 2026-08-06

## Scope and outcome

Read-only audit of `common/decisions/006_independence_wave_macedonia_decisions.txt`, its MAC helper effects and triggers, the shared Event 006 decision layer it overlaps, and the related English localisation.

No gameplay, central-admission, advisor, GUI, or live-game changes were made.

## Parent follow-up disposition

After this audit, the parent applied the direct lifecycle corrections: MAC cleanup now clears the six one-shot mission/project flags, and the Danube Network action cancels when its league route or live league phase is withdrawn. The early-phase reward concern is therefore closed by gating the action to phases where the shared league-value writer consumes deltas. The shared-operation concurrency note remains an intentional package-policy choice and is documented in the MAC package page.

The package has a coherent passive founding-crisis contract and concrete, non-political-power project costs, but it has one reactivation-cleanup defect and two medium network/operation-lock concerns.

## Refresh verification - current roster and planner gate

The current MAC package now contains the requested role-roster and exact planner proof. `has_independence_wave_mac_command_roster` requires `MAC_independence_wave_vardar_presidium` and confirms that character as a corps commander. `has_prepared_independence_wave_iw_026_package_setup` requires that roster, `independence_wave_command_roster_ready`, the signature-module registration, selected and registered Danubian formable profile, focus framework and route registrations, exact anchor/former-host conditions, and the IW-026 force-package mapping.

`independence_wave_setup_iw_026_macedonia` first recruits `MAC_independence_wave_vardar_presidium` only if absent, then invokes hidden roster event `chaosx.nr6.350`, which sets the MAC roster checkpoint only after the same roster trigger passes. The setup effect only marks `independence_wave_iw_026_setup_complete` after that gate passes. This is sound static lifecycle proof for the newly added roster/planner contract. It does not remove the decision-surface findings below, and source inspection alone cannot prove a live runtime setup sequence.

## Issues, ordered by severity

### High — package cleanup leaves one-shot decision state behind

`independence_wave_cleanup_iw_026_macedonia` removes the mission and decisions but does not clear six package flags set by the decision surface:

- `independence_wave_mac_foundation_crisis_resolved`
- `independence_wave_mac_foundation_crisis_failed`
- `independence_wave_mac_depots_reopened`
- `independence_wave_mac_networks_screened`
- `independence_wave_mac_community_council_convened`
- `independence_wave_mac_durable_sovereignty`

Although cleanup clears several setup, roster, government, and route flags, the founding mission's activation and the project visibility checks still rely on the six omitted flags. If the MAC carrier is returned to an IW-026 lifecycle after package cleanup, the founding mission remains suppressed, the three foundation projects remain hidden, and durable sovereignty remains unavailable.

Recommended bounded fix: add matching `clr_country_flag` entries in `common/scripted_effects/006_independence_wave_macedonia_package_effects.txt` inside `independence_wave_cleanup_iw_026_macedonia`.

### Medium — Danube Network can complete after its league route is withdrawn

`independence_wave_mac_open_danube_network` requires `independence_wave_league_route_available` only in `visible`. A running timed decision is not cancelled merely because it stops being visible. Its `cancel_trigger` checks package identity, network membership, and capital control, but not withdrawal of the league route.

The project can therefore apply `independence_wave_mac_reward_network_project` after route withdrawal. This is the same lifecycle class found in the current Iberian network audit.

Recommended bounded fix: add `NOT = { has_country_flag = independence_wave_league_route_available }` to this decision's `cancel_trigger` in `common/decisions/006_independence_wave_macedonia_decisions.txt`.

### Medium — the network tooltip can promise league gains that are silently not applied

The Danube action becomes visible with MAC network membership and the local league-route availability flag. Its reward always raises MAC network standing, but the shared `independence_wave_change_league_values` helper applies cohesion, common-cause, reserve, and confidence changes only from `regional_conferences` onward. In `informal_network`, the decision is consumed and the localisation still promises league-wide gains.

Recommended design decision: either gate MAC's Danube project to a league phase accepted by `independence_wave_change_league_values`, or use phase-aware tooltip/effect wording that describes a network-standing-only early use. This is a narrow decision/reward clarification, not a request to redesign the league.

### Medium — package projects do not participate in the shared Event 006 operation locks

The MAC-local `has_independence_wave_mac_active_package_project` serializes the eleven timed package projects. The shared `has_independence_wave_active_founding_mission`, `has_independence_wave_active_diplomatic_action`, and `has_independence_wave_active_security_mission` helpers contain no IW-026 mission or project IDs.

Consequences to decide deliberately:

- The 420-day passive Vardar crisis can coexist with the shared founding-mission chain.
- `independence_wave_mac_settle_yugoslav_ledgers` can run with a shared former-host diplomatic operation.
- Depot/veteran actions can run with shared security operations, and the Danube action can run with shared diplomatic actions.

This may be intentional parallel progression, but it does not implement the shared one-active-operation policy. The unused `independence_wave_mac_foundation_crisis_active` branch in the MAC-local lock confirms that the founding crisis has no active-operation representation. Parent review should choose between intentionally documenting the parallelism or adding narrowly scoped shared lock membership; no central admission change is required either way.

### Low — package document describes a cost that the passive mission does not have

`docs/events/006_independence_wave/macedonia_package.md` calls the founding crisis a “paid 420-day mission.” The actual mission is deliberately passive: `available = { always = no }`, no `selectable_mission`, no custom cost, and no `complete_effect`. Projects, not the timer, pay the concrete costs.

Recommended documentation-only correction: call it a passive 420-day founding crisis resolved through costed projects.

## Decision category lifecycle notes

Category: `independence_wave_mac_vardar_council_category`.

The passive mission `independence_wave_mac_hold_vardar_council_together` activates only for the configured MAC/IW-026 package until a result flag is set. `available = { always = no }` correctly prevents a non-selectable mission from immediately completing. It lasts `constant:independence_wave_macedonia_duration.founding_crisis` (420 days), succeeds by cancellation when both local ledgers are at least `independence_wave_macedonia_pressure.stable` (60), and fails on timeout or loss of capital control. Success sets `independence_wave_mac_foundation_crisis_resolved`; failure applies the documented five-value and two-ledger loss through `independence_wave_mac_apply_project_failure`.

The category's timed projects all require package identity, a controlled capital, and no active MAC package project. Ordinary project cancellation handles package loss/capital loss; the former-host project additionally cancels if the former host disappears or war starts. The five route-confirmation projects check the corresponding selected shared route both on visibility and cancellation, and their installer helpers repeat the route/no-government guard. This is a sound local route lock.

The shared full-focus capstone, not this mission, sets `independence_wave_founding_settlement_complete`; the strategic `independence_wave_mac_codify_vardar_settlement` correctly requires that separate completion flag.

## Mission quality notes

| Owner | Category / region | Requirement | Duration | Success / failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| MAC / IW-026 | Vardar Civic Council / Balkans-Danube, anchor state 106 | Exact MAC package, IW-026 setup complete, no prior result | 420 days | Stable civic mandate and mountain defence cancel to success; timeout or lost capital fails and lowers ledgers/state values | No duplicate local ID; currently overlaps shared founding operations because it is absent from their active-mission helper |

## Costs, requirements, and tooltip notes

The concrete cost contract is complete and pairs each custom-cost trigger with its matching payment helper:

| Actions | Cost palette and timing |
| --- | --- |
| Depots; Municipal Charter; Mountain Workers | Administration light: Command Power, manpower, and one civilian factory for depot duration; 75 days |
| Community Council | Administration standard: Command Power, manpower, and two civilian factories; 120 days |
| Veteran Networks | Security standard: manpower, Army Experience, infantry equipment, support equipment; 120 days |
| Mountain Commission | Security major: larger manpower, Army Experience, infantry, and support commitment; 120 days |
| Former-host ledgers; Village Autonomy; Rail Patron; Danube Network | Diplomatic standard: Command Power and either convoy or train reserve; 180 days |
| Vardar Settlement | Strategic: Stability, War Support, Command Power, convoy/train commitment, and spare civilian-factory capacity; immediate, one-shot |

Every inspected decision name, description, custom effect tooltip, and custom cost key—including `_tooltip` and `_blocked` variants—has English localisation. The two localisation files retain UTF-8 BOM encoding. No raw trigger was exposed to the player by this package's own descriptions; cost text explains the resource commitments.

The shared cost predicates use strict `>` checks against the displayed cost values, retaining a tiny/single-unit reserve over the shown threshold. This is inherited shared-palette behavior, not an IW-026-only defect; retain it deliberately or revise the shared wording/thresholds in a separate core decision pass.

## AI validity and route-lock notes

All twelve entries declare `ai_will_do`. The meaningful score ranges are 10/20 for peace-weighted former-host settlement, 25/50 for veteran screening in war, and 100/200 for the emergency commission in war; all other package actions use the shared standard or high scores. Availability, controlled-capital, package identity, and selected-route checks remain the hard validity gates. No target decision can select a dead or invalid country.

The dedicated read-only IW-026 probability audit is running separately as `/root/event6_iw026_macedonia_ai_probability_audit_current`; its MCP scenario evidence must be read with this handoff before any AI weight change. No AI value was changed here.

## Cleanup and exploit-risk notes

The local active-project guard prevents parallel MAC timers, and all rewards are one-shot flags or `fire_only_once` settlement state. No free-unit or repeatable equipment loop is introduced by this package surface.

The cleanup omission described above is the remaining direct exploit/lifecycle defect. The former-host action safely refuses a dead host and cancels if host war starts. The Danube action's missing route-withdrawal cancellation and early-phase league-value no-op remain the two live reward-state risks.

## MCP and validation evidence

- The repository exposes no decision/mission-specific inspect/render tool. `hoi4.event_inspect` accepted the source-file selector but returned only a workspace-wide, partial Event Chain Viewer scan (`EVENT_INSPECTED_PARTIAL`) rather than decision/mission semantics: revision `ac30ffb41cd030372cc34c0d4229d1d6c58242e02002e28c6a2c291bdd397238`, graph hash `e1ecab98dcea0cc6a837c50c386f108efec055aff103ad775c71aa0dd3dc90a2`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c81d7ebcfd9c9dc2a0c06717ded539d6e8e619743bf98eb98206137d30e67093/db0bbe4dcaf3a424d5ba056d08785024b8beb600ca3af46bb27a8edba0adc331/event-scan-ac30ffb41cd0.json`. It explicitly reports partial validation because helper/lifecycle projections were deferred. This is not equivalent to a decision/mission engine audit.
- `hoi4.probability_inspect` was available; numerical decision/mission evidence is intentionally owned by the separately running probability auditor named above.
- No decision-owned scripted GUI exists in the scoped MAC decision, effect, or trigger files, so `hoi4.gui_inspect` and `hoi4.gui_render` did not apply.
- Refreshed static reference coverage found 13 MAC category/decision identifiers and 12 custom-cost/effect-text references with zero missing English localisation keys; called scripted helpers still resolve within the inspected package/shared layer.
- No live-game launch was performed.

## Files changed

- Added this audit-only handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw026_macedonia_decision_mission_audit_current_2026_08_06.md`

No decision, mission, scripted GUI, localisation, effect, trigger, or central-admission identifier was changed.

## Remaining follow-up

Parent should decide the intended shared-operation concurrency model, apply the high cleanup correction and Danube cancellation fix if accepted, and reconcile the network action's promise with its allowed global league phases. Read the independent probability handoff before accepting or changing AI behavior.
