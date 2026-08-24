# Event 014 irregular infantry implementation handoff

> Superseded snapshot (2026-08-24): this historical handoff predates the ninth `cannibal_bone_riders` integration and the consolidated nine-token CXT wrapper. The current source of truth is `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_custom_unit_integration_audit_2026-08-24.md`; the historical eight-family implementation notes below remain for provenance.

This handoff covers the gameplay and documentation tranche for the original eight Event 014 Cannibalism foot-formation families. The implementation uses real inactive land subunits as stable consumers for the downstream map-model contract while keeping recruitment behind the existing locked-template and Event 014 creation paths.

## Changed gameplay surfaces

- `common/units/014_cannibalism_irregular_infantry.txt` defines the original eight infantry-like custom subunits, their family-specific stats, terrain modifiers, ordinary equipment requirements, stable `sprite` tokens, and the shared Event 014 implementation contract; the current package also includes `cannibal_bone_riders`.
- `common/unit_tags/chaosx_categories.txt` adds `category_cannibal_irregular_infantry` for explicit irregular-infantry classification.
- `common/scripted_effects/014_cannibalism_effects.txt` gives each of the original locked templates a plurality of its matching custom subunit while retaining role-appropriate support companies and artillery.
- `common/on_actions/014_cannibalism_on_actions.txt` adds the guarded additive `on_daily_CXT` registration block for the original eight subunits and their existing equipment dependencies.
- `localisation/english/014_cannibalism_l_english.yml` adds the shared category name plus names, abbreviations, and descriptions for the original eight subunits. The file remains UTF-8 with BOM and uses no `:0` localisation suffixes.

No equipment archetype was added, so `common/script_enums.txt` was intentionally unchanged. The implementation does not add or reference a Prison Host.

## Subunit and sprite contract

| Family | Subunit id | Sprite token | Equipment gate | Final speed |
| --- | --- | --- | --- | ---: |
| Scavenger Warband | `cannibal_scavenger_warband` | `cannibal_scavenger_warband` | `infantry_equipment` | 7.40 |
| Feast Guard | `cannibal_feast_guard` | `cannibal_feast_guard` | `infantry_equipment` | 7.20 |
| Feast Cohort | `cannibal_feast_cohort` | `cannibal_feast_cohort` | `infantry_equipment` | 7.80 |
| Bone Guard | `cannibal_bone_guard` | `cannibal_bone_guard` | `infantry_equipment` | 8.20 |
| Island Reavers | `cannibal_island_reavers` | `cannibal_island_reavers` | `infantry_equipment` plus marine equipment need | 7.60 |
| Siege Eaters | `cannibal_siege_eaters` | `cannibal_siege_eaters` | `infantry_equipment` | 7.52 |
| March Predation Column | `cannibal_march_predation_column` | `cannibal_march_predation_column` | `infantry_equipment` plus `motorized_equipment` and motorized transport | 26.40 |
| Network Cadre | `cannibal_network_cadre` | `cannibal_network_cadre` | `infantry_equipment` | 8.00 |

Every subunit uses documented `type = { infantry }` and `group = infantry`, is marked `active = no`, and includes `category_cannibal_irregular_infantry` in its category list. Island Reavers additionally use the documented marine and special-forces categories and coastal exfiltration capability. March Predation remains infantry-like rather than a cavalry or motorized unit type, but deliberately includes `transport = motorized_equipment` so its truck gate supplies movement.

## Exact stat comparison

The direct subunit columns below are the authored battalion-level contributions before equipment, technology, doctrine, commander, and terrain effects. Vanilla baselines are the installed vanilla infantry and cavalry precedents inspected in `common/units/infantry.txt`, `common/units/cavalry.txt`, and their equipment files.

| Unit | Speed | Max organisation | Max strength | Morale | Direct soft attack | Direct breakthrough | Direct defence | Equipment gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Vanilla infantry | 4.00 | 60 | 25 | 0.30 | 0 | 0 | 0 | 100 infantry equipment |
| Vanilla cavalry | 6.40 | 70 | 25 | 0.30 | 0 | 0 | 0 | 120 infantry equipment |
| Scavenger Warband | 7.40 | 22 | 13 | 0.14 | 8 | 10 | -4 | 100 infantry equipment |
| Feast Guard | 7.20 | 20 | 12 | 0.16 | 9 | 8 | -2 | 100 infantry equipment |
| Feast Cohort | 7.80 | 26 | 14 | 0.17 | 12 | 14 | -3 | 100 infantry equipment |
| Bone Guard | 8.20 | 18 | 10 | 0.11 | 15 | 20 | -6 | 100 infantry equipment |
| Island Reavers | 7.60 | 24 | 12 | 0.18 | 11 | 14 | -4 | 150 infantry equipment with marine role |
| Siege Eaters | 7.52 | 21 | 11 | 0.13 | 13 | 16 | -5 | 100 infantry equipment |
| March Predation Column | 26.40 | 14 | 10 | 0.10 | 12 | 18 | -7 | 100 infantry equipment plus 35 motorized equipment and transport |
| Network Cadre | 8.00 | 12 | 8 | 0.10 | 7 | 9 | -8 | 100 infantry equipment |

The speed formula is `equipment maximum_speed * (1 + subunit maximum_speed modifier)`. Regular infantry equipment has base maximum speed 4, and vanilla cavalry’s installed maximum-speed modifier produces 6.4. The six non-March families therefore resolve to 7.2–8.2 using infantry equipment, all above cavalry. March uses the installed motorized equipment transport base of 12 and its `maximum_speed = 1.20`, resolving to `12 * (1 + 1.20) = 26.40`; the explicit motorized transport field is required for that result. The family ordering keeps March fastest.

The negative direct `defense` values are deliberate additive subunit contributions and make survivability fragile even when ordinary equipment contributes its own defence. Terrain modifiers use the vanilla `defence` spelling and are percentage-style terrain modifiers. Family identities are expressed through the authored terrain rows: scavenger forest/jungle/marsh/desert raiding, Feast Guard fort/urban/hill defence, Feast Cohort organized plains/forest/urban assault, Bone Guard elite fort/urban/hill/mountain shock, Island Reavers amphibious/coastal and marsh/river action, Siege Eaters fort/urban assault, March Predation pursuit across open and rough terrain, and Network Cadre small seeding/support operations.

## Locked template mappings

The existing template names, lock flags, `force_allow_recruiting = no`, recruitment population gates, Larder gates, and equipment gates remain intact. Only the line composition was changed where necessary to establish a plurality of the matching custom subunit.

| Existing template | Matching custom line | Retained role support |
| --- | --- | --- |
| Scavenger Warband | 4 `cannibal_scavenger_warband` | None |
| Feast Guard | 6 `cannibal_feast_guard` | Engineer support |
| Feast Cohort | 9 `cannibal_feast_cohort` | Engineer and recon support |
| Bone Guard | 6 `cannibal_bone_guard` | 2 artillery battalions, engineer and recon support |
| Island Reavers | 6 `cannibal_island_reavers` | Engineer support |
| Siege Eaters | 6 `cannibal_siege_eaters` | 2 artillery battalions and engineer support |
| March Predation Column | 6 `cannibal_march_predation_column` | Recon support |
| Network Cadre | 3 `cannibal_network_cadre` | Recon support |

This plurality ensures each template resolves its own sprite token instead of falling back to a mixed vanilla plurality. Ordinary infantry, artillery, support, and motorized equipment remain the only concrete equipment dependencies; no free equipment is created by the unit definitions.

## CXT dynamic extension contract

The historical additive `on_daily_CXT` block in `common/on_actions/014_cannibalism_on_actions.txt` was guarded by `chaosx_test_country_initialized` and an idempotence flag. It registered the original eight subunit tokens plus the existing `infantry_equipment_3`, `support_equipment_1`, `artillery_equipment_3`, and `motorized_equipment_1` tokens through the existing ChaosX test-country registration effects. The current consolidated CXT wrapper registers all nine tokens; see `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_custom_unit_integration_audit_2026-08-24.md`. The shared CXT runtime then unlocks each registered subunit, creates its one-line `CXT Registered - [UNIT]` template, and spawns the registered test divisions once, while the existing weekly registry maintenance handles technology and stockpile refill. No broad world on-action or Event-specific weekly loop was added.

## Documentation and validation evidence

The aligned Event 014 overview, country-package specification, acceptance criteria, asset matrix, package status, package validation, and test-country contract were updated in the corresponding `docs/events/014_cannibalism/`, `docs/specs/014_cannibalism_specs/`, and `docs/testing/` paths. The existing model plan already records the same stable IDs and sprite tokens for the parent 3D/entity/counter workers.

The focused Event 014 MCP inspection completed with status `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, revision `b3e7af9424b053a2a2f7b3ce0823e85d0888e7dcb1efdd5a8a5dfee6d7a3fc06`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e38690374c546b2ac3940c349e0ab21e61f3df97dbec227728f5f21ac5a3b6a5/cbacd6bd1fb5335a706ace60d7ce2a68334f6ecc4a2564a5a2835f5c5c66f4e9/event-lint-b3e7af9424b0.json`. The bounded event-state render completed with zero blocking diagnostics and artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d1f599d23662eb02e17add948a95380f39a49fd0a1b25dff2257230ff8d5290f/6c811d2b0979a7fe8872d09b9d04c3e8dc7dfb9af896b415f6563b329509cc81/event-state-b3e7af9424b0-manifest.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0170e506319dc18de8bcddf3d8c5616edd18977dc022ee69da90b759949be6a/d399651ca38b5a9f45a633058c66808a35301bbc0fece8e3b9efc9c340315973/event-state-b3e7af9424b0.json`.

Read-only focus inspection confirmed the existing Event 014 trees load as `cannibalism_unified_focus_tree` with 108 focuses, `cannibalism_warlord_focus_tree` with 68 focuses, and `cannibalism_wendigo_focus_tree` with 28 focuses. The attempted national-mode focus renders were rejected by the MCP input validator because the request included the unsupported `columns` argument; no focus source was changed and this is outside the unit tranche. No map or technology surface was changed, and no probability-bearing surface was introduced, so their specialized MCP routes were not applicable.

## Ownership boundary and remaining risks

No gameplay simplification was made. The downstream 3D/model/entity/GFX/counter/sound workers still own the visual outputs corresponding to these active sprite consumers, and no `.mesh`, `.anim`, `.asset`, `.gfx`, DDS, counter, or sound file was created or wired in this tranche. The remaining integration risk is that each stable sprite token must receive its parent-owned visual definition before the map-model consumer is visually complete. Runtime confidence also depends on the parent’s live game validation of the custom unit definitions and CXT test-country setup; agents do not launch the game under repository policy.
