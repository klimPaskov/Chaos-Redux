# System Camp Repression Rework Spec, Part 5: Detailed Country Decision Kits and Focus Hooks

Working feature id: `system_camp_repression_rework`

All names in this file are working labels and implementation ids, not final localisation. Final event, focus, decision, GUI, achievement, and super-event prose must be written later through the normal localisation pass. Keep localisation direction-only when using this file as source design.

This part turns the broad country packages from Part 2 into implementation-ready country kits. It covers the U.K. and Raj, U.S.A., France and Vichy, Italy and Libya, Belgium and Congo, and generic users. Germany, Japan, and the Soviet Union remain governed by Part 3 for their deepest country-specific logic.

## Shared country-kit contract

Each country kit should use the same underlying helper families so the system stays maintainable.

### State-pool order

Every country-specific decision should ask a scripted trigger for its eligible pool instead of duplicating raw state lists inside decisions.

Priority order:

1. Controlled occupied non-core states that match the country package.
2. Controlled colonial or subject-administered states tied to the country package.
3. Controlled non-core states tied to the country package.
4. Country-specific borderland, periphery, overseas, or strategic-security pools.
5. Core fallback only when no higher pool exists and when the route explicitly allows fallback.

No country kit should expose a protected-class selector. State pools may use sovereignty, occupation, colony, subject, frontier, overseas, strategic coastal, military-security, high-resistance, and political-opposition conditions.

### Common costs

Costs should scale through constants and helper effects.

Common cost components:

- political power for legal, cabinet, or administrative actions.
- command power for security command strain, never above the project command-power cap.
- infantry equipment and support equipment for guards and administration.
- trucks, trains, and convoys for transport, rail, and overseas burden.
- manpower for guards, administrators, and internal security.
- civilian-factory burden for construction, camp closure, inspections, redress, and compensation.
- stability, war support, legitimacy, autonomy, or colonial pressure for political damage.
- local resistance, compliance damage, and reform pressure in affected states.

Economic output should never be free. Stronger labor output must consume guard capacity, rail capacity, political legitimacy, and future evidence risk.

### Common mission durations

Use the following duration bands unless a country-specific section gives a better reason.

| Mission type | Duration band | Notes |
| --- | ---: | --- |
| Emergency activation or first inspection | 90 to 120 days | Short enough to feel like a wartime cabinet action. |
| Expansion or regional construction mission | 120 to 180 days | Use for rail, roads, forts, resource corridors, and local works. |
| Suppression or unrest response mission | 120 to 210 days | Give the player time to move units, keep supply, and meet state requirements. |
| Reform, dismantlement, redress, or compensation | 180 to 365 days | These should compete with war and reconstruction priorities. |
| Major colonial reckoning or postwar reform | 270 to 540 days | Use when the route is a full reversal of an inherited system. |

### Common idea lifecycle pattern

Every kit should use staged ideas rather than one new idea per decision.

Lifecycle stages:

1. Dormant legacy marker with no monthly death processing.
2. Active network idea after the player or AI expands the system.
3. Overextended network idea when reach, evidence, or unrest crosses threshold.
4. Discovery or reform pressure idea after exposure, regime change, legal review, or decolonization pressure.
5. Dismantled or reformed legacy idea when the country pays the long cleanup cost.

Ideas should be country-specific in naming and effects, but script should use shared modifiers where possible.

### Common discovery route

Discovery stays evidence-based. Battlefield discovery uses state-control change. Domestic legal exposure, colonial inspection, decolonization inquiries, and postwar tribunals can also expose evidence when a country-specific route makes that plausible.

Discovery output:

- apply condemnation to `genocide_responsible_country`.
- update Chaos Meter Condemnation and Deaths views.
- mark the discovered state.
- increase tribunal severity.
- add country-specific stability, subject autonomy, resistance, or legal pressure.
- unlock reform, compensation, inspection, or evidence-handling decisions.
- avoid recurring minor leak event spam.

## United Kingdom and British Raj package

The U.K. kit should model imperial emergency detention, Raj labor administration, dominion control, wartime manpower pressure, and postwar reform. It should be useful enough that a player can choose it during a dangerous world war, but it should create a real burden for India, the Raj, and British legitimacy.

### State-pool logic

Primary scripted state groups:

| Working trigger | State pool | Use |
| --- | --- | --- |
| `is_uk_raj_detention_pool_state` | British Raj controlled or subject-administered states | Main pool for detention and labor burden. |
| `is_uk_indian_ocean_security_pool_state` | Burma, Ceylon, Malaya, and other imperial Asian security states when controlled | Secondary wartime overseas pool. |
| `is_uk_colonial_emergency_pool_state` | Other controlled colonial states with unrest or strategic bases | Limited emergency expansion pool. |
| `is_uk_core_fallback_pool_state` | U.K. core states | Valid only if empire pools are unavailable and the country is in severe homeland crisis. |

Population loss and local burden should apply to the target state owner where appropriate, while Britain remains the responsible country for evidence, discovery, and reform obligations. If the Raj exists as a subject, it receives the local burden idea and autonomy pressure.

### Decision families

| Working decision id | Availability | Costs | Main visible effect | Consequence pressure |
| --- | --- | --- | --- | --- |
| `uk_survey_raj_emergency_detention` | At war, Raj or Indian security pool exists, system dormant | Political power, small civilian-factory burden | Reveals the Raj package and marks dormant sites for possible activation | Minor colonial legitimacy damage |
| `uk_activate_raj_emergency_detention` | Survey complete, war or rebellion pressure | Political power, support equipment, manpower, stability | Activates Raj emergency detention and adds modest dominion control pressure | Raj labor burden, autonomy resistance, evidence level |
| `uk_route_colonial_labor_to_military_construction` | Active Raj network, valid construction target | Trains, trucks, support equipment, civilian-factory burden | Adds temporary construction, infrastructure, fort, or supply work in selected colonial states | Population loss pressure, resistance pressure, rail burden |
| `uk_expand_raj_detention_districts` | Network active, high wartime pressure or India unrest | Infantry equipment, support equipment, command power, manpower | Increases network reach and short-term control | Larger stability damage and future discovery severity |
| `uk_demand_indian_manpower_levy` | Major war, Raj exists or India pool controlled | Political power, autonomy pressure, war support | Adds manpower or manpower-factor pressure to Britain or the Raj command pool | India receives stronger autonomy resistance and labor burden |
| `uk_tighten_dominion_security_coordination` | At war, dominions or Raj exist | Political power, convoys, command power | Improves subject obedience and imperial coordination for a timed period | Legitimacy damage and reform pressure |
| `uk_allocate_additional_colonial_guards` | Active network, unrest or overextension | Manpower, infantry equipment, support equipment | Lowers immediate breakdown and resistance pressure | Higher guard burden and monthly population loss pressure |
| `uk_release_political_prisoners_for_negotiations` | Reform pressure, India autonomy pressure, or postwar state | Political power, stability cost, temporary control loss | Reduces Raj labor burden and autonomy resistance | Lowers labor output and dominion control pressure |
| `uk_reform_colonial_labor_administration` | Democratic route, postwar, or high discovery risk | Civilian-factory burden, political power, 270 day mission | Starts dismantlement and inspection route | Reduces evidence risk over time, raises short-term unrest |
| `uk_dismantle_raj_detention_network` | Reform mission complete or regime change | Civilian-factory burden, support equipment, stability investment | Removes active sites and replaces burden ideas | Ends output and creates reform credit if completed before discovery |

### Missions and timing

| Working mission id | Duration | Success requirements | Success result | Failure result |
| --- | ---: | --- | --- | --- |
| `uk_hold_raj_security_line` | 150 days | Keep supplied divisions or garrison strength in selected Raj states | Reduces immediate unrest and breakdown | Increases India autonomy resistance and network overextension |
| `uk_complete_raj_military_works` | 180 days | Maintain train, support equipment, and construction capacity while the decision runs | Adds infrastructure, forts, airbase, or supply improvements in selected colonial states | Adds rail burden, local deaths pressure, and evidence depth without full output |
| `uk_postwar_raj_review` | 365 days | Be at peace or after major war pressure falls, keep reform authority above threshold | Converts active network into reformed legacy and lowers tribunal severity | Keeps reform pressure active and risks a colonial reckoning discovery route |
| `uk_negotiate_indian_release_terms` | 270 days | Avoid new expansion decisions, keep India autonomy pressure below threshold | Reduces Raj burden and gives Britain reform credit | Triggers stronger India autonomy pressure and possible unrest mission |

The player should not receive a wall of Raj missions. Use an active mission cap of one security mission and one reform or construction mission.

### AI weights

| AI condition | Expansion weight | Reform weight | Notes |
| --- | ---: | ---: | --- |
| Peace, stable empire | 0 | 20 | AI should leave dormant infrastructure quiet. |
| World war, Raj exists, low India pressure | 25 | 5 | Light activation only. |
| World war, high India unrest or Burma threat | 45 | 10 | Can use construction and security decisions. |
| Democratic U.K. after war | 0 | 80 | Reform and dismantlement should dominate. |
| Discovery, high condemnation, or decolonization pressure | 0 | 100 | Stop expansion, start cleanup. |
| Non-democratic high-chaos empire | 55 | 5 | Still capped by train, manpower, and active-site limits. |

AI caps:

- no more than a small Raj active network before 1939.
- no extermination-style escalation by normal U.K. AI.
- no core fallback unless the U.K. has lost overseas pools and is in severe homeland emergency.
- one active labor-construction mission at a time.

### Idea lifecycle

| Idea id | Owner | Start or unlock | Role | Upgrade or removal |
| --- | --- | --- | --- | --- |
| `uk_imperial_detention_legacy` | U.K. | Dormant marker when valid Raj or colonial pool exists | Keeps the package discoverable to focus and decision hooks | Replaced by active administration or reform legacy |
| `uk_imperial_detention_administration` | U.K. | Activation decision | Gives modest dominion control, security, and construction routing access | Upgrades to overextended administration or dismantled legacy |
| `uk_overextended_imperial_detention` | U.K. | High reach or unrest | Adds stability, train, manpower, and reform pressure | Removed by dismantlement or worsened by discovery |
| `raj_colonial_labor_burden` | Raj or India local owner | Active Raj expansion | Local population damage, autonomy pressure, compliance and resistance effects | Reduced by release, reform, or dismantlement |
| `uk_imperial_reform_credit` | U.K. | Successful dismantlement before severe discovery | Improves decolonization legitimacy and reduces tribunal severity | Timed or permanent small reform memory |
| `uk_colonial_reckoning_pressure` | U.K. | Discovery or failed postwar review | Legal, diplomatic, and subject-autonomy pressure | Removed by compensation and reform route |

### Focus hooks

Working focus hooks, not final focus names:

- `uk_focus_imperial_security_board`: reveals survey and security coordination decisions.
- `uk_focus_wartime_raj_logistics`: improves construction routing but raises Raj labor-burden sensitivity.
- `uk_focus_indian_manpower_question`: unlocks manpower levy and negotiation alternative.
- `uk_focus_dominion_coordination`: makes dominion security coordination stronger while increasing postwar scrutiny.
- `uk_focus_colonial_reform_committee`: unlocks reform and postwar review before discovery.
- `uk_focus_indian_self_government_settlement`: enables dismantlement with lower unrest if Britain has stopped expansion.

These hooks can be added to existing U.K. or British Empire focus files if present. If the live repository lacks a custom U.K. focus route, implement as decision-category route flags that future focuses can set.

### Dismantlement route

Dismantlement should be hard, visible, and useful.

Required steps:

1. Stop new expansion decisions.
2. Run inspection or review mission.
3. Release or reclassify detainees through a timed decision.
4. Pay compensation or administrative conversion cost.
5. Remove active site flags, unregister active camp states, and keep a dormant legacy marker only.
6. Replace U.K. and Raj ideas with reform-credit or postwar legacy ideas.

Failure during dismantlement should not restart the old network automatically. It should leave overextension, unrest, and discovery risk until the player finishes cleanup or accepts a harsher colonial security route.

### Discovery route

Discovery can happen through:

- enemy control of a colonial site.
- India autonomy crisis crossing a high threshold.
- postwar international review if Britain refuses reform.
- decolonization event chains if the Raj or India breaks away while the network is active.

Discovery effects:

- Britain receives condemnation and colonial reckoning pressure.
- Raj or India receives autonomy pressure and local unrest relief if the network is dismantled.
- democratic allies may receive war-support or political-pressure reactions if Britain remains democratic.
- the system unlocks compensation and public inquiry decisions rather than repeated leak popups.

### Asset ids

| Asset id | Type | Use |
| --- | --- | --- |
| `GFX_decision_uk_raj_detention` | decision icon | Raj activation and expansion family |
| `GFX_decision_uk_colonial_labor_works` | decision icon | construction routing family |
| `GFX_idea_uk_imperial_detention_administration` | idea icon | U.K. active network idea |
| `GFX_idea_raj_colonial_labor_burden` | idea icon | Raj or India burden idea |
| `GFX_report_event_raj_detention_discovery` | report image | first Raj network discovery |
| `GFX_news_event_colonial_reckoning` | news image | severe postwar or decolonization exposure |

## United States package

The U.S. kit should model wartime emergency relocation and security labor as a democratic emergency authority with legal and legitimacy pressure. It should not become an economy optimization route.

### State-pool logic

Primary scripted state groups:

| Working trigger | State pool | Use |
| --- | --- | --- |
| `is_usa_wartime_security_zone_state` | West Coast, Pacific strategic, Alaska, Hawaii, canal, or other military-security zones when owned or controlled | Main emergency relocation pool. |
| `is_usa_overseas_security_pool_state` | U.S. controlled overseas territories or occupied enemy territory | Secondary wartime security pool. |
| `is_usa_interior_relocation_site_state` | Interior states with low combat risk and available infrastructure | Site placement pool for relocation authority. |
| `is_usa_core_emergency_fallback_state` | U.S. cores outside the above pools | Only valid during homeland invasion or extreme high-chaos emergency. |

The pool is geographic and military-security based. It must not ask the player to select an ethnicity, religion, nationality, or protected group.

### Decision families

| Working decision id | Availability | Costs | Main visible effect | Consequence pressure |
| --- | --- | --- | --- | --- |
| `usa_authorize_emergency_relocation_zones` | War, homeland threat, Pacific war pressure, sabotage fear, or high chaos | Political power, stability, war support | Activates wartime security authority and limited counter-espionage pressure | Civil liberties damage, court challenge, relocation disruption |
| `usa_expand_interior_security_camps` | Authority active, interior site pool exists | Support equipment, trucks, manpower, civilian-factory burden | Adds controlled site capacity and small security effect | Population disruption and evidence level |
| `usa_assign_detainee_labor_to_local_works` | Active sites, construction need | Civilian-factory burden, support equipment, stability | Minor infrastructure or repair output in selected states | Stronger democratic legitimacy damage for limited output |
| `usa_strengthen_wartime_review_boards` | Authority active | Political power, administrative cost | Reduces breakdown and court pressure for a time | Keeps system active and delays reform pressure |
| `usa_allow_court_review` | Court pressure or democratic legitimacy damage above threshold | Political power, stability, 180 day mission | Opens judicial review and reduces future condemnation if followed | Can block further expansion or force termination |
| `usa_release_detainees_under_supervision` | Authority active, threat falling or court review active | Support equipment, political power | Reduces relocation disruption and site reach | Reduces security effect and can raise short-term war-support debate |
| `usa_terminate_relocation_authority` | Threat below threshold, court route, postwar, or reform pressure | Civilian-factory burden, political power, 270 day mission | Closes sites and unregisters active states | Ends security benefits and starts redress pressure |
| `usa_establish_redress_commission` | Termination complete or discovery route | Civilian-factory burden, political power, long mission | Converts damage into reform credit and lowers tribunal or condemnation memory | Costs stability and budget capacity during completion |

### Missions and timing

| Working mission id | Duration | Success requirements | Success result | Failure result |
| --- | ---: | --- | --- | --- |
| `usa_court_review_period` | 180 days | No new expansion, maintain democratic stability above threshold | Enables termination with lower unrest and redress cost | Forces a political crisis idea and higher civil-liberties damage |
| `usa_security_authority_sunset` | 270 days | War threat falls and authority is not expanded | Auto-reveals termination decision, lowers AI expansion weight | If ignored, increases court challenge and democratic legitimacy damage |
| `usa_redress_commission_work` | 365 days | Pay civilian-factory burden and avoid reactivation | Removes redress pressure and grants reform-credit memory | Keeps civil-liberties damage and may trigger domestic exposure event |

### AI weights

| AI condition | Activation weight | Expansion weight | Reform weight | Notes |
| --- | ---: | ---: | ---: | --- |
| Peacetime, no high chaos | 0 | 0 | 0 | Category hidden. |
| War without homeland or Pacific pressure | 5 | 0 | 10 | AI usually avoids activation. |
| Pacific war pressure or homeland raids | 25 | 10 | 5 | Limited activation possible. |
| Homeland invasion or extreme high chaos | 40 | 20 | 5 | Still capped by legitimacy and court pressure. |
| Court review active | 0 | 0 | 65 | AI should move toward termination. |
| Postwar or threat below threshold | 0 | 0 | 100 | Reform and redress dominate. |

AI caps:

- no radicalized atrocity escalation for democratic U.S. AI.
- no economy-focused expansion loop.
- no core fallback unless homeland invasion or high-chaos emergency.
- terminate after threat falls or legal pressure rises.

### Idea lifecycle

| Idea id | Owner | Start or unlock | Role | Upgrade or removal |
| --- | --- | --- | --- | --- |
| `usa_wartime_security_authority` | U.S. | Emergency authorization | Counter-espionage and security pressure with legitimacy damage | Upgrades to contested authority or terminates |
| `usa_contested_relocation_authority` | U.S. | Court challenge or overextension | Strong democratic legitimacy damage and political debate | Removed by court review and termination |
| `usa_civil_liberties_damage` | U.S. | Any sustained expansion | Stability, democratic support, reform pressure | Converted to redress pressure or reform credit |
| `usa_relocation_population_disruption` | State or U.S. | Interior site expansion | State population disruption and compliance damage | Removed by release and termination |
| `usa_redress_pressure` | U.S. | Termination or exposure | Postwar political and budget burden | Removed by redress commission mission |
| `usa_reform_credit` | U.S. | Successful termination and redress | Modest democratic resilience and reduced tribunal severity | Permanent or long timed memory |

### Focus hooks

Working focus hooks:

- `usa_focus_wartime_security_authority`: reveals authorization under war pressure.
- `usa_focus_home_front_security_review`: lowers activation cost but increases court pressure if expanded.
- `usa_focus_supreme_court_review`: unlocks the court review route early.
- `usa_focus_civil_liberties_restoration`: unlocks termination and redress even during war if threat is low.
- `usa_focus_redress_commission`: improves final cleanup and reform-credit outcome.

If no U.S. custom tree is present, these should be implemented as focus-hook flags for future compatibility and decision gates for the base package.

### Dismantlement route

Dismantlement steps:

1. Stop expansion decisions.
2. Run court review or sunset mission.
3. Release detainees under supervision or immediate termination depending on threat.
4. Unregister active sites and remove state disruption modifiers.
5. Start redress commission.
6. Convert civil-liberties damage into reform credit after completion.

The U.S. route should make early dismantlement cheaper than late forced redress. It should never reward the player for maximizing population loss.

### Discovery route

U.S. exposure is mainly legal, domestic, and postwar unless enemy forces capture a relevant site. Discovery can happen through:

- court review failure.
- postwar legal inquiry.
- enemy control of an overseas or occupied security site.
- high chaos domestic unrest if authority remains active after threat falls.

Effects:

- civil-liberties and democratic legitimacy ideas intensify.
- reform and redress decisions unlock.
- foreign condemnation remains lower than battlefield atrocity discovery unless overseas occupied sites are involved.
- internal stability and democratic-support penalties are large.

### Asset ids

| Asset id | Type | Use |
| --- | --- | --- |
| `GFX_decision_usa_emergency_relocation` | decision icon | authority activation |
| `GFX_decision_usa_court_review` | decision icon | legal review route |
| `GFX_decision_usa_redress_commission` | decision icon | redress route |
| `GFX_idea_usa_wartime_security_authority` | idea icon | active authority idea |
| `GFX_idea_usa_civil_liberties_damage` | idea icon | legitimacy damage idea |
| `GFX_report_event_usa_relocation_review` | report image | court or postwar exposure report |

## France, Vichy, and North Africa package

France should split by regime. Democratic France and Free France receive inheritance, inspection, reform, and refugee-aid routes. Vichy or authoritarian France can expand camp legacy and North African labor systems. The package should avoid turning ordinary democratic France into an expansion economy.

### State-pool logic

| Working trigger | State pool | Use |
| --- | --- | --- |
| `is_france_camp_legacy_state` | Mainland states with dormant detention legacy markers, including the Gurs working region if represented | Dormant inheritance and inspection route. |
| `is_vichy_collaboration_pool_state` | Vichy-controlled mainland or collaboration-administered states | Collaboration and internment administration route. |
| `is_france_north_africa_labor_pool_state` | Algeria, Morocco, Tunisia, Sahara, and other French North African controlled states | Colonial labor and desert works route. |
| `is_france_colonial_labor_pool_state` | Other controlled French colonial territories | Secondary colonial route. |
| `is_france_core_fallback_pool_state` | French cores | Only authoritarian or collaboration route, only when legacy pool exists or high crisis applies. |

When Vichy operates under German influence, responsibility must remain clear. Vichy is responsible for Vichy-created sites. Germany can gain linked evidence or collaborator-benefit variables only through explicit decisions that store responsibility correctly.

### Decision families

| Working decision id | Regime | Costs | Main visible effect | Consequence pressure |
| --- | --- | --- | --- | --- |
| `fr_inspect_camp_legacy` | Democratic or Free France | Political power, civilian-factory burden | Reveals dormant legacy markers and starts reform route | Temporary stability and refugee pressure |
| `fr_close_camp_legacy_sites` | Democratic or Free France | Civilian-factory burden, support equipment, 270 day mission | Removes dormant or active legacy sites | Reform credit and lower tribunal severity |
| `fr_expand_vichy_internment_administration` | Vichy or authoritarian | Political power, infantry equipment, support equipment | Activates mainland collaboration pool | Evidence, resistance, tribunal severity |
| `fr_route_north_africa_labor_to_rail_projects` | Vichy or authoritarian, North Africa pool | Trucks, trains, convoys, civilian-factory burden | Adds rail, infrastructure, fort, or supply work in North Africa | Population damage and local unrest |
| `fr_collaboration_transfer_records` | Vichy or collaboration route | Political power, stability, evidence risk | Increases German-aligned collaboration pressure if Germany exists and is eligible | Higher discovery severity for both linked routes where scripted |
| `fr_suppress_refugee_and_rescue_networks` | Vichy or authoritarian, active network | Command power, manpower, support equipment | Lowers short-term visibility and resistance | Higher evidence depth and refugee pressure later |
| `fr_open_colonial_labor_review` | Democratic, Free France, regime change, or discovery | Political power, civilian-factory burden | Starts reform route for North Africa and colonial sites | Short-term unrest and lower output |
| `fr_dismantle_north_africa_labor_network` | Review complete | Civilian-factory burden, convoys, support equipment | Removes active colonial network | Reform credit, lower decolonization pressure |

### Missions and timing

| Working mission id | Duration | Success requirements | Success result | Failure result |
| --- | ---: | --- | --- | --- |
| `fr_gurs_legacy_review` | 180 days | Do not activate new Vichy expansion, maintain reform route | Converts dormant legacy to inspected legacy | Legacy becomes evidence risk if enemy captures state later |
| `fr_north_africa_rail_labor_project` | 180 days | Maintain convoy or train capacity and control selected states | Adds infrastructure or rail output | Adds deaths pressure and resistance without full output |
| `fr_refugee_pressure_response` | 150 days | Use reform or aid decisions, avoid suppression | Lowers refugee pressure | Increases resistance and foreign visibility |
| `fr_post_liberation_reckoning` | 365 days | Free France or democratic France controls legacy states and pays reform cost | Removes collaboration burden and lowers tribunal severity | Keeps Vichy legacy idea and discovery risk |

### AI weights

| AI condition | Expansion weight | Reform weight | Notes |
| --- | ---: | ---: | --- |
| Democratic France before collapse | 0 | 30 | Inspect dormant legacy, no expansion. |
| Free France controls legacy or colonial states | 0 | 70 | Reform and refugee aid. |
| Vichy, German alignment, at war | 45 | 5 | Uses collaboration and North Africa labor lightly. |
| Vichy, high resistance or German pressure | 60 | 0 | Can expand but capped by stability and foreign visibility. |
| Regime changed away from Vichy | 0 | 90 | Dismantle and post-liberation reckoning. |
| High condemnation or enemy near sites | 0 | 60 | Reform if possible, evidence destruction only for authoritarian collapse route. |

AI caps:

- democratic France never expands active labor camps.
- Vichy can activate and expand but should not become Germany-scale.
- no extermination-style escalation unless an extreme chaos doctrine route explicitly unlocks generic radicalized escalation.
- Free France prioritizes reform.

### Idea lifecycle

| Idea id | Owner | Start or unlock | Role | Upgrade or removal |
| --- | --- | --- | --- | --- |
| `fr_camp_legacy` | France or Vichy | Dormant inheritance | Marks legacy for inspection, Vichy use, or reform | Replaced by Vichy collaboration reach or reform credit |
| `vichy_collaboration_repression` | Vichy or authoritarian France | Vichy expansion | Grants control and collaboration leverage with heavy legitimacy cost | Upgrades to overextended collaboration or removed after liberation |
| `fr_north_africa_labor_burden` | France or local state owner | North Africa labor projects | Colonial construction output with local population and unrest damage | Removed by colonial labor review and dismantlement |
| `fr_refugee_pressure` | France, Vichy, or Free France | Suppression, discovery, or failed review | Stability and diplomatic pressure | Reduced by aid or reform route |
| `free_france_reform_credit` | Free or democratic France | Successful inspection and closure | Legitimacy and tribunal relief | Permanent or timed memory |
| `fr_post_liberation_reckoning` | France | Discovery or liberation of active sites | Legal and political cleanup burden | Removed by post-liberation mission |

### Focus hooks

Working focus hooks:

- `fr_focus_legacy_review_commission`: reveals inspection and closure.
- `fr_focus_refugee_aid_networks`: reduces refugee pressure and blocks suppression decisions.
- `vichy_focus_national_revolution_security`: reveals Vichy collaboration expansion.
- `vichy_focus_north_africa_labor_projects`: unlocks North Africa rail and labor missions.
- `vichy_focus_collaboration_records`: increases German-linked collaboration pressure and evidence risk.
- `free_france_focus_republican_reckoning`: strengthens post-liberation reform and removes Vichy burdens.

### Dismantlement route

Democratic or Free France should be able to dismantle without first activating death-producing sites.

Dismantlement steps:

1. Inspect legacy sites.
2. Close or convert dormant sites.
3. Open refugee and survivor aid route if discovery has happened.
4. Dismantle North Africa labor networks where active.
5. Replace Vichy or colonial burden ideas with reform credit.
6. Clear active-state registration and keep historical memory only in docs or event details.

### Discovery route

Discovery can happen through:

- Allied or enemy liberation of Vichy mainland sites.
- Allied capture of North Africa labor sites.
- Free France post-liberation review.
- postwar tribunal threshold if Vichy collapses with high evidence.

Effects:

- apply condemnation to the responsible regime.
- increase Vichy tribunal severity.
- give Free or democratic France reform decisions if it controls the sites.
- create refugee and political pressure rather than recurring leak popups.

### Asset ids

| Asset id | Type | Use |
| --- | --- | --- |
| `GFX_decision_fr_camp_legacy_review` | decision icon | inspection route |
| `GFX_decision_vichy_internment_admin` | decision icon | Vichy expansion |
| `GFX_decision_fr_north_africa_labor` | decision icon | colonial works route |
| `GFX_idea_fr_camp_legacy` | idea icon | dormant legacy or inheritance |
| `GFX_idea_vichy_collaboration_repression` | idea icon | active Vichy route |
| `GFX_report_event_fr_liberated_camp_records` | report image | discovery or liberation report |
| `GFX_news_event_vichy_reckoning` | news image | severe discovery or postwar reckoning |

## Italy and Libya package

Italy should focus on colonial repression, desert logistics, forced settlement, roads, forts, and colonial security battalions. The kit should be stronger in Libya and East Africa than in Europe, but it should create severe local resistance and long-term colonial claim damage.

### State-pool logic

| Working trigger | State pool | Use |
| --- | --- | --- |
| `is_italy_libya_repression_pool_state` | Italian-controlled Libya and Cyrenaica working regions | Main colonial repression pool. |
| `is_italy_east_africa_repression_pool_state` | Italian East Africa when controlled | Secondary colonial pool. |
| `is_italy_balkan_occupation_pool_state` | Occupied Balkans or other non-core occupied territories after war escalation | Wartime occupation extension. |
| `is_italy_colonial_logistics_project_state` | Colonial states with ports, supply routes, roads, or fort targets | Labor-output target pool. |
| `is_italy_core_fallback_pool_state` | Italian cores | Desperate fallback only, with poor output and heavy stability damage. |

State output should favor roads, forts, ports, infrastructure, and supply. Resource or factory output should be secondary unless the state has a clear existing resource or industrial target.

### Decision families

| Working decision id | Availability | Costs | Main visible effect | Consequence pressure |
| --- | --- | --- | --- | --- |
| `ita_reopen_desert_camp_administration` | Fascist or authoritarian Italy, controls Libya or East Africa | Political power, infantry equipment, support equipment | Activates colonial camp administration | Libyan resistance, population damage, evidence level |
| `ita_redirect_colonial_labor_to_roads_and_forts` | Active colonial network, logistics target | Trucks, trains, convoys, civilian-factory burden | Builds or repairs infrastructure, forts, ports, or supply links | Desert camp burden, local unrest, rail and convoy burden |
| `ita_force_settlement_of_rebel_districts` | High resistance or insurgency pressure | Command power, manpower, infantry equipment, stability | Reduces short-term local resistance and increases colonial control | High population loss pressure and future revolt severity |
| `ita_raise_colonial_security_battalions` | Active network and local unrest | Infantry equipment, support equipment, manpower | Spawns or strengthens local security units or garrison modifier | Increases colonial resentment and equipment strain |
| `ita_expand_desert_transport_guard` | Network overextended | Trucks, fuel, command power | Reduces breakdown and convoy loss risk | Raises fuel and manpower burden |
| `ita_close_desert_camps` | Regime change, reform focus, high discovery risk, or colonial defeat | Political power, civilian-factory burden, 270 day mission | Dismantles active colonial network | Loses short-term control and construction output |
| `ita_compensate_local_communities` | Closure started or discovery route | Civilian-factory burden, stability investment | Reduces postwar colonial claim damage | Costs reconstruction capacity and political pressure |

### Missions and timing

| Working mission id | Duration | Success requirements | Success result | Failure result |
| --- | ---: | --- | --- | --- |
| `ita_desert_road_labor_project` | 180 days | Control selected colonial states, maintain trucks, convoys, and supply | Adds infrastructure or supply improvements | Adds local deaths pressure and resistance without full output |
| `ita_colonial_security_sweep` | 150 days | Place supplied divisions or garrison strength in selected colonial states | Temporarily lowers resistance and network breakdown | Raises long-term resistance pressure and evidence depth |
| `ita_desert_camp_closure` | 270 days | Stop expansion, control the active sites, pay reform costs | Removes active sites and lowers discovery severity | Creates revolt pressure and keeps overextended burden idea |
| `ita_postwar_colonial_compensation` | 365 days | At peace or after regime change, no new colonial repression decisions | Reduces colonial claim damage and local unrest | Keeps postwar colonial claim damage and foreign pressure |

### AI weights

| AI condition | Expansion weight | Reform weight | Notes |
| --- | ---: | ---: | --- |
| Fascist Italy controls Libya, peace or low war pressure | 20 | 0 | Light colonial administration only. |
| Fascist Italy at war, high Libya or East Africa resistance | 55 | 0 | Uses roads, forts, and security battalions. |
| Italy losing North Africa | 25 | 10 | Can destroy evidence or close sites depending on route. |
| Regime change away from fascism | 0 | 85 | Close and compensate. |
| Discovery or high condemnation | 0 | 70 | Reform unless authoritarian collapse route chooses evidence destruction. |
| No colonial states controlled | 0 | 0 | Category hides except cleanup. |

AI caps:

- no large European camp system from Italy unless generic extreme ideology route unlocks it.
- no core fallback unless colonial pools are gone and Italy is in severe crisis.
- keep colonial projects at a limited active count.
- evidence destruction only when enemies approach and evidence is undiscovered.

### Idea lifecycle

| Idea id | Owner | Start or unlock | Role | Upgrade or removal |
| --- | --- | --- | --- | --- |
| `ita_colonial_repression_legacy` | Italy | Dormant or first Libya route | Marks colonial security system | Replaced by active desert administration or reform legacy |
| `ita_desert_camp_administration` | Italy | Reopen decision | Gives colonial logistics and control with stability and manpower burden | Upgrades to overextended desert camps or closes |
| `ita_libyan_resistance_pressure` | Italy or local state owner | Forced settlement or security sweeps | Resistance, sabotage, and discovery pressure | Reduced by compensation and reform |
| `ita_colonial_logistics_output` | Italy | Road and fort labor route | Timed infrastructure and fortification output | Ends when network closes |
| `ita_postwar_colonial_claim_damage` | Italy | Discovery, defeat, or failed closure | Damages colonial legitimacy and diplomatic claims | Reduced by compensation mission |
| `ita_colonial_reform_credit` | Italy | Successful closure before severe discovery | Reduces postwar penalties | Timed or permanent memory |

### Focus hooks

Working focus hooks:

- `ita_focus_fourth_shore_security`: reveals Libya pool decisions and increases AI colonial-route weight.
- `ita_focus_libyan_road_works`: improves road and fort labor output while raising evidence risk.
- `ita_focus_colonial_security_corps`: unlocks colonial security battalions.
- `ita_focus_east_africa_emergency_labor`: opens East Africa pool if Italy controls it.
- `ita_focus_postwar_colonial_reform`: unlocks closure and compensation with lower unrest.
- `ita_focus_abandon_colonial_camps`: direct dismantlement opener for non-fascist or reform route.

### Dismantlement route

Dismantlement should be possible during war but expensive.

Steps:

1. Stop new forced settlement and labor projects.
2. Run desert camp closure mission.
3. Convert security battalions to ordinary garrison, disband them, or transfer them to normal colonial defense.
4. Pay compensation or local administration cost.
5. Remove active site flags and local burden modifiers.
6. Replace colonial claim damage with reform credit if completed before severe discovery.

### Discovery route

Discovery can happen through:

- Allied capture of Libya or East Africa camp states.
- local uprising control change.
- postwar colonial review.
- Italian capitulation with active network and high evidence.

Effects:

- Italy gains condemnation and postwar colonial claim damage.
- local states gain resistance and autonomy pressure.
- Allied countries can receive intervention or propaganda decisions if already at war.
- reform route opens if Italy changes regime.

### Asset ids

| Asset id | Type | Use |
| --- | --- | --- |
| `GFX_decision_ita_desert_camp_admin` | decision icon | activation and expansion |
| `GFX_decision_ita_colonial_road_labor` | decision icon | roads and forts mission |
| `GFX_decision_ita_camp_closure` | decision icon | closure route |
| `GFX_idea_ita_desert_camp_administration` | idea icon | active colonial network |
| `GFX_idea_ita_libyan_resistance_pressure` | idea icon | local resistance pressure |
| `GFX_report_event_libyan_camp_discovery` | report image | Allied discovery in Libya |

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
| `generic_upgrade_existing_site_to_radicalized_atrocity_site` | Existing concentration camp, extreme ideology or chaos doctrine, major war or crisis | Political power, stability, guard and rail cost | Converts site to radicalized escalation route | Severe Deaths, evidence, resistance, and tribunal severity |
| `generic_restricted_contaminated_site_escalation` | Existing radicalized, gulag, or experiment site, relevant capability, strict route gate | Existing stockpile and logistics costs, stability, evidence risk | Marks contaminated evidence and severe consequence branch | No efficiency curve, only higher evidence, accidents, spread risk, and tribunal severity |
| `generic_destroy_evidence_before_retreat` | Enemy near undiscovered active site | Command power, manpower, support equipment, stability | Reduces or changes evidence depth if successful | Adds deaths pressure, failed cover-up risk, and discovery severity if failure |
| `generic_dismantle_detention_network` | Reform route, regime change, discovery, or player choice | Civilian-factory burden, support equipment, long mission | Removes active sites and ends output | Short-term unrest, long-term reform credit |

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
