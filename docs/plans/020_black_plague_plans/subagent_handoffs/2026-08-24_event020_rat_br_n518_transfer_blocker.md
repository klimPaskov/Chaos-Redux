# Event 020 br-n518 rat transfer blocker handoff

Date: 2026-08-24
Owner: `020_black_plague`
Asset: `rat_ground_unit_shared`
Status: **blocked; no runtime mutation**

Adapter 1.10.0 successfully ingested the zero-cost CC0 br-n518 `rat.blend` through the repository-owned allowlisted stdio route. The exact source is `Rat_Armature` plus direct mesh `Rat`. Its five native 24 FPS actions have distinct curve hashes: `idle-loop`, `walk-loop`, `run-loop`, `attack`, and `death`.

The required four-nearest dual-source preparation completed as request `7d50fa525bce4e39aad6e3bcd6385bd4`, preserving the original Meshy rat's 32,909 vertices, 29,999 triangles, target height `7.3518247604`, entity scale `1.35`, and audited PDX textures. It failed acceptance: the Meshy geometry is visibly pinched/malformed, and 5,889 vertices exceed four influences, reaching seven.

The Walk-only gate then inspected frames 0, 7, and 15 through requests `2d1b1d3ec3244f829495c8b23c5cc794`, `564990cd5dfe461b90a1cb35a5e36d37`, and `093ab6d3c81f4be9b5eca93270dfb4c3`. All selected the native `walk-loop` curve hash `432FADAA3A2C9FFAA766766E9047C2117E16B833BFB756EA9DC569F1AE0E41C2` with NLA muted. Decoded-pixel comparison reports infinite PSNR between start/mid and mid/end in both left and front views: no visible multi-frame deformation survived the binding.

No batching, retiming, sanitation, export, reimport, runtime synchronization, or missing-role retarget was attempted. Danimal and Quaternius remain source evidence only; no alias or relabel was used. Audio/GFX/runtime files were left untouched. Full source, dependency, checkpoint, request, hash, influence, and preview evidence is in `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/evidence/free_animation_sources/br_n518_action_and_transfer_audit.md`.

Parent follow-up: retain the existing runtime unchanged. Any later free route must first pass a clean common-rig Walk bind with visible phase differences, intact anatomy, grounded contact, and an engine-compatible influence cap before additional roles can be processed.
