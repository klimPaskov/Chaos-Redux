# Immediate Civil Defence sale transactions

Disposition: implemented and reviewed in source; matching MCP comparison returned partial evidence, with native execution and cost-row rendering unverified.
The [accepted correction](../../specs/chaos_warfare_system_specs/corrections/2026-10-03_immediate_protection_sale_transactions.md) covers Emergency Distribution and Hospitals/Utilities from Event 026's remaining CBRN protection owner inventory.

Emergency Distribution retains the complete existing physical five-model issue, need, wastage, fitting, filters, military priority, and state/country coverage accounts.
Only its PP service fee is quoted: 10 normally, 5 at the nominal half sale, and 3 at the nominal quarter sale.
A recorded fee precedes issue; zero issue refunds it and grants no surge, congestion, or purchase credit.
Positive real consumption commits the fee and invokes the original outcome through a debit-free helper.
The owner refund path refuses that committed receipt ID; a later unavailable confirmation cannot turn retained coverage into a free issue.
The inspected issue/outcome helpers do not mutate universal receipt data, and the maintenance call only schedules the existing delayed country job.

Hospitals/Utilities consumes preparation materials without adding civilian mask coverage.
It quotes the PP fee and one aggregate mask/support price, allocates the mask charge among exact real models oldest first, and pays/records all components before the protection outcome.
At the synthetic ordinary 30-mask/20-support profile, the full order costs PP10 plus 30 masks and 20 support; half costs PP5 plus 15/10, and quarter costs PP3 plus 8/5.
The original 14-day protection effect is unchanged; temporary savings do not multiply issue, protection duration, or combat modifiers.
Zero-paid model rows retain unfilled ordinary counterfactual cost solely as accounting and create no inventory.
Late payment, recording, or settlement failure grants no protected flag/modifier and refunds the actual recorded models through the shared API.
An unrecorded native credit failure retains exact kind/amount for an idempotent retry; partial/rejected recorded refunds retain their diagnostic and paid receipt evidence.
Unused allocator proof is cleared if no first receipt row exists.
Malformed shared receipt data is a detected recovery boundary; no engine rollback is claimed from source execution.

The existing STATE entry points and gates delegate through ROOT to the COUNTRY transaction, retaining FROM as the selected controlled state.
Both human and AI clicks use the same callbacks.
The original willingness blocks are unchanged; the two native saving hints use the minimum whole-PP quantum so a full-price hint cannot exclude a cheaper quote.
The cost row colors each payment separately with the same current quotation and existing PP, respirator-archetype, and support-equipment icons.
A source audit caught Unicode pipe corruption in fourteen owned text keys; the actual currency/color codepoints were repaired before commit.
Expected-outcome tooltips are conditional, so a rejected transaction does not promise completed protection.
No new decision, UI window, periodic loop, equipment, unit, technology, or CXT content grant is added.

## Source evidence

The six [before files](../../testing/2026-10-03_cbrn_immediate_protection_before/source_manifest.json) capture the actual shared working tree, including other owners' caller-storage repairs; they are not asserted identical to HEAD.
The [architecture review](subagent_handoffs/2026-10-03_cbrn_immediate_protection_cost_architecture_review.md) distinguishes full issue from consumed preparation and confirms typed receipt metadata, returned output storage, exact model allocation, and the post-issue boundary.
The [decision audit](subagent_handoffs/2026-10-03_cbrn_immediate_response_decision_audit.md) records exact cost-row and callback findings.
The [actual-source test suite](../../testing/2026-10-03_cbrn_immediate_protection_source_tests.js) executes the two CBRN component/refund helpers and the real shared debit/credit/receipt APIs, modeling native resource queries/effects alone.
All 21 top-level scenarios pass, including cold/warm helper frames, mixed-model payments/refunds, repeated-refund refusal, failed first/later components, unused allocator cleanup, zero-paid counterfactual rows, committed emergency refusal, corrupt-chain diagnostics, and exact stored-credit retry.
The result records 1,074 actual helper returns and 3,576 discarded helper-local values, with selected source bodies stable during the run.
Its [handoff](subagent_handoffs/2026-10-03_cbrn_response_receipt_source_tests.md) states the limits: component input amounts/allocations are explicit fixtures, not proof of the quote producer, full ROOT/FROM order, physical issue, engine behavior, performance, or pending-credit creation after a native credit fault.

## MCP and remaining acceptance

The isolated installed v3.6.0 SDK route answered the narrow emergency discovery, hospital baseline inspection, and two-candidate after inspection under `decision_ai_will_do`.
The [baseline evaluation](../../testing/2026-10-03_cbrn_immediate_protection_mcp/immediate_protection_before_evaluation.json) returned partial analysis for 17 scenarios and 34 candidate rows: zero resolved eligible, four excluded, thirty unresolved, and 34 unresolved items.
Its scenario hash is `432219b1fa1459d920bdea3e411eccfd1a6e47d7f71714c44d87feeb399e4ecf`.
The baseline decision input expands exactly the two changed old gate bodies while sharing unchanged current helper/framework context; it is a controlled source comparison, not a full historical mod or native-frame restoration.
The [persisted baseline summary](../../testing/2026-10-03_cbrn_immediate_protection_mcp/before_summary.json) retains candidate raw-value/support fields, uncertainty, metadata, and provenance, with a lossless authoritative archive.
No normalized AI choice, native stock deduction, full refund, issued coverage, live tooltip/cost-row fit, or clean error log is claimed from that partial result.
The [after evaluation](../../testing/2026-10-03_cbrn_immediate_protection_mcp/immediate_protection_after_evaluation.json) reached the same 17 scenarios and 34 rows with 43 unresolved items; the [matching comparison](../../testing/2026-10-03_cbrn_immediate_protection_mcp/immediate_protection_same_scenario_compare.json) returned partial analysis with 77 unresolved items at source revision `2ec709441cb0d4375aeebed2b5c6916f2ac955c40eb3cc025d8a104f3f386ec2`.
The [actual deltas](../../testing/2026-10-03_cbrn_immediate_protection_mcp/score_and_eligibility_deltas.json) retain zero raw-score/rank deltas in all 34 rows and unchanged eligibility fields: four exclusions and thirty unresolved.
Raw score-only priorities remain 120 for both orders in ordinary price/material cases, 360 emergency versus 120 hospital at trace contamination, and 240 hospital versus 120 emergency above 2,500 population-k.
Those in-scope priorities are useful modifier evidence, not normalized click probabilities or proof that discounted stock/payment gates work in the engine.
The analyzer's introduced uncertainty is recorded, including quote-valid/affordable outputs and trigger-side temporary arithmetic; no fabricated quote output was supplied to make eligibility pass.
The [artifact manifest](../../testing/2026-10-03_cbrn_immediate_protection_mcp/artifact_manifest.json) binds lossless original analyses and their emitted visualizations.
Native execution/receipt/row evidence and resolved quote/order coverage remain required.
A [three-point population sensitivity sweep](../../testing/2026-10-03_cbrn_immediate_protection_mcp/immediate_protection_high_population_sweep.json) also returned partial score-only analysis at scenario hash `d479bcfe935b4fe56cc9cfdc3a20f15214f4a441936c5cf8d45182060e75496c`.
Both orders score 120 at population-k 2,000 and 2,500; hospital rises to 240 at 3,000 while emergency stays 120.
The emitted rank-reversal/threshold-cliff diagnostic therefore brackets the existing greater-than-2,500 hospital factor; the lower scores are a tie, not an established emergency preference.
Eligibility is unresolved, and ordinary material inputs are held fixed in this one-axis score sweep; it is not a price recalculation or engine-frequency measurement.
Exact large requests are retained losslessly by [request manifest](../../testing/2026-10-03_cbrn_immediate_protection_mcp/request_archive_manifest.json).
No public event-log/detail/evolution wording or catalog field changes in this payment tranche, so no workbook save/CSV regeneration was warranted.
Skills applied are decisions/missions, events integration, subagent routing, and isolated shared-tree commits; no new skill is added by this tranche.
No gameplay simplification is introduced by these two payment repairs; omitted native/full-order evidence and the two remaining source actions are explicitly listed above.
Export and Occupied Distribution remain separate source work; the broader CBRN overhaul and Event 026 remain incomplete.
