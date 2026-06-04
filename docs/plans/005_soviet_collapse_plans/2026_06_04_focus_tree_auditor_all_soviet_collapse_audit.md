# Event005 Soviet Collapse Focus Tree Audit

Date: 2026-06-04
Role: chaosx_focus_tree_auditor
Scope: `common/national_focus/005_soviet_collapse_republics.txt`, `005_soviet_collapse_custom_splinters.txt`, `005_soviet_collapse_factory_successors.txt`, `005_soviet_collapse_ancient_restorations.txt`

No focus-file patches were made. The defects found are broad route/layout/reward-depth issues, not isolated one-line fixes.

## Audit Counts

- Focus trees audited: 41.
- Direct focus blocks audited: 1,698.
- By file: republics 9 trees / 501 focuses; custom splinters 25 trees / 1,005 focuses; factory successors 3 trees / 128 focuses; ancient restorations 4 trees / 64 focuses.
- Direct multi-idea `add_ideas` stacks in focus rewards: 0 found.
- Repeated visible direct reward operations excluding marker-only state: 20 focuses.
- Mechanically shallow or helper-only reward candidates: 1,054 focuses. This is intentionally broad and includes false positives where the helper is deep, but it marks the remaining manual review surface.
- Duplicate absolute coordinates: 82 coordinate groups.
- Focuses at one-step horizontal/vertical spacing: 678 pairs.
- Continuous focus panel overlap candidates: 0.
- Missing prerequisite targets: 0.
- Mutual-exclusion asymmetry: 0.
- Isolated direct focus nodes: 0.
- Missing or empty `search_filters`: 0.
- Missing `ai_will_do`: 0.
- Simple baseline AI blocks with no route/state modifiers: 351 focuses.

## Top Concrete Findings

1. `soviet_collapse_breakaway_focus_tree` has severe duplicate-coordinate collapse: `soviet_collapse_assemble_emergency_government`, `soviet_collapse_old_underground_branch`, and `soviet_collapse_rail_hub_or_mountain_pass` all resolve to `(14,0)` at lines 2157, 2603, 2775.
2. `soviet_collapse_breakaway_focus_tree` repeats this across most of the tree: examples include `(18,0)` at lines 2171, 2451, 2711; `(22,0)` at lines 2186, 2216; `(6,0)` at lines 2260, 2380, 2496.
3. Ukraine has dense crossing/too-close risk around the early fork and foreign/military branches: examples include `ukr_soviet_collapse_war_without_a_declaration` and `ukr_soviet_collapse_open_the_liaison_offices` at adjacent positions `(25,4)` and `(25,5)`, lines 147 and 190.
4. Ukraine route paths interleave around `ukr_soviet_collapse_the_commander_or_the_cabinet`, `ukr_soviet_collapse_army_supremacy`, and `ukr_soviet_collapse_mixed_emergency_cabinet` at lines 568, 593, 621; the fork is functional but visually compact.
5. `ukr_soviet_collapse_league_founding_charter` at line 1376 has a large visible reward stack with several unlock/tooling effects plus formation logic. It should be compressed behind one clear route tooltip or moved into a documented helper.
6. `ukr_soviet_collapse_league_of_equals` at line 1415 and `ukr_soviet_collapse_border_states_accept_kyiv` at line 1664 have similar visible reward density and should be reviewed with the League decision category open.
7. `ukr_soviet_collapse_external_border_arbitration` at line 1692 is another League/expansion reward stack that risks noisy completion tooltips.
8. Belarus is better connected than earlier audits, but the rail route still has shallow-feeling early payoffs: `blr_soviet_collapse_the_rail_map_on_the_wall` line 8556 and `blr_soviet_collapse_timetable_state` line 9038 rely on helper payloads with simple AI.
9. Belarus rail finishers are functional but under-differentiated: `blr_soviet_collapse_railway_neutrality` line 9135 and `blr_soviet_collapse_rail_war_state` line 9156 need stronger divergent decisions, postwar handling, or route-specific AI strategy.
10. `CFR_soviet_collapse_focus_tree` has major coordinate collapse. `CFR_count_the_cranes`, `CFR_the_trust_office_takes_the_seal`, `CFR_ration_cards_for_workers`, `CFR_emergency_cement_accounts`, and `CFR_the_unfinished_city_speaks` all resolve to `(17,0)`, lines 22, 40, 61, 80, 100.
11. `CFR_rails_first` line 383 and `CFR_build_the_border_bend_the_border` line 923 both resolve to `(12,0)`, turning an important construction/railway route into layout overlap.
12. `CFR_the_plan_is_the_law` line 1004 resolves to the same `(17,0)` cluster as the opening trunk. This makes the construction tree unreadable even if the rewards are mechanically stronger.
13. `OGB_soviet_collapse_focus_tree` has coordinate collapse across each lane: opening/restoration nodes at `(6,0)`, trade nodes at `(0,0)`, guard nodes at `(8,0)`, and Volga compact nodes at `(12,0)`. Example lines: 1105, 1124, 1144, 1207, 1239, 1262, 1348, 1372, 1394, 1412, 1490, 1569.
14. `OGB_future_bulgaria_file` line 1569 has the right identity direction but needs a stronger bridge into decisions or end-state resolution before the final restoration payoff.
15. `MFR_soviet_collapse_focus_tree` also has broad coordinate collapse: the opening chain at `(15,0)` covers lines 1670, 1688, 1708, 1727, 1746, 1765, 2216, 2546, 2823, 2854.
16. `MFR_eternal_arsenal_marches` line 2995 is appropriately aggressive but repeats multiple AI strategy effects and should be consolidated behind a helper or route payoff effect.
17. `FEV_war_plan` line 16698 has visible repeated building rewards and generic security payoff; it needs a more distinctive Far Eastern war mechanic or decision hook.
18. `FEV_harbor_fortress_line` line 16617 has a large building payload hidden behind a tooltip. The tooltip approach is better, but the branch still reads as construction spam without a clearer port/fortress mechanic.
19. `NRF_fleet_that_does_not_dock` line 3688 and `NRF_northern_revenant_fleet` line 3774 are strong identity beats, but the mid-branch between them is still mostly resources, claims, and generic pressure; add a unique naval mission loop or fleet-raising decision chain.
20. Ancient restorations are too shallow overall. `KZR_khazar_charter` line 281, `SOG_sogdian_city_charter` line 690, `KHW_khwarazmian_water_charter` line 1089, and `ALN_expansionist_mountain_claims` line 1451 have oversized direct variable/claim batches without enough playable systems around them.

## Parent Priorities

1. Fix layout first for `CFR`, `OGB`, `MFR`, and the generic breakaway tree. These are not small coordinate nits; whole trees resolve into horizontal stacks and need a parent-owned layout tranche.
2. Give Ukraine and Belarus a pathline cleanup pass focused on branch spacing, especially Ukraine's early fork/League/foreign paths and Belarus rail route finishers.
3. Consolidate the 20 repeated direct reward-operation focuses into scripted effects or hidden payloads with one clear tooltip each.
4. Deepen construction, railway, ancient restoration, FEV, NRF, and OGB route payoffs with decisions, postwar handling, unit/template hooks, or crisis systems.
5. Replace simple baseline AI on high-impact route focuses with route-aware modifiers. Prioritize the 219 simple AI blocks in republic trees and the 48 simple AI blocks in ancient restorations.
6. Leave filters mostly as a cleanup pass after reward/depth work. Coverage exists everywhere; the issue is overbroad or generic tagging rather than missing filters.

## Validation Notes

- Mechanical parser confirmed all direct focus blocks are inside focus trees.
- No missing prerequisite targets, mutual-exclusion asymmetry, isolated nodes, missing filters, or missing `ai_will_do` blocks were found in the audited files.
- No local focus patches were made because the actionable issues are broad and design-owned.
