# Event 029: Riches Found specification package

This package expands Event 029 into a repeatable state-bound wealth crisis for Chaos Redux.

Extract the folder `029_riches_found_specs` directly into `docs/specs/`.

The package is planning material only.

It does not claim that Event 029 has been implemented, wired, balanced through the HOI4 probability tools, or tested in game.

## Package map

1. `029_riches_found_spec_part_1_core_loop.md` defines the event identity, valid target rules, persistent mine state, controller benefits, visible values, repeatability, and presentation.
2. `029_riches_found_spec_part_2_baseline_progression.md` maps the complete ordinary lifecycle from discovery through development, concessions, armed competition, closure, recovery, and controller transfer.
3. `029_riches_found_spec_part_3_decisions_missions_foreign_interference.md` maps the decision category, decision families, missions, costs, foreign concessions, raids, occupation behavior, and cleanup.
4. `029_riches_found_spec_part_4_evolutions.md` defines The Resource Curse, Gold Disease, Demons Beneath the Mine, and their late crisis outcomes.
5. `029_riches_found_spec_part_5_ai_balance_interactions.md` defines AI strategy, repeatable-event balance, exploit prevention, multiplayer behavior, Event 18 separation, and shared-system integration.
6. `029_riches_found_spec_part_6_assets_localisation_achievements.md` defines the visual package, writing direction, event-detail direction, catalog direction, and achievement set.
7. `029_riches_found_research_notes.md` records the historical, economic, governance, security, and folklore research used by the design.
8. `029_riches_found_ai_probability_scenarios.md` gives the required named scenarios and expected weighted behavior for later MCP auditing.
9. `029_riches_found_acceptance_criteria.md` gives implementation and live-test acceptance scenarios without claiming they have been run.
10. `029_riches_found_asset_prompt.md` is a context-complete production prompt for the asset subagents.
11. `029_riches_found_achievement_prompt.md` is a context-complete achievement implementation prompt.
12. `029_riches_found_decision_mission_prompt.md` is a context-complete decision and mission implementation prompt.
13. `029_riches_found_coding_prompt.md` is the full implementation prompt.
14. `029_riches_found_goal_prompt.md` is a compact implementation goal prompt under 4,000 characters.
15. `029_riches_found_catalog_alignment.md` maps the required catalog and Event Details content direction.
16. `029_riches_found_source_review_manifest.md` records what was read, what could not be accessed, and which design choices followed from the source review.

## Main design decisions

Event 029 remains a Minor Repeatable event with no cluster assignment.

The event grants the selected country exactly 1,000 political power on discovery because that amount is part of the user-supplied design.

The lasting system belongs to one selected state and follows the current controller when control changes.

The event is distinct from Event 018 Resources Found.

Event 018 owns physical strategic-resource discovery, deeper deposits, caves, fossils, Oth-Kesh, and The World Opens Below.

Event 029 owns windfall politics, a mining rush, claims, concessions, revenue distribution, corruption, private security, raids, obsessive greed, and a fictional supernatural bargain tied to valuation and extraction.

The player sees one primary value, Extraction Pressure, and three supporting values, Mine Development, Local Order, and Revenue Legitimacy.

The system uses an ordinary decision category with a static category picture.

A dedicated scripted GUI would add maintenance and visual weight without improving the decisions the player must make.

Only three numbered evolutions are registered.

The user fixed Evolution I at Chaos Tier, 600+, while the project rule permits one evolution stage per chaos tier.

The two remaining higher tiers support Evolution II at 800+ and Evolution III at 1,000+.

The empty Evolution IV and Evolution V placeholders are therefore developed as late crisis outcomes inside the existing tracks instead of being registered as extra evolution stages.

This is a compliance decision, not a reduction of the event's late-game content.

## Source and tool limits

Every file supplied with the task was read in full, including the three CSV catalogs and every TOML file inside `subagents.zip`.

The active environment did not expose the Chaos Redux repository, the offline Paradox wiki snapshot, the installed vanilla game files, the authoritative XLSX catalog workbook, the custom Codex subagent spawning interface, or the HOI4 MCP tools.

The package therefore applies the supplied project rules and source snapshots directly, but it is not repository-inspected or MCP-validated.

Those missing checks are mandatory during implementation and are named in the prompts and acceptance criteria.

No section was shortened or omitted to produce a quicker response.
