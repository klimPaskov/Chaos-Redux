# Limitations, Blockers, and Honest Scope Disclosure

> Documentation reconciliation, 2026-08-06: the unavailable-source statements below preserve the historical planning-package context. Current static evidence supersedes any blanket no-implementation reading: exactly `RTA` and `RTX` remain the only runtime Rat tags, the RTA/RTX focus surfaces are documented as 52/71 nodes, the last-response pair is native mission data, the dedicated weapon-delivery icon, Rat King portrait, Royal Burrows seal, Severe/Collapsed crisis seal, and Rat King terminal-readiness seal packages are promoted, and three Event 020 WAVs are 44.1 kHz. One shared rat ground-unit model/entity package is promoted for six RTA/RTX subunits and five locked templates, with no per-subtype or separate Rat King model. Sound-definition wiring, counter review, live game, playback, balance, and release-attribution checks remain open.

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

This historical limitation was resolved for the current tranche by inspecting the live runtime surfaces before wiring the two-tag package, shared category, public scenario row, mapmode hooks, scoped defeat hooks, and slot-087 package. Engine-supported black-fog wiring and live consumer validation still require their dedicated verification pass.

## Custom subagent tooling

All 16 supplied subagent contracts were read and their standards were applied manually. No project custom subagent spawn tool was available, so no subagent was actually launched. The manual role reviews are labeled honestly.

## Asset status

The historical planning package supplied only inventories and prompts. The current Event 020 tranche promotes final report/news assets, slot-087 art, the source-frame Rat King portrait, the source-frame Royal Burrows seal, the Severe/Collapsed crisis seal, the Rat King terminal-readiness seal, and the dedicated weapon-delivery icon. Broader crisis-report, Doctor Wu, route/hierarchy, and aftermath presentation remains incomplete. Final asset provenance, release attribution, and live validation remain implementation-owned.

## Audio status

The historical planning package supplied research leads only. The current tranche promotes final 44.1 kHz audio IDs 101, 102, and 103 with shared wrappers and catalogue evidence; CC BY-SA release attribution and live playback validation remain open.

## Mapmode and black fog

The existing disease mapmode must render every established Black Plague state with a black base colour. This is a mandatory design requirement, not an optional visual. Static inspection confirms the black base resolver and phase/containment/weaponization/rat-control overlay hooks; live map rendering remains user validation. State-attached black fog remains technically uncertain.

State-attached black fog remains technically uncertain. The spec requires a real prototype and a reproducible blocker report if the live engine cannot support it safely. Failure of the fog prototype does not permit failure of the black mapmode colour.

## Triggerable scenario

The scenario design is complete and the live implementation uses `SCN-012` with the corrected two-tag contract. The scenario remains idempotent, preserves or creates only the accepted `RTA` and `RTX` actors, and must not set Evolution V or `world_end`; focused launch and lifecycle validation remains open. The preflight fails closed and clears reservation markers on downstream failure, but a full journaled rollback of already-applied disease, transfer, country, and Chaos mutations is still an explicit blocker.

## Balance status

The package provides outcome bands, tuning targets, and 20 balance or scenario cases. It does not claim in-game balance or performance testing because the game was not launched in this workflow. The Maximum scenario, mass mapmode rebuild, simultaneous internal RTA broods, and Rat King coexistence need dedicated performance testing.

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
- one shared rat ground-unit model/entity package is promoted for the six locked RTA/RTX unit consumers; per-subtype and separate Rat King models remain out of scope, and parent-owned sound definitions, counter review, and live in-game validation are still open

No requested correction was omitted from the revised planning package.
