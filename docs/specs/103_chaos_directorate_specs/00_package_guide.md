# Event 103 planning package

## Purpose and status

This package specifies Chaos Directorate, the Major event replacing Conscription, together with The Final Boss triggerable scenario and the Chaos Always Wins world-end branch. It is a design and implementation handoff. It contains no implemented gameplay, generated art, researched final quotation or music, and no engine validation. Proposed balance numbers are starting anchors. The three user-supplied names (Chaos Directorate, The Final Boss, Chaos Always Wins) are final. Other titles, labels, asset identifiers and helper names are working directions until their implementation or research gate is complete.

Acceptance bases: the preserved brief supplies the explicit user requirements, Part 14 records the planning parent's selection of expansions, Part 15 records its acceptance of five review corrections, and the user's 10 October 2026 decisions and spec audit are logged below. Importing the package authorizes documentation and review, not gameplay implementation.

## Current use and review

Use the [import evidence](../../plans/103_chaos_directorate_plans/103_import_evidence_2026-10-10.json) and the [import review](../../plans/103_chaos_directorate_plans/subagent_handoffs/103_import_review_2026-10-10.md) for checkout findings, document dispositions and the resume point. The [shared identifier registry](../shared_identifier_registry.md) owns allocations.

Active workflow follows [AGENTS.md](../../../AGENTS.md), [CLAUDE.md](../../../CLAUDE.md), the [events](../../../.claude/skills/chaos-redux-events/SKILL.md) and [subagents](../../../.claude/skills/chaos-redux-subagents/SKILL.md) skills, and the subject-owner skills they name. Use supported MCP checks with the initial request and at most one corrected retry for an underlying failure, then local references, source review and useful local checks, recording what was unavailable. Missing implementation is distinct from an unavailable optional check. Do not request or await user-owned game testing, and do not claim live engine behavior from static evidence.

On 10 October 2026 the user selected **Allow relaunch after defeat**. It supersedes the original lifetime manual-launch lock and is owned by [Part 09](09_chaos_always_wins_and_the_final_boss.md#relaunch-after-confirmed-defeat). The Final Boss may create a fresh immutable episode after confirmed destruction and completed cleanup, with a clean available CXT carrier and no incompatible terminal state. One episode may be active or provisionally committing at a time, automatic Event 103 stays fire-once, and old work and achievement checks are isolated from the replacement actor. Parts 02, 11, 12, 13 and 16 consume the contract.

## Specification map

| File | What it decides |
| --- | --- |
| [01. Identity and campaign](01_directorate_identity_and_campaign.md) | Catalog identity, player experience, campaign stages and scope |
| [02. Arrival and pool](02_arrival_grace_and_major_pool.md) | Continuous one-year grace, growing weight, candidate state selection and transactional arrival |
| [03. Opening power](03_opening_power_and_sustainment.md) | World-scaled force, equipment, manpower, industry, supply readiness and the sustainment indicator |
| [04. Universal arsenal](04_universal_chaos_arsenal.md) | Every current and future installed capability, owner registration, valid modes and actual operational use |
| [05. Conquest and geography](05_conquest_absorption_and_geography.md) | Frontier wars, absorption, whole-continent control, impassable-state settlement, remote reach and defeat |
| [06. Country and focus](06_country_institutions_and_focus_paths.md) | Complete CXT transformation, three spirit slots and eight connected focus families |
| [07. Orders and resistance](07_orders_and_resistance.md) | Six boss order families, terminal replacements, seven resistance families, costs and missions |
| [08. AI and probability](08_strategic_ai_and_probability.md) | Strategic priorities, real special operations, family service and probability scenarios |
| [09. Ending and scenario](09_chaos_always_wins_and_the_final_boss.md) | Live terminal gates, counterplay, continued world conquest, four manual intensities and relaunch |
| [10. Presentation and assets](10_presentation_and_assets.md) | Identity, flags, portrait, news, focus and decision art, indicators and the single terminal super-event |
| [11. Chaos and achievements](11_chaos_consequences_and_achievements.md) | Concrete Chaos gains and reversals, repeat guards, five resistance and three boss-player achievements |
| [12. Implementation contracts](12_implementation_and_integration_contracts.md) | Integration order, shared ownership, identifier reservations, callbacks, catalog updates and required bindings |
| [13. Acceptance matrix](13_validation_and_acceptance_matrix.md) | Success, boundary, near-miss, rollback, compatibility and lifecycle cases |
| [14. Sources and routing](14_sources_reconciliation_and_usage_maps.md) | Source conflict dispositions, repository documents depended on and specialist routing |
| [15. Review disposition](15_design_review_and_disposition.md) | Accepted review fixes F01 through F05 and the remaining implementation gates |
| [16. Arsenal architecture](16_arsenal_interfaces_and_migration.md) | Neutral owner APIs, effective-definition census, carrier migration and bounded callback lifecycle |

## Implementation prompts

Read the complete specifications before executing a specialist prompt. The prompts route production work to the relevant skills and do not restate the design.

- [Coding prompt](103_chaos_directorate_coding_prompt.md)
- [Asset prompt](103_chaos_directorate_asset_prompt.md)
- [Super-event prompt](103_chaos_directorate_super_event_prompt.md)
- [Achievement prompt](103_chaos_directorate_achievement_prompt.md)
- [Decision and mission prompt](103_chaos_directorate_decision_mission_prompt.md)
- [Goal prompt](103_chaos_directorate_goal_prompt.md)

## Authority

The [brief requirement matrix](brief_requirement_traceability.md) maps every explicit user requirement to its specification, and the [original brief](103_chaos_directorate_source_brief.md) is preserved verbatim. Parts 03, 05 and 09 own the force, territorial and ending predicates used elsewhere. Part 11 owns achievement eligibility and Chaos accounting. Part 16 provides the technical interfaces beneath Part 04 without narrowing its universal promise. If implementation evidence requires a change to any promise, record and resolve it explicitly instead of silently substituting a smaller feature.

The planning reservations are The Final Boss `SCN-033` / raw `33` / key `the_final_boss` with name-sort key `the_final_boss_name = 4.375`, Chaos Always Wins world-end `19` / key `chaos_always_wins` / owner event `103` with the shared primary per-event sort `10`, presentation slot `124`, and independently reserved playback audio `124`. The equal presentation and audio numbers are an explicit cross-namespace mapping. None of this registers a scenario, ending, media file or catalog row. CXT is reused, so no new country tag is required.

## Historical receipts

These files record the original planning run and its supplied source archive, which is not part of this repository. They have no design or runtime consumer, are not instructions, and do not describe a fresh read or validation of this checkout. Do not consult them to resolve a design question. They are kept as provenance because the [import evidence](../../plans/103_chaos_directorate_plans/103_import_evidence_2026-10-10.json) cites each of them as a protected historical input by path and hash.

| Files | What they record |
| --- | --- |
| `package_validation.json`, `delivery_audit_validation.json` | Archive inventory, hashes and structural checks of the original planning ZIP. Many package files have since changed, so the hashes describe only the original versions |
| `archive_inventory.json`, `source_groups.json`, `coverage_check.json`, `root_coverage.json`, `core_coverage.json`, `systems_coverage.json`, `assets_coverage.json` | Source-reading ledgers (extracted members, distinct bodies, reading ranges) for the supplied archive |
| `repository_evidence.json`, `repository_initial_evidence.json` | Blob identities of the original read-only repository lookups |
| [`source_reading_manifest.md`](source_reading_manifest.md) | Human-readable index of the ledgers above |
| [`103_chaos_directorate_source_protocol.md`](103_chaos_directorate_source_protocol.md) | The external project's source-reading procedure used by the planning run |

The reading ledgers, the two repository-evidence files, the protocol and the manifest are candidates for removal in a coordinated cleanup that also updates the import evidence. Part 14's scope section explains how the planning run's tool and reading observations should be read.

## Open questions and proposals

These touch accepted design or explicit user decisions, so they are proposals and not applied.

1. **Directorate decision families may be AI-only.** Arrival never switches the human player, and ordinary control of CXT may prove unsupported (a verified gate in Part 15). In that case six Directorate order families with full quotes, costs and refunds serve only the AI. Proposal: if control is never verified, implement the AI behavior directly through the owner operations and keep the quote contract only for resistance actions. This reduces a requested deliverable, so it needs the user's approval. It touches the brief's requirement for a boss that actively conquers and the three boss-player achievements B1 through B3.
2. **Five of eight achievements need confirmed Directorate destruction**, which Part 07 calls nearly impossible once the boss is mature. Proposal: after balance measurement, check that R1 through R5 are attainable at the intended intensity before release. This touches the user's statement that defeating the boss should be extremely difficult.
3. **Sustainment indicator precision.** Part 10 permits at most two public values. This audit keeps both, and makes the sustainment value a target by gating its limiting component behind Reconnaissance. If playtesting shows the second value never changes a decision for the Directorate player, fold it into the tooltip of the first. This touches the "exactly two public measures" design in Part 10.

## Revision log

### 2026-10-10 spec audit

Basis: the 10 October 2026 spec audit under the user's planning-package brief.

- Removed process narration and stale workflow from Parts 14, 15, 16, 12, 13 and 10 (source-reading tables, tool-registry observations, planned-tool status tables, Codex `fork_turns` and `collaboration.spawn_agent` wording, `.agents/skills` links, the planning model name). Part 14 is now conflict dispositions, depended-on repository documents and routing. Part 15 keeps F01 through F05 and the gates. Filenames were kept because the import evidence cites them.
- Classified the JSON ledgers, the protocol and the manifest as historical receipts in this guide. Nothing was deleted, because the import evidence names them as protected inputs.
- Consolidated repeated rules into their owners: identifier reservations live in Part 12 and this guide, relaunch in Part 09, the force and output formulas in Part 03 (the coding prompt now points to them), and Part 11 holds the R3, B1, B2 and B3 formulas (the achievement prompt now points to them).
- Pass 2: resistance families reduced from nine to seven. Population evacuation was removed because migration already owns Evacuate Civilians and famine owns Evacuate, Escort Relief and Airlift Relief. Sea corridor merged into Aid convoy together with Material aid. Reconnaissance now gates the sustainment indicator's limiting component and extends the Counterattack and Local asset denial target lists. Every resistance success must change a physical state of the war or extend what another action can target.
- Pass 2: the absorption choice between fast exploitation and restoration lives only in the Reconstruction action, and the role-emphasis choice only in Production priority. Focus percentages were tied to named consumers, and the Combined arsenal coordination focus group now raises concurrent emphases to two instead of repeating the choice. Spirit stages must name one consumer.
- Pass 2: added Part 09's counterplay table (starve the foothold, keep one state, contest the crossing, deny the yield, answer the special arsenal, close the Chaos gate) with acceptance cases P14, P15 and W12 and AI scenarios in Part 08.
- Preserved unchanged: the catalog identity, ID 19, SCN-033 with key 4.375, slot and audio 124, CXT reuse, the 10 October relaunch decision, one active or provisional boss, ordinary terminal-conflict gates, the eight focus families, three spirit slots, eight achievements and all numeric anchors not named above.
