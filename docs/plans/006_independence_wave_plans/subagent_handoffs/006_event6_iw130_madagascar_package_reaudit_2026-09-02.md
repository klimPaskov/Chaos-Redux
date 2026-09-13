# Event 006 IW-130 Madagascar country-package re-audit — 2026-09-02

## Disposition

NO-CHANGE / PACKAGE-LOCAL PREPARATION ONLY / FAIL-CLOSED.

This re-audit adds only this handoff. No gameplay, asset, central-dispatch, FORM-31, SCN-008, Join, or map file was edited. The current source does not support a source-safe package-local implementation tranche.

## Accepted contract

The accepted row is IW-130 Madagascar restoration, carrier MAD, package iw_130, anchor state 543, reservation group RG-543, southern Africa and Indian Ocean region, regional depth, port_or_island allocator archetype, and FORM-31 Indian Ocean League State direction.

The accepted package docket is independence_wave_iw130_convene_island_settlement; projects iw130_balance_highland_and_coastal_delegates, iw130_reopen_island_revenue_service, iw130_reconnect_rail_and_ports, and iw130_organize_island_guard; settlements iw130_ratify_representative_council, iw130_restore_crown_council, and iw130_authorize_emergency_governor; and network action iw130_open_indian_ocean_shipping_mission.

The current accepted evidence remains the 2026-08-28 source gate and symbol gate, the IW-130 row in docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:131 and docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:131, the current map binding in docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:131, and the force mapping in docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:131.

## Country package coverage checklist

| Surface | Status | Evidence and exact gap |
| --- | --- | --- |
| Tag registration and identity | STABLE / BLOCKED | Vanilla registers MAD; Event 006 has only a dormant registered-tag reservation and identity classification. No IW-130 content identity is attested. |
| Ownership and origin | BLOCKED | State 543 is currently FRA-owned; Event 012 owns the direct MAD Merina carrier lifecycle and rejects Event 006 origin reuse. No Event 006 release transaction is admitted. |
| 1936 roster and rights | BLOCKED | No period-valid 1936 officeholder or authentic provisional institution has been accepted. No portrait-rights package exists for the required identity. |
| Flags and symbols | BLOCKED | Vanilla has ideology-specific MAD ladders only; the accepted Event 006 base symbol and provenance are absent. |
| History and setup | BLOCKED | No IW-130 country-history override, character recruitment, OOB, setup, or package setup effect exists. |
| Politics and parties | BLOCKED | Vanilla neutral election setup is present, but no IW-130 party names, route ladder, laws, popularity, or settlement politics are wired. |
| Focus tree | BLOCKED | Shared Event 006 tree is present, but no IW-130 callback/route assignment or package-specific focus behavior is present. |
| GUI | STABLE / HOST-ONLY | The shared Event 006 status window and Event 012 Charter window render and inspect read-only; neither provides an IW-130 package surface. |
| Decisions, missions, ideas | BLOCKED | None of the accepted IW-130 docket IDs has a package-local implementation, lifecycle, icon, or localisation surface. |
| Forces and playability | BLOCKED | The documentation force row is not runtime setup; no IW-130 template, equipment, manpower, reinforcement, or cleanup adapter exists. |
| Industry, technology, supply | PARTIAL / BLOCKED | Vanilla anchor buildings and one infantry technology remain inspectable; no IW-130 production, research, convoy, port, railway, or supply package exists. |
| AI and weighted logic | BLOCKED | No IW-130 AI strategy/focus/decision surface exists. The required probability-auditor route is unavailable in the current tool inventory. |
| Assets and localisation | BLOCKED | No Event 006 MAD flag, portrait, character GFX, ideas, decision icons, focus icons, or package localisation is present. |
| Admission and lifecycle | BLOCKED | No IW-130 runtime adapter, content attestation, preflight branch, Join/SCN-008 publication path, FORM-31 member adapter, or package cleanup exists. |

## File surface checklist

### Present but allocator or host-only

- common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2477-2493 loads iw_130, MAD, state 543, RG-543, the region, depth, archetype, and host pointer; it does not create a country package.
- common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2557-2565 prepares an allocator weight and common/scripted_effects/006_independence_wave_effects.txt:3460 initializes the iw_130 weight to zero; these are inert planning plumbing.
- common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:2621-2628 reserves state 543 only after the generic planner predicate passes.
- common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:891-898 contains the generic IW-130 planner predicate for an available dormant MAD carrier and available state 543.
- common/scripted_triggers/006_independence_wave_package_triggers.txt:44-77 provides the shared dormant/origin-safe candidate gate, including rejection of Event 012 package-active and focus-tree-loaded flags.
- common/scripted_effects/006_independence_wave_scenario_effects.txt:184 ranks the iw_130 package ID in a scenario list; it does not attest or execute the package.
- common/scripted_triggers/006_independence_wave_package_triggers.txt:469-581 classifies MAD as a registered Event 012 overlap; classification is not Event 006 content.
- common/national_focus/012_africa_continental_focus_tree.txt:1354-1480, common/decisions/012_africa_priority_member_decisions.txt, and common/ai_strategy_plans/012_africa_focus_plans.txt are Event 012 host-package surfaces and are not IW-130 consumers.

### Absent for IW-130

- No common/countries/Madagascar.txt mod override and no history/countries/MAD - Madagascar.txt Event 006 override.
- No IW-130 history/units OOB, package startup setup, force installer, equipment grant, template, reinforcement, or generation-safe cleanup.
- No IW-130 character definition or recruitment entry in common/characters/006_independence_wave_characters_registry.txt and history/general/006_independence_wave_character_recruitment_registry.txt.
- No IW-130 implementation in common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt or its matching trigger surface; that file currently contains the bounded IW-095 package only.
- No IW-130 package ideas in common/ideas/006_independence_wave_ideas_registry.txt, decisions or missions in common/decisions/006_independence_wave_categories.txt and the Event 006 decision files, or package AI strategy in common/ai_strategy/006_independence_wave_ai_strategy_registry.txt.
- No Event 006 MAD localisation, character/leader GFX, portrait consumer, flag ladder, or asset manifest.
- No IW-130 entry in the adapter and content-attestation OR lists in common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63 and :159-201. The preflight at :207-213 requires both lists.
- No IW-130 Join/SCN-008 execution branch, FORM-31 member/proclamation adapter, or package-local cleanup branch.
- No writer for independence_wave_package_content_ready exists; this flag must not be added as an admission shortcut.

## Identity, ownership, roster, rights, and assets

Vanilla common/country_tags/00_countries.txt:124 registers MAD to countries/Madagascar.txt, and vanilla common/countries/Madagascar.txt:3-6 supplies only African graphical cultures and the vanilla color. This registration is reusable, but it is not an Event 006 package.

Event 012 directly owns the live MAD Merina carrier through africa_priority_merina_sovereign in common/characters/012_africa_priority_member_characters.txt:151-159 and history/general/012_africa_priority_member_character_recruitment.txt:49-52. Its lifecycle flags and focus/idea/force consumers are guarded separately. Event 006 must not overwrite, recruit beside, or reuse that origin identity.

The only existing Merina portrait consumer is GFX_portrait_012_africa_priority_merina_sovereign in interface/012_africa_priority_member_characters.gfx:59-60, sourced to a circa-1862 Radama II image. The accepted source gate explicitly treats its rights as conditional and its date as unsuitable for a 1936 provisional leader. No Event 006 portrait worker evidence, sourced placeholder, runtime DDS, character GFX, or portrait-specific wiring exists.

The research row requires either a sourced real male period leader valid for the release date and not active elsewhere, or authentic archival material for the actual provisional institution. No such choice is accepted. The institutional alternative must use an institutional name, not a personal random-name pool. Any future female-presenting or male-presenting character must also satisfy the repository gender-pool and leader-metadata rules; no Event 006 character currently reaches that review.

Vanilla supplies only ideology-specific MAD_neutrality, MAD_democratic, MAD_fascism, and MAD_communism flag ladders with medium and small variants. There is no accepted Event 006 base symbol, historical route variant, provenance record, or rights review. The existing ladders cannot be treated as proof of the chosen 1936 restoration identity.

## Map and state setup

Vanilla history/states/543-Madagascar.txt:2-29 defines state 543 with 3,694,611 manpower, rural category, MAD core, FRA owner, victory point 5128 at value 1, infrastructure 1, air base 1, naval base 1 at province 5222, ten listed provinces, and local_supplies 0.0. Vanilla history/countries/MAD - Madagascar.txt:1-69 sets capital 543, infantry_weapons = 1, set_convoys = 5, and neutral 1936 politics, but no OOB.

The accepted current binding is 543=FRA with FRA retaining at least one protected remnant. The state is a reservation anchor only. No transfer, controller change, core change, capital change, railway, port, supply, or building edit is authorized before the central release transaction and host-survival proof.

Read-only map evidence for the selected state is artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/163906b29aa13383aaca523ac529ada49515b38e9921abb9472d77f91c334e1b/f7d9a06c4d0311e13234d459c5cb3d73f7ff738b766ec07e7a1bbe0c77ff93bd/map-inspect.9ecfc1f41da23dc6.json and rendered state-layer evidence is artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2b6b372fd033533db9ca8f68b2749b8fe6c7fc8c6a983be6bed2bcc29b457b6/c15b4e9948de3a9bc26a24efc6ae5bdeda167b819011836e46d723a25537fe65/map-state.json. The selected state passed state/region/network/adjacency/supply/rail checks; the global report still contains unrelated building-position and port-adjacency diagnostics from mod:map/buildings.txt. No map write occurred.

## Politics, parties, leaders, portraits, flags, and advisors

Vanilla MAD history sets ruling_party = neutrality, last_election = 1936.1.1, election_frequency = 48, elections_allowed = yes, and popularities democratic 27, fascism 8, communism 15, neutrality 50. It has no country leader, party-name overrides, advisors, high command, commanders, or Event 006 laws/war-support/stability setup.

The accepted direction is a former Merina monarchy and French colonial administration joined to highland/coastal political interests, ports, rail, labour, and island representation. That is a design direction, not a permission to invent a 1936 officeholder, royal restoration, civic symbol, or generic council. The source and rights gates remain open.

## Focus, decisions, ideas, and assets

Read-only Event 006 focus inspection succeeded for independence_wave_focus_tree with 184 focuses and 196 connectors; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77b4a08236607dcee53e66474cf351435748498e1c43a9a23e6f9ad750ff543d/ce8f1379012cd0c99aeaf5b18486df2a5a281021839950e181c78577152f8dbc/focus-inspect.d3d6d41b22af3cbe.json. Render evidence is artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c01589ebc3f05995a3f5e7afe7b4b79b00b8b23e01aa1c088e8d9cb045f73289/1d530d76807b5331f716548435fe5475f2c16ea5bbd23f9235c76a64a9a8fe4a/independence_wave_focus_tree.focus.json; the inspected tree has no IW-130 callback or route. The Event 006 root/render evidence for chaosx.nr6.1 is partial because helper/lifecycle passes are deferred, but has no blocking diagnostics for this absent package.

Read-only Event 012 focus inspection/rendering confirms a separate africa_continental_focus_tree with six Madagascar overlay IDs, including africa_madagascar_islands_settle_island_authority, africa_madagascar_islands_open_the_convoy_network, africa_madagascar_islands_protect_the_first_island_partner, africa_madagascar_islands_join_highland_and_coast, africa_madagascar_islands_convene_the_islands_council, and africa_madagascar_islands_prove_the_ocean_mandate. These are Event 012 host focuses gated by africa_focus_uses_madagascar_islands_overlay, not IW-130 callbacks.

Event 012 decisions, ideas, AI, starting force, and overlay localisation are likewise separate host-package consumers. They cannot satisfy the IW-130 docket or prove an Event 006 identity. No Event 006 package idea, decision category, mission, icon, focus icon, flag, portrait, GFX registration, or localisation is present.

The shared Event 006 status GUI is not country-owned and has no IW-130-specific element. Fresh read-only inspection of independence_wave_status_window with scenario independence_wave_status_default returned GUI_INSPECTED, 48 inspected elements, complete source graph, no missing or unresolved resources, and no blockers; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3a19139df756bf3c10c96d3e0ca122b6fbb19c5461a9481a9c5a7073887d084/a4797f1c5cb8e1938bd1f28732d55f1e5f39d1b7f459fe27c210211aa45bef96/gui-inspect.8d8164d0b4910b0d.json. Its render covered normal, warning, long-text, and missing-localisation at 1920x1080 and returned GUI_RENDERED with no blockers and changedPixels = 0; representative artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1dfd194c6663220e6dc7ef3f54c5d258efe50dde2409a4420f136479edc9b0a/1329314199ec206eaf641e83f2d37ac0b524c24639f27860786aa38714996e08/independence_wave_status_window-full.svg. Existing static-fallback, clipping, and overlap diagnostics are shared GUI findings and were not changed.

The Event 012 Charter GUI is likewise host-owned through africa_charter_window and the africa_charter_council_category. Fresh inspection returned GUI_INSPECTED with 107 inspected elements, complete source graph, no missing or unresolved resources, and no blockers; artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a675bbee9847a483d63742a1b41abaf1ed26bb9fa7bb0f997a4be6eeec0eaa9/18a4639727d49c5ea14cadbecc177330f3a69b73593e79c4071be97203334f76/gui-inspect.aa328f9633c63953.json. Its render covered normal, warning, long-text, and missing-localisation at 1920x1080 and returned GUI_RENDERED with no blockers and changedPixels = 0; representative artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb0c32542ba8fdbb3bedf77443ea8fcb162ccca1c3a383a4160e9affa51236c8/d450e1c062dbfe5546ec239b3bcd7b06a2b66644574d1e17bff1e1a0b3ab79d6/africa_charter_window-full.svg. Its visible-overlap and click-region diagnostics belong to the existing Event 012 host GUI and do not create an IW-130 dependency.

## Starting military, technology, industry, supply, and production

The vanilla MAD country history has no OOB or starting divisions, no production lines, no research-slot override, no starting ideas, and only infantry_weapons = 1 plus five convoys. State 543 contributes the static infrastructure, air-base, and level-one naval-base entries listed above.

The accepted documentation force mapping at docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:131 describes highland infantry, coastal guards, colonial veterans, mountain_frontier archetype, nominal strength 60, engineers/reconnaissance/mountain logistics first, and no navy inheritance. It is a design mapping only; no runtime adapter, templates, equipment, manpower, supply, reinforcement, or cleanup is implemented.

No Event 006 custom technology, doctrine, 3D dependency, or technology-tree route is proposed for IW-130. The installed package exposes no separate Technology Tree Viewer. hoi4.tech_inspect produced a vanilla infantry_weapons trace artifact at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e545a14af38f7c7c36a4b5cc738bd5bde4db3cd3be06c69651af66460c46fdb8/b672742deece8ad66f2674a55d7fb3187617962583614d97e117cb9faf589b6e/technology-trace-a1417861a875.json, but hoi4.tech_render timed out after 180 seconds. This is an unresolved tooling limitation, not evidence of a package technology implementation.

## AI and playability

No IW-130 AI strategy, focus preference, decision score, mission score, diplomacy strategy, template behavior, or survival path exists. Event 012 Madagascar host plans in common/ai_strategy_plans/012_africa_focus_plans.txt:1755-1795 are not Event 006 AI.

The raw probability inspection of the declared custom pool containing independence_wave_weight_iw_130 returned candidates = 0 and unresolved = 6, artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05bfe50b04985315b80e0684eb9f3104f1f0bf5e39fe8fd9ebbdb75b059ad9c5/1effc3aa54b15ea83f84ef0c7fc6a8afc131f1b6f503a4216e5a005cd77abb10/probability-inspect-8788a95e9207.json. Raw source discovery for the Event 006 AI strategy registry returned no weighted surfaces, artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35ae099a01e41dd2ad55e95686186da0744fd5fc9f093b206891ff9170f6b9f8/0111fa98a174b20a0b813497808c57fa23b6b16b690fdd75cb978bd727875adc/probability-inspect-9fa2ceabcceb.json.

The mandatory chaosx_ai_probability_auditor route is not exposed in the current callable tool inventory; only the raw hoi4.probability_* routes are available. No evaluate, sweep, sequence, simulation, or compare claim is made, and no AI weight has been patched.

## Admission, lifecycle, formable, and cleanup

The shared planner can locate a dormant MAD reservation, but there is no IW-130 package shell or source-owned content-ready writer. The dispatch adapter OR list and content-attestation OR list omit iw_130, while preflight requires both exact entries. The generic region loader, scenario ranking row, reservation group, and weight variable are not an admission or execution path.

No IW-130 branch exists for release setup, central attestation, SCN-008 publication, Join, FORM-31 membership/consent/anchor proof, project settlement callbacks, host-survival transfer, force cleanup, or annexation/puppet/release cleanup. The generic Indian Ocean League State registry is metadata only and has no MAD member/proclamation adapter.

## Read-only MCP evidence

- Event 006 root chaosx.nr6.1 inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ca15a6ec31cd27cb9b39b3e7d81ab9cbf21236f70f402670ab0c50f4f0fc804/2b11076e963d66cdc79ba6f78f9e1826c4ea07effd6409099b172498fe8b25b7/event-trace-18bf807c8be3.json; focused trace is partial with deferred helper/lifecycle validation.
- Event 006 focus inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77b4a08236607dcee53e66474cf351435748498e1c43a9a23e6f9ad750ff543d/ce8f1379012cd0c99aeaf5b18486df2a5a281021839950e181c78577152f8dbc/focus-inspect.d3d6d41b22af3cbe.json; 184 focuses, 196 connectors, validation true, no IW-130 route.
- Event 012 root africa_priority_member.1200 inspect artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec7230f35fa153b98aa210d42d3cef57c4ee6d4a208bc5f0a1a10e389d6b9e43/689db51ce61525428452ff6d8473aa3b20ada678999da01dc39ce37e52223ff4/event-trace-18bf807c8be3.json; focused trace is partial with deferred helper/lifecycle validation.
- Event 012 focus render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50977347e7af30d54ec9bdce3825450ca581015c5698e6414b7af548294b5f94/ff2631a5478be0afd997d6a175ed42aab01584b86ed86df35109e9b70534ff71/africa_continental_focus_tree.focus.json; separate host tree with Madagascar overlay focuses.
- Map inspect/render artifacts are recorded in the Map and state setup section; no map rewrite was requested or run.
- Technology trace and render limitation are recorded in the Starting military, technology, industry, supply, and production section.

## Exact blockers and next owner

1. Research/source ownership must select and attribute a period-valid 1936 leader or authentic provisional institution, with portrait provenance and rights.
2. Symbol ownership must close the MAD base/route flag origin and rights without reusing Event 012 or an unsupported ideology ladder.
3. A package owner must implement and review the complete IW-130 docket, including history/setup, character recruitment, ideas, decisions/missions, force/industry/supply setup, localisation, assets, and generation-safe cleanup.
4. The parent must then wire the exact runtime adapter, content attestation, preflight, SCN-008/Join boundary, and FORM-31 member/consent/anchor path only after all package gates are closed.
5. The mandatory chaosx_ai_probability_auditor route and the technology render/viewer limitation need an available validated path before quantitative AI or technology evidence is claimed.

Until these gates close, keep independence_wave_package_content_ready unset and keep IW-130 out of central attestation, Join, SCN-008, and FORM-31 execution.

## Validation and skipped work

Completed meaningful checks: required AGENTS.md, repository skills, offline Paradox wiki pages, vanilla documentation, vanilla MAD tag/country/state/history/flag files, accepted IW-130 specs and prior handoffs, targeted source scans, Event 006 and Event 012 read-only event/focus inspection and rendering, shared Event 006 status and Event 012 Charter GUI inspection/rendering, state 543 map inspection/rendering, raw probability source inspection, and vanilla infantry_weapons technology inspection. No live game was launched and no map write occurred.

Skipped by design: gameplay edits, asset production, portrait-worker routing, central attestation/SCN-008/Join/FORM-31 changes, focus/decision implementation, probability evaluation/compare, and live runtime validation because the identity, rights, roster, package-consumer, AI, and admission gates are open. The dedicated chaosx_ai_probability_auditor is unavailable in the current callable tool inventory, and hoi4.tech_render timed out after 180 seconds.

## Changed files

- docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw130_madagascar_package_reaudit_2026-09-02.md

No gameplay or asset files were changed, staged, or committed.
