# Event 007 Fury planning package

This package turns Event ID `7`, `Fury`, into a source specification pack for Chaos Redux.

Fury replaces the old expansionism placeholder with a dynamic repeatable war event. A small AI country is taken by a fast expansion system, receives an initial army and finite hidden reinforcement reserve capped at 100 scripted divisions per actor, attacks weaker eligible neighbors, absorbs territory through compliance and coring work, and either burns out or grows into a continental threat.

## Package map

| Path | Role |
| --- | --- |
| `specs/007_fury_spec_part_1_core.md` | Core event identity, eligibility, targeting, lifecycle, and player experience |
| `specs/007_fury_spec_part_2_evolutions_world_end.md` | Evolution tracks, super-event thresholds, world-end branch, defeat and cleanup |
| `specs/007_fury_focus_tree_spec.md` | Shared Fury focus tree architecture and branch standards |
| `specs/007_fury_decisions_missions_spec.md` | Fury decision category, missions, costs, AI behavior, and anti-Fury response hooks |
| `specs/007_fury_triggerable_scenario_spec.md` | Custom triggerable scenario named `The World in Fury` |
| `specs/007_fury_achievements_spec.md` | Achievement designs and tracking notes |
| `matrices/007_fury_country_package_matrix.md` | Dynamic country package for transformed minors |
| `matrices/007_fury_ai_balance_matrix.md` | AI, balance, pacing, exploit checks, and target scoring |
| `prompts/007_fury_asset_prompt.md` | Handoff prompt for visual assets |
| `prompts/007_fury_super_event_prompt.md` | Handoff prompt for super-event quote, remark, audio, and image research |
| `prompts/007_fury_achievement_prompt.md` | Handoff prompt for implementing and asseting achievements |
| `prompts/007_fury_decision_mission_prompt.md` | Handoff prompt for decision and mission implementation |
| `prompts/007_fury_coding_prompt.md` | Main implementation prompt |
| `prompts/007_fury_goal_prompt.md` | Compact `/goal` prompt under 4000 characters |
| `research/007_fury_research_notes.md` | Source notes and design constraints |
| `acceptance/007_fury_acceptance_criteria.md` | Pass or fail criteria for implementation |

## Core non-negotiables

- Fury is AI-selected only in random and triggerable setup.
- The player is never granted the Fury package by this event.
- Baseline target selection can choose AI or player-controlled countries when normal target gates allow it; player exclusion applies to Fury actor selection.
- Fury candidates are dynamic small mainland minors with few states and a valid land-neighbor target.
- Initial units, finite reserve-spawned reinforcements, coring, war declarations, target choice, and AI behavior scale dynamically. Reserve-spawned reinforcements draw slowly from the hidden reserve instead of appearing as instant or infinite weekly divisions.
- Baseline Fury fights one weaker neighbor at a time.
- Evolution II allows two Fury actors and cooperation mechanics.
- Evolution III allows three Fury actors and all-neighbor declarations.
- The custom triggerable scenario is named `The World in Fury`, has the normal four intensity stops, excludes the player, and has pact or hostile type choices.
- Maximum intensity creates up to sixteen dispersed Fury minors when enough eligible AI countries exist.
- A news event marks the first conquest.
- A super-event marks a Fury country becoming a major.
- A terminal world-end branch can spread Fury to other continents and bind new Fury countries to the main Fury faction.
