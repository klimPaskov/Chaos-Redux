# Event 006 northern and western Europe generated-art handoff

## Outcome

The bounded ACX/AFX/AGX/AJX live-flag repair is complete at the asset layer;
the pre-existing five-tag portrait tranche remains separately documented:

- four official-ImageGen-derived historical flat flag masters;
- four complete 82×52, 41×26, and 10×7 bottom-origin TGA triplets;
- five independently generated fictional institutional council portraits;
- five independently generated fictional male-presenting regional officer
  portraits;
- ten requested 156×210 uncompressed BGRA DDS files;
- five 50×67 officer thumbnails required by the vanilla army portrait block;
- generated source PNGs, deterministic processed PNGs, actual-runtime DDS
  decodes, contact sheets, prompts, hash inventory, and exact GFX/character
  handoff notes.
- the obsolete standalone AEX generated flag master, processed previews, and
  runtime triplet are retired; the Flanders lion source remains overlay evidence
  for vanilla `BEL_flanders` only.

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
| ACX | unsuffixed St Piran's Cross, institutional committee, coastal commander | flag-complete; unique Cornwall geography/state ownership remains unresolved |
| AEX | no standalone flag; portrait staging retained; Lion of Flanders source is vanilla-overlay evidence only | `BEL_flanders` cosmetic overlay, not a standalone Event 006 country flag |
| AFX | unsuffixed 1913 coq hardi, provisional assembly, reserve commander | ready for package-owner wiring; assembly is for accepted civil routes, commander for emergency command |
| AGX | unsuffixed Friesland provincial flag, coastal council, coastal commander | ready for package-owner wiring; bounded Friesland only, never a pan-Frisian claim |
| AJX | unsuffixed Saar Territory 1920–1935 tricolour, municipal neutral commission, industrial-security commissioner | ready for package-owner wiring; no ideology/cosmetic variant mapping is inferred |

No ideology or cosmetic flag variant was created for any live flag tag.

## Exact changed-file inventory

`docs/assets/006_independence_wave/generated_nwe_hashes.sha256` is the exact
one-path-per-line inventory of all cited flag inputs, canonical vanilla ladder
inputs, generated source, processed, decoded, contact-sheet, and runtime binary
files delivered by this tranche. Each line
contains that file's SHA-256 hash and repository-relative path; this avoids a
second, manually duplicated binary inventory drifting from the actual package.

The exact non-binary/support files outside that binary hash ledger are:

- `docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py`;
- `docs/assets/006_independence_wave/generated_nwe_hashes.sha256`;
- `docs/assets/006_independence_wave/prompts/006_nwe_generated_art.md`;
- `docs/assets/006_independence_wave/006_nwe_historical_flag_comparison.md`;
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

- The flag-only build completed with four flag triplets, retired the exact AEX
  flag paths, and validated every live TGA header and payload length.
- Git's `file.exe` identified every TGA as 32-bit RGBA with eight-bit alpha at
  exactly 82×52, 41×26, or 10×7. None was reported with the `top` orientation
  marker, matching the required bottom-left origin.
- The same probe identified every large portrait as 156×210 ARGB8888 and every
  officer thumbnail as 50×67 ARGB8888.
- `contact_sheets/006_nwe_generated_flags_contact_sheet.png` reopens the actual
  runtime TGAs, confirming correct visual orientation and engine-size
  readability.
- `contact_sheets/006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png`
  compares each cited reference, unchanged ImageGen source, and flat master.
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
- `imagegen` for every live historical flag source raster and the existing
  fictional portrait sources;
- `chaos-redux-subagents` for bounded ownership and parent handoff discipline.

## Simplifications, omissions, and blockers

No fallback, placeholder, historical-person substitution, shared portrait,
transform-only substitute, or weaker art replacement was used. No requested
asset is omitted.

Route-specific and ideology/cosmetic flag variants are absent because no exact
mapping was approved; creating them would have exceeded the accepted design.
This is not an asset fallback. ACX geography remains a country-content blocker.
AEX is intentionally excluded from standalone flag scope because it is a
vanilla cosmetic overlay, not because a substitute asset was used.
