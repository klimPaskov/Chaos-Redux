# Fallout The Vault of Voices Chain Proof

## Static evidence

- Candidate row: `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`, candidate `359`.
- Trigger contract: `common/scripted_triggers/fallout_world_end_vault_of_voices_event_triggers.txt`.
- Transaction effects: `common/scripted_effects/fallout_world_end_vault_of_voices_event_effects.txt`.
- Event ids `359` through `365`: `events/fallout_world_end_events.txt`.
- Constants: `fallout_event_359_*` groups in the dedicated constants file plus shared event identity, cooldown, and candidate reservation groups.
- Event Log history `9130`: shared type and name-detail mappings plus the dedicated fifteen-payload mapping.
- Report asset: generated source, processed preview, DDS, manifest, and GFX handoff under `docs/assets/air_cleanliness_fallout/fallout_vault_of_voices/`.
- Workbook row: `FALLOUT-359` in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, with the generated CSV export refreshed by `.tools/export_event_catalog_csv.py`.

Static review checks the touched script braces, unsupported comparison operators, non-ASCII script tokens, duplicate event ids, localisation BOM, duplicate localisation keys, and sprite path.
The chain has four visible human branches, one hidden AI lane, delayed result, delayed callback, state-level consequences, Deaths routing, Event Log payloads, and idempotent cleanup.

## Engine-sensitive evidence

The bounded read-only `hoi4.event_inspect` lint request for `chaosx.fallout.359` used helper expansion disabled, depth one, twenty nodes, and forty edges.
The exact returned object was `status: error`, `code: EVENT_ISSUE_LIMIT`, `workspaceId: mod_chaos_redux_ea3b2d67c2c0`, `filesScanned: []`, `proposedFiles: []`, `changedFiles: []`, `diagnostics: []`, `artifacts: []`, `validation.passed: false`, and one blocker stating `Event-chain issue count exceeds the fixed result ceiling` with `count: 23077` and `maximum: 20000`.
Exact engine-side reachability of this chain's target scope, delayed receipts, host authority, save recovery, multiplayer delivery, and Event Log opening therefore remains unproven.
No HOI4 runtime was launched for this tranche.

## Release-floor disposition

The Vault of Voices is a dormant reviewed pilot and contributes zero countable blocks to the 660-block release floor until scheduler activation and engine-sensitive delivery surfaces are proven.
