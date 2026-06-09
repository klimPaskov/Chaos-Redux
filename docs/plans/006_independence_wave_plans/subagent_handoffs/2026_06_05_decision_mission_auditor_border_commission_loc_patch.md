# Event006 Decision/Mission Auditor Handoff: Border Commission and Tooltip Patch

Date: 2026-06-05
Agent role: `chaosx_decision_mission_auditor`
Scope: Event006 decision-category gameplay only.

## Files changed

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_decision_mission_auditor_border_commission_loc_patch.md`

No focus trees, country files, assets, audio, super-events, spreadsheets, or Event005 files were edited.

## Gameplay surface changed

### Border Commission generic access

Changed trigger:

- `can_independence_wave_open_border_commission`

Before:

- The Border Commission opened only for Event006 releases with one of these route or focus flags:
  - `independence_wave_route_national_directorate`
  - `independence_wave_route_officer_mandate`
  - `independence_wave_route_civic_mandate`
  - `independence_wave_focus_border_office`
  - `independence_wave_focus_arbitration_files`

After:

- Any independent country with `chaosx_release_origin_independence_wave` can open the Border Commission.
- Subject releases are still blocked with `is_subject = no`.
- State-targeted border actions still require `independence_wave_border_survey_filed`, no active `independence_wave_border_commission_cooldown`, and valid target-state triggers.

Why this is safe and bounded:

- It implements the current correction that the Border Commission should provide generic expansion for every released republic.
- It does not add new decision families, new tags, new package routes, focus changes, or Event005 coupling.
- Existing target triggers still prevent protected host-state grabs, capital grabs, already-owned states, already-claimed states, and host deletion through the owner state-count gate.

### Missing effect tooltip localisation

Added localisation for 53 decision `custom_effect_tooltip` keys that were referenced by `common/decisions/006_independence_wave_decisions.txt` but unresolved in the audited localisation files.

Affected key families:

- Volga/Kama ministry effect tooltip
- Assyrian recognition congress effect tooltip
- Danzig free-city board effect tooltip
- Buganda, Sokoto, Bukhara, Khiva, Mesopotamia, Don, Dahomey, Barotse, Miskito, Itza, Maya, Guarani, Charrua, Kurdish, Circassian, Andean, Nahua, Inuit, Namibia, Bechuanaland, Ghana, Eritrea, Darfur, and Zulu open/map/register/review effect tooltips
- Railway authority junction and bridge-guard effect tooltips

Before:

- Those decisions would show raw localisation keys in player-facing effect text.

After:

- Every referenced decision tooltip key in `006_independence_wave_decisions.txt` resolves against `006_independence_wave_l_english.yml` or `chaosx_gui_l_english.yml`.

## Validation run

- Brace validation on:
  - `common/decisions/006_independence_wave_decisions.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
  - `common/scripted_guis/006_independence_wave_scripted_guis.txt`
- Result: all checked files ended at brace depth `0`, with no early closes and no unterminated strings.
- BOM validation on:
  - `localisation/english/006_independence_wave_l_english.yml`
  - `localisation/english/chaosx_gui_l_english.yml`
- Result: both files still have UTF-8 BOM.
- Localisation reference audit:
  - Parsed decision ids, descriptions, `tooltip =`, `custom_cost_text =`, and `custom_effect_tooltip =` references from `006_independence_wave_decisions.txt`.
  - Result after patch: `missing referenced decision loc 0`.
- Duplicate localisation key audit on `006_independence_wave_l_english.yml`.
  - Result: `duplicate_keys 0`.
- Unsupported operator scan on touched script/localisation surfaces:
  - `rg -n "<=|>=|:0\\s+\\\"" common/scripted_triggers/006_independence_wave_triggers.txt localisation/english/006_independence_wave_l_english.yml`
  - Result: no matches.
- AI block scan:
  - No AI-usable clickable decision in `006_independence_wave_decisions.txt` was found missing `ai_will_do`.

## Skipped validation

- No in-game validation was run. The user will verify in a live session.
- No commit was created because the worktree already contained large unrelated modified and untracked Event005/Event006 changes, including untracked Event006 gameplay files. Staging a commit would risk including prior work outside this subagent patch.

## Remaining risks and design gaps

- Broad package-route and formable depth remain outside this audit. The patch only fixes generic Border Commission availability and missing tooltip keys.
- The Border Commission now appears for all independent Event006-origin releases, but countries with no valid external core states will still have no valid state-targeted expansion actions after filing a survey. That is expected from current target-state gates.
- Several older KUB/ALT records remain in historical handoffs and possibly parser-stability remnants, but the audited current trigger gate excludes `KUB` and `ALT` from candidate tag use. No KUB/ALT expansion was added.
- Event006 completion remains incomplete; this handoff is not a final completion claim.

## Skills used

- `hoi4-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-subagents`
