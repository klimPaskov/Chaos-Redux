# Event 26 achievement implementation prompt

Implement one Chaos Redux achievement for Event 26 using the working ID `026_black_friday_five_departments`. Read `AGENTS.md`, the Event 26 specs, the achievement rules in `chaos-redux-event-planning`, the event and decision skills, and the current Chaos Redux achievement registry before editing.

## Unlock contract

During one naturally selected Black Friday sale, one human-controlled country must complete paid actions from five distinct registered cost-surface families before the sale expires.

The credited families must include:

- at least one institutional family, such as law, personnel, officer role, or intelligence
- at least one material or commitment family, such as equipment, fuel, convoys, trains, factories, or dockyards
- at least one action whose paid resource is not political power

A transaction counts only when its ordinary current cost was positive, its discounted payment was positive, and the action committed successfully. Repeating one family does not add progress. Each logical transaction credits at most one registry-defined primary family, even when the action pays several resource types.

## Disqualifiers

Do not unlock when Event 26 was started through Force Trigger Mode, ordinary manual settings launch, debug setup, or a triggerable substitute. Do not count AI transactions, free actions, refunded actions, failed transactions, or payments after expiry.

## Tracking

Track progress per human country for the active sale. Credit a family after final successful commitment. Store enough family state to prevent duplicate credit. Clear temporary progress after expiry. Award immediately when the fifth valid family completes and all composition requirements are satisfied.

Use the same family IDs as the final cost surface registry. Do not create a second achievement-only classification system.

## Full achievement surface

Implement:

- registry entry in `common/achievements/chaos_redux_achievements.txt`
- tracking flags, arrays, or variables
- unlock trigger
- disqualifiers
- cleanup
- final player-facing name and description
- debug or audit visibility where current achievement precedent requires it
- normal, grey, and not-eligible icon wiring from the asset handoff
- Event 26 documentation and catalog-facing achievement note where the project records achievements

The description must explain five different purchase types during one natural Black Friday and mention the institutional and material requirements. Do not expose internal family IDs.

## Validation

Test successful unlock, repeated-family rejection, missing non-political resource rejection, force-trigger rejection, manual-launch rejection, refund rejection, AI rejection, expiry cleanup, save and reload, and one valid completion at both 50 percent and 75 percent sale strength.

Report every file changed, final IDs, localisation keys, asset paths, tracking state, validation result, and blocker. Do not mark the achievement complete while the cost family registry or asset triplet is incomplete.
