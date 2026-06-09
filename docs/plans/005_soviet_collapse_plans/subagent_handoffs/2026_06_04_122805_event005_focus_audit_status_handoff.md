# Event005 Soviet Collapse Focus Audit Status Handoff

Date: 2026-06-04

Scope audited:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Related scripted effects inspected only to understand hidden focus reward helpers.

## Current Findings

- All parsed focuses in the four scoped files had `search_filters` and `ai_will_do`; no missing-filter or missing-AI cases were found in the mechanical pass.
- No direct `add_ideas`, `swap_ideas`, `modify_idea`, `remove_ideas`, or `add_timed_idea` spam was found inside the four focus files. Reward churn is mostly hidden behind scripted helper effects and repeated custom tooltips.
- Reward spam risk remains from repeated helper calls that produce similar visible reward themes: recognition/depot/military/league helpers, repeated small equipment grants, repeated single-state construction, and recurring factory/rail/supply-node rewards.
- Chaos and special successors are stronger than ordinary republic trees, but several shared custom splinter trees still rely on repeated 47-focus shapes and route tooltip families. They need parent-level identity passes, not small audit patches.
- Major layout risks still worth parent attention:
  - CFR has four-way mutually exclusive rows where other mutually exclusive alternatives sit between pair endpoints (`CFR_elect_the_site_committees` / `CFR_publish_the_planners_charter` / `CFR_invite_the_foreign_contract_board` / `CFR_the_concrete_committee`, and `CFR_cities_first` / `CFR_rails_first` / `CFR_factories_first` / `CFR_contracts_first`). This needs a small layout redesign, not a one-node nudge.
  - Ukraine still has broader likely crossing pressure around political, army, and diplomacy branches. I did not redesign it.

## Patches Made

Only coordinate changes were made. No prerequisites, rewards, flags, flag files, flag sprites, or interface flag files were edited.

Changed `common/national_focus/005_soviet_collapse_republics.txt`:
- `ukr_soviet_collapse_re_register_the_party`: moved to `x = 23`, `y = 11`
- `central_asia_soviet_collapse_negotiate_with_the_mountain_bands`: moved to `x = 4`, `y = 4`
- `moldova_soviet_collapse_ukrainian_border_compact`: moved to `x = 12`, `y = 3`
- `blr_soviet_collapse_railway_neutrality`: moved to `x = 13`, `y = 10`

Changed `common/national_focus/005_soviet_collapse_custom_splinters.txt`:
- `FTH_radical_turn`: moved to `x = 3`, `y = 7`
- `BSC_radical_turn`: moved to `x = 5`, `y = 7`
- `TNC_radical_turn`: moved to `x = 5`, `y = 7`
- `ALA_radical_turn`: moved to `x = 5`, `y = 7`
- `BBH_radical_turn`: moved to `x = 3`, `y = 7`
- `KRS_radical_turn`: moved to `x = 3`, `y = 7`
- `IUL_radical_turn`: moved to `x = 4`, `y = 7`
- `BAC_radical_turn`: moved to `x = 3`, `y = 7`

Changed `common/national_focus/005_soviet_collapse_factory_successors.txt`:
- `OGB_scholars_guard_the_charter`: moved to `x = 3`, `y = 3`
- `OGB_the_volga_cannot_have_two_seals`: moved to `x = 15`, `y = 4`

## Quick Validation

Before this handoff, quick validation passed:
- No duplicate focus coordinates in the four scoped focus files after the coordinate patch.
- No same-row mutually exclusive pairs closer than three grid units after the coordinate patch.
- Brace balance passed on touched focus files.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt` passed.

## Prioritized Parent Recommendations

1. Redesign CFR's two four-way mutually exclusive rows so alternatives occupy clear lanes without nodes sitting between mutually exclusive endpoints.
2. Continue replacing repeated stacked helper rewards with route-specific aggregate helpers where already available, especially in custom splinter and factory successor trees.
3. Give shared custom splinters stronger country-specific route payoffs and fewer generic repeat branches.
4. Audit Ukraine pathlines with a full branch layout pass; it still has likely crossings that are too broad for a safe subagent nudge.
5. Keep ancient restoration trees deliberately overpowered, but convert claim/equipment/factory dumps into more identity-specific end-state mechanics where parent scope permits.

## Notes

- I did not touch `gfx/flags` or `interface/flags`.
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt` was inspected but not patched by this tranche.
- The working tree already contained unrelated modifications and many untracked handoff files; this handoff only describes the coordinate patches above.
