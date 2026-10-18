# Belgium and Congo package (block 2)

Verbatim part of [system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md](system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md), which indexes this specification.

## Belgium and Congo package

Belgium should receive a Congo extraction and concession labor system. It should provide meaningful wartime resource and exile-economy pressure while damaging Congo and creating severe colonial accountability risk.

### State-pool logic

| Working trigger | State pool | Use |
| --- | --- | --- |
| `is_bel_congo_concession_pool_state` | Belgian Congo controlled states, especially rubber, mineral, transport, and concession regions | Main extraction pool. |
| `is_bel_congo_transport_project_state` | Congo states with rail, river, port, infrastructure, or supply targets | Transport corridor mission targets. |
| `is_bel_colonial_emergency_pool_state` | Other Belgian-controlled colonial territory if any exists | Secondary pool. |
| `is_bel_core_fallback_pool_state` | Belgian cores | Should not be used for Congo package. Only generic system can use core fallback under separate rules. |

If Belgium is occupied in Europe but still controls Congo or operates as an exile government, the Congo system can remain available. If Congo is released, independent, or no longer subject to Belgium, expansion decisions must hide and reform or accountability decisions should remain if Belgium is still responsible for existing evidence.

### Decision families

| Working decision id | Availability | Costs | Main visible effect | Consequence pressure |
| --- | --- | --- | --- | --- |
| `bel_expand_concession_labor_quotas` | Belgium controls Congo pool, war or resource pressure | Political power, command power, support equipment, manpower | Increases resource extraction and concession output | Congo population damage, unrest, evidence level |
| `bel_route_labor_to_rubber_and_minerals` | Active concession network, resource states exist | Trucks, trains, convoys, civilian-factory burden | Adds rubber, minerals, infrastructure, or production output where valid | Strong local burden and strike pressure |
| `bel_build_congo_transport_corridors` | Active network, transport project states | Trucks, trains, convoys, civilian-factory burden | Adds infrastructure, rail, supply, or port improvements | Population loss pressure, convoy burden, evidence depth |
| `bel_suppress_colonial_strikes` | Strike or unrest pressure | Command power, infantry equipment, support equipment | Restores short-term output | Higher unrest, autonomy pressure, and discovery severity |
| `bel_open_international_inspection` | Democratic route, discovery risk, or foreign pressure | Political power, civilian-factory burden | Reduces future condemnation if followed | Temporarily lowers output and raises reform pressure |
| `bel_reform_concession_system` | Inspection active, postwar, or high accountability | Civilian-factory burden, political power, 365 day mission | Converts concession network to reformed administration | Ends extraction bonus and reduces unrest over time |
| `bel_recognize_local_administration` | Reform route or decolonization pressure | Political power, stability, autonomy concession | Reduces Congo burden and future revolt | Lowers Belgian resource output and direct control |

### Missions and timing

| Working mission id | Duration | Success requirements | Success result | Failure result |
| --- | ---: | --- | --- | --- |
| `bel_congo_resource_quota_cycle` | 120 days | Maintain control of selected resource states and transport capacity | Adds timed resource output and extraction pressure | Raises strike pressure and evidence without full output |
| `bel_congo_transport_corridor_project` | 210 days | Maintain convoy, truck, train, and civilian-factory burden | Adds infrastructure, rail, or supply improvements | Adds local unrest and transport burden |
| `bel_colonial_strike_response` | 150 days | Choose negotiation, reform, or suppression route | Negotiation lowers unrest but lowers output, suppression restores output but raises evidence | If ignored, output falls and discovery risk rises |
| `bel_concession_reform_mandate` | 365 days | Stop quota expansion, pay reform costs, keep Congo controlled or subject | Removes active network and creates reform credit | Keeps accountability pressure and may trigger decolonization crisis |

### AI weights

| AI condition | Expansion weight | Reform weight | Notes |
| --- | ---: | ---: | --- |
| Belgium controls Congo, peace, stable economy | 15 | 10 | Light background extraction only. |
| Belgium at war or in exile, resource shortage | 50 | 0 | Expands quotas and transport projects. |
| Democratic Belgium with foreign pressure | 10 | 55 | Starts inspection. |
| Discovery or high accountability pressure | 0 | 90 | Reform and local administration route. |
| Congo released or independent | 0 | 80 | Cleanup or accountability only. |
| Non-democratic high-chaos Belgium | 65 | 0 | Higher expansion, still capped by active quota count. |

AI caps:

- no Germany-style extermination route by default.
- no Belgian core fallback through Congo decisions.
- one resource quota cycle and one transport project at a time.
- strike suppression should not loop without rising cost and evidence.

### Idea lifecycle

| Idea id | Owner | Start or unlock | Role | Upgrade or removal |
| --- | --- | --- | --- | --- |
| `bel_congo_concession_labor_system` | Belgium | Dormant or first quota expansion | Gives resource route access and mild output | Upgrades to extraction pressure or reforms |
| `bel_congo_extraction_pressure` | Belgium | Active quota expansion | Strong resource and transport output with stability and evidence cost | Worsens with strikes or is removed by reform |
| `congo_concession_labor_burden` | Congo or local owner | Active network | Population damage, unrest, autonomy pressure | Reduced by inspection, reform, or local administration |
| `bel_colonial_resource_output` | Belgium | Successful quota or corridor mission | Timed resource and logistics output | Ends when network closes or Congo leaves control |
| `bel_postwar_accountability_pressure` | Belgium | Discovery, failed inspection, or decolonization crisis | Diplomatic, stability, and tribunal pressure | Removed by reform mandate and local administration |
| `bel_congo_reform_credit` | Belgium | Successful reform before severe discovery | Reduces postwar penalties | Timed or permanent memory |

### Focus hooks

Working focus hooks:

- `bel_focus_congo_resource_office`: reveals concession quota decisions.
- `bel_focus_exile_economy_congo`: increases wartime output if Belgium is occupied in Europe.
- `bel_focus_congo_transport_corridors`: unlocks transport projects.
- `bel_focus_colonial_inspection_mandate`: opens inspection before discovery.
- `bel_focus_reform_concession_system`: strengthens reform route.
- `bel_focus_local_administration_recognition`: unlocks autonomy or decolonization-friendly closure.

### Dismantlement route

Steps:

1. Open inspection or reform mandate.
2. Stop quota and strike suppression loops.
3. Complete concession reform mission.
4. Recognize local administration or convert concession control to ordinary colonial governance with reduced extraction.
5. Remove active site flags and local burden ideas.
6. Keep a reform credit or accountability memory depending on timing and discovery state.

### Discovery route

Discovery can happen through:

- enemy or rebel control of Congo concession states.
- international inspection if Belgium blocks reform.
- decolonization crisis while the network is active.
- postwar tribunal logic if accountability pressure is high.

Effects:

- Belgium receives condemnation or accountability pressure.
- Congo receives autonomy and unrest pressure.
- resource output drops sharply.
- reform and local administration decisions unlock.
- repeated minor leak popups stay removed.

### Asset ids

| Asset id | Type | Use |
| --- | --- | --- |
| `GFX_decision_bel_congo_concession_quota` | decision icon | quota expansion |
| `GFX_decision_bel_congo_transport_corridor` | decision icon | transport missions |
| `GFX_decision_bel_colonial_inspection` | decision icon | inspection route |
| `GFX_idea_bel_congo_extraction_pressure` | idea icon | Belgian output idea |
| `GFX_idea_congo_concession_labor_burden` | idea icon | Congo burden idea |
| `GFX_report_event_congo_labor_discovery` | report image | local discovery or inspection report |
| `GFX_news_event_congo_colonial_reckoning` | news image | severe international exposure |

## Generic camp-system users

The generic system should let any country access the mechanic under extreme political, war, occupation, or chaos conditions. It must stay less detailed than country packages and should not create a universal optimal atrocity economy.

### State-pool logic

| Working trigger | State pool | Use |
| --- | --- | --- |
| `is_generic_occupied_camp_pool_state` | Controlled occupied non-core states with resistance or war pressure | Main generic pool. |
| `is_generic_colonial_camp_pool_state` | Controlled colonial or subject-administered states | Secondary pool for empires. |
| `is_generic_noncore_security_pool_state` | Non-core controlled states with high resistance or compliance damage | Emergency security pool. |
| `is_generic_political_opposition_pool_state` | Country-specific political-opposition state markers set by focuses or crises | Used by scripted routes, not player selectors. |
| `is_generic_core_fallback_pool_state` | Core states | Last fallback with low output and high internal penalties. |

### Generic decision families

| Working decision id | Availability | Costs | Main visible effect | Consequence pressure |
| --- | --- | --- | --- | --- |
| `generic_activate_detention_network` | Authoritarian, extremist, chaos doctrine, occupied resistance, or severe crisis | Political power, support equipment, manpower | Activates base detention network in valid pool | Evidence, deaths pressure, stability damage |
| `generic_expand_labor_quotas` | Active network, valid pool | Infantry equipment, support equipment, trains, manpower | Increases labor output and coercive control | Larger population loss and overextension |
| `generic_redirect_labor_to_construction` | Active labor output, construction target | Civilian-factory burden, trucks, trains | Adds construction or repair output | Rail burden and resistance pressure |
| `generic_redirect_labor_to_resource_extraction` | Resource state target | Support equipment, trucks, trains | Adds resource extraction pressure | Stronger local burden and evidence depth |
| `generic_allocate_additional_guards` | Overextension or unrest | Manpower, infantry equipment, command power | Reduces immediate breakdown | Higher guard burden and deaths pressure |
| `generic_reduce_labor_quotas` | Active network with quota or overextension pressure | Political power and reduced output | Lowers labor pressure and recurring harm while the order remains active | Reduced coercive output and persistent evidence |
| `generic_upgrade_existing_site_to_radicalized_atrocity_site` | Existing concentration camp, extreme ideology or chaos doctrine, major war or crisis | Political power, stability, guard and rail cost | Converts site to radicalized escalation route | Severe Deaths, evidence, resistance, and tribunal severity |
| `generic_restricted_contaminated_site_escalation` | Existing radicalized, gulag, or experiment site, relevant capability, strict route gate | Matching stockpile and logistics costs, stability, evidence risk | Applies an abstract chemical or biological severity tier through one Deaths path | Higher contamination or outbreak risk, evidence, resistance, instability, and tribunal severity |
| `generic_destroy_evidence_before_retreat` | Enemy near undiscovered active site | Command power, manpower, support equipment, stability | Reduces or changes evidence depth if successful | Adds deaths pressure, failed cover-up risk, and discovery severity if failure |
| `generic_dismantle_detention_network` | Reform route, regime change, discovery, or player choice | Civilian-factory burden, support equipment, long mission | Removes active sites and ends output | Short-term unrest, long-term reform credit |
| `camp_repression_close_dormant_legacy_site` | Controlled inherited dormant marker and an accepted reform route | Political power, support equipment, and local closure work | Removes the dormant marker without activating the site | Preserves responsibility and reform memory |

### Generic missions and timing

| Working mission id | Duration | Success requirements | Success result | Failure result |
| --- | ---: | --- | --- | --- |
| `generic_labor_project_cycle` | 120 to 180 days | Keep control, equipment, transport, and construction burden | Adds construction, repair, resource, or local works output | Adds population damage and evidence without full output |
| `generic_network_overstretch_crisis` | 150 days | Allocate guards, dismantle sites, or reduce quotas | Lowers overextension and resistance pressure | Triggers large-network breakdown and discovery risk |
| `generic_reform_and_dismantlement` | 270 to 540 days | Stop expansion and pay reform costs | Removes active network and lowers tribunal severity | Keeps reform pressure and increases unrest |
| `generic_retreat_evidence_crisis` | 30 to 60 days | Enemy proximity remains high, choose evidence action or evacuate | Handles discovery or cover-up branch | Severe discovery if ignored or failed |

### Generic AI weights

| AI condition | Activation weight | Radicalized escalation weight | Dismantlement weight | Notes |
| --- | ---: | ---: | ---: | --- |
| Democratic, no chaos doctrine | 0 | 0 | 30 | Dismantle inherited active sites if any. |
| Neutral or non-aligned, stable | 0 | 0 | 15 | Avoid. |
| Authoritarian, major war, occupied resistance | 25 | 0 | 0 | Limited detention network possible. |
| Fascist or communist extremist route, major war | 45 | 15 | 0 | Escalation possible only with route gates and caps. |
| Chaos doctrine atrocity branch | 55 | 25 | 0 | Still needs valid non-core or occupied pool. |
| Losing war with enemy near sites | 5 | 0 | 40 | Evidence destruction or dismantlement depending on ideology. |
| Regime change away from extremist route | 0 | 0 | 90 | Reform and cleanup dominate. |

AI caps:

- max active generic concentration network by country size and occupied pool size.
- max radicalized sites far below Germany-specific historical path.
- no radicalized escalation without route, ideology, war, and valid site.
- no protected-class target selection.
- no contaminated-site escalation unless a country already meets strict special-system gates.

### Generic idea lifecycle

| Idea id | Owner | Start or unlock | Role | Upgrade or removal |
| --- | --- | --- | --- | --- |
| `generic_detention_network_administration` | Responsible country | Activate network | Base forced-labor and control idea with penalties | Upgrades to expanded or overextended network |
| `generic_expanded_labor_network` | Responsible country | Expand quotas or labor projects | Stronger output with stronger costs | Worsens to overextended or dismantles |
| `generic_overextended_repression_network` | Responsible country | High reach or resistance pressure | Stability, rail, guard, and revolt burden | Reduced by guard allocation or dismantlement |
| `generic_radicalized_atrocity_policy` | Responsible country | Radicalized escalation | Extremist lock-in with severe Deaths and evidence | Removed only by regime change or costly dismantlement |
| `generic_reform_pressure` | Responsible country | Discovery, reform route, or overextension | Cleanup burden and legal pressure | Converted to reform credit after dismantlement |
| `generic_reformed_legacy` | Responsible country | Successful dismantlement | Lowers future tribunal severity and blocks easy reactivation | Can be permanent memory |

### Generic focus hooks

Generic hooks should be route flags, not a new universal focus tree.

Working hook flags:

- `unlocked_generic_detention_network`: lets an authoritarian or crisis route activate base network.
- `unlocked_generic_labor_quota_expansion`: permits labor-output decisions.
- `unlocked_generic_radicalized_atrocity_escalation`: permits upgrade only with valid existing site.
- `unlocked_generic_reform_and_dismantlement`: opens dismantlement even while ideology remains authoritarian.
- `unlocked_generic_evidence_destruction`: opens retreat evidence decisions for regimes that already have active sites.

Focus trees that use these hooks must also provide AI route weights, visible costs, and cleanup. A focus should not silently unlock the generic system with no decision category explanation.

### Generic dismantlement route

Steps:

1. Freeze new activation and expansion decisions.
2. Select active sites for closure, prioritizing core fallback sites, discovered sites, and overextended states.
3. Pay civilian-factory, support equipment, and manpower costs over a long mission.
4. Reduce local resistance spikes through compensation or regular security transition.
5. Unregister states from `global.genocide_active_camp_states` when inactive.
6. Convert national idea to `generic_reformed_legacy`.

### Generic discovery route

Discovery can happen through:

- state control change.
- capitulation and tribunal preparation.
- country-specific legal or reform review.
- high evidence and foreign visibility when a route explicitly exposes records.

Effects:

- responsible country receives condemnation and reform pressure.
- discoverer receives appropriate evidence event only for first or severe discovery.
- state owner receives population-loss history in Deaths tab.
- the system avoids repeated minor flavor popups.
- reform, tribunal, evidence, and propaganda decisions unlock where appropriate.

### Generic asset ids

| Asset id | Type | Use |
| --- | --- | --- |
| `GFX_decision_generic_expand_labor_network` | decision icon | expansion decisions |
| `GFX_decision_generic_dismantle_network` | decision icon | dismantlement decisions |
| `GFX_decision_generic_destroy_evidence` | decision icon | retreat evidence route |
| `GFX_decision_generic_guard_allocation` | decision icon | guard decisions |
| `GFX_idea_generic_detention_network` | idea icon | active network idea |
| `GFX_idea_generic_overextended_repression_network` | idea icon | overextension idea |
| `GFX_report_event_generic_camp_discovery` | report image | discovery report |
| `GFX_news_event_global_atrocity_evidence` | news image | first severe radicalized discovery |
