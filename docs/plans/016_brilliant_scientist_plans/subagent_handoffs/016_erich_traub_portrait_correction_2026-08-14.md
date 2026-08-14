# Erich Traub portrait correction handoff

Date: 2026-08-14.

## Outcome

The user identified `6925d2612b927.image_00001.dds` as Erich Traub. The supplied `156x210` DDS now replaces `gfx/leaders/scientists/portrait_GER_erich_traub.dds` byte-for-byte while preserving the existing `GER_erich_traub` character, `GFX_portrait_GER_erich_traub` sprite, specialization, skill, trait, localisation, identity flag, and startup recruitment.

The second anonymous input, `s-l1200_00001.dds`, is explicitly ignored. It is retained under `docs/assets/portraits/016_brilliant_scientist/not_needed/s-l1200_00001/` for audit continuity and has no identity, sprite, runtime path, character, or recruitment consumer.

## Asset and evidence files

- Runtime DDS: `gfx/leaders/scientists/portrait_GER_erich_traub.dds`.
- Durable Traub package: `docs/assets/portraits/016_brilliant_scientist/subjects/GER_erich_traub/`.
- Independent converter output: `docs/assets/portraits/016_brilliant_scientist/conversion_qa/portrait_GER_erich_traub_converted.dds`.
- Updated manifest and QA: `manifest.md`, `input_mapping.json`, `conversion_qa_summary.json`, and `checksums.sha256` in the portrait package root.
- Updated visual evidence: `contact_sheets/installed_scientists_native_contact_sheet.png` and `contact_sheets/installed_scientists_4x_contact_sheet.png`.

## Validation

The supplied source, durable original, independent converter output, and runtime DDS are byte-identical with SHA-256 `71d437dfe1466c0a86ef33800363aeec9963bcfae042aab09792ae0a9bf8ab59`.

The DDS is a strict one-level uncompressed BGRA texture with dimensions `156x210`, pitch `624`, opaque alpha, header flags `0x100F`, pixel-format flags `0x41`, and caps `0x1000`.

Parent review of the native and 4x installed-runtime sheets passed framing, canvas integrity, transparency, conversion quality, and consistency with the existing painted scientist portrait family.

The final package contains 66 installed identities: 20 replacements and 46 new portraits, plus 4 archived alternates, zero blocked inputs, and one explicit `not_needed` input.

No shared `.gfx`, gameplay, character, startup, localisation, advisor-card, trait, skill, decision, event, AI, or UI file was changed for this correction.
