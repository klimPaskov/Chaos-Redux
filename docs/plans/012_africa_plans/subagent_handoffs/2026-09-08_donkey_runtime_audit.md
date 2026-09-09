# Donkey plague-carrier runtime audit

Date: 2026-09-09

Disposition: The bounded Donkey plague-carrier model and synchronized-audio runtime tranche passes this read-only integration audit. This finding covers the nine model payloads, seven WAV payloads, model and sound registries, entity bindings, action-state behavior, material streams, scale, facing evidence, and the existing spawn-scoped selection caller. It does not establish live-game validation or completion of the wider Event 012 asset package.

## Source-of-truth map

| Surface | Evidence | Disposition |
| --- | --- | --- |
| Parent integration closure | `docs/assets/012_africa/models_3d/plague_carriers/validation/plague_carriers_blender_repair_20260906/final_parent_integration_closure.json` | Closed with nine model and seven audio payloads recorded, all reported destination hashes matching their selected sources. |
| Accepted model and runtime payloads | `docs/assets/012_africa/models_3d/plague_carriers/validation/plague_carriers_blender_repair_20260906/final_runtime_copy_manifest.json` | `installed_parent_integration_companion_gaps_explicit`; its nine destination payloads are recorded as installed and verified. |
| Accepted Blender source | `docs/assets/012_africa/models_3d/plague_carriers/blender/checkpoints/16_forward_yaw_blender_repair_20260908.blend`, SHA-256 `B4E16129CA828C644ABF0077C4CA2B5F577EBAE21D560FCF8439A44B3A06E020` | Accepted unchanged by the parent for this integration tranche. |
| Action registry | `gfx/models/units/animation_012_africa_strange_forces.asset` | Five existing animation types resolve to the installed action files. |
| Mesh and entity registry | `gfx/entities/012_africa_strange_forces.gfx` and `gfx/entities/012_africa_strange_forces.asset` | Implemented and internally consistent for `chaosx_plague_carriers_mesh` and `plague_carriers_entity`. |
| Synchronized audio payloads | `docs/assets/012_africa/models_3d/plague_carriers/audio/final/20260908_synced_pcm16/copy_manifest.json` | `installed_parent_integration_companion_gaps_explicit`; its seven destination payloads are recorded as installed and verified. |
| Runtime sound registry and attribution | `sound/012_africa_strange_forces_sound.asset` and `sound/012_africa/units/plague_carriers/ATTRIBUTION.md` | Seven sounds and seven effects resolve; public-domain and CC BY-SA 4.0 provenance is retained. |
| Counter | `docs/assets/012_africa/models_3d/plague_carriers/counters/manifest.md` and `docs/assets/012_africa/models_3d/plague_carriers/counters/source/prompt.txt` | Unresolved: the retained counter depicts an armored amphibious carrier creature rather than the accepted pack donkey. |

## Exact model payload audit

Every installed runtime file has the manifest byte count and SHA-256. No mismatch was found.

| Runtime file | SHA-256 |
| --- | --- |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_death.anim` | `D8B61ECBF3712DC483CB5E9970297C54F815BF7BC995A642B077C8C8B27B3D10` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_deploy.anim` | `7AC50DEA1EE533C96F28F142AF4E5F8AB97C66E3F9110005EB207E562E2CE063` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_idle.anim` | `FA0606B675F48F46D041D8DECEE8B6D7120CB15CC4DD31E84E7B4F9FF58BBAF3` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_move.anim` | `0BE90261BDFBB4949EBBD17A1B4142DD1478C87A9F3D5E0DD65551F12CF65B46` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carrier_release_containment.anim` | `0EAE6E35D86487AB39DEE7D568DA700DEAD3C287EDD60C460D39E6CC7A191527` |
| `gfx/models/units/012_africa_plague_carriers/chaosx_plague_carriers.mesh` | `EAE6702AB88559A6F9194939DE91C63AF2AF1CC95E37DD0DF15642920982B2CF` |
| `gfx/models/units/012_africa_plague_carriers/texture_0.dds` | `082B9E3B57BE4396B23E8716BE03393ABEFDC1604C84BFB7EF070AF46568758A` |
| `gfx/models/units/012_africa_plague_carriers/texture_normal.dds` | `059B71BCABEDF1F8F49BCE4005B687FFB05F7DE948FB5E806E3070F060E48074` |
| `gfx/models/units/012_africa_plague_carriers/texture_specular.dds` | `764862278C87C3E866808A824C6DB2EE826E889B851E1F04DAF46B8E61C94344` |

The exact mesh contains 25 bones and 25,000 triangles across four exported streams: `mesh.001[0]` has 21,845 triangles, `mesh.001[1]` has 3,035, `plague_carriers_cargo_hatch_frame[0]` has 72, and `plague_carriers_cargo_hatch[0]` has 48. The four current `meshsettings` rows bind those exact object/index pairs to the installed diffuse, specular, and normal textures with `PdxMeshAdvanced`.

The model manifest records `-Y` forward and `+Z` up, and each of the five actions carries a distinct export receipt and actual-byte reimport receipt from the yaw-corrected export. The reimported death proof records ground contact at frame 81, and the manifest preserves eleven terminal contact vertices supported by `pack_L` or `hanging_basket`. The cargo-hatch design evidence sets a 68-degree peak opening; parent visual review accepted the frame-29-to-35 opening phase, closure by frame 53, and the actual-byte frame-81 left and three-quarter terminal views with cargo and side-pack support.

## Registry, state, and terminal behavior audit

| Entity state or states | Mesh action id | Registered animation type | Frames at 30 FPS | Runtime behavior |
| --- | --- | --- | --- | --- |
| `idle`, `training` | `idle` | `chaosx_plague_carrier_idle_animation` | 1-61 | Looping; each state emits its idle cue once at state time 0 through `trigger_once = yes`. |
| `move`, `retreat` | `move` | `chaosx_plague_carrier_move_animation` | 1-41 | Looping; both states emit the move cue at 0.333333 seconds. |
| `attack`, `defend`, `support_attack`, `deploy` | `deploy` | `chaosx_plague_carrier_deploy_animation` | 1-61 | One-shot; each emits the deploy cue at 1.400000 seconds and returns to `idle`. |
| `supply_load` | `release_containment` | `chaosx_plague_carrier_release_containment_animation` | 1-61 | One-shot; emits release at 0.933333 and impact at 1.733333 seconds, then returns to `idle`. |
| `death` | `death` | `chaosx_plague_carrier_death_animation` | 1-81 | One-shot and terminal; it has no `next_state`, and its cue starts at 1.333333 seconds. |

All five mesh action ids resolve through the unchanged animation registry to the installed files. The entity applies `scale = 1.0` exactly once, so no second scale factor exists in the Donkey consumer chain. The working-tree diff for the two shared Africa entity registries is confined to the Donkey block: the old single material binding is replaced by the four exported streams, the synchronized cue rows are updated, and the death return to idle is removed.

## Exact audio payload and cue audit

All seven source handoff files and installed runtime files match the manifest SHA-256 and byte counts. Direct RIFF header inspection confirms uncompressed PCM format 1, mono, 44.1 kHz, and 16 bits per sample for every runtime WAV.

| Runtime WAV | SHA-256 | Duration | Consumer and fit |
| --- | --- | --- | --- |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_select.wav` | `BCCE79F413EF09980760B29D8609510F7F5A4178FC914E6F624660255770AF6D` | 1.600000 s | Spawn selection branch; it is independent of an animation window. |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_idle.wav` | `07A17640CE9623603F7B619195F731BA337210A3E01DF277DCB864432E85BCB2` | 2.000000 s | Starts at 0 in the 2.000000-second idle/training cycle and ends at the cycle boundary. |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_move.wav` | `F2DE930650CB0C69AC18655B69A0691296990FB42E79B4171B090A00059E1190` | 1.000000 s | Starts at 0.333333 in the 1.333333-second move/retreat cycle and ends at its boundary. |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_deploy.wav` | `16F30D575A1E9BBA3830C697DA8C52CB7CADA9E2BC52BA518AF13FCE3C588378` | 0.600000 s | Starts at 1.400000 in the 2.000000-second deploy action and ends at its boundary. |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_release_containment.wav` | `BFCF0F3B4AC1C223C0796A70D0FC6B2C697D08E25D0F7445EA47E14235228A87` | 0.766667 s | Starts at 0.933333 and ends at 1.700000 in the 2.000000-second release action. |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_impact.wav` | `54D89B852702DCEC97796DDC69D6FB2B30BADC584049256916E55044AA7A3407` | 0.266667 s | Starts at 1.733333 and ends at the 2.000000-second release boundary. |
| `sound/012_africa/units/plague_carriers/chaosx_plague_carriers_death.wav` | `BF2D33AD765776C9A74F9C0148C3F15C55C37E169B8C537C347E38647D971C46` | 1.333333 s | Starts at 1.333333 and ends at the 2.666667-second death boundary. |

The runtime sound registry maps each WAV to one sound and one non-looping sound effect, and every entity event names a defined effect. The existing selection consumer is `common/scripted_effects/012_africa_action_effects.txt:6970`, whose plague-carrier branch calls `scoped_sound_effect = "chaosx_plague_carriers_select_sfx"` at line 6973 after the requested kind resolves to `constant:africa_strange_force_kind.plague_carriers`.

The attribution document retains the public-domain status and source-page URLs for `Cough 1` by ezwa/PDSounds and `Air duster` by stephan/PDSounds. It retains Camshaft64's `Metal Clanging Noises` attribution, direct source URL, CC BY-SA 4.0 license URL, and the derivative transformation notice.

## Documentation reconciliation

| Document or instruction | Disposition | Reason |
| --- | --- | --- |
| Final model runtime copy manifest | Implemented, with validation limits retained | The manifest records `runtime_copy_status = installed_by_parent_per_verified_integration_report`, and the parent closure records all nine model payloads. |
| Synchronized PCM16 copy manifest | Implemented, with validation limits retained | The manifest records `runtime_copy_status = installed_by_parent_per_verified_integration_report`, and the parent closure records all seven audio payloads. |
| Counter manifest and source prompt | Unresolved | The manifest calls the counter complete while the retained prompt explicitly requests a squat amphibious carrier creature; this conflicts with the accepted pack-donkey identity. |
| Live consumer behavior | Blocked from this audit | The agent did not run Hearts of Iron IV; user-owned live-game validation remains outside this read-only audit. |

## Remaining limitations

- No audio audition was performed in this audit, so the exact hashes, formats, cue timing, registration, and licensing are verified while perceptual suitability remains unvalidated here.
- The three named historical original OGG files are absent; the runtime package preserves trimmed, faded, PCM16-converted descendants whose existing source-page evidence remains documented.
- The current counter has the wrong armored-creature identity for the accepted pack donkey and requires a parent-owned replacement decision and later consumer review.
- Parent visual acceptance covers the specified actual-byte repair evidence, but live-game scale, orientation, animation playback, event sound playback, and terminal pose behavior remain unvalidated by this agent.
- The bounded Donkey tranche passes with no payload, registry, material-stream, action-chain, scale, terminal-death, sound-resolution, or cue-window mismatch; this does not complete other Event 012 models or the wider asset package.
