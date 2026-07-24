# Event 012 Africa Evolution Visual GFX Handoff

## Result

All six sprite definitions already exist in `interface/012_africa_evolutions.gfx`. Their registered texture paths exactly match the final DDS files produced by this package, so no GFX edit or integration block is required.

| Sprite | Registered and completed texture | Dimensions |
| --- | --- | ---: |
| `GFX_report_event_012_africa_evolution_regional_consolidation` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_regional_consolidation.dds` | 210 x 176 |
| `GFX_report_event_012_africa_evolution_continental_machinery` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_continental_machinery.dds` | 210 x 176 |
| `GFX_report_event_012_africa_evolution_world_pole` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_world_pole.dds` | 210 x 176 |
| `GFX_portrait_012_africa_evolution_regional_council` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_regional_council.dds` | 156 x 210 |
| `GFX_portrait_012_africa_evolution_continental_secretariat` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_continental_secretariat.dds` | 156 x 210 |
| `GFX_portrait_012_africa_evolution_world_pole_delegation` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_world_pole_delegation.dds` | 156 x 210 |

## Consumer verification

- Event `chaosx.nr12.401` uses the regional-consolidation report sprite.
- Event `chaosx.nr12.402` uses the continental-machinery report sprite.
- Event `chaosx.nr12.403` uses the world-pole report sprite.
- Event Log evolution stages I, II, and III select the regional council, continental secretariat, and world-pole delegation portrait sprites respectively.
- No alias or fallback sprite is involved.

The portrait token is retained because it is the frozen GUI and scripted-localisation interface. The art deliberately depicts the named collective institution rather than inventing an individual leader.
