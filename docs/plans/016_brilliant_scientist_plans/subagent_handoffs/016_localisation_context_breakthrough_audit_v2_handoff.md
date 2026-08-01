# Event 016 localisation audit v2

Date: 2026-08-01

Scope: Event 016 English localisation and scripted localisation after the `.4`, `.5`, and `.6` context and first-prototype report tranche.

The audit followed `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, `hoi4-decisions-missions`, `hoi4-focus-trees`, `chaos-redux-super-events`, and the Event 016 localisation auditor prompt. The required offline Paradox wiki localisation, data structure, trigger, effect, modifier, scope, on-action, event, decision, idea, and AI pages were consulted together with the relevant vanilla localisation and script documentation.

## Audit result

Missing keys: none after excluding intentional `GFX_*` sprite identifiers. The Event 016 gameplay and event localisation references have zero missing non-GFX keys.

Duplicate keys: none within the 15 Event 016 English localisation files and none across that Event 016 set. The parser found 2,368 unique keys and 2,368 entries.

Scripted localisation issues: none. The two Event 016 scripted-localisation files expose 331 `localization_key` results, all of which resolve to Event 016 keys except intentional `GFX_*` outputs. All Event 016 `GetBrilliantScientist*` methods called by localisation are defined. `GetBrilliantScientistBreakthroughProjectName` resolves the stored `.6` family through all 15 project families and has an unresolved-family fallback. `GetBrilliantScientistForeignProjectName` is actor-scoped through the foreign selected-family variable.

Dynamic text opportunities: the `.6` report uses `[This.GetBrilliantScientistBreakthroughProjectName]`, the Directorate overview uses the existing last-breakthrough getter, and foreign surfaces use dynamic actor, host, recipient, former-host, facility, route, and project-family text. The `.4` and `.5` event bodies identify the current host through event scope and already have context-specific descriptions. A future flavour tranche could add an explicit host-country name to those bodies, but this is not a missing-key or wiring issue.

Cross-surface mismatch notes: no localisation key or scripted-localisation mismatch was found. The `.4` and `.5` descriptions distinguish public, strategic, industrial, distributed, school, security, and mediation routes. The `.6` descriptions remain family-specific. Alien arms explicitly says proof is incomplete, temporal uses evidence and debt language, and no description turns a transformation into an alien origin claim. The `.4` and `.5` option gates use standard event `trigger` blocks without custom blocked-requirement tooltip keys. Those checks are simple route, government, war, or factory gates rather than raw state lists, and adding player-readable blocked text would require an event-script patch outside this localisation-only scope. Event Details and workbook wording were not changed in this audit because the current accepted catalog handoff already treats the `.4`, `.5`, and `.6` slice as ordinary flavour. The workbook was not rerun here.

File encoding concerns: all 15 Event 016 English localisation files were checked as UTF-8 with BOM. The four touched files still begin with `EF BB BF`. No `:0` key suffix was introduced. No em dash or semicolon style marker was found in Event 016 English localisation.

## Patch made

The binding contract exposes Mandate, Dependence, Exposure, and Project Capacity. Independent Capacity and Grievance remain hidden causal state. Existing tooltips exposed exact hidden-state names and arithmetic, so the patch removes those labels and numbers while preserving every visible value and the gameplay effect behind each tooltip. The replacement text gives qualitative private-reach and staff-pressure consequences without revealing hidden thresholds.

Changed files:

- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml`
- `localisation/english/016_brilliant_scientist_evolutions_l_english.yml`
- `localisation/english/016_brilliant_scientist_containment_l_english.yml`
- `localisation/english/016_brilliant_scientist_foreign_l_english.yml`

Changed keys in `016_brilliant_scientist_directorate_outcomes_l_english.yml`:

- `brilliant_scientist_context_public_science_tt`
- `brilliant_scientist_context_strategic_security_tt`
- `brilliant_scientist_context_industrial_mobilization_tt`
- `brilliant_scientist_context_distributed_research_tt`
- `brilliant_scientist_context_recognize_assistant_school_tt`
- `brilliant_scientist_context_bind_assistant_service_tt`
- `brilliant_scientist_context_mediate_assistant_conflict_tt`
- `brilliant_scientist_breakthrough_public_tt`
- `brilliant_scientist_breakthrough_classified_tt`

The parent agent's `.4`, `.5`, and `.6` title, description, option, and record additions in this file were preserved. This audit changed only the nine tooltip keys listed above.

Changed keys in `016_brilliant_scientist_evolutions_l_english.yml`:

- `brilliant_scientist_evolution_i_open_methods_tt`
- `brilliant_scientist_evolution_i_strategic_laboratory_tt`
- `brilliant_scientist_evolution_i_industrial_timetable_tt`
- `brilliant_scientist_evolution_i_university_confederation_tt`
- `brilliant_scientist_evolution_ii_state_security_tt`
- `brilliant_scientist_evolution_ii_military_guard_tt`
- `brilliant_scientist_evolution_ii_private_guard_tt`
- `brilliant_scientist_evolution_ii_allied_protection_tt`
- `brilliant_scientist_evolution_ii_open_science_tt`
- `brilliant_scientist_evolution_iii_safe_public_science_tt`
- `brilliant_scientist_evolution_iii_secret_projects_tt`
- `brilliant_scientist_evolution_iii_negotiated_limits_tt`
- `brilliant_scientist_evolution_iv_safe_regional_compact_tt`
- `brilliant_scientist_evolution_iv_charter_tt`
- `brilliant_scientist_evolution_iv_concession_tt`
- `brilliant_scientist_evolution_iv_military_seizure_tt`
- `brilliant_scientist_evolution_iv_foreign_containment_tt`
- `brilliant_scientist_evolution_iv_refusal_tt`
- `brilliant_scientist_sovereignty_deadline_mission_desc`

Changed keys in `016_brilliant_scientist_containment_l_english.yml`:

- `brilliant_scientist_launch_military_seizure_effect_tt`

Changed keys in `016_brilliant_scientist_foreign_l_english.yml`:

- `brilliant_scientist_foreign_encourage_defection_desc`
- `brilliant_scientist_foreign_defection_requirements_tt`

Before the patch, these 31 keys exposed exact Independent Capacity or Grievance labels or deltas. After the patch, visible Mandate, Dependence, Exposure, Capacity, Political Power, Stability, War Support, and deadline values remain explicit. Hidden effects are described as private reach, public access, pressure, oversight, or dissatisfaction where useful.

## Validation

The following task-specific checks were run after the patch:

- UTF-8 BOM check on all 15 Event 016 English localisation files. Result: all present.
- Duplicate-key scan within and across the Event 016 localisation set. Result: none.
- Gameplay and event localisation-key coverage scan. Result: zero missing non-GFX keys.
- Scripted-localisation output coverage scan. Result: 331 outputs, zero missing non-GFX keys.
- Dynamic method definition scan. Result: all Event 016 `GetBrilliantScientist*` methods used by localisation are defined.
- Hidden-label scan for exact `Independent Capacity` and `Grievance` in Event 016 localisation. Result: no exact hidden-state labels remain. Lowercase narrative uses of `grievance` remain in ordinary incident prose and do not expose a variable or arithmetic field.
- Style scan for em dash and semicolon markers. Result: none.

Skipped meaningful validation: no live game, GUI, audio, or event popup run was performed because live consumer validation belongs to the parent or user. The workbook was not edited, so the required workbook export was not run.

Unresolved wording decisions: none blocking. Live UI overflow and rendered text fit remain user-owned acceptance checks. The existing accepted boundary still queues broader country-specific flavour, bespoke report/news art, quantitative route-balance evidence, and live consumer acceptance.

No plan handoff was written for a missing mechanic. This file is the localisation audit and patch handoff only.
