# Event 006 focus geometry v62 handoff

Date: 2026-08-01

Scope: Geometry-only audit of `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt`. The direct 184-focus framework and shared/CAT import boundary were preserved. No route, prerequisite, reward, icon, localisation, AI, country, decision, formable, asset, workbook, or unrelated Event 020/Fallout file was changed.

## Outcome

`hoi4.focus_inspect` and `hoi4.focus_render` both reproduce the authored layout hash `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf` and report `validation.passed = false` with **14 blocking focus diagnostics**. The tree has 184 direct focuses, 223 connectors, 45 connector crossings, 7 node intersections, and 28 long connectors. The 14-blocker summary is the same as the v47 accepted authored-layout hold.

The raw MCP diagnostics expose 19 warning entries because several crossing entries are separate pairings over the same connector endpoint. Every geometry location resolves to the direct Event 006 tree (lines 246-677); none is sourced from a shared-focus definition or a CAT overlay import. The direct tree closes at line 3165. Shared-focus definitions begin at line 3172, and the CAT additive roots are only import declarations at lines 77-82. Therefore these are genuine Event 006 authored-layout warnings, not external/shared-import blockers. They are visual/layout blockers in MCP, not Clausewitz route or load blockers.

No narrow coordinate move was retained. Two reversible probes were tested and restored: moving `independence_wave_adopt_military_archetype_program` x=36 to x=39 reduced long connectors (28 to 26) but introduced a new through-node crossing and a 10-column connector; moving `independence_wave_establish_emergency_revenue` x=32 to x=28 reduced long connectors (28 to 27) but introduced a new through-node crossing. Neither reduced the 14-blocking summary, so both were rejected. `git diff` confirms the focus source is unchanged.

## Route coverage

| Required route family | Implemented source range | Geometry status |
| --- | --- | --- |
| Survival/state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement`, lines 88-242 | Covered; capstone fan-out causes intentional crossings |
| Economy/infrastructure | `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury`, lines 306-421 | Covered; one long connector and two crossing pair groups |
| Army/security and professional defence | Lines 427-691 | Covered; one long opening connector, four capstone crossing pairings, and four long edge connectors |
| Diplomacy/recognition/patrons | Lines 697-836 | Covered; no direct diagnostic endpoint except the final sovereignty route crossing |
| Government settlements/internal power | Lines 844-1294 (including AJX municipal commission) | Covered; no reward or route edit in this audit |
| Former-host settlement and regional ambition | Lines 1300-1529 | Covered; capstone-to-former-host and regional fan-out crossings are authored geometry |
| Network/league/formable/signature | Lines 1536-1979 and shared imports at lines 40-82 | Covered; shared imports are not the source of current diagnostics |
| Country/package overlays | Lines 1997-3145 plus root shared imports | Covered; no package geometry warning is reported by MCP |

## Exact diagnostics

| # | MCP code | Connector(s) | Source lines | Impact |
| ---: | --- | --- | ---: | --- |
| 1 | `FOCUS_LAYOUT_LONG_CONNECTOR` | `complete_founding_settlement -> map_internal_power_centers` (17 columns) | 246-258 | Founding capstone to optional internal-power branch is a broad fan-out |
| 2 | `FOCUS_AVOIDABLE_CONNECTOR_CROSSING` | `bind_the_first_oath -> integrate_provinces_and_councils` × `inventory_the_state -> establish_emergency_revenue` | 306-323 | Opening survival/economy paths cross |
| 3 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | Same pair as #2; endpoints fixed/relative | 306-323 | Same crossing cannot be auto-rerouted |
| 4 | `FOCUS_LAYOUT_LONG_CONNECTOR` | `inventory_the_state -> establish_emergency_revenue` (12 columns) | 306-323 | Economy lane starts far right of the inventory parent |
| 5 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `complete_founding_settlement -> ajx_appoint_neutral_commission_focus` × `secure_food_and_fuel -> build_regional_transport_authority` | 345-362 | Founding fan-out crosses economy lane |
| 6 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `complete_founding_settlement -> define_former_host_policy` × `secure_food_and_fuel -> build_regional_transport_authority` | 345-362 | Same |
| 7 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `complete_founding_settlement -> recognize_fellow_new_states` × `secure_food_and_fuel -> build_regional_transport_authority` | 345-362 | Same |
| 8 | `FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE` | `complete_founding_settlement -> survey_regional_ambition` intersects `activate_package_economic_program` | 383-400 | Regional ambition connector runs through economy capstone |
| 9 | `FOCUS_LAYOUT_LONG_CONNECTOR` | `bind_the_first_oath -> integrate_militia_commands` (14 columns) | 427-445 | Army lane starts far right of the oath parent |
| 10 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `complete_founding_settlement -> ajx_appoint_neutral_commission_focus` × `secure_national_depots -> recall_and_vet_officers` | 468-487 | Founding fan-out crosses depot lane |
| 11 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `complete_founding_settlement -> define_former_host_policy` × `secure_national_depots -> recall_and_vet_officers` | 468-487 | Same |
| 12 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `complete_founding_settlement -> recognize_fellow_new_states` × `secure_national_depots -> recall_and_vet_officers` | 468-487 | Same |
| 13 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `complete_founding_settlement -> survey_regional_ambition` × `form_border_guard -> adopt_military_archetype_program` | 509-526 | Regional and army lanes cross |
| 14 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `focus_build_permanent_foreign_service -> secure_durable_sovereignty` × `preserve_independent_command -> found_professional_defense_institution` | 528-551 | Final capstones cross |
| 15 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `focus_build_permanent_foreign_service -> secure_durable_sovereignty` × `standardize_with_league -> found_professional_defense_institution` | 528-551 | Same final-capstone fan |
| 16 | `FOCUS_LAYOUT_LONG_CONNECTOR` | `confirm_civilian_control -> found_professional_defense_institution` (9 columns) | 528-551 | Professional-defence choice edge |
| 17 | `FOCUS_LAYOUT_LONG_CONNECTOR` | `preserve_independent_command -> found_professional_defense_institution` (9 columns) | 528-551 | Professional-defence choice edge |
| 18 | `FOCUS_LAYOUT_LONG_CONNECTOR` | `adopt_military_archetype_program -> adopt_reclamation_doctrine` (9 columns) | 651-663 | Right-side archetype choice edge |
| 19 | `FOCUS_LAYOUT_LONG_CONNECTOR` | `adopt_military_archetype_program -> standardize_with_league` (11 columns) | 665-677 | Right-side archetype choice edge |

Entries 2/3, 5-7, 10-12, and 14-15 are duplicate diagnostic views of the same seven crossing groups. MCP's validation summary correctly reports 14 blocking diagnostics; the raw collection should be retained as the detailed audit evidence.

## Missing or simplified content

- No direct focus route is missing: the inspect result resolves all 184 direct focus blocks.
- No shared/CAT import was changed or silently treated as a direct geometry fix.
- Geometry is still an authored-layout hold; no automatic compact rewrite or route redesign was applied.

## Icon, localisation, reward, and AI checks

This geometry-only pass found no new issue in these surfaces. The prior v47 static audit remains the source for the full 312-block icon/localisation/reward/AI cross-check: all scanned focus blocks had resolved icons, title/description keys, completion tooltips, completion rewards, AI blocks, and constant-based costs. Package focus blocks that rely on paired `common/ai_strategy/006_independence_wave_*.txt` route profiles remain a review risk but are unrelated to the geometry warnings.

## High-priority follow-up

1. Keep the current authored layout and treat the 14 MCP diagnostics as a parent-owned geometry follow-up, not a package-admission shortcut.
2. Any future reflow must move whole lane anchors or add deliberate intermediary layout nodes; moving one endpoint can trade a long connector for a through-node crossing without reducing the blocking count, as shown by the two rejected probes above.
3. Preserve the professional-defense five-choice grouping and the direct/shared import boundary during any future reflow.

## Validation

- `hoi4.focus_inspect` (workspace `mod_chaos_redux_ea3b2d67c2c0`): status `FOCUS_INSPECTED`; 184 focuses; 223 connectors; 14 blocking diagnostics; layout hash `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`.
- `hoi4.focus_render`: status `FOCUS_RENDERED`; HTML/SVG/JSON artifacts preserve the same layout hash and rendered dimensions 17904x2440.
- Static source hygiene: balanced braces (1811/1811), no unsupported `<=` or `>=` operators, 184 direct focus blocks, and no retained source diff after reversible probes.
- Skipped `hoi4.focus_rewrite` because compact mode would be a whole-tree geometry rewrite outside this narrow task scope.
- Skipped in-game execution per repository policy; live consumer validation belongs to the parent/user.

## Artifacts

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bcb9184d157feb36d09853145723cdfe92ee7bf9ca7425a98ba70b8bb53ce6f3/5c3dddbc6390185f7ea57e8ae65b8740581edee2ae1c68147fb01ef47210a528/focus-inspect.6aaf5ffe9d69da13.json`
- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/851338a874752aab23cb217f917a6b59a0594e39460b7c8e9f698c05c9c09cdc/74c6a641def624f32ba89bb40c64e9ffe9dc53f6668a5ca195c2ed2bd37dd993/independence_wave_focus_tree.focus.html`
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db058a79681af4beadd7012b103961104222162d8df430e7e294a1c47cbc39dd/ad53ec81572a74fa7f58ba831c50d90372562fac6834b0206e6bd8c637476d24/independence_wave_focus_tree.focus.svg`
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9987bc22eed2ddcd71c28c705169b9dbfc5a14fa683952abf57ae6a5b739570/d25c29c57b68c61c8a04dcff831b0168502877ad768012a29ab77af3d0e40b14/independence_wave_focus_tree.focus.json`
- Render source-map and plan artifacts are available in the same MCP render result and share layout hash `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`.

No gameplay files changed in this audit. Parent review is required before any broad geometry reflow.
