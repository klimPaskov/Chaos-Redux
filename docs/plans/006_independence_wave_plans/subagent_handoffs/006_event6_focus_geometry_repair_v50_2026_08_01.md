# Event 006 focus geometry repair v50

Date: 2026-08-01.

Scope: bounded geometry audit of `common/national_focus/006_independence_wave_focus.txt` for `independence_wave_focus_tree`.

## Disposition

No gameplay or focus-source patch was applied. The source file remains unchanged because every unsatisfied crossing diagnostic reports fixed or relative endpoints and the conflicts are distributed across the shared trunk, convergence capstones, and package overlays. A one-node coordinate edit cannot be proven safe without moving a larger route family, and `hoi4.focus_rewrite` compact mode would be a whole-tree reflow outside this bounded task.

No focus id, prerequisite, mutual exclusion, reward, cost, icon id, localisation key, AI block, country overlay, route lock, or coordinate was changed by this handoff.

## Route coverage table

The accepted architecture spec (`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md`) defines seven interacting lane families. The source file contains each lane and the package/shared roots below; this geometry audit found no missing gameplay branch.

| Spec lane or surface | Source anchors | Coverage result |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` (source lines 76-293) | Present; founding trunk and capstone are connected. |
| Government and internal power | Government settlement block (lines 831-1286) plus `independence_wave_map_internal_power_centers` and power-center route focuses | Present; package-aware government routes and optional power struggle are represented. |
| Economy, infrastructure, and administration | Lines 294-414, including `independence_wave_establish_emergency_revenue`, `independence_wave_secure_food_and_fuel`, and `independence_wave_build_regional_transport_authority` | Present; geometry is crossed around the shared trunk but rewards and prerequisites were not changed. |
| Army, security, and military identity | Lines 415-684, including `independence_wave_form_border_guard`, `independence_wave_adopt_military_archetype_program`, and `independence_wave_found_professional_defense_institution` | Present; convergence is visually congested but route semantics are intact. |
| Diplomacy, recognition, and patrons | Lines 685-830, including `independence_wave_focus_build_permanent_foreign_service`, `independence_wave_send_first_missions`, and `independence_wave_secure_durable_sovereignty` | Present; crossovers with the army and treasury lanes remain. |
| Former host, borders, and expansion | Lines 1287-1541, including `independence_wave_define_former_host_policy`, `independence_wave_survey_regional_ambition`, and `independence_wave_sponsor_further_ruptures` | Present; the long founding-to-survey connector passes through unrelated nodes. |
| Network, league, formables, and high-chaos ambitions | Lines 1542-1982, including league proposals, formable preparation, and the hidden high-chaos lane | Present; proposal and capstone branches are connected. |
| Package ambition overlays | Lines 1983-3138 for IW-001, IW-002, IW-010, IW-004, IW-006, IW-007, IW-008, IW-009, IW-018, and IW-019, plus explicit shared imports at lines 40-74 | Present; package-specific branches are loaded without changing the shared route contract. |
| Shared overlay and carrier consumers | Lines 3159-3516, including IW-012 and IW-017 consumers | Present; additive overlay remains separate from the full framework. |

## MCP evidence

`hoi4.focus_inspect` was run against workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `2efca956de1535fff3162f937fc89258036020fd3525a344201f0175e9f3b86c`, and layout hash `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9593af89208d9f0a3b2100076e88d0b00d05cfe8f04760fa1619315ea82e3e12/c7e64f459214ef7505371d8a29fa28d7ad076c92f008885ece1f2ed6ac81e39d/focus-inspect.2efca956de1535ff.json`.

The inspect surface reports 184 national focuses, 14 continuous focuses, 223 connectors, 45 connector crossings, 7 connector-through-node intersections, 28 long connectors, 5 same-row spacing violations, bounds x=1..101 and y=0..19, and a failed `focus-diagnostics` check with 14 blocking focus diagnostics.

The expanded target-file artifact contains 130 layout warnings: 28 `FOCUS_LAYOUT_LONG_CONNECTOR`, 45 `FOCUS_AVOIDABLE_CONNECTOR_CROSSING`, 45 `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`, 7 `FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE`, and 5 `FOCUS_LAYOUT_SAME_ROW_SPACING_UNSATISFIED`. The 14 blocking count is the MCP validation summary; the artifact exposes the underlying warning records and does not mark them with a separate `blocking` field.

`hoi4.focus_render` completed with the same 14-blocking-diagnostic validation result and produced review artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06d2201888009a94e892bbce4e1f0f56b341f51c7115cf52165ae412da78af2e/13163b60ec21baecd13a2b96c2248bf3f436687e48fea33b9280cd34f00c3cd1/independence_wave_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa80848370dc34202a4b67c245207b9e28392e1a443ab096f0530f3d0bebd67e/429ad78ef91689989899b6b94e2faca59ca7adebf225d775cdb715dfc030c767/independence_wave_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3042950478140a1c82191308cfec90826e3fa9bcb914a06a8ad3237c18f0356f/7d765f8dc6a7926a587633450375fff868fd46cc836ac6ff0102f21e3e4ccf27/independence_wave_focus_tree.focus.json`.

## Highest-priority geometry findings

| Priority | Diagnostics and source locations | Why a bounded repair is unsafe |
| --- | --- | --- |
| 1 | `independence_wave_complete_founding_settlement -> independence_wave_map_internal_power_centers` is 17 columns at lines 238-250; the same founding node fans to `independence_wave_ajx_appoint_neutral_commission_focus`, `independence_wave_define_former_host_policy`, `independence_wave_survey_regional_ambition`, `independence_wave_recognize_fellow_new_states`, and `independence_wave_prepare_first_assembly` with 12-67 column spans at lines 337-392 and 460-518. | The fan-out is a shared trunk used by government, host, regional, and package routes; moving one child changes several crossings and package overlay alignment. |
| 2 | Crossings at lines 298-315 involve `independence_wave_bind_the_first_oath`, `independence_wave_inventory_the_state`, `independence_wave_name_provisional_authority`, and their economy/government children; `inventory_the_state -> establish_emergency_revenue` is 12 columns. | The four endpoints are fixed or relative in every unsatisfied record, so a local nudge cannot be isolated to one connector. |
| 3 | Lines 419-543 contain the military and diplomacy convergence: `bind_the_first_oath -> integrate_militia_commands` is 14 columns, and `focus_build_permanent_foreign_service`, `preserve_independent_command`, `standardize_with_league`, `create_independent_treasury`, `confirm_civilian_control`, `found_professional_defense_institution`, and `secure_durable_sovereignty` produce repeated crossings. | This is a multi-route convergence with shared capstones; a single endpoint move would trade one crossing for another or change route readability. |
| 4 | `independence_wave_complete_founding_settlement -> independence_wave_survey_regional_ambition` intersects seven unrelated focuses, including `independence_wave_activate_package_economic_program`, `independence_wave_preserve_independent_command`, and `independence_wave_focus_build_permanent_foreign_service` (lines 375-392). | The connector passes through unrelated nodes; removing it requires reflowing the former-host/ambition lane, not a safe one-node offset. |
| 5 | Package overlay connectors from `independence_wave_prepare_capital_administration` span 48-80 columns to Scotland, Wales, Saar, Brittany, Wallonia, Frisia, Rhineland, Bavaria, Sardinia, and Sicily roots; package rows also produce same-row spacing warnings for Bri/Ajx, SCO/ASX, ARX/ASX, and related overlay nodes. | These are deliberate shared-root imports; moving a package root changes every package connector and could violate the additive-overlay layout contract. |

## Missing or simplified content

No route, focus, prerequisite, mutual exclusion, reward, cost, country overlay, decision hook, mission hook, formable hook, claim/core hook, or high-chaos branch was found missing in this geometry-only scope. The only simplification is that geometry remains unresolved; no gameplay fallback or placeholder was introduced.

## Icon coverage table

| Surface | Result |
| --- | --- |
| 184 national focuses in `independence_wave_focus_tree` | Parent MCP evidence reports valid icon references for all 184; no target-file `FOCUS_ICON_REFERENCE_MISSING` diagnostic was emitted. |
| Package-specific icons under `gfx/interface/goals/006_independence_wave/` and registered `interface/006_independence_wave*.gfx` files | Render scanned the package asset inventory and resolved the target focus icons; no icon id was changed. |
| Continuous-focus diagnostics in vanilla `common/continuous_focus/generic.txt` | The inspect artifact also contains unrelated vanilla missing-sprite errors; they are outside Event 006 geometry scope and were not patched. |

## Localisation and reward mismatch list

Parent MCP evidence reports resolved localisation, reward, cost, prerequisite, and AI coverage for all 184 national focuses. No focus-name/description versus reward mismatch was observed, and no localisation or reward key was changed.

## AI behavior gaps

Parent MCP evidence reports AI blocks for all 184 national focuses. Shared country weighting and route-aware modifiers are present in the source; this geometry pass found no AI gap and made no AI change. Runtime focus choice and timing remain outside static geometry validation.

## Validation and skipped work

Completed: required repository, focus-tree, event, decision, asset, improvement-loop, and subagent skills were read; required offline wiki and vanilla documentation references were consulted; `hoi4.focus_inspect` and `hoi4.focus_render` were run; source coordinates for all five same-row spacing pairs were spot-checked with `rg`; and the target file had no pre-existing worktree change before this handoff.

Skipped: `hoi4.focus_rewrite` was not run because authored/compact rewrite would affect a broad shared tree and cannot be reviewed as a bounded coordinate-only patch; no in-game launch was performed per repository rules.

## Remaining route risks and handoff

The shared tree remains playable at the script-semantic level but visually noisy at the listed crossings, through-node intersections, long connectors, and package-root spacing conflicts. The next safe action is a separately scoped whole-tree geometry pass that can move complete route families, rerun inspect/render, and compare connector counts before and after; it must preserve all focus ids, prerequisites, mutual exclusions, rewards, localisation, AI, and additive-overlay ownership.

Changed files: this handoff only. Changed focus ids: none. Changed localisation keys: none. Changed icon ids: none. Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_geometry_repair_v50_2026_08_01.md`.
