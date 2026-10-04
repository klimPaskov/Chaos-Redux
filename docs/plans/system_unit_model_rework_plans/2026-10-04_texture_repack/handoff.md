# 2026-10-04 unit texture repack handoff

Status: **needs_user_review**: the textures are repacked and installed, and Blender previews were rendered and reviewed. The in-game check is pending; the parent will film it.

Route: this was a Blender-only, texture-only repair. There were no Meshy calls and no balance checks, and 0 credits were estimated or spent. No geometry, rig, animation, `.mesh`, `.anim`, `.gfx`, `.asset` or entity file was changed.

## Files changed

All five files are uncompressed B8G8R8A8, 1024x1024, single level, 4,194,432 bytes. Each 128-byte header is byte-identical to `cannibal_bone_guard_normal.dds`.

| Runtime file | Original SHA-256 | New SHA-256 |
|---|---|---|
| `gfx/models/units/014_cannibalism/cannibal_island_reavers/cannibal_island_reavers_normal.dds` | `4AA8F7530160C4C4681555F11FE5D610EDA1E0B8C1B426D947B8294F5B49470A` | `FA72C9A908AA01A60445D3C5F5376BB30C868637AFB414732F63750962CA241C` |
| `gfx/models/units/014_cannibalism/cannibal_island_reavers/cannibal_island_reavers_specular.dds` | `E8A4FBACD0BEE1DCCBEECA89FBBBB15FD4F31D36C1381E8450FC9B4AD00DD6C0` | `9E7DDF3D6A1FCD1F6726AA853AFA62CEE5E29E911EF3091CBDEAB42F54D5777D` |
| `gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_normal.dds` | `4A306CDB30F82FD14E264ECDC52257E28790B265D1D58402E59FEAE8B139C4F2` | `76C13BCD886D349DD5465491C229DD7A570E438205ACA22D49EB3A871748958F` |
| `gfx/models/units/014_cannibalism/cannibal_march_predation_column/cannibal_march_predation_column_specular.dds` | `8B42E70BB0FD8371C0D7287776D1729E2C6EED9DCB29B478115DD9202657FFCE` | `56AD306DF14FD1DA7F997E62D263FBD986F124A135239863BC06B92E479E70BA` |
| `gfx/models/units/alien_infantry/alien_infantry_normal.dds` | `DF1F9C947B64478BA5B739BC215D18400EC38272B2325D2F19E395C108873E39` | `56CF3A704B6BFD4F05B7FD91456139F2DD362CF54CDC5E273B3B763958462CCB` |

The byte-exact originals are in `originals/`, with `originals/SHA256SUMS.txt`. Those hashes match the ones in the existing reavers, march and alien manifests and handoffs. Before installing, each runtime file was re-hashed to confirm that no other agent had changed it since the backup.

Unchanged by this pass: `cannibal_feast_cohort_*` (see the diagnosis below) and every other family and alien map.

## Engine contract used

These units use `shader = "PdxMeshAdvanced"`, which defines `PDX_IMPROVED_BLINN_PHONG` in the installed `gfx/FX/pdxmesh.shader` (lines 466-543) and `standardfuncsgfx.fxh`. The relevant decoding is as follows.

- Normal map: `UnpackRRxGNormal` reads x from G and y as the negated A, then derives z as `sqrt(saturate(1 - x² - y²))`. R is unused, and B is read as the `EMISSIVE` strength, which blends the pixel toward unlit diffuse at night.
- Specular map: G sets specular strength (`F0 = G² * 0.4`), B sets metalness (remapped as `1 - (1 - B)²`, which darkens the diffuse and tints the reflection with the diffuse colour), and A sets glossiness (Blinn-Phong power `2^(11A)` and env-map mip `(1 - A) * 8`). The environment reflection is `spec + (max(A, spec) - spec) * (1 - N·E)^5`.

## Why reavers and march rendered as chrome

Both models carried an ordinary RGB tangent normal map, with A = 255 and B around 207 to 220. The engine decoded A = 255 as y = -1, so every texel got z = 0, meaning the decoded normal lay flat in the surface plane (100% of texels, measured). Every texel therefore sat at grazing Fresnel and reflected at the full glossiness value.

The specular maps were grey raw roughness (R = G = B, mean 136 and 118, A = 255). That gave gloss 1.0 (mirror, env mip 0), a metalness remap of about 0.78 that blacked out the diffuse, and specular strength G of about 0.5 against the family's 32/255. Together these produce the polished chrome that was filmed. The normal-map B channel also drove about 0.8 emissive at night.

The `humanoid_unit` profile in `.tools/3d_pipeline/config/asset_profiles.json` forbids raw roughness as specular (`raw_roughness_as_specular: false`).

## Channel decisions

### Normal maps (reavers, march, alien orphan)

- New layout: R = 0, G = source R (tangent X), B = 0 (no emission), A = source G (tangent Y). This matches the family's working maps and `.tools/3d_pipeline/review/pdx_textures.py`, and every X/Y value is preserved exactly.
- No Y flip was applied, because the vanilla convention matches the source. A curl (integrability) probe on installed vanilla infantry normals (ENG, GER, FRA, FIN, JAP, ITA, SOV, USA, BEL weapons) shows Y stored green-up (OpenGL) in A, with correlation -0.14 to -0.42 unsmoothed and -0.46 to -0.55 after smoothing (ENG, GER).
- The Meshy-derived sources follow glTF's mandated green-up convention, and the curl probe leans the same way on all six Meshy-derived maps. Those are the three RGB maps plus the already-packed feast_cohort, feast_guard and siege_eaters maps, at -0.02 to -0.11, which is weak but consistent.
- The probes are `work/analysis/normal_y_convention_curl.py` and `work/analysis/normal_y_convention_multiscale.py`.
- After the repack, 8.3% (reavers) and 11.9% (march) of texels tilt past 60 degrees. That is within the family range of 9.2 to 13.1%.

### Specular maps (reavers, march)

The specular maps were rebuilt as follows. The derivation is in `work/repack_textures.py` and the numbers are in `work/repack_record.json`.

- `gloss_raw = 255 - grey`, the profile's inverted roughness.
- A is a linear map of `gloss_raw` p1..p99 (reavers 71..174, march 96..179) onto cannibal_bone_guard's A p1..p99 band, [91, 178].
- G = 32 is the profile constant and matches every family model.
- R = 0.
- B = 0 everywhere except a geometric metal mask. Inside the mask, the in-mask `gloss_raw` p5..p95 is mapped onto [64, 123], which is the 75th-percentile metal band of cannibal_bone_guard (64) and cannibal_feast_guard (123). Rougher, rustier texels therefore stay less metallic.

Result means (RGBA) compared with the working references:

| Map | R | G | B | A |
|---|---|---|---|---|
| reavers specular (new) | 0 | 32 | 0.2 | 131.3 |
| march specular (new) | 0 | 32 | 1.8 | 134.4 |
| cannibal_bone_guard | 0 | 32 | 7.0 | 131.0 |
| cannibal_feast_guard | 0 | 32 | 14.8 | 156.0 |

### Metal identification

Colour thresholds failed for these Meshy atlases. The reavers diffuse has no low-saturation texels at all (5th-percentile saturation 0.44), and the march candidates landed on a grey loincloth. Metal was therefore located on the model.

`work/pdx_material_preview.py` dumped rest-pose triangle positions and UVs from the shipped `.mesh` files. `work/build_metal_masks.py` then selected the weapon triangles and rasterized their UV footprint, with a 1-texel dilation. The selections were checked with magenta overlay renders, and the diffuse sampled at those triangles confirmed the choice.

- **cannibal_island_reavers:** the harpoon's iron tip above z 6.62 (rgb about 63,48,35, saturation 0.44) and its barb hook. The barb is the set of triangles more than 0.12 from the fitted shaft axis between z 5.70 and 6.45 (rgb about 68,50,35, saturation 0.48). The wooden shaft (rgb about 95,61,39, saturation 0.58 to 0.60, radius about 0.085), its lashing, skin, bone trophies, rope and cloth stay non-metal. This covers 200 triangles and 0.21% of texels.
- **cannibal_march_predation_column:** the cleaver-style machete blade, which lies flat forward (-Y) of the right hand. The hand, the handle butt, skin, tooth trophies, the self bow, the quiver, leather and the coat stay non-metal. This covers 356 triangles and 1.82% of texels. The blade's diffuse is blood-red, so it reads as dark bloodied steel.
- The masks are in `work/masks/` (`*_metal_mask.png` and `metal_masks.json`). To regenerate the UV dumps, run `python .tools/3d_pipeline/review/review_cli.py blender --script docs/plans/system_unit_model_rework_plans/2026-10-04_texture_repack/work/pdx_material_preview.py --config docs/plans/system_unit_model_rework_plans/2026-10-04_texture_repack/work/uvdump_request.json`.

### DDS format

The files were converted with the repository converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. texconv is not installed, so it used its ffmpeg BGRA backend. Every DDS was decoded back and compared texel by texel with its PNG (exact match) before being copied to the runtime path.

On the "mipmaps" part of the brief: the working cannibal_bone_guard and cannibal_feast_guard maps, like every Chaos Redux unit map scanned here, store a single level with mip count 0. I matched that format exactly rather than introduce a different one. Vanilla unit maps ship as DXT5 with full mip chains. See follow-up 2.

## cannibal_feast_cohort diagnosis: values in range, no change made

- Specular mean (0, 32, 0.4, 156.4) equals cannibal_feast_guard's (0, 32, 14.8, 156.0), and metal is essentially absent. The normal map is already packed (0, 126.9, 0.7, 127.2) with no emission. Every value is inside the family range, so the brief's fix condition is not met.
- The dark-chrome speckle comes from the cohort's own diffuse, not from its specular or normal channels.
  - In the diffuse-only render (matte, no normal map, no specular), the cohort already shows a dark body covered in gold/cream flecks. That patchwork of light texture islands ignores anatomy and runs across skin, hide and the spear alike.
  - The clay render of the same mesh is clean.
  - A diagnostic-only render with gloss scaled down to the vanilla infantry mean (about 87, versus 156) barely changes the look.
  - All three are in `previews/cannibal_feast_cohort_diagnosis.png` and `previews/cannibal_feast_cohort_diagnosis_components.png`.
- Two secondary amplifiers apply in game but not in the Blender preview:
  - **Strongest normal map in the family:** 13.1% of texels tilt past 60 degrees, against 0.2 to 2.8% for vanilla infantry. Together with family gloss of about 0.61 (vanilla 0.14 to 0.34), that gives the largest grazing-reflection share in the family (0.081, against feast_guard 0.056).
  - **No mip chain:** the single-level DDS lets that high-frequency detail alias into per-pixel sparkle at map zoom.
- A real fix needs a new diffuse, through a provider retexture or a Blender re-projection or bake. That is outside this texture-repack scope and was not attempted.

## alien_infantry_normal.dds is not runtime-bound

`gfx/entities/alien_infantry.gfx` binds `alien_infantry_body_{diffuse,specular,normal}.dds` for all seven `mesh.002` streams, and the pistol maps for `AlienRayPistol`. The `.mesh` itself references only `alien_infantry_body_*` and `alien_infantry_pistol_*`, and no `.gfx` or `.asset` names `alien_infantry_normal.dds`.

As instructed, the orphan was repacked to the Paradox layout, but it cannot change the live alien look. The bound maps are already correctly packed: body normal (0, 127, 0, 127) and body specular (0, 32, 0.6, 150). `previews/alien_infantry_runtime_binding.png` shows the live binding rendering matte and correct.

The pistol normal carries B up to 150, which is deliberate night emission on its glow parts. It was left unchanged.

## Previews

All previews were rendered headless with the locked Blender. The "before" rows use the byte-exact originals decoded exactly as the engine decodes them, and the "after" rows use the installed runtime bytes.

The material graph approximates the shader:

- Base colour = diffuse.
- Metallic = `1 - (1 - B)²`.
- Specular IOR level = `G² * 0.4 / 0.08`.
- Roughness = `1 - A`, the skill's preview mapping.
- The tangent normal is rebuilt from x = G and y = A. Stored Y is used directly because the importer already unflips the UVs.
- Emission is ignored (daylight).

The lighting is the bundled `sunrise.exr` plus a sun, with views front, three-quarter, high game angle and rear.

- `previews/cannibal_island_reavers_before_after.png`: before is mirror chrome; after shows skin, cloth, a wooden shaft and a dark iron harpoon head.
- `previews/cannibal_march_predation_column_before_after.png`: before is chrome; after shows red skin, a wooden bow, the coat and a dark bloodied metal blade.
- `previews/cannibal_feast_cohort_diagnosis.png`: the current cohort, feast_guard as the reference, and the diagnostic vanilla-gloss variant (not shipped).
- `previews/cannibal_feast_cohort_diagnosis_components.png`: cohort clay, cohort diffuse-only, and feast_guard clay.
- `previews/alien_infantry_runtime_binding.png`: the alien's live body and pistol binding.

The before renders reproduce the filmed chrome, which supports the approximation. They are still offline previews, not in-game evidence.

## Dependency and route evidence

- Blender 5.2.2 LTS, build `d13f752e3b9c` (from `work/render_report.json`), matches the `routes.blender` entries `version` and `build_commit` in `.tools/3d_pipeline/config/dependencies.lock.json`. The executable is `C:/Users/klimp/AppData/Local/Programs/Blender 5.2.2/blender-5.2.2-windows-x64/blender.exe`.
- io_pdx_mesh is 0.91.0. The compat archive `.tools/3d_pipeline/vendor/io_pdx_mesh/blender-io_pdx_mesh-0.91-py313.zip` has SHA-256 `508643626FEFE78511903B1894B8B4D68C387EDD6228AD70487699A866886702`, which matches the lock. The three installed patch files (`__init__.py`, `pdx_maya/maya_ui.py`, `pdx_blender/blender_import_export.py`) also match their locked hashes.
- The `chaosx_blender_hoi4_process_textures` schema only extracts or relinks DDS maps in a saved scene; it does not repack channels. The adapter was therefore not used, and the adapter health operation was not called.
- The repack is a deterministic host script (numpy, Pillow and the repository DDS converter) that always reads from `originals/`.
- Rendering and UV dumping ran through the repository route `.tools/3d_pipeline/review/review_cli.py blender --script ...`, which launches the locked Blender with `--background --factory-startup` and the locked extension. The worker `work/pdx_material_preview.py` is read-only: it imports into a disposable scene, never saves a `.blend`, and writes only PNG and NPZ outputs to the request paths.
- The imported object names match the `.gfx` meshsettings: `output_unwrapped.002` (reavers), `char1.002` (march), `mesh.003` (cohort), `char1.003` (feast_guard), and `mesh.002` plus `AlienRayPistol` (alien).

## Validation performed

- Channel statistics and DDS headers were checked for every target, family model and vanilla infantry precedent, using `work/analysis/ddsscan.py`.
- Y-convention probes were run on vanilla and source normals.
- Normal-tilt and grazing-reflection measurements were taken before and after.
- Every installed DDS round-trips texel-exact against its PNG, its header is identical to bone_guard's, and its runtime hash equals the staged hash.
- Metal masks were verified visually on the model from four views, with diffuse samples at the selected triangles.
- Before and after renders were reviewed for both repaired models, and the cohort was taken through clay, diffuse-only and gloss-scaled diagnostics.

## Not validated

- The in-game look is pending; the parent films it. Night emission and map-zoom aliasing can only be judged in game.
- No `.mesh` reimport or export was involved, because geometry is unchanged.

## Follow-ups for the parent (not done here)

1. **Inverted Y in three working normal maps:** `cannibal_bone_guard_normal.dds`, `cannibal_scavenger_warband_normal.dds` and `alien_infantry_body_normal.dds` are strongly Y-down (DirectX), with curl correlations of +0.42 to +0.98. They look derived from diffuse luminance, which makes their Y inverted relative to vanilla. Their relief is shallow (std 3 to 8), so the effect is subtle: vertical bumps are lit from the wrong side. A one-line fix would flip A (`A = 255 - A`), but this pass did not change them.
2. **No mip chains, family-wide:** the repository converter writes single-level DDS by design, while vanilla ships full DXT5 mip chains. If the in-game footage still shows shimmer or speckle at map zoom, add mip generation to the converter and pipeline (texconv is not installed), then regenerate the family maps.
3. **feast_cohort needs a new diffuse:** rebuild it from a retexture or a Blender re-projection. Optionally also soften its normal map and bring gloss toward the vanilla band. This needs a decision, because a retexture is paid provider work. Superseded: the follow-up section below found the root cause. All three cohort maps belong to a superseded UV layout.
4. **Stale package docs:** `docs/assets/014_cannibalism/models_3d/cannibal_march_predation_column/manifest.md` and the reavers and alien package manifests and handoffs still list the old normal and specular hashes. The new hashes are in the table above and in `work/repack_record.json`. Updating those parent-owned documents was outside this pass's write scope.
5. **Stale texture names inside the reavers mesh:** `cannibal_island_reavers.mesh` internally names `cannibal_island_reavers_diff.dds` and `cannibal_island_reavers_spec.dds`, which do not exist. The `.gfx` meshsettings (`output_unwrapped.002`, index 0) override them, so the runtime is unaffected. This only matters if those meshsettings are ever removed.

## Package layout

- `originals/`: byte-exact backups and `SHA256SUMS.txt`.
- `previews/`: the before/after and diagnostic sheets.
- `work/repack_textures.py` and `work/repack_record.json`: the repack and its per-file hashes, statistics and parameters.
- `work/build_metal_masks.py`, `work/masks/` and `work/uvdump_request.json`: the metal identification.
- `work/pdx_material_preview.py`, `work/render_previews.py`, `work/preview_request.json`, `work/diagnostic_request.json` and `work/render_report.json`: the preview worker, driver and requests.
- `work/analysis/`: the DDS statistics and normal Y-convention probes.
- Regenerable intermediates (staging PNG and DDS, decoded PNGs, individual renders, UV dumps) were removed after verification. Rerunning `work/repack_textures.py` (without `--install`) and `work/render_previews.py` recreates them.

## Follow-up 2026-10-04: feast cohort diffuse speckle

Status: **blocked for a real fix; the requested inpaint is built and staged, not installed**. The runtime `cannibal_feast_cohort_diffuse.dds` is unchanged (SHA-256 `4324CFC698CC617BC4348459DD1759490168A718C73304DEC24E0AF10DAD66DE`). A byte-exact backup was added to `originals/` and `originals/SHA256SUMS.txt`, and it matches the hash in the cohort package manifest. This pass made no Meshy calls, spent no credits, and changed no geometry, rig, animation or `.gfx` file.

### Root cause: the cohort's maps belong to a different UV layout

The cohort's diffuse, normal and specular maps were all baked for the superseded recovery model's UV layout, not for the shipped mesh.

- **Lineage:** `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/blender/reports/textures_dds.json` shows that all three DDS maps were extracted from `blender/checkpoints/05_pre_export.blend` with adapter 1.8.1. The job history logs that as the only `pdx_textures_processed` event, at 2026-08-22T16:48, for the earlier recovery model (rig task `01a02a43-8497-7eb4-96da-e40495030a69`).
- **The shipped mesh is the later v6 model:** `export_mesh.json` shows it was exported from `recovery_v6_11_runtime_sanitized_11014.blend`. That is the 2026-08-24 recovery_v6 model: generation `01a033c5-1c4c-7dd8-8c0c-ad365327dc1d`, remesh `01a033d0-7114-7171-9b10-4236e971a992`, rig `01a033ee-4dfe-7e18-8137-1293d3106cb8`, then Blender decimation. Its `textures.json` and every v6 prepare report list no texture bindings, and no texture-processing event follows the v6 generation. The existing cohort manifest had already flagged the texture-to-runtime relationship as unresolved.
- **Atlas evidence:** with the mesh's own UV islands overlaid, the texture's patch shapes, flat padding fills and radial smear streaks fall inside the mesh's islands, and the island borders cut through texture patches. The reavers and feast_guard atlases, by contrast, line up with their islands.
  - A padding-agreement test (`work/analysis/uv_layout_agreement.py`) scores the identity orientation best for all four control models: reavers 0.236, feast_guard 0.481, siege_eaters 0.211, march 0.368.
  - The cohort is the only atlas where identity is not best: 0.196, against 0.204 for a vertical flip and similar values for every other flip and rotation.
  - So no orientation fix exists: the cohort atlas does not belong to this layout at all.
- **What it looks like on the model:** skin-like and hide-like patches land on the spear and hook, cream patches cover the face, and the "flecks" are the old atlas's own padding and patches. The normal and specular maps are scrambled the same way, which adds per-patch lighting noise.

### The requested inpaint (staged candidate)

`work/cohort_fleck_inpaint.py` always starts from the backup. The script header documents the method; in summary:

- Islands come from the shipped mesh's UV islands, built in `work/uv_islands.py` (607 islands, gutter excluded).
- A fleck is a warm cream or gold texel at least 1.45 times brighter than its island's local background (and at least 0.10 brighter in absolute terms), with a 1-texel dilation kept inside the same island.
- Each island is inpainted separately with OpenCV Telea. Every texel outside the island is marked unknown, so nothing is drawn across a seam.
- Gutter texels within 2 texels of an island are re-padded from their nearest island texel.
- Size, header and alpha are unchanged, and the DDS round trip is texel-exact.

The result is recorded in `work/cohort_fleck_record.json`:

- **Not a scattering of flecks:** it touches 205,668 texels, which is 27% of all island texels, in 581 of 607 islands. The "flecks" are a quarter of the content.
- **Partial mitigation only:** the candidate is calmer (fewer bright cream flecks), but the camouflage patchwork remains, including cream islands on the head, chest and shoulders where the surrounding material is itself cream. It does not restore skin, hide or spear materials, because none exist under this mesh's UVs.
- **No ornaments could be protected:** in a mismatched atlas no texel corresponds to the bone and teeth gear, beads or metal fittings, so no texel qualified for the brief's "intentional detail on real geometry" protection.

It is staged at `work/staged/cannibal_feast_cohort_diffuse.dds` (SHA-256 `06640B159F0AE788ADE4A31C51DEC3B399B49A7F197F9F6BF3D9DFA4F87E3885`, 4,194,432 bytes), with its mask at `work/staged/cannibal_feast_cohort_fleck_mask.png`. It is not installed: shipping it would present a mismatched atlas as repaired, and it leaves the scrambled normal and specular maps in place. To accept it as an interim anyway, run `python docs/plans/system_unit_model_rework_plans/2026-10-04_texture_repack/work/cohort_fleck_inpaint.py --install`. That rebuilds the file from the backup, installs it, and records the installed hash.

### Previews

- `previews/cannibal_feast_cohort_fleck_inpaint_before_candidate.png`: five rows over the same four diagnosis views. Before and candidate are shown with the full PDX material, then as diffuse only, and the last row overlays the inpainted texels in magenta on the shipped diffuse.
- `previews/cannibal_feast_cohort_fleck_inpaint_closeups.png`: torso, waist, head and spear close-ups, before, candidate and mask. The spear-point camera framed the shaft rather than the point.

### Real fix options (parent decision)

1. **Free recovery of the matching v6 textures (recommended):** download the existing v6 rig task `01a033ee-4dfe-7e18-8137-1293d3106cb8` again, using the same rigged GLB the shipped mesh was decimated from, if Meshy still serves it. Then process its maps with `.tools/3d_pipeline/review/pdx_textures.py` and confirm the fit with `work/analysis/uv_layout_agreement.py` (identity must score clearly best). Downloading an existing task is not a new paid attempt, but it is a Meshy call, which this brief excluded, and it needs the `MESHY_API_KEY` gate and locked-route verification first. This replaces all three cohort maps correctly.
2. **Paid retexture:** if the v6 assets have expired, run a Meshy retexture on the shipped mesh. This needs explicit authorization.
3. **Interim only:** install the staged candidate, and optionally flatten the scrambled normal map. This is a symptom mitigation that leaves the wrong atlas in place.

### Validation

- The runtime file is unchanged (hash re-checked).
- The candidate's DDS round trip is texel-exact, its header is identical to the shipped file's, and its alpha is unchanged.
- Islands were derived from the shipped `.mesh` through the locked Blender and `io_pdx_mesh` route.
- The renders were reviewed at full resolution.
- In game: nothing has changed in game, so there is nothing new to film for the cohort.
