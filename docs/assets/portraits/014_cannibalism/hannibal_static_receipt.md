# Event 014 canonical Hannibal static portrait receipt

Receipt date: 2026-08-26.

Scope: the two exact static portrait textures supplied by the user for the revealed Hannibal Lecter and Wendigo Hannibal character bindings.

## Protected files

| Runtime file | User-supplied canonical path | Dimensions | Bytes | SHA-256 |
| --- | --- | ---: | ---: | --- |
| `gfx/leaders/014_cannibalism/hannibal.dds` | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\gfx\leaders\014_cannibalism\hannibal.dds` | 156x210 | 174608 | `5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88` |
| `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\gfx\leaders\014_cannibalism\hannibal_wendigo.dds` | 156x210 | 174608 | `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717` |

Both files were observed as valid 32-bit uncompressed BGRA DDS textures with eight mip levels and opaque alpha, and the bytes remain unchanged from the protected runtime files.

## Wiring

`interface/014_cannibalism.gfx:232` binds the ordinary static texture through `GFX_portrait_CBL_hannibal`, while lines 560-563 bind the ordinary and Wendigo static fallback aliases to these same protected files.

The animated sheets remain separate runtime assets and are not regenerated or replaced by this receipt.

## Evidence boundary

This receipt records the exact user-supplied files, their observed format, hashes, dimensions, and runtime bindings; it does not assert an external source URL, redistribution licence, original crop, or independent visual acceptance.

The 56 regional warlord portraits remain source placeholders with `replacement_pending: true`, and no 3D workflow was used or reopened.
