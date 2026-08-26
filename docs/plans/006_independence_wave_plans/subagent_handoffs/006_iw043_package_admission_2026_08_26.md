# Event 006 IW-043 CHU package admission audit — 2026-08-26

Reviewer: `/root/event6_chu_package_admission`.

Scope: bounded audit of `IW-043` Volga Bulgaria on the reused vanilla `CHU` carrier, including its accepted research/spec gates, country identity and history, state anchors, leaders and portraits, flags and symbols, forces and ideas, visible focus/decision/event mechanics, AI and diplomacy, host/region/formable routes, central adapter/attestation/dispatch/capacity/Join registries, and task-specific validators.

## Verdict

**HOLD / fail-closed. IW-043 is not safe for central admission.**

No central admission patch was applied.

The current authority explicitly keeps `IW-043 CHU` in the adapter-only set. The package has substantial source-local gameplay and registry wiring, but the central content-attestation gate, automatic capacity dispatch, and deterministic Join order intentionally omit `IW-043`. The grounded portrait/source-rights roster is also not fully admission-ready. Promoting the package now would bypass the accepted sourced-roster and two-gate admission contract.

No gameplay, central registry, asset, localisation, map, or spreadsheet file was changed by this audit. Only this handoff was added. No file was staged or committed.

## Accepted authority and research gates

| Gate | Current evidence | Disposition |
| --- | --- | --- |
| Package research | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:44` resolves `IW-043` as Volga Bulgaria on `CHU`, `high_chaos_only`, anchors `249|256`, reservation group `RG-MIDDLE-VOLGA-KAZAN`, and modern Volga congress leadership. | Accepted design direction. |
| Identity research | `docs/specs/006_independence_wave_specs/research/006_signature_country_research_dossiers.md:7-19` requires a modern Middle Volga congress, later Volga Bulgaria restoration, compact Bolgar-Kazan anchor, modern civic seal opening, and no settled reconstructed medieval flag. | Source direction present; does not grant runtime admission. |
| State/reservation research | `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:95` binds `RG-MIDDLE-VOLGA-KAZAN` to `249|256`, package IDs `IW-043|IW-044|IW-046|IW-047`, capacity `1`, and reserve-host-first semantics. | Accepted; shared group and CHU mutex remain required. |
| Country package design | `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md:76-90` defines the CHU package, rights/river-security routes, forces, central politics, FORM-12/13, cleanup, and exact mutually exclusive proof writers. | Source tranche implemented, admission still gated. |
| Research acceptance | `docs/specs/006_independence_wave_specs/quality/research_acceptance_checklist.md:28` and `research_validation_report.md:37-40` require CHU package flags and mutual exclusion between `IW-043` and `IW-046`. | Structurally present. |
| Current package authority | `docs/specs/006_independence_wave_specs/quality/package_manifest.md:11,27,115` and `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:391` keep `IW-043` adapter-only and fail-closed in the current `32` attested / `29` group / `40` adapter / `161` unattested boundary. | Blocking current authority. |

The older package paragraphs that call CHU admitted are superseded and were not used as authority.

## Country package coverage checklist

| Surface | Current status | Evidence and identifiers |
| --- | --- | --- |
| Carrier/tag | Source-present, reused vanilla carrier | No mod `common/countries/CHU` or `history/countries/CHU` is present; the package uses `original_tag = CHU`, exact package ID `iw_043`, package flag `independence_wave_package_iw043_volga_bulgaria`, and `liberation_origin.independence_wave` in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:19-37`. |
| Identity/mutex | Source-present and fail-closed | `is_independence_wave_iw043_country`, `is_independence_wave_exact_package_iw_043_tag_available`, `has_valid_independence_wave_chu_package_mutex`, and `..._for_setup` require exact CHU/package/flag agreement and reject simultaneous `IW-043`/`IW-046`. |
| Vanilla history | Preserved | Vanilla `history/countries/CHU - Chuvashia.txt` retains `capital = 256`, `set_research_slots = 3`, vanilla 1936 politics, technologies, doctrines, and `CHU_gerasim_ivanov`. No replacement history was added. |
| State anchor | Source-present, live proof absent | Region loader `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:882-892` saves CHU and state `249`; package setup/validation uses compact anchor `249` and optional Cheboksary `256`. `RG-MIDDLE-VOLGA-KAZAN` capacity is one. |
| Host/origin | Source-present, runtime receipt absent | `can_initialize_independence_wave_iw043_package` and the shared planner require prepared Event 006 origin, saved anchor/former-host targets, state `249` ownership/control and capital conditions, signature depth, region, river/corridor archetype, and CHU mutex. No live transaction or save/load evidence is claimed. |
| Politics/parties | Source-present | `independence_wave_apply_iw043_political_surface` in `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:126-224` defines opening democratic politics and route-specific federal, restoration, popular, traditional, patron, and emergency party surfaces. |
| Institutional leaders/characters | Source-present, roster admission partial | Four male civilian-large character consumers are defined in `common/characters/006_independence_wave_characters_registry.txt:282-319`: `CHU_independence_wave_middle_volga_congress`, `...federal_presidium`, `...bolgar_civic_presidium`, and `...river_security_directorate`. Recruitment is in `history/general/006_independence_wave_character_recruitment_registry.txt:75-81`. Institutional names are fixed sourced role identities, not opposite-gender random pools. |
| Leader traits | Source-present | `common/country_leader/006_independence_wave_leader_traits_registry.txt:38-62` defines four non-random IW-043 traits for congress, federal, Bolgar, and river-security roles. |
| Portraits | Blocking admission gate | The four runtime basenames and GFX sprites exist in `interface/006_independence_wave_portraits_registry.gfx:167-180` and `gfx/leaders/006_independence_wave/`. Runtime file presence is not attestation. Galimzhan Ibrahimov federal-presidium v2 is parent-promoted to the existing DDS; Luka Semyonovich Spasov v45 has a bounded visual/provenance pass and post-wire receipt; Mirsaid Sultan-Galiev remains rights/source-gated; Karim Tinchurin v3 remains rights/date `needs_user_review` because the 1937 NKVD source is outside the accepted baseline. No portrait evidence admits CHU. |
| Flag/symbol identity | Source-present, admission still blocked | Cosmetic IDs `CHU_independence_wave_middle_volga_congressX`, `CHU_independence_wave_volga_bulgariaX`, and `CHU_independence_wave_volga_federationX` are in `common/countries/006_independence_wave_formable_cosmetics.txt:46-60`; normal/medium/small TGA families are present under `gfx/flags/`. Accepted research calls the opening a modern civic seal and the Bolgar route a sourced archaeological/Tatar-Muslim motif, not a settled medieval flag. |
| Advisors/high command | Intentionally absent | No custom Event 006 advisor icons, advisor portrait/sprite blocks, or CHU advisor consumers are authorized. The force package uses a collective Middle Volga defence commission rather than an invented khan or single-community commander. |
| Forces | Source-present | `IW-043` row in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` binds CHU to `river guards, cavalry, defecting units`, `river_jungle`, military tradition `62`, no navy/air inheritance, and the accepted reinforcement mask. `common/scripted_effects/006_independence_wave_force_package_effects.txt` loads/applies the p43 mapping and records force receipts. |
| Ideas | Source-present | `common/ideas/006_independence_wave_ideas_registry.txt:2275-2365` defines congress, federal charter, Bolgar constitution, emergency navigation, disrupted/reopened river economy, provisional/civilian/emergency river guard ideas. Icons are wired through the consolidated small-assets registry. |
| Starting setup | Source-present, runtime proof absent | `independence_wave_setup_iw043_middle_volga` in `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1263-1381` initializes ledgers, ideas, force receipts, package identity, focus framework, routes, formable family, and opening event after exact mapping/anchor gates. |
| Focus | Source-present, MCP render blocked | `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` provides `23` package focus IDs as a shared-focus extension attached to `independence_wave_focus_tree`; route mutexes and FORM-12/13 capstones are explicit. The extension file is not itself a standalone tree. |
| Decisions/missions | Source-present, quantitative AI proof blocked | `common/decisions/006_independence_wave_iw043_iw058_decisions.txt:17-1117,2140-2230` defines `18` IW-043 decisions across roll call, four rights clauses, river/customs, muftiate, guard, workshop, host transit, trade, FORM-12/13, reconciliation, and staged integration. Costs/timers and success/timeout/cancel paths are localised in `localisation/english/006_independence_wave_iw043_iw058_l_english.yml:301-424,569-581`. |
| Events | Source-present, structural MCP blocked | Current consolidated support registry `events/006_independence_wave_support_events.txt:1672-2217` defines `chaosx.nr006.4301` through `.4314` with CHU exact-package triggers, options, transaction effects, route locks, and cleanup-compatible dispatch. Current localisation is in `localisation/english/006_independence_wave_iw043_iw058_l_english.yml:591-820`. |
| AI/diplomacy | Source-present, probability unresolved | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:969-1097` defines foundation, reserve recovery, tracked crisis, federal, restoration, emergency, and civilian-normalization strategies with CHU exact-package/setup/route/crisis gates. Former-host transit and trade decisions are package-gated. No quantitative balance claim follows. |
| Formables | Source-present, dependent admission remains blocked | FORM-12 Volga-Ural and FORM-13 Idel-Ural adapters use exact CHU carrier, state/anchor, consent, rights, route, member, staged-integration, generation, and cleanup gates in `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt`, `...formable_registry_triggers.txt`, and paired effects. Their local proof writers do not bypass central CHU package attestation. |
| Localisation | Source-present | CHU leaders, traits, parties, cosmetic names/adjectives, ideas, decisions, events, focus names/descriptions/tooltips, route labels, and formable strings are in the consolidated IW-043/IW-058 English file. Localisation presence is not a source-rights or admission proof. |

## File surface checklist

The relevant current source surfaces are:

- `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt` for CHU identity, mutex, origin, anchor, route, and setup/final-validation predicates.
- `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt` for political, institutional, cosmetic, force, setup, validation, and cleanup effects.
- `common/scripted_effects/006_independence_wave_iw043_iw058_focus_effects.txt` for focus completion and route proof writers.
- `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` for the `23` IW-043 shared-focus nodes.
- `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` for the `18` package decisions and staged FORM-12/13 actions.
- `events/006_independence_wave_support_events.txt` for `chaosx.nr006.4301`-`.4314` after the 2026-08-26 registry consolidation.
- `common/characters/006_independence_wave_characters_registry.txt` and `history/general/006_independence_wave_character_recruitment_registry.txt` for the four CHU institutional character consumers.
- `common/country_leader/006_independence_wave_leader_traits_registry.txt` for the four IW-043 leader traits.
- `common/ideas/006_independence_wave_ideas_registry.txt` for the nine IW-043 idea definitions.
- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` for the seven CHU strategy layers.
- `common/countries/006_independence_wave_formable_cosmetics.txt` and `gfx/flags/{,medium,small}/` for route cosmetic identities and flag families.
- `interface/006_independence_wave_portraits_registry.gfx` and `gfx/leaders/006_independence_wave/` for the four portrait consumers.
- `interface/006_independence_wave_small_assets.gfx` and `gfx/interface/{goals,ideas,decisions}/006_independence_wave/volga_assyria/` for focus, idea, and decision sprites.
- `localisation/english/006_independence_wave_iw043_iw058_l_english.yml` for the package text surface.
- `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:882-892` and `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:381-388` for region loading and candidate planning.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` for central adapter, attestation, normal preflight, and scenario preflight.
- `common/scripted_triggers/006_independence_wave_triggers.txt` for central capacity dispatch.
- `common/scripted_effects/006_independence_wave_join_effects.txt` for deterministic Join probes/order.
- Vanilla `history/countries/CHU - Chuvashia.txt` for the preserved carrier history.

## Central admission and registry findings

| Registry | Finding | Result |
| --- | --- | --- |
| Runtime adapter | `has_independence_wave_runtime_package_adapter_for_execution_id` includes `constant:independence_wave_package_id.iw_043` at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63`. | Adapter exists. |
| Content attestation | `has_independence_wave_runtime_package_content_attestation_for_execution_id` at `...package_dispatch_triggers.txt:159-202` contains no `iw_043`. | **Blocking omission by design.** |
| Normal preflight | `is_independence_wave_runtime_package_preflight_ready` requires adapter **and** content attestation before its exact package/tag branch at `...package_dispatch_triggers.txt:207-311`. | CHU cannot pass while attestation is absent. |
| Scenario preflight | `is_independence_wave_scenario_package_preflight_ready` requires the same content attestation before the visible IW-043 exact-tag branch at `...package_dispatch_triggers.txt:411-520`. | SCN-008 cannot select CHU. |
| Region loader | `independence_wave_load_package_iw_043` exists and loads signature depth, river/corridor archetype, high-chaos disposition, CHU, and anchor `249`. | Local candidate/loader source is present. |
| Candidate planning | `can_plan_independence_wave_package_iw_043` and `independence_wave_prepare_weight_iw_043` exist in the region registries and require high-chaos disposition plus anchor/group availability. | Planner surface is present but central reservation rechecks attestation. |
| Reservation | `independence_wave_reserve_package_iw_043` calls shared `independence_wave_begin_package_reservation`, which rejects non-attested execution IDs before reservation. | No safe admission shortcut exists. |
| Capacity | No `independence_wave_liberations_capacity_try_iw_043` exists in `common/scripted_triggers/006_independence_wave_triggers.txt`; the central call list includes IW-044 but not IW-043. | **Blocking omission.** |
| Join | `common/scripted_effects/006_independence_wave_join_effects.txt:213-247` has no `independence_wave_join_candidate_id = ...iw_043` entry. | **Blocking omission.** |
| Shared CHU collision | CHU is intentionally shared by IW-043 and IW-046; `RG-MIDDLE-VOLGA-KAZAN` capacity is one and package flags/mutexes prevent both identities in one generation. | Must remain unchanged if later admitted. |
| FORM-12/13 | Exact CHU carrier and member/anchor/consent writers are present, but they are downstream of package setup and do not grant central admission. | Operational local adapter, not admission proof. |

The static source check performed during this audit returned `adapter=True`, `content_attestation=False`, `capacity_try=False`, `join_order=False`, and `region_loader=True` for IW-043.

## Map and state setup issues

The accepted map contract is coherent at source level: vanilla CHU starts at state `256` (Cheboksary), IW-043 reserves state `249` (Kazan) as its compact anchor and capital after setup, and state `256` is the optional extended member in `RG-MIDDLE-VOLGA-KAZAN`. The package must reserve the protected host before this one-capacity group and must never let CHU/IW-046 share the same generation.

No state transfer, owner/controller change, railway, port, supply-node, resource, building, victory-point, or adjacency mutation is present in the IW-043 package source. The map MCP inspection for states `249` and `256` was attempted but returned `Transport closed` after the service timeout path, so installed-map geometry and runtime ownership/control are not claimed here.

## Starting military, technology, industry, supply, and production issues

| Area | Current finding | Admission impact |
| --- | --- | --- |
| Military | p43 maps to river guards, cavalry, and defecting units with tradition `62`; the package records force mapping/application/current-generation receipts and permits the accepted militia, depot, defector-conversion, terrain-unit, and professional-officer reinforcement paths. | Source-present; no live force receipt. |
| Technology/doctrine | No IW-043 custom technology or doctrine is defined. Vanilla CHU retains its starting research slots, infantry/support baseline, and mass-assault/new-fleet-in-being doctrine history. | Preserved carrier baseline; technology MCP route unavailable. |
| Industry | Setup and route decisions use the package's civilian capacity, workshop, infrastructure, and industrial effects; no broad factory or major-balance expansion was added by this audit. | Source-present; no live production proof. |
| Supply/transport | The package uses river-control, ferry/customs, rail, train, convoy, and supplied-formation gates, with disrupted/reopened river-economy ideas and route-specific supply modifiers. | Source-present; no live supply-network proof. |
| Production/manpower | Decisions and force setup consume explicit command power, manpower, equipment, train, convoy, and civilian-factory commitments from package constants/localisation; no unbounded stockpile grant is present. | Source-present; probability/runtime receipt unavailable. |

## Missing or stale package surfaces

1. The central compile-time content attestation is intentionally missing for `IW-043`; this is the decisive admission blocker.
2. Central automatic capacity and deterministic Join entries are absent because the package is not attested; adding them without a full package audit would create an unsafe partial admission.
3. Portrait runtime basenames exist, but source evidence and rights status are not uniform. The four-consumer roster must not be inferred from DDS/GFX presence.
4. Mirsaid Sultan-Galiev evidence remains rights/source-gated; the independent visual audit is not a legal or central admission approval.
5. Karim Tinchurin v3 has visual/style/provenance PASS with a source-resolution caveat but rights/date `needs_user_review` for a 1937 NKVD source outside the accepted 1936 baseline; no DDS/GFX/admission promotion is authorized.
6. Galimzhan Ibrahimov federal-presidium v2 is promoted to the existing CHU DDS consumer, but that single consumer does not admit the package.
7. Luka Semyonovich Spasov v45 has a bounded visual/provenance pass and a post-wire receipt for the river-security consumer, but that single consumer does not admit the package.
8. No custom advisor/high-command portrait or icon is missing from an accepted surface; none is authorized for this package.
9. The current focus extension is not independently renderable as a standalone tree. It depends on `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt`.

## MCP evidence and exact blockers

The installed HOI4 MCP workspace was `mod_chaos_redux_ea3b2d67c2c0`.

- `hoi4.focus_inspect` on the IW-043 extension with `treeId = independence_wave_focus_tree` returned `FOCUS_TREE_NOT_FOUND`; the extension contains shared focuses rather than a standalone tree.
- `hoi4.focus_render` on the IW-043 extension returned `FOCUS_TREE_NOT_FOUND` with the exact message `The source file contains no focus tree`.
- A corrected `hoi4.focus_inspect` on `common/national_focus/006_independence_wave_focus.txt` timed out after `180s`; no artifact was returned.
- `hoi4.event_inspect` on `chaosx.nr006.4301` and on the consolidated support file both timed out after `180s`; no current event artifact was returned.
- `hoi4.map_inspect` for states `249` and `256` first entered the service timeout path and then returned `Transport closed`; no map artifact was returned.
- `hoi4.map_render` was attempted with state/owner/controller/region-relevant overlays in the same service call and did not return an artifact before the transport closed.
- `hoi4.tech_inspect` and `hoi4.tech_render` were attempted read-only; both returned `Transport closed`. No IW-043 custom technology or doctrine dependency was found in source, and vanilla CHU starting technology/doctrine remain the preserved carrier baseline.
- `hoi4.probability_inspect` was attempted for `ai_strategy_factor`, `national_focus_ai_will_do`, and `decision_ai_will_do`; all returned `Transport closed`.
- The required custom `chaosx_ai_probability_auditor` route is not exposed in this runtime's callable tool list. Direct probability MCP calls therefore cannot be treated as the mandatory auditor pass, and no quantitative AI/balance claim is made.
- No Technology Tree Viewer is exposed by the installed package. This remains an unresolved required-tool limitation, not a claim that technology rendering passed.

The prior Event 006 structural MCP receipts in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_current_whole_event_completion_audit_2026_08_13.md:116-120` and `006_event6_focus_geometry_closure_current_2026-08-25.md` are broader dated baseline evidence, not a current CHU-specific admission receipt. They do not override the current fail-closed authority.

## Validation run

Fresh read-only repository validators were run from the mod root on 2026-08-26.

| Command | Result |
| --- | --- |
| `python -B .tools/audit_event6_allocator.py` | PASS; `149` publishers, `126` automatic/high-chaos selectable packages, `138` SCN-008 ranked packages, `40` adapters, `32` attestations, `29` compatible groups, static standalone witness `20`, and ladder `3/4/5/7/10`; output explicitly lists `IW043` among adapter-only fail-closed IDs. |
| `python -B .tools/audit_event6_country_api.py` | PASS; `242` broad rows, `191` unique carriers, `0` missing, `0` duplicates, IW-031 crosswalk pass. |
| `python -B .tools/audit_event6_flags.py --strict` | PASS; `102` registered Event 006 tags, `102` complete flag families, `0` incomplete families. This validates the global flag registry, not CHU admission. |
| `python -B .tools/audit_event6_form16.py` | PASS for the unrelated admitted ARM/GEO/AZR FORM-16 contract; it is not CHU admission proof. |
| `python -B .tools/audit_event6_scenario_matrix.py` | PASS for all `32` SCN-008 cells and `8` declared edge cases; the matrix validates shared scenario contracts, not an unattested CHU selection. |
| `python -B .tools/audit_event6_gui_matrix.py` | PASS for the shared Statehood Ledger source matrix; runtime rendering and save/load are not claimed. |

No live game, save/load, release transaction, map rewrite, or player-observed runtime validation was performed.

## Smallest implementable next step

Complete the independent CHU sourced-roster admission package before touching central registries.

1. Resolve source rights/date/role acceptance for the complete required CHU institutional roster, retaining the current institutional role mapping and no unapproved fallback.
2. Route the completed portrait package through the required independent portrait and country-package audits, including final-vs-placeholder/runtime basename evidence and archive/runtime separation.
3. Re-run the package-specific source, localisation, focus, event, map, formable, and cleanup audits with the MCP structural routes available.
4. Run the mandatory `chaosx_ai_probability_auditor` baseline/evaluate/compare pass for strategy, focus, and decision weighting under named IW-043 scenarios; no direct source arithmetic substitutes for this route.
5. Only after those gates pass should the parent apply one reviewed central attestation entry, then add the matching central capacity and Join surfaces with the same CHU mutex/reservation group and compare/post-validation evidence.

## Simplifications, omissions, and blockers

- No gameplay simplification or fallback was introduced.
- No central admission patch was attempted because the package is not complete enough for admission.
- No RunPod was operated and no user-supplied grounded portrait final was assumed.
- MCP focus/event/map/technology/probability routes were attempted but are unresolved due the exact errors above.
- The required custom probability auditor is unavailable in this runtime.
- The installed Technology Tree Viewer is unavailable.
- No live/save-load claim is made.

## Parent handoff

The parent should review this handoff as a **no-patch, fail-closed** result. Preserve the adapter-only status of `IW-043 CHU`, the CHU/IW-046 mutex, `RG-MIDDLE-VOLGA-KAZAN` capacity `1`, anchor semantics `249|256`, and the current `32/29/161/40` central boundary. Do not add `IW-043` to central attestation, capacity, or Join based on the local source tranche or any single portrait promotion.
