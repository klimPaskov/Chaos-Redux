# Event 006 support-event and small-asset registry merge

Date: 2026-08-24

## Scope

This source-layout pass reduces parser-file overhead without changing gameplay ownership, event identifiers, sprite identifiers, texture paths, package admission, or the pre-event visibility boundary.

The three remaining same-namespace event files were folded into `events/006_independence_wave_support_events.txt`:

- `events/006_independence_wave_form01_02_04.txt`
- `events/006_independence_wave_wallonia_frisia.txt`
- `events/006_independence_wave_mediterranean.txt`

The support registry keeps one `add_namespace = chaosx.nr6` declaration. The moved event IDs retain their fully qualified names and executable bodies. SCN-008 remains separate because `events/006_independence_wave_scenario.txt` owns the `chaosx.triggerable_scenarios` namespace and delayed launch barrier. The larger Rhineland/Bavaria, IW-043/IW-058, IW-093/IW-098, and root event files remain separate for package ownership and audit readability.

Seven small GFX files were folded into `interface/006_independence_wave_small_assets.gfx`:

- `interface/006_independence_wave_form48.gfx`
- `interface/006_independence_wave_iw093_iw098_categories.gfx`
- `interface/006_independence_wave_iw093_iw098_ideas.gfx`
- `interface/006_independence_wave_iw093_iw098_portraits.gfx`
- `interface/006_independence_wave_pacific_portraits.gfx`
- `interface/006_independence_wave_iw043_iw058_idea_icons.gfx`
- `interface/006_independence_wave_event_pictures.gfx`

The combined registry has one `spriteTypes` container and source markers for each former file. Larger package-owned GFX registries remain separate.

## Preservation evidence

- Event ID comparison against the four pre-merge files: 37 unique IDs before and after, with no set difference.
- Sprite comparison against the seven pre-merge files: 31 unique names and 31 unique texture paths before and after, with no set difference.
- Brace balance: support events 355/355; small asset registry 32/32.
- Event 006 allocator audit passed with 149 publishers, 126 automatic/high-chaos selectors, 138 SCN-ranked selectors, 40 adapters, 32 attestations, and 29 compatible reservation groups.
- Strict flag-family, FORM-16, and Statehood Ledger semantic validators passed.
- `hoi4.event_inspect` on `chaosx.nr6.18` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4275cc2195182da071252c629c9a5cccbdcd35f76ff8f6c1f868f59f0803565/70f06b8310f8776f0c1e0a4272695848a55044a16459eb33ea265789c24a8f23/event-lint-8bc8b3313a85.json`.
- `hoi4.event_render` on `chaosx.nr6.18` returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics. Artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f0bdd3a8c8ee75433e70561e3b250d19692e44c230ac854770b810c9f36c032/05f392803425e46ed36aa4e4d24bfc04a7f8be24993adcc9e1a2770bb2f72252/event-neighborhood-8bc8b3313a85-manifest.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29e2baf7ee1cd10dec48fd7d8468dd48d8234e325048584b1ac18f19caa61546/25318bee1308f099a23610ddf0385fe9756979dad9a6f54f799be37630796eed/event-neighborhood-8bc8b3313a85.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4faa02b992c80d3c604715d8c44b23c0d063c494b4a2971eb9ac8c2a381426b4/add4d97953d634f4befcbaa4a6d72901442a43e01a548b2529cd0f525a220093/event-neighborhood-8bc8b3313a85.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ecdc75e3d244188d83591a7b7b98a07da0c120bc7c3577816b2f3a7eb9bea15/07699d5490ae09a3b6605c539287d184401c318ff239a80dc31440c844681f0a/event-neighborhood-8bc8b3313a85.png`.

## Boundary

This is a source-layout consolidation only. It does not promote any country package, alter admission or allocation, reintroduce a pre-event category/mission/cost, or claim live game execution. The whole Event 006 disposition remains HOLD / PARTIAL.
