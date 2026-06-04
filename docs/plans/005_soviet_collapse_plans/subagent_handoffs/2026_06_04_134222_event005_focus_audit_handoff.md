# Event005 Focus Audit Handoff - 2026-06-04 13:42:22 UTC

Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

Constraints followed:
- Used `hoi4-focus-trees`.
- Consulted the offline Paradox wiki core pages plus National focus modding, and vanilla documentation/examples before auditing focus files.
- Did not inspect or edit flag sprites or flag asset directories.
- Kept patches to narrow focus search-filter fixes only.

Changed files:
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_134222_event005_focus_audit_handoff.md`

Patched focus IDs:
- `FEV_harbor_fortress_line`: added `FOCUS_FILTER_INDUSTRY` and `FOCUS_FILTER_ANNEXATION`; the reward grants coastal buildings and expansion/conflict-plan helpers, not only army/navy value.
- `UWD_factory_militia_charter`: added `FOCUS_FILTER_INDUSTRY`; the reward builds forts and anti-air in addition to manpower/equipment/army XP.
- `kaz_soviet_collapse_army_of_the_open_horizon`: added `FOCUS_FILTER_INDUSTRY` and `FOCUS_FILTER_ANNEXATION`; the reward grants an airbase and breakaway neighbor conflict plan in addition to military rewards.
- `MFR_no_peace_without_orders`: added `FOCUS_FILTER_ARMY_XP` and `FOCUS_FILTER_ANNEXATION`; the reward grants artillery and creates neighbor annexation wargoals.

Mechanical audit summary:
- Focus blocks parsed: 1698.
- Missing `ai_will_do`: none found.
- Non-reciprocal `mutually_exclusive`: none found.
- Exact duplicate x/y positions in the current parse: none found.
- Worst visible reward spam still present: `FEV_harbor_fortress_line` remains a long visible reward list with convoy stockpile, five direct building construction lines, army XP, navy XP, and two helper effects. I patched filters only; the reward itself still needs a tooltip/helper cleanup pass.
- Repeated `add_ideas` or repeated same helper in one completion reward: none detected in the current mechanical pass.

Remaining layout/pathline risks:
- `ukr_soviet_collapse_purge_moscow_loyalists` <-> `ukr_soviet_collapse_re_register_the_party`: same-row mutex at y=11 with `ukr_soviet_collapse_black_soil_oath` between them, creating a likely mutex-line collision.
- `internal_soviet_collapse_security_council` <-> `internal_soviet_collapse_border_and_rail_liaisons`: same-row mutex at y=5 with `internal_soviet_collapse_legal_autonomy_congress` between them.
- Central Asia route fork: `central_asia_soviet_collapse_local_republic_council`, `central_asia_soviet_collapse_turkestan_federation_road`, `central_asia_soviet_collapse_military_border_authority`, and `central_asia_soviet_collapse_foreign_border_patronage` are all mutually exclusive on y=4 with other choices between endpoints.
- `moldova_soviet_collapse_conditional_union` <-> `moldova_soviet_collapse_reject_the_union_question`: same-row mutex at y=7 with `moldova_soviet_collapse_alliance_not_union` between them.
- CFR early committee fork: `CFR_elect_the_site_committees`, `CFR_publish_the_planners_charter`, `CFR_invite_the_foreign_contract_board`, and `CFR_the_concrete_committee` form same-row mutex spans across intervening focuses on y=6.
- CFR first build-priority fork: `CFR_cities_first`, `CFR_rails_first`, `CFR_factories_first`, and `CFR_contracts_first` form same-row mutex spans across intervening focuses on y=9.
- Vertical prerequisite line risks: `ukr_soviet_collapse_the_bread_line_becomes_a_border` -> `ukr_soviet_collapse_when_the_fields_refuse_the_state` crosses `ukr_soviet_collapse_minority_autonomy_statutes`; `moldova_soviet_collapse_moldova_route_fork` -> `moldova_soviet_collapse_river_guard_brigades` crosses `moldova_soviet_collapse_ukrainian_border_compact`; `blr_soviet_collapse_state_between_armies` -> `blr_soviet_collapse_join_the_league_when_war_comes` crosses `blr_soviet_collapse_orders_printed_like_timetables`.
- Same-row prerequisite risks remain in Ukraine, internal republic, Central Asia, Belarus, and Moldova branches. These are lower confidence than the explicit mutex spans but still should be reviewed in a layout pass.

Remaining reward/depth defects:
- The fallback breakaway tree still has many small direct rewards such as `soviet_collapse_assemble_emergency_government`, `soviet_collapse_depot_repair_crews`, `soviet_collapse_home_industry_contracts`, and `soviet_collapse_border_militia_standard`. These are functional but still read like generic emergency filler compared with the bespoke country routes.
- Several military focuses build forts, radar, AA, or airbases directly. Some filters were fixed here, but the larger issue is still visible clutter and weak mechanic identity where these should be wrapped in named helpers/tooltips or tied to decisions.
- Ancient restorations and factory successors are more coherent than the generic fallback, but still have focuses with direct building/equipment lists that should become route-specific scripted effects or custom tooltips in a larger pass.

Validation:
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_factory_successors.txt`: passed.
- Brace balance for touched focus files: all ended at `final_depth=0`, `min_depth=0`.
- Unsupported comparison operator search on touched focus files: no matches.
- `git status --short -- gfx/flags interface/flags`: no output; flag directories remained clean.

Notes:
- The worktree was already heavily dirty before this audit, including the Event005 focus files. I did not attempt broad rewrites or unrelated cleanup.
