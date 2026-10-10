# Event 103 planning package

## Purpose and extraction

This package specifies Chaos Directorate, the Major event replacing Conscription, together with The Final Boss triggerable scenario and Chaos Always Wins world-end branch. The imported specification is installed at `docs/specs/103_chaos_directorate_specs/`.

The deliverable is the original planning design and its implementation handoffs, with the current user's manual-relaunch decision incorporated below. The preserved brief supplies explicit user requirements, while Part 14 records the planning parent's selection of expansions and Part 15 records its acceptance of the five review corrections. Those are the original acceptance bases. Import authorizes documentation installation and review, without granting gameplay implementation approval. The package contains no implemented gameplay, generated art, researched final quotation or music, or claimed engine validation. Proposed balance numbers are starting anchors. The three user-supplied names above are final. Other titles, labels, asset identifiers and helper names are working directions until their proper implementation or research gate is complete.

## Current use and review

Use [current import evidence](../../plans/103_chaos_directorate_plans/103_import_evidence_2026-10-10.json) and the [core review handoff](../../plans/103_chaos_directorate_plans/subagent_handoffs/103_import_review_2026-10-10.md) for checkout findings, document dispositions and the resume point. Parts 14 and 15 and all imported JSON receipts describe the original planning run. Their source paths, tool failures, source-reading claims and hashes do not describe a fresh read or validation of this checkout. The original protocol is historical input. Its full supplied-project reading gate is not an instruction to recreate omitted source archives or repeat the planning task.

Active workflow follows [AGENTS.md](../../../AGENTS.md), [events](../../../.agents/skills/chaos-redux-events/SKILL.md), [subagents](../../../.agents/skills/chaos-redux-subagents/SKILL.md) and the current subject-owner skills named by those files. Use meaningful supported MCP checks with the initial request and at most one corrected or narrower retry for an underlying failure. Then use relevant local references, source review and useful local checks, recording what was unavailable. Keep missing implementation distinct from unavailable optional verification. Do not request or await user-owned game testing to deliver otherwise finished work, and do not claim live engine behavior from static evidence.

On 10 October 2026, the user selected **Allow relaunch after defeat**. That explicit decision supersedes Part 09's original historical launch prohibition and is promoted into Parts 02, 09, 11, 12, 13 and 16. The Final Boss may create a fresh immutable episode after confirmed destruction and completed cleanup, with a clean available CXT carrier and no incompatible terminal state. Only one episode may be active or provisionally committing at a time. Automatic Event 103 remains fire-once, and relaunch preserves prior history and isolates all old work and achievement checks from the replacement actor. This design decision does not authorize gameplay implementation during import.

## Specification map

| File | What it decides |
| --- | --- |
| [01. Identity and campaign](01_directorate_identity_and_campaign.md) | Catalog identity, player experience, campaign stages and scope |
| [02. Arrival and pool](02_arrival_grace_and_major_pool.md) | Continuous one-year grace, growing weight, candidate state selection and transactional arrival |
| [03. Opening power](03_opening_power_and_sustainment.md) | World-scaled force, equipment, manpower, industry, supply readiness and sustainment indicator |
| [04. Universal arsenal](04_universal_chaos_arsenal.md) | Every current and future installed capability, owner registration, valid modes and actual operational use |
| [05. Conquest and geography](05_conquest_absorption_and_geography.md) | Frontier wars, absorption, whole-continent control, impassable-state settlement, remote reach and defeat |
| [06. Country and focus](06_country_institutions_and_focus_paths.md) | Complete CXT transformation, three spirit slots and eight connected focus families |
| [07. Orders and resistance](07_orders_and_resistance.md) | Six boss order families, terminal replacements, nine resistance families, costs and missions |
| [08. AI and probability](08_strategic_ai_and_probability.md) | Strategic priorities, real special operations, family service and complete probability scenarios |
| [09. Ending and scenario](09_chaos_always_wins_and_the_final_boss.md) | Live terminal gates, continued world conquest and four manual intensities |
| [10. Presentation and assets](10_presentation_and_assets.md) | Identity, flags, portrait, news, focus and decision art, indicators and the single terminal super-event |
| [11. Chaos and achievements](11_chaos_consequences_and_achievements.md) | Concrete Chaos gains and reversals, repeat guards, five resistance and three boss-player achievements |
| [12. Implementation contracts](12_implementation_and_integration_contracts.md) | Integration order, shared ownership, receipts, callbacks, catalog updates and required bindings |
| [13. Acceptance matrix](13_validation_and_acceptance_matrix.md) | Success, boundary, near-miss, rollback, compatibility and lifecycle cases |
| [14. Sources and usage maps](14_sources_reconciliation_and_usage_maps.md) | Complete source reading, conflicts, repository research and future tool and specialist work |
| [15. Review disposition](15_design_review_and_disposition.md) | Final improvement review, accepted fixes, scope closure and remaining implementation gates |
| [16. Arsenal architecture](16_arsenal_interfaces_and_migration.md) | Detailed neutral owner APIs, effective-definition census, carrier migration and bounded callback lifecycle |

## Separate implementation prompts

Read the complete specifications before executing a specialist prompt. The prompts preserve the design and route production work to the relevant supplied workflow.

- [Coding prompt](103_chaos_directorate_coding_prompt.md)
- [Asset prompt](103_chaos_directorate_asset_prompt.md)
- [Super-event prompt](103_chaos_directorate_super_event_prompt.md)
- [Achievement prompt](103_chaos_directorate_achievement_prompt.md)
- [Decision and mission prompt](103_chaos_directorate_decision_mission_prompt.md)
- [Goal prompt](103_chaos_directorate_goal_prompt.md)

## Evidence and authority

The [brief requirement matrix](brief_requirement_traceability.md) maps every explicit user requirement to its specification. The [source-reading manifest](source_reading_manifest.md) indexes all 91 fully read distinct bodies and 42 verified identical copies, covering 133 supplied text paths. It links the individual reader ledgers and exact repository response metadata. The [original brief](103_chaos_directorate_source_brief.md) and [original source protocol](103_chaos_directorate_source_protocol.md) are preserved verbatim.

Parts 03, 05 and 09 own the force, territorial and ending predicates used elsewhere. Part 11 owns achievement eligibility and Chaos consequence accounting. Part 16 provides the technical interfaces beneath Part 04 without narrowing its universal promise. If later implementation evidence requires a change to any promise, record and resolve that change explicitly instead of silently substituting a smaller feature.

The original planning ZIP reserved no numeric scenario, world-end, display or audio ID. Current assignments belong to the [shared identifier registry](../shared_identifier_registry.md) and import evidence. Keep the namespaces distinct, preserve existing identities and inspect the active consumers before runtime binding. CXT is reused, so no new country tag is required.

The current planning reservations are The Final Boss `SCN-033` / raw `33` / key `the_final_boss`, its independent name-sort key `the_final_boss_name = 4.375`, Chaos Always Wins world-end `19` / key `chaos_always_wins` / owner event `103`, presentation slot `124` and independently reserved playback audio `124`. The ending uses the existing shared primary per-event sort `10`. Matching presentation/audio values are explicit assignments across separate namespaces. They do not establish runtime registration, approved media or catalog migration.

The [original package validation record](package_validation.json) records the delivered archive inventory, hashes, prompt consistency, structural checks and arithmetic checks. Its hashes apply to the immutable original package, including versions intentionally corrected during import. The current import evidence records checkout changes separately. Neither receipt establishes native engine behavior or completed implementation.
