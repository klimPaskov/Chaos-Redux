# Event 012 Africa Scripted-System Helper Audit Handoff

Subagent: `chaosx_scripted_system_architect`
Date: 2026-06-17

## Files changed

- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_guis/012_africa_scripted_gui.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_scripted_system_helper_audit_handoff.md`

Audited without gameplay changes:

- `common/script_constants/012_africa_constants.txt`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`

## Helper map

Added GUI eligibility triggers in country scope:

- `can_africa_use_gui_congress_session`
  - Inputs: runtime unifier state, `africa_gui_congress_session_recent`, PP threshold.
  - Output: boolean click eligibility.
  - Side effects: none.
  - Call sites: `africa_gui_congress_session_button_click` and `_click_enabled`.
- `can_africa_use_gui_refresh_register`
  - Inputs: runtime unifier state, `africa_gui_refresh_register_recent`, PP threshold.
  - Output: boolean click eligibility.
  - Side effects: none.
  - Call sites: `africa_gui_refresh_register_button_click` and `_click_enabled`.
- `can_africa_use_gui_start_dossier`
  - Inputs: Authority Atlas gates, selected dossier state, survey/guard cooldown flags, support equipment, PP.
  - Output: boolean click eligibility.
  - Side effects: none.
  - Call sites: `africa_gui_start_dossier_button_click` and `_click_enabled`.
- `can_africa_use_gui_authority_seats`
  - Inputs: runtime unifier state, regional authorities open flag, cooldown, PP, controlled authority seat.
  - Output: boolean click eligibility.
  - Side effects: none.
  - Call sites: `africa_gui_authority_seats_button_click` and `_click_enabled`.
- `can_africa_use_gui_bestiary_terms`
  - Inputs: runtime unifier state, habitat board open flag, one-time negotiated flag, cooldown, PP.
  - Output: boolean click eligibility.
  - Side effects: none.
  - Call sites: `africa_gui_bestiary_terms_button_click` and `_click_enabled`.
- `can_africa_use_gui_sponsor_readiness`
  - Inputs: runtime unifier state, sponsor/world-root flags, mission state, cooldown, `world_end`, convoys, support equipment, command power, PP.
  - Output: boolean click eligibility.
  - Side effects: none.
  - Call sites: `africa_gui_sponsor_readiness_button_click` and `_click_enabled`.

Changed existing helper behavior:

- `africa_white_peace_allies_after_rsa_continental_victory`
  - Replaced the broad `every_country` faction scan with an ENG self-peace check plus `every_allied_country`.
  - Preserves intended peace with ENG and ENG allies while avoiding a whole-world loop.
- `africa_mark_selected_dossier_surveyed`
- `africa_mark_selected_dossier_local_office`
- `africa_mark_selected_dossier_guarded`
- `africa_mark_selected_dossier_settled`
- `africa_mark_selected_dossier_observer_settled`
- `africa_mark_selected_dossier_direct_archive_settled`
  - Added selected-dossier idempotency guards before counters and profile side effects.
  - Prevents repeated helper calls from inflating Authority Atlas survey, office, guard, settlement, and seat-secure counters for the same dossier.

## Constants and tuning

No constants were added or changed. Existing constants were reused for GUI PP, equipment, command-power, and cooldown gates.

## Event targets and cleanup

- No new event targets were added.
- RSA peace continues to depend on existing global event target `africa_rsa_continental_side`.
- Existing `africa_bestiary_warning_state` and runtime target cleanup were audited; no new cleanup helper was needed for this patch.

## Migration and call sites

- Scripted GUI click effects now call the same `can_africa_use_gui_*` triggers as their `_click_enabled` blocks.
- No decision or focus files were edited. Existing decision/focus call sites remain valid.
- Parent follow-up may optionally migrate any future direct GUI-like decision calls to these same triggers if new call sites are added outside this write scope.

## Validation

- Checked all allowed Event 012 helper files for unsupported comparison-operator tokens; none found.
- Checked brace balance on the allowed Event 012 helper files; final depth was `0` for each.
- Confirmed `africa_white_peace_allies_after_rsa_continental_victory` now uses `white_peace = ENG`, `every_allied_country`, and `white_peace = PREV`, with no remaining `is_in_faction_with = ENG` scan in the helper.
- Confirmed every `africa_gui_*_button_click` handler and matching `_click_enabled` trigger references the same `can_africa_use_gui_*` helper.
- Confirmed selected-dossier counter helpers now guard against repeated selected-dossier survey, local office, guard, and settlement marks.
- Ran `git diff --check` on the allowed Event 012 helper files; no whitespace errors were reported.

## Remaining risks and parent follow-up

- `has_africa_valid_unifier_candidate`, weighted unifier selection, cleanup helpers, paper-claim grants, super-event audio broadcasts, and some state setup helpers still use broad `any_country`, `every_country`, or `every_state` scopes. They appear intentional for candidate selection, cleanup, map-state setup, or player super-event playback, but they should not be moved into daily/weekly on-actions without explicit parent review.
- `common/scripted_localisation/012_africa_scripted_localisation.txt` uses `localization_key`, which matches vanilla documentation and existing Chaos Redux scripted localisation style. No dynamic localisation ID patch was needed.
- The existing `common/scripted_effects/012_africa_effects.txt` file contains pre-existing indentation irregularities in `africa_clear_runtime_context`; this handoff did not reformat unrelated blocks to avoid broad churn in a dirty shared worktree.
- No Event 010 files were read or edited.
