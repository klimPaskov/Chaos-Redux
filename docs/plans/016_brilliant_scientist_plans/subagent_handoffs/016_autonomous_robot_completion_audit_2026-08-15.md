# Autonomous Robot completion audit

Parent disposition: the provider-505 derivative activation blocker identified in this read-only snapshot was resolved afterward. `chaos_unit_family_provider_505_event19_setup_derivative` grants the neutral robot operational selector in the derivative country scope before installing the public derivative package. The selection-audio engine limitation and unavailable probability proof remain explicitly reported.

Date: 2026-08-15

Scope: the shared `autonomous_robot`, `autonomous_robot_equipment`, and `autonomous_robot_equipment_1` runtime; Event 016 robot operational and weaponization technologies and grant paths; Event 019 family/provider 505; the installed model, entity, actions, textures, sounds, technology/equipment icons, counters, localisation, production evidence, and current documentation. This audit does not assess the remainder of Event 016.

Overall status: **partial, with one high-severity Event 019 causality blocker, one explicit selection-audio engine blocker, and incomplete probability evidence**. The Event 016/shared gameplay definitions and the installed static visual/audio package are otherwise coherent in the current working snapshot.

## Severity-sorted findings

### High — Event 019 derivative 505 does not acquire the operational unlock needed by its advertised trainable/production contract

Family/provider 505 registers as `trainable_and_spawnable` in `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:114-130`. Its derivative setup sets `infantry_spawn_event16_provider_derivative` and installs only a leader/idea/route receipt at lines 1597-1732. It never grants `brilliant_scientist_robot_formations_tech`, never calls the neutral `chaosx_grant_custom_operational_technology` API, and never sets `chaosx_custom_technology_robot_operational`.

That omission is causal, not cosmetic:

- `autonomous_robot` is `active = no` in `common/units/016_brilliant_scientist_project_forces.txt:160-203`.
- `autonomous_robot_equipment_1` is `active = no` in `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt:328-334`.
- The equipment production gate at the same file's lines 255-323 accepts the neutral operational flag or Event 016 project/host state, but not `infantry_spawn_event16_provider_derivative`.
- `brilliant_scientist_event19_robot_provider_unlocked` permits a derivative solely from the derivative family/provider receipt in `common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt:28-45`.
- The installed idea is an empty hidden receipt in `common/ideas/016_brilliant_scientist_project_force_ideas.txt:39-44`, while localisation claims that the derivative can raise and maintain robots through isolated production in `localisation/english/019_infrantry_spawn_l_english.yml:1687-1688`.

The initial exact-recreation/spawn path may still create a locked template and unit through Event 019's provider callbacks, but the source does not establish the promised continuing subunit unlock and production authority for the derivative. This leaves family 505's trainable, sustainment, and isolated-production claims unproved and likely unusable once transferred equipment is exhausted.

Recommended owner action: define a provider-owned derivative knowledge/production receipt, grant the dependency-safe operational technology during successful provider-505 setup, and add ownership-aware cleanup so independently acquired robot knowledge is never revoked. The public neutral technology API is the closest existing grant precedent, but its documentation already notes that a revocation ownership contract is still future work; do not clear a shared technology or flag without such a ledger. Re-run the Event 019 provider lifecycle and probability scenarios after the owner patch.

### High — Per-subunit selection audio is registered but has no runtime consumer

`sound/autonomous_robot_sound.asset:4,11` defines `autonomous_robot_select_source` and `autonomous_robot_select_sfx`. A repository-wide active-source search found no reference to `autonomous_robot_select_sfx` outside that definition. The entity binds move, idle, footfall, attack/support attack, and death sounds in `gfx/entities/autonomous_robot.asset:8-75`, but there is no selection callback.

This is explicitly disclosed rather than hidden: `docs/shared_autonomous_robot_system.md:41` and `016_autonomous_robot_runtime_handoff_2026-08-15.md` explain that installed ordinary land-unit selection routing is country/original-tag infantry voice routing, which cannot provide a provider-neutral per-subunit sound without replacing ordinary infantry voices. The sourced selection one-shot and stable identifier are preserved, but selection-role runtime coverage remains **blocked** under the 3D-unit completion contract.

Recommended owner action: retain this explicit blocker until a verified per-subunit selection consumer exists. Do not wire the sound to a country-wide infantry voice token and do not count registration alone as selection playback evidence.

### Medium — Required weighted-surface evidence is not complete in this handoff

The robot participates in the weighted random custom-technology pool in `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:215-270`, and provider 505 contributes `spawn_weight = 14` at `common/script_constants/016_brilliant_scientist_project_force_constants.txt:422-450`. A `chaosx_ai_probability_auditor` pass was launched for the required all-unowned, robot-only-unowned, and robot-already-owned scenarios and for any provider-505 selection pool. It had not returned a completed MCP result when the parent required this audit to finalize. Therefore uniform random-grant behavior, zero-total behavior, and provider-505 normalized selection probability are not certified here.

Recommended owner action: preserve and review the probability auditor's eventual result before claiming this tranche complete. Any weight change requires the same named scenarios and a post-patch `hoi4.probability_compare` pass.

### Medium — Production and planning records have not all been promoted to the installed state

The current authority `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_autonomous_robot_runtime_handoff_2026-08-15.md` accurately records the installed runtime. Several accepted production/working records still state that parent wiring is pending or retain the retired runtime identifiers:

- `docs/assets/shared_robot_system/models_3d/autonomous_robot/manifest.json` still has status `production_complete_parent_wiring_pending` and `runtime_wiring = parent_owned_pending`.
- `docs/assets/shared_robot_system/models_3d/autonomous_robot/manifest.md`, `runtime/handoff.md`, and `runtime/crosswalk.md` still describe the entity/sound/counter runtime as unwired or parent-pending.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/autonomous_robot_3d_model_handoff.md` and `autonomous_robot_counter_art_handoff.md` retain parent-wiring/live-consumer pending wording.
- `docs/plans/016_brilliant_scientist_plans/016_event19_generic_unit_family_3d_model_backlog.md`, `016_core_runtime_handoff_map.md`, and `subagent_handoffs/016_project_reuse_identifier_map.md` still describe `kruger_robot_frame` / `kruger_robot_equipment(_1)` and an unproduced or deferred generic model.

Dated historical audit handoffs may retain their old observations, but the active backlog/map/manifest surfaces need an explicit superseded disposition or promotion to the generic installed IDs. The current runtime handoff is not enough to make contradictory working documents self-dispositioning.

## Completion status by surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Generic runtime IDs | Finished | Definitions and active consumers consistently use `autonomous_robot`, `autonomous_robot_equipment`, and `autonomous_robot_equipment_1`. No retired `kruger_robot_frame` or `kruger_robot_equipment(_1)` token remains in active `common`, `events`, `interface`, `gfx`, `sound`, or `localisation` source. |
| Event 016 operational technology | Finished statically | `brilliant_scientist_robot_formations_tech` is grant-only, AI-disabled, enables the exact variant/subunit, and applies the documented robot bonuses in `common/technologies/016_brilliant_scientist_project_technologies.txt:58-72`. Public API and Event 016 history rebuild grant it dependency-safely. |
| Event 016 weaponization technology | Finished statically | `brilliant_scientist_robot_formations_weaponization_tech` is grant-only, AI-disabled, depends on the operational tech, and modifies the exact generic subunit in `common/technologies/016_brilliant_scientist_project_force_technologies.txt:67-79`. The upgrade API grants the base first. |
| Subunit/equipment statistics and modifier families | Finished statically | The subunit uses both `armor` and `mechanized` types, `group = armor`, and the expected armor/infantry categories. Equipment and technology values match `docs/shared_autonomous_robot_system.md` and the dated runtime handoff. No orphaned runtime token was found. |
| Event 019 provider 505 registration/callback surface | Partial | Registration, eligibility, template, manifest, spawn, sustainment, management, payment/refund, derivative setup/removal/cleanup callbacks exist. Derivative production/unlock causality is missing as described above. |
| Hidden robot technology icons and equipment icon | Finished statically | Both technology sprites are registered in `interface/016_brilliant_scientist_hidden_technologies.gfx:12-13`; equipment art is registered in `interface/autonomous_robot_system.gfx:7`. Runtime DDS hashes match the icon handoff: operational `bf54fe65...abaf0`, weaponization `b6151923...fd4`, equipment `8ba187b7...50e0`. |
| Large and on-map counters | Finished statically; live acceptance pending | Exact large and on-map DDS files exist, match handoff hashes `147cf90c...61b09` and `bdeb527f...edd4b`, and are registered under the exact vanilla-pattern sprites in `interface/autonomous_robot_system.gfx:4-6`. The counter handoff records installed vanilla definition/DDS inspection, skill-local reference-family review, sampled vanilla greens, original ImageGen art, and round-trip evidence. |
| Mesh/entity/8 actions/3 textures | Finished statically; live acceptance pending | The installed mesh, eight `.anim` actions, and three textures exist. All twelve production hashes exactly match `manifest.json` and the 3D handoff. `autonomous_robot_mesh`, `autonomous_robot_entity`, snow/desert clones, scale `0.8`, eight state bindings, and exact animation registrations resolve in current source. |
| Six sourced sounds | Partial | All six originals and all six derived OGG hashes match the source ledger. All six installed WAVs are 44.1 kHz, mono, 16-bit PCM with the documented durations. Five action roles have entity consumers; selection remains registered but unconsumed. |
| Localisation | Finished for scoped keys | Subunit, equipment, both technology names/descriptions, and family-505 cost/host text resolve. The dated localisation audit records 40/40 expected keys, no scoped duplicates, no retired active runtime tokens, and constant-aligned costs. The derivative production claim currently overstates the source behavior. |
| Documentation/accepted-plan disposition | Partial/stale | The current runtime handoff is accurate, but older active working maps/backlogs and production manifests remain pending or use retired identifiers without a clear superseded disposition. |
| Probability/AI evidence | Blocked pending required auditor result | Source contains both a random technology pool and provider spawn weight. No completed scenario-specific probability result was available at handoff time. |

## Meaningful validation and MCP limits

- Fresh bounded `hoi4.event_inspect` calls for `chaosx.nr16.1` and `chaosx.nr19.1` returned `EVENT_INSPECTED_PARTIAL`, status `ok`, with one artifact each. Event 016 and Event 019 renders returned `EVENT_RENDERED_PARTIAL`; the first Event 019 neighborhood attempt timed out after 180 seconds, while the subsequent two-node options render succeeded. Large-workspace helper/lifecycle projection remains deferred, so these are structural receipts, not provider-505 lifecycle proof.
- Fresh technology explains for both robot technologies returned `TECH_INSPECTED_PARTIAL`, status `ok`. The weaponization technology render and a retry of the operational asset render returned `TECH_RENDERED_PARTIAL`; the first operational technology render timed out after 180 seconds. The current runtime handoff also records current explain, unlock, asset-render, and comparison artifacts with zero reported structural regressions.
- This audit's direct `hoi4.event_compare` and `hoi4.tech_compare` probes returned exact blockers `EVENT_COMPARISON_BASELINE_REQUIRED` and `TECH_COMPARISON_BASELINE_REQUIRED`. No synthetic before/after claim is made. The parent-provided current technology comparison artifact is recorded in the runtime handoff, but no event-graph baseline was supplied to this audit.
- Independent SHA-256 checks matched the 3D manifest for the mesh, eight actions, and three textures; the counter and technology/equipment icon handoffs for the five scoped DDS files; and the audio ledger for six originals and six derived OGGs.
- `ffprobe` independently confirmed all six runtime WAVs are PCM signed 16-bit little-endian, 44.1 kHz, mono, with durations 1.2, 3.0, 4.0, 1.5, 2.75, and 2.6 seconds for select, move, idle, footfall, attack, and death respectively.
- No Hearts of Iron IV process was launched. Live map entity selection, action transitions, scale, shader/material appearance, counter consumption, sound mixing, and combat behavior remain user-owned acceptance evidence.

## Recommended next actions

1. Repair provider-505 derivative knowledge/production ownership and cleanup, then rerun the bounded Event 019 lifecycle inspection/render and relevant exact-transfer/management scenarios.
2. Complete and review the probability-auditor scenario result before any completion claim; compare the same scenarios after a causal patch.
3. Keep selection audio explicitly blocked until a verified per-subunit consumer exists.
4. Promote or explicitly supersede the stale production manifest, runtime crosswalk, working backlog, runtime map, and identifier map.
5. Preserve the current installed assets and hashes; no model, action, texture, icon, counter, or combat-sound replacement is indicated by this audit.

No gameplay, asset, localisation, spreadsheet, or runtime file was edited by this audit. This handoff is the only file added. No commit was created.
