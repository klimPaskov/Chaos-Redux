# Autonomous Robot Runtime Handoff

Date: 2026-08-15

Status: the provider-neutral Autonomous Robot gameplay, technology, visual, animation, counter, and positional-sound package is installed. Live consumer validation remains user-owned, and HOI4 exposes ordinary land-unit selection audio through country/original-tag infantry voice templates rather than a subunit entity callback.

## Runtime identity and consumers

- Subunit: `autonomous_robot`.
- Equipment archetype and variant: `autonomous_robot_equipment` and `autonomous_robot_equipment_1`.
- Entity and mesh: `autonomous_robot_entity` and `autonomous_robot_mesh`.
- Event 016 operational and weaponization technologies: `brilliant_scientist_robot_formations_tech` and `brilliant_scientist_robot_formations_weaponization_tech`.
- Event 019 provider: family/provider 505 through `chaos_unit_family_provider_505_register`.
- Public grant surface: the robot selectors of `chaosx_grant_custom_operational_technology` and `chaosx_grant_custom_technology_upgrade`.

Provider 505's derivative callback grants the neutral robot operational selector in the released country scope before installing its public derivative identity. The derivative therefore receives `brilliant_scientist_robot_formations_tech`, the durable `chaosx_custom_technology_robot_operational` production gate, the locked robot template, and the idempotent provider registration required by its advertised trainable and isolated-production contract.

The identifiers contain no Kruger or Event 016 ownership. Event 016, Event 019, and future events that use the public custom-technology API resolve the same subunit, equipment, entity, counters, and model.

## Gameplay profile

The two-width line battalion belongs to both armor and mechanized-infantry modifier families. It has 45 base organization, 45 HP, 40% recovery, 50 manpower, 4 suppression, 180 training days, and requires 50 Autonomous Combat Robots plus 10 Support Equipment. Forest, jungle, and marsh penalties preserve an open-terrain mechanized role.

Each Autonomous Combat Robot costs 18 production, uses steel, tungsten, chromium, and rubber, consumes fuel, and provides 88% hardness, 70 armor, 60 breakthrough, 50 defense, 36 soft attack, 30 hard attack, 75 piercing, 8 air attack, 7 km/h speed, and 92% reliability before technology bonuses. The operational technology adds 75% hard attack, 75% breakthrough, 60% defense, and 10 organization. Weaponization adds another 75% hard attack, 75% breakthrough, and 35% reliability.

## Purpose-built icons and counters

`interface/016_brilliant_scientist_hidden_technologies.gfx` registers all eighteen Event 016 hidden technology icons. `interface/clone_system.gfx` registers both Mengele clone-refinement icons. `interface/autonomous_robot_system.gfx` registers the robot equipment art and both counter surfaces.

The hidden-icon manifest contains 22 checked entries including the preserved clone-access icon. All listed runtime files exist and match their recorded SHA-256 values. The Autonomous Robot counters are:

- `gfx/interface/counters/divisions_large/unit_autonomous_robot_icon.dds`, SHA-256 `147cf90c3d053947640f7865f1dade6d8ffaba99942e8401ed4575d53db61b09`.
- `gfx/interface/counters/divisions_small/onmap_unit_autonomous_robot_icon.dds`, SHA-256 `bdeb527f8a73494b918adec27c26aec97c299f51ad00d2da2946a37a278edd4b`.

## Model and animation package

The accepted 3D package uses a 29,971-triangle mesh, 24-bone sanitized rig, 1024-pixel packed PDX textures, and entity scale 0.8 against the installed vanilla infantry reference. Both integrated forearm machine guns remain distinct through the accepted action contact sheet.

`gfx/models/units/autonomous_robot/` contains the reimport-proven mesh, packed diffuse/normal/specular textures, and eight real 24-FPS skeletal actions: idle, move, attack, defend, support attack, retreat, training, and death. `gfx/entities/autonomous_robot.gfx` binds the exact exported mesh object `char1.003`, and `gfx/entities/autonomous_robot.asset` supplies the generic, snow, and desert entities. Runtime copies match every staging hash in `autonomous_robot_3d_model_handoff.md`.

The Meshy lineage consumed 63 credits and finished at a balance of 156. The original 300,000-face recovery exceeded the strict provider rig threshold at 310,853 faces; the user-approved 280,000-face recovery produced 290,165 faces and passed the rig gate. The failed provider retreat animation was refunded. The required retreat role was authored through the allowlisted Blender workflow from Meshy's bundled real running skeleton, not replaced with a static pose or transform-only animation.

## Audio

Six licensed evidence derivatives cover selection, movement servo, idle machinery, armored footfall, exact-weapon dual-MG fire, and destruction. Immutable evidence copies and licences remain under `docs/assets/shared_robot_system/models_3d/autonomous_robot/evidence/audio/`.

Parent integration converts only the runtime copies from 192 kHz mono Vorbis to the installed positional-unit precedent of 44.1 kHz, mono, 16-bit PCM WAV. `sound/autonomous_robot_sound.asset` registers all six sources and sound effects. Entity events synchronize movement, footfalls, dual-MG attack/support fire, idle machinery, and destruction to their reviewed action frames.

The selection one-shot is registered as `autonomous_robot_select_sfx` but is not assigned to a country-wide `<TAG>_infantry_idle` token. HOI4's installed land-unit selection surface is country/original-tag based, so such a binding would replace ordinary infantry selection voices and would not remain provider-neutral or subunit-specific. No unrelated voice fallback was installed.

## MCP evidence

- Fresh base-technology explain: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8675b77e2eb47a971e53028f79732789294f9edd06c5df6f4bfdfecf35b03cf6/0cb872818f5a952792af25dc94693aa83610f1365226833e341da58b90ea71c4/technology-explain-6868e499ca31.json`.
- Fresh Autonomous Robot subunit unlock report: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d16f448c7a767a7388bc6a246cc1e38ed745428dcef2df2e3b3200764d1f4a76/29131a5c29743204ae68b313f7ff0114c7d2eed9479e4ccf7ec0b84ba1e7c830/technology-unlocks-6868e499ca31.json`.
- Fresh asset render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3820d5cdf7f1b0d8beb38a34c512e23923fbe6ddcd581a0ebe4a1468038e1af3/736f9c9fd9cdce488d8dd6b01a68dc52e376bf3cc8d4885960b39f258ebba2ca/technology-assets-6868e499ca31-manifest.json`.
- Fresh comparison: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93fc0cd3609240808391bf8509cf21e55492c7f8386f9b8b1a4d73f090983191/f765fd72e0908f03f52cac271125f9cf3a1e2f505dbc51f6c7731decc602933e/technology-compare-6868e499-76beaf87.json`.

The required focused `technology_ai_will_do` probability inspection was retried against `common/technologies/016_brilliant_scientist_project_technologies.txt` with the robot operational technology as the candidate pool. The installed MCP route timed out after 180 seconds without returning an artifact, so source-only review is not presented as probability evidence. Both hidden robot technologies retain the package-wide disabled research factor and are granted by project/event/API effects rather than selected by normal research AI.

The fresh technology routes report no blockers and the comparison reports zero structural regressions. Their partial status is limited to the server's large-workspace inline-inventory and deferred helper projections.

## Validation and remaining boundary

- All eight entity animation references resolve to one registered action definition.
- Every entity sound reference resolves to a registered sound effect and existing 44.1 kHz mono PCM WAV.
- All twelve staged model/animation/texture hashes match the installed runtime copies.
- All 22 hidden/shared technology icon manifest entries exist and match their checksums.
- Retired `kruger_robot_frame`, `kruger_robot_equipment`, and `kruger_robot_equipment_1` identifiers are absent from active runtime and localisation source.
- Scoped localisation contains every robot subunit, equipment, technology, project, incident, and Event 019 family key with no duplicate keys; all edited localisation retains UTF-8 BOM.
- The completion audit's provider-505 derivative activation finding was resolved by making the derivative callback invoke the public operational-technology API in the derivative country scope before public-package setup.

No model, animation, icon, counter, or combat-sound fallback remains. Live map-unit presentation, action-state switching, positional-sound mixing, tooltip wrapping, and combat behavior remain user-owned validation. Per-subunit selection-audio binding remains unavailable on the installed engine surface; the licensed one-shot and stable sound-effect identifier are preserved for a future verified consumer.
