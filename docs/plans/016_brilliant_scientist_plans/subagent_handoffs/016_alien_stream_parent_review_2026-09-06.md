# Alien Infantry export stream parent review

Disposition: blocked pending a geometry-preserving export partition and matching runtime registration.

The user-approved Event 016 Final Completion Plan requires the existing Alien Infantry mesh to fit the verified exporter ceiling and pass actual-byte reimport.
The user forbids geometry regeneration and permits repair of the existing model.

## Current evidence

The active `gfx/models/units/alien_infantry/alien_infantry.mesh` has SHA-256 `A8740E95C5F12D63D656B58891A52E1F059EDA2CDBF55DB521968D3932F906B4`.
This matches the selected export documented in `016_alien_infantry_v13_runtime_closure_2026-09-05.md`.
Its companion text at `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/export/v13_firearm_preset_locator_closure_20260904/alien_infantry.txt` declares `p (float, 539991)` and `tri (int, 179997)` for the body stream.
The position array therefore contains 179,997 vertices, exceeding the recorded 65,535-vertex stream ceiling.
The active `gfx/entities/alien_infantry.gfx` registers only `char1.002`, index 0.

The preceding handoff explicitly records the adapter's contradictory `maximum_stream_vertices = 1` result.
That summary field is invalid evidence for this export.
Successful Blender reimport establishes that the importer can read the file, but does not establish that its stream fits the engine limit.
The previous stream acceptance conclusion is rejected on this specific ground.
Other action, material, audio, and locator claims retain their individual review status.

## Required repair and acceptance

Partition the preserved skinned geometry into bounded streams while retaining its appearance, topology, materials, weights, skeleton, muzzle attachment, and accepted action data.
Verify that the selected operation supports skeletal meshes.
Measure the resulting position and triangle-index arrays directly from each exported stream and verify the applicable limits against the installed toolchain and vanilla references.
Reimport the resulting mesh and affected animations from their actual bytes, then review deformation and weapon contacts.
Register every exported stream in the active GFX and synchronize runtime copies only after parent review.

The bounded repair is assigned to `alien_stream_repair`.
No runtime file was changed by this review.
The overall Event 016 goal remains incomplete.
