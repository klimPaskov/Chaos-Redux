# Event 008 report value localisation patch, 2026-10-05

Disposition: implemented localisation patch, pending parent integration and review.
Acceptance basis: explicit parent assignment to preserve the stage and numeric packet captured before the root incident adds chaos.

## Changed source

`common/scripted_localisation/008_tensions_rising_scripted_localisation.txt` only.
The script retains its original plain UTF-8 encoding.
No YAML, event, effect, trigger, GUI or shared source was edited.

## Changed functions, keys and values

`GetTensionsRisingMainDesc`, `GetTensionsRisingOption`, and `GetTensionsRisingEffectText` select stage IV, III, II, I in descending order using `tensions_rising_report_stage` and the matching `constant:tensions_rising_event_log.stage_N`.
Each retains its baseline fallback.
All current-tier global flag checks were removed from these popup getters.
The 15 existing output keys remain unchanged: `chaosx.nr8.stage_N.d`, `chaosx.nr8.stage_N.a`, `chaosx.nr8.stage_N.effect` for N=1 through 4, plus `chaosx.nr8.baseline.d`, `.a` and `.effect`.

Every numeric branch copies normal variable `tensions_rising_report_world_tension` into temporary `tensions_rising_display_world_tension` inside its `text.trigger`.
The four evolved branches also copy normal variable `tensions_rising_report_chaos` into temporary `tensions_rising_display_chaos`.
The baseline branch copies only world tension.
Existing literal YAML output keys and their integer `|0` formatter are preserved.
These are direct assignments with no nested helper output lifetime dependency.

## Before and after

Before: each open popup consulted the current global chaos tier and selected freshly read tuning constants.
If the applied incident crossed a chaos-tier threshold, its displayed prose and numeric summary could describe the next stage.
After: all three getters consume the stage and packet stored for that report, so a later tier change does not affect its description, option or summary.
No gameplay effect or player-facing prose was changed by this follow-up.

## Validation and limitations

Task-specific source checks found twelve stored-stage conditions, five stored world-tension copies, four stored chaos copies, and no current-tier selection in the three getters.
All fifteen output localisation keys remain resolved in the existing YAML.
No colour or number formatter was changed.
No quotation occurs in the touched script.

The parent owns storing `tensions_rising_report_stage`, `tensions_rising_report_world_tension`, and `tensions_rising_report_chaos` before chaos changes, and clearing these normal variables when the root option is acknowledged.
Those writes were not present at the start of this follow-up and are a required integration dependency.
Concurrent open reports on the same recipient share these normal variable names, so this change alone does not establish distinct per-popup storage for overlapping incidents.

MCP event inspection and reference routes previously returned `MCP tool ... is not available to the model`, and the advertised event render route was not callable.
The source review does not establish runtime rendering or branch execution.
No artifact URI was produced.
Parent must carry that unresolved validation limit.

## References and skill guidance

Applied `.agents/skills/chaos-redux-events/SKILL.md`, lines 162-164: numeric `defined_text` uses a literal real YAML key and assigns temporary display variables in the same text trigger.
Previously read offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, lines 656-691, documents first-matching scripted output and temporary trigger assignments remaining visible to the chosen key.
Previously read installed `documentation/effects_documentation.md`, lines 7820-7844, documents `set_temp_variable` accepting another variable.
The previous localisation audit handoff retains reference hashes and full source paths.
No skill changed, staging or commit performed.
