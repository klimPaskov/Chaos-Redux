# Event 006 IW-057 FER country package audit — 2026-08-31

## Scope and disposition

This is a bounded source audit of the Far Eastern Republic package `IW-057`, tag `FER`, covering country identity, history and characters, anchors, forces, ideas, focus callbacks, decisions and mission logic, AI, localisation, visual assets, cleanup, and the central Event 006 admission path.

Disposition: **HOLD / PACKAGE-LOCAL SOURCE PRESENT / CENTRAL ADMISSION BLOCKED / NO GAMEPLAY PATCH**.

The only file changed by this audit is this handoff; no FER gameplay file, shared registry, map file, asset, or gate was edited, and nothing was staged or committed.

## Accepted specification and identity receipt

The accepted registry row in `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:58` assigns `IW-057` to the Far Eastern Republic with registered tag `FER`, region `Volga, Urals, Siberia, and Far East`, archetype railway-and-port republic, ordered anchors `408|409`, anchor names Vladivostok and Khabarovsk, and reservation group `RG-408-409`.

The accepted research row in `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` requires the registered tag to remain unused, a defensible period leader or authentic institution, a source-cleared identity flag, and a compact release anchor after rebinding to the installed map.

The accepted reservation row in `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv` reserves `408|409` only when the candidate tag is not living and host protection succeeds; public 763-state IDs must be rebound to the installed map before runtime use.

The regional overlay in `docs/specs/006_independence_wave_specs/matrices/006_regional_overlay_matrix.csv:6` requires rail, river, distance, extraction, frontier, and multiethnic constraints and forbids flattening distinct peoples or granting large empty territory automatically.

The force mapping in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:58` assigns `regular_defectors`, tradition `67`, separate railway-port headquarters, defecting regulars, railway troops, coastal guards, and five reinforcement paths.

The package research and identity addendum `docs/plans/006_independence_wave_plans/006_iw057_fer_identity_roster_symbol_receipt_addendum_2026-08-15.md` remains research-only for proposed Nikiforov/Krasnoshchyokov identity candidates, portrait IDs, and flag candidates; it does not authorize runtime wiring.

## Country package coverage checklist

| Surface | Status | Evidence and finding |
|---|---|---|
| Tag and country shell | Partial, source present | Vanilla registers `FER = "countries/Fareastern Republic.txt"` in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\country_tags\00_countries.txt:224`; the mod only adds the separate Event 005 `FEV` shell in `common/country_tags/chaosx_countries.txt:31`. |
| Event 006 identity | Blocked | No accepted FER Event 006 identity receipt, neutral runtime flag, cosmetic tag, or central package admission exists. |
| History and starting setup | Source context present | Vanilla `history/countries/FER - Far Eastern Republic.txt` uses capital `563` (Chita), three research slots, vanilla technology, democratic elections, and no OOB; the package intentionally releases against ordered anchors `408|409` instead of treating dormant historical state `563` as a runtime anchor. |
| State anchors and host safety | Package guards present, engine proof pending | `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt:34-111` requires owned and controlled `408` or `409`, a capital anchor, protected former-host state, and the package region/depth/archetype. |
| Characters and roster | Blocked | No FER Event 006 character or portrait consumer exists; `has_independence_wave_fer_command_roster` only accepts parent-owned flags `independence_wave_iw_057_identity_rights_cleared` and `independence_wave_iw_057_command_roster_ready` at `...far_eastern_package_triggers.txt:113-118`. |
| Politics and routes | Source present | `...far_eastern_package_effects.txt:160-272` installs four local routes: constitutional autonomy, railway charter, coastal councils, and coastal emergency command. |
| Focus integration | Source present, engine refresh blocked | The shared tree calls five FER-owned callbacks at `common/national_focus/006_independence_wave_focus.txt:142,195,229,1461,1732`; this shared file has concurrent edits and was not touched. |
| Decisions and mission | Source present | `common/decisions/006_independence_wave_far_eastern_decisions.txt` contains the 420-day founding mission `independence_wave_fer_hold_railway_council` and ten serialized projects. |
| Ideas | Source present | `common/ideas/006_independence_wave_ideas_registry.txt:1221-1298` contains seven FER ideas with package rights gates and shared Event 006 icons. |
| Forces and technology | Source present, engine proof pending | Force profile `p57`, `regular_defectors`, tradition `67`, reinforcement mask `590`, and both navy/air inheritance bits are registered in `common/script_constants/006_independence_wave_constants_registry.txt`; vanilla FER history supplies the starting technology baseline but no OOB. |
| AI | Source present, probability audit blocked | Four FER strategies exist in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:589-657`; two settled/emergency strategies omit setup and current-generation guards, but no weight patch is safe without the required probability baseline/compare. |
| Localisation | Package keys present, identity keys intentionally absent | `localisation/english/006_independence_wave_far_eastern_l_english.yml` covers package parties, ideas, mission, projects, callbacks, and cost/tooltips; no leader, flag, or cosmetic-name keys can be accepted before identity receipts. |
| Flags, portraits, and manifests | Blocked | No FER Event 006 flag, portrait, `.gfx` sprite, or runtime manifest entry exists; installed vanilla ideology flags and Event 005 FEV assets are not valid substitutes. |
| Cleanup | Package-local source present | `...far_eastern_package_effects.txt:449-497` removes the mission, projects, ideas, local ledgers, route flags, and local roster marker and restores vanilla FER politics; the parent-owned identity-rights receipt is intentionally not cleared. |

## File surface checklist

The package-local source surfaces inspected were `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt`, `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt`, `common/decisions/006_independence_wave_far_eastern_decisions.txt`, `common/decisions/categories/006_independence_wave_categories.txt`, `common/ideas/006_independence_wave_ideas_registry.txt`, `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, and `localisation/english/006_independence_wave_far_eastern_l_english.yml`.

The shared source surfaces inspected without editing were `common/national_focus/006_independence_wave_focus.txt`, `common/scripted_effects/006_independence_wave_effects.txt`, `common/scripted_effects/006_independence_wave_join_effects.txt`, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`, `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt`, `common/scripted_effects/006_independence_wave_force_package_effects.txt`, `common/script_constants/006_independence_wave_constants_registry.txt`, and `common/scripted_effects/006_independence_wave_scenario_effects.txt`.

The source scan found no runtime FER entries in `common/characters`, `history/general`, `interface/006_independence_wave_portraits_registry.gfx`, `gfx/flags`, or `gfx/leaders/006_independence_wave`; proposed IDs such as `FER_independence_wave_pyotr_nikiforov`, `GFX_portrait_FER_independence_wave_pyotr_nikiforov`, and `FER_INDEPENDENCE_WAVE_PROVISIONALX` occur only in research documentation.

## Map and state setup

Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\408-Vladivostok.txt` is a coastal town with a value-15 Vladivostok victory point, infrastructure, dockyard, airbase, naval base, coastal bunkers, naval supply hub, chromium, and cores for `SOV`, `FER`, and `VLA`.

Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\409-Khabarovsk.txt` is a connected inland/riverside anchor with infrastructure, an industrial complex, airbase, naval base, chromium, and cores for `SOV`, `FER`, and `VLA`.

Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\563-TS 5.txt` is Chita, the vanilla FER historical capital with steel, chromium, infrastructure, airbase, and `SOV`/`FER` cores; the local runtime gate deliberately excludes this dormant state from the `408|409` release identity check.

The source-level anchor ordering is coherent with the accepted railway-port identity, but no current map MCP inspection was available, so adjacency, supply, railway, port, controller, and installed-map collision safety remain unproven for this turn.

## Politics, leaders, portraits, flags, advisors, and parties

The four local route installers set the intended ideology, elections, popularity, party names, route ideas, route flags, and ledger changes, while `independence_wave_fer_restore_vanilla_politics` restores democratic elections and vanilla-like popularity values during cleanup.

Localisation covers `FER_independence_wave_constitutional_party`, `FER_independence_wave_socialist_party`, `FER_independence_wave_railway_charter_party`, and `FER_independence_wave_emergency_party` plus their long names.

There is no FER Event 006 leader, advisor, high command, commander, character registry entry, portrait sprite, or gender/name metadata; the parent-owned roster flags are a receipt gate, not evidence that a character consumer exists.

The strongest researched human candidate is Pyotr Mikhailovich Nikiforov, but the source and portrait handoffs remain unaccepted and the Commons public-domain assertion is not independent legal clearance; the researched FER passport is institutional and cannot be used as a human leader portrait.

The strongest researched flag candidate is `FER-H0-1920-FLAG`, but its reconstructed CC-BY-SA source has unresolved underlying rights and is not a neutral 1936 runtime identity; no synthetic substitute or Event 005 FEV asset is authorized.

## Focus, decision, mission, idea, and asset surfaces

The shared focus callbacks are `independence_wave_fer_focus_convene_railway_council`, `independence_wave_fer_focus_secure_railway_ports`, `independence_wave_fer_focus_integrate_coastal_guards`, `independence_wave_fer_focus_settle_former_host_ledgers`, and `independence_wave_fer_focus_open_pacific_corridor`; aliases for secure communities and the Ural corridor are package-local helper names.

The ten project IDs are `independence_wave_fer_secure_railway_ports`, `independence_wave_fer_integrate_coastal_guards`, `independence_wave_fer_register_fer_communities`, `independence_wave_fer_settle_former_host_ledgers`, `independence_wave_fer_ratify_constitutional_autonomy`, `independence_wave_fer_adopt_railway_charter_compact`, `independence_wave_fer_convene_coastal_councils`, `independence_wave_fer_establish_coastal_emergency_command`, `independence_wave_fer_codify_durable_sovereignty`, and `independence_wave_fer_open_pacific_corridor`.

The founding mission and projects have current-generation, capital, anchor, route, host, network, cancellation, cost, duration, and tooltip checks in source; no package-specific GUI is expected by the accepted design.

The seven starting/lifecycle ideas are `fer_fragmented_railway_mandate`, `fer_railway_compact`, `fer_railway_council_charter`, `fer_coastal_councils`, `fer_community_register`, `fer_railway_charter_compact`, and `fer_coastal_emergency_command`.

The ideas intentionally reuse registered Event 006 icon definitions, so no icon gap was found; the absence of FER portraits, flags, and `.gfx` entries is an identity gate failure rather than an asset substitution opportunity.

## Starting military, technology, industry, supply, and production

The accepted force mapping is `regular_defectors` with profile `p57`, military tradition `67`, reinforcement mask `590` for regional guards, secure depots, defecting-host conversion, factory/railway guards, and professional officers, and inheritance mask `3` for navy and air assets.

`common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt:365-435` invokes the generic generation-safe force applier only after the parent roster receipt and local setup conditions pass; it does not create an unverified character or bypass the central package gates.

The vanilla FER history provides infantry, engineer, mountaineer, truck, mass-assault, and new-fleet-in-being technology context and three research slots, while the 408/409 source states provide a narrow port-and-rail industrial spine and the local ledger ideas model fragmented or compact logistics.

No package-local OOB, major army expansion, unsupported equipment, or broad balance change was found or added.

## AI and playability

`independence_wave_fer_railway_port_survival` correctly targets army, infantry/artillery/support production, infrastructure, and bunkers under the package/setup/profile conditions.

`independence_wave_fer_host_restraint` correctly limits starting wars while a living former host remains unsettled.

`independence_wave_fer_settled_compact` checks compact stabilisation but omits setup and current force-generation guards, and `independence_wave_fer_coastal_emergency_guard` checks emergency government but likewise omits setup and current-generation guards.

These are weighted AI strategy surfaces, so changing them requires the mandatory `chaosx_ai_probability_auditor` baseline and same-scenario `hoi4.probability_compare`; the required custom auditor and current probability route are unavailable in this runtime, and no weight patch was made.

## Central admission, attestation, Join, runtime adapter, and cleanup gates

`common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1158-1235` and `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:477-490` contain planning metadata for `iw_057`, `RG-408-409`, region 05, and registered tag `FER`; planning metadata is not runtime admission.

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` has no `iw_057` runtime-adapter branch, and `:159-202` has no `iw_057` attestation branch.

The normal and SCN-008 preflights in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-568` contain no exact FER/IW-057 branch, so the package remains fail-closed.

The central setup, final-validation, and cleanup dispatchers in `common/scripted_effects/006_independence_wave_effects.txt:3631-3736` do not call `independence_wave_dispatch_fer_package_setup`, `independence_wave_validate_fer_package`, or `independence_wave_cleanup_fer_package`.

The deterministic Join candidate sequence in `common/scripted_effects/006_independence_wave_join_effects.txt:234-271` ends before `iw_057` and therefore cannot admit this package.

These are shared central surfaces outside the permitted FER-local patch boundary and must be resolved by the parent event owner only after identity, rights, roster, neutral flag, route-leadership, and typed-probability receipts are accepted.

## Required HOI4 MCP evidence and blockers

Fresh read-only HOI4 MCP calls were attempted for the focus route, but `hoi4.focus_inspect` returned the exact runtime error `MCP tool hoi4_agent_tools/hoi4.focus_inspect is not available to the model`; the current callable inventory likewise exposes no callable `hoi4.focus_render`, `hoi4.event_inspect`, `hoi4.map_inspect`, `hoi4.tech_inspect`, or `hoi4.probability_inspect` functions.

The required custom `chaosx_ai_probability_auditor` route is not callable in the current runtime, so no new probability baseline, scenario evaluation, or comparison can be claimed.

The installed package exposes no Technology Tree Viewer, which remains an unresolved limitation for the technology dependency surface.

Prior retained artifacts are useful only as historical evidence: the 2026-08-27 focus inspection reported 184 focuses, 195 connectors, and zero geometry diagnostics at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb255e65e6922a662a4117cfdc0e1151a033bb5a87b6e36b523d7555324a3dc0/a96838d016ce3d609f9859316171f8c101c8d35db4b1b7e69961eaa455e78ed8/focus-inspect.9887d2c9efb1cba6.json`, while the prior map and technology routes failed with `ARTIFACT_MANIFEST_INTEGRITY_FAILED`.

The prior Event 006 root scan/render artifacts at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9bf23d701573bac86f105977a459bb0705579027f4f876cbbfdd53f7589f88d5/0dc5d2a6fcb677c1ff97bc296a234eab8f6305e2bdea00a4492d4da41e539f7c/event-scan-f4498b37c697.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f9a8382c23a63b7443f80df272cb5d3956526b47f2b7a481e7edd10f9575d03b/b0df8a36f5aa42042a74a9ee9c3c94a55f2c557b7a826143a93f74cf880ef1a0/event-overview-f4498b37c697-manifest.json` are root Event 006 evidence, not proof of an admitted FER package.

No map write, live game run, save/load test, or Technology Tree Viewer claim was made.

## Next owner and acceptance work

The parent event owner should first obtain accepted identity-rights, leader-or-institution roster, portrait provenance/runtime, neutral flag, and route-leadership receipts for `FER`, then add the central adapter, attestation, normal/SCN-008 preflight, setup/final-validation/cleanup dispatch, and deterministic Join branches in shared files.

After central admission is accepted, the parent should rerun focus, event, map, and probability MCP routes, perform the required same-scenario AI probability compare for the two under-guarded FER strategies, and validate the 408/409 reservation against the installed map.

## Simplifications, omissions, and uncertainty

No fallback identity, invented leader, synthetic flag, generic portrait, generic focus tree, gate relaxation, central registry edit, AI weight change, map write, or major balance change was used.

The package is intentionally incomplete and not runtime-admissible until the blockers above are resolved; source presence must not be reported as engine-validated package availability.
