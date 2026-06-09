# Event006 Create Unit Count Parser Safety

Date: 2026-06-05
Owner: parent Codex agent

## Change

Patched `common/scripted_effects/006_independence_wave_effects.txt`, `common/script_constants/006_independence_wave_constants.txt`, and the reduced-start army handoff.

- Moved the startup guard and local defense brigade `create_unit` counts to file-scoped constants in `006_independence_wave_effects.txt`.
- Replaced `count = constant:independence_wave_startup.*` inside `create_unit` with `count = @independence_wave_*_divisions`.
- Removed the now-unused global script constants for those two counts to avoid duplicate tuning sources.

## Reason

Vanilla precedent consistently uses literals or file constants for ordinary `create_unit` count fields, while Event005 only injects dynamic counts through `meta_effect`. This patch preserves Event006's starting army behavior while avoiding a likely parser issue in the release setup and local defense brigade decision.

## Validation

Passed parent validation:

- Scoped brace-balance checks returned zero for the touched Event006 script files and handoffs.
- Unsupported less-equal/greater-equal operator scan returned clean for the touched files.
- Trailing-whitespace and CRLF checks returned clean for the touched files.
- Follow-up reference scan found no remaining `count = constant:` usage in Event006 release-unit code.

## Remaining Scope

This is a parser-safety fix only. It does not complete the wider Event006 country package, final audit, asset, or balance scope.
