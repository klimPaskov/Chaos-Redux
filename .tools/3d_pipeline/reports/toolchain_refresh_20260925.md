# 3D toolchain refresh, 2026-09-25

## Installed routes

- Blender 5.2.2 LTS Windows x64 runs from the portable installation recorded in `config/dependencies.lock.json`; the prior 5.1 installation remains available for existing work.
- Blender Lab MCP server and add-on use upstream tag `v1.0.3` at commit `2cea8d566dde07fbac28a61d698909d69724e853` and the 5.2 add-on repository.
- The live Lab bridge listens on `127.0.0.1:9877`; its `execute_blender_code` call reported Blender `5.2.2 LTS` with both Lab MCP and io_pdx_mesh enabled.
- The repository-owned Blender HOI4 adapter remains at `1.10.51` and now launches Blender 5.2.2 with the compatible 5.2 io_pdx_mesh extension.
- Meshy MCP uses official package `0.5.2` and MCP SDK `1.30.1`; the unchanged repository patch adds the artifact selector and Text-to-Motion tools required by this pipeline.
- io_pdx_mesh remains at latest published release `0.91`; the original release archive is preserved and the separately locked archive changes the two removed Python `imp` imports and guards the removed Blender material `shadow_method` property.

The exact executable, add-on, archive, package, patched runtime, source revision, and checksum evidence is in `config/dependencies.lock.json`; the live Meshy input declarations are in `config/meshy_tool_schema.lock.json`.

## Compatibility evidence

- `verify_environment.py --blender-only` returned no findings for the installed Blender, Lab checkout/add-on, adapter, and io_pdx_mesh hashes.
- `verify_environment.py --probe-meshy` returned no findings, listed all 13 required tools in the patched 29-tool server, confirmed Meshy 7 in the image generation schema, and read the balance without submitting a paid task.
- The Meshy motion contract tests passed (3 tests), artifact compatibility tests passed (2 tests), and wrapper lifecycle tests passed (4 tests), including concurrent startup and process cleanup.
- Two simultaneous Lab tool-list verification processes caused one transient empty stdio response; the same combined Blender and Meshy verification passed when run sequentially, so Lab bridge probes should be serialized.
- A fresh adapter stdio process returned `blender_version = 5.2.2`, both exporter functions, and four available io_pdx_mesh operators from its `stone_cohorts` health call.
- The stone cohort checkpoint `docs/assets/012_africa/models_3d/stone_cohorts/blender/checkpoints/53_move_resume_20260908.blend` exported a skinned `.mesh` of 6,224,728 bytes and a 49-frame `.anim` of 43,281 bytes through Blender 5.2.2 and the patched io_pdx_mesh extension.
- The exported bytes reimported as three mesh objects, one 29-bone armature, and action `io_pdx_rigAction` spanning frames 1 through 49.
- The temporary mesh SHA-256 was `3F293AA2D0F7A5C57331DF35D1F3BB3CE185A7A0A1C36D20FDA67437DF7238ED`; the animation SHA-256 was `AE559DD7F8764CADDBAF67A6A334C772A85FAE1729FEC5681C81277D9E27DE09`.
- Reimport warned about texture files because the probe exports were placed in an isolated temporary directory without copied textures; this probe establishes mesh, skin, armature, and animation compatibility rather than finished material appearance.

## Activation and limits

The updated `.codex/config.toml` enables the Lab authoring route with an explicit tool allowlist and points it at port 9877; an already running Codex MCP server may retain the old Blender path until Codex reloads its MCP configuration.
The fresh adapter stdio probe used the updated configuration, while the in-session adapter tool still reported Blender 5.1.2 from its earlier process.
No paid Meshy generation, rigging, or animation task was submitted during this toolchain refresh.
No Hearts of Iron IV runtime test was run; the user owns live game validation.
