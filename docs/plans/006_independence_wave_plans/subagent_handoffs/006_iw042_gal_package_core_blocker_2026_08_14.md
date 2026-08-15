# IW-042 Galicia-Lodomeria package-core blocker handoff (2026-08-14)

## Decision

No package-local gameplay core is safe to add for IW-042 in this tranche.

The existing dormant GAL compatibility wrapper remains unchanged. No constants, ideas, AI, decisions, localisation, focus hooks, country setup, leader, portrait, flag, central adapter, attestation, preflight, release list, Join route, map writer, workbook, or unrelated gameplay file was added or edited.

This handoff is the durable blocker record requested for the next parent review. The parent agent owns review and commit; this subagent did not stage or commit.

## Accepted registry and research boundary

The accepted research row at `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:43` binds IW-042 to registered `GAL`, `high_chaos_only`, anchors `91|89`, reservation group `RG-91-89`, and a limited Galicia-Lodomeria restoration package.

That row requires a period royal, customary, or historical institution joined to a provisional cabinet, municipal administration, veterans, schools, labor, and assembly route.

The same row requires regionally sourced institution names and states that portraits require a sourced real male officeholder or authentic archival material for the actual institution; it explicitly says to block the package when neither can be established.

The row also requires an attested royal, civic, religious, or regional symbol with documented faction ownership and permits only a restrained generated civic flag after the relevant source decision.

The installed binding at `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:43` is `ready_high_chaos`, fixed anchor 91, compact set 91|89, current owners `89=POL|91=POL`, and host remainder `POL=10`.

## Blocking findings

### 1. No source-backed GAL institution or leader identity

Vanilla registers `GAL` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:371` and loads `history/countries/GAL - Galicia and Lodomeria.txt` with capital 88, but that history contains no GAL-specific `recruit_character`, `add_country_leader`, or `set_country_leader` surface.

The installed vanilla character definitions contain no GAL character, leader, advisor, or commander that can be safely reused for an IW-042 institutional route.

The accepted asset coverage marks IW-042 as a Group C attested-symbol/restoration package at `docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md:108-110`; its leadership table has no cleared GAL subject or institution row.

Adding a generic council, invented claimant, fictional personal name, party, idea, decision, focus hook, or country localisation before a named institution is source-approved would turn an unresolved restoration identity into player-facing canon.

### 2. Flag and symbol provenance is explicitly blocked

`docs/plans/006_independence_wave_plans/asset_research/006_generated_flag_blockers.md:21-25` explicitly lists IW-042 Galicia-Lodomeria among the blocked Group C packages.

The unblock condition requires an asset-specific source establishing exact symbol owner, date, function, route, and licence, plus a decision identifying whether the source is a dynasty standard, faith symbol, regiment flag, town/province arms, restoration emblem, or neutral civic motif.

No generic flag, vanilla GAL flag substitution, or unowned royal or religious symbol is authorized by the current evidence.

Therefore no flag wiring, country identity idea, country cosmetic name, icon, or symbol-dependent decision/focus route can be safely added.

### 3. The map is reservation-ready but not package-ready

The current Region-04 loader at `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt:107-151` reserves GAL as candidate tag, state 91 as anchor, and state 89 as compact companion; it does not apply GAL ownership, cores, capital, force setup, or package gameplay.

Vanilla `history/states/91-Tarnopol.txt` and `history/states/89-Krakow.txt` are currently POL-owned and do not provide a vanilla GAL core on the IW-042 anchors.

Vanilla GAL history retains capital 88, while the accepted IW-042 compact package is Lwów/Stanisławów at 91/89. A gameplay core would need a package-owned state/core/capital transaction and post-apply validation that is not present in this scope.

The vanilla CZE route remains separate: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/czechoslovakia_mu.txt:1650,1690,3125-3127` adds a GAL core on state 88 and may release GAL there. No IW-042 package core may rewrite, consume, or silently replace that state-88 behavior.

### 4. Research-only force text does not justify a gameplay core

`docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:43` describes a future `regular_defectors` profile 63 with territorial infantry, defecting regulars, screened officers, engineers, reconnaissance, artillery, logistics, signals, and multiethnic command constraints.

This is research/design guidance, not a source-backed starting OOB, equipment allocation, technology inheritance contract, idea lifecycle, AI strategy, or decision family.

Adding a generic force, AI strategy, idea, or decision surface now would create disconnected content behind an unadmitted identity and would bypass the unresolved institution, symbol, and map transaction gates.

## Coverage checklist

| Surface | Disposition | Concrete finding |
| --- | --- | --- |
| Tag registration and origin | PASS for existing wrapper | Registered GAL is present and the wrapper guards `original_tag = GAL`, active Event 006 origin, exact package id `iw_042`, and living-tag state. |
| State ownership, cores, capital, host safety | HOLD | Binding is 91/89 with POL host remainder, but vanilla GAL has capital 88 and no GAL core on 91/89. Package-owned apply/rollback proof is absent. |
| CZE-origin preservation | PASS for preservation only | Vanilla CZE state-88 GAL core/release behavior remains untouched; it cannot authorize a new IW-042 package transaction. |
| Politics, parties, laws, diplomacy | BLOCKED | No named IW-042 institution or political identity is accepted; generic parties or restoration labels would invent identity. |
| Leaders, characters, advisors, commanders, portraits | BLOCKED | No vanilla GAL character exists and no sourced GAL institution/officeholder portrait is cleared. Portrait work must route to `chaosx_portrait_creator` after source acceptance. |
| Flags and symbols | BLOCKED | IW-042 is explicitly listed in the Group C generated-flag blocker; exact owner/date/function/route/licence evidence is missing. |
| Focus tree and hooks | HOLD | GAL has only the vanilla generic focus surface; no source-backed IW-042 route hook exists. CZE/POL Galicia focuses are separate vanilla routes and must not be repurposed. |
| Decisions, missions, ideas, localisation | BLOCKED | No named route, institution, cost model, idea lifecycle, or player-facing terminology can be authored safely. |
| Military, technology, industry, supply, production | HOLD | Force mapping is research-only; no package setup or technology inheritance contract exists. The installed package exposes no Technology Tree Viewer. |
| AI and probability | HOLD | Region-04 IW-042 remains a central dynamic random-list candidate, but this tranche adds no AI or weighted surface. No probability compare is applicable to an unchanged source. |
| Cleanup and replay safety | PASS for existing wrapper | The prior package-local wrapper remains dormant and marker-only; no new cleanup path was introduced. |

## Required unblock sequence

1. Accept a named provisional GAL institution or route-specific historical body with regionally sourced terminology and clear faction ownership.
2. Research and approve a real male officeholder or authentic all-male archival image for that exact institution, including date, role, rights, crop, and portrait-worker handoff evidence.
3. Resolve a symbol source for the exact institution or route and record owner, date, function, licence, and whether it is a civic baseline or route-owned restoration symbol.
4. Reconfirm current-map state 91/89 ownership, GAL core application, capital migration from vanilla 88, host survival, and rollback behavior through the parent-owned package transaction.
5. Only after those gates close, design package-local ideas, decisions, focus hooks, localisation, force setup, and AI, with the mandatory MCP focus/map/event/probability inspections and before/after probability audit for any new weighted surface.

## MCP evidence and limitations

The earlier bounded adapter audit recorded successful read-only MCP evidence in workspace `mod_chaos_redux_ea3b2d67c2c0`:

- States 91/89 map inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4161998b9908a3efb2e59d1f3dde8613eb255c70128a39dd929500410e1a352d/2107d6da03547383446d8f2025695915f9a2933b55e183a35e1bce9218312dd4/map-inspect.24bebf72ae84437c.json`.
- Owner-layer map render with state buildings, supply, rail, victory points, and resources: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0d0bc8e50fc6856b219c9805f27b7990a35c7f16410772e7be3071b48d53e48/603dcc3251e66b139f4bacfcf11b06bafd0dbc8b6d27256ba97a5d04feba256b/map-owner.json`.
- CZE `mu_czech_focus` inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e314ed6be593659e583d187e320dbe967e761db8576deed6d211046208fed68/b2c7788e787ad21b445b44144bb7f62e2ae09cf219ee3b9f01032a1320b73261/focus-inspect.5bb17398adee2259.json`.
- POL `polish_focus` inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4709a037fdfdbacd9a3abb492c09e06296452e33ecaa18458f24eb8fc29aae4f/92ad488712405e8e8dd0d142cc9559cf0db66f1eb2e34f75b31651e18ff351a1/focus-inspect.5bb17398adee2259.json`.
- Event 006 trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3cb368c1050f023b3da7fedb01b92680a9d51a04c164708ac8cb3d525c1ac3ac/b9f04288fc3461eea99254a96c5102a8101e1b34cf9ea08b4d08c27e335d4208/event-scan-741883f50501.json`.
- Region-04 random-list inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b51fac93d010fe3d487ab60c307b4ab417f48fafbe8dde9ae5db7d50ff08b05e/abb47daadebdb416eb2270a864d86a3805bc3b66f00a8e7d4bf71dd085e5a131/probability-inspect-e8f1792fa6b1.json`, structurally complete with eight candidates and no unresolved expressions.

The Event Chain Viewer did not include the mod `events/006_independence_wave.txt` in its scanned inventory and instead returned the vanilla event inventory; this remains an unresolved mod-source MCP limitation.

Fresh concurrent MCP retries for this tranche were attempted for map, focus, event, and probability surfaces but hung beyond the tool wait window and were terminated. The prior successful artifacts above remain the usable receipts; no source or map write was attempted.

## Validation and uncertainty

Offline Paradox wiki pages and installed vanilla documentation were consulted for country, state, trigger, effect, focus, decision, idea, localisation, AI, and probability syntax before deciding whether a core could be added.

Vanilla GAL tag registration, country history, state 89/91 history, CZE GAL core/release focus effects, POL Galicia route, GAL character search, and current Event 006 loader/force/asset research were reviewed.

No live game, save/load, package execution, Technology Tree Viewer, source-backed portrait, flag production, or probability compare was run.

The package remains incomplete and blocked; no simplification or fallback was silently substituted.
