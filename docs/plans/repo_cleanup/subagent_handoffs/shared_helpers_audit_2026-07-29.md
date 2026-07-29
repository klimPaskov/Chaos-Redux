# Shared helper audit handoff

Date: 2026-07-29

Scope: shared scripted systems and helper registries, with Event 001-020-specific references audited only where they consume a shared helper. GUI event-target usage was treated as valid repository practice and was not migrated, removed, or recommended for removal.

## Changed files

- `common/scripted_triggers/chaosx_dynamic_triggers.txt`
  - Helper: `is_desert_state`.
  - Removed the second `state = 857` alternative and the second `state = 402` alternative from the same `OR` block.
  - The trigger remains a state-scope boolean registry with the same 73 unique state IDs and the same result for every state.
- `common/scripted_triggers/chaosx_dynamic_triggers.md`
  - Documented the `is_desert_state` scope contract, explicit state-ID registry, uniqueness invariant, and extension rule.
- No scripted effects, scripted localisations, scripted GUIs, interface/GFX files, constants, collections, on-actions, events, localisation, or workbook files were changed.

## Reference evidence

The complete repository search for `is_desert_state` found only these gameplay call sites:

- `events/026_industry_to_desert.txt:31,35,56,77,90` for Event 026 owned-state selection and factory relocation.
- `common/scripted_effects/cbrn_doctrine_effects.txt:247` for the state-scope low-water cleanup multiplier.

The only definition and documentation references are:

- `common/scripted_triggers/chaosx_dynamic_triggers.txt:78`.
- `common/scripted_triggers/chaosx_dynamic_triggers.md:11,15`.

Searches across localisation (`*.yml`), scripted GUI (`*.gui`), GFX/entity (`*.gfx`, `*.asset`), documentation/catalog (`*.md`, `*.html`, `*.csv`, `*.xlsx`), scripted effects/triggers, and on-actions found no additional dynamic, meta-effect, scripted-localisation, GUI, GFX, docs, or workbook consumers.

The repository's GUI event-target convention remains untouched. No `event_target:` pattern was edited or migrated.

## Validation

- Parsed the `state = <id>` alternatives in `is_desert_state` and confirmed 73 entries with no duplicate IDs after the patch.
- Re-ran repository reference searches and confirmed the two gameplay consumers above remain unchanged.
- Ran `git diff --check` on both changed files.
- Did not launch Hearts of Iron IV, per repository instructions.

## Retained and deferred candidates

- Retained legacy selector aliases in `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`, including `select_triggerable_scenario_final_silence` and `trigger_final_silence_scenario`. Their comments identify save/script compatibility redirects to Fallout, so deletion would require save migration evidence and broader scenario-surface review.
- Retained compatibility and GUI-facing helper names in `common/scripted_effects/chaosx_settings_effects.txt`. Several are not directly referenced by ordinary text call sites, but they may be bound by scripted GUI or retained saves. The parent-owned settings surface was not modified.
- Retained the broad event-log, cluster, triggerable-scenario, world-threat, condemnation, air-cleanliness, deaths, collections, and on-action registries. No safe deletion candidate had complete cross-surface evidence within this bounded pass.
- Did not change any GUI event-target pattern. The prior migration concern is explicitly deferred as invalid for this repository.

## Risks and follow-up

The cleanup is behavior-preserving because duplicate alternatives in a boolean `OR` block cannot change the result. Future desert-state additions should update the shared trigger and its documentation together. Any future attempt to retire compatibility helpers must audit direct calls, meta effects, scripted localisation, scripted GUI bindings, GFX-linked text, docs, workbook references, and save compatibility before deletion.
