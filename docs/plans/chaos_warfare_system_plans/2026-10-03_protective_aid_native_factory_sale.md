# Protective Aid native factory sale implementation

Disposition: implemented and independently reviewed in source; recovered MCP evaluation is partial and comparison retries remain unresolved, with native execution unverified.

The accepted [owner correction](../../specs/chaos_warfare_system_specs/corrections/2026-10-03_protective_aid_native_factory_sale.md) closes the previously unadapted factory commitment while preserving the conserved respirator shipment.
The ordinary and sale native definitions share one public label, cost row, icon, 21-day timer, complete/cancel/remove callbacks, and the original willingness body.
The native modifiers use two factories normally or one for a valid one-factory canonical quote.
Factory quotation uses `universal_cost_family.factory_commitment`, ordinary quantity two, quantum one, the registered Black Friday source, and the live exact producer; unsupported or invalid quotes fail closed.
Nominal half and quarter sale modes both round to one whole factory.
The sale definition's fixed AI saving hint is the smallest positive currency quantum, while actual PP affordability remains the canonical quotation; the ordinary hint remains 25.

The new module files are `common/scripted_triggers/cbrn_protective_aid_decision_triggers.txt` and `common/scripted_effects/cbrn_protective_aid_decision_effects.txt`.
They centralize source/price checks, native selection, reservation, one PP payment, completion, cancellation, and receipt settlement.
The native selection stamps the donor/state `cbrn_external_aid_purchase_cooldown_@ROOT` timed flag for the existing 90-day reenabling interval, including a failed activation, so switching definition IDs cannot evade the same interval.
The post-selection callback deliberately omits that freshly stamped cooldown and free-factory availability while retaining country, source/price, PP, stock, and target checks.
Selection mode stays bound to its actual native commitment through sale expiry and national stock depletion.
The existing common close clears the mode and committed display fee, but does not erase the independently expiring cooldown.

The five real mask models remain a composition of one pooled respirator-crate resource, not five independently chosen prices.
No shipment quantity is discounted and no additional model debit occurs at timer completion.
The existing state escrow, recorded donor, exact-model refund, positive-reservation PP payment, and delayed successful-delivery receipt still own the resource transaction.
The fee, factory count, and model breakdown shown during a running delivery read its committed state data rather than repricing against an expired sale or emptied stockpile.
Failed activation leaves no successful delivery receipt, and the existing native cancellation predicate rejects a missing escrow or invalid country/target; native cancellation owns factory release, with its precise tick timing still unobserved.
No manual factory credit, second attack adapter, administrative selector, periodic iteration, equipment definition, or CXT grant was added.

## Source checks and balance

The [baseline identity record](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_before/baseline_identity.json) verifies that all seven immutable before files match recorded commit `f9f057581c080784b92ed14fd0a736f6f9708958` after line-ending normalization.
An earlier auditor sampled constants after the owner's first constant patch; that later sample does not invalidate the immutable before set.
The [source-contract record](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_before/source_contract_result.json) compares 27 just-below/exact/above factory/PP combinations, selected/current-quote visibility states, and shared cooldown boundary cases.
The original willingness bodies match in both native definitions, and every retained unrelated occupation action is unchanged.
Both definitions call one shared reservation and PP-payment entry point and the same completion/cancellation owners.
Nominal factory commitment falls from 42 factory-days to 21 during either sale rate; delivery remains 21 days, reenabling 90 days, and actual respirator quantity unchanged.
These are source and arithmetic cases, not observed game payments, cancellation, or AI choices.

The [architecture review](subagent_handoffs/2026-10-03_protective_aid_factory_architecture_review.md) identifies caller-owned temporary storage, PP/factory output separation, post-click cooldown omission, and preserved timer mode as required contracts.
The parent initializes generic and aid-specific outputs before nested quotations and payment, resets the factory quantum before PP quotation, and initializes completion proof before the delivery helper.
The generic Event 026 source files are being edited by another owner and are not part of this write set or commit.

## Recovered MCP route and evidence limits

The parent recovered a live v3.6.0 stdio client through the installed official SDK and a temporary configuration with private state and workspace-storage roots, one exact mod workspace, and no broad `modRoots` discovery.
The [connection record](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/connection.json) records successful initialization, ping, server version, and empty client capabilities; no native task/helper-expansion route was assumed.
The [live tool inventory](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/tools_list.json) supplies actual schemas.
The initial [weighted-source discovery](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/aid_after_probability_inspect.json) returned `PROBABILITY_SOURCE_DISCOVERED` and classified both aid definitions under `mission_ai_will_do`; it did not evaluate their scenarios.
The startup recovery investigation found that the normal shared service can restore interrupted transaction bytes before connecting, so the private empty transaction state was necessary to preserve other agents' work.
The [route-recovery handoff](subagent_handoffs/2026-10-03_hoi4_evidence_route_recovery.md) records the supported configuration and the separate absent standalone Technology Tree Viewer.

The same forty declared scenarios were evaluated before and after with scenario hash `b3c4ca4c08650b5bd0c80a98e339fec52b50d3c5a97b9fb8164f30165205f8c9`.
The [before evaluation](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/aid_before_evaluation.json) returned `PROBABILITY_ANALYZED_PARTIAL` with 40 candidate rows, 20 excluded, 20 unresolved, and 133 unresolved items.
The [after evaluation](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/aid_after_evaluation.json) returned the same partial status with 80 candidate rows, 22 excluded, 58 unresolved, and 208 unresolved items; two native definitions explain the doubled row count, not a doubling of attacks or an established choice probability.
The [compact unresolved evidence](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/probability_unresolved_summary.json) retains actual code/path counts, provenance, source revisions, and artifact metadata while the [artifact manifest](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/probability_artifact_manifest.json) binds lossless compressed copies of the 44 MB and 76 MB authoritative traces and the matching unresolved visualizations.
It identifies unsupported trigger-side temporary-variable and conditional evaluation alongside missing declared actor/target facts; no synthetic quotation results were substituted to force eligibility.
The controlled before input expands the two changed old availability helpers from the immutable baseline while using the same current shared Event 026 framework on both sides.
That preserves the old two-factory Boolean gate for this comparison but is not a complete historical mod snapshot or proof that nested temporary-variable execution is equivalent in the engine.
The [forty-scenario comparison](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/aid_same_scenario_compare.json) failed with `INTERNAL_ERROR`; the [narrower 27-boundary retry](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/aid_same_scenario_core27_compare.json) failed with `JOB_WORKER_EXIT` and produced no terminal analysis artifact.
A final [three-anchor retry](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/aid_same_scenario_exact3_compare.json) did return `PROBABILITY_ANALYZED_PARTIAL` for ordinary two-factory/25 PP, half-sale one-factory/13 PP, and quarter-sale one-factory/7 PP, at scenario hash `6875751c294a3da4ffac4ab7f9ef68fe84744a576b0c8b03aa8ac864fb823d98` and source revision `9a383ce59828abaa638533232c374c886237582c68f5b921798cae0bbc7cd91d`.
Its six [candidate deltas](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/aid_exact3_comparison_deltas.json) remain unresolved, with no numeric score/probability delta; the old ordinary two-factory gate excludes both one-factory sale anchors before the change, while the after quotation is unresolved.
The analyzer labels all six comparisons `UNRESOLVED_ANALYSIS_INTRODUCED`; those are recorded coverage regressions rather than proven gameplay regressions.
Both informational diagnostics report an unexercised trauma modifier in these three price-only anchors.
The same adapter and declared assumptions were retained, and the complete comparison plus attribution is persisted losslessly in the artifact manifest.
No normalized probability, exact after-affordability verdict, or native transaction proof is established by the partial result.
The native decision scenario route returned `INTERNAL_ERROR` for the ordinary definition and timed out for the sale definition, with no scenario artifact; the sale lookup was retried as a narrower inventory query.
That [inventory retry](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/aid_native_sale_decision_inventory_retry.json) returned `DECISION_ANALYZED_PARTIAL` at revision `dce2bd1c70c345762deabad3d8fee3f7eca605768580432a9010fce178a67ed9`, scanning 7,945 decisions with 218 unresolved definitions and no scenarios.
It is global inventory coverage despite the requested ID, not native timer execution or a row render.
The actual after-analysis unresolved visualization was inspected and agrees with the recorded unresolved count; it depicts analyzer uncertainty rather than a native cost-row render.

The actual native commitment/release, failed activation, simultaneous targets, source expiry, receipt settlement, AI choice, and native row rendering still require stronger evidence.
No full clean error log, native factory execution, or numeric probability comparison is claimed from the source tests or discovery response.
Event 026 remains default-disabled while broader owner coverage is incomplete.

Large exact call requests are compressed losslessly and indexed by [request archive manifest](../../testing/2026-10-03_cbrn_protective_aid_factory_sale_mcp/request_archive_manifest.json); the readable forty-scenario fixture and expanded before source remain in the probability handoff folder.
