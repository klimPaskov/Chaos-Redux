# Event 014 sourced model inputs: foot group A

Date: 2026-08-24.

Scope: parent review and native ImageGen faithful cleanup for Scavenger Warband, Feast Cohort, and Bone Guard. This handoff does not claim Meshy geometry, rigging, animation, PDX export, or runtime wiring.

## Accepted sources

| Unit | Internet artwork | Source SHA-256 | Rights mode |
| --- | --- | --- | --- |
| Scavenger Warband | Polycount, *Cannibal of Entwood* | `42D7B70DF2941EED8F7344E4B120D01CCFF4A1AB0EA9BD67721439B89EA080EE` | `reference_only_user_authorized`; no explicit NoAI restriction found |
| Feast Cohort | Path of Exile 2, *Bone Cultist Savage* | `2A666BB1EB238967332FC4F1340B318F770BE757A18502F51738F9DD0BE654D7` | `reference_only_user_authorized`; no explicit NoAI restriction found |
| Bone Guard | Galaad Miniatures, *Elite Skeleton Warrior 03* | `83C5B783D9FF322342B0469A1477476F4EBDAB05C0BDE6D68A4403611F502417` | `reference_only_user_authorized`; no explicit NoAI restriction found |

The source researcher archived the untouched bytes, source pages, direct URLs, creator or publisher fields, NoAI checks, ranked alternates, dimensions, checksums, contact sheets, and source-only manifests in each package under `docs/assets/014_cannibalism/models_3d/<slug>/refs/source/`.

## Faithful ImageGen processing

Native ImageGen edited each accepted source instead of generating a replacement design. The prompts locked the source identity, silhouette, pose, anatomy, proportions, clothing, armor, weapons, grips, materials, palette, asymmetry, and distinctive details. Allowed changes were resolution recovery, subject isolation, scenery, base, logo, or irrelevant-text removal, compression or exposure cleanup, and alpha-edge preparation.

Bone Guard began as an unpainted gray sculpt. Its geometry and equipment remained locked while ImageGen resolved its material ambiguity into aged carved bone, dark scavenged iron, leather, charcoal cloth, and restrained dried-blood accents. The first metal-dominant material pass was rejected as too generic and remains evidence only.

ImageGen returned baked checkerboards instead of genuine transparency for all three native-alpha requests. The approved fallback changed only each background to uniform `#00FF00`, then used FFmpeg `colorkey=0x00FF00:0.35:0.15,despill=type=green:mix=1.0:expand=0.15:green=-1.0,format=rgba`. Each result was inspected over white and black backgrounds. The Scavenger input also received independent source-worker alpha verification with zero green-dominant partial-alpha edge pixels.

## Final exact-one inputs

| Unit | Final input | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| Scavenger Warband | `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/refs/original/meshy_input.png` | `1672x941` RGBA | `2CA9A46B84B9CE6EF3C0633FD84C60899031D5C7350F7BD1FE6E2D08E0AB2FA4` |
| Feast Cohort | `docs/assets/014_cannibalism/models_3d/cannibal_feast_cohort/refs/original/meshy_input.png` | `1050x1536` RGBA | `CA10096DF7FD4C9D35421A4B2A836EC0218FFBFBA012AB707378EF44F9D9AB30` |
| Bone Guard | `docs/assets/014_cannibalism/models_3d/cannibal_bone_guard/refs/original/meshy_input.png` | `1254x1254` RGBA | `CDE9F9D0F119579EBDFE1243FB20569571F1DCA0D1115046CDBF2D1CE98636DB` |

Only the listed `meshy_input.png` file may pass each package's exact-one-image Meshy gate. Source images, checkerboard failures, chroma intermediates, and QA composites are evidence only.

## Remaining work

- Produce and visually accept Meshy 7 geometry for all three inputs.
- Require clean provider rigging and real Meshy or explicitly approved professional skeletal motion.
- Complete Blender calibration, PDX material packing, `.mesh` and `.anim` exports, reimport proof, runtime copies, entities, state bindings, sourced audio, counter handoffs, and parent-owned wiring.
- Do not count this input tranche as a finished model package.
