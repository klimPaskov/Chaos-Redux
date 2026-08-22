# Country-package repository-cleanup baseline for Events 001–020

Date: 2026-08-22

Mode: read-only country-package audit. The only file created by this pass is this handoff. No gameplay, country history, localisation, flag, portrait, focus, decision, spreadsheet, interface, GUI, map, `.codex`, or `.qoder` file was edited, and no commit was made.

## Scope and verdict

This audit covers country tags, country definitions, histories, identity, loading, shared country classifiers and collections, ideas, advisors and characters, units, technology dependencies, claims, cores, AI, formables, and cleanup references owned by Events 001–020.

Events 021 and later were not audited as event implementations. Their event files were only reference-scanned for direct use of shared country registries or helpers, as required by the parent task.

No interface layout or coordinate inspection or recommendation is included.

The shared and Events 001–020 country source is mostly internally coherent. The read-only checks found no duplicate registered country-tag definitions, no missing country-definition targets, no live references to the retired country-tag aliases, and no invalid static `set_capital` state IDs in the scoped static setup blocks.

No safe gameplay deletion or country-source cleanup candidate was proven by this pass. The actionable cleanup candidates are documentation or catalog authority reconciliations, while several country packages remain conditional or blocked for design, provenance, probability, engine, or live-consumer reasons.

## Required references and evidence boundary

The audit read `AGENTS.md` and the applicable Chaos Redux skills: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-comfyui`, and `chaos-redux-improvement-loop`.

The required offline Paradox wiki pages were consulted from `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding, Equipment modding, Division modding, Technology modding, State modding, Map modding, Portrait modding, and Cosmetic tag modding.

The installed vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\` was consulted for script concepts, effects, triggers, modifiers, dynamic variables, contextual localisation, collections, country creation, state transfer, `release`, `create_dynamic_country`, `set_capital`, and `transfer_state_to` precedents.

The installed HOI4 MCP exposes event, focus, map, technology, and probability routes, but no country-specific inspector and no separate Technology Tree Viewer. Event and focus routes are often workspace-heavy and returned partial projections or 180-second timeouts. Those limitations are recorded below and are not treated as source proof.

The callable-tool inventory does not contain `chaosx_country_package_auditor` or `chaosx_ai_probability_auditor`, and no collaboration/spawn route was exposed in this runtime. The mandatory probability-owner pass therefore could not be routed through the required custom auditor. Direct `hoi4.probability_inspect` output and prior handoff artifacts are retained only as bounded evidence, not as an equivalent auditor pass.

The worktree was already heavily dirty with concurrent changes owned by other agents. Those changes were preserved.

## Country-package coverage checklist

| Event | Country-linked surface | Current source result | Cleanup disposition and exact evidence |
| --- | --- | --- | --- |
| 001 Communism Spread | No new country package; shared special-country exclusion and event-log country clauses only. | No Event 001 tag, country definition, history, focus, or country-owned setup surface was found. | Retain shared classifier use. No country cleanup candidate. |
| 002 Zombie Outbreak | Fixed `ZZZ` carrier plus `create_dynamic_country` derivatives. | `common/country_tags/chaosx_countries.txt`, `common/countries/Zombie Outbreak.txt`, `history/countries/ZZZ - Zombie Outbreak.txt`, `common/national_focus/002_zombies.txt`, `common/scripted_effects/002_zombie_outbreak_effects.txt`, `common/ai_strategy/002_zombie_outbreak_ai.txt`, ideas, units, and technology files are aligned. The fixed history is a dormant bootstrap and runtime creates 20 Brainzz Horde divisions after transferring the outbreak state. | No fallback or stale fixed-tag path was found. The repeated `upgrade_economy_law = yes` calls in `events/002_zombie_outbreak.txt:65-67` appear to be deliberate law progression and were retained because no engine or precedent evidence proves them dead. Event-file MCP scan was partial; render timed out. |
| 003 The Holy Realm | Existing `TIB`, `BHU`, and `NEP` carriers become the `THR` cosmetic country. | `common/scripted_effects/003_holy_realm_effects.txt:1842-1898` sets the Holy Realm flags, `THR` cosmetic identity, neutral politics, institutional leader, cores, protection, and `load_focus_tree = THR_focus`. No new country-tag definition is required. | Carrier reuse is intentional. Do not create or delete a fixed `THR` country. No stale tag or state setup was proven. |
| 004 Random War | No new country package; shared special-country exclusion and random-war actors. | No Event 004 fixed tag, country history, or country-owned shell was found. | Retain shared exclusion behavior. No country cleanup candidate. |
| 005 Soviet Collapse | Custom breakaway and successor tags in `common/country_tags/chaosx_countries.txt`, histories, country definitions, focus trees, AI, ideas, and dynamic release helpers. | Static source checks found matching tag definitions, country files, histories, focus loaders, transfer/release helpers, and valid static capital IDs. Ancient restoration histories intentionally omit `capital` because `common/scripted_effects/005_soviet_collapse_effects.txt` assigns capitals after state transfer. Existing `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_08_09_event005_probability_completion.md` reports a named-scenario weighted audit for Event 005, while broader country/setup and focus acceptance remains conditional. | Do not “repair” omitted ancient-history capitals or delete dynamic release helpers. A current focus MCP call for `common/national_focus/005_soviet_collapse_custom_splinters.txt` timed out after 180 seconds, so no new engine-backed focus cleanup claim is made. |
| 006 Independence Wave | 102 reserved X tags, registered vanilla carriers, overlays, 206 package registry rows, dynamic allocator, country setup, formables, focus/decision/AI adapters, and cleanup. | `common/country_tags/006_independence_wave_countries.txt` documents 102 X-tag rows, 85 individual country definitions, and 17 inert parser-safe reservations. `docs/events/006_independence_wave/systems/country_registry.md` documents 206 package rows, 102 new-X reservations, 91 registered-tag reuse rows, 13 overlays without standalone tags, 193 tagged rows, and 191 unique resolved carriers. The current completion authority remains HOLD/PARTIAL: 32 content-attested selectable packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows. | Inert reservations, shared carriers, overlays, and fail-closed rows are intentional and must not be deleted. The current uncommitted focus prerequisite issue, missing terminal receipt for a manual no-country outcome, and blocked whole-event probability/MCP lifecycle gates are parent-owned follow-ups, not safe country cleanup. |
| 007 Fury | No fixed country tag; the Fury actor is flag/classifier-driven. | `events/007_fury.txt` references the USA as an existing host and the shared `fury_actor` flag. No new country definition or history was found. | Retain flag-driven actor handling. No fixed-tag cleanup candidate. |
| 008 Tensions Rising | No new country package. | No Event 008 country definition, history, or fixed tag was found. | No country cleanup candidate. |
| 009 White Peace | No new country package. | No Event 009 country definition, history, or fixed tag was found. | No country cleanup candidate. |
| 010 Death | Fixed dormant `DTH` country plus dynamic Death route. | `common/country_tags/chaosx_countries.txt`, `common/countries/Death.txt`, `history/countries/DTH - Death.txt`, `common/scripted_effects/010_death_effects.txt`, focus, AI, ideas, flags, portraits, and cosmetic-tag files are present. The route obtains its territory dynamically and uses `death_country`/original-tag guards. | Prior Death handoffs report the country surface covered. No static state omission, stale tag, or dead cleanup reference was proven. Keep dynamic origin behavior. |
| 011 Secret Alliance | No new fixed country package. | Event 011 uses existing country actors and shared event-log/details country clauses; no Event 011 country tag or history was found. | No country cleanup candidate. Any asset-archive issue belongs to the Event 011 event-asset handoff, not country source. |
| 012 Africa Is One | Reused Event 006 and vanilla carriers, Africa overlays, host playbooks, focus overlays, decisions, ideas, AI, and package effects. | `docs/plans/012_africa_plans/subagent_handoffs/012_africa_final_country_certification_2026-08-10.md` records 22 full and 26 compact host playbooks, six promoted Tier A carriers, and no new country-tag shell. HZX Basutoland, EUX Swaziland, and ELX Zanzibar remain blocked by the absence of an accepted unique map state. Sixteen priority members and all 64 AI rows remain blocked by formation, receipt, provenance, or probability gates. | Carrier reuse and dormant package rows are intentional. Do not invent states, country tags, advisors, portraits, or AI weights to clear the gates. Global map diagnostics are unrelated to the bounded African anchors. |
| 013 Natural Disasters | No new country package; dynamic host/event settings only. | No Event 013 fixed tag, country definition, or country history was found. | No country cleanup candidate. Shared settings name selectors are outside this country-only handoff. |
| 014 Cannibalism | Fixed reusable warlord slots `CBA`–`CBH` and dedicated unified host `CBL`, plus a ZZZ Wendigo route. | `common/country_tags/014_cannibalism_countries.txt`, matching definitions/histories, `common/scripted_effects/014_cannibalism_effects.txt`, ideas, units, AI, and cleanup logic align. Runtime migration uses `set_state_owner_to = CBL`, `set_state_controller_to = CBL`, core migration, and CBA–CBH cleanup before annexation. | Reusable dormant slots and the CBL host are intentional. No stale slot alias or release cleanup defect was found. |
| 015 Utopia Manifesto | No fixed country package; dynamic political/institutional and country-routing effects. | `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/country_package_current_reaudit_2026-07-15.md` reports all numbered country findings PASS and no fixed Event 015 tag. | No country-source cleanup candidate. Keep dynamic route and institutional-body identity handling. |
| 016 Brilliant Scientist | Fixed `KRG` Kruger state and fixed `DHR` D’Rhondan country, shared alien-infantry API, technologies, units, focus trees, decisions, characters, portraits, flags, and AI. | `common/country_tags/016_brilliant_scientist_country.txt` and `016_dhrondan_country.txt`, definitions, histories, runtime setup, focus loaders, characters, and assets are aligned. The current DHR audit reports conditional static acceptance, with 12 characters and 88 focuses, but blocks 3D alien infantry, custom probability-owner evidence, dynamic state-flow engine evidence, complete event rendering, and live acceptance. | The existing narrow `send_equipment` correction at `common/scripted_effects/016_dhrondan_country_effects.txt:126-130` is already present and was not changed. No additional safe country cleanup was proven. |
| 017 A Faction Comes Calling | No new country package. | Event 017 uses existing countries and shared faction behavior; no fixed Event 017 country definition/history was found. | No country cleanup candidate. |
| 018 Resources Found | Fixed dormant `DHO` Oth-Kesh Host with dynamic origin, cave units, ideas, focus, AI, and technology dependencies. | `common/countries/The Oth-Kesh Host.txt`, `history/countries/DHO - Oth-Kesh Host.txt`, `common/scripted_effects/018_resources_found_cave_effects.txt`, `common/national_focus/018_resources_found_cave_focus_tree.txt`, `common/ai_strategy/018_resources_found_ai_strategy.txt`, and `common/ideas/018_resources_found_cave_ideas.txt` are source-coherent. Current focus source, MCP evidence, and `docs/events/018_resources_found/cave_country.md` all record 67 focuses; older historical handoffs still describe the superseded 65-focus snapshot. | The current source-of-truth documentation is aligned. Historical snapshot counts remain historical evidence rather than active authority. No DHO fixed-state fallback or stale country reference was found. Live supply/production and typed probability remain conditional. |
| 019 Soldiers from Nowhere | Dynamic derivative countries with no fixed tag fallback, provider identities, route/family flags, focus tree, decisions, missions, ideas, AI, and cleanup. | `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_country_package_live_final_reaudit_2026-07-16.md` reports 13 identities across seven regions, a 45-node derivative tree, 68 decisions, 14 missions, 42 ideas, 22 AI profiles, and exact derivative cleanup. | No fixed-tag or generic fallback was found. Regional flag-production provenance remains separately owned and is not a gameplay cleanup issue. |
| 020 Black Plague | Fixed `RTA` Rat Nation and `RTX` Rat King, dormant histories, focus trees, units, ideas, AI, and weaponization cleanup. | `common/country_tags/020_black_plague_rat_countries.txt`, definitions/histories, `common/scripted_effects/020_black_plague_rat_effects.txt`, focus, AI, and asset wiring align. Current source has 52 RTA focus roles and 71 RTX roles; older claims of 51/missing frames are superseded. | `history/countries/RTA - Rat Nation.txt:9` already had the dormant Dominion-grant correction in a prior patch and was not changed. Remaining identity/provenance gaps are design or asset issues: title-only public `Rat King`, no rat advisors/high command/commanders, and missing durable portrait-source/rights manifests. No dead country helper was proven. |

## Shared country infrastructure audit

### Tag registration and definitions

The read-only parser over `common/country_tags/*.txt` found 155 country-tag definitions and 155 unique tags, with zero duplicate tag groups.

Every quoted country target in the country-tag files resolved to an existing file under `common/`, with `missing_country_targets = 0`.

The seven non-country-definition files under `common/countries/` are expected cosmetic or consolidated bundles: `006_independence_wave_formable_cosmetics.txt`, `012_africa_cosmetic.txt`, `012_africa_world_order_cosmetic.txt`, `016_brilliant_scientist_cosmetics.txt`, `016_dhrondan_cosmetics.txt`, `cosmetic.txt`, and `fallout_consolidated_countries.txt`.

The fixed custom tag set checked for vanilla collisions contains no collision with vanilla `common/country_tags`. The scoped fixed custom histories for `ZZZ`, `DTH`, the Event 005 breakaways, CBA–CBL, `KRG`, `DHR`, `DHO`, `RTA`, and `RTX` all exist.

The exact Event 006 reservation comments are important evidence rather than dead code. The `AUX` token at `common/country_tags/006_independence_wave_countries.txt:23` is a comment explaining that a retired reservation is a Windows device basename. It is the only token-level reference to `AUX`; no live alias reference exists.

Token-boundary scans excluding documentation, graphics, interfaces, and binary assets found zero live references for the retired aliases `ALA`, `ALN`, `BAC`, `BSC`, `KHW`, `KRS`, `KZR`, `OGB`, `RMC`, `TSC`, `APX`, and `MRC`, and one comment-only `AUX` reference. These aliases should remain retired rather than being reintroduced or deleted from explanatory comments.

### Shared classifiers and collections

`common/scripted_triggers/chaosx_dynamic_triggers.txt:16-82` currently classifies the known zombie, Holy Realm, Death, cave, cannibal, Event 019 derivative, Kruger, D’Rhondan, and rat actors through `is_special_chaos_country` and `is_actual_nonhuman_country`.

Event 006 tags are intentionally not added to those global special/nonhuman classifiers. Their active-current-country semantics are provided by Event 006 package predicates and collections. Adding all dormant reservations to the global classifier would alter unrelated event eligibility and is not a safe cleanup.

`common/collections/chaosx_country_collections.txt:14-126` exposes active current-country views for all Chaos countries, Event 006 ownership/registration/selectability/overlay views, Africa views, and Soviet Collapse. Dormant Event 006 reservations are represented by static registry arrays and exact package triggers rather than collection membership. This distinction is documented and must be preserved.

The Event 006 country registry explicitly requires package ID, anchor, origin, and carrier provenance when a registered tag is shared. Selecting by tag alone is unsafe for shared carriers such as `CHU` and `BIA`.

### Dynamic release, transfer, core, capital, and cleanup behavior

The source uses the engine-supported distinction between `transfer_state_to` for owner/controller transfer and `set_state_owner_to` for owner-only mutations. Event 014 explicitly sets both owner and controller for CBL, while Event 005 and Event 016 preserve their documented dynamic state-transfer boundaries.

The static `set_capital = { state = <number> }` scan across the scoped Event 005 setup file found 44 numeric references and zero IDs absent from the 1,081 vanilla state definitions. Other scoped country routes use event targets or dynamic state values by design. The omitted capitals in ancient Event 005 histories are not stale data: their comments and runtime setup assign capitals after state transfer.

The dormant `capital = 1` shells for KRG, DHR, DHO, RTA, RTX, and CBA–CBL are bootstrap state, not evidence of a permanent capital assignment. Runtime initialization replaces or sets the appropriate capital after the event-owned country exists.

No stale fixed-tag fallback, unguarded release, or orphaned Event 001–020 country cleanup helper was proven by the source scans. Dynamic country and derivative cleanup must remain fail-closed until its owner has the required terminal receipts.

## File-surface checklist

| Surface | Coverage result | Exact files or identifiers | Remaining risk or action |
| --- | --- | --- | --- |
| Country tags and loaders | Static-positive for fixed tags and Event 006 reservations. | `common/country_tags/chaosx_countries.txt`, `006_independence_wave_countries.txt`, `014_cannibalism_countries.txt`, `016_brilliant_scientist_country.txt`, `016_dhrondan_country.txt`, `018_resources_found_cave_country.txt`, `020_black_plague_rat_countries.txt`. | Event 006 central admission remains partial; do not infer package readiness from tag registration. |
| Definitions and histories | Static-positive for the checked custom definitions and histories. | `common/countries/`, `history/countries/`, Event-specific history/units files. | Dynamic shells still need live consumer evidence; no game executable was run. |
| State ownership, controllers, cores, claims, capitals | No invalid static capital IDs or obvious source mismatch found. | `common/scripted_effects/005_soviet_collapse_effects.txt`, `003_holy_realm_effects.txt`, `014_cannibalism_effects.txt`, `016_dhrondan_country_effects.txt`, `018_resources_found_cave_effects.txt`, `020_black_plague_rat_effects.txt`. | Event 006 terminal receipt and Event 016 dynamic state-flow evidence remain blocked. |
| Politics, parties, laws, diplomacy | Fixed country definitions and route setup are source-present; Event 003 neutral institutional setup and Event 005/016/020 route identities are intentional. | `common/countries/*.txt`, `common/characters/`, `common/country_leader/`, Event-specific effects. | Event 020 public Rat King naming is a design gap, not a cleanup patch. |
| Leaders, characters, advisors, commanders | Static rosters exist for most fixed packages. | `common/characters/`, `common/country_leader/`, Event 016 DHR handoff. | Event 012 deliberately has no package-specific advisors/high command; Event 020 has no rat advisors/high command/commanders; both require design ownership. |
| Portraits and flags | Runtime references are generally present for checked packages. | Event-specific `interface/*.gfx`, `gfx/`, portrait and flag handoffs. | Event 006 has 14 supplied portraits without safe consumers; Event 012 portraits remain source-locked; Event 020 durable source/rights manifests were not found; Event 016 3D portrait/unit evidence remains blocked. No portrait-worker claim is made here. |
| Focus loading and trees | Source loaders and focus IDs exist for the checked country packages. | `THR_focus`, `CFR_soviet_collapse_focus_tree` and related Event 005 trees, `dhrondan_focus_tree`, `brilliant_scientist_kruger_state_focus_tree`, `018_resources_found_cave_focus_tree`, `black_plague_rat_focus_tree`, `black_plague_rat_king_focus_tree`, `infantry_spawn_derivative_focus_tree`. | Event 005 MCP focus route timed out; Event 006 current graph/prerequisite issue remains parent-owned; the current Event 018 source-of-truth doc is aligned at 67; broad focus acceptance cannot be claimed from source-only checks. |
| Decisions, missions, and formables | Country-owned decision and formable hooks are source-present where the event owns them. | Event 006 registry/formable matrices, Event 012 host/priority matrices, Event 014 cleanup decisions, Event 016 DHR decisions, Event 018 DHO decisions, Event 019 dynamic decisions/missions. | Event 006 has only a bounded admitted formable subset; Event 012 and Event 016 gates remain conditional; no formable expansion is authorized by cleanup. |
| Ideas, national spirits, and lifecycle | Starting and route lifecycle ideas are present for checked country packages. | Event 006 package idea files, `common/ideas/014_cannibalism*`, `016_*`, `018_resources_found_cave_ideas.txt`, `020_*`. | No orphaned country idea ID was proven. Icon and localisation ownership remains with event/asset workers. |
| Units, OOB, stockpiles, production, supply | Dormant shells and dynamic grants follow event-specific designs. | `history/units/`, Event-specific unit/equipment files, event runtime grants. | No live campaign, AI front, supply, production-line, or stockpile validation was authorized or run. Event 012 and Event 016 live acceptance remain conditional. |
| Technology dependencies | Technology files and references exist for Event 016 alien infantry and Event 018 cave systems; other packages use vanilla tech. | `common/technologies/016_*`, `common/technologies/018_*`, Event-specific effects. | Installed package exposes no separate Technology Tree Viewer; tech inspect/render is partial or timed out. No technology deletion or tree claim was made. |
| AI strategy and probability | Source AI files exist for fixed and dynamic packages. | `common/ai_strategy/005_soviet_collapse.txt`, Event 006 AI files and package adapters, `016_*`, `018_resources_found_ai_strategy.txt`, `020_black_plague_rat_ai_strategy.txt`, Event 019 strategy profiles. | Mandatory custom probability-auditor route is unavailable. No weight patch or probability compare was claimed. |
| Cleanup, annexation, and transfer | Source cleanup helpers are present and guarded. | Event 005, 006, 010, 014, 016, 018, 019, and 020 scripted effects/triggers. | Do not remove meta-effect-dispatched or dynamic helpers without a complete reference expansion and terminal-state evidence. |
| Shared event-log/details country references | Shared selectors and clauses were reference-checked for Event 001–020 country IDs. | `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, `common/scripted_effects/chaosx_events_log_effects.txt`, Event-specific integration files. | Functional log/details text is parent scope; no layout change was inspected or recommended. |

## Missing, stale, or uncertain country-package surfaces

### Safe bounded documentation or catalog candidates

1. Reconcile the superseded Event 006 registry handoff with the current authority. The current whole-event handoff at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event006_completion_audit_current_2026_08_22.md` is the current source for 32 admitted packages and 161 unattested selectable rows out of 193 non-overlay rows. Older Event 006 registry handoffs carry historical counts and must not remain ambiguous authority.

2. Event 018 focus-count reconciliation is already reflected in the current source-of-truth doc: `docs/events/018_resources_found/cave_country.md` records 67 focuses. Older handoffs that say 65 are dated snapshots and should not be promoted as current authority.

3. Parent review confirmed that the current Event 006 catalog export matches `chaosx.events_log.window.event_details.independence_wave`; the earlier mismatch observation is stale and requires no spreadsheet edit.

### Retained code that could look dead but is not proven dead

- The 17 Event 006 inert reservations in `006_independence_wave_unresearched_reservations.txt` are deliberate fail-closed parser-safe reservations for unresolved identities.
- Event 006 overlays with no standalone tag are documented non-selectable overlays and must not be promoted or deleted by a tag-only scan.
- Event 006 shared registered carriers require package provenance and cannot be collapsed by tag name.
- Event 005 ancient-history files without `capital` rely on runtime state transfer and capital assignment.
- KRG, DHR, DHO, rat, and cannibal dormant `capital = 1` shells are dynamic bootstrap state.
- `AUX` is a historical Windows-basename comment, not a live alias.
- Event 019’s lack of fixed tags is intentional dynamic derivative design.
- Event 012’s reuse of Event 006/vanilla carriers is an accepted architecture; adding country tags would be a redesign.
- Event 003’s THR identity is a cosmetic/formation carrier over existing TIB/BHU/NEP, not an orphaned country tag.
- Event 002’s repeated economy-law effects are retained because they may represent deliberate sequential law progression and no engine evidence proves a no-op.

### Country identity and presentation risks requiring owner decisions

- Event 020’s public RTX identity remains title-only `Rat King` in the current country package; replacing it with an actual-like fictional name or epithet is a design decision.
- Event 020 has no rat-specific advisors, high-command advisors, or commanders in the current package; this is a content gap, not safe deletion.
- Event 020 handoffs reference durable portrait source/rights manifests that were not found under the current local `docs/assets` listing. Runtime DDS wiring should not be changed until provenance ownership reconciles the archive.
- Event 006 has 14 supplied portraits without exact safe consumers, and the current fail-closed refusal to wire them is correct.
- Event 012 portraits remain source-locked and priority-member package rows remain blocked by provenance and route gates.
- Event 016 DHR has static 2D coverage but its required alien-infantry 3D entity/action/sound package is incomplete; no fallback is authorized.

## Map and state setup findings

The bounded Event 006 anchors are states 82 Banat, 184 Thrace, 185 Epirus, and optional extension 805. The prior country-package audit reports matching vanilla owners/capitals and read-only MCP state inspection/render evidence:

- Map inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b41eea68e1c61384eb62a4e0159cb53b543c8b56f483ef57031b521c2cd7d400/18ca6c3ff22c0b57a1cb6ca9cc1792b1867cd1ddb896bba1a5e9c998bfe3a095/map-inspect.3665a7b49fd0ffa1.json`.
- State render PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1e048305649726acd6ca2586a15c2fcdcd904d4b5c238d1374b8bb5d3294a8d/992ebf478dd9b6bc4cb5ee9738bb53cbb4fab7e86c0561a33eefa4df11fb3fe1/map-state.png`.

Event 012’s promoted Tier A anchors are states 900, 768, 298, 548, 460, and 448 plus 661. Its bounded map inspect returned 25 states, no unknown province IDs, and no missing geometry; the useful artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f95a3b31b739c76917df72537d3e60a9ac2c8fb753c9c9d4099fcb1a9e0ab24c/8b40a37cf5ad8fefd06c379f588178ea076e9924bddeb2576b7dd125049e55d9/map-inspect.17d3c6af4f7bb226.json`.

Event 018 has no fixed DHO state because the first origin is selected at runtime. Its bounded state-1 map inspect/render passed state-membership and network checks; the current handoff records `map-inspect.d4bae4183ffda7fd.json` and `map-state.png` artifacts under the Event 018 MCP run.

Event 020’s state-1 map inspect/render found no RTA/RTX-specific map failure. The exact inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86d2f13cbde650494bf7a697b4952f31191ad2f00210015f357cf3d14b773114/092a5d20f7c108cd71618fa70afa51861f70704e1c7eb11c1a319781227d5447/map-inspect.f1c123073e1222ac.json` and the render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48523ff3b868652410cf501163e7da6631266dc80a98838b57853ad3f2d7a34a/400705f10fa13ba23e02aa97120a84a7c350eeab51e9399b45bef847ccc88437/map-owner.png`.

The MCP map reports global `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics in `mod:map/buildings.txt` in the Event 006, Event 012, Event 018, and Event 020 handoffs. The reported counts are 1,323 invalid building positions and 1,331 invalid port-adjacency records in the broader workspace. No inspected scoped country anchor was identified as the cause, and no map write was performed.

A fresh bounded map call for `[1,82,184,185,248,608]` was terminated after exceeding the available wait window. This is a tooling limitation, not evidence of a map defect.

## Politics, leaders, portraits, flags, advisors, and parties

The fixed custom tags and country definitions have matching names/adjectives and expected party/cosmetic references in the current source scans. Existing institutional identities are preserved for Holy Realm and dynamic Event 005/016 routes.

The character-specific review found no opposite-gender portrait/name pairing in the checked Event 016 and Event 019 packages. Event 016 DHR’s 12-character roster is source-complete at the static level. Event 019’s generated derivative identity pools are route-specific and retain gender metadata guards.

The unresolved presentation gaps are package-specific rather than stale references: Event 020 lacks rat advisors/high command/commanders and has title-only RTX public naming; Event 012 deliberately has no package-specific advisors/high-command roster; Event 006 has intentionally unmapped supplied portraits; and Event 016’s remaining model/audio work is not a country-tag cleanup issue.

No flag or portrait runtime path was changed. Character portrait production and provenance remain owned by `chaosx_portrait_creator` and the event asset workers.

## Focus, decision, idea, and asset findings

Source loaders for the checked country-linked trees are present: `THR_focus`, the Event 005 custom splinter trees, `dhrondan_focus_tree`, `brilliant_scientist_kruger_state_focus_tree`, `018_resources_found_cave_focus_tree`, `black_plague_rat_focus_tree`, `black_plague_rat_king_focus_tree`, and `infantry_spawn_derivative_focus_tree`.

Event 006’s current focus handoff reports 184 focuses and 193 connectors with no crossings or node intersections, but one long connector, four linear-detour warnings, and two isolated military-choice nodes. The current uncommitted prerequisite issue is parent-owned and was not changed here.

Event 018’s current focus tree has 67 focuses and 81 connectors with no Event 018-local diagnostics. The current event documentation is aligned at 67; older 65-focus handoffs remain historical snapshots.

Event 020’s current source/MCP handoff has 52 RTA roles and 71 RTX roles with registered focus assets. Older 51-focus and missing-frame claims are superseded and should not trigger deletion.

Event 016 DHR’s current focus audit reports 88 focuses, 102 connectors, resolved DHR icon assets, and only bounded layout warnings. The installed Technology Tree Viewer is absent, so no technology visual-completion claim is made.

No orphaned country idea IDs or direct focus/idea icon path mismatches were proven in the source and handoff checks. Asset archive discrepancies remain documentation/provenance work, not safe runtime cleanup.

## Starting military, technology, industry, supply, and production

The checked dormant histories intentionally provide minimal bootstrap shells. Event-owned runtime effects grant starting armies, equipment, research, factories, laws, supply, or production only after the relevant country-creation or route gates.

Event 002 creates its zombie forces after the outbreak transfer. Event 005 successors receive route-specific transfers and setup. Event 014 migrates warlord forces into CBL. Event 016 DHR creates the bounded alien landing cohort through the shared API. Event 018 DHO starts with zero normal recruitment and route-specific cave systems. Event 019 creates dynamic derivative forces through provider callbacks. Event 020 uses its rat-specific units and stockpiles.

No source scan proved an accidental large army, duplicate OOB, duplicate starting idea grant, invalid equipment type, orphaned production line, or fixed-state supply assignment in the scoped country packages.

Live stockpile, supply-capacity, production-line, train, convoy, front allocation, and AI survival behavior were not validated by launching the game or a save. Event 012 and Event 016 handoffs explicitly retain those live-consumer limitations.

The technology route is also conditional. Event 016’s alien infantry technology dependencies are source-present, and Event 018 has no custom DHO tree, but technology inspect/render is partial or timed out and no Technology Tree Viewer is installed. No technology source was deleted or rewritten.

## AI and playability findings

AI strategy files and focus/decision AI blocks exist for the checked fixed and dynamic country packages. The current source did not justify changing an AI weight without a named-scenario baseline and same-scenario comparison.

The mandatory `chaosx_ai_probability_auditor` route is unavailable in this runtime. A direct `hoi4.probability_inspect({})` call only returned the installed adapter list (`PROBABILITY_ADAPTERS_LISTED`) with zero candidates. No owner-routed auditor baseline or `hoi4.probability_compare` pass was possible.

Existing bounded handoffs remain useful but do not satisfy the missing owner route:

- Event 005’s dated probability handoff reports its supported named-scenario pass, while broader country package acceptance remains open.
- Event 006’s Thrace and Epirus inspections found no adapter-recognized weighted surface, while the Banat adapter returned `INTERNAL_ERROR: Unexpected internal error`; whole-event AI/probability acceptance remains blocked.
- Event 012 keeps all 64 AI profile rows blocked pending mandatory probability scenarios and campaign balance.
- Event 016 DHR has partial direct probability artifacts but no custom auditor pass.
- Event 018’s probability handoff remains conditional because typed campaign pools and ownership/control/neighbor/enemy predicates are not fully proven.
- Event 020’s `ai_strategy_factor` request against `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` returned `PROBABILITY_SURFACE_EMPTY`; this means the adapter did not recognize a matching weighted block, not that the source AI file is absent.
- Event 019’s provider-pool odds remain unresolved in its current handoff, and its prior MCP attempts hit `ARTIFACT_STORAGE_LIMIT`.

No AI strategy, focus weight, decision score, mission score, event chance, MTTH, random-list weight, or custom-pool weight was changed.

## Shared Events 021+ references

Eighty-one event files with numeric prefixes 021 or later were reference-scanned only for shared country registry/helper tokens. The only direct future-event reference found was in `events/091_the_great_revolution.txt:77`, `:84`, and `:110`, where `is_special_chaos_country` excludes special actors from the Event 091 country loops.

This is a shared classifier dependency, not an Event 091 country-package audit. The classifier definition remains in `common/scripted_triggers/chaosx_dynamic_triggers.txt`; no Event 021+ event-specific country implementation was inspected or edited.

No direct Event 021+ reference to `chaosx_country_*`, `is_actual_nonhuman_country`, `independence_wave_*`, or `soviet_collapse_*` was found in the event files beyond the shared `is_special_chaos_country` use above.

## MCP and task-specific validation

The following read-only MCP evidence was used or inherited from current dated country handoffs.

- Event 002 file scan for `events/002_zombie_outbreak.txt` returned `EVENT_INSPECTED_PARTIAL` with diagnostic `MCP_INLINE_FILES_TRUNCATED`, no blocking diagnostics in the requested projection, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d1b3466568b8cc45dbe9be6e75f433768f9a8fdd20e93eb0dce827a0b2957269/a65d6a7c2fc1a2e3661f56175f350dd2b95fbcb27d6b8aebadb65f3c6285e749/event-scan-2af1fa63424e.json`. Event render timed out after 180 seconds.
- Event 006 event lint/state artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3d419ff19ce207cb0110493bb3a315f8faac09208c62689a54ec136544cefda/736e1313a62b0cbd7e05e5796f4ff09867abb24bb94d746e67e35eeea7a63004/event-lint-bc0062fc8506.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d1dec1775fec791c205006bc4b4d1ac0c57d0b74a2d7d50c94cab8a5fdd9c0a1/b8234721ae57a7ab312356790e5098dd2a4dea5a5785b740a3a628b52f36a979/event-state-bc0062fc8506-manifest.json`. Both are partial projections and do not close package lifecycle or terminal-receipt gates.
- Event 006 focus/current map artifacts are recorded above in the map section and in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event006_completion_audit_current_2026_08_22.md`.
- Event 012 focus and map routes completed bounded inspections; its priority focus artifact and map artifact are recorded in `docs/plans/012_africa_plans/subagent_handoffs/012_africa_final_country_certification_2026-08-10.md`. The country handoff reports no unknown geometry for inspected anchors and no local focus diagnostics.
- Event 016 DHR focus, event, map, technology, and direct probability artifacts are recorded in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_final_country_audit_2026-08-22.md`. The map render, technology render, and custom probability-owner route remain blocked or timed out.
- Event 018 focus, event, map, and partial technology artifacts are recorded in `docs/plans/018_resources_found_plans/subagent_handoffs/event018_country_final_current_2026-08-09.md`. The focus and bounded map routes are useful; the global technology scan is partial.
- Event 019 prior focus/event MCP attempts returned `ARTIFACT_STORAGE_LIMIT`; the source/data/binary evidence in `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_country_package_live_final_reaudit_2026-07-16.md` is not equivalent to an engine artifact.
- Event 020 focus, event, map, and probability artifacts are recorded in `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-06_event020_rat_country_package_current_audit_handoff.md`. The event route is partial because `MCP_INLINE_FILES_TRUNCATED`; the rat AI adapter returned `PROBABILITY_SURFACE_EMPTY`.
- A fresh Event 005 focus inspection timed out after 180 seconds. A fresh bounded map call for multiple Event 001–020 state IDs was terminated after exceeding the available wait window. A fresh global technology scan was similarly terminated. These are exact route/tooling blockers, not source defects.

The installed MCP package exposes no separate Technology Tree Viewer. This remains an unresolved limitation for every country-linked technology surface.

No map write was performed, so there is no dry-run/apply/post-validation or rollback evidence to report. No GUI route was inspected.

## Behavior risk and parent actions

Deleting Event 006 inert reservations, shared carriers, dynamic bootstrap histories, classifier entries, or meta-effect-dispatched cleanup helpers could make dormant identities selectable, change unrelated event eligibility, strand runtime references, or break rollback. Those actions are not safe cleanup without a package-specific accepted plan and terminal evidence.

The highest-confidence next action is documentation authority reconciliation for older Event 006 registry handoffs. The Event 018 source-of-truth doc and current Event 006 catalog export are already aligned. Country-source changes should wait for the blocked probability, MCP lifecycle, map/receipt, asset-provenance, and live-consumer owners where applicable.

## Changed files, skipped work, and simplifications

Changed files: only `docs/plans/repo_cleanup/subagent_handoffs/country_cleanup_baseline_2026-08-22.md`.

No country package, country tag, history, focus, decision, idea, AI, technology, map, asset, localisation, spreadsheet, interface, `.codex`, or `.qoder` file was modified.

No source cleanup was skipped after a confirmed dead reference was found; none was proven. The audit intentionally did not turn conditional or blocked package surfaces into fallbacks, did not invent country identity content, did not promote Event 006 reservations, did not alter map data, and did not substitute direct probability evidence for the unavailable mandatory custom auditor.

No commit was made.
