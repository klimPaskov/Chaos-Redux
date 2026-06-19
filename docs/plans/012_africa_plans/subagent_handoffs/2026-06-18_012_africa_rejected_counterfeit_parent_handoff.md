# Event 012 Africa Rejected-Counterfeit Settlement Parent Handoff

Parent tranche: `Reject Counterfeit Claim` Authority Atlas settlement fork.

## Implemented Surface

- Added the fifth playable historical-dossier settlement branch, `africa_settle_selected_dossier_reject_counterfeit`.
- Gated the branch behind documents-before-consent, the Authority Register, an exposed direct Archive seal, or Ananse counterfeit-watch access.
- Added non-PP-store costs: political power, support equipment, manpower, command power, and army experience.
- Added `africa_mark_selected_dossier_reject_counterfeit_settled`, per-dossier rejected-counterfeit flags, and the visible rejected settlement counter.
- Added rejected-counterfeit profile effects, passive resistance-watch gates, active Congress mediation, success/failure value movement, and cleanup from the shared dossier-resistance context.
- Added Authority Atlas header visibility, scripted localisation mode text, decision tooltips, and an AI strategy for active rejected-claim watches.

## Gameplay Identifiers

- Decision: `africa_settle_selected_dossier_reject_counterfeit`
- Trigger: `can_africa_settle_selected_dossier_reject_counterfeit`
- Settlement effect: `africa_mark_selected_dossier_reject_counterfeit_settled`
- Watch effect: `africa_start_dossier_resistance_watch_for_selected_reject_counterfeit_settlement`
- Watch flag: `africa_dossier_resistance_watch_rejected_counterfeit`
- Counter: `africa_dossier_rejected_counterfeit_settlement_count`
- Scripted localisation: `africa_dossier_resistance_mode.rejected_counterfeit`
- AI strategy: `africa_unifier_authority_atlas_rejected_counterfeit_watch`

## Files Changed

- `common/ai_strategy/012_africa.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/script_constants/012_africa_constants.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `localisation/english/012_african_union_l_english.yml`

## Audit Status

- `chaosx_decision_mission_auditor` was requested with `fork_context=false`, but the subagent hit a usage-limit error before returning output or patches.
- Parent local audit checked branch availability, watch resolution ownership, stale mode-flag cleanup, visible cost/effect text, and the observer/protected/rejected mediation split versus the direct/regional enforcement split.

## Remaining Risk

- Does not close the broader Event 012 blockers around deeper historical-dossier missions, Continental Congress presentation families, scenario validation, or final super-event sourcing/audio.
