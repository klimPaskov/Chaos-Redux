# Event005 Soviet Collapse Focus Tree Cleanup Parent Tranche

Date: 2026-06-04
Owner: parent Codex agent

## Scope

This tranche targeted the current focus-tree complaints without touching flag sprites:

- remove shallow filler payoffs where the focus concept pointed to ports, rail, logistics, or foreign interaction instead
- make one shared republic tree lane split cleaner and less artificially mutually exclusive
- make the Far Eastern successor branch interact with Japan/Pacific liaison systems instead of raw one-off rewards
- remove the subagent-audited duplicate reward-helper chains that could display or apply the same rail/mobile payoff twice

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

The read-only subagent audit was written separately:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_174751_event005_focus_tree_rework_audit.md`

## Gameplay Changes

### Shared internal republic tree

The three early shared lanes now sit as parallel branch anchors instead of mutually exclusive route locks:

- `internal_soviet_collapse_legal_autonomy_congress`
- `internal_soviet_collapse_border_and_rail_liaisons`
- `internal_soviet_collapse_security_council`

The lanes now stage existing mechanics:

- legal autonomy exposes regional recognition goal text
- border/rail liaisons expose regional logistics goal text and add logistics plan progress
- security council creates league unit templates, unlocks league deployment decisions, and exposes regional defense goal text

### Far Eastern successor tree

Added `soviet_collapse_apply_fev_pacific_japanese_liaison`, used by:

- `FEV_pacific_observer_missions`
- `FEV_sakhalin_ferry_protocols`
- `FEV_pacific_city_compact`

This makes the branch provide fuel, convoys, recognition, liaison reach, Japan-facing opinion/intelligence behavior when Japan exists, and Soviet foreign/depot pressure.

Removed the shallow `FEV_settlement` / `FEV_radical_turn` mutual exclusion so those focuses stop adding route clutter where downstream focuses already gate by route completion.

### Copied custom splinter fork cleanup

Removed the same artificial settlement/radical lock from the copied `UDC` and `SDZ` fork blocks where downstream industry already accepts either route:

- `UDC_settlement`
- `UDC_radical_turn`
- `UDC_industry_plan`
- `SDZ_settlement`
- `SDZ_radical_turn`
- `SDZ_industry_plan`

### Duplicate helper spam cleanup

Removed redundant direct calls to `soviet_collapse_apply_focus_rail_authority_reward` or `soviet_collapse_apply_focus_mobile_columns_reward` from the subagent-audited duplicate chains where a broader plan helper already advances the same rail/mobile depth path in the same focus reward.

Representative cleaned ids:

- `soviet_collapse_rail_hub_or_mountain_pass`
- `internal_soviet_collapse_northern_timber_rail_fund`
- `internal_soviet_collapse_ural_cavalry_roads`
- `internal_soviet_collapse_ural_mobile_defense`
- `internal_soviet_collapse_tuvan_steppe_guard`
- `moldova_soviet_collapse_odessa_contact_posts`
- `moldova_soviet_collapse_smugglers_and_border_committees`
- `blr_soviet_collapse_depot_cars_without_labels`
- `kaz_soviet_collapse_the_army_that_crosses_distance`
- `kaz_soviet_collapse_turkmen_rail_and_desert_talks`
- `kaz_soviet_collapse_rail_guard_brigades`
- `PRA_coal_water_and_spare_parts`
- `FTH_doctrine`
- `BSC_doctrine`
- `TNC_doctrine`
- `TNC_economy`
- `UDC_doctrine`
- `UDC_signal_truck_yards`
- `NLC_doctrine`

## Validation

Passed:

- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_republics.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_174751_event005_focus_tree_rework_audit.md`
- unsupported operator scan for `<=` / `>=` in touched script/localisation files
- brace balance check on the three touched `.txt` script files
- duplicate focus-coordinate audit on the two touched focus files

## Remaining Gaps

This is not the full focus-tree rework. The subagent audit still lists broad unresolved design work:

- many 47-focus high-chaos custom splinter trees still need bespoke political, industry, and expansion lanes
- Ukraine still has specific line-crossing and branch-shape issues in the audit
- Belarus, Baltic, Moldova, Caucasus, and shared fallback trees still need deeper staged mechanics and expansion payoffs
- several remaining standalone rail/mobile helpers need a separate concept pass before removal, because they are not all duplicate chains

No flag sprites were edited by this tranche.
