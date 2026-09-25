# Event 006 REG-03 TRA/BOS/MAC Focus-Tree Audit

**Audit date:** 2026-09-26. The requested 2026-09-25 filename is retained.

**Disposition:** Source coverage for the accepted three five-focus groups is present. Imported-group layout evidence remains blocked by the focus MCP's omission of root-level shared_focus imports, and route-aware AI evidence remains unresolved.

**Scope:** Read-only review of the eight files named in the request. No gameplay or localisation source was changed. The only file written by this audit is this handoff.

## Severity-ranked findings

### P1 — Imported shared-focus attachment and layout remain unverified

The source contains all 15 root-level shared_focus definitions and imports all 15 into the Event 006 full tree; the Austro-Hungarian carrier imports the ten TRA/BOS nodes and omits MAC as specified. There are no direct-focus duplicates used as a fallback. However, fresh focus inspect/render only expose direct focus nodes, so they do not prove that any of these imported groups attach, route, render their icons, or avoid overlap in either carrier. This is the user-approved MCP limitation, not a source-count failure. See 006_independence_wave_focus.txt:53-76,4291-4688 and austro_hungarian_releasable_shared.txt:29-48.

The fresh Event 006 inspect returned 184 direct nodes and layout hash a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7; its direct graph has 196 connectors, zero crossings, zero node intersections, and one long connector. The fresh carrier inspect returned 56 direct nodes and layout hash 8e1c44e617e03adc234cb622e850552e6b313e775be0cd3452761fa1f52f98bf; its direct graph has 62 connectors, one crossing, one node intersection, and 13 existing carrier diagnostics. These agree with the parent evidence at source revision ac4caa08ac559d2420c9fc4384b3c56d692b2846cadd970f8b11908a9a3985cc.

### P1 — Route-aware focus AI is absent; probability evidence is pending

None of the 15 REG-03 shared focuses has an explicit ai_will_do block, so the engine's default focus score is 1 before external strategy factors. The accepted documentation describes state-aware route intent, but the reviewed focus definitions do not encode it. No route ranking or probability can be claimed from this audit.

The six existing companion-payment decisions do have AI weights: the three administrative actions use the high base, while the three security actions add the war modifier. Their identifiers are `independence_wave_tra_convene_multiethnic_assembly` and `independence_wave_tra_screen_defecting_regulars` (006_independence_wave_balkan_decisions.txt:1545-1599); `independence_wave_bos_convene_cantonal_council` and `independence_wave_bos_screen_defecting_garrisons` (:311-365); and `independence_wave_mac_convene_community_council` and `independence_wave_mac_screen_veteran_networks` (:803-857). The required read-only chaosx_ai_probability_auditor was spawned as agent 01a0da52-a519-7b70-b264-77f8b5f9db64, but it had not returned scenario evidence when this handoff was finalized at the user's request. Therefore, no probability_inspect/evaluate/sweep result is claimed for those decision weights. The accepted addendum records an incomplete candidate pool and missing typed campaign inputs for the imported groups; this audit leaves the same route-ordering question unresolved rather than substituting source-only analysis.

The 15 focus definitions without explicit `ai_will_do` are `independence_wave_tra_register_district_authorities`, `independence_wave_tra_account_for_rails_and_mines`, `independence_wave_tra_seat_the_district_assembly`, `independence_wave_tra_mandate_the_frontier_guard`, `independence_wave_tra_publish_border_arbitration_docket`; `independence_wave_bos_convene_sarajevo_service_board`, `independence_wave_bos_map_drina_passes_and_depots`, `independence_wave_bos_bind_cantonal_guarantees`, `independence_wave_bos_commission_mountain_veterans`, `independence_wave_bos_publish_drina_corridor_docket`; and `independence_wave_mac_register_vardar_municipal_offices`, `independence_wave_mac_survey_vardar_rail_and_grain`, `independence_wave_mac_ratify_village_appeals`, `independence_wave_mac_screen_mountain_veterans`, `independence_wave_mac_publish_vardar_arbitration_docket` (006_independence_wave_focus.txt:4291-4688).

### P2 — Sprite registration and texture files were outside the authorized source list

All 15 focus definitions carry the intended sprite ID for their role, and the event document maps those five IDs to existing definitions and textures. The .gfx registry and DDS files are outside the requested review scope, and the MCP renderer omits the imported groups, so sprite registration, decoded artwork, and in-carrier icon rendering were not independently verified. No missing icon field was found in the focus source.

### P3 — Existing direct-tree layout/lint warnings are unrelated to the REG-03 imports

The full-tree MCP inspect reports one long connector from independence_wave_adopt_military_archetype_program to independence_wave_adopt_reclamation_doctrine, spanning 10 columns; its source is 006_independence_wave_focus.txt:772-790. The carrier inspect reports existing repeated generic rewards and linear detours in the older ah_* focuses, plus existing naval connector crossing and node-intersection diagnostics around ah_flexible_navy, ah_large_navy, ah_cruiser_effort, ah_submarine_effort, and ah_NAV_effort at austro_hungarian_releasable_shared.txt:52-75,139-165,167-326,939-1013,1193-1587. These are direct carrier content warnings; imported REG-03 nodes are absent from the inspector's graph, so none can be attributed to the new groups. The inspect also reports the unrelated game-file warning for continuous_restrict_freedom_desc in game:common/continuous_focus/generic.txt.

## Route coverage

| Package | Required group and route | Full-tree imports | Austro-Hungarian carrier imports | Gate and coverage |
| --- | --- | --- | --- | --- |
| IW-023 TRA | register district authorities → account for rails and mines → seat the district assembly XOR mandate the frontier guard → publish border arbitration docket | All five | All five | Root accepts either full-tree capital administration or overlay take-stock; exact TRA package and generic-focus contract; state 84 must be owned, controlled, and capital. Source: 006_independence_wave_focus.txt:4291-4421. |
| IW-029 BOS | convene Sarajevo service board → map Drina passes and depots → bind cantonal guarantees XOR commission mountain veterans → publish Drina corridor docket | All five | All five | Root accepts either full-tree capital administration or overlay take-stock; exact BOS package and generic-focus contract; state 104 must be owned, controlled, and capital. Source: 006_independence_wave_focus.txt:4424-4554. |
| IW-026 MAC | register Vardar municipal offices → survey Vardar rail and grain → ratify village appeals XOR screen mountain veterans → publish Vardar arbitration docket | All five | None; full-framework-only is the accepted design | Full-tree capital-administration prerequisite; exact MAC package and full-framework visibility gate; generic-focus contract and state 106 owned, controlled, and capital. Source: 006_independence_wave_focus.txt:4557-4688. |

The 15 full-tree imports are at 006_independence_wave_focus.txt:62-76. The ten TRA/BOS carrier imports are at austro_hungarian_releasable_shared.txt:34-43. All three roots and all three dockets put multiple focus entries in one prerequisite block, which is the native OR form; each route therefore needs only one alternative opener and one alternative branch respectively. The TRA, BOS, and MAC branch choices name one another reciprocally in mutually_exclusive blocks. No AND/OR inversion or broken mutual exclusion was found. The inspected offline National focus modding page documents the single-block OR rule, reciprocal mutual-exclusion behavior, shared-focus imports, and the default focus score.

## Costs, timing, paid dockets, and companion lifecycle

Each selected route is four completed focuses: short 5 + short 5 + standard 7 + standard 7, totaling 24 focus-cost units or 168 days at normal speed. The file constants are 5 and 7 at 006_independence_wave_focus.txt:8-9; the group assignments are in the route ranges above. The accepted event document and addendum identify the current TRA/BOS/MAC founding crises as 420 days, and the decision file retains their existing founding_crisis timer references at 253, 752, and 1494. These local groups do not complete the crisis or replace a paid project.

Each docket requires its package's relevant paid-project receipts in a single OR condition inside custom_override_tooltip. Its tooltip and not_tooltip use distinct recorded-versus-required keys for each package: TRA at 006_independence_wave_focus.txt:4404-4413, BOS at 4537-4546, and MAC at 4670-4679. The focus completion rewards only change the package's two settlement ledgers.

Each package uses the same accepted local tradeoff shape with its own ledgers: opening +5 to the first ledger, logistics +5 to the second, one chosen branch +10 to its favored ledger and -5 to the other, and docket +5 to both. The selected branch's paid companion adds +5 to its favored ledger once. The focus source uses the existing minor_gain, standard_gain, and minor_loss constants; the event document and accepted addendum define those as +5, +10, and -5. Exact constant definitions were outside the authorized source list, so the underlying numeric definitions were not independently opened during this audit.

Every base and companion reward calls the existing package ledger helper. TRA clamps both settlement values and refreshes its lifecycle at 006_independence_wave_balkan_package_effects.txt:2760-2777; BOS clamps both ledgers at 503-520; MAC clamps both ledgers at 1424-1441. The six companion helpers each require the exact package, paid receipt, matching completed branch focus, and an unset awarded marker, then assign both deltas before invoking the clamp helper: 2785-2843. Focus-first completion uses the same paid-receipt and one-time-marker conditions in 006_independence_wave_focus.txt:4346-4390,4480-4523,4612-4656.

The six markers are TRA district-assembly/frontier-guard, BOS cantonal-guarantees/mountain-veterans, and MAC village-appeals/mountain-veterans. The paid-decision callbacks set the receipt before invoking the matching helper from the success remove_effect blocks at 006_independence_wave_balkan_decisions.txt:311-365,803-857,1545-1599. Package cleanup does not clear these six awarded markers; the full-framework assignment clears them alongside the focus-history reset immediately before load_focus_tree keep_completed = no at 006_independence_wave_focus_effects.txt:55-69. No duplicate companion route or marker clear was found in the reviewed files.

Read-only git diff against HEAD shows the existing paid decisions received only the new success callbacks in remove_effect. Their cost predicates and labels, payment complete_effects, standard days_remove timers, cancel_trigger conditions, and cancel_effect failure handling are unchanged. The offline Decision modding page confirms that a true cancel_trigger ends a timed decision without running remove_effect, while cancel_effect handles cancellation; accordingly, cancellation does not grant a companion bonus.

## Icon coverage

| Focus role | TRA/BOS/MAC IDs | Sprite ID | Source-level result |
| --- | --- | --- | --- |
| Local administration opener | tra_register_district_authorities / bos_convene_sarajevo_service_board / mac_register_vardar_municipal_offices | GFX_goal_independence_wave_founding_administration | 3/3 assigned |
| Transport and logistics step | tra_account_for_rails_and_mines / bos_map_drina_passes_and_depots / mac_survey_vardar_rail_and_grain | GFX_goal_independence_wave_infrastructure_authority | 3/3 assigned |
| Civilian branch | tra_seat_the_district_assembly / bos_bind_cantonal_guarantees / mac_ratify_village_appeals | GFX_goal_independence_wave_popular_councils | 3/3 assigned |
| Frontier branch | tra_mandate_the_frontier_guard / bos_commission_mountain_veterans / mac_screen_mountain_veterans | GFX_goal_independence_wave_army_integration | 3/3 assigned |
| Docket capstone | tra_publish_border_arbitration_docket / bos_publish_drina_corridor_docket / mac_publish_vardar_arbitration_docket | GFX_goal_independence_wave_former_host_settlement | 3/3 assigned |

The focus source has 15/15 icon fields and five role-based sprite IDs; reuse across the three regions is consistent with the accepted shared-group pattern. The event document lists the corresponding existing sprite definitions and DDS paths at reg03_danube_focus_groups.md:25-37. Because the MCP omits imported nodes and the .gfx/texture files were outside scope, visual or registry validation is not claimed.

## Localisation and reward mismatch list

The group requires 57 keys: 15 title/description/reward-tooltip triplets (45), six paid-companion bonus tooltips, and six docket paid-requirement/paid-recorded messages. All 57 are present exactly once in 006_independence_wave_focus_l_english.yml:447-505. The source-level key comparison found no missing group keys or duplicates. One additional TRA-prefixed tooltip key in the same range belongs to the pre-existing shared overlay and is not part of this group.

No title, description, or reward mismatch was found. The administrative and transport names/descriptions align with their ledger deltas; each civilian or frontier title matches the ledger it improves and the opposing ledger loss; each docket describes the two-ledger reward and its paid gate. The conditional companion tooltips are shown only when the matching paid receipt exists and its marker is unset. The two docket tooltip states are distinct per package.

## Missing or simplified content

No route, focus, import, branch, paid docket alternative, companion callback, or localization key required by the accepted three-group design is missing from the reviewed source.

The intentionally bounded implementation is a package-specific institutional and settlement-ledger bridge, not a complete political or expansion route family. It does not itself unlock a new decision family, resolve a mission, grant claims or cores, transfer states, admit countries, settle a former host, or open a league/network. The accepted event document explicitly keeps those outcomes in their existing paid projects and framework routes at reg03_danube_focus_groups.md:19-23. This is consistent with the accepted scope and is not reported as an unapproved fallback.

## MCP evidence and remaining limits

Fresh focus_inspect and focus_render both returned successfully for both named files at workspace mod_chaos_redux_ea3b2d67c2c0. The inspect artifact revision was 049f5ba2036fe28df0a2899c2b9065b6e8b4636a6f399c24e0f4c8bd789d569c; the full-tree and carrier layout hashes match the parent-reported hashes. These inspect/render artifacts show only direct focus nodes; they cannot establish visual validation of the 15 imported groups.

- [Fresh Event 006 inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdd7ec1fe03196313a45048bca1ba720a14998bdfa6498e216c3bb75261209ab/0bb457f1a0e60ca316e6fbaf6edf6e69549a5d74cde7f8fa9c27b65d1a37cc67/focus-inspect.049f5ba2036fe28d.json)
- [Fresh Event 006 rendered tree](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e6262aa14491369c6a08adbe9c6679f01651774b5392b7034ca3909b8baec64/335b62f111bf4f27c5df9982d6fdae8c05915137678d538d7761ee4ccee91bb5/independence_wave_focus_tree.focus.html)
- [Fresh Austro-Hungarian carrier inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9afe87a98ff4a21d428a6f9dad55696917a3a373701f0ecc6061ea99076f6c06/20992ede0b38b5b92a58a056360d659e39b44c3a28c0c7e7cc5e1a1364b57497/focus-inspect.049f5ba2036fe28d.json)
- [Fresh Austro-Hungarian carrier rendered tree](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a4366ee5ac031b06f89d2c347b5a90f7f244adeb236d7e1c884905ca2595f87/7eb43c68ce420773b73b35fbde9b20874ca72c46dc45b3a8424d8c4e5c98ddda/austro_hungarian_releasable_focus.focus.html)

Meaningful validation was limited to read-only focus inspect/render, source-level import/gate/prerequisite/reward/marker checks, a 57-key localisation comparison, and a read-only git diff for the six paid actions. No game or tests were run, as requested. The icon registry and texture files were not reviewed because they were outside the allowed files; the imported-group visual check is blocked by the MCP omission; exact script-constant values were not reopened because their definitions are outside scope; and the weighted auditor had not returned its required scenario evidence at cutoff.

## Files and skills

**Changed by this audit:** docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_reg03_focus_tree_audit_2026-09-25.md only. No focus IDs, source effects, decision costs, cancellation rules, or localisation keys were changed.

**Skills used:** chaos-redux-focus-trees, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-event-assets, chaos-redux-improvement-loop, and chaos-redux-subagents. No skills were created or updated.
