# Event 033 report asset paths

Disposition: implemented.
The user's Event 033 visual repair request authorizes correcting stale sprite paths and placing event-owned art in its proper engine folder.
The parent accepted the five report relocations after verifying that their SHA-256 values matched the previously decoded and individually reviewed DDS files.

The final report paths are `gfx/event_pictures/033_acid_rain/033_acid_rain_arrival.dds`, `033_acid_rain_severe.dds`, `033_acid_rain_shelter.dds`, `033_acid_rain_transport.dds`, and `033_acid_rain_dissipation.dds` in the same folder.
All five retain their exact 210x176 BGRA32 pixels and report-card alpha treatment.
Twelve `GFX_report_event_033_acid_rain_*` and `GFX_event_033_acid_rain_*` aliases in `interface/033_acid_rain.gfx` use those existing files.
Their sprite identifiers and gameplay consumers are unchanged.
The five matching working-manifest records use the same paths.

The source, processed PNG, decoded DDS, native-size review, and checksums remain in the active Event 033 asset evidence workspace.
The post-repair inventory contains 80 Event 033 DDS files and no stale prototype registrations or unused runtime files in that inventory scope.
This does not include the eight missing required animation files and is not full asset coverage evidence.

The source lookup request timed out after 600 seconds, and specialist tasks returned workspace-routing timeouts.
No MCP render, engine execution, final GUI acceptance, or full event completion is claimed by this path repair.
The change only restores existing sprite consumers to identical reviewed files at their event-owned paths.
