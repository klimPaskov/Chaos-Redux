# Event 006 Brittany regionalist portrait parent integration

Date: 2026-07-22  
Scope: `IW-004` civic leader portrait and identity only  
Disposition: `approved_and_wired`; package-level re-admission remains subject
to the fresh country-package audit

## Result

The stable `BRI_independence_wave_civic_delegate` token now presents the real
male Breton regionalist Régis de l'Estourbeillon. The existing
`GFX_portrait_BRI_independence_wave_civic_commission` sprite continues to point
to the same runtime path, but that path now contains the independently reviewed
v3 identity-preserving HOI4 repaint of John Wickens's 1904 photograph.

No new character token, sprite, advisor, dossier, commander miniature,
`_small` portrait, female identity, generated substitute, or alternate runtime
surface was added.

## Source and visual authority

- Unchanged source: John Wickens, *A Book of Mad Celts* (1904), retained at
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/source_masters/BRI/BRI_regis_de_l_estourbeillon_john_wickens_1904.jpg`.
- Source SHA-256:
  `C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D`.
- Processed v3 PNG:
  `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/processed_png/leader_bri_regionalist_regis_de_l_estourbeillon_v3.png`.
- Processed SHA-256:
  `5426E39BC1622E7ECD32A41CC0A1C05D6596446A40FA0B7BA2047EF350BBAE80`.
- Independent audit:
  `006_bri_regionalist_regis_de_l_estourbeillon_v3_visual_provenance_audit_2026-07-22.md`.
- Audit result: likeness, male-only, role, explicit head-and-shoulders crop,
  full-color restrained HOI4 finish, costume, provenance, native readability,
  and absence of invented symbols all passed.

## Runtime output

- Preserved package DDS:
  `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/final_dds/BRI/portrait_BRI_independence_wave_civic_commission.dds`.
- Runtime DDS:
  `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`.
- DDS SHA-256:
  `583F821ED7F8B78A89321DBB7E1E7B7CAD7E30829DFA5DD14B6F255E42E27DC0`.
- Both files are byte-identical legacy one-level uncompressed BGRA DDS files,
  exactly `156x210`, exactly 131,168 bytes, with opaque alpha.
- Decoded RGB pixels are identical to the approved v3 processed PNG.
- The existing `.gfx` declaration was retained unchanged because its stable
  sprite and texture path were already correct.

## Player-facing alignment

`localisation/english/006_independence_wave_brittany_l_english.yml` now names
Régis de l'Estourbeillon and describes his documented regionalist-union and
Morbihan-deputy background. The package documentation now treats him as the
researched role-compatible civic figure rather than retaining the fictional
Tangi Kerbrat placeholder or presenting the unavailable Debeauvais material as
the only possible source path.

## Protected and excluded surfaces

- Rupprecht of Bavaria retained SHA-256
  `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`.
- Josef Friedrich Matthes retained SHA-256
  `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`.
- No Event 006 advisor or `_small` file exists under
  `gfx/leaders/006_independence_wave/`.

## Remaining package boundary

The civic portrait is complete, but portrait completion alone does not grant
allocator readiness. `iw_004` remains outside the deliberately empty
compile-time content-attestation set until the fresh post-replacement Brittany
country-package audit verifies the complete roster and the existing gameplay,
AI, focus, decision, force, cleanup, host-survival, reservation, Event 5
collision, and scenario contracts.
