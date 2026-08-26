# Event 014 Scavenger Warband Runtime Handoff (v2)

Date: 2026-08-25

This handoff promotes the source-approved Scavenger Warband package from the retained Meshy 7 and Blender export evidence into the Event 014 runtime tree. It supersedes the earlier provisional handoff that described the package as a pending adapter review.

## Ownership and consumer

- Unit definition: `common/units/014_cannibalism_irregular_infantry.txt#cannibal_scavenger_warband`.
- Mesh registry: `gfx/entities/014_cannibalism_units.gfx#cannibal_scavenger_warband_mesh`.
- Entity state machine: `gfx/entities/014_cannibalism_units.asset#cannibal_scavenger_warband_entity`.
- Animation registry: `gfx/models/units/014_cannibalism/cannibal_scavenger_warband/animation_cannibal_scavenger_warband.asset`.
- Audio definitions: `sound/014_cannibalism_units_sound.asset#cannibal_scavenger_warband`.
- Runtime mesh and action root: `gfx/models/units/014_cannibalism/cannibal_scavenger_warband/`.
- Runtime audio root: `sound/014_cannibalism/units/cannibal_scavenger_warband/`.

## Provider and adapter evidence

The package uses one parent-approved source reference at `docs/assets/014_cannibalism/models_3d/cannibal_scavenger_warband/refs/original/meshy_input.png` with SHA-256 `0ECE0EF273CB498FA1335E4F7E4C445ECB292CDD77F6163B869B5C64EF3C765A`. Meshy 7 task lineage is recorded in `manifest.json` and `job.yaml`: image-to-3D `01a034bb-7129-716b-bc17-177ca0eb9a1a`, remesh `01a03967-eaff-72d3-a8a9-2ec3efa29a15`, rig `01a0396c-09fc-7026-b5b3-1210dbfa2f1c`, and verified attack source `01a0345b-25c0-7884-a669-a34ac60ff5a3`.

The final PDX mesh is 30,000 triangles, 14,666 source vertices, zero degenerate faces, zero non-manifold edges, and a calibrated source height of 7.351824760437012 with entity scale 0.8. Evidence is in `blender/reports/export_mesh.json`, `blender/reports/weights_sanitized.json`, and the eight action import/reimport JSON reports.

## Actions and state timing

All eight required roles are distinct exported skeletal actions at 24 FPS: idle, move, attack, defend, support attack, retreat, training, and death. The action files are copied from `exports/` and are registered in the runtime animation asset. Attack, support attack, and death transition back to idle; movement and retreat dispatch movement audio; attack dispatches two attack cues and one impact cue; training intentionally has no event because this package has no training source. Timings are bounded by the exported action lengths documented in the manifest and report set.

## Materials and audio

The runtime uses the retained PDX DDS derivatives: diffuse, normal, and specular. The runtime copies are named for the unit and are bound to the `mesh_node.001` material stream in the mesh registry. Six sourced audio derivatives are installed for selection, movement, idle vocal, weapon attack, weapon impact, and death. `evidence/audio_sources/ffprobe_and_hash_receipt.json` records PCM S16LE mono at 44100 Hz for every source and the runtime copies are byte-identical to the derived files.

## Archive cleanup boundary

Provider binary download caches and obsolete candidate galleries were removed during the 2026-08-25 Event 014 archive cleanup. Final `.mesh`, `.anim`, DDS, WAV, task receipts, provenance JSON, reimport reports, one representative pre-export checkpoint, and the source/approval manifests were retained. No runtime file points into `docs/assets`; the current manifest deliberately points at retained final exports and evidence rather than deleted provider binaries.

## Remaining review

The bespoke counter handoff remains parent-live-review pending, and live map-model rendering remains outside the agent workflow. Bone Riders and Network Cadre are separate gameplay consumers covered by the approved vanilla `cavalry` and `infantry` sprite decision, not unresolved custom-model packages, and are not represented by this handoff.
