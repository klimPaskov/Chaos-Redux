# Event 099 Sandstorm specification package

## Package status and use

This package supplies the complete proposed rework specification and production handoff for **Sandstorm**, Event **099**.
It preserves **Minor Fire-Once**, **tier 1**, **Natural Disasters High membership**, and **To Be Reworked** status.
The written design covers all 78 atomized requirements from the current user brief.
Implementation and native validation remain subject to the explicit owner and engine gates.

The package is installed at `docs/specs/099_sandstorm_specs/`.
The original archive had one top-level folder, `099_sandstorm_specs/`.
Working plans and subagent handoffs belong separately under `docs/plans/099_sandstorm_plans/`.
The archive contains source specifications and original planning acceptance records, with every recorded review finding either incorporated or explicitly retained as an implementation gate.
The 2026-10-08 import authorizes documentation review only and does not accept unapproved tuning or authorize implementation.
The original source-reading ledger and package-verification JSON retain their original 2026-10-07 provenance and hashes rather than describing this edited checkout.
See [2026-10-08 import review](../../plans/099_sandstorm_plans/099_import_review_2026-10-08.md) for current changes and inventory, and [2026-10-08 import evidence](../../plans/099_sandstorm_plans/099_import_evidence_2026-10-08.json) for the parent's current source and MCP checks.
Presentation **120** is reserved for the proposed World of Dust milestone, and Natural Disasters uses cluster **5**, as recorded in the [shared identifier registry](../shared_identifier_registry.md).
Audio ID remains separately unassigned, and the package requires no triggerable-scenario, world-end or country-tag allocation.

Read the nine numbered creative parts in order, then the authority, evidence, contracts and execution maps before using a production prompt.
The numerical tuning and implementation shapes added by this plan are explicit proposals, not claims that those exact values came from the user or already work in HOI4.
All new action, mission, achievement, interface and asset labels are working directions.
Final player localisation, quotation selection, art and music remain production tasks governed by the separate prompts.

## The proposed experience

A huge connected wall begins inside one dynamically selected suitable major desert.
One authoritative moving footprint governs the visible front, forecast, military exposure, civilian risk and industrial consequences.
It crosses countries and coastlines, traverses sea, changes heading and speed, and varies in breadth, depth and local intensity.
The player can watch the approach, make costly preparations and see conditions clear behind the wall.

Both sides of a battle lose visibility, coordination, organization and effective movement or attack within the affected area.
Air operations suffer local detection, navigation, efficiency and accident consequences.
Civilian losses follow current residents, actual geographic exposure, duration and protection, with one measured population debit per aggregate interval.
Factories and supply suffer temporary disruption, while actual building and railway damage remains until repaired.

At 200+, The Great Dust Wall broadens and strengthens the front.
At 400+, Splinter Storms adds independent uneven branches.
At 600+, The Returning Storm permits genuine curved returns and finite desert reseeds.
At 800+, The World of Dust creates simultaneous major-desert fronts that can merge and cover much of the planet.
All stages retain the original season identity, conserved history, bounded creation and an immutable 360-day maximum.
Qualified recovery and achievement observations may finish their existing windows after the weather ends.

The proposed player-facing scope is exactly two persistent public values, five primary response families, three mission families and eight difficult achievements.
Existing mask, migration, famine, Air, cost and repair systems retain their own responsibilities.
The design does not add parallel shared ledgers merely to make Event 099 self-contained.

## Nine creative specification parts

| Part | File | Main contents |
| --- | --- | --- |
| 01 | [099_sandstorm_part_01_identity_and_campaign.md](099_sandstorm_part_01_identity_and_campaign.md) | Identity, campaign role, player loop, public information, narrative directions and complete scope |
| 02 | [099_sandstorm_part_02_fronts_and_forecasts.md](099_sandstorm_part_02_fronts_and_forecasts.md) | Dynamic deserts, broad opening, swept movement, intensity, ocean transit, forecasts, overlap and finite closure |
| 03 | [099_sandstorm_part_03_military_and_air.md](099_sandstorm_part_03_military_and_air.md) | Symmetric ground disruption, organization, supply, equipment, air operations, counterplay and locality proof |
| 04 | [099_sandstorm_part_04_civilians_industry_and_recovery.md](099_sandstorm_part_04_civilians_industry_and_recovery.md) | Current population, exposure, direct risk, protection, industrial effects, physical damage, repair and atmospheric overlaps |
| 05 | [099_sandstorm_part_05_responses_and_missions.md](099_sandstorm_part_05_responses_and_missions.md) | D1–D5 actions, full costs, preparation, effective durations, cancellation, authority, automation and M1–M3 missions |
| 06 | [099_sandstorm_part_06_evolutions.md](099_sandstorm_part_06_evolutions.md) | All four named stages, active and pre-fire entry, settings, physical manifestations, material, branches, returns and mergers |
| 07 | [099_sandstorm_part_07_shared_systems_chaos_and_ai.md](099_sandstorm_part_07_shared_systems_chaos_and_ai.md) | Cluster integration, shared owners, particulate admission, bounded Chaos receipts, AI and lifecycle integration |
| 08 | [099_sandstorm_part_08_presentation_and_asset_direction.md](099_sandstorm_part_08_presentation_and_asset_direction.md) | Main-map wall, forecasts, attached response UI, accessibility, scene and icon roster, real animation and super-event direction |
| 09 | [099_sandstorm_part_09_achievements_and_campaign_tests.md](099_sandstorm_part_09_achievements_and_campaign_tests.md) | Eight demanding outcome-backed achievements and combined campaign acceptance scenes |

## Evidence, contracts and review records

| File | Purpose |
| --- | --- |
| [099_sandstorm_source_authority.md](099_sandstorm_source_authority.md) | User authority, current-source conflicts, catalog reconciliation, complete reading method and precise evidence limits |
| [099_sandstorm_source_reading_ledger.json](099_sandstorm_source_reading_ledger.json) | Historical 2026-10-07 provenance: archive and source identities, reader ledgers, the 78-requirement register and pinned repository observations. Not required reading for implementation; the requirement coverage file carries the register that matters |
| [099_sandstorm_requirement_coverage.md](099_sandstorm_requirement_coverage.md) | Every user requirement linked to an exact design heading and meaningful future acceptance proof |
| [099_sandstorm_implementation_contracts.md](099_sandstorm_implementation_contracts.md) | Existing versus proposed APIs, geometry and interval authority, measured population, payment, repair, owner boundaries, persistence and aftermath retention |
| [099_sandstorm_research_and_evidence.md](099_sandstorm_research_and_evidence.md) | Primary WMO, WHO and NASA grounding, pinned repository observations and ten explicit release gates |
| [099_sandstorm_balance_scenarios.md](099_sandstorm_balance_scenarios.md) | Proposed civilian, residence, capacity, damage and payment arithmetic plus required probability scenarios |
| [099_sandstorm_balance_calculations.json](099_sandstorm_balance_calculations.json) | Machine-readable inputs and results for the illustrative planning calculations |
| [099_sandstorm_execution_maps.md](099_sandstorm_execution_maps.md) | Applied skill map, Subagent Usage Map, MCP Usage Map, immutable comparison evidence and implementation order |
| [099_sandstorm_review_dispositions.md](099_sandstorm_review_dispositions.md) | Accepted source, architecture, documentation and final improvement findings with closure status and remaining proof |
| [099_sandstorm_package_verification.json](099_sandstorm_package_verification.json) | Historical original-archive file identities and verification at 2026-10-07 15:35:37 UTC. It describes the archive, not this checkout, and needs no refresh |

## Six separate execution prompts

| Prompt | Intended task |
| --- | --- |
| [099_sandstorm_asset_prompt.md](099_sandstorm_asset_prompt.md) | Full scene, icon, map-consumer and real animation production with source and native-size verification |
| [099_sandstorm_super_event_prompt.md](099_sandstorm_super_event_prompt.md) | One earned global presentation, primary text research and a unique verified musical recording |
| [099_sandstorm_achievement_prompt.md](099_sandstorm_achievement_prompt.md) | All eight achievement trackers, eligibility, actual outcome receipts and icon variants |
| [099_sandstorm_decision_mission_prompt.md](099_sandstorm_decision_mission_prompt.md) | Five action and three mission families with transactions, authority, automation and observed outcomes |
| [099_sandstorm_coding_prompt.md](099_sandstorm_coding_prompt.md) | Complete staged implementation, shared wiring, owner gates, evidence, documentation and catalog handoff |
| [099_sandstorm_goal_prompt.md](099_sandstorm_goal_prompt.md) | Compact `/goal` execution instruction, 3,952 characters including its heading and final newline |

The prompts require the canonical specifications rather than treating the compact goal as a replacement for detailed behavior.
Their future implementation instructions are not a claim that gameplay code, assets, final localisation or live validation were produced in this planning task.

## Reading completeness and limitations

The source-reading statements in [source authority](099_sandstorm_source_authority.md) describe the original 2026-10-07 planning record: 88 distinct supplied text versions across five archives, fully read by at least one named reader, with repository work pinned to `a3ef485c5da7e2337122eca04ac65c175050f251`.
The package does not claim exhaustive repository reading, installed vanilla geometry inspection, workbook inspection or HOI4 execution.
The current 099 bridge, the measured-population helper discrepancy and the missing local military, air, geometry and owner evidence are recorded as implementation gates.
Population geography, casualty coefficients and several physical behaviours are modelling proposals whose engine feasibility is still a dependency.

## Revision log

### 2026-10-10 spec audit

- Marked the source-reading ledger and package-verification JSON as historical provenance that implementation does not need to read, and folded the long reading-completeness narration into four lines pointing at the source-authority file.
- Replaced the Codex-specific `fork_turns` instruction in the execution maps with the repository's self-contained-prompt rule, and pointed every skill link at the tracked `.claude/skills/` location instead of the ignored `.agents/skills/` copy.
- Pass 2 review retained the design: two public values (local intensity and estimated exposed civilians), five response families, three missions, and hidden material, dose and turn weights. The storm's consequences run through the existing mask, migration, famine, Air Cleanliness, cost and repair owners rather than new ledgers.
