# Timed Mask Reservation Probability Compare Handoff

Date: 2026-09-25.
Status: read-only post-edit audit; evaluation evidence is partial and historical comparison is unresolved.

## Scope and current source

Audited `cbrn_supply_occupied_population` in `common/decisions/cbrn_protection_decisions.txt` and `cbrn_deploy_protective_aid` in `common/decisions/cbrn_occupation_decisions.txt` with the `mission_ai_will_do` adapter. The parent reported the post-edit mission durations as 30 days and 21 days respectively; the source entries reference `cbrn_protection_decision_timing.occupied_distribution_days` and `cbrn_occupation_timing.protective_aid_days`.

No source or gameplay file was edited by this audit. The local SHA-256 values captured during this pass do not match the MCP `sourceHash` values returned by the current workspace inspections/evaluations, so the tool results cannot be proven to describe the exact local files.

| Surface | Local SHA-256 | MCP source hash | Inspect revision | Evaluate revision | Inspect artifact |
| --- | --- | --- | --- | --- | --- |
| `cbrn_supply_occupied_population` | `7c029e52c4344b8503cde7257cc4d8d27ee9992e659666751e374ca70fa60a2b` | `9981b52f2d2f96f5aa2546cb52fed7de41eef9093cc49e0fc0e1b4aaee4ad3ae` | `b78a9fa11b67da476c1e99c57e083edc9ecdb4052a141974cb5ea0a8b1ca81e3` | `3387c9e4560850df98a547233821cd78478d46c72d248fa006173580c23fed5e` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/071124426c1d9e7e85102dde536b59df0636e90481539e9141dfb36cb90e1146/bcdaab28c474e8b05e36fb18438b6e525399c30c49135b8af610408615a11600/probability-inspect-9981b52f2d2f.json` |
| `cbrn_deploy_protective_aid` | `1bafef19b302c711f4628f0fa5c96f73f6b68426deba15c32b672dbabab8fe4c` | `f2bd3033a68b6de40f643685aae4affcc890e29fa5e601cfabfd28ac4b28bbb9` | `8b7199307a0ab434b3628894c0326033b394dd2b1895bdffb66bfaf6727bd58b` | `c0b37eaca3f3b39dac7bfd6fb7d63996fc479762e062892b8dccde2266fff4e2` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d58b2820c0f90b5e9e1487e8ef84f06ac2cf2e5a5f98e748261cf1952914a462/fc4ebcacb29fdddcf417c5a494dc248c8950bf37f5edb019566a4a4a7c91812a/probability-inspect-f2bd3033a68b.json` |

## Scenario replay and MCP results

Reused the seven named scenario IDs from the baseline handoff for both surfaces: `stock_none`, `stock_exact`, `stock_above`, `target_eligible`, `target_ineligible`, `policy_available`, and `ai_affordability`. The scenario-set ids were `cbrn_occupied_distribution_baseline_2026_09_25` and `cbrn_protective_aid_baseline_2026_09_25`; actor was `CXT`, with the same flat primitive states, flags, and `FROM` scope values summarized in the baseline handoff. `stock_exact` and `stock_above` remain identical boolean stock inputs because the adapter does not accept a typed inventory count.

The previous handoff saved only the scenario summary table, not the exact JSON fixture. The reconstructed protection scenario hash is `f8bdabfa1cde3e65ca1564de85486d4443dca12f11d2b08ddb4be6fcd8ab03ef`, which differs from the baseline hash `95911f2bcb590d731c2626a92f2139e03da670203153ab62c87de9a30588e052`. Thus matching scenario IDs do not prove byte-identical inputs. The occupation baseline evaluation returned an internal error and has no baseline scenario hash or result artifact.

| Tool and surface | Status | Evidence |
| --- | --- | --- |
| `hoi4.probability_inspect` / `mission_ai_will_do` / `cbrn_supply_occupied_population` | `PROBABILITY_SOURCE_INSPECTED`; pool incomplete; 7 source candidates; 8 required inputs | Inspection artifact above; one initial call returned `INTERNAL_ERROR: Unexpected internal error`, then an identical retry succeeded |
| `hoi4.probability_inspect` / `mission_ai_will_do` / `cbrn_deploy_protective_aid` | `PROBABILITY_SOURCE_INSPECTED`; pool incomplete; 3 source candidates; 11 required inputs | Inspection artifact above |
| `hoi4.probability_evaluate` / protection | `PROBABILITY_ANALYZED_PARTIAL`; 7 scenarios; 7 candidate rows; 2 unresolved; 0 diagnostics | Analysis `probability-ce7b1121afddfcbf38497dec`; scenario hash `f8bdabfa1cde3e65ca1564de85486d4443dca12f11d2b08ddb4be6fcd8ab03ef`; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d07202b5575129ed7d596f6377d048e4c5dc04ff5fec373fa8f038cf4bc6387b/fc89bad4ab31f917e71975a5a12a28157c513dfab4def6946593d3ca22fd7061/probability-ce7b1121afddfcbf38497dec.json` |
| `hoi4.probability_evaluate` / occupation | `PROBABILITY_ANALYZED_PARTIAL`; 7 scenarios; 7 candidate rows; 5 unresolved; 0 diagnostics | Analysis `probability-226ba1dbc5ae865c62646111`; scenario hash `73505db456abf84045217903747c705ece4ace1c2802c04520b54d2f9522681c`; JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44cca393b1a55d4d7574afa7df836fc6202c07951b7cd21c103c3db971747247/bdfbde60753c8ab2c42428aaf72a5fa8182b2017e89cb9a77934056ba0e3e650/probability-226ba1dbc5ae865c62646111.json` |
| `hoi4.probability_evaluate` / protection, first attempt | `INTERNAL_ERROR: Unexpected internal error`; no artifact, scenario hash, source revision, or diagnostics | Identical retry returned the partial result above |

Protection visual artifacts: ranking SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0bf5c15b387479a5d915aa0cb76695222ce69a3c841bda3a047eee3d3349d544/48be45e71ecb067337f172453bb40c695b52ddcf39af5c6a50779b5d4dbfba9d/probability-probability-ce7b1121afddfcbf38497dec-ranking.svg`, matrix SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cfbf11f9f363f0b8203b43e78c3b5f8512a7c59be2ae093e901ec337b779f0fb/6f1862a5d738b30cc3791c28f9b62eaf3a9a446a668ee9329a921ff312e74775/probability-probability-ce7b1121afddfcbf38497dec-matrix.svg`, and unresolved PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b289a3562d70cfb6a6fddaa03e8eccc3b637eb54aa79f5e21208425332468b8f/5989120a78b0deab5d8bab4454f01f31a3f18ba74126382fdeb25ec376163f00/probability-probability-ce7b1121afddfcbf38497dec-unresolved.png`.

Occupation visual artifacts: ranking SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea6111f0942a5a2f448736a67667c84261d1da582ebf86ae35063f2fb02b83e9/31b723f44aa72f008338ba636467a3e131ba5d3e8a749d44712c2aa45ccbd0f1/probability-probability-226ba1dbc5ae865c62646111-ranking.svg`, matrix SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64f36053a495917f9a5c59a1ca62afc605a157d0ddd8b6bb6f3c89b38c3ba264/29e50472931ef0c4b9503a9888d2cb2be60279d89223d64e9a434ea11b366d60/probability-probability-226ba1dbc5ae865c62646111-matrix.svg`, and unresolved PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f9e01f2ba72208476bae79bfb4d564b158e1a566e5a0014e5c752e1796697ca/ac78fe2e59ae18528a87197204dd21f3bd00f7e43935ff76ef08280a77133e68/probability-probability-226ba1dbc5ae865c62646111-unresolved.png`.

## Comparison safety and interpretation

No `hoi4.probability_compare` call was made. The comparison contract requires valid before and after source paths. There is no preserved historical source file path for the baseline, the previous occupation evaluation produced no baseline artifact, the protection scenario hash was not reproduced, and the current MCP hashes differ from the local file hashes. Comparing the current path to itself or supplying an unverified historical source would not be attribution-safe. Both requested historical comparisons are unresolved.

The mission adapter is score-only and does not expose normalized selection probability or mission completion-time distributions. The tool results are partial and pool-incomplete, with no basis for claiming an exact probability, timing shift, rank change, dominance, starvation, or AI behavior improvement. The exact/above inventory distinction, eligibility gates, and AI factory affordability are not proven by these primitive fixtures. The parent should treat the returned after traces as unverified against the local patched sources until the MCP workspace hash synchronization and historical before sources are resolved.

## Follow-up and blockers

1. Re-establish MCP source synchronization so inspection/evaluation source hashes identify the saved local decision files.
2. Preserve the exact baseline scenario JSON and historical source snapshot before any future weighted edit.
3. Rerun `mission_ai_will_do` evaluation and `probability_compare` with a matching scenario hash and valid before/after source files. Keep the interpretation score-only; the mission adapter does not quantify selection probability or completion timing.

No sweep, simulation, or sequence analysis was run. The seven fixed scenarios contain no declared input distributions or complete custom pool with cadence/transitions; the inventory booleans also cannot support an exact-versus-above threshold sweep. No further retry was made after the identical protection retry succeeded.
