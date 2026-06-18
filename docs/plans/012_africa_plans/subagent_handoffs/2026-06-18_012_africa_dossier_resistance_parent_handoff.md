# 2026-06-18 Event 012 Africa Dossier Resistance Parent Handoff

## Scope

Implemented the Authority Atlas local-resistance tranche for historical dossiers after the earlier dossier-settlement tranche.

## Subagents

- `019edba6-c45b-7cc0-956e-67520d31095c` (`chaosx_scripted_system_architect`, `fork_context=false`) wrote `2026-06-18_012_africa_dossier_resistance_helpers.md` and committed it as `472891f7`.
- `019edba6-71ce-7d12-9fb7-2455388e4065` (`chaosx_decision_mission_auditor`, `fork_context=false`) wrote `2026-06-18_012_africa_dossier_resistance_audit.md` with no gameplay edits.

## Gameplay Changes

- Observer settlements can now commit `africa_mediate_dossier_resistance_watch`.
- Direct Archive settlements can now commit `africa_enforce_dossier_resistance_watch`.
- Both timed interventions use stored `africa_archive_resistance_*` context rather than the later selected dossier.
- Both interventions spend concrete resources up front and resolve only after the timed decision finishes.
- Both interventions require dossier-profile logistics: convoys for Nile/river/lake/ocean cases, trucks and army XP for Sahel cases, infantry escorts for Maghreb/desert and western-crown cases, and trains for southern stone-seat cases.
- While an active local resistance watch exists, later dossier settlements are blocked so the single-context watch cannot be bypassed.
- Success/failure reports name the stored dossier, seat, settlement mode, intervention method, and dossier-profile consequence.

## Files Changed

- `common/script_constants/012_africa_constants.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_dossier_resistance_audit.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_dossier_resistance_parent_handoff.md`

## Audit Findings Addressed

- Active-watch settlement bypass is blocked in `can_africa_settle_selected_dossier`.
- Resistance-watch duration tuning is aligned at 150 days between file-scoped and script-constant values.
- Mediation and enforcement costs now include profile logistics instead of mode-only flat costs.
- Mediated/enforced flags and intervention counts are cleared by the Authority Atlas reset path.
- The Congress warning card now reports the Archive resistance dossier instead of the selected Bestiary package.
- Visible reports now distinguish mediated, enforced, and passive watch outcomes.

## Remaining Scope

This does not close full Event 012 completion. Remaining known blockers still include deeper settlement forks beyond observer/direct plus intervention, fuller Congress card families, targeted scenario validation, and final super-event source/audio blockers where research handoffs require them.
