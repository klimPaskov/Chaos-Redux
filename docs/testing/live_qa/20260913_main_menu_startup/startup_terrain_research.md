# Terrain predicate repair

Five Event 027 geography predicates applied the COUNTRY-only `has_terrain` trigger inside STATE-scoped `any_controlled_state` blocks.
The mountain terrain's installed ID is also singular `mountain`.
The researcher verified that no Chaos Redux state, province-definition, or default-map override exists and identified native `any_state_of` as the exact state membership route.
The parent subsequently generated the machine-readable sets and applied the repair directly after stopping that read-only researcher.

`common/script_constants/027_doctrine_research_terrain_states.txt` centralizes the states containing at least one forest, mountain, or plains province.
Its schema mirrors vanilla `common/script_constants/state_groups.txt` (`array = state`).
`common/scripted_triggers/027_doctrine_research_terrain_triggers.txt` uses native `any_state_of` with these arrays and `is_controlled_by = PREV`.
PREV is the calling country after the iterator enters a state, so nested country scopes retain the original current-country control check without assuming ROOT is the caller.
The two existing Event 027 effect files replace only the five failing geography predicates; score additions and all weight values remain unchanged.

References: offline `Triggers - Hearts of Iron 4 Wiki.md` and `Map modding - Hearts of Iron 4 Wiki.md`; installed `documentation/triggers_documentation.md` sections `has_terrain`, `any_state_of`, `any_controlled_state`, and `is_controlled_by`; installed `common/decisions/CHI_decisions.txt:3820`; installed `common/script_constants/state_groups.txt`.
The MCP read-only map inspection confirmed 1,081 states and 13,414 province definitions, valid state/region membership, and valid supply/railway/adjacency networks.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d73f11bcbfc11f8b50464e69f67ed341ba0c91101b7eb265f2d98b5494d28bee/4780c9c3f439869d914d6aa6d7a78671eb1e5bb00c26985ad9693c2bd8af50bd/map-inspect.56f1dfc28c19ab7e.json`.
That wider inspector also reports unrelated floating-harbor position errors; no map file was rewritten and no map-position completion is claimed.

The exact join covers 1,081 inherited state files, 13,414 province definitions, and 10,272 state province memberships with no duplicate membership or filename/internal-ID mismatch.
The resulting arrays contain 454 forest states, 459 mountain states, and 675 plains states.
The parent's independently generated province SHA-256 and state-file manifest SHA-256 match the researcher's reported values exactly.
`startup_terrain_state_sets.json` records all IDs and both source hashes.
`startup_terrain_repair_receipt.json` records the five replacements and byte hashes.
`baseline/terrain/` preserves both effect files before the parent repair.

These arrays are exact classifications of the current map, not adjustable balance values.
They must be regenerated if state membership or province terrain changes.
No terrain gate was deleted or broadened to a country ownership check.
Fresh main-menu logs provide loader acceptance; the probability handoff separately records weighted-tool coverage and its limitations.
