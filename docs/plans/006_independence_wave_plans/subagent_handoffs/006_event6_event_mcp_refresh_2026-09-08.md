# Event 006 root Event MCP refresh — 2026-09-08

## Scope

This is a fresh read-only structural refresh for the Event 006 root `chaosx.nr6.1` after the current source and visual/localisation audits. The refresh made no gameplay, asset, UI, admission, or runtime edits.

## Event inspection

The narrow `hoi4.event_inspect` lint used selector `{kind: event, eventId: chaosx.nr6.1}`, downstream direction, `maxDepth = 1`, `maxNodes = 40`, `maxEdges = 80`, helper expansion disabled, `refresh = yes`, and workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `EVENT_INSPECTED_PARTIAL` with status `ok`, revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6eeb66681b9568658ee015638fba6e28360858104df2e5b19e03112a74699b51/4433437331be222dba4df3da25608c7855a59cab3a3e326e9abcee7ecf0d4d44/event-lint-4bccb6ec7fe1.json`.

The workspace projection reports 9,741 events, 15,167 options, 1,159 entries, 30,451 state accesses, 38,369 edges, 2,199 diagnostics, and one global blocking diagnostic. The service validation is `passed = false` only because helper-expanded and lifecycle projections are deferred for this large workspace; no selector-specific source blocker or skipped source was returned. This is partial structural evidence, not a runtime or semantic-helper receipt.

## Event render

The matching read-only `hoi4.event_render` overview used the same event selector, downstream direction, depth and node bounds, helper expansion disabled, `includeHtml = no`, `refresh = yes`, and workspace. It returned `EVENT_RENDERED_PARTIAL` at the same revision and graph hash, with layout hash `118888ec7d6771854b8f62f596ed4f25c9bbdcb117a9e47a91f177e7fec7a571`. The manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7061ca853a1bc761f1b6ff99c6d16ddd29def90d88bdbef7fa3f268f4b5f45b7/8184738e0ba48c893ed74aec3aa1060e7b33960fc3801d8d43b93fe07593d3f0/event-overview-4bccb6ec7fe1-manifest.json`; JSON, SVG, and PNG artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a42cd125593143fbef54a4925fe2580991103586ba01a7945280a55800838d14/bfd3fa80ef414b41fa3095794aad55d8c2a3b7baac121bea993634c761b4cd06/event-overview-4bccb6ec7fe1.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6ed4dafc2a6968890d0c27b24ce022df8370f43b36c21bffe0b4da37eadd258/93cc7e63317a97235629f912edf18440d807cdf87c885918ec915cbe851feb33/event-overview-4bccb6ec7fe1.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39237c8a7d38a5e7a82df5e7d951ae0da10e2c8647f3f7057d928af1455522e4/793b4a9e28238a3695e1b4b0ebd8a22ad4bdab14b907d26ee27312f512820587/event-overview-4bccb6ec7fe1.png`.

The bounded overview selected three nodes and omitted 42,569 nodes; it retains the same one global blocking diagnostic and deferred helper/lifecycle limitation. It does not prove release materialisation, option semantics, save/load persistence, or live gameplay.

## Related static boundary

The current focused source validators remain passing for the exact 3/4/5/7/10 allocator ladder and World Collapse 10, 32 scenario cells plus eight edge cases, five GUI tabs and animation-frame contracts, the 191-carrier country API, 102 strict flag families, and the ARM/GEO/AZR FORM-16 contract. The whole Event 006 disposition remains **HOLD / PARTIAL** because package attestation, typed probability comparison, unresolved portraits/provenance, SE23 audio/runtime reachability, and live engine evidence remain open. No generic admission or other fallback was introduced.
