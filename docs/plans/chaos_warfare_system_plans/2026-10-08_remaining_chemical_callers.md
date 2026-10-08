# Remaining chemical caller output ownership

Disposition: implemented in source, independently checked and reviewed by the parent; native execution and wider acceptance remain incomplete.
Acceptance basis: the user's approved CBRN single accounting path and the parent's explicit authorization of output-lifetime repairs, including the 66-field Camp contract and one missile retaliation-status declaration.
No new design, fallback, payment path, public wording, asset, equipment or event is introduced.
The broader CBRN goal remains incomplete.

## Source-of-truth map and dispositions

| Document or surface | Disposition and basis |
| --- | --- |
| Accepted CBRN overhaul | The user's 2026-09-20 request is recorded in `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md`; this bounded repair preserves its single accounting path. |
| [Camp patch handoff](subagent_handoffs/2026-10-07_camp_chemical_lifetime_patch.md) | Implemented in source after explicit parent release of the 66-declaration gate; archives and insertion manifest establish exact source preservation, with native execution unresolved. |
| [Missile follow-up Markdown](subagent_handoffs/2026-10-07_missile_cbrn_caller_followup.md) and [JSON](subagent_handoffs/2026-10-07_missile_cbrn_caller_followup.json) | Historical read-only evidence retained; its proposed one-field fix is implemented in current source under parent authorization and superseded for current patch status by this report. Its justified partial-packet analysis remains applicable. |
| [Original insertion map](subagent_handoffs/2026-10-07_chemical_action_lifetime_insertion_map.json) | Historical field/default evidence retained; the removed `missiles_check_chemical_payload_stock` entry is superseded by the current missile follow-up and must not be applied. |
| [Independent source checks](subagent_handoffs/2026-10-08_remaining_chemical_callers_source_checks.md) | Implemented bounded test review: 46 passing cases, exact archive/declaration checks, explicit fixtures and sink limits; parent owns final review and integration. |
| Shared dependencies | Implemented in committed source by peer `5793df4345a413dcf7cadf5aeae99597a859020a` and follow-up `0dc5df3f11da5639e79752591cf78781b7da4d43`; their presence in current HEAD resolves the historical untracked reservation-file caveat without certifying custody transactions. |
| Camp graph comparison/render | Blocked: parent's `ARTIFACT_NOT_FOUND` reports unavailable provenance; the separate reconciliation attempt returns `EVENT_GRAPH_ARTIFACT_LIMIT` at the fixed byte ceiling. No full graph read or successful comparison/render. |
| Full native execution, sink transactions and balance | Unresolved; these source-model tests do not establish them, and eleven biological caller reviews remain queued. |

## Caller contract and frozen source

`camp_rework_apply_chemical_escalation_in_action_state` declares 66 scalars immediately before `camp_rework_prepare_chemical_method_outcome` inside the original eligibility branch.
These are the original 60 action-record fields, five method outputs and `cbrn_action_civilian_deaths`, which the existing Camp death bridge consumes after dispatch returns.
`missiles_dispatch_chemical_payload` declares only `cbrn_action_retaliation_status = constant:cbrn_retaliation_status.none` before reset.
The strategic missile route's existing partial packet is justified by direct input assignments, owned returned outputs and explicit missing-condition gates; no universal 60-field allocation is claimed.
Every original statement, cost, gate, target and helper order remains unchanged when the recorded insertions are removed.
The Camp debit remains its existing exact-model action path; the missile caller uses its existing frozen verified-debit receipt without adding script-side payment.
Fresh owners initialize dispatch proof, while the shared dispatcher preserves proof for repeated calls within one prepared record.
A fresh full Camp invocation creates a separate record and may pay again.

| Source under `common/scripted_effects/` | Frozen after-archive SHA-256 |
| --- | --- |
| `camp_repression_rework_effects.txt` | `cf83c6498e7cd94ebd8125f26e572113d0a83cb121829c87636cf86487a20ada` |
| `032_missiles_operations_effects.txt` | `5f803dd63867d0303d19e7e7e388f00ba6440130b53237ffbe961b715d0ae67b` |

Before/after archives and insertion manifests remain under `docs/testing/2026-10-07_camp_chemical_lifetime/` and `docs/testing/2026-10-07_missile_chemical_retaliation/`.
The Camp current file still matches its frozen after archive.
The missile file also contains concurrent evolution-pressure and clock-arming edits outside the chemical caller, so its current whole-file hash differs from the archive.
The independent checks require the current chemical caller AST, exercised shared dependencies and missile result/resolution/guidance constant categories to match their reviewed contracts, and record all actual input hashes and end-of-run stability.
Those evolution changes remain outside this patch's ownership and commit.
Reconciled HEAD is `8574c5e58eeb01752e6249a3d67b919b3194fddb`.
Its exposure calculator contains the eighteen route/class/exact-agent output declarations, its generic protection resolver contains six output declarations, and its private protection calculator retains the six weights from `611cbb63`.
The reservation API is tracked in that HEAD, including `cbrn_payload_validate_request_authorization`.
These facts record peer implementation evidence and do not transfer ownership or certify all custody/payment primitives.

## Independent source evidence and limits

The [reviewed test handoff](subagent_handoffs/2026-10-08_remaining_chemical_callers_source_checks.md) records 46 passing cases against actual parsed source and the unchanged conservative Event 026 parser/VM.
The checks reconstruct the exact raw baselines after removing only 66 Camp and one missile declarations and preserve original structure/order and frozen source identities.
Current mixed-file checks are scoped to the chemical caller and relevant dependencies; they reject duplicate callers or changed shared exposure definitions rather than treating unrelated evolution edits as chemical changes.
Dependency fingerprints normalize only CRLF/LF differences.
The Chaos Meter guard pins the two values actually read by the retained consequence path, `chemical_cap_factor = 1.45` and chemical-attack reason `3`, and rejects any change in that read set; unrelated added history reason IDs are outside the exercised contract.
The same 46 cases also pass against a projection of the isolated commit contents, excluding the other working-tree edits.
Seven method tiers with and without mastery retain all five outputs; exact costs are asserted, while the other four outputs are checked for retained presence rather than independently rederived tuning.
Twenty-one stock boundary cases run the actual exact-model predicate/debit bodies at cost minus one, exact cost and cost plus one using fixture stock maps and standard costs without mastery.
Outer rejection makes no debit/death; preparation rejection occurs after the existing debit and supplies no death/site receipt, with no refund behavior inferred.
Actual strategic missile preparation/classification/history covers none and authorized status; proportionate is only a separate generic tactical-classifier probe.
The actual returned-death Camp consumer records the supplied fixed death value 25, and the same-record repeated shared dispatch applies one captured death/history record.

Country initialization and method-tier resolution are supplied fixtures.
Actor, exact target/site, policy, research, agent unlock, payload profile, war, division and active retaliation rights are fixture conditions rather than complete eligibility proof.
Doctrine, protection and exposure outputs are supplied, with civilian death fraction 1, forwarded duration and a fixed native death return of 25.
Unit damage, first-exposure shock, contamination, full state consequences, protection arithmetic, weather, masks, atrocities and balance are outside the model.
Condemnation, unified append, humanitarian callback, site/evidence registration, genocide credit, famine adaptation, country recalculation and achievements are captured or no-op sinks; actual actor history and local Camp state writes execute without proving the external ledgers.
Exact-model removal updates fixture stock rather than native accounting; the missile verified-debit flag and consumed quantity 40 are supplied receipts without custody, payment, refund or outcome-selection proof.
The constant loader excludes literals whose fractional spelling contains more than five characters; all 19 excluded current values are mathematically representable after trailing-zero removal.
This is a lexical loader restriction, with fail-on-request behavior, rather than native fixed-point rounding or mathematical unrepresentability.

## MCP provenance and unresolved acceptance

The parent's initial event scan returned `INTERNAL_ERROR`; its narrowed cached scan returned `EVENT_INSPECTED_PARTIAL` at revision `db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5`.
The [96,333,999-byte graph artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77cb0ba17d9f169c19ee52572d30e46e25940e67acd4ac8c775a3038a45b5beb/113ab135dc4d7bb2a2bb5eef4289a29641b74e3f701686652d5fc359922417bd/event-graph-db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5.json) has zero expanded helpers and deferred lifecycle projections.
The parent used `before.artifactUri` with that graph and selected `camp_administration_country.1`; comparison returned `ARTIFACT_NOT_FOUND` because the artifact provenance manifest is unavailable.
This genuine artifact-access failure is distinct from the earlier attempt to use a trace report as a graph baseline.
The [parent receipt](../../testing/2026-10-07_camp_chemical_lifetime/recorded_mcp_attempts.json) preserves the recorded request/result facts from the preceding session; it explicitly identifies reconstruction from recorded tool outputs rather than a retained raw structured response.
The complete graph body was not read.
During reconciliation, a separate current-source cached scan returned the same partial revision/artifact, with helper/lifecycle passes deferred; it does not establish a fresh pre-change baseline or full current-source coverage.
Two initial reconciliation requests were rejected for selector shape; the accepted request used `{ kind: "event", eventId: "camp_administration_country.1" }`, with depth/nodes/edges one and helper expansion/refresh false.
The already-running reconciliation comparison used that graph's `before.artifactUri`, the same selector, chain/render limits one, `render = false` and `refresh = false`.
It returned `EVENT_GRAPH_ARTIFACT_LIMIT`: the 96,333,999-byte snapshot exceeds the fixed 67,108,864-byte comparison ceiling, with no comparison artifacts or checks performed.
This separate current-source attempt neither replaces the parent's earlier provenance result nor establishes an independent pre-change baseline; no retry or graph expansion followed.
Tool exposure and this partial response do not establish complete service health or standalone viewer availability.
No successful comparison/render, native callback cardinality, stock settlement or complete action-lifetime execution is established.
A separate single-setter country-scope validation request also timed out after 600 seconds; its [receipt](../../testing/2026-10-07_missile_chemical_retaliation/setter_validation_2026-10-08.json) records the missing result and absence of a backend job handle.
The earlier [chemical probability handoff](subagent_handoffs/2026-10-07_chemical_raid_lifetime_probability.md) remains scenario-specific unresolved RNG evidence; this tranche changes no weights, distribution, tuning or balance target.
No spreadsheet/export update is required by this tranche because public wording, assets, equipment and events are unchanged.
Skills used: `chaos-redux-events`, `chaos-redux-native-raids` and `chaos-redux-subagents`; none changed.
