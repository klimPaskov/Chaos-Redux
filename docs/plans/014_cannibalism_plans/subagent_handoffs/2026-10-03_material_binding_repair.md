# Event 014 material binding repair

Disposition: implemented for the Scavenger Warband material registration correction and the bounded binary audit.
Acceptance basis: the user-authorized Event 014 continuation and correction of a confirmed runtime consumer mismatch within the installed seven-model package.

The Scavenger Warband mesh registration binds its diffuse, normal and specular overrides to the exported object `mesh.001`, stream index 0.
The previous `mesh_node.001` registration named an object absent from the installed mesh.
The source-approved export also contains `mesh.001`, so the correction follows both the selected source and installed runtime candidate.

## Changed files

- `gfx/entities/014_cannibalism_units.gfx`: correct the Scavenger Warband `meshsettings.name`.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_scavenger_warband_v2_runtime_handoff.md`: align the material binding description with the exported object.
- `docs/plans/014_cannibalism_plans/evidence/2026-10-03_runtime_unit_bindings_before.json`: preserve the actual source hashes and the mismatched registration.
- `docs/plans/014_cannibalism_plans/evidence/2026-10-03_runtime_unit_bindings_after.json`: preserve the corrected source hashes and decoded package audit.
- `docs/plans/014_cannibalism_plans/evidence/2026-10-03_scavenger_source_runtime_comparison.json`: identify the approved export and its installed derivative separately.
- This handoff records the repair and its evidence boundary.

## Meaningful validation

Read-only decoding through the vendored `pdx_data.py` checks seven installed meshes, their 56 animation files and exact bone order, animation sample counts and finite values, 21 DDS maps, and 86 registered state audio cues.
All seven material object names match after the correction.
All 56 actions have multiple samples and nonconstant quaternion data; this detects empty or static files but does not establish pose, contact or motion quality.
Every checked state cue resolves to a sound definition and a decoded signed 16-bit, 44.1 kHz WAV file, and every explicit cue time lies within the corresponding animation's last sample time.
The runtime binaries have identical before-and-after hashes.

The Scavenger source export has SHA-256 `32797fd2487009d0f25b64546b5842d7e687ac9aedf5c71c7c17c75be851f19b`, matching the existing selected-source manifest.
Its installed mesh has SHA-256 `72532f027fd58a7d2f7ef0151a192140b1698a5193df0130132ee390023af308`.
The complete decoded trees differ only in three material texture basenames, which point to the unit-specific runtime DDS files; all other decoded geometry, skeleton, skinning and locator data are equal.
The files are consequently documented as a source and adapted runtime derivative, rather than byte-identical copies.

## Reference evidence

- Offline wiki: `paradox_wiki/Entity modding - Hearts of Iron 4 Wiki.md`, lines 19–50 and 52–120, SHA-256 `74ff51b8ea0924281eb1c067300b52dc373ea9d112341bbb9c34fcb1a11d2d6a`, establishes the mesh-to-entity and animation registry structure.
- Installed vanilla precedent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/infantry.gfx`, lines 335–347, SHA-256 `6439fb7fc1a94e9b2f20368f18bd73526b2abb9a559b62e58a2c2768396e71d4`, uses `meshsettings.name = BEL_infantry_weapon_rifleShape`, stream index 0, and `PdxMeshAdvanced`.
- The referenced vanilla `gfx/models/units/BEL_infantry_weapon_rifle.mesh` decodes to that exact object with one material stream; SHA-256 `060bb33cc6097633b1bd1424611ce67777690d17e890df6229841dc766a01cc0`.
- No `meshsettings` or `pdxmesh` section was found in installed markdown documentation under `documentation/` or `gfx/models/`.
  The installed source precedent and actual binary decoding supply the material-node evidence; no missing documentation section is invented.
- The connected `hoi4.reference_search` and `hoi4.source_lookup` requests timed out after 600 seconds.
  The wiki-only single-section search and single-definition 12-line lookup retries also timed out after 600 seconds.
  The local source and binary audit is not represented as a successful MCP result.

The separate CXT check confirms that `chaosx_test_country_sync_registered_content` only marks registered content pending in the current shared helper at `common/scripted_effects/chaosx_test_country_effects.txt:442`.
Event 014's tag-scoped daily hook therefore does not grant content and requires no change.
Installed on-action documentation at `common/on_actions/_documentation.md:7–19` and the offline wiki `On actions` section at lines 91–137 confirm the tag-scoped hook pattern.

## Simplifications, omissions, and blockers

No new simplification or fallback was introduced by this repair.
No model, animation, DDS, WAV, unit statistics, AI weights, portrait, or gameplay outcome was changed.
No player-facing wording changed, so the catalog workbook remains unchanged.
This bounded repair does not establish completion of Event 014 or a clean live `error.log`.

Five archival `manifest.json` paths named by `docs/assets/014_cannibalism/models_3d/family_jobs.json` are absent: Feast Guard, Feast Cohort, Bone Guard, Siege Eaters and March Predation Column.
Their runtime meshes and actions are installed and decoded; missing source receipts are a distinct evidence gap and remain unresolved.
The new byte receipts do not replace provider, authorship, rights, visual acceptance or reimport provenance.
Portrait archive/review work, probability coverage, event completion review and orchestrator-owned live evidence remain separate outstanding work.

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-3d-model-pipeline`, `chaos-redux-event-assets` and `chaos-redux-shared-git-commit`.
The model-pipeline skill's generalized material-binding gate is reviewed and committed separately from this runtime repair.
