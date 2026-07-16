# Event 006 Mediterranean portrait validation

Date: 2026-07-16

Result: accepted. The runtime package contains eight distinct, adult-male,
156x210 large portraits and no small or advisor artwork.

## Consumer-to-runtime audit

| Consumer | Registered sprite | DDS SHA-256 |
|---|---|---|
| `COR_corsican_municipal_congress` | `GFX_portrait_COR_independence_wave_petru_santucci` | `60074ec4ff2d0fa1aa87059c3da95d2ce5b15a77d43ca356440e6563f031ba35` |
| `COR_pasquale_venturi` | `GFX_portrait_COR_independence_wave_pasquale_venturi` | `ca51d10deb1ecad55f2c14d766ac6e02082f48649c001b2f39212af236da3fc9` |
| `ARX_sardinian_provisional_assembly` | `GFX_portrait_ARX_independence_wave_antioco_melis` | `c279d1c079b8d6174395124471ca8651b17292ebe6dcdb374000b135d6ed49ec` |
| `ARX_sardinian_crown_consultative_council` | `GFX_portrait_ARX_independence_wave_vittorio_pala` | `443e92aca9f57fce6988296692949f70a859508ff85f85b30a61897243214fae` |
| `ARX_gavino_piras` | `GFX_portrait_ARX_independence_wave_gavino_piras` | `f8eab9bfe2551ba68166bbf698e486f1dac1452f1509801a59db5ca8ad20a4b7` |
| `ASX_sicilian_provisional_assembly` | `GFX_portrait_ASX_independence_wave_sebastiano_restivo` | `f9cbdf5f7754bddf54be88b3e7f328ed227dc025aba06b4c0b6c94e8c1e19482` |
| `ASX_sicilian_crown_council` | `GFX_portrait_ASX_independence_wave_vincenzo_lanza` | `71906593b9ba35ed9793ce110ae16ce0b84968ecad537be60138e7899d33d012` |
| `ASX_salvatore_licata` | `GFX_portrait_ASX_independence_wave_salvatore_licata` | `e7348e508b4e9b8170448621582842aca106b5764a489d90edd4e8fa580c5e02` |

The character file contains all eight large consumers, the GFX file contains
exactly eight matching sprite registrations, and every registered texture
exists at the expected path.

## DDS contract and decode audit

Every runtime file passed the same binary checks:

- 156x210 pixels;
- uncompressed 32-bit BGRA/B8G8R8A8 layout;
- 128-byte DDS header, 124-byte DDS structure, 32-byte pixel-format structure;
- pixel-format flags `65` (`RGB | ALPHAPIXELS`), FourCC `0`;
- masks `R=0x00ff0000`, `G=0x0000ff00`, `B=0x000000ff`,
  `A=0xff000000`;
- pitch 624 bytes, texture caps `0x1000`, no mip chain;
- exact file length 131,168 bytes;
- decoded DDS pixels equal the corresponding calibrated PNG pixel for pixel.

All eight DDS file hashes and all eight decoded RGBA hashes are unique. The
decoded contact sheet was visually approved against the protected BAY/RHI
baseline.

## Male-only proof

- The pinned prompt record contains exactly eight `fictional adult male`
  constraints, one for every retained source.
- The final and decoded contact sheets contain eight individual adult men and
  no female subject, collective, placeholder, or duplicate identity.
- Distinguishing traits remain visible after calibration: Petru's full dark
  moustache; Pasquale's broad stubbled face; Antioco's wire-rim glasses;
  Vittorio's white handlebar moustache; Gavino's scar and dark moustache;
  Sebastiano's swept-back curls and expressive brows; Vincenzo's aquiline
  profile and broad white moustache; Salvatore's widow's peak and narrow face.

## Protected-reference integrity

The binding visual references were read but not edited. Their runtime hashes
remain:

- BAY Rupprecht:
  `7f0af64fdf4fecd49df454d1198935bb3ce6a8f74afc1ac82f8223704eaaad2b`
- RHI Matthes:
  `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`

## No-small and no-advisor-art audit

- No Mediterranean character consumer refers to a COR/ARX/ASX `_small`
  sprite.
- The new GFX file contains no `_small` registration and exactly eight large
  sprite types.
- The package contains no filename with `small`, `advisor`, or `dossier`.
- The prompt record contains no 65x67, small-output, dossier, or advisor-art
  section.
- No COR/ARX/ASX small or advisor DDS was created.

The generic leader-processing script filename found in retained
pre-calibration metadata is not an asset role: each record is `mode = leader`,
and no dossier overlay entered the accepted large pipeline.

## Style and identity review

The approved comparison sheet places the protected BAY/RHI portraits beside
the eight final portraits. The final pass uses muted gray/sepia color,
archival/colorized-photo facial texture, restrained brushwork, fine matte grain,
and flatter studio values while preserving eight distinct faces and role-based
lighting. The before/after sheet confirms no pose, facial geometry, clothing,
or identity replacement.
