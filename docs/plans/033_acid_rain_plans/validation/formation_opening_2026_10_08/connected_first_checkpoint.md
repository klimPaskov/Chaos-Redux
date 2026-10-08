# F6 connected-first failure checkpoint

Disposition: unresolved source contract failure on historical 71F0 and D717.
The runner remains `7f689cb453f724704836dae37f51c135c88ebeda5a85620c1d701bc9477c530b` at this checkpoint.
Gameplay source was never patched by this worker.

## Frozen files

- `baseline_71f0.json` preserves the original nine input files as verified gzip/raw-byte payloads.
- `failing_checkpoint_inputs.json` preserves the failing runner and the verified D717 runtime, AE069 triggers, unchanged constants and root bytes.
- `failing_71f0_replay.json` retains 69 cases, 67 executed checks and two source contract failures.
- `failing_d717_replay.json` retains 75 cases, 73 executed checks and two source contract failures.

The full replay stdout is losslessly compressed in each receipt with byte count and SHA-256.
D717 was reproduced through a read-only archived-source filesystem facade after the live file changed to E5.
The receipt explicitly records that VM execution-stack tails differ from the original direct CLI run.
The source assertions, graph inputs and selected membership are preserved, not relabelled as a pass.
The original direct CLI observations were 67/69 for 71F0 and 73/75 for D717, with zero fixture failures.

## Exact unsorted graph inputs

Both fixtures use frozen array order `S1_0,S1_1,...,S1_19`, region1, 20 eligible states, footprint draw20 percent and target4.
All state target flags begin absent.
The test does not provide an active seed or sort the array.

The non-topological connected chain has edges along `0-19-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18`.
State1 is a disconnected singleton.
The main connected component has nineteen states.

The interleaved-islands graph has five disconnected chains:
`0-19-18-17`, `1-16-15-14`, `2-13-12-11`, `3-10-9-8` and `4-5-6-7`.
Each has four states.

| Fixture | Actual selected before fallback | Reachable untouched then | Actual final selection |
| --- | --- | --- | --- |
| non_topological_chain | 0,19 | 2 | 0,19,1,2 |
| interleaved_islands | 0,19 | 18 | 0,19,1,2 |

The actual D717 fallback loop is at `common/scripted_effects/033_acid_rain_effects.txt:2742`.
The source itself seeds state0 through its active-count-zero OR arm, then reaches state19 in its single forward neighbor pass.
It fails to revisit earlier array entries after state19 becomes active.
Unrestricted fallback starts while a connected untouched candidate is still available, violating Part3's connected-growth-until-stall rule.
Correct footprint count alone is insufficient.

## Control coverage already executing

The passing D717 checks include baseline200, all 24 stage masks at 400/600/800, genuine zero region-result global admission, III global opening versus available but non-meaningful II allocator, no ordinary draw or impacts before the three-day warning, immediate second/third creation, live seven-day split notice without another entry delay, duplicate roots and work, rejected roots, empty/reserved region pools, tiny1/2-state regions, draws12/20, cap40, actual state membership and population-baseline writes, three-day pulse dispatch and unchanged seven-day existing reassignment.
The actual two-visit traversal reaches 12 plus 8 unique states, 20 coverage receipts and one region movement.
Weighted, quota, drift, pulse and physics AST preservation was checked for D717.
The E5 neighbor-growth body is an authorized exception to that prior body-equality check, not a reason to weaken the graph assertions.

## Scope and next owner step

Typed native graph facts are declared fixtures.
Actual activation, source neighbor predicates, footprint loops, state target/coverage writes and ordinary episode population baselines execute.
Helper temporary frames and regular saved maps are separate.
There is no unknown-to-zero fallback or numeric scope-pointer arithmetic.
National accounting, migration, achievement settlement, presentation, Air/Chaos mutation and physical impact bodies remain labelled boundaries.
There is no invented population loss or benefit, native runtime, finance, multiplayer or probability acceptance.
AA owns the affected comparison.

The owner's E5 repair must now be replayed against the same array order and target4.
Neighbor closure must precede fallback, and a stalled component may add only one island seed before neighbor expansion resumes.
No gameplay patch is authorized to this worker.
