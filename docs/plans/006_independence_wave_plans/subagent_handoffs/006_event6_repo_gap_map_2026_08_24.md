# Repo Explorer Handoff

## Scope read

- Parent task: audit Event 006 against the accepted specifications, `006_source_of_truth_map.md`, and `006_independence_wave_resume_packet.md`, then identify one bounded next implementation gap.
- Explicit constraints: read-only repository exploration; no gameplay, localisation, GUI, GFX, asset, history, country, focus, decision, scripted-effect, scripted-trigger, on-action, event, spreadsheet, or plan-source edits; this handoff is the only requested write.
- Files and ids reviewed: `chaosx.nr6.1`, `.2`, `.3`, the Event 006 focus tree `independence_wave_focus_tree`, and the economy-lane focuses `independence_wave_secure_food_and_fuel`, `independence_wave_build_regional_transport_authority`, `independence_wave_establish_customs_service`, `independence_wave_activate_package_economic_program`, and `independence_wave_create_independent_treasury`.
- Skills and references read: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, the required offline wiki core pages plus `National focus modding - Hearts of Iron 4 Wiki.md`, and the installed vanilla documentation for effects, triggers, script concepts, localisation objects, and dynamic variables.

## Primary findings

The single safest source-addressable next tranche is one coordinate-only focus-layout correction: move `independence_wave_build_regional_transport_authority` from `x = 32, y = 5` to `x = 32, y = 4` in `common/national_focus/006_independence_wave_focus.txt:411-428`. Its sole visible prerequisite, `independence_wave_secure_food_and_fuel`, is at `x = 32, y = 3`, while the next economy nodes continue at `x = 32, y = 6`, `y = 7`, and `y = 8`; the current `x = 32, y = 4` coordinate is unused in the source file.

The current focus evidence explicitly records this edge as `FOCUS_LAYOUT_LINEAR_DETOUR`. This is the smallest remaining authored layout defect with a concrete id, a direct source fix, and no change to prerequisites, availability, rewards, AI, package admission, or runtime event behavior. It is safer than selecting one of the 161 unattested packages, changing a weighted surface without the required probability-auditor route, or changing payment logic whose trigger/effect/localisation contracts must move together.

This is not a whole-focus acceptance claim. The source-of-truth map and resume packet still record seven Event 006 authored layout warnings, fourteen unrelated vanilla continuous-focus icon diagnostics, and focus acceptance `HOLD`; this one-line correction addresses only the named economy detour.

The exact automatic ladder is not the next gap: commit `a2abd65d7` and the current handoff already preserve nominal `3/4/5/7/10` targets and fail closed with `insufficient_pool`. The current boundary remains 32 content-attested packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `common/national_focus/006_independence_wave_focus.txt:391-487` | Owns the economy lane and the exact bounded edit. `secure_food_and_fuel` is `x = 32, y = 3`; `build_regional_transport_authority` is `x = 32, y = 5`; `establish_customs_service`, `activate_package_economic_program`, and `create_independent_treasury` follow at `y = 6`, `7`, and `8`. | Direct source inspection; no `x = 32, y = 4` focus is present. The nearest local direct-chain pattern is the military lane at `:518-578`, where `y = 3`, `4`, and `5` are consecutive before a deliberate branch gap. |
| `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md:965-978` | Accepted layout direction requires a broad readable tree, economy support lanes, visually clear capstones, and regional modules that do not cross the whole tree. | The economy detour contradicts the direct readable lane shape, while the proposed coordinate change preserves all route logic. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_overlay_audit_2026-08-22.md` | Current source-linked focus audit names `independence_wave_secure_food_and_fuel` → `independence_wave_build_regional_transport_authority` as a medium `FOCUS_LAYOUT_LINEAR_DETOUR` and records that no source was changed. | Existing inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c823cbdb823425b8cba8975d6d874e17b7c63347705a79a318394e4ea24aebd/2a391953ddd07ecc70e2a7d7214556448ef980161cdfe17b0f7b46cf0a966c20/focus-inspect.e96a318054c8867f.json`; render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe758b11228c203e9dbbbe784074e0da37e5049de9ed492a8e1e2f55403ae66c/71b6ff14ad894ed30e344782b8638ac57e6a392f023c2d9bb30315c2218e1a5c/independence_wave_focus_tree.focus.svg`. |
| `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:49-94` | Current authority retains focus `HOLD`, seven authored warnings, the 32/29/40/161 boundary, and the queued instruction to rerun focus inspect/render after a parent-owned graph change. | Current source-of-truth map; it also records the latest source-linked focus artifacts and the absence of a focus lint/validate route. |
| `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:9-13,49,65-84` | Confirms the current package boundary, exact ladder repair, focus warning hold, and continuation order. | Current resume packet; it supersedes older package counts and partial-wave recommendations. |
| `events/006_independence_wave.txt:11-127` | Defines hidden entry `chaosx.nr6.1`, committed-only public report `chaosx.nr6.2`, and retired cleanup `chaosx.nr6.3`; no event-logic patch is recommended. | Narrow `hoi4.event_inspect` and `hoi4.event_render` evidence below show the event surface remains partial rather than exposing a safer source defect. |

## Existing patterns

The closest Chaos Redux pattern is the same file's military lane: `independence_wave_integrate_militia_commands` at `x = 38, y = 2`, `independence_wave_secure_national_depots` at `x = 38, y = 3`, `independence_wave_recall_and_vet_officers` at `x = 38, y = 4`, and `independence_wave_form_border_guard` at `x = 38, y = 5`. The subsequent `y = 7` military-archetype node is an intentional branch/fork layout, so it should not be copied as an economy-lane detour.

Keep the proposed patch in the existing absolute `x`/`y` style. Do not add `relative_position_id`, alter the prerequisite, or use `hoi4.focus_rewrite`; the accepted tree has authored coordinates and the requested tranche is a one-line local correction.

## Vanilla or reference precedents

- Offline wiki: `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`, sections “Position” and “Interaction with other focuses”, states that prerequisite parents should be above children and that coordinates determine the focus grid position.
- Vanilla: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/australia_taog.txt:213-225` defines `AST_the_pacific_pact` immediately below `AST_war_is_coming` with `relative_position_id`, `x = 0`, and `y = 1`, demonstrating the direct one-row prerequisite pattern. The proposed change uses the existing Chaos Redux absolute-coordinate style while preserving the same geometry principle.
- No vanilla gameplay or cost logic is needed for this tranche. The relevant vanilla documentation directory contains no separate national-focus reference; the offline national-focus page is the applicable syntax authority.

## Likely edit order for the parent

1. Review the existing dirty diff for `common/national_focus/006_independence_wave_focus.txt` and confirm the target block is not concurrently owned by another patch.
2. Change only the `y = 5` line under `independence_wave_build_regional_transport_authority` to `y = 4`; leave its prerequisite, availability, reward, icon, cost, search filters, and `ai_will_do` unchanged.
3. Verify that no other direct or imported focus occupies the resulting coordinate and that the economy lane remains readable in the normal-zoom render.
4. Rerun the mandatory national-focus inspect and render, then review the returned source map and diagnostics. Accept only if the economy detour is gone and no crossing, overlap, isolated node, or new long-connector diagnostic appears.
5. Keep the remaining authored warnings, unrelated vanilla continuous-focus diagnostics, package backlog, probability limitation, GUI evidence gap, and super-event 23 rights block as separate follow-up items; do not widen this tranche.

## Validation checks

- Source check before and after the edit: `rg -n -C 4 "id = independence_wave_(secure_food_and_fuel|build_regional_transport_authority|establish_customs_service|activate_package_economic_program|create_independent_treasury)|x = 32|y = 4|y = 5" common/national_focus/006_independence_wave_focus.txt`.
- Run `hoi4.focus_inspect` with `mode = national`, `relativePath = common/national_focus/006_independence_wave_focus.txt`, `treeId = independence_wave_focus_tree`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.
- Run matching `hoi4.focus_render` for the same path/tree and inspect the normal-zoom SVG/JSON/source-map artifacts. Expected topology remains 184 direct focuses and 195 connectors unless concurrent source changes exist; the named economy `FOCUS_LAYOUT_LINEAR_DETOUR` should disappear without new Event 006 geometry diagnostics.
- Confirm the source diff contains exactly one coordinate change in the target block and no edits under `common/decisions`, `common/scripted_effects`, `common/scripted_triggers`, `events`, localisation, GUI, or assets.
- Run the current static smoke commands if the parent has any concurrent Event 006 edits: `python -B .tools/audit_event6_allocator.py`, `python -B .tools/audit_event6_country_api.py`, `python -B .tools/audit_event6_flags.py --strict`, `python -B .tools/audit_event6_scenario_matrix.py`, and `python -B .tools/audit_event6_form16.py`.
- Focus lint/validate routes are not exposed in the installed package, so `hoi4.focus_inspect`/`hoi4.focus_render` are the available engine-backed checks; source-only review must not be reported as equivalent if those calls remain unavailable.

## Risks and blockers

Confirmed blockers:

- Fresh `hoi4.focus_inspect` and `hoi4.focus_render` calls for this audit both timed out after 180 seconds, so no post-change or fresh current-revision focus acceptance can be claimed here. The dated 2026-08-22 artifacts above are the usable source-linked baseline.
- Fresh Event 006 MCP inspect/render returned `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` with deferred helper/lifecycle projections, 8,289 unresolved nodes in the workspace projection, and 41,225 omitted render nodes. `hoi4.event_compare` first returned `EVENT_COMPARISON_BASELINE_REQUIRED`, then `EVENT_REVISION_NOT_CACHED` for the requested prior revision. These are evidence limits, not reasons to change event logic.
- The callable `chaosx_ai_probability_auditor` route is not exposed in this runtime. No weighted target, AI, MTTH, or `ai_chance` change is recommended or supported by this handoff.

Ordinary risks:

- A coordinate-only move can expose a collision or branch-clarity issue in imported/shared focus projections that is not visible from the direct source file; the mandatory MCP rerun must check the full tree before acceptance.
- One warning removal does not clear the focus `HOLD`; the remaining authored detours/long connectors and unrelated vanilla continuous-focus icon diagnostics remain documented.
- The patch is layout-only, but focus coordinate changes can affect normal-zoom readability and connector routing. Do not combine it with prerequisite, AI, cost, localisation, package, or GUI changes.

## Recommended next action

Apply the single coordinate change `independence_wave_build_regional_transport_authority: y = 5` → `y = 4` in `common/national_focus/006_independence_wave_focus.txt`, then rerun `hoi4.focus_inspect` and `hoi4.focus_render` when the MCP route is available. If the tool continues to time out, leave the source unchanged and carry this exact blocker forward rather than claiming the detour is resolved.
