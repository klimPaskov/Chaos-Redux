# Event 014 Europe/Asia/Africa Warlord Portrait Processing

Tranche ID: `E14-POR-WARLORD-EAA-01`

## Reference basis

The installed vanilla HOI4 `156x210` leader-portrait set was inspected for face
scale, upper-torso readability, subdued period backgrounds, and thumbnail
silhouette. The Event 014 registrations in `interface/014_cannibalism.gfx` were
checked before output filenames were frozen. No vanilla portrait was supplied to
image generation or copied into a final asset.

## Image-generation boundary

Final blood-like dark-burgundy field staining is present in the accepted
imagegen source itself. When a direct stained prompt was output-moderated, the
same built-in image generator produced a clean prop/pose base and then performed
a precise surface-color edit. Local image processing never painted stains,
changed a face, added a prop, or created a second portrait from one source.

## Crop and resize

All 24 accepted sources were reviewed in the source contact sheets before
processing. Their source aspect ratios were already at or extremely close to the
HOI4 leader-portrait ratio. A centered cover crop therefore removed only the
minimum edge pixels needed to reach `156:210`, preserving every face, hand, and
identity prop. The exact per-file source dimensions and crop rectangles are in
`europe_asia_africa_crop_ledger.csv`.

Each crop was converted to RGBA and resized once with Lanczos sampling to
`156x210`. The reproducible, tranche-limited helper is
`../build_europe_asia_africa_tranche.py`; it names the 24 owned files explicitly
and does not discover or modify other regions.

## DDS conversion

Each processed PNG was converted with the repository-standard
`.tools/convert_to_dds.py`, passing explicit width `156`, height `210`, BGRA
output, and one image level. Runtime files are uncompressed 32-bit DDS with:

- header size `124`
- row pitch `624`
- pixel-format flags `0x41` (`RGB` plus alpha pixels)
- bit depth `32`
- red mask `00FF0000`
- green mask `0000FF00`
- blue mask `000000FF`
- alpha mask `FF000000`
- texture caps `0x1000`
- file size `131168` bytes

The build helper then decoded every DDS and compared its RGBA pixels directly to
the processed PNG. Detailed machine results are retained in
`europe_asia_africa_validation.json`.
