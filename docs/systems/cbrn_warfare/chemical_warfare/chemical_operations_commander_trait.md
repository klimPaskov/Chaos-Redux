# Chemical Operations Commander Trait

## Current source contract

`chemical_operations_commander` is a service-earned corps-commander trait in `common/unit_leader/chaosx_traits.txt`. It is credited to the named leader after two qualifying, fully completed CBRN Headquarters operations, under `common/script_constants/cbrn_commander_progression_constants.txt` and the character-scoped effects and triggers in `common/scripted_effects/cbrn_commander_progression_effects.txt` and `common/scripted_triggers/cbrn_commander_progression_triggers.txt`. Decontamination Corridor is the qualifying chemical-operation code; two successfully supplied completions earn the service trait. The completion callback runs after the final successful paid upkeep while the operation and leader still match, then refreshes earned traits. A random new-leader or level-up roll is not part of this path.

The trait is the source for a native CBRN High Command advisor role at specialist, expert, or genius rank through `common/country_leader/cbrn_high_command_traits.txt`. Current source sets `gain_xp = { always = no }` and a static cost of 1000 for the earned-trait definition; it does not use the earlier 500-cost manual assignment promise. The Chemical Operations Academy spirit grants +3% army experience gain through `common/ideas/cbw_spirits.txt` and does not grant the trait. The two systems can coexist without making academy selection a service substitute.

## Retired ability and bonus claims

The four `chemical_<agent>_attack` cylinder ability IDs in `common/abilities/chemical_abilities.txt` remain inert compatibility definitions with `allowed = { always = no }`. The trait does not unlock them. Active chemical release uses the exact-target native CBRN raid and operation adapters. The current trait definition contains no direct +20% Livens or agent-tank support-company modifiers, and the eighteen agent-specific tank companies are inactive compatibility definitions under the consolidated unit design.

The earlier historical candidate review considered Soviet, Japanese, Italian, Spanish, French, Canadian, British, German, and American commanders as research provenance. A search of current `history/countries/` found no `chemical_operations_commander` preassignment, so those names are not a current starting-roster claim. Any historically preassigned commander or new trait icon requires separate source and asset evidence before this guide can present it as active.

## Evidence limits and future depth

The source checks above establish definitions and callback wiring, not live-game award timing, advisor visibility, or player-facing presentation. The parent owns final integration and the user owns live consumer validation. Future expansion could add a distinct earned specialization only after its service trigger, effect budget, localisation, and visual consumer are approved.
