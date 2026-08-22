# Event 006 supplied portrait source-placeholder wiring handoff

Date: 2026-08-22.

Scope: audit and portrait-specific wiring of the 51 exact user-supplied DDS files under `C:\Users\klimp\Documents\ComfyUI Workflows\HOI4\hoi4_portraits_output\output\156x210\iw\dds`. The source files are grounded real-person or grounded institutional source-placeholder inputs supplied by the user. They are not styled-final replacements, and no RunPod, native ImageGen, repaint, identity substitution, or generic fallback was used.

## Current result

Thirty-eight supplied files have safe existing Event 006 consumers and are already installed at their stable runtime basenames under `gfx/leaders/006_independence_wave/`. The existing runtime files were byte-identical to the selected supplied inputs at this audit, so no binary copy was repeated in this tranche.

The existing portrait-specific `.gfx` files and admitted character or package consumers already point at the runtime basenames recorded below. No character identity, traits, gameplay, localisation, event, focus, decision, country setup, or unrelated UI file was changed.

Thirteen supplied files remain explicitly unmapped because no safe existing Event 006 character plus portrait-specific `.gfx` consumer and runtime basename was found. They were not copied, renamed, relabelled onto another real person, or promoted through a global vanilla override.

## Source, provenance, rights, and replacement state

- Source root: `C:\Users\klimp\Documents\ComfyUI Workflows\HOI4\hoi4_portraits_output\output\156x210\iw\dds`.
- Archive root: `docs/assets/portraits/006_independence_wave/`, which remains flat for original source evidence with its existing `processed/` evidence folder; no source subfolder or duplicate DDS archive was created.
- Provenance: the supplied DDS filenames are retained verbatim in the mapping and unresolved tables, while the matching original-source, crop, provenance, and rights evidence remains in the existing Event 006 portrait archive and dated handoffs.
- Rights status: this wiring tranche records no new licence or redistribution clearance. User-supplied DDS files remain `source_placeholder`; any per-identity rights or date gate remains governed by the existing archive evidence and package handoff. An unresolved row is not cleared by the presence of a DDS file.
- Replacement state: all 38 installed rows remain `source_placeholder`; no explicit styled-final request was applied and no `replacement_pending` claim is made.

## Installed identity-to-runtime mapping

Every row below is a byte-for-byte source-to-runtime match with SHA-256 shown for both files. Every runtime target is 131,168 bytes, has a `DDS ` header, is 156x210, uses 32-bit BGRA uncompressed pixels, and declares no mipmaps.

| Supplied DDS | Runtime DDS | Existing character / portrait key | SHA-256 |
|---|---|---|---|
| `portrait_WLS_j_h_thomas_source_00002.dds` | `portrait_WLS_independence_wave_national_council.dds` | `WLS_independence_wave_national_council` / `GFX_portrait_WLS_independence_wave_national_council` | `e11254da91774c9f0495c60943835a8ba26263934b8bc4e2d6e3016c01e4334d` |
| `iw013_nav_jose_antonio_aguirre_source_placeholder_2026_08_13__portrait_NAV_jose_antonio_aguirre_original_00002.dds` | `portrait_NAV_jose_antonio_aguirre.dds` | `NAV_independence_wave_jose_antonio_aguirre` / `GFX_portrait_NAV_jose_antonio_aguirre` | `19bed96acca3728eaf7cb79f861b097f1e12c3af4fabab8962af843f6e16ac7c` |
| `iw024_banat_otto_roth_source_placeholder_2026_08_06__portrait_AXX_independence_wave_otto_roth_source_00002.dds` | `portrait_AXX_independence_wave_otto_roth.dds` | `AXX_independence_wave_banat_presidium` / `GFX_portrait_AXX_independence_wave_otto_roth` | `1b81c6cc882491d8d19352c13dff93864cd068df21dd43e2c24894995c60245c` |
| `iw027_thrace_hristo_silyanov_source_placeholder_2026_08_06__portrait_BAX_independence_wave_hristo_silyanov_original_00002.dds` | `portrait_BAX_independence_wave_hristo_silyanov.dds` | `BAX_independence_wave_thrace_council` / `GFX_portrait_BAX_independence_wave_hristo_silyanov` | `c33d80a78f8b086a0449e6bc1946897fa46c60368faa4ca2d99aefb94d78c05f` |
| `IW028_~1_00002.dds` | `portrait_BBX_independence_wave_georgios_christakis_zografos.dds` | `BBX_independence_wave_epirus_council` / `GFX_portrait_BBX_independence_wave_georgios_christakis_zografos` | `38d0db7147fcf41a31086840bf62d43ed8bfd2b51e0abe60448c11d0c0e01698` |
| `iw028_epirus_spyros_spyromilios_source_placeholder_2026_08_09__portrait_BBX_independence_wave_spyros_spyromilios_00002.dds` | `portrait_BBX_independence_wave_spyros_spyromilios.dds` | `BBX_independence_wave_spyros_spyromilios` / `GFX_portrait_BBX_independence_wave_spyros_spyromilios` | `753471904a7cc8226caeaea7debd3b9533eafbcd342c0222de8c93becb7af1ef` |
| `iw029_bosnia_mehmed_spaho_source_placeholder_2026_08_06__portrait_BOS_independence_wave_mehmed_spaho_source_00002.dds` | `portrait_BOS_independence_wave_mehmed_spaho.dds` | `BOS_independence_wave_drina_council` / `GFX_portrait_BOS_independence_wave_mehmed_spaho` | `67b35a927ca64a43b97d58652f04ee9bdcca36b5239573c30d54d072ec1ad7b2` |
| `iw030_montenegro_source_placeholders_2026_08_09__portrait_MNT_blazo_jovanovic_source_crop_00002.dds` | `portrait_MNT_blazo_jovanovic.dds` | vanilla `MNT_blazo_jovanovic` / `GFX_portrait_MNT_independence_wave_blazo_jovanovic` | `fbbb5759f37663d6f35fae959a9a5da64a0cc0d227ab621780a334eee6d846df` |
| `iw030_montenegro_source_placeholders_2026_08_09__portrait_MNT_independence_wave_mitar_martinovic_source_00002.dds` | `portrait_MNT_independence_wave_mitar_martinovic.dds` | `MNT_independence_wave_mitar_martinovic` / `GFX_portrait_MNT_independence_wave_mitar_martinovic` | `61b3eecc0954becc41650bf02c07904d6a88d5dc9d652150acfdb70671adb006` |
| `iw030_montenegro_source_placeholders_2026_08_09__portrait_MNT_kristo_popovic_source_00001.dds` | `portrait_MNT_kristo_popovic.dds` | vanilla `MNT_kristo_popovic` / `GFX_portrait_MNT_independence_wave_kristo_popovic` | `a50cd5478756349b1f4a4ce61ea837873fde1aa812e2c7268a7c4f628a123eb7` |
| `iw031_kosovo_source_placeholders_2026_08_09__portrait_KOS_independence_wave_ferhat_draga_source_00002.dds` | `portrait_KOS_independence_wave_ferhat_draga.dds` | `KOS_independence_wave_ferhat_draga` / `GFX_portrait_KOS_independence_wave_ferhat_draga` | `a31fc49eb4156e1bb4942e8982ad4c8623b6c331abd71ba4e36e4c8bb6ab5774` |
| `iw031_kosovo_source_placeholders_2026_08_09__source_crops__portrait_KOS_independence_wave_miladin_popovic_source_crop_00002.dds` | `portrait_KOS_independence_wave_miladin_popovic.dds` | `KOS_independence_wave_miladin_popovic` / `GFX_portrait_KOS_independence_wave_miladin_popovic` | `a90edc0a60878d9947d127919a46bf841c681d745da434feb1f1a0c2f7bf5529` |
| `iw038_rut_andriy_brodiy_source_placeholder_2026_08_10__portrait_RUT_independence_wave_andriy_brodiy_source_00002.dds` | `portrait_RUT_independence_wave_andriy_brodiy.dds` | `RUT_independence_wave_andriy_brodiy` / `GFX_portrait_RUT_independence_wave_andriy_brodiy` | `c74be40fc813cab1b4f63d8b9bbe70a73c0a892a570f910f2a8b93755c6c38b1` |
| `iw038_rut_augustin_voloshyn_source_placeholder_2026_08_10__portrait_RUT_augustin_voloshyn_source_00002.dds` | `portrait_RUT_augustin_voloshyn.dds` | vanilla `RUT_augustin_voloshyn` / `GFX_portrait_RUT_independence_wave_augustin_voloshyn` | `4e05d6813329d879cb90a974d002df5360430dacd17685ec90a6e77c615ddfae` |
| `iw038_rut_dmytro_klympush_source_placeholder_2026_08_10__portrait_RUT_independence_wave_dmytro_klympush_source_00002.dds` | `portrait_RUT_independence_wave_dmytro_klympush.dds` | `RUT_independence_wave_dmytro_klympush` / `GFX_portrait_RUT_independence_wave_dmytro_klympush` | `e1b935fc0410e24668d23108519b63dcd0828e071827f0973a944b5a1c00336c` |
| `iw038_rut_ivan_mondok_source_placeholder_2026_08_10__portrait_RUT_independence_wave_ivan_mondok_source_00002.dds` | `portrait_RUT_independence_wave_ivan_mondok.dds` | `RUT_independence_wave_ivan_mondok` / `GFX_portrait_RUT_independence_wave_ivan_mondok` | `bd05b469dac25edf2565ed96d174d61f0c8e0e743698cefab3555227134e4124` |
| `iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_original_00001.dds` | `portrait_BSK_independence_wave_yakov_bykin.dds` | vanilla `BSK_yakov_bykin` / `GFX_portrait_BSK_independence_wave_yakov_bykin` | `5dfe39dd9a7c72a1ac360ee3695b4779be67c10bad783458025433fdb0665e88` |
| `iw051_sakha_yak_pavel_pevznyak_source_placeholder_2026_08_15__portrait_YAK_pavel_pevznyak_original_00002.dds` | `portrait_YAK_independence_wave_pavel_pevznyak.dds` | vanilla `YAK_pavel_pevznyak` / `GFX_portrait_YAK_independence_wave_pavel_pevznyak` | `7fcb0b641c7a390cc3f0c38a4028242e6248f24246d3d468ec2b80b99d910e6f` |
| `portrait_ARX_independence_wave_emilio_lussu_source_00002.dds` | `portrait_ARX_independence_wave_emilio_lussu.dds` | `ARX_sardinian_provisional_assembly` / `GFX_portrait_ARX_independence_wave_emilio_lussu` | `0cc98f4364ac4ec5f6b15fc4e599c76b73d50a8747ba022079da19c63f65120e` |
| `portrait_ARX_vittorio_verne_source_00002.dds` | `portrait_ARX_vittorio_verne.dds` | `ARX_gavino_piras` / `GFX_portrait_ARX_independence_wave_vittorio_verne` | `529e40539e9c3623428a809eaa427a607042d28dc2516fbefc3ab1e7c8b463e5` |
| `portrait_ASX_luigi_rizzo_source_00002.dds` | `portrait_ASX_independence_wave_luigi_rizzo.dds` | `ASX_independence_wave_luigi_rizzo` / `GFX_portrait_ASX_independence_wave_luigi_rizzo` | `9a260040a88adcb7250583d7c00d20132076672781e3e3b6c614789a32f24367` |
| `portrait_ASX_luigi_sturzo_source_00002.dds` | `portrait_ASX_independence_wave_luigi_sturzo.dds` | `ASX_independence_wave_luigi_sturzo` / `GFX_portrait_ASX_independence_wave_luigi_sturzo` | `58c1d9e42a25d48e2ebf471817e6d8545a3a9d296bf29e9ee430b5582a0f00e8` |
| `portrait_ASX_pietro_lanza_di_scalea_source_00002.dds` | `portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` | `ASX_independence_wave_pietro_lanza_di_scalea` / `GFX_portrait_ASX_independence_wave_pietro_lanza_di_scalea` | `b84a64e25f270d624726e0351538d0f8cd05de54b586fd92d39e003e0118ea13` |
| `portrait_ASY_independence_wave_civic_national_assembly_source_00002.dds` | `portrait_ASY_independence_wave_civic_national_assembly.dds` | `ASY_independence_wave_civic_national_assembly` / `GFX_portrait_ASY_independence_wave_civic_national_assembly` | `717e5c11a5ac85d90d34f8aca53cc9611fb8ef0716c85bad885b5afb95829821` |
| `portrait_ASY_independence_wave_levies_guardianship_source_00002.dds` | `portrait_ASY_independence_wave_levies_guardianship.dds` | `ASY_independence_wave_levies_guardianship` / `GFX_portrait_ASY_independence_wave_levies_guardianship` | `4c75d0c118de632ecd0913525f7258758dbd1458edc1b96d1a7e66a5ede69eb1` |
| `portrait_BAY_rupprecht_of_bavaria_source_00002.dds` | `portrait_BAY_rupprecht_of_bavaria.dds` | vanilla `BAY_rupprecht_of_bavaria` / `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria` | `fb7bce1d8316f52d728e82e299eaf9675fa0dabe57f2f7c9aff154c1012478b7` |
| `portrait_CHU_independence_wave_bolgar_civic_presidium_source_00002.dds` | `portrait_CHU_independence_wave_bolgar_civic_presidium.dds` | `CHU_independence_wave_bolgar_civic_presidium` / `GFX_portrait_CHU_independence_wave_bolgar_civic_presidium` | `e031470617e94b88168155bb64826db0bdc13b83a41b4e97245a2dc30be26f67` |
| `portrait_CHU_independence_wave_federal_presidium_source_00002.dds` | `portrait_CHU_independence_wave_federal_presidium.dds` | `CHU_independence_wave_federal_presidium` / `GFX_portrait_CHU_independence_wave_federal_presidium` | `60d7a7bfb037a9f51143beb79132f5c180888dd082551794b3c1b45f60d87603` |
| `portrait_CHU_independence_wave_middle_volga_congress_source_00002.dds` | `portrait_CHU_independence_wave_middle_volga_congress.dds` | `CHU_independence_wave_middle_volga_congress` / `GFX_portrait_CHU_independence_wave_middle_volga_congress` | `2c4e5e0b00ecec70d29901bf2938bd0695192b7af0336e56e9b12cebb0a2d8a3` |
| `portrait_CHU_independence_wave_river_security_directorate_source_00002.dds` | `portrait_CHU_independence_wave_river_security_directorate.dds` | `CHU_independence_wave_river_security_directorate` / `GFX_portrait_CHU_independence_wave_river_security_directorate` | `82e790af00f8f91fbd84ed2b0195c974433c8705deb3c207f4872284d5724dc3` |
| `portrait_COR_adolphe_landry_source_00002.dds` | `portrait_COR_independence_wave_adolphe_landry.dds` | `COR_corsican_municipal_congress` / `GFX_portrait_COR_independence_wave_adolphe_landry` | `46505f5533fafcff0ee1edfa2d01cad848862742a10650006fdf2e36886ec101` |
| `portrait_COR_jean_chiappe_source_00002.dds` | `portrait_COR_independence_wave_jean_chiappe.dds` | `COR_jean_chiappe` / `GFX_portrait_COR_independence_wave_jean_chiappe` | `c91ef35a10d2f6a28594c0a30216f31317afea83bd75e820e9894ba79adf318b` |
| `portrait_DOX_prempeh_ii_source_00001.dds` | `portrait_DOX_prempeh_ii.dds` | `DOX_prempeh_ii` / `GFX_portrait_DOX_prempeh_ii` | `a04827f02e775c26e20aee6de2d25a30839a3e0ddde0b9a46af82f562ead1b79` |
| `portrait_GLC_alfonso_daniel_castelao_source_00002.dds` | `portrait_GLC_alfonso_daniel_castelao.dds` | `GLC_independence_wave_alfonso_daniel_castelao` / `GFX_portrait_GLC_alfonso_daniel_castelao` | `15f9ca69d7536439d2421dd8d55c96e94b5c56f9cdeb5ae5ee6a6210aaf25237` |
| `portrait_MAC_independence_wave_metodija_andonov_cento_source_00002.dds` | `portrait_MAC_independence_wave_metodija_andonov_cento.dds` | `MAC_independence_wave_vardar_presidium` / `GFX_portrait_MAC_independence_wave_metodija_andonov_cento` | `1e5794441f15c301659db2e2b3b0f96746b7a6ef1125f552e5635efe0fa17c11` |
| `portrait_RHI_josef_friedrich_matthes_source_00002.dds` | `portrait_RHI_josef_friedrich_matthes.dds` | `RHI_josef_friedrich_matthes` / `GFX_portrait_RHI_josef_friedrich_matthes` | `fb43deb0b8708e7f5d1000b1f67ab63aca43d54efcb75618fb9097112a7699aa` |
| `portrait_SOK_muhammad_dikko_source_00002.dds` | `portrait_SOK_muhammad_dikko.dds` | `SOK_muhammad_dikko` / `GFX_portrait_SOK_muhammad_dikko` | `84feaacc0f2e83c3f7380bb39d5a0849f30825de0e36a5c30ede82d346c676f4` |
| `portrait_WLS_george_cornwallis_west_source_00002.dds` | `portrait_WLS_independence_wave_mountain_commandant.dds` | `WLS_independence_wave_mountain_commandant` / `GFX_portrait_WLS_independence_wave_mountain_commandant` | `2a478e85cb4d025baf0bf47e5c2df5a9b75387744cd0ede894c517c2984baee2` |

The opaque `IW028_~1_00002.dds` name is mapped to Georgios Christakis-Zografos because the supplied Spyros filename provides the other exact Epirus identity and the existing Epirus portrait file contains exactly those two consumers. The supplied `MNT_kristo_popovic` and `DOX_prempeh_ii` rows intentionally use the explicitly supplied `_00001` files.

## Supplied files left unresolved

All rows below independently pass the same DDS header and dimension validation, but no safe Event 006 consumer was found. Their supplied files remain in the user source folder only.

| Supplied DDS | SHA-256 | Blocker and state |
|---|---|---|
| `iw051_sakha_yak_anatoly_pepelyayev_research_2026_08_15__portrait_YAK_anatoly_pepelyayev_original_00002.dds` | `b01b99c37a3e636db8d860c59693daa735f4593548689ac498cfa70239de2c1b` | Vanilla `YAK_anatoly_pepelyayev` exists, but Event 006 has no admitted replacement runtime basename or portrait-specific `.gfx`; a global vanilla override is outside this wiring scope. `source_placeholder`, unresolved. |
| `iw052_bya_ardan_markizov_source_research_2026_08_15__portrait_BYA_ardan_markizov_original_00002.dds` | `a75fc9449bb87cb1d5182cfbf5eb35a8033c016cae172bd9a828c9b0dac1a61f` | No existing Event 006 BYA character, live portrait consumer, or stable portrait `.gfx` key. `source_placeholder`, unresolved. |
| `iw052_bya_mikhei_erbanov_source_research_2026_08_15__portrait_BYA_mikhei_erbanov_original_00002.dds` | `72c693e538dcca71ff90a125ef83358107388f147e8b3df8b25221110063a16e` | No existing Event 006 BYA character, live portrait consumer, or stable portrait `.gfx` key. `source_placeholder`, unresolved. |
| `iw053_altai_grigory_gurkin_source_original_2026_08_15_00002.dds` | `0d0f4256d1b0bec248af91a34955c46053a6535f74e28f0e8ee441edeeba9ecd` | Vanilla `ALT_grigory_gurkin` exists, but Event 006 Altai has no admitted replacement runtime basename or portrait-specific `.gfx`. `source_placeholder`, unresolved. |
| `iw053_altai_samuil_yufit_source_original_2026_08_15_00002.dds` | `d52e9210c5e799f0a8373eca6952ace9067010d8ee15196ac15d051c921f6952` | Vanilla `ALT_samuil_yufit` exists, but Event 006 Altai has no admitted replacement runtime basename or portrait-specific `.gfx`. `source_placeholder`, unresolved. |
| `iw057_fer_alexander_krasnoshchyokov_source_original_00002.dds` | `d77715b47690703331f14551444ffe4ec3ff201078e3d43afc2705666923e84e` | No admitted FER character, portrait, or runtime consumer; the IW-057 package remains unadmitted. `source_placeholder`, unresolved. |
| `iw057_fer_pyotr_nikiforov_source_original_00002.dds` | `7aa7778130b9de37d1e6cecb98e4b70c5c1073ccbff29873702989332e241d95` | No admitted FER character, portrait, or runtime consumer; the IW-057 package remains unadmitted. `source_placeholder`, unresolved. |
| `iw060_kur_seyid_riza__portrait_kur_seyid_riza_original_00002.dds` | `5f5c00efac5524eb75f9aa172d63e0f0fd2c08ffcae2f777675d7fe8370ab1a1` | Vanilla `KUR_seyid_riza` exists, but no admitted Event 006 KUR character/portrait/runtime consumer exists; a global override is outside this wiring scope. `source_placeholder`, unresolved. |
| `portrait_ACX_cornish_port_and_mines_committee_source_00002.dds` | `48755c4c9afe3c20ac9f98c1e9283ad0c976bccf6ee4af0fd8549351525acefd` | An ACX runtime stub exists, but the existing package audit found no live ACX character or `.gfx` consumer. `source_placeholder`, unresolved. |
| `portrait_ARX_gioacchino_solinas_source_00002.dds` | `8e48f76061e93bca7343e6cb44be2078707292c240edab2f7c0a44a6484781b9` | Evidence-only ARX identity with no admitted runtime consumer; relabelling another ARX real-person character would be unsafe. `source_placeholder`, unresolved. |
| `portrait_FIJ_ratu_sir_lala_sukuna_source_00002.dds` | `00d565861009060937e8ed1a32d2b76c77a80bb59450af6af5c4d3038cf2f542` | No existing Sukuna character or portrait `.gfx` consumer. `source_placeholder`, unresolved. |
| `portrait_FIJ_vishnu_deo_source_00002.dds` | `c9c5a7cdfecad00fe72d51e7365aad7edc7e0eaf9aa52fa9e884370ba6080b06` | No existing Vishnu Deo character or portrait `.gfx` consumer. `source_placeholder`, unresolved. |
| `portrait_GLC_alexandre_boveda_source_00002.dds` | `4f2a1208be9d4fa772596c9eba9aaa284d8d12ca7926c77da5355bd33e6bd32b` | Existing GLC consumer is Alfonso Daniel Castelao; no Alexandre Bóveda character or stable runtime `.gfx` key exists, and substitution would relabel a real person. `source_placeholder`, unresolved. |

## Crop, framing, conversion, and review result

- All 51 selected source inputs pass the source-level DDS contract: `DDS ` magic, 124-byte header, 156x210 dimensions, 32-bit BGRA, no mipmaps, 131,168 bytes, and the expected uncompressed RGB/alpha pixel flags.
- All 38 installed targets pass the same contract and match their selected source byte-for-byte by SHA-256.
- Crop/framing result: the runtime framing contract passes for every selected file; existing source originals, crop evidence, and dated provenance handoffs remain the visual/source authority. This wiring-only audit makes no new same-person or HOI4-painted styled-final approval claim.
- DDS conversion through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` was skipped because the user supplied valid runtime DDS files and a second conversion would introduce an unnecessary derivative.
- No PNG output was created, no source file was copied into the repository, and no new source folder was created.
- Existing installed vanilla portrait references and the Event 006 leader/commander/operative reference families were inspected as the 156x210 framing baseline.
- RunPod was not opened, operated, configured, queued, or monitored.

## Changed files

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_portrait_wiring_supplied_runtime_2026_08_21.md` — marked superseded by this current audit so the 37/14 historical count is not mistaken for the current 38/13 state.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_portrait_wiring_supplied_runtime_2026_08_22.md` — current source path, provenance/rights state, exact hashes, identity-to-runtime mapping, unresolved list, and validation evidence.

No runtime binary or portrait `.gfx` file required modification in this tranche because the 38 safe runtime files and their existing portrait-specific registrations were already present and verified. The 13 unresolved files remain blocked pending a parent-approved, identity-safe consumer admission; no fallback was used.
