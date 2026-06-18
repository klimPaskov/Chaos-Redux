# Event 012 Africa Dossier AI Parent Handoff

Date: 2026-06-18

## Scope

This parent tranche closes the narrow "richer per-package AI" portion of the accepted foundation addendum for historical dossiers by wiring the existing Authority Atlas lifecycle and eight dossier profiles into AI behavior.

It does not claim full closure of the foundation addendum. Package-specific historical mission families, deeper settlement forks, local resistance event chains, fuller Continental Congress presentation families, and targeted scenario validation remain open.

## Files Changed

- `common/ai_strategy/012_africa.txt`
- `common/decisions/012_africa_decisions.txt`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`

## Gameplay Changes

- Added static AI strategies for active Authority Atlas survey and archive-guard work.
- Added observer-settlement and direct-Archive resistance-watch AI postures.
- Added AI strategies for all eight historical dossier profiles:
  - Nile/Red Sea
  - Maghreb/desert
  - Sahel charter
  - western crowns
  - central river
  - Great Lakes
  - Indian Ocean
  - southern stone seats
- Profile strategies react to both the current selected dossier profile trigger and the persistent `africa_dossier_profile_*_opened` flags.
- Authority Atlas decisions now weight dossier opening, local offices, old-seat guards, observer settlements, and direct Archive settlements by route and selected dossier profile.

## Validation

- Subagent `019edb82-fddb-71e3-83dd-9160a82edddd` (`chaosx_decision_mission_auditor`, `fork_context=false`) reviewed the proposed static AI strategy approach and reported no missing trigger or flag names.
- Confirmed all referenced `is_africa_selected_dossier_profile_*` scripted triggers exist in `common/scripted_triggers/012_africa_triggers.txt`.
- Confirmed the persistent `africa_dossier_profile_*_opened` flags are set and cleared by the existing Authority Atlas effects.
- Confirmed route flags used in decision AI weights are set by the main Africa focus tree.
- Checked brace counts for the touched AI and decision files after the edit.
- Ran `git diff --check` on the touched AI and decision files.

## Remaining Risks

- No live HOI4 AI dump or scenario run was performed in this tranche.
- The opened-profile AI strategy bands intentionally stack as institutional memory after each profile enters the Archive. If later balance testing shows cumulative production pressure is too high, narrow those `enable` blocks to the active `is_africa_selected_dossier_profile_*` triggers only.
- The new AI strategies affect production/construction/war restraint and decision weighting; they do not create bespoke historical subject tags or new per-dossier mission events.
- The broader Event 012 completion audit should still treat targeted scenario validation as open.
