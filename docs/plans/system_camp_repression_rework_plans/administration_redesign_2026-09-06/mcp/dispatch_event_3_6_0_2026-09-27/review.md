# Bounded country timer event inspection

Status: current-source structural and timing evidence from installed HOI4 MCP 3.6.0; live scheduling and exactly-once monthly execution remain unproved.
The direct server reported version 3.6.0 and exposed the event, job and reference routes recorded in `tool-list.json`; this call used ordinary `trace` and `timing` routes, not helper-expansion or a native task.
`manifest.json` verifies 14 saved inputs, results and original artifacts against their returned hashes, and confirms the inspected event source remained SHA-256 `a62500735c71202f80231c1d642b74ec30d61e03f0dc8a6b602da831230a3bb8`.

The exact selector was `camp_administration_country.2`, with depth 3 and bounded node/edge counts.
`hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` at graph revision `f3299e7496fd64e6fb32481dae865b9505b7c6fc511867cd853eeb77504d45bb`, graph hash `3fe2e42293ed8631344613ef8c54714e8152f9bbbd10d6679153aaac94fffe12`, and zero selected-route blocking diagnostics.
Its focused trace contains a delayed self-call plus three unresolved helper-call edges; helper expansion and the exact recipient effect remain outside this graph result.
`hoi4.event_render` returned `EVENT_RENDERED_PARTIAL`, one selected timer node, 42,916 omitted nodes and [the archived timing PNG](event-timing-f3299e7496fd.png), which was visually inspected.
The self-edge retains `days = constant:camp_admin_dispatch.period_days` but reports `mode = unknown` and `Event timing could not be resolved statically.`
After verifying the server's optional task support, client task capability and live `helper_expansion` schema, a bounded page request using the recipient helper-call edge as `rootIds` returned `HELPER_ROOT_UNKNOWN` with no artifact. The focused graph classifies the three helper calls as unresolved and reports zero helper nodes, so that edge is not an accepted helper-expansion root; [the exact request and error](helper-attempt.json) are retained. A workspace-wide expansion without a confirmed root would exceed this scoped evidence request and was not substituted.
This is an inspector coverage limit; the source constant and installed effect syntax support the 28-day delay without proving the engine schedules it.

The direct `hoi4.reference_context` and exact `reference_search` resolved both installed game documentation and the offline wiki snapshot, and `reference_read` fetched the relevant sections with path, line span and revision.
Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` lines 2943–2967, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, states that `country_event` is country-scoped and that `days` adds a delay.
Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` lines 117–150 and 192–229, revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`, distinguishes triggered-only events from automatic checks and documents delayed `country_event` effects.
The three saved `reference_read` wrappers retain the exact returned text, path and revision; no web wiki lookup was used.

The source-owned [dispatch contract](../../../../../camp_administration_dispatch.md) and source scenarios remain the proof of the intended registry, timer flag and calendar-month guard.
Neither source arithmetic nor this one-node MCP view proves that a running game fires one timer per registered country, avoids a duplicate payment when the Chaos Meter dispatcher also runs, or persists the month key through a save.
