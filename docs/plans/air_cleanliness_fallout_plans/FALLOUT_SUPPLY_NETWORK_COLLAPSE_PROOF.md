# Fallout Supply Network Collapse Proof

## Status

World transition schema 12 retains the transactional province supply-network collapse for `supply_node` and `rail_way`. The selector grammar, building identities, aggregate variables, direct province query, migration bounds, and downstream receipt gates have static source support.

This is not runtime acceptance. Hearts of Iron IV was not launched. No exact vanilla or approved-mod precedent removes either network family with this route. Railway edge cleanup and immediate script visibility remain engine-sensitive blockers.

## Owned files

The implementation is owned by:

- `common/script_constants/fallout_world_end_constants.txt`
- `common/scripted_effects/fallout_world_end_effects.txt`
- `common/scripted_triggers/fallout_world_end_triggers.txt`

The world transition uses schema 12. The network receipt uses `fallout_supply_network_collapse_schema.version = 1` so its payload can be audited independently inside the transition.

## Assets and localisation

This transaction adds no player-facing key, icon, sprite, sound, or image reference. It changes the physical state rewrite and its hidden proof ledger only. No asset manifest or localisation file is required for this tranche.

## Engine reference basis

The installed official documentation establishes these surfaces:

- `documentation/effects_documentation.md` lines 6621 through 6628 defines `set_building_level` in state scope for state or province buildings.
- `documentation/effects_documentation.md` lines 5838 through 5871 defines `remove_building` and states that a state-scoped call does not recursively find province buildings.
- `documentation/triggers_documentation.md` lines 1621 through 1641 defines `any_province_building_level` with a province selector, building type, and level comparison.
- `documentation/triggers_documentation.md` lines 1830 through 1839 lists `supply_node` and `rail_way` as supported building identities for building-count queries.
- `common/buildings/00_buildings.txt` lines 98 through 123 classifies both `supply_node` and `rail_way` as provincial buildings.

The offline Effects reference lines 9883 through 9945 documents the compound `province = { all_provinces = yes ... }` selector for `set_building_level`. Vanilla `common/decisions/GER.txt` lines 13348 through 13356 uses the same reset shape with `level = 0`, `all_provinces = yes`, `limit_to_border = no`, and `level > 0` for bunkers.

Close network precedents exist for the selector grammar, but not for removal:

- Vanilla `common/scripted_effects/SOV_scripted_effects.txt` lines 8286 through 8294 selects `supply_node` through `all_provinces` under `add_building_construction`.
- Approved mod `1458561226/common/national_focus/SWK_RAJ_50s.txt` lines 204 through 213 selects `rail_way` through the same shape under `add_building_construction`.
- Vanilla has destructive `damage_building` precedents for both families, but damage does not meet the required complete physical-collapse contract.

An exhaustive source search found no active `set_building_level` or `remove_building` block targeting `supply_node` or `rail_way` across vanilla and approved mods `1521695605`, `2265420196`, and `1458561226`. The search covered 167 active `set_building_level` calls and 749 active `remove_building` calls.

## Why `remove_building` is not used

The documented `remove_building` province argument is a scalar province id. Its state form explicitly does not recurse into provincial buildings. A compound province selector under that effect would be unsupported.

The implementation therefore uses `set_building_level` with the documented all-provinces selector. It does not introduce a hardcoded Fallout province registry, one-state proxy, state modifier substitute, or variable-only claim of physical loss.

## State transaction

`fallout_apply_supply_network_collapse` runs only from a current grading row.

On its first pass it commits one immutable intent row with:

- transition and network schema generations
- frozen snapshot aggregates for nodes and railways
- immediate live aggregates for both families
- grade-owned request values
- cleared result and reconciliation fields

Grades below dead city request zero for both families. They settle as explicit no-op rows and never call the engine mutation.

Dead-city and higher grades request the complete immediate live aggregate. Each family then follows this idempotent contract:

1. If the aggregate is zero and no selected province has a positive level, mark that family settled without an engine call.
2. Otherwise call `set_building_level` with level zero and the all-provinces selector.
3. Read the aggregate and direct province query again.
4. Mark the family settled only when both report zero.
5. If the effect chain was interrupted or the engine result is delayed, leave the family unsettled. A later coordinator pass may repeat only the same set-to-zero operation.

The row intent is not reinitialized during retry. A repeated set-to-zero call cannot remove an additional level below zero. This avoids relying on persistence atomicity between a pre-call issue flag and the engine command.

Both destructive calls include an explicit grade check at dead city or above. A stale positive request on a lower-grade row cannot reach either mutation.

## Receipt contract

`fallout_state_supply_node_surface_is_zero` and `fallout_state_rail_way_surface_is_zero` require both:

- `building_level@<family>` equals zero
- `any_province_building_level` finds no selected province whose level is above zero

After both families settle, reconciliation records after values and observed aggregate loss. The exact payload requires:

- matching transition and network generations
- snapshot copies equal to the frozen state values
- nonnegative baseline, request, after, and observed fields
- zero request and zero observed loss below dead city
- complete baseline request, zero after value, and exact observed loss at dead city or above
- an applied flag only when a destructive-grade row records a positive aggregate decrease

The current receipt adds the live zero checks for destructive grades. The durable receipt retains the authenticated result after normal later construction changes. A lower-grade no-op row does not become invalid merely because its network changes after the row settled.

## World commit and downstream gates

The physical phase writes the global network schema and generation only after every state row is current. It marks physical collapse complete and advances only after `fallout_physical_collapse_rows_are_durable` sees that global receipt and every durable state row.

The durable network receipt is also required by:

- successor state inventory rows
- the general successor allocation begin gate
- the named state rewrite postcondition
- the physical-collapse component used by map return

No allocation or map return can treat a semantic supply modifier as the physical network receipt.

## Schema-10 migration

Migration never fabricates a network receipt.

| Schema-10 state | Policy |
| --- | --- |
| Snapshot phase before snapshot application or destruction | Rebuild the complete schema-12 snapshot epoch |
| Phase 2 before grading mutation | Promote to schema 12 and continue |
| Phase 3 or 4 before allocation | Require current grading and exact live-to-frozen network equality for every destructive-grade state, then continue to or execute physical collapse |
| Phase 5 or 6 before allocation | Require current grading and exact live-to-frozen network equality for every destructive-grade state, then rewind to physical collapse and invalidate derived rows |
| Phase 7 or 8 | Fail closed |
| Allocation already initialized | Fail closed |
| Unrelated transition error | Preserve the error and fail closed |
| Completed transition | Preserve completion, do not replay destruction, and mark current-schema and supply-network receipts absent |

The later-phase preflight prevents schema migration from deleting supply construction that cannot be attributed to the frozen transition snapshot. Rewinding clears physical, government, and derived conflict completion state, but it does not rebuild or reinterpret the accepted snapshot.

## Static validation boundary

Static inspection can prove that:

- only the two Fallout-owned all-provinces reset calls target the network families
- each destructive call is grade-gated
- each family remains unsettled until aggregate and direct province zero are visible
- retry repeats only an idempotent set-to-zero operation
- the global receipt is written after all current rows
- physical completion and advancement require the durable global receipt
- schema-10 migration cannot enter the destructive extension after allocation

Static inspection cannot prove that:

- `set_building_level` accepts both network families in this exact mutation form at runtime
- every cross-state railway edge disappears when the selected province levels reach zero
- aggregate and province queries expose the result immediately in the same effect chain
- a save interruption preserves the intended retry state
- multiplayer clients observe the same mutation and receipt timing

If any runtime surface fails, the row remains unsettled, the global receipt remains absent, and the blackout cannot advance. No weaker supply modifier or state-level proxy is accepted as completion.
