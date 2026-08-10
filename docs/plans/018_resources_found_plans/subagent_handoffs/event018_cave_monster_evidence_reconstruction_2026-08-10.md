# Event 018 cave-monster evidence reconstruction handoff

Date: 2026-08-10.

Status recommendation: `needs_user_review`. Static runtime-byte reimport, counter review, source provenance reconstruction, and WAV signal/timing analysis are complete. Fresh 3D/action visual evidence is blocked by an exact locked-adapter limitation; auditory and live-consumer review remain user-owned. No HOI4 launch, provider call, paid operation, runtime mutation, staging, commit, or revert occurred.

## Scope and skills

The tranche followed `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, and `chaos-redux-subagents`, AGENTS.md, the complete named closure audit and handoffs, the offline Graphical Asset and Entity Modding pages, and installed runtime/vanilla counter consumers. The permanent output is documentation and non-mutating validation evidence only.

## Dependency and route evidence

- MESHY_API_KEY hard gate: present and nonblank before repository intake. The value was never printed.
- Dependencies lock SHA-256: `D764E440754241E58A066A7BE8F95F97B7D682B3568AC9FF46D49A33C092EF16`.
- Meshy schema lock SHA-256: `DBB9CAD7FB12AFE81ECA05A2F381EF4251C035F4D22BF17856A2F6D41F16A62D`.
- Blender adapter config SHA-256: `225D5BE4E7517B2C340EDF2D0F7AD522A7940664B09A7A193F68C5941D45748B`.
- Official Meshy MCP package: 0.4.0, git head `d8c77d1cb897e345eb41d38b510b8391b1664346`. No Meshy tool or balance call was made; credits estimated and consumed are both zero.
- Locked Blender: 5.1.2 build `ec6e62d40fa9`; adapter 1.2.2; io_pdx_mesh 0.91.0 with the checksum locked by the dependencies file.
- Exact allowlisted job root: `docs/assets/018_resources_found/models_3d/cave_monster/`. It was reconstructed from byte-for-byte copies of the installed runtime mesh, four animations, and three DDS maps. `manifest.md` records that these are validation inputs, not production sources.
- Adapter health request `aa730ec9cb124eb3822985175cf2a274`: PASS; io_pdx_mesh loaded and all four import/export operators were present.

## Runtime-byte reimport

| Surface | Request | Proof | Result |
| --- | --- | --- | --- |
| Mesh | `69348683ca2b4b2481bca993744b230c` | `blender/checkpoints/reimport_runtime_mesh_static.blend` | 17 bones, 30,000 triangles, 18,927 serialized seam vertices, 14,998 vertices after diagnostic position weld, zero degenerate faces, zero negative-scale objects, zero loose/non-manifold position-welded edges. |
| Idle | `33593b2079d04bc59e71a0aafd8a2c7a` | `blender/checkpoints/reimport_runtime_idle.blend` | Action present; frames 1/25/49 sampled at ground contact `0.0000109661`. |
| Move | `06768af1400341608dc1ccc3b44ec5e2` | `blender/checkpoints/reimport_runtime_move.blend` | Action present; frames 1/13/25 sampled at ground contact `0.0000109661`. |
| Attack | `26750574db2648e7b8f6d64b2460e9f5` | `blender/checkpoints/reimport_runtime_attack.blend` | Action present; frames 1/17/33 sampled at ground contact `0.0000109661`, `0.0000144839`, `0.0000109661`. |
| Death | `bf087c00dd584a0580fac55b7f24e091` | `blender/checkpoints/reimport_runtime_death.blend` | Action present; frames 1/19/37 sampled at ground contact `0.0000109661`, `0.0000092089`, `0.0000109076`. |

The fresh mesh reimport reports AABB Z extents `-0.0031263828` to `7.3532309532`, with a Blender float dimension of `7.3563575745`. The independent byte parser's retained convention is `7.3563573360`; the sub-microunit representation difference does not affect the documented `0.8` scale result.

### Preview blocker

Fresh textured front/rear/left/right/top/underside/three-quarter and representative action-frame rendering was attempted with request `b95a1f1196e84d0db1f0a1cc5087674b`. It failed exactly with `Preview rendering found no working mesh objects.`

The complete live schema and adapter dispatch were inspected. There is no restore, import-existing, promote, select, or mark-working operation. `reimport_export` creates valid proof objects but does not set the `chaosx_working` tag required by `inspect_scene` rendering. `save_checkpoint` only opens and saves, `process_textures` does not promote objects, and `prepare_candidate` accepts only GLB/FBX and performs prohibited normalization/material mutation. The adapter and proof were not altered. Wireframe and untextured preview modes are also absent from the schema.

Therefore fresh silhouette, visual scale, clipping/shear, restrained idle/move readability, and attack/death readability remain unproven. Existing historical preview conclusions are not presented as fresh evidence.

## Scale reconciliation

- Pre-export Blender working-geometry convention: height `7.3518247977`; entity scale `0.8`; calibrated effective height `5.8814598382`.
- Parsed exported-runtime AABB convention: height `7.3563573360`; entity scale `0.8`; byte-level effective vertical extent `5.8850858688`.
- Difference: `0.0045325383` source units, or `0.0036260306` effective units.

Both values are retained because they answer different questions. The runtime AABB is authoritative for installed-byte extent; the pre-export value remains the calibration record. The evidence does not prove which exporter evaluation detail creates the small delta, so no causal explanation is invented.

## Counter evidence

Fresh visual evidence: `docs/assets/018_resources_found/models_3d/cave_monster_static_closure/evidence/counter/cave_monster_counters_contact_sheet.png`, SHA-256 `5EA83DB17CFADB8F7FBD9E1C63F48D53D46F8D460CDC2CBE503ED22379280654`.

Mechanical evidence: `evidence/counter/cave_monster_counters_analysis.json`, SHA-256 `61802D789C9EA09AFD52A9BB61933F0B9B9AF3C59CFF09E6A3D3323F6FC8D71A`.

- All ten runtime DDS strips contain two nonidentical frames with transparent outer bounds.
- All five large strips are 152 by 42 with two 76 by 42 frames; all five on-map strips are 60 by 12 with two 30 by 12 frames.
- Ten unique frame-0 hashes and ten unique frame-1 hashes were observed across the complete package.
- Large frame 0 uses the inspected olive family, including deep RGB `(24,35,24)` and anchors near `(62,89,62)` through `(66,95,66)`; large frame 1 contains no green pixels and is the disabled grayscale state.
- The on-map pair follows the installed `medium_white` grayscale precedent rather than incorrectly introducing green.
- Parent visual review: PASS. All five large frame-0 sprites are distinct olive/vanilla-green silhouettes with transparent edges; frame 1 is clearly disabled/grayscale. On-map pairs are necessarily tiny but stay within bounds and retain differing silhouettes.

## Runtime WAV analysis

Machine-readable report: `docs/assets/018_resources_found/models_3d/cave_monster_static_closure/evidence/audio/runtime_audio_analysis.json`, SHA-256 `AD9BBE4166D8ABE772CE4D0C0E5E929A09460D72D303A147A81AA641A21D6EA1`.

| Cue | Duration | Peak dBFS | RMS dBFS | Integrated LUFS | Clipped samples | Timing assessment |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Idle | 24.240000 s | -14.87 | -30.38 | -29.3 | 0 | Low-level state-entry bed; live overlap/stop behavior remains unproven. |
| Foot 01 | 0.280000 s | -25.16 | -43.23 | EBU gate below range | 0 | Fits the 0.125-second phase; about 15 dB RMS quieter than foot 02. |
| Foot 02 | 0.280000 s | -8.42 | -27.95 | EBU gate below range | 0 | Fits the 0.375-second phase. |
| Foot 03 | 0.274671 s | -14.53 | -31.66 | EBU gate below range | 0 | Fits the 0.625-second phase. |
| Foot 04 | 0.280000 s | -13.34 | -37.55 | EBU gate below range | 0 | Fits the 0.875-second phase. |
| Attack | 0.841723 s | -7.78 | -18.20 | -18.0 | 0 | Hook at 0.60 s; internal peak near +0.50 s, strongest point near action time 1.10 s, before the 1.333-second end. |
| Death | 1.500000 s | -2.06 | -32.20 | -29.7 | 0 | Hook at 0.75 s; internal peak near +0.60 s, strongest point near action time 1.35 s, before the 1.50-second end. |

All files are mono 44.1 kHz 16-bit PCM WAV. Static envelope and hook arithmetic pass. Foot-contact balance, the isolated high death peak, and idle density require auditory/live review; no listening conclusion is inferred from numbers alone.

## Source provenance and recipe recovery

Durable URL/licence table: `docs/assets/018_resources_found/models_3d/cave_monster_static_closure/evidence/audio/source_provenance.md`.

- Idle: `https://commons.wikimedia.org/wiki/File:Alligatorbellow1.ogg`; direct `https://commons.wikimedia.org/wiki/Special:Redirect/file/Alligatorbellow1.ogg`; U.S. Fish and Wildlife Service public domain; fresh SHA-256 match `72A5612E99B6A941D751EFBCCF1E44F816C06C7884E3108C5298A2BA84B25169` already passed in the parent audit.
- Move: `https://commons.wikimedia.org/wiki/File:Walking-on-gravel-38827.ogg`; direct `https://commons.wikimedia.org/wiki/Special:Redirect/file/Walking-on-gravel-38827.ogg`; CC0 1.0; fresh SHA-256 match `14990DE1FD15418B55A2C939B0A99348446E613C1C4A5A307E49A87D228DE5EF` already passed.
- Attack: `https://commons.wikimedia.org/wiki/File:Lion_raring-sound1TamilNadu178.ogg`; direct `https://upload.wikimedia.org/wikipedia/commons/7/7d/Lion_raring-sound1TamilNadu178.ogg`; தகவலுழவன், public-domain self-release; fresh SHA-256 match `AB237D0F960E83412251D0C11F69959F3C2E8D3B14595F7181C3056F7FA18BF7`.
- Death: `https://commons.wikimedia.org/wiki/File:Assorted_gravel_rock_and_stones.ogg`; direct `https://upload.wikimedia.org/wikipedia/commons/a/a3/Assorted_gravel_rock_and_stones.ogg`; stephan, public-domain release; fresh SHA-256 match `BC254F5C70EE0252FDC79278F83E5428B6953807CFC21805052E6A617F2BB330`.

The initial attack/death refresh attempts returned HTTP 429, but a later cache-busted Commons redirect with the same provenance URLs retrieved both originals and exactly matched the production hashes. Direct waveform comparison, cross-correlation, production-session recovery, and sample-addressed FFmpeg reconstruction then recovered the four movement intervals, fade envelopes, attack timestamp reset, bounded trims, and absence of gain or normalization filters. The normalized commands and results are durable in `event018_cave_audio_recipe_reconstruction_2026-08-10.md`. Six of seven runtime cues reproduce byte-for-byte; movement foot 02 has a one-unit final-sample quantization variance under the current FFmpeg build and matches all preceding 12,347 PCM samples.

## Tool-call ledger

1. Environment check: MESHY_API_KEY present; no value exposed.
2. Read-only repository intake: AGENTS.md, three complete skills, named audit/handoff/addendum/system/assets docs, offline wiki pages, installed runtime consumers, vanilla counter definitions/DDS, and skill-local contact sheets.
3. Lock checks and SHA-256 calculations: passed as recorded above; actual live adapter schema enumerated.
4. Initial adapter health before root reconstruction: failed because the exact allowlisted production root was absent.
5. Authorized root reconstruction: copied installed runtime bytes to the exact allowlisted validation root; no runtime write.
6. Adapter health `aa730ec9cb124eb3822985175cf2a274`: passed.
7. Mesh and four animation reimports: five requests listed above; all passed and wrote proof blends/reports.
8. Preview request `b95a1f1196e84d0db1f0a1cc5087674b`: failed with the exact working-object limitation above; live schema/source inspected for alternatives and none exists.
9. Counter evidence script `logs/render_counter_evidence.py`: completed; contact sheet viewed by this worker and parent; parent PASS recorded.
10. Audio analysis script `logs/analyze_runtime_audio.py`: completed; ffprobe and ffmpeg EBU/astats logs retained per file.
11. Source-page web inspection: all four Wikimedia Commons pages opened; creator/licence/direct-file evidence reconstructed.
12. Attack/death source refresh: initial direct requests returned HTTP 429; later cache-busted Commons redirects retrieved exact production-hash matches for both files.
13. Recipe recovery: production-session inspection, waveform cross-correlation, sample comparison, and FFmpeg reconstruction recovered the normalized commands recorded in `event018_cave_audio_recipe_reconstruction_2026-08-10.md`; six current runtime hashes match exactly and the seventh differs only by one least-significant final PCM unit.
14. No Meshy balance/provider/generation/remesh/retexture/rig/animation/conversion call, no unrestricted Blender call, and no HOI4 launch occurred.

## Files created or changed

Created temporary validation evidence under:

- `docs/assets/018_resources_found/models_3d/cave_monster_static_closure/`
- `docs/assets/018_resources_found/models_3d/cave_monster/` as the exact locked adapter reimport root; runtime-byte copies and generated proof files only.

Durable documentation updated:

- `docs/plans/018_resources_found_plans/subagent_handoffs/cave_monster_3d_model_handoff.md`
- `docs/plans/018_resources_found_plans/018_cave_monster_3d_integration_addendum.md`
- `docs/systems/resources_found_cave_monster_model.md`
- `docs/events/018_resources_found/assets.md`
- this handoff.

No gameplay, localisation, GUI, focus, decision, spreadsheet, runtime asset, accepted specification, unrelated handoff, or adapter lock/config file was changed.

## Remaining review and closure recommendation

Keep status `needs_user_review` until:

1. A supported working checkpoint or live consumer provides fresh silhouette, scale, grounding, clipping/shear, restrained idle/move, and attack/death readability review.
2. The seven WAVs receive auditory review for movement-contact balance, attack/death alignment, and idle overlap/density.
3. The user performs live consumer validation if desired; this tranche deliberately did not launch HOI4.
4. No audio provenance or recipe decision remains; retain the durable recipe handoff and authoritative runtime hashes.

The bespoke counter package needs no further non-live visual review. No simplification or fallback was introduced; the unperformed checks are explicit blockers rather than substituted claims.
