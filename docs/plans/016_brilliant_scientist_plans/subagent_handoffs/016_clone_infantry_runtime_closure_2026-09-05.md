# Event 016 clone infantry runtime closure handoff

Status: `needs_user_review`.

Scope: existing-geometry recovery and export closure for `clone_infantry`, using the accepted body geometry from `03_rig_approved.blend` and the already-approved vanilla rifle checkpoint. No Meshy generation, regeneration, geometry substitution, gameplay edits, focus edits, GUI edits, spreadsheet edits, catalog edits, or unrelated documentation edits were performed in this continuation.

The package has a valid recovered 24-bone armature, four-influence weight ceiling, registered rifle locators, PDX/io_pdx_mesh mesh export, nine action exports, and actual-byte reimport evidence. It is not an honest final runtime-complete claim because two role pairs still have byte-identical action channels, active runtime consumers have not been switched to the closure exports in this role, and the audio evidence package lacks most immutable source bytes and final semantic audition evidence.

## Source lineage and approved inputs

The accepted body source is `docs/assets/shared_clone_system/models_3d/clone_infantry/blender/checkpoints/03_rig_approved.blend` with 5,148,975 bytes and SHA-256 `3442604F6EF83B3DA049915AB72CEBC3F536712974D891886B38E6C6C37B2A39`.

The existing-geometry manual recovery source is `docs/assets/shared_clone_system/models_3d/clone_infantry/blender/checkpoints/manual_recovery_2026_08_27.blend` with 2,031,323 bytes and SHA-256 `CD2FAA002DF7BBEFD6FFDDCBF6477612D8F3455B3C6AB0E850250F6BFBDC66C9`.

The approved rifle source is `docs/assets/shared_clone_system/models_3d/clone_infantry/blender/checkpoints/reimport_vanilla_ENG_weapon_rifle.blend` with 114,440 bytes and SHA-256 `3B9243F43F4ECC49538703AA3113E0EB34DAEB2EEBB61B1E7837D134F93214A9`.

The approved vanilla rifle mesh is `docs/assets/shared_clone_system/models_3d/clone_infantry/blender/reference/ENG_weapon_rifle.mesh` with SHA-256 `6CF9711A575DC72A5CE8F796FD04F9CAC30C134DB7D48AEDED36CB4B07ACD485`.

The approved rifle maps are `ENG_infantry_diffuse.dds` SHA-256 `95F45D8DB078AAAF620A99443A7EDAC2E76DD36D6F2039B0FBCF92F397F4979D`, `ENG_infantry_spec.dds` SHA-256 `623A5ED117C22002FA80E81215BE4997C0AE76403DE62361EC895A2C07A7E871`, and `ENG_infantry_normal.dds` SHA-256 `B6B66489AFAAF315D7472402F372E70E799314F44C32767376A7EDBB1B5C728F`.

No provider task, source-image refinement, Meshy model, remesh, rig, conversion, or animation task was used because the accepted closure plan explicitly forbids regeneration and substitution. The live Meshy balance was checked as a capability record and returned 7 credits; estimated and consumed paid credits for this closure are both 0.

## Dependency, route, and bridge evidence

The repository root resolved from the current checkout is `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux` and the deterministic job root is `docs/assets/shared_clone_system/models_3d/clone_infantry`.

The locked official Meshy package is `@meshy-ai/meshy-mcp-server` version `0.4.0`, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`, integrity `sha512-py2xFIrrBcU4SW7ked90/qjRqa6bheVn0fNLEW8Lnki3BCJTFaVvWN0W6a9mJYr26+M9y0WezGsTCKalzWrGtg==`, and schema revision `meshy-7-compat-live-declaration-2026-08-21`. The exact verified image identifier is `meshy-7`; no paid Meshy operation was invoked.

The lock-selected Blender build is 5.1.2, build `ec6e62d40fa9`, executable `C:\Program Files\Blender Foundation\Blender 5.1\blender.exe`.

The lock-selected add-on is `mcp` version 1.0.0 from `.tools/3d_pipeline/vendor/blender_mcp/addon/blender_mcp_addon/blender_manifest.toml` on socket port 9876.

The repository-owned adapter is `chaosx_blender_hoi4` version `1.10.21` from `.tools/3d_pipeline/config/blender_hoi4_adapter.json`.

The checksum-locked `io_pdx_mesh` extension is version `0.91.0` from `C:\Users\klimp\AppData\Roaming\Blender Foundation\Blender\5.1\extensions\user_default\io_pdx_mesh\blender_manifest.toml` with installed-manifest SHA-256 `C6865CEB3CE323BD54255BB37FF860E03607BD2AABED4057E9DCBE04C29682EC` and lock archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.

The lock file SHA-256 is `B68663B74AA51CD3D191AA98C0EB0BD2E7C3612E238B87D7867C923093C1EA92`, the Meshy schema lock SHA-256 is `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`, and the adapter configuration SHA-256 is `C68298F02A04084F9A0EF48196BE7AE4806EE746D9C7A290A3C27F3D202EA6FC`.

The adapter source hashes matched the dependency lock: `chaosx_blender_hoi4_mcp.py` `B72B323CC9B0C9D70597F662F951D1EC0B18F566BB9CFC3854E321D6D03849A4`, `blender_worker.py` `0C59C4E1D6A241003F59458F5DD130C05670633D304A05AB017E554410216FD6`, `normalization_convergence.py` `91AC1D4BA9BE4D39AB4697F9044060A9F119A8998E1DADA8F4A8E6F58A5F9ED5`, and `blender_client.py` `B2FE78FA84E297C6A9130F4E2E17E2E3C1620F417306E33F3066B6F9162241A50`.

The socket was initially not listening, so the lock-selected Blender executable was started hidden with `--background --online-mode --command blender_mcp --host 127.0.0.1 --port 9876`. The subsequent bridge probe listened successfully. Adapter health request `412542b1326442b3a86f0f45267f7b04` reported Blender 5.1.2, `io_pdx_mesh_loaded: true`, all four required PDX operators, and worker log `logs/adapter/412542b1326442b3a86f0f45267f7b04.result.json`.

## Recovered geometry, materials, rig, and weights

The final source checkpoint is `blender/checkpoints/closure_2026_09_05_locators_v2.blend` with 2,030,839 bytes and SHA-256 `29DAAC7EFF2A884F5D34864EAFFE0DFD8383850307A31441FA2E4E5B60182C84`.

The preceding registered-muzzle checkpoint is `blender/checkpoints/closure_2026_09_05_muzzle_locator_v2.blend` with 2,030,894 bytes and SHA-256 `A15D24FE85B2FFFA64200C2E97A77CB739EFDB138B8CC86EECA05570DFAB4EF6`.

The final inspect request was `386e4093078545649d403aa380cd5d9f`.

The preserved mesh is `Mesh_0.002` with 15,398 vertices and 30,409 triangles, dimensions `[6.665046691894531, 1.6425962448120117, 7.351824760437012]`, zero degenerate faces, zero non-manifold edges, 351 boundary edges, and 43 boundary components. Existing boundary/loose-edge evidence is recorded rather than repaired through geometry replacement because the no-regeneration closure plan requires preserving the accepted body geometry.

The calibrated source height is 7.3518242835 m, the effective runtime height is 5.8814594268 m, and the entity scale is 0.8 applied once. The selected vanilla comparison is `western_european_infantry.mesh`; forward is `-Y` and up is `+Z`, with collision-only geometry excluded from the measurement.

The armature is `clone_infantry_rig` with exactly 24 bones. The final weight audit reports 15,398 weighted vertices, histogram `1 influence: 391` and `4 influences: 15,007`, zero vertices over four influences, zero zero-weight vertices, and weight sums from `0.9999999553` to `1.0000000447`.

Materials retain the recovered body material and the approved vanilla rifle material. The rifle material is `PDXmat_MeshShape` using `ENG_infantry_diffuse.dds`, `ENG_infantry_spec.dds`, and `ENG_infantry_normal.dds`; the recovered body material and textures remain in the source checkpoint and were not replaced.

The rifle remains joined to the recovered mesh with 391 rifle vertices and the documented `armature_modifier_Spine02_single_influence_with_idle_pose_compensation` attachment. Three-quarter attack and death previews show both arms converging on the rifle and the rifle remaining attached through the pose; no numeric hand-to-trigger or hand-to-foregrip distance audit was available from the locked adapter, so parent review of contact remains required.

The preview evidence is `blender/previews/reimport_closure_2026_09_05_attack_frame_025_three_quarter.png`, `blender/previews/reimport_closure_2026_09_05_attack_frame_001_three_quarter.png`, and `blender/previews/reimport_closure_2026_09_05_death_frame_025_three_quarter.png`. The attack views show a non-static rifle firing pose with the arms around the weapon. The death view shows an articulated collapse/reaction with the body leaning and the rifle crossing the waist rather than a static standing alias.

## Registered locators and export evidence

The adapter rejected an attempted update of the old unowned name `muzzle` with request `8ead076e08ac4f6aa22e1b88dea2c4eb` and error `ValueError: Locator name collision or ownership/registration mismatch.` This is the exact reason the final export uses new job-owned names instead of silently mutating the old unregistered empties.

The registered muzzle locator was created by request `1778ef08d253488d80f9c69157fa045d` as `clone_muzzle` under `clone_infantry_rig`, bone `Spine02`, with position `[2.1539011001586914, 0.4609694480895996, 0.9051755666732788]` in Blender local coordinates and normalized quaternion `[0.5792905968, -0.4534693849, -0.4856686362, -0.4721375830]` in Blender x/y/z/w order. The checkpoint matrix reconstruction error was `2.384185791015625e-7`.

The registered cartridge locator was created by request `5105aa78c0a54f8d86dcab951c8344d9` as `clone_cartridge` under `clone_infantry_rig`, bone `Spine02`, with position `[-0.3788050711154938, 0.20806217193603516, 0.6232104301452637]` in Blender local coordinates and the same normalized quaternion. The checkpoint matrix reconstruction error was `2.384185791015625e-7`.

The final mesh export is `export/closure_2026_09_05/clone_infantry_locators.mesh` with 2,476,066 bytes and SHA-256 `1C25F0E8C14B4E58CAAB8F33BFE2A9713C748D09D912CE8293C48BBDF455751B`. Export request was `8d3a69a7262d4313afd7919cefe41d1b`. The export reported 15,398 vertices, 30,409 triangles, no exporter warnings, streams of 22,727 and 1,227 vertices for 30,000 and 409 triangles, and the preserved 43 boundary components and 351 loose edges.

The locator text companion is `export/closure_2026_09_05/clone_infantry_locators.txt` with 8,571,451 bytes and SHA-256 `7A338C14849106B373C293902F04478BC3FB73FFC06ACEECCAEA329EB4655011`. Its serialized locator records are `clone_muzzle` and `clone_cartridge`, each parented to `Spine02`, with PDX coordinate order `p=[x,z,y]` and quaternion `[0.5792905688285828, -0.48566877841949463, -0.4534693956375122, 0.47213754057884216]`.

The old unregistered `muzzle` and `cartridge` empties remain in the checkpoint but are not selected for export. Parent runtime wiring must therefore reference `clone_muzzle` and `clone_cartridge`, or perform a separately reviewed bounded rename/registration operation that preserves ownership and does not regenerate geometry.

## Action exports and actual-byte reimports

The final source contains nine actions at 24 FPS. The normal range is frames 0 through 48, and `clone_infantry_support_attack` is frames 0 through 36.

| Role | Export path | Export request | `.anim` SHA-256 | Reimport proof `.blend` SHA-256 | Validation JSON SHA-256 | Grounding evidence |
| --- | --- | --- | --- | --- | --- | --- |
| idle | `export/closure_2026_09_05/anim/clone_infantry_idle.anim` | `66bbbeeb186a4a1abfa94c47d6909217` | `2FCC46C6B198B8F3CB7E094F6A63BC314151123C6397F046550740078F1029B2` | `368D914CA7C4BF17714632AD9F581C62421174CC14BBA734753F6FD33C2840C4` | `829C06D28234DB102ECAA6C1F866381E481B8B013114DFE0E7470DE4AB7BD30E` | minimum `-6.423899776564213e-7` |
| move | `export/closure_2026_09_05/anim/clone_infantry_move.anim` | `33afb866dda94bda811ba8b9fe872cfb` | `6AD974F352F3945D13FC1526FAE31674FEE0886CFC70FC0A9E9DF61F9624CC06` | `230A56CA3A10E39412778F9620788B68ED7373066A55CE8B24EE4F8C08CE1237` | `EBB6FFE73513B3F5691DC440C7209BEE291867C0A265227D281002FB867CC36A` | samples alternate around 0, minimum `-8.555389285902493e-7` |
| attack | `export/closure_2026_09_05/anim/clone_infantry_attack.anim` | `b0fcb39b319946139d0064525e47ec0b` | `B60CC3BC1ED2015F6B6893916AA2E72B8FC17BEE210DC17BBB10C63899F5567E` | `7E7EE7F829FFEB4F9F71BEC2386A4ABE67CCFEBE31E2B8118214C4F44FE12FC9` | `151E24366F9842A4AF588D10607DFD088DCA2A333BC4580A4BD003AC7ADCB9EB` | minimum `-6.423899776564213e-7` |
| defend | `export/closure_2026_09_05/anim/clone_infantry_defend.anim` | `2f1c2ecceb474d1bbea61eb6b5fa1b53` | `2FCC46C6B198B8F3CB7E094F6A63BC314151123C6397F046550740078F1029B2` | `3BD1FBA5B57F4DDD4A22D0EB316109D587EE1787FBDB4C2A9783FFA06333B125` | `29C3263CCF1977B9A9AE13E534598522ECBF8CE4CF0AACFB6697C0FE01F56C98` | minimum `-6.423899776564213e-7` |
| support_attack | `export/closure_2026_09_05/anim/clone_infantry_support_attack.anim` | `3c706fd076444dccb4281371a68b0db5` | `565C7E7DD330F282FABA4149599DED9F27984C9720576C726BAC168E3398C77A` | `2895F0470267CA275BED4DCBE39F1873A9FFAF51042A74DFB337AD3A4693285D` | `ABC05FB7B3F2A4434920797DDC2BC40A51CC48D443713FA04967042E82F4D902` | minimum `-6.423899776564213e-7` |
| retreat | `export/closure_2026_09_05/anim/clone_infantry_retreat.anim` | `5a37be1560d54ce8aa083968e500dfb9` | `5DEB70EC8C3FC6E6B7D45A9A91496A6379889CD24EF906F13C18B7ABD05D7C16` | `309187DEFA77D958ED6A5876FE3E736B96E2907352272B9BC67462831EC21DEA` | `4226AE10A3C57DCC39EFEAE454D9F88CE5E3820470F408F8CDCAE7FFCB4505F0` | minimum `-6.423899776564213e-7` |
| training | `export/closure_2026_09_05/anim/clone_infantry_training.anim` | `d95fb913f8674c069286dec21f16f7bd` | `214C8D6929D5A830A90CC209B2C8E72409D43E106FBB5BCCD559523CCA818F25` | `F5C6C9343C37B1F9443E94A822851B27D51F365020CB5ADF29880643B0033264` | `B9C385CBEB08CB94C7B89C5D2B0803952B3271A90FEDC0E8A3329CB57FF03FE6` | minimum `-6.267775347623683e-7` |
| wounded | `export/closure_2026_09_05/anim/clone_infantry_wounded.anim` | `6a1281a0f1bb490890bcd6bd82417be7` | `214C8D6929D5A830A90CC209B2C8E72409D43E106FBB5BCCD559523CCA818F25` | `565F50E7FD79E23F6802B5864542FFEC3A8A247C52CC15F151B9859CA1B0FF80` | `D2F2323FAA15B789444740935375817EC38BA291570BD37D49F78358582FA672` | minimum `-6.267775347623683e-7` |
| death | `export/closure_2026_09_05/anim/clone_infantry_death.anim` | `348b8c20612a43678686d879f3cb4970` | `3C57E34460E6C59D0A35577139DE0DD6C780B65BC4FC20D2285464FFD7986FF4` | `6D2BAE07396A0F167277A44F050F1B1180BA3A7B7D4FD38475BADC5EE14329B8` | `6828BE25C6B4DF2653A5963C8787F58B81B6AA93DD2CE780F680A3C244029E31` | frame 1 `-8.555389285902493e-7`, later samples within approximately `4e-7` |

All nine actual-byte reimports completed through the locked `reimport_export` route without an error. Each reimport reported a 24-bone `io_pdx_rig`, one mesh, and 30,409 triangles. The importer diagnostic exposes UV/normal seam vertices and 1,849 boundary components with 14,739 loose edges before position welding; the position-welded diagnostic reports 15,229 vertices, 67 loose edges, and zero non-manifold edges. These are importer diagnostics and must not be confused with the export-side 43-component/351-edge topology evidence.

Reimport preserves `clone_muzzle` and `clone_cartridge` with parent bone `Spine02`; the importer strips the adapter-only `owner_job` and `registered_for_export` metadata, which is expected and recorded here.

The death action is articulated and non-static in the source and preview evidence. Its recovery record contains 13 source action curves and a 39,763-byte full export. Grounding correction retained the documented recovery death root offset range of approximately `-0.489938` through `0.004214`.

Attack phase evidence identifies a multi-frame firing action with `firing=true` and discharge at source frame 25, or 1.0416667 seconds at 24 FPS. Support attack identifies discharge at source frame 19, or 0.7916667 seconds at 24 FPS. The source recovery record and previews retain rifle aim/discharge/recoil/recovery structure, but the unavailable phase-patch operation prevented a fresh independently generated channel report; parent should perform the final action-phase review before declaring runtime acceptance.

## Action distinctness blocker

The native action-channel SHA-256 values are identical for `idle` and `defend` (`DF52AF6108ACDE2958FDDDC452EFFC29C4C32996D47CBF340262FD2BF5077910`) and identical for `training` and `wounded` (`674458D8F14F5BA894D91FE746CFA7A65E646CA271835E0256518395D1A8BFFE`). The exported `.anim` hashes repeat the same pairs, proving that the role names are not sufficient to establish genuine distinct motion.

The other native action hashes are `move` `8E7568A559FFE2E825434201CAC883A12D9289C69459D71F12072A9935E9793C`, `attack` `3DE688204DE65A947575A810D81BE0BE1DBD81CA5D99F72EA0DA594154CB3C0A`, `support_attack` `4DF21214AE8CE8067628CDC5C5AEA950AA951CDA838FBFBC0E7F9B728853CB44`, `retreat` `FD6B19ED72A559198103AE2BABFE5EAD430F568AD94F8C190720A1E1F936CFA5`, and `death` `0D6BCFA7BE4512ED3621C088A801B5B05DB6E8C84EB58E35A28EDC559E3FEEF0`.

The adapter configuration lists `patch_existing_humanoid_action_phases`, but no callable MCP route exposing that operation was available in this runtime. `author_humanoid_actions` and procedural/local replacement actions were not used because the skill forbids local final skeletal motion and the closure plan forbids replacing accepted geometry or source motion. This is the exact remaining action blocker, not a permission request or a reason to substitute geometry.

## Runtime consumer and particle/light handoff

No `.asset`, `.gfx`, animation registry, sound registry, gameplay, or entity source file was edited in this role because runtime wiring is parent-owned and concurrent runtime edits are present elsewhere in the workspace.

The read-only clone entity source is `gfx/entities/clone_infantry.asset`. It currently names the nine states `idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, `wounded`, and `death`, uses entity scale 0.8, and has existing sound events at move 0.0417/0.5833, attack voice 0.0/rifle 1.15/cartridge 2.2, support voice 0.0/rifle 0.3/cartridge 0.55, wounded 0.0417, and death 0.0417.

The read-only clone graphics source is `gfx/entities/clone_infantry.gfx`; the animation registry is `gfx/models/units/clone_infantry/animation_clone_infantry.asset`. The active runtime animation files currently have older hashes and were not replaced in this role. Parent must either copy the closure exports to the existing runtime paths or update the animation registry after the duplicate-action blocker is resolved.

The installed vanilla precedent `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\entities\units_infantry.asset` was inspected. Its ENG rifle `attack` event uses node `muzzle`, particle `rifle_muzzle_particle`, light `muzzle_flash`, and soundeffect `infantry_rifle_attack` at 1.15 seconds, followed by node `cartridge`, particle `rifle_cartridge_particle`, and soundeffect `infantry_rifle_cartridge` at 2.2 seconds. Its `defend` event uses muzzle at 0 and cartridge at 1.2, and its `support_attack` event uses muzzle at 0 and cartridge at 1.2.

The clone entity currently has no verified particle/light event block. Parent should add the narrow consumer wiring after action review, using `clone_muzzle` and `clone_cartridge` or a reviewed registered rename, and should preserve the measured attack discharge time of 1.0416667 seconds and support discharge time of 0.7916667 seconds rather than blindly copying vanilla timing. A cartridge timing was not measured in the recovered action evidence, so it must not be invented; parent should select it from the accepted action-phase audit.

## Audio provenance and remaining audio blocker

The existing provenance record is `audio/evidence/provenance.md` and the sound handoff is `audio/sound_design_handoff.md`, currently marked `needs_user_review`.

Documented candidate sources are OpenGameArt soldier voice acting at `https://opengameart.org/content/soldier-voice-acting` by `kurt` under CC BY 3.0, OpenGameArt male death and pain grunts at `https://opengameart.org/content/grunts-male-death-and-pain` by `thebardofblasphemy` under CC0, BigSoundBank marching boots at `https://bigsoundbank.com/marching-in-1-s3023.html` with direct file `https://bigsoundbank.com/UPLOAD/bwf-en/3023.wav`, BigSoundBank 7.62 mm cartridge on concrete at `https://bigsoundbank.com/douille-de-7-62mm-sur-beton-1-s1367.html` with direct file `https://bigsoundbank.com/UPLOAD/bwf-en/1367.wav`, and Wikimedia `Gunshots 8.ogg` at `https://commons.wikimedia.org/wiki/File:Gunshots_8.ogg` with direct redirect `https://commons.wikimedia.org/wiki/Special:Redirect/file/Gunshots_8.ogg` by `aradlaw` under a public-domain dedication.

The active candidate WAVs under the repository `sound/` tree and their hashes are `sound/shared_clone_system/clone_infantry/clone_infantry_attack_voice_01.wav` 33,712 bytes SHA-256 `7D2B088E00FA2010B0C0EFE00A73933FE8EC5BDDCDE71BEF92F102932A5B224B`, `sound/shared_clone_system/clone_infantry/clone_infantry_casing_01.wav` 87,928 bytes SHA-256 `389BF2808C4398BF5B5EE93B462905D8D4460DF6501C3C1732E588FA4AD22EA6`, `sound/shared_clone_system/clone_infantry/clone_infantry_death_01.wav` 122,412 bytes SHA-256 `2302251F6BD604AB16D46446AC9556689951C827D980CE20868BDDB37E3E7DA9`, `sound/shared_clone_system/clone_infantry/clone_infantry_rifle_01.wav` 79,576 bytes SHA-256 `A2C95706A790F48A318CC2301CF5B776433ABA28815072D3F437E5A59478CD7C`, `sound/shared_clone_system/clone_infantry/clone_infantry_step_left_01.wav` 23,040 bytes SHA-256 `77ABDB9056F7D9539CA5BC00F64781220093444770EFBA07F4F338825917CC1C`, `sound/shared_clone_system/clone_infantry/clone_infantry_step_right_01.wav` 29,302 bytes SHA-256 `10E99BE91B24A7AD8C67B205CC16E39EEE8D4A11DF043C55B95BE6C687FE59A0`, and `sound/shared_clone_system/clone_infantry/clone_infantry_wounded_01.wav` 60,966 bytes SHA-256 `89F0A1B92C4CB19796E4CE40C68F89D420F858853A053CD095ABCA724F46F85D`.

Only `audio/evidence/originals/cartridge_762_concrete.wav`, `audio/evidence/originals/death_pain_grunts.wav`, and `audio/evidence/originals/marching_boots.wav` are present under the job root. The provenance document names additional originals and derived OGG candidates, but those immutable source bytes are absent from this checkout. The spoken semantics were not auditioned in this role, and the original rifle/casing synchronization was previously blocked; registered locators now exist, but that does not close the licensing or audition gap.

The documented proposed synchronization is move left frame 1 and right frame 14, wounded frame 1, death frame 1, attack voice at start, rifle report at the accepted discharge phase, and cartridge after the accepted ejection phase. Parent must re-audit source bytes, licenses, identifiers, and exact attack/support synchronization before treating the sound package as complete.

## Counter handoff

The bespoke counter package is under `counter_art/` and its manifest is `counter_art/manifest.md` with status `complete_for_parent_wiring`. The large strip is `counter_art/dds/clone_infantry_large_strip.dds` at 152x42 with two 76x42 frames and SHA-256 `ccc3cf926beea92caead6ac54cb8006694b5c1ccf6e957c4ceae63f83f9edde8`. The on-map strip is `counter_art/dds/clone_infantry_map_strip.dds` at 60x12 with SHA-256 `5dd84708accc4cd9ce5e8de3f307eea8a3b64661c1cfb8dca4548750f7f8344b`.

The supplementary equipment strip is `counter_art/dds/clone_equipment_archetype.dds` with SHA-256 `21ee953054fe6546b58e242d935f803e879d0c3c1cb15389cccd02791ada6056`, and the technology strip is `counter_art/dds/clone_equipment_technology.dds` with SHA-256 `39b356a06d68b05c4baa60dcfe93f3439f821f47ede0d2130672f9ac3ed22adb`.

The counter contact sheet SHA-256 is `56dc3cc87ac7eead0961294230e127c010d483c92c83997e929bd2aa175965f1`. Sampled vanilla-green values are `(73,106,73,255)`, `(74,107,74,255)`, `(83,114,83,255)`, `(100,128,100,255)`, and `(116,141,116,255)`.

Parent-owned token and consumer notes are in `counter_art/gfx_handoff.md`, including `GFX_group_clone_infantry_icon`, `GFX_unit_clone_infantry_icon_medium`, and `GFX_unit_clone_infantry_icon_medium_white`.

The Aryan counter package is `counter_art/aryan_clone_infantry/dds/aryan_clone_infantry_large_strip.dds` SHA-256 `f682cc37f94996da4be945ca35c9521b1011dadf20fd9d9971322635c2f86d27` and `counter_art/aryan_clone_infantry/dds/aryan_clone_infantry_map_strip.dds` SHA-256 `2ada47ce06be2da387f78c5022540c80c9382af0ea7c5c1588603a6f403be00a`. Its status is `visual_review_accepted_parent_wiring_pending`.

Aryan clones remain normal German infantry model aliases. The read-only `gfx/entities/zz_clone_infantry_aryan.asset` aliases `GER_infantry_entity`, `GER_infantry_entity_snow`, and `GER_infantry_entity_desert`; this mapping was not changed and must not be redirected to the clone mesh.

## Parent-owned remaining work

1. Resolve the exact `idle` versus `defend` and `training` versus `wounded` duplicate-channel blocker through an authorized provider/professional-source route or an exposed locked phase-cleanup route. Do not use local procedural replacement, static aliases, or geometry substitution.

2. Review the attack and support action phase evidence, retain aim/discharge/recoil/recovery, choose the cartridge event phase from evidence, and wire all nine distinct action identifiers to the accepted exported bytes.

3. Copy or reference the final closure `.mesh` and `.anim` outputs from `export/closure_2026_09_05/` only after resolving action distinctness, and update the parent-owned animation/material/entity consumers without changing Aryan aliases.

4. Add and verify clone particle/light events against the inspected vanilla `rifle_muzzle_particle`, `rifle_cartridge_particle`, and `muzzle_flash` consumers, using the registered locator names and measured action timings.

5. Re-audit the audio source bytes and licenses, preserve immutable originals under the job evidence root, audition identity-matched voice candidates, and synchronize rifle/cartridge/death/wounded/step roles to final action phases with checksums.

6. Wire the bespoke clone large and on-map counters from `counter_art/` and preserve the Aryan German-infantry alias behavior.

7. Review the export-side 43 boundary components/351 loose edges and importer diagnostic seam artifacts as an acceptance risk. The geometry was intentionally preserved and no regeneration or substitution was performed.

## Files created or generated in this continuation

The new documentation handoff is this file: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_clone_infantry_runtime_closure_2026-09-05.md`.

Generated or updated closure artifacts are `blender/checkpoints/closure_2026_09_05_muzzle_locator_v2.blend`, `blender/checkpoints/closure_2026_09_05_locators_v2.blend`, `export/closure_2026_09_05/clone_infantry_locators.mesh`, `export/closure_2026_09_05/clone_infantry_locators.txt`, nine files under `export/closure_2026_09_05/anim/`, nine reimport proof `.blend` files under `blender/checkpoints/` named `reimport_closure_2026_09_05_<role>.blend`, nine `validation/reimport_closure_2026_09_05_<role>.json` files, and the reimport preview PNGs named above.

No files outside the clone-infantry model job, its evidence package, and this handoff were intentionally changed by this role. No files were staged or committed.

## Validation limits and completion decision

Meaningful validation completed: locked adapter health, live socket probe, exact source/checkpoint hashes, scene geometry and material inspection, 24-bone audit, normalized weight audit, registered locator creation and matrix checks, PDX mesh export, nine PDX animation exports, nine actual-byte reimports, reimport action/rig/topology summaries, grounded frame samples, three-quarter attack/death previews, vanilla particle/light consumer inspection, and counter checksum/palette inspection.

Meaningful validation skipped: live game consumer validation, final runtime animation binding, exact hand-to-trigger/foregrip distance measurement, independent attack/support cartridge-phase measurement, audio audition, complete immutable source-byte verification for all documented audio candidates, and resolution of the duplicate-role action channels. These remain parent/user review items rather than silently passed gates.

The package is therefore `needs_user_review`, with the recovered existing geometry, approved rifle, rig, weights, registered locators, export bytes, reimport proofs, and counter art handed off, but with exact action-distinctness, runtime consumer, topology-risk, and audio-provenance limitations explicitly retained.
