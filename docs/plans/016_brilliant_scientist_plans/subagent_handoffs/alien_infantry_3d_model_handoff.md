# Alien infantry 3D model production handoff

Status: **blocked — V7 neutral model/rig passed, but all three audited official Meshy firearm actions catastrophically deformed the integrated rifle topology**. No `.mesh`, `.anim`, export/reimport proof, firing crosswalk, or runtime wiring is claimed.

## Source and exact-one input

- User-supplied immutable source: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/refs/source/user_supplied_alien_reference.png`, SHA-256 `17FEF636D5ADA350D92B1F432B58459B135F038BEB97CFEDA201CCF314BF984F`.
- User-requested ImageGen preparation and sole Meshy input: `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/refs/original/meshy_input.png`, 1024x1536, SHA-256 `AB15C53A9BF317F5BD0BBD8E9A881F85E4F9EDFE4B5A38FFE4472BBDD33D604B`.
- The input contains the same classic bald olive-green alien, glossy black eyes, charcoal retro uniform and boots, and the supplied retro ray gun in a two-hand low-ready grip. Meshy received exactly this one image. No multi-view, auxiliary input, A-pose, or T-pose was used.

## Dependencies and calibration

- Environment verifier completed with zero findings.
- Official `@meshy-ai/meshy-mcp-server` 0.4.0, repository compatibility `meshy-7-v4`, explicit live `meshy-7` identifier.
- Blender 5.1.2; repository adapter `chaosx_blender_hoi4` 1.10.3; io_pdx_mesh 0.91.0, locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
- Dependency lock SHA-256 `01CAE764172374943B0718048B136C029E3CEBDBFCFA737C24AFC75DF7EA08EF`; Meshy schema lock SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`; adapter config SHA-256 `24F865F90077104493EA092C015E140B8519780B400B4AD2CFF748EA7AF91875`.
- Read-only vanilla mesh: installed `gfx/models/units/western_european_infantry.mesh`, staged as `blender/reference/western_european_infantry.mesh`, SHA-256 `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`.
- Entity precedent: installed `gfx/entities/units_infantry.asset#infantry_rifle_entity`. Source height 7.3518242835, entity scale 0.8, effective runtime height 5.8814594268, forward -Y, up +Z. Entity scale is applied exactly once.

## Provider lineage, rejection, and credits

The first new user-input lineage is rejected and retained only as `provider/rejections/generation_user_supplied_v1.md`:

- Generation `01a033ce-2052-7782-8c56-a3bb163fe4f1`, 30 credits.
- Remesh `01a033d8-2724-7127-8d6f-9794d65186e0`, 5 credits.
- Rig `01a033e1-c9c3-799f-b824-3bf849429e19`, 5 credits.
- Action 98 `Run_and_Shoot`, task `01a033f1-0c58-7ed4-a426-c7f66435b3fc`, 3 credits, rejected at frame 0 for catastrophic arm/body stretch and destroyed gun silhouette.
- Action 690 `Walk_Forward_While_Shooting_inplace`, task `01a033fa-16c8-7a6c-b738-6b10f7b31e2b`, 3 credits, rejected at frame 0 for the same deformation.
- Large v1 provider models, Blender checkpoints, previews, and logs were deleted after the minimal record was written. No Blender weapon repair, attachment, or replacement animation was attempted.

The historical v2 geometry lineage passed neutral geometry review but is not a selected runtime lineage:

- Balance immediately before generation: 85.
- Meshy 7 image-to-3D task `01a03404-752c-7d05-be14-b204c817f9dd`, succeeded after 178 seconds / 11 polls, 30 credits.
- Historical GLB SHA-256 `DD96097BFAB051A59D08E918B0EF741E4BA400FB0784225B073CA96614BFC050` and FBX SHA-256 `69514019CED0D60EDAB6C6C70F96D79DED994E6E5CCB0D234CFD6D6CDEBBD6AA`.
- Historical PBR map hashes: base color `13C75C37A732A2FDCC3E8C970F6C60917636754CB9F5D275198A4E096DA229ED`; metallic `5096AF6F13E54FA3DD4D68C6608823F93C99F83296C6BAC97C44DB7ABC7AC920`; normal `3F5101F06915E5A58B0C718BB6A970EDEFC353C36FCD04305FFF3FD38037FF85`; roughness `28F5F5A2519787CDB390E60F2113698FB46C96B142BB8AFB088C1CC158C1098D`.
- Total spend owned by this run: 76 credits.

The historical probes returned 25 and then 20 credits and blocked continuation. The verified read-only recheck at `2026-08-24T14:15:09Z` returned 1,410 credits. Minimum mandatory remaining spend is 31 credits: remesh 5 + rig 5 + seven distinct actions 21. This excludes retry margin, but the current balance is sufficient. Historical blocker evidence remains at `validation/meshy_balance_blocker_2026-08-24.json`; the current receipt is `validation/meshy_balance_recheck_2026-08-24.json`.

## Accepted v2 geometry/material/scale evidence

Adapter request `d422c421fcfa4b8386555049ef515feb` imported, protected, normalized, repaired, reduced, material-tagged, checkpointed, and rendered the v2 model. Evidence is under `blender/source/alien_infantry_user_v2_provider_source.blend`, `blender/checkpoints/`, `blender/previews/alien_infantry_user_v2_*.png`, and `logs/adapter/d422c421fcfa4b8386555049ef515feb.result.json`.

- Multi-angle visual gate: alien identity, supplied ray gun, continuous muzzle, both-hand low-ready contact, grounded boots, and no overhead/floating weapon mass passed.
- Provider density: 1,629,142 triangles / 844,888 vertices.
- Working QA candidate: exactly 30,000 triangles / 14,986 vertices; triangular; one mesh; zero loose boundary edges, non-manifold edges, degenerate faces, negative-scale objects, or zero-length normals.
- PDX material: `PdxMeshAdvanced`, using immutable provider diffuse, normal, and roughness-source bindings. No synthesized or repainted texture was used.
- Final QA height 7.3527107239; effective runtime height 5.8821685791; delta from calibrated target +0.0007091523.

This checkpoint is not final runtime geometry because it has no accepted provider rig, weights, or actions. No final packed DDS set was created.

## Required actions and firing crosswalk

All roles remain blocked on v2 rig/action production. Reserved policy is 24 FPS, in-place; idle/move/defend/retreat are loops, attacks/death are one-shots.

| Role | Runtime action | Provider action | Required evidence | Discharge/node/effect/light/audio |
|---|---|---|---|---|
| Idle | `alien_infantry_idle` | not submitted | quarter-loop motion, grip/deformation | no discharge; existing `alien_infantry_idle` sound candidate on entry |
| Move | `alien_infantry_move` | not submitted | quarter-loop, feet/ground, two-hand retention | foot-contact sync to existing `alien_infantry_move` sound candidate |
| Laser attack | `alien_infantry_laser_attack` | not submitted | aim, discharge, recoil, recovery | frame/time and muzzle node blocked; parent-owned beam/muzzle particle + light; `alien_infantry_laser_fire` at verified discharge |
| Defend | `alien_infantry_defend` | not submitted | quarter-loop guard motion and grip | non-firing unless the accepted clip visibly discharges |
| Support attack | `alien_infantry_support_attack` | not submitted | independent aim, discharge, recoil, recovery | frame/time and muzzle node blocked; parent-owned beam/muzzle particle + light; `alien_infantry_laser_fire` at verified discharge |
| Retreat | `alien_infantry_retreat` | not submitted | quarter-loop, backward contacts, grip | foot-contact sync to existing movement sound candidate |
| Death | `alien_infantry_death` | not submitted | articulated collapse, impact, terminal settle, gun retained | collapse/impact sync to existing `alien_infantry_death` sound candidate |

No firing discharge frame, time, muzzle locator/node, particle, light, or action-specific audio synchronization may be guessed from the neutral geometry. Parent owns final `.asset`, entity, particle/light, and sound-definition wiring after valid actions exist.

## Sourced audio package

The existing audio package was not replaced. Full URLs, attribution, CC0 terms, transformations, and records are in `evidence/audio/provenance/audio_sources.json` and `runtime/sound_handoff.md`. Existing mono 44.1 kHz signed 16-bit PCM derivatives are:

- Laser: OpenGameArt `Space Laser`, bart, `https://opengameart.org/content/space-laser`; original SHA-256 `3A26ECAB8F36DCA14A91519657E60351566A268D28A2EC4F933B0F9718A7258D`; derived `alien_infantry_laser_fire.wav` SHA-256 `4E9552C0D023A34BBE816DAD3443E7C4C0C889720C5F5735871F2D7D7682C770`.
- Movement: OpenGameArt `Footsteps: 01-footstep`, GboxMikeFozzy, `https://opengameart.org/content/footsteps-0`; original SHA-256 `33C9BEF5E8AEB1069455699A34A0C5E1EF1787FD3F61594B0859D7E6BB9F9DEC`; derived `alien_infantry_move.wav` SHA-256 `E0B36F9B38769ADD16F2569189B7B013749D6F014C37CDB146CD61B060A6A99E`.
- Idle: OpenGameArt `Sci-Fi Vehicle Sound`, Ogrebane, `https://opengameart.org/content/sci-fi-vehicle-sound`; original SHA-256 `46AB090FAE668CD83D613019EBC42F8F24B4C511572F4EAC024AD5006680E350`; derived `alien_infantry_idle.wav` SHA-256 `B0234598B2DC11635A8713C076A0F6C7E697F29FCA21813EA68922AD38D91C7A`.
- Death: OpenGameArt `Various Sound Effects: snd_death1`, Julie Damsgaard / Spring Spring / Spring Enterprises, `https://opengameart.org/content/various-sound-effects-0`; original SHA-256 `9216E8A1E252765392CB30637489F8E58831280B1139FA5E2E916B79E375C916`; derived `alien_infantry_death.wav` SHA-256 `AFFCE4695B4B493BD2611E591EFA39931BBFAE19E0079D9C77DA5B71D201263B`.

Selection and acknowledgement remain intentionally unwired because installed `TAG_infantry_*` consumers are tag-wide and would replace ordinary infantry voices.

## Counter reconciliation

- Registered consumers: `interface/alien_infantry_system.gfx`.
- Large: `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds`, 152x42/two frames, SHA-256 `5F982AF84059CB980828E5CBE63489AABB13F04A2AABFBC81B9B01038193FC6A`.
- On-map: `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds`, 60x12/two frames, SHA-256 `775980A00D618DCC675BFD12192F53C11ACAD7380D36B008A69FAA432CBDC07B`.
- Installed precedent: `interface/subuniticons.gfx`; matching skill-local families `units/land/counters_large/` and `units/land/map_counters/`.
- Counters were inspected/reconciled only; they were not recreated or overwritten. Final live visual review remains parent/user-owned.

## Export/runtime status and parent next steps

No final `.mesh` or `.anim` exists; therefore there are no export hashes, actual-byte parses, io_pdx_mesh reimports, or runtime copies. Proposed identifiers are `alien_infantry_mesh`, `alien_infantry_entity`, `alien_infantry_idle`, `alien_infantry_move`, `alien_infantry_laser_attack`, `alien_infantry_defend`, `alien_infantry_support_attack`, `alien_infantry_retreat`, and `alien_infantry_death`.

To resume without guessing, bring the live balance to at least 31 Meshy credits plus practical retry margin, then continue only from task `01a03404-752c-7d05-be14-b204c817f9dd`: remesh to the provider rig ceiling, inspect retention, rig, inspect neutral weights/contact, test one strongest two-hand firing action, and only after it passes submit six distinct remaining actions. Reject the v2 lineage if the gun deforms. After all action gates pass, complete packed textures, weight/deformation QA, PDX export and actual-byte reimport, discharge/node/audio crosswalk, and parent-owned runtime wiring.

Meaningful validation performed: hard API-key gate; dependency/schema/adapter preflight; exact input hash and exclusivity; provider balance before every paid call; immediate downloads and hashes; multi-angle geometry and neutral-rig review; two distinct firing-action deformation tests; vanilla scale calibration; topology/material reporting; audio and counter reconciliation.

Historical v2 note: those stages were initially skipped because of the then-current credit blocker. The superseding recovery result below records the later V6/V7 paid work and the final provider-capability blocker. No simplification or fallback was accepted.

## Superseding automatic recovery result

The v2 credit-blocker and resume instructions above are historical and superseded. Automatic recovery advanced through V3–V7 while balance and provider capability permitted it. V5 and V6 independently reproduced catastrophic upper-body/weapon stretching under action 690. V7 is the strongest accepted-neutral diagnostic lineage:

- Meshy 7 generation `01a03499-135b-7a19-b5f3-eef4fc9d1515`, 30 credits; GLB SHA-256 `5CF528C917701DEC9634A268EF4B8E6754D11EEC13693B0562A756638CD81757`; FBX SHA-256 `50A626F366DE44D3C05364248E48556411A2410E9999AED47AE9C8F922580EA8`.
- Remesh `01a0349e-d89f-76b4-baca-da8a190aafe5`, 5 credits; GLB `E0EF4D0A7DEC36A2879BAEA4C22E55DFDCED32A000BA168048930C907A396392`; FBX `442C395D7C9F67DEF73F9C65D817153B5EB4F4372E082B099B6867EA671B4465`.
- Rig `01a034a4-700b-7a32-b9a8-ed95969a139a`, 5 credits; GLB `89ABD8EE5114AB5BA79DFF4C7B409202CE0037B168D18DA1EFC018FB267D212B`; FBX `484A267C779E704B84C0C0BF61494767B62580A9CAAC5FBC782B89C7677FB295`. Neutral review passed the 24-bone rig and retained the integrated rifle silhouette and two-hand low-ready pose.

The V7 remesh is 100,456 triangles / 83,611 vertices in the provider-rig artifact. This exceeds the requested final 30,000-triangle budget, but no final reduction/export was attempted because the mandatory action gate failed first. Adapter calibration preserved source height 7.3518247604, entity scale 0.8, and effective runtime height 5.8814598083. Material inspection found `PdxMeshAdvanced` bindings to provider base color, normal, and roughness sources, but the source maps remain 2048/4096 and were not processed into final <=1024 packed DDS textures.

## Official alternate firearm action audit

The official Meshy animation library was inspected after action 690 failed. Two materially different candidates with reduced or different displacement were chosen: action 104 `Side_Shot`, a stationary lateral shot without sustained locomotion, and action 232 `Cowboy_Quick_Draw_Shooting`, a longer draw/aim/fire/recover sequence. Action 98 `Run_and_Shoot` was not repeated because it had already failed a prior lineage and imposed more locomotion.

| Action | Task and cost | 24 FPS range | Evidence frames | Result |
|---|---|---:|---|---|
| 690 `Walk_Forward_While_Shooting_inplace` | `01a034a6-9666-79b9-8929-cc3598191272`, 3 credits | 0–80 | 0/20/40/60/80 | Catastrophic torso/arm/rifle stretch; gun and muzzle lost. |
| 104 `Side_Shot` | `01a034ab-1c04-7c5a-ab0d-00687510cedf`, 3 credits | 0–97 | 0/16/32/48/64/80/97 | Same failure during stationary lateral-shot phases; no coherent trigger/support grip. GLB `596E4D2AD09ABDC42CCA885967F6D5B28DD64DC49F783647800CE16048DAB4E8`; FBX `1D40AA025844AB73450481BE726EF3FA34C4FCC52D05EC48520EF8CFE2237124`. |
| 232 `Cowboy_Quick_Draw_Shooting` | `01a034b5-7230-7789-831b-e2ad3faae058`, 3 credits | 0–176 | 0/22/44/66/88/110/132/154/176 | Same failure across draw, aim, firing, and recovery; no stable muzzle. GLB `F05F1C685603AB0FE6B9EEA038C3DFE927159B27B87FD24D0B479FD19E540F3C`; FBX `F6DB5C2E8464523A5C58EA8F5E48880ACFEA7A2931889A3936CB242DDABE3DE6`. |

Balances recorded for this alternate audit were 559 before action 104, 466 before action 232, and 433 after completion. The account was used concurrently; this audit consumed exactly 6 credits. No duplicate live task was submitted.

This establishes a provider capability blocker for the current integrated-rifle topology: independent generations/rigs V3–V7 and materially distinct shooting clips all fail the same deformation class. The other semantic actions were not purchased after the mandatory firing gate failed. The authoritative compact record is `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/provider/rejections/generation_recovery_v7_firearm_capability.md`.

## Firing crosswalk status

| Runtime action | Provider source | Exact discharge frame/time | Muzzle node | Particle/light consumers | Audio |
|---|---|---|---|---|---|
| `alien_infantry_laser_attack` | none accepted | blocked; all audited clips deform | blocked; no stable verified node/locator | parent-owned `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash`, unwired | sourced `alien_infantry_laser_fire`, unsynchronized |
| `alien_infantry_support_attack` | not purchased after attack gate failure | blocked | blocked | parent-owned `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash`, unwired | sourced `alien_infantry_laser_fire`, unsynchronized |

No discharge frame, time, or muzzle node was guessed. No runtime particle, light, or sound wiring is proven.

## Reusable firearm workflow findings for the 3D skill

The parent or skill maintainer should capture the following reusable workflow after reviewing this evidence:

1. Generate the armed character as one Meshy result and reject geometry before rigging unless the complete firearm silhouette, muzzle, trigger hand, support hand, and stock/fore-end are readable from multiple angles.
2. After remesh, verify that those same regions remain separate and readable. Do not infer future weapon rigidity from a neutral render.
3. After rigging, inspect neutral geometry and weights, but treat this only as a precondition. An accepted-neutral rig does not prove that a large integrated firearm has usable animated weights.
4. Purchase the strongest required firing role first and render start, aim, discharge neighborhood, recoil, and recovery before buying any other semantic role.
5. Reject immediately if any phase stretches the torso into the weapon, loses the muzzle, breaks trigger/support contact, bends the rifle non-rigidly, or cannot show a credible aim–discharge–recoil–recover sequence. Blender must not repair weights, add a weapon bone, attach/parent/constrain the gun, or author replacement motion.
6. Before declaring provider capability failure, audit at least two materially distinct official firearm clips on the best accepted-neutral rig: one reduced-locomotion shot and one different aim/fire/recovery pattern. Record exact official names/IDs, why they are distinct, task IDs, costs, hashes, and full-phase evidence.
7. If the alternate clips fail the same deformation class across independent rigs/generations, stop further semantic spend and mark a provider capability blocker. Retain compact hashes/task IDs/frame evidence and delete heavy failed artifacts only through an approved safe cleanup route.
8. A firing crosswalk is valid only after visual acceptance: record the exact discharge frame/time, a verified stable muzzle node/locator, particle/light consumers, and audio event. Never guess these values from neutral geometry or a deformed clip.

Failure gates learned from V3–V5 and confirmed by V6–V7 are: neutral weapon retention is insufficient; rerigging the same integrated topology does not cure catastrophic animated deformation; repeated action 690 is not diagnostic by itself; and materially different reduced-motion firearm clips are required before a capability conclusion. The accepted firing crosswalk is currently empty because no clip passed.

## Final package state and remaining parent decision

No final `.mesh`, `.anim`, packed <=1024 DDS textures, export hashes, actual-byte reimport reports, or runtime staging candidates exist. Meaningful validation completed includes exact-one-input verification, dependency-lock/schema/adapter checks, multi-angle V7 geometry and neutral-rig review, three full-phase V7 firearm action tests, vanilla scale calibration, and audio/counter reconciliation. Skipped because of the provider capability blocker: the other six semantic actions, final weight/deformation approval, firing synchronization, death-collapse proof, texture packing, PDX export/reimport, runtime synchronization, and in-game validation.

Parent decision is required before any broader route can resume: wait for a Meshy firearm-animation capability change, or obtain explicit user approval for a professional authored firearm-animation source compatible with the existing restrictions. No simplification, Blender repair, alias, or manual/procedural motion fallback was used.

Heavy failed-provider cleanup is complete. After resolved-path verification confined every target to the Event 016 alien workspace, failed provider downloads, transient provider request/response/credit directories, and Blender source/checkpoint directories were deleted. The cleanup reclaimed 2,537,107,276 bytes and retained compact rejection records, task IDs, hashes, reports, and representative preview frames. No accepted runtime candidate was deleted because no lineage passed the mandatory firearm gate.
