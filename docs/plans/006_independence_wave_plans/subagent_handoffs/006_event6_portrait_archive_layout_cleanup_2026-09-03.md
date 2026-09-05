# Event 006 portrait archive layout cleanup — 2026-09-03

## Result

The archive now has one flat parent folder for original source masters and the existing single `processed` child for crops, reviews, metadata, and other derivatives.

No additional subfolders were created.

## Files moved

The following two exact source-crop derivatives were already present byte-for-byte in `processed`, so the duplicate parent copies were removed by moving the parent entries onto those existing processed paths:

- `iw095_dah_abomey_royal_customary_body_source_2026_08_26_source_crop.png`
- `iw095_dah_casimir_dalmeida_source_2026_08_27_source_crop.png`

The SHA-256 values were checked before the move and remained `A1742DFF3BB1A3C238FA22F42ABEFE6AF9B1BE1391686835AC4CA77F5D88812A` and `18E44CDC0EB8D4D2146BC8936F8CDE67A97238815DEE0D5EC912A9E7DEB164FD` respectively.

## Post-cleanup checks

`docs/assets/portraits/006_independence_wave/` contains exactly one directory, `processed`, and the parent contains zero `source_crop` files.

`docs/assets/portraits/006_independence_wave/processed/` contains both canonical crop files and no child directories.

Original source masters were not deleted, renamed, or relabelled, and no runtime portrait, GFX, gameplay, localisation, or admission surface changed.
