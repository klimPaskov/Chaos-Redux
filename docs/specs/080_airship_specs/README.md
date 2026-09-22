# Event 080: Airship planning package

## Use

Extract the `080_airship_specs/` folder into the repository's `docs/specs/` directory. The result is `docs/specs/080_airship_specs/`.

Read the numbered specifications in order. For implementation, use the coding prompt and its linked specialist prompts. The separate goal prompt is ready to copy as a `/goal` instruction and stays within the planning skill's 3,500 to 4,000 character range.

This is a detailed design proposal. New balance values, capacities, content situations, reward conditions, and the rare Flying City super-event are proposed expansions. The user's catalog entry, existing route, 121 two-day transitions, controller-based host rules, real deaths, immediate foreign-controller war, and named evolutions remain fixed.

## Specifications

| Part | File | Content |
|---|---|---|
| 1 | [Core voyage](080_airship_spec_part_1_core.md) | Identity, launch, route, timing, stops, diversions, phases, and endings |
| 2 | [Condition and operations](080_airship_spec_part_2_condition_and_operations.md) | Condition, incident model, standing orders, service costs, missions, and AI |
| 3 | [Passengers and hosts](080_airship_spec_part_3_passengers_and_hosts.md) | Population-backed manifest, 36 passenger situations, 24 host situations, and story continuity |
| 4 | [War, crashes, and rescue](080_airship_spec_part_4_war_crashes_and_rescue.md) | Combat encounters, capture, casualty profiles, state damage, immediate war, fires, and rescue |
| 5 | [Evolutions and experiments](080_airship_spec_part_5_evolutions_and_experiments.md) | Grand Tour, Experimental Flight, Flying City, six trial families, and exposure-based rewards |
| 6 | [Rewards, Chaos, and achievements](080_airship_spec_part_6_rewards_chaos_and_achievements.md) | Success and failure benefits, host rewards, complete Chaos map, shared connections, and eight achievements |
| 7 | [Map and presentation](080_airship_spec_part_7_map_and_presentation.md) | Existing map, native interface, ship forms, scene inventory, news, super-event, and writing direction |

## Ready prompts

| Prompt | File |
|---|---|
| Main implementation | [Coding prompt](080_airship_coding_prompt.md) |
| Goal instruction | [Goal prompt](080_airship_goal_prompt.md) |
| Visual production | [Asset prompt](080_airship_asset_prompt.md) |
| Operations and AI audit | [Decision and mission prompt](080_airship_decision_mission_prompt.md) |
| Achievement implementation and icons | [Achievement prompt](080_airship_achievement_prompt.md) |
| Rare catastrophe presentation research | [Super-event prompt](080_airship_super_event_prompt.md) |

## Supporting handoffs and evidence

[Implementation handoff](080_airship_implementation_handoff.md) defines the owner boundaries and important integration gates. [Specialist handoffs](080_airship_specialist_handoffs.md) give bounded assignments for the actual agent environment. [Validation matrix](080_airship_validation_matrix.md) contains 64 functional fixtures and 16 probability scenario groups. [Risk arithmetic](080_airship_risk_arithmetic.md) checks only the illustrative fixed-Condition formula and is not a probability-tool audit.

[Route crosswalk](080_airship_route_crosswalk.md) preserves all inspected legacy indices from departure 0 through return 121. It contains region predicates, not fabricated state IDs or city stops. Exact geographic binding remains required.

[Research and source report](080_airship_research_and_source_report.md) records all reading, repository inspection, source conflicts, historical research leads, and outstanding gates. The [supplied-source reading ledger](080_airship_supplied_source_read_ledger.json) includes the exact file hashes and completed reading coverage.

## Reading and execution limits

All 42 supplied text files were read in full, including all twenty subagent definitions. They total 1,202,682 bytes and 14,072 lines. Externally referenced required resources were not all available or fully read. These include the original map files, exact state and stop bindings, installed vanilla sources, offline wiki, actual canonical visual references and processors, the dedicated MTTH skill, the authoritative workbook, and complete shared custody and fire implementation contracts.

No provided subagent was launched. No HOI4 MCP probability, GUI, technology, or runtime test was performed. No finished artwork, final super-event quotation or audio, source-code implementation, or workbook edit was produced. The package gives the complete planned design and the exact work needed to close those gaps. It does not label missing evidence as a passed check.
