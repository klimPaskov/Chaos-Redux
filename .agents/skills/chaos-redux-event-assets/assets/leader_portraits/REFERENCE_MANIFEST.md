# Curated male portrait reference manifest

This manifest records the binary copies retained for the top-level
`assets/leader_portraits/` compatibility pack. Every PNG below is an exact
copy of a canonical Vanilla HOI4 review PNG from
`../vanilla_reference/portraits/`; the pack files are reference-only and must
never be wired or shipped as Chaos Redux runtime art.

Canonical provenance, native dimensions, source DDS paths, and owning
definitions remain in [`../vanilla_reference/CATALOG.md`](../vanilla_reference/CATALOG.md).

## Portrait copies

All eight portrait copies decode as RGBA `156x210` PNGs. Pack and canonical
SHA-256 values are identical because the files are byte-for-byte copies.

| Role | Pack PNG | Canonical PNG | Vanilla source DDS | Owning definition | SHA-256 |
| --- | --- | --- | --- | --- | --- |
| Country leader | `leaders/afg_mohammed_zahir_shah.png` | `../vanilla_reference/portraits/leaders/afg_mohammed_zahir_shah.png` | `gfx/leaders/AFG/Portrait_Afghanistan_Mohammed_Zahir_Shah.dds` | — | `f606bc3c6204e0dbd35d8edceb21f87ae6f93a0ae7ad657382c7e9043e8907a0` |
| Country leader | `leaders/den_thorvald_stauning.png` | `../vanilla_reference/portraits/leaders/den_thorvald_stauning.png` | `gfx/leaders/DEN/Portrait_Denmark_Thorvald_Stauning.dds` | — | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` |
| Country leader | `leaders/eth_haile_selassie.png` | `../vanilla_reference/portraits/leaders/eth_haile_selassie.png` | `gfx/leaders/ETH/Portrait_Ethiopia_Haile_Selassie.dds` | — | `e06bc1bd67ce70e1fb22e39d4c6d2732327d23a58efeb74b096b456318b7eb4b` |
| Country leader | `leaders/ire_eamon_de_valera.png` | `../vanilla_reference/portraits/leaders/ire_eamon_de_valera.png` | `gfx/leaders/IRE/Portrait_Ireland_Eamon_de_Valera.dds` | — | `ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0` |
| Land commander | `commanders/generic_africa_land_1.png` | `../vanilla_reference/portraits/commanders/generic_africa_land_1.png` | `gfx/leaders/Africa/Portrait_Africa_Generic_land_1.dds` | `interface/_random_portraits.gfx` | `17d875344719b09a03ef32cc3329971778a738c4ac20210f6cbb7394a1e7585f` |
| Land commander | `commanders/generic_africa_land_3.png` | `../vanilla_reference/portraits/commanders/generic_africa_land_3.png` | `gfx/leaders/Africa/Portrait_Africa_Generic_land_3.dds` | `interface/_random_portraits.gfx` | `76731af64301c3c68eee012a9eb9f001f4a11561e42bbb13cae0949ea5535b0b` |
| Naval commander | `commanders/generic_africa_navy_1.png` | `../vanilla_reference/portraits/commanders/generic_africa_navy_1.png` | `gfx/leaders/Africa/Portrait_Africa_Generic_navy_1.dds` | `interface/_random_portraits.gfx` | `6351227cc9a7416698d2b94e87ea07fb1cf97afe8874cbee2015a3362cfcb0ec` |
| Naval commander | `commanders/generic_africa_navy_2.png` | `../vanilla_reference/portraits/commanders/generic_africa_navy_2.png` | `gfx/leaders/Africa/Portrait_Africa_Generic_navy_2.dds` | `interface/_random_portraits.gfx` | `a608d7554187cd944130862e09ed4279fd5311f16a6735d07cf357148d11250f` |

The four named country-leader references and four generic Africa commander
references were visually checked against their canonical contact sheets and
are male-presenting. This is a style-reference classification; it does not
create character metadata, a name pool, or a claim about the identities of
generic commander portraits.

## Pack contact sheets

The contact sheets contain only the eight curated male references above and
are review aids, not final assets.

| Pack sheet | Canvas | SHA-256 |
| --- | ---: | --- |
| `leaders/contact_sheet.png` | `440x558` RGB | `bf1ac6a6ed7f1d91b3fa8e4069c7b9f396bb63f450af1fe340005f7981a3cb60` |
| `commanders/contact_sheet.png` | `440x558` RGB | `9c56b18b1d6115c3cc5c6b46a90b7b26121b46182822cef1b8fae05835834faf` |

No female leader, advisor, theorist, high-command, officer-corps, or Event 6
asset is included in this compatibility pack. Use
`../vanilla_reference/portraits/advisors/` for the separate `65x67` dossier
family and follow the advisor provenance workflow when that asset type is
explicitly required.
