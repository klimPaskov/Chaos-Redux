# IW-036 Courland (BJX) preflight audit

Audit date: 2026-08-10.

Scope: read-only country-package and admission preflight for Event 006 IW-036 Courland, with current-map, host-survival, tag, identity, asset, force, focus, formable, network, event, and weighted-pool checks. No gameplay files were changed, and no readiness flag or admission branch was granted.

## Disposition

IW-036 is **fail-closed and not viable for admission**.

The candidate has a valid dormant BJX shell, a unique static Kurzeme anchor, and a collision-free X-tag in the current installed audit. The package does not have an executable Event 006 adapter, content attestation, package setup/final-validation/cleanup lifecycle, identity roster, provenance-cleared flag, force mapping, AI strategy, decisions, ideas, or country-specific focus/formable contract. The correct next action is the bounded implementation plan at `docs/plans/006_independence_wave_plans/006_iw036_courland_plans/006_iw036_courland_bounded_implementation_plan.md`; do not promote from registry or region-04 plumbing alone.

## Country-package coverage checklist

| Surface | Result | Evidence and exact gap |
| --- | --- | --- |
| Tag registration | Partial | `common/country_tags/006_independence_wave_countries.txt:30` registers `BJX = "countries/006_independence_wave_BJX.txt"`; `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:43` includes `original_tag = BJX`. |
| Tag collision | Pass for current audit scope | `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_08_06.json` reports zero BJX collision rows and zero BJX identity matches across the vanilla game, scanned workshop roots, local mods, archives, and Chaos Redux non-Event-006 surfaces. The audit explicitly excludes Random Events because it is an event-only compatibility surface. |
| Country shell and history | Partial | `common/countries/006_independence_wave_BJX.txt:1-9` owns only graphical cultures and map color; `history/countries/BJX - Courland.txt:1-15` is a neutral dormant loader with no capital, OOB, technology, production, or runtime lifecycle. |
| Country localisation | Partial | `localisation/english/006_independence_wave_countries_l_english.yml:241-256` supplies Courland/Curonian keys for all ideologies, but no route, party, leader, advisor, idea, decision, or package-specific text exists. |
| Current-map anchor | Pass as static candidate, runtime evidence still required | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:37` binds IW-036 to state `190` Kurzeme with `190=LAT` and `LAT=808`. Vanilla `history/states/190-Kurzeme.txt:4-25` contains the same six-province state and LAT owner/core. The mandatory MCP map inspection returned `MAP_INSPECTED` for state 190 and provinces 3194, 3296, 3319, 6322, 9262, and 11246 with valid state membership and network checks; the linked artifact is recorded below. |
| Host survival | Conditional pass | Vanilla `history/countries/LAT - Latvia.txt:1` sets Latvia's capital to state 808, while state 190 is a separate coastal state. Releasing 190 can preserve the host capital and other Latvian states, but the runtime trigger at `common/scripted_triggers/006_independence_wave_package_triggers.txt:9-18` checks only owner/controller/Soviet/reservation/protected-state conditions and does not prove the final LAT remnant. A BJX adapter must add a final host-remnant proof and Event-005 conflict guard. |
| Reservation group | Partial | IW-036 is in `RG-BALTIC-LIVONIA` with IW-034 and route-only IW-035 at `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:67`. The group permits at most one automatic package and reserves protected host states before this group. |
| Identity and community | Research-ready but unresolved | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:37` requires a period royal/customary/historical institution joined to a provisional cabinet, municipal administration, veterans, schools, labor, and assembly, with mixed-population rights/autonomy routes. No concrete community or institutional roster is yet selected in gameplay files. |
| Leaders and portraits | Blocked | No BJX character, advisor, commander, high-command, or portrait files exist under `common/characters`, `common/country_leader`, `gfx/leaders`, or `interface`. The research resolution requires sourced real male officeholders or authentic archival material for the actual institution and blocks the package when neither can be established. Grounded portraits cannot be replaced by generated personal portraits. |
| Flags and symbols | Present but blocked | BJX base and ideology TGA families exist under `gfx/flags/BJX*.tga`, `gfx/flags/medium/BJX*.tga`, and `gfx/flags/small/BJX*.tga`, but provenance is not cleared. `docs/plans/006_independence_wave_plans/asset_research/006_generated_flag_blockers.md:23` and `006_package_asset_coverage.md:110` explicitly list IW-036 as blocked pending exact symbol owner, date, function, route, and license review. |
| Politics and parties | Blocked | The dormant history sets neutrality to 100 with elections disabled; no BJX party names, popularity setup, route leaders, laws, diplomatic stance, stability/war-support tuning, or cleanup exists. |
| Focus tree | Blocked | The shared `independence_wave_focus_tree` exists and is inspectable, but no BJX package adapter assigns it or publishes route hooks. No BJX focus IDs or localisation are present. |
| Decisions and ideas | Blocked | No IW-036 decision category, paid project, mission, idea lifecycle, idea icon, or cleanup file exists. The three BJX mentions in `common/decisions/006_independence_wave_iw043_iw058_decisions.txt:770,1450,1819` are generic target lists, not Courland package content. |
| Force and starting setup | Blocked | Research/force matrix row `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:37` specifies coastal guards and territorial infantry, profile `coastal_maritime`, and military identity 49, but no IW-036 code maps this row to a setup effect, template, stockpile, manpower, production, port, supply, or cleanup. |
| Technology | Unresolved limitation | No custom BJX technology surface exists. The installed package exposes no Technology Tree Viewer, so technology-tree MCP evidence cannot be produced if a later package adds custom technology. |
| AI and playability | Blocked and quantitatively unresolved | No `common/ai_strategy` IW-036 file exists. The Region-04 random pool contains IW-036, but no package-level score or survival strategy is implemented. Do not claim an AI balance result. |
| Formable and regional route | Blocked | The generic registry has a Baltic Federation profile at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:190-199`, and generated Baltic state-puzzle manifests include state 190. However, `is_valid_independence_wave_formable_founding_carrier` at `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:116-166` has no Baltic branch, and the commit/readiness allowlists at `:551-629` likewise omit it. Existing `EU_baltic_expansion_decision` state list at `common/decisions/formable_nation_decisions.txt:3254-3347` belongs to vanilla EU content and is not a BJX route. |
| Network and event integration | Blocked | Root Event 006 exists, but no IW-036 event, network receipt, route decision, host settlement, or package-specific event integration exists. |

## Exact admission blockers

1. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-55` has no `iw_036` runtime adapter entry, and `:135-173` has no IW-036 content-attestation entry.
2. The normal and scenario preflight OR-lists at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:181-356` and `:356-500` have no BJX/state-190 branch, so an otherwise prepared package cannot execute.
3. `common/scripted_triggers/006_independence_wave_packages_region_04_triggers.txt:28-35` gates IW-036 through `is_independence_wave_candidate_tag_available`; that legacy trigger at `common/scripted_triggers/006_independence_wave_package_triggers.txt:46-49` requires `independence_wave_package_content_ready`. No BJX grant exists, and the file comments forbid granting this flag as a shortcut.
4. `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt:41-50,122,145,154` provides only a planner wrapper and state-190 reservation call. It does not create country setup, politics, forces, ideas, focus, AI, decisions, assets, host settlement, or cleanup.
5. No IW-036 package-specific setup, final-validation, cleanup, force, AI, decision, idea, character, portrait, or event files exist.
6. Identity research is medium-confidence and has no selected institution, named leader, male source-placeholder, or symbol ownership dossier. `IW-036` is explicitly blocked in the generated-flag/asset coverage ledgers.
7. Event-005 collision handoff identifies Livonia/Courland versus Latvian and Estonian spaces as a high-risk different-tag geographic collision. Event-005 must publish its exact footprint before BJX can pass final host/conflict validation.
8. The Baltic Federation profile is only registry metadata until a family-specific founding-carrier, territory, identity, flag, member-policy, readiness, and commit adapter is added; state-puzzle art for state 190 is not a BJX admission proof.
9. The installed Technology Tree Viewer is unavailable. This is an unresolved tooling limitation, not evidence of technology completeness.

## MCP evidence and limitations

The mandatory `hoi4.map_inspect` call used workspace `mod_chaos_redux_ea3b2d67c2c0` and returned `MAP_INSPECTED` for state 190 and the six state provinces. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f8d030da4408df5433b03d74015f87e9b6a16100efc434da5a276e631ebdba6/b048bac882cc3dced10b321327ad91607480fcab9c15dc9792361145a1b870df/map-inspect.fa968eed150af9e7.json`.

The map inspection's state-membership, bitmap, adjacency, supply-node, and railway checks passed. Whole-workspace diagnostics reported unrelated building-position and floating-harbor errors plus a localisation BOM error in `012_africa_elephant_operations_l_english.yml`; no selected-state blocker was returned. The linked MCP result does not inline the selected owner/controller rows, so owner/controller safety remains source-bound until the final package transaction is inspected with a frozen runtime scenario.

The matching owner/network render returned `MAP_RENDERED` with validation passed. Owner PNG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0610a166e8e08877d5a2fc27cddb5656b9ad93125156adfcd25b08ff7eef74c/962a7b44f13613da2314abe7024f3590312af3460403217f00050f849e71e475/map-owner.png`.

The shared focus inspection returned `FOCUS_INSPECTED` for `independence_wave_focus_tree` with 184 focuses, 193 connectors, zero crossings, and zero node intersections. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5082a2f1a12bdfbe31ca1e369d51b93c93e67b0f301a105c9071109e4900fc0/9826e228e0b69db15584f75a35435da60ec9e95c7484b27f9b5b4fd6594be646/focus-inspect.9be13b2cf8f8c522.json`.

The focus render returned `FOCUS_RENDERED` for the same tree. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb40f2bfb9a1333fa26ada4991a5b0b787d21d4fe3ea999e62e0b7cdbd3c5ec6/4f6f8542b95ad550e41e818d04fee2eabeeacbf778a6ee0f83a1be6d10d81bbc/independence_wave_focus_tree.focus.html`. The inspector reported 14 unrelated missing vanilla continuous-focus sprites and five shared-tree layout warnings; no BJX-specific node exists to validate.

The root Event 006 inspection for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with helper/lifecycle projections deferred and no blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d22b08e60b34260a3145a519f7d5e7e57be599bee41e957210abcae43e94525c/3dc4572dbebaa721c0aa40fa3a78cf237318b0c6199873d349c22c39c23831c4/event-scan-e1ba28da7aaf.json`.

The matching event overview render returned `EVENT_RENDERED_PARTIAL` and deferred the same workspace-wide helper projections. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ec77a32918f4dd253924b39d2fd1f82dde5573ad7a95dda9c102b3ecafa9ec7/fbbd042bc8ca7fa7e0f4dfdb39c3764506894dd7961c93a50584aee483beb045/event-overview-e1ba28da7aaf-manifest.json`.

The mandatory probability source discovery on `common/scripted_effects/006_independence_wave_packages_region_04_effects.txt` selected the `random_list` adapter and found the eight source entries IW-033, IW-036, IW-037, IW-038, IW-039, IW-040, IW-041, and IW-042 with zero unresolved source expressions. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a3f606c41d70d1e1f6597bbfc6fe5c6a0b34900b530ff1e0780291286815c58/8ca0857237bd7a15ae65cc1854813936705bb745055495db23dedac6a73ceab1/probability-inspect-e8f1792fa6b1.json`.

This source-level pool result does not evaluate `can_plan_independence_wave_package_iw_036`, dynamic host/reservation arrays, attestation, or a normalized selection probability. The existing Region-04 probability-auditor handoff records those dynamic inputs as unresolved, so no numeric AI or package-selection claim is made.

## Recommendation

Keep `BJX`, state 190, the reservation-group row, planner wrapper, and dormant shell unchanged and fail-closed. Admit IW-036 only after the bounded plan completes identity and symbol research, a sourced male or institutional portrait decision, package lifecycle and force setup, shared focus assignment and route hooks, AI/decision/idea content, final host/Event-005 guards, Baltic formable-family adapter proof, and the same MCP plus probability-auditor evidence used for admitted packages.

No gameplay patch, asset promotion, readiness grant, history overwrite, or commit was made in this audit.
