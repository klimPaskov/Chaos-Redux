# Dated release evidence

This directory holds dated evidence produced by adapter and verification runs.

Nothing in it is an input to the pipeline. The current generated snapshots are `environment_report.json` from `verify_environment.py` and `meshy_live_schema_probe.json` from `inspect_meshy_live_schema.py`.
Regenerate them after dependency changes; their timestamps and locked versions identify the installation actually checked.
The other dated files are records kept for history:

- `adapter_stdio_*`, `orphan_image_*`, `partition_image_consumers_*`, `stone_partition_preflight_*`, `explicit_batch_repair_1_10_47_*`, and `io_pdx_deployed_source_verification_*` record the adapter version and conditions of their original runs.
- `demonic_skin_batch_source_preconditions_1_10_47.json`, `demonic_native_skin_inventory_1_10_47.json`, `explicit_batch_skin_object_delta.json` and `explicit_batch_repair_1_10_47_v5_skin_rejection.json` document the batch skin-repair route that the pipeline no longer carries. They are retained as history; no code reads them, and no current operation produces or consumes them.

Do not edit these files by hand and do not treat a filename version as the current adapter version; the authoritative record is `routes.blender_hoi4_adapter` in `../config/dependencies.lock.json`.
