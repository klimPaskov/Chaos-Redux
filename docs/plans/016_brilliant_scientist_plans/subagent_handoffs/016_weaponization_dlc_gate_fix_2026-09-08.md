# Event 016 Weaponization DLC gates

Disposition: implemented and source-reviewed; exact-baseline probability comparison remains unresolved after the bounded post-change audit.
Acceptance basis: the user's Final Completion Plan requires project progression without DLC-only presentation while preserving prerequisites, costs, and causal history.

## Exact implementation

Only `brilliant_scientist_can_begin_rocketry_weaponization` and `brilliant_scientist_can_begin_high_energy_weaponization` in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` gain a `NOT = { has_dlc = "Gotterdammerung" }` alternative inside their native-project OR block.
Their exact Deployment receipts, valid project board, and payment requirements remain mandatory outside that block.
With the DLC, Rocketry still requires Long-Range Ballistic Missile or Supersonic Jet, and High Energy still requires Thermonuclear Bomb or Nuclear Warheads.
Without it, the completed paid Deployment stage permits the existing paid Weaponization action.
The patch does not complete native projects, issue rewards, modify raid equipment, or bypass resource and technology gates.

Installed vanilla `rocket_projects.txt`, `air_projects.txt`, and `nuclear_projects.txt` explicitly require Götterdämmerung in the `allowed` blocks of those four alternatives.
The earlier Deployment prerequisites remain unchanged because Ballistic Missile, Axial Jet Engine, and Nuclear Bomb have base-game paths.

## Evidence boundary

Frozen baseline: `probability-07549106fa411f7bcdd36d84`, twenty scenarios, forty rows, scenario hash `0554685fc1eca42c6fa8be6dfb7773ce9226a038e3a193c9e936bdef906c3971`.
It reports a complete two-ID score pool with zero unresolved rows, but score-only ranking does not establish click probabilities or fully bound live eligibility.
The companion audit `016_mengele_conventional_probability_2026-09-08.md` owns the exact baseline fixture and post-change comparison.
The returned comparison `probability-0fe892fa51efde812ddbcd79` contained twenty scenarios, forty rows, zero unresolved rows, and zero score changes.
However, its scenario hash `34cdc8b3e288c8809796a331f94b6106ccfc9f59d078803d9c7706aeef4619c0` differs from the frozen baseline, and its path-only source descriptors both resolved the current decision-board source rather than capturing the changed indirect trigger file.
This is not accepted as proof of the requested before/after eligibility comparison, and the exact-baseline gate remains open.
The parent ran `node .tools/audit_mengele_project_adapter_contract.mjs` against the current source.
Its 320 Weaponization assertions evaluate both actual entry-gate blocks across all five stage values and every combination of DLC ownership, board readiness, affordability, and the two native alternatives.
They confirm that only the exact Deployment stage can proceed, missing board/payment eligibility still blocks, either native alternative works with DLC, and neither native alternative is required without DLC.
Board readiness and the nested payment helper are explicit test inputs; this does not prove the engine's evaluation of those helpers or replace MCP comparison.
Current shared-trigger SHA-256: `e1d924491fc9c00ecfc7eed2097397622292f39742d4412a7e3d5e7d9dd1abf2`.
No full Event 016 acceptance follows from this narrow compatibility correction.

## Commit boundary

Only the two added trigger alternatives and this scoped handoff belong to this fix.
Other uncommitted Prototype, component, private-program, asset, model, and documentation changes remain outside it.
Do not stage the whole shared trigger file to commit this fix.
