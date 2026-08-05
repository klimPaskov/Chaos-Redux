# Event 006 current localisation coverage audit

Date: `2026-08-06`.

Scope: Event 006 event registration, popups, Event Log, Event Details, evolutions, generic focus tree, current package decisions, missions and ledgers, SCN-008, the Statehood Ledger, and ordinary super-events 23 and 24. This audit follows the current 21-package, 20-reservation-group authority and does not promote any package or claim whole-event completion.

## Result

Current referenced-key coverage passes for the inspected English surfaces. The audit found and patched six narrow prose defects across six keys. No gameplay logic, package admission, quoted super-event text, dynamic token, or cost value changed.

## Missing key list

- None in the 327 explicit Event 006 popup title, description, and option-name references.
- None in the 348 Event 006 scripted-localisation `localization_key` references.
- None in the 39 Statehood Ledger GUI text, button, and tooltip references.
- None among the 319 Event 006 focus IDs after excluding the focus-tree container ID, which does not require an `<id>_desc` key.
- None among the top-level Event 006 decision, mission, and category identifiers after excluding script properties misidentified by the structural scan.
- All 160 referenced custom-cost families contain the base, `_blocked`, and `_tooltip` keys.

## Duplicate key list

- None. The 50 Event 006 English localisation files contain 6,900 unique scoped keys.

## Scripted localisation issues

- No broken Event 006 scripted-localisation reference or duplicate target key was found.
- The pre-existing robustness opportunity remains for enum selectors without a final unconditional neutral branch, particularly the crisis resolution, transport, economic, military, ambition, power-center, and force-template selectors. This is an unset or out-of-enum blank-text risk, not a reproduced current failure.
- The super-event selectors map ordinary slots 23 and 24 to the correct `.t`, `.d`, `.q`, and `.a` families. Image dispatch also uses ordinary values 23 and 24.

## Dynamic text opportunities

- The Statehood Ledger already uses dynamic bands, actors, host and patron names, league phase, founding phase, mission status, and formable costs. No safe additional conversion was needed in this patch.
- The five long ledger panel values still need a consumer-specific visual acceptance pass with representative runtime text. The MCP renderer produced offline states, but its synthetic scenarios do not populate the actual Event 006 dynamic values.
- SCN-008 correctly keeps its readiness text rule-based instead of hardcoding the current package snapshot. Its eight mode labels and descriptions and four intensity labels resolve, and the 32-cell static matrix passes.

## Cross-surface mismatch notes

- Current authority, localisation, and selectors agree on ordinary super-event 23 for `The League of New States` and ordinary super-event 24 for `Every Border a Casus Belli`.
- Ordinary super-event 23 remains blocked on rights-cleared audio, wrappers, and firing. Ordinary super-event 24 remains source-wired with partial reachability. Localisation does not claim otherwise.
- Event popup, Event Log, Event Details, evolution, focus, decision, mission, category, Statehood Ledger, SCN-008, and ordinary super-event references resolve against the current English key set.
- No stale four-digit super-event identifier was found in current Event 006 localisation.
- Internal country-collection display labels still include `Event 006` in three collection names. They are registry/debug-style collection labels rather than in-world event, decision, focus, GUI, or super-event prose, so this bounded patch did not rename their identifiers or labels.

## File encoding and source-format concerns

- All 50 scoped YML files retain the required UTF-8 BOM and contain no NUL or Unicode replacement character.
- No `:0` key suffix was found.
- Twelve scoped files contain 644 pre-existing indented localisation-key lines. This conflicts with the repository no-leading-space convention, although the inspected keys still resolve in source and MCP scans. A whole-file indentation normalization would create broad churn in parallel-edited files and was not included in this narrow patch.

## Prose-quality findings and repairs

### Vagueness

- `independence_wave_mnt_project_failure_effect_tt` formerly said that unspecified `Event 006 ledgers` deteriorated. It now names legitimacy, recognition, state capacity, security, and instability, matching `independence_wave_mnt_apply_project_failure`.
- The Montenegro and Transylvania sovereignty tooltips formerly referred to generic public `Event 006 values`. They now state which public values rise and that instability falls, matching each package's major-settlement effect.

### Bloat

- No broad prose compression was performed. The six repaired keys remain limited to their original player-facing consequence or premise.

### Obvious explanation

- No tooltip was found that merely repeated its button title after the patched keys were reviewed.

### Repetition

- No repeated paragraph or duplicated explanatory sentence required an in-scope patch.

### Overcomplication

- `independence_wave_form08_autonomous_danube_member_desc` formerly described internal `origin` and `focus content`. It now describes reciprocal access, guarantees, retained government, and retained territory.

### Style-rule repair

- `chaosx.nr6.35.d` no longer uses an em-dash contrast construction.
- `independence_wave_form08_project_cost_tooltip` no longer uses a semicolon and replaces the implementation-facing `carrier` with `country`.
- No remaining em dash or sentence semicolon was found in the scoped Event 006 localisation after the patch.

## Sourced quotation preservation

- `chaosx_super_event.23.q`, attributed to Woodrow Wilson's Fourteen Points, was preserved verbatim.
- `chaosx_super_event.24.q`, attributed to Hosea 8:7 in the King James Version, was preserved verbatim.
- Attribution accuracy was not re-researched in this bounded coverage audit. No quoted punctuation or wording was normalized.

## Changed files and keys

- `localisation/english/006_independence_wave_l_english.yml`: `chaosx.nr6.35.d`.
- `localisation/english/006_independence_wave_formable_registry_l_english.yml`: `independence_wave_form08_autonomous_danube_member_desc`, `independence_wave_form08_project_cost_tooltip`.
- `localisation/english/006_independence_wave_montenegro_l_english.yml`: `independence_wave_mnt_project_failure_effect_tt`, `independence_wave_mnt_sovereignty_effect_tt`.
- `localisation/english/006_independence_wave_transylvania_l_english.yml`: `independence_wave_tra_sovereignty_effect_tt`.
- This handoff.

Dynamic localisation added or fixed: none. All existing dynamic tokens and constant references were preserved.

Behavior before: six player-facing strings exposed an internal event number, implementation terminology, vague ledger consequences, or forbidden punctuation and contrast structure.

Behavior after: the same mechanics display direct in-world consequences and compliant prose without changing values, requirements, or route identity.

## Meaningful validation

- Event 006 static coverage: 50 files, 6,900 unique keys, zero scoped duplicates, zero bad BOMs, 327 popup references resolved, 348 scripted-localisation references resolved, 39 Statehood Ledger GUI references resolved, and all 160 custom-cost trios complete.
- `python -B .tools/audit_event6_scenario_matrix.py`: PASS for all 32 SCN-008 mode/intensity cells and eight recorded edge cases.
- `python -B .tools/audit_event6_gui_matrix.py`: PASS for the Statehood Ledger semantic source matrix.
- Event MCP: focused `chaosx.nr6.1` scan and neighborhood render completed with partial-analysis status. The neighborhood artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d43e304143e4ad17f3c05ac87375e925a7aa3b52287fc5c38e4ea34fe33e1e27/c17b013abe3bda6b412bcbc6474f69acd0a5a59b7ccfcee35997011c3f6b9754/event-neighborhood-04e76dcf50ae.json`.
- Focus MCP: `independence_wave_focus_tree` resolves 184 titles and 193 connectors. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f870424025618ad2f10cd5ae4346e1269875f91c332ce2fb5e7f64814470ebb/51ce3f9d6ede1ef10b020815c1327e32f00160a440a079406840d30aeb3c0653/focus-inspect.589775a6a495eb68.json`. The 14 blocking icon diagnostics belong to installed vanilla continuous focuses, not Event 006 localisation.
- Statehood Ledger GUI MCP inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c1d29fb104a6ca57e69d6867b15b3f3df26a04068e54cfc53f25901986e5382/932e2bd5258cdb21faaff0aebcde3db2e98b412d6982c1fc112f85a79cb1e1a0/gui-inspect.744f605afe9e7c62.json`. Render fidelity artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0860cb0ae3e9f16fd9528a736f82498978fbc96c8dd7f38517c93b68005284b6/6cdf6641072a7a2e9f9f9289834e84b76c7b5a10a97437930176e7d7a6fcbeb0/independence_wave_status_window-fidelity.json`.
- SCN-008 GUI MCP inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/839720039dd0baccb2adc4fa6e48de402c064055af7012ec639be93cffa8477b/d4073fcf659ad86ae423496ae40d48eac40c20b0e0f5bb6ec5aa66c5c89bef1e/gui-inspect.5cc2b284af0d4ba1.json`. The focused window reports no visible-overlap diagnostic.
- Event Log GUI MCP inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21cfa20d4a3295066579a795d024ae9ee50ff6744beba3186f06d1226e54eb84/f80956b8b145bc68b5b61218904a5bbfde36258112ea60cc4490824bc690fbe3/gui-inspect.7039b40c86d5e2b7.json`.
- Super-event GUI MCP inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f87b8c1f5b22602a4fbb4d8f8ef522b1b98466e893779c9a315487ebfaafd4e/9511a344f661daa64ba38a5ce4f0b7fb3e50e7166ef3b08e43d8f8d33d878855/gui-inspect.7b5d0538c9f3134d.json`.

## Skipped or limited validation

- No dedicated Technology Tree Viewer exists in the installed package. No Event 006 technology or doctrine surface was in this localisation scope.
- The installed MCP has no decision-list localisation renderer. Decision and mission visual overflow, blocked-cost presentation, and raw-trigger presentation remain source-checked rather than visually proven.
- The Event Log and super-event synthetic GUI scenarios did not inject Event 006 runtime text. Their renders returned `changedPixels = 0` between compared synthetic scenarios, so they do not prove Event 006-specific overflow. Source coverage is not treated as equivalent visual evidence.
- The GUI tool continues to report 1,894 workspace-wide blocking diagnostics and shared-window overlaps. Those global diagnostics prevent a clean GUI completion claim and were not attributed to Event 006 without an isolated finding.
- No live game, runtime event firing, or save/load test was performed under repository policy.

## Unresolved wording decisions

- Whether the enum selectors should receive unconditional neutral fallback branches under their current value contracts.
- Whether the long Statehood Ledger panels should be shortened after a real dynamic-value consumer review.
- Whether the three internal collection labels containing `Event 006` are intended to be player-visible debug labels or should be renamed in a separate collection-localisation cleanup.
- The public reveal timing of `independence_wave.evolution.5.body` remains an owning-event question.

## Simplifications, omissions, and blockers

No gameplay simplification, fallback, package invention, advisor-icon work, quote edit, or broad prose rewrite was introduced. Event 006 remains **HOLD / PARTIAL** under the current authority, including the ordinary-super-event-23 audio and firing blocker and ordinary-super-event-24 reachability limits.
