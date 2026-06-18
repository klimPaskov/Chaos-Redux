# Event 012 Africa Settlement-Fork Parent Handoff

Date: 2026-06-18
Parent tranche: Authority Atlas historical dossier settlement forks.

## Implemented

- Added two playable historical dossier settlement decisions:
  - `africa_settle_selected_dossier_protected_seat`
  - `africa_settle_selected_dossier_regional_office`
- Protected Seat is route-locked to respect/federal/sovereign-seat paths, requires Regional Trust and Authority, spends political power, infantry equipment, support equipment, and manpower, records a protected settlement counter/flag, and starts the protected-seat resistance watch.
- Regional Authority Office is route-locked to regional-authority plus documents/register paths, requires Authority and League Cohesion, spends political power, support equipment, trains, and manpower, records a regional-office settlement counter/flag, and starts the regional-office resistance watch.
- The Authority Atlas category header now exposes all four settlement fork counters: observer, protected, regional office, and direct Archive.
- Resistance watch gates now cover all four settlement modes:
  - observer: Regional Trust plus League Cohesion
  - protected: Regional Trust plus Authority
  - regional office: Authority plus League Cohesion
  - direct Archive: Authority plus Restoration Debt cap
- Mediation now resolves observer and protected-seat watches. Enforcement now resolves regional-office and direct Archive watches.
- Watch success and failure now move distinct protected-seat and regional-office values instead of falling through to observer/direct outcomes.
- AI strategy now has active-watch postures for protected-seat and regional-office resistance cases, including infantry/support/trains/infrastructure pressure where appropriate.
- Runtime and Authority Atlas cleanup clear the new fork counters and watch-mode flags.
- Docs and source-of-truth notes were updated to describe the four-fork settlement layer and the remaining rejected/counterfeit settlement branch gap.

## Audit

Subagent: `chaosx_decision_mission_auditor`, spawned with `fork_context=false`.

Handoff:

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_settlement_fork_audit_handoff.md`

Audit patch accepted:

- Removed the stale `NOT = { has_variable = africa_archive_resistance_dossier_id }` guard from all four `africa_start_dossier_resistance_watch_for_selected_*_settlement` helpers.
- This prevents the first resolved resistance watch from permanently blocking all later dossier resistance watches.
- The active cap remains `africa_dossier_resistance_watch_active`, and base settlement still blocks while an active watch exists.

Audit residual risk:

- The current report variables still serve as both active watch context and last-report context. This is playable after the accepted patch, but if report event text ever proves late-bound after a new watch starts, the report could theoretically display the newer watch context. A fuller follow-up would split active watch variables from last-report variables.

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
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-18_012_africa_settlement_fork_audit_handoff.md`

## Validation

- Static audit confirmed route locks, costs/spends, train/equipment/manpower handling, watch creation, mediation/enforcement completion, passive gates, cleanup, scripted localisation, category header text, AI behavior, and docs alignment for the new forks.
- Parent validation checked brace deltas on touched script files, stale observer/direct-only wording, localised key coverage for the new decision ids, and localisation BOM.
- `git diff --check` passed on the touched Event 012 files.

## Remaining Event 012 Gaps

- The accepted settlement fork list still has no dedicated rejected/counterfeit-claim settlement decision branch.
- Historical dossier content remains value-rich but still lacks deeper package-specific missions beyond settlement and resistance watches.
- Final completion still requires later Continental Congress presentation depth, targeted scenario validation, spreadsheet alignment, completion audit, and unresolved super-event sourcing/audio work where already documented.
