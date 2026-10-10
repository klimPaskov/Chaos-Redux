# The Great Revolution planning specification

Event 091, `091_the_great_revolution`.

This package expands the complete supplied brief into a source specification for the connected Event 001 and Event 091 crisis. It contains fourteen design chapters, accepted technical handoffs, researched presentation candidates, requirement coverage, acceptance scenarios, review dispositions, and six separate prompts for later implementation.

## Destination and use

The package is imported at:

```text
docs/specs/091_the_great_revolution_specs/
```

Read the design chapters as one package. The technical handoffs make ownership, feasibility, and validation obligations concrete without turning the player-facing design into pasteable code. The six prompts divide future implementation responsibilities and must be read with the authority and current-state boundaries below. Embedded implementation instructions are future task inputs, not authorization to execute them during import.

The deliverable is planning only. Game scripts, native compatibility, art, audio, models, animations, and runtime integration are separate implementation work. A source plan does not constitute permission to claim those surfaces complete without their required evidence.

## Design chapters

| Part | Scope | File |
| --- | --- | --- |
| 1 | Vision and player experience | [091_the_great_revolution_spec_part_1_core.md](design/091_the_great_revolution_spec_part_1_core.md) |
| 2 | Connected 001 evolutions, containment and selection | [091_the_great_revolution_spec_part_2_001_evolutions_and_selection.md](design/091_the_great_revolution_spec_part_2_001_evolutions_and_selection.md) |
| 3 | Worldwide opening, inherited bases and state rights | [091_the_great_revolution_spec_part_3_opening_and_territory.md](design/091_the_great_revolution_spec_part_3_opening_and_territory.md) |
| 4 | Country package, political philosophies and playable roles | [091_the_great_revolution_spec_part_4_countries_and_political_routes.md](design/091_the_great_revolution_spec_part_4_countries_and_political_routes.md) |
| 5 | Influence, sovereignty, Momentum and Third-Eye powers | [091_the_great_revolution_spec_part_5_influence_momentum_and_powers.md](design/091_the_great_revolution_spec_part_5_influence_momentum_and_powers.md) |
| 6 | Eight army families, force sources, equipment and sustainment | [091_the_great_revolution_spec_part_6_army_and_economy.md](design/091_the_great_revolution_spec_part_6_army_and_economy.md) |
| 7 | Complete focus families, route logic and country overlays | [091_the_great_revolution_spec_part_7_focus_tree_architecture.md](design/091_the_great_revolution_spec_part_7_focus_tree_architecture.md) |
| 8 | Action phases, missions, costs and role-aware AI | [091_the_great_revolution_spec_part_8_decisions_missions_and_ai.md](design/091_the_great_revolution_spec_part_8_decisions_missions_and_ai.md) |
| 9 | Expansion, Red World, finite survival and aftermath | [091_the_great_revolution_spec_part_9_war_expansion_and_endings.md](design/091_the_great_revolution_spec_part_9_war_expansion_and_endings.md) |
| 10 | Scientific, supernatural, political and civilian connections | [091_the_great_revolution_spec_part_10_cross_event_connections.md](design/091_the_great_revolution_spec_part_10_cross_event_connections.md) |
| 11 | Narrative flow, twelve months and three super-events | [091_the_great_revolution_spec_part_11_story_and_presentation.md](design/091_the_great_revolution_spec_part_11_story_and_presentation.md) |
| 12 | Portraits, flags, icons, models, animation, counters and sound | [091_the_great_revolution_spec_part_12_visual_and_audio_design.md](design/091_the_great_revolution_spec_part_12_visual_and_audio_design.md) |
| 13 | Eight achievements and the month-meta disposition | [091_the_great_revolution_spec_part_13_achievements.md](design/091_the_great_revolution_spec_part_13_achievements.md) |
| 14 | Chaos impact, balance, anti-farming and rare openings | [091_the_great_revolution_spec_part_14_chaos_balance_and_variants.md](design/091_the_great_revolution_spec_part_14_chaos_balance_and_variants.md) |

## Six implementation prompts

All six prompts were created after the full specification was assembled. They contain instructions for the subsequent implementation task, not a record that those actions were executed during planning.

| Prompt | Responsibility |
| --- | --- |
| [091_the_great_revolution_asset_prompt.md](091_the_great_revolution_asset_prompt.md) | All visual assets, grounded portraits, flags, models, real animations, bespoke counters and sourced unit sound |
| [091_the_great_revolution_super_event_prompt.md](091_the_great_revolution_super_event_prompt.md) | Three complete researched text, image, audio and registration packages |
| [091_the_great_revolution_achievement_prompt.md](091_the_great_revolution_achievement_prompt.md) | All eight achievement identities, conditions, disqualifiers, tracking and art |
| [091_the_great_revolution_decision_mission_prompt.md](091_the_great_revolution_decision_mission_prompt.md) | Complete action and mission implementation with costs, sovereignty, AI and lifecycle proof |
| [091_the_great_revolution_coding_prompt.md](091_the_great_revolution_coding_prompt.md) | Parent implementation, integration, audits, catalogs and full completion standard |
| [091_the_great_revolution_goal_prompt.md](091_the_great_revolution_goal_prompt.md) | Compact goal with the required character limit and key pass or fail requirements |

## Accepted technical handoffs

| File | Purpose |
| --- | --- |
| [architecture.md](implementation_handoffs/architecture.md) | Crisis ownership, opening and political lifecycle, finite survival and terminal accounting |
| [state_and_transaction_contracts.md](implementation_handoffs/state_and_transaction_contracts.md) | Saved state, exact receipts, finite queues, initial Momentum formula, deadlines and conservation |
| [integration_contracts.md](implementation_handoffs/integration_contracts.md) | Verified repository seams, 001 migration, shared owners and obsolete behavior to retire |
| [feasibility_and_mcp_map.md](implementation_handoffs/feasibility_and_mcp_map.md) | Specific future native inspections, comparisons, probability work and engine proof |
| [country_technology_and_registry_handoff.md](implementation_handoffs/country_technology_and_registry_handoff.md) | Full country setup, technology graph, research development and public documentation |
| [canonical_subagent_usage_map.md](implementation_handoffs/canonical_subagent_usage_map.md) | All twenty supplied canonical roles, bounded assignments and parent integration |

These are accepted design contracts promoted from reviewed planning work. New working addenda, production handoffs and audit follow-ups in the implementation repository belong under `docs/plans/091_the_great_revolution_plans/`. Fold accepted changes back into this source package and record their disposition.

## Research and source records

| File | Scope |
| --- | --- |
| [01_source_precedence_and_repository_findings.md](research/01_source_precedence_and_repository_findings.md) | Complete supplied-source coverage, conflicts, pinned repository evidence and known limits |
| [source_inventory_and_reading_coverage.json](research/source_inventory_and_reading_coverage.json) | SHA-256 inventory and compact coverage for every supplied text and reading block |
| [02_historical_foundations.md](research/02_historical_foundations.md) | Comintern, councils, the Stalin-Trotsky debate, symbols, Lenin's cult and calendars |
| [03_super_event_text_research.md](research/03_super_event_text_research.md) | Verified quote candidates, separate cultural remarks, source attribution and corrections |
| [04_super_event_audio_research.md](research/04_super_event_audio_research.md) | Three musical roles, first candidates and reserves, rights layers and audition gates |
| [05_lenin_portrait_source_handoff.md](research/05_lenin_portrait_source_handoff.md) | Three historical portrait source options, one authoritative identity and dynamic overlay production |
| [06_unit_audio_sources_and_roles.md](research/06_unit_audio_sources_and_roles.md) | Fourteen source leads, rejected or unresolved candidates, eight-family role coverage and synchronization |

The historical material informs this fictional supernatural event. Candidate source records do not mean that final images or sound files were acquired, visually inspected, auditioned, licensed for every territory, or approved for runtime use. Those distinctions are recorded per candidate.

## Design decisions to preserve

The event is a fire-once Major at Chaos level 5, beginning at 800 Total Chaos, with the catalog name The Great Revolution and no cluster. Actual entry into Event 001 Evolution 3, through active-event progression or a pre-fire evolved opening, creates the permanent historical unlock. Baseline firing or a Chaos threshold alone does not unlock 091. Active spread and current world conditions remain separate eligibility requirements. Every actual later whisper adds 200 weight, and locked weight persists.

The opening uses independent frozen proportional nominations, guaranteed Event 001 inheritance first, and one physical union. It has no arbitrary territorial minimum. An invalid zero-origin proposal fails before actual firing and retains its selections and weight. Occupation overlap can affect more territory than a country's own nomination, with the excess explicitly recorded. Joining governments retain non-origin local rights under a native split-rights contract that must be verified.

Stalin's current Soviet government refuses. Trotsky's current Soviet government joins as an autonomous cofounder whose protection persists across later leadership change and the terminal phase. Ordinary supporters receive meaningful aid and a separate Influence struggle. Independence remains free and accessible until annexation actually commits.

Revolutionary Momentum and ordinary-joiner Influence are the two persistent public event values. Momentum follows current strategic facts with finite milestone receipts. The body and at most seven anchors create a bounded victory problem. Four finite person-equivalent manifestation grants seed the host, while other growth consumes real formations, people, equipment, production or aid.

The Red World requires Chaos strictly above 1000 and current rule over strictly more than half of the frozen population-weighted inhabited world, plus actual Lenin and country existence, shared settings, and no competing terminal state. It begins final resistance and final political choices. It does not erase Trotsky's autonomy or perform instant worldwide absorption.

Three political philosophies, eight coherent focus families, six distinct regional campaigns, eight army families and eight substantial achievements create the full campaign. The across-campaign Twelve Possible Revolutions achievement is explicitly parked until a verified persistence provider exists. All twelve month titles remain required.

## Authority and current repository state

The uploaded package is preserved as Event 091 design source. Its [review disposition](validation/review_disposition.md) records the original planning parent's acceptance of the technical contracts and concrete design choices within a supplied user brief. That record is the import's historical acceptance evidence, rather than a folder name or status label. The full original 2357-line brief and its conversation are not bundled here, so this review cannot independently establish every original acceptance claim. On 10 October 2026 the user explicitly chose "Use the new 091 package and align Event 001 (Recommended)". This accepts the shared handoff's inherited-first proportional nominations, rebel political choice and continuing targeted 001 cells. Their gameplay implementation is accepted and queued because this task imports and aligns documentation only.

Current workflow authority is [AGENTS.md](../../../AGENTS.md) and the owning skills linked by the implementation prompts. Imported research, source inventory, historical validation reports and SHA256SUMS are receipts for the original package. The actively maintained `validation/acceptance_scenarios.md` is a future-scenario contract rather than a frozen QA receipt. Their source revision `a3ef485c5da7e2337122eca04ac65c175050f251`, tool unavailability, original 3968-character goal and archive validation describe that planning environment. Preserve those bytes and do not treat their checksums as current edited-file hashes or their completed reviews as current gameplay proof.

The [current import evidence](../../plans/091_the_great_revolution_plans/091_import_evidence_2026-10-09.json) records original/current hashes, source evidence, catalog differences and identifier checks. The [documentation review handoff](../../plans/091_the_great_revolution_plans/subagent_handoffs/091_import_review_2026-10-09.md) records per-document dispositions, the 10 October acceptance and remaining implementation questions.

The current 091 root remains legacy implementation. It still absorbs communist rebels and clears the insurgency system. The authoritative workbook still has the older Chaos level, Soviet response and evolution wording. Those are future migration surfaces, not implemented versions of this imported design. The [integration contract](implementation_handoffs/integration_contracts.md#current-checkout-reconciliation-2026-10-09) records the superseded 001 design wording, explicit acceptance and current source boundary. The [aligned 001 World Revolution State Integration](../001_communism_spread_specs/001_communism_spread_spec.md#world-revolution-state-integration) carries the same accepted shared handoff.

The [shared identifier registry](../shared_identifier_registry.md) reserves Red World world-end ID 18, presentation slots 121/122/123 and independently checked playback audio IDs 121/122/123 for opening/Red World/earned defeat respectively. Revalidate these reservations before wiring. They approve neither runtime registration nor a track or asset. Keep incumbent `REV` and `REV_vladimir_lenin` identities. An installed external mod also defines REV, which remains a compatibility fact to handle during implementation rather than a reason to add a second identity in this import.

## Verification and remaining implementation work

[requirement_coverage.md](validation/requirement_coverage.md) maps every level-two and level-three section of the user's full brief. [acceptance_scenarios.md](validation/acceptance_scenarios.md) defines opening, country, sovereignty, military, endgame, presentation and integration evidence. [review_disposition.md](validation/review_disposition.md) records the parent acceptance and the final independent reviews. [package_validation.md](validation/package_validation.md) records the checks actually performed on this deliverable.

The independent [AI and probability planning audit](validation/ai_probability_planning_audit.md), [completion audit](validation/completion_audit.md), and [fresh improvement review](validation/final_improvement_review.md) retain their findings and evidence boundaries. The parent disposition records which findings were fixed and why broad expansion stopped.

The original planning receipts report that all supplied Project Sources were processed, covering 133 text instances, 91 distinct byte sequences and 526 completed reading blocks. They record duplicate checks, reading of distinct passages and recovery of truncated source reads. The package preserves that inventory and its independent audit findings as historical evidence, without claiming this import reread the absent external sources.

Targeted repository inspection used commit `a3ef485c5da7e2337122eca04ac65c175050f251` in `klimPaskov/Chaos-Redux`. It was not a full installed-game audit. The supplied CSV catalogs were export snapshots, and no editable catalog workbook was supplied. Implementation must inspect current registries and edit the actual workbook through its owner.

Material future work includes native split ownership and control, one-Lenin character continuity, installed tag and DLC compatibility, actual unit and population accounting, deadline and receipt behavior, focus and technology layout review, dynamic Politics and Diplomacy overlays, model and animation production, final sourced sound coverage, and musical audition and rights resolution. Tool unavailability in the original planning environment is historical. Discover current capabilities when implementation is authorized.

Follow current AGENTS.md for proportionate verification and the shared retry limit. An unavailable optional MCP route permits source/reference review, source-derived scenario calculations and useful local checks, with the missing observation recorded as a limitation. Use one initial read-only request and at most one useful corrected retry per underlying failure across agents, tools and resumed turns. A known defect, missing required output, indispensable unresolved native capability or unapproved design reduction remains open. The user owns live-game validation. Do not request or await it, or ask for logs, saves, screenshots or testing as a completion gate.

[SHA256SUMS.txt](SHA256SUMS.txt) records the original imported payload bytes. Current edited-file hashes belong to the current import evidence linked above.

The current catalog status remains To Be Reworked. Later status classification follows the current event skill and explicit user approval rules rather than an unavailable optional check or pending user testing.
- 2026-10-10 spec audit: pass 2 incomplete. Design, handoff and validation files were reconciled; the research files were not re-read.
