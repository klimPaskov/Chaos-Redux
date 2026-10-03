# Event 014 Hannibal static portrait receipt

Receipt date: 2026-10-03.

Status: protected user-supplied runtime files; this receipt records the current bytes and bindings and does not claim external source rights or artistic acceptance.

The parent brief preserves both static portraits as protected user-supplied assets based on the prior Event 014 completion records identifying these exact runtime files. The earlier receipt named in that completion record was absent in this checkout, so this record was reconstructed from the present runtime files and the retained Event 014 handoffs. This identifies the retained evidence basis without inferring a new user approval or missing artistic acceptance.

| Runtime file | Dimensions | Bytes | Current SHA-256 | Current DDS header and pixel evidence |
| --- | ---: | ---: | --- | --- |
| `hannibal.dds` | 156x210 | 174,608 | 5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88 | 32-bit BGRA, 8 mips, alpha (255, 255) |
| `hannibal_wendigo.dds` | 156x210 | 174,608 | 26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717 | 32-bit BGRA, 8 mips, alpha (255, 255) |

Both files decode as opaque RGBA at 156x210. Their DDS pixel format is 32-bit with masks `0x00ff0000, 0x0000ff00, 0x000000ff, 0xff000000` and mip count 8. The legacy mip chain is retained exactly.

## Wiring

`interface/014_cannibalism.gfx` binds `GFX_portrait_CBL_hannibal` and `GFX_cannibalism_revealed_portrait_static` to `gfx/leaders/014_cannibalism/hannibal.dds`. It binds `GFX_portrait_ZZZ_hannibal_wendigo` and `GFX_cannibalism_wendigo_portrait_static` to `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`. The CBL and ZZZ character entries in `common/characters/014_cannibalism_characters.txt` reference the corresponding `GFX_portrait_*` sprites.

The protected animated sheets remain byte-identical to the retained hashes:

| Runtime file | Dimensions | Bytes | Current SHA-256 |
| --- | ---: | ---: | --- |
| `leader_CBL_hannibal_sheet.dds` | 1872x210 | 1,572,608 | `f67a1b33a1d4f9b9b1b5ec0d6fb716ad1f2342083e9992550b5dd7356f590587` |
| `leader_ZZZ_hannibal_wendigo_sheet.dds` | 2496x210 | 2,096,768 | `f0dfa61ea29293f8393711f97eb67524d336cb6c2a2d55734c0c38484219d18b` |

## Visual review and provenance limits

The current static pair was decoded from the runtime DDS files and visually inspected in [`current_review/event014_hannibal_protected_static_pair.png`](current_review/event014_hannibal_protected_static_pair.png). The ordinary portrait presents a centered face against a dark red background; the Wendigo portrait uses a high-contrast black silhouette, red/white arcs, and a white field. This is a review of the current installed pixels only.

No original source files, source URL, named creator, crop record, processing record, redistribution license, public-domain basis, or independent art-acceptance receipt was present in the checkout. This receipt does not infer any of those facts from the supplied runtime DDS files. The earlier source audit also records that the missing original/crop/license evidence was unresolved.

No runtime image was rewritten. The PNG contact sheet is review evidence only and is not a replacement portrait.
