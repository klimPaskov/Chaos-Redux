# Event016 Rocketry native selection scenario evidence

This documentation fixture compares the four Rocketry selection and withdrawal AI actions across the D27 decision-file change.
It changes no gameplay source and introduces no decision, project, technology, flag or model into the mod.

## Frozen source contract

`source_manifest.json` records the original logical gameplay path, the exact before/after snapshot paths and their SHA-256 hashes.
The before file is the exact Git blob from `a4b0c089ab8ad406551ec361db5f8d2c02e52b88`, the parent of D27 commit `dd10a3f3e36aa63d50a9cfd5294b75a23126bc46`.
The after file preserves the current physical decision bytes.
Both are read through `source.path` set to the logical gameplay file, `source.snapshotPath` set to the frozen documentation file and `source.expectedSourceHash` set to the corresponding exact hash.
The folder's `.gitattributes` disables text conversion for snapshots and JSON evidence so Git round trips preserve the recorded byte hashes.
The connected 3.10.0 route accepted this contract in the initial exact-input pilot.
These snapshots are not loaded as gameplay files.

Shared helpers and constants come from the current workspace in both sides of the comparison.
This bounds the result to the D27 decision-file delta under current dependencies.
It is not a full historical workspace comparison.
Relevant dependency hashes and current route results belong in the reviewed audit evidence.

## Scenario meaning

`scenarios.json` contains fifteen genuinely different declared source states without candidate eligibility overrides.
They cover each single researched source, each sole prerequisite, stale held selections with the opposite source researched or completed, a held source still researching, an already-completed held source, a closed provider, an active paid Prototype receipt and the war/factory-margin factors.
Factory counts three and four straddle the actual low-margin condition, which is the negation of more than three spare civilian factories.
The country facts represent a declared MCL laboratory-state provider and are not a live save observation.
These input-level checks do not establish that a campaign reaches every declared combination.

The installed scalar-condition evaluator compares a declared string such as `is_special_project_completed = sp:sp_air_jet_engine` against each literal native query.
The fixture token `none` means none of the named project or technology operands matches in that case.
This is distinct from omitting an input, which leaves it unresolved.
The exact paid array element is declared as `variable.mengele_event016_active_project_stage_entries^3`.
Country flags and active-stage values differ between the provider and paid-receipt cases.

The adapter cannot represent multiple true operands for the same generic native query through this scalar mechanism.
Both Rocketry projects completed or researched, both prerequisite technology paths, and simultaneous Gotterdammerung/By Blood Alone states therefore remain outside these declared MCP cases.
No single-project fixture is labeled as one of those multi-value states.
They remain explicit requirements for separate source reasoning and future supported domain evidence.

## Eligibility and proof limits

The probability decision adapter reads the decision's `available` block and its AI score.
It does not include `visible` or category gates in that eligibility block.
The parent uses the decision inspection route separately for valid-provider, closed-provider and paid-receipt withdrawal visibility.
An available withdrawal with a hidden provider category must not be presented as a selectable in-game action.

Decision AI supports raw scores and ranks, not normalized selection probabilities.
The original pilot returned `PROBABILITY_ANALYZED`, one available candidate and zero unresolved items for the held Flying Bomb selection after Jet Engine completion.
Its declared native fields and paid receipt replaced the previous forced-candidate assumption.
The current evaluation and same-scenario comparison were returned and independently reviewed in `comparison_review.json`.
The recovered exact MCP bytes are retained in `after_analysis.json` and `compare_analysis.json`, with their declared sizes and SHA-256 verified by the parent.
Four stale-selection cases gain a release score from zero to ten, and one closed-provider case has the same score change while remaining hidden.
The separate zero-political-power visibility/affordability result is retained in `decision_visibility_evidence.json`.
Reports remain partial because of unbound state-88 branches, and the scalar joint-state limitations above remain open.
This source audit does not establish native execution timing, campaign reachability or full Event016 acceptance.

## Primary implementation references

Installed package: `C:/Users/klimp/AppData/Roaming/npm/node_modules/hoi4-agent-tools`, version 3.10.0.
The connected server status also reports 3.10.0.
`docs/probability.md` documents scenario state, immutable snapshots, candidate overrides and decision score semantics.
`dist/hoi4_agent_tools/schemas/probability.js:263-300` defines the snapshot selector and hash contract.
`dist/hoi4_agent_tools/core/condition-evaluator.js` defines scalar comparisons, flag state and numeric variable lookup.
`dist/hoi4_agent_tools/probability/source-analysis.js:130-168` shows the decision adapter's available-only eligibility boundary.
No package or service configuration was edited to produce this fixture.
