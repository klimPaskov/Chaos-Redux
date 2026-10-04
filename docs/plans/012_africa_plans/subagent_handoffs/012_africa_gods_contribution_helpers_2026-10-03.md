# Event 012 contribution helper repair handoff

Date: 2026-10-04.
Disposition: implemented bounded arithmetic and contract-binding repair, contribution/native exactness coverage remains partial.
Acceptance basis: the parent's accepted [full grading plan](012_africa_gods_full_grading_rewards_design_2026-10-03.md), its unchanged 500 payment/1000 capacity/cooldown contract, the explicit F1-F6 repair assignment, and the subsequent primary-evidence clarification.
This handoff supersedes the previous helper-complete claim and its 1499-reject/1500-allow interpretation.
Parent independent review is required before publishing or integrating this contribution tranche.
No Git operation, HOI4 launch, inherited context, other-worker edit or parent-hook edit was performed.

## Files changed and ownership

| Source/doc changed | SHA-256 at this handoff |
| --- | --- |
| [012_africa_gods_contribution_effects.txt](../../../../common/scripted_effects/012_africa_gods_contribution_effects.txt) | 5e77ad1923895907ecbd059d679df5f6d390051e41ffd335ab47529db5a31328 |
| [012_africa_gods_contribution_triggers.txt](../../../../common/scripted_triggers/012_africa_gods_contribution_triggers.txt) | 3ccee425b9e50c2093374b61e9c9abf0544cdca65dfefc69045c110370a350be |
| [012_africa_gods_contribution_constants.txt](../../../../common/script_constants/012_africa_gods_contribution_constants.txt) | 0b4f0fc738321f0965f3279e0ef06252b77d38fde79ab02a526fa9a0e161ae6e |
| [012_africa_gods_contribution_effects.md](../../../../common/scripted_effects/012_africa_gods_contribution_effects.md) | 3c8369ffff8054c1b54902b3b4a6d89afe2787b51caf1a8848d01b1aec968f51 |

This handoff was rewritten, and [the arithmetic repair evidence](012_africa_gods_contribution_arithmetic_repair_2026-10-04.md) was added with the reproducible bounded source fixture and reference limitations.
The parent already renamed the conversion category to gods_of_africa_contribution_measure in the three owned source files before this repair.
That name is retained.
Grading's integer contribution_units category and denominators were not edited.
Parent score, hooks, costs, lifecycle, treaty ownership, decisions, GUI, event, localisation, spreadsheet and the other worker's grading arithmetic files were not changed.
No new UI, native cost type, decision, AI weight, timer, country or asset was introduced.

## F1-F6 disposition

| Finding | Repair and remaining limit |
| --- | --- |
| F1 | Fuel/manpower BEFORE and AFTER remain native k, directed differences are computed in k, common actual is bounded to request_k before raw conversion, and fuel room stays k. Native getter/normal-field precision and width remain unverified. |
| F2 | Each of the six real chassis has separate donor/receiver BEFORE/AFTER and directed raw differences. Aggregation adds only bounded differences, with excess identified before bounding. Individual raw num_equipment range/precision is unresolved, no num_equipment_k exists in this implementation, and an externally supplied high-stock fixture is retained evidence rather than proof of native getter support. |
| F3 | Voluntary infantry requires exactly 500 shipped and 1000 total source stock before debit. The constant/comment/API wording no longer treats 1000 as an additional retained reserve. Fuel requires the existing exact 500 and existing capacity/cooldown. |
| F4 | Request must equal normalized payment_amount and kind must match the explicit actual emit kind, frozen mobile subtype and real convoy/train preflight branch. Epoch-bound receipt identity added. All prospective quantity and PP writes are checked before receipt consumption. Unsupported fractional or lifetime accumulation retains pending measurements/snapshots without changing prices, truncating actuals, capping history, waiving amounts or inventing recovery. Native exact-type coverage and its recovery representation remain unresolved. |
| F5 | Separate fixed_point contribution_measure retained and documented. Parent grading contribution_units int category remains separate. No duplicate-category merge behavior is assumed. |
| F6 | Prior 24 source fixtures are historical, unbounded and superseded for arithmetic/pricing. Fifteen reproducible bounded source case groups are retained in the repair evidence. No engine-complete claim is made. |

The three-decimal quantum and 2147483.647 bound are conservative source-audit assumptions.
Installed mathExpression fixed_point wording does not establish every getter/normal variable type width or precision.
The offline five-decimal variable paragraph and three-decimal modifier-display wording may describe different types, rather than an engine contradiction.
The documented deprecated plain manpower overflow is separate evidence, so manpower_k remains required regardless of that unresolved type question.

## Parent input and output contract

Invoke boolean helpers in PARTICIPANT COUNTRY scope inside the actual contiguous native transaction.
Initialize all bare temporary inputs in the parent effect before calling begin.
There are no parameter macros and no scoped temporary inputs.

| Bare input | Exact binding |
| --- | --- |
| gods_of_africa_contribution_kind | Stable actual kind 1-11, from the selected native branch |
| gods_of_africa_contribution_native_emit_kind | Same kind selected by the actual native owner, captured through a parent-private normal selection field before copying to this bare temp |
| gods_of_africa_contribution_requested | Exact raw normalized gods_of_africa_payment_amount for ordinary payment, exact existing 500 amount for voluntary aid |
| gods_of_africa_contribution_voluntary | Explicit zero or one, no default |

The parent must retain its actual chosen truck/artillery or convoy/train kind, rather than derive it later from a generic family.
Mobile matching uses gods_of_africa_payment_mobile_type and gods_of_africa_mobile_payment_matches_contract.
Transport matching mirrors the native convoy-first capacity branch and requires train capacity for the train alternative.
A mismatched request, input kind, selected mobile type or transport branch fails before native emission readiness.
The parent must emit only on the fresh material_transfer_begin_ready flag and use the same selected branch and exact normalized amount it bound to begin.
Do not change selection or insert another native mutation between capture and emission/completion.

| Field/output under gods_of_africa_ | Units and freshness |
| --- | --- |
| material_transfer_begin_ready | Fresh COUNTRY flag, cleared each begin, permits one exact owner emission |
| material_transfer_completion_consumed | Fresh COUNTRY flag, cleared each completion, confirms successful one-time helper accounting |
| material_transfer_output_kind / output_requested | Normal COUNTRY enum/raw request from begin |
| material_transfer_receipt_{source_before,source_after,receiver_before,receiver_after} | Native k for fuel/manpower, raw units for scalar equipment/PP, unused scalar zero for armor |
| material_transfer_receipt_requested_native | request_k for supported fuel/manpower requests, raw for other kinds. With fractional k precision_blocked it retains raw request as an explicitly unusable conversion placeholder. |
| material_transfer_{source,receiver}_<chassis>_{before,after,delta} | Independent raw num_equipment snapshots and positive directed differences for each real chassis, retained while pending |
| material_transfer_source_debit_native / receiver_credit_native | Native k for fuel/manpower, raw for scalar equipment/PP. Armor aggregate is bounded raw, with separate complete per-chassis differences and excess evidence. |
| material_transfer_source_debit / receiver_credit | Raw convenience outputs, bounded by request for fuel/manpower. They do not describe the full excess k delta. |
| material_transfer_actual_amount / receipt_amount | Raw common actual when supported by measurement, may be published while ledger accounting is blocked. A missing unsupported fractional-k amount is an evidence gap, never proof of zero delivery. |
| contribution_fuel_headroom_k | Normal receiver max_fuel_k minus fuel_k, no complete-room conversion |
| material_transfer_full_match | Both native measured differences equal helper request with no armor excess. It proves helper amount equality only. |
| material_transfer_receipt_pending / material_receipt_representation_blocked / material_transfer_native_read_blocked | Retained evidence and quarantine, never permission for another debit or history truncation |
| material_transfer_precision_blocked / audit_domain_unresolved / sequence_allocation_unresolved | Source-audit evidence limitations, not assertions of native unsupported prices or engine maxima |

Parent balance/fulfillment processing must require fresh completion_consumed plus exact output kind/request and independently owned current contract/remaining-balance proof.
Full_match alone does not close a contract.
Pending measured fields cannot be used as a consumed receipt, and they cannot authorize another debit.
For raw fractional 0.5 the native quoted amount stays exactly 0.5, while material-ledger conversion remains blocked and the measured amount/snapshots remain pending.
For fractional fuel/manpower the helper does not claim room sufficiency, request_k precision, raw amount or full_match until native type evidence resolves the representation.
This follows the later owner clarification and does not integer-floor or reprice the payment.

## Helpers, constants, cleanup and migration

The adjacent [API document](../../../../common/scripted_effects/012_africa_gods_contribution_effects.md) maps all scopes, inputs, outputs, defaults, side effects and intended call sites.
New internal effect call sites are capture_contribution_armor_before from begin_material_transfer, capture_contribution_armor_after and measure_contribution_armor_after from complete_material_transfer.
All retain the gods_of_africa_ prefix.
New private trigger contracts cover native kind uses_k, selected-branch matching, conservative before/after readable-value domain and exact prospective accumulation.
Existing conduct, maximum Wrath floor, core return, emergency freeze and campaign activation helpers retain their gameplay design.

The fixed_point representation category centralizes audit_quantum, ceiling and sequence_preincrement_ceiling.
The fixed_point voluntary category now names infantry_capacity, not infantry_reserve.
These are local helper constants, while native prices, cooldowns, grading denominators and reward tuning remain owned by their existing files.

Receipt epoch equals the current participant authority epoch and host authority epoch, plus demand authority epoch for ordinary payments.
Source/receiver object references and IDs, origin, generation, contract ID, day and reserved sequence remain mandatory.
Regular receipt_source targets last through the synchronous chain and are not a replacement for these retained normal fields.
No global target or central router was added.

Exact counter room is computed as conservative ceiling minus the exact receipt increment before ANY total/subset/PP writer runs.
If a total or qualified subset cannot be written, none of the quantity writers runs, pending and snapshots remain, and last_consumed stays unchanged.
Clear refuses representation/native-read failures and abandon refuses measured, pending, captured, mismatched or noncurrent envelopes.
A genuinely unmeasured abandoned reservation records gap_{id,host_id,origin_id,generation,epoch} once for its current host session and advances the reserved ID without quantity.
Successful consumption clears only work, with native outputs, prior history and cumulative totals preserved.
There is no counter reset, lifetime cap or paid-amount waiver.
A wider exact accumulation representation/recovery protocol needs verified type evidence and parent acceptance.

Parent migration remains queued within the accepted design:
1. Wrap actual payment and voluntary branches, using exact selected kind/amount and fresh acknowledgements.
2. Keep typed armor/mobile owner receipts beside the independent snapshots, preserving actual native variants.
3. Keep voluntary infantry 500 shipment, 1000 pre-debit capacity and cooldown, and fuel's exact existing native contract.
4. Freeze actual original emergency context before issue, bind campaign at its actual owned activation, and clear only contract work after accounting.
5. Wire unresolved evidence into final-grade proof and preserve pending transfers through cleanup.
6. Parent independently reviews source and this handoff before integration/publication.

## Meaningful validation and remaining gaps

The reproducible fixture in the repair evidence parses and executes the actual helper sources.
It checks native-range-safe payment arithmetic, family/kind/request denial, per-chassis measurement, exact capacity, replay, epoch drift, fractional pending evidence and atomic counter guards.
Its native stocks are declared inputs and external owner predicates are mocked.
It is neither a complete Clausewitz interpreter nor engine execution.
The fixture's one initial failure was an omitted country id accessor in the test model, corrected before all fifteen groups passed.
No gameplay simplification was applied to fix that fixture.

Primary reference paths, line spans, revisions, successful MCP source references and exact route gaps are recorded in the repair evidence.
MCP event evidence remains focused with zero helper coverage, artifact provenance is unavailable and event comparison lacks a retained baseline revision.
Connected script_validate and verified health/version/task negotiation are unavailable, so helper_expansion/jobs/native tasks were not invented.
No native-engine, live-game or complete event validation was performed.
No probability audit was needed because these observational helpers contain no weighted/AI/probability change.

F2 remains unresolved for native individual stockpile getter range/precision and native subtype/variant observations.
F4 remains unresolved for exact fractional and lifetime representation across getter, normal variable and constant types, plus explicit accounted recovery of retained pending receipts.
Treaty source proof remains blocked because no inspected existing owner provides an accepted continuing participant promise and objective once-only breach identity.
No treaty_break_count writer was fabricated from mark_offender, generic war, refusal, recognition or host-given protection.
Parent hooks, classification, costs, broader documentation/catalog alignment, native owner evidence and final completion remain parent-owned.
No full contribution or Gods completion claim is made.

No gameplay price, design, content route, asset or UI simplification was introduced.
The explicit omissions are native exactness evidence, unsupported exact representation/recovery and parent integration.
Skills used: chaos-redux-events and chaos-redux-subagents.
No skill was created or changed inside this restricted assignment.
