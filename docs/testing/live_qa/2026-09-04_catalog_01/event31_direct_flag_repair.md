# Event 31 direct flag repair

Date: `2026-09-05`

Status: `needs_user_review` for parent-owned native launch and final visual consumer acceptance.

## Scope and acceptance

The parent approved an additive startup repair for the eight dormant Event 031 carrier tags. The direct no-suffix base mapping is `JHX` → `event31_dormant_carrier_01`, `JIX` → `event31_dormant_carrier_02`, `JKX` → `event31_dormant_carrier_03`, `JLX` → `event31_dormant_carrier_04`, `JMX` → `event31_dormant_carrier_05`, `JNX` → `event31_dormant_carrier_06`, `JOX` → `event31_dormant_carrier_07`, and `JPX` → `event31_dormant_carrier_08`.

The repair reuses the existing approved Event 031 runtime TGA ladders byte-for-byte as `gfx/flags/{TAG}.tga`, `gfx/flags/medium/{TAG}.tga`, and `gfx/flags/small/{TAG}.tga`. These direct bases are shared across ideologies only until the runtime applies its existing cosmetic identity.

This repair created no artwork, generated/source PNG, DDS, `.gfx` entry, ideology-suffixed direct flag, active Event 006/012/016/023 asset, or gameplay change. The existing Event 031 package manifest remains `needs_user_review` for its broader 37-design identity and live-review status.

## Pre-write collision gate

The apply command enumerated all 24 requested direct destinations and verified `Test-Path -LiteralPath` was false for every destination before copying. The gate reported `PREWRITE_DESTINATION_COUNT=24` and `PREWRITE_DESTINATIONS_ABSENT=24`, then copied exactly `24` files with overwrite disabled.

## Mapping, hashes, and headers

Each direct destination SHA-256 equals its approved `event31_dormant_carrier_*` source TGA SHA-256. All files are TGA image type `2`, `24`-bit, descriptor `0` with bottom-left origin, and the expected native byte length for their size.

| Direct tag | Source ladder | Normal direct TGA / SHA-256 | Medium direct TGA / SHA-256 | Small direct TGA / SHA-256 |
| --- | --- | --- | --- | --- |
| `JHX` | `event31_dormant_carrier_01` | `gfx/flags/JHX.tga` / `3d0d07512bf49d9fbea040bfbdc608ca85ee676709765f870731ccda97fae67e` | `gfx/flags/medium/JHX.tga` / `61e90edfc459e91bf4505430d4dfb0965fe40761d43043142e8380c2525fccc9` | `gfx/flags/small/JHX.tga` / `54ade04c09906d54c3e40e2263b48a6e92bd12fb572f8b5fa34098e82020a7a9` |
| `JIX` | `event31_dormant_carrier_02` | `gfx/flags/JIX.tga` / `83532b0e65796f84bba564321b585948d231f5c62ac743c27f588206e2839cd3` | `gfx/flags/medium/JIX.tga` / `030de0309000d23b141cdea250389a92c7f7444b4dbd5a5f95b2137d0e8b2c0d` | `gfx/flags/small/JIX.tga` / `b0acafd1fa12b2de34ee4eae2eabe7e7d7cfad6bcc88f2a4e46feaffde2f96bc` |
| `JKX` | `event31_dormant_carrier_03` | `gfx/flags/JKX.tga` / `38fea07ea13b4612414ac1e659a052c2dfaf556458759d47edbe8b3115212cce` | `gfx/flags/medium/JKX.tga` / `94349b77b21d1d2c9fa4c42d39722b6fb5d48d6ead7e3599c50bc432aca508c1` | `gfx/flags/small/JKX.tga` / `79848301060366b728997692246c1daea09ccf85b46acf83a199680d31c98c70` |
| `JLX` | `event31_dormant_carrier_04` | `gfx/flags/JLX.tga` / `e64577d3c397b7be59ce6bd11e23ffbfb0df99c678f8aa9a920d6a6f5da73e93` | `gfx/flags/medium/JLX.tga` / `766db1e1f069b3213ccb2eafd0c2857cb7876fb3aeac2074c0aed9b9f6c5094b` | `gfx/flags/small/JLX.tga` / `8f6f162c516110e873359e4508913ddc3cfeba7d24ffa03d2ea36b1cbc4ce9e7` |
| `JMX` | `event31_dormant_carrier_05` | `gfx/flags/JMX.tga` / `861a5d4ab10ab38346f92c593829be2007ab1751853dc8d5f8c2aa3be22b6fc0` | `gfx/flags/medium/JMX.tga` / `3af09b9349b771a27424e14a0d17a7dc00091d0bc769b24dd121cbe9e2dc7832` | `gfx/flags/small/JMX.tga` / `c89414ec06819d692359128954c9c2afd6ed66c75b55ed161918ce37717cfa62` |
| `JNX` | `event31_dormant_carrier_06` | `gfx/flags/JNX.tga` / `50eb52d609b30e1e77013739979928bf2d87a24c17a1999b8228ad42afada176` | `gfx/flags/medium/JNX.tga` / `03aa520308c8fcdce1935bde1880a5201d1de0bbab4bedfa823b7d664dbb0681` | `gfx/flags/small/JNX.tga` / `beb374d3e7a15773fb1cf32c0bf0fdc7bc2a8b06aa1ab5704ec0b88f211da283` |
| `JOX` | `event31_dormant_carrier_07` | `gfx/flags/JOX.tga` / `b6380fa6b7cc9828f10a44d013fc47cda05df6388553aad0f042d84fa6638df8` | `gfx/flags/medium/JOX.tga` / `7e0dbbc0ad8c040d3c1071632c265b8f95b073ab4bb20159f9f48627aa0812d4` | `gfx/flags/small/JOX.tga` / `74e71baa90c050df15258fa09bab11ff51acc56d34d340beac1d14385035f0ff` |
| `JPX` | `event31_dormant_carrier_08` | `gfx/flags/JPX.tga` / `d6cef5096d9d1aefc0672802d3060ab22577f3d235c0b1062cc35f8d0a4213d3` | `gfx/flags/medium/JPX.tga` / `21e0368905b49d72286db0abb737aacbd66e52a8f2af695e0f1fc14d7a563d03` | `gfx/flags/small/JPX.tga` / `0de5ea00fd2155e3d7004e94e39817545fb6ba26e4c2f9cb07d5569a1ec0b731` |

The normal files are `82x52` and `12810` bytes, the medium files are `41x26` and `3216` bytes, and the small files are `10x7` and `228` bytes. No destination collision was present before the write, and no destination hash differs from its source hash after the write.

## Vanilla and offline reference evidence

The offline `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md:322-342` page states that country flags are TGA files automatically assigned from their filenames, that a non-specific `TAG.tga` is the fallback when an ideology-specific flag is absent, and that the standard ladder is `82x52`, `41x26`, and `10x7`.

The canonical flag reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/`, including its `README.md`, `CATALOG.md`, and `contact_sheet.png`. The installed vanilla `BEL_beligca_fascism.tga` ladder has image type `2`, `24`-bit depth, descriptor `0`, and dimensions `82x52` / `41x26` / `10x7`, matching the existing Event 031 TGA encoding and origin convention used by this repair.

## Runtime roundtrip evidence

The 24 existing Event 031 runtime roundtrip PNGs under `docs/assets/031_random_terror/flags/roundtrip/{normal,medium,small}/` were decoded and compared pixel-for-pixel with the processed PNGs and source TGA bytes for all eight dormant carriers before the copy. After the copy, all 24 new direct files were decoded and compared pixel-for-pixel with the corresponding existing runtime roundtrip PNGs.

The check reported `POSTWRITE_DIRECT_FILES=24` and `POSTWRITE_ALL_HASHES_AND_HEADERS_MATCH`. The existing contact sheet already shows all eight dormant carrier designs at normal, medium, and small sizes, so no contact sheet refresh was needed for these byte-identical aliases.

## Remaining acceptance

The direct file repair is ready for the parent-owned native launch and final visual consumer review. No global Event 031 package acceptance is claimed, and the broader manifest status remains pending its existing identity and live-review gates.
