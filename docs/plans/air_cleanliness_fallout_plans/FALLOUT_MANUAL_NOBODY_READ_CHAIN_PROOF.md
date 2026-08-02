# Fallout The Manual Nobody Read Chain Proof

## Static evidence

- Candidate row: `common/scripted_effects/fallout_consolidated_effects.txt`, candidate `345`.
- Trigger contract: `common/scripted_triggers/fallout_consolidated_triggers.txt`.
- Transaction effects: `common/scripted_effects/fallout_consolidated_effects.txt`.
- Event ids `345` through `351`: `events/fallout_world_end_events.txt`.
- Constants: `fallout_event_345_*` groups in the dedicated constants file plus shared event identity, cooldown, and candidate reservation groups.
- Event Log history `9128`: shared type and name-detail mappings plus the dedicated fifteen-payload mapping.
- Report asset: generated source, processed preview, DDS, manifest, and GFX handoff under `docs/assets/air_cleanliness_fallout/fallout_manual_nobody_read/`.

Static review checks the touched script braces, unsupported comparison operators, non-ASCII script tokens, duplicate event ids, localisation BOM, duplicate localisation keys, and sprite path.
The chain has four visible human branches, one hidden AI lane, delayed result, delayed callback, state-level consequences, Deaths routing, Event Log payloads, and idempotent cleanup.

## Engine-sensitive evidence

The bounded read-only `hoi4.event_inspect` lint request for `chaosx.fallout.345` used helper expansion disabled, depth one, twenty nodes, and forty edges.
It returned `EVENT_ISSUE_LIMIT` with 23,025 issues against a fixed ceiling of 20,000, no artifact, and no files scanned in the returned bounded result.
Exact engine-side reachability of this chain's target scope, delayed receipts, host authority, save recovery, multiplayer delivery, and Event Log opening therefore remains unproven.
No HOI4 runtime was launched for this tranche.

## Release-floor disposition

The Manual Nobody Read is a dormant reviewed pilot and contributes zero countable blocks to the 660-block release floor until scheduler activation and engine-sensitive delivery surfaces are proven.
