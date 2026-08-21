# Icon DDS header repair

Status: complete.

This bounded repair covers exactly the 16 DDS files assigned by the parent. It rewrote only each 128-byte legacy DDS header using `write_bgra_dds` from `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. For every file, width and height were read from header offsets 16 and 12, the pre-repair length was asserted as `128 + width * height * 4`, and the original bytes from offset 128 through EOF were passed unchanged as the BGRA payload.

No artwork was generated, resized, filtered, recoloured, redrawn, or replaced. No `.gfx`, `.gui`, gameplay, localisation, source-art, or unrelated asset files were edited. The full-file hash changed only because the malformed header was replaced; the payload hash is identical before and after for every row below.

## Runtime results

| Runtime DDS | Dimensions | Before full SHA-256 | After full SHA-256 | Payload SHA-256 (before = after) | Payload identical | Alpha min..max | Pillow decode |
| --- | ---: | --- | --- | --- | --- | ---: | --- |
| `gfx/interface/chaosx_add_10.dds` | 26x26 | `4f03bb38b4795bbb820b53a87df55f31db63cb6ea1675b978a0285d02153dfa3` | `50fd2ad0d2244b6fd3f7ef7a8021b2f369ed93c8fb840c42a689b864ae8d1cbf` | `dd350c59f4eb2d86adde1c9f4deb49325ff159a894f09a41e4ffa6b24dc482a7` | yes | 0..255 | DDS RGBA 26x26, 1 frame |
| `gfx/interface/abilitylist/cbrn_combined_overmatch.dds` | 34x33 | `5c9bcce04e8913cf1fb660583d8c5c0d6ed16ea5356d0d50280dcc6e773181ae` | `fbfe4607b2cef83ed7263de1895745b4c232879357ee382ec299c4d6201689d1` | `f0ec154937ce5e1f29b43a4e62bf361ef26b00cae33fbac3629364baeed09370` | yes | 0..255 | DDS RGBA 34x33, 1 frame |
| `gfx/interface/abilitylist/cbrn_decontamination_corridor.dds` | 34x33 | `57b046cc5f6ba3674f7573728e9982f84e021eea2ab7df540c9cb4e97415dcf9` | `2a957cfe02c42bda6a085d1efa414e1553d8d7509c879602882cffeb55f5f7c4` | `15838eef759ea981fc433b20cb19736634c2b1acb62373e9f731ecb11d218488` | yes | 0..255 | DDS RGBA 34x33, 1 frame |
| `gfx/interface/abilitylist/cbrn_mass_antidote_response.dds` | 34x33 | `3ae8188b39691401ebed5d134247f961df915ee7e95afc2247fabe3ae3cfdb53` | `2c245b78f9074955e03d2194e7e4318072342e5fe49c88912a9f14979ac4c01e` | `7661fff07c31cce767d47fe0fadfaeb6ee8a456183e3f10f636bd44ac7c68e92` | yes | 0..255 | DDS RGBA 34x33, 1 frame |
| `gfx/interface/abilitylist/cbrn_prepare_chemical_offensive.dds` | 34x33 | `d6c114e2458aad920af75004518a0e91b5c6685e27485952971f9376a861d2b3` | `c9a28a2df6147154cdd8d8d94c741b443f824c61349eaec6e708348cc6c2c99c` | `76ed5533997f476abc6b65a08bf735ae93bd8a52a0512794673f5a743dec7718` | yes | 0..255 | DDS RGBA 34x33, 1 frame |
| `gfx/interface/abilitylist/cbrn_seal_infection_corridor.dds` | 34x33 | `713d59e046e622abcf0a3d3db6c31c8f82f2156e29cca3fc1ad7a1b0100be470` | `28a4a65928d02118db751ce7768880c95822509db9b6995292d604542fd2cf2b` | `54960923423fb2f9ea1099f43547dcb088fb04c4c3f50325f778744b778da973` | yes | 0..255 | DDS RGBA 34x33, 1 frame |
| `gfx/interface/abilitylist/cbrn_seal_operational_area.dds` | 34x33 | `01d1af53df68f9c9fda1b4545e5359343f764f6d6e42ba9a477b783bc768e07c` | `8b9e7514c6d0708913278625818f773068f4662c5e0ed8624580a613e2e0704d` | `363cee14a15165058c4b9e30a12523c404e063ec1f0cf273d8ddbcac7c25d3b6` | yes | 0..255 | DDS RGBA 34x33, 1 frame |
| `gfx/interface/abilitylist/cbrn_theater_protective_posture.dds` | 34x33 | `1e9ee2e1be36df456afdc4a0591c5b1cfd2c6f46e2265a25320f9c67f6034b6b` | `0c7a4a09bfc1fbc07ef80d9dead264e584fd5114aebd1769dc4429aa9596250f` | `dd1c14054610c06d1e082edd4ba6296b0f3dbdd2c8b6fc29e1b7eb8598bee0c2` | yes | 0..255 | DDS RGBA 34x33, 1 frame |
| `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_biological_security_section_icon.dds` | 60x12 | `5ad17b0a73d8e6876697018ba4347ffc7ca76748ab191b5870221d4adf2eaf7d` | `5056c8082c13f5d3ebe56581a1cd64bb385cc43f8468fe6e796129a810441db0` | `ab2baa5ddd5145f4c5717f398c35807e6e9aa950633ca07dfc52505460425c62` | yes | 0..255 | DDS RGBA 60x12, 1 frame |
| `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_intelligence_weather_cell_icon.dds` | 60x12 | `a870b5489ee3c8ddc7cf50cc5ac4866fcbc233e3b2bb4865cb681ccade4447dd` | `f3c3d56e94e8e4ff49b10ad406974610e56242ff4338dfc01009ae38826b606d` | `6840b952355f4bd24e44574f3c4e8700677cc0d6d965c7dd77410a5837ef9167` | yes | 0..255 | DDS RGBA 60x12, 1 frame |
| `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_medical_countermeasure_directorate_icon.dds` | 60x12 | `1bb4a2f41606d295cf6d922f9d5541a8150ec3663bf35a0f0af9fa548e4a7544` | `78cccc44080f730b649abf8b861ccbf72068a23994a5dc61a0ef369ca77f215a` | `e279f87bfa0412951178811a5deeefbb4bdac307e12b4a0ccb47cd4e2a58fb5b` | yes | 0..255 | DDS RGBA 60x12, 1 frame |
| `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_mobile_decontamination_column_icon.dds` | 60x12 | `3fffc8868a509d6366382fda41a98532a4c5708692062560d71c97fcca87d240` | `2c7b58d8dd6fbdf504f37aa88b1c23bd1c28f33d52a1a94ce34f1b8370c43e4f` | `7eb524002a005264874fa9637450df95dc99310718456faa157701774534e396` | yes | 0..255 | DDS RGBA 60x12, 1 frame |
| `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_operations_section_icon.dds` | 60x12 | `ec088f2fd59ee72645b53a5c899cfc7f412e28f08450acfd79397af645b0e786` | `2aacc500b5b756dd90b917ef5d615fdac1f65645c5f3cf889bb50c637294cb3f` | `8987c33dc7384dc4e59c55a4a862df136a3e795bbe95352cc7a5c3d97f8e0365` | yes | 0..255 | DDS RGBA 60x12, 1 frame |
| `gfx/interface/counters/divisions_small/onmap_unit_cbrn_hq_protective_logistics_section_icon.dds` | 60x12 | `dff41cedc47bdd2ef3b9797ab9ba641b556fc4089d75b6c4318c1b4796d5069b` | `7c0bdc1a684b675968d6970a347536f8fbdabaf18963dd439957b865bac04ad5` | `27cf6c584ff231f9ad635cc3f05eec2c80d49d74bda26b42d8e746928890f07f` | yes | 0..255 | DDS RGBA 60x12, 1 frame |
| `gfx/interface/technologies/cbrn_theater_cbrn_headquarters.dds` | 64x64 | `28f892bb7991b7c69e057b35e75965c834f60d066b92ad18d225ac61fd2bc032` | `5e5d7f629b1d4e2b219d87b519c72e5bb9eb5467768e0bd47f60a015243ac4b5` | `ccb118ae3561786325da43bc82b30eb79242afe4cf1d02a434458d6640f96a92` | yes | 0..255 | DDS RGBA 64x64, 1 frame |
| `gfx/interface/traits/trait_infantry_expert.dds` | 23x33 | `c88a771683a7d1bb8fb9f43cb66d1b1733dbf3d161f99716c69150ca2f361ce9` | `6973370faf2ac902c4ac3bc827fbb0ee1a039356d612bf524df3b1e0c8eb1c80` | `76cc71616c32cdd584ae17f82476878462905dac0efe71c6512aff45bf56df39` | yes | 0..255 | DDS RGBA 23x33, 1 frame |

## Header validation

All 16 post-repair files passed the complete legacy one-level BGRA contract: `DDS ` magic, `DDS_HEADER` size 124, declared dimensions, exact length `128 + width * height * 4`, `DDS_PIXELFORMAT` size 32 at byte 76, pixel-format flags 65, fourCC 0, 32 bits per pixel, masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, and `DDSCAPS_TEXTURE = 0x1000` at byte 108. Pillow loaded every file as `DDS`, native dimensions, `RGBA`, one frame.

## Source/reference review and blockers

The required `chaos-redux-event-assets` workflow and its DDS section were read. The required offline Paradox wiki core pages were consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. The installed vanilla documentation consulted before the edit was `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/modifiers_documentation.md`, and `documentation/script_concept_documentation.md`; no gameplay syntax was changed.

The matching canonical reference folders were checked under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference` for ideas, decisions, achievements, technologies, officer-corps spirits, and land/air/naval counter families. Their contact sheets were Git LFS pointer stubs during this bounded repair, so they were not used as visual evidence; the parent subsequently hydrated and validated every tracked PNG. This did not affect the header-only repair because no source artwork or visual design decision was made. No blocker remains for these 16 DDS containers.

No source PNG, processed PNG, manifest, contact sheet, or `.gfx` handoff was generated because this task explicitly forbids artwork/registration changes and repairs existing runtime DDS containers only. The parent owns the task commit.

## Exact historical idea restoration

Status: complete.

The eight missing runtime idea DDS files below were restored exactly from the path-identical Git LFS pointers at commit `74cd1226e`. Each pointer OID was resolved under `.git/lfs/objects/<oid[0:2]>/<oid[2:4]>/<oid>`, the object bytes were copied unchanged to the runtime path, and the resulting full-file SHA-256 equals the historical OID. The paths were missing before this restoration; no pre-restore runtime hash exists.

| Runtime DDS | Historical LFS OID and restored SHA-256 | Bytes | Dimensions | Compression | `chaosx_ideas.gfx` texturefile references | Blocker |
| --- | --- | ---: | ---: | --- | ---: | --- |
| `gfx/interface/ideas/025_antarctic_ufo_race/idea_antarctica.dds` | `3e54d5f508435a4ff92b3f2da2c4d7d28a890f347b445b69d87e315ae54cbafc` | 2176 | 64x64 | DXT1 | 1 | none |
| `gfx/interface/ideas/049_mass_panic/idea_mass_panic.dds` | `86ded24f262972cb9fc15a48d2f42bbbb1ed5038ddec177489855f5c49936f64` | 4224 | 64x64 | DXT3 | 1 | none |
| `gfx/interface/ideas/049_mass_panic/idea_mass_panic_red.dds` | `eeb434183f51a080710cfe5d3930333115c141d4621d946439e171921bb8244f` | 4224 | 64x64 | DXT3 | 1 | none |
| `gfx/interface/ideas/049_mass_panic/idea_mass_panic_good_1.dds` | `c9b5ae635c47d8322e69f83803cab91ce9cce75639d6ff05d3adc77920baa1a0` | 4224 | 64x64 | DXT3 | 1 | none |
| `gfx/interface/ideas/049_mass_panic/idea_mass_panic_good_2.dds` | `1b9dd31132ba9d2e113e8eabebadb1529ef91766c747c4b4da9774b243107b88` | 4224 | 64x64 | DXT3 | 1 | none |
| `gfx/interface/ideas/049_mass_panic/idea_mass_panic_good_3.dds` | `c13de09d5a071a21f66f4bda5e5313cca39050859f4b0e471ee8dfd898f46a12` | 4224 | 64x64 | DXT3 | 1 | none |
| `gfx/interface/ideas/049_mass_panic/idea_mass_panic_bad_1.dds` | `accb43d9be33a10f3d28938bb14289ca122b0d1a5c4cb4e89388c1bf2b59a701` | 4224 | 64x64 | DXT3 | 1 | none |
| `gfx/interface/ideas/049_mass_panic/idea_mass_panic_bad_2.dds` | `0c8f3ca667c7eb4d629f8822068baebc8d47d6db37dc98a12b6b7bbeb1c42417` | 4224 | 64x64 | DXT3 | 1 | none |

### Restoration validation

All eight restored files passed `DDS ` magic, `DDS_HEADER` size 124, 64x64 dimensions, `DDS_PIXELFORMAT` size 32, FOURCC flags 4, the expected DXT1 or DXT3 FOURCC, `DDSCAPS_TEXTURE = 0x1000`, and exact block-compressed lengths of 2176 bytes for DXT1 or 4224 bytes for DXT3. Pillow loaded every file as `DDS`, native 64x64 dimensions, `RGBA`, one frame. Every restored path appears exactly once as a `texturefile` in the existing `interface/chaosx_ideas.gfx`; no registry or wiring file was edited.

No artwork was generated or altered, and no unrelated or concurrent edit was changed. The parent owns the task commit.
