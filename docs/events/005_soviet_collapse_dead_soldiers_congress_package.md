# Event 005 Dead Soldiers' Congress Package

Audit date: 2026-05-21

## Overview

The Dead Soldiers' Congress (`DSC`) is a high-chaos Soviet Collapse successor for the veteran and revenant military-memory state requirement. It appears when Soviet military obedience has fallen below contested authority, deep collapse pressure exists, and the USSR still owns and controls Stalingrad (`217`) and Voronezh/Borisoglbsk (`260`).

## Gameplay Flow

`can_soviet_collapse_spawn_dsc` gates the package behind the high-chaos successor spawn checks, the collapse threat gate, and the state-control requirements. `soviet_collapse_spawn_dsc_if_enabled` transfers states `217` and `260`, cores them for `DSC`, applies Soviet pressure consequences, and calls `soviet_collapse_setup_dsc_successor`.

The setup effect marks `DSC` as a high-chaos successor, sets Stalingrad as the capital, runs the shared breakaway setup, loads `DSC_soviet_collapse_focus_tree`, initializes roll-call legitimacy and revenant mobilization variables, applies starting ideas, records the high-chaos evolution log stage, and fires `chaosx.nr5_custom.41`.

## Focus And Decision Content

The `DSC_soviet_collapse_focus_tree` has 18 focuses with political, industry, military, diplomacy, expansion, and endgame branches. The tree splits between witness-officer settlement and revenant-staff hardline routes, then converges into veteran-town diplomacy, dead-regiment columns, soldiers-road claims, and settlement or dead-army endgames.

The `soviet_collapse_dead_soldiers_congress` decision category gives `DSC` three recurring or route-closing tools:

- `dsc_verify_the_roll_call`
- `dsc_raise_dead_regiment_columns`
- `dsc_convene_the_dead_army`

The witness-officer cleanup hides the raw `remove_ideas` line behind `dsc_witness_officers_settle_grave_regiments_tt`.

## Icons And Assets

Required asset wiring:

- Flags: `gfx/flags/DSC.tga`, ideology variants, `medium/`, and `small/`.
- Leader portrait: `gfx/leaders/005_soviet_collapse/DSC_leader.dds`, sprite `GFX_portrait_DSC_congress_of_dead_regiments`.
- Focus icon package: `gfx/interface/goals/soviet_collapse/005_dsc_custom_splinter_focus.dds`, sprites `GFX_focus_DSC_*` and `GFX_focus_DSC_*_shine`.
- Idea icon package: `gfx/interface/ideas/soviet_collapse/005_dsc_custom_splinter_idea.dds`, sprites `GFX_idea_dsc_*`.
- Decision icon package: `gfx/interface/decisions/soviet_collapse/005_dsc_custom_splinter_decision.dds`, sprites `GFX_decision_dsc_*`.

The current DDS files are wired and present. The package still uses one generated tag emblem across the DSC focus tree, so distinct final per-focus art remains pending if final acceptance requires unique rendered art rather than unique sprite assignments that share one source texture.

## Validation Notes

Source validation for this package covers tag registration, country/history files, country localisation, setup/spawn effects, event-log stage mapping, custom event `chaosx.nr5_custom.41`, decision category and decisions, ideas, focus IDs, focus rewards, AI weights, localisation, sprite keys, and asset existence.

## Future Plans

- Replace the shared DSC focus-emblem texture with distinct final focus icons for each focus identity.
- Add late-game border settlement events for the soldiers' road claims if the broader Event 005 high-chaos pass expands dead-state diplomacy.
- Consider a shared dead-state interaction between `ICD`, `RMC`, and `DSC` once all death-state packages have final art and route audits.
