# CXT naval-facility stall repair

Date: 2026-09-13.
Disposition: source repair and review complete; runtime freeze outcome unverified.
This report supersedes the unresolved setup-stage diagnosis in `../20260913_cxt_technology_validation/freeze_repair.md` with the user-supplied naval-facility boundary evidence.

## Evidence and repair

The supplied Germany reproduction completes annexation, capital restoration, condemnation refresh, and technology setup, then enters `naval_facility` provisioning without returning.
The last marker brackets the complete facility helper; it does not identify an exact native instruction, callback, or construction operation.
The source calls an inner runtime `meta_trigger` from three host checks inside an outer generated effect.
Read-only inspection of the installed meta evaluators confirms that both effect and trigger evaluation compile their generated text before execution.
The native contract is `native_meta_contract.json`; it establishes the repeated compilation path without claiming a proven mutex deadlock or runtime freeze cause.

The facility template resolves its literal building type once and invokes native `can_construct_building` directly at every host-existence, candidate-rejection, and final-construction gate.
`chaosx_test_country_state_meets_facility_requirements` retains the shared ownership, control, coastal, and no-other-campus predicates without another runtime expansion.
The rejection gate keeps both predicates inside `AND` under `NOT`, preserving restoration when either requirement fails rather than applying Clausewitz NOR to sibling conditions.
Candidate selection, temporary acquisitions, owner/controller restoration, construction, existing-campus checks, and missing-facility flags retain their original behavior.
All six facility types, their order, technology/project setup, stockpiles, units, and package synchronization are preserved.

## Review and verification

`source_validation.json` compares the complete effects AST against the baseline after expanding the host predicates and removing temporary tracing.
All gameplay predicates and outputs match; earlier trigger definitions and the six facility calls are unchanged.
The four rejection scenarios evaluate the actual parsed `NOT` and `AND` blocks using Clausewitz NOR semantics and restore a candidate when either placement requirements or native legality fails.
The scripted-system architect approved the final source after the negation and diagnostic-scope corrections.

Temporary markers distinguish generated-body entry, search entry/exit, ownership/controller transfer, restoration, and native construction.
State-scoped marker guards read CXT's country flag explicitly through `ROOT`.
The wider setup trace is retained until the freeze's exact blocking stage is identified and repaired; every temporary marker must then be removed.

Parent event inspect, render, and compare calls returned `Transport closed`; the specialist returned partial direct evidence with helper projections and lifecycle analysis deferred.
Exact MCP queries and limitations are recorded in `mcp_receipt.json`.
No game was launched, no computer was controlled, and no logs were requested or searched; the runtime evidence is the user's supplied excerpt.
Source equivalence and partial MCP evidence do not establish a successful native execution or prove that the freeze has disappeared.

## Files and scope

Gameplay changes: `common/scripted_effects/chaosx_test_country_effects.txt` and `common/scripted_triggers/chaosx_test_country_triggers.txt`.
The CXT testing guide describes the direct native placement gates, and events guidance records the reusable NOR and diagnostic-country-scope rules.
Evidence files in this directory retain the supplied runtime boundary, native evaluator contract, source validation, and MCP receipts.

No gameplay simplifications, omitted facility types, substituted hosts, or disabled test content were introduced.
The reported freeze remains unverified after this source repair, so the full runtime repair task is not claimed complete.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and the official `skill-creator` workflow for the small guidance update.
No Astra subagents were used.
