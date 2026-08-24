# Bone Riders adapter 1.10.7 reload gate

Status: blocked because the callable MCP process has not reloaded the repository-authoritative adapter.

The repository dependency lock resolves `chaosx_blender_hoi4` 1.10.7 and records the adapter source checksums. Adapter recovery commit `a3e0a1497b6926b025070267eb9c75bd00b77c93` and registration commit `7e3af24ac4af87b12cd49c782d89f998d7fab915` are present. The repository environment verifier completed with zero findings after a Meshy route probe.

Current lock receipts are:

- `.tools/3d_pipeline/config/dependencies.lock.json`: SHA-256 `2D8345866846B6E110F94C87D7F2300CB0886F8E06B0F23B091533413AC75A79`.
- `.tools/3d_pipeline/config/meshy_tool_schema.lock.json`: SHA-256 `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233`.
- `.tools/3d_pipeline/config/blender_hoi4_adapter.json`: SHA-256 `44D2F8A47758F1B7D2284D12D2559F8BE2A36DEE48C28E0F726C68618F921DB5`.
- Blender is 5.1.2 and checksum-locked `io_pdx_mesh` is 0.91.0.

The live health request `fe776868337d4ce1ae9e98a07ad62228` reports adapter 1.10.3, despite the 1.10.7 repository lock. The callable registry exposes only these 11 legacy operations:

1. `health`
2. `prepare_candidate`
3. `inspect_scene`
4. `process_textures`
5. `author_humanoid_rig`
6. `author_humanoid_actions`
7. `author_locomotion_action`
8. `export_mesh`
9. `export_animation`
10. `reimport_export`
11. `save_checkpoint`

The live `prepare_candidate` declaration is also stale: it does not expose the 1.10.7 `geometry_object_name` or `dual_source_base_rig` surface.

The approved three-entity architecture cannot be completed with that registry. It requires separate horse/rider geometry processing and independent professional-action transfer, but the live process omits `segment_creature_components`, `calibrate_creature_scale`, `import_animation_action`, `retime_animation_action`, `correct_action_grounding`, and `sanitize_runtime_candidate`. The local authoring operations are forbidden as final motion and cannot substitute for the missing sourced-action route. The adapter's inability to merge horse and rider actions is not itself a blocker because installed vanilla cavalry keeps them as separate child entities and propagates common states; the blocker is that this process cannot call the registered 1.10.7 operations needed to prepare those independent children.

No Meshy animation call was made. The planned eight distinct rider actions remain 24 credits, and total historical model spend remains 35 credits. Spending is paused because generated actions could not be safely imported, upper-body retargeted, synchronized by state and phase, exported, and reimported in this process.

Required recovery: restart or reload Codex MCP so live health reports 1.10.7 and the required structured operations are callable, then rerun the dependency and capability gates before any paid rider-action tranche.
