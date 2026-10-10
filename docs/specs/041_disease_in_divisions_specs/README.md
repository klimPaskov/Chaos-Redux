# Event 41: Disease in Divisions specification pack

This folder is the source design package for Event 41, Disease in Divisions.

The event remains a Chaos level 1 Minor Repeatable event and a Low member of the Diseases cluster. Its baseline is a contained military epidemic in one ordinary country at war. The player manages one public value, Army Infection Pressure, while a hidden simulation tracks affected formations, exposure conditions, recovery, deaths, and transmission routes.

## Package map

### Specifications

- `specs/041_disease_in_divisions_spec_part_1_core.md` defines the incident, targeting, opening, visible pressure model, military effects, and player promise.
- `specs/041_disease_in_divisions_spec_part_2_simulation_and_balance.md` defines hidden disease profiles, bounded spread, real manpower accounting, recovery, mortality, repeatability, and tuning targets.
- `specs/041_disease_in_divisions_spec_part_3_decisions_and_resolution.md` defines the temporary decision category, response actions, operational tradeoffs, target mission, resolution, and aftermath.
- `specs/041_disease_in_divisions_spec_part_4_evolutions_and_international_spread.md` defines Camp Fever Across the Trenches, War Plague, active-event entry, pre-fire evolved openings, cross-border transmission, and civilian handoff.
- `specs/041_disease_in_divisions_spec_part_5_connections_cluster_and_presentation.md` defines cross-event integration, Diseases cluster behavior, event reports, Event Details, Event Logs, multiplayer presentation, and writing direction.
- `specs/041_disease_in_divisions_spec_part_6_ai_achievements_and_replay.md` defines AI doctrine, strategic choices, achievements, rare combinations, and replay value.

### Quality and implementation evidence plans

- `quality/041_disease_in_divisions_chaos_impact_map.md` maps every event-owned Chaos gain and reversal and prevents overlap with shared deaths and contamination sources.
- `quality/041_disease_in_divisions_ai_probability_scenarios.md` provides named probability-audit scenarios and expected AI action orderings.
- `quality/041_disease_in_divisions_acceptance_criteria.md` provides the full design acceptance contract.
- `quality/041_disease_in_divisions_catalog_alignment.md` records the required workbook and cluster corrections.
- `quality/041_disease_in_divisions_improvement_loop_closure.md` records the final depth and anti-bloat review.
- `quality/041_disease_in_divisions_source_audit.md` records the supplied project files, skills, catalogs, and subagent definitions used for this planning pass.

### Research and diagrams

- `research/041_disease_in_divisions_historical_medical_research.md` turns historical military medicine into design anchors.
- `research/041_disease_in_divisions_bibliography.md` records the research sources and how each source supports the design.
- `diagrams/041_disease_in_divisions_lifecycle.md` maps the incident lifecycle.
- `diagrams/041_disease_in_divisions_decision_state_map.md` maps visible actions by pressure and evolution state.

### Prompts and handoffs

- `prompts/041_disease_in_divisions_asset_prompt.md`
- `prompts/041_disease_in_divisions_achievement_prompt.md`
- `prompts/041_disease_in_divisions_decision_mission_prompt.md`
- `prompts/041_disease_in_divisions_coding_prompt.md`
- `prompts/041_disease_in_divisions_goal_prompt.md`
- `handoffs/041_disease_in_divisions_subagent_routing.md`

## Design summary and acceptance

The imported package preserves the disease design and historical source review.
Its accepted labels do not cite independent approval for each expansion; missing claim-specific acceptance remains `unresolved` under the [repository acceptance rules](../../../CLAUDE.md#specs-and-plans).
Current [owner skills](../../../.claude/skills/chaos-redux-subagents/SKILL.md) govern implementation workflow over duplicated package instructions.

The opening infects a bounded group of frontline formations. The event never deletes equipment because soldiers become sick. Affected formations lose effective manpower, organization, recovery, reinforcement capacity, and combat power. Recoverable sick soldiers enter a temporary convalescent ledger and return gradually. Fatal cases are registered once as military casualties in the shared Deaths system.

The hidden simulation uses three adaptable profiles. Camp-borne disease responds strongly to crowding, hygiene, shared camps, and cold exposure. Enteric disease responds strongly to damaged supply, unsafe water, ruined infrastructure, and heat. Tropical and vector-borne disease responds strongly to warm wet climates, marshes, jungle, insects, poor prophylaxis, and long exposure. The player sees symptoms and response advice, not three additional meters.

The baseline can be contained in one country. Evolution I allows rapid movement through military networks and sustained contact across fronts. Evolution II permits civilian spillover and distant theater transmission. Civilian cases enter the existing biological outbreak and humanitarian systems through a bounded adapter. Event 41 does not create a second civilian disease system.

The presentation uses an ordinary temporary decision category with one strong static category picture, the pressure stage and trend as status text, map highlighting, division status, and decision tooltips. A dedicated scripted mechanic window would add little value to this low-severity event.

The runtime slot `events/041_disease_in_divisions.txt` still holds the legacy stub; no part of this package is implemented.

## Open questions

- The workbook row still carries Event 42's skyfall premise as its details; the catalog owner should apply `quality/041_disease_in_divisions_catalog_alignment.md` when the event is implemented.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:
- Resolved the unresolved picture-plus-meter conflict by design: the category keeps its static picture and shows Army Infection Pressure as stage text with a trend word, which the event skill permits (Parts 1, 3, 5 and the decision prompt).
- Recorded that the workbook already lists Event 41 as the Low Diseases member, so only the wrong details text remains a catalog defect.
- Replaced `AGENTS.md`, `.agents` links, and Codex `fork_turns` wording with the current Claude-first equivalents.

Pass 2, design improvement:
- Consolidated the response menu from 21 actions to 14 by merging true duplicates: Assign Medical Evacuation Priority and Repair the Medical Corridor became Open the Medical Corridor; Emergency Medical Mobilization became the once-per-episode emergency scale of Expand Field Hospitals; Inspect Allied Formations folded into Exchange Field Medical Reports; Separate Coalition Camps folded into Establish Quarantine Camps; Restrict Allied Access folded into Restrict Military Access; and Close Military Ports, Protect Civilian Transport Hubs, and the duplicate War Plague district isolation became the War Plague scope of Isolate the Military District.
  Each merged pair repeated the same cost and the same effect under two names in different phases.
