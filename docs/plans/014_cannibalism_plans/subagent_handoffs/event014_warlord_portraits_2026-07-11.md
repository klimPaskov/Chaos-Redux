# Event 014 Warlord Portrait Asset Handoff

Date: 2026-07-11

Subagent: `chaosx_generated_event_art`

Batch: `E14-POR-WARLORD-01`

## Result

Eight European-region base portrait packages are complete at the stable CBA-CBH paths: exactly two Island Host, two Siege Commune, two March Host, and two Prison Host candidates. Each slot has an independent built-in image-generation source, an exact-size processed PNG, a final uncompressed 32-bit BGRA DDS, prompt evidence, hashes, contact-sheet review, manifest entry, and exact GFX/character handoff. They are one regional subset of the later accepted 56-portrait matrix.

The portrait tranche used no fallback, reused portrait, local drawing, procedural blood overlay, real person, living-cultural regalia, sacred motif, or supernatural cue.

## Files changed

Final runtime portraits:

- `gfx/leaders/014_cannibalism/leader_CBA_warlord.dds`
- `gfx/leaders/014_cannibalism/leader_AHX_warlord.dds`
- `gfx/leaders/014_cannibalism/leader_CBC_warlord.dds`
- `gfx/leaders/014_cannibalism/leader_AIX_warlord.dds`
- `gfx/leaders/014_cannibalism/leader_CBE_warlord.dds`
- `gfx/leaders/014_cannibalism/leader_CBF_warlord.dds`
- `gfx/leaders/014_cannibalism/leader_AMX_warlord.dds`
- `gfx/leaders/014_cannibalism/leader_CBH_warlord.dds`

Asset package:

- `docs/assets/014_cannibalism/warlord_portraits_imagegen/source_png/` — eight independent generated source PNGs
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/processed_png/` — eight `156x210 RGBA` processed PNGs
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/contact_sheets/` — vanilla reference, source review, processed review, actual-size review, and DDS-decoded review sheets
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/prompts/warlord_portrait_prompts.md` — creative brief and first-pass record
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/prompts/accepted_production_prompts.md` — exact accepted prompt and source-path record
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/generation_attempts.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/processing.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/validation.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/hashes.sha256`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/manifest.md`
- `docs/assets/014_cannibalism/warlord_portraits_imagegen/gfx_handoff.md`

Event asset index:

- `docs/assets/014_cannibalism/manifest.md` — added the portrait package, live-output family, and handoff links

This file is the required subagent handoff under the Event 014 plans folder.

## Exact identities and sprites

| Slot | Origin assignment | Exact expected sprite | Final texture |
| --- | --- | --- | --- |
| CBA | Island Host candidate 1 | `GFX_portrait_CBA_warlord` | `gfx/leaders/014_cannibalism/leader_CBA_warlord.dds` |
| AHX | Island Host candidate 2 | `GFX_portrait_AHX_warlord` | `gfx/leaders/014_cannibalism/leader_AHX_warlord.dds` |
| CBC | Siege Commune candidate 1 | `GFX_portrait_CBC_warlord` | `gfx/leaders/014_cannibalism/leader_CBC_warlord.dds` |
| AIX | Siege Commune candidate 2 | `GFX_portrait_AIX_warlord` | `gfx/leaders/014_cannibalism/leader_AIX_warlord.dds` |
| CBE | March Host candidate 1 | `GFX_portrait_CBE_warlord` | `gfx/leaders/014_cannibalism/leader_CBE_warlord.dds` |
| CBF | March Host candidate 2 | `GFX_portrait_CBF_warlord` | `gfx/leaders/014_cannibalism/leader_CBF_warlord.dds` |
| AMX | Prison Host candidate 1 | `GFX_portrait_AMX_warlord` | `gfx/leaders/014_cannibalism/leader_AMX_warlord.dds` |
| CBH | Prison Host candidate 2 | `GFX_portrait_CBH_warlord` | `gfx/leaders/014_cannibalism/leader_CBH_warlord.dds` |

The parent confirmed that these are the exact sprite names expected by live leader effects. The ready-to-copy sprite block and character-binding lines are in `docs/assets/014_cannibalism/warlord_portraits_imagegen/gfx_handoff.md`.

## Before and after

Before this tranche, all eight stable CBA-CBH portrait paths were missing and the retained older clean suited source did not satisfy the live Part 10 brief.

After this tranche, every stable portrait path contains a distinct blood-heavy bald fictional warlord with origin-specific invented scavenged gear and environment. The files are format-complete and ready for sprite registration and leader-effect use.

## Why the change is safe and bounded

- Only the eight requested portrait slots and their asset documentation were produced.
- No existing portrait source was reused or overwritten.
- No gameplay, `.gfx`, character, localisation, spreadsheet, flag, achievement, animation, focus, idea, decision, event, or GUI file was edited.
- The protected Event 014 leader file was never used as a reference and retains its expected SHA-256.
- All subjects are fictional adults; no archival image, identifiable real person, or living-cultural regalia entered the package.
- The original eight portraits are European variants only. The accepted repair at `docs/plans/014_cannibalism_plans/014_warlord_regional_portrait_repair.md` adds six further regional variants per slot so the portrait, male name pool, and actual state origin agree.

## Meaningful validation

- Direct review of full-source, processed 2x, actual 156 by 210, and DDS-decoded contact sheets confirmed eight distinct faces, poses, gear sets, palettes, and environments.
- All eight processed files are `156x210 RGBA`.
- All eight finals probe as `156x210 bgra` and have the required uncompressed 32-bit BGRA channel masks.
- Every final DDS decodes pixel-identically to its processed PNG.
- Source, processed, and DDS SHA-256 sets each contain eight unique hashes.
- Full-image 64-bit difference-hash distances range from 22 to 44; same-origin pairs differ by 29 to 41 bits.
- Protected-file SHA-256 after conversion remains `5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88`.

Detailed results and checksums are in `docs/assets/014_cannibalism/warlord_portraits_imagegen/notes/validation.md` and `hashes.sha256`.

## Skipped validation

No in-game portrait resolution was performed because sprite registration, leader-effect wiring, and gameplay changes are outside this subagent's scope. The parent must perform final integration review after adding the exact sprite definitions.

## Simplifications, omissions, and blockers

- The original handoff is complete only for the eight European variants. Forty-eight additional regional portraits remain required by the accepted repair before the Event 14 portrait scope is complete.
- Flag blocker: the live Event 014 gap map still marks the warlord and unified flag batches blocked by an unresolved cosmetic-tag ledger conflict. No flag was generated and no filename was guessed. The portrait manifest records the proposed CBA-CBH base-family path pattern and non-cultural visual cues for a later accepted flag tranche.
- Wiring remains intentionally pending: the parent owns `.gfx`, leader effects, regional male name selection, localisation, and any later character-database entries.

## Parent follow-up

1. Copy the eight exact sprite definitions from the package GFX handoff into the existing `spriteTypes` block in `interface/014_cannibalism.gfx`.
2. Verify each live CBA-CBH `create_country_leader` call uses its matching `picture = GFX_portrait_<slot>_warlord` token.
3. Keep each incarnation's name drawn from the actual origin state's male regional pool and avoid female metadata.
4. Reconcile and freeze the full flag/cosmetic-tag ledger before requesting `E14-FLAG-WARLORD-01`.

## Skills used

- `chaos-redux-subagents`
- `chaos-redux-event-assets`
- `imagegen`

No skill was created or updated.
