# Event 014 localisation completion audit, 2026-08-26

## Scope and result

This bounded pass audited `localisation/english/014_cannibalism_l_english.yml`, `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`, and the Event 014 event, decision, focus, and scripted-GUI consumers needed to verify those strings.

The audit found one concrete display defect and patched it in three localisation keys. The affected aftermath strings used the nonexistent `£train_equipment_text_icon` token. They now use vanilla's registered `£GFX_train_texticon` token. No gameplay, decision logic, GUI layout, focus, asset, portrait, model, super-event art or audio, achievement definition, or spreadsheet file was edited.

The two owned source files already had shared uncommitted work at the start of this pass. That work was preserved and audited in place. The pass did not rewrite or revert it.

## Counts and coverage

- Event 014 localisation file: 2,038 unique keys across 2,188 physical lines.
- Scripted localisation file: 44 unique `defined_text` selectors and 119 `localization_key` outputs. Two outputs are deliberate GFX sprite tokens used by tab-sprite selectors, leaving 117 ordinary localised-text outputs.
- Event references checked: 110 explicit Event 014 title, description, option, and tooltip keys.
- Decision surfaces checked: 127 top-level decision or mission IDs and their base descriptions.
- Decision category surfaces checked: 13 category IDs and their base descriptions.
- GUI surfaces checked at source level: 66 text, button, and tooltip keys across five Event 014 windows.
- Focus surfaces checked at source level: 207 focus IDs and descriptions across the unified, warlord, and Wendigo trees. The three tree-root IDs correctly have names without `_desc` keys.
- Cost-text surfaces: 91 keys. Eighty-eight contain direct semantic icons. Two delegate to scripted-localisation cost selectors that return icon-bearing text. The remaining mission note explains that launch and press costs are paid separately and is not itself a price list.
- Sourced quotation surfaces preserved: four super-event quotation keys, `chaosx_super_event.49.q`, `.50.q`, `.52.q`, and `.53.q`.

## Missing, duplicate, scripted-localisation, and encoding audit

- Missing key list: none in the audited event, decision, category, GUI, focus, or scripted-localisation consumers.
- Duplicate key list: none within the Event 014 localisation file and none across other English localisation files for the 2,038 Event 014 keys.
- Duplicate scripted-localisation selector list: none.
- Broken scripted-localisation reference list: none. Every dynamic `[Get...]` call in the Event 014 localisation file resolves to a defined selector. Every ordinary `localization_key` output resolves to English localisation. `GFX_chaosx_sort_button_100x29_2` and `GFX_sort_button_100x29` are deliberate sprite-return values, not missing text keys.
- File encoding concerns: none. The `.yml` file is strict UTF-8 with BOM (`EF BB BF`). The scripted-localisation `.txt` file is strict UTF-8; it does not require a localisation-file BOM.
- Malformed localisation entries: none. All non-comment content is either the `l_english:` header or a valid one-line key/value entry.

## Changed files and keys

Files changed by this pass:

- `localisation/english/014_cannibalism_l_english.yml`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_localization_completion_2026-08-26.md`

Keys changed by this pass:

- `cannibalism_aftermath_institution_requirements_tt`
- `cannibalism_aftermath_institution_cost_text`
- `cannibalism_compact_ratification_cost_text`

Before, each key rendered a nonexistent `£train_equipment_text_icon` token where the train cost or readiness reserve should appear. After, each uses the registered vanilla `£GFX_train_texticon`, so the train cost has the intended semantic icon.

The shared localisation diff contained 31 changed keys after this pass. The audit covered all of them, including the four new origin-specialist equipment strings, `cannibalism_raise_origin_specialist_cost_text`, the remaining semantic cost strings, `cannibalism_unified_player_mission_slots_tt`, and the three train-token fixes above. The pre-existing scripted-localisation diff adds `GetCannibalismOriginSpecialistEquipmentCost`. This pass verified its Island Host, Siege Commune, March Host, and generic fallbacks and did not alter it.

## Dynamic text opportunities and cross-surface consistency

- Dynamic localisation added by this pass: none.
- Dynamic localisation audited and retained: `GetCannibalismOriginSpecialistEquipmentCost`, `GetCannibalismRationAuditCost`, `GetCannibalismLogisticsCost`, spread source and route selectors, GUI list selectors, and the achievement tracker selectors.
- Additional required dynamic-text opportunities: none found. Existing state, country, target, timer, cost, and meter tokens already preserve the relevant live values.
- Cross-surface mismatch notes: none after the train-token repair. All 66 GUI keys resolve, all 127 decision or mission IDs and 13 categories have base names and descriptions, all 204 focus nodes have names and descriptions, and the three tree-root IDs have their required names.

## Reveal secrecy and retired-origin audit

- Live runtime and localisation matches for `Prison Host`, `prison_host`, `origin_prison`, `warlord_prison_`, `lockhouse`, and `lock_house`: zero under `common/`, `events/`, `history/`, `interface/`, and `localisation/`.
- The early header, network ledger, and warlord command GUI blocks explicitly require that `cannibalism_reveal_complete` is absent.
- The revealed command and Wendigo command GUI blocks explicitly require `cannibalism_reveal_complete`.
- Events `chaosx.nr14.70` through `.77` and captured-Hannibal event `.81` gate their revealed-name text behind `cannibalism_reveal_complete`.
- Achievement tracker 13 requires `cannibalism_reveal_complete`; tracker 16 requires the recorded Wendigo merge. Their underlying achievements are hidden.
- No direct `Hannibal Lecter` text is consumed by a pre-reveal Event 014 decision or scripted GUI surface. Internal identifiers containing `hannibal` or `wendigo` remain script-only.

## Prose-quality audit and before/after summary

- Vagueness: no in-scope passage required a rewrite. Requirements and outcomes name concrete actors, states, resources, meters, and consequences.
- Bloat: several complex requirement tooltips are long because they enumerate distinct dynamic reserves, target conditions, and readiness-only resources. Removing those details would obscure gameplay meaning. No redundant sentence was removed.
- Obvious explanation: no title-repeating or button-narration defect justified a rewrite. The three patched strings changed only a broken icon token.
- Repetition: no repeated sentence or duplicated tooltip content justified a rewrite.
- Overcomplication: no wording change was made. The longest requirement strings remain mechanically dense, but their costs and readiness rules are concrete and cannot safely be shortened without changing player information.
- Style-rule repair: the player-facing file contains no em dash and no sentence semicolon. Pattern checks found no thesis-antithesis-synthesis template, staccato chain, prompt fragment, implementation history, or tuning-history prose requiring repair.

The four sourced quotation keys were preserved byte-for-byte by this pass. Their historical punctuation and capitalization were not normalized. All dynamic tokens, formatting codes, state and country calls, values, costs, and named consequences were preserved except for the three intentional train-icon token substitutions.

## Meaningful validation and MCP evidence

- A strict key-resolution audit confirmed zero missing event, decision, category, GUI, focus, or ordinary scripted-localisation keys and zero duplicate Event 014 English keys.
- A strict UTF-8 decode and BOM inspection confirmed the localisation file remains UTF-8 with BOM after the patch.
- A full text-icon resolution pass across mod and installed vanilla interface definitions confirmed all 21 distinct Event 014 `£` tokens now resolve. Before the patch, `train_equipment_text_icon` was the sole unresolved token.
- A targeted Event Chain Viewer inspection of `chaosx.nr14.1` completed with partial status and returned `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ce9fa6f55260fcf0f13c83c434b9d4816f8c97af4b1c56ef45211e821701c60/a46aa56c5f6c90a9f9e9cbda9d6616f56ca925a0b0768fd54846d9fad85d7de3/event-trace-43388d6b2737.json`.
- The matching options render completed with partial status. Its manifest URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8c950a8e88e55491e5fd22b01e6493a9bde62dcb5d3b3c35ba003c00cf61bc5/7aa6fa3df970b402a29de9077c1357438d1a52b56965851f99b8955ef1fb34df/event-options-43388d6b2737-manifest.json`; source-linked SVG and PNG artifacts were also produced.

## Skipped or blocked meaningful validation

- Event artifact bodies could not be reopened through the resource route because the server reported `Artifact provenance manifest is unavailable`. The URIs remain useful identifiers, but their bodies were not treated as reviewed evidence.
- `hoi4.gui_inspect` timed out after 180 seconds for `cannibalism_early_header_window`. A parallel attempt covering all five Event 014 windows also failed to return and was terminated. Therefore source-level key coverage, dimensions, reveal gates, and text lengths were checked, but MCP-rendered long-text and overflow acceptance is unresolved. Source-only review is not treated as equivalent visual evidence.
- `hoi4.focus_inspect` timed out after 180 seconds for `common/national_focus/014_cannibalism_focus.txt`. Focus name and description coverage was verified from source, but MCP focus diagnostics and rendered overflow evidence are unresolved.
- The installed package has no Technology Tree Viewer route available for this localisation agent. Event 014 bridge-technology name coverage was checked from source only; no technology-tree visual claim is made.
- No in-game display validation was performed. Live consumer validation remains with the user and parent agent.

## Unresolved wording decisions, blockers, and simplifications

No wording decision remains unresolved. The unresolved evidence blockers are the GUI and focus MCP timeouts, the unavailable event-artifact provenance manifest, and the absent Technology Tree Viewer. No fallback wording, gameplay simplification, hidden-name exposure, retired Prison Host identity, or sourced-quotation alteration was introduced.

No additional design-gap plan was written.
