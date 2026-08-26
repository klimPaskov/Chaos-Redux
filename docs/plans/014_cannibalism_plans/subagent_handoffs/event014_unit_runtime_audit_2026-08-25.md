# Event 014 Unit and Runtime Consumer Audit

Status date: 2026-08-25 parent read-only audit

Historical supersession notice: this audit predates the 2026-08-26 approved vanilla-visual reuse decision. Its Bone Riders and Network Cadre custom-model blocker language remains failure evidence only; Bone Riders now uses vanilla `sprite = cavalry`, Network Cadre uses vanilla `sprite = infantry`, and no custom model/action/provider gate remains for either gameplay consumer.

## Scope

This audit covers the nine Event 014 line-unit definitions, their locked template consumers, the bounded CXT registration path, and the seven model packages currently installed under `gfx/models/units/014_cannibalism/`. It does not treat source-only Meshy checkpoints as runtime packages and does not claim live in-game validation.

## Gameplay definition evidence

`common/units/014_cannibalism_irregular_infantry.txt` contains exactly nine distinct inactive sub-unit IDs: `cannibal_scavenger_warband`, `cannibal_feast_guard`, `cannibal_feast_cohort`, `cannibal_bone_guard`, `cannibal_bone_riders`, `cannibal_island_reavers`, `cannibal_siege_eaters`, `cannibal_march_predation_column`, and `cannibal_network_cadre`.

All nine carry `category_cannibal_irregular_infantry`, front-line or mobile army categories, stable sprite tokens, low maximum strength and organisation, high direct soft attack or breakthrough, weak defence, and supply pressure. The infantry-equipment families use the vanilla 4 km/h equipment base with positive maximum-speed modifiers from 0.80 to 1.05, so they exceed vanilla infantry and vanilla cavalry's 6.4 km/h result after the equipment-speed modifier. Bone Riders use the documented `cavalry = yes`, `group = mobile`, and `category_cavalry` contract while retaining the requested infantry-equipment cost. March Predation Column retains the existing `transport = motorized_equipment` gate and is the fastest family. Island Reavers retain the documented special-forces and marine categories.

The locked template creator in `common/scripted_effects/014_cannibalism_effects.txt#cannibalism_create_current_warlord_templates` creates all nine custom templates plus the separate one-battalion vanilla `Scavenged Elephant Column` template. All ten templates are locked and force-disable ordinary recruitment. Every scripted recruitment path calls the existing population and Larder transaction helpers before unit creation; no focus or technology bridge directly grants a free division. The creation path grants installed vanilla `elephantry` technology, and rollback/reset removes the ten templates and clears the nine bridge technologies.

`common/scripted_effects/014_cannibalism_cxt_test_effects.txt#chaosx_cxt_extension_event014_cannibalism_apply` registers all nine custom frontline tokens exactly once. `on_startup` and the tag-scoped `on_daily_CXT` fallback consume that idempotent wrapper; no global recurring country scan was added.

## Installed runtime package evidence

The following seven packages have a mesh, eight distinct action exports (`idle`, `move`, `attack`, `defend`, `support_attack`, `retreat`, `training`, and `death`), three material DDS maps, animation registries, entity/GFX bindings, snow/desert clones or equivalent terrain clones, and runtime sound definitions:

| Package | Mesh | Actions | Maps | Entity/GFX | Runtime sound |
| --- | --- | ---: | ---: | --- | ---: |
| `cannibal_feast_guard` | present | 8 | 3 | present | 7 WAV |
| `cannibal_feast_cohort` | present | 8 | 3 | present | 7 WAV |
| `cannibal_bone_guard` | present | 8 | 3 | present | 7 WAV |
| `cannibal_siege_eaters` | present | 8 | 3 | present | 7 WAV |
| `cannibal_march_predation_column` | present | 8 | 3 | present | 7 WAV |
| `cannibal_island_reavers` | present | 8 | 3 | present | 7 WAV |
| `cannibal_scavenger_warband` | present | 8 | 3 | present | 6 WAV |

The parent path audit found zero missing mesh, animation, material-map, entity, or sound-file references for these seven packages. The runtime sound tree contains 48 WAV files for the installed packages; ffprobe reports `pcm_s16le`, 44,100 Hz, mono for all installed files. Sound IDs are unique across the installed packages.

## Historical package disposition (superseded 2026-08-26)

- `cannibal_bone_riders`: no accepted compound horse/rider Meshy-to-validated skeletal package; a reused humanoid or transform-only fallback would violate the model pipeline and is not wired.
- `cannibal_network_cadre`: accepted geometry and maps exist, but the provider animation lease is unavailable and no provider-sourced action exports or reimports exist.

The accepted Island Reavers v11 and Scavenger Warband v2 packages are recorded in their dedicated runtime handoffs; the earlier blocker descriptions are superseded.

The current Meshy account balance check returned 10 credits. Eight custom actions alone required 24 credits under the former package scope, before any missing generation or rigging work. That provider-cost finding is historical and no longer blocks the approved vanilla sprites.

## Current disposition

Bone Riders and Network Cadre are approved vanilla-visual simplifications rather than incomplete custom model packages. The seven dedicated model packages remain subject to parent live consumer review, and no in-game behavior or map-model playback is claimed by this audit.

## Parent validation boundary

This audit is source and artifact evidence only. It does not claim live game behavior, map-model rendering, or unit animation playback. Parent-owned sound-definition dispatch, final super-event wiring, and the seven bespoke package live review remain open in the Event 014 completion ledger.
