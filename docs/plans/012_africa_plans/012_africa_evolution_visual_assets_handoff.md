# Event 012 Africa Evolution Visual Assets Handoff

## Delivered

All six evolution visuals required by `docs/events/012_africa/evolutions.md` are complete:

- three distinct 210 x 176 report-event DDS files at their registered `gfx/event_pictures/012_africa/evolutions/` paths;
- three distinct 156 x 210 collective-institution DDS files at their registered `gfx/leaders/012_africa/evolutions/` paths; and
- retained source masters, processed PNGs, decoded-DDS copies, provenance, manifest, coverage proof, contact-sheet review, and technical validation under `docs/assets/012_africa/evolution_visuals/`.

The incident sequence shows African actors directing corridor logistics, continental administration, and world diplomacy. The revised Event Log portrait sequence shows fictional collective institutions in action: a storm council over a living rail map, an anomalous communications secretariat, and a world-pole delegation confronting the old powers beneath an eclipse. No real ruler or arbitrary solitary person is made the identity of a collective institution.

## Runtime files

| Sprite | Final DDS | SHA-256 |
| --- | --- | --- |
| `GFX_report_event_012_africa_evolution_regional_consolidation` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_regional_consolidation.dds` | `04288afca1bcc034df2d2b7459956cde5ef508fce7590fe155bcbf585ad3b155` |
| `GFX_report_event_012_africa_evolution_continental_machinery` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_continental_machinery.dds` | `04ca4abd155bca382a55845a88a0ddcddc8ee652188f6b790602c8a1795ccc82` |
| `GFX_report_event_012_africa_evolution_world_pole` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_world_pole.dds` | `bd80b111a1b3578b2b710d826f408e8a5932418524dc4312eeed6b4fea5572f9` |
| `GFX_portrait_012_africa_evolution_regional_council` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_regional_council.dds` | `ff69732af159353e4c2d5a7fa154ba4a96c2d1ef56b759713b44e4bf2f69a410` |
| `GFX_portrait_012_africa_evolution_continental_secretariat` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_continental_secretariat.dds` | `4175d7c1ded251972bff1efe46476da0388db8f99c3ce7efb59f4b289b017aed` |
| `GFX_portrait_012_africa_evolution_world_pole_delegation` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_world_pole_delegation.dds` | `eabc8d99ff7f36366bf69bf183107950d5f3898f5c1e89e82b84898dd976568b` |

## Integration and validation

- `interface/012_africa_evolutions.gfx` already registers all six exact sprite/path pairs; no shared GFX edit is needed.
- Events `chaosx.nr12.401`, `.402`, and `.403` already consume the three report sprites.
- Event Log scripted localisation already maps Event 12 stages I-III to the three portrait sprites.
- Every DDS has the exact registered dimensions, uncompressed BGRA8 legacy header, expected alpha behavior, and a successful decode whose RGBA pixels exactly equal the processed PNG.
- The 1800 x 1480 source/processed/DDS contact sheet was visually reviewed and accepted after the dramatic revision.

Primary evidence:

- `docs/assets/012_africa/evolution_visuals/manifest.md`
- `docs/assets/012_africa/evolution_visuals/coverage_crosswalk.md`
- `docs/assets/012_africa/evolution_visuals/contact_sheets/contact_sheet_review.md`
- `docs/assets/012_africa/evolution_visuals/validation/evolution_visuals_validation.tsv`

No gameplay, event, localisation, scripted-localisation, GUI, or GFX source was edited. No commit was created. There are no aliases, placeholders, generic reuses, fallbacks, simplifications, omissions, or remaining blockers in this asset package.
