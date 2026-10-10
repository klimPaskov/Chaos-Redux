# Event 093: Treaty of Tordesillas Restoration

**Expanded specification, 2 October 2026, audited 10 October 2026.** The complete requested gameplay scope is developed in 18 sequential parts.
This is a design package, not an implementation or a release-readiness claim.
Installed-game verification, specialist audits, final audio research, and asset production belong to the implementation run.

Event identity: **093**, **Minor Fire-Once**, **Chaos level 1**, **Formables / Medium**.
Original catalog name: **Portugal wants land**.
Implementation status stays **To Be Reworked**.

Implementation plans and specialist handoffs belong under `docs/plans/093_treaty_of_tordesillas_restoration_plans/`.

## Read the design

Start with Part 01.
Read Parts 02-04 for the opening and its political memory, Parts 05-10 for expansion and the final campaign, and Parts 11-18 for interaction, country paths, AI, tuning, shared systems, production direction, achievements, and acceptance.
Part 14 is the canonical proposed numerical register.

| Part | Specification |
| --- | --- |
| 01 | [core design](093_treaty_of_tordesillas_restoration_spec_part_01_core.md) |
| 02 | [the Galicia crisis](093_treaty_of_tordesillas_restoration_spec_part_02_galicia_crisis.md) |
| 03 | [intervention in the Spanish Civil War](093_treaty_of_tordesillas_restoration_spec_part_03_spanish_civil_war.md) |
| 04 | [the Iberian relationship](093_treaty_of_tordesillas_restoration_spec_part_04_iberian_relationship.md) |
| 05 | [four evolutions](093_treaty_of_tordesillas_restoration_spec_part_05_evolutions.md) |
| 06 | [geography and the two spheres](093_treaty_of_tordesillas_restoration_spec_part_06_geographic_partition.md) |
| 07 | [regional integration](093_treaty_of_tordesillas_restoration_spec_part_07_regional_integration.md) |
| 08 | [faction, subjects, and expansion](093_treaty_of_tordesillas_restoration_spec_part_08_faction_and_empire.md) |
| 09 | [Two Crowns, One World](093_treaty_of_tordesillas_restoration_spec_part_09_world_end.md) |
| 10 | [the outside world](093_treaty_of_tordesillas_restoration_spec_part_10_outside_world.md) |
| 11 | [decisions, missions, and presentation](093_treaty_of_tordesillas_restoration_spec_part_11_decisions_and_missions.md) |
| 12 | [focus paths and country packages](093_treaty_of_tordesillas_restoration_spec_part_12_focus_and_country_paths.md) |
| 13 | [AI behavior and scenario matrix](093_treaty_of_tordesillas_restoration_spec_part_13_ai_behavior.md) |
| 14 | [balance and cost register](093_treaty_of_tordesillas_restoration_spec_part_14_balance_and_costs.md) |
| 15 | [connections and Chaos impact](093_treaty_of_tordesillas_restoration_spec_part_15_connections_and_chaos.md) |
| 16 | [visual assets and super-event direction](093_treaty_of_tordesillas_restoration_spec_part_16_visuals_and_super_event.md) |
| 17 | [achievements and writing direction](093_treaty_of_tordesillas_restoration_spec_part_17_achievements_and_localisation.md) |
| 18 | [continuity and acceptance](093_treaty_of_tordesillas_restoration_spec_part_18_lifecycle_and_acceptance.md) |

## Main design commitments

Galicia remains a complete opening crisis.
Real Portuguese aid can earn a postwar transfer, while victory, defeat, and betrayal have different consequences.
The two countries must resolve their relationship before restoring the treaty.
The global partition uses actual geography and a disclosed modern game convention, with fixed homeland protection and Galicia as a special settlement.

Regional coring works through coherent projects.
The two powers keep their identities, their meaningful country trees, and separate spheres.
Restitution respects ownership and consent.
The final campaign requires both crowns to demonstrate conquest and integration, and gives the remaining world genuine resistance and negotiation paths.

## Production handoffs

The six prompts are separate implementation handoffs.
The goal prompt is bounded to 4,000 characters including its final newline.

[Coding](093_treaty_of_tordesillas_restoration_coding_prompt.md)  
[Asset](093_treaty_of_tordesillas_restoration_asset_prompt.md)  
[Super Event](093_treaty_of_tordesillas_restoration_super_event_prompt.md)  
[Achievement](093_treaty_of_tordesillas_restoration_achievement_prompt.md)  
[Decision Mission](093_treaty_of_tordesillas_restoration_decision_mission_prompt.md)  
[Goal](093_treaty_of_tordesillas_restoration_goal_prompt.md)  

## Evidence and scope reports

[Source authority, research, and design decisions](093_treaty_of_tordesillas_restoration_source_and_decision_register.md)  
[Original reading coverage and missing references](093_treaty_of_tordesillas_restoration_reading_report.md)  
[Bounded inspection of the old implementation](093_treaty_of_tordesillas_restoration_repository_evidence.md)  
[Every user requirement and its design status](093_treaty_of_tordesillas_restoration_requirement_coverage.md)  
[Synthetic design tests and what they do not cover](093_treaty_of_tordesillas_restoration_validation_report.md)  
[Readable campaign and focus-path sketch](093_treaty_of_tordesillas_restoration_route_map.md)  
[Preserved original instructions](093_treaty_of_tordesillas_restoration_original_user_brief.md)  

The [machine-readable source manifest](093_treaty_of_tordesillas_restoration_source_manifest.json) records the 46 supplied text files read on 2 October 2026.
The [package inventory](093_treaty_of_tordesillas_restoration_package_inventory.json) lists the current files and hashes.

## Open questions

- **World-end and super-event identities.** The [shared identifier registry](../shared_identifier_registry.md) reserves no `world_end_scenario_id` or super-event presentation slot for Two Crowns, One World.
  Orchestrator decision, 10 October 2026: reserve both when Event 093 is implemented; Part 09 and the super-event prompt depend on them.
- **Catalog row.** The event catalog still describes the Galicia-only event without evolutions or a cluster; the Formables Medium membership and four evolution names wait for the workbook workflow.

## Revision log

### 2026-10-10 spec audit

Basis: 10 Oct 2026 spec audit under the user's planning-package brief.

- Aid contracts ship in quarter-package installments through one action instead of free-form deliveries with a 10 percent minimum; native volunteers serving 90 days add a fixed 10 points of Aid Fulfillment; intelligence and recognition earn no contract credit but make a recipient more willing to sign (Parts 03, 11, 14).
- Regional integration uses per-state thresholds only (the regional average and its 5-point drift rule are gone) and two confirmation choices: negotiated or coercive settlement, and ordinary or concentrated pace; a concentrated project that pauses reverts to ordinary pace (Parts 07, 11, 14).
- Connected integration to the humanitarian owners (owner seams accepted by the orchestrator on 10 October 2026 for their implementers): a coercive settlement sends a persecution displacement request to migration, famine pauses projects and food requisition makes them coercive, and Condemnation Tier 3 closes negotiated settlements, strains the compact, and from Tier 4 makes subordination offers fail (Parts 02, 04, 07, 09, 10, 13, 15, 18).
- The world-threat source is registered only while Two Crowns, One World is active (Part 15).
- Each public value's tooltip shows its current value, next gate and limiting cause only (Part 01).
- Deleted the role execution map, the main-agent review and the package-check JSON: historical process evidence whose corrections are already in the parts; the validation report is condensed to the synthetic suite, and the inventory is regenerated.
- Replaced Codex-specific spawning and `AGENTS.md` instructions in the prompts with `chaos-redux-subagents` routing and `.claude/skills/` paths; agents no longer run live tests; removed repeated planning-environment disclaimers from the parts.
- Reflowed the design files and prompts to one sentence per line.
- Part 15 links the Event 097 Collaboration contract for collaboration governments in the two spheres.
