# Event 016 Paleogenetic Creature runtime closure handoff

Date: 2026-09-05. Owner: `/root/paleogenetic_runtime_final`. Scope: final 3D runtime/artifact closure for the existing reusable `paleogenetic_creature` geometry. No regeneration, geometry substitution, gameplay edit, staging, commit, or live-game claim was made.

## Outcome

The preserved manual-recovery geometry now has a current-lock artifact package with an accepted asymmetric rig, seven distinct substantive skeletal actions, packed PDX materials, exact `.mesh` and `.anim` exports, current adapter reimport proofs, engine-facing byte-matched copies, entity/action registrations, and a parent-reviewed bespoke counter package. The package remains incomplete for sourced sound/effect role wiring and live consumer validation. Those gaps are explicit blockers, not silently replaced with global voices, placeholders, or aliases.

Detailed hash and frame evidence is in `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/validation/current_locked_runtime_audit_20260905.md`.

## Files created or changed in this tranche

Runtime/wiring files created or updated:

- `gfx/entities/paleogenetic_creature.gfx`
- `gfx/entities/paleogenetic_creature.asset`
- `gfx/models/units/paleogenetic_creature/animation_paleogenetic_creature.asset`
- `gfx/models/units/paleogenetic_creature/chaosx_paleogenetic_creature.mesh`
- `gfx/models/units/paleogenetic_creature/paleogenetic_creature_{idle,move,attack,defend,support_attack,retreat,death}.anim`
- `gfx/models/units/paleogenetic_creature/paleogenetic_creature_{diffuse,spec,normal}.dds`

Artifact evidence and reconciliation files:

- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/validation/current_locked_runtime_audit_20260905.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/runtime/crosswalk.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/runtime/handoff.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/counter_handoff.md`
- `docs/assets/chaos_redux_3d_model_pilots/models_3d/paleogenetic_creature/manifest.md`
- this handoff

The accepted counter DDS and `interface/016_brilliant_scientist_generic_counters.gfx` were produced and parent-reviewed in the separate `016_final_generic_counter_completion_2026-09-01.md` handoff; they were inspected and documented here but not rewritten in this tranche.

## Geometry-preserving checkpoint and calibration

The immutable accepted source checkpoint is `blender/checkpoints/manual_recovery_2026_08_27.blend`, SHA-256 `C61432E2B27D7BAFADD57C28081E8E8FE48DAF6396ECF7E8AD1FDF46471BA0E5`. The material-bound current working checkpoint is `blender/checkpoints/current_locked_2026_09_04_material_working.blend`, SHA-256 `328BB6010887526CFECC2216C466125834339A51271D340A0D09D76F4B240813`.

The preserved `paleogenetic_component_000` is one 29,999-triangle object with 14,928 weighted vertices, dimensions `6.2483215332 x 2.5114848614 x 7.3518238068 m`, one UV layer, zero degenerate faces, zero non-manifold edges, zero zero-length normals, and no negative-scale objects. The diagnostic position weld reports 59 loose boundary edges across 15 closed boundary components. Two attempted caps were rolled back because they introduced non-manifold topology; no geometry was regenerated or substituted.

The accepted `paleogenetic_creature_rig` contains 20 bones: ground root, asymmetric torso, two cranial chains, four independent arm chains, and two leg chains. Weight audit: zero zero-weight vertices, maximum four influences per vertex, and approximately unit weight sums. Source geometry, armature, material identity, and action channels were preserved in the current checkpoint.

Calibration reference is vanilla `gfx/models/units/western_european_infantry.mesh` with `gfx/entities/units_infantry.asset#infantry_rifle_entity`. Vanilla source height is `7.3518242835 m`, entity scale `0.8`, effective runtime height `5.8814594268 m`, forward `-Y`, up `+Z`, ground contact `0.0084189996 m`. Creature source height is `7.3518238068 m`; provider-to-Blender normalization factor is `3.8693812018`; entity scale is `1.35`; effective runtime height is `9.9249627827 m`; effective-height ratio is `1.6875`. The mesh export is unit-scaled and the entity applies the one runtime scale.

## Provider lineage, source provenance, and cost

The existing source lineage was preserved. Source is [Mutant Cook](https://opengameart.org/content/mutant-cook) by Gman2099 on OpenGameArt.org, stated CC0, retrieved 2026-08-27. Immutable `refs/source/untouched.png` SHA-256 is `2B1F9A01475217BF6925065703FB682822049B8D92F78AC0CD51FA48CDBD0176`; the single provider input `refs/original/meshy_input.png` SHA-256 is `29091392E7C875AF138DDEA1BE3C7B5A69BF786FB1E2C15609050CB5EDA2DCD5`. The exact native ImageGen prompt and source-to-refinement comparison are in `refs/original/input_manifest.json`; explicit parent authorization is dated 2026-08-27. Two native-alpha attempts failed with opaque checkerboards, so the documented `rembg` fallback retained the complete silhouette with transparent corners and no cast shadow or halo. Source and refined images remain non-shipping evidence.

Meshy used exact model `meshy-7`, generation task `01a0427d-0a5f-746f-8270-f64b4ba409c1`, consumed 30 credits. The rejected generic rig task was `01a04285-34b0-7d0f-b256-e2c3f0048d67`, consumed 5 credits, and produced an anatomically incompatible standard humanoid with a large sphere. It is not used by this artifact. No paid provider call was made in this tranche; no regeneration or provider recovery was attempted. The historic observed balance was 13 credits after the rejected rig.

The accepted rig/action recovery is the existing user-authorized manual recovery of the preserved geometry, permitted by the closure contract. Actions are promoted only where they show genuine multi-frame skeletal channels and distinct byte hashes; local transform-only aliases are not promoted.

## Action export and reimport evidence

Root policy is in-place at 24 FPS. The current material checkpoint was exported via locked `chaosx_blender_hoi4` 1.10.21 and reimported through the same adapter. Each output uses the 20-bone rig and has no exporter warnings.

| Role | Export `.anim` | Bytes | SHA-256 | Current-lock reimport proof |
| --- | --- | ---: | --- | --- |
| `idle` | `export/current_locked_2026_09_04_material/anim/paleogenetic_creature_idle.anim` | 25,533 | `A911DC3D1BB3E828C4D3636C10751184EBEAEACCFF76D053230C5F09ADE039E8` | `blender/checkpoints/reimport_paleogenetic_idle_20260904.blend`, SHA `CBF8718C7D75222CCA5880BCCB78EC98948C25C03C356D671755FFD0A6B6CDE2`, request `2d0f2f2efb6d4a38a628644441c1ad74` |
| `move` | `export/current_locked_2026_09_04_material/anim/paleogenetic_creature_move.anim` | 26,908 | `492A31119135C028994A3BB52FEC9A6AB076163E63EE82C5A5AFFB230FFA5549` | `blender/checkpoints/reimport_paleogenetic_move_20260904.blend`, SHA `CD9AA2D8948A511549161247ADB87F93349DCD4934D02A704676DB94BFD2FF1F`, request `b7a8b2d27c2c4b48a554876fde98bf63` |
| `attack` | `export/current_locked_2026_09_04_material/anim/paleogenetic_creature_attack.anim` | 25,533 | `BBB9DC684E923EC23EDD1C3FE30070F8EAD30FED2AF912270D89AA5950F36848` | `blender/checkpoints/reimport_paleogenetic_attack_20260904.blend`, SHA `E76E5D1AC87FF70F2E5470D923B5CF9227A9A1CFB3B7E1CA8490B139BDBB4406`, request `adbd265b5ab64338ac84e1dfa36c0023` |
| `defend` | `export/current_locked_2026_09_04_material/anim/paleogenetic_creature_defend.anim` | 22,980 | `78200CB2AAB4514DEF424A0B6DDEE4540C10614DDE8F2E4076A9EBC9A45E2026` | `blender/checkpoints/reimport_paleogenetic_defend_20260904.blend`, SHA `E06101ACDAE9142FD9D029CADA74892CE5F18B7430606F3D1E9E68BF5898CFD7`, request `28d5148fe8b645a5aefd1f0c948368a9` |
| `support_attack` | `export/current_locked_2026_09_04_material/anim/paleogenetic_creature_support_attack.anim` | 19,725 | `8C4C212543E936CA63AF926FB808C87713C405787A6B60AEDA6EAD73E67E1A26` | `blender/checkpoints/reimport_paleogenetic_support_attack_20260904.blend`, SHA `1E96CE665898B3E2CCBE182C2A9101FCD36F586D8A8ACA357B9F31D0A7ED050E`, request `d404f70688e440f2bb797f5b9c9d5f34` |
| `retreat` | `export/current_locked_2026_09_04_material/anim/paleogenetic_creature_retreat.anim` | 26,908 | `123C6AA138495085B3655DE614EA6B98E3F5871A84A38EFB40BEE25C95244C30` | repeat `blender/checkpoints/reimport_paleogenetic_retreat_20260905.blend`, SHA `48AFC4E4DBE31D1FD9CFCBC2DA1C0A41B0359F5162D71B7613DB5DA040C7A3C5`, request `168cb46cfc4c432093d9aa30628f481c` |
| `death` | `export/current_locked_2026_09_04_material/anim/paleogenetic_creature_death.anim` | 33,192 | `58CAF87D9DA6CA743AEEA0A59DAC9A2A140B8838B7CEFC2542F53F1E829D0C12` | repeat `blender/checkpoints/reimport_paleogenetic_death_20260905.blend`, SHA `35A430C73D267331D247CED43A27DA7253FA5A7FABEB0B20440CB87733131ADE`, request `eac54da81885470d87a240ea6ab53260` |

The export request ids for idle/move/attack/defend/support_attack/retreat/death were respectively `22949e1622f74809b9772e0f8ef81b18`, `5b5e3ae63cc4411ab49f1b484ccffdd5`, `70df3a86f296481ab9c1916aff2d5967`, `2d331dcdb9f64f2c92406c5905b6036a`, `3a03be603f91439a901942646bda748f`, `c7bbd6df559544c4a757da38300abfee`, and `51b14367a5924927ae2a8244bbaa8423`.

Source-immutability action-channel inventories used the current working checkpoint SHA and returned request ids idle `cab0a85a0b404b8fa107297d9d49b6f8`, move `f20356fa660d46ac9be00890ef666f23`, attack `b4823f208abf4f14897e101939e9610f`, defend `aa8869517e55471296399b38c85385da`, support_attack `ec7c9df6fdfd492ebf46d337cc9edc08`, retreat `6963692f16e1481997840ca850eb2775`, and death `6d912a3edfb743d0aeada78ac6022af5`. Every inventory reports 63 keyed channels, unchanged action data/rotation modes, and immutable source. The adapter's native curve hashes are retained in the request logs and are separate from the binary `.anim` hashes.

Reimport evidence includes frames 1, 13, 25, 37, and 49 in front, left, and three-quarter views. Death decreases from `7.3518238068 m` at frame 1 to `4.0691556931 m` at frame 49 with changing XY bounds, proving collapse/settling. Move, attack, defend, support_attack, and retreat also have changing sampled bounds and poses. `charge` and `roar` are not promoted because they are byte-identical (`0BC3F0AAB02404FE2201647ABA64BED7915649B48F109A97A12443CABF61A21B`); `wounded` is not promoted because it is byte-identical to `defend`. No semantic alias is wired.

## Mesh, materials, and runtime synchronization

The exact mesh export is `export/current_locked_2026_09_04_material/chaosx_paleogenetic_creature.mesh`, 2,971,499 bytes, SHA-256 `050C0B461050D86203C80A08C8E84C942BDB518B187BD59E7AD1BEBE7E0ECEF7`, adapter request `48e238dadb4c4be58a117d5b53eded27`. The export report records one selected geometry object, 29,999 triangles, 14,928 vertices, unit world scales, zero non-manifold/degenerate/negative-scale errors, and no warnings.

The runtime maps are 1024x1024 uncompressed one-mip DDS files, each 4,194,432 bytes: diffuse SHA-256 `5BDE97E313629B70E64693D8B937D978B8688E1085265BFC9514EACC5C07AEBC`, specular SHA-256 `79B1E7CB9E3FB5B4EAFB8FD27D6F0F80B277357B0A297211EC7658078D54E933`, and normal SHA-256 `33FD0F1D59DEED6518E6837AE61F67BC425A26C020CF9D8EB3928F88AD3F0C78`. The provider maps are preserved, and PDX packed companions are recorded in `blender/reports/pdx_material_pack.json` and `pdx_normal_pack.json`; raw roughness is not used as specular.

Byte comparison confirms the engine-facing files under `gfx/models/units/paleogenetic_creature/` match the export mesh, all seven required actions, and all three runtime DDS maps exactly. Destination SHA-256 values are mesh `050C0B461050D86203C80A08C8E84C942BDB518B187BD59E7AD1BEBE7E0ECEF7`, idle `A911DC3D1BB3E828C4D3636C10751184EBEAEACCFF76D053230C5F09ADE039E8`, move `492A31119135C028994A3BB52FEC9A6AB076163E63EE82C5A5AFFB230FFA5549`, attack `BBB9DC684E923EC23EDD1C3FE30070F8EAD30FED2AF912270D89AA5950F36848`, defend `78200CB2AAB4514DEF424A0B6DDEE4540C10614DDE8F2E4076A9EBC9A45E2026`, support_attack `8C4C212543E936CA63AF926FB808C87713C405787A6B60AEDA6EAD73E67E1A26`, retreat `123C6AA138495085B3655DE614EA6B98E3F5871A84A38EFB40BEE25C95244C30`, death `58CAF87D9DA6CA743AEEA0A59DAC9A2A140B8838B7CEFC2542F53F1E829D0C12`, diffuse `5BDE97E313629B70E64693D8B937D978B8688E1085265BFC9514EACC5C07AEBC`, specular `79B1E7CB9E3FB5B4EAFB8FD27D6F0F80B277357B0A297211EC7658078D54E933`, and normal `33FD0F1D59DEED6518E6837AE61F67BC425A26C020CF9D8EB3928F88AD3F0C78`. The PDX `.gfx` meshsettings bind the three custom map names. The `.asset` action registrations bind the seven action files one-to-one. The entity uses `chaosx_paleogenetic_creature_mesh`, exposes states idle/move/attack/defend/support_attack/retreat/death/training, and has `scale = 1.35`.

The machine-readable byte ledger is `validation/current_locked_byte_manifest_20260905.json`, SHA-256 `A02075C2F86D205EAE9CBEB07FE5C39165957A8F923140E14FC5C86D2C2984A0`, 5,898 bytes. It records the exact export/runtime/reimport lineage and the three reimport texture-alias hashes.

The existing consumer is `common/units/016_brilliant_scientist_project_forces.txt#paleogenetic_creature` with `sprite = paleogenetic_creature`. The runtime file therefore exposes both `chaosx_paleogenetic_creature_entity` and a conventional `paleogenetic_creature_entity` clone. No `common/units` or other gameplay file was edited.

## Counters

The accepted bespoke counter package is `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_generic_counter_completion_2026-09-01.md`, status `parent_reviewed`. Exact consumers are `GFX_unit_paleogenetic_creature_icon_medium` (large) and `GFX_unit_paleogenetic_creature_icon_medium_white` (on-map). The large strip is 152x42, 25,664 bytes, SHA-256 `3D5F51CACCAF7F7CDC39266317AB457ADDE4199C7CFDC1E5E18583F7846927CC`; the on-map strip is 60x12, 3,008 bytes, SHA-256 `D8FF99C23ECFC9F706849D29672A1BBDB0ED1FA8D2EA4CF503760CA1EDAEBD46`. Both use two frames, transparent unused canvas, and the inspected vanilla-green/pale-neutral treatment.

Counter source master hashes are large `35670A20E59DA0B9A52D31CE8C6861138C6C453672B76994BA00753BC7238845` and map `A4E9A21E1AAB87C1EE59F331A0ACEF0F1AC40A4B9ADE56536AFE03821ABFC0A3`; processed hashes are large `8667C9E6C8573B0FDC88305D59CA1294C5C60526F26EEEAAF8BA7C1D1D3D2FB8` and map `887346825580446B1ADB47AD6E69C627D3B0E38F7575BEA6B11BAB26BF9C5F1B`. Native-size contact sheet SHA-256 is `9BDF3B7375711496AA231251D53C87C8E763FAC61E46D8E10936012FC68CD455`; strict DDS round-trip SHA-256 is `1BD8BBC0D0F7010BE9AF62FDD7538650AB2AB37F33E5026AD4EFEE94BC124F94`. The parent-owned GFX registrations are in `interface/016_brilliant_scientist_generic_counters.gfx`.

## Sourced audio and effects

The source-only sound package is `audio/originals/monster_sfx_pack_2.zip`, SHA-256 `8D9831E5596446EBAFB8E6A958E757F07CBD385F9E417B4D9704D63A05A2CD63`, from [Monster Sound Effects 2](https://opengameart.org/content/monster-sound-effects-2) by Ogrebane, OpenGameArt.org, CC0, retrieved 2026-08-27. Seventeen original 44.1 kHz stereo 24-bit PCM WAVs are preserved with per-file hashes and durations in `audio/sound_handoff.md`.

Final roles `selection_idle_ambient`, `move`, `attack_contact_or_roar`, `impact`, `special`, `retreat`, and `death` remain blocked. The archive supplies sequential filenames without semantic file metadata, this environment has no auditory approval pass, and exact animation-frame sync cannot be claimed until the role audition and consumer proof occur. No derived game-ready audio, placeholder, generated sound, or global infantry voice replacement was created.

All current reimports report `locators: []`. The preserved creature contains no separate weapon/projectile component, so no muzzle or firearm particle is declared. Identity-matched attack/impact/death effects remain parent review work pending an approved effect consumer and definition. No fake or generic effect is wired.

## Dependency and route evidence

The dependency lock is `.tools/3d_pipeline/config/dependencies.lock.json`, SHA-256 `B68663B74AA51CD3D191AA98C0EB0BD2E7C3612E238B87D7867C923093C1EA92`; the Meshy schema lock is `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`, SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; the adapter config is `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, SHA-256 `C68298F02A04084F9A0EF48196BE7AE4806EE746D9C7A290A3C27F3D202EA6FC`.

The pinned provider package is `@meshy-ai/meshy-mcp-server` 0.4.0, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, SDK 1.29.0, git `e12cbd7078db388152f6e839abdbe09ba01f3f32`, exact model `meshy-7`. The verified Blender route is `chaosx_blender_hoi4` 1.10.21. Health request `2f6099cc2b7149a3b4bef6fca6754d87` reported Blender 5.1.2 build `ec6e62d40fa9`, loaded `io_pdx_mesh` 0.91.0, and active operators. Installed extension manifest is `C:/Users/klimp/AppData/Roaming/Blender Foundation/Blender/5.1/extensions/user_default/io_pdx_mesh/blender_manifest.toml`, SHA-256 `C6865CEB3CE323BD54255BB37FF860E03607BD2AABED4057E9DCBE04C29682EC`; lock archive SHA-256 is `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.

The mandated separate probe of `127.0.0.1:9876` was `NOT_LISTENING`; the lock-selected hidden Blender startup command was attempted and remained not listening. Adapter health, inspection, export, and reimport calls succeeded through the required repository-owned route. The standalone socket gap is retained as a limitation, not replaced with unrestricted Blender.

## Validation boundary and parent work

Meaningful validation completed: current adapter geometry/rig/weight inspection, multi-view action previews, locked `.mesh` export, seven `.anim` exports, seven actual-byte reimports, runtime texture staging, exact source/destination hash comparison, PDX material pack reports, vanilla scale calibration, installed vanilla counter inspection, accepted bespoke counter round-trip inspection, and source/audio provenance review. HOI4 was not launched and no live consumer validation is claimed.

Remaining parent work is limited and explicit: audit the existing subunit consumer against the conventional entity alias, audition the licensed WAV originals, prove the exact selection/movement/attack/impact/special/death sound consumers, choose roles and synchronize them to action phases, decide whether a non-weapon identity-matched effect is required, and perform live HOI4 validation. The 59-edge boundary diagnostic and absent standalone socket bridge remain documented. No other simplification, omission, alias, regeneration, or substitution was made.

No files were staged or committed.
