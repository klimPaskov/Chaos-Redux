# Shared Clone Equipment and Infantry

## Purpose

The clone system is a provider-neutral gameplay API for any Chaos Redux event that creates, captures, transfers, or fields artificial human soldiers.

The stable public identifiers are `clone_equipment`, `clone_equipment_1`, `clone_infantry`, `aryan_clone_infantry`, `clone_infantry_access_tech`, `clone_grant_infantry_access`, `clone_select_kruger_refinement`, `clone_select_mengele_refinement`, and `clone_select_mengele_aryan_refinement`.

## Access contract

`clone_infantry_access_tech` and every provider refinement use `allow = { always = no }`. They cannot be selected from the ordinary research menu and are granted only by scripted project or event results.

Kruger reaches cloning through `sp_brilliant_scientist_cloning` and the Event 016 project-stage system. Mengele reaches it through the separate `sp_mengele_cloning` project, which grants `clone_select_mengele_refinement`. No other country can initiate either cloning project through the normal project interface, although another event may deliberately grant the provider-neutral clone API result to its winner.

## Equipment and reserve manpower

One unit of `clone_equipment` represents one viable standardized clone cohort.

Every full unit physically present in a country's stockpile contributes `10` weekly manpower through `clone_reserve_manpower`.

The weekly on-action calls `clone_refresh_reserve_manpower`, reads `num_equipment@clone_equipment`, rounds the physical stockpile, and refreshes the visible dynamic modifier.

Deployed clone equipment does not count as reserve manpower because it is assigned to divisions rather than held in the stockpile.

Captured, transferred, or lend-leased clone equipment provides reserve manpower to its current holder even if that country cannot manufacture clones.

## Battalion and template

`clone_infantry` uses `1,000` manpower, `90` infantry equipment, and `1` clone equipment per battalion.

Its organization is higher than ordinary infantry, while its HP is lower, so clone divisions hold formation well but suffer heavily when they take losses.

`clone_grant_infantry_access` enables manufacture and recruitment and creates one editable ten-battalion, 20-width `Clone Infantry Division` template.

The Event 019 unit-family provider uses the same ten-battalion contract and charges the corresponding rifles, clone equipment, manpower, and army experience.

## Provider refinements

`clone_select_kruger_refinement` grants the Event 016 cloning refinement and removes Mengele's refinements.

`clone_select_kruger_weaponization` adds the stronger Event 016 weaponization layer.

`clone_select_mengele_refinement` grants ordinary Mengele clone conditioning to `clone_infantry` and removes both Event 016 refinement layers.

`clone_select_mengele_aryan_refinement` preserves that ordinary clone access, enables the stronger `aryan_clone_infantry` battalion, and creates its separate 20-width template.

These provider refinements are normally exclusive, while the shared equipment and battalion identifiers remain reusable.

## Assets and runtime wiring

The equipment icon token is `GFX_archetype_clone_equipment`, defined in the clone equipment GFX registry and consumed by `picture = archetype_clone_equipment`.

The unit sprite token is `clone_infantry`; its entity, mesh, materials, actions, and audio live under the shared clone asset package and are registered without Event 016 or Mengele names.

Kruger clones and ordinary Mengele clones both consume `clone_infantry_entity`.

The separate `aryan_clone_infantry` consumer resolves through `aryan_clone_infantry_entity`, which directly clones the installed `GER_infantry_entity` family for standard, snow, and desert variants.

The large counter tokens are `GFX_group_clone_infantry_icon` and `GFX_unit_clone_infantry_icon_medium`.

The map counter token is `GFX_unit_clone_infantry_icon_medium_white`.

Aryan clone counters use `GFX_unit_aryan_clone_infantry_icon_medium` and `GFX_unit_aryan_clone_infantry_icon_medium_white` and intentionally depict conventional German infantry rather than the generated generic clone body.

The repaired death action is accepted after export and canonical reimport with terminal ground contact within `0.000045` Blender units.

Attack, support-attack, and training use their exact exported actions and have complete runtime references, but combined rifle contact remains visually unaccepted because the locked adapter cannot create a hand locator or preview a second mesh attached to the recovered skeleton.

The runtime entity therefore does not invent an attachment node or register a detached rifle entity.

Source packages, license records, checksums, previews, Blender checkpoints, export proof, and handoffs live under `docs/assets/shared_clone_system/` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/`.

## Future extensions

Future events should grant the shared access effect and then add only their own provider refinement when their clones need distinct behavior.

Future clone types can reuse the same equipment economy or introduce a separate archetype only when capture, transfer, production, and manpower behavior must be causally distinct.
