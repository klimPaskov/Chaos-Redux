# Event 013 Natural Disasters, source-to-file surface map

This map is a handoff for live repository work. It names the surfaces the implementation must inspect and keep aligned. Exact file paths may differ in the live repository, so the coding agent must verify them before editing.

## Primary gameplay surfaces

| Surface | Likely owner | Source files that define behavior | Notes for the implementation pass |
| --- | --- | --- | --- |
| Event 013 sequence controller | Event script and scripted helpers | Parts 1, 2, 5, 7 | Entry event should own sequence start and one-row logging. Delayed subevents stay internal. |
| Disaster call contract | Scripted effects, scripted triggers, constants | Part 2, disaster call matrix, coding prompt | Must support direct family calls and random calls. |
| Target resolver | Scripted effects and triggers | Part 2, Part 8 | State, country, region, random valid target, and caller-provided target modes need safe validation. |
| Warning model | Events, decisions, scripted helpers | Parts 2, 3, 8, 10 | Family warnings can open preparation choices and lower losses without canceling disaster identity. |
| Impact model | Scripted effects, dynamic modifiers, state modifiers | Parts 2, 3, 8 | Damage must vary by family and vulnerability. |
| Deaths integration | Shared Deaths-system helper | Parts 1, 2, 3, 7, 8 | Population loss must feed the shared tracker and remain visible. |
| Report events | Events and localisation | Parts 1, 4, 6, 8, news report matrix | Serious affected countries receive delayed reports after impact. |
| News events | News event files and localisation | Parts 1, 6, 8, news report matrix | Early meaningful hits can be public. Later news needs throttling. |
| Aftermath category | Decision category, decisions, missions, localisation | Parts 4, 8, 10, aftermath matrix | Category should open visibly and manage active cards. |
| Foreign relief | Decisions, missions, AI, scripted helpers | Part 10 | Relief should be useful but not free or always optimal. |
| Evolution I | Event logic and constants | Part 5, Part 7 | Wider family pool and more active sequence. |
| Evolution II | Event logic, regional spread helpers, aftermath chains | Parts 5, 7, 8, 10 | Regional damage, stronger scaling, and chained aftermath. |
| Evolution III | Abnormal controller, GUI, super-events | Parts 5, 6, 8, 9 | Abnormal disaster age with moving systems and large impacts. |
| Disaster Barrage | Triggerable scenario registry and launch effects | Part 5, docs alignment, scenario catalog | Same controller, type and intensity controls, no world-end branch. |
| Natural Disasters cluster | Cluster constants and cluster runtime logic | Part 5, catalog notes | Cluster can include repeated Event 013 sequence behavior and tiered severity. |

## Event-log and catalogue surfaces

| Surface | Likely owner | Required alignment |
| --- | --- | --- |
| Event name mapping | Event-name localisation and scripted localisation | Event 013 must resolve as Natural Disasters and show correct type. |
| History row | Events log scripted effects | One row per Event 013 sequence. No rows for subevents. |
| Evolution rows | Events log scripted effects and scripted localisation | Evolution I, II, and III must show as mutation tracks, not ordinary baseline stages. |
| Event Details | Scripted localisation and GUI localisation | Describe premise and visible situation, not mechanical effect lists. |
| Cluster details | Cluster scripted localisation and GUI localisation | Natural Disasters cluster shows Event 013 repeated sequence behavior. |
| Scenario details | Triggerable scenario localisation | Disaster Barrage describes type choices and intensity behavior after final wording exists. |
| Spreadsheet | Event catalog workbook | Update after final in-game text exists, using spreadsheet worker. |

## Asset and presentation surfaces

| Surface | Likely owner | Required alignment |
| --- | --- | --- |
| Report images | Asset package and event picture GFX | Family or severity assets must match report usage. |
| News images | Asset package and news event GFX | Images must support family-specific public reports and news throttling. |
| Decision and category icons | Asset package and interface GFX | Aftermath category, preparation, rescue, stabilization, reconstruction, and relief need icon coverage. |
| State modifier icons | Asset package and modifier GFX | Transport disruption, ash, crater, drought, refugee, storm, heat, cold, and related states need readable symbols where implemented. |
| Achievement icons | Achievement assets and registry GFX | Completed, grey, and not-eligible variants must match achievement ids. |
| Abnormal GUI assets | GUI, GFX, scripted GUI, asset manifests | Map panel, path lanes, cards, warning states, animated sprites, and static fallbacks must align. |
| Super-event image and audio | Super-event GFX, music, sound, localisation, docs | Only after text, image, and audio research packages are complete. |

## Surrounding event surfaces

| Event | Required alignment |
| --- | --- |
| Event 046 | Remains inactive unknown placeholder. No separate Earth Earthquake logic. |
| Event 051 | Remains separate Heat Wave event. Event 013 heat calls avoid stacking. |
| Event 099 | Placeholder or narrow bridge into Event 013 dust and sandstorm calls. |
| Events that call disasters | Use the reusable Event 013 call contract and do not copy disaster logic. |

## Audit surfaces

| Audit | When to run | What it should prove |
| --- | --- | --- |
| Scripted-system architecture review | Before family expansion | Helpers, constants, event targets, cleanup, and call sites are reusable. |
| Decision and mission audit | After recovery tranche | Category is staged, capped, clear, AI-usable, and not exploitable. |
| Localisation audit | After final text exists | Keys, dynamic values, style, encoding, and research boundaries are correct. |
| Asset review | Before visual completion claim | Required assets, DDS files, manifests, and GFX handoffs exist. |
| Super-event research review | Before super-event wiring | Quotes, remarks, image, audio, source, license, and blockers are documented. |
| Completion audit | Before final completion | Spec requirements, implementation, assets, docs, and validation evidence align. |
