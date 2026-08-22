# Event 19 derivative focus tree final audit and geometry follow-up

Date: 2026-08-22

Scope: Event 19 (Minor Repeatable) and the infantry_spawn_derivative_focus_tree national-focus source, its planning sidecar, and the directly required Event 19 localisation key. The audit stayed inside the Event 19 surface and preserved unrelated concurrent work.

## Outcome

The final tree has 45 focuses and 54 connectors: 30 shared focuses plus one five-focus overlay for each zombie, ghost, and golem package. The claimant route uses the shared claimant lane and claimant decisions. All family overlays remain conditional and isolated from parent tags, parent counts, parent stages, evolutions, super-events, and world-end progression. The tree uses decisions only and introduces no scripted GUI.

The geometry follow-up corrected the two named authored detours and the related central-lane crowding. The final MCP layout has zero connector crossings, zero node intersections, zero long connectors, zero too-close same-row pairs, and no linear-detour diagnostic. The remaining raw MCP layout warnings are two deliberate conditional-family anchor advisories; the raster evidence proves that their authored positions prevent overlap with adjacent family and shared lanes. They are adjudicated as non-defects below.

The gameplay follow-up adds infantry_spawn_derivative_resolve_opening_local_asset_shortfall = yes to infantry_spawn_derivative_inventory_the_seized_districts after its family-specific reserve and before the depot-unlock flag. Its completion tooltip now states that the opening local-asset shortfall is reconciled in addition to the depot decision, and that family hosts also receive the listed reserve. The helper implementation remains root-owned; the final MCP pass resolved its helper reference with no gameplay-reference warning.

No route was omitted or reduced. The decision-backed sequential expansion, submission, and integration lane is an adapted-equivalent implementation of the Event 19 route allowance: each focus advances a concrete decision flag consumed by the existing Event 19 decision system.

## Files changed

| File | Change |
| --- | --- |
| common/national_focus/019_infantry_spawn_derivative_focus.txt | Eleven narrow authored-coordinate corrections and one helper call in infantry_spawn_derivative_inventory_the_seized_districts; no focus IDs, prerequisites, mutual exclusions, route gates, AI weights, icons, or other rewards changed. |
| common/national_focus/019_infantry_spawn_derivative_focus.focus-plan.json | Synchronized the eleven preferredX values and source-bound SHA-256. |
| localisation/english/019_infrantry_spawn_l_english.yml | Updated infantry_spawn_derivative_inventory_the_seized_districts_tt to describe the local-asset reconciliation, depot unlock, and family-host reserve. |
| docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_focus_tree_audit_2026-08-22.md | Replaced stale audit evidence with the final source, gameplay, layout, and MCP handoff. |

No icon, idea, decision, scripted-helper, GUI, leader, or event file was edited by this audit. The helper called by the focus is intentionally owned by the parent agent.

## Changed focus IDs and route behavior

| Focus ID | Final authored coordinate | Narrow reason |
| --- | --- | --- |
| infantry_spawn_derivative_hold_the_first_ground | (0,0) | Centers the five-focus opening spine. |
| infantry_spawn_derivative_count_the_surviving_host | (0,1) | Keeps the opening census directly below its prerequisite. |
| infantry_spawn_derivative_inventory_the_seized_districts | (0,2) | Keeps the asset/depot inventory on the opening spine; adds the root-owned local-asset helper call. |
| infantry_spawn_derivative_restore_a_chain_of_orders | (0,3) | Removes the authored one-column opening offset. |
| infantry_spawn_derivative_name_the_future_host | (0,4) | Places the child directly under restore_a_chain_of_orders, removing the named linear detour. |
| infantry_spawn_derivative_outlast_the_former_state | (2,10) | Places the child directly below quiet_the_fragmented_columns, removing the named sustainment detour. |
| infantry_spawn_derivative_make_an_army_of_the_host | (-2,9) | Moves the shared convergence focus into the left method lane. |
| infantry_spawn_derivative_concentrate_the_host | (-4,10) | Separates the mutually exclusive method choices by two columns. |
| infantry_spawn_derivative_scatter_the_bands | (-2,10) | Separates the mutually exclusive method choices without colliding with the central method. |
| infantry_spawn_derivative_arm_the_captured_auxiliaries | (0,10) | Leaves the central method lane clear for the shared sequence. |
| infantry_spawn_derivative_zombie_scavenge_the_abandoned_barracks | (-8,5) | Preserves a distinct zombie-family lane beside the shared opening. |

The source SHA-256 is e4df35d68962bbc5bd993b96563f7c1a90fb9e2c199608f33bf0b278dbdd01d0. The sidecar SHA-256 is 702fba1f7d3adfd9dd7c1e0b259ebe7640933938e5acea06170245a53a9d7efc, and its sourceHash matches the source hash above.

The gameplay change is at common/national_focus/019_infantry_spawn_derivative_focus.txt:87-93: the three family reserve branches run first, then infantry_spawn_derivative_resolve_opening_local_asset_shortfall = yes, then infantry_spawn_derivative_depot_operations_unlocked is set. The corresponding tooltip is infantry_spawn_derivative_inventory_the_seized_districts_tt in localisation/english/019_infrantry_spawn_l_english.yml.

## Route coverage

| Route segment | Focus coverage | Review result |
| --- | --- | --- |
| Event-created opening and survival | hold_the_first_ground, count_the_surviving_host, inventory_the_seized_districts, restore_a_chain_of_orders, name_the_future_host (5) | Present and sequential. Package activation and derivative-country gating remain intact. |
| Hierarchy selection | crown_the_claimant, convene_the_host_council, obey_the_family_instinct (3) | Present and mutually exclusive. Claimant availability uses the claimant trigger; council and family roots exclude claimant breakaway. |
| Hierarchy support | assign_command_estates, one_voice_over_the_host, bind_the_district_councils, no_host_abandoned, mark_the_family_domain, end_the_old_chain_of_rule (6) | Present. Child prerequisites remain branch-local and do not touch parent progression. |
| Sustainment and method choice | mark_the_muster_depots, reopen_captured_workshops, open_the_living_corridor, count_every_obligation, quiet_the_fragmented_columns, outlast_the_former_state, make_an_army_of_the_host, concentrate_the_host, scatter_the_bands, arm_the_captured_auxiliaries (10) | Present. The three method focuses remain mutually exclusive; the convergence focus and the former-state pressure sequence retain their existing prerequisites. |
| Former-parent pressure and regional ambition | a_method_fit_for_the_host, read_the_neighboring_frontiers, issue_the_submission_terms, absorb_the_conquered_districts, turn_the_host_outward, become_the_regional_predator (6) | Present and sequential. Existing controlled-territory, former-parent, victory, and family-completion gates remain unchanged. |
| Zombie overlay | zombie_scavenge_the_abandoned_barracks, zombie_number_the_devouring_bands, zombie_teach_the_base_dead_to_muster, zombie_keep_the_hunger_in_column, zombie_a_realm_of_base_dead (5) | Present behind zombie allow_branch and availability checks; no parent or world-end route. |
| Ghost overlay | ghost_mark_the_first_anchors, ghost_call_a_second_procession, ghost_bind_the_procession_to_place, ghost_thin_the_hunger_for_life, ghost_a_pale_dominion (5) | Present behind ghost allow_branch and availability checks; no parent or world-end route. |
| Golem overlay | golem_recover_the_broken_coal, golem_reconstruct_the_binding_marks, golem_turn_workshops_into_foundries, golem_share_the_living_pattern, golem_a_march_of_living_stone (5) | Present behind golem allow_branch and availability checks; no parent or world-end route. |

The route map is therefore 45 focuses total. Each nonhuman derivative package sees the 30 shared focuses plus its own five-focus overlay. The claimant package intentionally has no nonhuman overlay and remains on the claimant decision route.

## Provider-family and identity compatibility

- Shared focuses require the Event 19 derivative package to be active; family overlays require their own zombie, ghost, or golem provider-family trigger and allow_branch. The claimant route remains separate and does not receive a nonhuman family overlay.
- The inventory focus's family reserve branches run only for zombie, ghost, and golem hosts. Claimant derivatives still complete the focus and receive the opening local-asset reconciliation, depot decision unlock, and no family-only reserve.
- The focus source contains no leader creation, female leader, portrait focal figure, tag change, country identity change, or scripted GUI. Focus icons resolve to army-scene art, satisfying the Event 19 army-art requirement.
- No parent progression, family count, evolution, super-event, or world-end cleanup is reachable from this tree. The parent-owned local-asset helper is the only cross-file opening integration call and is now resolved by the final MCP reference scan.

## Adapted-equivalent decision-backed expansion proof

The sequential shared lane is not a disconnected generic reward chain. Its focus rewards set existing Event 19 decision flags consumed by common/decisions/019_infantry_spawn_derivative_decisions.txt and its scripted triggers:

| Focus/reward flag | Decision integration evidence |
| --- | --- |
| infantry_spawn_derivative_depot_operations_unlocked | Depot decisions and sustainment-site choices consume the opening depot flag. |
| infantry_spawn_derivative_fragmentation_operations_unlocked | Fragmentation operations consume the flag set by quiet_the_fragmented_columns. |
| infantry_spawn_derivative_command_net_operations_unlocked | Command-net operations consume the flag set by outlast_the_former_state. |
| infantry_spawn_derivative_frontier_intelligence_complete | Frontier-intelligence completion gates the former-parent pressure route. |
| infantry_spawn_derivative_submission_operations_unlocked | Submission decisions consume the flag set by issue_the_submission_terms. |
| infantry_spawn_derivative_integration_operations_unlocked | Integration decisions consume the flag set by absorb_the_conquered_districts. |
| infantry_spawn_derivative_outward_campaign_ready | Outward-campaign decisions consume the flag set by turn_the_host_outward. |
| infantry_spawn_derivative_regional_predator_ambition | Regional ambition logic consumes the terminal become_the_regional_predator flag. |

The source sets these flags at the existing focus rewards (019_infantry_spawn_derivative_focus.txt:410,428,552,571,589,608,635,683,726), while decision consumers are present in 019_infantry_spawn_derivative_decisions.txt around the depot, family, fragmentation, command-net, submission, and integration blocks. This satisfies the focus-tree skill's adapted-equivalent allowance without inventing a second visible route family. Event 19 remains decisions-only and has no scripted GUI.

## Missing, reduced, or blocked content

- No Event 19 route is missing from the source route map.
- No route was reduced to a parent-tag, parent-count, parent-stage, evolution, super-event, or world-end shortcut.
- The sequential decision-backed expansion and submission/integration path is documented above as an adapted-equivalent route, not as omitted content.
- The claimant package has no zombie, ghost, or golem overlay because its family ID is none; this is the intended claimant isolation rule.
- The helper implementation infantry_spawn_derivative_resolve_opening_local_asset_shortfall is parent-owned and was not created in this bounded focus patch. The final MCP pass verified the helper reference; no Event 19 gameplay-reference blocker remains in this tree audit.

## Icon coverage

| Surface | Coverage | Evidence |
| --- | --- | --- |
| Focus icon references | 45/45 focus blocks resolve to unique Event 19 icon IDs. | 019_infantry_spawn_derivative_focus.txt and interface/019_infantry_spawn.gfx. |
| Base and shine sprites | 45/45 base sprites and 45/45 shine sprites resolve. | interface/019_infantry_spawn.gfx. |
| DDS payloads | 45/45 DDS payloads exist with valid headers and 100x88 dimensions. | gfx/interface/goals/019_infantry_spawn/. |
| Art subject constraint | Existing references depict army scenes rather than human portrait focal figures. | Source/icon audit. |

No icon ID or asset file changed.

## Localisation and reward review

All 45 focus title, description, and completion-tooltip keys resolve in the Event 19 English localisation file. All 45 custom_effect_tooltip reward keys resolve. The only changed key is infantry_spawn_derivative_inventory_the_seized_districts_tt, which now says that the opening local-asset shortfall is reconciled, the Secure a Muster Depot decision is unlocked, and family hosts also receive the listed family-specific reserve. No reward key or focus ID was renamed.

The two existing focuses that converge on infantry_spawn_derivative_depot_operations_unlocked remain intentional: inventory_the_seized_districts performs opening local-asset reconciliation and reserve setup, while mark_the_muster_depots supplies the later political-power reward. This is a deliberate convergent decision unlock, not a missing reward.

## AI behavior and probability evidence

All 45 focuses retain non-zero ai_will_do blocks using the existing Event 19 AI constants. Availability, route locks, mutual exclusions, and package/family checks remain present for shared, hierarchy, method, and family focuses. No AI weight or probability-bearing value changed in this follow-up.

The earlier hoi4.probability_inspect/hoi4.probability_evaluate run found 45 candidates but returned a partial empty-state evaluation because package flags, prerequisites, route variables, and ordered strategy plans require runtime state. No probability_compare was required because neither geometry nor the new deterministic helper call changes AI weights. A complete runtime scenario should still include an active derivative package, each hierarchy/family route, former-parent pressure, and all prerequisite state before ranking focus AI.

## MCP evidence and post-change comparison

Workspace: mod_chaos_redux_ea3b2d67c2c0.

The MCP calls emitted the informational MCP_INLINE_FILES_TRUNCATED notice because inline inventory is capped at 64 paths (66-68 paths scanned); the linked inspect/render/raster artifacts are complete and validation passed. This inventory presentation limit did not block Event 19 source or layout validation.

The previous post-geometry layout hash was 573e53a1a7141fb44dd5ae5b0a99b27506b56e2a4d71459378a3b43ca365bf20 with two linear-detour warnings, four sibling-anchor advisories, and one broad sibling asymmetry. The final layout hash is a4f1cc968841c3a13f5912d9874447863f548f2b5b9ee92d45527927a1c639b9: the two detours and broad asymmetry are gone.

Final hoi4.focus_inspect (after the gameplay call, parent helper landing, and sidecar hash refresh): hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/571618444917d2d405c2717f0974b7d3fc4587a9121ac883e17cbda4e6656e85/6c7dbb85e27cc69364a07200e6ddd4e31d30e5d6159d145ee15d5bc64ff28e02/focus-inspect.800be5028ac05f77.json

Inspect metrics: 45 focuses, 54 connectors, zero crossings, zero node intersections, zero long connectors, zero too-close same-row pairs, maximum same-row spacing requirement 2, sibling cohort count 5, asymmetric sibling cohort count 0, off-anchor sibling cohort count 2, total sibling-anchor deviation 24, and maximum sibling-anchor deviation 16.

Final hoi4.focus_render artifacts:
- HTML: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a0a1bd6f11940b6fc2de150042a58cb3479e0c210584fb7b14d665c30a842bd/24e121511664079ec54577027450682eafcbf8e177b9426efceb20ab363a7d59/infantry_spawn_derivative_focus_tree.focus.html
- SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b64fd33c58389b3f801f87330c3615fe62675bb6ecc6c41167c3974f7c81afff/0158f23249c1fe9be06d66a395c5dc5b7e09b4fda21d5eb6b64e6e1c7772efe7/infantry_spawn_derivative_focus_tree.focus.svg
- JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d003a4e592652d089fd2172a3a71bc88d2f13e10cf20a76078b34e5bc1fcb5f9/505a548c8328e28d46cffada3b1050fd84b768a17ae2c8a5013a0db87dd95fe0/infantry_spawn_derivative_focus_tree.focus.json
- Source map: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2d091177a8cdac908ee6b925d6e1bbff90878ec9a3fd7d8b6fb51316dfc8a18/067350ed047077ac96abee031dee54aae490f72af7d4a835a14c0d87b9ee07b8/infantry_spawn_derivative_focus_tree.focus.source-map.json
- Sidecar artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b7a5be7868e0213b0ef7a8db674b59fc55d5fe9305effb33cb02ebd4e50bbb7/09a6550cf359779c8a00ccc50dec112abeb7296583d72c2dfd6c5bbbb8508c91/infantry_spawn_derivative_focus_tree.focus.plan.json

Structural render hashes: HTML 2a0a1bd6f11940b6fc2de150042a58cb3479e0c210584fb7b14d665c30a842bd, SVG b64fd33c58389b3f801f87330c3615fe62675bb6ecc6c41167c3974f7c81afff, JSON d003a4e592652d089fd2172a3a71bc88d2f13e10cf20a76078b34e5bc1fcb5f9.

Final 0.5 hoi4.focus_raster artifacts:
- PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bf349ea775f81a7f2953635124420807db048c272368f250d95f58b54e79ed02/03a566e586ca157dcec594f7e424c34a20afaa2b6d009bf00c46267814759c55/infantry_spawn_derivative_focus_tree.focus.png
- SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00dfd79f907188fb56d92972c6f3ad62e1132fb43755862f6776da7ed89242de/d0bd8422c17cfe73dbe2446d6819d900214c489d765a7db0ac1f1d0c3c4c83ce/infantry_spawn_derivative_focus_tree.focus.svg
- Raster JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d003a4e592652d089fd2172a3a71bc88d2f13e10cf20a76078b34e5bc1fcb5f9/b3f81e2931053d63d79b28b134e99cfbd1a4e3c6b17e1049d0f7df7e35f89938/infantry_spawn_derivative_focus_tree.focus.json

Final 0.25 review raster:
- PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ce412dbe36f924abc4b6841c204acfc74768bff464801c5f9e7e6def03ae801/b2c9be6d79cf7fa1e4ae6599fa7876a591adfd60a0862492c3a0a7dd7488f1e1/infantry_spawn_derivative_focus_tree.focus.png
- SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f276bf99e891e89e71c7c22434583a9f990a0a737d3000927e3ecc0f5b3e806a/348b4b3d4e14b577ba4e9b7d7848fcf36c8c78cca85c31b0b52c34cf082eb85d/infantry_spawn_derivative_focus_tree.focus.svg
- Raster JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d003a4e592652d089fd2172a3a71bc88d2f13e10cf20a76078b34e5bc1fcb5f9/474486abec65e0a44bacabc3077a9d3e99ddc4c6d9f0704d8e54dcf0b3e805f2/infantry_spawn_derivative_focus_tree.focus.json

The raster is 528x271; visual inspection shows the centered opening spine, separated method lanes, and distinct zombie/ghost/golem lanes with no apparent overlap or connector crossing.

### Adjudication of raw sibling-anchor advisories

- Ghost opener: ghost_mark_the_first_anchors is authored at (8,5) and its three sibling choices are (10,6), (12,6), and (14,6). Centering those choices around the opener would produce (6,6), (8,6), and (10,6), which would overlap the golem family lane at (4,6), (6,6), and (8,6). The MCP heuristic reports [8,10,12], anchor 6, deviation 16; the exact authored source/sidecar coordinates and raster are the controlling evidence.
- Golem opener: golem_recover_the_broken_coal is authored at (4,5) and its three sibling choices are (4,6), (6,6), and (8,6). Centering those choices around the opener would produce (2,6), (4,6), and (6,6), colliding with the shared depot route at (2,6). The MCP heuristic reports [2,4,6], anchor 2, deviation 8; the exact authored source/sidecar coordinates and raster are the controlling evidence.

These two warnings describe conditional family spacing rather than an overlap or route defect. The final metrics independently report zero intersections, crossings, long connectors, and broad sibling asymmetry. No focus_rewrite was needed: the sidecar-aware authored-coordinate workflow was rerun through inspect, render, and raster after the final source/hash update, and it preserves the intended visual geometry.

## Validation and skipped validation

- Source checks found 45 focus blocks, 45 unique IDs, zero duplicate authored coordinates, zero duplicate sidecar preferred coordinates, and a matching source hash between the focus file and sidecar.
- The Event 19 isolation scan found no direct focus-tree references to scripted GUI, world-end, evolution, super-event, parent tags/counts/stages, or focus-tree reload logic.
- Localisation checks found all Event 19 focus title, description, completion-tooltip, and reward keys, including the updated inventory tooltip.
- Icon checks found 45/45 focus references, base sprites, shine sprites, and DDS payloads.
- Final hoi4.focus_inspect, hoi4.focus_render, and hoi4.focus_raster all returned status: ok and validation.passed: true with no blocking diagnostics.
- The installed focus MCP does not expose a separate focus-lint command; inspect supplied the available source/reference/layout validation.
- No live HOI4 run was performed, per repository policy.
- No probability comparison was run because AI weights and probability-bearing values did not change.
- No hoi4.focus_rewrite was used because the requested edits were narrow source/sidecar geometry and one deterministic reward helper call; direct source plus sidecar-aware post-render evidence is retained.

## Remaining risks and parent actions

1. Retain the parent-owned infantry_spawn_derivative_resolve_opening_local_asset_shortfall implementation and its separate package-effect validation. The final focus inspect found no gameplay-reference warning for the call at source line 92.
2. Retain the two sibling-anchor warnings as documented non-defects unless a future full-tree lane redesign changes the shared/dependent family lanes. Centering either family cohort would create a real overlap, as proven above.
3. Keep the unrelated vanilla continuous_restrict_freedom_desc localisation warning outside Event 19 scope.
4. Retain the convergent Secure a Muster Depot decision tooltip as an intentional opening/later sustainment convergence; no reward mismatch remains.

No missing route, fallback tree, placeholder icon, missing Event 19 localisation, absent AI block, or unapproved content reduction remains in this bounded focus audit. The only raw diagnostics left are the two adjudicated family-lane sibling advisories and the unrelated vanilla continuous-focus localisation warning.

Handoff path: docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_focus_tree_audit_2026-08-22.md.
