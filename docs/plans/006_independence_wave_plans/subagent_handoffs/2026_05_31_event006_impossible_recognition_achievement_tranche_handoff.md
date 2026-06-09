# Event 006 Impossible Recognition Achievement Tranche Handoff

Date: 2026-05-31

## Scope

Implemented the first strange-state Event 006 achievement path without touching country flag assets, country definitions, or country history.

## Gameplay wiring

- Added `independence_wave_recognize_impossible_delegate` to the New States Congress decision set.
- Added `can_independence_wave_recognize_impossible_delegate` so only an independent Event 006 congress delegate can target another independent Event 006 release that is a strange package and has either revealed the strange file or completed containment.
- Added `independence_wave_recognize_impossible_delegate_effect`.
  - The acting country records `independence_wave_recognized_impossible_delegate`.
  - The target gains legitimacy and foreign attention.
  - The target records `chaosx_iw_impossible_recognized_by_iw_state` and `independence_wave_impossible_delegate_recognized`.
  - Both scopes refresh Event 006 achievement tracking.
- Added centralized tuning constants for the decision cost and recognition effects.

## Achievement wiring

- Added `cr_impossible_recognition`.
- The achievement requires:
  - clean independent Event 006 release origin
  - `chaosx_iw_strange_package`
  - another Event 006 country's Congress recognition flag
  - revealed or contained strange dossier state
  - no world-end bypass

## Localisation and assets

- Added decision localisation for the Congress recognition decision.
- Added achievement name, description, and tooltip localisation.
- Added `GFX_achievement_cr_impossible_recognition` sprite aliases.
- Added placeholder DDS trio:
  - `gfx/achievements/cr_impossible_recognition.dds`
  - `gfx/achievements/cr_impossible_recognition_grey.dds`
  - `gfx/achievements/cr_impossible_recognition_not_eligible.dds`
- Placeholder achievement art was copied from an existing custom achievement trio so the registered sprite names resolve. Final art direction remains: blank face on a passport stamp.

## Documentation

- Updated `docs/events/006_independence_wave.md` to describe the Congress recognition path, achievement tracking flag, and new achievement sprite.

## Validation

- Checked touched script/GFX files for balanced braces:
  - `common/script_constants/006_independence_wave_constants.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/decisions/006_independence_wave_decisions.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/achievements/chaos_redux_achievements.txt`
  - `interface/chaosx_achievements.gfx`
- Checked touched gameplay/localisation/docs files for unsupported less-than-or-equal or greater-than-or-equal operators; no matches.
- Checked localisation BOM and `:0` style:
  - `localisation/english/006_independence_wave_l_english.yml`: UTF-8 BOM present, no `:0` keys.
  - `localisation/english/chaosx_achievements_l_english.yml`: UTF-8 BOM present, no `:0` keys.
- Ran `git diff --check`; no whitespace errors.
- Checked `gfx/flags`, `common/countries`, and `history/countries`; no changes reported.
- Verified the new achievement placeholders are valid 64x64 DDS files.

## Remaining risks

- The achievement icon is placeholder art and still needs final production if/when achievement art is finalized.
- Broader Event 006 league-war and final-settlement achievements remain outside this tranche.
