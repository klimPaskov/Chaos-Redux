# Event 012 Africa Dossier Resistance Watch Parent Handoff

Date: 2026-06-18
Parent scope: Authority Atlas historical-dossier follow-up depth plus docs-subagent reconciliation integration.

## Summary

Added a one-at-a-time local resistance watch after historical dossier settlement. Observer settlements now leave a stored dossier/seat watch that can be calmed by keeping the seat secured while Regional Trust and League Cohesion meet their gates. Direct Archive settlements use the same stored context but require Authority and low Restoration Debt. Success and failure write visible per-dossier flags, move Event 012 values, and fire report events.

This implements a bounded tranche from the accepted foundation addendum: historical dossier settlement now has a visible local resistance/failure surface instead of ending at the observer/direct-Archive settlement button.

## Gameplay Files Changed

- `common/script_constants/012_africa_constants.txt`
  - Added resistance-watch value deltas, gates, and mission-day tuning constants.
- `common/decisions/012_africa_decisions.txt`
  - Added `africa_dossier_resistance_watch_mission`.
- `common/scripted_triggers/012_africa_triggers.txt`
  - Added `has_africa_dossier_resistance_watch_context`.
  - Added `controls_africa_archive_resistance_seat_state`.
  - Added `can_africa_complete_dossier_resistance_watch`.
- `common/scripted_effects/012_africa_effects.txt`
  - Stores settled dossier and seat state as `africa_archive_resistance_dossier_id` and `africa_archive_resistance_seat_state`.
  - Starts observer/direct Archive watch variants from the settlement effects.
  - Adds success/failure flag recording, outcome value movement, context cleanup, and reset integration.
  - Registers global gate variables for decision header/tooltips.
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
  - Added stored dossier name, stored seat name, settlement mode, and watch status resolvers.
- `events/012_african_union.txt`
  - Added `chaosx.nr12.49` and `chaosx.nr12.50` local report events.
- `localisation/english/012_african_union_l_english.yml`
  - Added mission, status, tooltip, and event localisation.
  - Updated the Authority Atlas header with Local Watch status.

## Documentation Files Changed

- `docs/events/012_africa_foundation.md`
  - Documented the new one-active local resistance watch.
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
  - Accepted docs-subagent reconciliation for the `BON`/`HYR`/`BIR`/`SAO` closure and root-terminal hybrid disposition.
- `docs/super_events/012_africa_super_event_research.md`
  - Marked the slot `72` text/image plus audio id `80` root-terminal split as intentional.
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_completion_audit_followup_handoff.md`
  - Removed stale active blockers for the four closed actor packages and root-terminal disposition.
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_root_terminal_super_event_text_handoff.md`
  - Added post-parent disposition note.
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_audio_root_terminal_resolution_handoff.md`
  - Added post-parent disposition note.
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_documentation_cleanup_handoff.md`
  - Docs-curator handoff for the reconciliation.

## Subagent Integration

Used `chaosx_documentation_curator` with `fork_context=false`.

Accepted its docs-only changes because they reconcile current implementation evidence without claiming Event 012 complete:

- Parent commit `9858db02` closes the specific `BON`/`HYR`/`BIR`/`SAO` actor-package, asset, and achievement queue.
- World Root terminal remains an intentional hybrid: shared slot `72` text/image and distinct audio id `80`; Archive remains distinct in slot `79`.

## Validation

Ran targeted checks on the touched Event 012 tranche:

- `git diff --check` on touched tracked files.
- Brace-balance pass on touched Clausewitz/scripted-localisation files.
- Unsupported comparison-operator scan on touched files.
- Localisation BOM check for `localisation/english/012_african_union_l_english.yml`.
- Targeted identifier scan for the new `dossier_resistance`, `archive_resistance`, scripted-localisation, and `chaosx.nr12.49`/`.50` surfaces.
- Focused diff review corrected one indentation issue and one duplicate reset call before staging.

## Remaining Blockers

Event 012 is still not full-spec complete. Remaining blockers are unchanged except where explicitly closed above:

- The 2026-06-16 foundation addendum still needs broader tranche disposition or implementation, especially package-specific dossier missions/forks and richer per-package AI.
- Targeted scenario validation is still missing for the required acceptance scenarios.
- UI/animation prompt proof remains unproven for the listed Authority Register, Omen Reliability, Forest Parliament, and related emblem/status surfaces.
- Broader country-package depth remains an acceptance issue beyond the now-closed `BON`/`HYR`/`BIR`/`SAO` actor tranche.
