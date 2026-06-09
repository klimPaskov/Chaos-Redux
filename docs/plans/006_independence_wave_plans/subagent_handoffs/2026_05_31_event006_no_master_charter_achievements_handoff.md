# Event 006 No-Master and Charter Achievement Tranche Handoff

Date: 2026-05-31

## Scope

Implemented two additional Event 006 achievements using existing Independence Wave recognition, patron, puppet, compact, and League tracking. No country flag assets, country definitions, country history, or Event 005 files were edited.

## Gameplay and achievement wiring

- Added `cr_independence_without_patron`.
  - Requires clean independent Event 006 origin.
  - Requires `independence_wave_recognition_secured`.
  - Rejects patron-accepted tracking and major cabinet-seat concessions.
- Added `cr_charter_not_chains`.
  - Requires clean independent Event 006 origin.
  - Requires the compact founder path, regional compact formation, anti-puppet clause, and the League member count threshold.
  - Uses new `chaosx_iw_charter_not_chains` proof from compact formation.
- Added `independence_wave_mark_charter_not_chains_if_clean`.
  - Runs during `independence_wave_form_regional_compact`.
  - Checks the anti-puppet clause.
  - Iterates `global.independence_wave_compact_members`.
  - Rejects missing, non-Event-006, non-member, subject, or puppet-ever members.
  - Marks the compact founder only when all checked founding members remain clean.

## Localisation and assets

- Added achievement name, description, and tooltip localisation for:
  - `cr_independence_without_patron`
  - `cr_charter_not_chains`
- Added sprite aliases:
  - `GFX_achievement_cr_independence_without_patron`
  - `GFX_achievement_cr_charter_not_chains`
- Added placeholder DDS trios:
  - `gfx/achievements/cr_independence_without_patron.dds`
  - `gfx/achievements/cr_independence_without_patron_grey.dds`
  - `gfx/achievements/cr_independence_without_patron_not_eligible.dds`
  - `gfx/achievements/cr_charter_not_chains.dds`
  - `gfx/achievements/cr_charter_not_chains_grey.dds`
  - `gfx/achievements/cr_charter_not_chains_not_eligible.dds`
- Placeholder achievement art was copied from existing Event 006 achievement trios so registered sprite names resolve. Final custom achievement art remains a later asset task.

## Documentation

- Updated `docs/events/006_independence_wave.md` to list the new achievements, the compact clean-charter proof flag, and the new achievement sprite names.

## Validation

Validation performed by the parent after this handoff:

- Brace balance on touched script/GFX files.
- Unsupported less-than-or-equal and greater-than-or-equal operator scan on touched files.
- Localisation BOM and no `:0` keys for touched localisation.
- `git diff --check`.
- `gfx/flags`, `common/countries`, and `history/countries` status check.
- DDS file type sanity check for the new placeholder assets.

## Remaining risks

- Achievement icons are placeholders, not final custom art.
- `cr_five_small_flags`, `cr_suppression_failed`, `cr_old_name_modern_state`, `cr_league_war_victory`, `cr_human_renunciation`, and the final settlement achievement remain outside this tranche.
- The previous Event 006 improvement addendum still needs explicit disposition before another improvement-loop planner should be spawned.
