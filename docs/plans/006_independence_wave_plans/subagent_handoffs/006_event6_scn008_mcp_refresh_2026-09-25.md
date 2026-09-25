# Event 006 SCN-008 MCP refresh — 2026-09-25

## Disposition

Status: **STRUCTURAL MCP PARTIAL; SCN-008 execution dossier remains HOLD/PARTIAL**.

This parent-owned refresh records current focused Event MCP evidence and the current 32-cell static matrix result for the accepted SCN-008 publication contract.

It does not prove any scenario outcome, allocation, map safety, event lifecycle, helper closure, probability, GUI, save/load, or live-game behavior.

## Static source evidence

`python .tools/audit_event6_scenario_matrix.py` passed with all 32 mode/intensity cells and eight edge cases.

The publication audit reports one committed-receipt setter, one ledger-visibility setter, one result-pending setter, two pending-flag clearers, one scenario-result dispatch, one scenario-log dispatch, the required `chaosx.nr6.2 -> chaosx.triggerable_scenarios.80` order, and zero failed-branch result or log dispatches.

The source-level P0 publication repair and the September 20 dead-option removal remain recorded in `006_event6_scn008_dead_option_repair_2026-09-20.md`. A subsequent parent patch adds a result-pending launch barrier so the one-day-delayed report cannot read a later scenario generation's shared flags or summary.

The patch sets `independence_wave_scenario_result_pending` only on the committed branch, rejects new SCN-008 launches while it is set, includes it in the existing transaction-busy scripted localisation, requires it for the report event and option, clears it when the report is acknowledged, and defensively clears it in `independence_wave_scenario_reset_summary`. A failed or rolled-back generation still cannot publish a report or ledger.

The relevant user approval basis is the user's 2026-09-25 instruction, “i approve everything,” authorizing completion of the Event 006 scope. This bounded lifecycle guard preserves the accepted success-only publication contract and does not change scenario outcomes or allocation weights.

The source patch touches `common/scripted_triggers/006_independence_wave_triggers.txt`, `common/scripted_effects/006_independence_wave_scenario_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`, and `events/006_independence_wave.txt`. The system explanation is updated in `docs/events/006_independence_wave/systems/triggerable_scenario.md`, and the source assertion is enforced by `.tools/audit_event6_scenario_matrix.py`.

The post-patch `python .tools/audit_event6_scenario_matrix.py` run passed all 32 cells and eight edge cases. Its publication census reports one committed setter, one ledger-visible setter, one result-pending setter, two pending clearers, one result dispatch, one log dispatch, `chaosx.nr6.2 -> chaosx.triggerable_scenarios.80` ordering, and no failed-branch result/log dispatch.

## Initial focused Event MCP inspection before the pending-result guard

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Selectors: `chaosx.triggerable_scenarios.8`, `chaosx.triggerable_scenarios.80`, `chaosx.nr6.1`, and `chaosx.nr6.2`.

Each `hoi4.event_inspect` call used `mode=lint`, `direction=both`, `expandHelpers=false`, `maxDepth=2`, `maxNodes=240`, `maxEdges=600`, and `refresh=false` on the already indexed current revision.

All four reports returned `EVENT_INSPECTED_PARTIAL`, analysis mode `focused`, source revision `55c3687633b124badd7d5e5a75a75f417ec894b9ca1452d6fd6c35511d9ae68d`, and graph hash `85e6a09595e4ab3938f491bd69e879a593d6d1e05e62bafa95064c95ef556dbb`.

The indexed graph reports 9,824 events, 15,175 options, 1,166 entries, zero projected helpers, 8,858 unresolved nodes, 7,764 terminals, 38,496 edges, 30,712 state accesses, 2,195 aggregate issues, zero blocking diagnostics, and zero skipped sources.

The inline source inventory contains 64 of 381 files; the linked reports retain the full inventory.

The service marks validation incomplete because focused lint deferred workspace-wide helper projections and lifecycle passes.

Inspection artifacts:

- `chaosx.triggerable_scenarios.8`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef4e435ee68687eef20c71259d210c9229706e16c00fcf72c7a03e1305304647/c9d1a3880962cc7174a8bf27d591a9bbe89cb8d7c1fffd0cec502121e1d98816/event-lint-55c3687633b1.json`.
- `chaosx.triggerable_scenarios.80`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b98586ab858025bdba4eeba22d17dfaa0f01827f85daa98258b728735f170a13/b0d6fa5c665bf23c4bce0bb1cf92230cc640a395568cafe848176a6226c65e72/event-lint-55c3687633b1.json`.
- `chaosx.nr6.1`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/740cf5393310e5b18ef104185b8fcf27faaeb102c300deed824b7d669e84c3c5/9a3a125269d1a5aac5b1a52e2e684b8541c8a21bc10c72e2ebe596cfe3461f41/event-lint-55c3687633b1.json`.
- `chaosx.nr6.2`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/13c637426b48f1c004019bd5510e03ff22f04b61aa57854d4e9fedd9e8ad9cf4/0281649e14609042b470460100c0c5e496e9e43e3baeaabfe3306364c8338bc7/event-lint-55c3687633b1.json`.

The only reported diagnostic is `MCP_INLINE_FILES_TRUNCATED`, with 381 total source paths and 64 returned inline.

## Initial focused Event MCP renders before the pending-result guard

Each `hoi4.event_render` call used its listed view, `direction=both`, `expandHelpers=false`, `maxDepth=1`, `maxNodes=40`, `includeHtml=false`, and `refresh=false`.

All four renders returned `EVENT_RENDERED_PARTIAL` at the same source revision and graph hash, with zero blocking diagnostics, zero projected helpers, no skipped sources, and zero branch renders.

- `chaosx.triggerable_scenarios.8`, `neighborhood`: 5 selected nodes and 42,782 omitted nodes; manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/697173b461185f958614d60c7acd18571b04a2dd0da62f0e05bed90466ac8035/89ae1c7b85088a5796358a5eea6454b5fe4c44a74121fa146a5fd55bccdca3cb/event-neighborhood-55c3687633b1-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c20a891732b25608b3afd9a7142189961cfa308b19a8217bf0739b7f4f04115/f923bd72772a8cd2689142e4f98a8835918e8191cc1060e81917b357f522bb0b/event-neighborhood-55c3687633b1.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0716b47a6746595c3d30e41cbe487f28263f35f154390c09df38958db74ddee/3164f4a8643aa4d38118db16fd4a05cf0e465b2f1e361e69d4e7b42d8ff9eb73/event-neighborhood-55c3687633b1.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebbb4a33837ad79ae9a5cd7a3fb182ea71988c0d4540eb06d2f3bd7892a742c4/9e42ad33e2906f9648bb4e251f8f9d944cdd196d402576009a8a03b99af39e49/event-neighborhood-55c3687633b1.png`.
- `chaosx.triggerable_scenarios.80`, `options`: 3 selected nodes and 42,784 omitted nodes; manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b744c59e21196c1b84c936b3594cd7d23f791915124bcacca71caa0d7742e1bb/bd80f7c4edc234699bd49f1572db539b10750b7f9692ee49f10ca0aa8e03882b/event-options-55c3687633b1-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/700fa11afe82fd37ed4d33a6b2c665be462af8d871299641aee9c6e38467e101/4438e0e8b7963ccdc67c26f4a44b2b562092f20ecd36de06a955bdc6835d593a/event-options-55c3687633b1.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/03f38168bbe0e8cb62f68ac60507e71f4af4b1aa22b477fcaa09293d215f90d3/23d58b4bf87928e128be9e4f97db0425eaaef32a967935d7f81f532fa84bc769/event-options-55c3687633b1.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/857efa385c44049f7ddbcfebda94f476a34212989eb8d93a6552871b7f2dd070/60078daf5f0649f3a1fd956d066af093ccb19a7d2061cb4e667e712b7e02a464/event-options-55c3687633b1.png`.
- `chaosx.nr6.1`, `neighborhood`: 3 selected nodes and 42,784 omitted nodes; manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd1ad70533ff49f94f554208b92c65909984143a63674cbdfe0d395d79bf3c72/6625101ab8ac8d101957585018c6ef20133b4c01e1c466a8212eeb01af50773f/event-neighborhood-55c3687633b1-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d4882505d6392be5a052906f54ceeeac81365eb2f940c48403d901041ded5a47/40f37b22ddaaa3e5972091f2e40ac20f62500ceb5fe9acb6a7d103590be3afce/event-neighborhood-55c3687633b1.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/75c21cd9239a5b58f5147f8f053956e23b76e7d66ab067e9331c135d727a887/9ba95e44d360d38f441a41c3da4a25e02ca11f39184e26009f1af3c731de10f1/event-neighborhood-55c3687633b1.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa9f9d31a69350abba5c32cc243978095e4d857b671861c0916cc275cd55ae29/e5a84be3e52212112363583e227d1546c8ce23a8adc07b2251c5d40ac52766f6/event-neighborhood-55c3687633b1.png`.
- `chaosx.nr6.2`, `options`: 3 selected nodes and 42,784 omitted nodes; manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc143ace3ad3fcec78e4627a4e829b681dd71e76b787b4ee561e5b41875be33e/2bf7d88e0a88d1f1a81400d436f53d7d82420196f8c33221f7027c6a1f147059/event-options-55c3687633b1-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7b5f9396ddfe43b3a0ce87e6d53955f8866fad9df3456dcba088d8ee644d0e7/e6b3df6dba3fb9a83acb3d60462e3f6bd5bdacc1d82b9d048b3ec5090d21ec5d/event-options-55c3687633b1.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a954bb98d79d3feecba4e863f2abc40b4870b2e993723b524b40a6aac5daff9e/cf29022a2d6573a5adc89e403bea16607624d679319101f8ca16036077d256ac/event-options-55c3687633b1.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e36610b67712494e1967291dc9641a2ed3a088becd1e42127e051f315b76ca3/953d0eaeebfd369da7cc413f219d08c983b545e8dcd37cdd7f9ab7f916dc600b/event-options-55c3687633b1.png`.

These renders are narrow structural views, not acceptance of visible layout or branch behavior; each omits more than 42,700 workspace nodes and reports no branch render.

## Post-patch Event MCP inspection and renders

The post-patch focused inspection of `chaosx.triggerable_scenarios.80` and its paired inspection of `chaosx.triggerable_scenarios.8` return `EVENT_INSPECTED_PARTIAL` at source revision `cc097d15c00f15159a92e4fc4de590cfe2b67224170be81d9d17e55e0c16c587`, graph hash `e4df4522cdd4460f8b3b9cc188e6ae4bcd45f20941f3a607e67d77b6cab4d019`, zero blocking diagnostics, zero skipped sources, and a focused-boundary validation failure because workspace helper and lifecycle passes are deferred. Counts remain 9,824 events, 15,175 options, 1,166 entries, zero projected helpers, 8,858 unresolved nodes, 7,764 terminals, 38,496 edges, 30,715 state accesses, and 2,195 aggregate issues.

- `chaosx.triggerable_scenarios.80` lint report: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64ac2f4efb869ae6897f910dc585349e8117f89c5fde9d11a397cb5fb923ebb3/c9d2e7d683f352f44e76a57b5a36265e9cd4cbd8e2a00cd8635c19727b990f95/event-lint-cc097d15c00f.json`.
- `chaosx.triggerable_scenarios.8` lint report: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbfb0056b7e7f7714e319c1d8c18a892bac8f9c6e8ead35dcb7fe3a11eb91f0b/13611185dccd7b01f08f7e5b77c0f4fa512d4035dc3fe0d6cb41ec51d0d56d4d/event-lint-cc097d15c00f.json`.
- Launch barrier neighborhood render selected 5 nodes and omitted 42,782: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6159d79bfbd9af169eda15b18aa45045a13a95bf9f9884ff72c3a65df17f8e5/46a9fa0f25d7a6a9e59a245e0ebf5583f1d37d25ea719805c26121f721ad0c40/event-neighborhood-cc097d15c00f-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba24bad3bab0e3c57bb30db69ac9d0eef5c5d4b3d78664c3948f2bb5a9976218/3895b8c2336717a9a845a5c145e90f619e7be2c249c4391c75181af635a95192/event-neighborhood-cc097d15c00f.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0716b47a6746595c3d30e41cbe487f28263f35f154390c09df38958db74ddee/0f51e0f167e67f3755f2fede386b469b6e5f685cbb725395422f162f552e17fe/event-neighborhood-cc097d15c00f.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebbb4a33837ad79ae9a5cd7a3fb182ea71988c0d4540eb06d2f3bd7892a742c4/71a403a182aa9ce8a2d51ef1dff504cef17a6efe45be0f7c76706ec8e3d82233/event-neighborhood-cc097d15c00f.png`.
- Public result options render selected 3 nodes and omitted 42,784: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef5f8f41d047038b486b7437270ea91dff6c6420414d369e1ba27a6f3c42acc0/82d79441fb8dd26a1239d90ffc635f69804f961b089c16b3c750c996f4595ca6/event-options-cc097d15c00f-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4934294f28d4570ae713b34b824276ea2bfb33be911439bc3135ae4a59bb559c/3a01741c93231860e1a10caeb3e3e67724bc31c3fbad9c779214c89c6c0dce2d/event-options-cc097d15c00f.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57ba0bd6ae73a9eafa5e6c632eed4a3c21f46774b0b1dac5c11ec58325ea7f5e/74fd76c0e5a510104555effbd6827b31a448a1a124347a30c384476187ed8ee0/event-options-cc097d15c00f.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/857efa385c44049f7ddbcfebda94f476a34212989eb8d93a6552871b7f2dd070/0a0ce846e7f5750e1da38808b84148c1af00bc59f3f474d45fd87c0b4e1be092/event-options-cc097d15c00f.png`.

## Compare and full lifecycle attempts

The pre-patch `hoi4.event_compare` from revision `53cfc668c05d032d7d279e9e9b3ddd7bfd6852cc288bbd5c857f7600bc679964` to `55c3687633b124badd7d5e5a75a75f417ec894b9ca1452d6fd6c35511d9ae68d` returned `EVENT_REVISION_NOT_CACHED`. A post-patch comparison from `55c3687633b124badd7d5e5a75a75f417ec894b9ca1452d6fd6c35511d9ae68d` to `cc097d15c00f15159a92e4fc4de590cfe2b67224170be81d9d17e55e0c16c587` returned the same blocker with no artifacts.

A full-analysis `hoi4.event_inspect` request for `chaosx.triggerable_scenarios.8` using `mode=state_flow`, `direction=both`, `expandHelpers=false`, `maxDepth=2`, `maxNodes=60`, `maxEdges=140`, and `refresh=false` returned `INTERNAL_ERROR` with no artifact at the pre-patch revision. A second bounded request at the patched revision, using `maxDepth=1`, `maxNodes=30`, and `maxEdges=80`, also returned `INTERNAL_ERROR` with no artifact.

The current Event MCP routes are callable, but these attempts do not provide a usable semantic comparison or full lifecycle projection. The focused render omits over 42,700 nodes and reports no branch render.

The `chaosx_event_completion_auditor` sidecar was not available in the preceding run because the account usage limit prevented it from completing; this parent evidence does not replace its required completion audit.

## Remaining SCN-008 work

The 32-cell static matrix and focused structural views do not cover actual scenario outcomes, the eight edge-case execution paths, the state and supply map, nested candidate probabilities, helper and lifecycle semantics, rollback, relaunch, or save/load. The pending-result race is source-guarded and statically audited, but still lacks live execution evidence.

The semantic compare is blocked by the uncached historical revision, and the full state-flow route returned an internal error.

No live-game process was launched; all live SCN-008 execution and save/load validation remain user-owned.

Event 006 remains **HOLD / PARTIAL**.
