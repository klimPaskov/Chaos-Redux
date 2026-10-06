# Unit texture tool implementation handoff

Disposition: implemented within the authorized shared pipeline scope.
Parent integration, independent t062 mip repair, all 119 installed maps and the focused texture commit are recorded in `pipeline_report.md` and `pipeline_evidence/texture_delivery/manifest.json`.
Intermediate pending-batch statements below are superseded by those artifacts; source-backed material repairs remain package work.

The parent-authorized scope was new modules under `.tools/3d_pipeline/textures/`, focused tests, and this handoff; adapter, MCP, lock, runtime asset, and root README ownership remains with the parent.

## Files changed

- `.tools/3d_pipeline/textures/__init__.py`
- `.tools/3d_pipeline/textures/atlas.py`
- `.tools/3d_pipeline/textures/bc_codec.py`
- `.tools/3d_pipeline/textures/cli.py`
- `.tools/3d_pipeline/textures/conventions.py`
- `.tools/3d_pipeline/textures/dds.py`
- `.tools/3d_pipeline/textures/delivery.py`
- `.tools/3d_pipeline/textures/README.md`
- `.tools/3d_pipeline/tests/test_texture_tools.py`
- `docs/plans/unit_fix_2026-10/texture_tools_handoff.md`

No runtime texture, model, GFX, `.asset`, Blender adapter, dependency-lock, skill, or root README file changed.

## Implemented behavior

`textures.bc_codec` is a deterministic NumPy BC1/BC3 encoder with legacy DXT1/DXT5 headers and a complete mip chain through 1x1; the current encoder version is `chaosx-bc-blockfit-1.2.0`.

Diffuse output uses BC1 when alpha is unused and BC3 when source pixels or an explicit consumer declaration use alpha; normal and specular output use BC3.

Output dimensions default to 512 pixels, never upscale, and accept 1024 only with a concrete written justification.

Every texture requires a grayscale UV occupancy mask; default dilation is 12 pixels, valid dilation is 8–16 pixels, and a UV-wrap exception can set dilation to zero only with an explicit reason.

`textures.dds` validates FourCC, header and pixel-format sizes, required flags and texture caps, dimensions, mip count, exact compressed payload length, and decoded BC1/BC3 pixels; its input-only BGRA path handles the existing uncompressed DDS sources without allowing BGRA runtime output.

The converter also decodes DDS base pixels through Pillow and compares them with the repository decoder; it checks every prepared mip, per-channel MAE/p95/max/PSNR, image RGB PSNR, diffuse alpha bounds, and full-chain dimensions.

Mips at least 8x8 require RGB PSNR of at least 25 dB and per-channel MAE at most 16; smaller one-block mips retain their measurements and use a 15 dB and 32 MAE floor to account for BC endpoint quantization.

`textures.conventions.repack_provider_normal` packs provider R to PDX R/G, source G to PDX A by default, and B to zero; green inversion requires a separate hashed handedness-evidence file, and no operation synthesizes normal detail.

`textures.conventions.packed_normal_cleanup` copies occupied existing G into R, preserves occupied G/A, clears B, sets unused pixels to flat `(128, 128, 0, 128)`, and dilates only from the explicit UV mask.

Provider specular generation requires exact provider roughness/metalness hashes and explicit class masks; it uses cloth G 40–90/A 60–100, skin G 110–160/A 120–160, leather G 120–160 with provider-derived alpha, steel G 180–255/A 150–180, stone G 60–90/A 50–70, and fur G 20–40/A 40–70.

The provider specular recipe masks B to zero outside the explicit steel mask and sets steel B to `max(200, original provider metalness)`; without a metalness map it uses B=200 inside steel.

Provider metalness variation in the 200–255 steel range is retained, while values below 200 inside steel are raised to 200 and every known nonsteel provider blue value is removed from the runtime derivative.

The specular processing report separates original provider metalness statistics from derived B statistics, records the number of occupied pixels changed by the explicit mask, includes original provider roughness/metalness/class-mask path and SHA-256 rows, and confirms that provider input files remain unchanged.

The class-aware specular gate rejects constant G, mean B over 5 outside the explicit steel mask, steel B below 200, and mean A over 110 for nonwet classes; the decoded BC3 gate permits up to five blue-channel values of block-compression quantization, while the raw recipe output must meet the full 200 minimum.

The normal gate measures occupied texels and enforces G/A standard deviations 15–35, mean tangent tilt no greater than 0.35, R/G mirror error no greater than 5 values, and the zero-blue convention.

Compression-only conversion is available without material provenance; it preserves occupied source channels, records semantic checks as unresolved when needed, and can still pass its DDS, mip, decoded-fidelity, alpha, source-hash, and CAS checks.

The CAS manifest binds source bytes, target preimages, occupancy masks, material provenance, staged outputs, QA reports, and archived source bytes; installation rechecks the complete set before atomic replacement and attempts rollback after partial batch failure.

## Integration API

Add the repository's `.tools/3d_pipeline` directory to `sys.path`, then import `textures.delivery` and the lower-level modules.

```python
from textures.delivery import prepare_batch, convert_batch, install_batch, resolve_uv_mask
from textures.conventions import packed_normal_cleanup, repack_provider_normal, build_pdx_specular_from_provider
from textures.bc_codec import build_dds_from_mips
from textures.dds import parse_dds_header, decode_mip_rgba
```

`prepare_batch(repo_root, request_json, staging_root, manifest_path)` validates a repository-relative request and writes a prepared manifest without converting files.

`convert_batch(repo_root, manifest_path, execute=False)` is a dry-run by default; `execute=True` writes immutable input copies, prepared PNGs, staged DDS files, per-item QA reports, and the updated install manifest under the separate staging root.

`install_batch(repo_root, manifest_path, execute=False)` revalidates and reports CAS targets without writing; `execute=True` backs up current targets, installs the staged DDS files, verifies final hashes, and updates the manifest.

`resolve_uv_mask(repo_root, mask_manifest_path, pdxmesh, texture_name, expected_mesh_sha256=None, expected_registration_sha256=None)` resolves the exact mask row and checks its mask, mesh, registration, dimensions, and coverage hashes.

Request items require `id`, `role`, `source_rel`, `target_rel`, and `occupancy_mask_rel`; optional fields are `conversion_scope`, `size`, `size_justification`, `dilation_px`, `skip_dilation_reason`, `alpha_used`, `minimum_coverage`, `expected_target_sha256`, and `provenance_rel`.

Use `conversion_scope: compression_only` for size/format/mip delivery; use `packed_normal_cleanup`, `provider_normal_repack`, or `provider_specular_recipe` only with the matching documented source evidence.

For the parent-rerasterized UV masks, the current manifest contains 38 PDX mesh records and 123 masks at 1024x1024 across 119 unique texture filenames; the recorded coverage spans 0.1824 through 0.9263.

The parent reports that the alien-infantry mesh.002 UV-wrap issue was resolved by rasterizing neighboring tile copies from the actual UV triangles; the current UV manifest has no unresolved issue rows, so the batch may use its verified masks without suppressing dilation.

The parent-owned batch path should keep all conversions in staging and use the captured target SHA values for CAS; this tool package has not applied the 119-map runtime batch.

## Evidence and validation

The user plan `C:/Users/klimp/Videos/chaos_redux_trailer/records/showcase/unit_fix_plan.md` has SHA-256 `1939B400CBA160C6D4903E37952E8E55EFDB1BFEACF0B4AB061E89C8792C79B2`; its lines 426–430 specify 512px default, justified 1024px, BC1/BC3 formats, full mips, occupancy-aware dilation, RRxG mapping, normal statistics, material-class recipe ranges, and the specular gates implemented here.

The offline `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md` snapshot has SHA-256 `74FF51B8EA0924281EB1C067300B52DC373EA9D112341BBB9C34FCB1A11D2D6A`; lines 19–43 cover mesh definitions, paths, animation references, and mesh scale, while lines 171–184 cover animation asset files.

The offline `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md` snapshot has SHA-256 `F8E3D4AD382F4E5F8E170492A484D090BAD62E3711CABFB5D3BF84E58AB32DD9`; lines 32–75 describe sprite texture paths and frame declarations but do not define model-material compression.

The offline `paradox_wiki/Font modding - Hearts of Iron 4 Wiki.md` snapshot has SHA-256 `B401070565A53CE4A37372CBB42116FEA85DB89710D39A2693038B2BF0EE4C26`; lines 51–56 describe general DXT1/DXT5 compression and transparency tradeoffs, and were treated as background rather than model-material authority.

The installed documentation directory was inspected and contains scripting documentation but no dedicated model-texture material page; exact local shader and installed texture files supplied the model-specific evidence.

The installed `gfx/FX/pdxmesh.shader` has SHA-256 `D16F4BF5CEFA60E873667E6AB3EE044B08FD67550BA93C3A5CCB627F79A994ED`; lines 470–478 read normal-map and specular alpha glossiness, and lines 523–527 map specular strength from G and metalness from B.

The installed `gfx/FX/standardfuncsgfx.fxh` has SHA-256 `0609C68F6819693A92300701F1B538FB7F606B7C9ED66AE47774B9D9897BA2D2`; lines 311–318 decode tangent X from G, tangent Y from negative A, and positive Z from the reconstructed vector.

The installed `gfx/entities/infantry.gfx` has SHA-256 `6439FB7FC1A94E9B2F20368F18BD73526B2ABB9A559B62E58A2C2768396E71D4`; lines 218–225 map `asian_infantry_rifle_mesh` to `gfx/models/units/asian_infantry.mesh` and its animation identifiers.

The installed `gfx/entities/units_infantry.asset` has SHA-256 `6AB4BE22BC0757C93F8132F7E247910592A5D8595EAF431D33F23DF03F32AA2D`; lines 497–507 bind `asian_gfx_infantry_entity` to that mesh and name runtime animation states.

The installed `gfx/models/units/asian_infantry.mesh` has SHA-256 `ACCB5F74E3E3484496BF27F6DF1F510AF382B0B3EF7A93FEF22E02826636938A`; its diffuse, normal, and specular files below were decoded read-only as the vanilla material precedent.

`gfx/models/units/asian_infantry_diffuse.dds` is BC1/DXT1 at 256x256 with 9 mips, 43,832 bytes, and SHA-256 `8AC109907C19118791B93A8DB40E5223020A1DCE7568CB4AD92F4C3D2B258CB7`.

`gfx/models/units/asian_infantry_normal.dds` is BC3/DXT5 at 256x256 with 9 mips, 87,536 bytes, and SHA-256 `9994FEF68328DF94FA2DF734174BAE697C3EC8CC5CD2F7566D451D6F0FB77A35`; decoded R/G mean absolute difference is 1.46, B is zero, G standard deviation is 18.28, and A standard deviation is 19.51.

`gfx/models/units/asian_infantry_spec.dds` is BC3/DXT5 at 128x128 with 8 mips, 22,000 bytes, and SHA-256 `DA13FED9B7F97E817190913CEB275CDBB55904E3A731B8779FC27E235FF4277C`; global decoded G standard deviation is 35.16, B mean is 4.75, and A mean is 62.69.

The installed PDX shader and texture references support the preserved provider-green default: the game shader negates the A tangent component, while the current local evidence does not establish a provider-specific green-handedness inversion.

The bounded `texconv` search found no PATH command or executable under Windows Kits, Microsoft DirectXTex program folders, `.codex`, Downloads, Tools, or the repository's `.tools/3d_pipeline`; the project now has an explicit native encoder instead of a silent uncompressed fallback.

The active Python environment used Python 3.9.12, NumPy 2.0.2, and Pillow 11.1.0; no Blender build, `io_pdx_mesh` operation, Meshy route, paid provider call, or source download was used.

The focused command `python -B .tools/3d_pipeline/tests/test_texture_tools.py -v` passed all 20 tests, covering deterministic BC output, full mip headers, legacy BGRA input, Pillow pixel decode, the t062 4x4 BC1 regression, alpha selection, mask-required dilation, PDX normal/specular gates, masked removal of nonmetal B leakage, steel B minimum and variation preservation, end-to-end provider source-hash reporting, source-hash preservation, dry-run behavior, 1024px justification, UV mask identity, and CAS conflict/rollback behavior.

A read-only roundtrip of the installed Asian infantry maps through the native encoder produced 256px BC1/9-mip diffuse at 43,832 bytes, 256px BC3/9-mip normal at 87,536 bytes, and 128px BC3/8-mip specular at 22,000 bytes; minimum per-mip RGB PSNR was 28.03 dB, 37.93 dB, and 34.38 dB respectively.

A 1024px BC3 full-chain encode completed in 4.095 seconds on the implementation environment and produced 1,398,256 bytes; this is a synthetic in-memory throughput probe, not an asset input or runtime texture.

The exact focused skill evidence read was `.tools/3d_pipeline/README.md` SHA-256 `8EF9049EEF31B5DCD18DD1A3856E11A7BD8D7CD6B32BD8B7AD8713E07F7E7669`, `chaos-redux-3d-model-pipeline/SKILL.md` SHA-256 `CA4FB9E9E52E91A6029E371254385BBC2BDFEFD2A4E2B973F88ADF551B0C1655`, `chaos-redux-event-assets/SKILL.md` SHA-256 `B7C197704BC758C7BAE97F6F14D7E209C8B010361329D6CE408B24E53544DF80`, and `chaos-redux-subagents/SKILL.md` SHA-256 `06079FB7E7C01BF09A5FEA1FFABDFBB73B99FCECDDD28EF7720415FBBCEEDA61`.


The dependency, Meshy-schema, and adapter lock/config files were read-only; the parent owns their shared-tree edits and no version or checksum was changed here.

## Bounded t062 repair

The parent-owned delivery manifest at `docs/plans/unit_fix_2026-10/pipeline_evidence/texture_delivery/manifest.json` remains `stage_failed` because item `t062` exceeded the unchanged 32-value per-channel MAE limit at mip 7, its 4x4 BC1 diffuse block.

The t062 source DDS SHA is `8ec5a0cab6ff3c96b78c53e7fdac46135a086b8aeb43edfd4d70594210416b15`, the UV mask SHA is `58757e90bcde8732bec350ab5083034c919a5251df294e3c9d727fa21ba62c81`, and the prepared-base SHA is `136d77788800e315a832f672f0d134f5ae147875662354eeebe08095b7ac27ae`.

Mip 7 contains four repeated source colors that cannot all lie on one BC1 interpolation line; the previous PCA/least-squares endpoints concentrated error in red, producing R MAE 33.5 while G MAE was 7.0 and B MAE was 17.0.

Encoder 1.2.0 adds a bounded source-color endpoint-pair search only for a single 4x4 BC1 diffuse mip block; it selects the source-derived endpoint pair minimizing maximum per-channel MAE, then total per-channel MAE, then RGB squared error, matching the gate's equal 32-value RGB channel bounds.

The search only uses quantized source texels plus the existing fitted endpoints and standard BC1 palette interpolation; it generates no texture detail and leaves all larger mips, BC3 maps, and DDS quality thresholds unchanged.

The repaired t062 mip has R MAE 25.5, G MAE 16.0, B MAE 7.5, RGB MAE 16.333, and RGB PSNR 19.503 dB, passing the existing 32-value channel bound and 15 dB small-mip floor; the previous mip had RGB MAE 19.167 and PSNR 19.609 dB, so the repair trades 0.107 dB aggregate PSNR for a lower worst-channel error consistent with the existing per-channel acceptance rule.

The repair DDS is `docs/plans/unit_fix_2026-10/pipeline_evidence/texture_delivery/repair_t062/t062_repaired.dds` with SHA-256 `14fd5f8cd58564bcae44689aac520dadc046d72ace6e418a5f22581d3a5a9e6c`.

Its QA report is `docs/plans/unit_fix_2026-10/pipeline_evidence/texture_delivery/repair_t062/t062_repair_qa.json` with SHA-256 `c7f0fc6e688af19ac58131608bff21f7d169134a474c122e53f51626abd40cd9`, and its lineage/CAS proof is `docs/plans/unit_fix_2026-10/pipeline_evidence/texture_delivery/repair_t062/t062_repair_proof.json`.

Mip 7 is the only DDS payload whose bytes differ from the failed 1.1.0 candidate; the header, dimensions, format, full 10-mip chain, all other mip payloads, original source, occupancy mask, prepared base, parent manifest, and parent candidate remained byte-identical during repair.

The parent may review the repair artifact and proof, then decide whether to replace the t062 staged candidate and reconcile its own manifest; the batch was not rerun, the parent manifest was not edited, and installation was not performed.

## Remaining parent work

The parent owns integration of this package into `chaosx_blender_hoi4_process_textures` or its batch wrapper, execution against the 119 runtime texture filenames, review of each staged report and per-class mask evidence, approved CAS installation, and final source-to-runtime synchronization.

The parent should retain semantic failures from compression-only maps as unresolved while accepting only their compression, mip, decode-fidelity, and CAS evidence; provider normal/specular repacks require their own source material provenance and passing semantic gates.

The parent still owns checkpoint and Blender export/reimport work, runtime material rebinding, in-game consumer validation, and the overall unit-fix completion claim.

No custom unit audio or counter work was performed because this task creates production tooling only; no Meshy credits were estimated or consumed, and no model-specific source, generation, sound, or counter artifacts were created.
