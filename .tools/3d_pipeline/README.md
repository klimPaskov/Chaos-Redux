# Chaos Redux autonomous 3D model pipeline

This repository-owned package runs the bounded path:

~~~text
one approved reference image
  -> Meshy MCP balance and image-to-3D
  -> immediate GLB/FBX download and lineage
  -> allowlisted Blender HOI4 adapter
  -> Blender checkpoints and PDX material processing
  -> checksum-locked io_pdx_mesh .mesh/.anim export
  -> reimport proof, QA evidence, and runtime handoff
~~~

The start gate is intentionally strict. MESHY_API_KEY must already be present
in the process environment. The package never prints or writes the key. A
missing key stops before path discovery, reference generation, balance checks, or
provider work.

The live lock is in config/dependencies.lock.json. The current pilot lock is:

* Meshy MCP @meshy-ai/meshy-mcp-server@0.4.0
* Blender Lab MCP v1.0.0, commit
  03004fd0216bfe5e0a3d9ac9b47d5efadc3d78c4
* Blender 5.1.2
* io_pdx_mesh 0.91.0, archive SHA-256
  A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2

## Entrypoints

From the repository root:

~~~powershell
python .tools/3d_pipeline/verify_environment.py --probe-meshy
python .tools/3d_pipeline/run_pilot.py --asset anomaly_signal_beacon
python .tools/3d_pipeline/run_pilot.py --asset anomaly_recon_trooper
python .tools/3d_pipeline/run_pilot.py --all
~~~

The pilot runner creates missing job directories and evidence files. If a
provided brief does not contain a ready image, the parent Codex workflow must
create one through the approved image-generation route and place exactly one
refs/original/meshy_input.png in the job before the paid gate. No side-profile,
turnaround, or multi-view board is ever sent to Meshy. Blender may render QA
views after generation; those views are not provider inputs.

The official Blender Lab MCP route is available for isolated development
inspection. Unattended production uses
wrappers/run_blender_hoi4_adapter.cmd, which exposes only structured,
job-root-bounded operations. It does not expose arbitrary Blender Python or shell
execution to the pipeline.

Runtime source files are staged under .tools/3d_pipeline/staging for parent
review. docs/assets/... is evidence and working material, not a runtime source
root.
