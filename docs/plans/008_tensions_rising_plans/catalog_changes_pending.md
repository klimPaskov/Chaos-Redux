# Event 008 catalog changes pending

**Status:** Exact in-game wording prepared for a later authorized workbook update; workbook and export CSVs were not edited in this task.

The catalog row should remain `Needs Testing`. Update the Event Details and evolution-detail fields from the current localization keys below so the workbook matches the player-facing text. Preserve the runtime/workbook Cluster 3 discrepancy as unresolved rather than changing cluster identity, membership, severity, or detail based only on source implementation.

**Event Details** (`chaosx.events_log.window.event_details.tensions_rising`): “Public accusations and leaked military cables spread rumours of war. Embassies guard their entrances, shipping grows dearer, and frontier commanders put their patrols on alert.”

**Evolution I — Cable Traffic Increase** (`chaosx.events_log.window.evolution_details.tensions_rising.title.stage_1`; `...body.stage_1`): “Embassy telegraph rooms work through the night as leaked cables fill the papers. Rumours of mobilisation deepen distrust between neighbouring capitals.”

**Evolution II — Competing Accusations** (`chaosx.events_log.window.evolution_details.tensions_rising.title.stage_2`; `...body.stage_2`): “Rival governments accuse their neighbours of preparing for war. Newspapers repeat the accusations, and border commanders tighten their patrols.”

**Evolution III — Staff Readiness** (`chaosx.events_log.window.evolution_details.tensions_rising.title.stage_3`; `...body.stage_3`): “General staffs work through the night preparing troops for mobilisation. Exhausted officers weigh fresh rumours, and frontier patrols grow quicker to challenge unfamiliar movements.”

**Evolution IV — Extended Alert** (`chaosx.events_log.window.evolution_details.tensions_rising.title.stage_4`; `...body.stage_4`): “Troops remain on alert along the frontier as commanders delay leave. Fresh accusations deepen distrust, and exhausted patrols risk turning a confrontation into a clash.”

The selected wording is sourced from `localisation/english/008_world_tension_rises_l_english.yml`. A workbook editor must update its Event Details and evolution-detail fields together and then run `python .tools/export_event_catalog_csv.py` from the mod root. The event-category row remains `Needs Testing`; its cluster assignment and cluster-detail wording require the cluster owner to reconcile the workbook's Cluster 3 Diplomacy record with the current shared runtime definition.
