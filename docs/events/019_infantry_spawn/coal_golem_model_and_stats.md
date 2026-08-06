# Coal Golem Model and Combat Statistics

This document records the oversized coal-golem 3D model contract and the current battalion comparison against the installed vanilla light, medium, and heavy tank battalion definitions.

## Model contract

The coal golem is a single heavy humanoid model with anthracite coal plates, dark iron braces, restrained ember seams, and a furnace chest core.

The model targets source height `12.0` with the vanilla infantry entity scale `0.8` applied exactly once, producing an effective runtime height of approximately `9.6` versus the installed western infantry runtime height of `5.8814594268`.

The runtime consumer is `common/units/coal_golems.txt:sub_units.coal_golem`, and the model package is staged under `docs/assets/chaos_redux_3d_model_pilots/models_3d/coal_golem/`.

## Unit-template comparison

The tank columns below are the exact battalion-template values from the installed vanilla files `common/units/light_armor.txt`, `common/units/medium_armor.txt`, and `common/units/heavy_armor.txt`.

| Stat | Coal golem | Light tank | Medium tank | Heavy tank |
| --- | ---: | ---: | ---: | ---: |
| Combat width | 2 | 2 | 2 | 2 |
| Maximum organisation | 18 | 10 | 10 | 10 |
| Maximum strength | 26 | 2 | 2 | 2 |
| Default morale | 0.22 | 0.30 | 0.30 | 0.30 |
| Maximum speed | 3.40 | Equipment design | Equipment design | Equipment design |
| Reliability | 0.72 | Equipment design | Equipment design | Equipment design |
| Manpower | 10 | 500 | 500 | 500 |
| Training time | 210 days | 180 days | 180 days | 180 days |
| Suppression | 4.00 | 2.50 | 2.50 | 2.50 |
| Weight | 3.20 | 1.00 | 1.25 | 1.50 |
| Supply consumption | 0.55 | 0.22 | 0.25 | 0.32 |
| Base breakthrough field | 32.00 | 0.15 | 0.15 | 0.15 |
| Required equipment or chassis | 70 Coal Golem Equipment | 60 Light Tank Chassis | 50 Medium Tank Chassis | 40 Heavy Tank Chassis |

The golem is therefore slower, heavier on supply, harder to train, and far less manpower-intensive than a tank battalion template, while retaining substantially higher organisation, strength, hardness, and direct combat values in the mod unit definition.

## Combat-stat comparison

Coal-golem combat values are direct subunit values in `common/units/coal_golems.txt`.

Vanilla tank attack, armour, piercing, hardness, and final breakthrough values are equipment-design results rather than fixed battalion-template values, so the tank cells are intentionally marked as design-dependent instead of presenting a misleading single number.

| Combat stat | Coal golem | Vanilla tank battalions |
| --- | ---: | --- |
| Soft attack | 24.00 | Equipment design dependent |
| Hard attack | 20.00 | Equipment design dependent |
| Defense | 24.00 | Equipment design dependent |
| Breakthrough | 32.00 direct unit value | 0.15 battalion base plus equipment design |
| Armour | 58.00 | Equipment design dependent |
| Piercing (`ap_attack`) | 46.00 | Equipment design dependent |
| Hardness | 0.72 | Equipment design dependent |

## Chassis anchors for tank comparison

These are installed vanilla chassis-level anchors for the first modern chassis entries, not complete tank designs.

| Chassis anchor | Light Tank Chassis 1 | Medium Tank Chassis 1 | Heavy Tank Chassis 1 |
| --- | ---: | ---: | ---: |
| Model year | 1934 | 1936 | 1934 |
| Maximum speed | 5 | 5 | 5 |
| Armour value | 15 | 30 | 55 |
| Reliability | 0.95 | 0.80 | 0.80 |
| Base build cost | 2.35 IC | 3.75 IC | 9.00 IC |

The golem's armour value of `58.00` is slightly above the first heavy chassis anchor of `55`, while its speed of `3.40` is below the first heavy chassis anchor of `5` and its supply consumption is higher than every listed tank battalion.

## Production burden

One fully equipped coal-golem battalion requires `70` Coal Golem Equipment.

Each Coal Golem Equipment unit costs `36` IC and consumes `30` coal, `4` steel, `3` chromium, and `2` tungsten, giving a fully equipped battalion an equipment-stock burden of `2,520` IC-equivalent, `2,100` coal, `280` steel, `210` chromium, and `140` tungsten before attrition, reinforcement, or efficiency effects.

Tank production cannot be reduced to one equivalent resource total because the final cost depends on the selected turret, armament, engine, armour, suspension, radio, and special modules.

## Asset and icon wiring

The intended model runtime path is `gfx/models/units/019_infantry_spawn/coal_golem/coal_golem.mesh` with animation assets in the same folder and a parent-owned entity definition using the `coal_golem` sprite token; those runtime files remain blocked by provider rigging failure.

The large counter is `gfx/interface/counters/divisions_large/unit_coal_golem_icon.dds` and is registered as `GFX_unit_coal_golem_icon_medium` in `interface/chaosx_subuniticons.gfx`.

The on-map counter is `gfx/interface/counters/divisions_small/onmap_unit_coal_golem_icon.dds` and is registered as `GFX_unit_coal_golem_icon_medium_white` in `interface/chaosx_subuniticons.gfx`.

The existing counter source, processed PNG, DDS, and contact-sheet evidence is under `docs/assets/chaos_warfare_system/stage_10_cbrn_counter_icons/v3_counters/`.

## Future plans and suggestions

The next balance pass should compare a fully designed 1936 medium tank and 1934 heavy tank against the golem in the same division template, because the current tank values are intentionally equipment-design dependent.

The visual package can later add a separate furnace-vent attack effect or a foundry-specific alternate material, but those additions should remain separate from the base unit mesh so the shared Event 019 model stays reusable.
