# Event 006 shared focus-tree MCP diagnostics handoff

## Scope and result

Read-only audit of `independence_wave_focus_tree` in
`common/national_focus/006_independence_wave_focus.txt`. No gameplay, focus,
icon, localisation, portrait, or layout files were changed. The MCP workspace
was `mod_chaos_redux_ea3b2d67c2c0`, revision
`2549e0eb4238079c04af453e2b07327ac2f612effeb5cf0ca15afde383a97bc7`.

`hoi4.focus_inspect` reports 176 regular focuses, 214 connectors, and 148
diagnostics. The validation check says **14 blocking focus diagnostics**.
Those 14 are layout crossings only. This run reports no parser, focus-tree
wiring, icon, localisation, or prerequisite-semantics blocker. The MCP source
inventory is truncated in the inline response, not in the scan: 68 paths were
scanned and only 64 returned inline (`MCP_INLINE_FILES_TRUNCATED`, info).

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2897f68793adb93b5a9529d02cc55dbae779c6790aa1691ffc1abe7fd2234a18/fb8954a8f9ff77c9d408d98b51fa7c7808a0fa4c0c077d0eab5c7eb4e23743ad/focus-inspect.2549e0eb4238079c.json`

## Exact blocking diagnostics (14)

The 14 blocking entries are one `FOCUS_AVOIDABLE_CONNECTOR_CROSSING` and
thirteen `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` entries. Every entry
has `severity = warning`, `category = layout`, and fixed/relative endpoints.

| # | Code | Source location | Crossing endpoints |
| --- | --- | --- | --- |
| 1 | `FOCUS_AVOIDABLE_CONNECTOR_CROSSING` | `006_independence_wave_focus.txt:280-297`, symbol `independence_wave_establish_emergency_revenue` | `independence_wave_bind_the_first_oath -> independence_wave_integrate_provinces_and_councils` crosses `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue` |
| 2 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:280-297`, symbol `independence_wave_establish_emergency_revenue` | same pair as #1 |
| 3 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:319-336`, symbol `independence_wave_build_regional_transport_authority` | `independence_wave_complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` crosses `independence_wave_secure_food_and_fuel -> independence_wave_build_regional_transport_authority` |
| 4 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:319-336`, symbol `independence_wave_build_regional_transport_authority` | `independence_wave_complete_founding_settlement -> independence_wave_define_former_host_policy` crosses `independence_wave_secure_food_and_fuel -> independence_wave_build_regional_transport_authority` |
| 5 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:319-336`, symbol `independence_wave_build_regional_transport_authority` | `independence_wave_complete_founding_settlement -> independence_wave_recognize_fellow_new_states` crosses `independence_wave_secure_food_and_fuel -> independence_wave_build_regional_transport_authority` |
| 6 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:441-460`, symbol `independence_wave_recall_and_vet_officers` | `independence_wave_complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` crosses `independence_wave_secure_national_depots -> independence_wave_recall_and_vet_officers` |
| 7 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:441-460`, symbol `independence_wave_recall_and_vet_officers` | `independence_wave_complete_founding_settlement -> independence_wave_define_former_host_policy` crosses `independence_wave_secure_national_depots -> independence_wave_recall_and_vet_officers` |
| 8 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:441-460`, symbol `independence_wave_recall_and_vet_officers` | `independence_wave_complete_founding_settlement -> independence_wave_recognize_fellow_new_states` crosses `independence_wave_secure_national_depots -> independence_wave_recall_and_vet_officers` |
| 9 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:501-524`, symbol `independence_wave_found_professional_defense_institution` | `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_border_defense` crosses `independence_wave_confirm_civilian_control -> independence_wave_found_professional_defense_institution` |
| 10 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:501-524`, symbol `independence_wave_found_professional_defense_institution` | `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_border_defense` crosses `independence_wave_grant_military_autonomy -> independence_wave_found_professional_defense_institution` |
| 11 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:501-524`, symbol `independence_wave_found_professional_defense_institution` | `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_reclamation_doctrine` crosses `independence_wave_confirm_civilian_control -> independence_wave_found_professional_defense_institution` |
| 12 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:501-524`, symbol `independence_wave_found_professional_defense_institution` | `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_reclamation_doctrine` crosses `independence_wave_grant_military_autonomy -> independence_wave_found_professional_defense_institution` |
| 13 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:501-524`, symbol `independence_wave_found_professional_defense_institution` | `independence_wave_adopt_military_archetype_program -> independence_wave_preserve_independent_command` crosses `independence_wave_build_professional_core -> independence_wave_found_professional_defense_institution` |
| 14 | `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `:501-524`, symbol `independence_wave_found_professional_defense_institution` | `independence_wave_adopt_military_archetype_program -> independence_wave_standardize_with_league` crosses `independence_wave_confirm_civilian_control -> independence_wave_found_professional_defense_institution` |

## Non-blocking layout warnings

These are in the 148 total diagnostics but are not part of the 14 blocking
count:

| Code | Source location | Finding |
| --- | --- | --- |
| `FOCUS_LAYOUT_LONG_CONNECTOR` | `:220-232`, symbol `independence_wave_map_internal_power_centers` | `complete_founding_settlement -> map_internal_power_centers`, 17 columns |
| `FOCUS_LAYOUT_LONG_CONNECTOR` | `:280-297`, symbol `independence_wave_establish_emergency_revenue` | `inventory_the_state -> establish_emergency_revenue`, 12 columns |
| `FOCUS_LAYOUT_LONG_CONNECTOR` | `:400-418`, symbol `independence_wave_integrate_militia_commands` | `bind_the_first_oath -> integrate_militia_commands`, 14 columns |
| `FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE` | `:357-374`, symbol `independence_wave_activate_package_economic_program` | `complete_founding_settlement -> survey_regional_ambition` intersects `activate_package_economic_program` |
| `FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE` | `:482-499`, symbol `independence_wave_adopt_military_archetype_program` | `complete_founding_settlement -> survey_regional_ambition` intersects `adopt_military_archetype_program` |

The remaining total is the MCP inventory info plus diagnostics not surfaced as
blocking by the validation check. The inspect result has no parser or
unresolved-reference error code.

## Shared-focus import/load confirmation

HOI4 national-focus files are directory-scanned. The offline National Focus
modding reference states that trees may be defined in any
`common/national_focus/*.txt` file and the filename is organizational only.
This package follows that model:

* `common/national_focus/006_independence_wave_focus.txt:25` defines
  `independence_wave_focus_tree`.
* The tree explicitly seeds
  `shared_focus = independence_wave_iw093_seat_kumasi_administration` at line
  55 and `shared_focus = independence_wave_iw098_reconvene_emirate_council` at
  line 56.
* `common/national_focus/006_independence_wave_iw093_iw098_focus.txt:23-24`
  defines the IW-093 root shared focus
  `independence_wave_iw093_seat_kumasi_administration`.
* The same standalone file defines the IW-098 root at
  `:405-406`, `independence_wave_iw098_reconvene_emirate_council`, and the
  IW-098 terminal preparation focus at `:738-739`.

Therefore the standalone file is loaded. The apparent omission is the MCP
inline inventory cap (`68` scanned versus `64` returned), not a missing import
directive or a focus-tree load failure. The scan status is `FOCUS_INSPECTED`,
with 176 resolved titles and all listed focus/icon/localisation dependencies.

## Route, asset, localisation, and AI audit boundary

This pass was limited to the MCP diagnostic/import question. No route family,
reward, AI weight, icon family, localisation wording, advisor asset, or
portrait surface was changed or re-designed. The MCP result resolves 176 title
keys and returns no icon/localisation/parser blocker. Full route-depth and
reward/AI audits remain the responsibility of the broader Event 006 focus
audit, not this layout diagnostic handoff.

## Smallest safe remediation order

1. Preserve all Event 006 origin/package gates, focus IDs, prerequisites,
   mutual exclusions, rewards, and shared-focus roots. Do not “fix” these
   warnings by deleting a prerequisite or changing route semantics.
2. Resolve the 14 crossing blockers by moving only authored/relative layout
   endpoints, clustered in this order: `:280-297` revenue pair, `:319-336`
   regional-transport group, `:441-460` officer group, then `:501-524`
   professional-defense group. The MCP details show no movable endpoints, so
   this requires an explicit source layout adjustment or a reviewed compact
   rewrite, not an automatic assumption that prerequisites may change.
3. Re-run `hoi4.focus_inspect` and `hoi4.focus_render` against the same tree
   and verify the blocking count is zero while route gates remain unchanged.
4. Only after blockers are gone, optionally shorten the three long connectors
   and route the two through-node warnings. They are readability warnings, not
   parser or gameplay blockers.

## Validation and skipped checks

Meaningful validation run: `hoi4.focus_inspect` on the named source/tree,
including the returned artifact, diagnostic categories, source locations,
resolved title count, connector metrics, and source inventory count. Source
inspection confirmed the standalone IW-093/IW-098 shared-focus roots and the
main-tree seed references.

Skipped: no `hoi4.focus_rewrite` or source edit, per the read-only constraint;
no full focus-render raster review, icon-art review, localisation-auditor pass,
or route/reward/AI audit because those are outside this bounded diagnostic
task. No advisor or portrait assets were touched.

## Remaining risk

The MCP inline response does not print all 68 scanned paths. Any later review
that needs the complete inventory should use the linked artifact rather than
interpreting the 64-path inline list as the loaded-file set. The 14 blockers are
layout-only in this run. A source change that alters prerequisites, origin
flags, or shared-focus seed roots could create new gameplay blockers and must
be re-inspected separately.
