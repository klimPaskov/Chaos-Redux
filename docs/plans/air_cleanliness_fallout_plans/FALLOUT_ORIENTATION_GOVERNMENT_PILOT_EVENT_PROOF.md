# Fallout Orientation Government Authority Pilot Proof

Review date: 2026-07-18.

Status: implemented as a dormant four-block pilot. The blocks are not release-countable and have no caller.

## Event transaction

Events `chaosx.fallout.74` and `chaosx.fallout.76` are the human root and delayed result. Events `chaosx.fallout.75` and `chaosx.fallout.77` are the hidden-AI root and delayed result. Human and AI routes use the same branch affordability, payment, score, result effects, durable memory, and cleanup transaction.

The three branches are consolidation, represented division of authority, and rival integration. Each pays the accepted Food, Fuel, Shelter capacity, or Scrap costs. Each resolves after exactly 3 days through `fallout_orientation_delay.government_archetype_days`. Nine manually written descriptions cover every branch and outcome combination.

## Exact twelve-row mapper

`fallout_orientation_prepare_government_mapping` is idempotent. It clears stale derived values, requires a current successor-assignment country row, writes current-generation identity fields, selects one exact row, commits its mapped flag last, and revalidates the complete payload. Unsupported memory, identity mismatch, stale allocation, invalid payload, and missing approval paths write typed diagnostics.

| Country memory | Region and archetype | Consolidation benefit | AI preference |
| --- | --- | --- | --- |
| Federal Continuity Zone | North America, Continuity government | Recognition 5 | Division |
| Alpine Redoubt | Europe, Bunker authority | Capital Recovery 4 | Division |
| Rhine Dead Cities | Europe, Scavenger syndicate | Capital Reclamation 5 | Consolidation |
| Don Steppe Hetmanates | Eurasian Interior, Warlord command | Capital Supply Access 4 | Rival integration |
| Mekong Greenhouse Compact | East Asia, Food compact | Capital Recovery 5 | Division |
| Bengal Delta Raft Republic | South Asia, Maritime remnant | Capital Supply Access 5 | Division |
| Levant Quarantine Cities | Middle East and North Africa, Quarantine state | Capital Recovery 5 | Division |
| Congo Green Basin | Sub-Saharan Africa, Mutant polity | Cohesion 5 | Division |
| Sahel Caravan Wards | Sub-Saharan Africa, Nomad convoy | Capital Adaptation 5 | Division |
| Ethiopian Highland Refuge | Sub-Saharan Africa, Religious refuge | Cohesion 5 | Division |
| Atacama Observatory State | Latin America and Caribbean, Technate | Capital Supply Access 5 | Division |
| Antarctic Listening Government | Oceania and Remote Islands, Machine protocol | Capital Adaptation 4 | Division |

The row id is also its effect token. The transaction gate compares the frozen country memory, region, archetype, effect kind, value, days, and token with the live current-generation mapping before a root choice or result can enter. The deterministic AI scorer adds the shared cell-preference bonus only to the exact preferred branch and still rejects unaffordable choices.

## Results and text

Successful consolidation receives the accepted Recognition and Cohesion gains, the 180-day consolidated-authority modifier, and the exact row benefit. Partial consolidation receives smaller gains and contested authority. Failed consolidation loses Recognition and Cohesion and receives the legitimacy-crisis modifier.

Division success records the institutional compact. Partial division records a disputed compact. Failure records an unresolved institutional dispute. Rival success records integration, partial success records autonomy, and failure records rupture. All paths use the accepted numerical table and existing durable flags.

The human root combines one archetype paragraph with one exact country-memory opening. Each of the three option labels names the local institution or rival. The visible result adds one exact country-memory return paragraph. The Congo text treats the altered river society as fictional high-chaos civic content and does not present it as ordinary radiation science.

## Deliberate non-activation

The mapper cannot approve itself. No setter exists for `fallout_orientation_government_row_surface_status`, the regional row approval, the archetype row approval, or the memory row approval. No call to `fallout_orientation_begin_government_archetype` exists outside its helper definition. Neither scheduler activation flag has a setter.

The other 96 region and archetype cells have no government runtime row. No generic row is substituted. Events `74` through `77` have no event-log or event-detail rows and remain uncounted. Defined Ash-week orientation blocks are now 15 of 23. The countable Fallout living-world total remains 0 of 660.

## Asset and engine-sensitive evidence

Human events `74` and `76` use `GFX_report_event_fallout_government_archetype`. The sprite resolves through `interface/fallout_world_end.gfx` to the dedicated Fallout DDS recorded in the Ash-week orientation asset manifest.

Hearts of Iron IV was not run, as requested. Source inspection proves the event ids, exact 3-day constant, tokenized dispatcher route, mapping, and sprite path. A refreshed read-only `hoi4.event_inspect` lint request targeted only `chaosx.fallout.74`, disabled helper expansion, and bounded traversal to 40 nodes, 80 edges, and depth 2. The service returned `EVENT_HELPER_PROJECTION_LIMIT` at its fixed 200000-helper ceiling before scanning files or producing an artifact or diagnostic. No MCP lint pass is claimed. Runtime popup presentation, save interruption, and multiplayer behavior are not claimed.

## Remaining blockers

- no government row approval setter
- no regional, archetype, or memory approval setters
- no government rows for the other 96 cells
- no orientation caller
- no event-log or event-detail integration
- no complete Ash-week orientation audit
- successor allocation and player continuation remain unproven
- the ordinary Fallout scheduler remains inactive
