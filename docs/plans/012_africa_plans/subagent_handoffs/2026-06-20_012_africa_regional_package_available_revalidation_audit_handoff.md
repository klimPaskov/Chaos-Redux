# Event 012 Regional Package Available Revalidation Audit Handoff

Date: 2026-06-20
Scope: bounded active audit for the ten Event 012 regional authority package decisions. No gameplay files were edited because the requested `available = { FROM = { ... } }` revalidation blocks are already present.

## Changed Files

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-20_012_africa_regional_package_available_revalidation_audit_handoff.md`

No changes were made to:

- `common/decisions/012_africa_decisions.txt`
- `localisation/english/012_african_union_l_english.yml`

## Decision IDs Audited

- `africa_convene_wac_port_congress`
- `africa_open_sah_caravan_columns`
- `africa_secure_ioc_sea_lanes`
- `africa_reopen_mag_harbor_dockets`
- `africa_chart_nhr_highland_warrants`
- `africa_lock_eac_railway_timetable`
- `africa_muster_glk_lake_guards`
- `africa_arm_cbc_river_quartermasters`
- `africa_open_zsc_stone_city_yards`
- `africa_secure_slc_mine_port_belt`

## Issue List

### No open blocker: same-tick target revalidation is present

All ten package decisions already have an `available` block that scopes into `FROM` and repeats the target safety checks from the matching `target_trigger`: required authority tag, matching capstone flag, one-time package flag absence, and `can_africa_target_regional_package_action_for_root = yes`.

The previous audit's daily-refresh concern is therefore resolved in the current tree. `target_trigger` still controls target row creation, while `available` greys out or blocks the click if the target becomes unsafe before the next daily target refresh.

### No localisation issue found for scoped cost tooltips

The ten `africa_regional_package_*_cost_tt_tooltip` localisation keys are present in `localisation/english/012_african_union_l_english.yml`. No localisation patch was needed.

## Before And After Behavior

Before this audit: current gameplay files already had same-tick `available` revalidation for the ten package actions.

After this audit: gameplay behavior is unchanged. The handoff records that the ten actions are already guarded against stale daily target rows by a per-frame `available` check.

## Decision Category Lifecycle Notes

- Owner: Event 012 active runtime unifier.
- Category: `africa_charter_league_diplomacy_category`.
- Lifecycle gate: package actions require `is_africa_runtime_unifier = yes` and `africa_regional_authorities_open` in `target_root_trigger`.
- Target lifecycle: `global.africa_charter_member_countries` provides target rows; each decision narrows to one regional authority tag and a matching authority capstone flag.
- Completion lifecycle: each action is one-time per target through its package flag, and the `available` block repeats the same one-time flag absence check.

## Mission Quality Notes

These are immediate targeted package decisions, not timed missions. No success/failure mission branch is expected for this bounded package tranche.

| Decision | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `africa_convene_wac_port_congress` | Unifier | Charter diplomacy | WAC | WAC, Port Union capstone, package flag clear, target safety trigger | `days_re_enable = regional_authority_mandate` | Helper effect and report | None; click gated | Low |
| `africa_open_sah_caravan_columns` | Unifier | Charter diplomacy | SAH | SAH, Oasis Routes capstone, package flag clear, target safety trigger | Same | Helper effect and report | None; click gated | Low |
| `africa_secure_ioc_sea_lanes` | Unifier | Charter diplomacy | IOC | IOC, Monsoon Passages capstone, package flag clear, target safety trigger | Same | Helper effect and report | None; click gated | Low |
| `africa_reopen_mag_harbor_dockets` | Unifier | Charter diplomacy | MAG | MAG, Harbor Compact capstone, package flag clear, target safety trigger | Same | Helper effect and report | None; click gated | Low |
| `africa_chart_nhr_highland_warrants` | Unifier | Charter diplomacy | NHR | NHR, Highland Survey capstone, package flag clear, target safety trigger | Same | Helper effect and report | None; click gated | Low |
| `africa_lock_eac_railway_timetable` | Unifier | Charter diplomacy | EAC | EAC, Railway Board capstone, package flag clear, target safety trigger | Same | Helper effect and report | None; click gated | Low |
| `africa_muster_glk_lake_guards` | Unifier | Charter diplomacy | GLK | GLK, Lake Muster capstone, package flag clear, target safety trigger | Same | Helper effect and report | None; click gated | Low |
| `africa_arm_cbc_river_quartermasters` | Unifier | Charter diplomacy | CBC | CBC, River Quartermasters capstone, package flag clear, target safety trigger | Same | Helper effect and report | None; click gated | Low |
| `africa_open_zsc_stone_city_yards` | Unifier | Charter diplomacy | ZSC | ZSC, Stone-City Yards capstone, package flag clear, target safety trigger | Same | Helper effect and report | None; click gated | Low |
| `africa_secure_slc_mine_port_belt` | Unifier | Charter diplomacy | SLC | SLC, Mine-Port Liberation capstone, package flag clear, target safety trigger | Same | Helper effect and report | None; click gated | Low |

## Cost And Requirement Clarity Notes

- The scoped cost hover keys are present for WAC, SAH, IOC, MAG, NHR, EAC, GLK, CBC, ZSC, and SLC.
- The `available` checks do not add new player-facing text. They mirror target validity, so unavailable stale rows should present the existing target requirement context rather than exposing a new raw trigger surface.

## AI Validity And Route-Lock Notes

- AI target validity benefits from the same `available` revalidation as the player click path.
- No route-lock patch was made. The package actions still require the same target tags, capstone flags, and `can_africa_target_regional_package_action_for_root = yes` safety trigger.

## Localisation And Tooltip Gaps

No scoped localisation gap remains for the ten package cost `_tooltip` keys. Localisation was checked but not edited.

## Cleanup And Exploit-Risk Notes

- Same-day stale-target click risk is mitigated by existing `available` blocks.
- One-time package flags remain the repeat-click blocker.
- No cleanup or exploit-risk patch was made because the bounded concern is already covered.

## Validation

- `awk` check on `common/decisions/012_africa_decisions.txt` found all ten `available` blocks:
  - WAC line 799
  - SAH line 851
  - IOC line 905
  - MAG line 958
  - NHR line 1011
  - EAC line 1063
  - GLK line 1116
  - CBC line 1168
  - ZSC line 1221
  - SLC line 1274
- Targeted block scan confirmed each of the ten decision blocks contains `available = {`, `FROM = {`, and `target_trigger = {`.
- `rg` check confirmed all ten `africa_regional_package_*_cost_tt_tooltip` keys are present.
- `git diff --check -- common/decisions/012_africa_decisions.txt docs/plans/012_africa_plans/subagent_handoffs localisation/english/012_african_union_l_english.yml` returned no whitespace errors.

## Skipped Meaningful Validation

- No HOI4 runtime validation was run. This task was a static bounded audit/patch pass.
- No broader Event 012 decision balance audit was run because the request was limited to the ten regional package actions and their same-tick target revalidation.

## Remaining Issues And Recommended Fixes

No remaining issue was found inside the requested scope. No plan handoff was needed.

