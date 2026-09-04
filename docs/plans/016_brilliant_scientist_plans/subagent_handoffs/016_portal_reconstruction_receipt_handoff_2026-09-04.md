# Event 016 Portal reconstruction receipt handoff

Status: owner-reviewed source correction on 2026-09-04.

## Changed contract

`brilliant_scientist_portal_raid_establish_beachhead` initializes the scope-less temporary result `brilliant_scientist_portal_reconstruction_committed` to zero and raises it only after the selected breach province changes controller and the locked six-battalion Quantum Transit Raiders cadre is created there.

Each native Portal raid success and critical-success `division_effects` block destroys the assigned source formation only when that result is positive.

This closes the target-race failure in which the source unit could be destroyed after the selected target became invalid and no replacement was created.

## Conservation boundary

The transaction conserves one deployed formation and the locked template's six-battalion baseline manpower and equipment budget.

The native raid remains the sole owner of its separate sixty-unit Teleportation Equipment reservation, outcome settlement, and target cooldown.

The reconstructed cadre does not claim to preserve the assigned division's damage, experience, temporary modifiers, commander context, or battalion-level reinforcement state.

The documented `teleport_armies` effect is state scoped and moves every qualifying army in the origin state; it does not expose the raid-selected division as a safe isolated source.

Using it here would therefore permit unrelated formations to transit with the raider and would violate the bounded one-formation contract.

## Files

- `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`
- `common/raids/016_brilliant_scientist_portal_raids.txt`
- `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.md`
- `docs/events/016_brilliant_scientist/systems/custom_technology_api.md`
- `docs/events/016_brilliant_scientist/systems/portal_raider_api.md`

## Remaining acceptance boundary

Repository evidence confirms that the source formation cannot be destroyed without a committed replacement under the scripted effect contract.

User-owned live acceptance remains responsible for confirming the native raid engine preserves the scope-less result through the outcome's `division_effects` callback exactly as documented.
