# Event 006 portrait-consumer closure audit

Date: 2026-08-26.

Scope: bounded read-only audit of the flat `docs/assets/portraits/006_independence_wave/` archive, the user-supplied `156x210/iw` PNG/DDS output set, the Event 006 portrait GFX registries, the consolidated Event 006 character registry, and the existing runtime portrait consumers.

No gameplay, character identity, trait, localisation, event, focus, decision, country setup, package-admission, flag, or unrelated UI surface was changed.

## Result

No additional portrait-specific runtime wiring was safe or necessary.

The user output folder contains 55 PNG/DDS pairs. Thirty-eight selected pairs are exact byte matches for existing Event 006 runtime portrait consumers and remain installed at their existing stable basenames. The remaining 17 pairs are either unresolved grounded identities, an alternate or rejected crop, an ambiguous filename, or a candidate with no exact Event 006 consumer. No new character or generic portrait consumer was invented, and no existing real-person identity was relabelled.

The 38 existing consumers remain governed by their prior source-placeholder/package handoffs. The external files contain a user-supplied HOI4-style workflow and painted output evidence, but this audit does not silently convert every prior `source_placeholder` manifest state into an accepted styled-final state. The only currently recorded accepted `styled_final` runtime states are NAV José Antonio Aguirre and GLC Alfonso Daniel Castelao in `006_iw013_iw015_user_supplied_portrait_final_audit_2026-08-26.md`.

## Evidence inspected

- `docs/assets/portraits/006_independence_wave/` is flat and contains the original-source shelf plus the sole `processed/` child directory requested by the parent task.
- The archive contains 58 root files and 24 Git LFS pointer stubs. Pointer stubs were not hydrated or rewritten; the existing dated source, provenance, crop, rights, and package handoffs remain the source authority.
- `interface/006_independence_wave_portraits_registry.gfx` contains 53 unique portrait sprite definitions.
- `interface/006_independence_wave_small_assets.gfx` contains 9 additional Event 006 portrait sprite definitions for the small/institutional registry.
- `interface/006_independence_wave.gfx` contains 2 additional Event 006 portrait sprite definitions for the RHI/BAY package effects.
- The three GFX files therefore expose 64 unique Event 006 portrait sprite/texture pairs, with no duplicate names, duplicate texture pairs, or missing registered DDS textures.
- `common/characters/006_independence_wave_characters_registry.txt` contains 47 unique Event 006 portrait GFX references, all resolved to definitions. The remaining effect-owned consumers are referenced by their package scripted effects, including BRI, BSK, MNT, RHI, BAY, SCO, WLS, YAK, and the RHI/BAY vanilla-character paths.
- `gfx/leaders/006_independence_wave/` currently contains 70 runtime DDS files; all 70 passed the same strict legacy portrait-contract validator, and 38 of them are exact byte matches for supplied output DDS files listed below.
- The installed-vanilla leader and commander references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/` were used as the full-portrait `156x210` framing baseline. Advisor-card references were not used as a substitute.

Relevant prior authority records are `006_portrait_wiring_supplied_runtime_2026-08-22.md`, `006_event6_portrait_gap_reaudit_2026-08-25.md`, `006_iw013_iw015_user_supplied_portrait_final_audit_2026-08-26.md`, and the per-package source handoffs referenced by those records.

## User output validation

All 110 PNGs are `156x210` RGB images. All 110 DDS files are `131168` bytes and pass the legacy uncompressed HOI4 portrait contract: `DDS ` magic, 124-byte header, width `156`, height `210`, pitch `624`, no mipmaps, 32-bit BGRA masks, `DDSCAPS_TEXTURE`, and opaque alpha range `255..255`.

The decoded BGRA pixels equal the matching PNG RGBA pixels for all 110 pairs. No malformed header, missing pair, alpha anomaly, or pixel mismatch was found.

Every PNG contains `prompt` and `workflow` metadata. The workflow is `hoi4_portrait_batch` revision `0` with `master_size=1024x1365`, `game_size=156x210`, `hoi4_portrait_flux2_klein_9b_lora_000002500.safetensors`, `adonis_base.safetensors`, `adonis_post.safetensors`, `argb8888`, and the prompt `make this portrait hoi4_portrait style`. The 55 `_00001` files use seed `569906346767745` and the 55 `_00002` files use seed `893029968453789`. No provider or job receipt was present in the supplied metadata.

Native-size and enlarged visual review covered every named `_00002` candidate plus the selected `_00001` alternatives for MNT Kristo Popović, DOX Prempeh II, and BSK Yakov Bykin. The 38 selected runtime candidates read as coherent painted head-and-shoulders portraits. The NAV source-crop alternate is full-body and does not meet the installed full-portrait framing; both Shaban `_00001`/`_00002` outputs fail as replacements because one is malformed and the other is effectively background-only; the rejected Kosovo group crop is malformed and remains rejected.

## Exact existing consumer map

The rows below are the 38 supplied DDS files whose bytes exactly match stable runtime DDS files already referenced by current Event 006 GFX and character/effect consumers. The runtime and supplied DDS hashes are identical.

| Supplied DDS | Runtime DDS | Existing consumer | SHA-256 |
| --- | --- | --- | --- |
| `portrait_ARX_independence_wave_emilio_lussu_source_00002.dds` | `portrait_ARX_independence_wave_emilio_lussu.dds` | `ARX_sardinian_provisional_assembly` / `GFX_portrait_ARX_independence_wave_emilio_lussu` | `0cc98f4364ac4ec5f6b15fc4e599c76b73d50a8747ba022079da19c63f65120e` |
| `portrait_ARX_vittorio_verne_source_00002.dds` | `portrait_ARX_vittorio_verne.dds` | compatibility key `ARX_gavino_piras` with visible identity Vittorio Vernè / `GFX_portrait_ARX_independence_wave_vittorio_verne` | `529e40539e9c3623428a809eaa427a607042d28dc2516fbefc3ab1e7c8b463e5` |
| `portrait_ASX_luigi_rizzo_source_00002.dds` | `portrait_ASX_independence_wave_luigi_rizzo.dds` | `ASX_luigi_rizzo` / `GFX_portrait_ASX_independence_wave_luigi_rizzo` | `9a260040a88adcb7250583d7c00d20132076672781e3e3b6c614789a32f24367` |
| `portrait_ASX_luigi_sturzo_source_00002.dds` | `portrait_ASX_independence_wave_luigi_sturzo.dds` | `ASX_sicilian_provisional_assembly` / `GFX_portrait_ASX_independence_wave_luigi_sturzo` | `58c1d9e42a25d48e2ebf471817e6d8545a3a9d296bf29e9ee430b5582a0f00e8` |
| `portrait_ASX_pietro_lanza_di_scalea_source_00002.dds` | `portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` | `ASX_sicilian_crown_council` / `GFX_portrait_ASX_independence_wave_pietro_lanza_di_scalea` | `b84a64e25f270d624726e0351538d0f8cd05de54b586fd92d39e003e0118ea13` |
| `portrait_ASY_independence_wave_civic_national_assembly_source_00002.dds` | `portrait_ASY_independence_wave_civic_national_assembly.dds` | `ASY_independence_wave_civic_national_assembly` / matching GFX | `717e5c11a5ac85d90d34f8aca53cc9611fb8ef0716c85bad885b5afb95829821` |
| `portrait_ASY_independence_wave_levies_guardianship_source_00002.dds` | `portrait_ASY_independence_wave_levies_guardianship.dds` | `ASY_independence_wave_levies_guardianship` / matching GFX | `4c75d0c118de632ecd0913525f7258758dbd1458edc1b96d1a7e66a5ede69eb1` |
| `iw024_banat_otto_roth_source_placeholder_2026_08_06__portrait_AXX_independence_wave_otto_roth_source_00002.dds` | `portrait_AXX_independence_wave_otto_roth.dds` | `AXX_independence_wave_banat_presidium` / matching GFX | `1b81c6cc882491d8d19352c13dff93864cd068df21dd43e2c24894995c60245c` |
| `iw027_thrace_hristo_silyanov_source_placeholder_2026_08_06__portrait_BAX_independence_wave_hristo_silyanov_original_00002.dds` | `portrait_BAX_independence_wave_hristo_silyanov.dds` | `BAX_independence_wave_thrace_council` / matching GFX | `c33d80a78f8b086a0449e6bc1946897fa46c60368faa4ca2d99aefb94d78c05f` |
| `portrait_BAY_rupprecht_of_bavaria_source_00002.dds` | `portrait_BAY_rupprecht_of_bavaria.dds` | vanilla `BAY_rupprecht_of_bavaria` via Event 006 package effect / `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria` | `fb7bce1d8316f52d728e82e299eaf9675fa0dabe57f2f7c9aff154c1012478b7` |
| `IW028_~1_00002.dds` | `portrait_BBX_independence_wave_georgios_christakis_zografos.dds` | `BBX_independence_wave_epirus_council` / matching GFX | `38d0db7147fc41a31086840bf62d43ed8bfd2b51e0abe60448c11d0c0e01698` |
| `iw028_epirus_spyros_spyromilios_source_placeholder_2026_08_09__portrait_BBX_independence_wave_spyros_spyromilios_00002.dds` | `portrait_BBX_independence_wave_spyros_spyromilios.dds` | `BBX_independence_wave_spyromilios` / matching GFX | `753471904a7cc8226caeaea7debd3b9533eafbcd342c0222de8c93becb7af1ef` |
| `iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06__portrait_BOS_independence_wave_mehmed_spaho_source_00002.dds` | `portrait_BOS_independence_wave_mehmed_spaho.dds` | `BOS_independence_wave_drina_council` / matching GFX | `67b35a927ca64a43b97d58652f04ee9bdcca36b5239573c30d54d072ec1ad7b2` |
| `iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_original_00001.dds` | `portrait_BSK_independence_wave_yakov_bykin.dds` | vanilla `BSK_yakov_bykin` via character-scoped Event 006 effect / matching GFX | `5dfe39dd9a7c72a1ac360ee3695b4779be67c10bad783458025433fdb0665e88` |
| `portrait_CHU_independence_wave_bolgar_civic_presidium_source_00002.dds` | `portrait_CHU_independence_wave_bolgar_civic_presidium.dds` | `CHU_independence_wave_bolgar_civic_presidium` / matching GFX | `e031470617e94b88168155bb64826db0bdc13b83a41b4e97245a2dc30be26f67` |
| `portrait_CHU_independence_wave_federal_presidium_source_00002.dds` | `portrait_CHU_independence_wave_federal_presidium.dds` | `CHU_independence_wave_federal_presidium` / matching GFX | `60d7a7bfb037a9f51143beb79132f5c180888dd082551794b3c1b45f60d87603` |
| `portrait_CHU_independence_wave_middle_volga_congress_source_00002.dds` | `portrait_CHU_independence_wave_middle_volga_congress.dds` | `CHU_independence_wave_middle_volga_congress` / matching GFX | `2c4e5e0b00ecec70d29901bf2938bd0695192b7af0336e56e9b12cebb0a2d8a3` |
| `portrait_CHU_independence_wave_river_security_directorate_source_00002.dds` | `portrait_CHU_independence_wave_river_security_directorate.dds` | `CHU_independence_wave_river_security_directorate` / matching GFX | `82e790af00f8f91fbd84ed2b0195c974433c8705deb3c207f4872284d5724dc3` |
| `portrait_COR_adolphe_landry_source_00002.dds` | `portrait_COR_independence_wave_adolphe_landry.dds` | `COR_corsican_municipal_congress` / matching GFX | `46505f5533fafcff0ee1edfa2d01cad848862742a10650006fdf2e36886ec101` |
| `portrait_COR_jean_chiappe_source_00002.dds` | `portrait_COR_independence_wave_jean_chiappe.dds` | `COR_jean_chiappe` / matching GFX | `c91ef35a10d2f6a28594c0a30216f31317afea83bd75e820e9894ba79adf318b` |
| `portrait_DOX_prempeh_ii_source_00001.dds` | `portrait_DOX_prempeh_ii.dds` | `DOX_prempeh_ii` / matching small-assets GFX | `a04827f02e775c26e20aee6de2d25a30839a3e0ddde0b9a46af82f562ead1b79` |
| `portrait_GLC_alfonso_daniel_castelao_source_00002.dds` | `portrait_GLC_alfonso_daniel_castelao.dds` | `GLC_independence_wave_alfonso_daniel_castelao` / matching GFX | `15f9ca69d7536439d2421dd8d55c96e94b5c56f9cdeb5ae5ee6a6210aaf25237` |
| `iw031_kosovo_source_placeholders_2026_08_09__portrait_KOS_independence_wave_ferhat_draga_source_00002.dds` | `portrait_KOS_independence_wave_ferhat_draga.dds` | `KOS_independence_wave_ferhat_draga` / matching GFX | `a31fc49eb4156e1bb4942e8982ad4c8623b6c331abd71ba4e36e4c8bb6ab5774` |
| `iw031_kosovo_source_placeholders_2026_08_09__source_crops__portrait_KOS_independence_wave_miladin_popovic_source_crop_00002.dds` | `portrait_KOS_independence_wave_miladin_popovic.dds` | `KOS_independence_wave_miladin_popovic` / matching GFX | `a90edc0a60878d9947d127919a46bf841c681d745da434feb1f1a0c2f7bf5529` |
| `portrait_MAC_independence_wave_metodija_andonov_cento_source_00002.dds` | `portrait_MAC_independence_wave_metodija_andonov_cento.dds` | `MAC_independence_wave_vardar_presidium` / matching GFX | `1e5794441f15c301659db2e2b3b0f96746b7a6ef1125f552e5635efe0fa17c11` |
| `iw030_montenegro_source_placeholders_2026_08_09__portrait_MNT_blazo_jovanovic_source_crop_00002.dds` | `portrait_MNT_blazo_jovanovic.dds` | vanilla `MNT_blazo_jovanovic` via Event 006 effect / matching GFX | `fbbb5759f37663d6f35fae959a9a5da64a0cc0d227ab621780a334eee6d846df` |
| `iw030_montenegro_source_placeholders_2026_08_09__portrait_MNT_independence_wave_mitar_martinovic_source_00002.dds` | `portrait_MNT_independence_wave_mitar_martinovic.dds` | `MNT_independence_wave_mitar_martinovic` / matching GFX | `61b3eecc0954becc41650bf02c07904d6a88d5dc9d652150acfdb70671adb006` |
| `iw030_montenegro_source_placeholders_2026_08_09__portrait_MNT_kristo_popovic_source_00001.dds` | `portrait_MNT_kristo_popovic.dds` | vanilla `MNT_kristo_popovic` via Event 006 effect / matching GFX | `a50cd5478756349b1f4a4ce61ea837873fde1aa812e2c7268a7c4f628a123eb7` |
| `iw013_nav_jose_antonio_aguirre_source_placeholder_2026_08_13__portrait_NAV_jose_antonio_aguirre_original_00002.dds` | `portrait_NAV_jose_antonio_aguirre.dds` | `NAV_independence_wave_jose_antonio_aguirre` / matching GFX | `19bed96acca3728eaf7cb79f861b097f1e12c3af4fabab8962af843f6e16ac7c` |
| `portrait_RHI_josef_friedrich_matthes_source_00002.dds` | `portrait_RHI_josef_friedrich_matthes.dds` | vanilla `RHI_josef_friedrich_matthes` via Event 006 package effect / `GFX_portrait_RHI_josef_friedrich_matthes` | `fb43deb0b8708e7f5d1000b1f67ab63aca43d54efcb75618fb9097112a7699aa` |
| `iw038_rut_augustin_voloshyn_source_placeholder_2026_08_10__portrait_RUT_augustin_voloshyn_source_00002.dds` | `portrait_RUT_augustin_voloshyn.dds` | vanilla `RUT_augustin_voloshyn` via Event 006 effect / matching GFX | `4e05d6813329d879cb90a974d002df5360430dacd17685ec90a6e77c615ddfae` |
| `iw038_rut_andriy_brodiy_source_placeholder_2026_08_10__portrait_RUT_independence_wave_andriy_brodiy_source_00002.dds` | `portrait_RUT_independence_wave_andriy_brodiy.dds` | `RUT_independence_wave_andriy_brodiy` / matching GFX | `c74be40fc813cab1b4f63d8b9bbe70a73c0a892a570f910f2a8b93755c6c38b1` |
| `iw038_rut_dmytro_klympush_source_placeholder_2026_08_10__portrait_RUT_independence_wave_dmytro_klympush_source_00002.dds` | `portrait_RUT_independence_wave_dmytro_klympush.dds` | `RUT_independence_wave_dmytro_klympush` / matching GFX | `e1b935fc0410e24668d23108519b63dcd0828e071827f0973a944b5a1c00336c` |
| `iw038_rut_ivan_mondok_source_placeholder_2026_08_10__portrait_RUT_independence_wave_ivan_mondok_source_00002.dds` | `portrait_RUT_independence_wave_ivan_mondok.dds` | `RUT_independence_wave_ivan_mondok` / matching GFX | `bd05b469dac25edf2565ed96d174d61f0c8e0e743698cefab3555227134e4124` |
| `portrait_SOK_muhammad_dikko_source_00002.dds` | `portrait_SOK_muhammad_dikko.dds` | `SOK_muhammad_dikko` / matching small-assets GFX | `84feaacc0f2e83c3f7380bb39d5a0849f30825de0e36a5c30ede82d346c676f4` |
| `portrait_WLS_george_cornwallis_west_source_00002.dds` | `portrait_WLS_independence_wave_mountain_commandant.dds` | `WLS_independence_wave_mountain_commandant` via package effect / matching GFX | `2a478e85cb4d025baf0bf47e5c2df5a9b75387744cd0ede894c517c2984baee2` |
| `portrait_WLS_j_h_thomas_source_00002.dds` | `portrait_WLS_independence_wave_national_council.dds` | `WLS_independence_wave_national_council` via package effect / matching GFX | `e11254da91774c9f0495c60943835a8ba26263934b8bc4e2d6e3016c01e4334d` |
| `iw051_sakha_yak_pavel_pevznyak_source_placeholder_2026_08_15__portrait_YAK_pavel_pevznyak_original_00002.dds` | `portrait_YAK_independence_wave_pavel_pevznyak.dds` | vanilla `YAK_pavel_pevznyak` via gated Event 006 effect / matching GFX | `7fcb0b641c7a390cc3f0c38a4028242e6248f24246d3d468ec2b80b99d910e6f` |

The 38 matching PNGs are the corresponding `156x210` RGB files with exact decoded pixel equality to the DDS rows above. Representative PNG SHA-256 values are `96067c011e30ba720d4d11ad49e2067b1b4e1ffa0c86dd393ef30e3419ab9a4d` for NAV Aguirre `_00002` and `5b99fdf9002e571a74d7e5d0b15ce3785f6e27cef878a69d55cde4706b418465` for GLC Castelao `_00002`.

## Unmapped, alternate, and duplicate dispositions

The following 17 user outputs were not copied, renamed, or wired.

| Supplied identity/output | Disposition |
| --- | --- |
| YAK Anatoly Pepelyayev | Grounded source and user-style candidate are valid files, but the exact vanilla owner is not an Event 006 consumer and the archived role/date evidence fails the 1936 Sakha office gate. Keep the candidate research-only and do not override vanilla globally. DDS SHA-256: `b01b99c37a3e636db8d860c59693daa735f4593548689ac498cfa70239de2c1b`. |
| BYA Ardan Markizov | No exact Event 006 BYA character or portrait sprite exists; parent identity/rights selection remains open. Keep unmapped. DDS SHA-256: `a75fc9449bb87cb1d5182cfbf5eb35a8033c016cae172bd9a828c9b0dac1a61f`. |
| BYA Mikhei Erbanov | No exact Event 006 BYA character or sprite exists, and the source is a group crop with a neighboring-subject sliver. Keep unmapped pending independent framing and rights review. DDS SHA-256: `72c693e538dcca71ff90a125ef83358107388f147e8b3df8b25221110063a16e`. |
| ALT Grigory Gurkin | Vanilla owner exists, but no Event 006 sprite/character is admitted and source-rights/1936-role gates remain open. Keep unmapped. DDS SHA-256: `0d0f4256d1b0bec248af91a34955c46053a6535f74e28f0e8ee441edeeba9ecd`. |
| ALT Samuil Yufit | Vanilla owner exists, but the archived source is post-opening and rights/role gates fail. Keep unmapped. DDS SHA-256: `d52e9210c5e799f0a8373eca6952ace9067010d8ee15196ac15d051c921f6952`. |
| FER Alexander Krasnoshchyokov | No admitted FER Event 006 character, sprite, or runtime consumer exists, and the active role is historical rather than an accepted 1936 office. Keep unmapped. DDS SHA-256: `d77715b47690703331f14551444ffe4ec3ff201078e3d43afc2705666923e84e`. |
| FER Pyotr Nikiforov | No admitted FER Event 006 character, sprite, or runtime consumer exists, and the active role is historical rather than an accepted 1936 office. Keep unmapped. DDS SHA-256: `7aa7778130b9de37d1e6cecb98e4b70c5c1073ccbff29873702989332e241d95`. |
| KUR Seyid Riza | Vanilla owner exists, but no Event 006 KUR character/sprite is admitted and the source rights chain remains fail-closed. Keep unmapped. DDS SHA-256: `5f5c00efac5524eb75f9aa172d63e0f0fd2c08ffcae2f777675d7fe8370ab1a1`. |
| ACX Cornish Port and Mines Committee | A stable source-placeholder DDS exists, but no live ACX character or portrait sprite consumer exists. Do not promote the readiness stub into a filler identity. DDS SHA-256: `48755c4c9afe3c20ac9f98c1e9283ad0c976bccf6ee4af0fd8549351525acefd`. |
| ARX Gioacchino Solinas | No exact Solinas character or sprite exists; relabelling Lussu, Mella, or the Verne compatibility consumer would substitute a different real person. Keep unmapped. DDS SHA-256: `8e48f76061e93bca7343e6cb44be2078707292c240edab2f7c0a44a6484781b9`. |
| FIJ Ratu Sir Lala Sukuna | No exact Sukuna character or sprite exists, and the archived circa-1940s source is outside the strict 1936 gate. Keep unmapped. DDS SHA-256: `00d565861009060937e8ed1a32d2b76c77a80bb59450af6af5c4d3038cf2f542`. |
| FIJ Vishnu Deo | No exact Vishnu Deo character or sprite exists; the period source does not establish the accepted 1936 founding-congress-chair role. Keep unmapped. DDS SHA-256: `c9c5a7cdfecad00fe72d51e7365aad7edc7e0eaf9aa52fa9e884370ba6080b06`. |
| GLC Alexandre Bóveda | Coherent user-style candidate, but no exact Event 006 character, sprite, or stable runtime basename exists. The existing Castelao consumer is a different real person and is not a substitute. DDS SHA-256: `4f2a1208be9d4fa772596c9eba9aaa284d8d12ca7926c77da5355bd33e6bd32b`. |
| NAV source-crop alternate | Same Aguirre identity but full-body framing does not meet the installed full-portrait crop; the original `_00002` is the existing exact runtime match. Treat as an alternate/duplicate, not a replacement. DDS SHA-256: `6dce73373b93b0f662ebf5462a2cf8251d519d62f8d76be46a9cd9edf2e6892f`. |
| KOS Shaban Polluzha `_00001`/`_00002` | An exact Shaban character and GFX consumer already exist, but `_00001` is malformed and `_00002` is background-only. Keep the existing attributed source-placeholder runtime DDS unchanged; do not replace it with either failed candidate. DDS SHA-256 values: `4dde54900ae098bee4988a6b347dc6d8bd8681077813bf71a599c26989074a70` and `b1c5b75b1e1e4f021b0fb8b0ea1e45f37a9cafe157864606d38efbe13309a7cf`. |
| Kosovo rejected group front-right crop | Explicitly rejected research image and a malformed candidate; no runtime consumer. Keep unmapped. DDS SHA-256: `187c42e90f80bbcbe9f22794a21c8523739ba5c249d17c806d9745a6c6622153`. |
| DON Vladimir Sidorin | Coherent user-style candidate, but no DON Sidorin character, GFX token, or stable Event 006 runtime consumer exists. Keep unmapped. DDS SHA-256: `2c56bd42a5d6e2702b506cd9a529bfcf518c3298cfd5fa22121dd172a1d0e7c5`. |

`IW028_~1_00002.dds` is not treated as a new identity. Its pixels match the existing Georgios runtime DDS, its face matches the archived Georgios source, and the other exact Epirus output is explicitly named Spyromilios. The stable Georgios consumer is retained without renaming the ambiguous external file.

The GLC Bóveda/Castelao pair is a deliberate different-person collision boundary, not a duplicate that can be merged. The ARX Solinas/Lussu/Mella/Vernè rows and FIJ Sukuna/Vishnu/founding-chair rows follow the same identity-safe rule.

## Source, provenance, rights, and replacement state

The archive source masters and crops remain attributed grounded evidence under the flat archive, with rights status inherited from the dated per-package handoffs. No new licence, public-domain, or redistribution claim is made for any supplied output. The 24 LFS pointer stubs are recorded as archive-state limitations, not silently hydrated.

The external PNG metadata proves a user-supplied ComfyUI painted workflow, but it does not include a provider/job receipt. NAV Aguirre and GLC Castelao retain the prior `styled_final` user-supplied disposition. The other 36 exact runtime matches remain `source_placeholder` at the controlling package/runtime state while their supplied files are retained as `styled_final_candidate` evidence only. The 13 grounded unresolved identities remain source-placeholder candidates or research-only holds as recorded by the prior gap re-audit. The NAV crop, malformed Shaban candidates, rejected group crop, and DON Sidorin output remain intentionally unmapped or alternate evidence.

No replacement state was inferred, no `replacement_pending` state was added, and no source archive file was relabelled or moved.

## Checks and skipped work

Performed checks were the strict DDS header/format/pixel validator for all 110 user pairs, decoded PNG/DDS pixel equality, SHA-256 inventory, runtime byte-match search, all 64 Event 006 portrait GFX path resolution checks, duplicate GFX name/texture checks, character-GFX reference resolution, exact consumer searches, native/enlarged visual framing review, archive layout inspection, and installed-vanilla leader/commander reference inspection.

`.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` was not run because all 110 supplied DDS files already satisfy the required legacy BGRA contract and no candidate cleared a new identity/consumer admission that would require conversion. Re-converting an already valid supplied DDS would create an unnecessary derivative.

RunPod was not opened, operated, configured, queued, or monitored. Native ImageGen was not invoked because every audited subject is grounded. No HOI4 process, live game, MCP runtime, save/load, or in-game rendering check was performed, so this handoff makes no live-game claim.

## Changed files

This dated handoff is the only file changed by this bounded audit:

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_portrait_consumer_closure_2026-08-26.md`.

No staging or commit was performed, per the parent task request. No simplification or fallback was used. The remaining blockers are the exact identity/role/rights/package gates recorded above, the missing accepted consumer for the unmapped identities, and the lack of a valid Shaban replacement candidate.
