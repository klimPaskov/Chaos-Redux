# Event 006 IW-177 Fiji country-package revalidation

Audit date: 2026-08-31.

Scope: FIJ/IW-177 only, including the accepted identity and research rows, reused vanilla carrier and state, package setup and cleanup, leader and portrait consumer, politics, flags, ideas, shared focus and decisions, forces, technology baseline, AI, central adapter and preflight gates, FORM-39 dependencies, and the no-pre-event invariant.

Disposition: **NO-CHANGE / FAIL-CLOSED.** The Fiji package is internally wired as a dormant adapter, but it is not centrally content-attested or admissible for normal or scenario execution. No safe FIJ-owned gameplay defect was proven. This revalidation writes only this handoff and does not alter gameplay, map, flags, portraits, central attestation, allocator, scenario, shared registries, or Join order.

## Country-package coverage checklist

| Surface | Status | Evidence and finding |
| --- | --- | --- |
| Accepted identity | PASS as dormant package | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:178` binds IW-177 to Fiji, registered tag `FIJ`, anchor `636`, region `13`, and `RG-PACIFIC-ISLANDS`; `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:178` is the research authority. |
| Tag and carrier | PASS | Vanilla registers `FIJ = "countries/Fiji.txt"` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:181`; no mod-local `common/countries/FIJ*.txt`, `history/countries/FIJ*.txt`, or `history/states/636*.txt` exists, which is correct for registered-tag/state reuse. |
| Package identity and setup | PASS at source, gated at runtime | `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:32-35` requires original tag FIJ, package-content activity, and IW-177; `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:803-855` gates setup through `can_initialize_independence_wave_iw_177_package`. |
| Leader identity | BLOCKED | `FIJ_independence_wave_founding_congress_chair` is a male centrism leader at `common/characters/006_independence_wave_characters_registry.txt:1083-1097`; the retained Ratu Sir Lala Sukuna source is explicitly circa 1940s against the accepted 1936-centered gate. |
| Portrait consumer | PROVISIONAL / needs review | `interface/006_independence_wave_small_assets.gfx:97-98` and `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds` provide the 156x210 consumer, but `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/source_manifest.json` remains `needs_user_review` and `provisional_pending_source_date_and_package_admission`. The 1929 Vishnu Deo alternative does not match the accepted role/date/source-quality contract, so no identity substitution is safe. |
| Politics and parties | PASS at source | `independence_wave_initialize_fij_politics` at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:112-129` sets democratic elections and the centralized `44/12/34/10` split; party names and long names are at `localisation/english/006_independence_wave_pacific_l_english.yml:246-253`. |
| State and host setup | PASS at source, live proof open | `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:247-260,437-490` requires anchor 636 owned and controlled by FIJ/ROOT, capital status, setup anchor/former-host targets, and a distinct protected former host. |
| Flags and advisors | PASS by bounded scope | FIJ reuses the installed vanilla normal, medium, and ideology flag triplets; the Event 006 flag audit reports all 102 registered families complete. No FIJ advisor, commander, operative, high-command, dossier, or extra portrait was accepted or invented. |
| Focus framework | PASS as dormant source | The shared `independence_wave_focus_tree` imports the FIJ roots at `common/national_focus/006_independence_wave_focus.txt:37-73`; six connected FIJ focus ids are defined at `:4167-4260` and gate on the FIJ package predicate. |
| Decisions and mission | PASS as dormant source | Category `independence_wave_fij_founding_congress_category` is gated at `common/decisions/categories/006_independence_wave_categories.txt:519-523`; `common/decisions/006_independence_wave_pacific_decisions.txt:444-556` defines the 250-day mission and six costed, cancellable project decisions. |
| Ideas and lifecycle | PASS as dormant source | `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact` are at `common/ideas/006_independence_wave_ideas_registry.txt:3584-3612`; setup and cleanup bind their lifecycle to FIJ package state. |
| Force and starting baseline | PASS at source, runtime proof open | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:178` maps coastal-maritime level 53 local/coastal forces, inherited navy, no air inheritance, and inter-island replacement tradeoffs; dynamic application is gated by command and roster readiness at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:817-845`. Vanilla FIJ remains infantry weapons 1, 20 convoys, no OOB, infrastructure 2, and naval base 1. |
| Technology and industry | BOUNDED BASELINE / TOOLING HOLD | No bespoke FIJ technology tree is claimed and no unsupported technologies, research slots, production lines, trains, fuel, or stockpiles are added. The installed package exposes no Technology Tree Viewer, so technology prerequisite/unlock/render evidence remains unresolved. |
| AI and playability | PRESENT / PROBABILITY HOLD | FIJ survival, founding-restraint, and host-threat profiles are at `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:2412-2437`, with priorities at `:2303-2311`; no quantitative ordering or probability claim is made because the required auditor route is unavailable. |
| Cleanup | PASS at source | `independence_wave_cleanup_iw_177_fiji` at `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:1017-1060` clears the mission, six decisions, three ideas, ledgers, route/setup/lifecycle/AI flags, formable selection, and temporary FIJ leader, restoring the generic tree only when present. |

## Map, state, and starting coherence

Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/636-Fiji.txt` defines a `small_island` FIJ-core state owned by ENG with infrastructure 2, naval base 1 at province 4286, victory point 4286, and provinces 4286, 7302, and 12159. Vanilla `history/countries/FIJ - Fiji.txt` defines capital 636, infantry weapons level 1, 20 convoys, democratic elections, and baseline popularity 50/6/38/6.

The read-only `hoi4.map_inspect` pass targeted state 636, region 13, and provinces 4286/7302/12159 and produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99df410818dbafd87bb687cfbb4a600f39ecd3c19991c6986409c466aacbe234/47dd00bd98be7a5e129380af75f0aa93978badab8e69f66ff02a056ef69f87b4/map-inspect.b4b7bdbf66d13006.json`. Province geometry and state-region membership passed for the selected records, while the global map result was not clean because unrelated `MAP_PORT_ADJACENT_SEA_INVALID` and `MAP_BUILDING_POSITION_INVALID` diagnostics were truncated at the server ceiling, plus one unrelated malformed localisation line in `localisation/english/039_murder_mystery_l_english.yml:389`.

The read-only state-layer `hoi4.map_render` pass produced the validated offline artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24f66076c537b9030cd14c38066bd763d40b1462f65a5872796ceec4222530d9/a1d19d8ff3bf18d5143d9110dcdf33f74ece122b32081eef2926f5488bdfd058/map-state.png`. No map write or live ownership/controller proof was attempted.

The reservation contract is `RG-PACIFIC-ISLANDS` at `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:103`, shared with IW-175, IW-176, and IW-179 at one automatic package per coarse anchor group. Extended Fiji territory remains a later claims, diplomacy, plebiscite, integration, or formable surface.

## Politics, leader, portrait, flag, advisor, and party issues

The four FIJ party/local-party pairs are complete and institutional: Constituent Congress, Workers and Wharf Board, Council of Chiefs and Provinces, and Coastal Defense League. The leader uses male metadata and a male name, with no opposite-gender pool or female metadata pairing. The outstanding source-date/role gate is an identity and asset admission blocker, not a safe local gameplay fix.

No FIJ-specific flag asset is required under the accepted registered-carrier contract. The existing portrait DDS/GFX path is retained as provisional evidence only, and no advisor or named-officeholder family is inferred from the country leader.

## Focus, decision, idea, and asset issues

The six focus ids are `independence_wave_fij_convene_constituent_congress_focus`, `independence_wave_fij_register_communal_veto_focus`, `independence_wave_fij_open_labor_shipping_board_focus`, `independence_wave_fij_settle_colonial_accounts_focus`, `independence_wave_fij_charter_coastal_guard_focus`, and `independence_wave_fij_ratify_island_compact_focus`. Their prerequisites, bypasses, package gates, decision handoffs, costs, and localisation are source-aligned.

The six decisions are `independence_wave_fij_convene_constituent_congress`, `independence_wave_fij_register_communal_veto`, `independence_wave_fij_open_labor_shipping_board`, `independence_wave_fij_settle_colonial_accounts`, `independence_wave_fij_charter_coastal_guard`, and `independence_wave_fij_ratify_island_compact`; the mission is `independence_wave_fij_hold_constituent_congress_together`. All current names, descriptions, cost strings, effect tooltips, activation, cancellation, timeout, and cleanup keys are present in the Pacific localisation file at `:246-305`.

The read-only `hoi4.focus_inspect` and `hoi4.focus_render` passes targeted `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree`. Inspect diagnostics reported no blocking FIJ tree issue, zero connector crossings, zero node intersections, and zero long connectors; the only warning was the unrelated vanilla `continuous_restrict_freedom_desc` reference. Useful artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69edebd0e6b0e8528d065d89f4b9872663c93f95e10f00ce3edcf42af7610730/012d2af0dbb270c016237a17b5a5f598226ef16fea0a7b941a33908fc7154d80/focus-inspect.3e9e27b9b2b333a1066a2da584d4a6a17b4d2f192aa640327c44f41990aaa994/focus-inspect.3e9e27b9b2b333a1.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a0e0bc769460f88d7363eed1e3e015b809c0c67b732001dc476e845f7a255d1/a471decd961b8e301b71a66839021e755f16e815d32f7c0d879cfa2ed0fc036d/independence_wave_focus_tree.focus.html`.

## AI, force, and probability evidence

The FIJ AI profiles are correctly gated by FIJ package/setup flags and use `abort_when_not_enabled = yes`. Their values cover army, infantry/support, convoy, fuel-silo, infrastructure, dockyard, coastal-defence, and founding-restraint behavior.

The mandatory `chaosx_ai_probability_auditor` route is not callable in this subagent context because no custom auditor tool or collaboration route is exposed. The direct read-only HOI4 probability discovery call against `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` returned `requestedAdapter = ai_strategy_factor`, `discoveryReason = no_weighted_surfaces`, `candidates = 0`, and `availableCandidates = 0` in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f992c00c29dbd0112b4806af07e40fa781bd0fd0f4af48c5ad16ed51251e3992/51bdb74e781ccb7ca000181555cce2a57c094112c4e279e65c0b30a1af0fbf10/probability-inspect-c5fef71b5a54.json`. This is not treated as the required auditor pass and no AI probability, dominance, or timing claim is made.

## Central adapter, preflight, Join, rights, and no-pre-event invariant

The runtime adapter OR-list contains IW-177 at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63,27`, and exact normal/scenario branches remain at `:320-323` and `:529-532`. The central content-attestation OR-list at `:159-202` still omits IW-177, while shared preflight requires both adapter and attestation, so FIJ is rejected before mutation. The attestation-ordered Join probe at `common/scripted_effects/006_independence_wave_join_effects.txt:234-270` ends at IW-184 and intentionally does not include unattested IW-177.

The current planner wrapper at `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:3885-3893` keeps IW-177 at zero until `can_plan_independence_wave_package_iw_177` and the attestation predicate pass. The planner trigger at `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:1252-1259` still requires the legacy candidate-availability/content-ready gate, so no admission bypass is safe here.

Every FIJ category, mission, decision, focus branch, idea, AI profile, and setup effect is package/setup gated. Before the package predicate and setup-complete flags exist, vanilla FIJ has no Event 006 package id, no package-specific category, no mission, no package decisions, no package focus assignment, and no package-owned ideas. This preserves the no-pre-event invariant in source; no runtime save or live-game claim is made.

The live FORM-39 source is `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:1558-1669` with effects at `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:2760-3070` and documentation at `docs/events/006_independence_wave/form39_melanesian_federation.md:3-35`. It requires exact FIJ/IW-177/state-636, PNG/IW-178/state-523, WPG/IW-157/state-669 member packages, research flags, frozen consent arrays, MFX reservation, reviewed flag package, and identity review. The FIJ/PNG/WPG research and route inputs, MFX reservation, flag readiness, and identity review remain closed with no safe FIJ-only setter; do not add a generic Papua/Melanesia substitute or promote FORM-39 from this audit.

Event root inspection/rendering was performed for `chaosx.nr6.1` using read-only MCP. The bounded render returned selected nodes but remained partial because the workspace contains 9,722 events and deferred helper/lifecycle analysis; artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dcdf6e2179e1ad9f99bf884ab2524bd15787fcac3620898e34aa44ca642cd144/291c486b7aec95bd5e38c4b1e6a526c905b5499492790ca59faafe00b03c5579/event-overview-2725045f62d1-manifest.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4533b65525a1b9fe638d88625524385d151a786261e318847b7249af96a290b9/78eb9026381117ad4740f15a9391214c63caa3b939bc6a818bb6736073d89cec/event-overview-2725045f62d1.png`. No FIJ-specific event defect was exposed by the bounded result.

## Validation and changes

The current focused validators passed:

- `python -B .tools/audit_event6_allocator.py`: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, eight adapter-only fail-closed ids including IW-177, 32 attested packages, and 29 compatible reservation groups.
- `python -B .tools/audit_event6_country_api.py`: 242 broad tags, 191 resolved carriers, zero missing, zero duplicates, and IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py`: 102 Event 006 tags and complete flag families for all 102.
- `python -B .tools/audit_event6_scenario_matrix.py`: all 32 SCN-008 cells and eight edge receipts passed.
- `python -B .tools/audit_event6_form16.py`: FORM-16 contract passed.
- `python -B .tools/audit_event6_gui_matrix.py`: Statehood Ledger semantic source matrix passed; no runtime GUI claim was made.

Changed files: only this handoff, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fij_country_package_revalidation_2026_08_31.md`.

Changed tags, state ids, leaders, parties, focus ids, decision ids, idea ids, localisation keys, formable ids, flags, portraits, AI values, central gates, Join order, assets, and map data: none.

Skipped meaningful validation: the installed Technology Tree Viewer is unavailable; the mandatory `chaosx_ai_probability_auditor` route is unavailable; event MCP analysis is partial at workspace scale; map MCP selected-state membership and geometry passed but global position diagnostics are not clean for unrelated files; no live HOI4 launch, save/load, runtime allocator, portrait visual promotion, or in-game ownership proof was attempted.

No simplification or unapproved fallback was made. Remaining blockers are the sourced 1936-valid FIJ leader/portrait admission, central content attestation and ordered Join promotion, complete named FIJ/PNG/WPG FORM-39 evidence, MFX identity/flag/rights review, and the unavailable auditor/technology evidence routes.

Parent action: retain IW-177 adapter-only and FORM-39 undiscoverable until the listed evidence is cleared in a separate promotion review; do not patch central attestation or Join from this handoff.
