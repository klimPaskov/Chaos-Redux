# Visual consistency repair: decision-category icons

Package scope: eight original small decision-category icons requested by the parent worker.

Asset type: `decision_category_icon`.

Source mode: native built-in ImageGen generation, one distinct prompt and one retained source PNG per asset.

Background mode: `native_transparent` for every asset; no background-removal fallback was used.

Target runtime canvas: exact `52x40` RGBA pixels, converted to one-level uncompressed 32-bit BGRA DDS.

Runtime folder: `gfx/interface/decisions/visual_consistency_repair/categories/`.

Evidence folder: `docs/assets/visual_consistency_repair/category_icons/`.

Contact sheets: `contact_sheet.png` is the first generated review sheet and `contact_sheet_review.png` is the clean labeled review sheet showing the native source preview, processed 1x output, enlarged smooth preview, and decoded DDS round-trip.

Strict validation record: `validation.json`.

Common DDS validation: every file is 8,448 bytes with `DDS ` magic, `DDS_HEADER` size 124, declared dimensions 52x40, pixel-format size 32, flags 65, fourCC 0, bit count 32, BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`, texture caps `0x1000`, and zero mipmaps.

All source and processed images have alpha extrema 0..255, fully transparent corners, and zero fully transparent pixels with nonzero hidden RGB; every DDS decoded pixel buffer equals its processed PNG pixel buffer exactly.

| Asset | Meaning | Source PNG | Processed PNG | Runtime DDS | Visible alpha bbox | Source SHA-256 | Processed file SHA-256 | DDS SHA-256 | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `decision_category_independence_wave_integration` | Civic and army units join beneath one common standard. | `source_png/decision_category_independence_wave_integration_source.png` | `processed_png/decision_category_independence_wave_integration.png` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_integration.dds` | `(2, 2, 49, 38)` | `09616f724dbaa8f3e6ff21ef9d2c1938721eecf1631a95da86c18fa967d6f82a` | `cc5035dcb6f8a0863a48284ac2d83d3e85e2c40b834d15aafd0326820d8be496` | `e08d3ff80519859d413f9525c03d58ecb231c00d3aa92b2d761e826d5364dbb5` | `needs_user_review` |
| `decision_category_independence_wave_government` | Founding council, blank charter, and civic seal. | `source_png/decision_category_independence_wave_government_source.png` | `processed_png/decision_category_independence_wave_government.png` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_government.dds` | `(3, 2, 49, 38)` | `5e32b3fdcc6d546756fac49410ce149715f734a5e23a52de14f1f004f952940e` | `229869f49e6c6ebcf25ccf845fb93279a727ac2e8bcbd9bc67e4e6296485cfd0` | `abc73585922ecab89a681bf18d53daab53225052918f477e6f00a2080d1c5329` | `needs_user_review` |
| `decision_category_independence_wave_diplomacy` | Clasped hands and linked treaty seals. | `source_png/decision_category_independence_wave_diplomacy_source.png` | `processed_png/decision_category_independence_wave_diplomacy.png` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_diplomacy.dds` | `(2, 2, 49, 38)` | `51b2730e3b43c6d0309eecd34018152803c0b76c33e8b9f7a4de3262b60ddc03` | `c71742a3558b337922aabc304c021a7fed43a1a193d598f0360decd17e7cea4a` | `d4c3f69f484da2ce24d02faaf70b556417b8b28db6db6aaf8d75a1cbb1f228df` | `needs_user_review` |
| `decision_category_independence_wave_network` | Rail or road nodes joined by communications links. | `source_png/decision_category_independence_wave_network_source.png` | `processed_png/decision_category_independence_wave_network.png` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_network.dds` | `(2, 4, 50, 34)` | `1c931508cb0e35f0f57750fb727a3392f7f5a3a1f5fb777a8bc5db740f6841e0` | `95ccf9fc8c8eb9aeb7f2712277f897654b7141c49534939bff757ef69a5623ed` | `ad8807ae16cc1a7641f9dc79b30b23abf4a07724c7a368763e6ec1b5e65c6b27` | `needs_user_review` |
| `decision_category_independence_wave_borders` | Frontier line, boundary markers, and arbitration seal. | `source_png/decision_category_independence_wave_borders_source.png` | `processed_png/decision_category_independence_wave_borders.png` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_borders.dds` | `(2, 2, 50, 34)` | `f864d727e98a326ed4c68eb764fd18ed75bf7cc2fda97dafeb0a7cabac66e123` | `4beb4bad853838b677e3fe8c130d7a632cd3498b8c3c567e4c4a11db1d4d5064` | `68f1fcd97bdeea6e512d9d19258d74be0a4b48bee5d5549a11aad8d0a04e17d0` | `needs_user_review` |
| `decision_category_independence_wave_death_survey` | Survey boat, charting instrument, and sounding line. | `source_png/decision_category_independence_wave_death_survey_source.png` | `processed_png/decision_category_independence_wave_death_survey.png` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_independence_wave_death_survey.dds` | `(5, 2, 49, 38)` | `e1bb0a6a1ff3f151e2d55e84d1bb753201549542b502a983bf7291ca140feb30` | `cd7ce5b6f3f6e272fdfa8f2cca2a039a7f699ce5866848090d9807defa01ba4a` | `152cc7d4613bdfb776f661f3ff52515060131f64182127317f2fa9f8d8420434` | `needs_user_review` |
| `decision_category_012_africa_charter_ledger` | African continental charter ledger with linked regional emblems and no lettering. | `source_png/decision_category_012_africa_charter_ledger_source.png` | `processed_png/decision_category_012_africa_charter_ledger.png` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_012_africa_charter_ledger.dds` | `(3, 2, 49, 38)` | `71d80899d1b5e8b490e2bb8db82cd1b3f6db8d7534fb89a8a8de2dc8f9e4e724` | `e7b4817940148d5738ca80fb7ca4b2113f8ea67984d5db200688442e898f8cc8` | `c572d6fdea7e6d73aac1716fe665c12e7d0a84477584852ec2dd2854cb5b3a7f` | `needs_user_review` |
| `decision_category_fallout_food_security` | Ration sacks, grain, and a protected communal storehouse. | `source_png/decision_category_fallout_food_security_source.png` | `processed_png/decision_category_fallout_food_security.png` | `gfx/interface/decisions/visual_consistency_repair/categories/decision_category_fallout_food_security.dds` | `(3, 3, 50, 36)` | `e318c2af4eff754834caf27afa69997e92c0ada8418e68f341137eb070069bc9` | `5e7a2c67d520be8fc31c61b60ecc86f72c5f71bae3a9f26ce43547d8c1f7858c` | `ba40c44fb3403b0bc2a53d5c89098c8cc130c9538439a53cd57375bdb65bf4e6` | `needs_user_review` |

Each prompt is retained beside the package under `prompts/<asset_name>.txt`.

Each decoded DDS review PNG is retained under `roundtrip_png/<asset_name>_dds_roundtrip.png`.

No existing file was overwritten, and no existing runtime art was used as a substitute.
