# Event 033 Acid Rain specification package

## Event identity

| Field | Accepted value |
| --- | --- |
| Event ID | `33` |
| Event slug | `acid_rain` |
| Event name | Acid Rain |
| Event type | Major |
| Status | To Be Reworked |
| Chaos level | 2, Gathering Storm minimum |
| Cluster | Natural Disasters |
| Cluster role | Severe optional member |
| Ordinary endpoint | Dissipation after complete valid-state coverage |

This package is the implementation-ready planning source for the Event 33 rework. It replaces the old minor-repeatable interpretation and the existing prototype that paints one continent, scans every country each day, and ends after seven continent identifiers have been recorded.

## Accepted event concept

An anomalous and potentially supernatural acid-rain system forms over one world region and moves through changing state footprints. The rain is intrinsically lethal. Direct exposure, corrosive aerosol, poisoned runoff, and the collapse of exposed services kill civilians. Every opening shock and sustained mortality pulse removes real civilian population from each affected state, then records the exact applied loss in the shared Deaths system. Transport damage, building damage, supply penalties, and environmental aftermath occur alongside those population losses. The system records exact state coverage and cannot become eligible to dissipate until every frozen valid state has been touched at least once.

A `local_manpower` penalty, recruitable-population modifier, casualty counter, or report text never counts as mortality. The population visible in the state must fall by the same amount that Event 33 records as applied civilian deaths, subject only to the protected population floor and the accepted pulse and episode caps.

## Package map

The `specs` directory defines the player loop, runtime contract, movement model, losses, decisions, interface, evolutions, AI, presentation, assets, integrations, and acceptance rules.

The `matrices` directory provides compact handoff tables for front states, decision costs, AI cases, requirement traceability, and the exact state-population loss contract.

The `research` directory records environmental and material references, the quote source, the audio candidate, and the visual reference set. These references inform corrosion, runoff, protection, and presentation. They do not limit the anomaly's fictional lethality.

The `docs_alignment` directory gives the exact catalog and cluster corrections required by the accepted concept.

The `implementation_readiness` directory maps the planned system to repository files and defines migration from the current prototype.

The `quality` directory records the final design review and the changes made after testing the first draft.

The `prompts` directory contains the required specialist handoffs for art, super-event work, achievements, decisions and missions, implementation, and the final goal prompt.

## Recommended implementation order

1. Register Event 33 as a Major event at Chaos level 2 and remove its repeatable registration.
2. Add constants, stable region identifiers, runtime schema, and the frozen eligible-state registry.
3. Implement one-front baseline movement and exact state coverage before adding damage.
4. Add the bounded three-day exposure pulse, exact state-population transactions, mortality receipts, building pressure, and aftermath state.
5. Add national Preparedness, projects, emergency actions, recovery work, and AI rules.
6. Add the Acid Rain Air Contamination source and both hard caps.
7. Add Severe Storm Cells, Multiple Weather Fronts, and Global Acid Rain in order.
8. Add the scripted GUI, reports, super-event, audio, assets, achievements, and documentation.
9. Add Natural Disasters cluster integration and mixed Major pacing only after independent firing is stable.
10. Run the complete acceptance matrix, probability inspection, multiplayer checks, and save migration tests.

## Core implementation rules

- Never restore the old daily all-country and all-owned-state scan.
- Build the world registry once at event start, then process only event-owned arrays.
- Keep world coverage and national Preparedness as the two active player-facing values.
- Track Event 33 contamination additions in basis points and clamp the actual applied delta.
- For every positive mortality pulse, call `apply_exact_state_civilian_population_loss`, reduce real state population by the returned applied amount, and send that same amount through the shared Deaths system exactly once.
- Never accept `local_manpower`, recruitable-population penalties, generic manpower loss, unit attrition, or a counter-only change as a substitute for state population removal.
- Let the Deaths and Air Cleanliness systems generate their ordinary Chaos effects. Event 33 must not duplicate them.
- Unlocking an evolution never creates Chaos by itself.
- Preserve an eventual guaranteed endpoint after the coverage condition is met.
- Keep all tuning in constants and verify weighted behavior with the repository probability tools.
