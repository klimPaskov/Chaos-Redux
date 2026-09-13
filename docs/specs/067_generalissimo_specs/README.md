# Event 067 Generalissimo Specification Pack

## Package identity

- Event ID: `067`
- Event slug: `generalissimo`
- Event name: Generalissimo
- Intended repository location: `docs/specs/067_generalissimo_specs/`
- Primary source: the accepted Event 067 rough specification supplied with this task
- Event type: Minor Fire-Once
- Minimum Chaos level: 1
- Accepted cluster: Military Preparation
- Accepted cluster role: High member
- Manual scenario: Generalissimo's Coup
- Proposed scenario ID: `SCN-015`
- Public world-end branch: The Generalissimos' World

## Purpose

This package turns Event 067 into a complete Chaos Redux design handoff. It preserves the central promise that the Generalissimo is the strongest ordinary military commander a country can receive and that keeping him is a rational choice. His danger comes from the power granted through real military use, public success, officer loyalty, institutional concessions, and control of the armed forces.

The event is designed around one public crisis value, Generalissimo Influence. Hidden values may model officer loyalty, coercive reach, industrial penetration, command authority, public prestige, and regional command support, but the player is never asked to manage a ledger of separate numbers.

The design supports four broad outcomes:

1. The government keeps the Generalissimo as a powerful commander while containing his influence.
2. The government removes him permanently before he can challenge the state.
3. The government submits and transfers power without a civil war.
4. A failed removal or rejected ultimatum creates the Generalissimo's military junta and an immediate civil war.

A victorious junta receives a full host-adaptive focus tree, route-specific decisions, a military government package, foreign-policy paths, and permanent use of the Generalissimo as ruler and commander. The world-end branch turns military rule into an international struggle between aligned juntas, rival officer regimes, civilian governments, and resistance movements.

## Specification files

- `specs/067_generalissimo_spec_part_1_core.md`
- `specs/067_generalissimo_spec_part_2_character_and_influence.md`
- `specs/067_generalissimo_spec_part_3_decisions_and_removal.md`
- `specs/067_generalissimo_spec_part_4_revolt_and_country_package.md`
- `specs/067_generalissimo_spec_part_5_focus_tree.md`
- `specs/067_generalissimo_spec_part_6_scenario_and_world_end.md`
- `specs/067_generalissimo_spec_part_7_integrations_ai_chaos.md`
- `specs/067_generalissimo_spec_part_8_presentation_assets_localisation.md`
- `specs/067_generalissimo_spec_part_9_acceptance_and_limits.md`

## Implementation prompt files

- `prompts/067_generalissimo_asset_prompt.md`
- `prompts/067_generalissimo_super_event_prompt.md`
- `prompts/067_generalissimo_achievement_prompt.md`
- `prompts/067_generalissimo_decision_mission_prompt.md`
- `prompts/067_generalissimo_focus_tree_prompt.md`
- `prompts/067_generalissimo_scripted_system_prompt.md`
- `prompts/067_generalissimo_coding_prompt.md`
- `prompts/067_generalissimo_goal_prompt.md`

## Research and diagrams

- `research/067_generalissimo_research_notes.md`
- `research/067_generalissimo_bibliography.md`
- `diagrams/067_generalissimo_state_machine.md`

## Handoffs and quality records

- `handoffs/067_generalissimo_catalog_alignment_handoff.md`
- `handoffs/067_generalissimo_probability_scenario_matrix.md`
- `handoffs/067_generalissimo_implementation_surface_map.md`
- `handoffs/067_generalissimo_subagent_routing_matrix.md`
- `quality/067_generalissimo_source_reading_manifest.md`
- `quality/067_generalissimo_parent_improvement_review.md`
- `quality/067_generalissimo_completion_report.md`

## Main design decisions

### One canonical Generalissimo

The normal event creates one fictional male character identified publicly by the title Generalissimo. The character uses one stable token across commander, field marshal, and country-leader roles. The implementation must never create separate clones for those roles.

If the engine cannot expose two commander roster entries for one character, the intended behavior is one field marshal-rank army leader with every applicable general and field marshal trait, full direct command use, and the maximum supported command capacity. This preserves the accepted design without duplicating the character.

### No fixed junta tag by default

The civil-war junta should use the engine's dynamic civil-war country creation where that route can preserve the host country's territory, cores, technology, equipment identity, and name. The new side is identified through event-owned flags and receives the dedicated focus tree and regime package.

A fixed country tag is prohibited unless engine inspection proves that a required surface cannot be supported with a dynamic civil-war country. Any fixed tag would require the full collision audit against vanilla, Chaos Redux, installed Workshop mods, and other local mods before it can be reserved.

### One visible crisis value

Generalissimo Influence is the only persistent event-specific value shown during the pre-coup crisis. The event may track hidden components for calculation and AI behavior. Those hidden components must feed the public influence total, visible status, action chances, or qualitative tooltips instead of becoming extra counters.

After a successful takeover, Generalissimo Influence closes. The junta uses Command Cohesion as its single visible government value. The two values never require simultaneous management.

### Ordinary decision category with a compact display

The crisis uses an ordinary decision category with a compact influence display and changing category pictures. It does not need a separate full-screen scripted GUI. The junta focus tree may use a small read-only focus inlay that shows the Generalissimo, the current regime structure, Command Cohesion, and the next important route condition.

### No custom unit or 3D model

The event is about command, loyalty, and military government. It uses existing divisions, equipment, naval assets, air wings, commanders, and host templates. No new unit family, custom counter, unit audio package, or 3D model is required.

### Scenario ID status

`SCN-015` is the required proposed ID because the supplied scenario export reaches `SCN-014`. The implementation must confirm that `SCN-015` is free in the authoritative workbook and runtime registry. A collision blocks registration until the source-of-truth ID is reconciled.

### Catalog mismatch

The accepted source assigns Event 067 to Military Preparation as a High member. The supplied event export leaves both cluster fields blank, and the supplied cluster export does not contain a Military Preparation row. The specification follows the accepted source. The workbook and runtime cluster registry must be aligned during implementation.

## Reading and process status

Every supplied project source file, every extracted subagent definition, and all three supplied catalog CSV exports were read in full. The source reading manifest records their sizes, line counts, and hashes.

The active environment did not expose a working custom-subagent invocation route. Two discovery attempts through the Codex Native connector failed with HTTP 429 and HTTP 404 responses. The specification therefore includes a parent-authored improvement review and complete prompts for the required subagents. It does not claim that an independent improvement-loop subagent completed a review.

## Extraction

Extract `067_generalissimo_specs.zip` into `docs/specs/`. The resulting repository path should be:

```text
docs/specs/067_generalissimo_specs/
```
