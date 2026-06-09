# Event006 Generic Release Playability Fix Handoff

## Scope

Parent patch for the urgent Independence Wave playability follow-up on 2026-06-05.

## Changed Files

- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md`

## Behavior

- The Independence Wave news event uses `GetIndependenceWaveReleasedCountryList` so `chaosx.news.6` can list every current-wave release slot from 1 through 16.
- The shared `independence_wave_liberation_provisional_tree` no longer contains hardcoded package-specific focus stacks gated by `is_independence_wave_*_package = yes`.
- Every released Event006 country receives an unlocked `Independence Wave Provisional Guard` infantry template, two starting guard divisions, startup manpower and equipment, and one emergency arms factory in a controlled core state.
- Border Commission arbitration and protected-transfer decisions now transfer the valid contested core state to the released country. Parish claims and dossier ultimatums remain claim/escalation tools.

## Validation To Re-run

- Brace balance on touched script files.
- UTF-8 BOM on touched English localisation.
- Focus prerequisite/reference audit after focus-row removals.
- Targeted search that no package-specific focus gates remain in `common/national_focus/006_independence_wave_focus.txt`.
- Error-log check after user live reload.

## Remaining Risks

- This pass intentionally keeps package-specific decisions, missions, ideas, and scripted effects outside the focus tree. Those surfaces are still part of package gameplay unless a later request removes or redesigns them.
- No live HOI4 session validation was run by the parent patch.
