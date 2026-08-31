# Event 006 ACX current-map inspection handoff

Date: 2026-09-02 (Europe/Kyiv).

Owner: `/root`.

Scope: IW-003 Cornwall (`ACX`) current-map anchor verification only.

## Disposition

A read-only HOI4 map inspection does not identify a current state named Cornwall, and the previously considered state `123` does not resolve as a selected state record in the current map catalog. No map rewrite, state reassignment, ACX promotion, or package-admission change is justified by this evidence.

## MCP evidence

The bounded inspection used `hoi4_map_inspect` with `query = "Cornwall"`, `queryLimit = 50`, `includeOverview = false`, and workspace `mod_chaos_redux_ea3b2d67c2c0`. The server returned `MAP_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8cd3f14ab7c10608ef21c64107d4689cd991cd0c08fdb91a998e01e6f1643031/c9e44a028bd09f5c9653212b0d62e6f3bdb0f31c3815825411ecc53e8899ad0a/map-inspect.bfaf7becc0c8c796.json`.

The map revision and shared revision are `bfaf7becc0c8c796e4a90a965eb38ab8db5b7a4bde2e0f4219c810810172632f`. The catalog reports 13,414 province definitions, 1,081 states, 304 strategic regions, and 534 ports. The query returned `queryMatchCount = 0`, `coordinateMatchCount = 0`, and no inspected state, province, region, or allocation records. A companion inspection with `stateIds = [123]` and the same query also returned no Cornwall match and no resolved selected state record.

## Validation boundary

The map geometry, state-region membership, network adjacency, and province-definition checks passed. The overall map result remains partial because unrelated workspace-wide diagnostics fail the positions/locators check, including 1,332 `MAP_PORT_ADJACENT_SEA_INVALID` entries, 1,323 `MAP_BUILDING_POSITION_INVALID` entries, and a malformed localization line in `localisation/english/039_murder_mystery_l_english.yml:389`. These diagnostics are outside the ACX package scope and were not edited.

## Event 006 implications

The current evidence confirms the existing source-of-truth decision to keep IW-003 fail-closed until a legally and technically valid current-map state binding is established. The ACX shell, historical research, and package-local preparation cannot be promoted using state `123` or an invented Cornwall anchor. Central allocator admission, dormant-carrier release logic, Event 006 pre-event visibility, and other package files remain unchanged.

ACX still lacks a proven current-map anchor, rights-cleared portrait/flag identity package, central package attestation and Join receipt, and complete gameplay package evidence. A future owner may revisit ACX only after a concrete map binding is established and independently audited.

No simplification or fallback was introduced by this inspection.
