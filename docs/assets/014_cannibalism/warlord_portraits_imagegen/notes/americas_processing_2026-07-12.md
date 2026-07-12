# Event 014 Americas Warlord Portrait Processing

Tranche: `E14-POR-WARLORD-AMERICAS-2026-07-12`

Scope: CBA-CBH `north_america` and `south_america` only. Oceania was reassigned before any Oceania asset was produced by this tranche.

## Processing boundary

Each accepted built-in `image_gen` source was preserved at its frozen source path. Local work was limited to a manually reviewed cover crop, Lanczos resize, RGBA PNG export, contact-sheet assembly, and conversion with `.tools/convert_to_dds.py`. No face, blood, clothing, prop, background, anatomy, or regional appearance was painted or fabricated locally.

## Crop ledger

Crop boxes are `(left, top, right, bottom)` in source pixels.

| Slot | Region | Source dimensions | Crop box | Final PNG |
| --- | --- | ---: | --- | --- |
| CBA | North America | 1081x1455 | `(0, 0, 1081, 1455)` | 156x210 RGBA |
| CBB | North America | 1080x1456 | `(0, 1, 1080, 1455)` | 156x210 RGBA |
| CBC | North America | 1024x1536 | `(0, 80, 1024, 1458)` | 156x210 RGBA |
| CBD | North America | 1080x1456 | `(0, 1, 1080, 1455)` | 156x210 RGBA |
| CBE | North America | 1082x1454 | `(1, 0, 1081, 1454)` | 156x210 RGBA |
| CBF | North America | 864x1821 | `(0, 160, 864, 1323)` | 156x210 RGBA |
| CBG | North America | 1080x1456 | `(0, 1, 1080, 1455)` | 156x210 RGBA |
| CBH | North America | 1080x1456 | `(0, 1, 1080, 1455)` | 156x210 RGBA |
| CBA | South America | 1081x1455 | `(0, 0, 1081, 1455)` | 156x210 RGBA |
| CBB | South America | 1024x1536 | `(0, 120, 1024, 1498)` | 156x210 RGBA |
| CBC | South America | 1024x1536 | `(0, 70, 1024, 1448)` | 156x210 RGBA |
| CBD | South America | 1024x1536 | `(0, 20, 1024, 1398)` | 156x210 RGBA |
| CBE | South America | 1024x1536 | `(0, 0, 1024, 1378)` | 156x210 RGBA |
| CBF | South America | 1024x1536 | `(0, 50, 1024, 1428)` | 156x210 RGBA |
| CBG | South America | 1024x1536 | `(0, 20, 1024, 1398)` | 156x210 RGBA |
| CBH | South America | 1024x1536 | `(0, 0, 1024, 1378)` | 156x210 RGBA |

South America CBB was moved farther down than a centered crop so the full weighted bell clapper remains visible without cutting the bald head. North America CBF received the only large vertical trim; four crop candidates were reviewed before selecting the box that preserves the head, unequal eyes, motor grille, tyre chain, and crank hand.

## DDS conversion

Every processed PNG was converted through `.tools/convert_to_dds.py` with explicit width `156`, height `210`, BGRA/B8G8R8A8-style output, and one stored image level. Runtime files use the already-registered paths under `gfx/leaders/014_cannibalism/`.

