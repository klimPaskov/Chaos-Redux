# Event006 Event-Log Wording Cleanup

Date: 2026-06-05
Owner: parent Codex agent

## Change

Patched player-facing Event006 event-log labels in `localisation/english/chaosx_gui_l_english.yml`.

The Event006 compatibility labels that can be resolved through the shared event-log detail system no longer display as `Independence Dossier`, `Independence Formation`, or `Independence Package` entries in a way that implies they are true evolution stages. They now display as `Independence History` dossier, formation, or package-file rows.

The four true Event006 evolution milestones remain:

- Gathering Storm Release Pattern
- Rising Cascade Release Pattern
- Old Names Release Pattern
- Impossible Statehood Release Pattern

Also patched `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md` so the relevant heading is `Formation and package history rules`, not package evolution rules.

## Gameplay Contract

No gameplay logging was changed. Event006 still records actual evolutions only through `independence_wave_record_tier_evolution_log_entry`, which contains four `record_events_log_evolution_entry = yes` calls for the chaos-tier escalation milestones.

Package files, formation proofs, and release dossiers remain route/history/detail state. They must not become per-release, per-package, or per-formable evolution spam.

## Validation

Passed parent validation:

- `localisation/english/chaosx_gui_l_english.yml` keeps UTF-8 BOM
- scoped brace-balance checks returned `0`
- unsupported less-equal/greater-equal operator scan found no invalid script tokens
- localisation `:0` scan found no versioned keys in the scoped files
- scoped `git diff --check` returned clean
- Event006 stale wording scan no longer finds player-facing `Independence Dossier:`, `Independence Formation:`, or `Independence Package:` labels

## Remaining Scope

This is a wording and source-spec cleanup only. Full Event006 completion still needs package/formable scope closure, achievement reachability review, final catalog/spreadsheet parity, and the final completion audit.
