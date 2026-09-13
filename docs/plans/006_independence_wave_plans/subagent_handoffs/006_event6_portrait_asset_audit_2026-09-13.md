# Event 006 portrait asset audit

Date: 2026-09-13 (Europe/Kyiv).

Owner: `chaosx_portrait_creator`.

Disposition: **incomplete and blocked; no-change to runtime; no completion claim**.

Scope: every current Event 006 runtime portrait DDS under `gfx/leaders/006_independence_wave/`, every portrait-specific Event 006 `.gfx` texture path, the corresponding character and scripted-effect portrait consumers, and the durable source shelf under `docs/assets/portraits/006_independence_wave/`.

## Authority and review basis

The accepted asset matrix remains `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv:46` (`ASSET-045`, the 156x210 leader portrait family), with the portrait acceptance rules in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md:528-582`.

The preceding gate authorities are `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_portrait_gate_reaudit_2026-09-12.md`, `006_event6_portrait_visual_repair_audit_2026-09-06.md`, `006_event6_portrait_consumer_gate_2026-08-31.md`, and `006_portrait_wiring_reconciliation_2026-08-30.md`.

I read `AGENTS.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, `.agents/skills/chaos-redux-comfyui/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md` before this audit. I also read the offline Character Modding, Graphical Asset Modding, Interface Modding, and Scopes wiki pages plus the required core offline wiki pages and the installed vanilla character and scripting documentation. The installed vanilla leader and commander portrait reference sheets were used for the 156x210 family comparison; the separate 65x67 advisor family was not treated as a substitute.

The durable source shelf is physically 60 parent files, consisting of 59 preserved original source files plus `README.md`, with one `processed` child containing 72 files and no nested child. The shelf README keeps ComfyUI inputs at the flat parent, keeps crops and provenance under `processed`, and explicitly says that a source file alone does not authorize a character, consumer, package admission, or HOI4-styled replacement. No source byte, crop, provenance record, or runtime file was changed.

## Current wiring inventory

The fresh repository search covered `common/characters`, `history/countries`, `interface`, `localisation`, `events`, and the Event 006 scripted-effect portrait consumers. It found 70 runtime DDS files and 64 unique Event 006 portrait sprite/texture pairs.

The 64 sprite definitions are split across `interface/006_independence_wave_portraits_registry.gfx` (53), `interface/006_independence_wave_small_assets.gfx` (9), and `interface/006_independence_wave.gfx` (2). Every registered texture path exists, every registered texture basename is unique, and every registered sprite is referenced somewhere in the Event 006 character or scripted-effect surfaces. No Event 006 portrait path was found in `history/countries`, `localisation`, or `events`.

`common/characters/006_independence_wave_characters_registry.txt` contains 72 `large` portrait references covering 46 unique local Event 006 portrait keys. The other 18 local keys are consumed by the existing Event 006 scripted effects for BRI, BSK, GLC, MNT, RHI, RUT, SCO, WLS, YAK, and BAY. The two intentional vanilla cleanup aliases remain `GFX_portrait_RHI_josef_friedrich_matthes` and `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria`; neither was renamed or repointed.

The six runtime DDS files below are not registered by any current `.gfx` file. They remain evidence-only and were not wired, renamed, copied, or deleted.

| Unregistered runtime DDS | Result |
| --- | --- |
| `portrait_ACX_cornish_coastal_commander.dds` | Legacy generated grounded-polity evidence with no current ACX character or consumer. |
| `portrait_ACX_cornish_port_and_mines_committee.dds` | Source-placeholder candidate whose Arthur Quiller-Couch source does not prove the named committee or 1936 office. |
| `portrait_AEX_flemish_civil_industrial_board.dds` | Superseded generated grounded-polity evidence with no current AEX consumer. |
| `portrait_AEX_flemish_industrial_security_commander.dds` | Superseded generated grounded-polity evidence with no current AEX consumer. |
| `portrait_ARX_independence_wave_gavino_piras.dds` | Legacy unregistered ARX evidence; the current `ARX_gavino_piras` consumer uses the distinct Vittorio Vernè sprite. |
| `portrait_ARX_independence_wave_vittorio_pala.dds` | Legacy unregistered ARX evidence with no current character or sprite consumer. |

The four currently wired pairs from the superseded generated grounded-polity package are the AFX, AGX, AJX, BAY, BRI, RHI, SCO, and WLS role pairs, for 16 wired textures total. They remain technically readable legacy assets but are not promoted as semantically admitted grounded portraits. No sourced real person was substituted for any of them.

## DDS technical and visual audit

All 70 current DDS files were read directly from the working tree, parsed from their binary headers, and decoded to temporary RGBA PNGs for visual review. Every file is a one-level uncompressed BGRA DDS with `DDS ` magic, 124-byte header, `dwFlags = 4111`, dimensions `156x210`, pitch `624`, zero mipmaps, pixel format size `32`, pixel flags `65`, fourCC `0`, 32-bit pixels, masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE = 4096`, zero extra caps, 131040 payload bytes, and exact file size 131168 bytes. Every decoded alpha channel is opaque with range `255..255`.

The current SHA-256 values have zero mismatches against the previous runtime inventory at `C:/Users/klimp/AppData/Local/Temp/chaosx_event6_portrait_audit/runtime_inventory.json`. Pixel-payload comparison found no duplicate decoded payload among the 70 files. All 70 native-size contact-sheet cells and all 70 nearest-neighbour 4x cells were reviewed.

The native and nearest-neighbour reviews found no clipped head, missing headroom, accidental frame or border, under-frame failure, alpha seam, transparent fringe, aspect-ratio defect, or path-induced wrong texture among the 70 files. The grainy KOS Shaban source remains source-authentic and was not repainted. Collective/institutional large portraits remain in the large consumer family and do not imply advisor, dossier, or small-card derivatives.

The visual review sheets were temporary evidence outside the repository:

- `C:/Users/klimp/AppData/Local/Temp/chaosx_event6_portrait_audit/native_contact_1.png` through `native_contact_4.png`.
- `C:/Users/klimp/AppData/Local/Temp/chaosx_event6_portrait_audit/nearest4x_contact_1.png` through `nearest4x_contact_4.png`.
- `C:/Users/klimp/AppData/Local/Temp/chaosx_event6_portrait_audit/archive_source_contact_1.png` through `archive_source_contact_3.png`, covering the 59 direct-parent source originals.
- `C:/Users/klimp/AppData/Local/Temp/chaosx_event6_portrait_audit/processed_contact_1.png` and `processed_contact_2.png`, covering the 21 processed PNG outputs; the remaining processed files are the associated metadata, HTML, text, review, and provenance evidence.

The source contacts retain recognizable source identity, period clothing, and source-visible framing. The processed contacts show the existing crop outputs and review variants without a concrete crop defect that can be repaired safely under the grounded-source rules.

### Runtime DDS inventory and hashes

Every row in this table was inspected at native size and in the nearest-neighbour 4x review. `wired` means a current Event 006 `.gfx` texture path exists; `orphan` means that no current Event 006 `.gfx` path exists.

| Runtime DDS | Decoded size | Bytes | SHA-256 | State |
| --- | ---: | ---: | --- | --- |
| `portrait_ACX_cornish_coastal_commander.dds` | 156x210 | 131168 | `b6b84c64e16c6112ff117300b6271a3e50e239acc663cf5fc7c7641673ed50e6` | orphan |
| `portrait_ACX_cornish_port_and_mines_committee.dds` | 156x210 | 131168 | `2b3b98f4621bc43f0f517a28f984337755bf193746d0dadcedffeb4f2cd9a0b8` | orphan |
| `portrait_AEX_flemish_civil_industrial_board.dds` | 156x210 | 131168 | `918efe9de7804567ec9dd130ad855d81ed32171cf7a0e4e4a6cf27cf19283153` | orphan |
| `portrait_AEX_flemish_industrial_security_commander.dds` | 156x210 | 131168 | `8fe59ea0b1b7c7d5b2f556a016aabf0c52a00f8260d3af8840e93c7ac90564ee` | orphan |
| `portrait_AFX_walloon_provisional_assembly.dds` | 156x210 | 131168 | `7d8612ca9b6b82a1a4ae39156f9465891684345219bc3c7c8d84ab5a673dc75a` | wired |
| `portrait_AFX_walloon_reserve_commander.dds` | 156x210 | 131168 | `0ad247810f8e98afade0362cfac275a68db401dc4bebf18b8343b8f77067dfff` | wired |
| `portrait_AGX_friesland_coastal_commander.dds` | 156x210 | 131168 | `e84d790ab245f5e14baadb71d0c66438dcb04586131f4b98893b0a4cbc8e8137` | wired |
| `portrait_AGX_friesland_coastal_council.dds` | 156x210 | 131168 | `85240ff6700bbebaed9eeba838f9b503d9d42a7e55cef6df2d8c71dc86c33d1e` | wired |
| `portrait_AJX_saar_industrial_security_commissioner.dds` | 156x210 | 131168 | `6595d33fc6a08b840eb51debe3e05bde56bdad38009cb22eef0019720a1eabfd` | wired |
| `portrait_AJX_saar_municipal_neutral_commission.dds` | 156x210 | 131168 | `07eff6959101bed7629f722276dbd46ec6d91d3e5e58f5d3462057c131bed426` | wired |
| `portrait_ARX_independence_wave_emilio_lussu.dds` | 156x210 | 131168 | `0cc98f4364ac4ec5f6b15fc4e599c76b73d50a8747ba022079da19c63f65120e` | wired |
| `portrait_ARX_independence_wave_gavino_piras.dds` | 156x210 | 131168 | `f8eab9bfe2551ba68166bbf698e486f1dac1452f1509801a59db5ca8ad20a4b7` | orphan |
| `portrait_ARX_independence_wave_vittorio_pala.dds` | 156x210 | 131168 | `443e92aca9f57fce6988296692949f70a859508ff85f85b30a61897243214fae` | orphan |
| `portrait_ARX_luigi_mella_santelia.dds` | 156x210 | 131168 | `746c60bedb76abdbdb948fa741cbd071581406ec7ff8d7fb9d6f92b19b4c18d8` | wired |
| `portrait_ARX_vittorio_verne.dds` | 156x210 | 131168 | `529e40539e9c3623428a809eaa427a607042d28dc2516fbefc3ab1e7c8b463e5` | wired |
| `portrait_ASX_independence_wave_luigi_rizzo.dds` | 156x210 | 131168 | `9a260040a88adcb7250583d7c00d20132076672781e3e3b6c614789a32f24367` | wired |
| `portrait_ASX_independence_wave_luigi_sturzo.dds` | 156x210 | 131168 | `58c1d9e42a25d48e2ebf471817e6d8545a3a9d296bf29e9ee430b5582a0f00e8` | wired |
| `portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` | 156x210 | 131168 | `b84a64e25f270d624726e0351538d0f8cd05de54b586fd92d39e003e0118ea13` | wired |
| `portrait_ASX_independence_wave_vincenzo_di_benedetto.dds` | 156x210 | 131168 | `1b9a19b65673924e50a903c0ea2b8b092167dbad4b67e482da3f2764ce11a02a` | wired |
| `portrait_ASY_independence_wave_civic_national_assembly.dds` | 156x210 | 131168 | `717e5c11a5ac85d90d34f8aca53cc9611fb8ef0716c85bad885b5afb95829821` | wired |
| `portrait_ASY_independence_wave_concordat_council.dds` | 156x210 | 131168 | `5c034700247de09480eedd294ca192045c18dd8b9582fe236dda776e7d67ad06` | wired |
| `portrait_ASY_independence_wave_levies_guardianship.dds` | 156x210 | 131168 | `4c75d0c118de632ecd0913525f7258758dbd1458edc1b96d1a7e66a5ede69eb1` | wired |
| `portrait_ASY_independence_wave_provisional_national_council.dds` | 156x210 | 131168 | `129fc2c576c57871ebaba5e715af35b4a1d50a4d655cd93e0eeb1e9e79cc1f43` | wired |
| `portrait_AXX_independence_wave_otto_roth.dds` | 156x210 | 131168 | `1b81c6cc882491d8d19352c13dff93864cd068df21dd43e2c24894995c60245c` | wired |
| `portrait_BAX_independence_wave_hristo_silyanov.dds` | 156x210 | 131168 | `c33d80a78f8b086a0449e6bc1946897fa46c60368faa4ca2d99aefb94d78c05f` | wired |
| `portrait_BAY_independence_wave_mountain_commandant.dds` | 156x210 | 131168 | `332d8578f4bdede1a9fead234b361aa8c9fd786d5261cb45dbea56475754dbab` | wired |
| `portrait_BAY_independence_wave_state_council.dds` | 156x210 | 131168 | `999857d191f7b088e11daa78fb29eadd0b514dc6da494a0102423c635e736e95` | wired |
| `portrait_BAY_rupprecht_of_bavaria.dds` | 156x210 | 131168 | `fb7bce1d8316f52d728e82e299eaf9675fa0dabe57f2f7c9aff154c1012478b7` | wired |
| `portrait_BBX_independence_wave_georgios_christakis_zografos.dds` | 156x210 | 131168 | `38d0db7147fcf41a31086840bf62d43ed8bfd2b51e0abe60448c11d0c0e01698` | wired |
| `portrait_BBX_independence_wave_spyros_spyromilios.dds` | 156x210 | 131168 | `753471904a7cc8226caeaea7debd3b9533eafbcd342c0222de8c93becb7af1ef` | wired |
| `portrait_BOS_independence_wave_mehmed_spaho.dds` | 156x210 | 131168 | `67b35a927ca64a43b97d58652f04ee9bdcca36b5239573c30d54d072ec1ad7b2` | wired |
| `portrait_BRI_independence_wave_civic_commission.dds` | 156x210 | 131168 | `583f821ed7f8b78a89321dbb7e1e7b7cad7e30829dfa5dd14b6f255e42e27dc0` | wired |
| `portrait_BRI_independence_wave_coastal_commandant.dds` | 156x210 | 131168 | `0806f9560139ea1dbc30ff4385b16e829560d85bcddd15a91a294b28d39802fb` | wired |
| `portrait_BSK_independence_wave_yakov_bykin.dds` | 156x210 | 131168 | `5dfe39dd9a7c72a1ac360ee3695b4779be67c10bad783458025433fdb0665e88` | wired |
| `portrait_CHU_independence_wave_bolgar_civic_presidium.dds` | 156x210 | 131168 | `e031470617e94b88168155bb64826db0bdc13b83a41b4e97245a2dc30be26f67` | wired |
| `portrait_CHU_independence_wave_federal_presidium.dds` | 156x210 | 131168 | `60d7a7bfb037a9f51143beb79132f5c180888dd082551794b3c1b45f60d87603` | wired |
| `portrait_CHU_independence_wave_middle_volga_congress.dds` | 156x210 | 131168 | `2c4e5e0b00ecec70d29901bf2938bd0695192b7af0336e56e9b12cebb0a2d8a3` | wired |
| `portrait_CHU_independence_wave_river_security_directorate.dds` | 156x210 | 131168 | `82e790af00f8f91fbd84ed2b0195c974433c8705deb3c207f4872284d5724dc3` | wired |
| `portrait_COR_independence_wave_adolphe_landry.dds` | 156x210 | 131168 | `46505f5533fafcff0ee1edfa2d01cad848862742a10650006fdf2e36886ec101` | wired |
| `portrait_COR_independence_wave_jean_chiappe.dds` | 156x210 | 131168 | `c91ef35a10d2f6a28594c0a30216f31317afea83bd75e820e9894ba79adf318b` | wired |
| `portrait_DOX_kwaku_ntim.dds` | 156x210 | 131168 | `172e194bfca197c96506b0ef44117c2801c91c06496cabfe1efb3b970e952856` | wired |
| `portrait_DOX_kwame_frimpong.dds` | 156x210 | 131168 | `fd5158e1ef81ae4ebfc7c5dedb4408d05062f464955274d9f74b0463e66b88ba` | wired |
| `portrait_DOX_prempeh_ii.dds` | 156x210 | 131168 | `a04827f02e775c26e20aee6de2d25a30839a3e0ddde0b9a46af82f562ead1b79` | wired |
| `portrait_FIJ_independence_wave_founding_congress_chair.dds` | 156x210 | 131168 | `31fea5eb5c7c4b6f34ec138ed6a3168a7c6c39755a992bd6abf0296c5838d2c6` | wired |
| `portrait_FSM_independence_wave_inter_island_congress_chair.dds` | 156x210 | 131168 | `64db23c13f8f3f488079ea24ca4d8ef9326bbb3fd9abbc94ee9b9251b004ae29` | wired |
| `portrait_GLC_alfonso_daniel_castelao.dds` | 156x210 | 131168 | `15f9ca69d7536439d2421dd8d55c96e94b5c56f9cdeb5ae5ee6a6210aaf25237` | wired |
| `portrait_HAW_independence_wave_territorial_delegate.dds` | 156x210 | 131168 | `ef68feef243e6758e15df13c35420a33b38f060b6016dc25e20c8a30c229e37b` | wired |
| `portrait_HBX_independence_wave_civic_convention.dds` | 156x210 | 131168 | `a158a968a1e67f2f83720d1b9201369542c3aaf7318a8c6332d659d91382cad1` | wired |
| `portrait_KOS_independence_wave_ferhat_draga.dds` | 156x210 | 131168 | `a31fc49eb4156e1bb4942e8982ad4c8623b6c331abd71ba4e36e4c8bb6ab5774` | wired |
| `portrait_KOS_independence_wave_miladin_popovic.dds` | 156x210 | 131168 | `a90edc0a60878d9947d127919a46bf841c681d745da434feb1f1a0c2f7bf5529` | wired |
| `portrait_KOS_independence_wave_shaban_polluzha.dds` | 156x210 | 131168 | `9a880d5933d07090205ff42d0176681851ef051698b809351e0341a1750bcf1c` | wired |
| `portrait_MAC_independence_wave_metodija_andonov_cento.dds` | 156x210 | 131168 | `1e5794441f15c301659db2e2b3b0f96746b7a6ef1125f552e5635efe0fa17c11` | wired |
| `portrait_MNT_blazo_jovanovic.dds` | 156x210 | 131168 | `fbbb5759f37663d6f35fae959a9a5da64a0cc0d227ab621780a334eee6d846df` | wired |
| `portrait_MNT_independence_wave_mitar_martinovic.dds` | 156x210 | 131168 | `61b3eecc0954becc41650bf02c07904d6a88d5dc9d652150acfdb70671adb006` | wired |
| `portrait_MNT_kristo_popovic.dds` | 156x210 | 131168 | `a50cd5478756349b1f4a4ce61ea837873fde1aa812e2c7268a7c4f628a123eb7` | wired |
| `portrait_NAV_jose_antonio_aguirre.dds` | 156x210 | 131168 | `19bed96acca3728eaf7cb79f861b097f1e12c3af4fabab8962af843f6e16ac7c` | wired |
| `portrait_RHI_independence_wave_provisional_directorate.dds` | 156x210 | 131168 | `080a1c3b3f6c7c3f01f7e380c8c6bfc064c238fcc44db084f2c559f1c3436bcb` | wired |
| `portrait_RHI_independence_wave_river_commandant.dds` | 156x210 | 131168 | `f8f99f0d3ef38601da687b9a2cea63edbde629017076e26e46b26b4b762e0df2` | wired |
| `portrait_RHI_josef_friedrich_matthes.dds` | 156x210 | 131168 | `fb43deb0b8708e7f5d1000b1f67ab63aca43d54efcb75618fb9097112a7699aa` | wired |
| `portrait_RUT_augustin_voloshyn.dds` | 156x210 | 131168 | `4e05d6813329d879cb90a974d002df5360430dacd17685ec90a6e77c615ddfae` | wired |
| `portrait_RUT_independence_wave_andriy_brodiy.dds` | 156x210 | 131168 | `c74be40fc813cab1b4f63d8b9bbe70a73c0a892a570f910f2a8b93755c6c38b1` | wired |
| `portrait_RUT_independence_wave_dmytro_klympush.dds` | 156x210 | 131168 | `e1b935fc0410e24668d23108519b63dcd0828e071827f0973a944b5a1c00336c` | wired |
| `portrait_RUT_independence_wave_ivan_mondok.dds` | 156x210 | 131168 | `bd05b469dac25edf2565ed96d174d61f0c8e0e743698cefab3555227134e4124` | wired |
| `portrait_SCO_independence_wave_civic_convention.dds` | 156x210 | 131168 | `61c08e14a90ffe6522781b7ad74cf0af36b7c11426a6faef85a3b1887346da53` | wired |
| `portrait_SCO_independence_wave_territorial_commandant.dds` | 156x210 | 131168 | `71531a64cdeaf535ec6f93e4fc00b30afbdd46929b3b104c7a47e83a65fe3f1a` | wired |
| `portrait_SOK_bello_rabah.dds` | 156x210 | 131168 | `c6a26906005d0f2a840156490609bab2c8500aacf5d9175135c6a7a464e17864` | wired |
| `portrait_SOK_muhammad_dikko.dds` | 156x210 | 131168 | `84feaacc0f2e83c3f7380bb39d5a0849f30825de0e36a5c30ede82d346c676f4` | wired |
| `portrait_WLS_independence_wave_mountain_commandant.dds` | 156x210 | 131168 | `2a478e85cb4d025baf0bf47e5c2df5a9b75387744cd0ede894c517c2984baee2` | wired |
| `portrait_WLS_independence_wave_national_council.dds` | 156x210 | 131168 | `e11254da91774c9f0495c60943835a8ba26263934b8bc4e2d6e3016c01e4334d` | wired |
| `portrait_YAK_independence_wave_pavel_pevznyak.dds` | 156x210 | 131168 | `7fcb0b641c7a390cc3f0c38a4028242e6248f24246d3d468ec2b80b99d910e6f` | wired |

## Source, crop, processed evidence, and replacement state

The flat source shelf and its processed child were opened through the source and processed contact sheets above. Existing records include attributed source URLs, source hashes, crop boxes and hashes, rights notes, and review PNGs for the admitted source-placeholder packages. Examples retained under `processed` include the YAK Anatoly/Pavel package, FER Krasnoshchyokov/Nikiforov, BSK Bykin, NAV Aguirre, KOS source crops, CHU source crops, and the IW-095 institutional records. The historical per-package manifests and the consolidated consumer reconciliation remain the provenance authorities; this audit did not duplicate or move their bytes.

The current Event 006 source/runtime authority still records NAV Aguirre and GLC Castelao as the only current user-supplied `styled_final` rows. Other admitted real-person rows remain `source_placeholder`. No explicit grounded styled-final request was admitted in this audit, so `replacement_pending=false` remains correct. The user alone may later supply a RunPod-produced HOI4-style final; no RunPod page, workflow, provider job, queue, or result was opened or operated.

The 13 supplied rows below remain `source_placeholder_candidate_hold` and are not promoted, wired, relabelled, or substituted:

- YAK Anatoly Pepelyayev: no admitted Event 006 office/consumer; do not relabel YAK Pavel Pevznyak or vanilla Anatoly.
- BYA Ardan Markizov: role selection, rights jurisdiction, and exact BYA consumer remain unresolved.
- BYA Mikhei Erbanov: group-image framing, role, and rights remain unresolved.
- ALT Grigory Gurkin: strict 1936 office and rights remain unresolved; no Event 006 consumer exists.
- ALT Samuil Yufit: strict opening-date role and rights remain unresolved; no Event 006 consumer exists.
- FER Alexander Krasnoshchyokov: active-1936 FER role/date and rights remain unresolved; no FER consumer exists.
- FER Pyotr Nikiforov: active-1936 FER role/date and rights remain unresolved; no FER consumer exists.
- KUR Seyid Riza: attributed rights/publication chain remains unresolved; preserve vanilla KUR wiring.
- ACX Cornish Port and Mines Committee: the attributed source visibly identifies Arthur Quiller-Couch rather than a verified 1936 committee officeholder.
- ARX Gioacchino Solinas: no exact Event 006 office/consumer and incomplete rights chain; do not relabel the distinct ARX runtime people.
- FIJ Ratu Sir Lala Sukuna: circa-1940s source-date and precise rights chain remain unresolved; do not relabel the FIJ institutional chair.
- FIJ Vishnu Deo: exact 1936 founding-chair role and complete source-rights chain remain unresolved; no exact consumer exists.
- GLC Alexandre Bóveda: route window, rights, and exact consumer remain unresolved; do not relabel GLC Castelao.

The detailed attributed URLs, source dimensions, source hashes, supplied candidate hashes, and role/date/rights analysis for these rows remain in `006_event6_portrait_gate_reaudit_2026-09-12.md`. That handoff remains authoritative and was not contradicted by this technical audit.

## PNG and DDS outputs

No new PNG output was created. The existing processed PNG evidence was opened from the temporary contacts and no crop/framing defect was found that could be repaired without changing a real person's identity or promoting a blocked role. No new DDS output was created or installed. The 70 runtime DDS files listed above are the current bytes; all are technically valid, and the six unregistered files remain preserved orphan evidence.

`.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` was not run because there was no authorized source-placeholder crop or conversion defect to repair. Re-running conversion would produce no justified runtime change and would not clear any identity, role/date, rights, or consumer gate.

## Changed files and validation

Only this handoff was added:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_portrait_asset_audit_2026-09-13.md`

No `gfx/leaders/006_independence_wave/*.dds`, portrait-specific `.gfx`, character file, history file, localisation file, event file, source archive file, crop, processed PNG, manifest, or prior handoff was edited. No file was staged or committed.

The read-only validation result is 70 valid DDS headers, 70 decoded `156x210` RGBA images, 70 opaque alpha channels, zero duplicate payloads, zero current-versus-prior-inventory hash mismatches, 64 existing GFX texture pairs, zero missing GFX texture paths, 72 character large references, 46 unique character-registry GFX keys, and six documented runtime orphans. Native and nearest-neighbour 4x visual review found no technical crop, headroom, alpha/fringe, aspect, or stale-path defect.

Skipped checks are the live game, HOI4 MCP rendering, and RunPod validation; these are outside this portrait audit and belong to the user/parent workflow. Native ImageGen was not invoked because every candidate in scope is a grounded real person or an existing legacy institutional/grounded asset, and no fictional or impossible subject was requested.

## Blockers and handoff

The 13 supplied rows remain blocked by missing or unresolved identity-safe Event 006 consumer, role/date, rights, or framing evidence. The six orphan DDS files have no safe consumer and must not be wired by inference. The 16 wired generated grounded-polity textures remain semantically superseded and require sourced real-person replacements or an explicit package decision; this audit does not invent or repaint them. No concrete crop, conversion, placement, alpha, aspect, or path defect justified a repair.

The parent may use this handoff as the current portrait technical receipt. Runtime remains untouched and fail-closed pending authoritative consumer admission and rights/role decisions.
