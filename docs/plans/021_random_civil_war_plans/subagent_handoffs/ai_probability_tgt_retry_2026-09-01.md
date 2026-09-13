# Event 021 TGT Target-Weight Audit — Blocked

Audit date: 2026-09-01

Revision: unresolved; the required initial probability inspection did not produce a revision.

Audit mode: read-only, single-family current-revision audit of Event 021 Random Civil War TGT target selection only.

## Audited surface

The requested surface was Event 021 Random Civil War target selection, family `TGT`.

The requested adapter was `custom_weighted_pool`.

The following surfaces were explicitly out of scope and were not audited: `ARC`, `SEV`, `STR`, `EVO`, `FRT`, `SPN`, `SET`, `REC`, `GLB`, `CLU`, `SCN`, decisions, and missions.

## Required first call

Tool: `hoi4.probability_inspect`

Arguments: `adapter = custom_weighted_pool`, `refresh = true`.

Result: MCP error `-32602`.

Exact message: `Input validation error: Invalid arguments for tool hoi4.probability_inspect: An adapter requires a source; provide a source alone to discover compatible adapters`.

This failure occurred before adapter discovery, candidate-pool discovery, source parsing, scenario evaluation, or manifest compatibility assessment.

## Requested scenarios

All requested scenario analyses are unresolved because the mandatory initial inspection failed and the stop rule forbade further traversal.

| Scenario id | Intended assertion | Candidate pool | External factors | Raw result | Normalized result | Analysis id | Scenario hash | Artifact URI |
|---|---|---|---|---|---|---|---|---|
| `TGT-STABLE-ELIGIBLE` | Stable eligible target retains live weight. | Unresolved; current declared pool was not discovered. | Unresolved; required inputs were not discovered. | Not produced. | Not produced. | None. | None. | None. |
| `TGT-WEAK-ELIGIBLE` | Weak eligible target retains live weight and outranks the stable eligible target under comparable conditions. | Unresolved; current declared pool was not discovered. | Unresolved; required inputs were not discovered. | Not produced. | Not produced. | None. | None. | None. |
| `TGT-INELIGIBLE-ZERO` | Ineligible/no-valid-target case has exact zero live weight. | Unresolved; current declared pool was not discovered. | Unresolved; required inputs were not discovered. | Not produced. | Not produced. | None. | None. | None. |

No `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_render`, or `hoi4.probability_compare` call was made after the required inspection failure.

## Comparison status

Historical-baseline comparison: not attempted.

Reason: the failed initial inspection prevented discovery of the current source, current candidate schema, declared custom target-pool manifest, and scenario-input contract. Therefore compatibility with the historical baseline manifest referenced by `ai_probability_audit.md` could not be assessed. No comparison id, revision, scenario hash, or comparison artifact exists.

## Findings

No ranking, live-weight, zero-weight, dominance, starvation, rank-reversal, repetition, or exploit-risk conclusion is established.

The requested claims remain unresolved:

- weak eligible target outranks stable eligible target: unresolved;
- both eligible targets retain live weight: unresolved;
- ineligible/no-valid-target case has exact zero live weight: unresolved.

## Exact blocker and remaining uncertainty

The probability adapter requires an explicit `source` argument, but the first required call was made without one and was rejected by MCP. Because the user instruction requires stopping after any tool error, the exact current weighted source, Event 021 target-weight requirements, declared custom pool, complete candidate pool, external factors, and historical baseline schema were not opened or inferred.

Required next action for a retry: provide the exact current Event 021 TGT weighted-source path or source selector to `hoi4.probability_inspect`, then rerun the three named scenarios with the complete current declared pool and required inputs before attempting any comparison.

No source files were edited. This report is the only intended durable output of the blocked audit.
