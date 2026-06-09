# Event006 Border Expansion Wrap-Up

Date: 2026-06-05

Parent scope: urgent Event006 playability fixes after the user correction that released countries need starting forces and a way to grow beyond one-state starts.

## Changed Files

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md`

## Behavior

- Split the Border Commission target checks into owner-valid, claimable, and contested states.
- `independence_wave_petition_border_parish` can now file claims on unowned non-capital cores or adjacent border states, so one-state Event006 releases can open a generic expansion path even when they do not have a wide restored-core map.
- Arbitration, protected transfer, observer freeze, surveyed-core recovery, and ultimatum checks can now target contested states that are either ROOT cores or ROOT claims.
- `independence_wave_issue_dossier_ultimatum` now transfers the contested state and adds a core, making the hardline border route a real expansion tool instead of a claim-only dead end.
- Localisation and docs now describe the claim-to-settlement loop.
- Event-log display wording for Independence Wave non-tier route records now says `Route Record` instead of `History Row`. Active Event006 evolution writing remains limited to the chaos-tier milestone writer.

## Existing Playability Confirmed

- `independence_wave_setup_released_country` already gives runtime Event006 releases startup manpower, infantry equipment, support equipment, an unlocked `Independence Wave Provisional Guard` template, two starting capital divisions, one arms factory in a controlled core, the provisional committee idea, and the shared Liberation Provisional Tree.
- The shared focus tree already includes army, industry, diplomacy, border, congress, patron, crisis, and package lanes.

## Validation

- Brace-count check was clean on touched script, localisation, and docs.
- The unsupported inequality-operator scan over Event006 effects, triggers, decisions, and focus files returned no hits.
- `localisation/english/006_independence_wave_l_english.yml` still has a UTF-8 BOM and no duplicate keys.
- `git diff --check` was clean for the touched files.
- `tmp/hoi4-error-logs` did not contain a current `error.log`; only the old `watchdog.log` was present.

## Remaining Risks

- No live in-game validation was run for AI selection, state-target visibility, or border-transfer balance.
- The completion auditor report `2026_06_05_182317_event006_completion_audit_current_state.md` still classifies Event006 as incomplete/weak-needs-validation overall, mainly because full game-load validation, Event005 cross-system proof, workbook parity, MAP flag parity, and queued plan closure remain open.
