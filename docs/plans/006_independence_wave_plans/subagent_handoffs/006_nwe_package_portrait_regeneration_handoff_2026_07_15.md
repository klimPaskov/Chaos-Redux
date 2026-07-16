# Event 006 NWE package portrait regeneration handoff

> **Portrait-specific supersession (2026-07-16):** The RHI, BAY, SCO, and WLS
> fictional visuals, hashes, approval, and mixed-gender collective direction in
> this record are superseded by the male-HOI4 package manifest and
> `006_event6_male_hoi4_portrait_final_independent_audit_2026_07_16.md`.
> Stable runtime names remain; Rupprecht and Matthes stay protected.

> Superseded for portrait-source and final-file evidence by
> `006_character_portrait_regeneration_handoff_2026_07_15.md`. The newer handoff
> preserves the same runtime tokens while replacing the generic visual set.

## Outcome

The bounded Event 006 northern/western Europe portrait tranche is produced and
wired through concurrent parent integration. Eight independent official ImageGen calls produced eight
fictional HOI4-style portrait masters for the exact final gameplay tokens. The
tranche contains four institutional civilian leaders, four army commanders,
four commander-only `50x67` small portraits, twelve installed DDS files, source
evidence, processing metadata, vanilla-reference review sheets, installed-DDS
contact sheets, a manifest, checksums, exact sprite references, and a runtime
effect ownership map.

This asset task did not edit gameplay, `.gfx`, localisation, spreadsheet, or
existing Event 006 source files. During final verification, the twelve exact
sprite registrations and guarded runtime `set_portraits` calls were present
through concurrent parent work. No commit was created, as required by the
parent assignment.

## Exact tokens and installed assets

| Character/localisation token | Portrait surface | Installed runtime DDS |
| --- | --- | --- |
| `RHI_independence_wave_provisional_directorate` | civilian large, institutional | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds` |
| `RHI_independence_wave_river_commandant` | army large | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds` |
| `RHI_independence_wave_river_commandant` | army small | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant_small.dds` |
| `BAY_independence_wave_state_council` | civilian large, institutional | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds` |
| `BAY_independence_wave_mountain_commandant` | army large | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds` |
| `BAY_independence_wave_mountain_commandant` | army small | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant_small.dds` |
| `SCO_independence_wave_civic_convention` | civilian large, institutional | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_civic_convention.dds` |
| `SCO_independence_wave_territorial_commandant` | army large | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds` |
| `SCO_independence_wave_territorial_commandant` | army small | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant_small.dds` |
| `WLS_independence_wave_national_council` | civilian large, institutional | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` |
| `WLS_independence_wave_mountain_commandant` | army large | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` |
| `WLS_independence_wave_mountain_commandant` | army small | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant_small.dds` |

The final SCO/WLS stems intentionally differ from the descriptive names of the
older input briefs. The exact runtime tokens above override those brief labels.

## Proposed sprites

- `GFX_portrait_RHI_independence_wave_provisional_directorate`
- `GFX_portrait_RHI_independence_wave_river_commandant`
- `GFX_portrait_RHI_independence_wave_river_commandant_small`
- `GFX_portrait_BAY_independence_wave_state_council`
- `GFX_portrait_BAY_independence_wave_mountain_commandant`
- `GFX_portrait_BAY_independence_wave_mountain_commandant_small`
- `GFX_portrait_SCO_independence_wave_civic_convention`
- `GFX_portrait_SCO_independence_wave_territorial_commandant`
- `GFX_portrait_SCO_independence_wave_territorial_commandant_small`
- `GFX_portrait_WLS_independence_wave_national_council`
- `GFX_portrait_WLS_independence_wave_mountain_commandant`
- `GFX_portrait_WLS_independence_wave_mountain_commandant_small`

The registry is `interface/006_independence_wave_region_01_portraits.gfx`. All
twelve proposed registrations were present at final verification. Exact expected
sprite definitions and the runtime-effect ownership map are in:

- `docs/assets/006_independence_wave/nwe_package_portraits_2026_07_15/gfx_handoff.md`

## Production package

Root:

- `docs/assets/006_independence_wave/nwe_package_portraits_2026_07_15/`

Key files:

- `manifest.md`: complete per-asset provenance, paths, gender/institutional requirements, era-fit notes, final checksums, and status
- `gfx_handoff.md`: exact sprite registrations, character portrait blocks, and surface boundary
- `checksums.sha256`: SHA-256 ledger for raw masters, processed PNGs, tranche DDS files, installed DDS files, and contact sheets
- `prompts/production_prompts.md`: exact production prompts used for all eight independent ImageGen calls
- `raw_imagegen/`: eight official ImageGen masters
- `processed_png/institutional/`: four approved `156x210` institutional portraits
- `processed_png/command/`: four approved `156x210` commander portraits
- `processed_png/command_small/`: four approved `50x67` army commander thumbnails
- `final_dds/`: retained byte-identical DDS copies grouped by surface
- `dds_decoded_png/`: independent decodes of the installed runtime DDS files
- `metadata/`: deterministic portrait-processor metadata
- `review_sheets/`: eight canonical-vanilla comparison sheets
- `contact_sheets/`: four final review sheets built from ImageGen masters and actual installed DDS decodes
- `_tooling/build_contact_sheets.py`: retained deterministic contact-sheet builder

## Source and visual review

- All subjects are fictional; no real-person portrait was generated.
- Each portrait used its older Event 006 source PNG as identity/composition guidance only.
- Canonical vanilla references were Thorvald Stauning, Eamon de Valera, and Carl Mannerheim from the event-assets reference library.
- All eight large portraits were visually inspected at `156x210` and on comparison sheets.
- All four commander-small portraits were inspected at native `50x67` and enlarged with nearest-neighbour sampling.
- The final contact sheets were inspected individually; no head, cap, face, label, or frame is clipped.
- The eight subjects/compositions remain distinct, period-readable, painterly, and free of text, watermarks, modern props, and visible invented insignia.

## Technical validation

- Large DDS dimensions: eight files at `156x210`.
- Army-small DDS dimensions: four files at `50x67`.
- DDS format: legacy uncompressed one-level 32-bit BGRA with header size `124`, pixel-format size `32`, flags `65`, `fourCC = 0`, `bitcount = 32`, standard RGBA masks, and caps `4096`.
- Every DDS length equals `128 + width * height * 4`.
- Every final image has an intended opaque painted background (`alpha 255..255`).
- Every retained DDS is byte-identical to the corresponding installed runtime DDS.
- Every independently decoded installed DDS pixel-matches its processed PNG.
- The checksum ledger records all production and installed hashes.

## Exact runtime wiring identifiers

- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`
  - `independence_wave_prepare_rhi_roster_and_portrait`
  - `independence_wave_prepare_bay_roster_and_portrait`
- `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt`
  - `independence_wave_prepare_sco_institutional_roster`
  - `independence_wave_prepare_wls_institutional_roster`

Each effect guards `set_portraits` behind `has_character`. Institutional tokens
receive `civilian.large`. Commander tokens receive `civilian.large` because they
can be promoted as country leaders, plus `army.large` and `army.small` for their
corps-commander surface.

## Parent verification checklist

1. Preserve the twelve existing registrations in `interface/006_independence_wave_region_01_portraits.gfx`; do not add duplicates.
2. Preserve the guarded `set_portraits` calls in the four exact runtime roster effects above.
3. Keep institutional names for the mixed-gender councils/directorate; do not use personal random-name pools.
4. Keep the four commanders male-presenting; do not set `female = yes` or pair them with a female name pool.
5. Do not use the `50x67` `_small` files as advisor/high-command portraits.

## Simplifications, omissions, and blockers

None within the assigned asset-production scope. There is no fallback art,
placeholder, identity reuse, or unprocessed final asset. Sprite and guarded
runtime character wiring are present through parent-owned integration in the
exact files/effects above; static `common/characters` blocks are intentionally
not used because the characters are generated at runtime. Separate
`65x67` advisor/high-command dossier art was neither requested nor produced;
the commander-small outputs are army thumbnails only and provide no advisor
roster coverage.

## Skills used

- `chaos-redux-event-assets`
- official `imagegen`

No skill files were created or updated.
