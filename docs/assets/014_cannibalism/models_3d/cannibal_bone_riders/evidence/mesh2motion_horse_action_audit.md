# Mesh2Motion horse action audit

The approved professional horse source is the Mesh2Motion `mesh2motion-assets` repository pinned at commit `6bab14fa197957bf7851477cad0c372960a48824`.

The repository source tree, exact CC0-1.0 license bytes, Blender sources, consolidated GLB, and hashes are archived under `provider/external_animation/mesh2motion_horse/`.

The adapter imported the self-contained `horse-animations.glb` into a protected donor checkpoint and measured one 56-bone horse armature, 2,146 weighted horse vertices, zero unweighted horse vertices, no vertex above four influences, and 15 genuine multi-frame actions at 24 FPS.

The per-action Blender files were also archived because they are the immutable source-format actions requested by the approval condition.
They link their model data to the shared rig Blender file, so isolated preview renders are blank unless the linked rig is resolved.
The self-contained GLB was therefore used for visual phase inspection without modifying the archived sources.

## Provisional horse semantic map

| Runtime role | CC0 source action | Frames at 24 FPS | Visual decision |
| --- | --- | ---: | --- |
| idle | `Idle` | 0-64 | Standing breath, head and tail life; loop candidate. |
| move | `Run` | 0-11 | Genuine gallop cycle; loop candidate. |
| attack | `Rear` | 0-71 | Mounted combat rear with clear rise, peak, and recovery. |
| defend | `Kick` | 0-32 | Rear-leg kick with extension and recovery; mounted defensive response. |
| support_attack | `Head_But` | 0-24 | Distinct forward head strike and recovery. |
| retreat | `Trot` | 0-17 | Distinct lower-intensity withdrawal-compatible gait; loop candidate. |
| training | `Eating` | 0-64 | Head-lowering, grazing, and recovery; suitable only if the rider training clip reads as calm mounted handling. |
| death | `Death` | 0-34 | Articulated collapse and settling. |

Every mapping is distinct; no alias or transform-only action is proposed.
The final compound acceptance remains conditional on retargeting these source motions onto the bespoke bone-barded horse and synchronizing a separately sourced Meshy rider action.

## Phase evidence

Three right-view frames were rendered for each proposed role under `blender/previews/mesh2motion_<role>_f###_right.png`.
The action source remains the consolidated GLB checksum `C6F890C307E457B9AA7CCEDA1FBC1E39F8E6723EF340F23E3E667E122673B51C`.

The source demonstration horse includes a large ground/reference icosphere that obscures some hoof contact in the renders.
That object is not part of the Bone Riders runtime geometry and must be excluded from any action transfer or export.

## Current processing gate

The registered adapter surface did not expose the lock-declared segmentation, sourced-action import/retarget, calibration, or grounding tools during this audit.
Adapter registration recovery commit `7e3af24ac` exists but requires a fresh Codex/MCP process before those operations are callable.
No shell Blender workaround, locally authored creature motion, or runtime substitute was used.
