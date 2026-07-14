# Event 006 Package Regions 06–08 Handoff

## Ownership and outcome

This tranche implements the accepted Event 006 independence-wave runtime package definitions for regions 06, 07, and 08. Work was intentionally limited to the six region-owned scripted trigger/effect files and this handoff. Shared allocator, constants, country-tag registration, localisation, assets, specifications, and spreadsheet surfaces were not edited.

The runtime slice contains 24 accepted bound packages. Every bound package has a planning trigger, metadata loader, reservation publisher, and exact accepted territory-role publication. The 22 automatically eligible packages also have an automatic-pool weight and a regional selector entry. The two route/scenario-restricted packages retain planning, loading, and reservation support without entering the automatic pool.

## Changed files

- `common/scripted_triggers/006_independence_wave_packages_region_06_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_06_effects.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_07_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_07_effects.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_08_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_08_effects.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_packages_regions_06_08_handoff.md`

## Package coverage

### Region 06

Implemented accepted bound packages:

- IW-058, IW-059, IW-060, IW-062, IW-064, IW-065, IW-066
- IW-067, IW-068, IW-069, IW-070, IW-071, IW-072

Omitted accepted unbound packages:

- IW-061
- IW-063

All 13 implemented packages are eligible for their specified automatic pool. The high-chaos gate is applied to IW-058, IW-059, IW-064, IW-068, and IW-069.

### Region 07

Implemented accepted bound packages:

- IW-073, IW-074, IW-076, IW-078, IW-081, IW-082

Omitted accepted unbound packages:

- IW-075
- IW-077
- IW-079
- IW-080

IW-073, IW-076, IW-078, IW-081, and IW-082 are in the automatic pool. IW-074 is formable/route-only, so it has planning, loading, and reservation support but deliberately has no automatic weight or selector entry.

### Region 08

Implemented accepted bound packages:

- IW-083, IW-085, IW-086, IW-089, IW-091

Omitted accepted unbound packages:

- IW-084
- IW-087
- IW-088
- IW-090
- IW-092

IW-083, IW-085, IW-086, and IW-089 are in the automatic pool. IW-091 is specific-community-only, so it has planning, loading, and reservation support but deliberately has no automatic weight or selector entry.

The 11 omitted rows have no accepted runtime binding. No fallback tag, state, reservation group, or territory shape was invented for them.

## Pool and metadata behavior

- 24 bound packages are available to explicit planning calls.
- 22 packages participate in regional automatic selection.
- 5 automatic packages are additionally gated by `is_independence_wave_high_chaos_pool_open`.
- IW-074 and IW-091 remain explicit-only packages and cannot leak into automatic selection.
- All 24 accepted bindings use `fixed_anchor_compact`; there are no `choose_one_ordered` rows in this tranche.
- Every reservation publisher passes the shared `independence_wave_wave_territory_level` and `independence_wave_wave_force_level` inputs to the shared territory publication effect.
- Package depth, disposition, registered-tag status, reservation group, region, tag, and state roles match the accepted binding, candidate, research-resolution, and reservation-group sources.

## Territory publication

The following multi-state bindings publish the first accepted state as coordinator and the remaining states according to their accepted roles:

- IW-073: coordinator 679; compact 856; extended 855.
- IW-074: coordinator 292; compact 857.
- IW-085: coordinator 450; compact 451 and 663.
- IW-086: coordinator 448; compact 661; extended 662.
- IW-089: coordinator 767; compact 887.

All other bound packages in regions 06–08 publish only their accepted coordinator state.

IW-067 and IW-068 both use state 354 while retaining their distinct accepted reservation groups, `rg_lazistan` and `rg_pontus`. The shared helper `is_independence_wave_region_06_state_354_mutex_open` prevents either package from being planned after the other and also requires state 354 to remain unreserved. Their ordinary package and anchor availability checks remain active, so this mutex supplements rather than replaces shared reservation protection.

## Manual archetype assignments

The accepted registries do not provide a direct runtime archetype token, so the following assignments were made from each candidate's opening, force profile, territory profile, signature, and package research notes:

- `mountain_or_frontier`: IW-058, IW-060, IW-064, IW-065, IW-066, IW-070, IW-071, IW-078, IW-083.
- `river_or_corridor`: IW-059.
- `industrial_breakaway`: IW-062, IW-072.
- `port_or_island`: IW-067, IW-068, IW-069, IW-073, IW-076, IW-081, IW-085, IW-086.
- `agrarian_regional`: IW-074, IW-089.
- `urban_administrative`: IW-082.
- `nomadic_or_dispersed`: IW-091.

Mountain/interior openings and mountain-infantry profiles were classified as frontier packages; the Mesopotamian river federation as a corridor package; Khuzestan and Azerbaijan's oil/industrial security profiles as industrial breakaways; coastal and port-led openings as port packages; Najd and Darfur's settled dynastic/regional structures as agrarian-regional; Palestine's mandate-administration profile as urban-administrative; and the Toubou dispersed desert polity as nomadic/dispersed.

## Validation evidence

- A row-by-row comparison parsed the implemented top-level package blocks and checked them against the accepted binding, candidate, research-resolution, state-role, and reservation-group sources: `assigned=35`, `bound=24`, `omitted=11`, `weighted=22`, `high_chaos=5`, `issues=0`.
- Binding-mode coverage was `fixed_anchor_compact=24`; no assigned bound row required ordered-choice behavior.
- Every referenced reservation group is defined in the Event 006 constants sources.
- Every referenced state ID resolves to an installed current-map state history file.
- A repository-wide top-level scripted trigger/effect symbol scan found 101 symbols owned by this tranche and zero duplicates.
- The region files contain no daily, weekly, monthly, or other whole-world iteration.
- Manual review confirmed the state-354 mutex, the five high-chaos gates, the two explicit-only packages, and all compact/extended state orderings.

## Integration risks and parent follow-up

### Accepted tag registration resolved

The parent integration registered the thirteen accepted new reserved tags used by these publishers after this bounded tranche:

- Region 06: CGX, CJX, CLX, COX, CPX, CQX.
- Region 07: CUX, CVX, CXX.
- Region 08: DGX, DHX, DKX, DMX.

Already registered tags used in this tranche are ASY, KUR, CIN, DAG, ARM, GEO, AZR, IMO, LEB, PAL, and RIF.

The package files retain the exact accepted tags; no fallback tag was substituted. Registration is no longer a blocker. Full researched country content, leaders, assets, and the package-content readiness flag remain separate completion gates.

### Shared allocator wiring remains parent-owned

The parent integration connected regions 06–08 to the aggregate preparation and two-stage weighted selection path. Explicit route, community, and scenario callers retain direct access to their package readiness and reservation publishers without entering the automatic pool.

## Simplifications, omissions, and blockers

No simplification or fallback was used inside the assigned runtime slice. All 24 accepted bound packages were implemented to their accepted bindings, while the 11 accepted unbound packages were intentionally omitted rather than assigned invented runtime data.

Completion of the wider Event 006 system still depends on full playable country-package content and final execution wiring. The tag-registration and shared automatic-allocator blockers described by the original bounded tranche are resolved. No localisation or visual asset was required or changed by these region-only runtime definitions.

## Skills used

- `chaos-redux-subagents` for ownership boundaries, handoff requirements, and parent/subagent routing.
- `chaos-redux-events` for Event 006 implementation structure and completion discipline.

No skill files were created or updated.
