# Event 020 Dedicated Category Localisation Audit

## Scope

Audited the dedicated Black Plague response category localisation and its scripted-localisation selectors in `common/scripted_localisation/020_black_plague_response_scripted_localisation.txt` and `localisation/english/020_black_plague_response_l_english.yml`.

Referenced category and decision ownership was checked in `common/decisions/categories/020_black_plague_response_categories.txt`, `common/decisions/020_black_plague_response_decisions.txt`, and `common/decisions/020_black_plague_shared_response_decisions.txt` without changing those gameplay files.

## Audit Results

### Missing keys

None.

All 231 player-facing keys referenced through `name`, `desc`, `custom_cost_text`, `custom_effect_tooltip`, and scripted-localisation `localisation_key` assignments in the two Event 020 response decision files are defined in English localisation. The two `defined_text` names are functions rather than YAML keys and were excluded from the final missing-key result.

### Duplicate keys

None among the referenced Event 020 response keys.

### Scripted localisation issues

None found.

`GetBlackPlagueCountermeasureStatus` evaluates in country scope and orders mutually meaningful states from most conclusive to least conclusive: completed programme, active programme, laboratory mobilisation, available findings, then the unconditional not-started fallback. Completion clears the active-programme flag in `black_plague_refresh_countermeasure_completion`, so the first branch remains a safe defensive priority.


The category description calls both functions without an explicit namespace, matching vanilla decision-category scripted-localisation usage such as `[GetRousingProletariatDesc]`. The surrounding category description is country-scoped, so its naked country variables and country-flag triggers resolve against the viewing country. Global deaths use the explicit `global.` namespace.

### Dynamic text opportunities

No additional dynamic text is necessary for the assigned summary.

The category already displays the viewing country's name and deaths, worldwide deaths, cure-programme status and progress, Medical Reserve, remaining and total Response Capacity, and international-response status. Integer formatters are present on every count and capacity value. The completion threshold is read from the existing script constant.

### Cross-surface mismatches

No mechanical mismatch found.

The dedicated `black_plague_response_category` is registered separately from `chaosx_disease_containment_category`. National research, reserve, knowledge, cooperation, and recovery actions are assigned to the dedicated category, while selected-state containment actions remain assigned to the shared disease category. The dedicated description tells the player to select Black Plague and a state on the shared Disease Containment board for quarantine, hospitals, rat clearance, cordons, treatment, and cleanup.

The dedicated category has no `scripted_gui` field. This matches the requirement that it remain a standard decision category rather than add another scripted GUI.

The text does not promise an instant cure. It states that completing the cure programme unlocks cure-capable cleanup and does not remove an active outbreak by itself.


### File encoding concerns

None.

`localisation/english/020_black_plague_response_l_english.yml` begins with the UTF-8 BOM bytes `EF BB BF` and retains the required `l_english:` namespace.

### Prose-quality issues

- Vagueness: no blocking issue. Each summary line has a concrete label, and the final paragraph identifies which actions belong on each category.
- Bloat: the status panel is dense but justified by the seven requested live values. The three-sentence routing note remains readable and avoids explaining implementation history.
- Obvious explanation: no redundant title restatement or button narration was found.
- Repetition: no harmful repetition was found. The cure status and cure progress lines serve distinct purposes.
- Overcomplication: no overloaded subordinate structure blocks first-read comprehension.
- Style-rule repair: `black_plague_countermeasure_status_complete` used a forbidden em dash. It now uses a colon.

### Sourced quotations

None of the audited category, status, or routing text is presented as a sourced or attributed quotation. No quotation wording was changed.

## Patch Summary

### Changed files

- `localisation/english/020_black_plague_response_l_english.yml`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-09_event020_dedicated_category_localisation_audit.md`

### Changed keys

- `black_plague_countermeasure_status_complete`

### Dynamic localisation added or fixed

None. Both assigned `defined_text` selectors were already correctly scoped, ordered, and covered by localisation keys.

### Display before and after

- Before: `Complete` and `cure-capable cleanup unlocked` were separated by an em dash.
- After: `Complete: cure-capable cleanup unlocked`

### Prose before-and-after summary

- Vagueness: unchanged because no vague assigned line required repair.
- Bloat: unchanged because the requested status panel needs all seven live values.
- Obvious explanation: unchanged because no title or action was redundantly narrated.
- Repetition: unchanged because the status and progress rows report different information.
- Overcomplication: unchanged because the routing paragraph remains direct enough for a standard category description.
- Style-rule repair: replaced the em dash in the completed status with a colon.

All dynamic tokens, formatting codes, decision/category meanings, and the no-instant-cure warning were preserved. No sourced quotations were present.

## Validation

The task-specific reference audit covered 231 distinct localisation references across the two Event 020 response decision files and both scripted-localisation selectors. All 231 resolve to exactly one English key.

The category split was checked at source: dedicated national actions use `black_plague_response_category`, while selected-state containment uses `chaosx_disease_containment_category`. The registered dedicated category has a description, `visible_when_empty = yes`, an icon, a picture, and no scripted GUI.

### Skipped meaningful validation

The installed HOI4 MCP package exposes event, focus, technology, probability, GUI, and map routes but no decision-category inspection or rendering route. Therefore the standard decision-category description could not be rendered for overflow or engine-derived source-location evidence. Source review and the vanilla decision-category precedent are recorded here but are not treated as equivalent MCP evidence.

The user owns live in-game display validation, so no game launch was performed.

## Unresolved wording decisions

The parent may choose to rename the visible label `International Coordination` to `International Cooperation` for literal terminology. The current label and prose already communicate the required cooperative status without changing mechanics.

## Simplifications, omissions, and blockers

No feature simplification was introduced. The only blocker is the unavailable HOI4 MCP decision-category render/inspection route described above.
