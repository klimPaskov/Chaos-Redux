# Event 016 Portal Raider preservation-only acceptance recovery

Status: in progress; no recovered package is approved for runtime copying yet.
Owner: `/root/portal_runtime_acceptance`, GPT-6-astra.
The parent owns all active entity, GFX, sound, gameplay and runtime-copy changes.
No live-game acceptance is claimed.

## Authority and protected scope

The user explicitly supplied `PLEASE IMPLEMENT THIS PLAN: Event 016 Final Completion Plan`.
Its Binding choices and section 8 preserve all seven existing geometries, forbid regeneration, and authorize manual Blender rig, weight, contact, action, material and export recovery.
The exact accepted closure contract is `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
That user acceptance overrides generic firearm-regeneration instructions and historical job prohibitions on manual repair.
This recovery makes no provider calls and spends zero credits.
The separate externally authored weapon-free generation attempts are not adopted or overwritten.

Job root: `docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider`.
Adapter job id: `portal_raider_meshy7_recovery`; the shorter `portal_raider` id resolves to the legacy shared job and is not used.
All relative model paths below are relative to this pilot job unless stated otherwise.

Protected source: `blender/checkpoints/accepted_static_geometry_pre_rig.blend`, SHA-256 `214DCF6067C49DD79E1CBFBB871E284D8D7BDD6803D97490456C1C01ABB5429D`.
Its working object `output_unwrapped.001` has 14,909 vertices and 29,999 existing triangles.
The new rig duplicates that object and bakes its world transform into the duplicate without moving any world-space vertex or changing triangle count, UV association or material identity.

## Superseded candidate and actual-byte evidence

The historical candidate `blender/checkpoints/portal_raider_final_runtime_recovered.blend`, SHA-256 `6E7D20F5B1999508DD015B73991392F6899925129FFEDFBF84B43FC0E0A01E9F`, is rejected for severe torso/backpack folds, invalid aiming and ground contact.
Its historical export `exports/portal_raider.mesh`, SHA-256 `9F66A01E6E0CE902D17A7A9E00A34DC97BBC1AD184FCE242CFFA9288D409D334`, exists but is not accepted.
Fresh actual-byte attack reimport request `f3c6cb552afd4ce099c70272911a02f0` reproduces the deformation in `blender/checkpoints/reimport_portal_raider_acceptance_20260906_attack.blend` and its saved multi-frame views.
The old raw stream contains 41,902 seam-expanded vertices and 89,997 triangle-index entries; the latter exceeds the package's 65,535-entry ceiling.
Index-entry count, maximum referenced vertex index and exported vertex count are separate measurements.
The old raw locator is genuinely present as `portal_raider_muzzle_locator`, parent `LeftHand`; this proves old byte serialization, not correct muzzle placement or weapon contact.
The historical pass reports and `portal_raider_runtime_recovery_handoff_2026-09-05.md` carry explicit superseded dispositions.

## Dependency and source inspection evidence

Current native tranche: adapter 1.10.24, Blender 5.1.2 build `ec6e62d40fa9`, io_pdx_mesh 0.91.0.
All ten checksum-selected adapter/client/config files matched `dependencies.lock.json` before health request `72abe8c4bf6d4c3c920070b64b32cce0`.
The io_pdx_mesh archive is locked to `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`.
The fresh repository-owned stdio wrapper and `BlenderAdapterClient` are used because the thread's initially exposed tool process retained stale 1.10.21 configuration.
No unrestricted Blender Python route is used.
The authored fitted helper is checksum-locked at `74FE984FD095FB0514ECE525FB62C17EFB78880CF8EFB327BC8C0F6B8AF700C9`; its nine contract tests pass, but tests do not establish animation acceptance.

Immutable source-coordinate report: `blender/reports/portal_raider_fitted_acceptance_source.json`, SHA-256 `28AE20C22F20843D9DB064116DF749F172E975C751A830BB9D926E4CFCE38E3E`, request `5adfab57a1724f36aa6cea83417d4837`.
Source world height is 7.3518238068, matching the measured installed `gfx/models/units/western_european_infantry.mesh` height 7.3518242835 within float precision.
The named vanilla consumer is `gfx/entities/units_infantry.asset#infantry_entity`, scale 0.8, giving effective runtime height 5.8814594268.
The final entity must apply 0.8 exactly once; no 1.8-metre substitute scale is used.
The protected source and fitted rig use -Y forward and +Z up before the locked PDX coordinate conversion.

## Fitted rig and action review

`blender/specs/acceptance_fitted_rig_v5.json` is the current 23-bone fitted rig recipe.
Rig and mesh names are `PortalRaider_FittedRig` and `portal_raider_fitted_body`.
The rig has identity world transform, one root, normalized maximum-three-influence weights and no unweighted vertex.
Weapon and both hand controls maintain an explicit rigid hierarchy; native two-bone IK solves the arms to the hands.
The IK poles follow Chest under the parent-approved `pole_parent_bone` extension, so the collapse does not leave the elbow planes fixed in world space.
Original measured fore-end indices 0–1199 are explicitly rigidly bound after the v4 firing view exposed an omitted lower-barrel section.
Fitted rig v5 request `c642e2de9ad349f48659ba412bdec190` measured zero world-position error and weight hash `B4F195AC9A010826B6DDFE1E2161FC0235F4E12CB5829711138DD99128DF71C8`.
The authored and per-frame baked actions are retained separately with no authored scale channels.

All nine role recipes exist in `blender/specs/acceptance_<role>_v1.json`; the current attack, support-attack and death revisions are `v2`.
The arrival recipe uses the exact role token `portal_arrival`.
These are individually authored semantic poses, not sine templates, static aliases or whole-object animation substitutes.
Attack discharge remains frame 116 at 24 fps and support discharge frame 40; defend is a nonfiring guard.
The v4 death settle was rejected as visibly elevated; v2 death pose keys lower the articulated impact and settling posture.
Role-specific visual, contact, native export and actual-byte reimport acceptance is still being completed.

## Winding and original boundary defects

Source culling probe `9914783d3ca8429284ea63db60030fa6` preserves the source hash and saves paired original, opaque-clay culling-on and culling-off views under `blender/previews/portal_raider_acceptance_source_culling_*`.
Culling-on removes broad rifle, leg and backpack patches; culling-off restores them.
Winding inspector `3504979be88e47dda4cd42451d940957` confirms 626 inconsistent shared edges, 83 original boundary edges and 11 orientation-propagation conflicts.
The automatic outward-orientation route correctly refuses this nonorientable source component.

The explicitly indexed partial correction is `blender/reports/portal_raider_acceptance_explicit_winding_candidate.json`.
Its 15,473 selected face reversals have list SHA-256 `ADF106324F3FD9ED6F01CD9E4779836C352916BEFEAD09B38A01FB1CAAD7F987` and reduce the inconsistent-edge count to two without adding, deleting or moving geometry.
Residual source pairs are faces 15044/15452 at original vertices 10327/10333 near the back waist, and faces 17368/17470 at vertices 3997/4001 near the neck.
This is explicitly not a closed-manifold or global-outward pass.
No cap, seam cut or other topology addition is authorized or performed.
Remaining source boundaries require evidence-led parent disposition after corrected culling and reimport review.

## Verified PDX material candidates

Provider base, normal, metallic and roughness maps remain immutable.
The selected 1024-square BGRA DDS candidates have exact decoded-pixel matches to their independently resized packed PNGs.
The normal channels are R=0, G=source normal R, B=0, A=source normal G.
The specular channels are R=0, G=32, B=metallic, A=roughness.
Raw grayscale roughness is not the final specular texture.

| Job-relative selected file | SHA-256 |
| --- | --- |
| `textures/dds/acceptance_channels/portal_raider_diffuse.dds` | `C779056BCFB007DC75C80A0839395D3E71BE47CCC26F4D54C5065293099C0736` |
| `textures/dds/acceptance_channels/portal_raider_normal.dds` | `96F1738D7380AF4A76A008360CD19C709CB9611E75362BEFC5294943439BD000` |
| `textures/dds/acceptance_channels/portal_raider_specular.dds` | `C4644EC9BA2A64FB251AE6E2CCFB6B6DE88E3AA8B89C029D9E6C0B84C3098439` |

Report: `blender/reports/portal_raider_acceptance_materials_channels.json`.
The earlier DDS candidates directly under `textures/dds/` are rejected because RGBA resizing altered packed channel values; do not select them.

## Sourced audio and preserved counters

The twelve derived mono 44.1-kHz PCM16 WAV files match `evidence/audio/audio_manifest.md` and their source/license ledger at `evidence/audio/licensing/source_ledger.md`.
No audio is generated, synthesized or newly recorded.
The manifest preserves source pages, creators, CC0/CC BY terms, originals, transformations and hashes.
Its historical timing table is not current action acceptance.
For an action beginning at source frame 0, attack frame 116 is 4.833333333 seconds and support frame 40 is 1.666666667 seconds.
PDX reimport starts sampled animation at frame 1; the matching reimport frames are therefore 117 and 41, without adding a frame to event time.
Final movement, retreat, impact, arrival and death cues will follow the selected accepted role phases.
Per-subunit selection audio is required only where supported by the installed engine; preserve ordinary infantry voices if the only available selection mechanism is tag-wide.

The bespoke counters and reference paths in `portal_raider_counter_art_handoff.md` are preserved without regeneration.
Parent runtime GFX is already in `interface/portal_raider_system.gfx`.
Large runtime `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds`: 152×42, two 76×42 frames, SHA-256 `4236DF5183605AF540D44339EED96F29B2B59A40D9F82E1472C5178963EF920E`.
Map runtime `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds`: 60×12, two 30×12 frames, SHA-256 `FB009C5EEED40C1AAD867D15C066422CB142AA24DC2C38D7311857BFA284D85E`.
Both literal runtime file hashes match their selected source artifacts.
The installed vanilla definition is `interface/subuniticons.gfx`; reference families are the skill-local land `counters_large` and `map_counters` families and their inspected contact sheets.
The current installed vanilla large infantry DDS hash is `B33A8E3B69CC789EB0E31BA99F4E5BA4E5B0A8B51EC1A7A7F709C3516F720C23`, and small infantry DDS hash is `58AB78662C2A64A519B8D5D144582E7B2785915BD0A0A822696D87A9DE6F766C`.
These current reference hashes correct the historical handoff's intermediate transcription without changing its shipped art.

## Runtime handoff boundary

Proposed destination family: `gfx/models/units/portal_raider/` for the mesh, nine actions and three selected DDS textures; `gfx/entities/portal_raider.gfx` and `gfx/entities/portal_raider.asset` for parent-owned registration.
Stable requested identifiers remain `portal_raider_mesh`, `portal_raider_entity` and the `portal_raider_*` animation family.
No Portal model/entity file was found in the literal current `gfx/entities` and `gfx/models/units` filesystem checks or `rg --no-ignore` search; ignored runtime assets must never be assessed with ordinary `rg` alone.
Do not copy the historical rejected mesh to these destinations.
Exact final meshsettings names, exported locator transform/parent, selected mesh/action checksums, copy crosswalk and wiring snippets remain pending the actual-byte export/reimport tranche.

## Remaining acceptance work

- Complete the corrected firing, recoil, collapse and settle visual/contact review.
- Complete the six remaining native authored roles and review gait, guard, arrival and wounded phases.
- Apply and inspect the explicit normal-only candidate, retaining the two nonorientable source defects as unresolved until a parent disposition exists.
- Bind selected packed materials on a preserved working copy; partition the exporter streams under both ceilings without dropping geometry.
- Export and reimport all nine roles and a Weapon-parented measured muzzle locator from actual bytes.
- Replace this in-progress section with a selected artifact crosswalk and exact parent wiring instructions.

Skills used: `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets`, `chaos-redux-subagents`.
No gameplay, active model/entity/GFX/sound files, runtime model copies, Git staging or commits are owned by this worker.
