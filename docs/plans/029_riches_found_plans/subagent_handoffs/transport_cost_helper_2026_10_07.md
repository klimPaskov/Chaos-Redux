# Event 029 transport cost helper handoff, 2026-10-07

Disposition: implemented module, accepted and queued parent call-site integration, and blocked native callback-generation proof.
Acceptance basis is the parent's bounded patch-authorized transport-cost assignment for specialist labour, workforce replacement, and evacuation.
This handoff does not claim completion of Event 029 or its integrated decisions.

## Files changed

Five new files are owned by this patch:

- `common/scripted_effects/029_riches_found_transport_cost_effects.txt`
- `common/scripted_triggers/029_riches_found_transport_cost_triggers.txt`
- `common/script_constants/029_riches_found_transport_cost_constants.txt`
- `docs/events/029_riches_found/transport_cost_contract.md`
- `docs/plans/029_riches_found_plans/subagent_handoffs/transport_cost_helper_2026_10_07.md`

Existing decisions, YML, cost triggers, works effects, shared helper docs, and the frozen physical-cost evidence are untouched by this subagent.
No git, index, commit, child-agent, GUI, asset, unit, or 3D operation was performed.

## Completed helper contract

Public families are `rf_specialist_transport_*`, `rf_workforce_transport_*`, and `rf_evacuation_transport_*`.
Each has quote, can_pay, has_receipt, debit, refund, and clear_receipt entry points.
The module has no named parameter API.
All helpers execute as COUNTRY THIS = ROOT with FROM bound to the original mine STATE.

| Family | Paid cost | Land transport | Sea transport |
| --- | --- | --- | --- |
| Specialist | two civilian factories reserved and 25 PP | one train_equipment_1 | five convoy_1 |
| Replacement | two civilian factories reserved and 1000 manpower | three train_equipment_1 | fifteen convoy_1 |
| Evacuation | two civilian factories reserved, 1000 manpower, and 75 motorized_equipment_1 | three train_equipment_1 | thirty convoy_1 |

The selected transport is paid once.
There is no manpower or support-equipment fee on specialist labour.
There is no PP fee on replacement or evacuation.
The four-cost ceiling is preserved.

The parent's native decision modifier owns civilian reservation and release.
The helper checks its inclusive availability and records its amount.
It never deletes or grants factories.

Quote inputs are documented caller-owned temps, including an explicit land/sea route request.
The request must match the state's actual existing route and corresponding validity flags.
Missing or invalid route input produces quote none, zero amounts, false preflight, and no debit.
No alternate resource is selected by affordability.

Persistent normal receipt fields belong to the paying COUNTRY, partitioned by family prefix and `_@var:rf_transport_cost_mine_seq`.
Canonical existing state source is `riches_found_mine_sequence`.
Each receipt retains route, transport amount, civilian reservation, PP, manpower, trucks, payer identity, and exact state identity.
An existing field, including an incomplete receipt, blocks overwrite.
Other families, mines, and controllers use independent fields.

Refund loads the old receipt, clears it before crediting, and restores the recorded discrete quantities to that payer.
Current route, controller, and price tuning do not change a refund.
Success cleanup clears the same receipt without credit.
No state receipt mirrors, global event targets, or new world loops were added.
No event-target cleanup is needed.
The contract lists every input, output, default, side effect, caller storage requirement, and private helper boundary.

## Parent call sites and migration

Call sites changed by this subagent: none, as instructed.

Parent integration targets:

- `decision_riches_found_specialist_labor`: use specialist can_pay in availability and custom cost, replace old payment/refund, and attach the existing two-factory timed modifier.
- `decision_riches_found_gold_replace_workforce`: use replacement can_pay, replace PP and simultaneous train/convoy fees, and attach the timed civilian reservation.
- `decision_riches_found_demons_evacuate_district`: use evacuation can_pay, replace PP and simultaneous train/convoy fees with emergency manpower, concrete trucks, and exactly one selected transport.

Each complete_effect must initialize caller storage, set the actual route request, call debit, and apply existing start effects only when `rf_transport_cost_paid = one`.
Each original-payer remove/cancel callback must load the exact paid mine sequence, require the matching has_receipt trigger, and close through success cleanup or exact refund.
Only `rf_transport_cost_closed = one` authorizes further receipt-owned cleanup or publication.
The parent's UI helper must use the same quote and exact equipment tokens.
If both established route flags exist and no actual choice is known, do not guess a route.

Prices reuse `riches_found_decision_cost`.
Only the unique `rf_transport_cost_model` protocol category was added.
No main constant group was redeclared.
The individual action recipes are in the contract document.

## Meaningful source validation

An in-memory interpreter executed the actual new effect/trigger source and current constants with a conservative five-decimal truncating arithmetic model and helper call-frame cleanup.
All `rf_*` helpers in each path were executed from source.
Mocks were limited to native scope identity, flags, getters, and discrete debit/credit primitives.
No production helper was replaced with a no-op.

140 declared source cases passed:

- Every family on each land/sea route produced its exact accepted cost tuple.
- Every positive spendable reserve was checked immediately below, exactly at, and immediately above its quoted threshold.
- A repeated debit with an open receipt produced no second native payment.
- Refund after control loss and removal of route flags restored the exact original quantities.
- Repeated refund after closure produced no native credit.
- Success cleanup produced no refund, and later refund after successful closure remained inert.
- Invalid route enums and fractional, zero, or negative mine sequences produced none and no payment.
- Several family receipts and a second mine coexisted on the payer, and a second controller had its own separate record.
- Wrong callback ROOT, wrong FROM state, and a missing mine receipt produced no refund.
- An incomplete pre-existing receipt prevented overwriting.
- Replacement and evacuation did not require PP when their PP fee was zero.
- Refund after changed current price constants still restored the paid amounts.

The model does not execute HOI4 or prove native equipment provenance, callback delivery, civilian modifier timing, or map connectivity.
It assumes documented stockpile quantity mutation and does not reconstruct producer/variant identity.
The 140 cases establish only the bounded source contract.

Validated source SHA-256:

| Source | SHA-256 |
| --- | --- |
| New effects | `98f78fc6747c873817dae66a44c1ca5db910619299796e38ca5f476de9b453cb` |
| New triggers | `620ffbc15889f5dd7cde27ba77a86769888cde33e7262fe41b8135e58f30dfa1` |
| New constants | `3e9bc524ab48a06feb9228726d193b7fd3f0cb9be99d214c966af6354374443c` |
| Part 3 spec | `d7e58adfcd167400a6e097859a42266975fd2ecc9c35da6161a1232414719630` |

## Scope findings and exact blockers

The current source binds the state history sequence once in `riches_found_bind_history_sequence`, `common/scripted_effects/029_riches_found_effects.txt:198-217`.
The existing capability refresh derives `riches_found_rail_route_valid` and `riches_found_port_route_valid` at lines 547-574.
Selected-route flags and their validity markers are distinct inputs.

Native targeted-decision documentation establishes COUNTRY actor and FROM target for decision evaluation.
The offline wiki identifies ROOT as the acting country and FROM as the target STATE, and separates complete_effect from remove_effect.
No inspected documentation establishes an invocation nonce or an exact native callback-data binding for a generation of the same payer/family/mine receipt.

Exact blocker: once an earlier receipt has closed and the same payer pays the same family for the same mine again, an old duplicate callback and the later invocation have identical available receipt keys.
The helper cannot distinguish them.
Open-receipt duplicate debit and repeated closure before re-payment are guarded.
Callback-generation replay protection after re-payment remains unproven.
Do not claim it or invent an actor_nonce, callback payload, scratch-state mirror, or placeholder ledger.

The parent must establish native per-target timer exclusivity and original-payer callback binding, or provide a supported exact identity input.
Entering another COUNTRY scope does not rebind ROOT.
A callback rooted in another country must not redirect refunds to the current controller.
Lost original payer or sequence context is an integration blocker, not a reason to guess.

Parent-owned civilian reservation timing and early cancellation need their own evidence.
This module provides no native timer or reservation implementation.
The current helper source is not integrated into the three decisions until the parent makes those authorized call-site edits.

## MCP evidence and route limitations

The connected tool list exposes reference_context, reference_search, reference_read, source_lookup, event_inspect, event_render, event_compare, decision_inspect, and script_validate.
Tool exposure is not service-health or native execution proof.

A successful source_lookup for `decision_riches_found_specialist_labor` returned the current workspace definition at `mod:common/decisions/029_riches_found_decisions.txt:854-940`.
The bounded text read covered 854-873.
Its revision was `6f596095d18722c615df9fc4e878f8a7a67056daa619c3d659ea4a6efe0a0abc`, sourceScope `workspace_index`, complete true, definitionCount one, references disabled.
It returned no artifact.

Schema findings were corrected before interpreting domain coverage:

- script_validate rejected an explicit ROOT binding with `SCRIPT_BINDING_RESERVED`, explaining that ROOT, THIS, and PREV follow the supplied scope/traversal.
- File validation rejected simultaneous path plus kind/scope and a limit of 100.
- Corrected validation requests use actual helper bodies, kind effect/trigger, scope country, only FROM bound to state, and limit 32.
- decision_inspect in inspect mode requires declared scenarios.
- reference_read requires revision-bound hashed ids and revisions, not filesystem paths or the literal current.

Further live result status is recorded in the final MCP addendum below.
Pending inspection or validation is not a passing result.
Source-only evidence does not replace required MCP evidence.

No GUI, focus, technology, or map source surface was edited.
This helper consumes existing state route markers and makes no independent map-connectivity claim.
The parent's separate probability auditor owns decision AI inspection and comparison.
Its supplied frozen baseline root is `docs/plans/029_riches_found_plans/evidence/2026_10_07_physical_cost_before`.
This subagent neither changes that root nor substitutes a current source for it.

## Reference revisions

Detailed sections and native precedents are listed in the contract document.
Local reference reads supplement MCP requests and are not claimed as successful MCP retrieval.

| Local source | SHA-256 |
| --- | --- |
| Offline Data structures | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline Effects | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline Triggers | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Offline Scopes | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Offline Decision modding | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| Installed effects documentation | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed triggers documentation | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed script concepts | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed constant schema | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |

## Simplifications, omissions, and follow-up

No accepted cost family was simplified and no alternate-resource fallback was added.
Call-site integration, native civilian reservation, and UI wording remain with the parent as explicitly assigned.
Callback generation identity, native execution, and any outstanding MCP result remain unresolved.
No agent launched HOI4.

Skills used: chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-subagents.
No skill was created or updated because only these five files were authorized and no children were permitted.

## Final MCP addendum

Corrected script_validate requests completed for the actual quote, debit, and refund bodies with COUNTRY scope and FROM STATE binding.
All three returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, and `parametersChecked = false`.
The performed checks were syntax, command_kind, and declared_scope.
These are partial findings, not a validation pass.
The documentation inventory revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.

| Body | Commands checked | Total findings | Omitted findings | Unresolved commands/blocks | Argument blocks unchecked |
| --- | --- | --- | --- | --- | --- |
| `rf_transport_cost_debit` | 32 | 57 | 36 | 26 | 24 |
| `rf_transport_cost_refund` | 23 | 39 | 18 | 17 | 15 |
| `rf_transport_cost_quote` | 47 | 72 | 52 | 31 | 30 |

The unresolved helper commands were quote_context_valid, can_pay, store_receipt, load_receipt, and clear_loaded_receipt in their respective caller bodies.
They are implemented in the new files and were executed by the actual-source model.
The validator does not expand them as native commands.
It also leaves native argument blocks unchecked, including variable assignments/comparisons and equipment mutations.
Their relevant local documentation was read, but parameter semantics and engine behavior remain separate evidence.
No artifact URI was returned by these validator requests.

Successful revision-bound reference_read results:

- Offline `Data structures - Hearts of Iron 4 Wiki.md:547-554`, including integer `_@var:` targeting, id `5a770a811537c0690f7a3b9bf16209539c90ea31fe3e1a70654a99b8fb4503ee`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, no continuation.
- Installed `documentation/triggers_documentation.md:6442-6454`, modulo_temp_variable, id `e8381ed0f8e6d4d1a5bbf4d5fb1d3e1dad43d9b9db91d4a56732bb29117098c6`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, no continuation.

The targeted decision_inspect request with declared actor GER, FROM STATE 64, mine sequence 1, explicit controls, route flags, and exact land stockpile thresholds failed with:
`tool call failed for hoi4_agent_tools/hoi4.decision_inspect: timed out awaiting tools/call after 600s`.
No scenario artifact or eligibility/lifecycle result was delivered.
This is the exact unavailable decision-evidence route for this pass.
The source model is not substituted for it.

The earlier reference_context, initial reference searches, focused event_inspect trace, and broad decision inventory request remained unobserved at this addendum's checkpoint.
A pending observation is not proof of a failed server operation.
Their coverage and artifact references must not be invented.
Event rendering/comparison were not claimed because no completed event inspection result was available to bind them.
The parent still needs its owning decision and event evidence before integrated completion.
After preserving those observation limits, the client execution cell containing the initial batch was terminated.
No server job cancellation was requested and no server-side result or artifact was inferred from that client termination.

The native two-factory modifier may be applied by the engine's timer even if a stale complete_effect rejects a fresh helper preflight.
Whether the parent's native row can atomically reject that reservation is unproven here.
The module neither claims such atomicity nor creates a replacement reservation mechanic.
Carry this native stale-click/reservation limitation into integration alongside the callback-generation identity blocker.
