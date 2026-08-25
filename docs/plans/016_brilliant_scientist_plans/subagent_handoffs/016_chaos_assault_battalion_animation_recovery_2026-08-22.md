# Chaos Assault Battalion animation recovery handoff

Status: `blocked_provider_source_tasks_expired`

Owner scope was limited to `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion` and this handoff. No shared adapter, gameplay, runtime wiring, GFX, entity, sound definition, or unrelated asset file was edited. No commit was created.

## Outcome

The existing provider idle and move actions were verified as genuine skeletal Meshy outputs and remain accepted. The existing attack and death actions were rejected on visual and reimport evidence. The semantic defend, support-attack, retreat, and training aliases remain forbidden and were not retained as final actions.

Six dedicated official Meshy animation-library actions were prepared, but no new animation task was accepted. The live provider no longer recognizes the recorded rig task, and a fresh rig request against the immutable accepted remesh task also failed because that provider task has expired. The locked rig schema accepts only an extant provider task ID or a provider-accessible model URL. The package contains immutable GLB/FBX downloads but no durable provider URL, and the locked route exposes no local-file upload argument.

Conditional identity-preserving Meshy 7 regeneration was subsequently authorized only if the archived approved reference was a Meshy7-suitable T-pose. Direct inspection rejected that gate. `refs/original/meshy_input.png` is the authorized generated source with matching SHA-256 `6F2A53C3632B632544211ECD56B40103D2F41C4FBCA9799CA3BA2C7206ADA74F`, but it depicts the subject in a three-quarter, arms-down stance holding a projector rather than a clear T-pose. It is also opaque 24-bit RGB rather than native-alpha. No regeneration was submitted and no geometry identity decision was made.

## Dependency and route evidence

- Environment hard gate: passed.
- Official Meshy MCP package: `@meshy-ai/meshy-mcp-server` `0.4.0`.
- Locked compatibility revision: `meshy-7-v4`; exact image model identifier: `meshy-7`.
- Meshy route: verified; tool schema exposes `meshy_animate(rig_task_id, action_id)` and `meshy_rig(input_task_id | model_url)`.
- Blender: `5.1.2`, build `ec6e62d40fa9`.
- Repository Blender HOI4 adapter: `1.7.0` from the dependency lock.
- `io_pdx_mesh`: `0.91.0`, locked checksum `A68359D2B2CFC4B62D11D11D30674C256486772206F4D60DF9DD4A987575D9D6`.
- Clean probe result: `hard_gate=passed`, Meshy route `verified`, no findings, balance `894`.

The inherited geometry job records `ai_model: meshy-6`; that historical lineage was preserved exactly and was not relabeled as Meshy 7. No geometry generation was performed in this recovery.

## Existing action audit

| Role | Provider task | Action ID | FBX SHA-256 | Result |
| --- | --- | ---: | --- | --- |
| idle | `019fd3d3-c281-75de-af1b-84dd17508035` | 0 | `2AF98AC72EB4C6F9747AA2D74C339C3C72FEB92D0CDA8B8EE351CDB5E0F91B8B` | Accepted: genuine multi-frame provider skeletal motion, credible idle, looping endpoints, reimport ground near zero. |
| move | `019fd3d3-c9d5-7b4c-a56c-4aee0e32134a` | 123 | `3CB8DDC259A01504AA21C3A9A0CD5542635C0CD251DB7B8F277E01C6E8A84E2A` | Accepted: genuine unsteady walk, credible locomotion, looping endpoints, reimport ground near zero. |
| attack | `019fd3d3-c591-75df-8b74-60fb021890fd` | 4 | `AE889BA88592D4784A2A4D9C5F42878317BFCCA317B11B26E1149D9B676439D0` | Rejected: genuine motion but generic wide crouch without the projector aim, discharge, recoil, and recovery evidence required for this role. |
| death | `019fd3d3-c7db-7b4b-9808-b122fde0ae02` | 8 | `B3D83CAC7023B9C0CB40C9261147A756F812970095A7A2C6E0506DEE6F2FD0C7` | Rejected: articulated source motion, but final exported reimport has `1.2829219103m` ground clearance and visibly floats. |

Adapter import reports show 24 matched driven bones and 249 source F-curves for each inherited provider FBX. Existing phase previews were reviewed directly. No manual, transform-only, static-pose, procedural, or semantically reused motion was accepted.

## Prepared dedicated action map

| Required role | Official Meshy action | Action ID | Source preview SHA-256 | Phase-sheet SHA-256 |
| --- | --- | ---: | --- | --- |
| attack | `Walk_Forward_While_Shooting_inplace` | 690 | `D7004A6C79C9E02587E2DA718A20ACED9361D9C2FEEFDE41C7A8DCFCE2031802` | `7BA84239C3D89857A435A196CABE82AE86CF6C51E7C5B9BEF63018C5D73E830B` |
| defend | `Block1` | 138 | `7F29811BE238317315ACC479498F69951B70759B3C6F6459AD03079955D06EEB` | `66F9FFB0166D9DE6B1EB5DF09136347B5A323278B76BBD8354B580EB56AE2CC2` |
| support_attack | `Walk_Backward_While_Shooting_inplace` | 680 | `244371D75D001186180271AB744C44F22C0A7BEC9A7619F68DECB9D4D2D76F38` | `A0E68D1267DF9AA72AD236E7F3E4353D11030CF9969C1EC84AAC94C01F5EB56E` |
| retreat | `Walk_Backward_inplace` | 679 | `4A8C979CE61657D09E8F1B891BB53EC475CA5689D004932D7050C92E5E72D2EC` | `191933095F8302AED59369884471A8FD808C63E556D77C70CCD243107031C397` |
| training | `Boxing_Practice` | 87 | `E66A01E067B8908CBCA01EE1B8F58F886D3548A98E84D1EDF2A8C9FE5423E0D2` | `C76A489E7C09B2EAE86FC5A76BEBBA8D7FC29F1E5AFC80CFA26A8962A64204A4` |
| death | `Shot_and_Slow_Fall_Backward` | 185 | `20DD89454C7118DE546661AFF2B056142A4E89FA926B3E497E8946EBA7D8A511` | `59DA5E1777CBE66EB54C574074CBFD95E359446E139172601C24AF226DBF412E` |

Evidence is under `docs/assets/chaos_warfare_system/models_3d/chaos_assault_battalion/evidence/action_library_candidates/`. The phase sheets show role-specific genuine motion: forward aiming and shooting, blocking, backward aimed shooting, backward retreat locomotion, multi-phase boxing practice, and shot reaction through collapse, impact, and settling.

## Provider failure lineage and credits

- Stale rig: `019fd3cc-e4cb-74bc-aa20-5522b3a4ec9a`.
- Immutable accepted remesh source: `019fd3c8-68d8-7997-8bb6-3a2b013910c7`.
- `provider/responses/006_meshy_get_task_status.json`: provider reports the rig task was not found on any endpoint.
- `provider/responses/007_meshy_animate.json`: the first prepared action submission, attack action `690`, was rejected as `Resource not found`; no task ID was created.
- `provider/responses/008_meshy_rig.json`: identity-preserving fresh-rig request against the accepted remesh task was rejected as `Input task not found`; no task ID was created.
- Request/response hashes, respectively: `D96E418CC632AE4817936A21104F0D9CF88D99D7E588FD7F6E3A651C356ABED4`, `CD6CE3EF5C0C200F08FA8834019DC128FBF7B426FF093895848B87AB58B152B0`, `9907249BF393F9EC1F2678F20CD070C596EC2B30389DEC149023BF02F52749A5`, `758C4DC736E964DC6B8C1777095DAC4A8FF92BAEB68DDFC66EB803365A588487`, `89506647DC090546D038710205B40ED8CD53B9F27A720DC6B1F5EFB64876B2D9`, and `11E2A80FD71548A57A6D5D83BBDE58C52359222AFB99298E6C9247B86AE31391`.
- Balance before: `894`; balance after: `894`; consumed recovery credits: `0`.
- Planned but unconsumed action tranche: six animations at three credits each, estimated `18` credits. A replacement rig would have been estimated at `5` credits.

## Export and reimport status

The accepted idle and move exports and their existing actual reimport reports remain unchanged. No new FBX/GLB action download, Blender import, grounding correction, phase preview, `.anim` export, or actual export reimport could occur because no new provider action task or artifact existed. The rejected attack/death exports were preserved in place and were not overwritten. No Blender mutation was attempted after the provider hard blocker.

## Parent work and safe recovery boundary

Attack, defend, support attack, retreat, training, and death remain blocked. Do not bind aliases or the rejected old attack/death as final actions. A future safe recovery must first make the exact accepted body available to Meshy as an extant provider task or durable provider-accessible model URL, then create a fresh official Meshy rig and submit the six action IDs above. Alternatively, the parent can authorize creation and approval of a new identity-preserving, native-alpha, clear T-pose Meshy 7 input derived from the existing source before regeneration. The current archived image itself must not be represented as rig-safe.

After successful provider outputs exist, the locked Blender adapter can import each source action, correct ground contact while preserving substantive provider motion, render meaningful phases, export PDX `.anim`, and reimport each actual export. Parent-owned runtime wiring and live in-game validation remain pending and out of scope.

## Simplifications, omissions, and blockers

No fallback animation, semantic alias, manual body motion, procedural motion, static pose, or whole-rig transform substitute was used. The package is incomplete because six dedicated provider-backed roles, their downloads, Blender processing, PDX exports, and reimport evidence are blocked by expired provider source tasks.
