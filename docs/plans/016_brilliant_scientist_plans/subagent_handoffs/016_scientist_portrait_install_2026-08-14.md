# Scientist portrait installation handoff

Date: 2026-08-14.

Scope: bounded installation of the user-supplied scientist portrait finals from `C:\Users\klimp\Downloads\scientists`.

## Result

The supplied directory contained 71 DDS files rather than the requested 70, and contained no other input file type. All 71 were audited. Following the user's identity correction, 66 unique identities are installed, four duplicate candidates are retained as alternates, and one anonymous file is retained as explicit `not_needed` evidence. The full per-file manifest is `docs/assets/portraits/016_brilliant_scientist/manifest.md` with machine-readable evidence in `input_mapping.json`.

All installed scientist textures are exact `156x210` one-level uncompressed BGRA DDS files under `gfx/leaders/scientists/portrait_<ID>.dds`. The 20 existing runtime IDs were preserved and their supplied finals replaced the old DDS bytes. The 46 identities without an existing sprite received stable `GFX_portrait_<ID>` definitions and texture paths in `interface/_scientists_portraits_additions.gfx`; no character definition, recruitment, traits, skills, history, decisions, events, AI, or localisation was edited for them.

## Identity decisions

- Edwin Broun Fred: source 01 installed; source 02 archived as an alternate.
- Karl Friedrich Meyer: canonical filename installed; the `(1)` candidate is byte-identical and archived as an alternate.
- Masaji Kitano: source 02 installed after comparison with the Commons reference; source 01 archived as an alternate.
- Rudolf Weigl: source 01 installed after comparison with archived Weigl references; source 02 archived as an alternate.
- `Sigmund_Rascher_child_00001.dds`: resolved to `GER_sigmund_rascher` from filename and source-caption evidence.
- `Gutzeit-15_00001.dds`: resolved to `GER_kurt_gutzeit` from the existing repository consumer and Federal Archive/Commons comparison.
- `6925d2612b927.image_00001.dds`: identified by the user as Erich Traub and installed byte-for-byte for the existing `GER_erich_traub` consumer.
- `s-l1200_00001.dds`: explicitly ignored by the user and retained under `not_needed/` without an identity or runtime assignment.

The earlier ambiguous comparison sheets remain historical evidence. The corrected installed-runtime native and 4x contact sheets include Traub, and no identity is inferred for the ignored input.

## Existing consumers

Existing portrait references remain on their stable IDs and are listed per identity in `input_mapping.json`. Eleven accepted replacements also had static 65x67 CBRN advisor-card consumers. Those cards were regenerated from the accepted user-supplied 156x210 PNGs with `.agents/skills/chaos-redux-event-assets/tools/create_advisor_icon.py` and the canonical advisor template. `POL_franciszek_witaszek` remains unchanged because no accepted input targets him. Erich Traub has no advisor-card consumer. No card was created for new scientist-only identities. Card hashes and review artifacts are in `advisor_cards_manifest.json`.

## Evidence and QA

- `research_sources.md` records identity references, source mode, the unresolved redistribution-rights caveat for supplied styled-final bytes, duplicate rationale, and ambiguous-file evidence.
- `checksums.sha256` records every observed input and every installed runtime DDS.
- Every selected identity has a durable source package containing the unchanged supplied DDS, exact full-canvas crop JSON/PNG, processed 156x210 PNG, and completed provenance contract under `docs/assets/portraits/016_brilliant_scientist/subjects/<ID>/`.
- Native and 4x review sheets cover all 71 inputs: `contact_sheets/scientists_native_contact_sheet.png` and `scientists_4x_contact_sheet.png`. Installed-runtime sheets are `contact_sheets/installed_scientists_native_contact_sheet.png` and `installed_scientists_4x_contact_sheet.png`.
- `convert_to_dds.py` was run against all 66 processed PNGs. All 66 converter outputs passed the strict BGRA header/length check, decoded pixel equality, and byte equality with the supplied runtime finals. Converter outputs are retained in `conversion_qa/`; runtime textures preserve the supplied bytes.
- Regenerated advisor-card native and 4x review sheets are `contact_sheets/scientist_advisor_cards_native_contact_sheet.png` and `scientist_advisor_cards_4x_contact_sheet.png`.

## Parent review points

Review `manifest.md`, `input_mapping.json`, the native/4x contact sheets, and `interface/_scientists_portraits_additions.gfx`. New identities are intentionally asset-only and require gameplay owners to decide whether/where to create their character definitions. The supplied-final rights status is internal-installation authorization only; external redistribution rights were not supplied.
