# Limitations, Blockers, and Honest Scope Disclosure

## Fully read sources

Every project source file supplied in `/mnt/data` was read in full. The final inventory is 30 files, correcting an earlier interim progress count of 28. The source ledger lists every file, byte count, line count, and SHA-256.

## Unavailable project sources

The following implementation references were not mounted and therefore were not read:

- the live Chaos Redux repository beyond the supplied files
- the repository offline `paradox_wiki/` snapshot
- the local Windows Hearts of Iron IV installation
- vanilla HOI4 documentation and gameplay files
- live disease GUI, mapmode, scenario, special-project, focus, decision, and country-package files
- live asset reference folders

This historical limitation was resolved for the current tranche by inspecting the live runtime surfaces before wiring the two-tag package, shared category, public scenario row, and mapmode hooks. Final asset sprite names and engine-supported black-fog wiring still require their dedicated verification pass.

## Custom subagent tooling

All 16 supplied subagent contracts were read and their standards were applied manually. No project custom subagent spawn tool was available, so no subagent was actually launched. The manual role reviews are labeled honestly.

## Asset status

No final image, icon, portrait, flag, DDS, TGA, frame sheet, or animation was produced. The package supplies the asset inventory and production prompt. Final production belongs to implementation and the project asset roles.

## Audio status

No audio file was downloaded or converted. The package records verified research leads. Final audio still requires source verification, download, editing, 44.1 kHz conversion, attribution, and wiring.

## Mapmode and black fog

The existing disease mapmode must render every established Black Plague state with a black base colour. This is a mandatory design requirement, not an optional visual. Its final resolver hook and overlay method remain unverified until the live GUI and scripted mapmode files are inspected.

State-attached black fog remains technically uncertain. The spec requires a real prototype and a reproducible blocker report if the live engine cannot support it safely. Failure of the fog prototype does not permit failure of the black mapmode colour.

## Triggerable scenario

The scenario design is complete, but the proposed `SCN-008` identifier, registry sort value, exact intensity constants, tag capacity, and bootstrap helper names are provisional. Live implementation must check conflicts and preserve the existing data-driven scenario UI. The scenario must remain idempotent and must not set Evolution V or `world_end`.

## Balance status

The package provides outcome bands, tuning targets, and 20 balance or scenario cases. It does not claim in-game balance or performance testing because no live game or implementation exists here. The Maximum scenario, mass mapmode rebuild, simultaneous Rat Nations, and Rat King coexistence need dedicated performance testing.

## Catalog and spreadsheet status

The supplied CSV catalogs were read and the live workbook was updated after final runtime localisation. The exported CSVs remain derived snapshots; future event-content changes must continue to update the workbook first and then run the exporter.

## Simplification disclosure

The planning output was not shortened for speed. It includes nine main spec parts, detailed matrices, prompts, research notes, focus graphs, and review files.

Deliberate design boundaries are:

- no dedicated Black Plague decision category, while Black Plague-specific decisions appear inside the shared disease category
- one shared base Rat Nation tree with four archetypes instead of one full tree per reusable tag
- no normal human diplomacy for rat countries
- black fog remains an engine-dependent enhancement
- the triggerable scenario starts Evolutions I through IV but does not grant Evolution V or terminal victory
- the defeat aftermath super-event remains gated behind global-crisis conditions

No requested correction was omitted from the revised planning package.
