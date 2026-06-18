# Event 012 Africa - Historical Dossier Specific Settlement Handoff

## Parent tranche

This tranche reduces the Authority Atlas depth blocker by giving every historical dossier a distinct once-only settlement outcome. It does not add new country packages, tags, assets, events, or mission families.

## Files changed

- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`

## Scripted helpers

- `africa_record_selected_dossier_specific_settlement`
- `africa_apply_selected_dossier_specific_settlement_effects`
- `GetAfricaSelectedDossierSettlementSummary`

## Gameplay behavior

- `africa_mark_selected_dossier_settled` now calls the specific settlement helper inside its existing `NOT = { has_africa_selected_dossier_settlement = yes }` guard.
- Every existing `africa_dossier_id` entry receives a mapped value-only outcome when it is first settled.
- The helper records `africa_dossier_[id]_specific_settlement` for later audit/achievement/event use.
- Observer and direct Archive branch effects remain in the existing observer/direct profile helpers; this avoids reading cumulative branch-history flags as if they were current-action flags.
- The Authority Atlas header now shows `GetAfricaSelectedDossierSettlementSummary` beside the profile outcome.

## Subagent input

`chaosx_scripted_system_architect` (`019edb8f-fe4b-7630-9da5-a705b613f29a`) recommended a bounded value-only settlement helper, one call site inside `africa_mark_selected_dossier_settled`, reuse of existing `africa_value_delta` constants, and validation that every dossier id is covered. The parent implementation followed the value-only/call-site/constant guidance and kept branch-specific effects in the existing branch helpers to avoid ambiguity from cumulative observer/direct flags.

## Remaining risk

- This is not the full bespoke historical dossier mission/event package requested by the addendum.
- No new local resistance event chains, spawned historical subject tags, or per-dossier mission objectives were added in this tranche.
- No live HOI4 scenario validation was run.
