# Event006 Reduced-Start Army and Expansion Patch

Date: 2026-06-05
Owner: parent Codex agent

## Change

Patched `common/scripted_effects/006_independence_wave_effects.txt`, `common/script_constants/006_independence_wave_constants.txt`, and `docs/events/006_independence_wave.md`.

- Reduced-footprint releases now receive `independence_wave_border_survey_filed` when masked cores are restored, so their Border Commission recovery decisions are immediately available against unowned core states.
- The local defense brigade decision now creates one actual `Local Defense Brigade` division at the released country's capital using the shared `Independence Wave Provisional Guard` template.
- Added the file-scoped `@independence_wave_local_defense_brigade_divisions` count because `create_unit` count fields are stricter than normal variable-capable effect fields.
- Documented that reduced-footprint releases use the Border Commission as their recovery route.

## Existing Coverage Confirmed

The generic Event006 release setup already gives each released country:

- Event006 origin and aftermath flags.
- The shared `independence_wave_liberation_provisional_tree`.
- Startup manpower, infantry equipment, and support equipment.
- The shared provisional guard division template.
- Two starting `Provisional Guard` divisions.
- One arms factory in an owned controlled core state when a valid state exists.

## Validation

Passed parent validation:

- Scoped brace-balance checks returned zero for touched Event006 script files, localisation, docs, and handoffs.
- Unsupported less-equal/greater-equal operator scan returned clean for touched Event006 script/localisation/doc files.
- UTF-8 BOM checks passed for touched localisation files.
- Localisation version-key scan found no `:0` keys in touched localisation files.
- Scoped `git diff --check` passed.
- No fresh `error.log` was present in `tmp/hoi4-error-logs`; only the old May 29 watchdog log remained.

## Remaining Scope

This does not complete Event006. It closes the immediate playability gap for reduced one-state starts and follow-up army creation, but full package/formable depth, final catalog parity, and final completion audit remain separate.
