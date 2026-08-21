# Event 20 Black Plague Planning Package

> Accepted corrections, 2026-08-09 and 2026-08-21: Event 020 has a dedicated national cure and strategic-management decision category in addition to the shared disease-containment category. State-selected containment remains on the shared board; cure research, medical logistics, cooperation, knowledge policy, and recovery use the dedicated category. The dedicated category also mounts a compact, read-only Event 020 scripted GUI for its three live response values. These later corrections supersede every older “no dedicated category” or “text-only category” statement in the historical design pack. See [`corrections/2026-08-09_dedicated_response_category.md`](corrections/2026-08-09_dedicated_response_category.md) and [`corrections/2026-08-21_dedicated_response_scripted_gui.md`](corrections/2026-08-21_dedicated_response_scripted_gui.md).

> Documentation reconciliation, 2026-08-06: this package remains the accepted full-design source. The current gameplay tranche registers the Diseases cluster, the public Black Plague world-end row, exactly two runtime Rat tags (`RTA` and `RTX`), SCN-012, the shared workbook row, the wired report chain, five dedicated Event 020 report-card families plus the Doctor Wu bridge, fourteen public achievement contracts with their icon triplets, and route-gated Rat King policy lanes for all three governments. The source-frame Rat King portrait, Royal Burrows seal, Severe/Collapsed crisis seal, and Rat King terminal-readiness seal packages, the dedicated weapon-delivery icon, and the three 44.1 kHz Event 020 audio WAVs are promoted static evidence. Full-design completion remains partial because broader route depth, additional crisis/Doctor Wu/route presentation, release attribution, and live validation still require disposition. One shared rat ground-unit 3D package is now promoted for the RTA/RTX runtime consumers; no per-subtype or separate Rat King model is authorized. Its worker evidence and static runtime registration are recorded in [`docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-05_event020_rat_shared_3d_model_handoff.md`](../../plans/020_black_plague_plans/subagent_handoffs/2026-08-05_event020_rat_shared_3d_model_handoff.md), while sound-definition wiring, counter review, and live in-game validation remain open. Current status is documented in [`docs/events/020_black_plague/overview.md`](../../events/020_black_plague/overview.md) and the dated documentation reconciliation handoff. The package must not be read as either a no-code claim or a whole-spec completion claim.

This folder is the complete source specification for the Black Plague rework.

## Core design

Event 20 begins naturally in one weighted vulnerable mainland state. The disease kills real population over time, spreads through state and transport routes, uses the shared disease and biological warfare interface, supports non-instant countermeasures and a long weaponization project, evolves into a reusable `RTA` Rat Nation carrier and a sentient `RTX` Rat King, and can end in a terminal Rat King world takeover. A separate triggerable scenario can immediately seed many states on several continents, activate Evolutions I through IV, and create or preserve one `RTA` carrier with internal brood state markers plus the separate `RTX` Royal Basin for an instant global challenge.

The later correction in `corrections/2026-07-29_two_rat_tags.md` supersedes all multi-tag Rat Nation requirements. Runtime country identity is limited to the reusable Rat Nation `RTA` and the separate Rat King `RTX`.

The later correction in `corrections/2026-08-09_dedicated_response_category.md` supersedes the historical single-category rule. Runtime response ownership is one dedicated Black Plague national-response category plus the existing shared selected-state disease-containment category.

The later correction in `corrections/2026-08-21_dedicated_response_scripted_gui.md` supersedes the historical text-only presentation rule. The dedicated category uses one read-only Event 020 dashboard without moving or duplicating any gameplay action.

## Read order

1. `corrections/2026-07-29_two_rat_tags.md`, `corrections/2026-08-09_dedicated_response_category.md`, and `corrections/2026-08-21_dedicated_response_scripted_gui.md`
2. `specs/020_black_plague_spec_part_1_core_crisis.md`
3. `specs/020_black_plague_spec_part_2_crisis_board_and_containment.md`
4. `specs/020_black_plague_spec_part_3_cure_spread_and_biowarfare.md`
5. `specs/020_black_plague_spec_part_4_evolutions_and_rat_emergence.md`
6. `specs/020_black_plague_spec_part_5_rat_nations.md`
7. `specs/020_black_plague_spec_part_6_rat_king.md`
8. `specs/020_black_plague_spec_part_7_world_end_and_aftermath.md`
9. `specs/020_black_plague_spec_part_8_ai_balance_assets_and_acceptance.md`
10. `specs/020_black_plague_spec_part_9_triggerable_scenario.md`
11. supporting matrices and focus graphs
12. production prompts
13. research notes
14. review and limitation files

## Folder map

- `corrections/`: later acceptance criteria that override conflicting historical text
- `specs/`: accepted event design
- `matrices/`: detailed state, decision, evolution, country, AI, triggerable-scenario, achievement, asset, tuning, catalog, and acceptance tables
- `focus_graphs/`: route and state-flow diagrams
- `prompts/`: asset, super-event, achievement, decision, coding, and goal prompts
- `research/`: source ledger, research notes, quote and audio leads, bibliography
- `review/`: improvement closure, manual role reviews, source-of-truth map, limitations, and completion audit

## Important implementation boundaries

- All labels in the specs are working labels unless a research note identifies a verified quote candidate.
- Final localisation is written during implementation.
- The live repository, offline wiki, and vanilla HOI4 installation must be inspected before final IDs, file paths, tags, GUI anchors, sprite names, or helper names are chosen.
- Established Black Plague states must use a black base colour in the existing disease mapmode. Black fog remains a separate engine-dependent prototype.
- Rat Nations and the Rat King are supernatural alternate-history evolutions, not claims about ordinary plague biology.
- Biological weapon mechanics remain abstract and nonprocedural.

## Package status

This is a complete planning handoff for the full design, with a separate core-stabilization implementation tranche documented by the current Event 020 overview and readiness report. The current goal accepts the exactly-two-tag boundary: `RTA` is the reusable Rat Nation carrier, `RTX` is the separate Rat King, internal broods remain state markers, and one shared rat ground-unit model/entity package serves the six locked RTA/RTX unit consumers. Per-subtype and separate Rat King models remain out of scope. The live focus surfaces are recorded as 52 RTA nodes and 71 RTX nodes. The `.45` hierarchy acknowledgement, scoped defeat participant hooks, duration/peak/deaths/major-participant gate, resolver-owned `.72`, slot-087 art/text/audio/sprite/sound package, source-frame Rat King portrait and Royal Burrows, crisis-seal and terminal-readiness packages, dedicated weapon-delivery icon, native last-response missions, and three 44.1 kHz Event 020 audio WAVs are promoted static evidence; model sound-definition wiring, counter review, live runtime validation, broader narrative, presentation depth, workbook, release attribution, and live balance-validation surfaces remain incomplete.
