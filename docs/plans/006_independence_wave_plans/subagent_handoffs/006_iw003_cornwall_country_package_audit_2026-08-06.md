# IW-003 Cornwall country-package audit

Date: 2026-08-06

Scope: accepted Event 006 registry/research binding, installed-map and vanilla history, regional dispatch, country package surfaces, focus/decision/idea/AI/force coverage, portraits, flags, localisation, and installed-tag collision evidence.

Verdict: **HOLD / fail-closed. No complete playable package or narrow gameplay promotion is safe.**

No gameplay, map, tag, asset, localisation, adapter, or attestation file was edited in this audit. The only change is this handoff.

## Accepted binding and current authority

- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` binds `IW-003` to `Cornwall`, tag `ACX`, reservation group `RG-123`, baseline state `123`, and the `automatic_pool_ready` research disposition.
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv` says `RG-123` may reserve state 123 only when the anchor is unique, the tag is not living, and the host-remnant test succeeds; it also requires rebinding public-baseline IDs against the installed map.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` current IW-003 override and the dated `subagent_handoffs/006_iw003_acx_admission_audit_current_2026_08_03.md` supersede the registry's optimistic disposition: the installed-map contract has no legal unique contiguous state ID, ACX remains dormant, and no filler state, map renumbering, fallback identity, or attestation bypass is authorized.
- `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt` explicitly omits IW-003 because the accepted current-map audit found no unique Cornwall anchor.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt` adds `iw_003` and `ACX` to the blocked scenario arrays in `independence_wave_scenario_append_unbound_registry_rows`.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` does not include `iw_003` in `has_independence_wave_runtime_package_content_attestation_for_execution_id`; the accepted list starts with IW-001, IW-002, IW-004, and the other admitted packages.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` has no Cornwall setup, final-validation, or cleanup adapter call, and its shared final barrier cannot admit ACX without a package adapter, content attestation, generic focus contract, and generic AI profile.

## Country-package coverage checklist

| Surface | Status | Evidence and gap |
|---|---|---|
| Tag registration | PASS as reservation only | `common/country_tags/006_independence_wave_countries.txt` maps `ACX` to `countries/006_independence_wave_ACX.txt`. |
| Country shell | PASS as shell only | `common/countries/006_independence_wave_ACX.txt` contains graphical cultures and map color only. |
| History/start setup | HOLD | `history/countries/ACX - Cornwall.txt` is neutral placeholder history with no capital, territory, units, technology, industry, ideas, or characters. |
| State/map anchor | BLOCKED | Research points to state 123, but the accepted installed-map authority rejects it as a legal unique contiguous anchor. |
| Host survival | BLOCKED | No adapter reserves a protected ENG remnant or proves post-transfer host validity. |
| Politics and parties | BLOCKED | No ACX runtime party, popularity, laws, elections, stability, or war-support setup exists. |
| Leaders/characters | BLOCKED | No ACX character definitions, leader IDs, advisors, generals, or commanders are wired. |
| Portraits | BLOCKED | ACX portrait stems exist only in the readiness-pool archive; no runtime DDS/GFX consumer or character wiring exists. |
| Flags | EVIDENCE ONLY | ACX TGA triplets exist and are hash-listed, but the source authority marks them unregistered readiness-pool art; this is not package admission evidence. |
| Localisation | PARTIAL PASS | Base, adjective, DEF, and six ideology name keys exist in `006_independence_wave_countries_l_english.yml`; leaders, parties, ideas, decisions, focuses, tooltips, and route keys do not. |
| Ideas/spirits | BLOCKED | No ACX starting, lifecycle, or route idea definitions or consumers found. |
| Focus loading | BLOCKED | No ACX focus assignment or route flags exist; the shared tree cannot substitute for package admission. |
| Decisions/missions | BLOCKED | No ACX decision category, decision, mission, timed objective, or focus-unlocked action exists. |
| Forces/OOB | BLOCKED | No ACX division template, force mapper, equipment stockpile, commander roster, or OOB setup exists. |
| Technology/industry/supply | BLOCKED | No ACX technology, production, industry, port, supply, or starting-stockpile setup exists. The installed package exposes no Technology Tree Viewer, so no engine technology-tree evidence can be produced. |
| AI | BLOCKED | No ACX AI strategy, template policy, diplomacy profile, or focus-choice profile exists. There is no ACX probability surface to evaluate; any future AI weight must receive the mandatory probability-auditor pass. |
| Cleanup | BLOCKED | No ACX release rollback, annexation, puppet, transfer, subject, or stale-flag cleanup branch exists. |

## File-surface checklist

### Present scaffolding

- `common/country_tags/006_independence_wave_countries.txt`
- `common/countries/006_independence_wave_ACX.txt`
- `history/countries/ACX - Cornwall.txt`
- `localisation/english/006_independence_wave_countries_l_english.yml`
- `common/script_constants/006_independence_wave_package_constants.txt`
- `common/script_constants/006_independence_wave_country_registry_constants.txt`
- `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt`
- `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt`
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt`
- `common/scripted_effects/006_independence_wave_focus_effects.txt`
- `common/national_focus/006_independence_wave_focus.txt`

### Missing ACX-owned surfaces

- Cornwall setup, final-validation, and cleanup adapter file and its package triggers.
- Region 01 planner/weight/reservation/loader branch for IW-003.
- ACX characters, country leader, generals, commanders, traits, and portrait consumers.
- ACX party names, political setup, starting laws, ideas, spirit lifecycle, and decision/mission category.
- ACX force/OOB setup, templates, equipment, technology, production, industry, port, and supply setup.
- ACX AI strategy and focus-selection policy.
- ACX focus assignment, route flags, package-specific focus or additive overlay contract.
- ACX-specific decisions, missions, tooltips, and scripted effects/triggers.
- Final asset manifest and accepted runtime portrait evidence.

## Map and state setup

Vanilla `history/states/123-Cornwall.txt` is a single Cornwall state owned and cored by ENG with provinces `540 3422 3463 6526 9562 11406`, victory points at 540 and 6526, a level-8 naval base at province 540, infrastructure, industry, anti-air, radar, and air base. The mod has no `history/states` override.

The vanilla state is therefore a useful historical/map precedent but not an accepted Event 006 binding. Vanilla ENG also has Cornwall-specific focus logic in `common/national_focus/uk.txt` and decisions in `common/decisions/ENG.txt` and `common/decisions/resource_prospecting.txt`; a future ACX release must preserve or intentionally retire those host consumers while leaving the rest of ENG's meaningful tree intact.

The required read-only `hoi4_map_inspect` pass for state 123 and provinces `540, 3422, 3463, 6526, 9562, 11406` succeeded. Evidence is linked at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af172af58e69c160186f1ec25bce1effcddcf5dcf9bc0aa863c3399220debd66/cac6050d5c62388c9f585e21c0e49cbeb8faffa425d8468ebc68499e72e5ce88/map-inspect.7bad7eba914b9c33.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a73d237330ffc44789e63a99a9f11a213815439f0ec689fd97e0e9c1a07ce67/d296dc3704b0b6ca57ff52b720c2380402287ad5525cb02d671a2769a69fceda/map-province-geometry.7bad7eba914b9c33.ba05b31b47c2bab7.json`. All six province IDs and the state membership resolved, but the global map scan carries unrelated building/locator diagnostics.

The required `hoi4_map_render` pass with the state layer and port/victory-point/resource/building/supply/railway/adjacency overlays succeeded with `MAP_RENDERED` and passed its render validation. The PNG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c8a38f2a0c09e2af8e7995c5a27803696c79c642b4d19a9fb7e001d8d2e9ae9/ff97e695e82ca6e872baab0ab4b87f3b8c065999c078157934bfc6e07f7c18fa/map-state.png`; JSON and HTML companions are in the same artifact group. This is whole-map structural evidence, not a new accepted reservation. The prior current-map audit remains the binding blocker: state 123 is not a legal unique contiguous reservation under the installed Workshop layout.

## Politics, leaders, portraits, flags, advisors, and parties

The research resolution requires a provisional assembly, cabinet, municipal council, or congress with regionally sourced institutional naming and sourced male officeholder or authentic archival evidence. It also requires a period civic flag from researched regional motifs and forbids presenting an invented historical flag as authentic.

`docs/assets/006_independence_wave/northern_western_europe_source_manifest.md` identifies St Piran's Cross as a Cornish community motif and states that the ACX TGA triplet is an exact design input, not evidence of a sovereign 1936 Cornish state. `gfx/flags/ACX.tga`, `gfx/flags/medium/ACX.tga`, and `gfx/flags/small/ACX.tga` are present and hash-listed, but the same source authority marks ACX flag and portrait consumers as readiness-pool/unregistered. No ACX leader, advisor, party, or portrait runtime wiring was found.

`docs/assets/006_independence_wave/portrait_refresh_male_hoi4_2026_07_18/manifest.md` lists fictional male institutional and coastal-commander stems, but current source-of-truth documentation keeps ACX outside registration. The bounded source-placeholder tranche now provides `gfx/leaders/006_independence_wave/portrait_ACX_cornish_port_and_mines_committee.dds` plus archived source/crop evidence, but there is still no ACX `.gfx` sprite or character consumer; `portrait_ACX_cornish_coastal_commander.dds` remains absent. Do not turn the unregistered source placeholder or archive/readiness outputs into a playable leader without a fresh portrait-worker role review and package admission review.

## Focus, decision, idea, and asset evidence

`hoi4_focus_inspect` on `common/national_focus/006_independence_wave_focus.txt` succeeded for `independence_wave_focus_tree` and reported 184 nodes, no authored branches, one long shared connector, and five diagnostics. The corresponding `hoi4_focus_render` succeeded structurally but returned 14 blocking missing-icon diagnostics and layout warnings. The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f870424025618ad2f10cd5ae4346e1269875f91c332ce2fb5e7f64814470ebb/51ce3f9d6ede1ef10b020815c1327e32f00160a440a079406840d30aeb3c0653/focus-inspect.589775a6a495eb68.json`; the rendered HTML is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77c1af84241a4da87ed185d5f0a81296f92e1cf7d4d338be09412ce2e88a85d7/44601650b9b999ddb7dbd38777e37dc078f6e8db08b973c0370ea8f757139307/independence_wave_focus_tree.focus.html` and its SVG/JSON companions are in that artifact group.

The generic tree is an available framework, not ACX content. Loading it without a package adapter, ACX route flags, ideas, decisions, forces, AI, and host cleanup would be a shallow placeholder and would fail the central runtime content-attestation gate.

No ACX-specific idea, decision, mission, icon, advisor, or route asset surfaces were found. Shared Event 006 icon families do not prove country-specific coverage.

## Installed-tag collision evidence

The current audit `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_08_06.json` records `ACX` in the Event 006-owned identifiers and in the owned history filename `history/countries/acx - cornwall.txt`. Its collision arrays are empty for ACX, custom cosmetic collision count is zero, and binding identity-match count is zero. The audit therefore supports retaining ACX as the reserved X tag; it does not establish map or package readiness. The same audit records 17 other reserved-tag collisions, so future tag changes must not reuse a casually selected namespace.

## Required implementation order if IW-003 is reopened

1. Obtain an accepted installed-map rebind proving a legal unique Cornwall anchor and a valid protected ENG remnant; do not add a filler state, renumber the map, or use a fallback identity.
2. Re-run the full installed tag/cosmetic/history/localisation/flag collision audit and retain ACX only if the collision-free result remains current.
3. Accept a country design tranche covering provisional government, party/politics, starting ideas, forces, industry/supply, decisions/missions, AI, focus assignment, route flags, host settlement, and cleanup before any automatic-pool or attestation change.
4. Route the complete leader/portrait package through `chaosx_portrait_creator`; source or archive male subjects/institutional evidence and wire only accepted runtime outputs. Keep names/presentation gender-consistent.
5. Route the flag package through the asset source/review process; document St Piran's Cross as a community motif or explicitly alternate civic design rather than a fictional sovereign historical claim.
6. Implement a dedicated ACX adapter and region-01 loader/weight/reservation branches with dry-run, review, apply, post-validation, and rollback evidence; only then add IW-003 to runtime content attestation.
7. Re-run map/focus/event/probability MCP checks for the final package. The installed package has no Technology Tree Viewer, so technology-tree engine validation remains an explicit unresolved limitation.

## Simplifications, omissions, and blockers

- No country package gameplay was patched because the map binding and package-content gates are both hard blockers.
- Existing generated/readiness-pool flags and portraits are not treated as runtime admission evidence.
- The shared generic focus tree is not treated as a Cornwall focus tree or a substitute for country mechanics.
- No map rewrite was attempted because the accepted authority forbids filler-state allocation and no user-approved map design exists.
- No probability compare was run for ACX because no ACX AI or weighted package surface exists; any future AI/weight change must be routed through the mandatory probability-auditor workflow.
- No technology-tree MCP evidence exists because the installed package currently exposes no Technology Tree Viewer.

Reopen reference: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw003_acx_admission_audit_current_2026_08_03.md`.
