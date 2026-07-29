# Chaos Redux 3D Model Pipeline

This package owns the bounded production path from one approved reference image
to a candidate Hearts of Iron IV `.mesh`/`.anim` package. It does not perform
gameplay, entity, `.asset`, `.gfx`, localisation, or in-game wiring; those remain
parent-agent responsibilities after the runtime handoff has been reviewed.

## Start gate

Every entry point checks `MESHY_API_KEY` before path discovery, image generation,
balance checks, or local Blender work. If the variable is absent or blank, stop
and tell the user to run:

```powershell
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
```

The user must restart the shell or Codex afterward. The key is passed through the
environment only and is never written to configuration, manifests, logs, or
handoffs.

## Installed routes

The trusted project configuration is `.codex/config.toml`:

- `meshy`: the version-pinned official `@meshy-ai/meshy-mcp-server@0.4.0` wrapper.
- `blender_hoi4`: the repository-owned, job-root-bounded adapter exposing only
  named Blender operations.
- `blender_lab_dev`: the official Blender Lab MCP checkout at tag `v1.0.0`, kept
  disabled for production because its general-purpose code bridge is broader
  than the production allowlist.

The locked local dependencies are recorded in
`.tools/3d_pipeline/config/dependencies.lock.json`. Blender 5.1.2 is launched
headlessly through its executable at
`C:/Program Files/Blender Foundation/Blender 5.1/blender.exe`; the user-facing
shortcut is retained and verified at
`C:/Users/klimp/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Blender/Blender 5.1.lnk`.
The checksum-locked `io_pdx_mesh` extension is installed in Blender's user
extension directory and is loaded directly by the worker for deterministic
export and reimport.

Run the environment probe from the repository root with:

```powershell
py -3.13 .tools/3d_pipeline/verify_environment.py --probe-meshy
```

## Autonomous job lifecycle

`init_pilot_jobs.py` creates deterministic job roots under
`docs/assets/chaos_redux_3d_model_pilots/models_3d/<asset_slug>/`. A brief-only
job generates exactly one final Meshy input image at
`refs/original/meshy_input.png`; a ready reference is preserved and used as-is.
No side-profile sheet, turnaround board, collage, or multi-view Meshy input is
created. The one-image count and checksum are recorded in the reference
preflight and input manifest.

`run_pilot.py` records each paid provider call before waiting, checks balance
before every paid tranche, downloads successful GLB/FBX results immediately,
and appends state transitions to `history.jsonl`. A paid task is never silently
retried. Existing task and download records allow a stopped run to continue
without spending a second generation tranche.

The official Meshy MCP server returns signed `assets.meshy.ai` URLs for rigging
and animation packages rather than local files. The adapter records those URLs
as provider lineage, validates the host, and fetches the signed artifact into the
job root with a checksum manifest. This is provider-artifact transport, not a
REST/API fallback; the API key remains environment-only. Exploratory conversion
tasks may remain in the append-only lineage, but a converted static file is never
selected as a substitute for a requested rig or skeletal action.

The provider candidate is passed to the allowlisted Blender adapter, which:

1. preserves provider-source objects and creates a working duplicate;
2. normalizes height, transforms, origin, triangulation, and PDX material tags;
3. records geometry/material/action metrics and renders multiple read-only QA views;
4. converts extracted textures through the repository DDS converter;
5. saves named Blender checkpoints;
6. exports through the locked `io_pdx_mesh` functions; and
7. reimports the exported files and writes proof reports.

Humanoid land-unit scale is calibrated against an imported read-only vanilla infantry mesh, not a generic human-height constant.
The current reference is `gfx/models/units/western_european_infantry.mesh` against `gfx/entities/units_infantry.asset#infantry_rifle_entity`: the main mesh is `7.351824` source units tall, the vanilla entity scale is `0.8`, and the resulting effective runtime height is `5.881459` units.
The custom pilot is normalized to the `7.351824` source-unit height before the same `0.8` entity scale is applied, while provider height remains a separate field because Meshy and HOI4 use different coordinate conventions.

Model textures use the profile's verified maximum dimension.
The current HOI4 model surface is capped at `1024` pixels on the longest side and final DDS headers are checked after conversion.
Custom `common/units` subunit ids must also register their generated unit texticons against a verified vanilla icon.

Each job contains provider requests/responses/tasks/downloads, Blender source and
checkpoints, texture evidence, exports, logs, validation, runtime handoff, and
screenshots/evidence. Final runtime files must be copied or staged outside
`docs/assets` before entity wiring.

## Pilot profiles

The first two bounded pilots are:

- `anomaly_signal_beacon`: a static occult signal beacon prop with one mesh.
- `anomaly_recon_trooper`: a standard humanoid reconnaissance trooper with
  `idle` and `attack` skeletal action roles.

Profile calibration is in `.tools/3d_pipeline/config/asset_profiles.json`.
Working triangle targets are intentionally lower than the provider preference
caps when the exporter requires controlled reduction; the job manifest records
that decision and the source-to-working geometry lineage.

## Runtime handoff

The parent agent must review the generated `runtime/handoff.md`, manifests,
checksums, material reports, action manifest, and reimport proof before creating
any `.asset`, entity, `.gfx`, or gameplay references. The worker may propose
stable model and action identifiers. In the normal route, a live consumer and
in-game screenshots move a pilot from a package candidate to overall workflow
completion.

## Live-validation status

The 2026-07-22 launch waiver is retained as historical evidence, but it is no longer the current runtime state. A subsequent Germany run exposed that the standalone showcase's history-only consumers were not visible. The showcase was repaired with an idempotent `on_startup` consumer and a tag-specific `on_daily_GER` repair hook that create the pilot division/template and set the pilot building in Brandenburg state 64, isolated province 9560; the pilot troop remains in province 6521. The custom building map row is `64;anomaly_signal_beacon_pilot_spawn;2995.00;9.70;1556.00;0.00;0`, with X and bottom-up Z selected from the installed `provinces.bmp` interior pixels for province 9560. The building effect selects the exact province with `province = { id = 9560 }`, while the template is created in Germany's country scope and the building and `create_unit` calls run in a direct state 64 scope. The latest user-run session still reports renderer geometry corruption and a missing building, so live completion remains unclaimed.

The unit pilot adds one runtime texticon registration in `interface/chaosx_3d_model_pilots.gfx`, reusing the vanilla infantry icon; it uses the vanilla-supported `PdxMeshAdvanced` material route with explicit diffuse, normal, and specular maps, and its move state binds a real Blender-authored in-place locomotion action; it does not add player-facing localisation keys. Any later runtime integration must follow the normal Chaos Redux asset and localisation rules in `AGENTS.md`.

## Known review items

Exporter performance is measured against the working triangle target; very dense
source meshes may require a lower calibrated working target. DDS conversion uses
the repository converter and records the backend used in the texture report. Any
boundary-edge, material-channel, action, or runtime-consumer warning remains a
review item until the parent resolves it or explicitly carries it forward.
