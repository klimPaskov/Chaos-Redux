# Random Weaponized Zombie Command

## Overview

This adds a hidden debug command that instantly completes the `Weaponize the Zombies` special project with a fully random profile.

It does not use a fake shortcut outcome. It rolls the same project attributes the normal chain uses and then resolves the final result through the existing completion logic.

The command is intentionally safe:

- it never rolls the forbidden branch
- it never resolves into a Wendigo failure result
- it never resolves into the human-friendly deployment profiles that require zombie-controlled target states
- it always ends in a valid deployable weaponized-zombie raid outcome

## Usage

Run the hidden event on the target country:

```txt
event chaosx.weaponized_zombies.10 GER
```

Replace `GER` with any country tag.

## What It Does

1. Resets the current weaponized-zombie project tracking state for the target country.
2. Randomly selects the normal profile steps:
	- nature
	- life state
	- resources
	- strength
	- infectiousness
	- speed
	- durability
	- cure resistance
	- friendliness
	- field testing conduct or skip
3. Always uses the normal refinement path rather than the forbidden branch.
4. Sanitizes any randomly rolled profile that would otherwise trip the guaranteed Wendigo failure condition.
5. Marks the special project complete.
6. Runs the normal completion resolver for a standard successful weaponized-zombie unlock.

## Notes

- The command works even if no zombie outbreak currently exists.
- If used on a country that already completed the project, it rerolls the profile and refreshes the completed result instead of stacking the initial stockpile again.
- Field tests are still real field tests. If the random roll chooses to conduct them, the usual field-test side effects and outbreak risks still apply.

## Files Touched

- `events/zombie_weaponized_special_projects.txt`
- `common/scripted_effects/zombie_special_project_effects.txt`
- `common/special_projects/projects/zombie_weaponized_projects.txt`
- `common/script_constants/zombie_special_project_constants.txt`

## Icons

No new icons, sprites, or `.gfx` wiring are required for this command.
