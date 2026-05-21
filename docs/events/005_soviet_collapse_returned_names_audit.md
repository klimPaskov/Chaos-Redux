# Event 005 Returned Names Restoration Audit

Audit date: 2026-05-21

This audit covers the ancient and medieval restoration requirement from the final clean merged Part 6 specification. The current implementation uses dynamic host-country restoration packages rather than standalone new tags for the Khazar, Sogdian, Khwarazmian, and Alan claim lines. This is still a deviation from a literal one-tag-per-restoration package, but the gameplay surface now contains the shared restoration category, claim decisions, ideas, AI weights, effects, and asset wiring required for the Returned Names route.

## Shared Category Coverage

| Requirement | Source evidence | Status | Notes |
| --- | --- | --- | --- |
| Shared restoration category | `common/decisions/categories/005_soviet_collapse_categories.txt` defines `soviet_collapse_returned_names` with active-collapse, returned-name, and rejection gates. | implemented | The category appears only for countries whose high-chaos path activated `soviet_collapse_returned_names_claim_lines_active`. |
| Proclaim/open restoration debate | `soviet_collapse_open_museum_cabinets` in `common/decisions/005_soviet_collapse_decisions.txt`; effect `soviet_collapse_apply_returned_names_open_museum_cabinets`. | implemented | Opens old records, adds `soviet_collapse_returned_names_pressure`, raises recognition, and increases old-movement pressure. |
| Gather scholars and claim staff | `soviet_collapse_recruit_archivists`; effect `soviet_collapse_apply_returned_names_recruit_archivists`. | implemented | Adds `soviet_collapse_archivist_claim_council` and gates stronger claims. |
| Raise old banner | `soviet_collapse_commission_old_banner`; effect `soviet_collapse_apply_returned_names_commission_old_banner`. | implemented | Adds `soviet_collapse_old_banner_mobilization` and makes claim lines available. |
| Reject/contain restoration clubs | `soviet_collapse_reject_antiquarians`; effect `soviet_collapse_apply_returned_names_reject_antiquarians`. | implemented | Clears the active returned-name flags and removes the public-pressure ideas inside a hidden effect. |

## Claim-Line Rows

| Claim line | Eligible hosts | Decision and effect evidence | Status | Deviation or blocker |
| --- | --- | --- | --- | --- |
| Khazar toll and Lower Volga-Caspian claim | `IUL`, `OGB`, `TAT`, `BSK` | Trigger `can_argue_soviet_collapse_khazar_toll_claim`; decision `soviet_collapse_argue_khazar_toll_claim`; flag `soviet_collapse_khazar_toll_claim_asserted`; effect `soviet_collapse_apply_returned_names_claim_pressure`. | dynamic_host_implemented | No standalone Khazar tag, history file, flag set, or focus tree exists. |
| Sogdian city-network claim | `TNC`, `UZB`, `TAJ` | Trigger `can_argue_soviet_collapse_sogdian_city_claim`; decision `soviet_collapse_argue_sogdian_city_claim`; flag `soviet_collapse_sogdian_city_claim_asserted`; shared claim-pressure effect. | dynamic_host_implemented | No standalone Sogdian tag, history file, flag set, or focus tree exists. |
| Khwarazmian oasis claim | `BSC`, `TMS`, `UZB` | Trigger `can_argue_soviet_collapse_khwarazmian_oasis_claim`; decision `soviet_collapse_argue_khwarazmian_oasis_claim`; flag `soviet_collapse_khwarazmian_oasis_claim_asserted`; shared claim-pressure effect. | dynamic_host_implemented | No standalone Khwarazmian tag, history file, flag set, or focus tree exists. |
| Alan pass-defense claim | `MRC`, `GEO`, `ARM`, `AZR` | Trigger `can_argue_soviet_collapse_alan_pass_claim`; decision `soviet_collapse_argue_alan_pass_claim`; flag `soviet_collapse_alan_pass_claim_asserted`; shared claim-pressure effect. | dynamic_host_implemented | No standalone Alan tag, history file, flag set, or focus tree exists. |

## Asset And Localisation Evidence

| Surface | Evidence | Status |
| --- | --- | --- |
| Decision names/descriptions/tooltips | `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` contains names, descriptions, and custom effect tooltips for all Returned Names decisions. | implemented |
| Icons | `interface/005_soviet_collapse_factory_ancient_icons.gfx` wires stable category, decision, and idea sprite names for the Returned Names package. | wired_placeholder_reuse |
| Ideas | `common/ideas/005_soviet_collapse_ideas.txt` defines `soviet_collapse_returned_names_pressure`, `soviet_collapse_archivist_claim_council`, and `soviet_collapse_old_banner_mobilization`. | implemented |
| Achievement tracking | `common/achievements/chaos_redux_achievements.txt` checks `soviet_collapse_returned_names_claim_lines_active` for `chaosx_ach_returned_names`. | implemented |

## Remaining Deviation

The Returned Names system is now a playable dynamic-host restoration package, not only localisation and placeholder asset records. It still does not satisfy a literal standalone-country interpretation of the Part 6 ancient restoration requirement. If the final requirement is one independent tag per ancient restoration, the remaining work is to add tags, country/history files, flags, portraits, focus or decision content, release/spawn logic, AI, asset rows, and validation for each standalone restoration.
