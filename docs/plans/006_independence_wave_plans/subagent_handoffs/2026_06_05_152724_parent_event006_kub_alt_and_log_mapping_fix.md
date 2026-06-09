# Event 006 KUB/ALT Cutback and Log Mapping Fix

## Scope

Parent-side patch for the 2026-06-05 user correction:

- Stop treating Kuban (`KUB`) and Altai (`ALT`) as current Event 006 package-expansion scope.
- Keep the accepted new-country lane focused on niche generic releases such as `ASN`, `KBN`, `PLM`, and `AYM` using `independence_wave_liberation_provisional_tree`.
- Repair Event 006 event-log type-name mappings so newer formation/package entries display consistently in current, history, event-detail, and selected-detail log views.

## Files Changed

- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- Documentation was reconciled separately by `chaosx_documentation_curator` in `2026_06_05_152010_documentation_curator_kub_alt_correction.md`.

## Gameplay Changes

- Removed KUB and ALT special reduced-release anchor selection from the Event 006 reduced-release path.
- Removed KUB and ALT injection into the Event 006 high-chaos package candidate pool.
- Removed KUB and ALT package promotion inside `independence_wave_score_candidate_package_type`, so they no longer receive:
  - `independence_wave_package_kuban` / `independence_wave_package_altai`
  - historical-return package identity
  - KUB/ALT formable-family variables
  - KUB/ALT startup package spirits
- Removed KUB/ALT seed-gate exceptions from `can_independence_wave_use_candidate_tag`.

Existing unused KUB/ALT helper definitions and constants remain in place for parser stability and future explicit reuse, but there is no current Event 006 seeding or package-scoring path that activates them.

## Log Mapping Changes

Added missing Event 006 type-name mappings for these formation/package constants across:

- `GetEventsLogEvolutionTypeView`
- `GetEventsLogSelectedHistoryEvolutionTypeView`
- `GetEventsLogEventDetailEvolutionTypeView`
- Existing selected-detail mappings were already present and were used as the parity source.

Constants covered:

- `namibia_land_council_formation_type`
- `bechuanaland_kgotla_council_formation_type`
- `ghana_legislative_council_formation_type`
- `eritrea_red_sea_council_formation_type`
- `darfur_council_formation_type`
- `zulu_council_formation_type`
- `namibia_land_records_package_type`
- `bechuanaland_kgotla_records_package_type`
- `ghana_gold_coast_records_package_type`
- `eritrea_red_sea_records_package_type`
- `darfur_records_package_type`
- `zulu_records_package_type`

This does not add evolution records. It only fixes display names for entries already recorded or selected by the shared log UI.

## Validation

- Brace balance and trailing-whitespace check passed for:
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- Event 006 newer type mapping parity check passed for current, history-detail, event-detail, and selected-detail log views.
- Documentation curator grep validation confirmed KUB/ALT are no longer current Event 006 package source-of-truth.

## Remaining Risks

- The repo worktree is still heavily dirty and several Event 006 files are untracked, so no scoped commit was made.
- KUB/ALT unused helper definitions remain for stability; a later cleanup pass can remove them only after checking all focus, decision, localisation, constants, and log references together.
- No new `error.log` was present under `tmp/hoi4-error-logs`; the fix used local script evidence and reported in-game behavior.
