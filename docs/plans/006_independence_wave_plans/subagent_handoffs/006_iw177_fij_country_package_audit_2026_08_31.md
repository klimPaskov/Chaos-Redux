# Event 006 IW-177 Fiji country package audit

Audit date: 2026-08-31.

Scope: bounded source and admission audit of the IW-177 Fiji package, including country identity, vanilla state/history reuse, characters, leader and portrait wiring, politics, forces, ideas, shared focus and decision surfaces, localisation, flags, cleanup, FORM-39 dependencies, central admission/attestation/Join/runtime adapters, and available engine-side evidence.

Disposition: **NO-CHANGE / FAIL-CLOSED.** The package is internally wired as a dormant FIJ adapter, but it is not content-attested or admissible for normal or scenario execution. No safe Fiji-owned gameplay defect was proven, so no gameplay source was changed. This handoff is the only file written by this audit.

## Package identity and coverage

| Surface | Status | Evidence and exact identifiers |
|---|---|---|
| Accepted identity | PASS as dormant package | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:178` binds IW-177 to Fiji, registered tag `FIJ`, anchor state `636`, region `13`, and reservation group `RG-PACIFIC-ISLANDS`; the research row is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:178`. |
| Tag carrier | PASS | Installed vanilla registers `FIJ = "countries/Fiji.txt"` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:181`; the mod intentionally has no duplicate FIJ country file or FIJ country history file. |
| Package identity trigger | PASS as dormant adapter | `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:32-36` requires `original_tag = FIJ`, an active country scope, and package id `constant:independence_wave_package_id.iw_177`. |
| Country setup | PASS at source, gated at runtime | `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:803-855` prepares laws, leadership, politics, ledgers, shared focus routes, force mapping, AI, and lifecycle only through `can_initialize_independence_wave_iw_177_package`. |
| Leader identity | BLOCKED | `FIJ_independence_wave_founding_congress_chair` is a male centrism country leader at `common/characters/006_independence_wave_characters_registry.txt:1083-1097`, but the retained Sukuna source is explicitly circa 1940s and fails the strict 1936-centered visual gate. |
| Portrait consumer | PROVISIONAL / BLOCKED | `interface/006_independence_wave_small_assets.gfx:97-98` maps the exact leader sprite to the existing DDS, but `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/source_manifest.json:6,14,34,62-64,111-122,153-160` remains `needs_user_review` and `provisional_pending_source_date_and_package_admission`. |
| Politics and parties | PASS at source | `independence_wave_initialize_fij_politics` in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:112-129` sets democratic elections and popularity `44/12/34/10`; party and long-party names are localised at `localisation/english/006_independence_wave_pacific_l_english.yml:246-253`. |
| State and host setup | PASS at source, live proof open | Anchor state `636` is the vanilla Fiji capital and the setup trigger requires FIJ to own and control it while retaining a distinct living former host; exact checks are at `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:247-260,437-489`. |
| Focus framework | PASS as dormant source | Shared tree `independence_wave_focus_tree` imports the FIJ roots at `common/national_focus/006_independence_wave_focus.txt:37-73`; the six FIJ focus ids are defined at `:4167-4260`. |
| Decisions and mission | PASS as dormant source | Category and mission are in `common/decisions/categories/006_independence_wave_categories.txt:519-523` and `common/decisions/006_independence_wave_pacific_decisions.txt:444-556`; the six project decisions use the same FIJ flags and costs, and the 250-day mission is fail-closed while inactive. |
| Starting ideas | PASS as dormant source | `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact` are defined at `common/ideas/006_independence_wave_ideas_registry.txt:3584-3612` with existing shared idea pictures and FIJ package limits. |
| Forces | PASS at source, runtime proof open | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:178` maps IW-177 to `coastal_maritime`, force level `53`, coastal/local infantry, navy inheritance `yes`, air inheritance `no`, and the inter-island replacement tradeoff. Dynamic application is gated at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:841-845`. |
| AI | PRESENT but unquantified | FIJ coastal survival, founding restraint, and severe-host profiles are at `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:2412-2437`; the constants are at `:2303-2311`. The mandatory probability audit could not run because the auditor/MCP route is unavailable in this subagent context. |
| Flags | PASS by intentional reuse | IW-177 reuses the installed vanilla FIJ normal, medium, and ideology flag triplets; no new FIJ flag was invented or added. |
| Localisation | PASS for current source | Party, leader, ideas, category, mission, decision, focus, tooltip, and FORM-39 display keys are present in `localisation/english/006_independence_wave_pacific_l_english.yml:246-305` and `localisation/english/006_independence_wave_formable_registry_l_english.yml:87,131-199`; the Pacific file has a UTF-8 BOM. |
| Cleanup | PASS at source | `independence_wave_cleanup_iw_177_fiji` at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:1017-1060` removes the mission, six decisions, three ideas, five ledgers, setup/lifecycle/AI/route flags, selected formable family, and temporary leader, and restores the generic tree only when the shared tree is present. |

## File surface checklist

The current package is intentionally distributed across shared Event 006 registries rather than a standalone FIJ folder.

| File surface | Current state |
|---|---|
| `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` | Contains FIJ setup, politics, dispatch, final validation, force application, and cleanup. |
| `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt` | Contains FIJ identity, setup, prepared, and complete-package predicates. |
| `common/characters/006_independence_wave_characters_registry.txt` | Contains the single named FIJ founding-congress chair. |
| `history/general/006_independence_wave_character_recruitment_registry.txt:68-71` | Recruits the FIJ leader from the shared registry when the FIJ carrier exists. |
| `common/national_focus/006_independence_wave_focus.txt` | Contains shared tree registration and six FIJ focus definitions. |
| `common/decisions/categories/006_independence_wave_categories.txt` and `common/decisions/006_independence_wave_pacific_decisions.txt` | Contain the FIJ founding-congress category, mission, and six decisions. |
| `common/ideas/006_independence_wave_ideas_registry.txt` | Contains the three FIJ package ideas. |
| `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` | Contains FIJ AI profiles and priorities. |
| `interface/006_independence_wave_small_assets.gfx` | Contains the exact FIJ leader sprite definition. |
| `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds` | Exists as a `156x210` DDS with valid `DDS ` magic, 131168 bytes, and SHA-256 `31FEA5EB5C7C4B6F34EC138ED6A3168A7C6C39755A992BD6ABF0296C5838D2C6`; it remains provisional. |
| `localisation/english/006_independence_wave_pacific_l_english.yml` | Covers current FIJ party, leader, idea, focus, decision, mission, category, and tooltip keys. |
| `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` | Owns the current FORM-39 trigger source at `:1558-1669`; older handoff references to a retired `006_independence_wave_form39_triggers.txt` path are stale documentation references, not live files. |
| `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` | Owns the current FORM-39 effects at `:2760-3070`. |

No mod-local `common/countries/FIJ*.txt`, `history/countries/FIJ*.txt`, or `history/states/636*.txt` file was found, which is correct for the accepted reuse of the vanilla registered FIJ carrier and state.

## Map, state, and starting setup

The installed vanilla source binds state `636` to Fiji at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/636-Fiji.txt`. It is a `small_island` state with owner `ENG`, core `FIJ`, infrastructure `2`, naval base `1` at province `4286`, one victory point at `4286`, and provinces `4286 7302 12159`.

The installed vanilla country history at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/FIJ - Fiji.txt` uses capital `636`, infantry weapons level `1`, `20` convoys, democratic elections, and the baseline popularity split `50/6/38/6`; IW-177 setup replaces only the package-owned politics and dynamic release surfaces.

The accepted state reservation row is `RG-PACIFIC-ISLANDS` in `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`, where IW-177 shares the coarse-island reservation group with IW-175, IW-176, and IW-179. The reservation effect consumes only state `636` at `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:4119-4126`.

The runtime setup requires state `636` to remain FIJ-owned and controlled, remain the capital, and retain a distinct living former host with the protected-state relationship intact. This is source-coherent and correctly fail-closed, but installed-map live proof was not available through the required MCP route.

No state, province, ownership, controller, railway, supply, port, resource, building, or protected-host source patch is safe from this audit. Extended territory remains a later claims, diplomacy, plebiscite, or formable surface under the accepted spec.

## Politics, leader, portrait, flags, advisors, and parties

IW-177 sets `ruling_party = democratic`, `elections_allowed = yes`, and the package constants `fij_start_democratic = 44`, `fij_start_communism = 12`, `fij_start_neutrality = 34`, and `fij_start_fascism = 10` in `common/script_constants/006_independence_wave_constants_registry.txt:7366-7369`. The four party names and long names are complete and use institutional/community language rather than generic names.

The exact leader id is `FIJ_independence_wave_founding_congress_chair`. It is recruited by the shared history registry, has `gender = male`, uses centrism, and has no unsupported female metadata or opposite-gender name-pool pairing. The current localisation names Ratu Sir Lala Sukuna, whose role/community fit is strong, but the retained National Archives of Fiji image is dated circa 1940s and therefore fails the strict 1936-centered visual gate.

The retained Pt. Vishnu Deo image is dated 1929 but is an anonymous halftone and does not match the current founding-congress-chair role because the research records his Legislative Council service in 1929 and again from 1937, not during the 1936 baseline. Silently changing the person, role, or localisation would be an identity redesign and is outside this audit.

The portrait worker evidence remains review-only in `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/source_manifest.json`. The existing DDS/GFX consumer is present, but no final source-cleared runtime promotion is authorized. No advisor, operative, high-command, commander, dossier, or extra portrait was requested or invented.

No FIJ-specific flag asset is needed for the accepted carrier. Existing vanilla FIJ flag triplets are the source of truth, and the repository flag-family validator reports no incomplete Event 006 families.

## Focus, decision, idea, and asset issues

The six focus ids are `independence_wave_fij_convene_constituent_congress_focus`, `independence_wave_fij_register_communal_veto_focus`, `independence_wave_fij_open_labor_shipping_board_focus`, `independence_wave_fij_settle_colonial_accounts_focus`, `independence_wave_fij_charter_coastal_guard_focus`, and `independence_wave_fij_ratify_island_compact_focus` in `common/national_focus/006_independence_wave_focus.txt:4167-4260`. They are connected under the shared `independence_wave_focus_tree`, gate on FIJ package identity, and use existing shared focus icons.

The mission id is `independence_wave_fij_hold_constituent_congress_together`, and the decision ids are `independence_wave_fij_convene_constituent_congress`, `independence_wave_fij_register_communal_veto`, `independence_wave_fij_open_labor_shipping_board`, `independence_wave_fij_settle_colonial_accounts`, `independence_wave_fij_charter_coastal_guard`, and `independence_wave_fij_ratify_island_compact`. Their visible names, descriptions, tooltips, activation checks, timeout, cancellation, payment, and cleanup references are localised and source-aligned.

The idea ids are `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact`. Their lifecycle is attached to FIJ package cleanup, and their icon references are existing shared Event 006 ideas rather than missing FIJ-only art.

No missing FIJ focus icon, decision icon, idea icon, flag, leader GFX key, localisation key, or runtime DDS path was found in the bounded source review. A production MCP focus render/inspect pass was required but unavailable, so this is source evidence only and not an engine-render claim.

## Starting military, technology, industry, supply, and production

The accepted force row in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:178` selects `coastal_maritime`, military tradition `53`, engineers/reconnaissance/coastal signals/maintenance first, and inter-island depot requirements for artillery and logistics. The constants bind profile `p177 = 5` at `common/script_constants/006_independence_wave_constants_registry.txt:2201`, tradition `p177 = 53` at `:2415`, reinforcement mask `p177 = 659` at `:2629`, navy inheritance mask `p177 = 1` at `:2843`, and research sensitivity `p177 = 0` at `:3057`.

The setup applies the dynamic starting force only when the Pacific command structure and command roster are ready at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:817-845`. This avoids an unsupported static army, navy, air force, equipment windfall, or OOB in the reused vanilla carrier.

The vanilla baseline has infantry weapons level `1`, `20` convoys, no FIJ OOB, infrastructure `2`, and naval base `1`. No custom FIJ technology tree is claimed, and no technology dependency was invented. The installed package exposes no Technology Tree Viewer, so prerequisite, unlock, and rendered technology evidence remain unresolved.

No source evidence authorizes a larger army, aircraft, additional production lines, extra research slots, fuel, trains, convoys, or supply capacity. Those remain parent-owned balance decisions if later design work supplies them.

## AI and playability

The FIJ AI profiles are `independence_wave_fij_coastal_congress_survival`, `independence_wave_fij_founding_restraint`, and `independence_wave_fij_host_threat` at `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:2412-2437`. Their priorities cover army, infantry/support, convoys, fuel silo, infrastructure, dockyards, coastal defence, and avoidance of an unprepared founding war.

The mandatory AI/probability pass was not completed. The `chaosx_ai_probability_auditor` route is not exposed in this subagent context, and the direct HOI4 probability route was absent from `ALL_TOOLS` (`available = undefined`, advertised list empty). The prior 2026-08-26 closure handoff also records the required probability/MCP transport as closed. Therefore this audit makes no quantitative claim about AI weights, strategy factors, or probability outcomes.

## Central admission, attestation, Join, and runtime adapter gates

The runtime adapter predicate includes IW-177 at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63`, specifically `:27`. The central content-attestation predicate at `:159-202` omits IW-177. The shared preflight at `:207-213` requires both adapter presence and content attestation, so FIJ remains rejected before package mutation.

The normal exact FIJ branch remains present at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:320-323`, and the exact scenario branch remains present at `:529-532`; both are unreachable for IW-177 while central content attestation is absent.

The attestation-ordered Join probe at `common/scripted_effects/006_independence_wave_join_effects.txt:234-270` ends with IW-184 and does not include IW-177. This is correct while IW-177 is unattested; adding FIJ to Join now would violate the ordered-attestation contract.

The planner's IW-177 automatic-weight wrapper at `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:3885-3893` initializes a zero weight and calls `can_plan_independence_wave_package_iw_177`, while IW-173 and IW-179 wrappers additionally set an execution id and check attestation. This is an observed central consistency follow-up, not a Fiji-owned defect to patch here. The FIJ planner trigger at `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:1252-1259` still calls `is_independence_wave_candidate_tag_available`, whose legacy gate at `common/scripted_triggers/006_independence_wave_package_triggers.txt:71-77` requires `independence_wave_package_content_ready`. A current source scan found no setter for that flag, so FIJ remains dormant rather than gaining an admission bypass.

The next central owner should reconcile planner-wrapper conventions before any future promotion, then add IW-177 to content attestation and the attestation-ordered Join list only after the package and visual/formable gates pass. This audit does not edit those shared central files.

## FORM-39 Melanesian Federation blockers

The live FORM-39 trigger source is `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:1558-1669`, not the retired path named by some older handoffs. It requires exact FIJ/IW-177/state-636, PNG/IW-178/state-523, and WPG/IW-157/state-669 member packages, their research flags, frozen member and invitation arrays, the MFX identity reservation, reviewed flat-flag package, and identity-review flag.

The readiness predicate at `:1661-1669` requires `independence_wave_fij_melanesian_route_adapter_complete`, `independence_wave_form39_x_tag_reserved`, `independence_wave_form39_flag_package_ready`, `independence_wave_form39_identity_review_complete`, and the exact researched member packages. A source scan found only trigger checks and FIJ cleanup for these inputs, with no gameplay setter for the FIJ route adapter, FIJ/PNG/WPG research flags, MFX reservation, flat-flag readiness, or identity review.

The current FORM-39 effects are in `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:2760-3070`; readiness attestation at `:2775-2787` is correctly conditional and does not create missing evidence. The event documentation at `docs/events/006_independence_wave/form39_melanesian_federation.md:9-35` correctly keeps the route fail-closed.

IW-178 PNG and IW-157 WPG still lack accepted named-community/district package evidence, identity and portrait decisions, force/host setup, and runtime proof. MFX flat assets exist as review evidence, but identity and collision gates remain closed. Do not substitute generic Papua, generic Melanesia, an invented federation identity, or a new flag.

## Validation and MCP evidence

The following bounded repository validators passed:

- `python -B .tools/audit_event6_allocator.py`: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, 7 adapter-only fail-closed ids including IW-177, 32 attested packages, and 29 compatible reservation groups.
- `python -B .tools/audit_event6_country_api.py`: 242 broad tags, 191 resolved carriers, zero missing, zero duplicates, and IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py`: 102 registered Event 006 tags and complete flag families for all 102.
- `python -B .tools/audit_event6_scenario_matrix.py`: all 32 SCN-008 cells and eight listed edge-case receipts passed; publication dispatch counts/order passed.
- `python -B .tools/audit_event6_form16.py`: FORM-16 readiness, consent, mutation, rollback, and cleanup contract passed.
- `python -B .tools/audit_event6_gui_matrix.py`: Statehood Ledger semantic source matrix passed; no runtime rendering claim was made.

The required read-only HOI4 MCP focus, event, map, and probability routes were not available in this subagent context. Current focus/event/map calls reported “not available to the model” or function-missing errors, while the prior 2026-08-26 closure handoff records `tool call failed ... Transport closed`. The installed package has no Technology Tree Viewer. No MCP rewrite, map write, live-game launch, or source-only substitute was used as engine evidence.

The portrait-specific source and processing evidence was reviewed through the existing `chaosx_portrait_creator` handoff and manifest. It remains provisional and does not clear the source-date, role, or package-admission gates.

## Changes, omissions, and next owner

Changed files: only `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fij_country_package_audit_2026_08_31.md`.

Changed tags, states, leaders, parties, focus ids, decision ids, idea ids, localisation keys, formable ids, central gates, Join order, AI values, assets, and map data: none.

No simplification or unapproved fallback was made. No generic leader, opposite-gender portrait/name pairing, invented flag, fallback focus tree, generic formable route, or admission shortcut was added.

Next owner actions are to obtain an attributed, rights-reusable, role-valid male Fiji source dated no later than 1936 or explicitly approve and document an era exception; complete the named FIJ/PNG/WPG FORM-39 research, route, MFX identity, flag, collision, consent, and runtime evidence; rerun the unavailable focus/event/map/probability MCP inspections and the mandatory probability compare through `chaosx_ai_probability_auditor`; then update central content attestation and attestation-ordered Join only in a separate reviewed promotion change.

Until those gates pass, keep IW-177 adapter-only, keep FIJ outside central attestation and Join, and keep FORM-39 undiscoverable.
