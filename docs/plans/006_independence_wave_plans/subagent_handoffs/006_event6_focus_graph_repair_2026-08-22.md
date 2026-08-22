# Event 006 shared focus graph repair

Date: 2026-08-22

## Scope and disposition

This handoff covers the narrow shared Event 006 focus graph issue in `common/national_focus/006_independence_wave_focus.txt`.

The current source already contains the bounded repair from commit `89729c4b9`, so no additional gameplay source edit was made in this audit.

The source-confirmed repair adds visible prerequisite ownership from `independence_wave_adopt_military_archetype_program` to both previously reported isolated military choices.

The existing removal of the two impossible capstone-specific prerequisite blocks from `independence_wave_found_professional_defense_institution` remains intact.

## Route coverage and source evidence

| Focus identifier | Visible prerequisite | Existing availability gate | Route result |
| --- | --- | --- | --- |
| `independence_wave_standardize_with_league` | `independence_wave_adopt_military_archetype_program` | `has_completed_focus = independence_wave_adopt_military_archetype_program` plus `can_participate_in_independence_wave_network_focuses = yes` | Owned by the military archetype branch and mutually exclusive with independent command. |
| `independence_wave_preserve_independent_command` | `independence_wave_adopt_military_archetype_program` | `has_completed_focus = independence_wave_adopt_military_archetype_program` plus `can_use_independence_wave_full_focus_framework = yes` | Owned by the military archetype branch and mutually exclusive with league standardization. |
| `independence_wave_adopt_military_archetype_program` | `independence_wave_form_border_guard` | `can_use_independence_wave_full_focus_framework = yes` plus `has_valid_independence_wave_force_profile = yes` | Keeps the shared parent route unchanged. |

The two repaired focus definitions are at lines 758-796 of the current focus source.

The professional-defense focus at lines 599-639 retains its three intended OR-pair prerequisite blocks and does not reintroduce the removed capstone-specific prerequisites.

The older completion audit `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event006_completion_audit_current_2026_08_22.md` reported 184 focuses, 193 connectors, and two isolated military choices before this repair was present in its inspected revision.

The current source has the two explicit connectors and leaves all availability predicates and route flags unchanged.

## Before and after route behavior

The stale audit state left `independence_wave_standardize_with_league` and `independence_wave_preserve_independent_command` without visible graph ownership after the impossible capstone-specific blocks were removed.

The current source routes both choices directly from `independence_wave_adopt_military_archetype_program` while retaining their existing availability predicates, mutual exclusions, rewards, AI factors, coordinates, and icons.

No new route family, route lock, reward, or AI weight was introduced by this audit.

## Icon and localisation coverage

| Focus identifier | Icon | Localisation keys | Result |
| --- | --- | --- | --- |
| `independence_wave_adopt_military_archetype_program` | `GFX_goal_independence_wave_army_integration` | `independence_wave_adopt_military_archetype_program`, `_desc`, `_tt` | Existing source and localisation are present. |
| `independence_wave_standardize_with_league` | `GFX_goal_independence_wave_league_congress` | `independence_wave_standardize_with_league`, `_desc`, `_tt` | Existing source and localisation are present. |
| `independence_wave_preserve_independent_command` | `GFX_goal_independence_wave_army_integration` | `independence_wave_preserve_independent_command`, `_desc`, `_tt` | Existing source and localisation are present. |

No localisation or asset reference changed in this audit.

## Simplified content, mismatch list, and AI gaps

No route content was simplified by this audit.

No focus name, description, reward, icon, or localisation mismatch was found for the three identifiers in scope.

No AI weight was changed, so the mandatory probability-auditor route was not needed for this graph-only repair.

The broader Event 006 completion and balance audits remain parent scope and are not reclassified by this handoff.

## MCP evidence

Fresh `hoi4.focus_inspect` was run against `common/national_focus/006_independence_wave_focus.txt` with tree `independence_wave_focus_tree` in national mode.

The inspect returned `FOCUS_INSPECTED` with revision `33cafa6f042f1e23f4afe7ca54165024e1b901b3581df29bdbf8646484c8d0f2` and artifact URI `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/851e9df4eabd39e1c2200e1e81fe6ebd0bfdbcfbf66e8f3c97146bbef28aab0e/7493d59331ddf4217fcf7e9a442b0d034657b6366b921f7f2a86707b0938f9dd/focus-inspect.33cafa6c042f1e23.json`.

The inspected tree contains 184 focuses and 195 connectors with zero isolated nodes, zero crossings, and zero node intersections.

The inspect recognizes both direct connectors from `independence_wave_adopt_military_archetype_program` to the two military choices.

The inspect reports three unrelated long Event 006 connectors for the two repaired choices and one authored downstream branch, plus four linear-detour warnings.

The 14 blocking validation diagnostics are generic vanilla continuous-focus icon references outside the scoped Event 006 focus file.

Two fresh `hoi4.focus_render` attempts were made with the inspected workspace. Both timed out after 180 seconds before returning `FOCUS_RENDERED`.

A retry that supplied `columns` was rejected because `columns` is invalid in national mode, so no unsupported render parameter was retained.

The existing prior handoff `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_prerequisite_repair_2026-08-22.md` records an earlier successful `FOCUS_RENDERED` artifact for this same repair workspace, but a fresh render artifact could not be retrieved in this audit.

No `hoi4.focus_rewrite` was used because the source repair is already present and an automatic rewrite would affect accepted authored geometry outside this narrow graph issue.

## Changed files and identifiers

No gameplay file was changed by this subtask.

The only new file is this handoff.

The source-confirmed identifiers are `independence_wave_adopt_military_archetype_program`, `independence_wave_standardize_with_league`, `independence_wave_preserve_independent_command`, and `independence_wave_found_professional_defense_institution`.

## Remaining risks and parent action

The two repaired connectors are long in the authored layout, spanning 11 and 13 columns respectively, but the graph is connected and has no isolated-node diagnostic.

The fresh render remains blocked by the MCP timeout, and the inspect remains non-passing only because of unrelated generic vanilla continuous-focus icon diagnostics.

The parent should treat the graph repair as already present in commit `89729c4b9`, retain the source as-is, and cite the inspect artifact plus the render timeout if a new render is required for the final release audit.
