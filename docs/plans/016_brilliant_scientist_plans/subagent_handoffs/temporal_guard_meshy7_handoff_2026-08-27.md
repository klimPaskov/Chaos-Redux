# Temporal Guard Meshy 7 handoff — 2026-08-27

## Status

`blocked`

The generic Temporal Guard has actual io_pdx_mesh `.mesh` bytes, eight distinct provider-authored `.anim` files, grounded export checkpoints, and parser/reimport proof for every exported action. The recovery pass produced and relinked the required 1024 PDX diffuse, packed normal, and packed specular DDS textures, re-exported the mesh, and reimported it with staged runtime textures and a five-phase idle action. It also has preserved, licensed sourced-audio originals and mechanically derived WAV candidates for every required sound role. The package remains blocked because the source-art/ImageGen authorization record is incomplete, the remesh/credit lineage is incomplete, dedicated provider-authored `support_attack` and `retreat` actions are absent, and the mandatory bespoke vanilla-green large/on-map counter package could not be produced under the explicit no-ImageGen recovery constraint. Parent-owned runtime wiring has not started.

Package root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/temporal_guard`

Parent consumer: `kruger_temporal_guard`

## Dependency, route, and cost evidence

- Credential gate passed: `MESHY_API_KEY` was present and non-blank; its value was never printed or persisted.
- Official Meshy MCP: `@meshy-ai/meshy-mcp-server` `0.4.0`, git `d8c77d1cb897e345eb41d38b510b8391b1664346`, compatibility revision `meshy-7-v5`; locked generation identifier exactly `meshy-7`.
- Live free balance on 2026-08-27: 140 credits.
- Blender `5.1.2`, build `ec6e62d40fa9`; adapter `chaosx_blender_hoi4` `1.10.14`; bridge `127.0.0.1:9876` listening.
- `io_pdx_mesh` `0.91.0`; locked archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`; installed manifest matched.
- All adapter/config hashes matched `.tools/3d_pipeline/config/dependencies.lock.json`, `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`, and `.tools/3d_pipeline/config/blender_hoi4_adapter.json`.
- No paid provider operation was made in this resumed pass. No balance or provider call was made after the parent directed finalization without further provider work. Locked-rate estimate for prior lineage is 61 credits: generation 30, remesh 5, rig 5, and seven custom animations at 3 each; walking was rig-included. Actual prior consumption is not provable because pre/post balance receipts are absent.

## Source and ImageGen provenance

- Immutable source: `refs/source/untouched.png`, SHA-256 `B704CC7286C3F76DC20A80D9DDEF44EADE350DA535E35B9DA64D02246A03F4DC`.
- Prepared intermediate: `refs/derived/opaque_reframe.png`, SHA-256 `983362547C48CDD919214B63663C902A5235BD28C82AA2F02BFB64AAE6C61D44`.
- Exact single Meshy input: `refs/original/meshy_input.png`, SHA-256 `F3D705EC5C7E8BF23F1BB74B3AE5E2D3DD50669ACC9A1463437319B7FEAF87D4`.
- Visual inspection confirms a modern designed-art source and a substantially re-presented full-body humanoid Temporal Guard input: dark metal armour, bronze trim, cyan temporal conduits, neutral T-pose, and no firearm.
- Blocking missing evidence: source URL/page, title, creator/publisher, stated terms, retrieval date, explicit authorization for the actual artwork, native ImageGen response id and exact prompt, source-to-refinement comparison, parent approval, and explicit non-shipping source declaration. These cannot be reconstructed safely from pixels.

## Meshy lineage

- Meshy 7 generation: `01a0427c-4e13-7b24-a0c4-56b4e1288288`. GLB SHA-256 `9F801F672886316033AD451B160C74D038E94B262D5EEF8EEF1AC6DE32D232A1`; FBX `A1EE7DA81549E40C9D855BC8812D3AE6EC672EECF27FDB81A9C6A91A81A9BA87`.
- Remesh local stage `remesh_01a04281`; full task id/response is missing. GLB SHA-256 `96F5A1198AB67595A3C038F70CF677BB2E0CC40E85AF117F54510B0689934C00`; FBX `32E101B95314FFC0383744BF5629D6D9EF68CE9077360C45A1020250F62C0A4D`.
- Rig: `01a04284-b375-7973-909c-8abd29417e11`. Rigged GLB SHA-256 `D21881DDF96AAE3C2773DFA1EAE849E246D2922AA6E6A96D126668610003C95B`; FBX `0626113F7C28D7E582271157A3281219408540C4B3A960DC410206912B75F840`.

## Geometry, rig, materials, and calibration

- One working mesh: 14,997 vertices, 30,000 triangles, zero degenerates, zero non-manifold edges, 38 loose boundary edges in ten closed small boundary components, no negative scale, one UV layer.
- Rig `Armature.001`, 24 bones. All 14,997 deforming vertices are weighted; weight sums are approximately 1.0; zero zero-weight deforming vertices; 2,297 vertices exceed four influences and remain a performance/deformation review item.
- One `PdxMeshAdvanced` material. The recovery pass relinked `texture_0`, `texture_normal`, and `texture_specular` to `textures/dds/*.dds` through adapter request `93a8a704534048e897d293c75ec80aea`; inspection request `b68cc0ff028a4db086098f6a089faa8e` confirmed the exact DDS paths. The normal layout is `R=0, G=source normal R, B=0, A=source normal G`; the specular layout is `R=0, G=32, B=metallic, A=roughness`.
- All three DDS files are 1024x1024, 4,194,432-byte, one-level legacy BGRA files with the required 128-byte header, `DDS_HEADER=124`, `DDS_PIXELFORMAT=32`, flags `65`, 32 bits per pixel, and `DDSCAPS_TEXTURE=4096`. Exact processed-PNG, DDS, pack-source, channel-layout, and relink evidence is in `blender/reports/textures_dds.json`.
- Reimport request `bfc8b5d86ed548a9998237ac6987f4ce` staged all three runtime textures under `export/mesh/` with source/destination hash identity and rendered the material successfully; there is no missing-texture magenta state in `blender/previews/reimport_temporal_guard_material_relinked_idle_frame_025_front.png`.

Selected material hashes and synchronization result:

| Selected source | SHA-256 | Staged copy | Final synchronization |
|---|---|---|---|
| `textures/dds/texture_0.dds` | `82071750202D2435542841E8354313DDB4B46BFD4B23CEBA0308CE4DE6DB4044` | `export/mesh/texture_0.dds` | hash-identical |
| `textures/dds/texture_normal.dds` | `508EF722D43C7E09E4BECB753AA88923B89BDE8734F8C0EF5F07B83ABA1AA30F` | `export/mesh/texture_normal.dds` | hash-identical |
| `textures/dds/texture_specular.dds` | `DBFD8E36D649BFD7B75E371DA6B133E7EC7B31874A370CF815327542247BD37B` | `export/mesh/texture_specular.dds` | hash-identical |

The staged `export/mesh/` copies are reimport evidence only. Parent-owned runtime synchronization into active `gfx/models/` paths has not occurred.
- No firearm, firing action, muzzle locator, muzzle light/particle, or gunshot role is present.

Vanilla calibration:

- Reference `blender/reference/western_european_infantry.mesh`, SHA-256 `F00FBADFDACDD1046F7119E62E2C47D644EA7A92D0F686B71D230BC843AEF8BA`; installed entity `.../gfx/entities/units_infantry.asset#infantry_rifle_entity`; measured mesh `polySurface106`, collision excluded.
- Axes `+Z` up, `-Y` forward. Vanilla height `7.351824797689915`, contact Z `0.00841899961233139`, entity scale `0.8`, effective height `5.881459838151932`.
- Temporal Guard height `7.3518242835998535`; apply entity scale exactly once at `0.8`; effective height `5.881459426879883`, target delta about `7.99e-11`.

## Provider action evidence and semantic review

Every action was transferred from an exact receipt under `provider/tasks/receipts/`; no local/procedural/static/transform-only replacement motion was authored. The adapter retained body fcurves, removed XY root travel, and used root-Z-only per-frame contact correction. Corrected ground contact stayed approximately within `-0.000311` to `+0.000102` source units.

| Role | Provider source | Task id | Frames/FPS | Semantic evidence | Import / grounding request |
|---|---|---|---|---|---|
| idle | `0 Idle`, SHA `F554DA...E8A75` | `01a04288-d5d7-777b-ac48-eb6ae717a2b1` | 1–97 / 24 | grounded stance, body/head sway, return; loop candidate | `18c33ad5ec50444a9d05a3032cd189b9` / `1b6ea93789274b85a5df1309473ef8cd` |
| move | rig-included walking, SHA `F6F8C4...2D918` | `01a04284-b375-7973-909c-8abd29417e11` | 1–32 / 24 | alternating stride/contact and return; in-place march candidate | `d7f9bb9bb64e468eb72cf5031d7ee3d9` / `785e9f2be01946f982ab8543a82f1f0b` |
| attack | `198 Punch_Combo`, SHA `31C752...68621` | `01a04288-ea5c-788f-ac52-ea205f248456` | 1–60 / 24 | guarded wind-up, articulated non-firearm contact, recovery | `098433524fdb4ca9a786739df3819038` / `ea48cfe9400040e69a61d4d6748a3dfc` |
| defend | `138 Block1`, SHA `95D1BA...D069A` | `01a04288-e297-7a72-ace5-2bcc301fa63b` | 1–84 / 24 | raised block, guarded weight shift, return | `f17ffbdeae8e4b6587e1e3ebe7d13f47` / `3c5833a37ed5451a87ac7ebada5b9e94` |
| entrain | `89 Combat_Stance`, SHA `DB78DF...34E5E` | `01a04288-ee21-789c-a0e0-ec81633d2d6a` | 1–40 / 24 | low formation stance, hand/weight adjustment, return | `243648a59fe941ff893dfbbfa6169c52` / `1d7074b8f8da4f738859abe83a3060ae` |
| death | `184 Shot_and_Fall_Forward`, SHA `E362AA...3E99F` | `01a04288-da2e-7e21-b11d-47325b6d390f` | 1–53 / 24 | impact reaction, collapse, forward fall, grounded settling | `21a34e3d9c3c49b39be3711454e29b0f` / `a49dc1d62a474640beae4d577a5ffd67` |
| temporal_anchor | `125 Charged_Spell_Cast`, SHA `7A1D84...D4CFE` | `01a04288-de40-777f-be17-dd4e11ce44fc` | 1–65 / 24 | gathering stance, two-hand charge/release, recovery | `62c413a469a943b7a86503d0c5256f52` / `50fd5bf151964169b8caced9adafc222` |
| synchronization | `126 Charged_Spell_Cast_1`, SHA `D6C2E6...509FEA` | `01a04288-e67c-7a73-aa64-95c67a8b27d7` | 1–104 / 24 | distinct extended sweep/charge, high release, recovery | `ea0778706c7a4801803ec6806fc1a43b` / `ab013271efcf49a7b5df4f056203f416` |

Required-role status beyond those exports:

- `support_attack`: `blocked`; no dedicated provider-authored action receipt/export/reimport exists. `attack`, `defend`, or `entrain` was not reused as a semantic alias.
- `retreat`: `blocked`; no dedicated provider-authored action receipt/export/reimport exists. `move` or `entrain` was not reused as a semantic alias.
- The unit is explicitly non-firing and has no firearm, so the `attack` role is a genuine articulated melee/contact combo; firearm aim/discharge/recoil requirements do not apply.

Multi-phase previews are under `blender/previews/`. `blender/previews/chaosx_temporal_guard_death_grounded_front.png` proves the corrected grounded settling pose.

## Export and reimport proof

Material-relinked mesh request `25d5231a154145f9a3a9aea5dfa41b9e` produced one 30,000-triangle stream with 38,906 seam-split vertices, below 65,535, with no warnings. Reimport request `bfc8b5d86ed548a9998237ac6987f4ce` returned 14,997 position-welded vertices, 38 loose boundary edges, zero degenerates, and zero non-manifold edges, plus a 24-bone rig and the five sampled idle phases.

| Runtime file | Bytes | SHA-256 | Reimport evidence |
|---|---:|---|---|
| `export/mesh/chaosx_temporal_guard.mesh` | 3,475,175 | `EA0C72AAC11CDA1B1A46CF74C6DC6A38EF3DC9833EC35DFE984E82D7FFD59516` | material-relinked parse with idle plus prior action proofs |
| `export/anim/chaosx_temporal_guard_idle.anim` | 76,627 | `C2BE045CF4079A647E012EFF8145B07CFE69CF3018E9F616FC898E90EF603563` | `f6d27a2092074c7e8061d040f86a5ff6` |
| `export/anim/chaosx_temporal_guard_move.anim` | 26,707 | `E3839142F49EA48A5182DB4145CAF04A462EAFEE9ABB8F39B42FF53DE947DAE4` | `34b5953349644f2dbbcfb7aab56dc84a` |
| `export/anim/chaosx_temporal_guard_attack.anim` | 48,211 | `F22DF39A34FADEF4ECA718102E966EA7AC704E3B3D89244D715D619CE406B3DF` | proof blend/previews exist |
| `export/anim/chaosx_temporal_guard_defend.anim` | 66,643 | `F468CB8B13041D18FC8D894557F82E70E3E31B79E0D15B2C53EBABC582655128` | proof blend/previews exist |
| `export/anim/chaosx_temporal_guard_entrain.anim` | 32,851 | `E130DDEF7FD1650C6D62E44F496F44CAF89784BF3575AA402306AD55AD6D7FEE` | proof blend/previews exist |
| `export/anim/chaosx_temporal_guard_death.anim` | 42,835 | `409714D9C162A0A2C072781327BBA73869021BC5CAA115A732EBFDCFE4494133` | `89aabf73946b424fb820060589d1e755` |
| `export/anim/chaosx_temporal_guard_temporal_anchor.anim` | 52,051 | `CF35348B9AE481D606240EFCA2722ACBB5CDACB4F5A858FBACAC4A37F28A715A` | `21df5e9ae4fd4b899c4434fdb5c510c1` |
| `export/anim/chaosx_temporal_guard_synchronization.anim` | 82,003 | `1DE85573412CE3A4A121AC6D4B6A5178EC308B3B37FD1FF1F4047E61B331624B` | `eb772a6cc2054eb196c8c0cd16e426a1` |

Every action reimport produced `io_pdx_rigAction`, a 24-bone `io_pdx_rig`, five sampled frame bounds with near-zero ground contact, `blender/checkpoints/reimport_chaosx_temporal_guard_<role>_reimport.blend`, and three-view previews. Parser text dumps sit beside all binaries.

## Sourced audio

Complete URLs, authors, terms, original/derived paths, hashes, transformations, ids, and sync points are in `audio/provenance.md`.

- Sources: BPK public-domain 60 Hz hum; MaksimPinigin CC BY-SA 4.0 walking; Camshaft64 CC BY-SA 4.0 metal impacts; Secretlondon CC BY-SA 3.0 dropped metal; stephan public-domain electric buzzing.
- Six mono, 44.1 kHz, PCM s16le WAV candidates cover selection/idle/ambient, move, attack/contact, impact, temporal special, and death; final hashes and ffprobe evidence are in `audio/provenance.md`.
- Parent must retain CC attribution/share-alike notices, inspect loop boundaries, and own sound/soundeffect/wrapper wiring.

## Counter inspection and blocker

Exact evidence is in `counters/gfx_handoff.md`.

- Installed definition: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`.
- Large precedent `GFX_unit_infantry_icon_medium`: `unit_infantry_icon.dds`, two frames, 152x42 strip, 76x42 each. Sampled greens include `(73,106,73)`, `(74,107,74)`, `(83,114,83)`, `(100,128,100)`, `(116,141,116)`, `(125,149,125)`.
- On-map precedent `GFX_unit_infantry_icon_medium_white`: `onmap_unit_infantry_icon.dds`, two frames, 60x12 strip, 30x12 each, transparent unused canvas.
- Matching skill-local land counter families/contact sheets were inspected.
- Required generic tokens: `GFX_unit_temporal_guard_icon_medium` / `unit_temporal_guard_icon.dds` and `GFX_unit_temporal_guard_icon_medium_white` / `onmap_unit_temporal_guard_icon.dds`.
- Blocker: no original PNG, processed strip, DDS, comparison sheet, manifest, icon-artist output, or approval exists. The accepted counter workflow requires original ImageGen-backed art, but this recovery brief explicitly forbids ImageGen, so no counter generation subagent was launched. No vanilla reuse/recolor fallback was used.

## Proposed generic runtime ids

- Entity `chaosx_temporal_guard_entity`; mesh registration `chaosx_temporal_guard_mesh`; mesh bytes `chaosx_temporal_guard.mesh`.
- Actions `chaosx_temporal_guard_idle`, `chaosx_temporal_guard_move`, `chaosx_temporal_guard_attack`, `chaosx_temporal_guard_defend`, `chaosx_temporal_guard_entrain`, `chaosx_temporal_guard_death`, `chaosx_temporal_guard_temporal_anchor`, and `chaosx_temporal_guard_synchronization`.
- Proposed required-but-blocked action ids: `chaosx_temporal_guard_support_attack` and `chaosx_temporal_guard_retreat`; parent must not bind either name to an existing semantic role.
- Runtime material basenames `texture_0.dds`, `texture_normal.dds`, and `texture_specular.dds`; parent must synchronize from the selected `textures/dds/` hashes recorded below rather than from filenames alone.
- Parent owns `.gfx`/`.asset`, entity, sound definition, localisation, and `kruger_temporal_guard` consumer wiring.

## Files changed by the recovery pass

- Rebuilt `export/mesh/chaosx_temporal_guard.mesh` after DDS relink and updated its parser dump.
- Added `textures/processed/{texture_0,texture_normal,texture_specular}.png`, `textures/dds/{texture_0,texture_normal,texture_specular}.dds`, packed provider companions `pdx_normal.png` and `pdx_specular.png`, and their pack reports.
- Added staged hash-identical copies under `export/mesh/`, material relink/inspection/export/reimport adapter logs, `blender/checkpoints/reimport_temporal_guard_material_relinked_idle.blend`, and multi-phase reimport previews.
- Added `blender/reports/textures_dds.json`, updated `manifest.md`, corrected final 44.1 kHz hashes/wording in `audio/provenance.md`, and refreshed this handoff.

No gameplay, `.gfx`, `.asset`, entity, sound definition, localisation, skill, spreadsheet, other package, or unrelated documentation file was edited. No HOI4 process was launched.

## Validation, blockers, and remaining work

- Passed: dependency environment verification with no findings; adapter health; geometry/weight audit; vanilla numeric calibration; receipt/source-hash verification; eight source-motion transfers; multi-phase semantic review; root-Z contact correction; 1024 PDX DDS construction/header/hash checks; material relink and visual inspection; io_pdx mesh export; material-relinked mesh/idle reimport; prior parser/reimport evidence for all eight exported actions; licensed audio container/hash verification; and exact installed counter definition/DDS/reference inspection.
- Failed or blocked: `support_attack` and `retreat` have no dedicated provider-authored sources; source-art/ImageGen authorization/provenance is incomplete; full remesh task/response and actual credit reconciliation are missing; bespoke counters/icon-artist approval are absent because ImageGen was forbidden for this recovery; parent runtime wiring and in-game consumer validation remain outstanding.
- No paid operation, ImageGen call, image-to-3D call, new base-model generation, manual motion, skeleton authoring, weighting, weapon attachment, semantic alias, gameplay edit, GFX edit, entity edit, or sound-definition edit occurred.
- This package must not be called complete or wired as final until those blockers are resolved. No fallback-complete claim or semantic alias was used.
