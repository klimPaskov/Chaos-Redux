# Material binding skill maintenance handoff

Date: 2026-10-03.
Disposition: `implemented` for the bounded skill update only.
Acceptance basis: the explicit parent instruction to generalize actual-byte material-binding validation to all custom model consumers, permit read-only parent decoding, edit only the model-pipeline skill plus this handoff, and make no commit.

## Changed files and behavior

- `.agents/skills/chaos-redux-3d-model-pipeline/SKILL.md`: moved the exported-name requirement out of the static-building material paragraph into one shared gate under `PDX export and reimport evidence`.
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_material_binding_skill_handoff.md`: this handoff.

Before: explicit `meshsettings.name` matching guidance addressed static buildings, while the general actual-byte decoding gate did not explicitly require comparison with runtime material bindings.
After: before final wiring, every custom model consumer, including articulated units, requires decoding or reimport of the selected actual `.mesh` bytes, comparison of each `pdxmesh` `meshsettings.name` and `index` with actual object-node and material-stream identities, and verification of shader and texture references.
The runtime handoff retains byte identity and the binding comparison, and a changed selected runtime mesh requires repeating that check.
Read-only parent decoding and binding review do not reopen model production.

## Evidence and rationale

The parent brief reports the repeated integration failure: a `meshsettings.name` retained a prior candidate's node name after the runtime binary changed, even though the `.mesh`, `.anim`, and DDS files existed and decoded.
This is parent-supplied task evidence, not a fresh binary inspection performed by this skill-maintenance pass.
The update captures the reusable distinction between decodable assets and verified consumer bindings without placing event-specific names or task history in the skill.
The existing building shader, packed-channel checks, stream-coverage rules, and building-consumer audit remain intact.

## Exact skill hunks

```diff
@@ -389,7 +389,7 @@
-For static map-building materials, use the shader from the installed vanilla building consumer. With the current vanilla surface this is `PdxMeshAdvancedSnow`. The GFX `meshsettings.name` must equal the actual exported mesh object name, such as `Mesh_0.001`. Provider labels, job slugs, and guessed names are not accepted. Verify packed PDX normal and specular channel statistics before synchronizing runtime DDS files.
+For static map-building materials, use the shader from the installed vanilla building consumer. With the current vanilla surface this is `PdxMeshAdvancedSnow`. Verify packed PDX normal and specular channel statistics before synchronizing runtime DDS files.
@@ -507,6 +507,8 @@
+Before final runtime wiring for every custom model consumer, including articulated units, decode or reimport the selected actual `.mesh` bytes and compare each `pdxmesh` `meshsettings.name` and `index` against the decoded object-node names and material-stream names and indices, then verify the shader and texture references. Provider labels, job slugs, prior-candidate names, file existence, and successful `.mesh`/`.anim`/DDS decoding alone do not prove material binding. Retain the byte identity and binding comparison in the runtime handoff, and repeat the check when the selected runtime mesh changes. The parent may perform this read-only decoding and binding review without reopening model production.
+
```

## Validation and ownership

Read `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-3d-model-pipeline`, and the official `skill-creator` skill.
Inspected the shared checkout status and target-file diff before editing; the model-pipeline skill had no pre-existing staged or unstaged change, and the requested handoff did not exist.
Reviewed the resulting skill diff: exactly two local hunks, with one shared binding paragraph replacing the building-only name instructions.
Ran `python C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-3d-model-pipeline`; result: `Skill is valid!`.
The prohibitions on programmatic bones, weights, and keys and the user-only live HOI4 testing boundary were left unchanged.
No gameplay identifiers, runtime bindings, model binaries, tools, other skills, or AGENTS.md were edited, and no staging or commit was performed.

## Parent follow-up and limits

Review the two skill hunks and apply the binding check to the selected runtime bytes during integration.
No AGENTS.md, subagent-routing, or generated-definition update is required: production and final-wiring ownership remain unchanged.
Actual model decoding, runtime-binding repair, and live-game evidence were outside this maintenance assignment and were not performed.
The documentation update is complete with no simplifications or blockers; it does not establish completion or correctness of the cannibalism model integration.
Skills updated: `chaos-redux-3d-model-pipeline`.
Skills created: none.
Skills read and left unchanged: `chaos-redux-subagents` and `skill-creator`.
