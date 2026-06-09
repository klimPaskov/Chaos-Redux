# Event 006 Decision Audit Handoff: Early Aftermath Tranche

Date: 2026-06-05 06:47 UTC
Role: `chaosx_decision_mission_auditor`
Scope: bounded small patch for Event 006 Independence Wave decisions and missions.

## Required references read

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla docs: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`.
- Vanilla precedents checked: `common/decisions/MTG_congress.txt`, `common/decisions/stability_war_support.txt`, `common/decisions/foreign_influence.txt`.

## Changed files

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_0647_decision_audit_early_aftermath.md`

`common/script_constants/006_independence_wave_constants.txt` was touched because previous helper effects referenced decision-file `@` macros from outside their file. Those values are file-scoped, so the affected helper values needed shared Event006 script constants.

## Changed decision and mission ids

- `independence_wave_open_dossier_talks`
- `independence_wave_evacuate_host_archives`
- `independence_wave_offer_local_autonomy`
- `independence_wave_arrest_committee_couriers`
- `independence_wave_arm_loyalist_councils`
- `independence_wave_hold_capital_ministry`
- `independence_wave_form_local_defense_brigades`
- `independence_wave_draft_anti_puppet_clause`

## Changed helpers and constants

Added scripted effects:

- `independence_wave_complete_hold_capital_ministry_failed`
- `independence_wave_complete_hold_capital_ministry_secured`
- `independence_wave_complete_form_local_defense_brigades`

Updated existing scripted effects:

- `independence_wave_complete_recognize_the_loss`
- `independence_wave_complete_send_delegates_to_congress`

Added shared constants under `independence_wave_decision`:

- `host_capital_failure_stability_cost`
- `minor_stability_gain`
- `recognition_stability_gain`
- `recognition_war_support_cost`
- `brigade_command_power_gain`

Removed now-unused decision-file macros for those same values from `006_independence_wave_decisions.txt`.

## Localisation keys added

- `independence_wave_open_dossier_talks_effect_tt`
- `independence_wave_evacuate_host_archives_effect_tt`
- `independence_wave_host_target_root_requirements_tt`
- `independence_wave_offer_local_autonomy_requirements_tt`
- `independence_wave_arrest_committee_couriers_requirements_tt`
- `independence_wave_arm_loyalist_councils_requirements_tt`
- `independence_wave_hold_capital_ministry_activation_tt`
- `independence_wave_hold_capital_ministry_failure_requirements_tt`
- `independence_wave_hold_capital_ministry_failure_effect_tt`
- `independence_wave_hold_capital_ministry_success_effect_tt`
- `independence_wave_form_local_defense_brigades_requirements_tt`
- `independence_wave_form_local_defense_brigades_effect_tt`
- `independence_wave_draft_anti_puppet_clause_requirements_tt`
- `independence_wave_draft_anti_puppet_clause_effect_tt`

## Before and after behavior

Before:

- Two early host decisions used helper effects but did not give clear custom effect feedback.
- Three host targeted decisions depended on raw `target_root_trigger` and hidden target checks, so the player could not see a clear requirement summary.
- `independence_wave_hold_capital_ministry` exposed raw activation and completion/failure mission logic and kept its effects inline.
- `independence_wave_form_local_defense_brigades` exposed raw requirements and kept its reward/cost logic inline.
- `independence_wave_draft_anti_puppet_clause` exposed raw requirements and fired its helper without a player-facing effect summary.
- Existing helper effects for recognition and congress delegates read decision-file `@` macros from `common/scripted_effects`, which is unsafe because `@` constants are file-scoped.

After:

- The eight patched decisions/missions have custom requirement and/or effect text.
- Host target decisions now show concise root and target requirement summaries while preserving existing scripted trigger logic and AI weights.
- The capital ministry mission uses helper effects for failure and success, with separate tooltip text for each outcome.
- Local defense brigade completion is handled by a scripted effect helper.
- Anti-puppet clause completion hides internal variable mutations and shows a concise effect summary.
- The unsafe cross-file `@` references for this tranche now use `constant:independence_wave_decision.*`.

## Safety and scope notes

- No Event 006 release logic was wired into Event 005 or Soviet Collapse systems.
- No release timing, country package routing, evolution logging, GUI button behavior, or broad balance philosophy was changed.
- Existing costs, AI weights, cooldowns, target arrays, and scripted trigger names were preserved.
- This is a narrow cleanup tranche, not a full decision-system completion claim.

## Validation run

- `git diff --check` passed.
- Extra no-index whitespace checks passed for untracked touched files:
  - `common/decisions/006_independence_wave_decisions.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/script_constants/006_independence_wave_constants.txt`
  - this handoff file
- Brace count validation passed:
  - `common/decisions/006_independence_wave_decisions.txt: brace_delta=0`
  - `common/scripted_effects/006_independence_wave_effects.txt: brace_delta=0`
  - `common/scripted_triggers/006_independence_wave_triggers.txt: brace_delta=0`
  - `common/script_constants/006_independence_wave_constants.txt: brace_delta=0`
- Localisation encoding/style checks passed:
  - `localisation_bom=present`
  - `localisation_colon_zero=none`
- Checked that the repaired helper constants no longer appear as unsafe cross-file `@` references in Event006 effects/triggers.

## Skipped validation

- No live in-game validation was run.
- No full parser audit was rerun for all 186 decisions/missions; this tranche intentionally covered only the next early host/breakaway/congress subset.
- No commit was created, per the subagent task.

## Remaining gaps

- Many later targeted decisions still need custom requirement summaries, especially patronage, congress, compact, border commission, and remaining formation-ledger target decisions.
- Several later clickable decisions still need explicit effect summaries where they currently rely on helper names or raw generated effects.
- Some later mission `activation`, `available`, `complete_effect`, and `timeout_effect` blocks still need the same treatment applied here.
- The broader dirty worktree includes many unrelated files; this handoff only covers the Event006 files listed above.
- Several Event006 script files touched in this tranche are currently untracked in git, so parent review should account for that when staging the final commit.

## Skills used

- `hoi4-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-subagents`
