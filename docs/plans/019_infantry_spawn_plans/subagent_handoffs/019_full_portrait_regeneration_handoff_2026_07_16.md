# Event 019 Army/Host Identity-Scene Regeneration Handoff

Date: 2026-07-16

Mode: patch-capable visual-asset production and source-of-truth documentation reconciliation

## Supersession authority

This is the current visual handoff for all 26 fixed Event 019 portrait slots. It supersedes every earlier Event 019 claimant/derivative human-portrait visual assessment, correction tranche, facial-identity description, and contact-sheet conclusion. Gameplay characters, fictional male names, regional male name pools, male-default leader metadata, archetype assignments, profile gates, filenames, sprite identifiers, and GUI consumers remain unchanged. Historical gameplay/name/gender audits remain useful only for those nonvisual contracts.

## Delivered visual contract

- Claimant slots C01-C20 each show a different regional army or muster scene.
- Derivative slots D01-D06 show massed zombie, ghost, or golem hosts; council-labelled slots express governance as exactly three massed formations or cohorts.
- No retained source, processed PNG, runtime DDS, or review-sheet panel has an individual focal human/person.
- All 26 fixed technical source filenames, processed filenames, runtime DDS filenames, `GFX_portrait_*` identifiers, 156x210 dimensions, claimant region/profile contracts, and derivative role bindings are preserved.
- No gameplay, localisation, name metadata, GUI, `.gfx`, workbook, CSV, or registry file was edited by this tranche.

## Skills and references

- `chaos-redux-event-assets`: source policy, visual contract, processing, DDS delivery, contact sheets, provenance, manifest alignment, and handoff requirements.
- `imagegen`: one separate built-in ImageGen call for every retained source.
- Required offline wiki core pages plus Interface Modding, installed vanilla portrait sprite precedents, and the canonical Event asset skill vanilla leader contact sheet were consulted. Vanilla art was used only for scale/style comparison, never as a retained source.

## Source production

The final tranche used 27 built-in ImageGen calls: 26 retained originals and one rejected C13 draft whose standards resembled a real national emblem. The rejected draft was never copied into the repository; a separate, symbol-free C13 original replaced it. No retained source was reused, transformed, recoloured, composited, or supplied as a fallback for another slot.

Retained concepts:

- C01-C04: European railhead logistics muster; frozen river bridgehead; oasis-fort defensive ring; monsoon port-and-rail fan.
- C05-C08: winter horse-artillery arrowhead; monsoon floodplain crossing; snowy forest infiltration echelons; highland pack-artillery chevron.
- C09-C12: industrial tram-square front; winter industrial artillery grid; plateau-canyon shield formation; amphibious wavefront.
- C13-C16: symbol-free coastal-cliff artillery zigzag; machineworks checkerboard blocks; storm-savanna mobile echelon; desert mobile crescent.
- C17-C20: blackout bicycle street grid; frozen-fjord ski envelopment; hurricane-delta levee zigzag; Australian outback motor hook.
- D01-D06: massed undead army wall; exactly three undead legion masses; massed spectral spearhead; exactly three spectral formations; collective quarry builder-host; exactly three geological cohorts.

Exact output ids, normalized reproduction directions, source paths, and source hashes are in `docs/assets/019_infantry_spawn/prompts/claimant_portrait_reproduction_specs_2026_07_16.md`.

## Runtime delivery

- 20 claimant sources: `docs/assets/019_infantry_spawn/source_png/portraits/claimants/`.
- 6 derivative sources: `docs/assets/019_infantry_spawn/source_png/portraits/derivatives/`.
- 26 processed 156x210 PNGs: `docs/assets/019_infantry_spawn/processed_png/portraits/`.
- 26 runtime 156x210 DDS files: `gfx/leaders/019_infantry_spawn/`.

The retained processor performs a centered cover crop to 156x210, then applies contrast 1.04, colour 0.90, and sharpness 1.04. DDS conversion uses legacy uncompressed 32-bit BGRA. Processing adds no subject replacement, composition, recolour derivative, or fallback.

## Review artifacts

- `docs/assets/019_infantry_spawn/contact_sheets/event_019_claimant_source_contact_sheet.png`
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_claimant_processed_contact_sheet.png`
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_derivative_portrait_source_contact_sheet.png`
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_derivative_portrait_processed_contact_sheet.png`
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_derivative_portrait_contact_sheet.png` (synchronized legacy processed-derivative path)

The source and processed review sheets show the full 20+6 formation set without human leader reference panels. Parent visual review approved the set at source and runtime size for army/host readability and absence of an individual focal subject.

## Source-of-truth reconciliation

Current visual wording is aligned across the Event 019 asset manifest, exact crosswalk, identity metadata, reproduction/provenance record, GFX handoff, possessed-general matrix, country-package matrix, asset prompt, acceptance spec, core/evolution/UI specs, asset inventory, current review/prompts, and this handoff. Historical human-portrait audits are retained but carry explicit supersession notices directing readers here.

## Meaningful validation

- 26/26 repository sources are byte-identical to their recorded retained ImageGen outputs.
- Source, processed, and DDS stages each contain 26/26 unique hashes.
- 26/26 processed PNGs and runtime DDS files are 156x210.
- 26/26 DDS files are valid legacy uncompressed 32-bit BGRA and exactly 131168 bytes.
- 26/26 processed PNG/DDS pairs are decoded-pixel-equal.
- All six required review sheets exist; exact hashes are recorded in `docs/assets/019_infantry_spawn/notes/claimant_portrait_asset_crosswalk_2026_07_16.md`.
- Fixed sprite registrations and texture paths remain unchanged and were not edited.

## Simplifications, omissions, and blockers

None. All 26 requested slots have separate generated sources, processed PNGs, runtime DDS files, contact-sheet evidence, exact provenance, crosswalk entries, and reconciled current documentation. No fallback, placeholder, source reuse, transformed duplicate, individual focal portrait, gameplay edit, localisation edit, name-metadata edit, registry edit, workbook edit, or sprite-definition edit was used.
