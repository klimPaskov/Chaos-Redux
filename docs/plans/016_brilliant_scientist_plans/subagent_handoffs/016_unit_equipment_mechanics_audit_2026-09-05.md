# Event 016 unit and equipment mechanics audit handoff

Date: 2026-09-05

Status: implemented as an audit-only handoff; no gameplay source patch was justified by the current evidence.

## Scope and boundary

This audit covers the reusable Event 016 battalions, equipment archetypes and variants, hidden technology unlocks, shared clone reserve manpower, Event 019 provider callbacks, cap removal, enums, CXT registration, and matching localisation.

No model, entity, mesh, animation, sound, particle, focus, event chain, GUI, D’Rhondan country, portrait, workbook, or unrelated package file was changed.

No source file was staged or committed.

## Files inspected

The owned gameplay surfaces inspected were:

- `common/units/016_brilliant_scientist_project_forces.txt`
- `common/units/clone_infantry.txt`
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`
- `common/units/equipment/clone_equipment.txt`
- `common/technologies/016_brilliant_scientist_project_force_technologies.txt`
- `common/technologies/016_brilliant_scientist_project_technologies.txt`
- `common/technologies/clone_technologies.txt`
- `common/script_enums.txt`
- `common/script_constants/016_brilliant_scientist_project_force_constants.txt`
- `common/script_constants/clone_system_constants.txt`
- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`
- `common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt`
- `common/scripted_effects/clone_system_effects.txt`
- `common/on_actions/clone_system_on_actions.txt`
- `common/on_actions/germany_mengele_clone_on_actions.txt`

Read-only supporting surfaces included `common/dynamic_modifiers/clone_system_dynamic_modifiers.txt`, the Germany Mengele production effects, the Event 016 CXT registration effect and on-action, the Event 019 ledger and muster helpers, `docs/testing/chaosx_test_country.md`, the current Event 016 specifications and prior unit handoff, and the matching English localisation files `016_brilliant_scientist_country_l_english.yml`, `clone_system_l_english.yml`, and `019_infrantry_spawn_l_english.yml`.

Required offline wiki pages and vanilla documentation were read before source review, including Unit modding, Division modding, Equipment modding, Technology modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, dynamic-variable documentation, and the vanilla AI-template/equipment/technology precedents.

## Findings by severity

### P0/P1 confirmed defects

None found in the owned gameplay surfaces.

### P2 unresolved engine or design blockers

1. The accepted Event 016 contract describes autonomous robots as constrained by equipment, fuel, power infrastructure, and production, but the current unit and equipment surfaces expose no documented HOI4 `power` field or robot-specific power trigger/effect. The robot has zero manpower, 50 `autonomous_robot_equipment` and 10 `support_equipment` per battalion, `fuel_consumption = 1.20`, build cost 18, and steel/tungsten/chromium/rubber costs in `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt` around lines 222-245. I did not invent an unsupported Clausewitz key; the parent needs an engine-supported power mechanism or an accepted design decision before this requirement can be called fully evidenced.

2. `clone_refresh_reserve_manpower` reads `num_equipment@clone_equipment`, while production and Event 019 payment use concrete `clone_equipment_1`. Vanilla documentation confirms `num_equipment@<equipment>` and vanilla uses archetype tokens for stockpile checks, but the available documentation does not explicitly state concrete-child aggregation for a custom archetype. The source arithmetic is correct under the vanilla archetype convention, but exact concrete-to-archetype aggregation remains an engine validation item.

3. The mandatory technology MCP routes were unavailable in this run. A full `hoi4_tech_inspect` scan with `mode = scan`, `refresh = true`, `maxNodes = 1600`, and `maxDepth = 4` timed out with the exact error `timed out awaiting tools/call after 180s`. A targeted `hoi4_tech_inspect` unlock query for `brilliant_scientist_clone_formations_tech` also timed out with the same error. A `hoi4_tech_render` technology view for that id timed out with the same error. The first compare attempt was rejected with `unrecognized key relativePath` for the `before` and `after` objects; the schema-correct empty `hoi4_tech_compare` retry then timed out after 180 seconds. The standalone Technology Tree Viewer is not exposed by the installed package, so no engine technology artifact can be claimed.

4. The named `chaosx_ai_probability_auditor` route was not callable in this runtime. No probability-bearing source was changed; all inspected Event 016 technology AI blocks use factor zero, so no AI balance patch was made. Any later AI, MTTH, strategy-factor, or weighted-target change still requires the named auditor and same-scenario comparison.

### P3 watch items, not confirmed defects

1. `brilliant_scientist_event19_remove_project_force_public_additions` removes all eight possible Event 019 family ideas in its shared cleanup helper. The current one-provider derivative invariant and provider-specific registry dispatch mean no active cross-provider leak was proven, and provider 508 explicitly revokes only `alien_infantry_contact_source.event019_provider_508` before shared cleanup. A narrower idea-removal contract would require a design decision and was not applied during a concurrent working-tree audit.

2. The CXT harness calls `unlock_subunit = alien_infantry` only to materialize its one locked test cohort, then sets `is_locked = yes` and `force_allow_recruiting = no`. The normal Event 019 provider remains `spawn_only` and its production path does not expose training. Whether `unlock_subunit` itself gives the developer harness an extra designer surface requires live engine confirmation; changing it could prevent the locked CXT cohort from being constructed.

3. `brilliant_scientist_event19_record_project_force_manpower_obligation` is a legacy-looking helper with no active caller found in the inspected package. Active provider callbacks queue and commit their current manifest through `infantry_spawn_record_provider_obligation_manifest`, so the unused helper is not an active missing-obligation defect and was left untouched.

## Identifier and enum coverage

The active generic unit identifiers are `portal_raider`, `autonomous_robot`, `paleogenetic_creature`, `xenobiological_assault_organism`, `alien_infantry`, and `temporal_guard`; shared clone identifiers are `clone_infantry`, `aryan_clone_infantry`, `clone_equipment`, and `clone_equipment_1`.

An `rg --no-ignore` search across gameplay and localisation found no `kruger_paleogenetic`, `kruger_xenobiological`, or `kruger_temporal` identifiers.

`common/script_enums.txt` contains the Event 016 and clone equipment archetype and concrete IDs at lines 729-742, including both `xenobiological_assault_organism_equipment` and `xenobiological_assault_organism_equipment_1`. No enum addition was required.

## Manual mechanics and arithmetic validation

| Family | Unit bill and baseline | Event 019 template or availability |
| --- | --- | --- |
| Clone Infantry | 2 width, 20 strength, 70 organisation, 1,000 manpower, 90 infantry equipment, exactly 1 clone equipment per battalion. | Ten battalions equal 20 width, 10,000 manpower, 900 infantry equipment, and 10 clone equipment. The provider is trainable and spawnable; normal recruitment uses the unlocked shared template and real unit needs. |
| Aryan Clone Infantry | Same manpower, rifle, clone-equipment, width, strength, and base organisation bill as shared clone infantry, with a separate subunit and Mengele-only refinement technology. | Ten-battalion provider 522 template; the Aryan refinement remains separate from Kruger refinement and weaponization. |
| Autonomous Robot | 2 width, 45 strength, 45 organisation, zero human manpower, 50 robot equipment and 10 support equipment per battalion. Robot equipment consumes fuel and rare materials. | Four-battalion provider 505 template; no free-spawn cap remains. Power infrastructure is unresolved as described above. |
| Paleogenetic Creature | 3 width, 36 strength, 38 organisation, 500 manpower, 55 paleogenetic equipment and 15 support equipment per battalion. | Three-battalion provider 506 template; equipment and manpower gates scale repeated requests. |
| Xenobiological Assault Organism | 2 width, 32 strength, 32 organisation, 300 manpower, 50 xenobiological equipment and 20 support equipment per battalion. | Three-battalion provider 507 template; equipment and manpower gates scale repeated requests. |
| Portal Raider | 2 width, 25 strength, 60 organisation, 1,000 manpower, 100 infantry equipment and 10 teleportation equipment per battalion. | Four-battalion provider 509 template; equipment and manpower gates scale repeated requests. |
| Temporal Guard | 2 width, 20 strength, 50 organisation, 700 manpower, 45 temporal equipment, 60 infantry equipment, and 15 support equipment per battalion. | Four-battalion provider 510 template; equipment and manpower gates scale repeated requests. |
| Alien Infantry | 2 width, 40 strength, 90 organisation, zero human manpower, zero ordinary equipment, and exactly 200 alien laser weapons per battalion. | Provider 508 is spawn-only and landing-gated. Its ten-battalion landing template requires exactly 2,000 laser weapons and has no Event 019 training or sustainment row. |

For the clone reserve, the active formula is `clone_equipment_stockpile = num_equipment@clone_equipment`, followed by `clone_reserve_weekly_manpower = clone_equipment_stockpile * constant:clone_system.weekly_manpower_per_equipment`, where the constant is 10. Therefore one whole stockpiled clone equipment yields `+10` weekly manpower, two yield `+20`, and so on. The dynamic modifier is refreshed on the global weekly hook and after relevant equipment mutations; no direct weekly `add_manpower` path was found. Assigned clone equipment is not part of the stockpile count, and seizure/capitulation paths use the next reconciliation rather than a duplicate transfer grant.

## Event 019 provider coverage

Provider registrations and the setup, template, spawn, sustainment, management, payment, refund, presentation, eligibility, and cleanup callback surfaces are present for 504 Clone Infantry, 505 Autonomous Robot, 506 Paleogenetic Creature, 507 Xenobiological Assault Organism, 508 Alien Infantry, 509 Portal Raider, 510 Temporal Guard, and 522 Aryan Clone Infantry.

Provider 508 is explicitly `spawn_only`, owns the `event019_provider_508` alien contact receipt, and its cleanup callback revokes that receipt only before dispatching the shared provider cleanup. Provider 508 has no Event 019 standing manpower or equipment obligation because the alien landing API owns the exact 2,000-laser reservation and rollback.

Providers 504 and 522 charge 15 Army Experience, 900 infantry equipment, 10 clone equipment, and 10,000 manpower for the initial trainability transaction, then the normal unlocked template scales through the battalion need block instead of an artificial division cap. Providers 505-510 use their per-request equipment, manpower, political-power, command-power, or landing contracts; the legacy native cap variables are cleared by the Event 016 rebuild and only bounded one-time opening `create_unit` helpers remain.

## CXT and localisation coverage

The Event 016 CXT carrier is `chaosx_cxt_extension_event016_alien_infantry` with the required `_apply` effect. Startup registration is bounded to an existing country, and `on_daily_CXT` provides tag-scoped recovery. The registration includes seven concrete equipment tokens, eight frontline subunit tokens, and one locked Alien Landing Cohort with `force_allow_recruiting = no`; the processed-frontline array prevents duplicate harness formations.

The matching localisation defines names and descriptions for every generic unit, every Event 016 and clone equipment ID, the clone reserve modifier, and Event 019 profiles 504-510 and 522. The profile key `xenobiological_organism` is an internal Event 019 profile label that maps consistently to the generic `xenobiological_assault_organism` unit and equipment IDs; no missing localisation key was found.

## Changed files and validation evidence

Only this handoff file was added: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_unit_equipment_mechanics_audit_2026-09-05.md`.

No owned gameplay file was changed because no confirmed local defect met the patch threshold.

Validation consisted of the required offline wiki and vanilla-documentation review, direct source and consumer inspection, exact identifier and old-name searches, callback and enum census, CXT carrier/consumer inspection, manual per-battalion and template arithmetic, and the mandatory technology MCP attempts recorded above. Hearts of Iron IV was not launched; live stockpile aggregation, CXT designer exposure, technology rendering, and the robot power interpretation remain engine or parent/user validation items.

No 3D, runtime model, entity, sound, particle, or counter completion claim is made by this handoff.

## Remaining omissions and blockers

- Robot power-infrastructure enforcement has no confirmed supported engine surface in the current owned files.
- Technology inspect, render, and compare MCP calls timed out or rejected the initial malformed compare shape, and the standalone Technology Tree Viewer is unavailable.
- Concrete-child versus archetype aggregation for `num_equipment@clone_equipment` needs engine evidence even though the source follows vanilla archetype precedent.
- No probability-auditor evidence is available in this runtime because no weighted source was changed and the named auditor route was unavailable.
- Live game acceptance remains with the parent and user; this subagent did not launch the game.
