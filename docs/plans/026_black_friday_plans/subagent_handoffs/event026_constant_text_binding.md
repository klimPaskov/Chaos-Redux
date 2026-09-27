# Event026 constant-backed localisation handoff

Disposition: implemented in source, with live display still unverified.

## Scope and result

- Changed `localisation/english/026_black_friday_l_english.yml`: `black_friday.evolution.1.body`, `black_friday.evolution.1.summary`, and `026_black_friday_five_departments_DESC` now call scripted localisation getters instead of unsupported `[?constant:...]` expressions.
- Changed `common/scripted_localisation/026_black_friday_scripted_localisation.txt`: added `GetBlackFridayEvolutionChaos`, `GetBlackFridayEvolutionDiscountPercent`, and `GetBlackFridayAchievementTargetFamilyCount`. Each getter assigns a temporary variable from the matching `constant:black_friday_event.*` value in its trigger and returns the formatted number. The discount getter serves both evolution strings.
- Expected visible values from `common/script_constants/026_black_friday_constants.txt`: chaos 600, evolution discount 75%, and achievement category count 5. These numbers are not duplicated in the new localisation or getter definitions.
- The achievement sentence continues to count a discounted Japan CBRN raid when it succeeds after the sale. No quotation-bearing text was changed.

## Audit

- Missing keys: none found among the three assigned strings. Duplicate keys: none found among them. Broken scripted-localisation references: the three new getter names are unique in the assigned file and resolve to definitions in that file; engine expansion remains unverified.
- Dynamic text opportunity addressed: three constant values now flow through supported temporary-variable display. No other in-scope dynamic text opportunity or cross-surface wording mismatch was found. Workbook alignment is unchanged because wording and meaning are unchanged. Spreadsheet owner receives the three final key names above without a wording update.
- Encoding: the edited `.yml` retains UTF-8 BOM. No encoding concern was found for the assigned `.txt` file.
- Prose: the assigned passages were read for vagueness, bloat, obvious explanation, repetition, overcomplication, and style violations. No prose rewrite was warranted by this bounded binding task. Before and after wording differs only at numeric interpolation tokens. Dynamic tokens outside those three expressions were preserved.

## Reference and inspection evidence

- Offline wiki `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, lines 656-705, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`: `defined_text` trigger temporary variables remain available in its selected localisation output. Lines 729-792 of the same revision document numeric temporary-variable display.
- Installed game `documentation/triggers_documentation.md`, lines 7482-7488, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`: `set_temp_variable` is supported in trigger scopes. `documentation/effects_documentation.md`, lines 7820-7827, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, confirms value assignment.
- Vanilla precedent: `common/scripted_localisation/SEA_PRC_scripted_loc.txt`, lines 38-54, defines a numeric getter with `set_temp_variable` in `trigger` and `localization_key = "[?temp_var...]"`; `localisation/english/SEA_focus_l_english.yml`, line 1948, embeds `[GetFiveYearPlanGoalCivFactoriesText]` in visible text. Event020 also has a valid stable-key variant, but the vanilla direct numeric form keeps this patch to the three assigned YAML keys.
- MCP `hoi4.event_inspect` trace accepted selector `{kind:"event",eventId:"chaosx.nr26.1"}` but returned `EVENT_INSPECTED_PARTIAL` at revision `c667b1897a5180f60b8895da5d08653ca6a4387b25419e98251c72bdfa1545df48b89ecd0d54d360dbc07cff09831ad4`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6b5aab1eb5497fa2acedbf40563fa428765a82ac11236742da8c0222ba2721d/3f955b717e64006f8269cd3e7606e5ff48b89ecd0d54d360dbc07cff09831ad4/event-trace-c667b1897a51.json`.
- MCP `hoi4.event_render` entries returned `EVENT_RENDERED_PARTIAL` at that revision, with zero selected nodes, so it cannot prove text display or overflow. Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da1ed6f49d1fa0ba6e1f5d339b160ee08aa5937355614410b429b533dd75763a/2881bf2c36764cbac602d39a592058a47ab87f95f1dee033eafff7a4258df862/event-entries-c667b1897a51.json`.

## Validation and remaining uncertainty

Source inspection confirms no `[?constant:...]` expression remains in the assigned `.yml`, the three getters map to the intended script constants, the achievement timing sentence is unchanged, and the `.yml` BOM remains present. Live in-game expansion and visual layout were not checked by this subagent. The MCP event render did not select the text-bearing event nodes, so its output is not display proof. No gameplay, achievement logic, costs, workbook, or unrelated files were edited. No simplification was made to the binding design.
