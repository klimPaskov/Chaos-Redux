# Cure Raid Payload Correction

## Acceptance basis

The authorized CBRN overhaul requires every actual CBRN raid to identify and consume a matching stockpiled weapon. The parent task explicitly assigned the `zombie_cure_strike` gap for implementation on 2026-09-27. This correction describes that accepted bounded change and does not alter the offensive zombie branch.

## Contract

Completing `sp:zombie_cure_bomb` directly unlocks buildable `zombie_cure_bomb_1` through the project's native `enable_equipments` output, without a separate research technology. The project retains the `anti_zombie_bomb_available` raid gate. A country supplies the raid by producing the concrete cure payload; each prepared raid reserves one from the `zombie_cure_bomb_equipment` archetype through native `essential_equipment`. Human and AI raids follow the same stockpile rule. No scripted effect removes or refunds that payload.

The cure payload costs 12 IC, two rubber, and one steel. Its narrower treatment role justifies a lower factory cost than the existing 18 IC offensive zombie payload, while the cure raid still requires ten Command Power, ten preparation days, and a bomber formation. These values are an accepted implementation choice within the requested stockpile integration and remain balance candidates for live validation.

At launch, a target must still be an untreated zombie-threatened state with an active cure. At a successful resolution, the effect checks those conditions again; a stale target receives a neutral no-effect tooltip. The native engine owns the reservation and cancellation outcome, and its cancellation refund behavior remains a user-run live validation question.

## Wiring and presentation

The equipment archetype and variant live in `common/units/equipment/zombie_special_bombs.txt`; both are listed in `common/script_enums.txt`. The special project output lives in `common/special_projects/projects/biowarfare_main_projects.txt`, and the raid cost and final gates live in `common/raids/biological_zombie_cure_raid.txt`. English equipment, project, and raid text explain production and use. Existing `gfx/interface/technologies/zombie_cure_bomb_equipment.dds` is referenced by `GFX_zombie_cure_bomb_equipment` and `GFX_zombie_cure_bomb_equipment_medium` in `interface/chaosx_equipment.gfx`; no new icon or GFX registration is needed. The existing raid map and project icons remain the presentation art.

The package-owned CXT carrier, startup registration, tag-specific fallback, and idempotent setup effect register the concrete equipment token for the shared fixture. They do not add a periodic grant.

## Validation and limits

Source review verifies the native special-project unlock syntax and the raid `essential_equipment` reservation syntax against installed game documentation and vanilla precedents. The production menu, actual stockpile collection, cancellation outcome, and target-loss display remain live-game questions for the user. This change does not assume or promise a native refund.

The installed `common/raids/_documentation.md` lines 165-186, revision `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e`, states that archetype stock is a precondition for creating a raid and is collected after creation. The installed `common/special_projects/special_projects_documentation.md` lines 238-254, revision `e5d1766e95fe9c71d676046720bb699918e2565c8a43fe5a9183359c98bfcbfe`, states that `project_output.enable_equipments` makes equipment available as the project reward. The offline `paradox_wiki/Equipment modding - Hearts of Iron 4 Wiki.md` lines 35-59, revision `8f1f9fe2bf72543697095b10bff8e80347533aeb372e7b4ac6c527c1bdeb1172`, distinguishes archetypes, buildability, and inactive variants. The installed vanilla `common/special_projects/projects/air_projects.txt` lines 426-429 and `common/raids/naval_commando_raids.txt` lines 225-228 provide matching project-output and native-reservation precedents.

The HOI4 MCP technology scan returned revision `1d4349c27d735797c7c807e31a3ec6888e78fa52e78e72e1bb1cf6e371b79cb0` with helper projections deferred in this large workspace; the later equipment impact graph returned source revision `26ee627bf97ff0056a8db1c87bacfe62a34048da20640d57141ac5dc691ca2f6` and partial dynamic-reference coverage. `hoi4.source_lookup` did not index the special-project identifier, and `hoi4.probability_inspect` exposes no raid or special-project adapter. Those routes do not establish live production, raid AI supply, or cancellation outcomes. No AI weight was changed in this correction.

The cure variant deliberately has no aircraft range, speed, agility, or bombing stats. The installed equipment schema treats unit stats as base values, while `is_buildable`, unlock state, grouping, and `interface_category` control production availability and placement. The existing buildable `choking_chemical_air_payload_lot_1` in `common/units/equipment/cbrn_payload_equipment.txt` lines 364-374 also uses `interface_category_air` with no aircraft stats; `common/technologies/chaosx_technologies.txt` line 481 unlocks it, and `common/raids/cbrn_chemical_air_raids.txt` lines 109 and 181 reserve its archetype. The two payloads differ in `type` (`infantry` and `support`), which defines equipment use rather than the production category. Production-menu appearance for the new variant remains a live-game validation point.
