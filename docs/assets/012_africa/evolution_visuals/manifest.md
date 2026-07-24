# Event 012 Africa Evolution Visual Asset Manifest

## Scope and result

This package supplies all six distinct static visual assets required by `docs/events/012_africa_evolutions.md`: three report-event images and three Event Log evolution-detail portraits. Every asset has an original generated source master, an exact-size processed PNG, a final DDS at the path already registered in `interface/012_africa_evolutions.gfx`, a generation record, and a decoded-DDS review copy.

The three incident images show African actors directing logistics, administration, and diplomacy. The three revised portrait-token assets identify collective institutions through active fictional ensembles, working surfaces, and stage-specific anomalies instead of assigning a real ruler or random solitary face to a council, secretariat, or delegation.

No alias, placeholder, recolour, generic reuse, or fallback is present. No gameplay, event, localisation, scripted-localisation, GUI, or GFX source was edited by this asset tranche.

## Package layout

| Surface | Location | Purpose |
| --- | --- | --- |
| Original generated masters | `source_png/` | Unchanged high-resolution built-in ImageGen outputs |
| Processed masters | `processed_png/` | Exact 210 x 176 report cards and 156 x 210 institutional portraits |
| Live report textures | `gfx/event_pictures/012_africa/evolutions/` | Final registered report-event DDS files |
| Live portrait textures | `gfx/leaders/012_africa/evolutions/` | Final registered Event Log detail DDS files |
| Generation ledger | `provenance/generation_records.md` | Tool-output handles, hashes, dimensions, and retained production briefs |
| Processing record | `provenance/processing_and_validation.md` | Deterministic processing and DDS validation details |
| Requirement proof | `coverage_crosswalk.md` | Source requirement, consumer, sprite, and texture mapping |
| Existing-wiring proof | `gfx_handoff.md` | Verification of the six already-registered sprite definitions |
| Review sheet | `contact_sheets/evolution_visuals_source_processed_dds_contact_sheet.png` | Source, processed, and decoded-DDS comparison |
| Review record | `contact_sheets/contact_sheet_review.md` | Visual, representation, and distinctness findings |
| Validation ledger | `validation/evolution_visuals_validation.tsv` | Exact dimensions, alpha, DDS headers, hashes, and pixel equality |

## Format contract

- Report events: 210 x 176 PNG and DDS, transparent sepia archival report-card treatment.
- Log details: 156 x 210 PNG and DDS, opaque institutional portrait treatment.
- DDS format: legacy uncompressed 32-bit BGRA 8:8:8:8, no FourCC compression and no mipmaps.
- DDS caps: `DDSCAPS_TEXTURE`.
- Report DDS size: 147,968 bytes each.
- Portrait DDS size: 131,168 bytes each.

## Asset index

| Evolution | Surface | Registered sprite | Original source | Processed PNG | Final DDS | Primary visual read | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I - Regional Consolidation | Incident | `GFX_report_event_012_africa_evolution_regional_consolidation` | `source_png/report_event_012_africa_evolution_regional_consolidation_source.png` | `processed_png/report_event_012_africa_evolution_regional_consolidation.png` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_regional_consolidation.dds` | African delegates and railway workers reconcile obligations at a working freight corridor | Complete and registered |
| II - Continental Machinery | Incident | `GFX_report_event_012_africa_evolution_continental_machinery` | `source_png/report_event_012_africa_evolution_continental_machinery_source.png` | `processed_png/report_event_012_africa_evolution_continental_machinery.png` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_continental_machinery.dds` | African clerks and planners operate a busy continental secretariat | Complete and registered |
| III - Africa as a World Pole | Incident | `GFX_report_event_012_africa_evolution_world_pole` | `source_png/report_event_012_africa_evolution_world_pole_source.png` | `processed_png/report_event_012_africa_evolution_world_pole.png` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_world_pole.dds` | An African delegation arrives as the central diplomatic party at an international airfield | Complete and registered |
| I - Regional Consolidation | Event Log detail | `GFX_portrait_012_africa_evolution_regional_council` | `source_png/portrait_012_africa_evolution_regional_council_source.png` | `processed_png/portrait_012_africa_evolution_regional_council.png` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_regional_council.dds` | A storm council negotiates over a living rail map beneath an impossible continental thunderhead | Complete, revised, and registered |
| II - Continental Machinery | Event Log detail | `GFX_portrait_012_africa_evolution_continental_secretariat` | `source_png/portrait_012_africa_evolution_continental_secretariat_source.png` | `processed_png/portrait_012_africa_evolution_continental_secretariat.png` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_continental_secretariat.dds` | A night-shift secretariat contains an anomalous communications map emerging from period machinery | Complete, revised, and registered |
| III - Africa as a World Pole | Event Log detail | `GFX_portrait_012_africa_evolution_world_pole_delegation` | `source_png/portrait_012_africa_evolution_world_pole_delegation_source.png` | `processed_png/portrait_012_africa_evolution_world_pole_delegation.png` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_world_pole_delegation.dds` | A three-person delegation confronts the old powers beneath an eclipse and levitating globe | Complete, revised, and registered |

## Requirement reconciliation

The Event 012 asset/animation matrix has no explicit rows for these six evolution visuals. They are direct requirements in the authoritative evolution implementation document and already have exact live sprite registrations. `coverage_crosswalk.md` therefore maps the six assets to `docs/events/012_africa_evolutions.md`, their event or scripted-localisation consumers, and `interface/012_africa_evolutions.gfx` without inventing matrix rows or modifying the matrix.

## Provenance and rights

The report sources were generated specifically for this package with the built-in OpenAI image-generation tool on 2026-07-17. The three Event Log portraits were revised with the same built-in tool on 2026-07-24 using only this package's prior generated institutional-room masters as image guidance. The depicted people are fictional and no real-person likeness, external photograph, flag, emblem, third-party artwork, or mod asset was used in a final composition. Vanilla and repository assets were inspected only as technical and stylistic precedents.

The unchanged generated outputs are retained in `source_png/`; exact tool-output handles and SHA-256 hashes are recorded in `provenance/generation_records.md`.

## Review and validation result

The enlarged contact sheet confirms six separate compositions, clear stage progression, respectful human agency, dramatically distinct institutional identities, controlled supernatural escalation in the portrait slots, and full processed-to-DDS visual parity. The validation ledger confirms exact dimensions, correct legacy DDS headers, expected alpha behavior, and byte-identical RGBA pixels after DDS decoding.

There are no simplifications, omissions, fallbacks, or unresolved asset blockers in this six-file evolution package.
