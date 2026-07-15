# Event 006 northern and western Europe generated-art manifest

## Scope and status

This package is the generated-art successor to
`northern_western_europe_source_manifest.md`. Its live flag scope contains four
northern/western Event 006 tags:

- ACX Cornwall;
- AFX Wallonia;
- AGX Friesland;
- AJX Saar.

It delivers four official-ImageGen-derived historical flag triplets, five
fictional institutional council portraits, five independently generated
fictional officer portraits, the five matching officer thumbnails required by
vanilla's army portrait block, processed PNGs, decoded DDS review files, contact
sheets, stable identifiers, prompts, and SHA-256 hashes. The retained AEX
portrait family does not create an AEX flag or standalone-country identity.

The flags reproduce cited historical/community designs; their historical
function and limits are recorded in `006_nwe_historical_flag_comparison.md`.
None of the ten portrait sources depicts or imitates a real historical person.

## Flag ownership and route boundary

Only the unsuffixed baseline family is produced. No ideology or cosmetic
variant has an approved route-to-filename mapping, so no
`<TAG>_democratic.tga`, `<TAG>_communism.tga`, `<TAG>_fascism.tga`,
`<TAG>_neutrality.tga`, or cosmetic-tag flag has been invented.

| Tag | Historical design | Runtime triplet | Route and content boundary |
|---|---|---|---|
| ACX | St Piran's Cross: white upright cross on black | `gfx/flags/ACX.tga`, `gfx/flags/medium/ACX.tga`, `gfx/flags/small/ACX.tga` | unsuffixed ACX identity; no ideology variant is inferred |
| AFX | 1913 Walloon coq hardi: one red rooster on yellow | `gfx/flags/AFX.tga`, `gfx/flags/medium/AFX.tga`, `gfx/flags/small/AFX.tga` | unsuffixed AFX identity; no ideology variant is inferred |
| AGX | Friesland provincial flag: seven diagonal bands and seven red pompeblêden | `gfx/flags/AGX.tga`, `gfx/flags/medium/AGX.tga`, `gfx/flags/small/AGX.tga` | unsuffixed AGX identity for Friesland; no pan-Frisian variant is inferred |
| AJX | Saar Territory 1920–1935 blue-white-black horizontal tricolour | `gfx/flags/AJX.tga`, `gfx/flags/medium/AJX.tga`, `gfx/flags/small/AJX.tga` | unsuffixed AJX identity; no ideology variant is inferred |

All twelve TGAs are uncompressed 32-bit BGRA with eight-bit alpha and a
bottom-left origin. The normal, medium, and small dimensions are 82×52, 41×26,
and 10×7 respectively.

AEX is deliberately absent. Its former generated civic master, processed PNGs,
and runtime TGA triplet are retired. The Lion of Flanders source remains only as
evidence for vanilla `BEL_flanders`, never as an AEX country flag.

## Institutional portraits

The institutional art is deliberately collective. These are fictional councils
with several visible delegates, not named people masquerading as historical
leaders.

| Tag | Character identifier / localisation key | Player-facing name | Sprite | Runtime DDS | Visual remit |
|---|---|---|---|---|---|
| ACX | `ACX_cornish_port_and_mines_committee` | Cornish Port and Mines Security Committee | `GFX_portrait_ACX_cornish_port_and_mines_committee` | `gfx/leaders/006_independence_wave/portrait_ACX_cornish_port_and_mines_committee.dds` | harbor, mine, municipal, and civil-defense delegates |
| AEX | `AEX_flemish_civil_industrial_board` | Flemish Civil-Industrial Security Board | `GFX_portrait_AEX_flemish_civil_industrial_board` | `gfx/leaders/006_independence_wave/portrait_AEX_flemish_civil_industrial_board.dds` | rail, factory, municipal, and civil-security delegates |
| AFX | `AFX_walloon_provisional_assembly` | Walloon Provisional Assembly | `GFX_portrait_AFX_walloon_provisional_assembly` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds` | mineworker, steel engineer, municipal magistrate, and reserve inspector |
| AGX | `AGX_friesland_coastal_council` | Friesland Coastal Council | `GFX_portrait_AGX_friesland_coastal_council` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` | municipal, harbor, dike-engineering, and coastal-constabulary delegates |
| AJX | `AJX_saar_municipal_neutral_commission` | Saar Municipal Neutral Commission | `GFX_portrait_AJX_saar_municipal_neutral_commission` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` | municipal, mine, rail, and industrial-security delegates |

The institutional images contain mixed-gender delegations. Do not assign an
individual biography, individual gender metadata, or a real person's name to
these group portraits.

## Officer portraits

Each officer source was generated independently in a separate call. The fixed
names are fictional, regionally plausible handoff names rather than historical
claims. All five images are male-presenting; character wiring must retain the
default male setting and must not set `female = yes`.

| Tag | Character identifier / localisation key | Fixed player-facing name | Large and small sprites | Runtime DDS files |
|---|---|---|---|---|
| ACX | `ACX_cornish_coastal_commander` | Thomas Trevorrow | `GFX_portrait_ACX_cornish_coastal_commander`, `GFX_portrait_ACX_cornish_coastal_commander_small` | `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander.dds`, `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander_small.dds` |
| AEX | `AEX_flemish_industrial_security_commander` | Hendrik Vermeulen | `GFX_portrait_AEX_flemish_industrial_security_commander`, `GFX_portrait_AEX_flemish_industrial_security_commander_small` | `gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander.dds`, `gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander_small.dds` |
| AFX | `AFX_walloon_reserve_commander` | Marcel Delcourt | `GFX_portrait_AFX_walloon_reserve_commander`, `GFX_portrait_AFX_walloon_reserve_commander_small` | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds`, `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander_small.dds` |
| AGX | `AGX_friesland_coastal_commander` | Sjoerd Hoekstra | `GFX_portrait_AGX_friesland_coastal_commander`, `GFX_portrait_AGX_friesland_coastal_commander_small` | `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds`, `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander_small.dds` |
| AJX | `AJX_saar_industrial_security_commissioner` | Karl Becker | `GFX_portrait_AJX_saar_industrial_security_commissioner`, `GFX_portrait_AJX_saar_industrial_security_commissioner_small` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds`, `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner_small.dds` |

Large portraits are 156×210 and army thumbnails are 50×67. All are one-mip,
uncompressed BGRA DDS files. The small files are deterministic reductions of
their own tag's independently generated officer master, not substitute art or a
reused portrait from another tag.

## Source, processed, and decoded layout

Generated masters:

- `source_png/generated_nwe/flags/`;
- `source_png/generated_nwe/institutional_portraits/`;
- `source_png/generated_nwe/command_portraits/`.

Deterministic processed PNGs:

- `processed_png/generated_nwe/flags/normal/`;
- `processed_png/generated_nwe/flags/medium/`;
- `processed_png/generated_nwe/flags/small/`;
- `processed_png/generated_nwe/institutional_portraits/`;
- `processed_png/generated_nwe/command_portraits/`;
- `processed_png/generated_nwe/command_portraits_small/`.

Runtime DDS decode evidence:

- `dds_decoded_png/generated_nwe/institutional_portraits/`;
- `dds_decoded_png/generated_nwe/command_portraits/`;
- `dds_decoded_png/generated_nwe/command_portraits_small/`.

## Review artifacts

- `contact_sheets/006_nwe_generated_flags_contact_sheet.png` reopens and shows
  the actual TGA triplets at every engine size;
- `contact_sheets/006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png`
  compares cited designs, unchanged ImageGen outputs, and flat masters;
- `contact_sheets/006_nwe_generated_institutional_portraits_contact_sheet.png`;
- `contact_sheets/006_nwe_generated_command_portraits_contact_sheet.png`;
- `contact_sheets/006_nwe_generated_final_dds_decoded_contact_sheet.png` reopens
  and shows all ten actual 156×210 runtime DDS files;
- `contact_sheets/006_nwe_generated_officer_small_dds_decoded_contact_sheet.png`
  reopens and shows the actual 50×67 officer DDS files.

## Prompts, build recipe, and hashes

- All production prompts and negative constraints are recorded in
  `prompts/006_nwe_generated_art.md`.
- `_tooling/build_nwe_generated_art.py` performs deterministic flag
  normalization and resizing, preserves the externally approved AFX/AGX
  portrait PNGs, finishes only the remaining legacy portrait set, performs
  TGA/DDS conversion and header validation, checks runtime decodes, assembles
  contact sheets, and refreshes the hash inventory.
- `generated_nwe_hashes.sha256` inventories every cited flag input, canonical
  vanilla ladder input, generated source, processed output, decoded review PNG,
  contact sheet, and runtime TGA/DDS in this package.

The hash ledger uses repository-relative forward-slash paths and can be checked
from the repository root with any SHA-256 verification tool.

## Integration boundary and blockers

No `.gfx`, `.gui`, character, country, state, event, decision, focus, idea,
history, localisation, or spreadsheet file is edited by this package. Exact
copy-ready sprite and character portrait blocks are in
`northern_western_europe_generated_art_gfx_handoff.md`.

The assets remove the flag-art blocker for the four live flag tags, but they do
not remove content blockers. ACX remains blocked by missing unique Cornwall
geography and state ownership. AEX remains a vanilla cosmetic overlay and is
outside the standalone flag scope. No country is to be described as
content-ready merely because its art exists.

## Simplifications and fallbacks

No fallback art, historical-person substitution, shared portrait, transform-only
replacement, placeholder flag, or unapproved route variant was used. No live
flag design was simplified or replaced. Ideology and cosmetic variants are
intentionally absent because the accepted design does not own exact mappings
for them; producing them would be an unsupported design expansion rather than
completion work.
