# Event 016 D'Rhonda country-package audit

> Historical country-package snapshot. The separate Alien Infantry package is now represented by the accepted V13 provider evidence and promoted static runtime registrations; its supported locator/effect, strict-audio, and live-acceptance gates remain open. Use the current Alien Infantry runtime handoff and promotion handoff for that shared package; retain this audit for D’Rhondan country evidence and limitations.

Date: 2026-08-25.

Owner: `/root/dhr_country_audit`.

Scope: the live DHR country tag, country definition/history, runtime revolt and enclave effects/triggers, characters, ideas, focus tree, decisions, events, AI, localisation, technology dependencies, and DHR visual registrations.

Status: static country-package audit complete with no gameplay-file patch. The package is conditionally acceptable at source level, but dynamic engine evidence, the required probability-owner pass, and user live acceptance remain outstanding.

## Files inspected

The requested filenames are represented by these live package files; no duplicate stale DHR source was found under the older expected names.

- `common/country_tags/016_dhrondan_country.txt`
- `common/countries/Empire of D'Rhonda DHR.txt`
- `history/countries/DHR - Empire of D'Rhonda.txt`
- `history/units/016_dhrondan_dormant.txt`
- `common/characters/016_dhrondan_characters.txt`
- `common/country_leader/016_dhrondan_traits.txt`
- `common/ideas/016_dhrondan_focus_ideas.txt`
- `common/ai_strategy/016_dhrondan_country_strategies.txt`
- `common/ai_strategy_plans/016_dhrondan_focus_ai.txt`
- `common/national_focus/016_dhrondan_focus_tree.txt`
- `common/scripted_effects/016_dhrondan_country_effects.txt`
- `common/scripted_triggers/016_dhrondan_country_triggers.txt`
- `common/scripted_effects/016_dhrondan_focus_effects.txt`
- `common/scripted_triggers/016_dhrondan_focus_triggers.txt`
- `common/decisions/016_dhrondan_country_decisions.txt`
- `common/decisions/016_dhrondan_contact_decisions.txt`
- `common/decisions/categories/016_dhrondan_country_categories.txt`
- `common/decisions/categories/016_dhrondan_contact_category.txt`
- `common/scripted_effects/016_dhrondan_contact_effects.txt`
- `common/scripted_triggers/016_dhrondan_contact_triggers.txt`
- `events/016_dhrondan_country_events.txt`
- `events/016_brilliant_scientist_dhrondan_contact_events.txt`
- `common/technologies/016_brilliant_scientist_project_technologies.txt`
- `common/technologies/016_brilliant_scientist_project_force_technologies.txt`
- `common/units/016_brilliant_scientist_project_forces.txt`
- `common/script_constants/016_dhrondan_country_constants.txt`
- `common/script_constants/016_dhrondan_focus_constants.txt`
- `common/script_constants/016_dhrondan_contact_constants.txt`
- `common/scripted_localisation/016_dhrondan_country_scripted_localisation.txt`
- `localisation/english/016_dhrondan_country_l_english.yml`
- `localisation/english/016_dhrondan_focus_l_english.yml`
- `interface/016_dhrondan_assets.gfx`
- `interface/016_dhrondan_focus_icons.gfx`
- `interface/016_dhrondan_portraits.gfx`
- `gfx/flags/DHR.dds`, `gfx/flags/DHR_IMPERIAL.dds`, `gfx/flags/DHR_SYNOD.dds`, and `gfx/flags/DHR_COVENANT.dds` with their medium/small ladders
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_portrait_package_handoff_2026-08-21.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_flags_event_art_handoff_2026-08-21.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_icon_asset_completion_handoff_2026-08-21.md`

The required offline Paradox wiki core pages, country/history/focus/decision/idea/AI/equipment/division/technology/character/portrait/GFX/map pages, and the relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` were read before this audit.

## Country-package coverage checklist

- [x] `DHR` tag registration and country-definition path agree at `common/country_tags/016_dhrondan_country.txt:8` and `common/countries/Empire of D'Rhonda DHR.txt`.
- [x] Dormant history is deliberately minimal and idempotent: `history/countries/DHR - Empire of D'Rhonda.txt:8-30` uses bootstrap capital state 1, empty OOB `016_dhrondan_dormant`, zero starting research/stability/war support, neutrality, and the twelve stable character IDs.
- [x] Runtime release is guarded by `dhrondan_revolt_transaction_lock`, validates the transferred capital, and sets `dhrondan_runtime_initialized` in `common/scripted_effects/016_dhrondan_country_effects.txt:461-499`.
- [x] The first release picks a host-owned passable marked landing state, transfers marked host-owned states, preserves the host core, adds DHR cores, and claims marked states not transferred in `common/scripted_effects/016_dhrondan_country_effects.txt:18-124`.
- [x] A global `dhrondan_origin_host` target is saved only once, preserving the first origin host for later enclave/reclamation content.
- [x] The three route regimes install leaders, party distributions, elections, cosmetic tags, and route flags through guarded effects at `common/scripted_effects/016_dhrondan_country_effects.txt:190-266`.
- [x] Twelve characters, five civilian advisors, one high-command officer, and three commanders resolve to stable localisation and portrait tokens.
- [x] Three lifecycle idea slots contain eleven ideas with clear-before-set helpers and DHR-only allowance.
- [x] The focus tree loads explicitly at runtime and has exactly 88 focus blocks with ten shortcuts and no DHR-specific MCP diagnostics.
- [x] Country and contact decisions, missions, event bridges, event localisation, decision icons, report/news pictures, flags, portraits, focus icons, and idea icons are present and statically wired.
- [x] Shared Alien Infantry technology and the paid 2,000-equipment landing contract are referenced rather than duplicated by DHR.
- [ ] Dynamic state/controller/core/capital transfer, runtime enclave component flood-fill, and actual unit materialisation have no current engine-run evidence.
- [ ] The mandatory `chaosx_ai_probability_auditor` pass is unavailable in the installed callable tool set, so no quantitative AI/probability acceptance claim is made.
- [ ] User-owned live/new-save acceptance and the separate Alien Infantry 3D model/entity/action/audio package remain outside this source audit.

## File surface checklist

Country tag, definition, history, OOB, character, leader-trait, idea, focus, focus-helper, trigger, decision, category, event, contact, AI-strategy, AI-focus-plan, constants, scripted-localisation, localisation, GFX, flags, portraits, and shared technology/unit surfaces were located and cross-referenced. No source patch was required. The only changed file in this handoff is this markdown report.

## Findings by surface

### Country identity, politics, leaders, portraits, flags, advisors, and parties

The fixed dormant tag is correctly registered as `DHR`. The country definition uses `western_european_gfx`, `western_european_2d`, and the D'Rhondan green colour. Cosmetic tags `DHR_IMPERIAL`, `DHR_SYNOD`, and `DHR_COVENANT` are defined in `common/countries/016_dhrondan_cosmetics.txt:7-22` and selected by the corresponding route effects.

The provisional regime installs Emperor Vael IX with neutrality and no elections. Imperial continuity retains Vael with 80 neutrality and 20 democratic popularity. The Synod installs First Calculant Sera Qel with the same neutral/technocratic distribution. The Covenant installs Speaker Ilyr Ren with 80 democratic and 20 neutrality, and enables elections. The country history starts neutral and dormant by design, while `dhrondan_initialize_country_runtime` supplies three research slots, 45 percent stability, 55 percent war support, the opening political-power grant, and the route regime after revolt.

The twelve IDs in `common/characters/016_dhrondan_characters.txt` all appear in history recruitment and localisation. Portrait-specific wiring resolves 21 full/role sprite tokens to existing DDS paths in `interface/016_dhrondan_portraits.gfx`. The portrait handoff records fictional native-ImageGen provenance, twelve full portraits, nine role cards, processing/DDS manifests, and parent visual approval in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_portrait_package_handoff_2026-08-21.md`.

No opposite-gender portrait/name pairing or female-leader metadata mismatch was found in the stable fictional roster. The approved roster uses fixed actual-ish fictional personal names rather than a runtime random-name pool and does not set gender metadata; this is a residual compliance question against the generic random-pool guidance, not an unambiguous source defect, so it was not changed without an accepted roster redesign.

All four DHR flag families have normal/medium/small DDS ladders. The flag and generated event-art handoff records the source and processed assets. No invented historical leader, symbol, or grounded-person substitution was introduced.

### Territory, cores, capitals, conservation, and origin-host/enclave behaviour

`dhrondan_capture_revolt_inputs` counts marked landing states and arrival receipts, chooses the first controlled passable host-owned landing site as `dhrondan_revolt_capital`, then falls back to a host-owned passable marked state under third-party occupation. `dhrondan_release_and_transfer_landing_states` releases DHR once, transfers host-owned marked states, preserves host cores, adds DHR cores, claims marked non-DHR states, and sets DHR's capital to the captured target.

The state transfer effect intentionally uses `transfer_state_to = DHR` when the host controls the state and `set_state_owner_to = DHR` when a third party controls it, allowing an occupied enclave to be born without silently granting control. The public state triggers in `common/scripted_triggers/016_dhrondan_country_triggers.txt:23-114` require DHR landing markers for reclamation, supply bridges, integration, and compact-related follow-up. Landing markers originate in the shared Alien Infantry API, which validates passable host-owned controlled states before setting `dhrondan_landing_state`.

The initial-force path prepares connected components of DHR-owned marked states outside the home area, deploys one cohort per component, concentrates remaining paid cohorts in the capital, and records supplemental floor extensions when more than fifteen components require a bounded extra cohort. The design is idempotent through `dhrondan_initial_force_consumed`, and the shared API debits/refunds exactly 2,000 `alien_laser_weapon_equipment_1` per successful/failed landing.

Remaining territory risk is evidentiary rather than a proven source bug: the MCP map route cannot execute the revolt transaction, so controller retention, host-core preservation, capital replacement, and disconnected-component behaviour still need runtime acceptance.

### Focus tree, decisions, events, ideas, and localisation

`common/national_focus/016_dhrondan_focus_tree.txt:25-41` defines `dhrondan_focus_tree`, selects DHR by `original_tag`, disables the default tree, positions the opening focus, and defines ten branch shortcuts. The source has exactly 88 unique focus IDs in these sections: survival 8, Imperial 8, Synod 8, Covenant 8, laboratory economy 10, predictive warfare 12, orbital support 8, diplomacy/intelligence 8, expansion/world order 12, and crisis/late game 6. The three route endpoints set the corresponding lifecycle spirit and route flag at `DHR_the_unbroken_imperial_line`, `DHR_the_government_of_certainties`, and `DHR_the_chamber_of_two_skies`.

The lifecycle ideas in `common/ideas/016_dhrondan_focus_ideas.txt:45-142` cover homeworld fragmentation/cohesion and the three regime outcomes, predictive lag/sight/command, and offworld isolation/relay/corridor. The focus helpers clear each prior slot before adding the replacement. Focus-created spirits therefore do not stack across route or progression changes.

The country decision file covers reclamation, disconnected-enclave supply support, postwar integration, and the Two-World Compact. The contact decision file covers Kruger/Mengele expeditions, accord honour, and the bounded rebellion pulse mission. Events `.40-.47` are contact/revolt follow-ups and `.48-.52` are DHR sovereignty/compact events. Event options revalidate targeted state/country legality and use the persistent diplomatic target cleanup effect.

Static localisation checks found all 88 focus IDs, focus shortcuts, country names/adjectives, party names, leaders, advisors, commanders, traits, ideas, decisions, missions, tooltips, and event/detail keys in the DHR English localisation files. The 88 focus icon tokens, eleven idea icon tokens, event/decision sprites, portraits, flag ladders, and referenced texture paths resolve through the installed GFX files. No dedicated DHR scripted GUI is introduced, so the dedicated GUI-worker/MCP route is not applicable.

### Starting military, technology, industry, supply, and production

The dormant OOB is intentionally empty. DHR receives no divisions, equipment, production, or normal Alien Infantry training before sovereignty. On revolt, `dhrondan_conserve_revolt_military_assets` removes any inherited `D’Rhondan Landing Cohort` and transfers the host's existing `alien_laser_weapon_equipment_1` stockpile with the documented `send_equipment = { target = DHR type = ... }` form. The runtime then grants the initial reserve, enables the landing contract, and deploys only cohorts that the paid shared API can materialise.

The shared hidden technology `brilliant_scientist_alien_infantry_tech` enables the alien laser equipment, while `brilliant_scientist_alien_predictive_warfare_tech` depends on it and enables the predictive tactics. DHR's runtime inherits a bounded set of the revolt host's technology before setting its own three research slots. No DHR-specific equipment archetype or division template is duplicated.

The focus effects add narrow civilian/logistics/air/lab/orbital capacity and research bonuses. One low-severity playability risk remains: `dhrondan_focus_add_orbital_dockyard` selects a random owned coastal state, so a fully inland post-revolt DHR can complete an orbital-support focus without receiving that building. This is an accepted design tradeoff in the current tree, not an unambiguous balance/scope patch.

### AI and playability

`common/ai_strategy/016_dhrondan_country_strategies.txt:9-27` enables Imperial, Synod, and Covenant role-ratio strategies by `original_tag = DHR` and route flag. `common/ai_strategy_plans/016_dhrondan_focus_ai.txt:13-176` supplies an opening plan plus one route plan per regime, each with route-specific focus queues, route gates, abort conditions, and focus factors.

The AI source is internally referenced and the route plan focus IDs resolve to the 88-focus tree. However, the required project `chaosx_ai_probability_auditor` is not exposed in the current callable tools (`ALL_TOOLS` search returned no country-package or probability-auditor worker). A direct `hoi4_probability_inspect` attempt on the focus AI surface timed out after the bounded 180-second tool limit, so no strategy-factor, focus-selection, event-chance, or rebellion-probability numbers are certified here. Parent review must retain this as an explicit blocker rather than treating source values as probability evidence.

### Assets and portrait-worker ownership

The DHR portrait handoff proves native ImageGen lineage, generated fictional source mode, processing, full/role DDS conversion, hashes, dimensions, GFX registration, and parent visual approval. The DHR flag/event-art handoff proves the four flag ladders and report/news assets. The DHR icon handoff proves 88 focus icons, eleven lifecycle idea icons, event/decision/project registrations, and binary validation. Runtime references point to the installed `gfx/` outputs and do not point into the durable archive.

The separate Alien Infantry 3D model/entity/action/audio package is not complete according to the Event 016 model handoffs. This is a shared package blocker for live visual/unit acceptance, not a DHR country-source defect.

## Exact MCP evidence

### Focus inspection and render

The installed `hoi4_focus_inspect` route was run against `common/national_focus/016_dhrondan_focus_tree.txt` with tree ID `dhrondan_focus_tree` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

- Status/code: `ok / FOCUS_INSPECTED`.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/243724a90804549398caeffa65b72c6c01b6ee6bbd26023c1d3b5eca9ec8e82e/da7496c5f5134b639c101f24ccaac2cf7fb66c7ac41d52dbf844342182c419e3/focus-inspect.81d1e4296be3e969.json`.
- Engine-style result: 88 focuses, zero DHR diagnostics, layout hash `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`, 102 connectors, zero crossings, zero node intersections, zero long connectors, bounds x=2..40 and y=0..22.

The installed `hoi4_focus_render` route also returned `ok / FOCUS_RENDERED` for the same source/tree. Useful artifacts are the rendered HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d8800e65fa05a8afcc74875ab7b4fa651c170c61601eada80f50f04e7d8a234/63fc6f79be1afd820a4a496b233f5d7b5d6abb93b80f4d1cf8bc2d1a98a3e722/dhrondan_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289/f0d3280e37d425ca80cab51db49f4b0aa76493f507261cc8b5e9bc1b665e82fb/dhrondan_focus_tree.focus.svg`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90b2ea0078cf3c08a0cc20bd77f18af76e2977da641565168c7b0396ab80be59/cf238b5b5399cd0be0b48d82fa27ebed515a2f19ae6e4d530d097c2b24213b12/dhrondan_focus_tree.focus.json`, and source-map/plan artifacts returned in the same response. Render dimensions were 6992x2788 with the same layout hash. The only reported validation text was the unrelated vanilla generic `continuous_restrict_freedom_desc` localisation warning.

### Events, map, technology, and weighted surfaces

The read-only Event Viewer calls for namespace `chaosx.nr16`, event `chaosx.nr16.47`, and reachability render returned `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` because the installed adapter scanned vanilla `game:` sources and did not ingest `mod:events/016_dhrondan_country_events.txt` or `mod:events/016_brilliant_scientist_dhrondan_contact_events.txt`. Useful partial artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4f1ec1ef194ac638c77a7fdb1f42df7353814b554fa013b2cf9f9dfce1e22fe/7cdc76bfa7cf157ec89255ae19653377846ea8bdf8917c69e464899fac6e4cb5/event-scan-7d541a2019d5.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10c1217414ea82e5ceb6db60a436e12a798916d4117891cbf01920a352aa16a4/5e3d954dd83a608c543cb627fd598eb633f3238b08781d22b1f9a5d2194fd90f/event-trace-7d541a2019d5.json`, and the reachability manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb4a7db209543d69819cc3b31b4f37166d3622ce8f7f76e1aa2613fa062c3132/e1e10b94aa02fc8e96c4496aeebfac6e8466eaf010e18e70f7a2c0a65cd5f0ef/event-reachability-7d541a2019d5.json`. These are limitation evidence, not DHR engine acceptance.

The read-only map inspect route returned `ok / MAP_INSPECTED` for selected state 1 and the map render route returned `ok / MAP_RENDERED` with offline representation and validated state/coast/port/supply/railway/adjacency layers. The useful inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b6d0a1ddd898650c84237a7a96fc6b5f6ac4080d58c4210f8b30560b6ec2b67/301774b4851772d8d831829721976b76ed8a118a5311a46461008ff284be666d/map-inspect.a5fbaddaf1dc54e3.json`, and the state render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2cf5a11d2dcbb08b9e1020ebcbb40bed717fdb9e0889ef9ad36d4d54edb369f/e2f405ec619c02adeafac0294eef7a27e83b3132ec16b68a8307f1d4e86c45fd/map-state.png`. The inspect validation was false because of unrelated workspace-wide invalid building positions and floating harbor adjacency diagnostics; the render itself passed. Dynamic DHR marker/controller/core/capital behaviour was not exercisable through this route. No map write was attempted.

The read-only technology inspect/render routes for `brilliant_scientist_alien_infantry_tech` returned `TECH_INSPECTED_PARTIAL` and `TECH_RENDERED_PARTIAL`, with helper projections deferred and `sourceAccurate=false`. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e5a25a4d59d2f72b52c2a5d503f8b3d70083923464bd9217b08b644f990a248/b99e519c09b91086fbd89fec89d1a0a1c69ad19d7843cf08c249e6ba99cbd697/technology-explain-dbaf119743a8.json`. Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e15511a7486e4a7acb1350043c3495d5bcfbc7ae5cc42322f1758f875c38e873/87fbc70650b76bb59b2f29bbc3bf61b881e565b856242bab2adc38efc26ab47b/technology-technology-dbaf119743a8-manifest.json`. The installed package exposes no separate Technology Tree Viewer, so technology visual acceptance remains unresolved as required by the parent instructions.

No callable `chaosx_ai_probability_auditor` or country-package-auditor tool was exposed. Direct probability inspection timed out at the bounded 180-second limit; no evaluate/sweep/compare result is claimed.

## Patches and changed identifiers

No gameplay files were changed. No tags, state IDs, leaders, parties, focus IDs, localisation keys, formable IDs, or asset tokens were added, removed, or renamed. The prior narrow `send_equipment` correction remains present at `common/scripted_effects/016_dhrondan_country_effects.txt:127-136` and was not repeated.

## Remaining risks, blockers, and parent actions

- Dynamic DHR revolt release, host-core conservation, controller retention, capital replacement, enclave flood-fill, stockpile debit, and initial cohort materialisation still need engine/live acceptance.
- The installed Event Viewer did not load the DHR event sources, so event `.40-.52` has source audit but no current mod-specific engine trace/render acceptance.
- The required custom probability auditor is unavailable and the fallback direct probability inspection timed out, so AI strategy factors and rebellion random-list balance remain uncertified.
- The installed Technology Tree Viewer is unavailable; the technology adapter returned partial, source-inaccurate evidence.
- The Alien Infantry custom 3D model/entity/action/audio package remains an external Event 016 blocker for full unit acceptance.
- The map inspect workspace reports unrelated building/harbor diagnostics; no DHR map write was made and no DHR-specific static map defect was proven.
- The stable generated portrait roster has no explicit gender metadata or runtime random-name pool. No opposite-gender pairing was detected, but changing this would require an accepted identity-roster decision.
- `dhrondan_focus_add_orbital_dockyard` can do nothing for an inland DHR because it searches a random coastal state; this is a low-severity design risk retained without an unambiguous balance patch.

No broad identity redesign, new focus route, new formable suite, major setup expansion, map edit, or unapproved asset fallback was made.
