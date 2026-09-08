# Portal Raider runtime audit

Date: 2026-09-08

Disposition: The bounded Portal Raider model, entity, sourced-audio, and retained-counter runtime integration is implemented in the current workspace and passes the checks described below.
This is filesystem and source-evidence validation after parent integration; it is not live-game acceptance or a claim that every package-level consumer is complete.

## Source-of-truth map

| Surface | Evidence | Finding |
| --- | --- | --- |
| Selected model payload | `docs/assets/chaos_redux_3d_model_pilots/models_3d/portal_raider/runtime_copy_manifest.json` and `final_asset_manifest.json` | All fourteen selected files are installed byte-exactly; rejected historical meshes are not selected by runtime wiring. |
| Action roles and cue times | `final_action_crosswalk.json` | Ten exported and actual-byte-reimported roles define the runtime loop, transition, and event-time contract at 24 FPS. |
| Animation registry | `gfx/models/units/animation_portal_raider.asset` | All ten animation types resolve to their selected runtime files. |
| Mesh and entity | `gfx/entities/portal_raider.gfx` and `gfx/entities/portal_raider.asset` | The three material streams, ten animation ids, ten entity states, scale, terminal death, sound cues, and muzzle effects match the accepted manifests. |
| Audio | `evidence/audio/runtime_proposal/runtime_sound_copy_manifest.json`, `sound/portal_raider.asset`, `sound/portal_raider/*.wav`, and `sound/portal_raider/ATTRIBUTION.md` | Twelve PCM16 WAVs are installed exactly, the source ledger is preserved as the attribution prefix, the runtime derivative addendum is present, and all sound and soundeffect references resolve. |
| Counter | `evidence/counter/manifest.json`, `interface/portal_raider_system.gfx`, and the two runtime counter DDS files | Both retained two-frame counter strips match their evidence hashes and the registered large/on-map sprite consumers. |
| Common unit consumer | `common/units/016_brilliant_scientist_project_forces.txt` | The `portal_raider` sub-unit uses sprite token `portal_raider`, which resolves to `portal_raider_entity`. |

## Model payload and geometry

All fourteen source files and runtime destinations match their manifest SHA-256 values and byte counts.
The exact runtime mesh hash is `3B63FF39642713334223C8820F500E0DC48251DCE093876F1AC2F711E9CB68B9`.
Because the runtime mesh is byte-identical to the selected export, the final asset proof applies directly: 45 rig bones, 29,662 triangles, and three streams containing 20,000, 8,630, and 1,032 triangles.
`gfx/entities/portal_raider.gfx` binds `mesh.003` indices 0 and 1 plus `portal_rifle` index 0 to the selected diffuse, specular, and normal DDS files with `PdxMeshAdvanced`.
`portal_raider_entity` applies scale `0.8` exactly once.

The exported locator evidence identifies `portal_raider_muzzle_locator`, parent bone `weapon`, and `registered_for_export = true`.
Attack, defend, and both support-attack discharges use this locator with the resolved shared `alien_laser_muzzle_particle` and `alien_laser_muzzle_flash` definitions.

## Action and event audit

| Role | Runtime policy | Event evidence |
| --- | --- | --- |
| idle | Loops | Bounded electrical pulse at 0.000000 seconds with `trigger_once = yes`. |
| move | Loops | Movement cues at 0.000000 and 0.666667 seconds. |
| attack | One-shot to idle | Muzzle discharge at 0.833333 seconds. |
| defend | Loops | Muzzle discharge at 1.083333 seconds. |
| support_attack | One-shot to idle | Muzzle discharges at 0.750000 and 1.666667 seconds. |
| retreat | Loops | Movement cues at 0.000000 and 0.833333 seconds. |
| guard | Loops | Bounded electrical pulse at 0.000000 seconds with `trigger_once = yes`. |
| portal_arrival | One-shot to idle | Arrival at 0.000000 and movement contact at 0.666667 seconds. |
| wounded | One-shot to idle | Impact at 0.416667 and movement contact at 1.166667 seconds. |
| death | Non-looping and terminal | Death cue at 0.333333 and impact at 1.916667 seconds, with no `next_state`. |

All ten registry-to-mesh-to-entity chains and all crosswalk event markers pass.
The installed electrical pulse is exactly 44,100 samples, or 1.0 second at 44.1 kHz, and its soundeffect has `loop = no`; idle and guard use one bounded trigger-on-entry pulse rather than a sustained electrical loop.

## Audio and attribution

All twelve runtime WAVs match the runtime sound-copy manifest source hashes and byte counts.
The runtime `sound/portal_raider.asset` contains twelve sound definitions and seven soundeffects; its only difference from the reviewed proposal is the installed header comment.
Runtime `ATTRIBUTION.md` has SHA-256 `BDDAB9FFCAC8345D0A2914E31EDE7C917D8A6119A38B25AF6BE8C3EA8D611041`.
After newline normalization, its complete prefix matches `evidence/audio/licensing/source_ledger.md`, and its appended runtime-derivative section accurately records mono 44.1 kHz PCM16 conversion, the bounded one-second electrical trim and fades, the preserved ten-second source, direct CC BY 4.0 and CC BY 3.0 license links, the CC0 link, and the runtime manifest path.
The `portal_raider_select` soundeffect is registered, but no per-subunit selection consumer is available or wired; this intentional limit avoids substituting a tag-wide infantry voice consumer.

## Counter verification

The retained large counter at `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds` matches SHA-256 `4236DF5183605AF540D44339EED96F29B2B59A40D9F82E1472C5178963EF920E` and the required 152x42 two-frame layout.
The retained map counter at `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds` matches SHA-256 `FB009C5EEED40C1AAD867D15C066422CB142AA24DC2C38D7311857BFA284D85E` and the required 60x12 two-frame layout.
`interface/portal_raider_system.gfx` resolves the group, large unit, and on-map sprite names to those files with two frames each.
The inherited counter evidence records a chroma-key removal workflow; this audit verifies retained bytes and runtime references without promoting that historical source workflow as new current-contract production evidence.

## Dispositions and limitations

| Item | Disposition | Basis or limitation |
| --- | --- | --- |
| Fourteen model payloads | Implemented | Exact source/runtime SHA-256 and byte-count match, with current registry, mesh, and entity evidence. |
| Ten action roles | Implemented | Registry, mesh aliases, state policy, event seconds, and final actual-byte reimport evidence agree. |
| Twelve audio files and attribution | Implemented | Exact runtime-copy hashes, resolved sound definitions, and exact attribution copy. |
| Selection acknowledgement | Accepted but intentionally unbound | The soundeffect is registered, but an isolated per-subunit selection consumer is unsupported; a tag-wide voice substitution is prohibited. |
| Counter runtime | Implemented as retained package | Both DDS hashes and sprite definitions resolve; no new visual acceptance or source-generation claim is made here. |
| Live consumer behavior | Outside agent validation scope | No live-game test was performed or claimed; this does not block the implemented bounded Portal runtime integration. |

The source manifests still carry `prepared_not_copied` and parent-integration-pending status labels because they are preserved worker handoffs; current runtime hashes prove that the parent promotion has since occurred.
No functional contradiction or payload mismatch was found in the bounded runtime surfaces.
The broader Event 016 task remains incomplete across other model packages and inherited integration work; this audit disposes only the Portal Raider surfaces named above.

## Audit handoff

This audit created only `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/2026-09-08_portal_runtime_audit.md`.
No gameplay, GFX, entity, animation, mesh, texture, sound, attribution, counter, spreadsheet, or source-manifest file was edited by the auditor.
Meaningful checks included fourteen source/runtime payload hashes and sizes, ten complete role chains, all crosswalk event times, locator and shared-effect resolution, three-stream geometry reconciliation, scale-count verification, twelve audio hashes and definitions, normalized ledger-prefix and runtime-addendum comparison, selection-consumer search, two counter hashes, and common sprite-consumer tracing.
No Blender operation or live-game validation was run.
