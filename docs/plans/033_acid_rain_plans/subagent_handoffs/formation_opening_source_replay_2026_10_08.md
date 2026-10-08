# Event033 F6 source replay handoff

Disposition: implemented bounded test/report tranche on sealed E5 source, with parent integration review and AA review separate from native acceptance.
The sealed worker rerun and independently saved parent rerun both pass 77 of 77 checks, with zero source-contract failures, zero fixture failures and 1,697 executed source locations.
Runner and gameplay writes were stopped before the final rerun.
The runner hashes itself at startup and verifies the same hash at exit, and it performs no filesystem writes.

## Current source-scoped identities

| Input | SHA-256 |
| --- | --- |
| Runtime | `e5c34d8bd73971609e26b7aef2d4a01cdd4f3f795c2856d83189dfcd546f5def` |
| Triggers | `ae069680a185d0a0aa24d301fe62d158edab09a1a8d7d4ca0a36752dfa974f86` |
| Constants | `900491e8c605450abc7c3057033276fdd00e52d0b709bff29be3bb42dbb15db7` |
| Root event | `e628e71cb9663743a76ce901c35a44cd2281952d5794bab179923605cd5fcfc1` |
| Sealed F6 runner | `dfa292394df926bb191fcf2352aa5c5b71afd82e07277a22ef056b3bdf886bb4` |

The exact current receipt is `docs/plans/033_acid_rain_plans/validation/formation_opening_2026_10_08/sealed_e5_source_replay_receipt.json`.
The parent-owned independent receipt is `parent_e5_source_replay_receipt.json` in the same directory.
Its expanded stdout is 28,932,374 bytes with SHA-256 `98cefd2a71e827f9230b17cd0c9a48b6ad00def390288e2fb7d60883f55ad579`.
This worker did not complete a second expanded-output archive and does not claim that parent output as its own copied artifact.
The compact receipt records the sealed worker result and attributes the parent byte/hash evidence explicitly.

## Files changed by this worker

- `.tools/validation/test_033_formation_opening.js`
- `docs/plans/033_acid_rain_plans/validation/formation_opening_2026_10_08/baseline_71f0.json`
- `docs/plans/033_acid_rain_plans/validation/formation_opening_2026_10_08/failing_checkpoint_inputs.json`
- `docs/plans/033_acid_rain_plans/validation/formation_opening_2026_10_08/failing_71f0_replay.json`
- `docs/plans/033_acid_rain_plans/validation/formation_opening_2026_10_08/failing_d717_replay.json`
- `docs/plans/033_acid_rain_plans/validation/formation_opening_2026_10_08/connected_first_checkpoint.md`
- `docs/plans/033_acid_rain_plans/validation/formation_opening_2026_10_08/sealed_e5_source_replay_receipt.json`
- This handoff.

No gameplay, GUI, cost, weight, shared helper, workbook, asset, dependency or commit was changed.
The parent receipt and AA files were read only.
The sealed dated F5 runner remains unchanged at `1c6867417d33f14a9caa5030dd8de207f2db5d8741a78b6e81b60d1e638dd48a`.

## Historical failure preservation

The checkpoint and two failing receipts remain historical, not overwritten as corrected passes.
71F0 executed 67 of 69 checks and D717 executed 73 of 75 checks, each with two actual connected-first failures and zero fixture failures.
The failing runner bytes remain archived at SHA-256 `7f689cb453f724704836dae37f51c135c88ebeda5a85620c1d701bc9477c530b`.
The lossless full archival replay payloads were decompressed and their byte counts and SHA-256 verified.
Their read-only archived-source VM execution-stack boundary is explicitly recorded.
The original source itself seeded the first eligible state, then failed to revisit earlier array entries before unrestricted fallback.
It was a one-pass ordering defect, not absence of a seed.

## Geometry and control evidence

Both connected-first fixtures retain array order `S1_0..S1_19`, no supplied active seed and target4.
E5 selects `0,19,2,3` on the unsorted nineteen-state connected chain with isolated state1.
It selects `0,19,18,17` in the five interleaved four-state islands.
The explicit stall case selects `0,19,1,18` through three passes: connected growth to 0 and19, zero-progress stall with exactly one seed1, then resumed neighbor growth to18.
The one-seed and closure assertions were retained.
The interim four-pass fixture expectation was corrected to the actual three-pass trace without changing target counts, graph order or membership assertions.

Other checks cover baseline200, all24 enable masks, pure frozen-start global admission, meaningful II versus global opening, genuine private region-result0, no ordinary draw or impact before three days, tiny1/2-state regions,12/20 percent draws and cap40, immediate second/third creation, live seven-day splitting without a second entry delay, zero-lead visit bindings without future warning reports/timed flags, existing seven-day reassignment, empty/reserved pools and duplicate/rejected roots.
The source footprint and population-baseline bodies execute directly.
A full actual two-visit traversal records 12 plus8 unique states,20 coverage receipts and one region movement.
Three-day pulse dispatch and six-day drift remain source-gated.

The E5 growth replacement is an explicitly authorized exception to whole-body equality for `process_front`.
Its non-growth prefix/suffix and activation/retiring blocks match D717.
The private break reset is immediately before the new while invocation, source pass bound remains40, and the runtime loop count is correctly77 before and78 after.
Other weight, quota, timing, drift, pulse, physics, constant and root bodies are unchanged.
No semantic pass was obtained by sorting fixtures or assuming an existing seed.

## Frame and acceptance limits

Typed STATE/COUNTRY graph, continent, population and controller facts are declared fixtures.
Normal/global saved maps are separate from helper temporary call frames.
Child-created temporary storage is discarded unless the caller predeclares it.
Opaque scope identities are not numeric pointers, unknown facts/commands fail, and documented array zero-fill is not a general unknown-value fallback.

Actual initialization, frozen eligibility/index, region arithmetic, activation, neighbor/island loops, target membership, coverage and ordinary episode population baselines execute.
National projections/bootstrap, migration, achievement settlement, presentation, Air/Chaos owner mutations and impact bodies are labelled boundaries.
The footprint builder is not a successful spy.
Birth mortality/damage callbacks fail the test, later cadence cases observe dispatch only, and the global transition physical body is not executed.
There are no invented losses, benefits or successful financial receipts.

Native neighbor iteration and bounds, declared graph facts, source replay and native engine behavior remain distinct.
Arithmetic uses JavaScript doubles and explicit source rounding, not native fixed-point or overflow proof.
There is no native geometry, physics, population-loss, finance, migration, multiplayer or GUI acceptance.

The parent reports AA's affected E5 comparison returned31 cases,217 records and zero changes.
AA is independently reviewing that result, and this worker neither performed nor accepts that audit.
The concrete next step is parent review of the sealed runner/current receipt and AA's review, followed by the parent's scoped commit.
Skills used: chaos-redux-events, chaos-redux-subagents and the loop-break-isolation reference.
No skill was changed.
All delegated bodies and omitted native acceptance are explicit.
