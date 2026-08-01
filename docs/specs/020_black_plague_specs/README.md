# Event 20 Black Plague Planning Package

> Documentation reconciliation, 2026-08-01: this package remains the accepted full-design source. The current gameplay tranche registers the Diseases cluster, the public Black Plague world-end row, the two-tag Rat lifecycle, SCN-012, the shared workbook row, the wired report chain, fourteen public achievement contracts, and route-gated Rat King policy lanes for all three governments. Full-design completion remains partial because broader route depth, route-specific AI strategy plans, achievement icon presentation, selected asset expansions, and explicitly superseded multi-tag surfaces still require disposition. Current status is documented in [`docs/events/020_black_plague/overview.md`](../../events/020_black_plague/overview.md) and the Event 20 audit handoff. The package must not be read as either a no-code claim or a whole-spec completion claim.

This folder is the complete source specification for the Black Plague rework.

## Core design

Event 20 begins naturally in one weighted vulnerable mainland state. The disease kills real population over time, spreads through state and transport routes, uses the shared disease and biological warfare interface, supports non-instant countermeasures and a long weaponization project, evolves into Rat Nations and a sentient Rat King, and can end in a terminal Rat King world takeover. A separate triggerable scenario can immediately seed many states on several continents, activate Evolutions I through IV, and create independent Rat Nations plus the Rat King for an instant global challenge.

The later correction in `corrections/2026-07-29_two_rat_tags.md` supersedes all multi-tag Rat Nation requirements. Runtime country identity is limited to the reusable Rat Nation `RTA` and the separate Rat King `RTX`.

## Read order

1. `specs/020_black_plague_spec_part_1_core_crisis.md`
2. `specs/020_black_plague_spec_part_2_crisis_board_and_containment.md`
3. `specs/020_black_plague_spec_part_3_cure_spread_and_biowarfare.md`
4. `specs/020_black_plague_spec_part_4_evolutions_and_rat_emergence.md`
5. `specs/020_black_plague_spec_part_5_rat_nations.md`
6. `specs/020_black_plague_spec_part_6_rat_king.md`
7. `specs/020_black_plague_spec_part_7_world_end_and_aftermath.md`
8. `specs/020_black_plague_spec_part_8_ai_balance_assets_and_acceptance.md`
9. `specs/020_black_plague_spec_part_9_triggerable_scenario.md`
10. supporting matrices and focus graphs
11. production prompts
12. research notes
13. review and limitation files

## Folder map

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

This is a complete planning handoff for the full design, with a separate core-stabilization implementation tranche documented by the current Event 020 overview and readiness report. It does not claim that the shared registry gaps, deferred narrative, presentation, bespoke 3D, workbook, or live balance-validation surfaces are complete.
