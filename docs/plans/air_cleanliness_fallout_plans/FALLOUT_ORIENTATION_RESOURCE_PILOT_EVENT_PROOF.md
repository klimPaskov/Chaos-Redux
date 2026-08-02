# Fallout Orientation Immediate Resource Pilot Proof

Review date: 2026-07-18.

Status: implemented as a dormant four-block pilot. The blocks are not release-countable and have no caller.

## Implemented event blocks

| Event | Visibility | Role | Result |
| --- | --- | --- | --- |
| `chaosx.fallout.70` | Human visible | Immediate resource root | Authenticated choice among public rationing, emergency requisition, and the exact tailored capital response |
| `chaosx.fallout.71` | Hidden AI | Immediate resource root | Runs the same affordability, cost, scoring, and delayed-result transaction through deterministic AI selection |
| `chaosx.fallout.72` | Human visible | Delayed result | Resolves the selected branch, preserves the exact result receipt, and presents one of nine branch and outcome descriptions |
| `chaosx.fallout.73` | Hidden AI | Delayed result | Resolves the same transaction without exposing a player event window |

The dispatcher owns the delay. `fallout_orientation_delay.immediate_resource_crisis_days` is exactly 4. The result due day is the choice day plus that constant, and the dispatcher issues only the authenticated event token for the current transaction mode and stage.

## Exact twelve-row registry

The idempotent `fallout_orientation_prepare_resource_mapping` effect accepts only the following complete country-memory, region, and archetype identities.

| Country memory | Region | Archetype | Supporting resource | AI preferred branch |
| --- | --- | --- | --- | --- |
| Federal Continuity Zone | North America | Continuity government | Fuel | Public ration ledger |
| Alpine Redoubt | Europe | Bunker authority | Power | Tailored capital response |
| Rhine Dead Cities | Europe | Scavenger syndicate | Power | Tailored capital response |
| Don Steppe Hetmanates | Eurasian Interior | Warlord command | Fuel | Emergency requisition |
| Mekong Greenhouse Compact | East Asia | Food compact | Fuel | Tailored capital response |
| Bengal Delta Raft Republic | South Asia | Maritime remnant | Fuel | Tailored capital response |
| Levant Quarantine Cities | Middle East and North Africa | Quarantine state | Power | Public ration ledger |
| Congo Green Basin | Sub-Saharan Africa | Mutant polity | Fuel | Tailored capital response |
| Sahel Caravan Wards | Sub-Saharan Africa | Nomad convoy | Fuel | Tailored capital response |
| Ethiopian Highland Refuge | Sub-Saharan Africa | Religious refuge | Fuel | Public ration ledger |
| Atacama Observatory State | Latin America and Caribbean | Technate | Power | Tailored capital response |
| Antarctic Listening Government | Oceania and Remote Islands | Machine protocol | Power | Public ration ledger |

The mapper clears its derived row before rebuilding, binds every field to the live transition generation, and commits its country flag only after the exact row revalidates. Unsupported memory, identity mismatch, stale allocation, invalid payload, and missing-package paths write typed diagnostics. No tag name is used as identity evidence.

The deterministic AI scorer adds the cell-preference bonus only when the resource mapping is current and the tested branch equals the exact row preference. It still rejects unaffordable branches and uses the same selected-branch transaction as a human choice. AI does not receive a different cost, effect, or result table.

## Capital-asset evidence boundary

The identity mapper selects Fuel or Power. It does not claim that the supporting asset exists. `fallout_orientation_resource_package_receipt_is_current` separately requires:

- a resource-package installed flag
- current schema, transition generation, country memory, supporting resource, and state target fields
- the exact assigned capital as the package state
- current ownership and control
- current survival identity, supply access, Air Winter snapshot, successor inventory, and assigned-capital receipts on that state

No effect sets `fallout_orientation_resource_package_installed` or its receipt fields. The tailored choice therefore cannot become reachable from this tranche. The other 96 cells of the reviewed region and archetype matrix also have no resource runtime row. No generic response is substituted.

## Transaction and result integrity

The begin envelope still requires the regional, archetype, and memory approval surfaces, the current successor assignment, the durable survival ledger, the exact assigned capital, a valid resource package, and at least one affordable branch. All three choices recheck affordability at the visible root. A package cannot make an unaffordable tailored branch selectable.

The result transaction initializes current-result Deaths and building damage to zero before applying an outcome. Requisition failure records the exact applied Deaths value through the existing Deaths route. Tailored failure damages one infrastructure level only when the assigned capital still has a surviving level, and it records whether damage was issued. The result then preserves the crisis resource, crisis value, tailored support resource, applied Deaths, and applied building damage in durable last-result fields before transient cleanup.

The visible result has nine manually written descriptions for the three branches and three outcomes. Country-memory opening and result paragraphs are exact for all twelve rows. The mutant-polity row is fictional altered-society content and is not presented as ordinary radiation science.

## Asset binding

Human events `70` and `72` use `GFX_report_event_fallout_resource_crisis`. The sprite resolves to `gfx/event_pictures/fallout/report_event_fallout_resource_crisis.dds` through `interface/fallout_consolidated.gfx`. The source, processed PNG, DDS hash, and conversion evidence remain in `docs/assets/fallout_world_end/ash_week_orientation/asset_manifest.json`.

## Dormancy and release count

This tranche adds no call to `fallout_orientation_begin_immediate_resource_crisis`. It adds no setter for the resource package receipt, any regional, archetype, or memory approval surface, `fallout_event_scheduler_activation_approved`, or `fallout_event_scheduler_active`.

Events `70` through `73` have no caller-owned event receipt. History `9110` supplies their component, branch, and outcome payloads through the shared Event Log and generic Event Details route, but runtime delivery remains unobserved. All 23 Ash-week orientation blocks are defined and remain uncounted, while countable Fallout living-world blocks remain 0 of 660.

## Engine-sensitive proof status

The event definitions, event tokens, exact four-day constant, tokenized dispatcher, and dedicated sprite path are source-verifiable. Hearts of Iron IV was not run, as requested. A refreshed read-only `hoi4.event_inspect` lint request targeted only `chaosx.fallout.70`, disabled helper expansion, and bounded traversal to 40 nodes, 80 edges, and depth 2. The service returned `EVENT_HELPER_PROJECTION_LIMIT` at its fixed 200000-helper ceiling before scanning files or producing an artifact or diagnostic. No MCP lint pass is claimed. Runtime event-window presentation, save interruption, and multiplayer behavior are not claimed by this proof.

## Remaining blockers

- no orientation caller
- no resource capital-asset receipt producer
- no setters for the regional, archetype, or memory approval surfaces
- no resource rows for the other 96 region and archetype cells
- no caller-owned event receipt or runtime Event Log and Event Details delivery proof
- no completion audit for the full Ash-week orientation sequence
- successor allocation and player continuation remain unproven
- the ordinary Fallout scheduler remains inactive
