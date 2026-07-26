# IW-007 Frisia (AGX) country-package re-audit - 2026-07-26

## Scope and disposition

This is a fresh bounded, read-only audit after commits `8c15baa17`, `c9337fd94`, `79663734e`, and the documentation refresh `032d36550`. It covers the AGX/Frisia tag, state 36 and RG-36 setup, origin purity, host survival, Event-005 collision protection, starting force and technology inheritance, politics, leaders, portraits, flags, ideas, all visible waterline/coastal/host/network/league/formable values, focus assignment and the eight-focus overlay, decisions and mission lifecycle, AI, formable integration, cleanup, localisation, and exact runtime attestation.

**Bounded package disposition: PARTIAL.** AGX identity, map binding, origin/setup proof, force mapping, politics, portraits, flags, ideas, focus overlay, formable hooks, cleanup, AI, localisation, and static runtime admission all pass their package checks. The AGX decision lane remains **HOLD** because the North Sea conference timer has one high lifecycle/route-lock defect and its visible strategic cost understates the reserved civilian-factory commitment. A low player-facing trigger-tooltip gap also remains.

The eight-focus AGX overlay is **PASS for package wiring** and **PARTIAL for the shared tree**: all eight IDs, effects, prerequisites, bypasses, AI weights, icons, and localisation are present, while the pre-existing shared focus layout still has fourteen blocking geometry diagnostics. The source-of-truth map and v7 completion addendum still describe the pre-overlay AGX module gap; those statements are stale for the narrow overlay but remain correct that whole-tree completion is HOLD.

The exact IW-007 runtime content attestation is **PASS at compile-time source level**. Static attestation does not prove that a live automatic or scenario allocation has passed its host, anchor, reservation, chaos-band, force, and transaction witnesses, and no live game or save-load run was performed in this subagent scope.

No gameplay, map, GFX, localisation, or asset source was changed by this audit. The only intended change is this handoff document.

## Authority and review basis

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` remain the package authority for the admitted IW-007 row, state-36/RG-36 binding, HOL survival, retry-02 portrait pair, and exact attestation requirement.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wallonia_frisia_package_handoff.md` is the accepted package contract for constitutional, popular-council, and patron-client routes, negotiation/guarded-frontier/association host routes, the labor-councils-versus-ministries struggle, the coastal-maritime force, the North Sea league hook, and the Low Countries Federation hook.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_focus_overlay_handoff_2026_07_26.md` is the accepted eight-focus implementation handoff and records the parent-owned `hoi4.focus_inspect`/`hoi4.focus_render` artifacts.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_decision_mission_reaudit_2026_07_26.md` is the current narrow decision authority and supplies the two unresolved AGX decision findings recorded below.
- `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_26.md` reports zero Event-006 tag and custom-cosmetic collisions across the scanned vanilla, Workshop, archive, sibling-mod, and Chaos Redux registries.
- The required offline Paradox wiki pages and the relevant vanilla HOI4 documentation were read before inspection, including data structures, triggers, effects, modifiers, localisation, scopes, on actions, event/decision/idea/AI modding, country creation, national focuses, states, portraits, graphical assets, maps, and the corresponding vanilla documentation files.

## Country-package coverage checklist

| Surface | Result | Current evidence and identifiers |
| --- | --- | --- |
| Tag registration and identity | PASS | `common/country_tags/006_independence_wave_countries.txt:17` maps `AGX` to `countries/006_independence_wave_AGX.txt`; `common/countries/006_independence_wave_AGX.txt` owns western-European graphical cultures and `rgb { 48 116 170 }`; English country localisation covers `AGX`, `AGX_DEF`, `AGX_ADJ`, and all ideology forms as Frisia/Frisian. |
| State, map, owner, controller, core, capital, resources, buildings | PASS | Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/36-Friesland.txt` starts `owner = HOL`, `add_core_of = HOL`, four victory points, infrastructure 2, two civilian factories, naval base 3, manpower 2,364,000, and city category. IW-007 preparation and prepared proof require state 36 to be owned and controlled by AGX and to remain the capital. No map write was attempted. |
| Binding, reservation, and host survival | PASS | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:8` binds IW-007/AGX to unique state 36, Friesland, RG-36, and `36=HOL` with HOL retaining at least one state; `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:84-97,281-287` loads and reserves only the frozen anchor. |
| Origin purity and setup | PASS | `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:43-64,233-289` requires exact `iw_007`, northern/western Europe, standard depth, `port_or_island`, event-targeted anchor and former host, baseline laws, roster, routes, focus assignment, formable readiness, force mapping, AI, and state-36 capital. The shared preflight rejects Soviet-collapse and active-origin flags/variables before the AGX identity branch. |
| Event-005 collision protection | PASS | `common/scripted_triggers/006_independence_wave_triggers.txt:508-552` defines country, anchor, and host clearance helpers; `:696-720` requires AGX, state 36, HOL host clearance, no duplicate selected country/anchor/group, then records `iw_007`, AGX, 36, and RG-36 in aligned capacity arrays. |
| Politics, parties, routes, and ideas | PASS | `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:216-364,793-839` initializes the 60/20/15/5 AGX political profile, party names, Kalma leadership, provisional authority, three allowed government routes, three allowed host routes, no emergency/traditional/radical/reclamation route, and the labor-councils-versus-ministries struggle. |
| Leaders, commander, gender, portraits, and names | PASS | `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-126` defines male `AGX_friesland_coastal_council` and male corps commander `AGX_friesland_coastal_commander`; localisation names are Douwe Kalma and Pieter Reenalda. No opposite-gender pool, female metadata, institutional/personal mismatch, or rejected candidate-01 consumer remains. |
| Flags and country assets | PASS | `gfx/flags/AGX.tga`, `gfx/flags/medium/AGX.tga`, and `gfx/flags/small/AGX.tga` exist; portrait sprites are registered at `interface/006_independence_wave_region_01_portraits.gfx:19-24`; the approved retry-02 runtime DDS pair is present at the exact stable paths. |
| Waterline, coastal, host, network, league, and formable values | PASS | `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:42-43,72-73,159-180` exposes AGX Waterline Integrity and Coastal Security and describes every overlay reward, Network Standing, League Cohesion, Common Cause, Shared Reserve, Member Confidence, and Low Countries Federation handoff. `localisation/english/006_independence_wave_gui_l_english.yml:6-17` exposes founding values, host Claim/Hostility/Obligations, patron influence, network standing, and league phase. `localisation/english/006_independence_wave_decisions_l_english.yml:17` exposes the global league ledger values. Form-03 AGX-specific dynamic bands are in `localisation/english/006_independence_wave_form03_l_english.yml:23-44` and `common/scripted_localisation/006_independence_wave_form03_scripted_localisation.txt`. |
| Focus assignment and AGX overlay | PASS package / PARTIAL shared tree | `common/scripted_effects/006_independence_wave_focus_effects.txt:35-43` assigns the full framework and `common/scripted_triggers/006_independence_wave_focus_triggers.txt:32-42` validates it. `common/national_focus/006_independence_wave_focus.txt:2458-2679` contains exactly eight unique AGX IDs, from waterline charting through the Low Countries dossier, with package gates, route/former-host/network/conference prerequisites, bypasses, AI weights, and reward hooks. Static source count is 198 unique focus IDs with no duplicates and exactly eight AGX IDs; the overlay handoff records 184 resolved focuses/titles in the parent-owned MCP artifact. The shared baseline still records fourteen layout blockers. |
| Decisions and mission | PARTIAL / HOLD | `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:309-607` contains the 540-day `independence_wave_agx_hold_the_waterline` mission, four opening projects, former-host records, three mutually exclusive government decisions, and the North Sea conference. The mission and most projects are coherent, but the conference has the High and Medium defects in the decision findings section. |
| Form-03 and Low Countries Federation | PASS | `common/scripted_triggers/006_independence_wave_form03_triggers.txt:32-71,202-265` requires the exact AGX state-36 anchor, capital, compatibility, consent, readiness, X-tag, flag, identity, integration, and member-policy attestations. `common/scripted_effects/006_independence_wave_form03_effects.txt:85-177` transfers/cores only consenting AFX/AGX anchors and preserves BEL/HOL/LUX as sovereign associates. |
| Starting force, technology, industry, supply, production, and research | PASS | `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:274-287` requires mapping package `iw_007`, `coastal_maritime`, p7 tradition, force package, and applied flag. Runtime constants are p7 profile 5 (`common/script_constants/006_independence_wave_force_package_constants.txt:72-85`), tradition 45 (`:286-298`), reinforcement mask 1047 (`:500-512`), inheritance mask 0 (`:714-726`), and research-sensitive 0 (`:928-940`). `common/scripted_effects/006_independence_wave_force_effects.txt:790-803,869-889` inherits host technology and minimum/industrial research slots, calculates population/factory/infrastructure/rail/port/supply/host inputs, builds the coastal template and opening divisions, adds bounded stockpiles/fuel, and transfers only approved small naval/air fractions. |
| AI and playability | PASS package / narrow route caveat | `common/ai_strategy/006_independence_wave_wallonia_frisia.txt:78-133` gates coastal survival, founding restraint, severe-host response, and civic coastal policy to AGX setup and AI flags, with priorities for army, infantry, support, trains, convoys, infrastructure, coastal bunkers, factories, and war restraint. All eight overlay focuses have `ai_will_do`; no focused probability sweep was available in this read-only pass. |
| Cleanup and replay safety | PASS | `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:950-998` removes the mission and all nine AGX decisions, removes AGX ideas, clears waterline/coastal variables, calls Form-03 cleanup, and clears every AGX route/project/focus/network/formable/AI/setup/lifecycle flag including conference authorization. Shared transaction cleanup remains responsible for global active-country, host, origin, and aligned-array registries. |
| Localisation and visible text | PASS package / LOW tooltip gap | Party, country, leader, commander, idea, category, mission, decision, focus title/description/effect-tooltip, status-GUI, league, and Form-03 keys resolve in the reviewed files and the AGX localisation file retains its BOM. The AGX decision/focus availability blocks do not all expose custom player-facing trigger tooltips for route, capital, former-host, project-lock, and conference-foundation requirements. |
| Exact runtime admission | PASS static / live unproven | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-30` includes the IW-007 adapter, `:55-68` includes `iw_007` in the content-attestation OR, `:70-79` applies dormant/origin safety, and `:93-100` binds `iw_007` exactly to `original_tag = AGX`. The scenario preflight also requires the same content attestation and exact IW-007/AGX identity. `common/scripted_triggers/006_independence_wave_triggers.txt:442-450` is the automatic IW-007 readiness branch. |

## File-surface checklist

- Tag and country shell: `common/country_tags/006_independence_wave_countries.txt:17`, `common/countries/006_independence_wave_AGX.txt`, and `history/countries/AGX - Frisia.txt:12-18`.
- Vanilla anchor and host: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/36-Friesland.txt` and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:8`.
- Setup/proof/cleanup: `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:538-694,793-883,950-1008` and `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:14-75,105-172,233-316`.
- Politics, ideas, parties, and constants: `common/ideas/006_independence_wave_wallonia_frisia_ideas.txt:111-167`, `common/script_constants/006_independence_wave_wallonia_frisia_constants.txt:9-101`, and `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:5-73`.
- Characters and portrait consumers: `common/characters/006_independence_wave_wallonia_frisia_characters.txt:81-126`, `interface/006_independence_wave_region_01_portraits.gfx:19-24`, `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds`, and `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds`.
- Flags: `gfx/flags/AGX.tga`, `gfx/flags/medium/AGX.tga`, and `gfx/flags/small/AGX.tga`.
- Focus assignment and overlay: `common/scripted_effects/006_independence_wave_focus_effects.txt:35-43`, `common/scripted_triggers/006_independence_wave_focus_triggers.txt:32-42`, `common/national_focus/006_independence_wave_focus.txt:2458-2679`, `interface/006_independence_wave.gfx:3-26`, and `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:157-180`.
- Decisions and category: `common/decisions/categories/006_independence_wave_wallonia_frisia_categories.txt:12-13` and `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:309-607`.
- Form-03: `common/scripted_triggers/006_independence_wave_form03_triggers.txt:32-71,202-265`, `common/scripted_effects/006_independence_wave_form03_effects.txt:85-177,287-310`, and `localisation/english/006_independence_wave_form03_l_english.yml:3-44`.
- Force and AI: `common/script_constants/006_independence_wave_force_package_constants.txt:72-85,286-298,500-512,714-726,928-940`, `common/scripted_effects/006_independence_wave_force_effects.txt:790-803,869-889`, and `common/ai_strategy/006_independence_wave_wallonia_frisia.txt:78-133`.
- Runtime and collision: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-100,163-190`, `common/scripted_triggers/006_independence_wave_package_triggers.txt:55-92`, and `common/scripted_triggers/006_independence_wave_triggers.txt:442-450,508-552,696-720`.

## Decision and mission findings

### High - conference completion is not cancelled when route or public eligibility changes

`independence_wave_agx_convene_north_sea_coastal_conference` at `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:575-607` checks stable waterline, recognition, network membership, Low Countries candidacy, conference authorization, no client-route lock, capital control, and no competing project before starting.

Its active `days_remove = constant:independence_wave_decision_duration.strategic` is 300 days (`common/script_constants/006_independence_wave_decision_constants.txt:24`), but its `cancel_trigger` at `:600` checks only AGX package identity, stable waterline, and capital control.

If the player loses recognition, network membership, Low Countries candidacy, the authorization flag, or route eligibility through a client lock after starting the timer, the decision can still reach `remove_effect` at `:599`, set `independence_wave_agx_north_sea_conference_complete`, grant `independence_wave_nwe_reward_regional_conference`, and unlock the downstream dossier focus.

This is a one-time reward/route-bypass defect rather than an infinite farming loop. The current decision authority recommends extending the continuing cancellation conditions and choosing an explicit no-reward cancellation outcome. No gameplay fix was applied in this read-only country audit.

### Medium - visible strategic cost understates the factory commitment

The same conference uses `modifier = { civilian_factory_use = constant:independence_wave_decision_cost.civilian_factory_major }` at `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:596`, and `civilian_factory_major = 3` is defined at `common/script_constants/006_independence_wave_decision_constants.txt:141`.

Its `custom_cost_text = independence_wave_cost_strategic` at `:595` resolves to `localisation/english/006_independence_wave_decisions_l_english.yml:33`, which displays `civilian_factory_standard = 2` from `common/script_constants/006_independence_wave_decision_constants.txt:140`.

The availability helper and active commitment therefore require/reserve three factories while the player-facing cost string says two. This is a balance/clarity defect in the AGX conference surface, not a missing package mechanic.

### Low - availability trigger explanations are incomplete

The AGX projects, government decisions, mandate focus, and conference expose readable descriptions and cost text, but their `available` blocks do not consistently wrap route, capital, former-host peace, project serialization, recognition, network, candidacy, and authorization requirements in custom trigger tooltips. The strings are not missing, but the player is not always told why an action is unavailable. This remains a quality follow-up rather than a runtime blocker.

## Map, origin, formable, and cleanup findings

State 36 is a valid distinct coastal anchor with HOL as the starting owner/core and RG-36 as its reservation group. The package setup keeps the former host as a non-ROOT event target and the prepared proof requires state 36 ownership/control and capital state 36. No static AGX state history claims territory, adds a core, creates an OOB, or overwrites HOL.

The shared exact-package preflight rejects `soviet_collapse_active_origin`, a Soviet-collapse `liberation_origin`, and `independence_wave_active_origin` before accepting `iw_007`/AGX. The AGX exact identity helper requires candidate-origin availability and `original_tag = AGX`, while the runtime automatic branch additionally requires AGX dormancy, state-36 anchor availability, and the package content attestation.

Form-03 readiness is not a cosmetic shortcut. `has_independence_wave_form03_readiness_attestation` requires a low-countries family, progression/readiness flags, territory adapter, reserved X tag, flag package, identity/integration adapters, and audited member policy. The integration effect transfers/cores only a consenting AFX or AGX anchor and leaves BEL/HOL/LUX sovereign associates.

AGX cleanup removes all package-local decisions, mission, ideas, waterline variables, Form-03 runtime state, route-government flags, project flags, conference authorization/completion, focus reward flags, AI profile, low-countries candidate, North Sea link, formable-family selection, and setup/lifecycle markers. Shared transaction cleanup still owns global active-country, host, origin, and network arrays; this is an intentional dispatcher boundary, not an AGX omission.

## Politics, leaders, portraits, flags, ideas, and visible values

AGX starts with the documented 60 democratic, 20 communist, 15 neutrality, and 5 fascist profile, four base party-name keys, Kalma as the route leader, and only constitutional, popular-council, and patron-client government choices. The setup clears traditional, emergency-military, radical-sovereignty, and host-reclamation availability, preventing an opposite-route leak.

The retry-02 portrait authority remains the two selected sourced real male subjects. The civilian DDS is Douwe Kalma at SHA-256 `2A98ECB576B331915E2B626C9CCC6DC03AF4012A411717B73D2F5253358E15A2`, and the commander DDS is Pieter Reenalda at SHA-256 `07689A7045C145401E5AA7A2CFC1AE0949D59C62D4B64F144714E20197558BBA`. The independent visual audit passes Kalma and Reenalda candidate-02 and fail-closes candidate-01; no live candidate-01, female, advisor, dossier, or `_small` AGX consumer was found outside historical documentation.

The five AGX ideas are `agx_exposed_waterline`, `agx_dike_and_coast_authority`, `agx_constitutional_water_board`, `agx_coastal_labor_councils`, and `agx_patron_harbor_mandate` at `common/ideas/006_independence_wave_wallonia_frisia_ideas.txt:111-167`. Their lifecycle is AGX-gated, their exposed/mature modifiers cover stability, building production, supply consumption, army organisation, political power, research, industrial capacity, efficiency, and consumer goods, and cleanup removes every one.

The category and status GUI expose live Waterline Integrity, Coastal Security, founding values, host Claim/Hostility/Obligations, patron influence, Network Standing, league phase, League Cohesion, Common Cause, Shared Reserve, Member Confidence, and Form-03 carrier values. The focus and decision tooltips describe deltas and preserve the consent/ratification boundary rather than presenting formable discovery as automatic annexation.

## Focus, decision, idea, and asset issues

The eight package focuses are:

- `independence_wave_agx_chart_waterline_authority_focus`
- `independence_wave_agx_bind_dikes_pumps_harbors_focus`
- `independence_wave_agx_integrate_coastal_guard_focus`
- `independence_wave_agx_codify_water_board_government_focus`
- `independence_wave_agx_settle_water_board_succession_focus`
- `independence_wave_agx_open_north_sea_network_office_focus`
- `independence_wave_agx_mandate_north_sea_coastal_conference_focus`
- `independence_wave_agx_prepare_low_countries_dossier_focus`

Each focus has a title, description, effect tooltip, hidden effect, registered generic icon, package gate, and AI block. The route sequence reaches existing AGX effects/decisions/Form-03 hooks, and the mandate focus sets `independence_wave_agx_north_sea_conference_authorized` without paying or completing the conference. Commit `c9337fd94` then gates the paid conference decision on that authorization flag, and commit `79663734e` corrected the AGX reward tooltip wording.

The AGX lane itself has no duplicate focus ID or missing static title/description/tooltip/effect key. The shared tree still carries the recorded fourteen geometry blockers, and the current source-of-truth map, v7 addendum, documentation-curator handoff, and old focus handoff should be reconciled so they no longer say that the AGX narrow module is absent.

## Starting military, technology, industry, supply, production, and AI

The p7 runtime mapping is coherent: `coastal_maritime` profile 5, military tradition 45, reinforcement mask 1047, inheritance mask 0, and research-sensitive 0. The five-bit reinforcement mask is decoded by the shared force package and the prepared proof requires a generated force package plus the applied flag.

The dynamic force effect snapshots owned-state population, factories, infrastructure, railways, ports, supply nodes, former-host divisions/surrender/war state, chaos band, legitimacy, tradition, patron support, and network standing. It computes bounded divisions, equipment, trains, trucks, convoys, fuel, experience, manpower, and logistics, creates a coastal template, stamps package/generation provenance on created divisions, inherits host technology and research slots, and does not copy host land units or general stockpiles.

The accepted package handoff and current source use p7 tradition 45. A stale planning row at `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:8` still records IW-007 as tradition 44. This is documentation debt that should be reconciled against `common/script_constants/006_independence_wave_force_package_constants.txt:298`; it does not change the current runtime value or prepared proof.

The AGX AI profile is self-gated and self-aborting: coastal survival prioritizes army 60, infantry production 45, support 35, trains 30, convoys 30, infrastructure/coastal defense 90, and coastal bunkers 75; founding restraint uses -140 avoid-war weight unless severe host threat or regional-power conditions apply; host threat raises army priority to 100; settled civic routes retain -45 war restraint and industrial priority 45. The eight focus AI blocks add route-sensitive urgency and preference without bypassing their availability predicates.

## Exact runtime attestation and validation limits

The current static authority is `has_independence_wave_runtime_package_content_attestation_for_execution_id` at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:55-68`, where `constant:independence_wave_package_id.iw_007` is explicitly present. The exact identity branch at `:93-100` pairs `iw_007` with `original_tag = AGX`, and the adapter at `:10-30` includes IW-007. The preflight at `:70-79` rejects dormant-tag, Soviet-collapse, and active-origin violations. The scenario preflight at `:163-190` reuses the same attestation and exact IW-007/AGX identity helper.

The automatic allocator branch at `common/scripted_triggers/006_independence_wave_triggers.txt:442-450` sets the execution package to IW-007, checks AGX exact/ready identity and runtime preflight, and checks state 36 anchor availability. The Event-005-aware capacity branch at `:696-720` additionally protects country, anchor, host, selected arrays, and RG-36 uniqueness. The source therefore admits the exact runtime pair, but it does not attest that any particular future allocation has passed all live host, anchor, reservation, chaos-band, force, and four-pass transaction checks.

Meaningful validation performed here was source tracing of every AGX package surface, a static focus-ID uniqueness count (198 unique focus IDs, exactly eight AGX IDs), direct key/effect/title/description/tooltip coverage checks for all eight overlay focuses, direct portrait/flag/GFX path and file-presence checks, exact p7/force/attestation/collision searches, and review of the current decision re-audit. No map rewrite, gameplay launch, save-load run, scenario execution, focused AI/probability sweep, or live MCP technology-tree inspection was performed.

The installed HOI4 agent package exposes no Technology Tree Viewer. Technology coverage is therefore limited to the p7 constants, force effects/triggers, vanilla documentation, and the package proof; a viewer-based technology-tree inspection remains an unresolved tooling limitation.

## Missing, stale, or blocked surfaces

- **High gameplay defect:** Extend the conference cancel trigger to cover continuing recognition, network membership, Low Countries candidacy, authorization, and client-route lock conditions, then define the intended no-reward cancellation result.
- **Medium player-facing defect:** Reconcile the conference cost text with the three-factory major commitment, or deliberately change the modifier and gate to the standard two-factory contract.
- **Low UI quality gap:** Add named trigger tooltips for the AGX route, capital, former-host peace, active-project, recognition, network, candidacy, and authorization requirements.
- **Shared focus HOLD:** Keep the fourteen geometry diagnostics in the global completion ledger and schedule a coordinated layout repair; do not treat the eight-focus package lane as a substitute for that shared repair.
- **Documentation drift:** Reconcile the source-of-truth map, v7 addendum, and old focus handoffs that still state that the AGX/Frisia narrow module is missing; reconcile the stale p7=44 planning row; and correct the retry-02 `gfx_handoff.md` wording that says DDS conversion was deferred even though the approved DDS files are wired.
- **Runtime evidence boundary:** Static exact attestation is present, but no live automatic/scenario allocation or save-load proof was run in this subagent scope.

No fallback, alternate country identity, generated replacement portrait, new advisor, new focus route family, map mutation, or gameplay simplification was introduced. The AGX package remains suitable for parent review after the two decision-lane defects and the documented global/stale-evidence limitations are handled.

## Changed files and handoff

- Added only `docs/plans/006_independence_wave_plans/subagent_handoffs/006_agx_country_package_reaudit_2026_07_26.md`.
- No tags, states, leaders, parties, focus IDs, localisation keys, formable IDs, gameplay effects, decisions, missions, assets, or map data were changed.
- Recommended parent disposition is to retain the AGX package admission and exact static attestation, keep the package decision surface at HOLD until the High and Medium findings are resolved, and preserve whole Event 006 at HOLD.
