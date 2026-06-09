# Event005 Parent Tranche: Focus Reward Visibility And Dynamic Release Gate

Timestamp: 2026-06-05 06:44 UTC

## Scope

Parent-owned bounded tranche for the active Soviet Collapse cleanup:

- reduce visible focus reward helper spam without changing route semantics
- add missing tooltip localisation for the cleaned focuses
- verify that non-base republic releases depend on crisis pressure and not chaos tier alone
- preserve the user's latest flag instruction by not touching `gfx/flags`

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `localisation/english/005_soviet_collapse_blr_focus_l_english.yml`
- `localisation/english/005_soviet_collapse_kaz_focus_l_english.yml`

## Reward Visibility Changes

Custom-splinter focuses now show one route-specific custom tooltip while their stacked generic mechanics run in `hidden_effect`:

- `FTH_war_plan`
- `DSC_dead_regiment_columns`
- `BSC_hidden_road_depots`
- `FEV_authority_from_the_harbor`
- `FEV_pacific_between_empires`
- `SZA_authority_from_the_railhead`

Belarus and Kazakhstan helper-stack hotspots received the same treatment:

- `blr_soviet_collapse_national_council_of_minsk`
- `blr_soviet_collapse_foreign_corridor_administration`
- `blr_soviet_collapse_council_bargains_with_forests`
- `blr_soviet_collapse_red_without_the_center`
- `blr_soviet_collapse_prepare_league_freight_tables`
- `blr_soviet_collapse_minsk_supplies_the_front`
- `kaz_soviet_collapse_league_cavalry_school`
- `kaz_soviet_collapse_mining_workers_councils`
- `kaz_soviet_collapse_planned_economy_without_center`
- `kaz_soviet_collapse_army_of_the_open_horizon`
- `kaz_soviet_collapse_the_steppe_outlives_the_union`

The visible generic helper-stack scan dropped from 27 flagged focuses to 16. The remaining flagged focuses are in Ukraine, internal republics, Central Asia, and Moldova.

## Release Gate Audit

The non-base release path is currently gated dynamically:

- internal republic candidates require `has_soviet_collapse_nonbase_republic_release_pressure = yes`
- dynamic union progressive candidates also require `has_soviet_collapse_nonbase_republic_release_pressure = yes`
- the follow-on backlog helper requires either non-base release pressure or severe component release pressure before it calls the dynamic follow-on release helper
- the dynamic follow-on helper zeros internal follow-on waves when non-base release pressure is absent
- the dynamic follow-on helper zeros generic follow-on waves when neither non-base release pressure nor severe component release pressure is present

`has_soviet_collapse_nonbase_republic_release_pressure` is not a chaos-tier-only gate. It is driven by real release pressure, release-level pressure, failed release months, regional cascade, war pressure, compound latent pressure, total collapse threat, urgency score, progressive release pressure, and failed-month roll pressure.

Chaos tier still widens the batch size and higher-tier candidate pressure, which is intentional. It should not by itself release non-base/internal republics without the above dynamic crisis pressure.

## Validation

Brace balance passed with zero early closes:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Unsupported operator scan:

- `rg -n "<=|>="` returned no hits in the audited Clausewitz files.

Whitespace check:

- `git diff --check` passed for the touched gameplay and localisation files.

## Remaining Work

- 16 visible generic helper-stack focuses remain in republic trees.
- Kazakhstan is still the worst remaining focus-layout hotspot according to the read-only focus audit.
- Broad focus depth/branch cleanup remains incomplete; this tranche did not redesign route structure.
- No flags were touched.
