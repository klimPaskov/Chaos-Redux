# MCP 3.5.1 documentation reconciliation

Scope: `completion.md` and `resume_packet.md` in the parent `administration_redesign_2026-09-06` directory.
Disposition: implemented documentation correction within the user's request to resolve stale MCP capability and proof claims.
The parent applied narrow evidence wording to both shared documents; their gameplay status remains incomplete.

The [receipt manifest](receipt-manifest.json) binds six archived JSON receipts to their original paths and exact byte hashes.
These receipts cover [GUI qualification](receipts/gui-qualification.json), [inspect](receipts/gui-inspect.json), [render](receipts/gui-render.json), [conditional AI comparison](receipts/probability-comparison.json), [probability regression tests](receipts/probability-regression.json), and [renderer source identity](receipts/renderer-source-identity.json).
The [application record](application.json) records the narrow shared-document edits.
Those two documents are untracked work owned by the broader system task, so they are not added wholesale by the MCP qualification commit.

## Source of truth and dispositions

| Surface | Evidence and disposition | Limit |
| --- | --- | --- |
| Public MCP delivery | The canonical `C:/Users/klimp/Documents/Projects/hoi4-agent-tools/.tmp/qualification-3.5.1.md` reports published 3.5.1 at `83079ff85089e5773a0cd1511ee91e47628a2b6f`, a fresh installed process exposing 34 tools, and unchanged renderer/domain implementation from 3.5.0. Record as qualified package and route exposure. | Tool exposure and publication do not certify every current Chaos Redux surface, a standalone viewer, or engine behavior. |
| GUI `date` and `controls` | The 3.5.0 `gui-mcp-qualification/report.json`, `gui_inspect.json`, and `gui_render.json` use `scenario.date = "1944.6.1"` and `scenario.controls = {"88":"GER"}` for `repression_ledger_window`; inspect returned `GUI_INSPECTED` and render returned `GUI_RENDERED` with source revision `a75adc6c001706ba83b70bed80ce0f3201b79d53eb69dd3b7575f504cc52f2fc`. The report binds the request to `mcp/after/picker_ger_1944_radical_hover_125.json`, SHA-256 `7b995b80bce7c6aea5b8786c912851109a8e161f559c1d0ee3363b6c210a232f`. A separate live read-only `hoi4.gui_inspect` of current `repression_ledger_window` also accepted a declared `1944.6.1` date and state-88 GER control, returning `GUI_INSPECTED`, no blockers, and source revision `90cd5d13dd9579f05313734c00dfbaa0fc1625dda1f0cf9d00d11dd14d1de668`; its artifact SHA-256 is `de0a9f74224079279b502cfef7af58b2b5eea3fe4df8a697d86d339728c1b0f1` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/de0a9f74224079279b502cfef7af58b2b5eea3fe4df8a697d86d339728c1b0f1/183c420678fd4a8407d7d2cc55630a2bd3a0eeb6e68bc269d2ff465fa702b51b/gui-inspect.90cd5d13dd9579f0.json`. Treat the previous schema rejection as a historical attempt and the later declared-fixture requests as schema-qualified. | These are declared source-render or inspect inputs, not observed 1944 campaign controllers, native clicks, tooltip display, or engine receipts. The [45-case source review](../current_click_matrix_3_5_1/README.md) records bounded image and per-state click-overlay evidence; native interaction and engine acceptance remain separate and unproved. |
| Populated native templates | `C:/Users/klimp/Documents/Projects/hoi4-agent-tools/docs/gui-comparisons.md` describes source-declared decision and occupation fixtures, including declared control of states 87 and 88. Preserve them as layout examples. | The decisions are not asserted simultaneously available in a campaign; unavailable occupation quantities are dashes, and the native action's engine availability is not evaluated. |
| German transfer AI | The specialist's existing `ai_evidence/transfer_decision_baseline_2026-09-26.md` and `ai_evidence/transfer_availability_probability_2026-09-27.md` retain their original, partial scenario handoffs. The later `C:/Users/klimp/Documents/Projects/hoi4-agent-tools/.tmp/real-mcp-qualification/probability-comparison.json` reports `decision_ai_will_do` conditional source scores `55→55` for `GER_CAPS_CLEAR_ELIGIBLE_SCORE`, `0→55` for `GER_SITE_CAP_BREACHED_ELIGIBLE_SCORE`, and `0→55` for `GER_EXPERIMENT_CAP_BREACHED_ELIGIBLE_SCORE`, with comparison source revision `70218efb4ff851fd310525e61383f6a5712af4d7af9f695e20cddcd35805db09`, source hash `ea983398aad10368114a4ce8e2ba8356dd686682cb0ced6287afff93c505ba0c`, and scenario hash `d87681c3977cd85a5369c0e35b888e40ad620ddedc0546134bb2d0554b97e2dd`. Record this as a later, separate frozen-source comparison without overwriting historical failed attempts. | Eligibility is a declared scenario assumption, while actual availability, competing selection, and AI click probability remain unproved. The `chaosx_ai_probability_auditor` handoff and parent review remain the package boundary for weighted logic. |
| Engine and native interaction | The user explicitly reports no saves available. Preserve the source-model and MCP visual findings as bounded evidence. | Native tooltip display, window raising, scrollbar and selected-location clicks, actual payment, transfer/debit/credit/bind, survivor release, delayed callback, and timer receipts remain unproved. Do not infer engine success from source-rendered fixtures. |

## Documentation audit

The corrected contradiction was `completion.md` item 5's present-tense claim that the MCP scenario schema rejects `date` and `controls`.
The resume packet distinguishes accepted scenario inputs from unproved campaign control and records current connected-service health.
The earlier failed German-transfer comparisons retain their historical evidence, while the exact conditional-score result is recorded separately.
The latest explicit answer that no saves are available is recorded alongside the earlier save-header history.

`completion.md` remains the package status report and `resume_packet.md` remains its index.
Their plan disposition is active implementation with unresolved native and engine acceptance.
This MCP documentation correction is implemented; the proposal is superseded by the application record.
No prompt, design decision or gameplay source changed.

The parent reviewed the proposed wording and the exact archived GUI and comparison receipts before applying the narrow corrections.
No new user design decision is inferred; the wider unresolved policy choices in the resume packet remain separate.

## Validation and remaining risk

The named JSON reports were inspected for request `date` and `controls`, result codes, GUI source revision, and probability source/scenario hashes.
One narrow current-source read-only `hoi4.gui_inspect` accepted the declared date and controller fields and returned the artifact above.
The curator requested no duplicate render and performed no game launch, save search or log search.
The parent reviewed the receipts and applied the documentation patch.
The independent [45-scenario source review](../current_click_matrix_3_5_1/README.md) is complete for its declared inputs and includes a separately archived click overlay for every case.
Nine targeted hover requests display the requested hover; six resolve to disabled states, split between intentionally locked controls and absent selected-state bindings.
Native interaction and engine proof remain unresolved.

The named `C:/Users/klimp/Documents/Projects/hoi4-agent-tools/.tmp/probability-condition-recheck.json` reports 108 passing tool regression tests with zero failures. That test receipt supports the condition evaluator's qualification only; it does not establish this campaign's availability or any AI click rate.

## Handoff to parent

The curator initially changed only this note and `proposed_patch.md`.
The parent added byte-preserved receipts and applied the narrow capability corrections recorded in `application.json`.
No gameplay identifier, key, tag, state group, prompt, asset or spreadsheet was changed.
The older handoffs remain with their original bounded evidence.
All 45 images and overlays have bounded review evidence; this does not establish full native-interaction or campaign acceptance.
Native UI execution and engine receipts cannot be inferred from static MCP fixtures and have no available save evidence.
