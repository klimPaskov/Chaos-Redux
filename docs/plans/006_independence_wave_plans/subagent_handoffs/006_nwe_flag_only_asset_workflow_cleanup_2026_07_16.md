# Event 006 NWE flag-only asset workflow cleanup handoff

Date: 2026-07-16

Status: complete bounded cleanup. The mixed northern/western generated-art
workflow is a flag-only authority for ACX, AFX, AGX, and AJX. No runtime flag
pixel changed, no non-flag evidence file changed, and no historical evidence
directory was deleted.

## Task boundary

This tranche changed only the five authorized mixed-workflow files and this
handoff:

- `docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py`;
- `docs/assets/006_independence_wave/generated_nwe_hashes.sha256`;
- `docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md`;
- `docs/assets/006_independence_wave/prompts/006_nwe_generated_art.md`;
- `docs/assets/006_independence_wave/northern_western_europe_generated_art_gfx_handoff.md`;
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_nwe_flag_only_asset_workflow_cleanup_2026_07_16.md`.

No gameplay, localisation, `.gfx`, `.gui`, spreadsheet, runtime leader DDS,
runtime portrait, other documentation authority, skill, or old evidence
directory was edited or deleted.

## Builder cleanup

`build_nwe_generated_art.py` now owns exactly four separately generated,
historically researched flat flag families:

- ACX St Piran's Cross;
- AFX 1913 Walloon coq hardi;
- AGX Friesland provincial flag;
- AJX Saar Territory 1920–1935 tricolour.

The builder now:

1. imports only the modules needed for flag normalization, TGA export,
   validation, contact sheets, and hashing;
2. prepares only the generated flag source/processed directories, flag contact
   directory, and standard HOI4 runtime flag ladder;
3. requires the four retained ImageGen raw inputs, rejects unrelated source
   files, and allows deterministic flat masters to be rebuilt from the raws;
4. validates the four cited historical design inputs and the ARM, ICE, and ISR
   canonical vanilla normal/medium/small ladders;
5. performs the retained exact-palette normalization and the documented ACX
   scanline cleanup without importing masks or redrawing geometry;
6. creates exactly the normal 82×52, medium 41×26, and small 10×7 triplets for
   ACX, AFX, AGX, and AJX;
7. validates uncompressed 32-bit TGA headers, eight-bit alpha, bottom-left
   origin, dimensions, and exact decoded-pixel/orientation equality with each
   processed PNG;
8. requires the completed source tree to contain exactly four raw/flat pairs
   and rebuilds only the two flag contact sheets;
9. writes the ledger from an explicit flag evidence allowlist rather than
   recursively scanning mixed source, processed, decoded, contact-sheet, or
   runtime roots;
10. accepts either no scope argument or `--scope flags`; former mixed scope
    values are rejected by argument parsing.

All portrait constants, functions, imports, directory creation, runtime reads,
DDS handling, contact-sheet generation, and hash collection were removed from
this builder.

The builder no longer deletes obsolete AEX artifacts. It validates that AEX has
no standalone source, processed, or runtime flag and stops with a reviewable
error if one appears.

## Flag ledger result

`generated_nwe_hashes.sha256` contains 47 unique flag-only rows:

| Evidence class | Rows |
| --- | ---: |
| retained ImageGen raws and deterministic flat masters | 8 |
| cited historical design inputs | 4 |
| deduplicated ARM, ICE, and ISR canonical vanilla ladders | 9 |
| processed normal/medium/small PNGs | 12 |
| runtime normal/medium/small TGAs | 12 |
| flag contact sheets | 2 |
| **Total** | **47** |

Every row resolves to an existing file and matches its recorded SHA-256. The
ledger contains zero `gfx/leaders`, portrait, DDS-decode, institutional,
command, officer, or non-flag contact-sheet rows.

## Documentation authority cleanup

The three current mixed documents were rewritten as flag-only authorities:

- the manifest now records only the four live flag families, source and
  ImageGen provenance, historical function, palettes, runtime paths, processing
  contract, contact sheets, ledger coverage, route locks, and AEX boundary;
- the prompt record preserves all four exact flag prompts, historical source
  links, rights notes, secondary identity checks, canonical ladder selections,
  original ImageGen output locations, repo copies, and exact palettes; rejected
  portrait recipes no longer remain in the current production record;
- the generated-art GFX handoff is now an engine lookup handoff explaining that
  HOI4 loads exact tag filenames from `gfx/flags/`, `gfx/flags/medium/`, and
  `gfx/flags/small/` without any `spriteType` registration. It contains no
  copy-ready portrait or character block.

The AEX boundary is consistent across all three documents: AEX remains the
vanilla `BEL_flanders` cosmetic overlay and has no standalone Event 006 flag
family.

## Validation evidence

### Successful corrected build

The canonical scoped invocation completed successfully:

```powershell
python -B docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py --scope flags
```

The equivalent no-argument invocation also completed successfully. The parser
rejected both old mixed values tested:

- `--scope all`: exit 2;
- `--scope portraits`: exit 2.

The installed Python runtime did not support `zip(..., strict=True)` during the
first validation attempt. That compatibility-only keyword was removed; both
iterables are fixed three-entry ladders. The failure occurred during read-only
source validation before flag processing. The corrected run passed all gates.

### Determinism and non-interference proof

A direct SHA-256 snapshot was taken immediately before and after the corrected
builder run:

- 47 explicit flag evidence files were byte-identical before and after,
  including all twelve runtime TGAs and both flag contact sheets;
- 88 protected non-flag files across the generated NWE legacy trees, the four
  old non-flag NWE contact sheets, and `gfx/leaders/006_independence_wave/` were
  byte-identical before and after;
- a static builder scan found zero references to portrait paths, `gfx/leaders`,
  DDS decode roots, subprocess conversion, or legacy portrait-processing
  imports;
- the five historical evidence packages named by the cleanup plan still exist:
  `portrait_regeneration_2026_07_15/`,
  `nwe_package_portraits_2026_07_15/`,
  `live_afx_agx_portrait_regen_2026_07_15/`,
  `bri_package_2026_07_15/`, and
  `army_small_dossier_correction_2026_07_15/`.

### Scope and boundary proof

- each processed ladder contains exactly ACX, AFX, AGX, and AJX;
- all twelve expected runtime TGAs exist;
- standalone AEX source, processed PNG, and runtime TGA paths are absent;
- all 47 ledger rows are unique, exist, and hash-match;
- the builder, ledger, manifest, prompt record, and engine handoff contain no
  dependency on generated NWE portrait directories or `gfx/leaders`;
- the scoped diff has no whitespace errors.

## Preserved historical flag evidence

The cleanup did not edit or delete:

- `docs/assets/006_independence_wave/006_nwe_historical_flag_comparison.md`;
- the four cited files under
  `docs/assets/006_independence_wave/source_png/country_symbols/`;
- the eight retained raw/flat files under
  `docs/assets/006_independence_wave/source_png/generated_nwe/flags/`;
- the canonical vanilla flag reference library;
- either NWE flag contact sheet;
- any runtime flag pixel.

Their hashes remain represented by the corrected flag-only ledger.

## Simplifications, omissions, and blockers

No fallback, simplification, placeholder, runtime rename, asset deletion, or
flag redesign was used. No scoped blocker remains. The broader rejected
portrait-evidence deletion transaction remains outside this tranche and is not
implicitly authorized by this builder cleanup.

## Skills used

- `chaos-redux-event-assets` for the flag source, ImageGen provenance, canonical
  ladder, TGA orientation, runtime placement, manifest, contact-sheet, and
  engine-handoff requirements.

No skill was created or updated during this cleanup.
