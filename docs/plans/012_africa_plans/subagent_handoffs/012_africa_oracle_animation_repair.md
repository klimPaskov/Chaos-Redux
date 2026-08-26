# Oracle Recon animation repair handoff

## Result

The accepted Oracle Recon animation package did not need a byte-level repair. All five `.anim` files are valid against the locked adapter/exporter evidence, contain their intended Meshy-sourced motion, reimport on the exported 24-bone rig, and exactly match the files already present in the parent-owned runtime folder.

No adapter/provider defect was proven; runtime consumer validation remains parent-owned.

## Files changed

- `docs/assets/012_africa/models_3d/oracle_recon/validation/oracle_animation_repair_audit_2026-08-26.md` — bounded dependency, action, hash, reimport, and read-only runtime-registration evidence.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_oracle_animation_repair.md` — this handoff.

No accepted checkpoint, `.mesh`, `.anim`, texture, runtime copy, gameplay file, GFX registration, entity definition, sound file, localisation file, spreadsheet, or unrelated dirty file was changed.

## Provider and source lineage retained

- Meshy 7 generation: `01a03996-6938-71f8-aec7-1d2b9c4b854c`, GLB SHA-256 `2B7598C2156F570AEDBB6032B1CB6E4E63E77E376DE02895E436C3FA4162D02E`.
- Remesh: `01a0399f-ec67-750d-a7cd-95d89bf18730`.
- Rig: `01a039a3-133e-7187-aeaf-30457d890033`, rig GLB SHA-256 `0842DF971A17DBDBB8CD9FE329E965ACF5FE186EFF8DBF16F255675C93F29677`.
- Idle: `01a039a5-21c8-7df7-ab4b-72e789dbe551`.
- Move: `01a039a5-eb2a-7241-814a-2dca7b8bd2c9`.
- Observation: `01a039a7-0e68-7e64-9876-8b979488d6b0`.
- Death: `01a039a7-c89d-7791-9413-6a7f753b73e8`.
- Accepted recon replacement: `01a039ad-b4c5-7a00-a2c0-0f87b3090390`, FBX SHA-256 `B102DD7F4FC83C39C6C1AB76841726ECBE85C6374FACDBF168C3E6BA14A138BC`.
- Rejected target-static recon remains rejected: `01a039a6-5a13-7e3a-a7c0-78d6710a6b16`.

No provider call was made during this audit. Estimated and consumed repair credits: `0`.

## Exact route evidence

- Health request: `chaosx_blender_hoi4_health`, request `287361179808413fa8e6404d54992575`, success.
- Read-only inspections: idle `719c05dedd704e1f988e1d727e53401c`; move `181f9e6abb9243e8a6b59edc59840ec9`; recon `cbb3a83471964eb79ab832676d8be937`; observation `9730bd6e51fa48a9b5b7ae5e8cbb3940`; death `7ccf6594377a403aad6f8dc0b22c507b`.
- Route versions: Blender `5.1.2` build `ec6e62d40fa9`; `chaosx_blender_hoi4` `1.10.14`; `io_pdx_mesh` `0.91.0`; Meshy MCP `0.4.0`, exact model lock `meshy-7`.
- The key-presence gate passed without exposing the key.

## Action and export decision

All actions are 30 FPS, have 168 processed F-curves, have no scale F-curves, and preserve substantive body motion. Idle and move close as loops. Recon shows real multi-phase raised-hand and head/body scanning and is the accepted fresh action rather than the rejected static candidate. Observation contains real multi-frame observation motion. Death contains stagger, collapse, impact, and settling to a terminal ground pose.

The selected hashes remain:

- Mesh: `4186EE95CAAD06A25CBA59862EF22842F01BFEFE5A3F0BC5A38B8FC4C1E7AA3A`.
- Idle: `B5556891348A21C683C31406D9DBD2C65C1075040CB59051610DF54D9F6C73A0`.
- Move: `367CE743DB2C58B0208B0798594FFEBC63265B269C12D89D8782212DD108730E`.
- Recon: `384A785EC2F8138D26CD9B568B689FC2199946747C8ACB5A2883FAEDA36F2E98`.
- Observation: `0945B7C0D2AE3870374A1AF2F7F14978E899F8AC8537BA131DD3C90D335E09FD`.
- Death: `25A5E5FAEF4C2A419E04F658D502356D3DEB642B22B4170FBC3AE9CA317028F2`.

Each runtime copy matches its selected export exactly. Because no failure was found, the allowed mutating adapter operations were deliberately not invoked and accepted evidence was not overwritten.

## Runtime registration result

The read-only runtime chain is internally consistent: `oracle_recon` selects sprite `chaosx_oracle_recon`; the GFX mesh definition maps all five IDs; the animation asset points those types to the correct basenames; the entity states reference those same IDs; and `meshsettings` uses `char1.002`, matching the exported mesh name.

The parent should concentrate live validation on whether the actual division/entity consumer reaches the expected state and how the engine handles the long one-shot recon action. The current death state also transitions back to idle after its terminal pose. These may affect perceived behavior but are parent-owned runtime semantics, not corrupt animation exports.

## Validation not performed

- No in-game validation or live entity-state observation.
- No runtime edit, resynchronization, or blind copy.
- No paid Meshy retry or balance check because no accepted action was shown to be broken.
- No local or procedural replacement motion.

The package is unchanged at the animation-byte level. The parent retains final wiring, live consumer, and in-game acceptance responsibility.
