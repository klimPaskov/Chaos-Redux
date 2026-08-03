# Event 016 Kruger State focus and AI audit handoff

Date: 2026-08-03

Scope: Kruger State national focus tree, route locks, focus rewards, icons, localisation, ideas, and Event 016 AI strategy plans.

This handoff records the read-only focus audit and the bounded AI-plan patch requested by the parent agent.

## High-priority fixes first

1. The four formation routes now have an AI continuation after the founding audit. Charter, rebellion, and enclave plans continue in place, while takeover uses the existing post-audit plan. The patch removes the premature audit abort from the first three plans and extends their ordered focus lists.

2. All 19 Event 016 AI strategy plans now have a vanilla-style `allowed = { brilliant_scientist_is_kruger_sovereign_country = yes }` guard. This matches the accepted architecture contract and prevents plan activation outside the Kruger State package.

3. The five focus IDs that were absent from every AI focus list are now referenced by appropriate plans: `KRG_clones_are_cohorts`, `KRG_human_machine_partnership`, `KRG_recall_the_defector_officers`, `KRG_laboratory_engineer_battalions`, and `KRG_evolution_four_sovereign_science`.

4. A live AI route sweep is still required for all four formation origins, the two clone and robotics law branches, disabled Evolution IV, and terminal commitment timing. The patch is statically safe but has not been consumer-tested in a live game.

## Changed files and identifiers

Changed gameplay file:

- `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`

Changed plan surfaces:

- `KRG_charter_republic_plan` now remains active after `KRG_complete_the_founding_audit` and orders economy, conventional security, human government, diplomacy, expansion, and Evolution IV continuation focuses.
- `KRG_rebellion_directorate_plan` now remains active after `KRG_complete_the_founding_audit` and orders economy, conventional security, Directorate, submission, expansion, and Evolution IV continuation focuses.
- `KRG_enclave_survival_plan` now remains active after `KRG_complete_the_founding_audit` and orders economy, conventional security, diplomacy, and laboratory-corridor expansion focuses.
- `KRG_takeover_post_audit_plan` now remains available after identity lock and includes conventional security, former-host settlement, expansion, and Evolution IV continuation focuses.
- `KRG_clone_sovereignty_plan` now references both `KRG_clones_are_citizens` and `KRG_clones_are_cohorts`.
- `KRG_machine_ascendancy_plan` now references both `KRG_human_machine_partnership` and `KRG_the_replacement_protocol`.
- `KRG_commonwealth_plan` and `KRG_submission_plan` now carry `KRG_evolution_four_sovereign_science` after the continental network.
- All remaining Event 016 plans received the same Kruger State `allowed` guard.

No national-focus source, reward, idea, localisation, interface, decision, or model files were changed.

## Route coverage table

| Route surface | Focus IDs | Audit result | Evidence |
| --- | --- | --- | --- |
| Formation and survival | 001-010 | Present. One audit opener, four origin openers, four recovery supports, and an all-four founding audit. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:36-289` |
| Government and population | 011-030 | Present. Human, clone, robotics, temporal, xenobiological, and synthesis identity lanes have project and identity gates. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:294-812` |
| Laboratory economy and supply | 031-040 | Present. Economy recovery, prototype works, four mutually exclusive supply doctrines, and sustainable capacity are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:817-1059` |
| Conventional security | 041-047 | Present. Conventional command, counterintelligence, air defense, and mutually exclusive staff/council solutions are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1064-1220` |
| Cloning | 048-053 | Present. Prototype, growth, identity, deployment, drift, and bounded replicated host route are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1225-1371` |
| Robotics | 054-059 | Present. Assembly, power, repair, command, rogue-node, and bounded machine route are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1376-1524` |
| Paleogenetics | 060-065 | Present. Restoration ledger, reserves, handlers, transport, escape, and dinosaur host route are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1529-1674` |
| Xenobiological synthesis | 066-071 | Present. Dossier, vats, control channel, containment, red-team, and engineered legion route are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1679-1829` |
| Portal operations | 072-076 | Present. Transit logs, terminal rings, depot link, breach closure, and strategic transit corps route are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1834-1957` |
| Temporal operations | 077-082 | Present. Ledger, anchor, synchronization, bounded warnings, stabilization, and continuity guard route are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1962-2113` |
| High energy, alien arms, and biological containment | 083-088 | Present. Reactor, delivery, interface, exotic guard, containment doctrine, and last-resort route are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:2118-2270` |
| Diplomacy and former host | 089-093 | Present. Foreign intelligence, former-host settlement, and commonwealth/submission mutex are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:2275-2386` |
| Expansion and integration | 094-097 | Present. Corridor, recovery, route-specific integration, and continental network are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:2391-2497` |
| Evolution IV and terminal commitments | 098-100 | Present. Evolution IV chronology gate and mutually exclusive Laboratory World/Singularity commitments are wired. | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:2502-2599` |

## Missing or simplified content

- No focus route is missing from the 100-focus tree, and every focus ID is now present in at least one Event 016 AI `ai_national_focuses` list.
- Seventeen focuses have no visible `prerequisite` block and enforce historical route gates only in `available`: `KRG_count_the_surviving_staff`, `KRG_secure_the_laboratory_heartland`, `KRG_repair_the_supply_spine`, `KRG_form_the_provisional_command`, `KRG_stabilize_the_laboratory_economy`, `KRG_restore_the_ordinary_chain_of_command`, `KRG_audit_the_growth_halls`, `KRG_wake_the_assembly_lines`, `KRG_open_the_restoration_ledger`, `KRG_open_the_designed_organism_dossier`, `KRG_recover_the_transit_logs`, `KRG_authenticate_the_temporal_ledger`, `KRG_build_an_independent_reactor_grid`, `KRG_make_containment_the_first_doctrine`, `KRG_a_state_without_friends`, and `KRG_secure_the_laboratory_corridors`.
- Additional architecture prerequisites are hidden in `available` for `KRG_authenticate_krugers_continuity`, `KRG_xenobiological_ascendancy`, `KRG_the_project_synthesis`, `KRG_recover_the_stolen_facilities`, `KRG_integrate_by_project`, and `KRG_evolution_four_sovereign_science`.
- These are runtime-safe historical/resource gates, but they are a player-facing route-clarity simplification because no connector or custom trigger tooltip exposes the historical prerequisite. The accepted architecture lists the intended visible prerequisites in `docs/plans/016_brilliant_scientist_plans/016_kruger_state_100_focus_architecture.md:96-100,123,126-127,258-270`.
- Identity capstones use the shared `brilliant_scientist_sovereign_identity_locked` trigger/effect gate instead of repeated pairwise `mutually_exclusive` blocks. This is runtime-safe and avoids duplicated mutex declarations, but static focus inspection will not display the pairwise identity mutexes.

## Icon coverage table

| Surface | Result | Evidence |
| --- | --- | --- |
| Focus source icon assignments | 100/100 unique `GFX_goal_KRG_*` IDs | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:36-2584` |
| Normal and shine sprite registrations | 100 normal plus 100 `_shine` goals | `interface/016_brilliant_scientist_kruger_state_focus.gfx` |
| Runtime DDS files | 100/100 paths exist with no duplicate texture paths | `gfx/interface/goals/016_brilliant_scientist/` |

## Localisation and reward mismatch list

- No focus title or description key is missing. All 100 focus IDs and all 100 `_desc` keys resolve in `localisation/english/016_brilliant_scientist_focus_l_english.yml`.
- All 100 `custom_effect_tooltip = KRG_*_effect_tt` keys resolve in the same localisation file.
- No title/description-to-reward mismatch was found in the static audit. Rewards are route-specific helper calls, unlock flags, lifecycle transitions, or bounded runtime rebuilds.
- No direct free equipment, manpower, factory, unit, missing-stage, debt-reset, synchronization-reset, arbitrary-core, or terminal-world-end reward was found in the focus file.
- The 163 focus unlock flags emitted by the tree all have at least one consumer outside the focus file.

## AI behavior gaps after patch

- `KRG_clones_are_citizens` appears before `KRG_clones_are_cohorts`, and `KRG_human_machine_partnership` appears before `KRG_the_replacement_protocol`. Because the two pairs are mutually exclusive, a live AI sweep should verify that focus-level weights still produce the intended law choice instead of always taking the first listed branch.
- Project plans enable after the matching deployment is operational. Opening project focuses therefore still depend on focus-level weights and live state before the specialized plan becomes active.
- No in-game AI simulation was run. The parent owns scenario balance, timing, war behavior, and terminal acceptance.
- `hoi4.focus_inspect` and `hoi4.focus_render` reported 14 global diagnostics for unrelated vanilla generic focuses and sprites. No KRG-specific layout, icon, or focus diagnostic was reported; the unrelated diagnostics were not patched.

## Validation run

- MCP inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da5cdaa5a1cd10fcb9e4f5ae83976059ce1ddadf7818d0e36caf9617739d409e/3800fd98d131f0d317e1a82baf86cc92779af5adf64a6a98c4874b1ac1357ea3/focus-inspect.308d914c1e5c7a4d.json`.
- MCP render artifacts: [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/509076cc5872dce5ce6587d3cd96a601e956aa65b90a272d40e145e00d236dbd/1cb80c0586ad1d850d8648d0a2f408f035f11ce95c1ac4f9b06cdbd512b6f8bb/brilliant_scientist_kruger_state_focus_tree.focus.html), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3940e09ebb5223b75ebc586a321aa5edc7bc8d4955d8f99332da13ca426dd532/442dce7c97c2a78c051082582f371396042d7e1af3a59dc5d0a343431bc19426/brilliant_scientist_kruger_state_focus_tree.focus.svg), and [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cdf8d27541333995c4f62696be80570485bcf74c61ad67e1f0f87952085cfbc9/4231acafb8282db17d6c635342ae38b0a0498216fd9350b0a17441165cddfcb3/brilliant_scientist_kruger_state_focus_tree.focus.json).
- MCP layout result: 100 focuses, 108 connectors, x=0..52, y=0..20, zero crossings, zero node intersections, zero long connectors, zero same-row spacing violations, and zero KRG-specific diagnostics.
- Python brace scan on `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt`: balanced depth 0.
- Static focus reference scan: 100 focus IDs, 99 in-file focus references, 0 undefined references.
- Static AI scan: 19 plans, 19 `allowed` blocks, 19 `ai_national_focuses` blocks, 0 undefined AI focus references, and 0 focus IDs missing from AI lists.
- Static consumer scan: 163 focus unlock flags, 0 consumerless/self-only flags.
- `git diff --check` on the changed AI file: clean.

Skipped meaningful validation:

- No second focus render was run after the AI-only patch because no focus source, layout, icon, or localisation file changed. The pre-patch MCP inspect/render artifacts remain valid for the tree itself.
- No Hearts of Iron IV process was launched, per repository rules.

## Remaining route risks

- The hidden historical prerequisites listed above remain a route-visibility concern and should be revisited only if the parent wants connector/tooltips changed within the focus-tree scope.
- The AI patch provides ordered continuation but does not prove real-time selection under disabled routes, failed missions, missing facilities, or terminal threats.
- The 14 unrelated global MCP diagnostics remain outside the Event 016 surface.

No model, asset, or fallback content was added. The AI patch is left uncommitted for parent review.
