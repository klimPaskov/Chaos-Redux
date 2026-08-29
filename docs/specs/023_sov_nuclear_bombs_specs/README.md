# Event 023: SOV Nuclear Bombs specification package

This folder is the source specification package for Chaos Redux Event 23, `SOV Nuclear Bombs`.

The intended repository destination is `docs/specs/023_sov_nuclear_bombs_specs/`.

The package preserves the user-defined premise that Soviet scientists secretly complete an arsenal and the Soviet Union receives exactly 100 nuclear bombs at the baseline opening. It expands that premise into an event-owned command, testing, production, coercion, targeting, collapse-custody, and escalation system while leaving blast damage, deaths, fallout, condemnation, Air Cleanliness, and terminal Fallout progression to the existing shared nuclear consequence systems.

## Event identity

| Field | Specification |
| --- | --- |
| Event ID | `23` |
| Stable slug | `sov_nuclear_bombs` |
| Entry event | `chaosx.nr23.1` |
| Type | Minor Fire-Once |
| Planned chaos level | `2`, Gathering Storm, 200 or more Chaos |
| Current catalog status | Unavailable, To Be Reworked |
| Planned cluster identity | `Arms-race`, registration deferred until a verified stable cluster ID and at least one other reworked member exist |
| World-end ownership | None, nuclear use may contribute to the shared Fallout route |
| Primary actor | The Soviet Union, `SOV` |
| Core opening grant | Exactly 100 nuclear bombs at baseline, with stronger pre-fire packages at later evolution stages |

## Design non-negotiables

- Event 23 remains the Soviet nuclear breakthrough and does not absorb Event 32 `Missiles`, Event 76 `USA tests weapons`, Event 47 `BOOM`, Event 5 `Soviet Union Collapse`, the shared Fallout scenario, or any shared nuclear strike consequence logic.
- A nuclear stockpile does not create instant unrestricted use. Delivery readiness, command integrity, exact target validity, authorization, war state, cooldowns, and shared consequence routing control practical use.
- The Soviet Union can threaten and pressure countries, including Soviet breakaways after Evolution II, but the target receives meaningful responses and can refuse, delay, seek protection, disperse, publicize the threat, or offer a partial settlement.
- Nuclear threats are not automatic victory buttons. Credibility, target strength, foreign backing, Soviet military position, command integrity, and prior behavior determine whether coercion works.
- Below 1000 Chaos, Soviet AI may use a limited weapon against a nonnuclear enemy or breakaway only under severe and bounded conditions. It does not deliberately initiate a major-to-major nuclear exchange below Evolution IV.
- At 1000 or more Chaos, Soviet AI first use against a nuclear major becomes possible under narrow strategic-loss conditions. High Chaos alone is insufficient.
- Every detonation, whether a test or combat use, must route through a shared nuclear test or strike adapter that owns real population loss, fallout, contamination, condemnation, and death logging.
- The first multi-major exchange receives a distinct nonterminal super-event. It does not set `world_end`, replace Fallout, or reuse the manual Final Silence scenario as a substitute.
- The event does not create a new Soviet focus tree, custom country, flag, portrait, custom unit, 3D model, or full scripted GUI.
- The primary presentation is an ordinary decision category with one static category picture, concise dynamic values, clear tooltips, and phased visibility.
- All labels in this package are working design labels unless a file explicitly says otherwise. The implementation agent must write final player-facing localisation from the defined direction and must not paste working labels as final text without a localisation pass.

## Package map

| File | Purpose |
| --- | --- |
| `023_sov_nuclear_bombs_spec_part_1_core.md` | Event promise, availability, opening, custody doctrines, lifecycle, and information rules |
| `023_sov_nuclear_bombs_spec_part_2_arsenal_command_and_production.md` | Arsenal Readiness, Command Integrity, posture, storage, reactors, assembly, delivery preparation, and idea lifecycle |
| `023_sov_nuclear_bombs_spec_part_3_testing_secrecy_and_foreign_reaction.md` | Test programs, secrecy, discovery, public reveal, foreign reactions, and rare incidents |
| `023_sov_nuclear_bombs_spec_part_4_targeting_coercion_and_use.md` | Target selection, demands, ultimata, target responses, strike profiles, authorization, and use limits |
| `023_sov_nuclear_bombs_spec_part_5_evolutions_and_exchange.md` | Evolution I through IV, pre-fire evolved openings, active evolution pacing, major exchange, AI first-use boundaries, and off-ramps |
| `023_sov_nuclear_bombs_spec_part_6_soviet_collapse_integration.md` | Event 5 bridge, storage-site custody, breakaway devices, foreign intervention, settlement routes, and cleanup |
| `023_sov_nuclear_bombs_spec_part_7_shared_systems_cross_event_and_cluster.md` | Shared nuclear consequence ownership, Fallout connection, event hooks, cluster contract, logs, and global threat state |
| `023_sov_nuclear_bombs_spec_part_8_presentation_localisation_and_assets.md` | Decision-category presentation, visual asset inventory, writing direction, accessibility, and information visibility |
| `023_sov_nuclear_bombs_spec_part_9_ai_probability_balance_and_exploits.md` | AI behavior, probability scenarios, tuning anchors, exploit controls, multiplayer, and validation expectations |
| `023_sov_nuclear_bombs_spec_part_10_achievements_acceptance_and_closure.md` | Achievement set, acceptance scenarios, DLC compatibility, closure review, and completion conditions |
| `023_sov_nuclear_bombs_decision_map.md` | Structured decision and mission families with costs, risks, pacing, AI intent, and cleanup |
| `023_sov_nuclear_bombs_probability_scenarios.md` | Named probability and timing scenarios for the mandatory AI audit workflow |
| `023_sov_nuclear_bombs_technology_and_dlc_notes.md` | Current-vanilla nuclear capability integration, reactor handling, DLC fallbacks, and technology graph checks |
| `023_sov_nuclear_bombs_catalog_alignment_notes.md` | Draft catalog alignment, cluster status, and the supplied scenario-catalog discrepancy |
| `023_sov_nuclear_bombs_research_notes.md` | Historical, scientific, command-control, coercion, humanitarian, and post-Soviet custody research |
| `023_sov_nuclear_bombs_source_and_audit_report.md` | Provided-file reading record, tooling limits, source hierarchy, and simplification disclosure |
| `023_sov_nuclear_bombs_asset_prompt.md` | Bounded prompt for final asset production |
| `023_sov_nuclear_bombs_decision_mission_prompt.md` | Bounded prompt for decision and mission implementation and audit |
| `023_sov_nuclear_bombs_super_event_prompt.md` | Research and implementation prompt for the multi-major exchange super-event |
| `023_sov_nuclear_bombs_achievement_prompt.md` | Full achievement implementation and asset prompt |
| `023_sov_nuclear_bombs_coding_prompt.md` | Implementation prompt for the complete event rework |
| `023_sov_nuclear_bombs_goal_prompt.md` | Repository goal prompt, kept within the required character limit |

## Extraction and use

Extract the top-level folder directly into `docs/specs/` so the resulting path is `docs/specs/023_sov_nuclear_bombs_specs/`.

The implementation agent must inspect the current repository, the existing Event 23 baseline, the installed vanilla nuclear systems, the offline wiki snapshot, current event-log and evolution helpers, the Event 5 implementation, shared nuclear consequence APIs, and current super-event registry before editing. The package defines accepted design. It does not claim that current file identifiers, event slots, sprite paths, or helper names have already been verified in the live repository.

## Package verification

- Markdown files in package: 23.
- Goal prompt length: 3,912 characters.
- No final implementation files, binary assets, or temporary continuation prompts are included.
- The source and audit report records every provided file read, external research used, source discrepancy, tooling limit, and simplification statement.
