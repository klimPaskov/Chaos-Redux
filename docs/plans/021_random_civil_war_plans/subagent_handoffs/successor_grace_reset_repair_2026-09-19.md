# Event 021 successor-grace and recurrence reset repair

Status: implemented source repair; owner-run probability projection complete; independent probability certification and live testing remain open.

## Successor grace gate

`random_civil_war_successor_grace_clear` now admits a country when no successor-grace flag exists or when `global.date` has reached the recorded `random_civil_war_successor_grace_until` date.

The trigger is applied to automatic target admission, Critical-queue target admission, manual-scenario target admission, recurrence eligibility, the parent opening-candidate filter, and dormant Event 006 candidate admission.

A grace flag with no expiry variable fails closed, so an incomplete successor receipt cannot reopen a target.

## Generation-local reset

After `event021_parent_mark_treaty_recurrence` records any prior agreement recurrence, `event021_begin_achievement_history` clears the prior settlement type and date, reconstruction deadline, local front-bound obligation pointers and dates, settlement hold deadline, settled-front counter, and transient obligation outcome flags.

The reset preserves the durable treaty registry, settlement violation, failed or harsh settlement history, recurrence memory, Event 006 identity, and completed achievement flags.

`event021_parent_select_settlement_obligation` and `event021_treaty_prepare_signatory_obligations` clear stale local obligation pointers, dates, hold receipts, objective-missed state, and terms-held state before assigning the new owner or signatory contract.

## Probability evidence

The source-backed MCP inspect used adapter `custom_weighted_pool` against `common/scripted_triggers/021_random_civil_war_triggers.txt::random_civil_war_country_can_be_target` and returned `PROBABILITY_SOURCE_DISCOVERED` with zero custom candidates because the live helper is not exposed as a declared custom pool.

The declared projection was therefore explicit and bounded rather than presented as a live global-country distribution.

The MCP declared-manifest inspect returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = true`, three candidates, zero required inputs, and zero unresolved inputs.

The same three scenarios were evaluated and compared before and after the gate: grace active, grace expired, and no grace.

The owner-run comparison returned `PROBABILITY_ANALYZED`, `analysisStatus = complete`, three scenarios, nine candidate rows, zero unresolved inputs, zero diagnostics, and three comparison changes.

The projection expectation is that grace-active removes all three opening surfaces, while grace-expired and no-grace retain the pre-patch support; this is manifest evidence, not engine execution of the live country registry.

Artifacts: source inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63dfc2b99598f891f55f72d5998e9cb9fb2c6bf9f01fa62537819b5d0ec0edbf/c1d8223a742770e71ee5d87e173ec54e37ab4421ddc3ee3b327542aa15544a93/probability-inspect-2fafe3da4050.json`; declared inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e57ebf652f020eb3e1414002a4a235d1b70c70c03d9c756a68fba770595890c/d5d48dc35e2136c3404ce9ee536fcca413612a1be3a8d4599421922463c66db2/probability-inspect-06396d7d268a.json`; evaluation `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de8a8b9e92a3d983fe3dcabf43cd407b1c06a3c33d9ee32e08b7589e19a237e1/168e99161cb8afe08cbcaed04e7edb7d31e73f4a05b2cb159498b774bf53486b/probability-7dc24862cc81a048349f1fa3.json`; compare `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77c2f6a3742d13afedeb0b9276efeddfb105d58669a3a8641a0ea6d7e034c297/54ab0eef06493d6e1774254886d23ac55ea870ab930bdcffd71a5c88a91a1c0d/probability-28aa4dd58aa69086c880cb13.json`.

The focused Event 021 event inspect remains the cached `EVENT_INSPECTED_PARTIAL` receipt with zero blocking diagnostics and deferred helper/lifecycle validation, so it does not certify the runtime grace or recurrence sequence.

## Remaining acceptance boundary

The shared fixed-target companion remains an explicitly documented framework blocker and is not substituted by this repair.

Actual successor war continuity, all-signatory treaty succession, live recurrence, save/reload, and user-owned HOI4 playtesting remain open.
