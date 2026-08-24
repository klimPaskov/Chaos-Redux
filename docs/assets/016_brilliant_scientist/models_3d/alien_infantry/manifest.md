# Alien infantry 3D package manifest

Status: **blocked — V7 neutral geometry/rig passed, but three distinct official Meshy firearm actions failed catastrophically**.

## Authoritative source and input

- Sole immutable user source: `refs/source/user_supplied_alien_reference.png`, SHA-256 `17FEF636D5ADA350D92B1F432B58459B135F038BEB97CFEDA201CCF314BF984F`.
- Sole exact-one Meshy input: `refs/original/meshy_input.png`, 1024x1536, SHA-256 `AB15C53A9BF317F5BD0BBD8E9A881F85E4F9EDFE4B5A38FFE4472BBDD33D604B`.
- Authorization: the user supplied the source and explicitly requested the faithful ImageGen preparation used as the Meshy input.
- Meshy received exactly that one image. No multi-view, auxiliary image, A-pose, or T-pose input was used.

## Provider lineage and spend

The rejected first lineage is represented only by `provider/rejections/generation_user_supplied_v1.md`. It consumed 46 credits: generation 30, remesh 5, rig 5, action 98 3, and action 690 3. The neutral rig retained the ray gun, but two independent firing actions catastrophically stretched the arms/body and destroyed the gun silhouette, so the complete lineage was rejected and its large artifacts were deleted.

The historical v2 geometry lineage was accepted only for neutral geometry review and was later rejected with the rest of the package because no valid firearm animation could be produced:

- Meshy 7 image-to-3D task `01a03404-752c-7d05-be14-b204c817f9dd`, succeeded, 30 credits.
- Historical GLB SHA-256 `DD96097BFAB051A59D08E918B0EF741E4BA400FB0784225B073CA96614BFC050` and FBX SHA-256 `69514019CED0D60EDAB6C6C70F96D79DED994E6E5CCB0D234CFD6D6CDEBBD6AA`.
- Historical PBR map hashes: base color `13C75C37A732A2FDCC3E8C970F6C60917636754CB9F5D275198A4E096DA229ED`; metallic `5096AF6F13E54FA3DD4D68C6608823F93C99F83296C6BAC97C44DB7ABC7AC920`; normal `3F5101F06915E5A58B0C718BB6A970EDEFC353C36FCD04305FFF3FD38037FF85`; roughness `28F5F5A2519787CDB390E60F2113698FB46C96B142BB8AFB088C1CC158C1098D`.
- Spend through the initial and historical v2 lineages was 76 credits. This is not the package-wide total because later V3 through V7 recovery calls are recorded separately in `history.jsonl` and the compact rejection records; the shared account was also used concurrently, so balance deltas are not treated as an authoritative package total.

## Accepted v2 geometry gate

Adapter request `d422c421fcfa4b8386555049ef515feb` prepared and rendered the v2 source. The front, left, rear, right, three-quarter, top, and underside previews are under `blender/previews/alien_infantry_user_v2_*.png`. The alien identity, supplied retro ray gun, continuous muzzle, two-hand low-ready contact, grounded boots, and absence of an overhead/floating weapon mass passed visual review.

The protected provider source contains 1,629,142 triangles. The working QA candidate is exactly 30,000 triangles / 14,986 vertices, triangular, with zero loose boundary edges, zero non-manifold edges, zero degenerate faces, and no negative-scale objects. It uses `PdxMeshAdvanced` bindings to the immutable provider maps. This is geometry evidence only, not a final weighted/exportable model.

Vanilla calibration used `blender/reference/western_european_infantry.mesh`, SHA-256 `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`: mesh height 7.3518242835, entity scale 0.8, effective runtime height 5.8814594268, forward -Y, up +Z. The v2 QA mesh measured 7.3527107239 high after reduction, for effective runtime height 5.8821685791 and delta +0.0007091523.

## Historical v2 continuation state (superseded by V7 closure below)

The locked live route was rechecked read-only at `2026-08-24T14:15:09Z`. The account balance is 1,410 credits. The minimum remaining mandatory provider route costs 31 credits: remesh 5, rig 5, and seven distinct Meshy actions at 3 each. The route is fundable with retry margin. No paid call was made during this recheck, so no v2 remesh, rig, animation, weight approval, action sampling, firing discharge/node synchronization, death-collapse proof, packed DDS output, `.mesh`, `.anim`, export, or actual-byte reimport proof exists yet.

Reserved runtime identifiers remain `alien_infantry_entity`, `alien_infantry_mesh`, `alien_infantry_idle`, `alien_infantry_move`, `alien_infantry_laser_attack`, `alien_infantry_defend`, `alien_infantry_support_attack`, `alien_infantry_retreat`, and `alien_infantry_death`. Parent owns final entity, particle, light, audio, and gameplay wiring. No in-game completion is claimed.

## Dependencies and companion packages

- Dependency lock SHA-256 `01CAE764172374943B0718048B136C029E3CEBDBFCFA737C24AFC75DF7EA08EF`; Meshy schema lock SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; adapter config SHA-256 `24F865F90077104493EA092C015E140B8519780B400B4AD2CFF748EA7AF91875`.
- Official Meshy MCP 0.4.0 with repository compatibility `meshy-7-v4` and explicit live `meshy-7`; Blender 5.1.2; adapter 1.10.3; io_pdx_mesh 0.91.0 with locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- The CC0 source/provenance package remains under `evidence/audio/`, and the derived PCM WAV files plus sound definitions are installed under `sound/shared_alien_system/alien_infantry/`, `sound/alien_infantry_sound.asset`, and the four package registrations in `sound/chaosx_sound.asset`. Exact entity-event synchronization is blocked until valid actions exist.
- Reusable muzzle particle and light definitions are installed as `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash`; they remain intentionally unbound because no stable muzzle node or discharge timestamp exists.
- Existing counters remain outside this job at `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds`, registered by `interface/alien_infantry_system.gfx`. They were inspected/reconciled but not recreated or overwritten.

## Authoritative recovery closure: V6–V7

The earlier v2 continuation text above is superseded by the completed automatic recovery audit. V6 and V7 were generated from the same immutable exact-one input. V6 passed generation/remesh/neutral-rig review but failed action 690 with catastrophic upper-body and integrated-rifle deformation. V7 likewise passed geometry/remesh/neutral-rig review, then failed action 690 and two materially distinct official-library alternatives: action 104 `Side_Shot` and action 232 `Cowboy_Quick_Draw_Shooting`.

The authoritative V7 lineage is generation `01a03499-135b-7a19-b5f3-eef4fc9d1515`, remesh `01a0349e-d89f-76b4-baca-da8a190aafe5`, and rig `01a034a4-700b-7a32-b9a8-ed95969a139a`. The firearm tasks are action 690 `01a034a6-9666-79b9-8929-cc3598191272`, action 104 `01a034ab-1c04-7c5a-ab0d-00687510cedf`, and action 232 `01a034b5-7230-7789-831b-e2ad3faae058`. Exact hashes, credits, and phase frames are recorded in `provider/rejections/generation_recovery_v7_firearm_capability.md`.

No remaining semantic actions, packed runtime textures, `.mesh`, or `.anim` files were produced after the firing gate failed. No discharge frame/time or muzzle node can be accepted from a deformed clip. The package is blocked on current Meshy firearm-animation capability, not on balance; the final observed shared balance was 433 credits.

After compact task, hash, rejection, report, and representative frame evidence was retained, failed provider downloads, transient provider request/response/credit receipts, and Blender source/checkpoint files were removed from this event workspace. The cleanup reclaimed 2,537,107,276 bytes and left the compact package at approximately 42.2 MiB. No deleted artifact was an accepted runtime candidate.
