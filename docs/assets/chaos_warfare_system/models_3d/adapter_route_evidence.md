# Chaos warfare facility model adapter evidence

The production route used the repository-owned `chaosx_blender_hoi4` adapter from `.tools/3d_pipeline/adapter` with the installed Blender 5.1.2 executable and `io_pdx_mesh` 0.91.0.

The adapter health operation returned Blender, extension, and operation capability data before production work began.

The desktop MCP health wrapper was attempted twice and did not return within its normal response window, so the same repository-owned adapter entry point was invoked directly through `uv --directory .tools/3d_pipeline/adapter run python`; this is the configured adapter path, not an alternate exporter.

The static export path now records `static_mesh_export_without_armature` when a job has zero armatures and retains the strict exactly-one-armature check for animated unit jobs.

Both jobs completed the adapter sequence of candidate preparation, texture relinking, PDX material packing, static `.mesh` export, and `.mesh` reimport proof.
