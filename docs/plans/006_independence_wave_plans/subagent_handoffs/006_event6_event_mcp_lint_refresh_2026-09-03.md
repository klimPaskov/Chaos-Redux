# Event 006 root Event MCP refresh — 2026-09-03

## Scope

This is a read-only structural refresh for the Event 006 root `chaosx.nr6.1` after the visual and documentation reconciliation. No source files were changed by the refresh.

## Evidence

The narrow `hoi4.event_inspect` lint used selector `{kind: event, eventId: chaosx.nr6.1}`, downstream direction, helper expansion disabled, depth `1`, 64 nodes, 128 edges, and refresh enabled. It returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics, zero skipped sources, and graph revision `27c77545e9241b4398d074f7bae0aaedf8ebba6790c26141f6e3508bf4238175`. The authoritative lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da36c27d092ac784723b79d77591be5715bf935d2746f7d3e206c8635a2e6e98/558295e4262ce922d1d777b59c0d3f228467f58802b826972f300d87aef8cbe3/event-lint-27c77545e924.json`.

The matching `hoi4.event_render` overview used the same selector and bounded downstream projection and returned `EVENT_RENDERED_PARTIAL` with no blockers. The overview manifest, JSON, SVG, and PNG are linked from `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7641c895e981c5d9b70400fa9961651110fb18c8acdb35f636ec0d2ad9c7af25/aee2b1193d5b57334e33f472e046a29dc87500862f06ea4d45d4b3ad8f137288/event-overview-27c77545e924-manifest.json`; its layout hash is `118888ec7d6771854b8f62f596ed4f25c9bbdcb117a9e47a91f177e7fec7a571`.

## Interpretation

The selected root has direct structural evidence and no selector-specific blocking diagnostic. The service still marks validation partial because the large workspace defers helper-expanded and lifecycle projections, so this receipt does not establish semantic helper behavior, save/load behavior, or live gameplay. The no-pre-event contract remains source/static evidence from the allocator and decision-surface audits.

## Validation boundary

The Event 006 allocator remains 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008-ranked packages, 40 runtime adapters, 32 content-attested packages across 29 compatible groups, and 161 unattested selectable rows. No admission, allocation, AI weight, event, GUI, asset, or runtime file was edited by this refresh. The whole-event disposition remains HOLD / PARTIAL.

## Supplemental upstream-roots trace

A second read-only `hoi4.event_inspect` request used selector `{kind: event, eventId: chaosx.nr6.1}`, upstream direction, helper expansion disabled, depth `3`, 120 nodes, 240 edges, refresh enabled. It returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at graph revision `efbe0ca7016c4e2e981367846826869ed2579ba82e64a7e2438481b73d5354e1` and graph hash `15cc4b9cce944b4e1047b383092206c0345626119a1d071d771dd8376bd3edd9`. In the returned roots report, `chaosx.nr6.1` and the analogous `chaosx.nr5.1` are listed under `callerlessTriggeredEvents`, while `chaosx.nr6.2` is downstream rather than callerless. This is the expected projection for the generic settings path: `common/scripted_effects/chaosx_settings_effects.txt` builds `country_event = { id = chaosx.nr[EVENT_ID].1 }` inside a `meta_effect`, which the static event graph does not materialize as a direct event edge. The result therefore supports the existing dynamic dispatcher and does not justify adding an ad-hoc caller, on-action, country-creation fallback, or a live interpretation of the user-reported empty release. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/882fa890f73442efa5cc83e57f34da8211b1b81d103c2377c725af169359ccde/71ba17e7e6fd4c6505b1f6ca8600442b4d0f972ec52bd1e07c19c1b51aee59f7/event-roots-efbe0ca7016c.json`.

## Supplemental focused lint — 2026-09-03

A fresh read-only `hoi4.event_inspect` lint used the same root selector in both directions, helper expansion disabled, depth `3`, 120 nodes, 240 edges, and refresh enabled. It returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and zero skipped sources at graph revision `58c35aacdc8966b79587b053bda405f07611cf6f38ba5cbb117b2602ceac126a` and graph hash `f938b51abe6e355fceb52e7a7d40331a2777f8d4b6427935ecb306bc0cd5ac4e`. The linked lint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2489798f8811becca491279261b9ae882d273799c290651dcd9d4085d882450/d3bec6a0b11e9193d09ffb72d8523971544cd51776d374915fd69974b1e572ca/event-lint-58c35aacdc89.json`.

The service still marks validation partial because this large-workspace lint defers helper-expanded and lifecycle analysis; it is structural evidence only and does not establish live release, save/load behavior, or semantic helper execution. No source, event, admission, asset, or runtime wiring file changed.

A bounded `state_flow` retry for the same root selector (depth `2`, 64 nodes, 128 edges, helper expansion disabled, refresh enabled) returned `INTERNAL_ERROR` with no artifact. This is an MCP transport/analysis limitation, not evidence of a source defect or a live empty release.
