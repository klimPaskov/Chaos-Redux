# Asset inventory

| Asset ID | Type | Runtime role | Source mode | Target or verified family | Animation | Required |
| --- | --- | --- | --- | --- | ---: | ---: |
| `025_super_event_discovery` | Super-event image | Opening reveal | Generated | Current super-event canvas, expected 457x328 | No | Yes |
| `025_news_winner` | News image | Winner announcement | Generated | Current news canvas, expected 397x153 | No | Yes |
| `025_report_departure` | Report image | Expedition departure | Generated | Current report canvas, expected 210x176 | No | Yes |
| `025_report_outpost` | Report image | Outpost established or damaged | Generated | Report canvas | No | Yes |
| `025_report_survey` | Report image | Survey and triangulation | Generated | Report canvas | No | Yes |
| `025_report_fragment` | Report image | Fragment recovery | Generated | Report canvas | No | Yes |
| `025_report_sabotage` | Report image | Route or outpost interference | Generated | Report canvas | No | Yes |
| `025_report_rescue` | Report image | Rescue operation | Generated | Report canvas | No | Yes |
| `025_report_final_recovery` | Report image | Final approach | Generated | Report canvas | No | Yes |
| `025_report_survivor_trace` | Report image | Evolution II | Generated | Report canvas | No | Yes when evolution enabled in final package |
| `025_report_militarised` | Report image | Evolution III | Generated | Report canvas | No | Yes when evolution enabled in final package |
| `025_report_fragment_field` | Report image | Evolution IV | Generated | Report canvas | No | Yes when evolution enabled in final package |
| `025_report_dependence` | Report image | Evolution V accident or policy | Generated | Report canvas | No | Yes when evolution enabled in final package |
| `025_board_background` | GUI panel | Full Expedition Board | Generated | GUI reference canvas | No | Yes |
| `025_board_sector_map` | GUI map art | Six Antarctic sectors | Generated or map-derived illustration | Board center panel | State variants | Yes |
| `025_value_progress` | GUI icon | Expedition Progress | Generated icon | Verified GUI icon size | No | Yes |
| `025_value_readiness` | GUI icon | Logistics Readiness | Generated icon | Verified GUI icon size | No | Yes |
| `025_value_exposure` | GUI icon | Exposure Risk | Generated icon | Verified GUI icon size | No | Yes |
| `025_value_dependence` | GUI icon | Alien Dependence | Generated icon | Verified GUI icon size | Optional loop | Yes |
| `025_route_icons` | GUI icon family | Route families and interruptions | Generated icons | Verified GUI icon size | No | Yes |
| `025_outpost_icons` | GUI icon family | Outpost states | Generated icons | Verified GUI icon size | No | Yes |
| `025_sector_states` | GUI state family | Unknown through recovered sectors | Generated or exact board geometry | Sector pieces | Optional signal overlay | Yes |
| `025_rival_frames` | GUI frame family | Rival card states | Generated UI art | Rival card canvas | No | Yes |
| `025_action_icons` | Decision icon family | Phase and evolution actions | Generated icons | Decision icon precedent, expected 32x32 | No | Yes |
| `025_category_picture` | Decision category picture | Ordinary category identity | Generated | Verified category-picture consumer | No | Yes |
| `025_idea_icons` | Idea icon family | Winner aftermath lifecycle | Generated icons | Idea precedent, expected 64x64 | No | Yes |
| `025_signal_loop` | Frame animation | Evolution I active signal | Generated per frame | Board overlay | Yes | Recommended |
| `025_survivor_trace_loop` | Frame animation | Evolution II moving trace | Generated per frame | Board overlay | Yes | Recommended |
| `025_fragment_instability_loop` | Frame animation | Evolution IV unstable debris | Generated per frame | Board overlay | Yes | Recommended |
| `025_dependence_loop` | Frame animation | Evolution V system activity | Generated per frame | Aftermath panel | Yes | Recommended |
| `025_achievement_*` | Achievement triplets | Fourteen achievements | Generated icons | Achievement root and native canvas | No | Yes |
| `025_super_event_audio` | WAV and sound definitions | Opening super-event | Sourced licensed music | 1 to 2 minutes | Audio | Yes |

## Explicitly excluded asset families

- character portraits
- new country flags
- focus icons
- custom unit counters
- 3D spacecraft or building models
- skeletal animations
- advisor cards

These exclusions follow the accepted gameplay scope. They are not missing assets.
