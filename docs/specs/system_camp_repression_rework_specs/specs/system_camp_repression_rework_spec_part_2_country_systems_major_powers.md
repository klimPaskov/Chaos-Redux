# System Camp Repression Rework Spec, Part 2: Country Systems and Major Powers

This part maps country packages. The working labels are not final localisation.

## Live implementation reconciliation

The live package implements the country systems through three decision files and one unified action bus:

- `common/decisions/camp_repression_major_country_decisions.txt` contains 29 verified Germany, Japan, and Soviet player actions.
- `common/decisions/camp_repression_colonial_country_decisions.txt` contains 43 verified U.K./Raj, U.S.A., France/Vichy, Italy, and Belgium player actions, including `fr_support_refugee_and_rescue_networks` and `bel_negotiate_colonial_strike_settlement`.
- `common/decisions/camp_repression_generic_decisions.txt` contains 12 verified generic player actions, including `generic_inspect_active_site`.
- `common/scripted_effects/camp_repression_action_dispatcher_effects.txt` routes every decision family through `camp_rework_route_country_specific_action`.

The final inventory is 84 player actions: 29 major, 43 colonial, and 12 generic. It excludes the separately verified 41 missions and the four Ledger show, hide, open, and close controls. The exact implemented IDs are recorded in `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md`.

France and Italy use the current consolidated pool helper names in `common/scripted_triggers/camp_repression_rework_triggers.txt`. Italy's package includes the homeland emergency action `ita_authorize_homeland_emergency_detention` and the transport-guard action `ita_expand_desert_transport_guard`. Subject-selected states use `camp_rework_action_state_id` rather than a world-state decision target.

Fixed country packages use explicit restricted-method gates. They do not inherit the generic fascist or communist route. The detailed design below remains controlling where it describes country identity and consequences. The live identifiers in this reconciliation control where an earlier working label differs.

## Germany: SS Camp Administration and Auschwitz Integration

Germany should remain the deepest country-specific package because the existing `germany_mengele` and `genocide_crisis` systems already share Auschwitz, Deaths, condemnation, and coup hooks.

### Starting posture

- Fascist Germany starts with dormant early camp infrastructure.
- Dormant sites do not enter monthly Deaths processing until Germany escalates.
- Active escalation becomes likely after war in Europe and occupation of Poland.
- Auschwitz remains the central shared node at state `88`.

### German values

- `racial_policy_radicalization`
- `ss_archive_control`
- `camp_network_reach`
- `occupied_deportation_pressure`
- `poland_transfer_pressure`
- `mengele_autonomy`
- `mengele_permission_level`
- `auschwitz_evidence_depth`
- `foreign_atrocity_awareness`
- `hardliner_pressure`

### Decision families

- Centralize SS Camp Administration.
- Expand Occupied Poland Camp Administration.
- Route Prisoner Labor to War Construction.
- Redirect Prisoner Labor to Eastern Fortifications.
- Tighten Deportation Logistics.
- Increase Guard Allocation.
- Restrict SS Autonomy.
- Military Review of Auschwitz.
- Close Auschwitz Program.
- Transfer Prisoners to Experiment Sites.
- Destroy Evidence During Retreat.
- Dismantle the Network after Regime Change.

### State pools

Germany should draw from occupied and non-core European states first. Occupied Poland is the preferred pool for Auschwitz-linked transfers. German cores are used only when Germany controls no valid occupied or non-core pool, and this fallback should sharply reduce benefits while increasing stability loss, war support loss, and internal backlash.

### Effects

Active camp networks provide forced-labor construction and occupation control. Extermination-site escalation is primarily negative but can increase hardliner pressure, racial radicalization, and Mengele autonomy if the Auschwitz program is active. Discovery should be catastrophic.

## Japan: Imperial Occupation Repression and Ishii Network

Japan should not copy Germany. Its system should focus on occupied China, Manchuria, colonial forced labor, reprisal policy, prisoner experimentation, Kwantung Army autonomy, Shiro Ishii, and biowarfare research risk.

### Starting posture

- Japan starts with dormant occupation repression and colonial security infrastructure.
- Manchuria and occupied China are the main future target pools.
- The route becomes active during war with China and when Japan controls Chinese or Manchurian states.
- Biowarfare integration requires Shiro Ishii influence, Unit 731-style research, or relevant special projects.

### Japanese values

- `imperial_occupation_reach`
- `kwantung_autonomy`
- `ishii_influence`
- `occupation_test_records`
- `bio_research_gain`
- `outbreak_accident_risk`
- `chinese_resistance_pressure`
- `occupation_evidence_depth`
- `tribunal_biowarfare_severity`

### Decision families

- Expand Forced Labor Camps in Occupied China.
- Intensify Occupation Reprisals.
- Transfer Prisoners to Experimental Facilities.
- Fund Pingfang Research Infrastructure.
- Shield Ishii from Army Review.
- Redirect Records to Army Medical Control.
- Suppress Chinese Resistance Cells.
- Destroy Experiment Evidence During Retreat.
- Open Epidemic Containment Office after Accident.
- Remove Ishii from Program Control.

### Japan-specific research branch

Working project labels:

- Pingfang Records Office.
- Kwantung Medical Intelligence.
- Occupation Test Ledger.
- Epidemic Mapping Bureau.
- Cherry Blossom Dossier.

These projects should unlock or alter existing Chaos Redux biowarfare mechanics, not create operational biological-attack recipes. Their gameplay is research speed, project availability, accident risk, evidence depth, outbreak risk, and tribunal severity.

### State pools

Japan uses controlled Chinese, Manchurian, and colonial states first. Home islands become valid only if Japan has no occupied pool and has entered desperate high-chaos or doomsday logic. Home-island fallback gives lower research benefits and much higher domestic stability and military obedience penalties.

## Soviet Union: Gulag, Paranoia, Famine, and Union Crisis Bridge

The Soviet Union should have a distinct system built around gulags, paranoia, forced labor, deportations, grain extraction, administrative purges, famine pressure, and Union Crisis interactions.

### Starting posture

- The Soviet Union starts with dormant gulag infrastructure.
- Remote Siberian, Far Eastern, northern, Kazakh, Central Asian, and industrial camp state groups should carry dormant flags or inactive modifiers.
- The system is quiet unless paranoia, purges, war pressure, borderland resistance, or player decisions expand it.

### Soviet values

- `gulag_network_reach`
- `nkvd_authority`
- `paranoia_pressure`
- `forced_labor_quota`
- `grain_extraction_burden`
- `famine_pressure`
- `republic_fear`
- `old_movement_grievance`
- `camp_administrator_corruption`
- `union_crisis_suppression_relief`
- `union_crisis_terminal_severity`

### Decision families

- Expand Remote Gulag Network.
- Transfer Prisoners to Industrial Camps.
- Intensify Forced Labor Quotas.
- Confiscate Grain from Disloyal Regions.
- Deport Suspected Opposition Networks.
- Purge Camp Administrators.
- Reinforce NKVD Authority.
- Reduce Paranoia Through Party Review.
- Release Prisoners for Military Service.
- Dismantle Overextended Camps.
- Destroy Records During Retreat.
- Emergency Famine Relief.
- Conceal Famine Mortality.
- Admit Local Administrative Collapse.

### Paranoia integration

High paranoia unlocks harsher decisions and increases AI willingness to use them. It also raises the chance of famine, deportation, and purge crises.

Low or managed paranoia keeps the system mostly background.

### Union Crisis integration

Repression can temporarily reduce organized opposition, Moscow Authority loss, or Military Obedience problems. That relief should stop at high crisis thresholds. The same actions should raise old movement grievance, republic fear, famine pressure, and foreign grievance. A player can use repression to buy time, but overuse should make a later collapse more bitter, violent, and harder to reverse.

### Extreme escalation

Soviet extreme escalation uses borderland, periphery, deportation, or political-opposition pools. It does not use ethnic protected-class target menus. It should be rare, ideology-locked, crisis-locked, and mostly negative.

## United Kingdom: Imperial Detention and Raj Labor Control

The U.K. package should emphasize imperial management, dominion control, Raj autonomy, wartime detention, and colonial labor extraction.

### Starting posture

- The British Raj can start with dormant emergency detention infrastructure.
- The system is low intensity and not a death-producing loop until the U.K. expands it.
- Expansion creates a U.K. national benefit and an India/Raj penalty.

### Values

- `imperial_detention_reach`
- `raj_labor_burden`
- `dominion_control_pressure`
- `indian_autonomy_resistance`
- `colonial_legitimacy_damage`
- `imperial_manpower_pressure`

### Decisions

- Expand Raj Emergency Detention.
- Route Colonial Labor to Military Construction.
- Tighten Dominion Security Coordination.
- Demand Indian Manpower Levy.
- Release Political Prisoners for Negotiations.
- Reform Colonial Labor Administration.
- Dismantle Raj Detention Network.

### Effects

The U.K. can gain construction speed, manpower pressure, and dominion-control leverage. India or the Raj receives an idea representing colonial labor burden, autonomy pressure, resistance, and population damage if expanded. If the U.K. democratizes reform routes or faces postwar pressure, the system should become a liability.

## United States: War Relocation and Emergency Security Labor

The U.S. package should be a democratic emergency system, not a forced-labor economy route.

### Starting posture

- The system is unavailable in peacetime.
- It becomes available under war, homeland threat, Pacific war pressure, high sabotage fear, or high chaos.
- It should be rare for AI and strongly penalized for democratic legitimacy.

### Values

- `wartime_security_reach`
- `civil_liberties_damage`
- `court_challenge_pressure`
- `democratic_legitimacy_damage`
- `relocation_population_disruption`
- `redress_pressure`

### Decisions

- Authorize Emergency Relocation Zones.
- Expand Interior Security Camps.
- Assign Detainee Labor to Local Works.
- Allow Court Review.
- Release Detainees Under Supervision.
- Terminate Relocation Authority.
- Establish Redress Commission.

### Effects

Short-term gains should be small: counter-espionage pressure, local security, or limited construction support. Penalties should be strong: stability loss, democratic support loss, court pressure, war-support division, population disruption, and postwar reckoning.

## France and Vichy: Gurs, North Africa, and Colonial Labor Camps

France should split by regime.

### Democratic or Free France

- can inherit dormant detention sites;
- can inspect, dismantle, or reform;
- can gain refugee-aid or anti-collaboration legitimacy;
- should not get an expansion incentive.

### Vichy or authoritarian France

- can expand Gurs and North African labor networks;
- can use Mer-Niger style railroad and desert labor pressure as historical anchors;
- gains limited construction or colonial extraction;
- raises resistance, evidence, and tribunal severity.

### Values

- `french_camp_legacy`
- `vichy_collaboration_reach`
- `north_africa_labor_burden`
- `refugee_pressure`
- `free_french_reform_credit`

## Italy: Libya and Colonial Repression

Italy's route should focus on colonial repression, logistics, and forced settlement.

### State pools

- Libya and East Africa if controlled.
- Balkans or occupied states only after war escalation.
- Italian cores only in desperate fallback.

### Values

- `colonial_repression_reach`
- `desert_camp_burden`
- `libyan_resistance_pressure`
- `colonial_logistics_output`
- `postwar_colonial_claim_damage`

### Decisions

- Reopen Desert Camp Administration.
- Authorize Homeland Emergency Detention.
- Redirect Colonial Labor to Roads and Forts.
- Force Settlement of Rebel Districts.
- Increase Colonial Security Battalions.
- Expand Desert Transport Guard.
- Close Desert Camps.
- Compensate Local Communities after Regime Change.

## Belgium: Congo Extraction and Forced Labor

Belgium should get a Congo-specific extraction system. It should not be a Germany-style extermination route by default.

### Values

- `congo_extraction_pressure`
- `concession_labor_burden`
- `colonial_resource_output`
- `congo_population_damage`
- `colonial_unrest_pressure`
- `postwar_accountability_pressure`

### Decisions

- Expand Concession Labor Quotas.
- Route Labor to Rubber and Mineral Extraction.
- Build Congo Transport Corridors.
- Suppress Colonial Strikes.
- Open International Inspection.
- Reform Concession System.
- Recognize Local Administration.

### Effects

Belgium gains resources, infrastructure pressure, or exile-economy leverage. Congo takes population loss, unrest, and autonomy pressure. Discovery or postwar decolonization should make the system politically explosive.

## Generic system

Every country can eventually access a generic camp system through ideology, occupation, war pressure, chaos doctrine, or extreme crisis. Generic content must stay shallow compared to country packages, but it should still be playable.

### Generic decisions

- Activate Detention Network.
- Expand Labor Quotas.
- Redirect Labor to Construction.
- Redirect Labor to Resource Extraction.
- Allocate Additional Guards.
- Reduce Labor Quotas.
- Upgrade Existing Site to Radicalized Atrocity Site.
- Escalate a Valid Site through the Restricted Contaminated Route.
- Destroy Evidence During Retreat.
- Dismantle Detention Network.
- Close a Dormant Legacy Site.

### Generic AI

Generic AI should be conservative. It should avoid expansion unless authoritarian, extremist, chaos-doctrine, in major war, occupying high-resistance states, or facing severe internal crisis. Democracies should almost never use it except for limited emergency internment routes, and should prefer reform or dismantling.
