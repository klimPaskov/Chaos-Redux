# Event 006 package localisation registry continuation — 2026-08-25

## Scope and outcome

Three already-consolidated package families now have matching localisation registries:

- Siberian: Altai, Buryatia, Khakassia, and Sakha → `localisation/english/006_independence_wave_siberian_l_english.yml`
- Western/North Atlantic: Brittany, Catalonia, and Iceland → `localisation/english/006_independence_wave_western_l_english.yml`
- Bashkiria/Mari: Bashkiria and Mari → `localisation/english/006_independence_wave_bashkiria_mari_l_english.yml`

Nine former parser files are removed. Kosovo, Komi, Ruthenia, Tatarstan, Udmurtia, the active Rhineland/Bavaria localisation, and other ownership-sensitive surfaces remain separate.

## Validation

- The Siberian registry has one UTF-8-BOM root, four source markers, 333 unique keys, and zero duplicates.
- The Western/North Atlantic registry has one UTF-8-BOM root, three source markers, 208 unique keys, and zero duplicates.
- The Bashkiria/Mari registry has one UTF-8-BOM root, two source markers, 259 unique keys, and zero duplicates.
- All nine committed source inventories compare with no missing or mismatched key/value pairs after line-ending and indentation normalization.
- Altai, Sakha, and Mari package notes now point to their registry sections.
- No package trigger, effect, decision, focus, AI, admission, or runtime behavior changed.
- No live localisation parser, UI render, or save/load receipt is claimed.

## Boundary

This is a source-layout consolidation only. Package identity, dynamic cost wording, fail-closed admission, and runtime ownership remain unchanged.
