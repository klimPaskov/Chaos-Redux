# Campaign scope repair: read-only probability audit

Status: audited unchanged AI arithmetic under declared scenarios; campaign target lifecycle and full-pool selection remain unverified.
Owner: `campaign_scope_probability_audit`, `chaosx_ai_probability_auditor`, Luna.
Parent reviewed the returned comparison JSON and preserved all linked artifacts and provenance manifests.
The auditor made no source changes or commits and did not launch or control HOI4.

## Source and scenario contract

The baseline is the original decision byte backup with SHA256 `9330430ad2c6f73f7bbb8a3f4c485a519e7ea8bc81a4dd07752cf643de1ca84e`.
The final six-guard source has SHA256 `1aa26206c4bfc7128567d5fdf12a6886309175589d822751014394aaa9594d3d`.
MCP normalized source hashes differ from these raw byte hashes.
Baseline inspection revision: `e1eda8a9b2ff3c2a56d0bbc08fa03945ed02f553a1ffc0216b70beaee0f22efb`.
Final inspection revision: `3b9342c175800b80b6165a112f8d06f32012ac24e2c9b108ea3d7d2ab9a8c624`.
The final inspection provenance includes the final raw source hash.

The three scenarios are `MM_START_ASSASSIN_TARGET_ABSENT`, `MM_ASSASSIN_TARGET_READY`, and `MM_ASSASSIN_TARGET_LOW_PP`.
They declare GER under AI control at peace, target and action availability, affordability, selected-cell validity, and visibility.
The same six repaired ordinary decisions are supplied as score-only candidate fixtures on both sides.
Eligibility overrides isolate the original AI arithmetic rather than claiming that the adapter executes campaign event-target lifecycle.
The first comparison using a baseline source path returned `PROBABILITY_SURFACE_EMPTY`; preserved baseline text was then supplied inline.

## Results

The authoritative comparison is operation `compare`, status `complete`, analysis `probability-33ae682738da8b5ee4381f47`.
Scenario hash: `ba0b0b9f09fefe6d41b968f27acff3e8704f577f801dc9cf20cd10dd6e5ebbf4`.
`adapterChanged` and `assumptionsChanged` are false; `scenarioChanges`, `regressions`, `diagnostics`, and `unresolved` are empty.
Each declared scenario contains six candidates with `supportLevel = score_only` and a complete fixture pool.
No AI weight, timing, cost, effect, or target-present predicate was retuned; the decision parent receipt proves exact restoration of the entire original file when the six guards are unwrapped.

The final full-source inspection discovers 29 candidates, reports `poolComplete = false`, and lists 13 required inputs.
That incomplete full-source adapter pool is distinct from the complete six-candidate declared fixture.
No normalized selection probability, full-pool decision behavior, or live campaign result is established.
No sweep, simulation, or sequence balance target was requested or changed.

The missile helper inspection reports `no_weighted_surfaces`.
The ten consuming missile decision AI bases remain 8, 4, 4, 1, 14, 14, 8, 4, 8, and 14, with original modifiers and zero-score gates unchanged.
The eight repaired helpers concern state eligibility, and the Country helper `missiles_target_is_valid` retains its original `exists` check.

## Preserved artifacts

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
All 12 artifacts are stored in `probability/`; `probability_artifact_inventory.json` records their SHA256, provenance hashes, and separate manifest byte hashes.

| Artifact | Content hash | Provenance hash |
| --- | --- | --- |
| `probability-inspect-f6f83c7963a5.json` | `0b4d61e79b6951cd7055de59dbd199e93f40e907eb8974126c6560bcdfad8c78` | `22fac680780e69678ece573972584e43c11e34ae9f1383f5f1effab4ee9b20b0` |
| `probability-inspect-969578472afc.json` | `119b3beef0db34e060f23149a76d085ad1de23d1116ae357d3b5733cd93b4d32` | `ce10e7c26a8be587eeb449619e8574aaf4166a9cdec01fe4d1b79770611fc8d9` |
| `probability-inspect-41fe92ff15a5.json` | `7f4a3843c8b163dca475e8a6f6d9e1265e5b3386427d1b98727fda3c41a06503` | `7d5e5cbc804849fe3c8715bad1e5de9ff142d1ea70900ff95ba0abcbd3e42dcc` |
| `probability-33ae682738da8b5ee4381f47.json` | `a1987ce3ab368df2e2aa124e41b14ebb1ce74b33c0c4e33e78e9b3496b7c007c` | `507b38442c1e9b64a2f030aca3c5389f0317c5f3fdc60c02fa3d9a806ff477d5` |

The original URI for each artifact has the form `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/<content hash>/<provenance hash>/<artifact name>`.
Rendered comparison, ranking, matrix, and unresolved evidence use the basename `probability-probability-33ae682738da8b5ee4381f47-` with SVG and PNG variants.
Content SHA256 and manifest provenance identity were checked separately; a provenance hash is not the byte hash of its manifest file.
