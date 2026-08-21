# Event 018 cave-monster visual closure handoff

Date: 2026-08-10.

Disposition: `complete` for the bounded static 3D package under the user's explicit no-HOI4-testing override. Fresh actual-byte mesh and action reimports, multi-view textured previews, five-frame loop proofs, runtime/export hash equality, parent-reviewed counters, and durable sourced-audio evidence close the worker-owned package. Audible playback and live HOI4 consumer behavior were not tested and are not claimed as in-game evidence.

## Scope and mutation boundary

This audit inspected only Event 018 cave-monster runtime model/action evidence and relevant durable documentation. It made no provider, balance, paid, Blender, adapter, or HOI4 call; consumed zero credits; did not change runtime assets, gameplay, GFX, entity, sound, adapter, dependency, configuration, or skill files; and did not stage, commit, delete, or replace evidence.

## Dependency evidence

- MESHY_API_KEY was present and nonblank before repository intake; its value was not printed.
- Dependency lock SHA-256: `D764E440754241E58A066A7BE8F95F97B7D682B3568AC9FF46D49A33C092EF16`.
- Meshy live-schema lock SHA-256: `DBB9CAD7FB12AFE81ECA05A2F381EF4251C035F4D22BF17856A2F6D41F16A62D`.
- Current Blender HOI4 adapter config SHA-256 at this audit's final read: `7757DCF814D748A0C1F3B792B7DB7BBC03B3338C168D4BDDE2E1BFD93BF1B3E5`. The fresh evidence-generation requests record the earlier config SHA-256 `225D5BE4E7517B2C340EDF2D0F7AD522A7940664B09A7A193F68C5941D45748B`; both expose adapter `chaosx_blender_hoi4` 1.2.2, the same cave-monster override, and the required `reimport_export` operation. The config was concurrently modified outside this audit and was not edited here.
- Locked route: official `@meshy-ai/meshy-mcp-server` 0.4.0 at git head `d8c77d1cb897e345eb41d38b510b8391b1664346`; no route call was made.
- Locked static evidence stack: Blender 5.1.2 build `ec6e62d40fa9`, `chaosx_blender_hoi4` 1.2.2, and checksum-locked `io_pdx_mesh` 0.91.0.
- Historical provider lineage remains legacy Meshy task `019fd394-e30c-7fbb-b0da-ee8078b86c38`, 20 estimated and 30 consumed credits. This audit estimated and consumed zero credits. Meshy 7 is required for future generation.

## Runtime and selected-export identity

The runtime mesh, four animations, and three model DDS maps exactly match the temporary selected-export copies byte-for-byte:

| Runtime file | SHA-256 |
| --- | --- |
| `resources_found_cave_monster.mesh` | `60C256EC1D958F77A93B6F9019A4B7C60072EA2F6B13E69C3672B84C474A491C` |
| `resources_found_cave_monster_idle.anim` | `A8EA9301744231054D3DA131AAF7D2EF264E13FD48A5F737325BA531DC9762D0` |
| `resources_found_cave_monster_move.anim` | `077D8ADCB45484215DB7BA6F4F45D95B184785358441DA67980B0D061EB52246` |
| `resources_found_cave_monster_attack.anim` | `13D54654770BD0E82846F847F4CDD14535755F061BA83DB2254F821FD2BB19AA` |
| `resources_found_cave_monster_death.anim` | `5A4677B24D0CB4ED3F506DDB1666B263AABF6D3CDB098255560DF6F773E1601A` |
| `resources_found_cave_monster_diffuse.dds` | `A876F57B87A36A79FE7A320D4445BD112CBA957474028E1E5680C0439626FE11` |
| `resources_found_cave_monster_normal.dds` | `9EF36A184A57A7BD451A6F90C6CB23D50CFC884EE6EE7FBF0958ABB0F3309D19` |
| `resources_found_cave_monster_spec.dds` | `9CFC7A88676CE46E4F017381DB38860BDBF84555C1BC59020C2D0FE4D2B88CDF` |

## Mesh, attack, and death review

- Fresh mesh reimport request `69348683ca2b4b2481bca993744b230c` confirms 17 bones, 30,000 triangles, zero degenerate faces, zero negative-scale objects, and zero loose or non-manifold position-welded edges.
- Mesh contact sheet `blender/previews/review/cave_monster_runtime_mesh_contact_sheet.png` has SHA-256 `F1E258E8E826FB0A49F6A551A2C977D39CD0197BE59F60F67B042F6EE8DA04D9`. Front, left, rear, right, three-quarter, top, and underside review shows a coherent textured armored quadruped without missing major parts or visible clipping.
- Attack request `26750574db2648e7b8f6d64b2460e9f5` and contact sheet SHA-256 `8B4F516607373D74D83E464A3685D8FBB87BDE304FFF17839EF78C27105D997C` show a readable grounded strike without visible shear. Validation JSON SHA-256 is `6BF2E600ED18A9C4A21406263ADA7547E8F7526C29E6DEE8616733090803A609`.
- Death request `bf087c00dd584a0580fac55b7f24e091` and contact sheet SHA-256 `D726E978A44FFD0C7687F449BC20DCAE6706B6A55C055C363F81E7764704D08A` show a readable grounded collapse without visible shear. Validation JSON SHA-256 is `5189A30A5FE4996B29909E5E75EA73079E5F9B10FB5F93E99AD96A53CBCD4C9B`.

## Idle and move five-frame proof

Idle request `c3231525b22440b6bb02d50b6324dc28` reimported the actual selected idle bytes and sampled frames 1/13/25/37/49. Ground contact ranges from `-0.0000001863` to `+0.0000121742` source units.

| Idle frame | Decoded front-view RGBA pixel SHA-256 | Interpretation |
| ---: | --- | --- |
| 1 | `8B07975634E686A3AA35200BB135B201012E405BBFC56AB67656F03E9E74798F` | neutral |
| 13 | `8BC073279891613E1084278D289FA609E3F0E932EFBE7D6E4836D884FD339F2E` | first quarter differs |
| 25 | `8B07975634E686A3AA35200BB135B201012E405BBFC56AB67656F03E9E74798F` | exact neutral return |
| 37 | `F465AFD73EB3692AB0BF285F6BB03BED56B4A244C4C86D2A68B52D602556E02C` | third quarter differs |
| 49 | `8B07975634E686A3AA35200BB135B201012E405BBFC56AB67656F03E9E74798F` | exact neutral return |

Move request `b6d51f89323a4d359187fc2e8354caee` reimported the actual selected move bytes and sampled frames 1/7/13/19/25. Ground contact ranges from `-0.0000001974` to `+0.0000131577` source units.

| Move frame | Decoded front-view RGBA pixel SHA-256 | Interpretation |
| ---: | --- | --- |
| 1 | `8B07975634E686A3AA35200BB135B201012E405BBFC56AB67656F03E9E74798F` | neutral |
| 7 | `949F11F95F3FF398E670DDB6BC38A4DEC6B9E971DA0A590762FB3CD7938AC1C8` | first quarter differs |
| 13 | `8B07975634E686A3AA35200BB135B201012E405BBFC56AB67656F03E9E74798F` | exact neutral return |
| 19 | `5763A4CFDC4B0504BC678C543A82E354769493092CD491B43AF5ECBC8B50CEA9` | third quarter differs |
| 25 | `8B07975634E686A3AA35200BB135B201012E405BBFC56AB67656F03E9E74798F` | exact neutral return |

The combined contact sheet is `blender/previews/review/cave_monster_runtime_idle_move_quarter_contact_sheet.png`, 724,637 bytes, SHA-256 `FC5D8A8AB3CCA0BE8143B7767DC55EE710E60CC7D4691C825958C8C5E03258AB`. Independent visual inspection confirms restrained but readable quarter-phase body, head, and limb movement. The earlier first/middle/last proof falsely suggested static loops because both authored loops return to neutral at midpoint and end.

Validation JSON hashes are `1EB9B669B27AC7E58C03C5692018458F15B34062B8F35D6A108CADF96DED1247` for idle and `9F11A0E52C627AB279D5A6AD1070F019102A6666EE1C88A9E9DE640B84BAD42E` for move. Adapter result hashes are `B197096A0D2613C5D2FB3FF29D23D0A032C91CA507E110FC7D4971E1F221C813` and `17601C4701E9432B8C089ECE21418FB6D71CDACA441A312A62993BF45368EED7` respectively.

## Counter and audio companion disposition

The parent-reviewed counter package remains PASS: five large 152 by 42 two-frame strips and five on-map 60 by 12 two-frame strips have inspected installed-vanilla consumers, correct alpha bounds and frame behavior, vanilla olive-green large normal states, grayscale disabled states, and distinct family silhouettes.

The sourced-audio package has four licensed immutable originals, recorded source URLs and licences, checksums, normalized derivation recipes, seven runtime mono 44.1 kHz 16-bit PCM cues, zero clipped samples, and documented action synchronization points. Six reconstructed cues reproduce the runtime bytes exactly; movement foot 02 differs only at the last sample by one 16-bit least-significant unit after 12,347 identical samples. Audible playback was not performed in this visual audit and remains an explicit caveat, not a source-provenance or recipe blocker.

## Remaining caveats and temporary-folder disposition

- HOI4 was not launched, as explicitly waived by the user. Normal-map-zoom presentation, live entity-state transitions, runtime sound playback, and audible density are not claimed.
- This is static worker-package closure, not in-game completion. Only the parent may close the overall Event 018 goal.
- Retain `docs/assets/018_resources_found/models_3d/cave_monster/` and `docs/assets/018_resources_found/models_3d/cave_monster_static_closure/` while the overall Event 018 goal remains active. They are evidence workspaces, not runtime dependencies, and no runtime reference points into them.
- Delete the complete event-scoped temporary workspace only after the parent has reconciled all durable evidence and genuinely closes Event 018. This audit did not delete, move, or overwrite any evidence.

## Files changed

- `docs/plans/018_resources_found_plans/subagent_handoffs/cave_monster_3d_model_handoff.md`.
- `docs/plans/018_resources_found_plans/018_cave_monster_3d_integration_addendum.md`.
- `docs/systems/resources_found_cave_monster_model.md`.
- `docs/events/018_resources_found/assets.md`.
- `docs/plans/018_resources_found_plans/subagent_handoffs/event018_cave_monster_visual_closure_2026-08-10.md`.

No simplification or fallback was introduced. The only skipped meaningful validation is live HOI4 and auditory playback, both disclosed above; the user explicitly waived HOI4 testing.
