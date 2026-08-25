# Event 006 Balkan localisation registry — 2026-08-25

## Scope and outcome

The seven Balkan package localisation files for Banat, Bosnia, Epirus, Macedonia, Montenegro, Thrace, and Transylvania now share `localisation/english/006_independence_wave_balkan_l_english.yml`.

The former seven parser files are removed. Kosovo remains separate because its active cost-localisation repair is an owned worktree change.

Each source section is retained under a `# SOURCE` marker beneath one `l_english:` root. The package-local wording, dynamic values, cost displays, party names, ideas, decision text, and character text remain intact.

## Validation

- The registry has one UTF-8-BOM `l_english:` root, seven source markers, 439 localisation keys, and zero duplicate keys.
- All seven committed source inventories compare with no missing or mismatched key/value pairs after line-ending and indentation normalization.
- Current Banat, Bosnia, Macedonia, and Montenegro package notes now point to the registry and identify their sections.
- No package trigger, effect, decision, focus, AI, admission, or Kosovo lifecycle behavior changed.
- No live localisation parser, UI render, or save/load receipt is claimed.

## Boundary

This is a source-layout consolidation only. The seven Balkan packages retain their existing identity, map, host, cost, and fail-closed admission contracts.
