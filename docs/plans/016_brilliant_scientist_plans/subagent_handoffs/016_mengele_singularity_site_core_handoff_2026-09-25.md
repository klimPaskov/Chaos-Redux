# Event 016 Mengele Singularity physical site core handoff

Disposition: implemented. This worker handoff originally covered only an unconnected provider-owned helper layer; engine acceptance remains unresolved.

Parent disposition, 2026-09-25: the helper layer is now connected to private paid construction decisions, state-control reconciliation, provider cleanup, and terminal readiness as documented in `016_mengele_singularity_physical_terminal_integration_2026-09-25.md`. The original handoff's engine-acceptance limits still apply.

## Ownership and acceptance basis

The parent assigned only the private command-node and power-link physical receipt layer for the registered Mengele Directorate. The accepted portfolio closure plan requires `mengele_event016_` state separate from Kruger's board and terminal. The final completion contract requires command and power infrastructure to retain physical site, role, and quantity receipts and to validate current ownership, control, and facilities. The user specified the exact parent-facing COUNTRY trigger `brilliant_scientist_mengele_singularity_site_has_minimum_live_network = yes`.

## Files and identifiers

New files: `common/scripted_effects/016_mengele_singularity_site_effects.txt`, `common/scripted_effects/016_mengele_singularity_site_effects.md`, `common/scripted_triggers/016_mengele_singularity_site_triggers.txt`, and this handoff. Existing files, decisions, events, GUI, map, 3D assets, and call sites were not edited. Nothing was staged or committed.

The implemented helper map, scopes, inputs, outputs, defaults, side effects, example, and array schema are in the matching effects documentation. The primary public trigger is `brilliant_scientist_mengele_singularity_site_has_minimum_live_network`. Public effects are `brilliant_scientist_mengele_singularity_site_reserve_construction`, `_complete_pending_construction`, `_cancel_pending_construction`, `_invalidate_selected_state`, `_invalidate_selected_row`, `_reconcile_receipts`, and `_retire_all`.

The country ledger uses private `mengele_event016_singularity_site_*` arrays, pending metadata, and event target, plus `mengele_event016_singularity_live_command_node_count`, `mengele_event016_singularity_power_link_count`, and `mengele_event016_singularity_live_command_network`. The terminal trigger rebuilds the counts from live rows and never trusts those counters. Existing role, quantity, lifecycle, history, and minimum constants are reused unchanged. No tuning constant was added.

## Behavior and migration

Before this layer, the Mengele provider had Singularity research component receipts but no private physical-site ledger or parent-facing private live-network trigger. The new layer accepts one exact selected state, role, and unit quantity per pending paid receipt. Finish requires matching callback identity, a valid registered provider, and an intact currently owned and controlled qualifying facility. It settles the pending row before the parent can award an outcome. Cancellation and terminal retirement preserve constructed history while removing pending work or deactivating live rows. Explicit destruction invalidates live rows permanently; capture or lost control suppresses live counts until an intact site is recovered.

The parent must add construction actions and cost/timer receipts, bind the private selected-state event target in begin and callback chains, check output markers before payment or reward, call reconciliation after relevant state/facility changes, and call retirement on provider terminal cleanup. No generic country count, component-completion flag, or Kruger physical row may be migrated into a Mengele physical receipt without exact paid-site provenance. A new row has no backward-compatible inferred default site.

## Sources and validation

Read `AGENTS.md`, the eleven required offline wiki core pages, offline Building modding and Map modding, vanilla script concept, script-constant, effects, and triggers documentation, and vanilla achievements with facility and owned/control predicates. Inspected the existing Kruger Singularity site effect, trigger, construction, constant, and documentation pattern, the Mengele provider gate, and the accepted plan and final contract.

Read-only MCP event scan revision `29448ebfff020537225b38e12f67f7354e5426eb1760472685584c673f1956cd` produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a614f3abc89d608f3c23802d6ee5fd0c70b1c0342a4717d218ef8a1ab76ef3b/15cf8f3161c3f57dfd5abe0d2583868568fa28bfaa9b6450b824a39267e0fb10/event-scan-29448ebfff02.json`. Focused trace revision `f50fb76d44de057fe86eff72c777b7748ed6d79862f47b0fef136453dabd22de` produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/70fc12232a3bd93755c8c3be8b4f160078cf3318cc4a4216f6872bec7dd1b512/2f9cc91098243d35a11c68cf8425a0a1a7a5833dd2f43d59b3f9f80dc46fe169/event-trace-f50fb76d44de.json`. The trace was partial and limited to Event 016 root and two levels, so it does not validate the new helper runtime.

Read-only MCP map inspection revision `c3c338113358afda7ba8f4a9a012be8c2276ba35269d8a3236b05977be675a03` produced `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf7d358a8596d84620f0cd23cc2ec53d680ec707bddf0c0aef452c24819de68a/9a7da431b86c619ab5f8aab2afc9f7ade02320d6c9a5c82209e7df8a2a375ade/map-inspect.c3c338113358afda.json`. Its global locator diagnostics are unrelated to a dynamically selected site and no site state was identified by the parent. Source checks cover exact helper references, private-write isolation, shared constant resolution, and new-file scope. Game runtime validation was not performed.

## Risks and parent follow-up

The helper files are deliberately uncalled until the parent wires decisions and the Fallout adapter. Native timed-decision callback identity and refund behavior must be proven at those call sites. The helper does not define a construction price, timer, state-selection UI, or facility construction effect. The parent must prevent payment when reservation fails and prevent reward when completion fails. The live-network trigger requires the existing Mengele provider gate, so a closed or terminal provider cannot authorize Singularity even if intact rows remain. There is no fallback or gameplay design expansion.
