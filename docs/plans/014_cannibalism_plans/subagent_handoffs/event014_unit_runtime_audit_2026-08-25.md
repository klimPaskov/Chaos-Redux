# Event 014 Unit and Runtime Consumer Audit

Status date: 2026-08-25 parent read-only audit

## Scope

This audit covers the nine Event 014 line-unit definitions, their locked template consumers, the bounded CXT registration path, and the five model packages currently installed under `gfx/models/units/014_cannibalism/`. It does not treat source-only Meshy checkpoints as runtime packages and does not claim live in-game validation.

## Gameplay definition evidence

`common/units/014_cannibalism_irregular_infantry.txt` contains exactly nine distinct inactive sub-unit IDs: `cannibal_scavenger_warband`, `cannibal_feast_guard`, `cannibal_feast_cohort`, `cannibal_bone_guard`, `cannibal_bone_riders`, `cannibal_island_reavers`, `cannibal_siege_eaters`, `cannibal_march_predation_column`, and `cannibal_network_cadre`.

All nine carry `category_cannibal_irregular_infantry`, front-line or mobile army categories, stable sprite tokens, low maximum strength and organisation, high direct soft attack or breakthrough, weak defence, and supply pressure. The infantry-equipment families use the vanilla 4 km/h equipment base with positive maximum-speed modifiers from 0.80 to 1.05, so they exceed vanilla infantry and vanilla cavalry's 6.4 km/h result after the equipment-speed modifier. Bone Riders use the documented `cavalry = yes`, `group = mobile`, and `category_cavalry` contract while retaining the requested infantry-equipment cost. March Predation Column retains the existing `transport = motorized_equipment` gate and is the fastest family. Island Reavers retain the documented special-forces and marine categories.

The locked template creator in `common/scripted_effects/014_cannibalism_effects.txt#cannibalism_create_current_warlord_templates` creates all nine custom templates plus the separate one-battalion vanilla `Scavenged Elephant Column` template. All ten templates are locked and force-disable ordinary recruitment. Every scripted recruitment path calls the existing population and Larder transaction helpers before unit creation; no focus or technology bridge directly grants a free division. The creation path grants installed vanilla `elephantry` technology, and rollback/reset removes the ten templates and clears the nine bridge technologies.

`common/scripted_effects/014_cannibalism_cxt_test_effects.txt#chaosx_cxt_extension_event014_cannibalism_apply` registers all nine custom frontline tokens exactly once. `on_startup` and the tag-scoped `on_daily_CXT` fallback consume that idempotent wrapper; no global recurring country scan was added.

## Installed runtime package evidence

The following five packages have a mesh, eight distinct action exports (`idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`), three material DDS maps, animation registries, entity/GFX bindings, snow/desert clones, and seven-role sound definitions:

| Package | Mesh | Actions | Maps | Entity/GFX | Runtime sound |
| --- | --- | ---: | ---: | --- | ---: |
| `cannibal_feast_guard` | present | 8 | 3 | present | 7 WAV |
| `cannibal_feast_cohort` | present | 8 | 3 | present | 7 WAV |
| `cannibal_bone_guard` | present | 8 | 3 | present | 7 WAV |
| `cannibal_siege_eaters` | present | 8 | 3 | present | 7 WAV |
| `cannibal_march_predation_column` | present | 8 | 3 | present | 7 WAV |

The parent path audit found zero missing mesh, animation, material-map, entity, or sound-file references for these five packages. The runtime sound tree contains 35 WAV files total; ffprobe reports `pcm_s16le`, 44,100 Hz, mono for all 35 files. Sound IDs are unique across the installed packages.

## Remaining blockers

- `cannibal_bone_riders`: no accepted compound horse/rider Meshy-to-validated skeletal package; a reused humanoid or transform-only fallback would violate the model pipeline and is not wired.
- `cannibal_island_reavers`: the approved v8 Meshy 7 request returned HTTP 402 before task creation; a later provider candidate task `01a034bb-7129-716b-bc17-177ca0eb9a1a` returned `SUCCEEDED`, but it has no accepted v8 rig/action/reimport package and remains outside runtime wiring.
- `cannibal_scavenger_warband`: the available geometry has a weapon-contact defect and remains explicitly at parent user-review status; no final action-safe package is wired.
- `cannibal_network_cadre`: accepted geometry and maps exist, but the provider animation lease is unavailable and no provider-sourced action exports or reimports exist.

The current Meshy account balance check returned 10 credits. Eight custom actions alone require 24 credits, before any missing generation or rigging work, so these four packages cannot be promoted without an external balance change or an approved source/action route. These are recorded blockers, not silent fallbacks.

## Parent validation boundary

This audit is source and artifact evidence only. It does not claim live game behavior, map-model rendering, or unit animation playback. Parent-owned sound-definition dispatch, final super-event wiring, and the four blocked packages remain open in the Event 014 completion ledger.
