# Event 012 Africa Package Gate Scripted Helper Audit Handoff

Date: 2026-06-20
Agent role: `chaosx_scripted_system_architect`
Scope: current uncommitted Event 012 package-action gate tranche only. No commit made.

## Summary

No gameplay, localisation, or documentation patch was required. The new `has_africa_required_regional_package_actions` helper is valid as a country-scope scripted trigger and is called from country scopes that resolve to the Africa unifier. The gate blocks sponsor readiness success, continent-unifier certification, and final World Is One gate preparation without moving the ordinary `AFR_africa_is_one` focus behind the new package-action counter.

The Continental Pole high-intensity validation seed is scoped to the scenario unifier and sets only validation counters/late-route prerequisite flags. It does not set proof-verified flags, certification, prepared-gate, `world_end`, or terminal World Is One flags.

## Files Inspected

- `common/scripted_triggers/012_africa_triggers.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_guis/012_africa_scripted_gui.txt`
- `common/national_focus/012_africa_focus.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
- `docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md`

Reference material consulted:

- Offline wiki core pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla documentation: `triggers_documentation.md`, `effects_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`.

## Findings

1. Helper syntax and scope: no issue found.
   - `has_africa_required_regional_package_actions` checks `africa_regional_package_action_count` against `constant:africa_mission_goal.regional_package_actions` with `compare = greater_than_or_equals` in `common/scripted_triggers/012_africa_triggers.txt:439`.
   - The mission completion gate is evaluated on the mission owner, with `is_africa_runtime_unifier = yes` and the active readiness flag in `common/decisions/012_africa_decisions.txt:5063`. That keeps the helper in the unifier country scope.
   - Certification and final gate preparation call the helper inside `event_target:africa_unifier_country` in `common/scripted_triggers/012_africa_triggers.txt:2276` and `common/scripted_triggers/012_africa_triggers.txt:2318`, so those calls also evaluate the unifier's country variable.

2. Bypass/deadlock risk: no narrow bypass found.
   - Sponsor readiness success now requires package actions before setting `africa_continent_sponsor_ready` in `common/decisions/012_africa_decisions.txt:5071` and `common/decisions/012_africa_decisions.txt:5092`.
   - Certification requires the same helper before setting `all_continent_unifiers_world_end_ready` and `africa_continent_unifiers_certified_for_world_is_one` in `common/scripted_triggers/012_africa_triggers.txt:2289` and `common/scripted_effects/012_africa_effects.txt:9473`.
   - Final gate preparation requires the helper before `africa_world_is_one_gate_prepared` can be set in `common/scripted_triggers/012_africa_triggers.txt:2331` and `common/decisions/012_africa_decisions.txt:5633`.
   - Normal Africa Is One is not deadlocked: `AFR_africa_is_one` still requires register/dossier coverage, regional authorities, and living cores, but not the regional package-action counter, in `common/national_focus/012_africa_focus.txt:2088`. The package gate enters after that through sponsor readiness and later terminal path checks.

3. Continental Pole scenario counter seeding: no issue found.
   - `africa_apply_triggerable_continental_pole_opening` calls validation gates only at high-or-higher intensity in `common/scripted_effects/012_africa_effects.txt:594`.
   - `africa_apply_triggerable_continental_pole_validation_gates` sets `africa_regional_package_action_count = constant:africa_mission_goal.regional_package_actions` in `common/scripted_effects/012_africa_effects.txt:642`, next to the other late-route validation counters.
   - The validation-gates helper does not set proof-verified flags, certification flags, prepared-gate flags, `world_end`, `world_end_africa_world_is_one`, `africa_world_is_one_terminal_started`, or `africa_world_is_one_gate_ready`. Terminal flags remain confined to `africa_mark_world_is_one_gate_ready` in `common/scripted_effects/012_africa_effects.txt:9487`.

4. Localisation and docs: accurate for this tranche.
   - Mission description and completion tooltip mention regional package actions in `localisation/english/012_african_union_l_english.yml:888` and `localisation/english/012_african_union_l_english.yml:1416`.
   - Certification and final preparation requirement text mention the new package-action requirement in `localisation/english/012_african_union_l_english.yml:1472` and `localisation/english/012_african_union_l_english.yml:1477`.
   - Docs/specs describe sponsor readiness, terminal certification, and Continental Pole validation seeding consistently in `docs/events/012_africa_foundation.md:45`, `docs/events/012_africa_foundation.md:225`, `docs/events/012_africa_foundation.md:234`, `docs/events/012_africa_foundation.md:238`, `docs/events/012_africa_foundation.md:305`, `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md:96`, `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md:100`, `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md:68`, and `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md:441`.

5. AI/GUI equivalents and validation hooks: no patch required.
   - AI decision weights for certification and final preparation reuse `can_africa_certify_continent_unifiers_for_world_is_one` and `can_africa_prepare_world_is_one_gate`, so the new helper is inherited by AI in `common/decisions/012_africa_decisions.txt:5624` and `common/decisions/012_africa_decisions.txt:5651`.
   - The scripted GUI sponsor button starts the same readiness mission through `africa_start_continent_sponsor_readiness_mission` in `common/scripted_guis/012_africa_scripted_gui.txt:82`; it does not directly set sponsor readiness. The mission completion gate blocks both decision-started and GUI-started readiness from succeeding without the package counter.
   - The scenario validation matrix explicitly covers the new counter and non-bypass flags in `docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md:18` and `docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md:20`.

## Changes Made

None. No files were patched except this handoff.

## Validation Commands and Results

- `awk '/^africa_apply_triggerable_continental_pole_validation_gates = \\{/{flag=1} flag{print} flag && /^\\}/{exit}' common/scripted_effects/012_africa_effects.txt | rg -n "proof_verified|continent_unifiers_certified|world_is_one_gate_prepared|world_end|world_is_one_terminal|world_end_africa_world_is_one|all_continent_unifiers_world_end_ready|africa_world_is_one_gate_ready"`
  - Result: no matches. The Continental Pole validation-gates helper does not set forbidden proof/certification/terminal flags.
- `rg -n "regional_package_action_count|has_africa_required_regional_package_actions" common/national_focus/012_africa_focus.txt common/scripted_effects common/scripted_triggers common/decisions common/scripted_guis`
  - Result: helper call sites are limited to sponsor readiness completion, certification, and final preparation; normal `AFR_africa_is_one` has no package-count dependency.
- `git diff --check -- common/scripted_triggers/012_africa_triggers.txt common/decisions/012_africa_decisions.txt common/scripted_effects/012_africa_effects.txt localisation/english/012_african_union_l_english.yml docs/events/012_africa_foundation.md docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md docs/plans/012_africa_plans/2026-06-20_targeted_scenario_validation_matrix.md`
  - Result: no whitespace errors reported for the audited uncommitted tranche.

## Residual Risks

- This was a static scripted-system audit only. Live mission timing, focus completion, and scenario launch behavior still need in-game validation by the parent.
- The GUI sponsor button tooltip says it starts the readiness mission, not every condition needed for the mission to succeed. That matches the current decision/mission split, but the parent may choose to expand GUI tooltip detail later if players miss why the mission cannot complete.
- Existing indentation around parts of the affected trigger blocks is uneven, but the inspected blocks remain structurally valid Clausewitz script and no syntax-changing patch was needed.
