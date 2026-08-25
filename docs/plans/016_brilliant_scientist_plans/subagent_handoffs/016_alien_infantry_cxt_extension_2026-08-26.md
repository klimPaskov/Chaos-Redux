# Event 016 Alien Infantry CXT extension handoff

## Scope

The CXT test-country contract requires every new special project, concrete equipment type, and land sub-unit to register through a package-owned hidden-idea carrier, idempotent `_apply` effect, bounded startup hook, and tag-scoped daily repair hook. Alien Infantry is scripted-only and must not become a normal recruitable unit.

## Changes

- Added `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt`.
- Added `common/ideas/016_alien_infantry_cxt_extension_ideas.txt`.
- Added `common/on_actions/016_alien_infantry_cxt_on_actions.txt`.
- Removed Alien Infantry from the static recruitable CXT roster.
- The package registers `alien_infantry`, `alien_laser_weapon_equipment_1`, and `sp_dhrondan_envoy_craft`.
- The package `_apply` effect creates one locked `CXT Test - Alien Landing Cohort` template with `force_allow_recruiting = no`, spawns three scripted divisions, and records the token as processed so the generic recruitable helper cannot duplicate it.
- Updated `docs/testing/chaosx_test_country.md` to describe the 87-template static baseline, the locked Event 016 exception, and the registration behavior.

## Validation and remaining risk

Brace balance and identifier scans were performed on the new script files. The HOI4 MCP remains the authoritative route for live parsing and CXT consumer validation; no game launch was performed. Existing CXT saves that were initialized before this extension may retain an older recruitable Alien Infantry template because the package does not destructively delete user-visible templates. New initialization and newly repaired saves receive only the locked package template.
