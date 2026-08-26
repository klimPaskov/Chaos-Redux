# Event 006 small-file merge continuation

Date: 2026-08-26

Status: source-layout complete, runtime behavior intentionally unchanged.

## Scope

This continuation removes eight clean, same-surface Event 006 parser files while preserving every executable decision block, category identifier, sprite identifier, texture path, effect file, cost value, and package source boundary.

## Decision registry

`common/decisions/006_independence_wave_balkan_decisions.txt` now contains the Banat, Bosnia, Epirus, Macedonia, Montenegro, Thrace, and Transylvania source blocks.

The receiver preserves seven category roots, 83 decision blocks, and fourteen file-local civilian-factory constants.

Montenegro constants are renamed to `CR_SC_INDEPENDENCE_WAVE_MNT_DECISION_COST_CIVILIAN_FACTORY_LIGHT` and `CR_SC_INDEPENDENCE_WAVE_MNT_DECISION_COST_CIVILIAN_FACTORY_STANDARD`.

Transylvania constants are renamed to `CR_SC_INDEPENDENCE_WAVE_TRA_DECISION_COST_CIVILIAN_FACTORY_LIGHT` and `CR_SC_INDEPENDENCE_WAVE_TRA_DECISION_COST_CIVILIAN_FACTORY_STANDARD`.

The aliases are file-local names inside the receiver and do not alter any gameplay value.

Removed parser files:

- `common/decisions/006_independence_wave_montenegro_decisions.txt`
- `common/decisions/006_independence_wave_transylvania_decisions.txt`

The decision receiver plus the two removed files save 985 source bytes after redundant package banners are condensed.

Kosovo remains in its own decision file because its package trigger surface is an active working-tree repair.

## GFX registry

`interface/006_independence_wave_small_assets.gfx` now also contains the clean FORM-03, Pacific, Mediterranean, IW-043/IW-058, Rhineland/Bavaria, and Wallonia/Frisia sprite blocks.

The receiver contains one `spriteTypes` wrapper, six source markers, and 264 unique sprite identifiers.

Every moved sprite retains its original texture path, optional `effectFile`, and identifier.

Removed parser files:

- `interface/006_independence_wave_form03.gfx`
- `interface/006_independence_wave_iw043_iw058_focus_icons.gfx`
- `interface/006_independence_wave_mediterranean_assets.gfx`
- `interface/006_independence_wave_pacific_focus_icons.gfx`
- `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- `interface/006_independence_wave_wallonia_frisia_assets.gfx`

The receiver plus the six removed files save 605 source bytes.

## Validation

The pre-merge GFX inventory contained 264 names with zero duplicates across the receiver and six source files.

The post-merge receiver contains 264 unique names and one `spriteTypes` wrapper.

The post-merge Balkan decision receiver contains seven unique category roots, 83 unique decision blocks, and no unscoped legacy Montenegro or Transylvania constant names.

The six maintained Event 006 static validators are run after this source-layout change.

Bounded Event MCP inspection and rendering are refreshed after the static pass.

This handoff does not claim live game loading, save/load, tooltip observation, or in-game asset rendering.

## Remaining boundaries

The Kosovo decision file, achievement on-action file, country shells, large package registries, and active package-owned files remain separate because their current ownership or engine callback boundaries are not part of this continuation.

No package admission, allocation ladder, decision cost, timer, trigger, effect, AI, focus, localisation, portrait, flag, or runtime transaction boundary changes in this source-layout pass.
