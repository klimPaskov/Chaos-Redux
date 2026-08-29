# IW-048 UDM source-contract audit

Date: 2026-08-24

## Disposition

This is a read-only package-local audit. No gameplay source, map source, identity asset, central admission surface, probability weight, or unrelated file was changed. IW-048 (`UDM`) remains fail-closed and no safe source patch was identified.

## Coverage checklist

- Identity and tag: `UDM`, vanilla `UDM_boris`, state `399` / Izhevsk, and the installed `RG-399` binding were cross-checked against `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:49`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:49`, and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:49`.
- Package-local source: `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt`, `common/scripted_effects/006_independence_wave_udm_package_effects.txt`, `common/decisions/006_independence_wave_udm_decisions.txt`, `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, `common/national_focus/006_independence_wave_focus.txt`, localisation, ideas, and the existing UDM handoffs were inspected.
- Map and state: the authoritative binding remains state `399` with current owner `SOV`; no map write or authority change is permitted in this tranche.
- Force contract: p48 is `industrial_security`, military tradition is `54`, and the accepted IW-048 pathways include factory or railway guards plus the existing four local pathways.
- Focus and event: the package uses five guarded callbacks in `independence_wave_focus_tree` and the Event 006 root surface `chaosx.nr6.350`; prior package receipts remain the current engine evidence.
- Decision and AI: the ten UDM project IDs and four package AI strategy IDs are present; no probability target was changed.
- Technology: no package-specific technology or doctrine dependency is declared. The installed package exposes no Technology Tree Viewer, so that route remains unresolved.
- Assets and rights: no portrait, flag, character, `.gfx`, DDS, or manifest change is safe without the parent-owned source and rights receipts.

## Concrete source-contract defect and blocker

The IW-048 force mapping row identifies `industrial_security` as the force profile, but the package-local setup gate uses the separate shared package-archetype token `industrial_breakaway`:

- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:49` records `"IW-048"` with force profile `"industrial_security"` and tradition `"54"`.
- `common/script_constants/006_independence_wave_constants_registry.txt:1873-1888` defines `independence_wave_force_profile.industrial_security = 2`.
- `common/script_constants/006_independence_wave_constants_registry.txt:6809-6822` defines `independence_wave_package_archetype.industrial_breakaway = 2` and has no `industrial_security` key in that typed archetype block.
- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:72-88` and `:136-172` intentionally require `industrial_breakaway` for the package archetype while requiring the exact `industrial_security` force profile and p48 tradition.

This is an evidence-backed contract discrepancy, but it is not safely fixable inside UDM ownership. Replacing the local gate with `industrial_security` would reference an undefined package-archetype token. Adding that token or changing the generic archetype mapping would modify the shared force contract and could change other package initialization behavior. Selecting another existing archetype would invent a source mapping. The prior UDM implementation and package-manifest handoffs explicitly record this as an admission-review blocker, so no gameplay patch was applied.

Next evidence needed is an owner decision that either registers a distinct shared `industrial_security` package-archetype token and updates its generic consumers, or explicitly accepts `industrial_breakaway` as UDM's package-archetype mapping while retaining p48 `industrial_security` as the force profile. That decision must precede any source edit.

## Repaired local contract still present

The bounded static check returned the following results:

```text
force_profile_industrial_security=True
package_archetype_industrial_breakaway=True
p48_mapping_row=True
udm_setup_profile=True
udm_setup_tradition=True
factory_rail_required=True
terrain_rejected=True
generation_guard=True
popularity_restore=True
package_archetype_keys=schema,any_key,data,urban_administrative,industrial_breakaway,agrarian_regional,port_or_island,mountain_or_frontier,river_or_corridor,nomadic_or_dispersed
contains_industrial_security=False
contains_industrial_breakaway=True
```

The earlier package-local repairs remain intact: `common/scripted_effects/006_independence_wave_udm_package_effects.txt:307` loads factory/rail guards, `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:178` requires that pathway and `:182` rejects terrain units, setup snapshots the generation at `:278`, cleanup checks equality and current-generation force ownership at `:325-327`, clears the snapshot at `:349`, and restores vanilla popularity at `:342`.

## MCP and validation limits

The current read-only MCP refresh was attempted for map state `399`, Event `chaosx.nr6.350`, and `independence_wave_focus_tree`. The first request was rejected with `WORKSPACE_NOT_REGISTERED` after an unregistered custom workspace ID; the bounded default-workspace retry was interrupted on the parent instruction to finish this turn. No new MCP artifact is claimed here. The prior receipts recorded in `006_iw048_udm_current_repair_audit_2026_08_15.md` remain the available map, event, and focus evidence.

No probability compare was run because no AI weight, decision score, or probability surface was changed and the mandatory `chaosx_ai_probability_auditor` route is not exposed in this environment. No live game was launched.

## Boundary and remaining blockers

The `32` content-attestation / `29` compatible-group / `40` runtime-adapter / `161` unattested-selectable boundary is unchanged. Central adapter, attestation, preflight, scenario, and deterministic Join surfaces remain intentionally untouched. Identity/portrait/flag rights, host-remnant and map admission, the provisional democratic setup/elections design review, the shared archetype decision above, and usable probability scenarios remain parent-owned blockers.

## Changed files

Only this read-only handoff was added. No gameplay identifiers, state IDs, leaders, parties, focus IDs, formable IDs, map bindings, weights, or central registry entries changed.
