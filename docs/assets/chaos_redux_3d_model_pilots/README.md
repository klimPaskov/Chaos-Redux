# Chaos Redux 3D model pilot package

This package is the autonomous pilot fixture for the Meshy -> Blender -> PDX workflow.
It contains one static prop pilot and one animated humanoid pilot, each generated from exactly one Meshy input image.

## Pilots

- `models_3d/anomaly_signal_beacon/`: static occult signal beacon `.mesh`, PDX texture set, checkpoints, provider lineage, reimport proof, runtime handoff, and static building consumer.
- `models_3d/anomaly_recon_trooper/`: 24-bone humanoid `.mesh`, idle and attack `.anim` files, PDX texture, checkpoints, signed provider-artifact lineage, reimport proof, runtime handoff, and unit consumer.

## Completion gate

The two model packages are export/reimport complete and are wired to the production runtime registrations under `gfx/` and `common/`.
The earlier 2026-07-22 live-validation waiver remains recorded in `validation/in_game_validation_waiver.json`, but a later Germany run exposed a history-only consumer gap.
The standalone showcase now has an explicit startup consumer and Germany-only daily repair hook for the pilot division and building.

The first live run reported an oversized unit DDS, a missing custom unit texticon, and an undersized black unit.
The DDS, icon registration, and vanilla-infantry scale calibration are corrected and re-exported.
No post-fix live HOI4 renderer screenshot is stored or claimed yet; the two `runtime/screenshots/` folders remain empty until the repaired showcase is visually verified.

The full Chaos Redux content set has separate launch errors outside this pilot surface.
The user-facing standalone `3d_pipeline` copy contains the same runtime registrations and artifacts plus the repaired live-consumer hooks; its runtime path is the bounded proof route for the two pilots.
