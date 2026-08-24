# Event 014 Bone Riders and Elephantry Implementation Handoff

> Superseded snapshot (2026-08-24): this historical handoff predates the consolidated nine-token CXT wrapper and the reusable bridge-technology reset safeguard. Current source of truth is `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_custom_unit_integration_audit_2026-08-24.md`; gameplay IDs and elephantry conclusions below remain valid.

## Outcome

Event 014 now has a ninth custom land sub-unit, `cannibal_bone_riders`, with the sprite token `cannibal_bone_riders`. It is an inactive, horse-mounted cavalry sub-unit in the mobile group with `type = { infantry }`, `category_cavalry`, and the shared `category_cannibal_irregular_infantry` category. It consumes real infantry equipment and is created only through the existing locked, paid Event 014 formation contract.

The installed vanilla `elephantry` technology is granted to every newly created Event 014 warlord, unified CBL, and the existing Wendigo inherited-recruitment path. The locked `Scavenged Elephant Column` template uses one vanilla `elephantry` battalion and one recon support company. It does not create a new elephant sub-unit, sprite token, model, counter, or equipment archetype.

## Exact stat comparison

The effective speed formula is `equipment base speed × (1 + sub-unit maximum_speed)`. Vanilla infantry equipment has a 4 km/h base and vanilla cavalry has a 0.6 maximum-speed modifier, yielding 6.4 km/h.

| Definition | Effective speed | Max organisation | Max strength | Soft attack | Breakthrough | Defence | Equipment need | Availability |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Vanilla infantry | 4.0 km/h | 60 | 25 | 0 | 0 | 0 | 100 infantry equipment | Vanilla `active = no` line unit |
| Vanilla cavalry | 6.4 km/h | 70 | 25 | 0 | 0 | 0 | 120 infantry equipment | Vanilla `active = yes`, `cavalry = yes` |
| `cannibal_bone_riders` | `4 × (1 + 1.6) = 10.4` km/h | 16 | 10 | 13 | 19 | -6 | 140 infantry equipment | Event 014 locked templates only |
| Event 014 March reference | `12 × (1 + 1.2) = 26.4` km/h | 14 | 10 | 12 | 18 | -7 | 100 infantry equipment + 35 motorized equipment, including `transport = motorized_equipment` | Fastest Event 014 family |

The Bone Riders values are deliberately direct battalion stats, so `defense = -6` is an absolute additive sub-unit stat rather than a percentage modifier. The low organisation and strength offset the high attack and breakthrough profile.

Vanilla `elephantry` remains equipment-bound at 3.0 km/h from `4 × (1 - 0.25)`, 55 organisation, 30 strength, 260 infantry equipment, and 30 artillery equipment. Its installed technology is `common/technologies/infantry.txt#elephantry`, and its unit precedent is `common/units/cavalry.txt#elephantry`.

## Recruitment and access flow

- `cannibalism_create_current_warlord_templates` creates and locks `Bone Riders` and `Scavenged Elephant Column`, and force-disables ordinary template recruitment for both.
- The existing warlord Bone Guard decision remains the population, Larder, support-equipment, artillery-equipment, and infantry-equipment gate. Once the Bone Guard route is opened, its first successful paid contract creates `Bone Riders`, its second creates `Scavenged Elephant Column`, and later contracts create `Bone Guard` as before. Each transaction consumes the existing exact Deaths population loss and Larder payment, and no focus or unlock grants a unit by itself.
- The existing unified CBL Bone Guard decision uses the same bounded sequence after the unified Bone Guard focus opens. CBL receives `elephantry = 1` at creation, and the template remains locked.
- The regular warlord setup, unified CBL creation, and inherited Wendigo recruitment path receive `elephantry = 1` alongside their existing prerequisites. No new equipment type or `common/script_enums.txt` entry was needed.
- Warlord rollback/release cleanup, incarnation reset locks, unified creation, and the Event 019 owner adapter include the new custom sub-unit and both new template names. The Event 019 provider remains spawn-only and does not alter Cannibalism progression.

## CXT and Event 019 registration

`common/on_actions/014_cannibalism_on_actions.txt` adds an idempotent `cannibal_bone_riders` frontline registration to the existing bounded `on_startup` and `on_daily_CXT` paths. The startup path gives the first `e chaosx_test` invocation the token immediately, while the tag-scoped daily path repairs an existing save without a world iteration. The consolidated Event 014 CXT wrapper now owns all nine custom tokens, including `cannibal_bone_riders`, through the idempotent carrier path. The bounded startup and tag-scoped daily hooks remain the registration contract; the former direct additive handoff is historical.

The Event 019 provider adapter in `common/scripted_effects/014_cannibalism_effects.txt` and `docs/events/019_infantry_spawn/systems/unit_family_coverage.md` now include the ninth combat token. Its existing family-only, spawn-only contract and ordinary equipment obligations remain unchanged.

## Changed files

- `common/units/014_cannibalism_irregular_infantry.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `common/on_actions/014_cannibalism_on_actions.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `docs/testing/chaosx_test_country.md`
- `docs/events/014_cannibalism/overview.md`
- `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`
- `docs/specs/014_cannibalism_specs/README.md`
- `docs/specs/014_cannibalism_specs/matrices/asset_inventory_matrix.md`
- `docs/specs/014_cannibalism_specs/quality/package_status.md`
- `docs/specs/014_cannibalism_specs/quality/package_validation.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_4_country_packages.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_10_assets_animation_and_localisation.md`
- `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_12_acceptance_criteria.md`
- `docs/plans/014_cannibalism_plans/014_cannibal_irregular_unit_model_plan.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/014_bone_riders_elephantry_implementation_2026-08-22.md`

The existing shared category in `common/unit_tags/chaosx_categories.txt` was verified and did not require an edit. `common/script_enums.txt`, decisions, and triggers were intentionally not changed because this tranche's ownership excludes them and no new equipment archetype or decision weight was introduced.

## Validation and evidence

- Direct vanilla references were read from `common/units/infantry.txt`, `common/units/cavalry.txt#elephantry`, and `common/technologies/infantry.txt#elephantry`; the installed infantry and cavalry speed, organisation, strength, equipment, cavalry, mobile-group, and transport precedents match the implementation above.
- Targeted Clausewitz structure checks passed for the changed unit, effect, on-action, and localisation files. The localisation file retains its UTF-8 BOM and the new keys have no `:0` suffix.
- The final mandatory Event 014 MCP inspect returned `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, revision `23147097ed55f495962df914f2ff83640db5fd37835e3cc09277860bfb43069f`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/984a3248827027eee8ffabcaf5e750867c7cf407334073fb2ab3dfec393cdc63/ca2c92be0040d40eeeba770a872e470807f61e85a95da778f13b9d8c933786a2/event-lint-23147097ed55.json`.
- The final bounded Event 014 MCP state render returned `EVENT_RENDERED_PARTIAL`, zero blockers, and artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57f4486e0c6645db3a651efcb358e5e3b927268cb1bdf8031bb04b46d8425eb6/511adfbf95c84980d746c9f2f4c859b3d346b12fb4e26531bb69189d4146553e/event-state-23147097ed55-manifest.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b587ff722458cf4b0dfc38c278b3c26973e0a63dc20c17c3ce4bb9c6e92014bf/5035c86b8c15338abc08fb65cdd4d2adceffd37089441f0d81e2a69e6aa64dd5/event-state-23147097ed55.json`, with linked SVG and PNG siblings.
- The mandatory vanilla `elephantry` MCP inspect returned `TECH_INSPECTED_PARTIAL` with no blockers and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b95f4f852d4319cf35d06e4d178b2480af7ed9da2606e4db43d5bdad2d4871b6/54c25a2d1bfcf03443fd1b45ad87125a2227e90d93df346c7ca7a1f9d9de6326/technology-lint-f302a0c138a2.json`. Its render returned `TECH_RENDERED_PARTIAL` with no blockers and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b79af24893bdf34ccd15b2ac38f19a20a96fe88b628998e31e9c53d14a9ca0f/cd4b690d2a5e0d8b9f08a8a5a1ecbdac6a5a663a05059c8dd000c3ed90db65ce/technology-technology-f06d428204c8.json`, with linked SVG and PNG siblings.
- No AI weight, MTTH, strategy factor, or probability-bearing surface changed, so the mandatory probability auditor/compare pass was not applicable.
- No live HOI4 session was launched. Model, entity, mesh, animation, GFX, DDS, counter, and sound work remains with the parent asset workers.

## Remaining risks and blockers

- The existing Bone Guard decision still carries the visible Bone Guard label; its localisation now explains the first-two-contract Bone Riders and Scavenged Elephant Column sequence. A future dedicated decision split would require edits to the excluded decisions, triggers, and shared constants surfaces.
- The Event 014 CXT wrapper now contains all nine custom tokens, including Bone Riders. The earlier eight-token/direct-additive description in this historical handoff is superseded by the current wrapper and the audit cited above.
- The MCP analyses are intentionally partial because the installed adapters defer large workspace helper projections and report many unrelated unresolved nodes. They returned no blocking diagnostics for the requested Event 014 or `elephantry` selectors.
- Parent-owned 3D/model/entity/counter/sound outputs are not present in this gameplay tranche and remain required before visual runtime acceptance.
