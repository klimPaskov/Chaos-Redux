# Event 006 focus, GUI, and scenario scripted-localisation registry merge — 2026-08-25

## Scope and outcome

The three remaining small Event 006 scripted-localisation parser files are now folded into the existing registry:

- `006_independence_wave_focus_scripted_localisation.txt`
- `006_independence_wave_gui_scripted_localisation.txt`
- `006_independence_wave_scenario_scripted_localisation.txt`

Their 24 `defined_text` blocks are preserved under source markers in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`. The former parser files are removed. The registry now contains 58 unique Event 006 selector names and six source sections with no duplicate names.

## Validation

- The registry remains UTF-8 with BOM.
- The registry has 58 `defined_text` blocks, 58 unique `name` values, and balanced braces (`1196` opening and `1196` closing braces).
- Each former file's complete executable body, from its first `defined_text` block through its final block, is present byte-for-byte after normalizing the original trailing whitespace.
- The former source files total 35,308 bytes; the receiver is 95,844 bytes after the merge, for a net source-tree saving of 9,330 bytes when the pre-merge 59,866-byte receiver is included in the comparison.
- No focus, GUI, scenario, package, event, decision, or admission identifier changed. No live parser, GUI render, scenario execution, or save/load receipt is claimed.

## Boundary

This is a source-layout consolidation only. Focus-title selection, status-panel text, SCN-008 summary text, branch order, scopes, localisation keys, fallback behavior, and the Event 006 `32/161` admission boundary remain unchanged. Package-local scripted-localisation files remain separate where their ownership or active edits require it.
