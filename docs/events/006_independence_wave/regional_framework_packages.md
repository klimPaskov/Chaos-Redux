# Event 006 regional framework packages

## Purpose

Most rows of the Event 006 candidate registry have a planner gate, a loader, a reservation group, an SCN-008 rank and a force mapping, but no package engine that can set the released country up. Without one, the finalizer rejects the row and the wave never releases it. The regional framework is one shared Level 1 package engine for those rows (agent decision D25). It gives a released country everything Part 5 lists for Level 1:

- the full common survival system (Statehood values, founding phase, host relation, League, incidents, milestones);
- its region's identity overlay, through the shared regional identity idea and focus transport flags;
- its package archetype and its regional ambition family;
- leadership: the vanilla roster of a registered tag, or the leader the game appoints for an institutional government;
- its mapped dynamic starting force;
- complete flag and localisation coverage, from the tag's existing assets.

Level 2 rows add their own layer on top: a starting problem, a decision family and two incidents.

## Admitted rows

- Levant and Arabia (D25): IW-073 Hejaz, IW-076 Hadhramaut, IW-078 Imamate of Oman, IW-081 Lebanon, IW-082 Palestine. See `levant_arabia_packages.md`.
- North Africa and Sahara (D26): IW-083 Rif, IW-086 Tripolitania. See `north_africa_packages.md`.

## How it works

1. The planner gate of an admitted row reads `is_independence_wave_runtime_automatic_package_iw_NNN_ready`, which proves the exact dormant tag and anchor and the runtime preflight.
2. The executor prepares the origin, then calls `independence_wave_dispatch_regional_framework_package_setup`. It acts only when `is_independence_wave_regional_framework_exact_carrier` lists the package id with the country's original tag.
3. `independence_wave_setup_regional_framework_package` checks `can_initialize_independence_wave_regional_framework_package` (the released country owns, controls and governs from its anchor, and the former host still holds its protected state). It then records the framework generation, assigns the full Event 006 focus tree, allows the four host routes, registers the ambition family and the League route, runs the row's identity block, clears and reloads the force mapping, and applies the dynamic starting force.
4. The identity block in `independence_wave_regional_framework_apply_identity` is the only per-row code. It records the identity basis, confirms the leadership, allows the government routes the row's research supports, registers its two power centres, and either marks the layer applied (Level 1) or calls the row's regional layer (Level 2).
5. `has_prepared_independence_wave_regional_framework_package_setup` checks every flag, variable and force receipt the setup writes. Final validation reads `is_independence_wave_regional_framework_runtime_ready`.
6. Cleanup runs in the generation reset and at origin end, but only for the generation that set the package up. It removes the Level 2 layer, restores a ruling party the row changed, and clears the framework receipts.

Decisions and incidents read `is_independence_wave_regional_framework_live`, whose setup receipt persists after the origin commit. None of the framework code reads ROOT for the released country, and none iterates countries or states.

## Custom X-tag carriers

A reserved X-ending tag has no historical cores, so `release` cannot create it. Each admitted X-tag row adds one `create_dynamic_country` branch to `independence_wave_release_one_frozen_country` and one entry to the baseline-law branch of `independence_wave_ensure_custom_carrier_startup_state` in `common/scripted_effects/006_independence_wave_execution_effects.txt`.

## Adding a row

1. Confirm the row has a planner gate and loader in the package region registries and force data in the script constants.
2. Add the id and tag to `is_independence_wave_regional_framework_exact_carrier` and an `is_independence_wave_exact_package_iw_NNN_tag_available` trigger.
3. Add its identity block. Decide the leadership on the record: a vanilla roster, a sourced character, or the appointed leader of an institutional government.
4. For an X-tag, add the release branch and the baseline-law entry.
5. Add the id to the adapter list, the content attestation, both preflights, the runtime-ready and capacity triggers, the planner gate, the Join probe order and the contact registry, and update `.tools/audit_event6_allocator.py`.
6. For a Level 2 row, add its layer, decision category, ideas, two incidents and localisation.

## Interaction with other systems

- Foreign reactions read the row's registered contacts.
- Package incidents (`chaosx.nr6.200` onward for framework rows) are scheduled by the shared founding-posture resolution.
- Statehood incidents, milestones, League and formable discovery use the shared systems unchanged. Framework rows register no formable family.

## Assets

Framework rows reuse existing assets: registered vanilla or Event 006 flags and names for the tag, vanilla leader portraits, shared Event 006 idea pictures (`GFX_idea_independence_wave_*` and vanilla `generic_*` idea pictures), vanilla report event pictures and the shared Event 006 decision icons in `interface/006_independence_wave.gfx`. No new sprite is registered by the framework.

## Future plans

- A sourced leader for each institutional X-tag row, added as a character through the portrait pipeline when a rights-cleared source exists.
- A five-node focus group for each Level 2 row, following the accepted TAT/KUB pattern.
- Bind the unbound rows whose anchor now exists on the map (for example IW-075 Jabal Shammar at state 857, Ha'il) with a planner gate, loader and reservation, then admit them through the framework.
