# Event 014 Warlord Portrait Processing

## Reference review

The event-assets skill has no dedicated leader-portrait reference folder in this checkout. The closest relevant precedent was therefore the installed vanilla HOI4 156 by 210 leader portrait set. Eight vanilla portraits were inspected in `../contact_sheets/vanilla_portrait_reference_contact.png` for face scale, upper-torso framing, subdued backdrop, and thumbnail readability. No vanilla portrait was supplied to image generation or copied into a final asset.

## Processing boundary

Local processing performed only manual cover crops, Lanczos resizing, RGBA PNG export, review-sheet assembly, and DDS conversion. It did not paint blood, replace faces, add props, recolor identities, or assemble one source into multiple portraits.

| Slot | Source crop box `(left, top, right, bottom)` | Processed size |
| --- | --- | --- |
| CBA | `(50, 0, 1030, 1320)` | `156x210 RGBA` |
| CBB | `(55, 0, 1025, 1306)` | `156x210 RGBA` |
| CBC | `(75, 0, 1005, 1252)` | `156x210 RGBA` |
| CBD | `(50, 0, 990, 1266)` | `156x210 RGBA` |
| CBE | `(110, 40, 970, 1198)` | `156x210 RGBA` |
| CBF | `(70, 0, 1010, 1266)` | `156x210 RGBA` |
| CBG | `(125, 25, 955, 1142)` | `156x210 RGBA` |
| CBH | `(140, 10, 940, 1087)` | `156x210 RGBA` |

Final conversion used `.tools/convert_to_dds.py` with explicit width `156`, height `210`, one mip level, and uncompressed BGRA/B8G8R8A8-style channel masks.
