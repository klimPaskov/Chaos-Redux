# Event 6 shared focus layout patch handoff - 2026-07-19

## Scope and outcome

This bounded pass audited the shared layout in `common/national_focus/006_independence_wave_focus.txt` and tested source-only coordinate moves. The gameplay source is intentionally unchanged: `git diff -- common/national_focus/006_independence_wave_focus.txt` is empty. No focus id, prerequisite, mutual exclusion, availability, completion reward, icon, localisation key, AI block, or standalone IW093/IW098 file was changed.

The authored MCP rewrite was tested only with complete plans imported from `hoi4.focus_inspect`. Moving a single early endpoint (`integrate_provinces_and_councils`) and then the economy endpoints relocated the same blocking crossings and introduced additional crossing/long-connector warnings. Those candidates were rejected and the source was restored to the baseline coordinate set.

## Evidence

Final read-only inspect (baseline source):

- Workspace: `mod_chaos_redux_ea3b2d67c2c0`
- Tree: `independence_wave_focus_tree`
- Source: `common/national_focus/006_independence_wave_focus.txt`
- Layout hash: `3e5996acbdbed97ab085d52cd058861f2fbd21acc896f859268b204a9c81a5a2`
- Metrics: 176 regular focus nodes, 214 connectors, bounds x=1..97/y=0..19, 49 geometric crossings, 18 node intersections, 26 long connectors.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb5ae5625ea8ca7f878aff685cdb9abe60b157815ef89d60c001b571491037dc/f46aa61946256fbcf9fcc9dae3e37f2c07c7af0d5d5f94b0eaa0fdc1e15e3a75/focus-inspect.8e0ce8bab26b528d.json`

Final render (same baseline source):

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d85859905f79f273630c41c090e6eac7288552cd798b39197a59efd0392992be/00f4a081632ef4b2fe3c1206cfa62f40c9aa408a84a7b64848fc881000abd529/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d74054ceefae952e810f86c67444a78301b86cf14fd47387159136c514bfc1a/4bc2ac7fb8ffe4aa99a73e171e7499d5d525e4ae8194a246d1c7bb18503f3344/independence_wave_focus_tree.focus.svg`
- Render validation remains `14 blocking focus diagnostics` (layout-only).

## Route coverage

| Route surface | Representative focus ids / source lines | Coverage result |
|---|---|---|
| Founding administration | `prepare_capital_administration`, `name_provisional_authority`, `inventory_the_state`, `bind_the_first_oath`, `integrate_provinces_and_councils`, `complete_founding_settlement` (lines 62-216) | Present; no semantic gaps found |
| Economy and state capacity | `establish_emergency_revenue`, `secure_food_and_fuel`, `build_regional_transport_authority`, `establish_customs_service`, `activate_package_economic_program`, `create_independent_treasury` (lines 280-397) | Present; economy connector crossings remain |
| Early defense and professional institution | `secure_national_depots`, `recall_and_vet_officers`, `adopt_military_archetype_program`, `confirm_civilian_control`, `grant_military_autonomy`, `raise_mass_reserve`, `build_professional_core`, `found_professional_defense_institution` (lines 421-608) | Present; professional-defense connector crossings remain |
| Military outcomes | `adopt_border_defense`, `adopt_reclamation_doctrine`, `standardize_with_league`, `preserve_independent_command` (lines 611-663) | Present; cross-product edges into the capstone remain |
| External and regional policy | `ajx_appoint_neutral_commission_focus` (1214), `define_former_host_policy` (1274), `recognize_fellow_new_states` (1529), `survey_regional_ambition` (1456), `secure_durable_sovereignty` (2896) | Present; root fan-out crossings remain |
| Shared overlay / package extensions | 13 `shared_focus` blocks at the end of the source; root references include IW093/IW098 | Present; standalone IW093/IW098 intentionally out of scope |

## Missing or simplified content

- No route, reward, decision hook, formable hook, country identity, or shared-focus mechanic was removed or simplified.
- A full planar redesign was not attempted because it would require coordinated movement of the founding fan-out, economy lane, officer lane, regional roots, and professional-defense convergence; moving one endpoint at a time only relocates blockers.
- The compact MCP rewrite was attempted once and returned `FOCUS_COMPACT_QUALITY_BLOCKED`; no compact output was applied.

## Final blocking diagnostics (baseline)

The following 14 layout diagnostics are the only blockers reported by the final inline inspect (one avoidable crossing plus 13 unsatisfied crossings):

1. `bind_the_first_oath -> integrate_provinces_and_councils` crosses `inventory_the_state -> establish_emergency_revenue` (lines 119, 177, 100, 281).
2. `complete_founding_settlement -> ajx_appoint_neutral_commission_focus` crosses `secure_food_and_fuel -> build_regional_transport_authority` (lines 197, 1214, 300, 320).
3. `complete_founding_settlement -> define_former_host_policy` crosses the same economy edge (line 1274).
4. `complete_founding_settlement -> recognize_fellow_new_states` crosses the same economy edge (line 1529).
5. `complete_founding_settlement -> ajx_appoint_neutral_commission_focus` crosses `secure_national_depots -> recall_and_vet_officers` (lines 421, 442).
6. `complete_founding_settlement -> define_former_host_policy` crosses the same officer edge.
7. `complete_founding_settlement -> recognize_fellow_new_states` crosses the same officer edge.
8. `adopt_military_archetype_program -> adopt_border_defense` crosses `confirm_civilian_control -> found_professional_defense_institution` (lines 483, 611, 527, 502).
9. The same border-defense edge crosses `grant_military_autonomy -> found_professional_defense_institution` (line 541).
10. `adopt_military_archetype_program -> adopt_reclamation_doctrine` crosses the civilian-control edge (line 625).
11. The same reclamation edge crosses the military-autonomy edge.
12. `adopt_military_archetype_program -> preserve_independent_command` crosses `build_professional_core -> found_professional_defense_institution` (lines 653, 569).
13. `adopt_military_archetype_program -> standardize_with_league` crosses the civilian-control edge (line 639).
14. The same standardize edge crosses the military-autonomy edge.

Remaining nonblocking layout warnings are the long connectors `complete_founding_settlement -> map_internal_power_centers`, `inventory_the_state -> establish_emergency_revenue`, `bind_the_first_oath -> integrate_militia_commands`, plus through-node intersections from `complete_founding_settlement -> survey_regional_ambition` through `activate_package_economic_program` and `adopt_military_archetype_program`.

## Icon, localisation, reward, and AI audit

| Surface | Result |
|---|---|
| Icons | 176 regular focus blocks and 13 shared-focus blocks each carry an `icon` assignment in this source; no missing-sprite diagnostic was emitted by the final focus inspect. No icon id changed. |
| Localisation | MCP resolved titles for all 176 regular focuses; no missing focus title/description diagnostic was emitted. No localisation key changed. |
| Rewards and hooks | No reward/localisation mismatch was reported. Existing decision, idea, event, claim/core, war-goal, and formable hooks were preserved. |
| AI | All 189 source blocks have `ai_will_do` and `available` entries by source count; no AI diagnostic was emitted. No AI weight changed. |

## High-priority next pass

1. Treat the economy and officer lanes as coupled layout clusters rather than moving only `build_regional_transport_authority` or `recall_and_vet_officers`.
2. Reposition the three regional roots (`ajx_appoint_neutral_commission_focus`, `define_former_host_policy`, `recognize_fellow_new_states`) together with the y=3/y=4 founding fan-out so the economy and officer vertical edges have a clear side of the fan-out.
3. Repack the professional-defense subgraph (`confirm_civilian_control`, `grant_military_autonomy`, `raise_mass_reserve`, `build_professional_core`, the four doctrine outcomes, and `found_professional_defense_institution`) as one converging cohort.
4. Only after the 14 blockers are cleared, address long connectors and the two through-node warnings.

## Changed files / identifiers

- Added this handoff only: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_shared_focus_layout_patch_2026_07_19.md`.
- Gameplay source changed: none.
- Focus ids changed: none.
- Localisation keys changed: none.
- Icon ids changed: none.

## Validation limits

The final inspect and render were run against the restored baseline. They confirm the same 14 layout blockers; they do not prove a future coordinated layout redesign. No game runtime or save-based validation was run because no gameplay source changed.
