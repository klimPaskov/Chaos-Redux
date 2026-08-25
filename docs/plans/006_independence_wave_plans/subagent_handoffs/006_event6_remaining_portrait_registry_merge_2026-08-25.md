# Event 006 remaining portrait-registry merge handoff

Date: 2026-08-25

## Scope

This source-layout pass consolidates the three remaining small Event 006 portrait sprite registries into `interface/006_independence_wave_portraits_registry.gfx`.

The removed source files are `interface/006_independence_wave_iw043_iw058_portraits.gfx`, `interface/006_independence_wave_mediterranean_portraits.gfx`, and `interface/006_independence_wave_region_01_portraits.gfx`.

The target preserves each source section with a source marker, the original sprite identifier, and the original runtime texture path.

## Preservation receipt

The moved definitions are eight IW-043/IW-058 institutional portraits, nine Mediterranean package portraits, and fourteen Northern/Western Europe package portraits, for 31 unique sprite/texture pairs.

The target registry now contains 53 unique sprite/texture pairs, with no duplicate sprite identifiers, no duplicate texture pairs, and no missing registered DDS texture paths.

No character token, `set_portraits` consumer, package gate, source-placeholder status, admission decision, or gameplay script changed.

## Documentation alignment

The IW-043/IW-058 signature-package note and Northern/Western Europe package note now point to `interface/006_independence_wave_portraits_registry.gfx`.

The Event 006 source-of-truth map and resume packet record this continuation as a portrait-registry consolidation and keep non-portrait package-owned GFX registries separate.

## Validation

The source-to-target comparison reconstructed the three removed registries from `HEAD` and found all 31 moved pairs in the target with no missing entries.

The target texture audit resolved all 53 registered texture paths to existing files.

The change is source-only and does not claim live HOI4 parser, rendering, save/load, or in-game portrait validation.

## Remaining boundary

The portrait archive and source-placeholder policy are unchanged, including the user-directed `docs/assets/portraits/006_independence_wave/` parent plus its single `processed/` child.

The Event 006 whole-event status remains HOLD / PARTIAL; this merge only reduces parser-file count and does not promote any package or portrait.
