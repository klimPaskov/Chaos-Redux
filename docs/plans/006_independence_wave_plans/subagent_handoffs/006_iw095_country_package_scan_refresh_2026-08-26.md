# Event 006 IW-095 Dahomey country-package scan refresh

Date: 2026-08-26

Scope: bounded read-only audit of IW-095 Dahomey (`DAH`) against the Event 006 candidate registry, Part 5 country-package contract, the current Event 006 shared framework, the installed DAH baseline, and the Event 012 Africa host precedent.

Decision: no gameplay patch and no central admission. The existing IW-095 allocator binding is the only source-ready surface; the package remains correctly fail-closed until its identity, asset, package, AI, origin, and engine proofs exist.

## Executive finding

IW-095 has a clean installed-map footprint but not a source-ready country package. The candidate row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:96`; it specifies a Level 2 Dahomey package on registered tag `DAH`, an Abomey anchor, a West African federation angle, local infantry and palace or national guards, and sourced historical flags and leaders.

The current runtime binding uses state `776`, not the matrix's stale public-baseline anchor `556`. `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:736-743` checks `DAH` and state `776`, while `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1549-1562` publishes `iw_095`, `rg_nigeria_coarse`, `west_central_africa`, `regional`, `agrarian_regional`, registered-tag mode, `DAH`, anchor `776`, and the owner of state `776` as the former host.

The generic eligibility gate at `common/scripted_triggers/006_independence_wave_package_triggers.txt:74-77` requires both origin availability and `independence_wave_package_content_ready`. No DAH/IW-095 source sets that readiness flag. The weight, pool, reservation, and scenario-ranking entries are registry plumbing, not package attestation.

This is a broad missing-package tranche, not a safe local correction. Setting readiness, borrowing a generic leader, reusing the DAH flag ladder, or adding a generic AI profile would bypass the Part 5 contract and could misclassify DAH in Event 012. No tag, state, gameplay, asset, specification, workbook, or central registry file was changed.

## Required references reviewed

Repository guidance and skills reviewed: `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, and `.agents/skills/chaos-redux-comfyui/SKILL.md`.

Offline Paradox wiki pages reviewed: `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, `AI modding`, `Country creation`, `National focus modding`, `Map modding`, `Technology modding`, `Equipment modding`, and `Division modding` under `paradox_wiki/`.

Vanilla documentation reviewed: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `loc_objects_documentation.md`, and `modifiers_documentation.md`.

Event 006 references reviewed: Part 5, the candidate registry row, package research resolution, state-anchor and reservation-group research, current installed-map bindings, `006_event6_first_footprint_admission_improvement_addendum_2026-08-26.md`, `006_event6_first_footprint_improvement_handoff_2026-08-26.md`, and the existing `006_iw095_package_audit_2026-08-26.md` and `006_iw095_asset_research_2026-08-26.md` handoffs.

Adjacent package precedents reviewed: `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`, `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`, `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt`, `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt`, `common/decisions/006_independence_wave_iw093_iw098_decisions.txt`, `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`, `common/scripted_effects/006_independence_wave_iw093_iw098_focus_effects.txt`, and shared Event 006 character, idea, AI, and localisation registries.

## Country package coverage checklist

| Surface | Status | Exact evidence and gap |
| --- | --- | --- |
| Carrier/tag | Partial | Vanilla registers `DAH` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:160`; no Event 006 DAH wrapper or origin-safe package adapter exists. |
| Anchor/map | Partial | Current binding and vanilla core use state `776`; the matrix and research rows retain public-baseline `556`. The selected state has a victory point, port, three provinces, and a DAH core, but host-survival and runtime transaction evidence are absent. |
| Country definition/history | Fail | Vanilla `common/countries/Dahomey.txt` and `history/countries/DAH - Dahomey.txt` provide only the dormant baseline; no IW-095 release setup or package-owned history exists. |
| Politics/parties | Fail | Vanilla history sets neutrality 50/25/20/5 with elections disabled; no IW-095 party names, government setup, route lock, or settlement exists. |
| Leader/characters | Fail | Vanilla `common/characters/DAH.txt` contains advisor-only IDs and no country leader, field marshal, or corps commander. No IW-095 character or institutional roster exists. |
| Portraits | Fail | No DAH/IW-095 portrait source placeholder, final portrait, portrait wiring, manifest, or portrait-worker handoff exists. The asset research handoff keeps the historical leader/institution choice conditional. |
| Flags/symbols | Partial | Vanilla DAH normal/medium/small ladders exist technically, but their green/yellow/red family is not cleared as a 1936 Dahomey identity. No Event 006 provenance decision or runtime flag ladder exists. |
| Ideas | Fail | No `independence_wave_iw095_*` ideas or lifecycle exists in `common/ideas/006_independence_wave_ideas_registry.txt`. |
| Decisions/missions | Fail | No founding mission, four serialized projects, three government settlements, network decision, decision AI, or cleanup exists. |
| Focus | Fail | The shared tree is present and MCP-clean structurally, but no DAH/IW-095 callback or package-specific focus effect exists. |
| Events/incidents | Fail | No IW-095 support-event branch, founding incident, route incident, or package event exists. |
| Formable/league | Fail | Generic FORM-24 metadata exists, but no DAH family-member gate, consent route, anchor proof, or `iw095_open_west_african_trade_mission` exists. |
| AI/probability | Fail | No IW-095 AI strategy, focus weighting, decision weighting, route strategy, or package probability surface exists. No quantitative balance claim is made. |
| Localisation | Fail | Vanilla defaults `DAH` to `Benin`/`Beninese`, while neutrality uses `Dahomey`/`Dahomeyan`; no IW-095 country, party, leader, idea, focus, decision, incident, debug, or formable keys exist. |
| Cleanup/origin | Fail | No IW-095 cleanup dispatcher, roster retirement, decision/focus removal, flag/variable cleanup, or Event 012-safe origin teardown exists. |
| Starting forces/tech/industry/supply | Fail | Vanilla DAH starts with infantry weapons level 1 and ten convoys only; no army, navy, air force, template, factory, production, research-slot, fuel, train, supply, or reinforcement package exists. |

Part 5 requires every selectable package to prove a unique anchor, host survival, no overlap, capital, tag path, identity, politics, leader mode, flags, ideas, forces, reinforcement, region, formable, AI, origin, focus, decisions, localisation, and documentation. Level 2 additionally requires a country-specific focus group, bespoke decision family, distinctive starting problem, unique leader or institution path, special regional/formable angle, and several unique incidents/assets. IW-095 has none of those package-owned surfaces beyond the registry row and current anchor plumbing.

## Expected package-local file surface

The addendum's expected package-owned files are absent for IW-095: `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt`, `common/scripted_triggers/006_independence_wave_first_footprint_package_triggers.txt`, `common/decisions/006_independence_wave_first_footprint_decisions.txt`, and `common/ai_strategy/006_independence_wave_first_footprint_ai_strategy.txt` have no IW-095 implementation. Shared registries exist but contain no DAH entries for ideas, characters, focus callbacks, AI, decisions, or localisation. No IW-095 support-event branch exists in `events/006_independence_wave_support_events.txt`.

The package docket remains unimplemented: `independence_wave_iw095_reconcile_abomey_and_porto_novo`; `iw095_convene_abomey_council`; `iw095_reopen_coastal_customs`; `iw095_register_palm_and_market_revenue`; `iw095_organize_civic_guard`; `iw095_ratify_civic_compact`; `iw095_restore_council_authority`; `iw095_authorize_emergency_directorate`; and `iw095_open_west_african_trade_mission`.

## Vanilla DAH and Event 012 precedent

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/countries/Dahomey.txt:3-6` defines African graphical culture and country colour only. `history/countries/DAH - Dahomey.txt:1-29` provides capital `776`, infantry weapons level 1, ten convoys, and generic advisor recruitment; `:32-78` is a 1939 generic technology/focus block; `:80-91` sets neutrality and popularity. It contains no 1936 units, factories, production lines, country leader, or Event 006 setup.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/776-Dahomey.txt:2-26` defines state `776`, DAH core, FRA owner, victory point province `10919`, infrastructure `2`, naval base `1` at `10919`, provinces `10919 12874 12762`, manpower `1,351,563`, category `pastoral`, and local supplies `1.0`.

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/DAH.txt` contains only advisor IDs `DAH_stc`, `DAH_aco2`, `DAH_aa2`, `DAH_ncs`, `DAH_nt`, `DAH_acas`, `DAH_acd2`, `DAH_democratic_guy`, `DAH_mt`, `DAH_ai2`, `DAH_coi`, `DAH_acr`, `DAH_pot`, `DAH_awt`, `DAH_communist_guy`, `DAH_ncm`, `DAH_acgs`, `DAH_nccr`, `DAH_fascist_guy`, and `DAH_ar`, with generic African advisor portraits and repeated missing-large-portrait comments.

Vanilla localisation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/countries_l_english.yml:2619-2633` mixes `DAH`/`DAH_DEF` as Benin, fascist and democratic forms as Benin, and neutrality/communist forms as Dahomey. A package-local identity decision is required before writing localisation or flags.

Event 012 maps `original_tag = DAH` to `africa_host_playbook.dahomey` at `common/scripted_effects/012_africa_effects.txt:358`, includes DAH in host triggers in `common/scripted_triggers/012_africa_triggers.txt:95,159,205,214,310,316,627`, and uses DAH/state-776 proof context in `common/scripted_triggers/012_africa_proof_triggers.txt`. Event 006 must therefore gate DAH callbacks on the Independence Wave origin and clear them without stripping a surviving Event 012 host package.

## Focus, decisions, assets, and package-specific identity

`common/national_focus/006_independence_wave_focus.txt:37-95` defines the shared `independence_wave_focus_tree` and imports several package branches, but no DAH/IW-095 focus. The seven common callbacks expected by the addendum have no `independence_wave_iw095_focus_*` implementation.

The Level 2 docket requires a country-specific first problem around Abomey and Porto-Novo, customs and palm-market revenue, civic guard organization, and three settlement routes. Those are design obligations, not safe candidates for generic copies from Asante or Sokoto.

The asset research handoff `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw095_asset_research_2026-08-26.md` leaves Ahovô/Arauvau metadata, Justin Aho's 1936 role continuity, the Abomey institutional route, and a defensible 1936 flag unresolved. No portrait-worker production or flag provenance receipt exists. IW-096's BIA/Edo sources are explicitly separate and must not be borrowed for DAH.

## MCP inspection and rendering evidence

All MCP calls below were read-only in workspace `mod_chaos_redux_ea3b2d67c2c0`.

`hoi4.event_inspect` scanned `chaosx.nr6.1` with selector `{kind: event, eventId: chaosx.nr6.1}` and returned `EVENT_INSPECTED_PARTIAL`; the workspace graph reported 9,514 events, 14,706 options, 37,149 edges, 8,315 unresolved nodes, and no blocking diagnostics because broad helper/lifecycle analysis was deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02d9d15fa00b8547b6bbb58d0ba6316433a252e0b59818675cea1caeb01fe065/5df59018cbfc1dd52716bbaf63a2ed4114475a9ea6358ca3a8b6e46881e4cf84/event-scan-f1288dea1225.json`.

`hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` for `chaosx.nr6.1`; its overview JSON/SVG/PNG artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a84cd1bcfd2da3b21d882d252cbb85f96e27a53f24e62387bb9f597233361f8/1b2068821505019b5b05a87087e4f25dff0531c213006de69e8132e9a5e09f57/event-overview-f1288dea1225.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e51cb569b275177961b1e2fa34b6272173454bb011a4568164835288b678d59/be0bf7a237c3b1af9c500c26d0a6748098c4379e18c36e78aee3f470d7cc1d3e/event-overview-f1288dea1225.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e70521053ed39f624d8ae99fcc5b20489a5d2339d5b9f8ff17f16b386515725/7f8a94862aadc1572832be52c3738a9b113fb8f88c1a9809d605240d5bbbb166/event-overview-f1288dea1225.png`. There is no IW-095 event branch to render.

`hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `independence_wave_focus_tree` with 184 focuses, zero blocking diagnostics, and no DAH/IW-095 nodes. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7419e86f14153bb9ce106783f2cc5610a8eb37ddb8dfa6a33c002947484115e9/d11935da5fbc5a2ef5005c9e3c42ef29d4d8e3f4c001ffa004da26b64ee9fd06/focus-inspect.b97c48b187683dec.json`.

`hoi4.focus_render` returned `FOCUS_RENDERED` with source-linked HTML/SVG/JSON/source-map/plan artifacts; the primary render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1387f679ebb46e99df9e4385f2d934232a98fdff7c3d1ee0a817d3b318cc0f0c/a650625a4c45877f60dea62d5b365dda8c56928841a55fc3a6c18cf78aae0951/independence_wave_focus_tree.focus.html`. The only reported warning was an unrelated vanilla generic continuous-focus localisation reference.

`hoi4.map_inspect` covered state `776` and provinces `10919`, `12874`, and `12762`, returning `MAP_INSPECTED`; state/region membership, networks, and adjacencies passed, and three province geometries were resolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/49f2705860e07d4007dd607bc9cb8cb5a44590ed6dce24045d57423254e89430/b7b59ee2f8aeee2f1ee0e4e8b4d17663231f256a2b72c1f5792f37437ede5cd9/map-inspect.adb80186aaf3a544.json`. Aggregate map validation remains false because unrelated `mod:map/buildings.txt` contains 1,323 invalid building-position errors and 1,331 invalid floating-harbor adjacency errors; this is not an IW-095 state geometry defect.

`hoi4.map_render` returned `MAP_RENDERED` for the state layer with coastlines, ports, victory points, resources, buildings, supply, railways, and adjacencies overlays. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c8a38f2a0c09e2af8e7995c5a27803696c79c642b4d19a9fb7e001d8d2e9ae9/95297fb4f5b0b2350814e33062a1c91653f609d11caa1d0a5862a395b40a5448/map-state.png`. The render is an offline representation of the full map and does not prove host-survival or release ownership.

`hoi4.gui_inspect` inspected `independence_wave_status_window` under `independence_wave_status_default` and returned `GUI_INSPECTED`, but aggregate validation retains 2,000 blocking graph diagnostics and reports visible overlap; this is shared-window evidence and no IW-095-specific GUI exists. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f78242e0626546c4cacd88d0887bbc4d1b287b8aae430dc4ce82f9d416815cc3/79d38c4e24c28bdcf15e661a05a91636272eacb2e3723a2e655e07ae1a6c9fad/gui-inspect.6a9e317fb32a3271.json`.

`hoi4.gui_render` returned the shared status-window SVG under normal, minimum-value, maximum-value, long-text, missing-localisation, and 1920×1080/2560×1440 requests. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cf000756ada11a3f72b77c58099ed8eb2f376d67cd52aa69bf75f77a8e2a31f/4ed6b44df7950ca1e291aaad786132c34922228d506235a68564c41f9e60a384/independence_wave_status_window-full.svg`. This does not constitute IW-095 package acceptance.

`hoi4.tech_inspect` and `hoi4.tech_render` ran read-only broad scans but returned partial workspace summaries with helper analysis deferred. The scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee1ca278c09a9f2b1e9196937bd8ca9ee9212836d1e5b932beadbde7d97bd289/c15ebd9be677f44489d2f9b09e14a069cb68532b225862ff1ac473aac13743cd/technology-scan-92f3e3d05a7d.json`; the summary artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cdfd29913497836c2764ef05da8e9d5bce345f66175cb5d923d9f6d35ac6b734/de365f76c5ec7a34613e99f9064c14ef599d5be006363c34ade473b416aafc23/technology-summary-0359942d151e.json`. No IW-095-specific technology node or package tech dependency exists, and the installed package provides no exact DAH Technology Tree Viewer acceptance surface; technology readiness remains unresolved.

The mandatory probability route was attempted through the available `hoi4.probability_inspect` route because the configured `chaosx_ai_probability_auditor` callable is not exposed in this environment. Inspecting `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` as a `random_list` returned `PROBABILITY_SOURCE_INSPECTED` with no diagnostics, 126 candidates, zero available candidates, 126 required inputs, and one unresolved input. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/68d4c0e45cb13d0668f3656112480e26a2625bf1392970e0f46bf12c5b248c5a/58d20b2490ac125400714caf2d54894136cbef84bfb389db2922882e26f26658/probability-inspect-e86c495f21fd.json`. No evaluate, sweep, simulation, or compare was run because IW-095 has no AI surface and the pool is incomplete.

## AI, playability, and admission blockers

No IW-095 AI profile exists for foundation survival, former-host threat, government route choice, project choice, recognition, or FORM-24 preparation. The adjacent package precedent shows that each admitted package needs route-specific AI strategies gated by exact setup-complete flags and package predicates; copying an adjacent profile would not be safe.

`RG-NIGERIA-COARSE` is shared by IW-095, IW-096, IW-097, IW-098, IW-099, IW-100, IW-106, and IW-107. The reservation group therefore needs package-specific overlap and host-survival proof before any DAH admission. The current loader's `agrarian_regional` archetype also differs from the matrix's `kingdom restoration or republic` direction and must be resolved by the package owner, not silently patched here.

Admission remains blocked until the owner supplies a defensible 1936 identity and male leader or authentic institutional body, portrait-worker provenance and runtime output, period-appropriate flag decision, complete package-local setup/effects/triggers/ideas/decisions/focus callbacks/events/AI/cleanup/localisation, Event 012-safe origin guards, FORM-24 membership and consent logic, host-survival and current-anchor receipts, and central final attestation. No safe package-local fix was proven in this scan.

## Changed files and validation

Changed file: this handoff only, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw095_country_package_scan_refresh_2026-08-26.md`.

No tags, state IDs, leaders, parties, focus IDs, decisions, ideas, formable IDs, gameplay files, central registries, specifications, workbook files, or visual assets were changed.

Meaningful validation consisted of direct source and vanilla DAH searches, adjacent Event 006 package-pattern review, and the bounded read-only Event, focus, map, GUI, technology, and probability MCP calls recorded above. Live game execution, save/load, allocator scenarios, and user-facing consumer tests were not run because this was an audit and live validation belongs to the parent/user workflow.

Conclusion: keep IW-095 unadmitted. The next implementation owner should build the package-local source tranche and asset/identity receipts first, then ask the central owner for one atomic admission patch and same-scenario probability comparison.
