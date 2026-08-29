# Event 020 rat Walk bind: adapter-version blocker

## Status

`superseded`

The parent explicitly superseded the stale 1.10.0 literal and authorized the matching locked/live adapter 1.10.1 route. The resumed production result is recorded in `2026-08-24_event020_rat_quaternius_walk_bind_blocker.md`.

The bounded Walk-only bind did not start because the live and locked Blender HOI4 adapter version does not match the exact version authorized by the parent brief.

## Hard-gate evidence

- `MESHY_API_KEY`: present and non-blank; the secret value was not read or recorded.
- Repository environment verifier: `python -B .tools/3d_pipeline/verify_environment.py` returned `findings: []`.
- Environment report: `.tools/3d_pipeline/reports/environment_report.json`, SHA-256 `005C9BDA7EF621ABAA216357F6B65D5CF0ACD1955C4324EE6389AE3A93610259`.
- Parent-authorized adapter: exactly `1.10.0` with `.tools/3d_pipeline/adapter/blender_worker.py` SHA-256 `9A5F6DD7C0A1F4925B8A2DB59939C7FD30F886A77FD3CEAF89495B40160C10D6`.
- Current dependency lock adapter: `chaosx_blender_hoi4` version `1.10.1`.
- Current dependency lock: `.tools/3d_pipeline/config/dependencies.lock.json`, SHA-256 `3E89F7B1DEAC705DE894E7FE07A0C3C33FE66066851EBEA09D6A4C62F3FC1A9C`.
- Current adapter config: `.tools/3d_pipeline/config/blender_hoi4_adapter.json`, adapter version `1.10.1`, SHA-256 `14BD97E12F6799E5FFC907136481D146AA43D9132775D05DA9A66A2DDBB099D7`.
- Current worker: `.tools/3d_pipeline/adapter/blender_worker.py`, SHA-256 `10B47B95854750B2657D303D123E11B3AABFA1FBEDBF5E118A74C879351954ED`.
- Live health result: adapter `chaosx_blender_hoi4` version `1.10.1`, request id `ce2b44aeb9bf447c8a61024862074f19`, Blender `5.1.2`, `io_pdx_mesh_loaded: true`.
- Live health receipt: `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/logs/adapter/ce2b44aeb9bf447c8a61024862074f19.result.json`.

## Work not performed

- No Meshy/provider balance or paid operation was called.
- Credits estimated and consumed: `0`.
- No Blender scene inspection beyond the mandatory health probe.
- No br-n518 `automatic_bone_heat` or `bone_distance` bind.
- No Quaternius donor inspection or bind.
- No checkpoint, preview, action processing, export, reimport, runtime file, gameplay file, GFX, entity, sound, localisation, or spreadsheet change.

## Required resolution

The parent must reconcile the task authorization with the repository-owned dependency lock. Resume only with a fresh bounded prompt that authorizes the exact locked/live adapter version and worker checksum, or after an authorized repository owner restores and verifies the required `1.10.0` route. The model worker must not edit adapter source, config, or locks.

## Files changed by this subagent

- `docs/plans/020_black_plague_plans/subagent_handoffs/rat_walk_bind_adapter_version_blocker.md`

No simplification or fallback was used.
