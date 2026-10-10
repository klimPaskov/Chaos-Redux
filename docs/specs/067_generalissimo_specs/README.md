# Event 067 Generalissimo Specification Pack

## Package identity

- Event ID: `067`
- Event slug: `generalissimo`
- Event name: Generalissimo
- Intended repository location: `docs/specs/067_generalissimo_specs/`
- Primary source: the supplied rough specification recorded in `quality/067_generalissimo_source_reading_manifest.md`
- Event type: Minor Fire-Once
- Minimum Chaos level: 1
- Accepted cluster: Military Preparation
- Accepted cluster role: High member
- Manual scenario: Generalissimo's Coup
- Reserved scenario ID: `SCN-024`, raw integer `24`
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

Generalissimo's Coup is reserved as `SCN-024`, raw integer `24`, by the [shared identifier registry](../shared_identifier_registry.md) under the user's 7 October 2026 allocation instruction.
The original `SCN-015` proposal is superseded because Missile Age occupies that slot.
This reserves the identifier without approving broader design, registering gameplay or updating the workbook.

### Catalog mismatch

The accepted source assigns Event 067 to Military Preparation as a High member. The supplied event export leaves both cluster fields blank, and the supplied cluster export does not contain a Military Preparation row. The specification follows the accepted source. The workbook and runtime cluster registry must be aligned during implementation.

## Acceptance and current workflow

The source-reading and parent-review records describe the original planning run.
They record a supplied rough brief as accepted, but the package does not retain an independent acceptance record for every expansion.
Preserve the design while keeping unattributed expansion claims unresolved until the parent records adoption within the authorized scope.
Use [AGENTS.md](../../../AGENTS.md) and [the current subagent skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md) for workflow, ownership and capability discovery.
Runtime event IDs use `chaosx.nr67.*` and filenames retain `067`.

## Original planning reading and process status

The source reading manifest records the original inputs; no independent improvement-loop subagent ran during planning, and the parent-authored review in `quality/` stands in for it.

## Changelog

### 2026-10-10 spec audit

- Concessions are demand outcomes only. The ten concession packages already formed the demand pool, so keeping them as standing decisions as well gave each concession two entry points and roughly doubled the category; the government's own initiative stays in command-use and counterweight decisions.
- The README drops the obsolete zip-extraction instructions and the original environment's connector failures, which the quality records keep. Subagent instructions use the Claude-first wording.
