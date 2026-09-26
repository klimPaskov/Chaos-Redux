# io_pdx_mesh upstream and Blender check, 2026-09-26

The latest published GitHub release is `0.91`.
The repository's `HEAD`, `refs/heads/master`, and `refs/tags/0.91` all resolve to commit `2249e35f80a1cc04ba4c2b8e4c650f36b18085db`, so the installed release contains the latest upstream revision at this check.
The dependency lock records that upstream commit, the original release archive SHA-256, and the separate Blender 5.2/Python 3.13 compatibility archive SHA-256.
The compatibility archive changes only the two removed `imp` imports and guards the removed `Material.shadow_method` property; Blender 5.2.2 loads the installed `0.91.0` extension from its `extensions/user_default/io_pdx_mesh` repository.

`verify_environment.py --blender-only` returned no findings for the installed files and locked hashes.
A fresh `chaosx_blender_hoi4_health` call reported Blender 5.2.2, io_pdx_mesh loaded, both export functions, and all four expected operators.
The stone cohort checkpoint exported a 6,224,728-byte skinned `.mesh` and a 43,281-byte, 49-frame `.anim` through that installed extension.
The exact exported bytes reimported as three mesh objects, one 29-bone armature, and `io_pdx_rigAction` spanning frames 1 through 49.
The temporary mesh SHA-256 was `1CC7824D494FB833EBDC6B7BBD5DB349613D6F7019B1C7D96DD4E353EF6BEDF6`; the animation SHA-256 was `AE559DD7F8764CADDBAF67A6A334C772A85FAE1729FEC5681C81277D9E27DE09`.
The isolated reimport directory did not contain the checkpoint's texture files, so the probe validates exporter, mesh, skin, rig, and animation compatibility rather than final material appearance.
No gameplay or asset source files were changed, and no Hearts of Iron IV runtime test was run.
