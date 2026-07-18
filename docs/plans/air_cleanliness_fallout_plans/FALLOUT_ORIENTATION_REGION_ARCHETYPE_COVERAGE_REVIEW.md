# Fallout Orientation Region and Archetype Coverage Review

Date: 2026-07-18

Status: source design complete, runtime coverage not implemented

## Authority reviewed

The review used the accepted Ash-week orientation contract, the live `fallout_region` and `fallout_government_archetype` script constants, the regional event bible, the government archetype event bible, and both existing thematic event matrices.

The source matrix is:

`docs/specs/air_cleanliness_fallout_specs/matrices/fallout_orientation_region_archetype_coverage_matrix.md`

## Coverage result

The source matrix contains nine live region sections. Every section contains all twelve live government archetypes exactly once. The result is 108 manually written cells.

Each cell records:

- national-authority language
- capital-condition emphasis
- local resource response
- government institution or rival
- candidate character or institution class
- meaningful AI preference
- branch prohibition tied to missing world-state evidence

The cells use regional infrastructure, food systems, water systems, transport, shelter conditions, and authority disputes. AI preferences respond to the same local evidence. Branch prohibitions are hard vetoes when a route, institution, resource, receiving state, safety row, or other named dependency is absent. Mutant-polity rows are explicitly fictional. Religious and historical institution classes require country and subregional research before final localisation.

## Region identity reconciliation

The live region ids separate South Asia from Middle East and North Africa. They also separate Sub-Saharan Africa and use Latin America and Caribbean. The earlier thematic event matrix combined or named some of those regions differently.

The source specs now identify the live nine-region list as the Ash-week eligibility authority. Polar and remote stations are route overlays that inherit a live region. They are not a tenth runtime id.

## Deliberate non-activation

This review does not create runtime regional rows, archetype rows, country-memory rows, or approval setters. It does not wire the orientation caller or the living-world scheduler. The dormant package continues to fail closed.

The following work remains before any coverage approval variable can be set:

1. research and write country-memory overlays for the selected successor pool
2. choose researched local institutions and final player-facing text
3. implement deterministic regional and archetype row producers
4. implement the other nineteen reserved event blocks with AI, delayed results, memory, and cleanup
5. complete exact capital repair and the character or institution registries
6. wire event log and detail surfaces
7. run the required focused audits

The caller remains additionally blocked by successor allocation, player continuation, and candidate registry proof.
