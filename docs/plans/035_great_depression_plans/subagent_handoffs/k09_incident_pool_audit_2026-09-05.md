# Event 35 K-09 incident-pool probability audit

## Scope

This handoff records the supported HOI4 probability-service audit for the Event 35 incident pools requested by acceptance scenario K-09.

The audit uses the `custom_weighted_pool` adapter with an explicit, audit-only manifest named `event35.k09.incident_pools`.

The manifest is not a second runtime registry and does not execute or replace the Clausewitz random lists in `common/scripted_effects/035_great_depression_incident_effects.txt`.

## Declared pool

The manifest contains 59 candidates: the 52 source incident kinds and seven stage-specific `no_incident` fallbacks.

The categorical timer uses a 21-day cadence and mirrors the source weights from `common/script_constants/035_great_depression_constants.txt` for common, uncommon, rare, major, severe, positive, and no-incident outcomes.

The declared gates cover active depression state, usable centers, distressed regions, project availability, partner and supplier relationships, evolution thresholds, organized actors, bank audit, obligations, emergency credit, clearing membership, deployed forces, humanitarian pressure, force packages, recovery plans, regional movement, contagion exposure, coup/separatist/civil-conflict thresholds, extreme-crisis review, and last-kind cooldown exclusion.

## MCP evidence

Source inspection returned `PROBABILITY_SOURCE_INSPECTED` with artifact `probability-inspect-a35e848d0bba.json`, source revision `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`, source hash `a35e848d0bba357b565a11c7b5b77b4e8d99a370c63cf7d8e40020939517458a`, 59 candidates, and zero unresolved inputs.

The complete evaluation is analysis `probability-00c43d73f98109724cc77856` with scenario hash `8ebb73c646d4ae42bd3f897b569440f533e376a67a6fd73dcdeb9cc6ee34b100`.

It evaluates 84 scenarios and 4,956 candidate-scenario rows with `analysisStatus = complete`, zero unresolved inputs, and two expected diagnostics.

The scenarios cover Severity values 10, 50, 70, 85, and 95 across evolution levels 0 through III, contagion at evolution I through III, Social Collapse across both applicable evolutions and all four organized stages, the extreme incident pool at evolutions II and III, and explicit invalid-target, invalid-partner, invalid-actor, closed-extreme, and no-regional-movement gates.

The only dominance diagnostics are the expected fail-closed `no_incident` outcomes for `K09-GATE-NO-TARGET` and `K09-GATE-NO-PARTNER`.

Ranking evidence is `probability-probability-00c43d73f98109724cc77856-ranking.svg` with its corresponding PNG, matrix evidence is `probability-probability-00c43d73f98109724cc77856-matrix.svg` with its corresponding PNG, and the unresolved-input view is available as the matching unresolved SVG and PNG.

## Boundary

The native source adapter cannot infer the custom incident pool from Clausewitz random-list effects, so the earlier native inspection correctly reported zero candidates and `poolComplete = false`.

The manifest result proves complete declared candidate and gate coverage for the K-09 audit contract, but it is not a normalized runtime probability receipt for the gameplay random-list effects or their downstream event effects.

No gameplay file was changed by this audit.
