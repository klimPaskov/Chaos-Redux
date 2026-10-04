# Event 021 linked-chain MCP revalidation

Date: 2026-09-25.

Disposition: **implemented as current audit evidence; lifecycle coverage remains blocked/partial**. This is a parent-owned read-only MCP and source-freshness revalidation. It changes no gameplay source and does not certify runtime behavior.

## Current-source identity

The connected HOI4 workspace was `mod_chaos_redux_ea3b2d67c2c0`. The live `hoi4.event_inspect` schema exposes `scan`, `roots`, `trace`, `explain_path`, `state_flow`, `lint`, and `impact`; `hoi4.event_render` exposes the documented read-only views. Neither schema exposes a `helper_expansion` mode. The current tool/resource inventory exposed no separate HOI4 server health or version endpoint; the version recorded by the earlier audit was not independently reverified in this pass.

Fresh selector-scoped Event 021 overview MCP source hashes match local `Get-FileHash` results for the four linked event files and the Event 006 support-event file:

| Source | SHA256 |
| --- | --- |
| `events/004_random_war.txt` | `e9b3496b334f2194ceb024ce56bfb434d43d4031c219c7db729f93e7c252bba9` |
| `events/006_independence_wave.txt` | `c1cedb06f2a79613bb96173180ff8c66536fcebf0f24344534629350a694185d` |
| `events/006_independence_wave_support_events.txt` | `f8db738666dc14003dc3240dd027da3ddd8ec3f67ee85465b9c8f580b4265021` |
| `events/007_fury.txt` | `7a5b762dc546c58b9ceb2ee41e9ae0d877c10d41e42e8ce41f519f2f3d5ca27f` |
| `events/021_random_civil_war.txt` | `0480e9ebb1fa78096a081a0b597ae8b1072b149d66c9990c5b32b1433d59685e` |

## Fresh event roots and renders

Fresh read-only `hoi4.event_inspect(mode=trace)` requests for Event 004, Event 006, and Event 007, plus `hoi4.event_render(view=overview)` requests for all four roots, used selectors `{kind:event,eventId:...}`, downstream direction, depth 5, and a 100-node render bound. The four renders share graph revision `1a03026de1cf615664728b4f3e312d0520ddf15b08c3d23bdd86a569ab2cae43` and graph hash `f6dcaf08c60bf08783d148ff440e412c96e0028720eddd827a0febdb35feb180`.

| Root | Render result | Selected graph result | Artifact |
| --- | --- | --- | --- |
| `chaosx.nr4.1` | `EVENT_RENDERED_PARTIAL`; 2 selected nodes; 0 helpers; 0 blocking diagnostics; 0 skipped sources | `random_war_fire_current_context` is shown as unresolved at `events/004_random_war.txt:33`; the helper exists at `common/scripted_effects/004_random_war_effects.txt:732` | [overview JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4d9cfd3acf2f30f6a6e1b0c770a37f7c46b58282ec34f9305ea750d25f4cf58/afd40bad83aa21ecc3616260083be97a850f94fc234b5b488a4541434e97e656/event-overview-1a03026de1cf.json) |
| `chaosx.nr6.1` | `EVENT_RENDERED_PARTIAL`; 5 selected nodes; 0 helpers; 0 blocking diagnostics; 0 skipped sources | The graph reaches `.nr6.2` and its single report option, then marks `independence_wave_prepare_and_execute_standalone_incident` unresolved at `events/006_independence_wave.txt:52`; the helper exists at `common/scripted_effects/006_independence_wave_execution_effects.txt:1184` | [overview JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1041614ab72e9e618b6949fbc3f8b6aa565865530127c4365ac681e8023c72c5/6a58a474ea7b82137291d2d50d19f9a8d4c21e0753a6e573b2986456fc095e1c/event-overview-1a03026de1cf.json) |
| `chaosx.nr7.1` | `EVENT_RENDERED_PARTIAL`; 2 selected nodes; 0 helpers; 0 blocking diagnostics; 0 skipped sources | `fury_prepare_random_event_fire` is shown as unresolved at `events/007_fury.txt:32`; the helper exists at `common/scripted_effects/007_fury_effects.txt:85` | [overview JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99674bfc8decd5d93ba1ab4af88477909ac12fd486f6463bf13af6ba401990cb/b34573b9afc552b8570d518e301a05530974b6766f0ca3b6fc36f582d60e5de0/event-overview-1a03026de1cf.json) |
| `chaosx.nr21.1` | `EVENT_RENDERED_PARTIAL`; 2 selected nodes; 0 helpers; 0 blocking diagnostics; 0 skipped sources | `event021_parent_dispatch_opening` is shown as unresolved at `events/021_random_civil_war.txt:19`; the helper exists at `common/scripted_effects/021_random_civil_war_parent_effects.txt:6759` | [overview JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51acddec216378eedecf4b3facb3f1496255606961973ab54e809fd5b0fe9a8b/1f8325e4e57af08dadcad8061b503f9e4316bec8028fe050eb09b1cc3528ce4a/event-overview-1a03026de1cf.json) |

The overview manifests report `complete=false`, 42,834–42,837 omitted nodes, a 383-path source inventory with only 256 source hashes retained, and an inline source list truncated to 64 paths. Focused event analysis is restricted to `events/**/*.txt` and `common/on_actions/**/*.txt`, so the unresolved helper entries are scope-boundary findings, not proof that the scripted effects are absent. The graph is direct-entry evidence only.

## Event 006 adapter route and exact MCP limit

The current Event 021 adapter path is visible in source at `event021_parent_start_event6_front` (`common/scripted_effects/021_random_civil_war_parent_effects.txt:4353`), `independence_wave_prepare_event021_adapter_origin` (`common/scripted_effects/006_independence_wave_effects.txt:858`), and the Event 006-owned adapter registry (`common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:12`). This is a scripted-effect integration, not a call to the normal Event 006 public event, so the three public-event overview graphs cannot certify adapter isolation or package lifecycle.

A fresh `hoi4.event_inspect(mode=state_flow, selector={kind:event,eventId:chaosx.nr6.1}, expandHelpers=true, maxDepth=5, maxNodes=150, maxEdges=250, refresh=true)` call timed out after the service's 180-second limit and returned no artifact. The live schema has no separate `helper_expansion` mode, and the documented full-analysis retry therefore remains unavailable in practice for this chain. No repeated timeout was requested. No `event_compare` was run because this audit made no source change; the existing `EVENT_REVISION_NOT_CACHED` comparison blocker remains as previously recorded.

## Validation boundary

These current MCP results resolve the prior completion auditor's linked-root coverage omission and verify that the event-file inputs match the checked-out source. They do not certify helper lifecycle, the Event 006 adapter's 32-package provenance, same-war successor continuity, arbitration, scenario behavior, cleanup, performance, probability, UI consumers, or live gameplay. No source, status, or test-entry classification was changed by this audit.
