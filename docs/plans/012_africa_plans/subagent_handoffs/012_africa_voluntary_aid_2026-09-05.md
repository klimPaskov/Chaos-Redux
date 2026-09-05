# Event 012 voluntary aid implementation handoff

## Disposition

Implemented source surface; live balance, MCP scenario projection, and in-game playback remain bounded acceptance work.

## Runtime evidence

- `common/script_constants/012_africa_gods_constants.txt` owns the 180-day cooldown, 500-unit equipment and fuel packages, protected 1,000-unit sender capacity, and first/repeat Wrath reductions.
- `common/scripted_triggers/012_africa_gods_triggers.txt` exposes `gods_of_africa_participant_can_offer_aid`. It requires a current participant generation, no active demand, no war with Africa, no defiance or terminal outcome, a current host need, and an affordable land-equipment or fuel branch.
- `common/scripted_effects/012_africa_gods_effects.txt` owns `gods_of_africa_offer_voluntary_aid`. It rechecks the trigger, debits the participant's real stockpile, credits the host, refreshes the host need profile, records `aid` history, applies diminishing Wrath relief, applies one reliable-partner memory, and opens the participant receipt.
- `common/decisions/012_africa_gods_decisions.txt` exposes one participant action with a concrete two-resource cost line and state-aware AI willingness.
- `events/012_africa_gods_of_africa.txt` and `localisation/english/012_africa_gods_l_english.yml` provide the separate `chaosx.nr12.614` receipt and all player-facing text.

## Boundaries

The action intentionally supports the two maintained material need flags only. Recognition, territory, alliance access, and emergency political relief remain separate optional demand-family scaffolding and are not silently represented by this shipment. Routine aid is not a new event-log milestone; the hidden history and opinion memory are the authoritative relationship receipts.

The elephant unit is unaffected: `chaosx_elephant` continues to use the vanilla `elephantry` sprite/model and animation family, with the retired custom package remaining archival/non-promoted.

## MCP weighted-logic evidence

The required post-change `hoi4.probability_inspect` used adapter `decision_ai_will_do` against `common/decisions/012_africa_gods_decisions.txt` and completed as `PROBABILITY_SOURCE_INSPECTED` with 33 discovered candidates, 13 required inputs, zero unresolved inspect diagnostics, and an intentionally incomplete runtime pool. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be2a267dd391085e108efbef1f31e955e2e35b469bf22218856fbbe0eb514433/4dc502bc5ac25988a04d470df70647b86d4eb649bd22cae11e0cdd8f08c7052b/probability-inspect-e9a8e911052f.json`.

A same-scenario before/after `hoi4.probability_compare` used the `HEAD` decision bytes as the before `inlineClausewitz` source and the current decision path as after, with scenario set `E012_GODS_VOLUNTARY_AID_2026_09_05` covering land-ready, fuel-ready, wartime, and cooldown states. The comparison returned `PROBABILITY_ANALYZED_PARTIAL`, `comparisonChanges=4`, 215 unresolved runtime-dependent items, and 11 diagnostics; the emitted ranking, matrix, comparison, and unresolved artifacts are retained under `probability-68ed2d7504256bf662b23398`. The result is score-only and does not establish click probabilities or live eligibility because event-target and helper state remain unresolved in the adapter. No balance claim is made beyond the bounded source comparison.
