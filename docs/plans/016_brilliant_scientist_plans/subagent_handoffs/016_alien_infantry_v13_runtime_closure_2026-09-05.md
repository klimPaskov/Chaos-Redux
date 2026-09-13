# Alien Infantry V13 runtime closure handoff

Date: 2026-09-05.

Disposition: the preserved V13 model, rig, genuine provider actions, supported muzzle locator, exact export/reimport evidence, sourced audio package, counter handoff, and narrow runtime bindings are implemented in this subtask; parent review and user-owned live consumer validation remain open.

This handoff supersedes the stale locator and impact statements in the earlier runtime handoffs while retaining their historical provider records. It does not claim that Hearts of Iron IV was launched or that the live game accepted the package.

## Scope and ownership

The job root is C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/assets/016_brilliant_scientist/models_3d/alien_infantry/.

The closure changed only Alien Infantry runtime/artifact/wiring surfaces: the promoted locator-bearing mesh, the alien entity event bindings, Alien Infantry sound definitions and category registration, the sourced impact WAV, audio provenance, current runtime crosswalks, and this handoff.

No gameplay balance, event, decision, focus, country, history, AI, localisation, GUI, spreadsheet, shared specification, unrelated package, or counter art file was edited.

No file was staged or committed by this subtask.

The seven existing .anim binaries were not regenerated, replaced, or locally authored; their hashes remain the accepted V13 hashes below.

## Source and provider lineage

The accepted input is the one-image V13 Meshy route recorded in refs/original/input_manifest.json and attempts/v13_firearm_preset/provider_lineage.json.

The user supplied and explicitly authorized the actual colorized reference; the immutable source is refs/source/user_supplied_alien_reference.png with SHA-256 17FEF636D5ADA350D92B1F432B58459B135F038BEB97CFEDA201CCF314BF984F, and the sole approved Meshy input is refs/original/meshy_input.png with SHA-256 E024BF5B536FB289744268D16389D17F2E2A09F15B211882F437FCF500CFE8AA.

The source has no external source page or creator attribution because it is user-supplied; its authorization basis is recorded as reference_only_user_authorized, and the source and all ImageGen preparation material remain non-shipping evidence.

The approved ImageGen preparation prompt, source-to-refinement comparison, colorization decision, opaque-background note, and approval timestamp are in evidence/imagegen/v13_tpose_right_pointing_colored/preparation.md and refs/original/input_manifest.json.

The exact provider model is meshy-7.

The accepted generation task is 01a03dc3-905a-7d02-aba6-05500f877b97; the rejected firearm-omitting generation is 01a03dbc-7913-7257-961a-56dea6cf6b04 and remains evidence-only.

The accepted triangular remesh task is 01a03dc9-8951-79ad-bc08-ae94ad607dfe, and the provider humanoid rig task is 01a03dcf-f0ba-7b67-b769-5a2678b03a40.

The provider action tasks and source FBX checksums are the per-role records in attempts/v13_firearm_preset/*_animation_provenance.json and the action table below.

Prior V13 provider spend was 103 starting credits, 91 consumed, and 12 remaining, including the rejected 30-credit generation, accepted 30-credit generation, 5-credit remesh, 5-credit rig, and seven 3-credit actions.

No Meshy operation or credit spend occurred during this closure; the 12-credit balance was not used.

## Locked toolchain and vanilla references

The process MESHY_API_KEY hard gate passed before repository intake; the key value was never exposed.

The dependency lock is .tools/3d_pipeline/config/dependencies.lock.json with SHA-256 B68663B74AA51CD3D191AA98C0EB0BD2E7C3612E238B87D7867C923093C1EA92.

The locked Meshy schema is .tools/3d_pipeline/config/meshy_tool_schema.lock.json with SHA-256 E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233; its revision is meshy-7-compat-live-declaration-2026-08-21 and exposes exactly one meshy-7 model identifier.

The selected official Meshy MCP package is @meshy-ai/meshy-mcp-server 0.4.0 at git head d8c77d1cb897e345eb41d38b510b8391b1664346, with SDK 1.29.0.

The selected adapter route is chaosx_blender_hoi4; its lock-resolved version is 1.10.21 from .tools/3d_pipeline/config/blender_hoi4_adapter.json, whose SHA-256 is C68298F02A04084F9A0EF48196BE7AE4806EE746D9C7A290A3C27F3D202EA6FC.

The selected Blender executable is C:/Program Files/Blender Foundation/Blender 5.1/blender.exe, version 5.1.2, build ec6e62d40fa9; the separately probed adapter socket is 127.0.0.1:9876.

The installed extension is io_pdx_mesh 0.91.0, with locked archive SHA-256 A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2 and installed manifest SHA-256 C6865CEB3CE323BD54255BB37FF860E03607BD2AABED4057E9DCBE04C29682EC.

The adapter health request 032b5d5dce4e41b89da8c6d0b4ab3d13 passed; its response is in logs/adapter/032b5d5dce4e41b89da8c6d0b4ab3d13.result.json.

The named vanilla model reference is C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/western_european_infantry.mesh.

The named vanilla entity precedent is C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/units_infantry.asset#infantry_rifle_entity.

The offline Paradox wiki graphical-asset/entity references and the installed vanilla documentation were consulted before the entity and sound syntax changes; the exact vanilla event forms for node, particle, keep_particle, light, and nested sound are evidenced by gfx/entities/nuke.asset and gfx/entities/units_infantry.asset.

## Geometry, exporter ceiling, and preservation result

The retained source checkpoint is blender/checkpoints/v13_firearm_preset_alien_locator_working_retention_checked_2026_09_02.blend with SHA-256 70CA01923E64DDC9FD671DD5801951973ED4FD3E7B0232CADDEAAABA8DE97185.

The only closure mutation was the adapter-authorized author_locator operation 5151850a57324a428be6080efaa7f071, whose policy is one registered leaf empty with no mesh, material, weight, bone, action, or scale edits.

The resulting checkpoint is blender/checkpoints/v13_firearm_preset_alien_locator_author_20260904.blend with SHA-256 6EFE1DFC67D9CFD13F2C524B8E924389DC39640501A0B58E0BCAB94B0B44E399.

The prior bounded V13 working reduction from the provider target to 59,999 triangles is retained because it already passed the accepted geometry path; no additional reduction, partition, decimation, weapon replacement, or regenerated geometry was performed in this closure.

The mesh export request was ce2af836a6b84870aca65f4789920e52 through the locked adapter and io_pdx_mesh route.

The closure export is export/v13_firearm_preset_locator_closure_20260904/alien_infantry.mesh, 15,122,561 bytes, SHA-256 A8740E95C5F12D63D656B58891A52E1F059EDA2CDBF55DB521968D3932F906B4.

The runtime mesh gfx/models/units/alien_infantry/alien_infantry.mesh is byte-identical to that closure export with the same 15,122,561-byte length and SHA-256 A8740E95C5F12D63D656B58891A52E1F059EDA2CDBF55DB521968D3932F906B4.

The accepted pre-locator provider mesh remains preserved at export/v13_firearm_preset/alien_infantry.mesh with SHA-256 D03EA316E2C5DCC4BD3224AE7D3C62DF3F86E4CADA77A6A7535C15D74BDF8342; it was not overwritten.

The export report is blender/reports/export_mesh.json with SHA-256 D8959E932A81EED12F12B9EB109647C9175FFBDF58175C5C546F260BC466A5E4.

The export report records 59,999 triangles, 59,451 scene vertices, one map1 UV layer, zero degenerate faces, zero non-manifold edges, zero negative-scale objects, zero zero-length normals, and no exporter warnings.

The report records vertex_stream_limit = 65535 but also reports maximum_stream_vertices = 1 and mesh_streams.vertices = 1, which is an adapter report/parser anomaly rather than the native stream count.

The actual exported text stream is preserved at export/v13_firearm_preset_locator_closure_20260904/alien_infantry.txt with SHA-256 477FEE2694AC4784E7DBB94D2F50669634ADD40D1C729CD8E3F38BE0F06A9874; its native position stream is p (float, 539991) for 179,997 split triangle vertices.

The acceptance basis for the ceiling is the zero-warning export plus actual-byte reimport through the locked adapter, not the anomalous report field.

The actual-byte mesh-only reimport request was 66813cc8087047c0ba5139367f9d048e.

Its validation is validation/reimport_alien_locator_closure_mesh_20260904.json with SHA-256 4FFA0F412B4556E149BF70FF1F3BD5DDC091B74C1803B1F440D7FF72FB9B6CDF, and its proof checkpoint is blender/checkpoints/reimport_alien_locator_closure_mesh_20260904.blend with SHA-256 4EF9DF1B76EECFD57683914D8A2B598BF54B59E8DC2205D86116B9B7EC49D93E.

The reimport contains 59,999 triangles, 179,997 split vertices, 30,035 position-welded diagnostic positions, 157 position-welded loose edges, zero non-manifold edges, zero degenerate faces, zero zero-length normals, one 24-bone armature, and the exported muzzle locator.

The 157 welded loose edges are the measured seam/topology diagnostic after position welding and are not a hole or non-manifold failure; the exported UV and normal seams remain unchanged.

## Calibration, materials, rig, and weights

The vanilla source height is 7.3518242835, forward is -Y, and up is +Z.

The V13 source geometry height is 7.3518023491, the runtime entity scale is exactly 0.8, and the effective runtime height is 5.8814594268.

The export bounds are [-3.0820617676, -0.9942462445, 0.0000884251] to [3.0818808079, 0.9942484498, 7.3518905640] with dimensions [6.1639423370, 1.9884946346, 7.3518023491].

The material is PDXmat_char1.002 with provider diffuse, specular, and normal channels; runtime GFX points the PdxMeshAdvanced material to the unprefixed runtime maps.

The runtime diffuse, normal, and specular DDS bytes remain identical to the V13 provider maps with SHA-256 0A44479B3205D2E732A5E4A9D1ECFC45BC61830E38244C06D1C028A89A62D3AA, DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39, and 5F1224A4443C20432182668DB6F567CCAD02B9D8143F57F08DFB88183CCE755D respectively.

The armature is io_pdx_rig with 24 bones, object scale [1,1,1], and mesh object scale [1,1,1] after export normalization.

The retained source weight audit has 59,451 vertices, 24 bone groups, zero non-bone groups, zero vertices over four influences, zero zero-weight vertices, influence histogram 1:28011, 2:17207, 3:4682, 4:9551, and weight sums between 0.9999999553 and 1.0000000447.

The fused right-hand laser pistol remains part of char1.002 in every action; no separate weapon object, attachment, constraint, weapon bone, or local weapon motion was introduced.

## Supported muzzle locator and actual-byte proof

The author_locator request created exactly one registered muzzle empty on io_pdx_rig bone RightForeArm with parent type BONE.

The requested bone-local position is [-0.088371573, 0.828393733, 0.061190991].

The requested bone-local quaternion in XYZW order is [0.19477866, 0.11260580, 0.84702980, 0.48158251], and the matrix round-trip maximum error is 2.384185791015625e-7.

The exported native locator record is muzzle with parent RightForeArm, position [-0.0883713365, 0.0611913800, 0.8283938766] in the export coordinate ordering, and quaternion [-0.1947786808, -0.8470298648, -0.1126058325, 0.4815824032].

The attack frame-145 inspect request was b9869e26fcd741029e603ee63d5173c8; it reports the locator parent contract and world translation [-0.7474380732, -0.0143082142, 5.0703063011].

The support frame-50 inspect request was 1beb8195d1dd404ebf220e0a6e7304af; it reports the locator parent contract and world translation [-0.1554826498, -0.2460858226, 4.9529342651].

The geometric muzzle-cap evidence measured against the prior actual-byte support and laser reimports places the locator in the existing cyan emitter region; measured cap lengths were approximately 0.0305663 in laser attack and 0.0315234 in support attack.

The cap-region inspection is geometric corroboration only; the runtime point is accepted because the adapter-authored locator itself survived export and actual-byte reimport with its RightForeArm bone parent.

Every closure reimport below reports muzzle parented to io_pdx_rig/RightForeArm, proving the supported locator through the actual exported bytes rather than through an inferred cap point.

## Seven genuine provider actions and actual-byte reimports

Every action uses the imported provider action io_pdx_rigAction at 30 FPS and retains substantive skeletal motion; Blender performed only adapter import, bounded grounding/cleanup already recorded in the provider evidence, export, and validation.

| Role | Provider action and task | Frames and semantic evidence | Closure reimport request | Proof SHA-256 | Validation SHA-256 |
| --- | --- | --- | --- | --- | --- |
| idle | Action 0 Idle, task 01a03dd1-23a5-7728-9c09-f09683d64ffe | 1-121; breathing/body motion and loop candidate | 6826e4a8083c4e9e84fd0a0b0480c0c1 | 0FD5BDE73C2290FF0239DB3BD818AA6FCF38CAA2F812B471F79E86504A638272 | D80883DD0EBD517778A8109BF03417318B8F488BC9157DD94942C6AA2AA0493F |
| move | Action 692 walking_2_inplace, task 01a03dd1-28ea-7ba5-b6cc-dde26e5b2d01 | 1-37; distinct in-place walk with grounded contacts | 350b541925f6434cbd7c958d5b245a6b | 7DC06E087F64A312DFC4EC626ED6178AC752889047049D088A3CF36C686949F4 | 85D7CE3BB53D40C24DA5B4ABC7C1AC62F66193F376C6F81AB4B3E5E2478B4D5F |
| laser_attack | Action 223 Draw_and_Shoot_from_Back_1, task 01a03dd1-2d74-70b2-a151-e8d98c82e4de | 1-236; draw, aim, discharge at 145, recoil, and recovery | b7bd60837643424baea5982f30c545a4 | 24C8E2886EED90E99549C398D878C0EBCB652737F6C725A7C42C4E91C56E80A2 | FFF049C2B2202F8748EBF720C8E471BC800C6C8A0FF8018167D55FC3840DC59C |
| defend | Action 89 Combat_Stance, task 01a03dd1-31cc-7729-9612-26eb8f7d44c3 | 1-51; genuine non-firing combat stance | 154102d143c24ce6ab9eb9437a2db496 | DEDC813B8F8949CA9974183F898FBACB973DEA2432C559330C6F7A021957A0CB | 69506165519705D6497D5640CB80D57F0689E19E06636A182B0B77A8CF8211D7 |
| support_attack | Action 234 Walk_Forward_While_Shooting, task 01a03dd1-35e5-7f37-a601-70982bdf5f74 | 1-99; advancing fire, aim, recoil, discharge at 50 | 87995412e3524170a66b907f6d2ebc28 | 8EF64FC5647917649CCB8DB8167743D8EBD53C269FA4C44B3216492EF53E9C92 | E052C477C20380158C860E316FF3C9DB10C4CB41B9304FF20BD13D57B33F3CA1 |
| retreat | Action 685 Walk_Backward_with_Gun_inplace, task 01a03dd1-3a02-7f38-8f3c-0236be3dc57e | 1-31; distinct backward in-place motion with contacts | a589625916fb4c488f2c89b187bea680 | 3A433FB5709DDAF947B9D445E82AB810815E68BD3BF8AFC8673E97938C05864A | EE2835CC08750A58A41558E6EB5E2A343A441E7EDCA599473CA6803A0A5EB248 |
| death | Action 183 Shot_and_Fall_Backward, task 01a03dd1-3dd9-772c-b0cd-9f7dc4de1fe4 | 1-106; hit reaction, articulated collapse, impact near 80, and settling | 44cf33579a0749e483f3970a040d92db | 32D2B156631DA7F94E76E32B3ECA08DB01F440B6C46D8AED787EE3B1A7AD3364 | 28C1E2E63DDCD6622E4EE42FB6744ED8A676B78C9D559296D44A1803CBCEBD94 |

Each seven-action validation contains 59,999 triangles, 179,997 split vertices, 24 bones, zero degenerate faces, zero non-manifold edges, zero zero-length normals, and the muzzle locator on io_pdx_rig/RightForeArm.

The action sample frames are idle 1,31,61,91,121; move 1,10,19,28,37; laser attack 1,60,118,177,236; defend 1,14,26,38,51; support attack 1,26,50,74,99; retreat 1,8,16,24,31; and death 1,27,54,80,106.

The death frame-80 validation reports ground contact approximately -4.53e-06, which is within the adapter contact tolerance and is accompanied by the collapse/impact preview frames.

The validation JSON files are validation/reimport_alien_locator_closure_<role>_20260904.json, and their exact checksums are recorded in the artifact checksum section below.

## Runtime entity, effects, and action wiring

gfx/entities/alien_infantry.gfx registers alien_infantry_mesh, PdxMeshAdvanced, the three runtime maps, and seven distinct animation identifiers: idle, move, attack, defend, support_attack, retreat, and death.

gfx/models/units/alien_infantry/animation_alien_infantry.asset maps those seven identifiers to the seven unchanged runtime .anim files.

The runtime binary manifest is gfx/models/units/alien_infantry/alien_infantry.mesh SHA-256 A8740E95C5F12D63D656B58891A52E1F059EDA2CDBF55DB521968D3932F906B4; alien_infantry_idle.anim D6936AE996DBE998DBEE0633B4DCAC346B6C5D974FC643ACA62AAC73719CB2EF; alien_infantry_move.anim 727BCA51B68EEA445198C1029331FF06F15F69215358ABC9CC29A4064096217F; alien_infantry_laser_attack.anim 288209BC4B9CBB3D19A629C2277DF7816CDF33B475EA68BF0D368F7C2E2150F0; alien_infantry_defend.anim F07A8BC46D68F72DD622014CE31BA9420A3CC1FF419BF3690D44D5F42E9E3A73; alien_infantry_support_attack.anim DADC3823EA4C2FE5F21F10DAE310F52D54E5379A124C01CDEE3AA954F4EE3061; alien_infantry_retreat.anim DB9E72F782A19C84A7C4C8CF429654D0BAAAC59A7999B381CA9267DD598BD2DC; and alien_infantry_death.anim D8D26A8B7A6F01ADCB64103885171C837DB36CB7BBB6A6A15EB6C2D66F15D7A0.

gfx/entities/alien_infantry.asset registers alien_infantry_entity at scale 0.8 and preserves its seven named states plus snow and desert clones.

The attack state binds node = muzzle, particle = alien_laser_muzzle_particle, keep_particle = yes, light = alien_laser_muzzle_flash, and sourced sound alien_infantry_laser_fire at frame 145 / 4.8000 seconds.

The support attack state binds the same locator, particle, light, and sourced laser sound at frame 50 / 1.6333 seconds.

The death state binds sourced alien_infantry_death at onset and sourced alien_infantry_impact at frame 80 / 2.6333 seconds.

The move state uses sourced movement events at 0.0 and 0.6333 seconds, and retreat uses movement events at 0.0 and 0.5 seconds, matching the provider contact phase crosswalk.

The idle state uses the sourced idle one-shot on state entry and does not assume an unverified loop seam.

The current entity intentionally exposes the accepted seven states only; no training or wounded alias action was invented or silently substituted.

gfx/entities/alien_infantry_particles.gfx registers alien_laser_muzzle_particle, gfx/particles/alien_infantry/alien_laser_muzzle.asset supplies its cyan glow/spark file, and gfx/entities/alien_infantry_lights.asset registers the cyan alien_laser_muzzle_flash.

## Sourced audio package and synchronization

The complete six-entry audio provenance ledger is evidence/audio/provenance/audio_sources.json with SHA-256 4D3987D6FA360CA8BA4CB06499D03267C8BAFAB26B5AE79739EA419A6430B9FD.

The existing sourced roles remain laser fire from bart's CC0 Space Laser, movement from GboxMikeFozzy's CC0 footstep, idle from Ogrebane's CC0 sci-fi vehicle sound, and death from Julie Damsgaard/Spring Enterprises' CC0 death sound, with their immutable originals and derived hashes recorded in the ledger.

| Role | Source page and direct download | Preserved original and SHA-256 | Derived game-ready candidate and SHA-256 | Synchronization |
| --- | --- | --- | --- | --- |
| laser fire | https://opengameart.org/content/space-laser; https://opengameart.org/sites/default/files/space%20laser.wav | evidence/audio/original/space_laser.wav; 3A26ECAB8F36DCA14A91519657E60351566A268D28A2EC4F933B0F9718A7258D | evidence/audio/derived/alien_infantry_laser_fire.wav; 4E9552C0D023A34BBE816DAD3443E7C4C0C889720C5F5735871F2D7D7682C770 | laser attack frame 145 / 4.8000 s and support attack frame 50 / 1.6333 s |
| movement | https://opengameart.org/content/footsteps-0; https://opengameart.org/sites/default/files/01-footstep_0.ogg | evidence/audio/original/footstep_01.ogg; 33C9BEF5E8AEB1069455699A34A0C5E1EF1787FD3F61594B0859D7E6BB9F9DEC | evidence/audio/derived/alien_infantry_move.wav; E0B36F9B38769ADD16F2569189B7B013749D6F014C37CDB146CD61B060A6A99E | move frames 1 and 19; retreat frames 1 and 16 |
| idle | https://opengameart.org/content/sci-fi-vehicle-sound; https://opengameart.org/sites/default/files/sci-fi%201_2.wav | evidence/audio/original/sci_fi_idle.wav; 46AB090FAE668CD83D613019EBC42F8F24B4C511572F4EAC024AD5006680E350 | evidence/audio/derived/alien_infantry_idle.wav; B0234598B2DC11635A8713C076A0F6C7E697F29FCA21813EA68922AD38D91C7A | one-shot on idle state entry; no unverified loop seam |
| death | https://opengameart.org/content/various-sound-effects-0; https://opengameart.org/sites/default/files/snd_death1.wav | evidence/audio/original/snd_death1.wav; 9216E8A1E252765392CB30637489F8E58831280B1139FA5E2E916B79E375C916 | evidence/audio/derived/alien_infantry_death.wav; AFFCE4695B4B493BD2611E591EFA39931BBFAE19E0079D9C77DA5B71D201263B | death onset frame 1 |

The newly preserved selection candidate is bart's CC0 Interface beeps pack from https://opengameart.org/content/interface-beeps and https://opengameart.org/sites/default/files/beeps.zip; the selected original is evidence/audio/original/source_search_20260905/bart_interface_beeps_cc0/Beeps/beep-03.wav with SHA-256 372CB6E8B6E58ABEA2C702540E24EFE189D17964C6C95B298F2DD4AB39441A28.

Its mechanical derived evidence is evidence/audio/derived/alien_infantry_selection.wav with SHA-256 890A08637B3FB4720607CDCA288133537A0CFED4A412AE32EEBB986ED6B90BE7.

The selection archive is evidence/audio/original/source_search_20260905/bart_interface_beeps_cc0.zip with SHA-256 B814C4B8281196E98E25B0161CE943B7195565B9B1A2626E7A732D91E39C0355.

The selected impact source is Kenney's CC0 Sci-Fi Sounds pack from https://opengameart.org/content/sci-fi-sounds and https://opengameart.org/sites/default/files/sci-fi_sounds.zip; the selected original is evidence/audio/original/source_search_20260905/kenney_sci_fi_sounds_cc0/Audio/impactMetal_000.ogg with SHA-256 956C6612A256AA1A67A2327FFFE2454F6B1D82E4C1C2BE28FD66916335D5B1D6.

Its mechanical derived evidence is evidence/audio/derived/alien_infantry_impact.wav with SHA-256 0CCAFC50E63C847F0285F3820DFD5B5A4FDDFB9C7F09E586FF3CE1B5083FDAE3.

The impact archive is evidence/audio/original/source_search_20260905/kenney_sci_fi_sounds_cc0.zip with SHA-256 119340F351A5098AD814F78719438C0DA355A9CE8A4C8A3AF6A8D48AA3D49E04.

Both new derived files are mechanical transformations only: metadata removal, mono conversion, 44.1 kHz resampling, and signed 16-bit PCM conversion; originals remain preserved.

The runtime impact file is sound/shared_alien_system/alien_infantry/alien_infantry_impact.wav with SHA-256 0CCAFC50E63C847F0285F3820DFD5B5A4FDDFB9C7F09E586FF3CE1B5083FDAE3.

The five runtime sound definitions are in sound/alien_infantry_sound.asset, and sound/chaosx_sound.asset registers alien_infantry_impact alongside the four existing Alien Infantry effects.

Selection/acknowledgement is explicitly blocked from runtime wiring because the installed vanilla TAG_infantry_idle, TAG_infantry_move_out, TAG_infantry_neutral_combat, TAG_infantry_positive_combat, and TAG_infantry_retreat consumers are country/original-tag-wide; replacing them would also change ordinary infantry voices.

No synthesized, generated, placeholder, test-tone, or unlicensed audio is used.

## Counter handoff

The bespoke counter package is already present and was not recreated or overwritten in this closure.

The large counter is gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds, 152x42 with two 76x42 frames, 25,664 bytes, SHA-256 5F982AF84059CB980828E5CBE63489AABB13F04A2AABFBC81B9B01038193FC6A.

The on-map counter is gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds, 60x12 with two 30x12 frames, 3,008 bytes, SHA-256 775980A00D618DCC675BFD12192F53C11ACAD7380D36B008A69FAA432CBDC07B.

interface/alien_infantry_system.gfx maps GFX_group_alien_infantry_icon and GFX_unit_alien_infantry_icon_medium to the large counter, and GFX_unit_alien_infantry_icon_medium_white to the map counter.

The installed vanilla definition is C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx with SHA-256 0D7B62CAF328B3C296EC27AB85318F3CC78CC760B02923538BF5240815963335.

The matching skill-local reference families are .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/ and .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/.

The recorded vanilla palette anchor is RGB 73,106,73, sampled from the decoded installed reference; frame order, alpha behavior, and border treatment are recorded in runtime/counter_handoff.md.

Parent/user live counter display acceptance remains open; no claim of an in-game counter render is made.

## Artifact checksum index

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| blender/checkpoints/v13_firearm_preset_alien_locator_author_20260904.blend | 4,355,541 | 6EFE1DFC67D9CFD13F2C524B8E924389DC39640501A0B58E0BCAB94B0B44E399 |
| export/v13_firearm_preset_locator_closure_20260904/alien_infantry.mesh | 15,122,561 | A8740E95C5F12D63D656B58891A52E1F059EDA2CDBF55DB521968D3932F906B4 |
| export/v13_firearm_preset_locator_closure_20260904/alien_infantry.txt | 53,601,767 | 477FEE2694AC4784E7DBB94D2F50669634ADD40D1C729CD8E3F38BE0F06A9874 |
| blender/checkpoints/reimport_alien_locator_closure_mesh_20260904.blend | 5,031,878 | 4EF9DF1B76EECFD57683914D8A2B598BF54B59E8DC2205D86116B9B7EC49D93E |
| validation/reimport_alien_locator_closure_mesh_20260904.json | 6,214 | 4FFA0F412B4556E149BF70FF1F3BD5DDC091B74C1803B1F440D7FF72FB9B6CDF |
| validation/reimport_alien_locator_closure_laser_attack_20260904.json | 26,884 | FFF049C2B2202F8748EBF720C8E471BC800C6C8A0FF8018167D55FC3840DC59C |
| validation/reimport_alien_locator_closure_support_attack_20260904.json | 26,935 | E052C477C20380158C860E316FF3C9DB10C4CB41B9304FF20BD13D57B33F3CA1 |
| validation/reimport_alien_locator_closure_idle_20260904.json | 26,722 | D80883DD0EBD517778A8109BF03417318B8F488BC9157DD94942C6AA2AA0493F |
| validation/reimport_alien_locator_closure_move_20260904.json | 26,717 | 85D7CE3BB53D40C24DA5B4ABC7C1AC62F66193F376C6F81AB4B3E5E2478B4D5F |
| validation/reimport_alien_locator_closure_defend_20260904.json | 26,807 | 69506165519705D6497D5640CB80D57F0689E19E06636A182B0B77A8CF8211D7 |
| validation/reimport_alien_locator_closure_retreat_20260904.json | 26,773 | EE2835CC08750A58A41558E6EB5E2A343A441E7EDCA599473CA6803A0A5EB248 |
| validation/reimport_alien_locator_closure_death_20260904.json | 26,730 | 28C1E2E63DDCD6622E4EE42FB6744ED8A676B78C9D559296D44A1803CBCEBD94 |
| evidence/audio/provenance/audio_sources.json | 6,806 | 4D3987D6FA360CA8BA4CB06499D03267C8BAFAB26B5AE79739EA419A6430B9FD |
| sound/shared_alien_system/alien_infantry/alien_infantry_impact.wav | 56,076 | 0CCAFC50E63C847F0285F3820DFD5B5A4FDDFB9C7F09E586FF3CE1B5083FDAE3 |
| gfx/entities/alien_infantry.asset | 2,811 | 9574B6EEF01610971265A108CC049EBD858A9EF293C3361FF86E70815B58A622 |
| sound/alien_infantry_sound.asset | 2,192 | 0453A45CBE5DE2CBA1ED89F5EB72E60E7781C4B6A225BA44D3537BF68B6544E1 |
| sound/chaosx_sound.asset | 106,061 | 8B952C2A8EC7D67B56252245FE985917B7130A7A0B57B5976BD289DC02CB95A2 |
| runtime/crosswalk.md | 5,521 | CC981AAD09CAA55CD010CC33A94B1740F0F2A93EE02D22282BB14903F026F9CF |
| runtime/handoff.md | 7,117 | CD6BCFC3ABF08F60C11F18A25B06E3282928B9B7ADA5E923C65522D7262E41CE |
| runtime/sound_handoff.md | 5,279 | E3511A59A814B9DF1C4D85BA6941050646B256AA4A1D83BB98FFAA0E85BDA912 |

The exact runtime mesh and seven runtime animation hashes are listed by Get-FileHash in the current runtime tree and match the provider hashes in the action table.

## Remaining blockers and parent work

The exact remaining hard blocker is per-subunit selection/acknowledgement audio: the installed vanilla consumer is tag-wide and cannot safely be overridden for Alien Infantry without changing ordinary infantry voices.

A distinct special-action sound consumer was not requested or safely identified, so no invented special-action role is wired.

The adapter report's maximum_stream_vertices = 1 anomaly should remain documented; the zero-warning export and successful actual-byte reimports are the stronger gate evidence, but parent review should retain this uncertainty rather than silently calling the parser field a measured ceiling.

The reimport reports list an empty runtime_texture_staging array because the closure export folder intentionally contains the mesh and locator but not copied texture files; runtime map files were preserved and remain byte-identical to the V13 provider maps.

Parent owns final review of the modified entity, GFX, animation, sound, effect, counter, and gameplay consumers and the overall completion claim.

The user owns live in-game validation; this handoff claims no live game result.

No geometry simplification, substitute geometry, weapon replacement, simple motion, semantic action alias, manual final animation, synthetic audio, placeholder audio, or counter reuse was used.
