# Event 006 event MCP trace refresh — 2026-09-12

Status: bounded read-only Event 006 structural evidence. This handoff records fresh event-inspection and lint receipts after the current source repairs. It makes no gameplay, asset, localization, package-admission, helper, or lifecycle edits. No live game, save/load, or runtime completion claim is made.

## Fresh trace

The mandatory read-only call used `hoi4.event_inspect` in `trace` mode for selector `chaosx.nr6.1`, downstream direction, `refresh = yes`, helper expansion requested, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

The service returned `EVENT_INSPECTED_PARTIAL` at graph revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d` with graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`. The global projection reported 9,741 events, 15,167 options, 1,159 entries, 38,369 edges, 30,451 state accesses, 8,737 unresolved nodes, 7,768 terminals, 2,199 diagnostics, one aggregate blocking diagnostic, and zero skipped sources. The returned graph still reports `helpers = 0` even though helper expansion was requested, and validation remains false because the large-workspace helper and lifecycle projections are deferred.

Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2134cb2cc3ad113e2aaafa14c491e4f565f84177a8554d428b714aef2fe4dac0/4677e99016cbd2e832f3d3c3688535aa97e3b692b2e8999716402f68764340c0/event-trace-4bccb6ec7fe1.json`.

One Event 006 unresolved-helper row names `independence_wave_apply_rhi_incident_deltas` at `mod:events/006_independence_wave_support_events.txt:1327`. The current source defines that helper at `common/scripted_effects/006_independence_wave_rhineland_bavaria_saar_package_effects.txt:174` and the support event calls it at the expected incident branches. Because the MCP helper catalog is empty (`helpers = 0`) and the global projection defers helper/lifecycle expansion, this row is not evidence of a missing source helper and no source patch is justified.

The absent-carrier materialisation shape was also checked against the installed effects documentation and the offline scope reference. `create_dynamic_country` accepts any scope and `copy_tag` copies from the current scope; inside the former-host event-target block, `copy_tag = THIS` intentionally copies the former host as the template while `original_tag` selects the candidate's dynamic origin. The same candidate-scope/host-scope shape is present in the installed Fallout fracture precedent. No `THIS`/`PREV` rewrite is justified from source documentation alone.

## Fresh narrow lint

A second read-only `hoi4.event_inspect` call used `lint` mode for selector `chaosx.nr6.11`, both directions, `expandHelpers = true`, `refresh = yes`, and bounded limits. It returned `EVENT_INSPECTED_PARTIAL` at the same revision and hash, again with `helpers = 0`, 8,737 unresolved nodes, 2,199 diagnostics, one aggregate blocking diagnostic, and validation false. The artifact explicitly reports that focused helper/lifecycle analysis was deferred for the indexed workspace.

Lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0d976807e9bd226e73fbebdb1e6d998a264bc3248058a51ecde4c5bf15daa9a/47eae3af4ac8d8ec4479c0fce8095b91fde75ad7a07032d0f8a6ee25d0ca233f/event-lint-4bccb6ec7fe1.json`.

Additional unresolved names in the bounded lint output are likewise workspace-catalog diagnostics, not accepted source defects, until the MCP helper projection is available. The parent must not delete or rename valid Event 006 helpers based on this partial graph.

## Disposition

The current source-linked Event 006 root, support-event, signature, and helper definitions remain unchanged by this tranche. The exact no-pre-event contract, exact wave ladder, fail-closed allocator, and current package-admission boundary remain authoritative. The event MCP route is a structural and lifecycle-evidence blocker; it does not authorize speculative gameplay rewrites. A future evidence tranche needs a helper-capable event graph or an approved equivalent engine receipt before claiming semantic event-chain closure.
