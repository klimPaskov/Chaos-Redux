# IW-048 UDM targeted map recheck — 2026-09-20

Disposition: implemented evidence-only receipt; the state-399 host-retention gate remains unresolved and no gameplay, map, reservation, central-admission, probability, identity, or asset source was changed.

## Scope

This parent-owned recheck tests whether the installed state-399 selection can establish the IW-048 compact anchor and former-host retention contract after the earlier allocation-request collision and globally truncated map diagnostics.

The accepted package remains vanilla `UDM`, state `399` / Izhevsk, reservation group `RG-399`, and the package-local `industrial_security` / `industrial_breakaway` crosswalk recorded by `006_iw048_udm_force_crosswalk_resolution_2026-09-20.md`.

## MCP receipt

The read-only `hoi4.map_inspect` request used `stateIds: [399]`, `includeOverview: false`, `query: "state 399 owner controller capital host retention infrastructure buildings"`, and `queryLimit: 40` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The call completed with `MAP_INSPECTED`, revision `03e62783a61e6d34fe3214a5fb7c6511dccad8c0d889098f6069a3a89a64a508`, `inspectedStateCount: 1`, and `queryMatchCount: 0`.

The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/49ee7723344d3c4c25c7cf4d1a44c77d9c9ca53a7edde63bd278fa1b2b16c738/02145e976bcd08033c6b9fb976270c958acf68cba83bd84c68e73cc1b6a56166/map-inspect.03e62783a61e6d34.json`, with reported SHA-256 `49ee7723344d3c4c25c7cf4d1a44c77d9c9ca53a7edde63bd278fa1b2b16c738`.

The result still carries global `MAP_DIAGNOSTICS_TRUNCATED` with 2,654 omitted errors, including `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`; the `map-positions-locators` validation remains failed even though the state, region, and network validators report success.

## Disposition

Selecting one installed state is useful anchor evidence, but `queryMatchCount: 0` and the failed, globally truncated locator validation do not prove owner, controller, capital, former-host retention, protected-state semantics, or reservation compatibility for IW-048.

No map rewrite, state allocation, host-retention predicate, reservation change, central adapter entry, attestation, preflight branch, scenario entry, Join entry, or AI-weight patch is justified by this receipt.

IW-048 remains package-local and fail-closed pending a clean state-399/former-host receipt, accepted identity and portrait-rights evidence, typed probability fixtures with same-scenario comparison, whole-event MCP evidence, and central wiring review.

## Follow-up owner

The next map owner must produce a clean scoped state-399 and former-host inspection or document the exact installed-map defect that prevents it before any package admission change is proposed.
