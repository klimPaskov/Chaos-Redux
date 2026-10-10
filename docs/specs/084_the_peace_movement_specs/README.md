# Event 84 · The Peace Movement

## Planning and implementation-handoff package

This package expands the user's Event 84 concept into a complete campaign design, from the first counterculture circles through negotiated reform, government change, international polarization, armed defense, and The Gay World.
It also defines the mature War for the Soul manual scenario.

## Status

| Surface | Status and basis |
|---|---|
| User decisions | The [original brief](084_the_peace_movement_original_brief.md): identity, two public values, the five responses, the eight character states, three evolutions at 200/400/600 Chaos, four formations, both Internationals, civil wars, The Gay World requirements, and the War for the Soul setup list |
| Accepted design | The authored expansion delivered on 22 September 2026, the 8 October 2026 cross-event connections, and the 10 October 2026 spec audit under the user's planning-package brief (see the revision log) |
| Implementation | Not implemented. `events/084_pp.txt` still holds the legacy hidden dispatcher and global +100 Political Power event, and the catalog row still reads "PP", Minor Repeatable |
| Numeric tuning | Authored proposals; balance evidence is an implementation deliverable |
| Identifiers | War for the Soul holds the reservation `SCN-031`, raw ID `31`, in the [shared identifier registry](../shared_identifier_registry.md); design IDs in this package are not engine IDs |

Start an implementation task with the [coding prompt](084_the_peace_movement_coding_prompt.md) or the compact [goal prompt](084_the_peace_movement_goal_prompt.md), and only under an assignment that accepts the relevant design.

## Main specification

| Part | Coverage |
|---|---|
| [1](084_the_peace_movement_spec_part_1_core.md) | Core experience and campaign structure |
| [2](084_the_peace_movement_spec_part_2_influence_and_reaction.md) | Influence, Reaction, national effects, and demographic policy |
| [3](084_the_peace_movement_spec_part_3_government_responses.md) | Government responses and playable commitments |
| [4](084_the_peace_movement_spec_part_4_characters_and_culture.md) | Culture, characters, private life, and public consequences |
| [5](084_the_peace_movement_spec_part_5_spread_and_evolutions.md) | International spread and Chaos evolutions |
| [6](084_the_peace_movement_spec_part_6_governments_and_country_packages.md) | Government transfer, political identities, and country packages |
| [7](084_the_peace_movement_spec_part_7_focus_architecture.md) | Focus architecture and strategic progression |
| [8](084_the_peace_movement_spec_part_8_armed_peace_and_forces.md) | Armed Peace, formations, equipment, and force development |
| [9](084_the_peace_movement_spec_part_9_blocs_civil_wars_and_settlements.md) | International blocs, civil wars, and settlements |
| [10](084_the_peace_movement_spec_part_10_the_gay_world.md) | World-end scenario: The Gay World |
| [11](084_the_peace_movement_spec_part_11_war_for_the_soul.md) | Manual scenario: War for the Soul |
| [12](084_the_peace_movement_spec_part_12_shared_systems_and_chaos.md) | Shared systems, Chaos impact, and event connections |
| [13](084_the_peace_movement_spec_part_13_presentation_and_assets.md) | Presentation, narrative direction, and asset requirements |

## Supporting design

| File | Contents |
|---|---|
| [Modifier precedence](084_the_peace_movement_modifier_precedence.md) | The single calculation across three spirits, route and wartime recovery rules |
| [Decision and mission matrix](084_the_peace_movement_decision_and_mission_matrix.md) | 33 actions, 17 mission types, visible pages, costs, and full, partial, failure, and cancellation outcomes |
| [AI, probability, and technology matrix](084_the_peace_movement_ai_probability_and_technology_matrix.md) | Intended AI behavior, 32 named scenarios, and the technology and capability checks |
| [Achievement matrix](084_the_peace_movement_achievement_matrix.md) | 16 challenges with eligibility, disqualifiers, tracking, and 48 icon states |
| [Asset register](084_the_peace_movement_asset_register.md) | Report, news, and super-event scenes, spirit, focus, and decision icons, identities, portraits, counters, and sound |
| [3D model briefs](084_the_peace_movement_3d_model_briefs.md) | Four firearm units, separate body and gun workflow, skeletal actions, and counters |
| [Super-event research](084_the_peace_movement_super_event_research.md) | Four presentation briefs, checked sources, two quotation candidates, and open text and recording rights |
| [Acceptance scenarios](084_the_peace_movement_acceptance_scenarios.md) | 92 future implementation checks |

Provenance: the [source ledger](084_the_peace_movement_source_ledger.md) and [source manifest](084_the_peace_movement_source_manifest.json) record what the 22 September 2026 planning session read and could not read; they are historical receipts.

## Handoff prompts

| Prompt | Intended use |
|---|---|
| [Coding](084_the_peace_movement_coding_prompt.md) | Main implementation, specialist routing, and completion standard |
| [Assets](084_the_peace_movement_asset_prompt.md) | Visual, portrait, flag, model, counter, and sound production |
| [Super-events](084_the_peace_movement_super_event_prompt.md) | Final verified cultural text, licensed recordings, images, and playback |
| [Achievements](084_the_peace_movement_achievement_prompt.md) | All 16 definitions and their 48 icon states |
| [Decisions and missions](084_the_peace_movement_decision_mission_prompt.md) | Objective-driven domestic and international decisions |
| [Goal](084_the_peace_movement_goal_prompt.md) | Compact overall goal, kept under 4,000 characters |

## Design commitments

Influence and Reaction are independent and are the event's only two public meters.
Orientation is never a mechanical penalty; only an explicit population policy changes future growth.
Peaceful takeovers and conservative pluralist settlements remain viable.
The four special formations need Armed Peace and real material, while ordinary national forces handle earlier defensive emergencies.
Existing national trees remain meaningful, and new authorities need complete country packages.
No rule in the event depends on a fixed calendar date.

World-end activation uses strictly more than 1,000 Chaos and strictly more than 50% of living world population, counted once per controlled state, plus the brief's two political requirements and the shared enable and ownership gates.
Activation starts the final campaign; it does not award victory.
Manual intensity adds Chaos explicitly and never duplicates people, forces, or earned progress.

## Open questions and unresolved proposals

| Item | Disposition and reasoning |
|---|---|
| Share one body model between Commune Guards and Rainbow Militias | Unresolved proposal. The brief requires four distinct formations, which this package keeps; the four full custom models with six skeletal actions each are package-authored scope. Guards could reuse the militia body with their own equipment, emblem, counter, and animations tuned for a cautious stance, saving one complete model pass. It reduces asset scope, so it needs the user's approval |
| Final player-facing text, super-event quotations, and audio | Unresolved production inputs. Working labels are direction only; see [super-event research](084_the_peace_movement_super_event_research.md) |
| Licensed modern body and gun references for the four units | Unresolved production input required by the 3D owner skill before generation |
| Catalog correction (name, type, clusters, status) | Accepted and queued. Applied through the workbook owner and export at implementation, not edited here |

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.

- Removed mobilization speed from the Event 84 modifier set; it changed a number without a felt choice.
  Route recoveries that used it now recover War Support instead (Parts 2, 6, 8, modifier precedence).
- The Influence and Reaction tooltips show at most the three largest current causes and the next threshold; the full pressure table stays internal (Parts 2, 13).
- Folded seven click-through decisions into the events or missions that already own them: the four reform packages into the negotiation event, the population-policy choice into the family-policy congress, and settlement maintenance and world ratification into automatic missions.
  The matrix lists 33 actions; decision icons follow (decision matrix, asset register, prompts).
- Connected the movement to current shared systems: a CBRN strike on the country or its own condemnation at tier 3 feeds the war-burden Influence source; abusive repression submits persecution pressure to migration; asylum uses migration's passage and reception decisions; relief uses the current famine decisions; eradication arrests in a country running camps belong to the camp and condemnation owners (Parts 2, 9, 12).
- Retired process-only acceptance items QA88, QA89, QA95, and QA96 (tool runs and review gates, not game behavior); 92 scenarios remain.
- Replaced Codex-specific spawning instructions and mandatory-tool gates in every prompt and the AI matrix with the `chaos-redux-subagents` routing and the repository's MCP and completion rules; linked canonical `.claude/skills/` paths; agents no longer run live acceptance tests, which belong to the user.
- Cut repeated status disclaimers, planning-session narration, and duplicated asset and audio rules; Part 13 and the prompts now link to the asset register and 3D briefs as the canonical homes.
