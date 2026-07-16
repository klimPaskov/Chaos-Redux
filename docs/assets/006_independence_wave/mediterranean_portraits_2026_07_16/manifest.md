# Event 006 Mediterranean large portrait manifest

This package contains exactly eight fictional adult-male, 156x210 Event 006
character portraits for Corsica (`COR`), Sardinia (`ARX`), and Sicily (`ASX`).
The protected BAY Rupprecht and RHI Matthes portraits are the binding visual
baseline: muted archival/colorized-photograph color, restrained brushwork,
matte grain, clear HOI4 facial planes, and sober studio lighting.

The package intentionally contains no 65x67 outputs, no `_small` sprites, and
no advisor artwork. The three commanders use their large portrait for both
`civilian` and `army` portrait scopes, which is supported by the vanilla
character portrait structure.

## Runtime crosswalk

| Character consumer | Adult-male identity | Sprite | Runtime DDS | ImageGen handle |
|---|---|---|---|---|
| `COR_corsican_municipal_congress` | Petru Santucci | `GFX_portrait_COR_independence_wave_petru_santucci` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_petru_santucci.dds` | `exec-3d70aa3e-dadf-4768-984a-3305b18f1433` |
| `COR_pasquale_venturi` | Pasquale Venturi | `GFX_portrait_COR_independence_wave_pasquale_venturi` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_pasquale_venturi.dds` | `exec-742aba34-8a99-4a90-9980-959c8fa1a3a2` |
| `ARX_sardinian_provisional_assembly` | Antioco Melis | `GFX_portrait_ARX_independence_wave_antioco_melis` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_antioco_melis.dds` | `exec-a6daf9a9-14a1-41a5-875b-f009391ca7eb` |
| `ARX_sardinian_crown_consultative_council` | Vittorio Pala | `GFX_portrait_ARX_independence_wave_vittorio_pala` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_vittorio_pala.dds` | `exec-75b65598-1149-4186-9006-06007e9bf0a3` |
| `ARX_gavino_piras` | Gavino Piras | `GFX_portrait_ARX_independence_wave_gavino_piras` | `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_gavino_piras.dds` | `exec-05428414-c9f8-44b3-97fb-303b8d489d92` |
| `ASX_sicilian_provisional_assembly` | Sebastiano Restivo | `GFX_portrait_ASX_independence_wave_sebastiano_restivo` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_sebastiano_restivo.dds` | `exec-e422e81c-636b-4f78-ab03-82e7ef0609a4` |
| `ASX_sicilian_crown_council` | Vincenzo Lanza | `GFX_portrait_ASX_independence_wave_vincenzo_lanza` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_vincenzo_lanza.dds` | `exec-689c08a9-d79b-4924-895a-49f1489b5e70` |
| `ASX_salvatore_licata` | Salvatore Licata | `GFX_portrait_ASX_independence_wave_salvatore_licata` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_salvatore_licata.dds` | `exec-b53b8dcf-f573-406a-8475-3a3b6ab27bcc` |

All eight sprites are registered in
`interface/006_independence_wave_mediterranean_portraits.gfx`.

## Source records

| Identity | Source master | Dimensions | Source SHA-256 |
|---|---|---:|---|
| Petru Santucci | `source_png/petru_santucci.png` | 1082x1454 | `74eb65134d31ed4d55ba12d6d6ad08ece54b105b7aa1132980a2592d52474199` |
| Pasquale Venturi | `source_png/pasquale_venturi.png` | 1082x1454 | `1bae9b462feda68ca91f527e7e16dbd1b3791a5541b8b4517439d46d1e1edbb3` |
| Antioco Melis | `source_png/antioco_melis.png` | 1080x1456 | `1670ecfbbc44a14f71e77b0d982672c56bf5aa3fe7b0fe7375e7d9dc9297a965` |
| Vittorio Pala | `source_png/vittorio_pala.png` | 1080x1456 | `ca66d3c0a876b60d27c2842bf8dc229e5df91308f40b2622928ae523420c77db` |
| Gavino Piras | `source_png/gavino_piras.png` | 1081x1455 | `1ac50b2073afd8fbdf3c41216185843ce60652b69cdb6b35d876e32fb0b8fb09` |
| Sebastiano Restivo | `source_png/sebastiano_restivo.png` | 1080x1456 | `e1582f6a3cbe76505c2a33179e49690bdffd477bc7649483dd2c6a0d309ed6e4` |
| Vincenzo Lanza | `source_png/vincenzo_lanza.png` | 1080x1456 | `9ba4aa3122a67b0ec0c79f7740089c8668427dbdba925f5f9e6a48a52739d19b` |
| Salvatore Licata | `source_png/salvatore_licata.png` | 1082x1454 | `12284b0fd89c9b5b988eb707083dac076636cc31afba6f70f72df1db8c4c9db1` |

The exact eight generation prompts and handles are pinned in
`prompts/imagegen_prompts.md` (SHA-256
`529d513aa8b1e4542ef26e7c99a6f2ec29bc2c2525116b4925ef24b962f4bc6a`).

## Processing and calibration

The canonical leader processor produced the initial 156x210 crops retained in
`processed_png/large_pre_calibration/`. The accepted calibration preserved
geometry and identity, then applied the same deterministic treatment to every
portrait:

- 53% partial luminance-quantile matching to the combined protected BAY/RHI
  baseline, leaving 47% of each portrait's original lighting;
- adaptive saturation reduction toward the BAY/RHI family without increasing
  saturation on already-muted portraits;
- deterministic, fine monochrome grain (2.15 code-value standard deviation,
  lightly correlated with a 0.22-pixel blur) at final resolution.

This keeps facial contrast, poses, clothing, and identity distinct while
removing the warmer, smoother digital-oil finish rejected in the first review.
The final calibrated PNGs are in `processed_png/large/`; DDS-decoded evidence is
in `dds_decoded_png/large/`.

## Review evidence

- `contact_sheets/mediterranean_large_calibrated_with_bay_rhi_binding_baselines.png`
  is the approved style comparison.
- `contact_sheets/mediterranean_large_before_after_identity_preservation.png`
  demonstrates identity preservation.
- `contact_sheets/mediterranean_runtime_dds_decoded_with_bay_rhi_baselines.png`
  is the final runtime decode comparison.
- `contact_sheets/mediterranean_runtime_dds_decoded_native_1x.png` shows the
  eight runtime images at native size.

The complete pinned inventory is `hashes/sha256_inventory.sha256`.
