# Fallout Ash-week office candidates

Disposition: implemented (static review; live delivery and AI choice frequencies are `needs_live_game`). Acceptance basis: round 2 lead item "Character or institution orientation step (events 78-81) and the first character arcs", taken under the user's grant of design authority and recorded as agent decision A16 in `agent_decisions_2026-10-04.md`. Titles come from the "Candidate character or institution class" column of the accepted coverage matrix `docs/specs/air_cleanliness_fallout_specs/matrices/fallout_orientation_region_archetype_coverage_matrix.md` and from the accepted pilot registry `matrices/fallout_orientation_pilot_memory_candidate_registry.md`.

Slot 1 is a relief or administration office (costs Medicine and Food), slot 2 a security or extraction office (Fuel and Scrap), slot 3 an institution (Power, Shelter capacity and Scrap). The role decides the national spirit the office installs and the arc that follows. Candidate ids: pilot candidates 1 to 36, cell candidates `100 + (region - 1) * 36 + (archetype - 1) * 3 + slot`. Source: `fallout_office_candidate_role` and the `fallout_office_candidate_<id>` localisation keys.

## Roles

| Role | Arc matrix role | Office idea | Civic institution | Command institution | Managed resource | Arc events |
| --- | --- | --- | --- | --- | --- | --- |
| `quartermaster` | Quartermaster | Quartermaster's Office (named after the candidate) | Public Ration Ministry | Army Commissariat | Food | 1060 to 1066 |
| `physician` | Doctor or medical board | Chief Medical Office (named after the candidate) | Public Health Board | Medical Command | Medicine | 1067 to 1073 |
| `engineer` | Grid engineer | Chief Engineer's Office (named after the candidate) | Public Works Authority | Works Directorate | Power | 1074 to 1080 |
| `commander` | Militia commander | Militia Command (named after the candidate) | Civil Defence Service | Militia High Command | Fuel | 1081 to 1087 |
| `ward_chair` | Local mayor or ward chair | Ward Council (named after the candidate) | Elected Ward Assembly | District Prefects | Shelter capacity | 1088 to 1094 |
| `magistrate` | Judge or tribunal chair | Emergency Court (named after the candidate) | Survivors' Courts | Emergency Tribunals | Recognition | 1095 to 1101 |

## Pilot memory candidates

| Id | Candidate | Role |
| ---: | --- | --- |
| 1 | Emergency Records Commissioner | Quartermaster |
| 2 | State Guard Supply Custodian | Militia commander |
| 3 | Emergency Congress Secretariat | Local mayor or ward chair |
| 4 | Tunnel Medical Mediator | Doctor or medical board |
| 5 | Redoubt Quartermaster | Quartermaster |
| 6 | Glacier Water Board | Grid engineer |
| 7 | Dead-City Permit Physician | Doctor or medical board |
| 8 | Factory Recovery Marshal | Militia commander |
| 9 | Rhine Salvage Court | Judge or tribunal chair |
| 10 | Grain Road Ration Clerk | Quartermaster |
| 11 | Steppe Host Quartermaster | Militia commander |
| 12 | Dnipro Barge Rada | Local mayor or ward chair |
| 13 | River Seed Clinician | Doctor or medical board |
| 14 | Ferry Militia Supply Captain | Militia commander |
| 15 | Mekong Seed Bank Council | Quartermaster |
| 16 | Raft Clinic Director | Doctor or medical board |
| 17 | Boat Militia Harbor Captain | Militia commander |
| 18 | Delta Grain Barge Council | Quartermaster |
| 19 | Field Hospital Registrar | Doctor or medical board |
| 20 | Medical Cordon Commissioner | Militia commander |
| 21 | Municipal Health Compact | Local mayor or ward chair |
| 22 | River Family Clinic Coordinator | Doctor or medical board |
| 23 | Basin Safe-Work Marshal | Militia commander |
| 24 | Altered River Assembly | Local mayor or ward chair |
| 25 | Mobile Well Medic | Doctor or medical board |
| 26 | Well Guardian Escort Captain | Militia commander |
| 27 | Caravan Court and Radio Market Council | Judge or tribunal chair |
| 28 | Highland Storehouse Relief Coordinator | Quartermaster |
| 29 | Mountain Road Protection Captain | Militia commander |
| 30 | Highland Sanctuary Council | Local mayor or ward chair |
| 31 | Desert Pump Engineer | Grid engineer |
| 32 | Mine and Port Supply Captain | Militia commander |
| 33 | Observatory Data Council | Grid engineer |
| 34 | Human Survival Records Officer | Judge or tribunal chair |
| 35 | Station Maintenance Chief | Grid engineer |
| 36 | Weather and Rescue Protocol Council | Local mayor or ward chair |

## Region and archetype cell candidates

| Region | Archetype | Slot 1 (id, role) | Slot 2 (id, role) | Slot 3 (id, role) |
| --- | --- | --- | --- | --- |
| North america | Continuity government | Chief County Clerk (101, Quartermaster) | Continuity Judge (102, Judge or tribunal chair) | Emergency Legislature (103, Local mayor or ward chair) |
| North america | Bunker authority | Surface Delegate (104, Local mayor or ward chair) | Chief Ventilation Engineer (105, Grid engineer) | Shelter Census Board (106, Quartermaster) |
| North america | Warlord command | Depot Quartermaster (107, Quartermaster) | Convoy Colonel (108, Militia commander) | Bridge Garrison Council (109, Local mayor or ward chair) |
| North america | Food compact | Elevator Steward (110, Quartermaster) | Cooperative Agronomist (111, Grid engineer) | Refugee Labor Delegation (112, Local mayor or ward chair) |
| North america | Maritime remnant | Lockmaster (113, Grid engineer) | Port Captain (114, Militia commander) | Refugee Flotilla Council (115, Local mayor or ward chair) |
| North america | Quarantine state | Field Epidemiologist (116, Doctor or medical board) | Permit Magistrate (117, Judge or tribunal chair) | Mobile Laboratory Service (118, Doctor or medical board) |
| North america | Scavenger syndicate | Salvage Assessor (119, Quartermaster) | Union Rigger (120, Grid engineer) | Public Archive Office (121, Judge or tribunal chair) |
| North america | Nomad convoy | Mechanic Elder (122, Grid engineer) | Route Marshal (123, Militia commander) | Mobile School Council (124, Local mayor or ward chair) |
| North america | Machine protocol | Human Exception Officer (125, Judge or tribunal chair) | Systems Custodian (126, Grid engineer) | Maintenance Collective (127, Local mayor or ward chair) |
| North america | Technate | Civil Engineer (128, Grid engineer) | Grid Dispatcher (129, Grid engineer) | Public Safety Review Board (130, Judge or tribunal chair) |
| North america | Mutant polity | Mixed-Family Physician (131, Doctor or medical board) | Altered-Community Advocate (132, Local mayor or ward chair) | Civic Recognition Court (133, Judge or tribunal chair) |
| North america | Religious refuge | Relief Chaplain (134, Doctor or medical board) | Lay Kitchen Organizer (135, Quartermaster) | Sanctuary Council (136, Local mayor or ward chair) |
| Europe | Continuity government | Parliamentary Clerk (137, Quartermaster) | Constitutional Jurist (138, Judge or tribunal chair) | Regional Delegation Council (139, Local mayor or ward chair) |
| Europe | Bunker authority | Shelter Ombudsman (140, Judge or tribunal chair) | Metro Engineer (141, Grid engineer) | Platform Ward Assembly (142, Local mayor or ward chair) |
| Europe | Warlord command | Military Quartermaster (143, Quartermaster) | Bridge Militia Captain (144, Militia commander) | Tunnel Commanders' Council (145, Local mayor or ward chair) |
| Europe | Food compact | River Market Steward (146, Quartermaster) | Cooperative Miller (147, Grid engineer) | Municipal Ration Delegation (148, Local mayor or ward chair) |
| Europe | Maritime remnant | Harbor Master (149, Quartermaster) | Convoy Commodore (150, Militia commander) | Dockworkers' Assembly (151, Local mayor or ward chair) |
| Europe | Quarantine state | Railway Medical Director (152, Doctor or medical board) | Border Health Magistrate (153, Judge or tribunal chair) | Laboratory Consortium (154, Doctor or medical board) |
| Europe | Scavenger syndicate | Industrial Assessor (155, Quartermaster) | Demolition Guild Foreman (156, Grid engineer) | Preservation Curators' Office (157, Judge or tribunal chair) |
| Europe | Nomad convoy | Route Cartographer (158, Quartermaster) | Convoy Mechanic (159, Grid engineer) | Migrant Household Assembly (160, Local mayor or ward chair) |
| Europe | Machine protocol | Human Liaison Engineer (161, Local mayor or ward chair) | Control-Room Custodian (162, Grid engineer) | Credential Review Panel (163, Judge or tribunal chair) |
| Europe | Technate | Grid Economist (164, Quartermaster) | Reactor Safety Chair (165, Grid engineer) | Elected Utility Auditors (166, Judge or tribunal chair) |
| Europe | Mutant polity | Recognition Advocate (167, Local mayor or ward chair) | Family-Law Mediator (168, Judge or tribunal chair) | Joint Clinic Council (169, Doctor or medical board) |
| Europe | Religious refuge | Relief Cleric (170, Doctor or medical board) | Lay Steward (171, Quartermaster) | Intercommunity Aid Council (172, Local mayor or ward chair) |
| Eurasian interior | Continuity government | Regional Legal Secretary (173, Judge or tribunal chair) | Rail Ministry Engineer (174, Grid engineer) | Republic Assembly (175, Local mayor or ward chair) |
| Eurasian interior | Bunker authority | Shelter Doctor (176, Doctor or medical board) | Mine Ventilation Chief (177, Grid engineer) | Surface Workers' Council (178, Local mayor or ward chair) |
| Eurasian interior | Warlord command | Depot Master (179, Quartermaster) | Rail Brigade Colonel (180, Militia commander) | Council of Route Commanders (181, Local mayor or ward chair) |
| Eurasian interior | Food compact | Seed Custodian (182, Quartermaster) | Grain-Train Coordinator (183, Grid engineer) | Livestock Corridor Delegation (184, Local mayor or ward chair) |
| Eurasian interior | Maritime remnant | Ice Pilot (185, Grid engineer) | River Flotilla Commander (186, Militia commander) | Naval Engineer Corps (187, Grid engineer) |
| Eurasian interior | Quarantine state | Sanitary Train Director (188, Doctor or medical board) | Steppe Medical Team Leader (189, Doctor or medical board) | Permit Court (190, Judge or tribunal chair) |
| Eurasian interior | Scavenger syndicate | Yard Appraiser (191, Quartermaster) | Mine Salvage Foreman (192, Grid engineer) | Transport-Share Exchange (193, Judge or tribunal chair) |
| Eurasian interior | Nomad convoy | Well Judge (194, Judge or tribunal chair) | Caravan Mechanic (195, Grid engineer) | Route-Memory Keepers (196, Local mayor or ward chair) |
| Eurasian interior | Machine protocol | Systems Interpreter (197, Local mayor or ward chair) | Relay Technician (198, Grid engineer) | Exception-Review Collective (199, Judge or tribunal chair) |
| Eurasian interior | Technate | Rail-Power Dispatcher (200, Quartermaster) | Thermal Engineer (201, Grid engineer) | Workers' Safety Commission (202, Local mayor or ward chair) |
| Eurasian interior | Mutant polity | Mixed Clinic Director (203, Doctor or medical board) | Altered Settlement Advocate (204, Local mayor or ward chair) | Family Registration Council (205, Judge or tribunal chair) |
| Eurasian interior | Religious refuge | Relief Leader (206, Quartermaster) | Lay Heating Steward (207, Grid engineer) | Interfaith Caravan Kitchen (208, Local mayor or ward chair) |
| East asia | Continuity government | Provincial Administrator (209, Quartermaster) | Legislative Secretary (210, Judge or tribunal chair) | Ward Federation (211, Local mayor or ward chair) |
| East asia | Bunker authority | Tunnel Ward Convener (212, Local mayor or ward chair) | Ventilation Engineer (213, Grid engineer) | Family Register Board (214, Judge or tribunal chair) |
| East asia | Warlord command | Arsenal Quartermaster (215, Quartermaster) | District Commander (216, Militia commander) | Floodgate Office (217, Grid engineer) |
| East asia | Food compact | Seed-Bank Agronomist (218, Quartermaster) | Irrigation Cooperative Chair (219, Grid engineer) | Urban Food Delegation (220, Local mayor or ward chair) |
| East asia | Maritime remnant | Fishing Fleet Organizer (221, Quartermaster) | Harbor Commander (222, Militia commander) | Island Rescue Council (223, Local mayor or ward chair) |
| East asia | Quarantine state | Port Health Director (224, Doctor or medical board) | Ward Epidemiology Team Leader (225, Doctor or medical board) | Certification Tribunal (226, Judge or tribunal chair) |
| East asia | Scavenger syndicate | Parts Exchange Registrar (227, Quartermaster) | Factory Salvage Engineer (228, Grid engineer) | Labor Safety Guild (229, Local mayor or ward chair) |
| East asia | Nomad convoy | Household Council Speaker (230, Local mayor or ward chair) | Convoy Route Planner (231, Militia commander) | Mobile Mechanic School (232, Grid engineer) |
| East asia | Machine protocol | Protocol Interpreter (233, Local mayor or ward chair) | Gate-Control Engineer (234, Grid engineer) | Human Records Commission (235, Judge or tribunal chair) |
| East asia | Technate | River Systems Engineer (236, Grid engineer) | Reactor Safety Chair (237, Grid engineer) | Public Load-Review Assembly (238, Local mayor or ward chair) |
| East asia | Mutant polity | Altered-Family Advocate (239, Local mayor or ward chair) | Civic Status Magistrate (240, Judge or tribunal chair) | Mixed Clinic Council (241, Doctor or medical board) |
| East asia | Religious refuge | Relief Cleric (242, Doctor or medical board) | Neighborhood Kitchen Coordinator (243, Quartermaster) | Lay Sanctuary Council (244, Local mayor or ward chair) |
| South asia | Continuity government | Refugee-City Mayor (245, Local mayor or ward chair) | Irrigation Administrator (246, Grid engineer) | Constitutional Secretariat (247, Judge or tribunal chair) |
| South asia | Bunker authority | Shelter Registrar (248, Quartermaster) | Water Engineer (249, Grid engineer) | Camp Liaison Council (250, Local mayor or ward chair) |
| South asia | Warlord command | Grain Quartermaster (251, Quartermaster) | Canal Garrison Commander (252, Militia commander) | Convoy Militia Council (253, Local mayor or ward chair) |
| South asia | Food compact | Refugee Labor Organizer (254, Local mayor or ward chair) | Seed Scientist (255, Grid engineer) | Canal Cooperative (256, Quartermaster) |
| South asia | Maritime remnant | Port Relief Captain (257, Quartermaster) | Coastal Convoy Commander (258, Militia commander) | Fishing Cooperative Council (259, Local mayor or ward chair) |
| South asia | Quarantine state | Camp Health Director (260, Doctor or medical board) | Water-Testing Corps Chief (261, Grid engineer) | Movement Appeals Tribunal (262, Judge or tribunal chair) |
| South asia | Scavenger syndicate | Public Stores Assessor (263, Quartermaster) | Ruin Surveyor (264, Grid engineer) | Electrical Salvage Guild (265, Local mayor or ward chair) |
| South asia | Nomad convoy | Tanker Coordinator (266, Quartermaster) | Route-Weather Reader (267, Grid engineer) | Mobile Household Parliament (268, Local mayor or ward chair) |
| South asia | Machine protocol | Census Exception Officer (269, Judge or tribunal chair) | Control Engineer (270, Grid engineer) | Human Protocol Council (271, Local mayor or ward chair) |
| South asia | Technate | Grid Dispatcher (272, Quartermaster) | Irrigation Engineer (273, Grid engineer) | Public Safety Audit Office (274, Judge or tribunal chair) |
| South asia | Mutant polity | Altered-Community Physician (275, Doctor or medical board) | Family Rights Advocate (276, Judge or tribunal chair) | Mixed Settlement Council (277, Local mayor or ward chair) |
| South asia | Religious refuge | Community Kitchen Organizer (278, Quartermaster) | Relief Leader (279, Doctor or medical board) | Interfaith Sanctuary Council (280, Local mayor or ward chair) |
| Middle east north africa | Continuity government | Constitutional Adviser (281, Judge or tribunal chair) | Water Ministry Engineer (282, Grid engineer) | Municipal Congress (283, Local mayor or ward chair) |
| Middle east north africa | Bunker authority | Shelter Registrar (284, Quartermaster) | Desalination Engineer (285, Grid engineer) | Surface-Family Delegation (286, Local mayor or ward chair) |
| Middle east north africa | Warlord command | Tanker Quartermaster (287, Quartermaster) | Pipeline Commander (288, Militia commander) | Well-Garrison Council (289, Local mayor or ward chair) |
| Middle east north africa | Food compact | Oasis Agronomist (290, Quartermaster) | Canal Scheduler (291, Grid engineer) | Market-Ration Delegation (292, Local mayor or ward chair) |
| Middle east north africa | Maritime remnant | Port Water Superintendent (293, Quartermaster) | Convoy Captain (294, Militia commander) | Harbor Council (295, Local mayor or ward chair) |
| Middle east north africa | Quarantine state | Border Physician (296, Doctor or medical board) | Water Certification Corps Chief (297, Grid engineer) | Movement Appeals Court (298, Judge or tribunal chair) |
| Middle east north africa | Scavenger syndicate | Pump Assessor (299, Quartermaster) | Refinery Salvage Foreman (300, Grid engineer) | Public Utilities Trust (301, Judge or tribunal chair) |
| Middle east north africa | Nomad convoy | Well-Route Judge (302, Judge or tribunal chair) | Tanker Mechanic (303, Grid engineer) | Mobile Family Council (304, Local mayor or ward chair) |
| Middle east north africa | Machine protocol | Exception Officer (305, Judge or tribunal chair) | Pipeline Systems Custodian (306, Grid engineer) | Human Maintenance Board (307, Local mayor or ward chair) |
| Middle east north africa | Technate | Desalination Director (308, Quartermaster) | Reservoir Engineer (309, Grid engineer) | Public Utility Review Council (310, Judge or tribunal chair) |
| Middle east north africa | Mutant polity | Mixed Clinic Director (311, Doctor or medical board) | Altered-Community Mediator (312, Local mayor or ward chair) | Equal-Status Court (313, Judge or tribunal chair) |
| Middle east north africa | Religious refuge | Relief Cleric (314, Doctor or medical board) | Water-Charity Steward (315, Quartermaster) | Sanctuary Route Council (316, Local mayor or ward chair) |
| Sub saharan africa | Continuity government | Constitutional Clerk (317, Judge or tribunal chair) | River-Basin Administrator (318, Grid engineer) | Regional Assembly (319, Local mayor or ward chair) |
| Sub saharan africa | Bunker authority | Shelter Health Officer (320, Doctor or medical board) | Mine Engineer (321, Grid engineer) | Surface Liaison Council (322, Local mayor or ward chair) |
| Sub saharan africa | Warlord command | Convoy Quartermaster (323, Quartermaster) | Bridge Commander (324, Militia commander) | Mine Garrison Council (325, Local mayor or ward chair) |
| Sub saharan africa | Food compact | Seed Custodian (326, Quartermaster) | Lake Cooperative Chair (327, Grid engineer) | Pastoral Corridor Delegation (328, Local mayor or ward chair) |
| Sub saharan africa | Maritime remnant | Port Market Captain (329, Quartermaster) | River Pilot (330, Militia commander) | Dock Cooperative (331, Local mayor or ward chair) |
| Sub saharan africa | Quarantine state | Mobile Clinic Director (332, Doctor or medical board) | Water-Testing Chief (333, Grid engineer) | Permit Appeals Council (334, Judge or tribunal chair) |
| Sub saharan africa | Scavenger syndicate | Generator Assessor (335, Quartermaster) | Mine Salvage Foreman (336, Grid engineer) | Local Ownership Tribunal (337, Judge or tribunal chair) |
| Sub saharan africa | Nomad convoy | Well-Corridor Mediator (338, Judge or tribunal chair) | Caravan Mechanic (339, Grid engineer) | Mobile Household Assembly (340, Local mayor or ward chair) |
| Sub saharan africa | Machine protocol | Systems Liaison (341, Local mayor or ward chair) | Relay Maintenance Chief (342, Grid engineer) | Community Exception Board (343, Judge or tribunal chair) |
| Sub saharan africa | Technate | Mine Safety Chair (344, Judge or tribunal chair) | Pump Engineer (345, Grid engineer) | Continental Relay Office (346, Local mayor or ward chair) |
| Sub saharan africa | Mutant polity | Altered-Community Organizer (347, Local mayor or ward chair) | Safe-Work Advocate (348, Judge or tribunal chair) | Mixed Clinic Board (349, Doctor or medical board) |
| Sub saharan africa | Religious refuge | Community Health Steward (350, Doctor or medical board) | Relief Leader (351, Quartermaster) | Multi-Settlement Sanctuary Council (352, Local mayor or ward chair) |
| Latin america caribbean | Continuity government | Constitutional Secretary (353, Judge or tribunal chair) | Public Works Administrator (354, Grid engineer) | Provincial Congress (355, Local mayor or ward chair) |
| Latin america caribbean | Bunker authority | Shelter Registrar (356, Quartermaster) | Tunnel Engineer (357, Grid engineer) | Surface Barrio Delegation (358, Local mayor or ward chair) |
| Latin america caribbean | Warlord command | Mineral-Camp Quartermaster (359, Quartermaster) | Pass Commander (360, Militia commander) | Airfield Colonels' Council (361, Local mayor or ward chair) |
| Latin america caribbean | Food compact | Grain-Port Steward (362, Quartermaster) | Cooperative Agronomist (363, Grid engineer) | Island Food Delegation (364, Local mayor or ward chair) |
| Latin america caribbean | Maritime remnant | Fisher Council Speaker (365, Local mayor or ward chair) | Convoy Captain (366, Militia commander) | River Pilots' Guild (367, Grid engineer) |
| Latin america caribbean | Quarantine state | Port Physician (368, Doctor or medical board) | Border Health Magistrate (369, Judge or tribunal chair) | Mobile Water Laboratory (370, Doctor or medical board) |
| Latin america caribbean | Scavenger syndicate | Turbine Assessor (371, Quartermaster) | Mine Recovery Foreman (372, Grid engineer) | Municipal Ruins Trust (373, Judge or tribunal chair) |
| Latin america caribbean | Nomad convoy | Pass Guide (374, Militia commander) | Convoy Mechanic (375, Grid engineer) | Mobile Family Assembly (376, Local mayor or ward chair) |
| Latin america caribbean | Machine protocol | Human Exception Officer (377, Judge or tribunal chair) | Hydro Systems Custodian (378, Grid engineer) | Relay Maintenance Council (379, Local mayor or ward chair) |
| Latin america caribbean | Technate | Hydro Dispatcher (380, Quartermaster) | Mine Safety Engineer (381, Grid engineer) | Public Utility Audit Board (382, Judge or tribunal chair) |
| Latin america caribbean | Mutant polity | Mixed Settlement Physician (383, Doctor or medical board) | Altered-Community Advocate (384, Local mayor or ward chair) | Equal-Status Council (385, Judge or tribunal chair) |
| Latin america caribbean | Religious refuge | Relief Leader (386, Doctor or medical board) | Neighborhood Kitchen Steward (387, Quartermaster) | Sanctuary Federation (388, Local mayor or ward chair) |
| Oceania remote islands | Continuity government | Parliamentary Clerk (389, Quartermaster) | Emergency Services Commissioner (390, Militia commander) | Island Federation (391, Local mayor or ward chair) |
| Oceania remote islands | Bunker authority | Shelter Registrar (392, Quartermaster) | Station Engineer (393, Grid engineer) | Surface-Island Delegation (394, Local mayor or ward chair) |
| Oceania remote islands | Warlord command | Airfield Quartermaster (395, Quartermaster) | Patrol Commander (396, Militia commander) | Harbor Chiefs' Council (397, Local mayor or ward chair) |
| Oceania remote islands | Food compact | Island Agronomist (398, Quartermaster) | Fisher Cooperative Chair (399, Grid engineer) | Landing-Ration Delegation (400, Local mayor or ward chair) |
| Oceania remote islands | Maritime remnant | Harbor Master (401, Quartermaster) | Rescue Commodore (402, Militia commander) | Refugee Fleet Council (403, Local mayor or ward chair) |
| Oceania remote islands | Quarantine state | Floating Clinic Director (404, Doctor or medical board) | Port Health Officer (405, Doctor or medical board) | Landing Appeals Board (406, Judge or tribunal chair) |
| Oceania remote islands | Scavenger syndicate | Cable Assessor (407, Quartermaster) | Marine Salvage Diver (408, Grid engineer) | Public Wreck Trust (409, Judge or tribunal chair) |
| Oceania remote islands | Nomad convoy | Flotilla Navigator (410, Militia commander) | Marine Mechanic (411, Grid engineer) | Shipboard Household Assembly (412, Local mayor or ward chair) |
| Oceania remote islands | Machine protocol | Rescue Exception Officer (413, Judge or tribunal chair) | Station Systems Custodian (414, Grid engineer) | Human Maintenance Council (415, Local mayor or ward chair) |
| Oceania remote islands | Technate | Cable Systems Director (416, Quartermaster) | Desalination Engineer (417, Grid engineer) | Public Load-Review Board (418, Judge or tribunal chair) |
| Oceania remote islands | Mutant polity | Mixed Clinic Team Leader (419, Doctor or medical board) | Altered-Islander Advocate (420, Local mayor or ward chair) | Equal-Landing Tribunal (421, Judge or tribunal chair) |
| Oceania remote islands | Religious refuge | Shipboard Chaplain (422, Doctor or medical board) | Relief Leader (423, Quartermaster) | Island Sanctuary Council (424, Local mayor or ward chair) |

