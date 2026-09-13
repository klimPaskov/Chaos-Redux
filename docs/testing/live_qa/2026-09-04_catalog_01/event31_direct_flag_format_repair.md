# Event 31 direct flag format repair

Date: `2026-09-05`

Status: parent-owned native retest and final visual consumer acceptance pending.

## Scope and source mode

This bounded repair covers exactly the 24 direct no-suffix carrier flag files for `JHX`, `JIX`, `JKX`, `JLX`, `JMX`, `JNX`, `JOX`, and `JPX` under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

The artwork is the already approved Event 031 dormant-carrier ladder, reused from the matching `event31_dormant_carrier_01` through `event31_dormant_carrier_08` TGAs with RGB pixels unchanged.

This is an inherited approved-artwork format repair, so no ImageGen call, new source PNG, processed preview, DDS, contact-sheet refresh, `.gfx` edit, or gameplay edit was made.

## Backup evidence

The exact pre-repair bytes were copied before conversion to `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_direct_flag_format/`, with normal, medium, and small subfolders and no overwrite of existing backup files.

The backup contains `24` files, and each backup SHA-256 is recorded in the table below as `backup_sha256`.

## Conversion contract

Each target was converted to an uncompressed TGA image type `2` with `32` bits per pixel and descriptor `8`.

Descriptor `8` retains bottom-left origin and declares an 8-bit alpha channel, while every emitted alpha byte is `255`.

The original BGR payload order, dimensions, and physical row order were retained, and one opaque alpha byte was appended to each source pixel.

The expected dimensions are normal `82x52`, medium `41x26`, and small `10x7`.

## File hashes and validation

`backup_sha256` is the exact pre-repair file hash, and `final_sha256` is the repaired runtime file hash.

| Target | Approved source ladder | Dimensions | Bytes | Backup SHA-256 | Final SHA-256 | Header and decoded checks |
| --- | --- | ---: | ---: | --- | --- | --- |
| `gfx/flags/JHX.tga` | `gfx/flags/event31_dormant_carrier_01.tga` | `82x52` | `17074` | `3d0d07512bf49d9fbea040bfbdc608ca85ee676709765f870731ccda97fae67e` | `0f26869f6a6285b7a403eab29c058953ba70d233176007cc1be4eeb9c21fe95c` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/medium/JHX.tga` | `gfx/flags/medium/event31_dormant_carrier_01.tga` | `41x26` | `4282` | `61e90edfc459e91bf4505430d4dfb0965fe40761d43043142e8380c2525fccc9` | `418a27b20c1a4969b6e84a55aafcc34378dd6edfd1103d12782dd76c642cbefd` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/small/JHX.tga` | `gfx/flags/small/event31_dormant_carrier_01.tga` | `10x7` | `298` | `54ade04c09906d54c3e40e2263b48a6e92bd12fb572f8b5fa34098e82020a7a9` | `d993ce1c4329496547da2040764e6c772fe60ff5ce99e0620c5569de55a67296` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/JIX.tga` | `gfx/flags/event31_dormant_carrier_02.tga` | `82x52` | `17074` | `83532b0e65796f84bba564321b585948d231f5c62ac743c27f588206e2839cd3` | `dbbe843b7bac10f885f778e4c4b50518fdc2a528be8e015c0848d63d1ed20b87` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/medium/JIX.tga` | `gfx/flags/medium/event31_dormant_carrier_02.tga` | `41x26` | `4282` | `030de0309000d23b141cdea250389a92c7f7444b4dbd5a5f95b2137d0e8b2c0d` | `6c37a5aae44a1e4c11309d5bcb3c9f3dc65fa4b8a70d5209a47f877d32718d83` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/small/JIX.tga` | `gfx/flags/small/event31_dormant_carrier_02.tga` | `10x7` | `298` | `b0acafd1fa12b2de34ee4eae2eabe7e7d7cfad6bcc88f2a4e46feaffde2f96bc` | `8436dea414503d421f869284d44c536f1443b436bcb9314b2e735b1793d7c2a2` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/JKX.tga` | `gfx/flags/event31_dormant_carrier_03.tga` | `82x52` | `17074` | `38fea07ea13b4612414ac1e659a052c2dfaf556458759d47edbe8b3115212cce` | `f210ea16b34e3607b8faab0b0a0a1e82b059bfea077d1288d027d0d85232f0e2` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/medium/JKX.tga` | `gfx/flags/medium/event31_dormant_carrier_03.tga` | `41x26` | `4282` | `94349b77b21d1d2c9fa4c42d39722b6fb5d48d6ead7e3599c50bc432aca508c1` | `f025ccb3ac4418b1942eb3f177b5936fec89d6161d3757fd8a011adffa61a839` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/small/JKX.tga` | `gfx/flags/small/event31_dormant_carrier_03.tga` | `10x7` | `298` | `79848301060366b728997692246c1daea09ccf85b46acf83a199680d31c98c70` | `8035ef9a14c8744d353cd09ae2584450e98408006dfcced924e0baa53495e04b` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/JLX.tga` | `gfx/flags/event31_dormant_carrier_04.tga` | `82x52` | `17074` | `e64577d3c397b7be59ce6bd11e23ffbfb0df99c678f8aa9a920d6a6f5da73e93` | `3846b34bf5bbe4287ed44cacc6fcc3bc9cc0f7de3867f545c6cfd77e16754944` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/medium/JLX.tga` | `gfx/flags/medium/event31_dormant_carrier_04.tga` | `41x26` | `4282` | `766db1e1f069b3213ccb2eafd0c2857cb7876fb3aeac2074c0aed9b9f6c5094b` | `eb507d7ceb68531e87ecb92c5f280a96165f16ff1781b3bf1def2aadc01f2cbd` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/small/JLX.tga` | `gfx/flags/small/event31_dormant_carrier_04.tga` | `10x7` | `298` | `8f6f162c516110e873359e4508913ddc3cfeba7d24ffa03d2ea36b1cbc4ce9e7` | `c705db59e7f69d5ad3ceada45f586c858f432f220d4e647fdc386187e4875aff` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/JMX.tga` | `gfx/flags/event31_dormant_carrier_05.tga` | `82x52` | `17074` | `861a5d4ab10ab38346f92c593829be2007ab1751853dc8d5f8c2aa3be22b6fc0` | `a9337b0bb607859963c415ce2a1b432f503d684af0cf0f0f017d0ca10b4a5740` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/medium/JMX.tga` | `gfx/flags/medium/event31_dormant_carrier_05.tga` | `41x26` | `4282` | `3af09b9349b771a27424e14a0d17a7dc00091d0bc769b24dd121cbe9e2dc7832` | `61de615f252a7026a4b9b4a2a1f86453c03349449de2a4e3ae4a7ed4d7e5558e` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/small/JMX.tga` | `gfx/flags/small/event31_dormant_carrier_05.tga` | `10x7` | `298` | `c89414ec06819d692359128954c9c2afd6ed66c75b55ed161918ce37717cfa62` | `6fc996bfb9fbec9ba06f13d858b53cce79cc12deda2b3c428d825351a35b2d78` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/JNX.tga` | `gfx/flags/event31_dormant_carrier_06.tga` | `82x52` | `17074` | `50eb52d609b30e1e77013739979928bf2d87a24c17a1999b8228ad42afada176` | `991d5fa21b40c0f46a54289bb05b8e64c3b7517b5f9b8439f8af46bd7ca3818d` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/medium/JNX.tga` | `gfx/flags/medium/event31_dormant_carrier_06.tga` | `41x26` | `4282` | `03aa520308c8fcdce1935bde1880a5201d1de0bbab4bedfa823b7d664dbb0681` | `bf79d9b846e1ee645cbba8ee0c19dd823208637b5f43a2ede0c8909a51f429e0` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/small/JNX.tga` | `gfx/flags/small/event31_dormant_carrier_06.tga` | `10x7` | `298` | `beb374d3e7a15773fb1cf32c0bf0fdc7bc2a8b06aa1ab5704ec0b88f211da283` | `2089c461388af653ae15b4f73f0a0ff57f33e6977d24230825b4f741d8d58d3e` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/JOX.tga` | `gfx/flags/event31_dormant_carrier_07.tga` | `82x52` | `17074` | `b6380fa6b7cc9828f10a44d013fc47cda05df6388553aad0f042d84fa6638df8` | `fa849630b6597e9f1555309a416a616715586c474ee3679ccfe1173620e40c7f` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/medium/JOX.tga` | `gfx/flags/medium/event31_dormant_carrier_07.tga` | `41x26` | `4282` | `7e0dbbc0ad8c040d3c1071632c265b8f95b073ab4bb20159f9f48627aa0812d4` | `540baa855954384607105b2ad04dcc103824c45aa77bb1e438dc7bd39be7113a` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/small/JOX.tga` | `gfx/flags/small/event31_dormant_carrier_07.tga` | `10x7` | `298` | `74e71baa90c050df15258fa09bab11ff51acc56d34d340beac1d14385035f0ff` | `47aa8d5a812923c7fe86e1c318cc126445aebfaa16a0333b95ad40933ffa8fcc` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/JPX.tga` | `gfx/flags/event31_dormant_carrier_08.tga` | `82x52` | `17074` | `d6cef5096d9d1aefc0672802d3060ab22577f3d235c0b1062cc35f8d0a4213d3` | `f7fee614a3fb6ec1dd6357b69f4059bbd6bd148af810acf450c1a69634a4ac5a` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/medium/JPX.tga` | `gfx/flags/medium/event31_dormant_carrier_08.tga` | `41x26` | `4282` | `21e0368905b49d72286db0abb737aacbd66e52a8f2af695e0f1fc14d7a563d03` | `ad2766e8f449e7018c8f7bc481a624eae3ff185e5c959bf01eed9868e29892eb` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |
| `gfx/flags/small/JPX.tga` | `gfx/flags/small/event31_dormant_carrier_08.tga` | `10x7` | `298` | `0de5ea00fd2155e3d7004e94e39817545fb6ba26e4c2f9cb07d5569a1ec0b731` | `bf8203af970c22bd4186697c8ce0f203434185337122217bb838922dc385ba1c` | `type2,bpp32,desc8,bottom-left,alpha255,rgb_exact` |

The decoded RGB payload of every final TGA equals its matching backup TGA exactly at the declared dimensions.

The decoded alpha channel of every final TGA has minimum and maximum `255`.

The repaired normal, medium, and small files are `17074`, `4282`, and `298` bytes respectively, matching `18 + width * height * 4` for uncompressed 32-bit TGA.

The canonical `flags/contact_sheet.png` family was inspected for the flat flag ladder and orientation convention, and the installed vanilla `BEL_beligca_fascism.tga` ladder was checked as the matching flag precedent.

The existing Event 031 roundtrip evidence remains valid for artwork identity because the conversion preserves every decoded RGB pixel and changes only the TGA pixel depth and opaque alpha byte.

## Handoff

The parent can run the already planned native launch against the 24 repaired direct paths and review the flag consumer visually.

No `.gfx` handoff is required because HOI4 resolves these flag files through their tag-based filenames, and no sprite definition was changed.

The broader Event 031 flag package remains `needs_user_review` for its existing carrier identity and live-consumer gates.
