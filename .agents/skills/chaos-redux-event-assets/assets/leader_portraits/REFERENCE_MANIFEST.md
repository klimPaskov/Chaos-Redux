# Curated male portrait reference manifest

This manifest records the binary copies retained in `assets/leader_portraits/`.
Every portrait PNG is an exact copy of a canonical Vanilla HOI4 review PNG from
`../vanilla_reference/portraits/`. The pack is reference-only and must never be
wired or shipped as Chaos Redux runtime art. Canonical provenance, dimensions,
source DDS paths, and owning definitions remain in
[`../vanilla_reference/CATALOG.md`](../vanilla_reference/CATALOG.md).

## Portrait copies

All twelve portrait copies decode as RGBA `156x210` PNGs. Pack and canonical
SHA-256 values are identical.

| Role | Pack PNG | Canonical PNG | Vanilla source DDS | Owning definition | SHA-256 |
| --- | --- | --- | --- | --- | --- |
| Country leader | `leaders/afg_mohammed_zahir_shah.png` | `../vanilla_reference/portraits/leaders/afg_mohammed_zahir_shah.png` | `gfx/leaders/AFG/Portrait_Afghanistan_Mohammed_Zahir_Shah.dds` | — | `f606bc3c6204e0dbd35d8edceb21f87ae6f93a0ae7ad657382c7e9043e8907a0` |
| Country leader | `leaders/den_thorvald_stauning.png` | `../vanilla_reference/portraits/leaders/den_thorvald_stauning.png` | `gfx/leaders/DEN/Portrait_Denmark_Thorvald_Stauning.dds` | — | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` |
| Country leader | `leaders/eth_haile_selassie.png` | `../vanilla_reference/portraits/leaders/eth_haile_selassie.png` | `gfx/leaders/ETH/Portrait_Ethiopia_Haile_Selassie.dds` | — | `e06bc1bd67ce70e1fb22e39d4c6d2732327d23a58efeb74b096b456318b7eb4b` |
| Country leader | `leaders/ire_eamon_de_valera.png` | `../vanilla_reference/portraits/leaders/ire_eamon_de_valera.png` | `gfx/leaders/IRE/Portrait_Ireland_Eamon_de_Valera.dds` | — | `ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0` |
| Land commander | `commanders/eng_bernard_montgomery.png` | `../vanilla_reference/portraits/commanders/eng_bernard_montgomery.png` | `gfx/leaders/ENG/Portrait_Britain_Bernard_Montgomery.dds` | `common/characters/ENG.txt` | `39b03871d7451ca96712a5ccf3c056528693f82642776e6c5e297e041943944e` |
| Land commander | `commanders/generic_africa_land_1.png` | `../vanilla_reference/portraits/commanders/generic_africa_land_1.png` | `gfx/leaders/Africa/Portrait_Africa_Generic_land_1.dds` | `interface/_random_portraits.gfx` | `17d875344719b09a03ef32cc3329971778a738c4ac20210f6cbb7394a1e7585f` |
| Land commander | `commanders/generic_africa_land_3.png` | `../vanilla_reference/portraits/commanders/generic_africa_land_3.png` | `gfx/leaders/Africa/Portrait_Africa_Generic_land_3.dds` | `interface/_random_portraits.gfx` | `76731af64301c3c68eee012a9eb9f001f4a11561e42bbb13cae0949ea5535b0b` |
| Naval commander | `commanders/generic_africa_navy_1.png` | `../vanilla_reference/portraits/commanders/generic_africa_navy_1.png` | `gfx/leaders/Africa/Portrait_Africa_Generic_navy_1.dds` | `interface/_random_portraits.gfx` | `6351227cc9a7416698d2b94e87ea07fb1cf97afe8874cbee2015a3362cfcb0ec` |
| Naval commander | `commanders/generic_africa_navy_2.png` | `../vanilla_reference/portraits/commanders/generic_africa_navy_2.png` | `gfx/leaders/Africa/Portrait_Africa_Generic_navy_2.dds` | `interface/_random_portraits.gfx` | `a608d7554187cd944130862e09ed4279fd5311f16a6735d07cf357148d11250f` |
| Land commander | `commanders/ger_erich_von_manstein.png` | `../vanilla_reference/portraits/commanders/ger_erich_von_manstein.png` | `gfx/leaders/GER/Portrait_Germany_Erich_von_Manstein.dds` | `common/characters/GER.txt` | `7bd74774884e907f4ca6289d20d31d7bfa2546b089b891588a2a8f9de722a71b` |
| Land commander | `commanders/ger_erwin_von_witzleben.png` | `../vanilla_reference/portraits/commanders/ger_erwin_von_witzleben.png` | `gfx/leaders/GER/Portrait_Germany_Erwin_von_Witzleben.dds` | `common/characters/GER.txt` | `10f4a1108f9d440213f70fb5802349a2291f298f9d132644241119561577d5b6` |
| Land commander | `commanders/ita_pietro_badoglio.png` | `../vanilla_reference/portraits/commanders/ita_pietro_badoglio.png` | `gfx/leaders/ITA/Portrait_Italy_Pietro_Badoglio.dds` | `common/characters/ITA.txt` | `9f4f2a5a8d3260ab24866821d3c4edfc75d7bdb1cd0444124d518f7854890e9f` |

## Contact sheets

| Pack sheet | Canvas | SHA-256 |
| --- | ---: | --- |
| `leaders/contact_sheet.png` | `440x558` RGB | `bf1ac6a6ed7f1d91b3fa8e4069c7b9f396bb63f450af1fe340005f7981a3cb60` |
| `commanders/contact_sheet.png` | `930x900` RGB | `ab02faef684f7b8b62806ec98edb671b61a37dd806762d604155db3119c3c8de` |

The pack contains no female portrait, advisor icon, dossier card, `_small`
derivative, generated identity, or Event 6 runtime asset.
