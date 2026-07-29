# Event 012 Charter autonomy and continental focus AI

## Overview

Event 12 uses two consent-based autonomy states and ten bounded AI strategy plans to make the Charter League's negotiated constitutional relationships visible in engine behavior.

The autonomy states are not colonial progress ladders.
They cannot drift through ordinary autonomy gain or loss, and the Event 12 relationship state machine is the only system that may apply or remove them.

The focus plans do not select a constitution or replace the 64-profile action AI.
They order already-eligible focuses after the host has selected a route, preserve crisis urgency, and keep shared institutional lanes moving toward proof-bearing outcomes.

## Runtime files

- `common/autonomous_states/012_africa_autonomy.txt`
- `common/ai_strategy_plans/012_africa_focus_plans.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/national_focus/012_africa_continental_focus_tree.txt`
- `localisation/english/012_african_union_l_english.yml`

## Charter autonomy flow

1. A member remains an independent Charter partner through the Protected, Associate, and Chartered relationship stages.
2. A negotiated autonomy statute records `africa_member_autonomy_statute_accepted` and explicit continental constitutional acceptance.
3. The shared relationship transition enters Autonomous Federal status and applies `autonomy_africa_federal_member`.
4. The member keeps its country identity, can decline calls to war, contributes no manpower levy, transfers no peace score, and cannot drift toward a different autonomy state.
5. Final integration requires `africa_member_final_integration_consent` and applies `autonomy_africa_integrated_region`.
6. The integrated region joins common command and shares a bounded portion of trade, industry, and manpower while keeping its country identity and local government.
7. Withdrawal, refusal, rivalry, resistance, or an outside settlement calls the shared release helper.
8. That helper ends only an Event 12 Charter subject relationship and never dissolves an unrelated pre-existing subject arrangement.

The two player-facing autonomy names and descriptions are `autonomy_africa_federal_member` and `autonomy_africa_integrated_region`.

## Continental focus AI flow

The ten strategy plans are:

- one uncommitted constitutional-deliberation plan;
- seven constitution-specific route plans;
- one shared support-institutions plan; and
- one Charter formation and post-formation plan.

Every plan requires an AI-controlled current Event 12 host with the continental tree.
Route plans additionally require the exact constitution and abort if the host or constitution changes.

Focus weights are centralized in the AI-plan file and express an order rather than a flat preference:

- low weights keep route-entry and prerequisite focuses available;
- normal and elevated weights advance route institutions and shared support lanes;
- very high and urgent weights prioritize proof focuses and Charter relationship milestones;
- crisis and outcome weights force constitutional crisis resolution before unrelated expansion.

The focus-local `ai_will_do` blocks remain responsible for live League values, member conditions, route choices, and mutually exclusive outcomes.
The plans supply sequence and urgency without bypassing focus availability or completion rules.

The bounded action controller composes all active regional, constitutional, relationship, foreign-power, high-chaos, world, and host-specific profile layers.
Its early and late dispatchers cover Actions 1 through 102 without scanning every country on a recurring on-action.
Scramble phase changes and the world-order opening refresh the stored host-policy snapshot immediately, so AI decision weights do not wait for the controller's next cadence.
The 22 full host playbooks also activate one exact country-specific focus plan.
Each plan translates its accepted matrix priorities into a distinct combination of shared-opening, host-signature, matching regional-overlay, support-lane, and constitutional-route weights while leaving live focus availability and `ai_will_do` gates authoritative.

The continental tree is installed through `africa_load_continental_focus_tree`.
That helper checks the active tree before loading, preserves completed-focus history during replacement, records `africa_continental_focus_tree_loaded` only after the new tree is active, and refreshes the layout once.
`africa_focus_route_ensure_continental_tree_loaded` is a compatibility wrapper around the canonical helper rather than a second implementation.
Priority packages keep their existing-tree safeguard and also preserve completed-focus history.
When South Africa's settlement transfers League custody to the saved exile patron, the old host is retained as the chain-local `africa_focus_completion_source`.
The canonical loader copies completed continental focuses from that source into the successor's tree while the separate RSA transfer continues to carry variables, flags, arrays, and relationship state.

## Interactions

- The relationship state machine remains the sole writer of the member relationship stage and its country arrays.
- Opinion is not an autonomy or integration input.
- The Action 102 priority-member promotion gate does not grant autonomy by itself.
- South Africa's Allied settlement restores its original Allied autonomy before any later voluntary Charter relationship is considered.
- The seven constitutional plans use different focus factors for representation, executive power, resources, command, withdrawal, crisis settlement, host limits, and route capstones.
- The support plan explicitly prioritizes voluntary diaspora citizenship, skills, capital, and local-consent focuses.

## Icons and UI

This mechanic adds no new icon or interface requirement.

The autonomy states use the standard subject interface with Event 12 localisation.
The strategy plans consume the icons already registered for the continental focus tree.

## Tuning

Autonomy values are file-scoped constants in `common/autonomous_states/012_africa_autonomy.txt` because the engine reads them only in that file.

AI plan weights are file-scoped constants in `common/ai_strategy_plans/012_africa_focus_plans.txt`.
Focus-local route and live-state behavior remains centralized in the existing Event 12 focus constants, triggers, and effects.

## Validation contract

- Both autonomy IDs must have one definition, one name, one description, one relationship transition, and one recognition trigger.
- Every focus key in the ten AI plans must exist in `africa_continental_focus_tree`.
- No autonomy state may allow automatic `can_take_level` or `can_lose_level` behavior.
- A member may enter either state only after the matching consent flags are present.
- A member leaving the Charter must not remain in an Event 12 subject state.
- A route plan must abort when its constitution or host identity is no longer current.

## Future plans

- Add route-specific subject-interface art only if the Event 12 asset matrix is expanded with exact sprite consumers and accepted filenames.
- Revisit autonomy transfer percentages after scenario balance evidence exists for small, medium, and large members.
- Add probability-tool scenario sweeps for focus-plan rank reversals once the current tool adapter can evaluate full national-focus plan context.
