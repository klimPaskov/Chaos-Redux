# Event 020 Rat decision value bindings

Disposition: implemented for the owned localisation and scripted-localisation files. Parent review and live game display remain pending.

## Scope and change

- `localisation/english/020_black_plague_rat_decisions_l_english.yml`: replaced all 206 unsupported `[?constant:...|0]` displays with named scripted-localisation calls and added 111 output keys. Each original value, colour code, text icon, and surrounding sentence remains in place.
- `common/scripted_localisation/020_black_plague_rat_value_localisation.txt`: added 111 `defined_text` getters. Each getter copies its exact script constant into one temporary variable and resolves to the corresponding output key. These are display-only getters.
- No gameplay, workbook, export CSV, Git index, or other localisation file was edited.

The two source files that define the 111 values are `common/script_constants/020_black_plague_rat_constants.txt` and `common/script_constants/020_black_plague_constants.txt`. A mapping audit checked every getter's full category and key against those files. All 111 names resolve, all getter names and output keys are unique, every getter is called, and every output temporary variable is defined. Numeric values range from 1 to 180, with the category meter maximum at 100. No unsupported raw constant display remains in the owned YAML.

## Source alignment and remaining limit

The decision file is `common/decisions/020_black_plague_rat_decisions.txt`; related payments and effects are in Event 020 scripted effects. All 37 `custom_cost_text` references in that decision file have localisation keys in the owned YAML. The displayed decision days, costs, gates, gains, cooldowns, and category caps retain the same exact constant identifiers used before this replacement. The original source descriptions and cost rows were not rewritten, so this patch does not claim to settle pre-existing prose or balance defects.

Two factory displays are still only numerically aligned with the decision source: `black_plague_rat_decision.royal_strike_civilian_factories` and `black_plague_rat_decision.terminal_campaign_civilian_factories` both equal 1, while the decision file declares file-local `@CR_SC_BLACK_PLAGUE_RAT_DECISION_ROYAL_STRIKE_CIVILIAN_FACTORIES = 1` and `@CR_SC_BLACK_PLAGUE_RAT_DECISION_TERMINAL_CAMPAIGN_CIVILIAN_FACTORIES = 1`. The parent owns any gameplay-side consolidation of these tuning sources. The display is correct at current values, but future tuning could diverge until they share one source.

## Validation and references

- The YAML has UTF-8 BOM (`EF BB BF`) and CRLF; the scripted-localisation file has CRLF. A task-specific scan found 206 getter calls, 111 getters, 111 output keys, zero missing bindings, zero duplicate YAML keys, and zero raw `[?constant:` strings.
- Checked the supported trigger-to-temporary-variable display pattern against the offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md` sections “Scripted localisation” (lines 656–705) and “Temporary variable display” (lines 729–792), snapshot revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`.
- Checked the custom cost text relationship in offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 284–336, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
- Checked installed `documentation/script_concept_documentation.md`, lines 216–228, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`: fixed-point script constants are accepted by scoped variables with `constant:`. The repository's `common/scripted_localisation/016_mengele_stage_value_localisation.txt` uses the same getter structure.
- The first read-only MCP decision inspection request was rejected because `scenarios` were required. The first event inspection request was rejected because its selector needed an object. A corrected read-only decision inspection was attempted and stopped after it failed to return promptly. Those calls are route/schema evidence only, not display validation. The file-level checks do not prove in-game rendering, wrapping, or decision hover appearance.
- `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` are exposed, but no separate standalone Technology Tree Viewer tool is exposed in this client. This is a package gap and does not affect these decision text bindings.

## Audit lists and prose

- Missing keys and duplicate keys in this owned file: none found.
- Scripted-localisation issues after patch: none found by key and temporary-variable linkage checks; runtime display remains unverified.
- Dynamic text opportunity completed: every raw constant in the assigned file now reads from a script constant at display time through `defined_text`.
- Cross-surface mismatch: the two factory macro values described above. No spreadsheet wording was changed; the 111 new `black_plague_rat_value_*` keys are internal numeric outputs, so no player-facing workbook text handoff is needed for this patch.
- Prose-quality audit: bounded to preserving the existing decision descriptions and short cost rows during the binding repair. No vague, bloated, repetitive, obvious, overcomplicated, or style-breaking sentence was changed in this pass; any independent prose cleanup remains a separate parent scope.
- Sourced quotations: none in the owned decision localisation file. Existing dynamic tokens, text icons, and formatting codes were preserved.
- No plan addendum was needed: this change implements the agreed display binding and adds no mechanic.
