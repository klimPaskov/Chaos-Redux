# Event 006 northern and western Europe generated-art handoff

## Outcome

The bounded ACX/AEX/AFX/AGX/AJX generated-art tranche is complete at the asset
layer:

- five independently generated fictional civic baseline flag masters;
- complete 82×52, 41×26, and 10×7 bottom-origin TGA triplets;
- five independently generated fictional institutional council portraits;
- five independently generated fictional male-presenting regional officer
  portraits;
- ten requested 156×210 uncompressed BGRA DDS files;
- five 50×67 officer thumbnails required by the vanilla army portrait block;
- generated source PNGs, deterministic processed PNGs, actual-runtime DDS
  decodes, contact sheets, prompts, hash inventory, and exact GFX/character
  handoff notes.

No `.gfx`, `.gui`, character, country, state, event, decision, focus, idea,
history, localisation, spreadsheet, or spec file was edited. No commit was made;
the parent owns final review, wiring, validation, and commit scope.

## Stable identifiers

| Tag | Institutional character | Officer character and fictional fixed name |
|---|---|---|
| ACX | `ACX_cornish_port_and_mines_committee` | `ACX_cornish_coastal_commander` — Thomas Trevorrow |
| AEX | `AEX_flemish_civil_industrial_board` | `AEX_flemish_industrial_security_commander` — Hendrik Vermeulen |
| AFX | `AFX_walloon_provisional_assembly` | `AFX_walloon_reserve_commander` — Marcel Delcourt |
| AGX | `AGX_friesland_coastal_council` | `AGX_friesland_coastal_commander` — Sjoerd Hoekstra |
| AJX | `AJX_saar_municipal_neutral_commission` | `AJX_saar_industrial_security_commissioner` — Karl Becker |

Sprite names are the character identifier prefixed with `GFX_portrait_`; the
officer thumbnails append `_small`. Exact copy-ready registrations and portrait
blocks are in
`docs/assets/006_independence_wave/northern_western_europe_generated_art_gfx_handoff.md`.

## Route and country-package disposition

| Tag | Asset mapping | Remaining package status |
|---|---|---|
| ACX | unsuffixed civic baseline, institutional committee, coastal commander | asset-complete but not content-ready; unique Cornwall geography/state ownership remains unresolved |
| AEX | unsuffixed civic baseline, civil-industrial board, industrial-security commander | asset-complete but not content-ready; protected Brussels/Flanders anchor remains unresolved |
| AFX | unsuffixed civic baseline, provisional assembly, reserve commander | ready for package-owner wiring; assembly is for accepted civil routes, commander for emergency command |
| AGX | unsuffixed civic baseline, coastal council, coastal commander | ready for package-owner wiring; bounded Friesland only, never a pan-Frisian claim |
| AJX | unsuffixed civic baseline, municipal neutral commission, industrial-security commissioner | ready for package-owner wiring; no `AJX_neutrality` or other ideology/cosmetic flag mapping was approved |

No ideology or cosmetic flag variant was created for any of the five tags.

## Exact changed-file inventory

`docs/assets/006_independence_wave/generated_nwe_hashes.sha256` is the exact
one-path-per-line inventory of all 95 generated source, processed, decoded,
contact-sheet, and runtime binary files delivered by this tranche. Each line
contains that file's SHA-256 hash and repository-relative path; this avoids a
second, manually duplicated binary inventory drifting from the actual package.

The exact non-binary/support files outside that 95-file ledger are:

- `docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py`;
- `docs/assets/006_independence_wave/generated_nwe_hashes.sha256`;
- `docs/assets/006_independence_wave/prompts/006_nwe_generated_art.md`;
- `docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md`;
- `docs/assets/006_independence_wave/northern_western_europe_generated_art_gfx_handoff.md`;
- `docs/assets/006_independence_wave/northern_western_europe_source_manifest.md`;
- `docs/assets/006_independence_wave/northern_western_europe_gfx_handoff.md`;
- `docs/assets/006_independence_wave/manifest.md`;
- `docs/assets/006_independence_wave/gfx_handoff.md`;
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_generated_art_handoff.md`.

The four pre-existing asset documentation files were changed only to link the
generated companion and remove stale statements that the five generated flag
families were still outstanding.

## Meaningful validation evidence

- The build script completed with five flag triplets, ten large portraits, and
  five officer thumbnails, then validated every TGA/DDS header and payload
  length.
- Git's `file.exe` identified every TGA as 32-bit RGBA with eight-bit alpha at
  exactly 82×52, 41×26, or 10×7. None was reported with the `top` orientation
  marker, matching the required bottom-left origin.
- The same probe identified every large portrait as 156×210 ARGB8888 and every
  officer thumbnail as 50×67 ARGB8888.
- `contact_sheets/006_nwe_generated_flags_contact_sheet.png` reopens the actual
  runtime TGAs, confirming correct visual orientation and engine-size
  readability.
- `contact_sheets/006_nwe_generated_final_dds_decoded_contact_sheet.png` and
  `contact_sheets/006_nwe_generated_officer_small_dds_decoded_contact_sheet.png`
  are assembled from decoded runtime DDS payloads, confirming final pixels after
  conversion rather than only the processed PNG masters.
- Visual review confirmed five distinct council scenes and five distinct
  independently generated people. No portrait is a crop, recolor, transform, or
  reuse of another tag's art.

## References and skills used

Required offline wiki references were consulted before asset work: Data
structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions,
Event modding, Decision modding, Idea modding, AI modding, Interface modding,
Scripted GUI modding, and Country creation. Vanilla documentation and examples
were consulted for character portraits, sprite registration, flag dimensions,
bottom-origin TGA expectations, and the army `large`/`small` portrait pairing.

Skills used:

- `chaos-redux-event-assets` for source/generated boundaries, rights notes,
  processing, manifests, and runtime handoff;
- `imagegen` for every fictional flag, institutional portrait, and officer
  source raster;
- `chaos-redux-subagents` for bounded ownership and parent handoff discipline.

## Simplifications, omissions, and blockers

No fallback, placeholder, historical-person substitution, shared portrait,
transform-only substitute, or weaker art replacement was used. No requested
asset is omitted.

Route-specific and ideology/cosmetic flag variants are absent because no exact
mapping was approved; creating them would have exceeded the accepted design.
This is not an asset fallback. Country-content blockers remain ACX geography and
AEX anchor ownership, and those blockers must remain visible in any completion
claim.
