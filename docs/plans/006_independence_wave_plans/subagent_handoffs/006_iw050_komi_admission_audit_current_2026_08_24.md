# IW-050 Komi admission audit — 2026-08-24

## Disposition

IW-050 Komi (KOM, package iw_050, anchor state 397 Syktyvkar, reservation group RG-397) remains package-local and fail-closed.

No exact central-admission gate is fully proven by the current files and current MCP attempt set.

The package-local source contract is substantially present, but the identity/source packet, central adapter/attestation/preflight/Join path, current map MCP evidence, and typed probability evidence remain incomplete.

Central Event 006 admission remains unchanged at 32 content-attested selectable packages, 40 runtime adapters, 29 compatible reservation groups, and 161 unattested selectable rows out of 193 non-overlay rows.

The eight adapter-only fail-closed IDs remain IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM.

This audit made one documentation-only package-local correction in docs/events/006_independence_wave/komi_package.md:39 so the strategic-cost description matches the current trigger and shared payment effect.

## Authority and scope

The accepted country-package authority is docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md and docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md.

The current implementation authority is docs/plans/006_independence_wave_plans/006_source_of_truth_map.md, docs/specs/006_independence_wave_specs/quality/package_manifest.md, docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md, and the dated IW-050 handoffs in docs/plans/006_independence_wave_plans/subagent_handoffs/.

The required offline wiki pages and vanilla country/history/character/portrait/flag references were read before this audit.

No HOI4 launch, save/load, map write, central admission edit, asset generation, portrait substitution, or broad identity redesign was performed.

## Country-package coverage checklist

| Surface | Status | Evidence and exact remaining gate |
| --- | --- | --- |
| Candidate identity | Partial | Registry row docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:51 fixes IW-050 as Komi, KOM, region 05, Layer B, standard compact package, 397 Syktyvkar, and RG-397. The package trigger common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:10-19 requires original tag KOM, active Event 006 origin, package iw_050, and non-Soviet origin. Parent identity-rights clearance is still absent. |
| Tag registration and reuse policy | Static pass; admission blocked | Vanilla common/country_tags/00_countries.txt:232 maps KOM to countries/Komi.txt. No Chaos Redux duplicate tag registration was found. Reuse is allowed only when the registered tag is dormant and the released identity/origin is accepted; central preflight does not list iw_050. |
| History and leader | Partial; source gate blocked | Vanilla history/countries/KOM - Komi Republic.txt:1,101 uses capital 397 and recruits KOM_pavel_murashev. Vanilla common/characters/KOM.txt:3-13 defines the male Stalinist country leader. The exact 1936 release-date source/rights packet is still missing. |
| Anchor and optional territory | Static source present; MCP gate unresolved | Accepted binding is 397 Syktyvkar with optional 262 Pechora/Torzhok and 581 Northern Urals in docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:51. The region-05 loader reserves 397 then tries 262 and 581 in common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:74-83,193-194. Current map MCP calls timed out or hit transport closure, so no current engine acceptance is claimed. |
| Host survival and Event 005 collision | Source guards present; runtime proof absent | Event 005 keeps KOM as its own Soviet-origin carrier and restores KOM cores on 262, 397, and 581 in common/scripted_effects/005_soviet_collapse_effects.txt:4079-4081. Event 005 state-free and active-origin guards remain in common/scripted_triggers/005_soviet_collapse_triggers.txt:14-19 and related release predicates. A live protected-host remnant receipt is not available. |
| Flag and symbol source | Blocked for admission | The current vanilla gfx/flags/KOM_*.tga ladder was rehashed and is stable in this audit: all are 82x52 32-bit files; KOM_communism.tga SHA-256 30FF8121E5099723E0CD3411A9A2C44FC4192549038A1B42F059D91358724AEE, and democratic/fascist/neutrality each SHA-256 F550493E3CA57BAB7337088291F5ADE36937729C0F1F234B44276DBA5187FB24. Hash stability is not historical provenance or route-fit proof. The mod's only KOM flag files are the Event 005 democratic ladder under gfx/flags/, and no Event 006 neutral/route flag source packet exists. |
| Portrait and source provenance | Blocked | Vanilla common/characters/KOM.txt:3-8 uses GFX_portrait_Pavel_Murashev, while vanilla interface/_leader_portraits.gfx:5576-5579 points it to generic gfx/leaders/Europe/Portrait_Europe_Generic_3.dds. The IW-050 portrait handoffs 006_iw050_komi_portrait_source_audit_2026_08_14.md and 006_iw050_komi_portrait_identity_research_2026_08_14.md found no attributable 1936 image or rights-clear institutional source. No source placeholder, crop archive, portrait-worker manifest, or final portrait promotion exists. |
| Politics, parties, government routes | Package-local source present | common/scripted_effects/006_independence_wave_komi_package_effects.txt:146-232 initializes democratic baseline politics and four guarded route governments. Party names are localized at localisation/english/006_independence_wave_komi_l_english.yml:2-9. Cleanup restores the vanilla party names and popularity at the package effects file lines 412-455. Runtime route behavior remains unobserved. |
| Ideas and lifecycle | Package-local source present | The consolidated idea registry common/ideas/006_independence_wave_ideas_registry.txt:2867-2938 contains seven Komi ideas restricted to original_tag = KOM. Setup and cleanup remove/add the package idea lifecycle in the package effects file lines 11-47 and 329-458. |
| Shared focus assignment | Static source present; current MCP unavailable | Five guarded KOM helper calls are present in common/national_focus/006_independence_wave_focus.txt:123,176,210,1444,1715. The 2026-08-14 focus receipt reported 184 focuses, 196 connectors, zero crossings, zero node intersections, and two long connectors; current focus inspect and render both failed with Transport closed. |
| Decisions and mission | Package-local source present; typed probability incomplete | common/decisions/006_independence_wave_komi_decisions.txt:14-285 defines one founding mission and ten serialized paid projects with package-specific availability, cancellation, cost, AI, and effect hooks. The prior typed inspect found 11 candidates, zero currently available candidates, 15 required inputs, and poolComplete=false; current probability calls could not reconnect. |
| Package AI | Source present; probability unresolved | Consolidated common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:1542-1610 contains survival, host restraint, settled-republic, and emergency profiles. The prior IW-050 probability audit returned no_weighted_surfaces and PROBABILITY_SURFACE_EMPTY; current ai_strategy_factor inspect failed with Transport closed. No balance claim is made. |
| Starting force and reinforcement | Source contract present; runtime proof absent | docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:51 fixes p50 mountain_frontier, tradition 55, no navy/air inheritance, and five named reinforcement pathways. common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:186-205 requires the mapping, current generation, five reinforcement flags, and Komi AI profile. No release transaction or final force receipt exists. |
| Industry, supply, production | Source/localized package surfaces present; runtime unproven | Komi projects use the civilian-factory reservation constant and shared command/manpower/convoy-or-train cost palette in common/decisions/006_independence_wave_komi_decisions.txt:68-285 and localisation/english/006_independence_wave_komi_l_english.yml:55-60. The shared payment effect is common/scripted_effects/006_independence_wave_decision_effects.txt:199-214,350-353. No live stockpile, supply, production, or playability receipt is available. |
| Localisation | Static package coverage pass | localisation/english/006_independence_wave_komi_l_english.yml contains 65 keys and has a UTF-8 BOM. The 27 package display references in the decision file resolve either locally or to shared Event 006 keys. No package-local missing display key was found. |
| Assets and manifests | Blocked at source/rights boundary | Package ideas and decisions use existing shared icons. No new Event 006 portrait, neutral flag, route flag, advisor icon, or manifest was created. Event 005 KOM visual assets under gfx/leaders/005_soviet_collapse/KOM_leader.dds and GFX_portrait_KOM_mine_river_committee are not valid substitutes for the Event 006 exact leader/source gate. |
| Formables and claims | Registry source present; admission unavailable | FORM-12/FORM-13 source consumers recognize KOM state 397 only through active package, frozen invitation, ownership/control, and consent receipts. Registry presence and KOM cores alone do not establish membership. No formable promotion was attempted. |
| Technology | Unresolved limitation, no package-specific tech surface | Vanilla KOM history has the normal research setup but IW-050 adds no technology or doctrine dependency. The installed HOI4 MCP package exposes no Technology Tree Viewer; no substitute technology evidence is claimed. |
| Central adapter and content attestation | Blocked | common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63 has no iw_050 adapter branch, and lines 159-202 have no IW-050 content-attestation branch. The exact preflight at lines 207-260 therefore rejects the package before runtime release. |
| Central setup/final validation/cleanup dispatch | Blocked | common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:45-86,93-119 calls no Komi setup, final-validation, or cleanup function. Package-local equivalents exist at common/scripted_effects/006_independence_wave_komi_package_effects.txt:400-458, but they are not central admission. |
| Deterministic Join and scenario preflight | Blocked | No iw_050 Join or normal/SCN-008 preflight path is present in central dispatch. The region-05 loader and reservation rows are planner inputs only. |

## File surface checklist

| Surface | Current file(s) and identifiers | Finding |
| --- | --- | --- |
| Registry and identity | 006_candidate_country_registry.csv:51; 006_package_research_resolution.csv:51; 006_state_anchor_and_reservation_groups.csv:33 | Canonical identity is consistent: IW-050/KOM/397/RG-397/region 05. Research still explicitly requires a sourced male leader or defensible institution and provenance-safe flag treatment. |
| Constants and IDs | common/script_constants/006_independence_wave_constants_registry.txt:6224-6267,7623; common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:74-83 | Package ID, regional constants, compact values, and loader are present in the consolidated registries. |
| Triggers | common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:10-220 | Identity, origin, anchor, host, roster-rights, force, AI, setup, and runtime-ready predicates are present. The parent-owned independence_wave_iw_050_identity_rights_cleared flag has no local setter. |
| Effects | common/scripted_effects/006_independence_wave_komi_package_effects.txt:329-458 | Setup, route initialization, five focus helpers, local roster checkpoint, final validation, and generation-safe cleanup are present. |
| Ideas | common/ideas/006_independence_wave_ideas_registry.txt:2867-2938 | Seven Komi ideas are consolidated and tag-restricted. |
| Decisions/category | common/decisions/006_independence_wave_komi_decisions.txt:14-285; common/decisions/categories/006_independence_wave_categories.txt:363-370 | One category, one 420-day founding mission, and ten package projects are source-wired. |
| AI | common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:1542-1610 | Four package AI strategy blocks are source-wired but not quantitatively MCP-audited in the current transport state. |
| Focus | common/national_focus/006_independence_wave_focus.txt:123,176,210,1444,1715 | Shared generic tree only, with five KOM-specific reward/helper calls. No bespoke tree is authorized by the accepted scope. |
| Localisation | localisation/english/006_independence_wave_komi_l_english.yml:2-70 | Party, idea, category, mission, decision, cost, and effect text is present. |
| Documentation | docs/events/006_independence_wave/komi_package.md:1-77 | Package-local contract and admission boundary are documented; this audit corrected the stale strategic-cost wording at line 39. |

## Map and state setup issues

Vanilla state history confirms state 397 is SOV-owned with a KOM core and capital victory point, while 262 and 581 are optional SOV-owned KOM-core extensions.

The accepted current-map binding records 262=SOV|397=SOV|581=SOV and a protected SOV remnant count of 219 in docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:51.

The package trigger requires state 397 to be owned and controlled by the released country and capital at both initialization and final validation in common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:57-89,149-220.

The current hoi4.map_inspect request for states 397, 262, and 581 timed out after 180 seconds, the retry for state 397 returned Transport closed, and the current hoi4.map_render request returned Transport closed.

The last successful source-linked map artifact remains hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cbab95cb59d8dbf924b89f3518684414317d11bc667a7fd513ff5c8ae5e56bc1/e613306c61b58cdb90c0e9bf9296d9b5084dd2fd706524b30f553461b64efc23/map-inspect.a08888ecbb9231a9.json from the 2026-08-14 crosswalk; it passed state/region membership and networks/adjacencies but did not prove a new allocation.

No map write was performed, and the prior explicit allocation request's MAP_STATE_ID_COLLISION is not treated as current map acceptance or rejection without a fresh MCP result.

## Politics, leader, portrait, flag, advisor, and party issues

The vanilla leader is male and the current package uses the exact KOM_pavel_murashev character key, so no opposite-gender pairing or random-name-pool defect is present.

The blocker is provenance and timing, not a missing key: the vanilla character is validly wired but its portrait sprite is generic, and the current source research has no rights-clear image or institutional source that satisfies the accepted 1936 identity contract.

The package correctly keeps Event 005's institutional GFX_portrait_KOM_mine_river_committee separate and does not substitute it into Event 006.

The current vanilla KOM flag ladder is structurally complete and hash-stable in this audit, but no accepted neutral/route provenance exists and the mod's democratic KOM flag is an Event 005 asset, not an IW-050 admission receipt.

No advisor or high-command package is authorized or present for IW-050; no advisor asset gap is being invented.

## Focus, decision, idea, and asset issues

The shared focus architecture is the accepted Event 006 scope and the five KOM helper calls are idempotent and package-guarded.

The historical focus inspect/render receipt reported 184 focuses and 196 connectors with zero crossings/intersections, but the current refresh calls failed with Transport closed; this is an engine-evidence limitation, not a new source defect.

The package decision source has one founding mission and ten serialized projects with concrete costs, cancellation, cleanup, and route effects.

The prior mission probability receipt reported an incomplete pool with 11 candidates and zero available candidates; no current typed scenario or compare is available.

The package uses existing shared icons and no unsupported placeholder flag or portrait has been promoted.

## Starting military, technology, industry, supply, and production issues

The accepted force row fixes p50 mountain_frontier, tradition 55, reinforcement mask 647, no navy inheritance, and no air inheritance.

The package setup requires exactly five reinforcement flags: independence_wave_reinforce_integrate_militias, independence_wave_reinforce_regional_guards, independence_wave_reinforce_secure_depots, independence_wave_reinforce_terrain_units, and independence_wave_reinforce_professional_officers.

The source does not add a bespoke technology or doctrine, and no package-specific production line or supply node is claimed.

Runtime equipment, manpower, train/convoy stockpile, supply, production, and current-generation force receipts are not available without a successful Event 006 transaction or live consumer validation.

## AI and playability issues

The AI source uses additive strategy factors for army, infantry/artillery/support production, infrastructure, bunker defense, former-host restraint, settled compact restraint, and emergency defense.

The prior read-only probability artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1113eb67f4cbcc233c451213f77f2001c8db81927f0163ad0793c01bb0795c7/3c7f93f637e74b4bccb1edc2c91a1d1deaaa79c2cff19d746376ad85cb1fa972/probability-inspect-78be03b0b074.json, with PROBABILITY_SOURCE_DISCOVERED, no_weighted_surfaces, and zero candidates.

The prior named empty evaluation returned PROBABILITY_SURFACE_EMPTY, so literal strategy values are not normalized probabilities and do not establish playability or balance.

The current mandatory hoi4.probability_inspect calls for ai_strategy_factor on common/ai_strategy/006_independence_wave_komi.txt and mission_ai_will_do on common/decisions/006_independence_wave_komi_decisions.txt both failed immediately with Transport closed.

The named chaosx_ai_probability_auditor route was not exposed in the installed callable tools, so no same-scenario hoi4.probability_compare was run and no quantitative claim is authorized.

No live HOI4 playability test was run by design.

## MCP evidence and limitations

The current read-only MCP attempts were:

- hoi4.map_inspect for [397,262,581]: timed out after 180 seconds.
- hoi4.map_inspect retry for [397]: exact blocker Transport closed.
- hoi4.map_render state layer with ports, victory points, resources, buildings, supply nodes, railways, and adjacencies: exact blocker Transport closed.
- hoi4.focus_inspect for common/national_focus/006_independence_wave_focus.txt, tree independence_wave_focus_tree: exact blocker Transport closed.
- hoi4.focus_render for the same source/tree: exact blocker Transport closed.
- hoi4.event_inspect for chaosx.nr6.350: exact blocker Transport closed.
- hoi4.event_render overview for chaosx.nr6.350: exact blocker Transport closed.
- hoi4.probability_inspect with ai_strategy_factor for the Komi AI source: exact blocker Transport closed.
- hoi4.probability_inspect with mission_ai_will_do for the Komi decision source: exact blocker Transport closed.

Useful earlier artifacts remain in the dated handoffs, but they are not refreshed current acceptance evidence.

The installed package has no Technology Tree Viewer, and no technology-specific source was added for IW-050.

## Meaningful validation

The current task-specific static audits passed:

- python -B .tools/audit_event6_allocator.py reported 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, 32 content attestations, 29 compatible groups, 20 static standalone witnesses, and the exact automatic ladder 3/4/5/7/10 with World Collapse 10.
- python -B .tools/audit_event6_country_api.py reported broad=242, resolved=191, Soviet=34, Africa=45, and no missing or duplicate carriers.
- python -B .tools/audit_event6_flags.py reported 102 registered Event 006 tags, 102 complete flag families, and zero incomplete families.
- python -B .tools/audit_event6_scenario_matrix.py passed all 32 SCN-008 cells and eight edge-case receipts.
- The package display-reference check found 27 decision display references, with the two nonlocal keys resolving in the shared Event 006 localisation file; no package-local missing display key was found.
- The current Komi localisation begins with UTF-8 BOM bytes and contains 65 keys.

The following meaningful validation was skipped or remains blocked:

- No live HOI4 run, save/load, event receipt, terminal receipt, or playability observation was performed.
- No current map, focus, event, or probability artifact was produced after the MCP transport closed.
- No same-scenario probability evaluation or compare was run because the named auditor route was unavailable and direct inspect could not reconnect.
- No Technology Tree Viewer evidence exists in the installed package.

## Patch and behavior change

Changed file: docs/events/006_independence_wave/komi_package.md:39.

Before, the package documentation claimed the strategic-cost tooltip showed stability, war support, command power, and factory burden.

After, it states stability, command power, convoy-or-train, and factory burden, matching can_pay_independence_wave_komi_strategic_cost in common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:51-55, the shared payment effect in common/scripted_effects/006_independence_wave_decision_effects.txt:199-214,350-353, and the package localisation in localisation/english/006_independence_wave_komi_l_english.yml:55-57.

No gameplay or admission behavior changed in this audit.

The working tree also contains an unrelated concurrent one-line diff in common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:51-55 removing the war_support_minor affordability condition; that diff was not authored, reverted, or folded into this audit.

## Exact remaining gates and required evidence

1. Parent-owned identity clearance must publish independence_wave_iw_050_identity_rights_cleared only after the exact 1936 leader or institution source, rights/provenance packet, portrait-worker archive, and portrait consumer review are complete.
2. The flag owner must provide stabilized vanilla KOM ladder hashes plus an accepted identity/origin reuse decision, or a sourced route-specific flag packet with GFX/manifest evidence; do not use Event 005 committee imagery or generated grounded portraits as substitutes.
3. The map owner must refresh MCP inspect/render for states 397, 262, and 581, the actual former-host remnant, ownership/controller/capital, supply/rail/port/building geometry, and the reservation group without allocation writes.
4. The weighted-logic owner must run the mandatory chaosx_ai_probability_auditor route with typed Komi setup, host, cost, mission, and AI scenarios, then perform the same-scenario hoi4.probability_compare; no literal AI factors may promote the package.
5. Only after package-local identity, flag, portrait, map, force, cleanup, and typed probability evidence is accepted may the parent add iw_050 to central adapter, content-attestation, setup/final-validation/cleanup dispatch, normal/SCN-008 preflight, and deterministic Join surfaces.
6. After central wiring, the parent must run focused Event MCP inspect/render for chaosx.nr6.350, package setup/final-validation state flow, terminals, and the no-country branch before considering admission.
7. The parent must retain the Event 005 Soviet-origin boundary and verify Event 005-first/Event 006-first collisions, living-tag rejection, optional-extension trimming, and protected-host remnant preservation.
8. If future IW-050 technology inheritance or doctrine claims are introduced, report the missing Technology Tree Viewer route instead of substituting source-only evidence.

## Simplifications, omissions, and blockers

No fallback identity, generic portrait, generated grounded portrait, invented flag, central adapter, central attestation, Join path, bespoke focus tree, formable promotion, technology evidence, or live runtime claim was substituted.

The only completed patch is the narrow package-documentation wording correction described above.

The package is not admitted, and the Event 006 whole-event HOLD/PARTIAL boundary remains unchanged.

Plan handoff path: docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw050_komi_admission_audit_current_2026_08_24.md.

