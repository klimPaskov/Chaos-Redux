# Events 1-20 focus-tree cleanup audit

Date: 2026-07-29

Status: read-only audit handoff; no gameplay, localisation, icon, GFX, or shared-loader source was changed by this pass.

## Scope and evidence

The bounded surface was the Event 1-20 national-focus inventory under common/national_focus/, the focus-localisation and focus-icon consumers, and the existing focus-loading hooks that select those trees.

Standalone Event 21+ trees, report/news/super-event assets, scripted GUI event-target usage, and broad shared-helper rewrites were out of scope.

Required repository guidance was read before inspection: AGENTS.md, the offline Paradox wiki pages named by the repository, the vanilla focus documentation and focus precedents, .agents/skills/chaos-redux-focus-trees/SKILL.md, .agents/skills/chaos-redux-events/SKILL.md, .agents/skills/chaos-redux-decisions-missions/SKILL.md, .agents/skills/chaos-redux-event-assets/SKILL.md, and .agents/skills/chaos-redux-subagents/SKILL.md.

The static pass parsed 3,105 ordinary focus = {} nodes and 111 shared_focus = {} definitions, with zero duplicate focus IDs and no unresolved prerequisite, mutually_exclusive, or has_completed_focus references in the scoped sources.

All 3,216 scoped focus/shared IDs have title and _desc localisation coverage in the current English surfaces.

Direct focus icon tokens were checked against recursively scanned mod and installed-vanilla .gfx definitions, including the vanilla nested goal and special-project collections; no actual dangling regular icon was found.

The HOI4 focus adapter does not resolve every installed vanilla generic .gfx collection, so its generic-icon diagnostics are recorded as adapter limits rather than source defects.

## Route coverage table

| Event and source surface | Focus inventory and route coverage | Audit result and remaining risk |
| --- | --- | --- |
| 002 Zombies, 002_zombies.txt:1-16, ZZZ_focus | Zero focus nodes; deliberately blank country tree. | Intentional design (“zombies have no strategic thinking”), not a missing branch. |
| 003 Holy Realm, 003_holy_realm.txt:36, THR_focus | 111 focuses covering refuge, Bodhisattva, teaching, Dhyana, three-way governance, Arhat administration, guardian defense, Sangha/compact diplomacy, borderland protection, anti-chaos powers, False Buddha Schism, Final Silence, and Empty Seat aftermath. Representative IDs are THR_send_first_envoys, THR_sit_beneath_prayer_flags, THR_council_of_abbots, THR_buddha_mandate, THR_debate_the_pretender_focus, and THR_final_silence. | Route coverage is complete in the current Event 003 plan and overview. Forty-eight opening/support/conditional nodes inherit the default AI factor rather than declaring a local ai_will_do; route anchors and common/ai_strategy/003_holy_realm.txt provide the meaningful route weighting. A full support-node AI pass remains optional balance work. |
| 005 Soviet Collapse, 005_soviet_collapse_ancient_restorations.txt | 64 focuses across four 16-focus restoration trees: INX_soviet_collapse_ancient_focus_tree, SOG_soviet_collapse_ancient_focus_tree, ANX_soviet_collapse_ancient_focus_tree, and ABX_soviet_collapse_ancient_focus_tree. Each has symbolic/settlement and expansionist branches. | Mechanically wired and AI-covered, but the four 16-focus trees remain shallow relative to the accepted restoration promise; modern administration, industry, diplomacy, postwar integration, and route-specific AI are compressed. Existing Event 005 redesign follow-up plans already cover this broad gap. |
| 005 Soviet Collapse custom splinters, 005_soviet_collapse_custom_splinters.txt | 1,021 focuses across the tag-specific successor family, including full and compact high-chaos identities. | IDs, prerequisites, rewards, icons, localisation, and AI are structurally present. Prior Event 005 audits still identify helper-heavy rewards, repeated stockpile/logistics patterns, compact crisis trees (TSC, RMC, DSC, NRF, ICD, PRA), and insufficiently visible direct aggression as broad route-depth work, not a safe one-node repair. |
| 005 Soviet Collapse factory successors, 005_soviet_collapse_factory_successors.txt | 128 focuses across CFR_soviet_collapse_focus_tree, IJX_soviet_collapse_focus_tree, and MFR_soviet_collapse_focus_tree. | The factory/governance/arms branches exist and all references resolve. OGB was remapped to IJX; the surviving compact factory successor surface remains shallower and more helper-driven than the architecture target, especially for diplomacy and postwar settlement. |
| 005 Soviet Collapse republics, 005_soviet_collapse_republics.txt | 515 focuses across Ukraine, breakaway/internal republic, Baltic, Caucasus, Central Asia, Moldova, Belarus, and Kazakhstan packages. | Broad political, military, industry, League, foreign, and expansion lanes are present. Prior audits still flag dense geometry, helper-opacity, limited direct claims/cores/war hooks on some routes, and flat high-chaos AI strategy as broad rework risks. |
| 006 Independence Wave, four 006_independence_wave*_focus.txt sources | 184 ordinary focuses plus 128 shared-focus definitions (312 total), covering survival/founding, seven government settlements, economy/administration, military identity, diplomacy/patrons, former-host policy, regional ambition, League/network, FORM-03 preparation, hidden/high-chaos, package modules, generic overlays, and post-formation overlays. | Latest Event 006 focus audit reports all IDs, icons, localisation, rewards, and AI declarations present. The central authored geometry remains validator-blocked (14 coupled layout blockers); meaningful-tree carrier reachability, package admission, focus-order AI, and post-formation visibility remain unproved. No isolated coordinate or route-lock patch is safe. |
| 007 Fury, 007_fury_focus_tree.txt, fury_focus_tree | 52-focus shared AI tree with opening, army, expansion, occupation, cooperation, rivalry, evolution, and world-end candidate branches. | Current source keeps the route anchors and all focus AI. The Internal Fury specification is represented mainly through opening/army/occupation mechanics rather than a named War Directorate/Civil Mobilization/Compliance fork; this is a documented design simplification, not a syntax failure. |
| 010 Death, 010_death_focus_tree.txt, death_focus_tree | 26-focus fixed-purpose lane tree: opening, Shroud/Hunger/Census pre-reveal, Public Death convergence, Coastal/Wasteland/Host post-reveal, and Last Shores/World Consumed. Dark Methods, Black Oath, Herald, and Black Apostolate correctly remain living-country decision routes. | Current Death audits report complete focus AI, icon/shine wiring, gates, and runtime loading. No normal-country economy/diplomacy branch is required by the accepted fixed-purpose architecture. |
| 012 Africa, 012_africa_continental_focus_tree.txt | 276 focuses: 16 opening, nine six-focus regional overlays, six host signatures, six 21-focus constitutional routes plus Hidden Covenant, 36 shared support nodes, and formation/post-formation lanes. Overlay roots use allow_branch predicates such as africa_focus_uses_maghreb_sahara_overlay. | All routes and rewards are present. The renderer treats mutually exclusive overlay templates as simultaneous and reports coordinate conflicts; this is intentional authored stacking and must not be “fixed” without branch-aware runtime proof. One hundred seven continental route-body nodes use flat normal AI, so route-phase and proof-aware focus ordering remains a balance gap. |
| 012 Africa priority member, 012_africa_priority_member_focus.txt | Eight-focus non-linear priority-member overlay, with compact political settlement, institution, economy, League, force, overlap, and post-settlement nodes. | Complete source/icon/localisation/reward/AI coverage; three long-connector warnings are present in the current inspect, but no local route or node collision was found. |
| 012 Africa world-order packages, six 012_africa_world_*.txt sources | 121 dormant package focuses: Asia 20, Europe 20, Middle East 20, North America 20, Oceania 20, South America 21. | Files and loaders remain deliberately dormant behind africa_world_package_implementation_ready. Current RC removes all 121 icon lines and the world-order .gfx/DDS package; no fallback art is allowed. This is an explicit asset gate, not a missing focus branch. |
| 014 Cannibalism, 014_cannibalism_focus.txt | 204 focuses in three roots: Unified CBL 108, Warlord 68, Wendigo 28. Routes include hierarchy, Larder, army/air/naval operations, expansion/counterwar, three Warlord origins, regional alignments, winter transformation, and terminal preparation. | The 2026-07-15 consolidated audit reports complete reachability, symmetric mutexes, rewards, AI, localisation, icon/shine wiring, and strict terminal gates. No route simplification remains in this bounded surface. |
| 015 Utopia Manifesto, 015_utopia_manifesto_focus_tree.txt, utopia_manifesto_tree | 124 focuses covering five interpretations, common support lanes, island variants, foreign/commonwealth, stewardship, crisis correction, formation, and post-formation play. | Route, reward, AI, localisation, and icon coverage are complete. The 2026-07-22 visual audit still reports 54 crossings, 17 through-node intersections, 21 long connectors, and a 9,808-pixel-wide authored tree; remediation is a coordinated layout pass, not a gameplay patch. |
| 016 Brilliant Scientist, 016_brilliant_scientist_kruger_state_focus.txt | 100 KRG focuses spanning foundation, Directorate/security/logistics, clone/machine, paleogenetics/xenobiology, portal/temporal, foreign/integration, conventional recovery, and terminal program routes. | Current completion audits report 100 focus nodes, 108 connectors, zero Event 016 layout diagnostics, 17 AI plans, complete localisation/icon/shine wiring, and 180 consumed focus receipts. |
| 018 Oth-Kesh, 018_resources_found_cave_focus_tree.txt, 018_resources_found_cave_focus_tree | 65 focuses: emergence trunk, three mutually exclusive hierarchy routes, resource anchors, three mutually exclusive surface-war doctrines, adaptation, continental conquest, and world-end preparation. | The 2026-07-25 visual audit reports zero layout diagnostics, all 65 custom icon/shine pairs, complete localisation/tooltips, and full AI. No source repair is justified here. |
| 019 Infantry Spawn Derivative, 019_infantry_spawn_derivative_focus.txt | 45 focuses: shared trunk, three mutually exclusive identity outcomes for each zombie/ghost/golem family, three doctrine roots, and route capstones. | Prior specialist audits report complete route gates, rewards, localisation, icon/shine wiring, and AI. Current render shows four connector-through-node warnings around infantry_spawn_derivative_name_the_future_host and its zombie/ghost children; this is a coordinated geometry issue, not a safe single-coordinate patch. |
| 020 Black Plague, 020_black_plague_rat_focus_tree.txt and 020_black_plague_rat_king_focus_tree.txt | Rat Nation 23 focuses: four origin lanes, hierarchy, capped pulses, immune blood, annexation, and crown preparation. Rat King 38 focuses: coronation, three government lanes, shared royal forces, crisis/knowledge, cohesion, and terminal route flag. | The hard OR-prerequisite locks were already repaired in the existing 2026-07-29 focus handoff. Current route architecture is intentionally shallow against the accepted target (roughly 40-50 Rat and 70-100 Rat King), and neither tree has focus-level ai_will_do; runtime strategy helpers are present. Broader route depth and focus-order AI require a plan-level pass. |
| Events 001, 004, 008, 009, 011, 013, and 017 | No Event 1-20 national-focus source was found for these event IDs. | Their current designs are event/decision/GUI/diplomatic systems rather than focus-tree packages; no focus omission was inferred without a focus requirement in the corresponding specification. |

## Missing or simplified content list

1. Event 005 is the primary broad depth gap: the four ancient restorations are 16-focus compact trees, the compact high-chaos trees remain crisis ladders, and many large splinter/republic rewards are shared-helper driven rather than visibly country-specific. Existing follow-up authority: docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md and the dated Event 005 focus audits under docs/plans/005_soviet_collapse_plans/subagent_handoffs/.
2. Event 006 has complete source definitions but remains HOLD/PARTIAL for coupled geometry, meaningful-tree carrier reachability, package admission, route-family probability proof, and focus-order AI; see docs/plans/006_independence_wave_plans/subagent_handoffs/006_focus_framework_audit_2026-07-29.md.
3. Event 007 does not expose named Internal Fury government forks as separate focus families; this is documented in docs/specs/007_fury_specs/specs/007_fury_focus_tree_spec.md and docs/plans/007_fury_plans/007_fury_followup_addendum_after_partial_implementation.md.
4. Event 012 world-order packages are intentionally iconless and dormant until the external implementation-ready gate is set; do not restore generic or placeholder art. The nine regional overlay templates reuse coordinates by design and require branch-aware proof before any layout rewrite.
5. Event 015 source is complete but the authored tree remains very wide and crossing-heavy in MCP geometry; a future multi-node layout pass must preserve all route IDs and rewards.
6. Event 019 has four current connector-through-node warnings around the shared host-naming fan; a layout pass should be coordinated across the family branches.
7. Event 020 remains intentionally simplified versus the accepted architecture and has no route-aware national-focus AI. The existing handoff is docs/plans/020_black_plague_plans/subagent_handoffs/2026-07-29_event20_focus_final_audit_handoff.md.

No fallback tree, placeholder reward, invented icon, or silent route substitution was introduced by this audit.

## Icon coverage table

| Surface | Current coverage | Reuse or limitation | Evidence |
| --- | --- | --- | --- |
| 002 ZZZ | No focus icon references because the tree is blank. | Intentional. | common/national_focus/002_zombies.txt:1-16. |
| 003 THR | 111 focus icon references, 70 unique IDs; regular tokens resolve against mod or installed vanilla collections. | Generic route families are reused, with highest reuse in GFX_focus_smiling_buddha, GFX_goal_THR_final, and generic treaty/League icons. | Static recursive .gfx scan; current render artifact below. |
| 005 Soviet Collapse | All scoped focus icon tokens resolve. Ancient/restoration/factory/splinter families intentionally reuse templated families. | Asset differentiation and reward identity are broader design work; no dangling token found. | Static recursive .gfx scan and prior Event 005 focus audits. |
| 006 Independence Wave | 312 definitions use 121 distinct icon IDs; 121 regular and 121 _shine registrations and texture paths resolve. | Reuse is thematic across settlement, military, administration, League, and package families. | 006_focus_framework_audit_2026-07-29.md. |
| 007 Fury | All 52 focus icon assignments resolve after the existing generic-icon repairs. | Eight custom Fury icons and generic support icons are intentionally mixed. | docs/plans/007_fury_plans/subagent_handoffs/2026-06-10_fury_focus_tree_audit_patch_handoff.md. |
| 010 Death | All 26 focus sprites have registered base and shine variants. | Fixed-purpose lane uses a small custom family plus generic support icons. | docs/plans/010_death_plans/subagent_handoffs/focus_tree_audit_handoff.md. |
| 012 Africa active trees | 21 unique active icon IDs: 13 continental family sprites and 8 priority-member sprites, all base/shine/DDS-complete. | World-order packages intentionally have zero current icon references and no fallback art while dormant. | 012_africa_focus_tree_rc_audit_2026-07-29.md. |
| 014 Cannibalism | 204/204 focus icon references and 204/204 base/shine pairs resolve. | Reuse is route-family-specific and no missing custom sprite remains. | event014_focus_tree_consolidation_reaudit_2026-07-15.md. |
| 015 Utopia | 124 references, 74 unique sprite IDs, 74/74 regular and 74/74 shine registrations. | Thematic reuse is intentional. | focus_tree_visual_audit_2026-07-22.md. |
| 016 KRG | 100 custom focus references with matching base/shine textures. | No missing focus icon or shine pair in current completion audit. | 016_core_runtime_completion_audit_handoff.md. |
| 018 Oth-Kesh | 65/65 regular and 65/65 shine pairs, 94x86 DDS files. | Each focus has a distinct icon; no missing pair. | focus_tree_visual_audit_2026-07-25.md. |
| 019 Derivative | 45/45 focus icon references and custom shine coverage. | Four layout warnings are unrelated to sprite registration. | 019_focus_tree_specialist_reaudit_2026-07-16.md plus current render. |
| 020 Rat/Rat King | All direct tokens resolve against mod or installed vanilla definitions; all nine custom token families have regular/shine coverage. | MCP generic-vanilla icon warnings are adapter false positives; some generated custom sprites are intentionally unused until route depth expands. | 2026-07-29_event20_focus_final_audit_handoff.md. |

## Localisation and reward mismatch list

- No missing title or _desc key was found across the 3,216 scoped focus/shared definitions.
- Event 006, Event 012, Event 014, Event 015, Event 016, Event 018, Event 019, and Event 020 specialist handoffs independently report complete title/description and custom tooltip coverage for their current focus surfaces.
- No sampled current focus name directly contradicts its completion helper: DHO_the_first_breach calls resources_found_cave_initialize_live_systems, KRG_audit_inherited_portfolio opens the KRG administration layer, black_plague_rat_first_warren starts the Rat route, and infantry_spawn_derivative_name_the_future_host records the shared host identity before its family overlays.
- The remaining mismatch class is reward opacity or missing route depth, not broken localisation: Event 005 helper-heavy compact trees, Event 012 flat support/body factors, and Event 020 simplified spirits/decision hooks need broader design review.
- A full prose review of every description/effect tooltip and live narrow-width hover wrapping was not repeated in this repository-wide bounded pass.

## AI behavior gaps

| Surface | Current behavior | Risk and identifiers |
| --- | --- | --- |
| 002 ZZZ | No focus AI because the tree is intentionally empty. | None while the zombie runtime uses scripted growth rather than national-focus choice. |
| 003 THR | 48 focuses omit a local ai_will_do and inherit default factor 1; route anchors and Event 003 strategy plans carry the meaningful weighting. | Candidate route-support gap, not a broken route. The no-block IDs are listed in the following paragraph. |
| 005 Soviet Collapse | Focus AI blocks are present in the audited current files, but many route bodies use common factors and helper-driven effects. | Political choice, expansion timing, patron/League alignment, and compact-chaos aggression remain underweighted in many trees; see 005_soviet_collapse_custom_splinters.txt, 005_soviet_collapse_factory_successors.txt, and 005_soviet_collapse_republics.txt. |
| 006 Independence Wave | All 184 regular and 128 shared focuses have ai_will_do; 80 regular and 133 shared/package blocks have inline modifiers, while base-only blocks remain common. | Package strategy files do not prove focus-order route selection; patron, League, former-host, formable, ICE, and post-formation probability sweeps remain open. |
| 007 Fury | All focus blocks have AI weights. | Named internal government route selection remains represented by indirect opening/army/occupation mechanics. |
| 010 Death | Focus-level stage-aware availability and AI weights are present. | No dedicated common/ai_strategy/DTH.txt is required by the fixed-purpose architecture; live pacing remains parent-owned. |
| 012 Africa | Focus AI exists across active and dormant definitions, with ten route plans for visible constitutional/formation support. | 107 continental route-body blocks use flat normal factors; overlay, priority-member, world-order, host-playbook, and package-phase focus ordering is not fully strategy-planned. |
| 014 Cannibalism | All 204 focus blocks have route-aware AI factors and 12 strategy plans. | No open syntax-level AI gap. |
| 015 Utopia | All 124 focus blocks and 12 strategy plans have AI; paid focus AI mirrors the same resource gates as players. | No focus-level AI gap; optional scenario balance remains. |
| 016 KRG | All 100 focus blocks and 17 route plans have AI. | No focus-level AI gap. |
| 018 Oth-Kesh | All 65 focus blocks have route-aware AI weights. | No focus-level AI gap. |
| 019 Derivative | All 45 focus blocks and dedicated ordinary/scenario strategy files have AI. | No focus-level AI syntax gap; current layout warnings are separate. |
| 020 Rat/Rat King | Neither tree declares ai_will_do; runtime setup supplies explicit template/front/role strategies at common/scripted_effects/020_black_plague_rat_effects.txt:446-450 and :780-782. | National-focus route choice stays at default ordering and needs a broader route-depth/AI matrix before more weights can be meaningful. |

The 003 no-block IDs are: THR_mountain_refuge, THR_shelter_border_villages, THR_guard_high_passes, THR_bodhisattva_accepts_seal, THR_first_doctrine_suffering, THR_rewrite_civil_register, THR_mandala_bureau, THR_arhat_examinations, THR_arhats_take_office, THR_labs_snow_line, THR_refuge_foundries, THR_vow_keeper_regiments, THR_quiet_envoys, THR_buddha_mandate, THR_white_flags_foreign_roads, THR_vow_against_annihilation, THR_release_through_administration, THR_convene_mountain_assembly, THR_seal_of_refuge, THR_ministry_of_vows, THR_silent_offices, THR_village_without_petitions, THR_question_false_attainment_focus, THR_count_mountain_roads, THR_monastic_labor_vows, THR_mountain_granaries, THR_snowline_clinics, THR_shelters_under_stone, THR_quiet_mobilization, THR_mountain_artillery_mandalas, THR_permit_foreign_pilgrimage, THR_letters_to_war_tired, THR_shelter_exiles, THR_mandala_of_nations, THR_refusal_of_empires, THR_no_victory_parades, THR_last_border_is_wound, THR_refuse_final_debate, THR_peace_without_ownership, THR_world_still_burns, THR_second_refuge, THR_seal_roads_from_panic, THR_sort_worthy_broken, THR_world_marked_as_wound_focus, THR_guardians_outer_passes, THR_roads_must_be_quiet, THR_outer_valleys_register, and THR_mandala_borders in common/national_focus/003_holy_realm.txt.

## Loader and route-lock review

The inspected loaders are structurally guarded and were not edited.

- Event 003 formation loads THR_focus at common/scripted_effects/003_holy_realm_effects.txt:1868-1870 after holy_realm_active is set.
- Event 005 regional loading is guarded by successor/republic flags at common/scripted_effects/005_soviet_collapse_effects.txt:10136-10260; custom splinter loaders begin at :21113.
- Event 006 full-framework assignment loads independence_wave_focus_tree at common/scripted_effects/006_independence_wave_focus_effects.txt:48-53 and marks the layout dirty.
- Event 007 loads fury_focus_tree at common/scripted_effects/007_fury_effects.txt:217.
- Event 010 loads death_focus_tree in common/scripted_effects/010_death_effects.txt:456.
- Event 012 has two guarded continental-tree helpers: common/scripted_effects/012_africa_effects.txt:1367-1386 and common/scripted_effects/012_africa_focus_route_effects.txt:11-32. Both test has_focus_tree/loaded flags before load_focus_tree; this is a parent-owned duplicate-loader proof item, not a safe local deletion.
- Event 014 unified, Warlord, and Wendigo loaders are guarded by their canonical country/identity flags in common/scripted_effects/014_cannibalism_effects.txt around the unified setup (:12363) and Warlord/Wendigo setup helpers.
- Event 015 acceptance loads utopia_manifesto_tree at common/scripted_effects/015_utopia_manifesto_effects.txt:316.
- Event 016 formation/takeover paths load brilliant_scientist_kruger_state_focus_tree in common/scripted_effects/016_brilliant_scientist_country_effects.txt around :605 and :882.
- Event 018 cave setup loads 018_resources_found_cave_focus_tree after the DHO identity flag in common/scripted_effects/018_resources_found_cave_effects.txt.
- Event 019 derivative setup loads infantry_spawn_derivative_focus_tree after the derivative identity is established at common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:577.
- Event 020 Rat and Rat King setup load their separate trees at common/scripted_effects/020_black_plague_rat_effects.txt:446 and :780.

No loader call was found for the events without a national-focus surface listed in the route table.

## MCP artifacts and layout findings

All MCP calls used read-only hoi4.focus_inspect/hoi4.focus_render; no hoi4.focus_rewrite was used.

- Event 003 render status was FOCUS_RENDERED; HTML artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0fb267dba92905309ada6054a1d51ee2848681717abba16780fe8ed0ac077eca/2f172e93373068b00e3d22c2a601bb44be69e5b34264da600d805910b0ea656c/THR_focus.focus.html, SVG artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9d80e099a667a01edc0982ca8395716fa54aea012c2cd5d115515bbd26d0e8b/4ae35b6bcc826eff566986e025b35ca442e1928560a21153912bcdf1466c5532/THR_focus.focus.svg, and JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cfedf90c26ec1b12bf1e8d65c5cc0b27300071764529793539abdcd37775c5e/a4c7a1c0db7b54d4b5d223e7e9258d2893a6988fa3bbe55ae2af85777b17a69f/THR_focus.focus.json. The current render is 7,696 by 2,904; inspect diagnostics are dominated by generic vanilla icon resolution limits.
- Event 012 continental render status was FOCUS_RENDERED; HTML artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d90692395cb257451d3c314c3c7af995163a5cf2b6e89e5c5c429e447c1bc35d/50e17a0fdb61068bfa65a9dfb70ea5d7c2595528d779f3e8427aea634d07b9af/africa_continental_focus_tree.focus.html. Current diagnostics include coordinate conflicts between overlay nodes such as africa_maghreb_sahara_face_divided_sovereignty and africa_congo_basin_transfer_authority_from_concessions at (12,2), which are intentional allow_branch template reuse. The latest dedicated Event 012 audit records the complete branch-aware limitation and the prior 570-diagnostic inspect artifact.
- Event 019 render status was FOCUS_RENDERED; HTML artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d72c541ab35aa29367d5d0b49856c99c614290d05b87d6f4e572d9f56c1fb51/a3437b84c1146d1a20c5e8a9b6200cacda5c3356f83ba7ec6042b4173df4f182/infantry_spawn_derivative_focus_tree.focus.html, SVG artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3dfeb722eeb4c72619ecc91df22f4a9b8c46b56a5b9feda98a7167e6e4a98e5e/6a9b0c54428a65d8de7ab91af9e9488a260ca822a68e915a64750b66580ab3ca/infantry_spawn_derivative_focus_tree.focus.svg, and JSON artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a1edf14a1c7204eb581bdbbf574d1dc089b5801c3b676f58bef1525eab68a65/449166585a2d552e5bafa450da6d060e7e4752f68dc543e00237946171fbd623/infantry_spawn_derivative_focus_tree.focus.json. Four FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE warnings all originate from the name_the_future_host fan into the zombie/ghost overlay lanes.
- Event 020 Rat Nation render status was FOCUS_RENDERED; HTML artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2522863670445700dafc9b2a4222e02bf6103fba12597fa6a4222b791ff606ff/1cff84cbab0e314b66ffe006711531344c12372c7589d5832b4895e8bae93558/black_plague_rat_focus_tree.focus.html. The current tree renders at 1,888 by 1,280 without a focus-specific layout warning in the returned first diagnostics batch; generic vanilla icon diagnostics remain adapter noise.
- Event 003 hoi4.focus_inspect produced artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fa6f496847866f6e6ec574cf413979fdd95977929ac4734c3b88cad3eba00032/b680fa60542dbc435cdbfd515680842aabc48071b1d2fcff4d310f570fa367cb/focus-inspect.e97c54ebea63d643.json with 111 focuses, 129 connectors, bounds x=0..42/y=0..23, 25 crossings, 21 node-intersection diagnostics, and 7 long-connector warnings before the adapter truncated its inline diagnostic collection. The diagnostics are not source-validity proof; the route source is covered by the Event 003 completion plan and overview.

The MCP adapter has a known global baseline of unrelated vanilla continuous-focus missing sprites/localisation, and its inline diagnostic collections can be truncated. Static nested .gfx scans and the event-specific handoffs above are the authoritative icon and route evidence for this cleanup.

## Validation performed

- Read the required offline wiki pages and vanilla focus/effects/triggers documentation before inspection.
- Parsed all scoped focus/shared files for duplicate IDs, dangling prerequisite/mutex/has_completed_focus references, title/description localisation keys, and direct icon references.
- Inspected the current Event 003, Event 012, Event 019, and Event 020 trees with read-only hoi4.focus_inspect/hoi4.focus_render calls and preserved artifact links above.
- Reconciled current source against the latest bounded handoffs for Events 005, 006, 007, 010, 012, 014, 015, 016, 018, 019, and 020.

Skipped meaningful validation:

- No hoi4.focus_rewrite call was made because the only current geometry defects are coupled multi-lane layouts or intentional branch-template coordinate reuse.
- No hoi4.focus_raster pass was necessary because this pass did not change focus assets and existing Event 012/014/015/016/018 raster evidence is already recorded by their bounded audits.
- No Hearts of Iron IV executable, live save, save/load, or in-game focus click test was run because live consumer validation belongs to the parent/user.
- No hoi4.probability_inspect sweep was run for route-aware focus selection because Events 006, 012, and 020 require parent-owned scenario matrices and broader route designs before a bounded sweep would be meaningful.
- No full prose review of all 3,216 descriptions/effect tooltips was repeated; static key coverage and sampled reward alignment found no local contradiction.

## Changed files and identifiers

Gameplay files changed: none.

Focus IDs changed: none.

Localisation keys changed: none.

Icon IDs changed: none.

The only file added by this subagent is this handoff: docs/plans/repo_cleanup/subagent_handoffs/focus_cleanup_events_1_20_2026-07-29.md.

## High-priority fixes first

1. Preserve the existing Event 006 HOLD / PARTIAL disposition and coordinate a multi-cluster layout/reachability/AI validation pass before claiming completion.
2. Keep Event 012 world-order readiness false until its 121-icon asset contract is restored atomically, and retain branch-aware overlay geometry rather than rewriting the intentionally stacked templates.
3. Queue Event 005 route-depth work for the compact ancient/high-chaos/factory families using the existing redesign plan; do not bulk-generate generic focuses.
4. Queue Event 020 Rat/Rat King route-depth and national-focus AI design against the accepted 40-50/70-100 architecture targets.
5. If visual polish is a parent priority, perform coordinated layout passes for Event 015 and Event 019 after preserving all route topology; isolated coordinate nudges are unsafe.
6. Treat Event 003 support-node AI defaults as a balance review item only after route anchors and Event 003 strategy plans are scenario-tested.

## Remaining route risks

- No runtime scenario proves every Event 005 successor, Event 006 package/carrier, Event 012 overlay/world-order, or Event 020 archetype/government route reaches its intended focus capstone under live conditions.
- The MCP adapter’s generic vanilla icon and baseline diagnostics can make a valid tree appear globally invalid; use the event-specific evidence and recursive static GFX scan when reviewing.
- Event 012’s two guarded continental loader helpers should be checked for no unintended duplicate load_focus_tree progress reset in the host-succession sequence.
- Event 019’s four connector-through-node warnings and Event 015’s broad crossings remain presentation risks.
- The compact Event 005 trees and Event 020 trees remain deliberately simplified and should not be reported as broad route completion without the existing plans being resolved.

No gameplay simplification or fallback was silently introduced by this audit.
