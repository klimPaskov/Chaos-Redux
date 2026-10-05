# Event 26 owner adoption requests

Disposition: `owner adoption pending` for every active workstream below (agent decision D8, 2026-10-04).
The Event 26 engineer does not edit active owners' files in the shared tree; each owner converts its own positive voluntary costs and commits them with its own work, under the spec Part 4 Future coverage rule.
Line numbers come from a decision-depth scan of the working tree at HEAD `280df0b95` on 2026-10-04, including uncommitted owner work present at that time; the Event 039 and Event 006 foreign-reaction lists come from HEAD `d0ceff0b2` on 2026-10-05. Rescan before editing.

## Which API to use

| Cost shape | API | Reference |
| --- | --- | --- |
| Native `cost = N` or `cost = constant:K` (political power) | Register the ordinary amount in the sale price table, set `cost = global.black_friday_price_<key>`, and bump `price_table_version` | [`026_black_friday_price_table_effects.md`](../../../common/scripted_effects/026_black_friday_price_table_effects.md) |
| Native `cost = <variable>` | Keep the variable as the ordinary price and move it to a custom cost priced with the simple API, or keep a sale copy computed with `black_friday_price_table_quote` when the sale starts and ends | Both references |
| Immediate custom cost in one resource, no refund | `black_friday_simple_cost_is_affordable` as `custom_cost_trigger`, `black_friday_simple_cost_pay` in `complete_effect`, and an owner `defined_text` pointing at `black_friday_simple_cost.line` | [`026_black_friday_simple_cost_api.md`](../../../common/scripted_effects/026_black_friday_simple_cost_api.md) |
| Immediate custom cost in several resources | One simple-API affordability check per resource in `custom_cost_trigger`; pay every component, with `black_friday_simple_cost_no_credit = 1` before each secondary component and the primary component paid last | Same |
| Refundable, delayed, or all-or-nothing bundle | The universal receipt framework and an owner adapter | [`universal_cost_modifier`](../../systems/universal_cost_modifier.md) |
| Penalty, upkeep, reward, casualty, or time | Not a purchase: record the exclusion in the registry | Spec Part 4 |

## Active workstreams

### 006 Independence Wave

Positive native costs: 6; dynamic native costs: 0; custom cost declarations: 714.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/006_independence_wave_balkan_decisions.txt` | - | - | 71, 88, 104, 121, 137, 153, 169, 184, 199, 214, 227, 293, 317, 345, 374, 390, 406, 422, 437, 452, 467, 480, 560, 577, 593, 610, 626, 642, 658, 673, 688, 703, 716, 792, 809, 837, 866, 882, 898, 914, 929, 944, 959, 972, 1048, 1065, 1081, 1098, 1114, 1130, 1146, 1161, 1176, 1191, 1204, 1273, 1293, 1312, 1357, 1390, 1406, 1422, 1437, 1452, 1467, 1535, 1552, 1580, 1609, 1625, 1641, 1657, 1672, 1687, 1702, 1715, 1766, 1783, 1799, 1816, 1845, 1861, 1877, 1892, 1907, 1920 |
| `common/decisions/006_independence_wave_bashkiria_mari_decisions.txt` | - | - | 74, 115, 158, 216, 286, 330, 373, 417, 470, 528, 630, 672, 716, 775, 846, 891, 935, 980, 1034, 1093 |
| `common/decisions/006_independence_wave_decisions.txt` | - | - | 39, 102, 147, 220, 277, 327, 356, 392, 451, 497, 559, 625, 710, 804, 875, 922, 974, 1145, 1186, 1230, 1261, 1310, 1364, 1413, 1472, 1522, 1571, 1619, 1664, 1738, 1778, 1840, 1906, 1969, 2015, 2109, 2169, 2210, 2264, 2317, 2374, 2419, 2460, 2543, 2666, 2793, 2842, 2908, 2994, 3055, 3086, 3121, 3180, 3203, 3226, 3249, 3272, 3313, 3396, 3451, 3534, 3594, 3676, 3733, 3822, 3864, 3904, 3951, 3985, 4037, 4100, 4229, 4376, 4417, 4458, 4499, 4544, 4591, 4631, 4671, 4720 |
| `common/decisions/006_independence_wave_don_decisions.txt` | - | - | 116, 152, 181, 197, 216, 234 |
| `common/decisions/006_independence_wave_far_eastern_decisions.txt` | - | - | 84, 128, 174, 235, 314, 361, 407, 454, 516, 576 |
| `common/decisions/006_independence_wave_form01_02_04_decisions.txt` | - | - | 36, 94, 145, 206, 234, 256, 271, 286, 316, 332, 348, 363, 378, 408, 424, 440, 455, 470 |
| `common/decisions/006_independence_wave_form03_decisions.txt` | - | - | 34, 81, 121, 157, 187, 220, 257, 296, 339, 372, 408, 450, 492, 522, 569, 629, 654, 684, 714, 742, 774, 804 |
| `common/decisions/006_independence_wave_foreign_reaction_decisions.txt` | - | - | 30 |
| `common/decisions/006_independence_wave_form05_decisions.txt` | - | - | 39, 81, 111, 144, 177, 209, 242, 275, 313, 375, 415, 457, 497, 530 |
| `common/decisions/006_independence_wave_form48_decisions.txt` | - | - | 29, 76, 112, 147, 228, 282, 337 |
| `common/decisions/006_independence_wave_formable_decisions.txt` | - | - | 33, 57, 81, 117, 173, 200, 224, 250, 281, 313 |
| `common/decisions/006_independence_wave_frontier_decisions.txt` | - | - | 79, 121, 165, 224, 295, 340, 384, 429, 476, 526, 585, 689, 731, 796, 876, 947, 992, 1036, 1081, 1135, 1194 |
| `common/decisions/006_independence_wave_iberian_decisions.txt` | - | - | 34, 50, 66, 83, 99, 116, 133, 149, 165, 181, 194, 228, 244, 260, 277, 293, 310, 327, 343, 359, 375, 388 |
| `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` | - | - | 30, 105, 143, 178, 218, 260, 359, 435, 515, 623, 702, 791, 885, 957, 1031, 1139, 1230, 1290, 1316, 1342, 1368, 1399, 1469, 1555, 1650, 1735, 1835, 1921, 2001, 2076, 2158, 2184, 2206, 2223, 2240, 2263, 2297, 2458 |
| `common/decisions/006_independence_wave_iw093_iw098_decisions.txt` | 102, 160, 219, 699, 754, 810 | - | 30, 235, 310, 361, 415, 504, 575, 629, 879, 931, 986, 1077, 1149 |
| `common/decisions/006_independence_wave_karelia_crimea_decisions.txt` | - | - | 61, 87, 124, 160, 187, 223, 249, 286, 313, 335, 357, 379, 400, 422, 444, 466, 487, 509, 527, 545 |
| `common/decisions/006_independence_wave_mediterranean_decisions.txt` | - | - | 43, 65, 85, 102, 117, 132, 146, 160, 193, 210, 227, 243, 258, 273, 287, 301, 334, 351, 368, 384, 400, 415, 430, 444, 458, 472 |
| `common/decisions/006_independence_wave_minor_overlay_decisions_registry.txt` | - | - | 60, 83, 109, 142, 175, 209, 249, 273, 302, 363, 390, 424, 448, 477, 538, 565, 599, 623, 652, 713, 740, 773, 797, 821, 876, 906, 923, 940, 975, 1003, 1020, 1037, 1069, 1088, 1105, 1122, 1154, 1173, 1190, 1207, 1239, 1267, 1279, 1291, 1317, 1332, 1344, 1356, 1382, 1397, 1409, 1421, 1447, 1462, 1474, 1486, 1512 |
| `common/decisions/006_independence_wave_pacific_decisions.txt` | - | - | 49, 71, 94, 117, 140, 157, 200, 222, 243, 266, 308, 324, 340, 356, 372, 388, 404, 424, 466, 483, 500, 516, 532, 548 |
| `common/decisions/006_independence_wave_rhineland_bavaria_saar_decisions.txt` | - | - | 63, 87, 108, 130, 152, 167, 182, 196, 210, 222, 239, 268, 283, 359, 375, 390, 405, 421, 436, 451, 465, 479, 491, 511, 534, 549, 628, 651, 673, 695, 718, 733, 748, 762, 777, 789, 809, 828, 868 |
| `common/decisions/006_independence_wave_scotland_wales_decisions.txt` | - | - | 21, 44, 66, 89, 111, 127, 143, 158, 173, 188, 210, 253, 270, 287, 303, 319, 335, 351, 366, 388 |
| `common/decisions/006_independence_wave_shared_decisions.txt` | - | - | 27, 72, 116, 161, 206, 265, 310, 369, 397, 423, 450 |
| `common/decisions/006_independence_wave_siberian_decisions.txt` | - | - | 93, 137, 183, 244, 318, 365, 411, 458, 514, 575, 689, 731, 775, 834, 905, 950, 994, 1039, 1093, 1152, 1265, 1307, 1351, 1410, 1481, 1526, 1570, 1615, 1669, 1728, 1841, 1883, 1927, 1986, 2057, 2102, 2146, 2191, 2245, 2304, 2369, 2386, 2403, 2420, 2437, 2454, 2471, 2488, 2504, 2521, 2607, 2624, 2641, 2658, 2675, 2692, 2709, 2726, 2754, 2800, 2906, 2952, 3000, 3063, 3157, 3202, 3246, 3291, 3345, 3408, 3520, 3562, 3606, 3665, 3736, 3781, 3825, 3870, 3924, 3983 |
| `common/decisions/006_independence_wave_transcaucasus_decisions.txt` | - | - | 53, 70, 86, 103, 133, 150, 166, 184, 214, 230, 247, 264, 282, 300, 318, 337, 349, 361, 373 |
| `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt` | - | - | 74, 111, 150, 194, 226, 242, 258, 274, 298, 378, 410, 441, 472, 508, 550, 566, 582, 619 |
| `common/decisions/006_independence_wave_western_decisions.txt` | - | - | 70, 94, 118, 141, 165, 191, 217, 233, 249, 265, 280, 295, 308, 331, 420, 437, 453, 470, 486, 503, 520, 536, 552, 568, 581, 651, 694, 733, 770, 805, 850 |

### 012 Africa

Positive native costs: 154; dynamic native costs: 0; custom cost declarations: 34.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/012_africa_decisions.txt` | 108, 337, 362, 405, 611, 630, 1521, 1848, 1866, 1884, 1899, 1908, 2126, 2154, 2192, 2529, 2593, 2608, 2627, 2643, 2660, 2679, 2698, 2717, 2736, 2755, 2768, 2780, 2792, 2804, 2816, 2828, 2842, 2854, 2866, 2878, 2890, 2902, 2922, 2944, 2963, 2982, 3001, 3015, 3029, 3046, 3061, 3076, 3089, 3100, 3111, 3122, 3133, 3148, 3162, 3173, 3187, 3198, 3207, 3216 | - | 462, 479, 1647, 1667, 2232, 2256, 2281, 2308, 3396, 3426, 3466 |
| `common/decisions/012_africa_elephant_operations_decisions.txt` | 42, 137 | - | 82 |
| `common/decisions/012_africa_gods_decisions.txt` | - | - | 95, 134, 165, 265, 291, 317, 457, 478, 499, 520, 549, 936 |
| `common/decisions/012_africa_priority_member_decisions.txt` | 14, 29, 44, 57, 69, 87, 129, 145, 161, 177, 193, 209, 225, 241, 257, 274, 290, 306, 322, 338, 354, 370, 384, 401, 418, 435, 452, 469, 486, 503, 520, 537, 554, 571, 588, 605, 622, 639, 658, 674, 690, 706, 722, 738, 754, 770, 786, 803, 820, 836, 852, 869, 886, 902, 918, 934, 950, 966, 979, 995, 1012, 1028, 1044, 1060, 1076, 1092, 1108, 1121, 1137, 1153, 1169 | - | - |
| `common/decisions/012_africa_promoted_tiera_decisions.txt` | 12, 21, 30, 39, 48, 57, 66, 75, 84, 93, 102, 111, 120, 129, 138, 154, 176, 198, 225, 249 | - | 155, 177, 199, 226, 250 |
| `common/decisions/012_africa_rsa_decisions.txt` | 186 | - | 29, 65, 124, 164, 214 |

South Africa purchases: the four immediate RSA actions other than the timed one keep their persistent receipt pointer when abnormal settlement fails after the outcome (`docs/systems/africa_rsa_purchase_transactions.md`, Remaining owner findings). The Event 12 owner needs to implement recovery for that state, settling or refunding the pending receipt on the next owner pulse, and confirm it survives save and reload.

### 014 Cannibalism

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 94.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/014_cannibalism_decisions.txt` | - | - | 58, 90, 113, 140, 164, 189, 217, 240, 264, 455, 483, 546, 616, 664, 700, 732, 767, 793, 823, 858, 902, 931, 969, 1098, 1128, 1302, 1326, 1415, 1443, 1487, 1504, 1520, 1536, 1593, 1616, 1633, 1650, 1668, 1685, 1702, 1719, 1754, 1771, 1788, 1805, 1822, 1839, 1856, 1869, 1885, 1904, 1918, 1936, 1949, 1987, 2005, 2023, 2041, 2061, 2076, 2095, 2138, 2156, 2190, 2219, 2249, 2276, 2306, 2336, 2371, 2402, 2432, 2460, 2485, 2510, 2538, 2559, 2580, 2619, 2654, 2679, 2708, 2737, 2761, 2785, 2814, 2873, 2905, 2937, 2962, 2975, 2991, 3004, 3017 |

### 016 Brilliant Scientist

Positive native costs: 307; dynamic native costs: 0; custom cost declarations: 111.

Event 019 family management: `brilliant_scientist_event19_pay_project_force_management` (`common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`), which providers `chaos_unit_family_provider_504` to `_507`, `_509`, `_510`, and `_522` call, pays army experience, infantry and clone equipment, manpower, political power, and command power at ordinary constants. Provider `_508` debits its laser reserve in the shared landing effect instead. Both are real payments and stay `owner adoption pending`; the matching affordability checks and the Event 019 management cost text must read the same sale price.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/016_alien_infantry_landing_decisions.txt` | - | - | 29 |
| `common/decisions/016_brilliant_scientist_achievement_decisions.txt` | 33, 73, 113, 153, 190, 231 | - | - |
| `common/decisions/016_brilliant_scientist_aftermath_decisions.txt` | 21, 38, 55, 74, 90, 115, 133, 149, 165, 187, 209, 227, 244, 265, 277, 289, 301, 313, 325, 337, 349, 361 | - | - |
| `common/decisions/016_brilliant_scientist_containment_decisions.txt` | - | - | 43, 115, 187, 259, 332, 404, 478, 551 |
| `common/decisions/016_brilliant_scientist_directorate_facilities.txt` | 35, 113, 212, 344, 462, 539 | - | - |
| `common/decisions/016_brilliant_scientist_directorate_foreign.txt` | 23, 63, 133, 227, 281, 333 | - | - |
| `common/decisions/016_brilliant_scientist_directorate_institutions.txt` | 28, 78, 130, 178, 232, 285, 331, 380, 432, 488, 537, 573, 693, 740, 786, 838, 891, 956, 1017, 1084, 1149 | - | - |
| `common/decisions/016_brilliant_scientist_directorate_project_board.txt` | 214, 247, 293, 381, 1006, 1067, 1128, 1185, 1246, 1307, 1364, 1425, 1486, 1543, 1604, 1665, 1722, 1783, 1844, 1901, 1962, 2023, 2080, 2141, 2202, 2259, 2320, 2381, 2438, 2499, 2560, 2615, 2674, 2733, 2788, 2847, 2906, 2961, 3020, 3079, 3134, 3193, 3252, 3307, 3366, 3425, 3480, 3539, 3598, 3845, 3885, 3925, 3965, 4008, 4200, 4268, 4336, 4404, 4472, 4540, 4608, 4676, 4744, 4812, 4880, 4948, 5016, 5084, 5152, 5211, 5264, 5317, 5370, 5423, 5476, 5529, 5582, 5635, 5688, 5741, 5794, 5847, 5900, 5953, 5997, 6039, 6081, 6123, 6165, 6207 | - | 4048, 4112, 5208, 5261, 5314, 5367, 5420, 5473, 5526, 5579, 5632, 5685, 5738, 5791, 5844, 5897, 5950, 5994, 6036, 6078, 6120, 6162, 6204 |
| `common/decisions/016_brilliant_scientist_directorate_synthesis.txt` | 39, 135, 223 | - | - |
| `common/decisions/016_brilliant_scientist_foreign_decisions.txt` | 27, 71, 98, 142, 186, 230, 274, 318, 345, 392, 436 | - | - |
| `common/decisions/016_brilliant_scientist_former_host_recovery_decisions.txt` | 34, 83, 124, 166 | - | - |
| `common/decisions/016_brilliant_scientist_kruger_state_canonical_and_exotic_decisions.txt` | 25, 55 | - | - |
| `common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt` | 30, 57, 139, 167, 249, 278, 292, 313, 330, 357, 379, 416, 439, 459, 473, 497, 525, 587, 604, 619, 662, 680 | - | 87 |
| `common/decisions/016_brilliant_scientist_kruger_state_foreign_integration_decisions.txt` | 24, 37, 58, 87, 119, 145, 178, 222, 268, 310, 341, 371, 392 | - | - |
| `common/decisions/016_brilliant_scientist_kruger_state_foundation_decisions.txt` | 23, 36, 58, 80, 102, 130, 169, 184, 199, 218, 232, 253, 286, 324, 351, 380, 407, 433, 449, 464, 484, 498, 538, 582, 601, 621, 644, 672 | - | - |
| `common/decisions/016_brilliant_scientist_kruger_state_paleo_xeno_decisions.txt` | 34, 76, 107, 127, 159, 190, 223, 250, 286, 327, 369, 402, 420, 453, 488 | - | - |
| `common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt` | 23, 46, 74, 106, 131, 159, 230, 257, 287, 308, 323, 340, 371, 440, 528, 558, 573, 595 | - | - |
| `common/decisions/016_brilliant_scientist_kruger_state_safeguard_decisions.txt` | 22, 40, 59, 79, 96, 116, 173, 250, 309 | - | - |
| `common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt` | 41, 80, 104, 126, 146, 165, 185, 215, 253, 286, 331, 363, 389, 425, 479 | - | - |
| `common/decisions/016_brilliant_scientist_portal_containment_decisions.txt` | - | - | 41 |
| `common/decisions/016_brilliant_scientist_technology_actions.txt` | - | - | 25, 47, 69, 88, 112, 137, 157, 176 |
| `common/decisions/016_dhrondan_contact_decisions.txt` | 34, 68, 93 | - | - |
| `common/decisions/016_dhrondan_country_decisions.txt` | 33, 95, 155, 198, 241 | - | - |
| `common/decisions/016_mengele_alien_arms_stage_decisions.txt` | - | - | 25, 66, 124, 165 |
| `common/decisions/016_mengele_biological_stage_decisions.txt` | - | - | 26, 73, 120, 167 |
| `common/decisions/016_mengele_biomedical_prototype_decision.txt` | - | - | 16 |
| `common/decisions/016_mengele_cloning_stage_decisions.txt` | - | - | 25, 66, 136, 177 |
| `common/decisions/016_mengele_computation_incident_decisions.txt` | - | - | 45 |
| `common/decisions/016_mengele_computation_stage_decisions.txt` | - | - | 51, 133, 215, 297 |
| `common/decisions/016_mengele_conventional_incident_decisions.txt` | - | - | 24, 73, 122, 171, 220 |
| `common/decisions/016_mengele_conventional_stage_decisions.txt` | - | - | 45, 92, 139, 186, 233, 280, 327, 374, 421, 468, 515, 562, 612, 659, 706 |
| `common/decisions/016_mengele_materials_stage_decisions.txt` | - | - | 16 |
| `common/decisions/016_mengele_native_prototype_selection_decisions.txt` | 10, 22, 36, 48, 60, 72, 84, 96 | - | - |
| `common/decisions/016_mengele_paleogenetics_stage_decisions.txt` | - | - | 25, 66, 124, 165 |
| `common/decisions/016_mengele_remaining_conventional_prototype_decisions.txt` | - | - | 21, 62, 103 |
| `common/decisions/016_mengele_robotics_stage_decisions.txt` | - | - | 25, 66, 124, 165 |
| `common/decisions/016_mengele_singularity_construction_decisions.txt` | - | - | 30, 86 |
| `common/decisions/016_mengele_singularity_incident_decisions.txt` | - | - | 21 |
| `common/decisions/016_mengele_singularity_stage_decisions.txt` | - | - | 22, 66, 110, 154 |
| `common/decisions/016_mengele_teleportation_stage_decisions.txt` | - | - | 25, 66, 124, 165 |
| `common/decisions/016_mengele_temporal_stage_decisions.txt` | - | - | 25, 66, 124, 165 |
| `common/decisions/016_mengele_xenobiological_synthesis_stage_decisions.txt` | - | - | 25, 66, 124, 165 |

### 021 Random Civil War

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 18.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/021_random_civil_war_decisions.txt` | - | - | 30, 67, 109, 153, 195, 239, 280, 316, 365, 393, 440, 503, 556, 600, 635, 672, 709, 746 |

### 023 Soviet Nuclear Bombs

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 64.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/023_sov_nuclear_bombs_decisions.txt` | - | - | 21, 36, 51, 66, 86, 100, 131, 146, 174, 203, 254, 268, 287, 306, 329, 343, 357, 376, 390, 404, 418, 432, 468, 497, 523, 537, 551, 591, 605, 619, 633, 660, 674, 688, 702, 720, 734, 761, 775, 789, 807, 838, 852, 866, 880, 899, 913, 927, 941, 955, 969, 983, 997, 1024, 1052, 1066, 1080, 1094, 1118, 1149, 1171, 1191, 1211, 1235 |

### 025 Alien Technology in Antarctica

Positive native costs: 3; dynamic native costs: 0; custom cost declarations: 70.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/025_alien_technology_in_antarctica_aftermath_decisions.txt` | - | - | 18, 42, 59, 76 |
| `common/decisions/025_alien_technology_in_antarctica_decisions.txt` | - | - | 23, 43, 62, 79, 98, 117, 136, 155, 174, 193, 212, 231, 253, 277, 300, 317, 334, 347, 357, 367, 377, 387, 402, 415, 425, 435, 445, 455, 474, 502, 531, 561, 591, 613, 629, 645, 661, 677, 705, 726, 746 |
| `common/decisions/025_alien_technology_in_antarctica_evolution_decisions.txt` | - | - | 15, 24, 33, 42, 51, 61, 70, 79, 88, 97, 110, 122, 134, 146, 155, 165, 174, 183, 192, 201, 211, 223, 232, 241, 254 |
| `common/decisions/025_antarctic_ufo_race_decisions.txt` | 10, 80, 160 | - | - |

### 029 Riches Found

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 92.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/029_riches_found_decisions.txt` | - | - | 71, 162, 243, 329, 409, 490, 567, 664, 751, 842, 936, 1026, 1122, 1207, 1288, 1380, 1474, 1571, 1660, 1763, 1853, 1943, 2029, 2113, 2192, 2283, 2371, 2468, 2576, 2683, 2796, 2904, 2996, 3091, 3190, 3285, 3375, 3464, 3554, 3648, 3728, 3824, 3913, 3999, 4081, 4172, 4265, 4356, 4448, 4541, 4620, 4711, 4803, 4902, 4994, 5089, 5182, 5273, 5364, 5453, 5540, 5628, 5705, 5789, 5879, 5964, 6050, 6140, 6230, 6316, 6401, 6491, 6580, 6676, 6771, 6862, 6951, 7037, 7123, 7213, 7305, 7392, 7480, 7567, 7653, 7741, 7831, 7920, 8028, 8129, 8231, 8338 |

### 031 Random Terror

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 42.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/031_random_terror_decisions.txt` | - | - | 71, 158, 269, 366, 439, 534, 616, 695, 758, 823, 895, 960, 1022, 1084, 1158, 1238, 1319, 1445, 1542, 1622, 1689, 1750, 1796, 1839, 1917, 1984, 2063, 2165, 2248, 2345, 2427, 2508, 2595, 2693, 2770, 2860, 2933, 3012, 3070, 3155, 3246, 3314 |

### 033 Acid Rain

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 13.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/033_acid_rain_decisions.txt` | - | - | 101, 149, 198, 247, 303, 344, 386, 428, 503, 578, 645, 712, 766 |

### 035 Great Depression

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 89.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/035_great_depression_decisions.txt` | - | - | 32, 69, 105, 141, 178, 214, 255, 287, 318, 360, 444, 491, 538, 585, 632, 686, 720, 771, 824, 858, 908, 944, 978, 1021, 1055, 1092, 1126, 1159, 1192, 1228, 1279, 1313, 1346, 1382, 1434, 1469, 1503, 1535, 1575, 1615, 1654, 1692, 1731, 1771, 1810, 1859, 1897, 1936, 1965, 1995, 2035, 2072, 2112, 2150, 2184, 2215, 2246, 2296, 2327, 2358, 2407, 2438, 2480, 2509, 2539, 2578, 2609, 2662, 2693, 2722, 2752, 2783, 2811, 2842, 2874, 2909, 2944, 2979, 3014, 3049, 3084, 3119, 3154, 3189, 3224, 3259, 3294, 3329, 3364 |

### Camps (administration and repression)

Positive native costs: 78; dynamic native costs: 0; custom cost declarations: 34.

Disposition (Camps owner, 2026-10-05): native costs `converted`. All 78 read `global.black_friday_price_camp_rework_cost_<key>` for the nine registered `camp_rework_cost.*_pp` keys, credit one Political Power purchase, and refund the recorded charged amount (`camp_rework_native_pp_paid`) when an order is refused; the window's action prices read the same globals (`docs/plans/system_camp_repression_rework_plans/agent_decisions_2026-10-04.md`, entry 13). Custom costs and the three genocide-crisis payments below: `owner adoption pending`. The line numbers below predate the conversion.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/camp_administration_country_decisions.txt` | - | - | 30 |
| `common/decisions/camp_repression_colonial_country_decisions.txt` | 23, 70, 152, 247, 335, 365, 389, 420, 513, 548, 688, 775, 837, 892, 912, 993, 1028, 1060, 1153, 1192, 1222, 1303, 1350, 1383, 1417, 1452, 1519, 1666, 1747, 1806, 1847, 1880, 1927, 1954, 2018, 2147, 2254, 2321, 2358, 2390, 2424, 2479, 2508 | - | 248, 1908 |
| `common/decisions/camp_repression_generic_decisions.txt` | 72, 235, 540, 582, 614, 883 | - | 73, 236, 305, 425, 541, 615, 688, 784, 821, 864, 884 |
| `common/decisions/camp_repression_major_country_decisions.txt` | 42, 93, 179, 223, 261, 314, 358, 537, 585, 628, 659, 680, 717, 775, 805, 831, 873, 912, 937, 962, 1119, 1180, 1222, 1244, 1268, 1309, 1334, 1397, 1432 | - | 43, 94, 180, 224, 262, 315, 359, 538, 718, 776, 806, 832, 874, 963, 1120, 1181, 1269, 1310, 1335, 1433 |

Camp-system payments called from the converted genocide crisis decisions also need the Camps owner's adoption: `camp_rework_germany_start_occupied_poland_expansion_mission_in_from` (manpower, support equipment, and trains from `camp_rework_cost.expansion_manpower` and `camp_rework_equipment_cost`, checked in `germany_expand_occupied_poland_camp_system`), `camp_occ_manual_transfer_can_pay` and its payment (`germany_transfer_prisoners_to_experiment_site`), and `camp_rework_consume_expansion_resources` (the Imperial occupation rail action). Each is an immediate payment that fits the price table (constant amounts) or the simple custom-cost API.

### Chaos warfare (CBRN)

Positive native costs: 21; dynamic native costs: 0; custom cost declarations: 55.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/biowarfare_disease_containment_decisions.txt` | 206, 382, 451, 488, 528, 567, 641, 681, 720, 794, 834, 873, 988 | - | 83, 138, 180, 273, 342, 611, 764, 917, 962, 1055, 1127, 1183, 1243, 1303 |
| `common/decisions/condemnation_sanctions_decisions.txt` | - | - | 111, 159, 180, 241, 316, 351, 371, 382, 402, 413, 424, 435, 456, 490, 524, 558, 603, 627, 651, 678 |
| `common/decisions/cbrn_diplomacy_decisions.txt` | - | - | 36, 110, 219, 329 |
| `common/decisions/cbrn_doctrine_decisions.txt` | - | - | 15, 62, 88, 118 |
| `common/decisions/cbrn_occupation_decisions.txt` | 27, 60, 325, 372 | - | 124, 197, 239, 284 |
| `common/decisions/cbrn_protection_decisions.txt` | 286, 325, 534, 555 | - | 58, 113, 171, 248, 379, 417, 460, 493, 516 |

Remaining CBRN surfaces beyond the line lists: the seal-state and destroy-records political power providers (`cbrn_seal_state` at `common/decisions/cbrn_occupation_decisions.txt:234` and `cbrn_destroy_contaminated_records` at `:279`, priced by the restored Condemnation providers) have no sale quote, payment, display, or achievement path yet; both are single political power payments and fit the simple custom-cost API.

The fixed procurement factory commitments in `common/decisions/cbrn_protection_decisions.txt` (`civilian_factory_use` at lines 48, 108, 163, 223, 289, and 327) have no sale variant; the Occupied Distribution (404 and 447) and Protective Aid (`cbrn_occupation_decisions.txt` 98 and 171) pairs show the accepted pattern of a mutually exclusive ordinary and sale commitment.

### 039 Murder Mystery

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 42.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/039_murder_mystery_decisions.txt` | - | - | 52, 103, 185, 261, 319, 380, 474, 551, 597, 648, 728, 805, 853, 901, 950, 1242, 1323, 1364, 1411, 1500, 1775, 1841, 1932, 1995, 2080, 2168, 2222, 2300, 2349, 2701, 2772, 2843, 2917, 2962, 3012, 3062, 3133, 3234, 3279, 3324, 3376, 3429 |

Its Event 019 family provider (`chaos_unit_family_provider_524_event19_pay_management_action`) pays nothing, so it is not a purchase.

### Famine and migration

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 26.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/famine_decisions.txt` | - | - | 217, 401, 589, 715, 943, 1139, 1283, 1508, 1652, 1740 |
| `common/decisions/migration_decisions.txt` | - | - | 517, 608, 661, 735, 839, 1057, 1284, 1434, 1479, 1615, 1826, 1960, 2124, 2278, 2407, 2638 |

## Queued with the Event 26 engineer

These owners have no active engineer, and their remaining costs are queued for the Event 26 engineer. Disposition: `queued: Event 26 conversion tranche 1` or `tranche 2`.

### Tranche 1

#### Event 013 Natural Disasters

Converted (agent decision D12): every cost trigger, payment, and cost text reads the sale price table; no Event 013 cost remains queued. The line list below predates the conversion.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 108.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/013_natural_disasters_decisions.txt` | - | - | 119, 159, 199, 239, 279, 319, 356, 392, 432, 468, 504, 540, 576, 616, 652, 688, 728, 764, 800, 840, 880, 920, 960, 1000, 1040, 1085, 1112, 1139, 1166, 1196, 1223, 1253, 1280, 1310, 1337, 1367, 1394, 1421, 1448, 1475, 1502, 1529, 1556, 1583, 1610, 1637, 1664, 1694, 1721, 1748, 1775, 1805, 1832, 1859, 1886, 1916, 1943, 1973, 2000, 2027, 2054, 2081, 2108, 2135, 2162, 2189, 2216, 2243, 2270, 2300, 2327, 2357, 2384, 2411, 2438, 2490, 2594, 2680, 2772, 2862, 2956, 3043, 3128, 3212, 3292, 3385, 3461, 3495, 3528, 3561, 3594, 3627, 3660, 3703, 3814, 3893, 3984, 4067, 4148, 4236, 4316, 4406, 4491, 4555, 6391, 6499, 6574, 6647 |

#### Event 020 Black Plague

Converted (agent decision D13): response, shared, national programme, last-response, and weaponization costs. The Rat Nation and Rat King meter decisions in `020_black_plague_rat_decisions.txt` are `not_a_purchase_cost` (D14). No Event 020 cost remains queued. The line list below predates the conversion.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 98.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/020_black_plague_rat_decisions.txt` | - | - | 20, 37, 57, 72, 94, 114, 149, 169, 185, 199, 213, 234, 253, 275, 296, 319, 342, 361, 380, 394, 413, 428, 461, 479, 499, 521, 542, 564, 598, 638, 679, 716, 766, 802, 838, 867 |
| `common/decisions/020_black_plague_response_decisions.txt` | - | - | 33, 94, 152, 201, 250, 308, 357, 413, 467, 512, 558, 604, 649, 697 |
| `common/decisions/020_black_plague_shared_response_decisions.txt` | - | - | 29, 73, 90, 111, 132, 153, 174, 195, 216, 237, 258, 279, 300, 321, 342, 363, 384, 405, 426, 447, 468, 489, 510, 531, 552, 574, 595, 616, 637, 658, 707, 772, 924, 944, 964, 984, 1004, 1024, 1044, 1064, 1084, 1104 |
| `common/decisions/020_black_plague_weaponization_decisions.txt` | - | - | 21, 51, 81, 110, 144, 180 |

#### Event 015 Utopia Manifesto (custom costs; native costs converted)

Converted (agent decisions D11 and D15): every constant-amount custom cost reads the sale price table in its trigger, payment, and text, and the state-scaled military and institutional growth costs and the Auxiliary Contract's consumed convoys follow the sale. No Event 015 cost remains queued. The line list below predates the conversion.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 101.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/015_utopia_manifesto_decisions.txt` | - | - | 39, 97, 177, 231, 284, 369, 539, 582, 626, 670, 716, 798, 850, 912, 981, 1054, 1101, 1148, 1196, 1276, 1356, 1421, 1486, 1559, 1626, 1718, 1771, 1808, 1845, 1882, 1919, 1967, 2057, 2110, 2160, 2216, 2268, 2320, 2418, 2469, 2599, 2669, 2801, 2847, 2896, 2954, 3008, 3061, 3236, 3313, 3368, 3462, 3511, 3585, 3652, 3720, 3762, 3817, 3886, 4009, 4099, 4149, 4191, 4267, 4359, 4454, 4549, 4613, 4670, 4834, 4962, 5027, 5107, 5184, 5241, 5341, 5388, 5439, 5490, 5544, 5580, 5612, 5652, 5712, 5809 |
| `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` | - | - | 31, 64, 97, 147, 181, 215, 251, 284, 318, 353, 390, 423, 459, 493, 527 |
| `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` | - | - | 66 |

### Tranche 2

#### Event 005 Soviet Collapse (custom costs; native costs converted)

Converted (agent decision D21). No Event 005 cost remains queued. The UWR aftermath invalid-target refunds return the charged price (D10). The line list below predates the conversion.

Resolved (agent decision D22): the nine decisions that showed and checked a cost but never charged it (`soviet_collapse_write_restored_charter`, `fev_negotiate_japanese_liaison_officers`, `ijx_press_trade_city_claims`, `pra_repair_the_branch_lines`, `pra_raise_mobile_supply_yards`, `pra_drive_the_junction_columns`, `dsc_register_field_hospital_columns`, `dsc_mark_the_unfinished_front_roads`, and `dsc_order_the_dead_army_forward`) now pay the shown cost through `soviet_collapse_pay_custom_splinter_medium_cost` or `soviet_collapse_pay_custom_splinter_low_cost`, at the sale price during a sale.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 198.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/005_soviet_collapse_decisions.txt` | - | - | 57, 122, 173, 237, 282, 327, 379, 4958, 5010, 5062, 5110, 5166, 5216, 5263, 5352, 5453, 5548, 5695, 5809, 5900, 5951, 6007, 6063, 6117, 6178, 6289, 6364, 6438, 6512, 6581, 6655, 6720, 6788, 6858, 6928, 7002, 7073, 7138, 7214, 7288, 7360, 7428, 7490, 7522, 7555, 7591, 7624, 7657, 7690, 7723, 7761, 7802, 7857, 7888, 7928, 8018, 8049, 8091, 8126, 8188, 8223, 8270, 8307, 8361, 8397, 8449, 8499, 8618, 8703, 8749, 8796, 8884, 8977, 9013, 9049, 9093, 9131, 9169, 9206, 9241, 9273, 9302, 9344, 9390, 9444, 9486, 9532, 9586, 9628, 9674, 9728, 9770, 9816, 9870, 9912, 9958, 10012, 10054, 10100, 10158, 10200, 10248, 10307, 10349, 10397, 10452, 10494, 10540, 10594, 10636, 10682, 10736, 10778, 10824, 10878, 10920, 10969, 11011, 11065, 11107, 11153, 11207, 11249, 11295, 11349, 11391, 11439, 11493, 11535, 11581, 11635, 11677, 11715, 11757, 11796, 11834, 11876, 11922, 11976, 12015, 12083, 12150, 12216, 12286, 12335, 12371, 12415, 12460, 12495, 12535, 12579, 12615, 12658, 12698, 12743, 12801, 12860, 12915, 12951, 13002, 13037, 13095, 13138, 13180, 13241, 13319, 13365, 13411, 13539, 13609, 13695, 13862, 13913, 13967, 14015, 14049, 14088, 14225, 14264, 14306, 14346, 14383, 14413, 14461, 14491, 14525, 14560, 14606, 14645, 14682, 14722, 14755, 14785, 14851, 14885, 14927, 14971, 15008 |

#### Event 010 Death

Converted (agent decision D17): every human payment reads the sale price table; Death's soul power and custodial capacity are not purchases. No Event 010 cost remains queued. The line list below predates the conversion.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 35.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/010_death_decisions.txt` | - | - | 33, 76, 114, 146, 178, 216, 245, 274, 343, 367, 392, 424, 450, 538, 561, 583, 624, 705, 731, 757, 787, 837, 895, 947, 968, 992, 1015, 1041, 1079, 1100, 1126, 1147, 1203, 1251, 1275 |

#### Event 011 Secret Alliance

Converted (agent decision D19). No Event 011 cost remains queued. The line list below predates the conversion.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 56.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/011_secret_alliance_decisions.txt` | - | - | 57, 77, 97, 117, 137, 158, 179, 209, 380, 391, 418, 440, 451, 475, 500, 527, 542, 554, 566, 578, 590, 602, 614, 630, 641, 652, 663, 674, 685, 696, 707, 722, 733, 744, 763, 780, 798, 833, 845, 857, 869, 881, 899, 910, 921, 932, 955, 966, 977, 1036, 1047, 1058, 1070, 1082, 1093, 1104 |

#### Event 018 Resources Found

Converted (agent decision D20). No Event 018 cost remains queued. The line list below predates the conversion.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 100.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/018_resources_found_decisions.txt` | - | - | 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 338, 348, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 492, 502, 512, 522, 533, 543, 561, 571, 581, 592, 610, 620, 630, 640, 650, 660, 670, 793, 803, 813, 823, 833, 843, 853, 863, 873, 889, 899, 909, 919, 929, 939, 949, 959, 1004, 1017, 1030, 1043, 1077, 1087, 1097, 1107, 1126, 1136, 1146, 1156, 1166, 1176, 1186, 1196, 1262, 1275, 1288, 1301, 1311, 1321, 1331, 1343, 1356, 1375 |

#### Event 019 Infantry Spawn (custom costs; derivative native costs converted)

Converted (agent decision D18): scaled formation requests, fixed management and prototype costs, claimant responses, derivative decisions, and the zombie rally band. Family management payments that `infantry_spawn_derivative_pay_current_family_management` routes to each unit family provider (`chaos_unit_family_provider_<id>_event19_pay_management_action`), rescanned on 2026-10-05:

- Not a purchase: `chaos_unit_family_provider_511` (Event 002, `002_zombie_outbreak_effects.txt`), `_514` (Event 010, `010_death_effects.txt`), `_518` (Event 018, `018_resources_found_cave_effects.txt`), `_520` (Event 020, `020_black_plague_effects.txt`), `_512` and `_513` (Event 012, `012_africa_effects.txt`), `_523` (Event 014, `014_cannibalism_effects.txt`), `_524` (Event 039, `039_murder_mystery_event19_effects.txt`), and `_521` (CBRN, `cbrn_doctrine_effects.txt`) only report whether the family can spawn or be sustained and charge nothing (`not_a_purchase_cost`).
- Owner adoption pending: the Event 016 providers `_504` to `_507`, `_509`, `_510`, and `_522` pay through `brilliant_scientist_event19_pay_project_force_management`, and `_508` through its laser reserve (see 016 above).
- Converted (agent decision D30): Event 019's own zombie, ghost, and golem family providers `_501`, `_502`, and `_503` (`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`) and the generic family management actions (cantonment, liaison, restricted deployment, containment, and dispersal in `019_infantry_spawn_muster_board_effects.txt`) read `global.black_friday_price_event19_*_family_*` and `global.black_friday_price_infantry_spawn_family_management_cost_*` in their checks, payments, refunds, and cost texts, and credit one achievement family per payment.
- Converted (agent decision D32): the eight paid incident options (`chaosx.nr19.301.a`, `302.b`, `303.c`, `308.a`, `309.a`, `310.a`, `311.b`, `312.b`), the four achievement combat trials, and the derivative claimant guard rally read `global.black_friday_price_infantry_spawn_incident_*`, `global.black_friday_price_infantry_spawn_achievement_combat_trial_cost_*`, and `global.black_friday_price_infantry_spawn_derivative_claimant_guard_army_experience` and credit one achievement family after paying. The claimant's demand terms keep their full price (D18).

The line list below predates the conversion.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 53.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/019_infantry_spawn_claimant_decisions.txt` | - | - | 44, 68, 122, 144, 169 |
| `common/decisions/019_infantry_spawn_decisions.txt` | - | - | 92, 116, 137, 181, 254, 283, 334, 401, 429, 462, 531, 552, 574, 596, 622, 640, 658, 676, 694, 716, 729, 742, 755, 768, 781, 794, 832, 869, 906, 943 |
| `common/decisions/019_infantry_spawn_derivative_decisions.txt` | - | - | 37, 62, 87, 112, 150, 173, 191, 206, 221, 244, 284, 317, 350, 384, 413, 442, 499, 521 |

#### Genocide crisis (custom costs; native costs converted)

Converted (agent decision D16): the Command Power, Army Experience, and Political Power payments of the 16 genocide crisis decisions read the sale price table in their requirements, payments, and cost texts. The three camp-system payments these decisions call stay with the Camps owner (see Camps below). The line list below predates the conversion.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 4.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/genocide_crisis_decisions.txt` | - | - | 64, 220, 870, 1068 |

## Other owners

These owners are outside the lead's active list and both conversion tranches. A rescan on 2026-10-05 found that every custom-cost decision in Events 001, 007, and 017 and in the Mengele decisions reads the sale through its bounded adapter, so their decision costs are converted; their paid event options are classified in the registry's BF-EVO rows (agent decision D26). The remaining owners here are `owner adoption pending` until the lead assigns them to an active engineer or a conversion tranche.

### Event 001 Communism Spread

Converted: all five custom-cost decisions read the sale through the BF-COM adapters.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 5.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/001_communism_spread_decisions.txt` | - | - | 10, 117, 193, 273, 319 |

### Event 007 Fury

Converted: all 17 custom-cost decisions read the sale through the BF-FUR adapters.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 17.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/007_fury_decisions.txt` | - | - | 31, 58, 92, 138, 166, 222, 243, 297, 332, 363, 396, 419, 444, 506, 574, 596, 661 |

### Event 017 Random Faction

Converted: all ten custom-cost decisions read the sale through the BF-RF adapters.

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 10.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/017_random_faction_decisions.txt` | - | - | 28, 84, 134, 192, 290, 340, 398, 452, 511, 611 |

### Event 024 Video Game in Sweden

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 19.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/024_video_game_in_sweden_decisions.txt` | - | - | 24, 58, 92, 144, 178, 211, 241, 277, 315, 346, 395, 429, 470, 515, 551, 579, 610, 673, 715 |

### Event 028 Asteroid Incoming

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 16.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/028_asteroid_incoming_decisions.txt` | - | - | 49, 164, 273, 368, 430, 491, 552, 609, 637, 667, 716, 808, 883, 971, 1045, 1123 |

### Event 032 Missiles

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 26.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/032_missiles_decisions.txt` | - | - | 78, 115, 146, 176, 205, 235, 275, 313, 351, 548, 587, 625, 675, 711, 791, 820, 847, 875, 900, 923, 948, 973, 995, 1017, 1043, 1079 |

### Fallout

Positive native costs: 12; dynamic native costs: 0; custom cost declarations: 41.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/fallout_consolidated_decisions.txt` | 45, 96, 169, 1492, 1719, 1751, 2508, 2531, 2562, 2622, 2692, 2833 | - | 319, 382, 432, 480, 530, 583, 632, 681, 728, 780, 830, 877, 932, 983, 1033, 1080, 1133, 1188, 1247, 1316, 1383, 1452, 1493, 1554, 1593, 1636, 1680, 1784, 1834, 1888, 1946, 2017, 2116, 2159, 2229, 2317, 2355, 2394, 2431, 2468, 2778 |

### Germany Mengele (custom costs; native costs converted)

Converted: the four custom-cost clone decisions read the sale through the BF-MEN adapters, and the native costs read the price table (D5) and credit Political Power (D27).

The uncommitted stale-completion refunds in `import_subjects_from_japanese_china`, `import_subjects_from_india`, and `import_subjects_from_africa` refund the ordinary `constant:germany_mengele_decision.import_*_subjects_cost`; when that work lands they must refund `global.black_friday_price_germany_mengele_decision_import_*_subjects_cost`, which is what the decision charged (agent decision D10).

Positive native costs: 0; dynamic native costs: 0; custom cost declarations: 4.

| File | Native positive cost lines | Dynamic native cost lines | Custom cost trigger lines |
| --- | --- | --- | --- |
| `common/decisions/germany_mengele_decisions.txt` | - | - | 455, 486, 517, 571 |
