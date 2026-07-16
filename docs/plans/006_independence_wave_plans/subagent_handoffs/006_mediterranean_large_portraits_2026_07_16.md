# Event 006 Mediterranean large portraits handoff

Date: 2026-07-16
Producer: `/root/med_portraits_resume`

## Result

Completed the approved large-only Mediterranean portrait tranche: eight
distinct adult-male 156x210 portraits, calibrated to the protected BAY
Rupprecht and RHI Matthes treatment, converted to runtime DDS, registered, and
audited end to end.

## Runtime files

- Added `interface/006_independence_wave_mediterranean_portraits.gfx` with eight
  large sprite registrations and no small/advisor sprites.
- Added eight DDS files under `gfx/leaders/006_independence_wave/`:
  - `portrait_COR_independence_wave_petru_santucci.dds`
  - `portrait_COR_independence_wave_pasquale_venturi.dds`
  - `portrait_ARX_independence_wave_antioco_melis.dds`
  - `portrait_ARX_independence_wave_vittorio_pala.dds`
  - `portrait_ARX_independence_wave_gavino_piras.dds`
  - `portrait_ASX_independence_wave_sebastiano_restivo.dds`
  - `portrait_ASX_independence_wave_vincenzo_lanza.dds`
  - `portrait_ASX_independence_wave_salvatore_licata.dds`

No gameplay, localisation, flag, focus, decision, idea, event-picture, or
package-icon file was edited by this subagent.

## Asset package

Created/updated
`docs/assets/006_independence_wave/mediterranean_portraits_2026_07_16/` with:

- eight ImageGen source PNGs and exact large-prompt/handle records;
- canonical pre-calibration crops and final BAY/RHI-calibrated PNGs;
- DDS-decoded PNGs;
- approved baseline, identity-preservation, and runtime contact sheets;
- `manifest.md`, `gfx_handoff.md`, SHA-256 inventory, and validation report;
- retained leader-mode pre-calibration metadata/review evidence.

All former 65x67 experiments, prompt sections, source iterations, provenance,
processed candidates, review artifacts, and metadata were removed. The package
contains no small or advisor art.

## Consumer audit

Verified exact live mappings for:

- `COR_corsican_municipal_congress`
- `COR_pasquale_venturi`
- `ARX_sardinian_provisional_assembly`
- `ARX_sardinian_crown_consultative_council`
- `ARX_gavino_piras`
- `ASX_sicilian_provisional_assembly`
- `ASX_sicilian_crown_council`
- `ASX_salvatore_licata`

The live commander consumers are Pasquale Venturi, Gavino Piras, and Salvatore
Licata. The earlier Vincenzo-small note was stale and is not present in the
accepted package. The parent resolved the accepted scope to vanilla-supported
large-only commander portraits and removed the optional `small =` consumers;
this subagent did not edit the character file.

## Meaningful validation

- Eight consumers resolve to eight unique registered sprites and eight unique
  DDS files.
- Every DDS is 156x210 uncompressed 32-bit BGRA, has the expected header/masks,
  is exactly 131,168 bytes, and decodes pixel-for-pixel to its calibrated PNG.
- Eight source prompts contain explicit fictional-adult-male constraints; the
  approved decoded contact sheet visually confirms eight individual men and
  distinct identities.
- The package has no filename or prompt section for small, advisor, or dossier
  art; the GFX file has no `_small` sprite; live COR/ARX/ASX consumers have no
  `_small` reference.
- Protected DDS hashes remain unchanged:
  - BAY Rupprecht:
    `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`
  - RHI Matthes:
    `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`

Full evidence is in
`docs/assets/006_independence_wave/mediterranean_portraits_2026_07_16/validation/validation_report.md`.

## Simplifications, omissions, and blockers

None against the parent-approved final scope. The final scope is exactly eight
large portraits; no substitute art, placeholder, or advisor asset was used.

## Skills used

- `chaos-redux-event-assets`
- `chaos-redux-subagents`
- `imagegen`

No skill file was created or edited by this subagent. No commit was created.
