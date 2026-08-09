# Event 018 final localisation audit and bounded repair

Date: 2026-08-10
Agent: `chaosx_localisation_auditor`
Scope: Event 018 localisation, Event 018 scripted localisation, and exclusively Event 018 shared keys

## Verdict

**Localisation implementation: PASS after one bounded prose repair.** Event 018 has complete static key coverage for its events, options, decisions, missions, decision categories, selected-field GUI, workboard pages, DHO country identity, characters, traits, ideas, templates, focus tree, super-events, achievements, news, event log, Event Details, four evolution stages, world end, regional defeat, and global defeat.

**Whole-event completion: BLOCKED by catalog wording drift.** The exported Event 018 workbook row does not use the final in-game Event Details and evolution wording even though `docs/specs/018_resources_found_specs/matrices/acceptance_criteria.md` marks both alignments complete. This task could not edit the workbook. The spreadsheet owner must reconcile `Events!C19:G19` with the accepted in-game strings or document and approve a different mirroring rule.

No gameplay, decision source, focus source, GUI geometry, asset, spreadsheet, or unrelated localisation file was edited.

## Changed files and keys

- `localisation/english/018_resources_found_system_l_english.yml`
  - `resources_found.gui.resources.tt`
- `docs/plans/018_resources_found_plans/subagent_handoffs/event018_localisation_final_current_2026-08-09.md`

### Display before and after

- Before: the selected-field resource tooltip began `Event 018 additions`, exposing an implementation identifier to the player.
- After: it begins `Recorded discoveries`, describing the ledger in-world while preserving every resource token, integer formatter, total, and closure explanation.

No dynamic localisation was added or changed. The new workboard pagination introduced before this audit is valid as implemented: `GetResourcesFoundSelectedWorkboardPage` maps Operations, Safety, Infrastructure, and Development explicitly and falls back to Administration. Its five target keys exist, and the selected field remains the correct scope for the per-field page variable.

## Key coverage

### Missing keys

None found.

- Event script: 562 unique title, description, option, and tooltip references, with 562 definitions.
- Decisions and missions: 135 top-level entries. Nine evolution-clock missions are permanently hidden internal timers and intentionally have no name or description. The remaining 126 rendered entries have names and descriptions. Direct tooltip and cost-text references resolve.
- Focus tree: 67 focuses, each with title, description, and completion tooltip. The tree name also resolves.
- Achievements: 15 Event 018 achievements have all 30 `_NAME` and `_DESC` keys and all 19 referenced eligibility or condition tooltips.
- Primary Event 018 files contain 1,586 keys: 562 event, 502 decision/mission/workboard, and 522 system/country/focus/GUI/log/super-event/news keys.

### Duplicate keys

None found among Event 018 identifiers across the English localisation database.

Six duplicate values longer than 20 characters remain and are intentional semantic reuse: the domestic-board option, regional-defeat event/news title, two decision/mission title pairs, and the idea/focus title pairs for Interlocking Carapaces and Urban Cellar Networks.

### Orphaned keys

No new orphan was found. The five `resources_found.workboard.*` keys are consumed by `GetResourcesFoundSelectedWorkboardPage`. Mission `_tt` families correspond to their rendered mission identifiers and are not dead draft text.

## Scripted localisation

### Issue list

None found.

- `common/scripted_localisation/018_resources_found_scripted_localisation.txt` contains 20 unique `defined_text` names and 75 unique target localisation keys. All targets resolve.
- The Event Details history calls `GetResourcesFoundHistoryMode` and `GetResourcesFoundHistoryResourceName` resolve in the shared Event Log scripted-localisation file.
- All Event 018 `GetResourcesFound*` calls resolve to a defined selector.
- The workboard selector checks the selected persistent field record and has a safe Administration fallback when the page variable is absent or still at its default.
- Event-target and state-scope name lookups retain their required prefixes and scope forms.
- Scripted-localisation files contain no literal `§` or `£` formatting characters.

### Integer formatting

All numeric values inspected in the three Event 018 localisation files use integer formatting where the design treats them as whole values (`|0` or `|Y0`). The apparent unformatted bracket expressions in closed-history status text are scoped scripted-localisation calls, not numbers.

## Dynamic text opportunities

No required opportunity remains inside this scope. Selected state names, owners, controllers, resource values, field indices, recorded resource names, history mode, field status, workboard page, evolution rows, costs, durations, and thresholds already use dynamic text where it materially improves clarity. The five workboard page names are fixed presentation labels and do not need variable-backed wording.

## Cross-surface mismatch notes

### Blocking catalog mismatch

The current export in `docs/spreadsheets/chaos_redux_events_catalog.csv` does not exactly match the live strings required by the accepted checklist:

- `Events!C19` / CSV `Details` differs from `resources_found.event_details.description`.
- `Events!D19:G19` / CSV `Evo I` through `Evo IV` use expanded catalog prose rather than the live `resources_found.evolution.stage_1.body` through `.stage_4.body` wording.
- `Events!I19` matches the live public premise of `DHO_the_world_opens_below_desc` and does not need a localisation repair.

The catalog text does not directly contradict the mechanics, but the repository contract says the workbook matches final in-game Event Details wording and evolution fields match final in-game evolution wording. The mismatch therefore remains a completion blocker until the spreadsheet owner updates the workbook and regenerates the CSV exports, or the parent explicitly approves non-identical summaries and updates the acceptance language.

### Other surfaces

- `chaosx.event_name.18` is `Resources Found` and matches the catalog event name.
- The Economy (pos) cluster name and Event 018 membership wording match the accepted catalog handoff.
- Public Event Details remains premise-only and does not reveal the Oth-Kesh route before chronology gates permit it.
- Four authored evolution stages and four unrevealed masks remain aligned with the shared Event Details selectors.
- Super-event slots 82, 83, and 84 retain distinct emergence, world-end, and conditional global-defeat text.

## File encoding concerns

None found. The three Event 018 English localisation files and the inspected shared English localisation files retain UTF-8 with BOM. No Event 018 key uses `:0`.

## Prose-quality audit

### Vagueness

No unresolved vague passage was found in the newly added workboard text or the inspected Event 018 surfaces. Requirements and consequences name the field, project family, resource, timer, state, actor, or route when the player needs that information.

### Bloat

No new bloat defect was found. Exact cost previews are long by necessity because they expose the complete calculated payment and capacity requirements. Their structure is icon-first and value-first.

### Obvious explanation

No tooltip introduced by the workboard page selector merely repeats its title. Its description explains per-field persistence, and its tooltip names the five pages and clarifies that the presentation filter does not cancel project state.

### Repetition

The six exact duplicate-value groups listed above are intentional cross-surface reuse. No accidental duplicate workboard, option, tooltip, focus, or super-event prose was found.

### Overcomplication

No newly introduced sentence required simplification. The longer achievement condition tooltips remain appropriate because they expose exact multi-part qualification rules.

### Style-rule repair

`resources_found.gui.resources.tt` was repaired because `Event 018 additions` described the implementation rather than the field record. The replacement is direct in-world wording. No player-facing Event 018 value now contains an em dash, sentence semicolon, prompt fragment, update-history wording, staged contrast formula, or the string `Event 018`.

## Sourced quotation preservation

All three sourced super-event quotations were preserved verbatim:

- Job 28:5, World English Bible, slot 82.
- Aeschylus, *Prometheus Bound*, Buckley translation, slot 83. The intentionally lower-case opening remains unchanged.
- Croesus in Herodotus, *Histories* 1.87, Godley translation, slot 84.

No quotation, attribution, punctuation, dynamic token, formatting code, or cultural remark was altered. Source and rights evidence remains in `docs/super_events/018_resources_found/text_research.md` and the super-event text researcher handoff.

## MCP evidence

- Current Event 018 event namespace scan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/739d40203a6c808d8684c7873a605419157061f067be6413c1bf125a7815aa7e/bc11bbef7426a858a7568d3686a40618b6ee241e24e3c586abb571495c47554d/event-scan-7e8e9a563058.json`. Result: `EVENT_INSPECTED_PARTIAL`, zero blocking Event diagnostics. Workspace-wide helper projection and lifecycle analysis were deferred by the adapter.
- Current DHO focus inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/833e57b2eb054ba8870b59e44313cacb73f8327e677cb39fc03f9fc3646ab746/47b21bf226236fd610fb96a49598a9cd5cbde39c807ae53ba0c174a64fb776ec/focus-inspect.8f5919065cc7e0ff.json`. It resolves all 67 focus titles and reports zero Event 018 tree diagnostics. The failed headline validation comes from unrelated vanilla continuous-focus icon diagnostics.
- Current selected-field GUI render at 1280x720, 1366x768, 1920x1080, and 2560x1440 with normal, hover, selected, disabled, warning, active, completed, empty/full, minimum/maximum, long-text, and missing-localisation probes: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65f260e93b8b02003e0d5a02f453a755dbc8582a27ec45fb9de593cac0f4310a/1e8e4616f6db7a25413cf7275c8deff4860f4ae3338ef1d5d0d184f5ca6b68e2/resources_found_field_window-full.svg`. Result: `GUI_RENDERED`; only response-wire truncation was returned.
- Post-repair GUI/localisation inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5dc4a721f3a79518d63d4552b639a902a7846f0ea6c490d8b5e21dc2d21628e/4bf1c72d566560679b2316cf317ef2fa2a23a904ea2fba2f503a70e1a11eaa03/gui-inspect.80b85d3235a5dcf7.json`. It inspected all 34 Event 018 GUI elements and returned no Event 018-local diagnostic. Its failed headline validation and 2,000 retained graph diagnostics are repository-global and dominated by unrelated source collisions and overlaps.

The installed package has no Technology Tree Viewer. Event 018 defines no custom technology or doctrine tree, so no technology-tree localisation surface was available or required for this audit.

## Meaningful validation

- Reconciled all explicit Event 018 event references against the English localisation database.
- Reconciled all rendered Event 018 decision and mission identifiers, custom tooltips, cost text families, and five workboard labels.
- Reconciled all 67 DHO focus title/description/tooltip families.
- Reconciled all 15 achievement name/description pairs and 19 tooltip references.
- Verified 20 Event 018 scripted-localisation blocks, 75 targets, shared history selectors, workboard scope, and integer display formatting.
- Re-ran duplicate-key, duplicate-value, forbidden-style, and UTF-8 BOM checks after the repair.
- Compared the canonical Event 018 CSV row with live Event Details, evolution, world-end, event-name, and cluster localisation.

## Skipped meaningful validation

- Hearts of Iron IV was not launched. Live font wrapping, hover-tooltip expansion, decision-list layout, runtime scripted-localisation evaluation, event-log clicks, super-event playback, and achievement display remain unobserved.
- The MCP renderer cannot evaluate every native scripted-localisation result without supplied scenario overrides. Source reconciliation covers those selectors, but it is not engine execution.
- The workbook was not edited or rendered because spreadsheet ownership was explicitly outside this task.

## Unresolved wording decisions

The only unresolved wording decision is ownership of the catalog mismatch: either copy the live Event Details and evolution wording into `Events!C19:G19`, or explicitly approve catalog-specific expanded summaries and revise the repository acceptance statement. No in-game Event 018 wording decision remains unresolved.

## Simplifications, omissions, fallbacks, and blockers

- No localisation fallback, placeholder, or simplification was introduced.
- No Event 018 key, scripted-localisation mapping, dynamic token, or sourced quotation was omitted.
- Catalog/in-game wording equality remains blocked outside this task's write scope.
- MCP event inspection remains partial because the adapter deferred workspace-wide helper and lifecycle projection.
- Live engine presentation remains outside agent validation.

No additional improvement-loop plan was written because the finding is a bounded spreadsheet reconciliation issue, not a design-depth gap.
