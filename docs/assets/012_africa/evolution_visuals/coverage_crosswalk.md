# Event 012 Africa Evolution Visual Coverage Crosswalk

## Coverage result

All six visual requirements listed in `docs/events/012_africa_evolutions.md` are complete at their exact registered paths. The three incident sprites are consumed directly by `chaosx.nr12.401`, `chaosx.nr12.402`, and `chaosx.nr12.403`. The three portrait sprites are selected for Event 12 evolution stages I through III by `GetEventsLogSelectedEvolutionPortrait` in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`.

| Requirement disposition | Count |
| --- | ---: |
| Direct evolution-document requirement | 6 |
| Exact registered texture completed | 6 |
| Alias, substitute, or fallback | 0 |
| Missing or unmatched requirement | 0 |

The Event 012 asset/animation matrix contains no explicit evolution-visual row. The live source of truth for this bounded package is therefore the six-row asset table in `docs/events/012_africa_evolutions.md`, cross-checked against the existing GFX registry and live consumers. The matrix was not edited and no synthetic asset key was added.

## Requirement-to-runtime mapping

| Evolution | Requirement surface | Live consumer | Registered sprite | Final texture | Runtime state |
| --- | --- | --- | --- | --- | --- |
| I - Regional Consolidation | Incident | `events/012_africa_evolutions.txt`, event `chaosx.nr12.401` | `GFX_report_event_012_africa_evolution_regional_consolidation` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_regional_consolidation.dds` | Complete and registered |
| II - Continental Machinery | Incident | `events/012_africa_evolutions.txt`, event `chaosx.nr12.402` | `GFX_report_event_012_africa_evolution_continental_machinery` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_continental_machinery.dds` | Complete and registered |
| III - Africa as a World Pole | Incident | `events/012_africa_evolutions.txt`, event `chaosx.nr12.403` | `GFX_report_event_012_africa_evolution_world_pole` | `gfx/event_pictures/012_africa/evolutions/report_event_012_africa_evolution_world_pole.dds` | Complete and registered |
| I - Regional Consolidation | Event Log detail | `GetEventsLogSelectedEvolutionPortrait`, Event 12 stage I | `GFX_portrait_012_africa_evolution_regional_council` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_regional_council.dds` | Complete and registered |
| II - Continental Machinery | Event Log detail | `GetEventsLogSelectedEvolutionPortrait`, Event 12 stage II | `GFX_portrait_012_africa_evolution_continental_secretariat` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_continental_secretariat.dds` | Complete and registered |
| III - Africa as a World Pole | Event Log detail | `GetEventsLogSelectedEvolutionPortrait`, Event 12 stage III | `GFX_portrait_012_africa_evolution_world_pole_delegation` | `gfx/leaders/012_africa/evolutions/portrait_012_africa_evolution_world_pole_delegation.dds` | Complete and registered |

## Narrative-to-visual mapping

| Evolution text obligation | Incident visual response | Log-detail identity response |
| --- | --- | --- |
| Corridors carry claims, debts, local terms, representation, and first regional guarantees | Active review of a freight ledger at a rail cargo corridor | Circular regional council chamber with ledger and route plans |
| Minutes become budgets, timetables, reserve plans, accession statutes, and visible integration burdens | Staffed African secretariat operating files, typewriters, telephones, and schedules | People-free administrative bureau with the same working instruments |
| Recognition, embargoes, bases, expeditions, and continent-scale diplomacy become international questions | African delegation positioned as the arriving central diplomatic party | Formal diplomatic station with portfolios, microphones, dispatch case, and press gallery |

## Evidence locations

- Requirement document: `docs/events/012_africa_evolutions.md`
- Incident consumers: `events/012_africa_evolutions.txt`
- Event Log portrait consumer: `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- Registration: `interface/012_africa_evolutions.gfx`
- Player-facing wording: `localisation/english/012_africa_evolutions_l_english.yml`
- Visual review: `contact_sheets/evolution_visuals_source_processed_dds_contact_sheet.png`
- Technical audit: `validation/evolution_visuals_validation.tsv`
