# IW-054 Khakassia (KHA) package viability audit

Status: FAIL-CLOSED. No country, map, central-admission, attestation, preflight, Join, identity, or asset files were changed by this audit.

Audit date: 2026-08-15.

Scope: bounded review of the IW-054 KHA candidate against the accepted Event 006 registry, current installed map binding, vanilla KHA content, Event 005 origin and collision surfaces, the REG-05 regional overlay and force contracts, existing Event 006 package patterns, and the required read-only HOI4 MCP inspections.

## Disposition

The installed map provides a valid unique KHA anchor at state 569, so the geographic reservation prerequisite is viable in isolation.

The package is not currently viable for Event 006 admission or implementation. KHA has no Event 006 package-local mechanics, no accepted identity or leadership provenance, no package flag, no KHA focus callbacks, and no package-local localisation, ideas, decisions, AI, or asset handoff. The registered vanilla tag must remain dormant unless the parent-owned readiness and origin gates pass.

Do not widen central admission, attestation, preflight, or Join for this candidate. Do not reserve state 569 while the origin, rights, identity, and host-remnant gates are unresolved.

## Authority and registry findings

The source-of-truth registry row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:55` for `IW-054`, Khakassia, tag `KHA`, Level 1, registered-tag reuse, `RG-KHAKASSIA`, REG-05, and the compact Khakass anchor contract.

The resolved research row is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:55`. It requires a current-map Khakass or Minusinsk group, an automatic unique-state pool, autonomous-republic or local institutional framing, and a sourced real male period leader or authentic archival provisional institution. It explicitly blocks when the leadership gate cannot be supported.

The reservation row is `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:86`. `RG-KHAKASSIA` allows one state at most, requires a unique anchor, requires the tag not to be living, requires a successful host-remnant test, and forbids taking a protected capital when a safe package exists.

The force contract is `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:55`: `mounted_mobile`, force level 55, cavalry and local guards, reconnaissance and engineers, rail-dependent logistics and artillery, a mounted reserve inspector, locally vetted junior officers, and no inherited navy or air force package.

The regional contract is `docs/specs/006_independence_wave_specs/matrices/006_regional_overlay_matrix.csv:6` (`REG-05`). It requires distance, multiethnic territory, rail and river dependence, extraction and isolated industry, railway troops or cavalry, cold-weather and frontier units, and federal, traditional, socialist, or military railway government options without flattening distinct peoples or granting empty territory automatically.

## Country package coverage checklist

| Surface | Result | Evidence and disposition |
| --- | --- | --- |
| Tag registration | Present in vanilla; no Event 006 registration needed | Vanilla `common/country_tags/00_countries.txt:251` maps `KHA` to `countries/Khakassia.txt`. The Event 006 registered-tag reuse contract forbids duplicate registration or replacement of the vanilla country file. |
| Country definition | Vanilla base only | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\countries\Khakassia.txt` contains graphical cultures and color only. No package-local identity layer exists. |
| Country history | Vanilla dormant carrier | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\KHA - Khakassia.txt:1,5,29-30,84-99` sets capital 569, two research slots, broad generic starting technology, mass assault and fleet-in-being doctrines, democratic elections, and 70/20/10 democratic/communist/neutrality popularity. It has no opening OOB and no character recruitment. Preserve this as the unadmitted vanilla branch. |
| State and anchor | Map-valid, host remnant required | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\569-TS 11.txt:3-36` defines state 569, 1,567,322 manpower, 16 coal, town category, owner/core SOV, core KHA, three victory points, 13 provinces, infrastructure 2, one industrial complex, and local supplies 0.0. Current binding confirms `569=KHAKASSIA`, `569=SOV`, and `SOV=219` retains a protected remnant. |
| Origin and readiness | Missing | The central candidate tag gate requires `independence_wave_package_content_ready`; no KHA package-local content-ready flag or parent attestation exists. |
| Event 005 collision | Blocking until runtime origin is checked | Event 005 can release KHA through its KMB concession route and assign KHA an Event 005 origin. KHA must remain excluded whenever that route is active or KHA is already living. |
| Leadership and roster | Blocking | No KHA character file, KHA history recruitment, or KHA country-leader definition was found in vanilla. The research gate requires a sourced real male period leader or authentic archival institution. No leader, institution, portrait, or gender metadata may be invented here. |
| Flags | Vanilla assets exist; provenance unresolved | Vanilla has `gfx/flags/KHA_communism.tga`, `KHA_democratic.tga`, `KHA_fascism.tga`, and `KHA_neutrality.tga`. Reuse is allowed only after the released identity/origin matches and source review accepts the route. No new flag or asset was produced. |
| Politics and parties | Vanilla fallback only | Vanilla KHA localisation defines regime variants and party names, but no Event 006 government archetype, rights model, recognition state, patron relationship, or package-specific party setup exists. |
| Focus tree | Shared tree exists; KHA route absent | The shared tree is `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt`. Its package callback sites contain no KHA helper or KHA callback. Adding those callbacks is shared-tree feature work, not a safe audit patch. |
| Decisions and missions | Missing | No `006_independence_wave_kha_decisions.txt` or KHA category exists. The REG-05 and IW-054 contract needs compact-anchor, rights, rail/depot, guard, and integration behavior before admission. |
| Ideas and starting problem | Missing | No `006_independence_wave_kha_ideas.txt` exists. The package needs a distinct regional council, traditional, socialist, or patron-client setup and a play-addressable starting weakness. |
| Forces and OOB | Missing | Vanilla KHA has no OOB. The accepted force contract requires dynamic mounted local guards, reconnaissance and engineers, rail-dependent support, and an institutional territorial command; this is not present. |
| Technology | Vanilla generic only; viewer limitation | Vanilla history supplies broad generic technology and two research slots, with no KHA-specific technology dependency. The installed package exposes no Technology Tree Viewer, so no technology-tree MCP evidence can be claimed. |
| Industry, supply, and production | Map baseline only | State 569 has infrastructure 2, one industrial complex, 16 coal, and local supplies 0.0. No KHA production lines, depot, rail, supply, or recovery contract exists. |
| AI and weighted behavior | Missing and unresolved | No KHA AI strategy file exists. The mandatory probability inspect recognized KHA as a random-list candidate, but no runtime scenario was supplied and the `chaosx_ai_probability_auditor` route is not callable in the installed tool set. No quantitative weight or balance claim is made. |
| Localisation | Vanilla carrier only | Vanilla country, adjective, and party keys exist. No KHA package keys for ideas, decisions, focus callbacks, forces, rights, recognition, or institution names exist. |
| Assets and manifests | Missing package handoff | No KHA portrait/source evidence, package asset manifest, focus/idea/decision icons, or new flag was produced. |
| Documentation | This handoff only | This file is the durable viability handoff. No implementation documentation was added because no package implementation was accepted. |

## Exact file and contract surface

The central Region 05 planner and reservation are already present in `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt:88-95` and `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:118-128,168,197`. The planner requires the package content-ready tag gate and state 569 anchor availability, and the reservation takes only state 569.

The central Region 05 weighted pool is `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:202-216`. KHA is the eleventh parsed candidate entry (`202.entry.11`). This is an existing central surface and was not edited.

The central origin and tag gates are `common/scripted_triggers/006_independence_wave_package_triggers.txt:9-49`. They exclude unavailable owners, reserved or protected states, living or reserved tags, Soviet Collapse origin, Event 006 origin, and Event 012 state before requiring the package content-ready flag. The KHA package cannot bypass these checks.

There are no KHA package-local files for constants, scripted triggers, scripted effects, ideas, decisions, decision categories, AI strategy, characters, focus callbacks, package localisation, or package assets. Existing package-local patterns in `common/scripted_effects/006_independence_wave_sakha_package_effects.txt`, `common/scripted_triggers/006_independence_wave_sakha_package_triggers.txt`, `common/ideas/006_independence_wave_sakha_ideas.txt`, `common/decisions/006_independence_wave_sakha_decisions.txt`, `common/ai_strategy/006_independence_wave_sakha.txt`, and their Buryatia counterparts are references only; copying them would constitute an unapproved country package implementation.

## Event 005 origin and collision gates

Event 005 has an explicit KHA collision path in the KMB basin route:

- `common/scripted_triggers/005_soviet_collapse_triggers.txt:8068-8087` requires KMB and KHA to be absent before the KMB basin spawn path can proceed and requires state 569 to be owned and controlled by the acting scope.
- `common/decisions/005_soviet_collapse_decisions.txt:13792,13800` keeps KHA absent for the KMB basin policy and references state 569 resource rights.
- `common/scripted_effects/005_soviet_collapse_effects.txt:22103-22118` adds KHA cores in the basin, releases KHA as a puppet, transfers state 569 to KMB, sets KHA capital 570, marks the Soviet Collapse event-created republic, and grants concession/resource rights.
- `common/scripted_effects/005_soviet_collapse_effects.txt:5664-5727` marks or clears the Event 005 active origin and `liberation_origin.soviet_collapse` state.
- `common/scripted_effects/005_soviet_collapse_effects.txt:10525-10532` loads the Event 005 event-created focus tree only when its republic flag is present and the Event 006 origin is absent.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt:14-19,2669-2670,3125-3130` excludes Event 006 active, reserved, or protected states and identifies Event 005 breakaway countries.

This means a normal dormant KHA carrier can be an Event 006 candidate only after the parent-owned origin and content gates pass, while a KHA created by Event 005 must remain on the Event 005 branch. Do not clear, override, or reinterpret the Event 005 origin flags from a KHA package patch.

## Focus, event, map, and probability MCP evidence

The required read-only MCP routes were run before reporting these surfaces.

Map inspect on state 569 and its 13 provinces returned `MAP_INSPECTED` with revision `633fcc8140a534c23405c15068df2e1d276d21dc5d4f8f167092a52c229c8f80`. Useful artifacts are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f982c2215d801918863c99387333a772312de2209cd24dfb3e2d9e7684a822a5/0ca25a75dddcc0dd5f4924aa1fec3e2732a8ab9cac6408efdbcddeaf19e02857/map-inspect.633fcc8140a534c2.json`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b7cd416f3ddc46906d5abcaa64e6e9317937c0f86f16dbae5771da335e67d9d7/ab7d63ad97ea1aa3c8ac35cc0c038bda50e143ef2468c52bc9ed67ede3bcda7c/map-province-geometry.633fcc8140a534c2.5f51e9a5387c4213.json`

The selected state and province membership checks passed with no unknown or missing province IDs. The report also contains unrelated global `map/buildings.txt` and port-position diagnostics; those are not KHA state failures and must not be attributed to state 569.

State-layer rendering with victory points, resources, buildings, railways, adjacencies, and supply-node overlays returned `MAP_RENDERED` and a valid PNG at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f3b337cbf767ad752f644cd254ee19447b8043089ef533606e789b3d5114aec/2b3ed103a1a1986632e4e3ea1ab43aa0776b7d97d17a0872db6e7cfdb11191e8/map-state.png`.

Focus inspection and rendering of `common/national_focus/006_independence_wave_focus.txt` and tree `independence_wave_focus_tree` returned a 184-node tree. Artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d3aa67b99e5d21bac5c5e637f0f1d47fa403cfa5e07bb34c99f383249b0758a/a8021880d4ad1810d27f5574d93ea4d6ea24611e39ebc9ff3cbbb8fb4f64221e/focus-inspect.38c9d173690ad592.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f73f5fb95e7f196377f3499cfaea352fd42460cf29e4e2b57ec55db429c00c22/be570069ae325834c36f88fc5b4ba8f31450ce25781f48c858eedf54cbb633db/independence_wave_focus_tree.focus.html`. The tree has unrelated missing vanilla continuous-focus sprite diagnostics, but no KHA callback surface. KHA-specific callback additions would require a future accepted package tranche and shared-tree ownership; none were made.

Event inspection and rendering of root `chaosx.nr6.1` returned partial workspace analysis with zero blocking diagnostics. Artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/699dfeefb7e3f2a79cb998b8d178b06674c0091a8bdb24025ce7f125372263d6/9bd7466ea16a4da4c556818f6e8b7855a664f8711a0f288b34439e29cd7dae8c/event-roots-741883f50501.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9a7b6b2a4e6b16562861666087c2954d306211081c25b4b292bcd2088a486bef/fffe48b4db3adaae0c72d9b3229c226d2f78e77d0b9c0725f5301d2aff787e37/event-overview-741883f50501-manifest.json`. The partial result is a workspace-analysis limit, not evidence that a KHA event chain exists.

The mandatory probability pass started with `hoi4_probability_inspect` and first returned the exact adapter input error that a custom weighted-pool adapter requires a source. Source discovery and random-list inspection then succeeded for `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt` and recognized 12 candidates. The useful artifacts are:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/73c127bcaf92a05980b3d35ba9c24ec65b5dca5def5bf760c8b66110819a2c16/4dc146ee55e72fdd3d34e2552f0ef4c16f364c722cad79957e443c02b7e20d53/probability-inspect-578028cf856f.json` for source discovery.
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef917dbe11d821cf1a6e4c77b06221ae3fac120cce218717194f78763ac4bebc/62ffea3e97f80b45ecba050090daea236eeb7427d9822f86889923b70cc8a197/probability-inspect-578028cf856f.json` for the 12-entry pool inspection.
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28f43dee4651bd03c207dfbe3f582a6e4e66f87dd731964d1a7cd05559dcaec2/90b2e77caac253d356adc3134947c172557a2d6aa4a846d05deec91f779e64f9/probability-inspect-578028cf856f.json` for exact KHA entry `202.entry.11` recognition.

The exact KHA inspection had one required runtime input and no unresolved parser input, but it did not calculate a runtime probability. The installed callable tool set has no `chaosx_ai_probability_auditor`, so no auditor-backed evaluate, sweep, simulation, or probability compare is claimed. Weighting remains unresolved until the parent can provide the required auditor route and named runtime scenarios.

## Safe next-owner surface

After identity, rights, and admission are separately accepted, the package owner may implement the bounded KHA package-local surfaces in new files such as `common/script_constants/006_independence_wave_kha_constants.txt`, `common/scripted_triggers/006_independence_wave_kha_package_triggers.txt`, `common/scripted_effects/006_independence_wave_kha_package_effects.txt`, `common/ideas/006_independence_wave_kha_ideas.txt`, `common/decisions/006_independence_wave_kha_decisions.txt`, `common/ai_strategy/006_independence_wave_kha.txt`, package-local localisation, and character/asset manifests. Those files must be grounded in the accepted identity and force research and must follow the existing Sakha/Buryatia package contracts without copying their identities.

The parent retains ownership of central readiness, attestation, preflight, Join, shared focus callback registration, shared regional pool changes, and final map reservation/application. A future package tranche must gate every KHA mechanic on the package origin flag, preserve the Event 005 branch when its origin is active, and prove the host remnant before reserving state 569.

## Blockers, uncertainty, and explicit omissions

- Leadership and identity provenance are unresolved. The vanilla KHA name pool in `common/names/00_names.txt` is not a historical leader roster and cannot satisfy the sourced-leader gate by itself.
- No KHA character or portrait source evidence exists. No portrait archive or runtime placeholder was created; any later portrait work must be routed to `chaosx_portrait_creator` and must follow the parent archive convention.
- Package-local ideas, decisions, AI, forces, localisation, and mechanics are absent. Creating them would be a broad country-package implementation, not a safe bounded audit patch.
- The shared focus tree has no KHA callbacks. Shared focus edits were intentionally omitted.
- Event 005 can make KHA a living event-created puppet and can claim the same state group. Event 006 must remain fail-closed against that origin.
- The technology dependency is limited to vanilla history. The installed package exposes no Technology Tree Viewer, so technology-tree completeness remains an unresolved tooling limitation rather than a passing claim.
- Probability runtime values and comparison evidence are unresolved because the auditor route is unavailable and no scenario was supplied. No weight was changed.
- No map rewrite, reservation, central adapter, attestation, preflight, Join, or asset generation was performed.

There are no changed gameplay files and no before/after behavior to report. This handoff is the only file added for the audit.
