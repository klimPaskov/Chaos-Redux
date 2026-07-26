# Event 006 AGX decision lifecycle repair — 2026-07-26

## Disposition

The bounded AGX decision audit in `006_agx_decision_mission_reaudit_2026_07_26.md` found a lifecycle gap in the paid North Sea coastal conference. The authorization gate was correctly published, consumed, and cleaned, but the active 300-day project could survive loss of route, network, candidacy, or recognition validity. The same audit found that the decision reserved three civilian factories while the shared strategic cost text described the standard two-factory tier.

This repair closes those two bounded defects without adding a fallback route or changing the accepted event design.

## Source changes

- `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`
  - `independence_wave_agx_convene_north_sea_coastal_conference` now cancels when any of the package, stable-waterline, recognition, network membership, Low Countries candidacy, focus authorization, route-lock, or capital-control gates become invalid while the project is active.
  - The existing `independence_wave_nwe_apply_project_failure` cancellation effect remains the single failure outcome for a live AGX package.
  - The decision uses the dedicated `independence_wave_cost_agx_coastal_conference` text key so the three-factory reservation and displayed requirement stay aligned.
- `localisation/english/006_independence_wave_decisions_l_english.yml`
  - Added the conference cost, tooltip, and blocked-state strings using `constant:independence_wave_decision_cost.civilian_factory_major`.

## Validation evidence

- Decision block braces remain balanced after the multiline `cancel_trigger` edit.
- The new cost key, tooltip, and blocked-state keys are present and the localisation file retains UTF-8 BOM encoding.
- The cancellation guard names are source-visible in the decision block and the failure effect remains wired.
- The Event 006 allocator audit remains the required system-level check; the whole-event completion audit is still HOLD.

## Remaining risk and scope

The bounded decision audit still recorded low-priority custom-trigger-tooltip coverage gaps outside this lifecycle repair. DM-58 scope preflight is PASS after the nested owner-scope repair, but distinct-owner feasibility and live host/collision matrices remain unproved. This handoff therefore does not change the whole-event HOLD disposition.
