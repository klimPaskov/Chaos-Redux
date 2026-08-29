# IW-050 Komi admission triage — 2026-08-25

## Verdict

This is a read-only Event 006 country-package admission audit for IW-050 Komi (`KOM`). No gameplay file, allocator registry, central adapter, attestation, map, asset, or promotion was changed.

IW-050 is the nearest package-local candidate by source completeness, but it is not safely promotable. Keep it fail-closed and do not add it to the central admission list or deterministic Join order.

The bounded recommendation is one parent-owned admission-evidence tranche: close the exact identity/rights, portrait, flag-origin, host/map, force-receipt, and typed AI evidence gates, then re-audit before any central wiring. Publishing `independence_wave_iw_050_identity_rights_cleared` without those receipts would bypass the package contract and is not recommended.

## Authority and package boundary

- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` remains authoritative: Event 006 is `HOLD / PARTIAL` with 32 content-attested selectable packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows.

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` explicitly keeps IW-050 package-local and fail-closed; a tag, history shell, portrait path, flag family, focus overlay, or local adapter is not an admission receipt.

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md` requires identity, politics, ideas, dynamic forces, complete flags and localisation, sourced grounded portraits, AI behaviour, reinforcement, safe host/map binding, and cleanup before selectable admission.

- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:51` identifies IW-050 as `KOM`, anchor state 397, and `RG-397`, with a sourced period leader or defensible institution required and no invented flag or portrait fallback permitted.

## Country package coverage checklist

- Identity and origin: present locally. `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:10-19` requires `original_tag = KOM`, package id `iw_050`, `liberation_origin.independence_wave`, and rejects the three Soviet Collapse origin markers and variable.

- Map and host: local gates are present. `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:57-71` requires setup, current-generation force, state 397 owned and controlled, state 397 as capital, a non-ROOT former-host target, and a former-host protected state still owned by `PREV`.

- Roster and identity rights: blocked by design. `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:91-97` requires both `KOM_pavel_murashev` and the parent-owned flag `independence_wave_iw_050_identity_rights_cleared`; the package does not set that flag locally.

- Setup and force: local validation is detailed. `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:149-209` requires the full framework, Komi route flags, p50 `mountain_frontier` force mapping, p50 military tradition, current-generation force package, five exact reinforcement flags, no navy or air inheritance, AI profile, lifecycle, starting idea, and state 397 capital.

- Politics and parties: the vanilla KOM carrier and package localisation/ideas/decisions are present, but this does not clear the grounded identity or admission asset gates.

- Focus and decisions: the package uses the accepted shared focus framework and a Komi decision category with serialized projects; no bespoke tree or unapproved fallback was introduced.

- AI: a Komi strategy profile exists, but it is not quantitatively admitted because the required named probability-auditor route is unavailable and the direct adapter found no normalized weighted candidates.

## File surface checklist and findings

### Identity, map, host, and collision

- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:10-19` is the exact package identity gate.

- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:57-71` is the exact runtime-ready gate.

- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:73-89` requires setup anchor and former-host event targets, state 397 ownership/control/capital, and host protected-state retention.

- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:99-109` makes tag availability conditional on candidate-origin availability, `KOM`, state 397 anchor availability, and a current owner that is not `KOM`.

- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:51` binds `IW-050` to `KOM`, state 397 Syktyvkar, optional states 262 and 581, and `RG-397`; it records that the current installed map is authoritative and that SOV must retain a protected state.

- `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv:33` gives `RG-397` capacity one and requires host protection before reservation; it forbids taking a protected capital when another safe package exists.

The current read-only `hoi4.map_inspect` for states 397, 262, and 581 returned `MAP_INSPECTED` with state membership, geometry-ID, network, and adjacency checks passing for the selected states. Overall validation was false because the workspace also reports global `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics from `map/buildings.txt`; this is not evidence of a Komi-local defect and does not prove former-host, capital, supply, or reservation safety. No map write was attempted.

### Politics, leader, portrait, flag, advisor, and party

- Vanilla `common/characters/KOM.txt` contains the exact male character `KOM_pavel_murashev` and `country_leader` metadata.

- Vanilla `interface/_leader_portraits.gfx` maps `GFX_portrait_Pavel_Murashev` to the generic `gfx/leaders/Europe/Portrait_Europe_Generic_3.dds`; no attributable 1936 Komi source and rights receipt is present for Event 006.

- There is no opposite-gender portrait/name pairing in the inspected carrier, but the generic portrait is not an acceptable grounded Komi identity. Event 005 committee art, another Murashev, an invented office, and generated grounded fallback are all prohibited by the accepted spec.

- The installed flag ladder includes `gfx/flags/KOM_democratic.tga`, `gfx/flags/medium/KOM_democratic.tga`, and `gfx/flags/small/KOM_democratic.tga`, and the static flag-family audit reports complete families. That proves file coverage only; accepted Event 006 neutral/route provenance and stable source/origin identity remain unresolved. No new KOM runtime flag or GFX wiring was added.

- `common/decisions/006_independence_wave_komi_decisions.txt` and `localisation/english/006_independence_wave_komi_l_english.yml` provide the package category, mission, projects, ideas, parties, and cost text. No Event 006 advisor portrait is required or authorized for this package.

### Focus, decisions, ideas, assets, and event admission

- `common/scripted_effects/006_independence_wave_komi_package_effects.txt:354-405` contains local lifecycle, setup, roster checkpoint, force/setup validation, and final-validation callbacks, but it deliberately does not admit KOM to the central dispatcher.

- `common/decisions/006_independence_wave_komi_decisions.txt` contains the Komi category and ten serialized projects. The current working-tree removal of `war_support_minor` from `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:51-55` is a concurrent edit; it was not authored, reverted, or treated as this audit's patch.

- Read-only `hoi4.focus_inspect` and `hoi4.focus_render` for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, returned 184 focuses, 195 connectors, zero crossings, and zero node intersections with no blocking diagnostics. Five authored layout warnings remain, including two long connectors; none is a Komi admission gate.

- Read-only `hoi4.event_inspect` and `hoi4.event_render` for `chaosx.nr6.350` returned partial workspace evidence with no blocking diagnostics, but selected-node and branch-render counts were zero because the large-workspace projection was deferred. This is not a runtime admission proof.

- No package-specific technology dependency was found. The installed package exposes no Technology Tree Viewer, so technology-tree engine evidence remains an unresolved tooling limitation if a future package revision introduces technology claims.

### Starting military, technology, industry, supply, and production

- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:186-204` proves the intended force mapping and reinforcement flag contract: `mountain_frontier`, p50 tradition, five reinforcement flags (`integrate_militias`, `regional_guards`, `secure_depots`, `terrain_units`, and `professional_officers`), and explicit rejection of navy and air inheritance.

- `common/scripted_effects/006_independence_wave_komi_package_effects.txt` contains package-local force setup and current-generation validation, but no live stockpile, manpower, train, convoy, fuel, supply, production, or map-owner receipt was available in this audit. The spec requires those dynamic force outputs before admission, so this remains an evidence gap rather than a safe patch target.

### AI and playability

- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:1543-1608` defines the Komi survival, host-restraint, settled-republic, and emergency strategy blocks with explicit army, infantry, artillery, support, infrastructure, bunker, and war-avoidance factors.

- Direct `hoi4.probability_inspect` on that source returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero candidates, and zero available surfaces. This adapter result cannot supply a quantitative scenario claim.

- The mandatory `chaosx_ai_probability_auditor` route and a same-scenario `hoi4.probability_compare` pass were unavailable in this runtime. No AI balance target or probability claim is made.

## Single bounded recommendation

Keep IW-050/KOM package-local and fail-closed. The next owner patch should be limited to an admission-evidence receipt for `independence_wave_iw_050_identity_rights_cleared`, grounded in the exact 1936 leader or actual provisional institution, portrait-worker archive and consumer review, a stable KOM flag-origin decision, a fresh map/host/collision receipt for state 397 and `RG-397`, and typed AI scenarios through the named probability auditor. After those receipts are accepted, the parent may add the central IW-050 adapter, attestation, preflight, setup/final/cleanup hooks, normal and SCN-008 publishers, and Join entry in one separately reviewed change.

Do not use a generic portrait, Event 005 committee art, generated grounded portrait, invented flag, central adapter, or source-only AI/map result as a fallback. No safe local gameplay patch was found in this audit.

## Validation and limitations

- Passed repository checks: `.tools/audit_event6_allocator.py`, `.tools/audit_event6_country_api.py`, `.tools/audit_event6_flags.py`, and `.tools/audit_event6_scenario_matrix.py`.

- Useful MCP artifacts: map inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/903a205e6753fb67206b318afbbebb9659d5d07f279b0170041e0bc2765fcc80/de9d08ba8bef2c04c38d92a00178def57d001f45694f65ce2c4871dacc825fc1/map-inspect.2f8752c59a6fc0cd.json`; probability inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cfd47123134de772b3a505974b1d5d031bd71fc1e4160213c508c421278ea39/fa10057903fb0040d4ad9274b0288116076bc20aaebb55c9c5743b2f4e6b9910/probability-inspect-4e0cfccef4e0.json`; focus inspect revision `4f4450e8ecd993eb4a5e1b0585eac6a6fff93f1a0ceb53d7100b3563fb226b18`.

- Event MCP inspect/render were partial and did not certify package admission. No HOI4 process was launched, no map or gameplay write was performed, and no promotion occurred.

- Remaining blockers are identity/rights provenance, portrait production and wiring review, flag-origin acceptance, host/map transaction evidence, live force/stockpile/supply receipt, and the unavailable named AI probability-auditor route.

## Changed files

- Added only this handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw050_komi_next_admission_triage_2026-08-25.md`.

- Gameplay, central registries, allocators, map, flags, portraits, and package source were not edited.
