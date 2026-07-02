# Event 014 Parent Follow-Up Resolution

Date: 2026-07-01

This note records parent-agent fixes applied after the final completion, focus-tree, decision-mission, country-package, localisation, and asset audit handoffs.

## Resolved Audit Findings

- Restored and protected `gfx/leaders/014_cannibalism/hannibal.dds`; its verified SHA256 is `5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88`.
- Removed live use of procedural/simple-shape Event 014 animation assets and replaced the runtime animation set with imagegen frame-sheet packages under `docs/assets/014_cannibalism/animations_imagegen/`.
- Added `_shine` focus sprite registrations for Event 014 focus icons in `interface/014_cannibalism.gfx`.
- Added route-aware CBL focus AI weights and custom trigger tooltips for `cbl_empty_larder_war_discipline`, `cbl_proclaim_the_last_table`, and `cbl_world_as_larder_gate`.
- Converted Event 014 response mission target state flags to country-targeted flags and documented cancellation/cleanup behavior.
- Tightened `Burn the Cookbooks` so archive progress counts distinct countries and excludes exploitation, CBL, and the Cannibal Pact route.
- Tightened `Hunger of Hannibal` so the unlock requires Hannibal or an accepted unifier, the revealed global table, enough network strength, enough cult nodes, enough communes, and no world-end route start.
- Tightened `After the Feast` so the unlock requires the global/Hannibal-linked threat to be defeated and the paid `cannibalism_aftermath_cleanup` decision to complete before world-end starts.
- Changed `cannibalism_exploit_terror_units` AI from availability-driven low weight to zero base weight with positive weight only under crisis/desperation conditions.
- Implemented `SCN-009: Cannibalism` in the Triggerable Scenarios system with War Horror Opening, Cult Seeds, Silent Islands, Cannibal Commune, and Hannibal Network types. The launch path suppresses the Event 014 fire-once slot, scopes and clears temporary scenario context, preserves the original report path for War Horror Opening, uses Event 014 outbreak/evolution/commune/Hannibal helpers for advanced starts, and keeps Hannibal Network locked behind Hannibal/unifier or the explicit test bypass flag.

## Remaining Review Scope

The parent still needs to run the final focused validation and, if clean, request/perform a final completion audit before any completion claim.
