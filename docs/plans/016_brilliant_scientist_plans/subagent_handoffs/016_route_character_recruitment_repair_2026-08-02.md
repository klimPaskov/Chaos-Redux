# Event 016 route-character recruitment repair

Date: 2026-08-02

Status: parent-owned repair complete; live formation and succession validation remain user-owned.

## Scope

The existing KRG command-staff handoff defines four route offices that must be recruited once before their advisor roles can be activated. A dirty working-tree change had removed those recruitment effects while leaving the permanent recruited flags and `activate_advisor` calls. The same change removed the recruitment call for the machine-route continuity character even though the helper immediately promotes that character.

## Changes

- Restored guarded `recruit_character` calls for `KRG_general_staff_office`, `KRG_machine_command_node`, `KRG_clone_officer_corps`, and `KRG_project_command_council` in `events/016_brilliant_scientist_kruger_state_events.txt`.
- Restored `recruit_character = KRG_continuity_network` before `promote_character` in `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`.
- Kept the separate reserved-DJX Kruger transfer contract in `common/scripted_effects/016_brilliant_scientist_effects.txt`; the dormant DJX history already recruits the fixed token, so opening appointment transfers its nationality to the selected host rather than creating a second token.
- Kept the corrected `train_equipment` gate in `common/decisions/016_brilliant_scientist_kruger_state_foundation_decisions.txt`.

## Evidence and validation

- `common/characters/016_brilliant_scientist_characters.txt` defines the four office characters and `KRG_continuity_network`; the route command handoff requires recruitment before advisor activation and promotion.
- Repository precedent uses guarded `recruit_character` followed by `activate_advisor` for fixed route offices, and the reserved-DJX pattern uses `set_nationality` for a globally held character.
- Static source review confirms every restored ID has a definition and every `recruit_character` call is guarded by the corresponding `has_character`/recruited flag path.
- No models, portraits, GFX, or new gameplay route were added.
- No Hearts of Iron IV process or live save was launched.

## Remaining risk

Live formation should confirm that the hidden event fires after each route selection, the matching advisor activates, repeated helper calls do not duplicate an office, and machine succession leaves the continuity network in charge.
