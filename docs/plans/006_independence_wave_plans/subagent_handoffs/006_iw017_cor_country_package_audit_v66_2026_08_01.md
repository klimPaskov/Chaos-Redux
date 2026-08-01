# Event 006 IW-017 Corsica country-package audit v66

Date: 2026-08-01

Scope: Evidence-only static audit of the Event 006 Independence Wave IW-017 Corsica package (carrier tag `COR`).

Disposition: PARTIAL.

The package source surfaces are statically covered and no patchable country-package defect was found in this pass.

The overall disposition remains PARTIAL because the shared Event 006 focus artifact reports fourteen blocking diagnostics, runtime compile and in-game allocation evidence is not available, and the installed package exposes no Technology Tree Viewer.

No gameplay, asset, localisation, map, or country-source files were changed by this audit.

## 1. Package identity and accepted resolution

| Surface | Evidence | Status |
| --- | --- | --- |
| Candidate registry | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` records IW-017 as Corsica with `resolved_tag=COR` and `tag_resolution=reuse_registered_tag`. | PASS |
| Research resolution | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` records COR reuse, automatic-pool readiness when not living, state 1, and RG-1. | PASS |
| Reservation group | `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv` binds IW-017 to RG-1, state 1, Mediterranean and Iberia, with no static collision. | PASS |
| Map binding | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` binds the fixed anchor to state 1 Corsica and the former host capital protection to FRA state 16. | PASS |
| Carrier identity | `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt` requires `original_tag = COR`, active package `iw_017`, and the exact COR roster. | PASS |
| Country shell | No mod country-definition or tag-registration shell is required because the accepted design reuses dormant vanilla COR. | PASS |

The accepted package identity is IW-017/COR/RG-1 with state 1 as the compact anchor, France as former host, and a Mediterranean and Iberia regional overlay.

## 2. Coverage checklist

| Country-package surface | Identifiers and source | Result |
| --- | --- | --- |
| Registry and tag reuse | `IW-017`, `COR`, `iw_017`, `RG-1`; `006_candidate_country_registry.csv`; `006_package_research_resolution.csv`. | PASS |
| Anchor and state control | State `1` (Corsica), capital state `1`; `is_independence_wave_cor_package`; `can_initialize_independence_wave_iw_017_package`. | PASS |
| Former-host survival | FRA former host, protected capital state `16`; `liberation_release_protected_state`; host survival guard in `006_current_installed_map_package_bindings.csv`. | PASS static |
| Opening politics and laws | `civilian_economy`, `export_focus`, `volunteer_only`; democratic elections; COR population constants. | PASS |
| Leaders and characters | `COR_corsican_municipal_congress`, `COR_jean_chiappe`, `COR_paolo_pietri`, `COR_antone_rocchi`. | PASS |
| Portrait metadata | Landry and Chiappe male records with large portraits; Pietri and Rocchi intentionally portraitless advisors. | PASS |
| Parties and names | Base and route-specific COR party/country keys in `006_independence_wave_mediterranean_l_english.yml`. | PASS |
| Focus assignment | `independence_wave_focus_tree`, full framework only for generic COR; five COR nodes. | PARTIAL global geometry |
| Decisions and mission | COR category, mission, and eight package decisions. | PASS |
| Ideas and visible values | Exposed-island, civic-coastal, route, guard, and customs ideas; Maritime Access variable. | PASS |
| Form05 link | COR maritime congress preparation and exact COR/state-1 carrier trigger. | PASS |
| Founding and route events | `chaosx.nr6.21` founding and `chaosx.nr6.24` route event; hidden synchronous roster event `chaosx.nr6.350`. | PASS static |
| Military opening | `coastal_maritime` profile `p17`, tradition `p17`, reinforcement and inheritance masks. | PASS static |
| Technology and slots | Former-host technology inheritance and minimum/industrial research-slot setup in force effects. | PASS static; viewer unavailable |
| Industry, supply, and production | Dynamic infantry/support/artillery/train/convoy/fuel stockpiles, port and infrastructure support. | PASS static |
| AI and playability | Survival, founding restraint, host threat, civic maritime, and island guard strategies. | PASS |
| Flags and assets | Vanilla COR base/ideology flags; COR portrait and focus/decision sprites. | PASS |
| Cleanup | Exact COR decision, idea, mission, character, variable, package flag, and focus-reset cleanup. | PASS static |
| Event 005 collision | Event 005 Soviet-core, host, and anchor exclusion predicates plus joint allocation ordering. | PASS static |

## 3. File-surface checklist

The package has the expected gameplay and documentation surfaces.

- `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt` contains COR identity, roster, Maritime Access thresholds, setup readiness, focus-framework, route, host, ambition, Form05, force, lifecycle, and cleanup predicates.
- `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt` contains the COR roster preparation, baseline politics, route setup, ambition, Form05, force-map, AI/lifecycle, founding-event, and cleanup effects.
- `events/006_independence_wave.txt` contains hidden event `chaosx.nr6.350`, which recruits the four COR records synchronously.
- `events/006_independence_wave_mediterranean.txt` contains `chaosx.nr6.21` and `chaosx.nr6.24` with exact COR package guards and no direct ownership-transfer effects.
- `common/characters/006_independence_wave_mediterranean_characters.txt` contains the four COR character records and their intended roles.
- `common/national_focus/006_independence_wave_focus.txt` contains the Event 006 full focus tree and the five COR focus nodes.
- `common/decisions/categories/006_independence_wave_mediterranean_categories.txt` contains `independence_wave_cor_corsica_category`.
- `common/decisions/006_independence_wave_mediterranean_decisions.txt` contains the COR mission and eight COR decisions.
- `common/ideas/006_independence_wave_mediterranean_ideas.txt` contains COR starting and route ideas.
- `common/ai_strategy/006_independence_wave_mediterranean.txt` contains the five COR AI strategy blocks.
- `common/script_constants/006_independence_wave_mediterranean_constants.txt` contains COR tuning, duration, politics, and AI constants.
- `common/scripted_effects/006_independence_wave_force_effects.txt` and `common/script_constants/006_independence_wave_force_package_constants.txt` contain the dynamic opening-force profile and `p17` mapping.
- `common/decisions/006_independence_wave_form05_decisions.txt`, `common/decisions/categories/006_independence_wave_form05_categories.txt`, `common/scripted_triggers/006_independence_wave_form05_triggers.txt`, and `common/scripted_effects/006_independence_wave_form05_effects.txt` contain the shared Form05 surface used by COR.
- `localisation/english/006_independence_wave_mediterranean_l_english.yml` contains current COR leaders, advisors, parties, category, mission, decisions, focus text, tooltips, and AI strategy keys.
- `localisation/english/006_independence_wave_form05_l_english.yml` contains the shared Form05 text used by the COR carrier link.
- `interface/006_independence_wave_mediterranean_assets.gfx`, `interface/006_independence_wave_mediterranean_portraits.gfx`, and `interface/006_independence_wave_form05.gfx` register the relevant sprite paths.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` provide accepted identity, research, and map authorities.

## 4. Registry, map, and state setup

`COR` is the accepted dormant vanilla carrier and is guarded by `is_independence_wave_exact_package_iw_017_tag_available`.

The allocator requires the candidate origin to be absent from the live country pool, unreserved, not rejected, and free of the Soviet, Event 006, and Event 012 origin flags before COR can be selected.

The package initializer requires state 1 to be owned and controlled by COR, state 1 to be the capital, and the former host to exist and not be ROOT.

The vanilla state file `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\1-France.txt` defines state 1 as Corsica with owner FRA, cores COR and FRA, province 3838 as the victory point, naval base 3, and the expected island provinces.

The vanilla former-host capital file `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\16-Ile de France.txt` keeps state 16 as FRA with Paris and the principal French industrial base.

The mod has no `history/states` override for state 1, so the accepted compact anchor is the installed vanilla Corsica state rather than a duplicate state definition.

Read-only MCP map inspection of state 1 passed state, region, network, supply, railway, port, and position checks.

Map artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50c156b9913ba0fef98fc568d124d203588af8775468ff7cb1b89baec4d39651/ed1b0fdee5d85d9b5123b2f5599927eb7f230d18d04831c64436f12b0777477c/map-inspect.b2a3d78a03c1d509.json`.

No static map or state defect was found.

Runtime state transfer, host survival during an actual allocator run, and save/load allocation behavior were not observed in this audit.

## 5. Host survival and release safety

The accepted binding protects FRA state 16 as the host capital and requires FRA to retain at least one 1936 state after the compact set.

The package setup uses the generic liberation-release protected-state guard before state 1 can be released.

The allocator and package effects do not grant an unconditional survival guarantee, and the regional design expects survival through careful play, geography, diplomacy, and outside aid.

Static code therefore matches the accepted host-survival design.

The remaining evidence gap is runtime: no live release, trim-extension, or host-loss sequence was run by this subagent.

## 6. Politics, leaders, portraits, flags, advisors, and parties

The opening package applies `civilian_economy`, `export_focus`, and `volunteer_only`, enables democratic elections, and uses the accepted COR population constants of democratic 46, communist 14, neutrality 32, and fascism 8.

The provisional authority setup promotes the Landry centrism record and then applies constitutional, traditional, guard, or patron route authority through the package effects.

The exact roster is `COR_corsican_municipal_congress`, `COR_jean_chiappe`, `COR_paolo_pietri`, and `COR_antone_rocchi`.

`COR_corsican_municipal_congress` is the visible male country leader with localisation `COR_adolphe_landry`, portrait `GFX_portrait_COR_independence_wave_adolphe_landry`, and centrism, socialism, and oligarchism ideology entries.

`COR_jean_chiappe` is a male despotism country leader and corps commander with the large civilian and army portrait `GFX_portrait_COR_independence_wave_jean_chiappe`, engineer-officer and infantry-officer traits, and the defined skill values.

`COR_paolo_pietri` is a male portraitless political advisor using idea token `COR_paolo_pietri`, the municipal customs trait, and the administrative cost.

`COR_antone_rocchi` is a male portraitless political advisor using idea token `COR_antone_rocchi`, the mountain defense trait, and the strategic cost.

No opposite-gender portrait/name pairing was found.

No `_small` or advisor portrait blocks are expected for the two portraitless advisors in the accepted package.

The current English localisation file covers the four visible names, descriptions, base and route party names, and advisor idea keys.

Vanilla `countries_l_english.yml` supplies `COR: "Corsica"` and `COR_ADJ: "Corsican"`.

The package intentionally reuses vanilla COR base, medium, small, and ideology flag variants at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\flags\COR.tga` and its variants.

No mod custom COR flag is required by the accepted "reuse base flag" resolution.

Historical candidate portrait files for Pasquale Venturi and Petru Santucci remain under `docs/assets/006_independence_wave/mediterranean_portraits_2026_07_16/`, but no current character, sprite, or gameplay source references them.

Those candidate files are evidence-only and are not a runtime asset defect.

## 7. Focus, decisions, ideas, and Form05

The package is assigned the Event 006 full framework only when the carrier is still on the generic focus tree.

The full framework is not additive for COR, which prevents an external full tree from being replaced by a shallow overlay.

The five COR focus IDs are `independence_wave_cor_reopen_ajaccio_customs_focus`, `independence_wave_cor_secure_mountain_post_road_focus`, `independence_wave_cor_register_coastal_communes_focus`, `independence_wave_cor_settle_french_maritime_accounts_focus`, and `independence_wave_cor_authorize_form05_delegation_focus`.

Their source prerequisites, package guards, icons, effects, AI weights, and English localisation are present.

The focus source expresses the accepted Mediterranean overlay through customs, mountain roads, coastal communes, French maritime settlement, and the Form05 maritime congress rather than generic romantic separatism.

Read-only `hoi4_focus_inspect` resolved the Event 006 tree source and returned 184 focuses and 223 connectors, but workspace validation was false with 130 diagnostics, including 14 blocking focus diagnostics.

Because those diagnostics are global to the shared tree and were not isolated to the five COR nodes, the focus surface is marked PARTIAL rather than treated as a package-local failure.

The COR category is `independence_wave_cor_corsica_category`.

The COR mission is `independence_wave_cor_hold_island_supply_together`.

The eight COR decision IDs are `independence_wave_cor_reopen_ajaccio_customs_house`, `independence_wave_cor_secure_mountain_post_road`, `independence_wave_cor_register_coastal_communes`, `independence_wave_cor_constitutional_communes`, `independence_wave_cor_mountain_communes`, `independence_wave_cor_island_guard_mandate`, `independence_wave_cor_protected_customs_mandate`, and `independence_wave_cor_prepare_maritime_congress`.

The mission and decisions are package-gated, costed, serialised, localised, and supplied with cancellation or failure effects.

The first three operational decisions improve maritime access or project flags, route decisions require stable access and route availability, and Form05 preparation requires stable access, the Form05 mandate, and the strategic cost.

COR ideas include `cor_exposed_island_supply`, `cor_civic_coastal_compact`, `cor_constitutional_communes`, `cor_mountain_communes`, `cor_island_guard_mandate`, and `cor_protected_customs_mandate`.

The ideas expose the intended supply, stability, trade, production, recruitable, defense, training, and coastal-security tradeoffs.

Form05 carrier validation requires original tag COR, package `iw_017`, anchor state 1 owned and controlled, capital state 1, the COR focus mandate, and the COR maritime-congress carrier mandate.

The Form05 path is charter-driven and does not annex, core, puppet, or transfer states.

## 8. Military, technology, industry, supply, and production

The accepted force mapping loads profile `coastal_maritime` with profile key `p17` and tradition key `p17`.

The force constants set `independence_wave_force_package_profile.p17 = 5`, `military_tradition.p17 = 53`, `reinforcement_mask.p17 = 1159`, `inheritance_mask.p17 = 1`, and `research_sensitive.p17 = 0`.

The reinforcement mask enables the mapped militia, regional-guard, depot, terrain-unit, and capital-border-defense components according to the force-file bit definitions.

The inheritance mask permits navy inheritance only; no unsupported free air force inheritance is enabled.

Opening divisions are generated dynamically at the anchor state using six infantry regiments and engineer support for the coastal-maritime template.

The force effects provision infantry equipment, support equipment, artillery, trains, motorised stock, convoys, and fuel using the package profile rather than a hardcoded country blob.

Former-host technology inheritance and minimum or industrial research-slot setup are present in the force effects.

No static source gap was found in the military, industry, supply, or production setup.

No runtime force materialisation or live research-slot outcome was observed.

The installed package currently exposes no Technology Tree Viewer, so technology-tree inspection is an unresolved limitation and is not claimed as complete runtime validation.

## 9. AI and playability

The COR AI strategy file contains `independence_wave_cor_island_survival`, `independence_wave_cor_founding_restraint`, `independence_wave_cor_host_threat`, `independence_wave_cor_civic_maritime_policy`, and `independence_wave_cor_island_guard`.

The survival strategy prioritises army, infantry, support, artillery, trains, convoys, infrastructure, and dockyards.

The founding-restraint strategy avoids severe host threats, regional-power overreach, and unnecessary wars with a founding restraint factor of -240.

The host-threat strategy shifts to emergency army and coastal or inland bunker priorities when the former host becomes severe.

The civic-maritime strategy supports constitutional, traditional, and patron governments with war restraint, dockyard, and convoy priorities.

The island-guard strategy increases emergency army and coastal-defense priorities for the guard route.

No COR AI strategy starts an unbounded war, bypasses the charter, or grants free forces.

The static strategy design is consistent with the accepted island-survival and regional-overlay requirements.

Actual AI focus selection, diplomacy, front behavior, and survival over a live scenario remain unobserved.

## 10. Events, lifecycle, and cleanup

The hidden `chaosx.nr6.350` event recruits the four COR records synchronously before the founding chain uses them.

The COR founding event is `chaosx.nr6.21`, and the route event is `chaosx.nr6.24`.

The event source uses exact COR package triggers and does not directly transfer ownership, cores, or subjects outside the accepted release setup.

COR lifecycle refresh changes `cor_exposed_island_supply` to `cor_civic_coastal_compact` when Maritime Access reaches the stable threshold of 65.

`independence_wave_cleanup_iw_017_corsica` removes the COR mission, all eight COR decisions, COR ideas, Maritime Access, Form05 family and package flags, resets an Event 006 focus tree to generic when applicable, and retires all four COR characters.

The shared cleanup dispatcher calls the COR-specific cleanup effect.

Static cleanup coverage is PASS; runtime cleanup after annexation, cancellation, or failed Form05 progression was not executed.

## 11. Event 005 collision and allocator safety

`common/scripted_triggers/006_independence_wave_package_triggers.txt` requires the exact dormant COR origin and excludes current reservations, rejected plans, and protected origin flags.

`common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt` requires the IW-017 plan slot, RG-1 availability, exact COR tag availability, and state 1 availability.

`common/scripted_triggers/006_independence_wave_triggers.txt` excludes Event 005 Soviet base republics, Event 005 opening-core anchors, and hosts holding Event 005 opening-core states.

The allocator order is Event 005 anchors, then Event 006 anchors, then optional territory, then reservation lock.

The current installed-tag audit dated 2026-08-01 reports 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions.

The static COR/state-1/FRA facts therefore show no Event 005 collision.

## 12. Stale, missing, and unresolved surfaces

No current gameplay source surface required for the accepted COR package was missing.

The absence of a mod `common/country_tags` COR registration, mod country definition, or custom COR flag is intentional under the accepted dormant-vanilla-tag and base-flag-reuse design.

Historical portrait candidate directories and older portrait source manifests under `docs/assets/006_independence_wave/` may retain pre-wire wording, but they are not referenced by current runtime character or sprite definitions.

The shared focus tree still has unresolved global geometry diagnostics from the read-only focus inspector.

Runtime compile, live allocator allocation, release, save/load, AI, and cleanup attestation were not performed by this subagent.

No Technology Tree Viewer is exposed by the installed MCP package, so technology-tree validation remains unresolved.

No active Venturi or Santucci character records are a gap; the accepted roster intentionally uses Landry, Chiappe, Pietri, and Rocchi.

## 13. Static validation evidence

- `python .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic or high-chaos selectable entries, 138 SCN008-ranked entries, 13 attested entries, 12 compatible groups, automatic counts 6/8/10/14/20, and the expected joint allocation order.
- `python .tools/audit_chaosx_country_tags.py --surface-scan` passed with 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions.
- Read-only MCP map inspection of state 1 passed all five map checks.
- Read-only MCP focus inspection resolved the Event 006 tree source but returned workspace validation false with 130 diagnostics and fourteen blocking focus diagnostics; this is recorded as the focus PARTIAL blocker.
- Read-only MCP event inspection of `chaosx.nr6.21` and state flow returned partial workspace reports with no blocking diagnostics for the selected event, but workspace-wide helper and lifecycle validation remained deferred.
- The relevant `.gfx` texturefile references for COR portraits, focus icons, decision icons, and Form05 sprites resolve to existing files in the inspected asset paths.

Map artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50c156b9913ba0fef98fc568d124d203588af8775468ff7cb1b89baec4d39651/ed1b0fdee5d85d9b5123b2f5599927eb7f230d18d04831c64436f12b0777477c/map-inspect.b2a3d78a03c1d509.json`.

Focus artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9baafa97ba4831bbf0dd87c70171aaede1ff5de2ea73530512a1c3d2392ca9d1/63ad5f314e231e7615bce834f348f1bbf827a2581f22dc76c54584ed66c2a379/focus-inspect.024553ab04f6531b.json`.

Event state-flow artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53e0bc031d56265a31f9fe0d0cec0001815b4e20c2f02e77939bc19a2aaa15d0/a3886aee9b7f189c93f77aa929f57f1e9815201f66a4d07ed71accf7f524c3f3/event-state_flow-d8990c907731.json`.

Event lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7284790b54b2e087566e77458915f2aa1e35d3487ef3a530fb6d72c2644c31c/9d4d81948796dcae147d31f8139d758dd152097e596d89bc53cb7790bd727218/event-lint-d8990c907731.json`.

## 14. Changed files and handoff

Changed file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw017_cor_country_package_audit_v66_2026_08_01.md`.

No tags, state IDs, leaders, parties, focus IDs, localisation keys, formable IDs, gameplay effects, or assets were changed.

No broad redesign plan was written because the audit found no patchable local country-package gap.

The parent should retain the PARTIAL disposition until the shared focus geometry is reviewed and runtime compile, allocation, and save/load evidence are supplied by the main implementation workflow.

Remaining setup and identity risk is limited to those runtime and shared-tree validation gaps plus stale evidence-only portrait documentation.
