# Event 26 native cost declaration inventory — 2026-10-03

Disposition: implemented declaration-discovery refresh; manual semantic coverage remains unresolved.
The acceptance basis is the parent prompt dated 2026-10-03, which records the original user goal of a full universal cost registry against the final commit.
The current worktree is evidence of declarations and call sites only; it does not establish design approval, working discounts, or universal coverage.
Event 26 implementation remains incomplete and default-disabled according to the parent; this refresh does not change that disposition.
Full scan window: 2026-10-03T05:18:11.9235070Z through 2026-10-03T05:18:37.7233668Z; detected concurrent source changes were refreshed through 2026-10-03T05:31:23.6952522Z.
Repository HEAD at the final targeted refresh: `5cb073ae0f4471f4a3330f8cdebb6d0b62a5c876`.
All 346 recorded file hashes and paths matched the final independent recheck at 2026-10-03T05:31:29.5310770Z.
These are worktree snapshots, not a final commit freeze; concurrent edits, especially the pending RSA owner patch, require a rescan before final reconciliation.
Mod root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Vanilla root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.

## Scan contract and classification

Every `*.txt` recursively beneath both `common\decisions` roots was scanned, including category files and files with no native cost declarations.
Comments and quoted strings were masked without moving line breaks; the exact assignment key `cost` was matched anywhere in active source, including inline declarations.
One-based original source lines are partitioned below into literal zero, numeric nonzero, and symbolic/unresolved values.
“Not literal zero” is a syntactic discovery class comprising numeric nonzero and symbolic values, not proof that a resolved constant or variable is positive.
For example, `012_africa_rsa_decisions.txt:179` uses `constant:africa_rsa_count.none`; it is symbolic here, and this pass does not infer its runtime value or audit the pending RSA adapter.
A literal zero describes only this declaration; the action can still consume resources in custom or effect-side paths.
Numeric nonzero retains signs; Vanilla `common\decisions\AST.txt:810` is `cost = -7`, so that row is not a proven positive purchase cost.
None of these classes claims a Black Friday discount, owner adapter, effective-load precedence, or engine inaccessibility.

| Source | Files scanned | Files with active native cost | Raw occurrences | Excluded comments/strings | Active declarations | Not literal zero | Literal zero | Numeric nonzero | Symbolic/unresolved |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Mod | 201 | 55 | 1316 | 0 | 1316 | 973 | 343 | 140 | 833 |
| Vanilla | 145 | 86 | 2955 | 52 | 2903 | 2516 | 387 | 2150 | 366 |

Mod has no excluded exact-key matches; Vanilla has 52 commented native-cost matches, listed separately below.
All 346 scanned paths are retained in the tables so zero-declaration files cannot disappear from discovery.
Each row records the SHA-256 of the same bytes used to count declarations; these hashes also identify the custom inventory's owner sources.
SHA-256 of the combined canonical source manifest: `aa74ae0af3bb85519ebe74ac603343271bd34cfe75fb4ee40cf482f4b929089a`.
Manifest serialization and the exact scan command are recorded in the [current declaration handoff](subagent_handoffs/2026-10-03_current_declaration_inventory.md).

## Mod exact occurrence and source-hash ledger

Paths are relative to the mod root.
A zero in the declaration-count column means no active exact `cost` assignment was discovered in that file; it does not mean the owner has no other payment surfaces.

| Owner/source path | Active declarations | Not literal zero | Literal-zero exact lines | Numeric-nonzero exact lines | Symbolic/unresolved exact lines | SHA-256 |
| --- | ---: | ---: | --- | --- | --- | --- |
| `common\decisions\001_communism_spread_decisions.txt` | 0 | 0 | — | — | — | `42f60da9cff89a1988abf02daa52c8374a78f9ca4bb68b03a35a59bcc7beb697` |
| `common\decisions\002_zombie_outbreak_decisions.txt` | 37 | 29 | `24, 73, 122, 171, 220, 269, 318, 367` | `424, 586, 745, 916, 1106, 1257, 1401, 2364, 2448, 2482, 2516, 2554, 2829, 2886, 2977` | `47, 96, 145, 194, 243, 292, 341, 396, 1539, 1685, 1839, 2008, 2191, 2609` | `c47e4a8cd30fa03cd02e4cb7914150432c35142702610e7988cb0de23d3a9014` |
| `common\decisions\003_holy_realm_decisions.txt` | 113 | 108 | `51, 64, 77, 90, 2649` | `103, 128, 178, 200, 227, 334, 365, 400, 914, 945, 977, 1013, 1193, 1224, 1260, 1291, 1324, 1399, 1616, 1661, 1699, 1731, 1776, 1826, 1879, 3060, 3096, 3129, 3159, 3191, 3227, 3265, 3302, 3341, 3375, 3412, 3447, 3483, 3521, 3547, 3578, 3604, 3640, 3665, 3699, 3736, 4231, 4256, 4283` | `250, 280, 306, 500, 544, 606, 633, 654, 702, 733, 776, 825, 1046, 1082, 1115, 1145, 1164, 1438, 1465, 1501, 1551, 1584, 1904, 1947, 1986, 2031, 2089, 2124, 2160, 2205, 2258, 2295, 2420, 2469, 2496, 2520, 2544, 2568, 2590, 2669, 2689, 2713, 2767, 2805, 2844, 2883, 2913, 2948, 2987, 3038, 3765, 3810, 3855, 3900, 3941, 3987, 4032, 4098, 4164` | `05c9b0485456c28c560d575e117e023dc0af61e82a23415231838065536a9ed4` |
| `common\decisions\005_soviet_collapse_decisions.txt` | 18 | 18 | — | — | `13458, 13490, 13522, 13592, 13650, 13679, 13759, 13786, 13816, 13844, 13895, 13949, 13997, 14036, 14078, 14108, 14147, 14169` | `c573bf40c72ed5a611bc823283e5d4b39541934fa47b8a2035362e7c497caafb` |
| `common\decisions\006_independence_wave_balkan_decisions.txt` | 0 | 0 | — | — | — | `4eb74fb2690187ee7d0c0160e49e0062adea5f427a814de7ea3107718dce65d7` |
| `common\decisions\006_independence_wave_bashkiria_mari_decisions.txt` | 0 | 0 | — | — | — | `f6d033b12f89f195a612c2abe66d4c2766d3d6b180480f6f00d74dc7fdc3255c` |
| `common\decisions\006_independence_wave_decisions.txt` | 3 | 0 | `959, 996, 1026` | — | — | `d874e03abddbab1c070c32980afea3634a336f2ca8ca4ac9d6e25ea0dfaa0a09` |
| `common\decisions\006_independence_wave_don_decisions.txt` | 0 | 0 | — | — | — | `8de0f0c80f037aad9cef3cea029e39f6565c2581b731b32ed53499c682d47280` |
| `common\decisions\006_independence_wave_far_eastern_decisions.txt` | 0 | 0 | — | — | — | `39083d15d317de4ca1d682f0d4a8075f2a90ab414dead6bb14ce24076aa34b31` |
| `common\decisions\006_independence_wave_form01_02_04_decisions.txt` | 0 | 0 | — | — | — | `90a0baafcfa47dfe831be6773191d61f76a414187e6d5091f1034618f3824365` |
| `common\decisions\006_independence_wave_form03_decisions.txt` | 0 | 0 | — | — | — | `1ad0931fe0d0926b6c435480620bc5b9c743f6041e3db4b7c2cbb934b80a37dd` |
| `common\decisions\006_independence_wave_form05_decisions.txt` | 0 | 0 | — | — | — | `e4c6a82b68756aab4d216df630ae3dabbb22eb19ddeaa23eea67bddfc2492a2a` |
| `common\decisions\006_independence_wave_form48_decisions.txt` | 0 | 0 | — | — | — | `49c36be76aefca2738ec3687087f2020381e49b74cb0476bde7b8c58aeeba295` |
| `common\decisions\006_independence_wave_formable_decisions.txt` | 0 | 0 | — | — | — | `1ca4ec780911e01a280fc392748218f5dac44b35f4e4fda6394282661f583f44` |
| `common\decisions\006_independence_wave_frontier_decisions.txt` | 0 | 0 | — | — | — | `c0f4c22714eb552f97d3e2c672a8a5f75a382a73bcf445af4fb84ce06bf6b493` |
| `common\decisions\006_independence_wave_iberian_decisions.txt` | 0 | 0 | — | — | — | `aa8f682027598e83cf07128f28528df87897f0b0cf53682f6f9a839023d003e9` |
| `common\decisions\006_independence_wave_iw043_iw058_decisions.txt` | 0 | 0 | — | — | — | `c6c1df3711f44269543fcc2d093a6f7f968bc2932aca113aa887663d371e13f6` |
| `common\decisions\006_independence_wave_iw093_iw098_decisions.txt` | 6 | 6 | — | — | `102, 160, 219, 699, 754, 810` | `16e0078faeee054062965957a5aed368bae4185b99da679715fe807912689a80` |
| `common\decisions\006_independence_wave_karelia_crimea_decisions.txt` | 0 | 0 | — | — | — | `5dba54952fe024724298a2a8054c6399cb94c77c3484da6ac0ede4968a004934` |
| `common\decisions\006_independence_wave_mediterranean_decisions.txt` | 0 | 0 | — | — | — | `0eed2c5419480a8edd91625a298cc27ef6c9ecb840fc9066f34f5c86dbc13f07` |
| `common\decisions\006_independence_wave_minor_overlay_decisions_registry.txt` | 0 | 0 | — | — | — | `f609418cba44a0882a71eba1d2cbced04a898c2176be91142b4eb1a914e3aa62` |
| `common\decisions\006_independence_wave_pacific_decisions.txt` | 0 | 0 | — | — | — | `435341426462bcba7ee9bc4caabce950dcbde09c63054db99bc771dc433c35d4` |
| `common\decisions\006_independence_wave_rhineland_bavaria_saar_decisions.txt` | 0 | 0 | — | — | — | `6f2b6d2d845f217248621133928cb89e442288b0e398a46d5275c60fd7fb1ad2` |
| `common\decisions\006_independence_wave_scotland_wales_decisions.txt` | 0 | 0 | — | — | — | `621e2c934358488b50a7f20b9ad7ce93152326ee633b11b365090359f5655cb6` |
| `common\decisions\006_independence_wave_shared_decisions.txt` | 0 | 0 | — | — | — | `4d065bde1aef2744c987a1e46f089e5398fd36c02993a1b35e7dc57f75b92d7d` |
| `common\decisions\006_independence_wave_siberian_decisions.txt` | 0 | 0 | — | — | — | `bd3e36c9023158478a3654f11e106e484ee8a270188a4cf0d39f95b716d82326` |
| `common\decisions\006_independence_wave_transcaucasus_decisions.txt` | 0 | 0 | — | — | — | `64ab4494402313ce70ac946e09a045016b00ecd5a3b4a48fe6c1d7e597f0cbf1` |
| `common\decisions\006_independence_wave_wallonia_frisia_decisions.txt` | 0 | 0 | — | — | — | `329b4bd985e13460024052564f82303c9ce68d5a41021c4b5052507dfc0e13ac` |
| `common\decisions\006_independence_wave_western_decisions.txt` | 0 | 0 | — | — | — | `da570f8ef1d328e9327d088c494204cf31a2ec6f32abc18c053731c872e98c38` |
| `common\decisions\007_fury_decisions.txt` | 0 | 0 | — | — | — | `3dc14d6c408880f561bcd5c552b98e980e2c63233610fce80f7077fc9e20b679` |
| `common\decisions\010_death_decisions.txt` | 3 | 0 | `477, 499, 1062` | — | — | `962c56c7516c3d0cf4fc0a7433b7a5a20102caec21539480a30f2c6e7f55253c` |
| `common\decisions\011_secret_alliance_decisions.txt` | 0 | 0 | — | — | — | `3f6d34e4d6224745c5988192923b5acbd2806e17d4955b74759956c179ee919a` |
| `common\decisions\012_africa_decisions.txt` | 204 | 60 | `14, 38, 50, 62, 82, 123, 140, 154, 165, 176, 187, 198, 209, 220, 231, 243, 255, 271, 283, 295, 307, 319, 385, 442, 643, 657, 669, 681, 693, 705, 717, 729, 741, 753, 764, 779, 791, 804, 817, 830, 843, 856, 867, 879, 890, 905, 917, 929, 941, 953, 965, 976, 988, 1000, 1012, 1027, 1039, 1051, 1063, 1075, 1086, 1098, 1110, 1121, 1133, 1148, 1160, 1172, 1184, 1196, 1208, 1220, 1232, 1244, 1256, 1271, 1283, 1295, 1307, 1319, 1331, 1343, 1354, 1369, 1381, 1393, 1405, 1416, 1427, 1439, 1450, 1465, 1477, 1491, 1505, 1548, 1563, 1579, 1593, 1607, 1621, 1633, 1649, 1669, 1683, 1725, 1743, 1755, 1767, 1779, 1791, 1803, 1815, 1827, 1839, 1995, 2018, 2030, 2042, 2054, 2066, 2078, 2090, 2102, 2114, 2332, 2356, 2374, 2395, 2489, 2503, 3233, 3248, 3263, 3278, 3293, 3308, 3323, 3340, 3356, 3372, 3398, 3428, 3468` | — | `108, 337, 362, 405, 611, 630, 1521, 1848, 1866, 1884, 1899, 1908, 2126, 2154, 2192, 2529, 2593, 2608, 2627, 2643, 2660, 2679, 2698, 2717, 2736, 2755, 2768, 2780, 2792, 2804, 2816, 2828, 2842, 2854, 2866, 2878, 2890, 2902, 2922, 2944, 2963, 2982, 3001, 3015, 3029, 3046, 3061, 3076, 3089, 3100, 3111, 3122, 3133, 3148, 3162, 3173, 3187, 3198, 3207, 3216` | `6bc1242a420249fecd9a74dc90a4e06bead0c3ad310ddf99489b7f9060912f22` |
| `common\decisions\012_africa_elephant_operations_decisions.txt` | 2 | 2 | — | — | `42, 135` | `3de3b78e332a6cb57b4988d07134930ec373ff6ce33e5e9f7608e96e57b5fa09` |
| `common\decisions\012_africa_gods_decisions.txt` | 36 | 0 | `98, 137, 166, 199, 235, 266, 292, 318, 345, 367, 398, 440, 461, 482, 503, 530, 550, 568, 586, 606, 629, 650, 671, 692, 713, 735, 758, 812, 855, 915, 946, 977, 1032, 1065, 1124, 1169` | — | — | `492b8e19e70c90052155d44ab68792262ec5c9b50483e209f199f378c966942b` |
| `common\decisions\012_africa_priority_member_decisions.txt` | 71 | 71 | — | — | `14, 29, 44, 57, 69, 87, 129, 145, 161, 177, 193, 209, 225, 241, 257, 274, 290, 306, 322, 338, 354, 370, 384, 401, 418, 435, 452, 469, 486, 503, 520, 537, 554, 571, 588, 605, 622, 639, 658, 674, 690, 706, 722, 738, 754, 770, 786, 803, 820, 836, 852, 869, 886, 902, 918, 934, 950, 966, 979, 995, 1012, 1028, 1044, 1060, 1076, 1092, 1108, 1121, 1137, 1153, 1169` | `1f59d0e93e6fc8b4826e93dcc983ebe6c343dcd73ede11fb2dabf284f13a28cb` |
| `common\decisions\012_africa_promoted_tiera_decisions.txt` | 20 | 20 | — | — | `12, 21, 30, 39, 48, 57, 66, 75, 84, 93, 102, 111, 120, 129, 138, 154, 176, 198, 225, 249` | `f1371bf1dd9b5a0bc511f1960f940305852926480c30d26465757a3eb51aa4d9` |
| `common\decisions\012_africa_rsa_decisions.txt` | 1 | 1 | — | — | `179` | `40283784e0d0ea091bd96c96c46f0155ec01e911091b2b20a0389ac5e1d696cc` |
| `common\decisions\013_natural_disasters_decisions.txt` | 0 | 0 | — | — | — | `c465c999e84e90c662329b954c3e2377361e958a8df2abcd6bd6dcf8a22cf882` |
| `common\decisions\014_cannibalism_decisions.txt` | 0 | 0 | — | — | — | `ad356db7875965262a049bcdc858499193ee5c2163dc1c736aa066c063d279d3` |
| `common\decisions\015_utopia_manifesto_decisions.txt` | 98 | 98 | — | — | `38, 95, 135, 176, 230, 282, 331, 368, 538, 581, 625, 669, 715, 797, 849, 911, 980, 1053, 1100, 1147, 1195, 1275, 1355, 1420, 1485, 1558, 1625, 1717, 1770, 1807, 1844, 1881, 1918, 1966, 2056, 2109, 2159, 2215, 2267, 2319, 2417, 2468, 2536, 2598, 2668, 2716, 2800, 2846, 2895, 2953, 3007, 3060, 3235, 3312, 3367, 3411, 3461, 3510, 3551, 3584, 3651, 3719, 3761, 3816, 3885, 3927, 3971, 4008, 4098, 4148, 4190, 4266, 4358, 4453, 4548, 4611, 4669, 4711, 4798, 4833, 4913, 4961, 5026, 5106, 5183, 5240, 5339, 5386, 5437, 5488, 5542, 5579, 5611, 5651, 5711, 5745, 5774, 5808` | `00b2f67494893cfc875a48b96404115beb61ec5ccd705af58eb657ed37ba6230` |
| `common\decisions\015_utopia_manifesto_evolution_consumption_decisions.txt` | 15 | 15 | — | — | `29, 62, 95, 145, 179, 213, 249, 282, 316, 351, 388, 421, 457, 491, 525` | `8309891d18c79e7ec186127eeaf76f21c616cdb351cd1b9786ad0b2bb3fd80b9` |
| `common\decisions\015_utopia_manifesto_prefire_evolution_decisions.txt` | 1 | 1 | — | — | `65` | `2e311fd1df8d6879123f6019459c2c5413f5fd7eb5dd704a6750a04ab51c7de6` |
| `common\decisions\016_alien_infantry_landing_decisions.txt` | 0 | 0 | — | — | — | `984be74d9d3d6a2e6d565d2e18114afa76ba8934011f58ad738e6f22ff7dff5d` |
| `common\decisions\016_brilliant_scientist_achievement_decisions.txt` | 6 | 6 | — | — | `33, 73, 113, 153, 190, 231` | `bc57569547fbcee1e2d4546351b08814fb70e4a75fc280862e529485a0ffec4c` |
| `common\decisions\016_brilliant_scientist_aftermath_decisions.txt` | 22 | 22 | — | — | `21, 38, 55, 74, 90, 115, 133, 149, 165, 187, 209, 227, 244, 265, 277, 289, 301, 313, 325, 337, 349, 361` | `2ff7d345d5a35cf331692e8af4baa3e001869960fa4a1bfa4cb26f7ed90ad4d5` |
| `common\decisions\016_brilliant_scientist_containment_decisions.txt` | 0 | 0 | — | — | — | `1aa246e942e85e89fdad60ad79c7db64dff1947e08215524f367af15aea8f7d1` |
| `common\decisions\016_brilliant_scientist_directorate_facilities.txt` | 6 | 6 | — | — | `35, 113, 212, 342, 458, 535` | `d114bf7a624448c8fd5462831794ce7e8a47a9725d4ac2790f34af08976a06a6` |
| `common\decisions\016_brilliant_scientist_directorate_foreign.txt` | 6 | 6 | — | — | `23, 63, 133, 227, 281, 333` | `569253c71f5aa9165bc465737d6f68e2034d7bd9098fbe65a7228fcaeed00a1f` |
| `common\decisions\016_brilliant_scientist_directorate_institutions.txt` | 21 | 21 | — | — | `28, 78, 130, 178, 232, 285, 331, 380, 432, 488, 537, 573, 693, 740, 786, 838, 891, 956, 1017, 1084, 1149` | `fc90189c192f7eb74de05933647df40ada504325e3d98501923d5e53d54ee1bf` |
| `common\decisions\016_brilliant_scientist_directorate_project_board.txt` | 91 | 91 | — | — | `156, 264, 305, 367, 469, 1047, 1104, 1161, 1218, 1275, 1332, 1389, 1446, 1503, 1560, 1617, 1674, 1731, 1788, 1845, 1902, 1959, 2016, 2073, 2130, 2187, 2244, 2301, 2358, 2415, 2472, 2529, 2584, 2639, 2694, 2749, 2804, 2859, 2914, 2969, 3024, 3079, 3134, 3189, 3244, 3299, 3354, 3409, 3464, 3519, 3750, 3790, 3830, 3870, 3913, 4105, 4173, 4241, 4309, 4377, 4445, 4513, 4581, 4649, 4717, 4785, 4853, 4921, 4989, 5057, 5112, 5161, 5210, 5259, 5308, 5357, 5406, 5455, 5504, 5553, 5602, 5651, 5700, 5749, 5798, 5842, 5884, 5926, 5968, 6010, 6052` | `ee129e541e275a4c48cf6fe375e8ae2833d85529e6ce5ef74b6707282b405293` |
| `common\decisions\016_brilliant_scientist_directorate_synthesis.txt` | 3 | 3 | — | — | `39, 135, 223` | `f9433cd4a0e3686bf026bf52203765b0b03c0cf87f55b6e98ae54f893053b76b` |
| `common\decisions\016_brilliant_scientist_evolution_missions.txt` | 0 | 0 | — | — | — | `4f19a1ef1f937235f87b869a11a988494f12553a35ff69516a5b1ca84dfd452f` |
| `common\decisions\016_brilliant_scientist_foreign_decisions.txt` | 11 | 11 | — | — | `27, 71, 98, 142, 186, 230, 274, 318, 345, 392, 436` | `eb163ae804104d01d68b2e2dfc4e76896fd6069812039e33e1a072f829052d62` |
| `common\decisions\016_brilliant_scientist_former_host_recovery_decisions.txt` | 4 | 4 | — | — | `34, 83, 124, 166` | `350a4f186a8347cffa327e660870b73932f33be431417107f387273632275fa0` |
| `common\decisions\016_brilliant_scientist_kruger_state_canonical_and_exotic_decisions.txt` | 2 | 2 | — | — | `25, 55` | `2f7ee5c6c7607e8c2d10adf9182be4cd52b9d8f85a56b777198c8cd78fde43db` |
| `common\decisions\016_brilliant_scientist_kruger_state_clone_machine_decisions.txt` | 23 | 22 | `86` | — | `30, 57, 139, 167, 249, 278, 292, 313, 330, 357, 379, 416, 439, 459, 473, 497, 525, 587, 604, 619, 662, 680` | `05a75c6dbd82a08e7a0353c3cc1c7f38a2a08fbe4293512e9f1e77e241935d3f` |
| `common\decisions\016_brilliant_scientist_kruger_state_foreign_integration_decisions.txt` | 13 | 13 | — | — | `24, 37, 58, 87, 119, 145, 178, 223, 270, 311, 342, 372, 393` | `2526feccdbdc1ffc91f9118d0d32944834af17861ea8ec0e32da99d069a3766f` |
| `common\decisions\016_brilliant_scientist_kruger_state_foundation_decisions.txt` | 28 | 28 | — | — | `23, 36, 58, 80, 102, 130, 169, 184, 199, 218, 232, 253, 286, 322, 349, 378, 405, 431, 447, 462, 482, 496, 536, 581, 600, 620, 643, 671` | `c6a30057e6094e7d46b24e53a0241486c0a29cd27ca801331104b6ede513a37c` |
| `common\decisions\016_brilliant_scientist_kruger_state_paleo_xeno_decisions.txt` | 15 | 15 | — | — | `34, 76, 107, 127, 159, 190, 223, 250, 286, 327, 369, 402, 420, 453, 488` | `10f6efe110bcdb027f705539efd84a66e519298d59ba0cd6008698cad0993029` |
| `common\decisions\016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt` | 18 | 18 | — | — | `23, 46, 74, 106, 131, 159, 230, 257, 287, 308, 323, 340, 371, 440, 528, 558, 573, 595` | `3abba24b06b940e8a14f77671b067fd1cde7070c2aa1aba0151336cccd6887ac` |
| `common\decisions\016_brilliant_scientist_kruger_state_safeguard_decisions.txt` | 9 | 9 | — | — | `22, 40, 59, 79, 96, 116, 173, 250, 309` | `3df511296b08708f18307821e8117b3e6d479cb64ff5d3341a0401161e3f5745` |
| `common\decisions\016_brilliant_scientist_kruger_state_terminal_decisions.txt` | 15 | 15 | — | — | `41, 80, 104, 126, 146, 165, 185, 215, 253, 286, 331, 363, 389, 425, 479` | `e5d24548df4cbe01f25a63a4528b65ebc2935274409ff4a098c3b78488bb65f3` |
| `common\decisions\016_brilliant_scientist_portal_containment_decisions.txt` | 0 | 0 | — | — | — | `2b941291fcbc71a882db7306dd40c4248c241bcba27e9e7d44b95f06ed89e0d6` |
| `common\decisions\016_brilliant_scientist_technology_actions.txt` | 0 | 0 | — | — | — | `13231c8d4cdcbac3a57548c646bd6fedd2650ffc5df730524fa5a38ade9608a1` |
| `common\decisions\016_dhrondan_contact_decisions.txt` | 3 | 3 | — | — | `34, 68, 93` | `c0f712f2d608ae43032ff2d92bc6bb07e5ba847b7e3a0491439dd15a808f6a3c` |
| `common\decisions\016_dhrondan_country_decisions.txt` | 5 | 5 | — | — | `33, 95, 155, 198, 241` | `542b7d01a0bfa06d57db719ea70c728062a92cca5ba85dc463e787700ab29071` |
| `common\decisions\016_mengele_alien_arms_stage_decisions.txt` | 0 | 0 | — | — | — | `4649dc8e739aa21cf6ce399fab9206e42600026b5e4add890e5fdbc2bbe6fb4b` |
| `common\decisions\016_mengele_biological_stage_decisions.txt` | 0 | 0 | — | — | — | `e8b7f4a0ed00257ec4f31b7bcc6e5a83a8c384a05a59c5a0ffb430bc86c28cbc` |
| `common\decisions\016_mengele_biomedical_prototype_decision.txt` | 0 | 0 | — | — | — | `bc5a679033701b055d455a367f45c49c0606129ff2b1693bb85944a911c9693d` |
| `common\decisions\016_mengele_cloning_stage_decisions.txt` | 0 | 0 | — | — | — | `d67cfef2a063dc1258fc0c6cc0858133cc30d009eb9cdc751db80d1245edf2c7` |
| `common\decisions\016_mengele_computation_incident_decisions.txt` | 0 | 0 | — | — | — | `19beeaa7b17196bcd37a50e4aacb41909da7d3525a1994d62b96070b31cef988` |
| `common\decisions\016_mengele_computation_stage_decisions.txt` | 0 | 0 | — | — | — | `4da2b0997e7a2c1f29a3f11b0884370e381fb2a57984745e704e90be4f6859f6` |
| `common\decisions\016_mengele_conventional_incident_decisions.txt` | 0 | 0 | — | — | — | `b59274d034ef9a107b5673ef115362ebdd5b7e314c2da257509ed25cb21f9bc4` |
| `common\decisions\016_mengele_conventional_stage_decisions.txt` | 0 | 0 | — | — | — | `0f90282ff26709bd050db5d6343fe199376000a8525613c3366974385faad584` |
| `common\decisions\016_mengele_materials_stage_decisions.txt` | 0 | 0 | — | — | — | `66078e7acaf6a2912dcd88fc3c2e19f4f7a8f9e86036989564bc7cf91fff5323` |
| `common\decisions\016_mengele_paleogenetics_stage_decisions.txt` | 0 | 0 | — | — | — | `ecef0940f6f591de5cc961e0ad4b49c96536cc970e28418408161b24dba7d973` |
| `common\decisions\016_mengele_remaining_conventional_prototype_decisions.txt` | 0 | 0 | — | — | — | `80b52209c7267f27db004b2f9ccc63023c14be76ecb9d4f2b317a0b4fb13c98f` |
| `common\decisions\016_mengele_robotics_stage_decisions.txt` | 0 | 0 | — | — | — | `18cb1ce3fc9a2a75b226a16ef256075a8de7d1dc0cc2f4582351d6de6bb12a3d` |
| `common\decisions\016_mengele_singularity_construction_decisions.txt` | 0 | 0 | — | — | — | `01231f46428bac9c6d6b2f5903cc7ef2432ed5cb83f5fb90373e2eb1f35d5571` |
| `common\decisions\016_mengele_singularity_incident_decisions.txt` | 0 | 0 | — | — | — | `fdd1b158e7e1c98feae17ec1082bfed2902120d69765e767521ac0063b753f39` |
| `common\decisions\016_mengele_singularity_stage_decisions.txt` | 0 | 0 | — | — | — | `d46a1f4cce5b407abdeef12cd455e5f7986c07c9b4b246106c2d9165468ed9cb` |
| `common\decisions\016_mengele_singularity_terminal_decisions.txt` | 0 | 0 | — | — | — | `7c3a3b27861c321f0b986d81bcf82e1cea0943e18921950aa4b0c857c8b86fc8` |
| `common\decisions\016_mengele_teleportation_stage_decisions.txt` | 0 | 0 | — | — | — | `3caf9a3d9a7d293974b1d13d206dec7e32738e9f19b4c1188572635c93b5e9c2` |
| `common\decisions\016_mengele_temporal_stage_decisions.txt` | 0 | 0 | — | — | — | `9508709b47cb96a7a28fb4afa1456e1d50977d0289e2f042c3f2356f7bb59372` |
| `common\decisions\016_mengele_xenobiological_synthesis_stage_decisions.txt` | 0 | 0 | — | — | — | `2af4a59676614084db49b7619d5b575c2e426c1f0c29f0bf4e1a84760c1de1b3` |
| `common\decisions\017_random_faction_decisions.txt` | 0 | 0 | — | — | — | `8ac0c80497d5989e2dc7427ab6ce4dbdfa5a6918b654d62f4b3700d270e59243` |
| `common\decisions\018_resources_found_decisions.txt` | 0 | 0 | — | — | — | `628d6e6ffb453ec3bfc156bc36e01f7cc5691de5d695c92c705819972ed4366c` |
| `common\decisions\019_infantry_spawn_claimant_decisions.txt` | 0 | 0 | — | — | — | `6ec6d7fe9ad0aed66a3d73f4b986cade80ccc4a725b857783dde5f73155596a5` |
| `common\decisions\019_infantry_spawn_decisions.txt` | 0 | 0 | — | — | — | `eeaf3696cf0886b7edfef060eaf87792896bab18e5cfb0350bd16ef4ff0e2aa3` |
| `common\decisions\019_infantry_spawn_derivative_decisions.txt` | 17 | 5 | `36, 61, 86, 111, 243, 283, 316, 349, 383, 412, 441, 498` | — | `136, 266, 550, 591, 600` | `3b8cde9695384f78b5f7b8dfc6bc34790bb9e88cb8e8ced8bfd80ef0ab2bf5b7` |
| `common\decisions\020_black_plague_rat_decisions.txt` | 0 | 0 | — | — | — | `34d2453d1cf0da370101cf0e18e8f25c2aefdc8118c126c9ac5c044f0a6e8796` |
| `common\decisions\020_black_plague_response_decisions.txt` | 0 | 0 | — | — | — | `413e75de56091f3fa1ce5424d9ac578d0de95038fabc9b53128e973c6e36dcec` |
| `common\decisions\020_black_plague_shared_response_decisions.txt` | 0 | 0 | — | — | — | `e17188abc99e3f8b23fb198b1b2218fd8e6443ee4b3449071e3a7a3d7607c229` |
| `common\decisions\020_black_plague_weaponization_decisions.txt` | 0 | 0 | — | — | — | `16f96c267d0a03cd0c713e9db6aa03dba6f09ecfaed4907fc7075b803216fa51` |
| `common\decisions\021_random_civil_war_decisions.txt` | 0 | 0 | — | — | — | `c928b1b802b4b2cccfa49913af9e288571099398a0000da1814b6e35cde81bc1` |
| `common\decisions\023_sov_nuclear_bombs_decisions.txt` | 68 | 0 | `20, 35, 50, 65, 85, 99, 130, 145, 173, 202, 253, 267, 286, 304, 325, 339, 353, 372, 386, 400, 414, 428, 450, 464, 493, 505, 519, 533, 547, 561, 575, 589, 603, 615, 630, 644, 658, 672, 690, 704, 716, 731, 745, 759, 777, 806, 820, 834, 848, 867, 881, 895, 909, 923, 937, 951, 965, 992, 1020, 1034, 1048, 1062, 1086, 1117, 1131, 1145, 1159, 1177` | — | — | `cebacc6aec4f7b5303f724369809c466a1efcf0c7258461432d364ebba420fd6` |
| `common\decisions\024_video_game_in_sweden_decisions.txt` | 0 | 0 | — | — | — | `dc1ea5273d6f22cfe8361c8d8ba176d344fc4ba98865f62a2145455d694f7f30` |
| `common\decisions\025_alien_technology_in_antarctica_aftermath_decisions.txt` | 0 | 0 | — | — | — | `1e7cdf6d0651972529df327b36c6459721a0dc85070efd3e9bc7e0b162232c3b` |
| `common\decisions\025_alien_technology_in_antarctica_decisions.txt` | 0 | 0 | — | — | — | `49867e7d4d2584787ab1afde756683c47fb1cc0f0b7870912c1e52eda696149b` |
| `common\decisions\025_alien_technology_in_antarctica_evolution_decisions.txt` | 0 | 0 | — | — | — | `0f17ebb9cce787e0308449f90e44ba9e48767d0dbb4ff2da65b9eaed8a7037c6` |
| `common\decisions\025_alien_technology_in_antarctica_missions.txt` | 0 | 0 | — | — | — | `a289957179752a175c0dcf1d3258523eb80901eb9b217161289ce9fdd0b8392c` |
| `common\decisions\025_antarctic_ufo_race_decisions.txt` | 3 | 3 | — | `10, 80, 160` | — | `05b1025a3c1cff318b21fb26467345187a5242ec9d9fc77751b2225ba4a62aa2` |
| `common\decisions\028_asteroid_incoming_decisions.txt` | 0 | 0 | — | — | — | `3caf81edcf7643695df0d1e1ed4545626ce50f3539c3a73d3a3cbbe7958eae26` |
| `common\decisions\029_riches_found_decisions.txt` | 0 | 0 | — | — | — | `1a485534b48a59d780a53c09642e4618659c69f8fcedda9f735cca412f886a14` |
| `common\decisions\031_random_terror_decisions.txt` | 0 | 0 | — | — | — | `fec966ee89d9e468f46fd049ec67b9272ea0bc9cc2364d15f02cbaff3c8c5933` |
| `common\decisions\031_random_terror_missions.txt` | 0 | 0 | — | — | — | `b24633fa4996fb2d25c44118c44a01f38b3c1c821dbcadf819fa71591813a71d` |
| `common\decisions\032_missiles_decisions.txt` | 0 | 0 | — | — | — | `faf772392b482ee0309ef317259ff6dd2520d3efa8a08f7415275841aca2e99f` |
| `common\decisions\032_missiles_missions.txt` | 0 | 0 | — | — | — | `a9d8a1f4c83d3b5450cda48540b8b69c38177c79ae0adacdfa61815ccd07f158` |
| `common\decisions\033_acid_rain_decisions.txt` | 0 | 0 | — | — | — | `31462e54c448eb46e947b3fe6dff93bfc145e5c4b2bf28ebeba527e91aed1863` |
| `common\decisions\035_great_depression_decisions.txt` | 0 | 0 | — | — | — | `2cb7b2538e5329772320a858ce7e3b06b5065e858fd4506c6f96dc75af77c185` |
| `common\decisions\039_murder_mystery_decisions.txt` | 0 | 0 | — | — | — | `56d53830b24e24fc66f6426963b4809c57ef58f893016a655870286b6a3caa5b` |
| `common\decisions\044_space_race_decisions.txt` | 21 | 21 | — | `15, 33, 73, 120, 167, 214, 261, 307, 353, 399, 445, 491, 537, 583, 629, 675, 721, 767, 813, 859, 900` | — | `1d10a837e8d1cc9c29d2161f9cb4e03de6d4f7fedbb8fe43088747b75b2cd228` |
| `common\decisions\049_mass_panic_decisions.txt` | 2 | 2 | — | `8, 84` | — | `6a3aa4dd56f127c20c74820b399715e30586babe2a43aa3ecca999a5436f20a0` |
| `common\decisions\079_the_master_decisions.txt` | 4 | 4 | — | `11, 94, 169, 212` | — | `cc73e005171e5ac27a877b4e01d381bd1e520e3c40afd253dfee2f01142e6cef` |
| `common\decisions\080_airship_decisions.txt` | 3 | 3 | — | `57, 79, 104` | — | `592bf540fb36897f6ecb47b8f91a613548db504fea8c1eb0945c04c2399af6f5` |
| `common\decisions\092_greenland_sale_decisions.txt` | 1 | 1 | — | `8` | — | `910941003c58a7900c1841e95a4ab8a6c6f6e6b38c0c95ebcbab93b2b3290d6b` |
| `common\decisions\biowarfare_disease_containment_decisions.txt` | 14 | 13 | `63` | — | `206, 382, 451, 488, 528, 567, 641, 681, 720, 794, 834, 873, 988` | `9b93eaa05bb328e7f64bee238dfbce5be1d1b95cb4ee241b9437ebb7621cd829` |
| `common\decisions\camp_administration_civil_decisions.txt` | 0 | 0 | — | — | — | `592fee36aa959f182dfbc50e40365db8367a96b384fbfd7f5a8215a2c737c361` |
| `common\decisions\camp_administration_country_decisions.txt` | 10 | 0 | `29, 42, 56, 64, 74, 88, 96, 106, 120, 128` | — | — | `8c4183bf840b142396fec56c0c01c757dd07c63f5a27a8fe7fa6cea878906b9a` |
| `common\decisions\camp_repression_colonial_country_decisions.txt` | 43 | 43 | — | — | `23, 70, 152, 247, 335, 365, 389, 420, 513, 548, 688, 775, 837, 892, 912, 993, 1025, 1057, 1150, 1189, 1219, 1300, 1347, 1380, 1414, 1449, 1516, 1663, 1744, 1803, 1844, 1877, 1924, 1951, 2015, 2144, 2251, 2318, 2355, 2387, 2421, 2476, 2505` | `a7a2956cdfc612bfa60b6b18207f3de7e02487835b9a45fa031de727b89527ab` |
| `common\decisions\camp_repression_generic_decisions.txt` | 16 | 6 | `15, 29, 42, 56, 303, 423, 686, 782, 819, 859` | — | `72, 235, 540, 582, 614, 883` | `fe36f6e1081c3f01c6bc7de548d2050aa6697860a827a060610bb9e476eec7e1` |
| `common\decisions\camp_repression_major_country_decisions.txt` | 29 | 29 | — | — | `42, 93, 179, 223, 261, 314, 358, 537, 585, 628, 659, 680, 717, 775, 805, 831, 873, 912, 937, 962, 1119, 1180, 1222, 1244, 1268, 1309, 1332, 1395, 1430` | `0a5fe8c6b52f7137f037077c91804115cb07f6d4eae74c077a8d8fafda34a016` |
| `common\decisions\categories\001_communism_spread_categories.txt` | 0 | 0 | — | — | — | `c77762c5045151e8e7aa4b4265ecec1f38c6540bb3eaaf742fe5058b04abd8c6` |
| `common\decisions\categories\002_zombie_outbreak_categories.txt` | 0 | 0 | — | — | — | `c028a2e6a2151f3f0876fbd043699c47c50408a223c5faad73e2a06a5d4d4324` |
| `common\decisions\categories\003_holy_realm_categories.txt` | 0 | 0 | — | — | — | `88ab02d4e66e00d3ccdb23c0e03525ddf19137ba979cd4bfa0d4b99ff9445150` |
| `common\decisions\categories\005_soviet_collapse_categories.txt` | 0 | 0 | — | — | — | `f42fd3b822d6aed5152961b4a7c158ef91cb254cf3afb5a6548b0902189803aa` |
| `common\decisions\categories\006_independence_wave_categories.txt` | 0 | 0 | — | — | — | `48f12fc11788641a76dfa0248deefb604c47f84414f97be09a9158d03eae48d7` |
| `common\decisions\categories\007_fury_categories.txt` | 0 | 0 | — | — | — | `1a8d33a7f6e434f13e1d6aac20e652c20df1b4320d94aeed4362591394a3e5c9` |
| `common\decisions\categories\010_death_categories.txt` | 0 | 0 | — | — | — | `5c02b9a6e6f453b15d78ac910e712d46703da599e11eb95edd45f65baca5b80d` |
| `common\decisions\categories\011_secret_alliance_categories.txt` | 0 | 0 | — | — | — | `e3270d441f29bcfea8260474b2854b95d166db3beb5f349eadcbfa782d365514` |
| `common\decisions\categories\012_africa_categories.txt` | 0 | 0 | — | — | — | `8323f9ffaaca58efcd837fef774e8918126f3dcff8d7580a99dcaf2aa97506a2` |
| `common\decisions\categories\012_africa_elephant_operations_categories.txt` | 0 | 0 | — | — | — | `a507a95e0415b9fcfd198b25ed842d66701507036d23e528d6841631b609ec30` |
| `common\decisions\categories\012_africa_gods_categories.txt` | 0 | 0 | — | — | — | `636c7953e75ef456e2e05e2fffd5806c35a6abe9392019029e2ac6cf0613bbc0` |
| `common\decisions\categories\012_africa_priority_member_categories.txt` | 0 | 0 | — | — | — | `7de01b88e798ee9d1f5586a2b400a1c246b45ab4f948d989fc36bda68841f01d` |
| `common\decisions\categories\012_africa_rsa_categories.txt` | 0 | 0 | — | — | — | `9e23c2d19148a1d6c50d8cb45c14158c87763c0b7d3d0c3f7e061f4e1ce8c582` |
| `common\decisions\categories\013_natural_disasters_categories.txt` | 0 | 0 | — | — | — | `c496f4529e225f1624576d45eab730e897d47da1a64c00fed841e4c067f4d185` |
| `common\decisions\categories\014_cannibalism_categories.txt` | 0 | 0 | — | — | — | `11b87433cc95344a96b6bfbf9612e751f28912fb9030613e3cc3f583cd56a9c6` |
| `common\decisions\categories\015_utopia_manifesto_categories.txt` | 0 | 0 | — | — | — | `4561772167030cf56681d160fcb166d27870e45871a5932ab5c6ff8342ae0844` |
| `common\decisions\categories\016_alien_infantry_landing_category.txt` | 0 | 0 | — | — | — | `4bf119ace5b7918e2267e9f49f46c2f45f83b2671bd4d1aef44e8be80ba12f77` |
| `common\decisions\categories\016_brilliant_scientist_achievement_categories.txt` | 0 | 0 | — | — | — | `13de07b94eb549aaf1d02481444263a8d06576f93b7a4d0963b5c270a3cce8f6` |
| `common\decisions\categories\016_brilliant_scientist_aftermath_categories.txt` | 0 | 0 | — | — | — | `68fd5982da0e8394a66c734e367593c53b7057d046f66dcea151f964aa46aa92` |
| `common\decisions\categories\016_brilliant_scientist_directorate_categories.txt` | 0 | 0 | — | — | — | `ffa06a83e960ea7b949d3f10f0ee1ed00a930352d502155064fc9c4f0529dde2` |
| `common\decisions\categories\016_brilliant_scientist_foreign_categories.txt` | 0 | 0 | — | — | — | `67dc3c71b89e32a56060afa354d20c62595e73eeac44c02d1b7bd4729ef98b13` |
| `common\decisions\categories\016_brilliant_scientist_kruger_state_categories.txt` | 0 | 0 | — | — | — | `38a679639baa7e254a6a7281c0d4ac729cca1a99ad284ef833b31ad19caa9b06` |
| `common\decisions\categories\016_brilliant_scientist_raid_lifecycle_categories.txt` | 0 | 0 | — | — | — | `cb22f1a6c6e0dde8dfe7e2af6e198aed2724cd8fdb88eb47e408b56d9c07e2a5` |
| `common\decisions\categories\016_brilliant_scientist_recovery_categories.txt` | 0 | 0 | — | — | — | `f99e07853b7790c6d8dd4be079711712f7ab87942c392a77dd70ccc2836b29bd` |
| `common\decisions\categories\016_conventional_technology_categories.txt` | 0 | 0 | — | — | — | `0681b66c2a5caaf62e84a01f1999da775625d9252835320b7b40458bf9db3092` |
| `common\decisions\categories\016_dhrondan_contact_category.txt` | 0 | 0 | — | — | — | `7d90082fd4b3737ca43c5b8edad13ca6dc69ad69041c0d8747887e3eb426d9c4` |
| `common\decisions\categories\016_dhrondan_country_categories.txt` | 0 | 0 | — | — | — | `189c7ed4dea843a1f57685adc9f4d92653e3d8c5fdd3c242b61dd574704988f5` |
| `common\decisions\categories\017_random_faction_categories.txt` | 0 | 0 | — | — | — | `ef550cdb18da8f43f7dbd3f8ae93e4e0b46efc335c8376c6586b13b12d0afdcc` |
| `common\decisions\categories\018_resources_found_categories.txt` | 0 | 0 | — | — | — | `0444ae01c50cc41d548828da476025b75d156f5f82c6dba66d6b25309912dd9a` |
| `common\decisions\categories\019_infantry_spawn_claimant_categories.txt` | 0 | 0 | — | — | — | `f1b277212cee65983c5a0c623d70e26cb66b0023a77e697049128ee30be5d394` |
| `common\decisions\categories\019_infantry_spawn_decision_categories.txt` | 0 | 0 | — | — | — | `c2e57c7bd0804a2c295a7673da7f36acf0445baa9c5222deb0660be1288e5e5d` |
| `common\decisions\categories\019_infantry_spawn_derivative_decision_categories.txt` | 0 | 0 | — | — | — | `c14ff4e5e71e9188f48c69ed1affd759bd6bd534b4e7476b15529e0f70fe6862` |
| `common\decisions\categories\020_black_plague_rat_categories.txt` | 0 | 0 | — | — | — | `d7730977be439fa2d8d128947e56cba767dae6f1dd1ef1384bfcda890a819240` |
| `common\decisions\categories\020_black_plague_response_categories.txt` | 0 | 0 | — | — | — | `2d738e5b90b52c63d79f627ff5d7e9fa01beb2b03a4c9c6c818d56a638800f0d` |
| `common\decisions\categories\021_random_civil_war_categories.txt` | 0 | 0 | — | — | — | `b15a843a7d6797b2769feb6a765bb1227347bf9985eba40807cedf06190766e7` |
| `common\decisions\categories\023_sov_nuclear_bombs_categories.txt` | 0 | 0 | — | — | — | `73e522e12687d2e0d0c62450806930e0bed033f08ea0f827e55e5e9e4882f011` |
| `common\decisions\categories\024_video_game_in_sweden_categories.txt` | 0 | 0 | — | — | — | `12778be8725534f1872a568f137f079f2f7f69e3f8d775e2c89653991ddac68b` |
| `common\decisions\categories\025_alien_technology_in_antarctica_categories.txt` | 0 | 0 | — | — | — | `8620cebe17aee46dd8ebf17711454b2d505db685512237547911a7cab7f6680d` |
| `common\decisions\categories\025_antarctic_ufo_race_categories.txt` | 0 | 0 | — | — | — | `4cc91c2b33da2d9d0d4ba858532160065ca1ff6407d9077b8c772144c5e4902a` |
| `common\decisions\categories\028_asteroid_incoming_categories.txt` | 0 | 0 | — | — | — | `06d975c5524f424ef3cbab8dde07cabc55368e863696c440cc58e5c0d38da359` |
| `common\decisions\categories\029_riches_found_categories.txt` | 0 | 0 | — | — | — | `8979a051f6008d2c69a969d140268a306a1c825a22733fdc24e6796a3a623572` |
| `common\decisions\categories\031_random_terror_categories.txt` | 0 | 0 | — | — | — | `eb0f1a2bbbe38656e9b9b852521e40907ee4fe7b89c1b211782cb212d871387e` |
| `common\decisions\categories\032_missiles_categories.txt` | 0 | 0 | — | — | — | `ac7ed77ec98d57a653d4c4e341ab76845e2997fd2886663c63a1eb016ceddaf5` |
| `common\decisions\categories\033_acid_rain_categories.txt` | 0 | 0 | — | — | — | `fa9ebd20f67157126b0bcea1f162d38f0d6675a0bd92be693479f8073d3aeb7d` |
| `common\decisions\categories\035_great_depression_categories.txt` | 0 | 0 | — | — | — | `05470bb75eb34e4fa57a3203cd325a1c7c9372ca59ce999be0f735f522c84274` |
| `common\decisions\categories\039_murder_mystery_categories.txt` | 0 | 0 | — | — | — | `899b2d3b940b190478dcd8f1e96c70b4ad1f1f981fdbbb1c2319457b2d385ccc` |
| `common\decisions\categories\044_space_race_categories.txt` | 0 | 0 | — | — | — | `7ee74dfd51b5dcc07b66c5c3daeda0c4498c93dad9fa19905ab6116667eecd41` |
| `common\decisions\categories\049_mass_panic_categories.txt` | 0 | 0 | — | — | — | `fd540421be74f1f0b0aa133f99a03255487b1ade306335b1f2850d552927446e` |
| `common\decisions\categories\079_the_master_categories.txt` | 0 | 0 | — | — | — | `a1e49295fa970c72a448a4d647700034b34073271b3484b6076560a89330d806` |
| `common\decisions\categories\080_airship_categories.txt` | 0 | 0 | — | — | — | `7ead2bb4d16d86dc58f59a01071eaa9edef11b695d6e42b85ddceae0488e5d2d` |
| `common\decisions\categories\092_greenland_sale_categories.txt` | 0 | 0 | — | — | — | `db945fab467a3147f5875c1ef3584ee16bc527faa8b4a47faa568d7ebcb52c65` |
| `common\decisions\categories\biowarfare_disease_containment_categories.txt` | 0 | 0 | — | — | — | `a7a5de07e86d3470a751b9f4005de28dfc1a7fa01346409223aebe8744f6717a` |
| `common\decisions\categories\cbrn_diplomacy_categories.txt` | 0 | 0 | — | — | — | `c5971496130b6322731813286ee671bf69bd0cb447db4c6b0a0cf353ca29c632` |
| `common\decisions\categories\cbrn_doctrine_categories.txt` | 0 | 0 | — | — | — | `049f6269c3a96e2571bacbc746d14990ce45c05f5418b4d96bcc4b8ccbdd7ddd` |
| `common\decisions\categories\cbrn_occupation_categories.txt` | 0 | 0 | — | — | — | `7d91eab1a5a2c161cc3d13b0878cd07d7cc17e3788760562a4adb8fe631e4576` |
| `common\decisions\categories\cbrn_protection_categories.txt` | 0 | 0 | — | — | — | `16ee2b82c125c66d3b716760f1401da675a81a8769ab8065775f465db4366c8c` |
| `common\decisions\categories\chaosx_decisions_categories.txt` | 0 | 0 | — | — | — | `d430808c42e7c30c7ebed4afaf19745a3b0cc611a6cc6cf718a79222e3d9001b` |
| `common\decisions\categories\chaosx_test_country_debug_categories.txt` | 0 | 0 | — | — | — | `24bff08748ca5733b89c13dc50bc1d5c83c2022445f700c583dfbeb2052eb7c2` |
| `common\decisions\categories\condemnation_sanctions_categories.txt` | 0 | 0 | — | — | — | `cff5793fb34d371b44d831ca67e259e862065b9e729bc4d33867470b34c0e70d` |
| `common\decisions\categories\fallout_consolidated_categories.txt` | 0 | 0 | — | — | — | `77efce6bc457187f94a6843a0090822c13a366a5fb1f0cd4b672ea3a695b2f1f` |
| `common\decisions\categories\famine_decision_category.txt` | 0 | 0 | — | — | — | `57f18cad843ed6b82adf796486f3cf962f682f7ad4ee9b00e0971af5aabce270` |
| `common\decisions\categories\genocide_crisis_categories.txt` | 0 | 0 | — | — | — | `2bc3cd9c4eecd5432df9ff518c493d354f39c67600615b6b013acd858f6b1cd4` |
| `common\decisions\categories\germany_mengele_categories.txt` | 0 | 0 | — | — | — | `20b4fcb7d6715d44c496ab1f31371578fc79d38e158c98dc5bd499e8f8e523c5` |
| `common\decisions\categories\migration_decision_category.txt` | 0 | 0 | — | — | — | `43e1ee749e97ef952e9b6cbdd66339346970ac4f308e30ca17e9da6d4a6bf5fb` |
| `common\decisions\categories\zzz_chaosx_formable_state_puzzle_categories.txt` | 0 | 0 | — | — | — | `dcb4bec9d34cc4e0e667113d2eb0dd207bfd855de0ee40976dc0ccd5604b44d2` |
| `common\decisions\cbrn_diplomacy_decisions.txt` | 0 | 0 | — | — | — | `dac4e01914d5e6516abe46f13e334ce3bf87efefbb049a8524125a1550aa0442` |
| `common\decisions\cbrn_doctrine_decisions.txt` | 0 | 0 | — | — | — | `6559c3e67ff99f067368e20b228f989610dfdb4a64d92f69d8a54a6ee9a1940e` |
| `common\decisions\cbrn_occupation_decisions.txt` | 4 | 4 | — | — | `25, 58, 335, 382` | `94f8cd7b06c0f99b7093599c5184685c69e4650bcaad156dc1d301586193000e` |
| `common\decisions\cbrn_protection_decisions.txt` | 4 | 4 | — | — | `256, 295, 473, 494` | `3b3e5ecc396b094710d86c6896eaf4a7db15112fe861ea16386e7d1ae9da26fa` |
| `common\decisions\chaosx_decisions.txt` | 0 | 0 | — | — | — | `06a3113c8cd3bd7660e1e1015d3abb5ad3768d66f2e7992931698adf80428a99` |
| `common\decisions\chaosx_test_country_debug_decisions.txt` | 6 | 0 | `7, 17, 27, 41, 51, 66` | — | — | `fe1851a42ff2286ddd6e3bfd4d7c43522c5046f9b6ddfa0312a2f6bfbc3c2a4b` |
| `common\decisions\condemnation_sanctions_decisions.txt` | 36 | 0 | `13, 22, 43, 63, 83, 99, 129, 154, 177, 199, 219, 238, 259, 273, 286, 299, 313, 329, 348, 368, 379, 390, 399, 410, 421, 432, 445, 479, 513, 547, 581, 592, 616, 640, 664, 691` | — | — | `8fc4e3d2929f880afb32e5f9793f46c2ee94298a941117d321ee4fcce9986e52` |
| `common\decisions\fallout_consolidated_decisions.txt` | 12 | 12 | — | — | `45, 96, 169, 1492, 1719, 1751, 2508, 2531, 2562, 2622, 2692, 2833` | `33ffdca3ecc7224fdbfc62770f217e609634a42d3d9e0c79b5cb3d73426d1e47` |
| `common\decisions\famine_decisions.txt` | 0 | 0 | — | — | — | `52e84b51b6c9faf5827f3152613870e4ebbd65215edd35d70e913d18ba01dfaa` |
| `common\decisions\formable_nation_decisions.txt` | 42 | 42 | — | `2844, 2950, 3102, 3257, 3373, 3510, 3687, 3806, 3994, 4102, 4242, 4340, 4453, 5070, 5198, 5268, 5384, 5441, 5518, 5604, 5666, 5728, 5789, 5866, 5955, 6072, 6146, 6203, 6300, 6361, 6422, 6515, 9282, 13783, 13880, 15851, 16171, 16278, 16380, 16499, 16639, 16798` | — | `bb5c4d67cc573cdb589f6609d8da4751dcb183d746dc94e0844e67b0f6765836` |
| `common\decisions\genocide_crisis_decisions.txt` | 26 | 26 | — | — | `35, 63, 139, 193, 261, 301, 389, 418, 443, 466, 494, 520, 544, 567, 607, 630, 688, 731, 833, 948, 1009, 1131, 1189, 1233, 1264, 1294` | `610117369787dad95b345632a7120a67823b35cfd9384f28fb87663db133fef2` |
| `common\decisions\germany_mengele_decisions.txt` | 26 | 26 | — | — | `10, 30, 49, 69, 87, 105, 128, 186, 234, 280, 299, 316, 344, 365, 383, 404, 434, 545, 603, 627, 649, 671, 697, 719, 740, 758` | `c9c32f368baf263b76a013dee17508463ba330efb66ed55cf7343bd77c4e31b4` |
| `common\decisions\migration_decisions.txt` | 0 | 0 | — | — | — | `279487dc7f2fcef921f7294fd207ba8c1c33f871c652280ebb31d2d1fd2a3e8b` |

## Vanilla exact occurrence and source-hash ledger

Paths are relative to the installed Vanilla root.
A zero in the declaration-count column means no active exact `cost` assignment was discovered in that file; it does not mean the owner has no other payment surfaces.

| Owner/source path | Active declarations | Not literal zero | Literal-zero exact lines | Numeric-nonzero exact lines | Symbolic/unresolved exact lines | SHA-256 |
| --- | ---: | ---: | --- | --- | --- | --- |
| `common\decisions\_debug_decisions.txt` | 13 | 0 | `398, 447, 480, 506, 541, 571, 599, 626, 658, 691, 715, 746, 902` | — | — | `268b61da99d9ac5ba4f4cae94c99a34b84c4c935e707970a6211b17437f4a16b` |
| `common\decisions\_exiled_governments_decisions.txt` | 7 | 5 | `248, 600` | `9, 376, 418, 471, 539` | — | `6057199a9654485de804abda9f76dbf29f927ce66a569e86d78b11acc324623c` |
| `common\decisions\_generic_decisions.txt` | 34 | 27 | `2386, 2563, 2745, 2934, 3096, 3244, 3408` | `97, 152, 347, 392, 466, 521, 618, 677, 1250, 1370, 1467, 1544, 1611, 1638, 1667, 1770, 1996, 2048, 2111, 2174, 3479, 3519, 3558, 3599, 3642, 3737` | `1869` | `83cd276f8fd2c0c90470225c996d7afee7b8c08437289dd23d819a4a29edb187` |
| `common\decisions\aat_mio_decisions.txt` | 30 | 30 | — | `8, 108, 199, 258, 350, 409, 502, 600, 692, 786, 887, 984, 1089, 1190, 1292, 1385, 1482, 1576, 1634, 1694, 1754, 1815, 1874, 1932, 1992, 2050, 2109, 2169, 2228, 2286` | — | `91d65aea364959d1ea94c8f190fe081e545c67631ec7359753744cabc40a0521` |
| `common\decisions\AFG.txt` | 28 | 25 | `39, 114, 847` | `242, 286, 326, 375, 424, 587, 647, 699, 802, 902, 949, 998, 1080, 1217, 1298, 1396, 1477, 1570, 1650, 1782, 1857, 1914, 1971, 2025, 2095` | — | `dabc91c3f7fb1810d64d91d07147e827068d42540326ce10554a0752ee48d7a7` |
| `common\decisions\African_Union_decisions.txt` | 6 | 6 | — | `4, 59, 96, 181, 220, 271` | — | `6a535d5ec3dffc41131a24a2a6c035b86305f220e7c10913cbf4dfcdda2239ad` |
| `common\decisions\anti_japan_infiltration.txt` | 7 | 7 | — | `16, 87, 176, 265, 354, 443, 532` | — | `58004e13816d613913613643033d5d1fcfaf7fa14ad5c8ce261c92df3b7d923f` |
| `common\decisions\ARG.txt` | 17 | 17 | — | `31, 138, 232, 302, 396, 466, 560, 630, 724, 812, 885, 961, 1179, 1240, 1316, 1358, 1402` | — | `e96c151e3254343ffb98a4d69099bc375b375b0044fbdf14675a67cadacc47c6` |
| `common\decisions\AST.txt` | 46 | 44 | `313, 1259` | `12, 137, 198, 262, 402, 479, 560, 754, 810, 929, 1014, 1067, 1676, 1724, 1940, 2021, 2076, 2131, 2186, 2247, 2308, 2366, 2426, 2511, 2571, 2607, 2643, 2690, 2728, 2764, 2825, 2896, 3008, 3085, 3160, 3235, 3316, 3386, 3514, 3570, 3631, 3672, 3712` | `2481` | `aad50da745f5a93c5f7470e06ed990a49a5416c81810849c8a2312600e81f4f2` |
| `common\decisions\AUS.txt` | 28 | 28 | — | `75, 136, 216, 277, 343, 423, 653, 703, 753, 813, 864, 1354, 1516, 1640, 1767, 1893, 2018, 2238, 2403, 2523, 2634, 2732, 2803, 2876, 2971, 3040, 3107, 3180` | — | `619f5e7d922c7900c2cfe31b54dc37d32b7583dedae9f33336a430d753362ef0` |
| `common\decisions\BALTIC.txt` | 2 | 2 | — | `163, 460` | — | `b6eb2295b9637223fb8dbfe748b11bf13c4efceca6b4745858672613506ec81a` |
| `common\decisions\BEL.txt` | 28 | 27 | `37` | `95, 155, 215, 260, 332, 445, 511, 574, 637, 684, 731, 819, 903, 975, 1048, 1157, 1276, 1332, 1388, 1506, 1549, 1609, 1651, 1699, 1746, 1785, 1824` | — | `840deb91d637fd807747ab5c5027f2152e64f2481f227d1ead0754b98704567b` |
| `common\decisions\BOL.txt` | 5 | 5 | — | `47, 133, 219, 299, 351` | — | `21c4afc979c9ca86130e844c14d006525c87ad32cf80e2034fc55fbccd7da56c` |
| `common\decisions\BRA.txt` | 14 | 14 | — | `35, 155, 222, 569, 644, 709, 765, 857, 908, 985, 1050, 1137, 1226, 1348` | — | `f423ecfb63334886246d56ea27531eda48708194b246037f9ef9bdc29c1cba15` |
| `common\decisions\BUL.txt` | 112 | 110 | `7982, 8296` | `4197, 4243, 4362, 4419, 4464, 4602, 4677, 4805, 4876, 5034, 5488, 5556, 5668, 5775, 5836, 5900, 5949, 7892, 8038, 8127, 8210, 8358, 8416, 8465, 8583, 8676, 8847, 8937, 9002, 9086, 9153, 9201, 9237, 9275, 9327, 9421, 9523, 9592, 9658, 10017, 10066, 10172, 10333, 10407` | `57, 144, 248, 321, 382, 459, 551, 616, 673, 735, 819, 918, 988, 1054, 1114, 1179, 1232, 1277, 1340, 1425, 1498, 1571, 1657, 1734, 1810, 1886, 1984, 2056, 2120, 2185, 2264, 2392, 2507, 2627, 2690, 2745, 2789, 2833, 2899, 2963, 3027, 3091, 3172, 3232, 3281, 3330, 3396, 3455, 3501, 3547, 3606, 3687, 3768, 3845, 6071, 6220, 6387, 6579, 6768, 6969, 7146, 7277, 7408, 7542, 7672, 7790` | `6d9c565d637cbb340d46e024930493c25b90faf4b7e5493ab324e0e33e38ad7f` |
| `common\decisions\categories\00_decision_categories.txt` | 0 | 0 | — | — | — | `4fabf2151a0728b70f3a0cdaa11342aac0bb2e1bdce3811fad64e980f606eb39` |
| `common\decisions\categories\00_formable_categories.txt` | 0 | 0 | — | — | — | `c9b3da97dfbdef1fc871370017e4ce349f09aa6d9347c748c33d7e7916b03384` |
| `common\decisions\categories\AFG_decision_categories.txt` | 0 | 0 | — | — | — | `23c260202b090a45a02f0f83ed1bbed1f547c4c2db93bf8774ee08b672e51567` |
| `common\decisions\categories\African_Union_decision_categories.txt` | 0 | 0 | — | — | — | `5b5723ef9f1491abe4660b7994e93a0e306149f32668a34f043075fbf80d642f` |
| `common\decisions\categories\ARG_decision_categories.txt` | 0 | 0 | — | — | — | `8cd82cf71b4611abdbb018cd22f27fcd0491a84f2b350a4823804596d801d16f` |
| `common\decisions\categories\AST_decision_categories.txt` | 0 | 0 | — | — | — | `a90aa4b86ee00540b2c2865ee4a6703cbb4e0274ad959d7805c50da523ecc0db` |
| `common\decisions\categories\AUS_decision_categories.txt` | 0 | 0 | — | — | — | `a98451649437b3ad5d533909c0d093e89e6af338bba0a21455301cb4c3ee2ccf` |
| `common\decisions\categories\BALTIC_decision_categories.txt` | 0 | 0 | — | — | — | `453554c6ebe02baf47f7ead466d937631ba4cf8471ead4c73d13eccc9f664525` |
| `common\decisions\categories\BEL_decision_categories.txt` | 0 | 0 | — | — | — | `316e0c31e97af4a6cb83d0a3b9be981e03dd9d6b74146b5d06f4e0da80e953a5` |
| `common\decisions\categories\BOL_decision_categories.txt` | 0 | 0 | — | — | — | `2f7db321d843e7d3891e7ddb957fb5275b808312d8d2cc669e6106ba128d57c4` |
| `common\decisions\categories\BRA_decision_categories.txt` | 0 | 0 | — | — | — | `dd1361b9f1f3d45cf34256173d79217ee43fb1998b0d92dc72ce2f2031960a1d` |
| `common\decisions\categories\BUL_decision_categories.txt` | 0 | 0 | — | — | — | `d53a6a42a8158e6f5a67b1cfeb3575550edaa5983643cd154a67b076e6664848` |
| `common\decisions\categories\CHI_decision_categories.txt` | 0 | 0 | — | — | — | `11399e09873bda3d8261eefd610d0dd7659298f02c1382e35aa9326eaf827497` |
| `common\decisions\categories\CHL_decision_categories.txt` | 0 | 0 | — | — | — | `b144ef3b754f28b0aff1adbd5e3c03c6f8ed7eaadce81e40d683ce8b5030c04e` |
| `common\decisions\categories\COG_decision_categories.txt` | 0 | 0 | — | — | — | `e383802064feb61ef9ad9df6cc356bed6df09d0bc9b77f793389cff6bc975c10` |
| `common\decisions\categories\CZE_decision_categories.txt` | 0 | 0 | — | — | — | `b125024e394272695fb1b3e96620882184d8d9d49dfe600b09a6d7f0d71858ca` |
| `common\decisions\categories\DEN_decision_categories.txt` | 0 | 0 | — | — | — | `ffb0eb88ff971941c707ca353dbd3e1dd738b11c71439a292d9dcede3d7fa5eb` |
| `common\decisions\categories\ENG_decision_categories.txt` | 0 | 0 | — | — | — | `7f80d354486fa0e82514bab6dc3bdf7dd24dc75e52bbd207abc5819269f4d0ea` |
| `common\decisions\categories\ETH_decision_categories.txt` | 0 | 0 | — | — | — | `0082d1e27b1e90179da09f675b8a48517f6413892112d6ab03d932cc714670a6` |
| `common\decisions\categories\FIN_decision_categories.txt` | 0 | 0 | — | — | — | `438a210c0c8340a2765204616a9df0e7542c97787d17776c533d83405276d2d5` |
| `common\decisions\categories\FRA_decision_categories.txt` | 0 | 0 | — | — | — | `b20c050b6b7721d48a8abd1bab0a1a239263101d5e91a11f84895f6b36d394b4` |
| `common\decisions\categories\GER_decision_categories.txt` | 0 | 0 | — | — | — | `56bd48059e9b1f217e0186069bc230be7de55cd898b480e1b18d22e1b80e8bd1` |
| `common\decisions\categories\GRE_decision_categories.txt` | 0 | 0 | — | — | — | `3fef999fa2f9bb52257540c3aab58b6c1adfaf09ad67aaf6c0279ce3b94b424a` |
| `common\decisions\categories\GUAY_decision_categories.txt` | 0 | 0 | — | — | — | `d76fe7df995a835678160ce9a6fc934191e35276d477cc30c6aa30896b300a84` |
| `common\decisions\categories\HOL_decision_categories.txt` | 0 | 0 | — | — | — | `7f146f6b245eb22ccdcc0ec04b1894028947ed91d451220e29d1eb22918ae47b` |
| `common\decisions\categories\HUN_decision_categories.txt` | 0 | 0 | — | — | — | `8d7c8974d89e1b303486841e766953a0bc852f9bf6ebed80c6fb8de04dd31d9c` |
| `common\decisions\categories\ICE_decision_categories.txt` | 0 | 0 | — | — | — | `efcefa427d4c1c97f2a1125a581b44413a45856ad56de5b3e83297a840cef52a` |
| `common\decisions\categories\infiltration_decision_categories.txt` | 0 | 0 | — | — | — | `316ea07e46da704bacbec1208dce8350ccb61ae350245418f0a56c5129a9e764` |
| `common\decisions\categories\INS_decision_categories.txt` | 0 | 0 | — | — | — | `3c4d80423b166e3b92eb82b01f218377b2b2c76e84a7e694c93cbc01b0466350` |
| `common\decisions\categories\IRQ_decision_categories.txt` | 0 | 0 | — | — | — | `847b97dedf787bc6edc4871ceb666590ef1603d5871c4d946aed7de4fa7ed18d` |
| `common\decisions\categories\ITA_decision_categories.txt` | 0 | 0 | — | — | — | `acecee0cfe2c2c09520ea1ab6c717d4a893511f431dd283d6f40740379443a3c` |
| `common\decisions\categories\JAP_decision_categories.txt` | 0 | 0 | — | — | — | `3c508d52301dbe38daa56be67df6903d03453ce6a19efad720286ec7fe159f0b` |
| `common\decisions\categories\MAN_decision_categories.txt` | 0 | 0 | — | — | — | `43a871efaa8200c402dc9efa180ee0c46ebf480a543a5e061f156b7d932af016` |
| `common\decisions\categories\MEN_decision_categories.txt` | 0 | 0 | — | — | — | `41476d65dbde231ba2a68c676f5861febef66b2abd6e486b3a85421e629164e3` |
| `common\decisions\categories\MEX_decision_categories.txt` | 0 | 0 | — | — | — | `cc181e259ecb4694316f973e4d78b63d804b632e9c50e062d348b804f3ddec1c` |
| `common\decisions\categories\NOR_decision_categories.txt` | 0 | 0 | — | — | — | `51c1520686a38e97e67cedad0f752f14304a7edc441da848945a66db1eca899e` |
| `common\decisions\categories\NORDIC_decision_categories.txt` | 0 | 0 | — | — | — | `afb8986bd1d67233d09836cf84cb6cff19144baffb0c82347454ff9857747107` |
| `common\decisions\categories\PER_decision_categories.txt` | 0 | 0 | — | — | — | `b21b5a21651b47b751c8fc5cc356805aff6463c555e71cefa572aa1d0238fe02` |
| `common\decisions\categories\PHI_decision_categories.txt` | 0 | 0 | — | — | — | `49a982016a91db07a4dcb575f6f86b1ac0bbcac79149d4e58c568a5d288ae8f6` |
| `common\decisions\categories\POL_decision_categories.txt` | 0 | 0 | — | — | — | `54b58b6ad34da19d7da8451db2732b6fb467ec680de213252310c10620857701` |
| `common\decisions\categories\POR_decision_categories.txt` | 0 | 0 | — | — | — | `650e80fa0ce4ff7fbfbc982a80752ea1a54a7e73c72dfb9fdd80434fbe1a3ab7` |
| `common\decisions\categories\PRC_decision_categories.txt` | 0 | 0 | — | — | — | `03690a95e30defc09d1c293fa76d7ff28e84c0a23914c4af8488f641c980848b` |
| `common\decisions\categories\PRU_decision_categories.txt` | 0 | 0 | — | — | — | `a91341d116634f21f4156708e7a8785c79e2d4658854f4bb3e265d45d5775969` |
| `common\decisions\categories\RAJ_decision_categories.txt` | 0 | 0 | — | — | — | `9886b53ab8f19bdaf81a21261db38a04b9b678265d329d027c533d73c93dc105` |
| `common\decisions\categories\RAJ_GOE_decision_categories.txt` | 0 | 0 | — | — | — | `bfb5bc7f3c9d3e0757df033bd1ec025484c4071fdc51af82b98a416b9dc31dba` |
| `common\decisions\categories\ROM_decision_categories.txt` | 0 | 0 | — | — | — | `ced29d74adc16c27c714ee09afbfba8260d1236a545b90756474ddf8f5ee5277` |
| `common\decisions\categories\SIA_decision_categories.txt` | 0 | 0 | — | — | — | `41c1ff442a46bdc18ad06b3446c9cc4b894a0573c48d4e26a4cd2362b2748bbd` |
| `common\decisions\categories\SOV_decision_categories.txt` | 0 | 0 | — | — | — | `595fdcbce0f1aa8f7f52c558b308e000e8c646a33aa8e224ddd295646ca9d117` |
| `common\decisions\categories\SPR_decision_categories.txt` | 0 | 0 | — | — | — | `529663384d2654a9f8d538708a29ebbde57ff2a902a225f9b626592ed923e5a1` |
| `common\decisions\categories\SS_decision_categories.txt` | 0 | 0 | — | — | — | `9fd8166cf7cb9bc35fb7cba6b4b2d9719d711ccf259dacc8afa2672e6641557b` |
| `common\decisions\categories\SWE_decision_categories.txt` | 0 | 0 | — | — | — | `81859c8e5848f172d87c4bb7b43b5663496a0fe2146deb54080b319e16ac265f` |
| `common\decisions\categories\SWI_decision_categories.txt` | 0 | 0 | — | — | — | `0e396973cbb028158f3c8976e8626de04a69d3926f04a52a32b1668ce0574f49` |
| `common\decisions\categories\TOA_shared_decision_categories.txt` | 0 | 0 | — | — | — | `d196204ee2c8dd06c0d7ae217daa1b65d776eeba76685ce4c15276767652a820` |
| `common\decisions\categories\TUR_decision_categories.txt` | 0 | 0 | — | — | — | `865cf0d8d758e2fa319f63a2bbad8dc590f48e16f7a570aa1f8590a4fa52c7ba` |
| `common\decisions\categories\USA_decision_categories.txt` | 0 | 0 | — | — | — | `9a45bde14096873a96424dbf19097dbec55b48e5e7c85f46e2caca491582e79f` |
| `common\decisions\categories\VEN_decision_categories.txt` | 0 | 0 | — | — | — | `8e24e62b76a45d9d39f18bebe68c0b1b898ef35c66f22f00dcbe8f9f0119724b` |
| `common\decisions\categories\YUG_decision_categories.txt` | 0 | 0 | — | — | — | `48362c431538ec83774ca2ffde193947daa0d1c6a90c25bf9a0f25c575d10d50` |
| `common\decisions\CHI_decisions.txt` | 112 | 105 | `290, 370, 5717, 5849, 5892, 5980, 9830` | `120, 212, 430, 465, 526, 617, 739, 821, 904, 987, 1070, 1153, 1236, 1319, 1401, 1484, 1567, 1649, 1732, 1814, 1897, 1979, 2061, 2143, 2225, 2307, 2373, 2820, 2887, 2960, 3668, 3737, 3881, 4011, 4093, 4160, 4189, 4284, 4430, 4539, 4729, 4910, 5107, 5347, 6078, 6149, 6259, 6661, 6724, 6787, 6850, 6913, 6976, 7039, 7102, 7165, 7228, 7291, 7354, 7417, 7480, 7543, 7606, 7688, 7733, 9422, 9575, 9606, 9674, 9710, 9751, 9816, 9935, 9991, 10033, 10213, 10289, 10339, 10386, 10685, 10755, 10833, 11146, 11224, 11668, 11718, 11767, 12384` | `3058, 3112, 3185, 3239, 3302, 3365, 3428, 3491, 3554, 3617, 9229, 9363, 10479, 10590, 10910, 11937, 12239` | `efcec834a71901a5da66eef97f8b817d1b7299c36f16e48893ff9f3918039068` |
| `common\decisions\CHI_warlord_decisions.txt` | 24 | 19 | `128, 203, 278, 985, 1041` | `38, 93, 168, 243, 318, 499, 615, 652, 689, 721, 769, 908, 934, 1101, 1135, 1169, 1202, 1240` | `852` | `3cd0a8a5e2060cde0f1435dac50094d6d77773fbce182e567c33935a70f79a4e` |
| `common\decisions\CHL.txt` | 70 | 70 | — | `39, 112, 184, 254, 318, 378, 457, 518, 579, 631, 700, 748, 831, 1354, 1441, 1526, 1628, 1737, 1833, 1912, 1971, 2031, 2090, 2511, 2592, 2696, 2796, 2881, 2955, 3025, 3259, 3349, 3442, 3534, 4082, 4157, 4288, 4463, 4614, 4752, 4963, 5236, 5444, 5636, 5867, 6098, 6254, 6405, 6611, 6865, 7245, 7570, 7845, 8225, 8923, 9206, 9275, 9356, 9437, 9518, 9610, 9702, 9822, 9912, 10100, 10325, 10507, 10691, 10957, 11042` | — | `a84ab8f3dcc8921208ecb401054088b3543eeb2b347f63b3be204308e699070d` |
| `common\decisions\COG.txt` | 34 | 34 | — | `36, 424, 487, 547, 621, 691, 768, 839, 912, 981, 1041, 1127, 1186, 1256, 1319, 1397, 1500, 1615, 1695, 1813, 1885, 1959, 2056, 2203, 2296, 2374, 2466, 2679, 2748, 2812, 2899, 2973, 3046, 3136` | — | `7dece4d71fa9ba1233d1983d1d82ab9b1ebaf007c2ebc64b4eba36ef99082885` |
| `common\decisions\CZE.txt` | 21 | 20 | `3499` | `1396, 1742, 1795, 1918, 1993, 2021, 2078, 2339, 2375, 2413, 2838, 6659, 6679, 6723, 7088, 7127` | `2707, 2960, 3084, 3343` | `11417830f663fe2db178fca27606a20d5fe4533822941b6a31e2bc4f7855a81b` |
| `common\decisions\DEN.txt` | 99 | 85 | `259, 3560, 3705, 4535, 4597, 5670, 5810, 6053, 6154, 6239, 6322, 7235, 7739, 7818` | `286, 399, 3807, 3877, 3924, 4002, 4074, 4158, 4200, 4241, 4286, 4342, 4384, 4430, 4488, 6708, 6797, 6886, 6975, 7335, 7417, 7481, 7585, 7697` | `481, 528, 596, 654, 757, 809, 862, 899, 932, 985, 1068, 1125, 1175, 1229, 1284, 1321, 1687, 1778, 1882, 2007, 2114, 2220, 2313, 2429, 2518, 2656, 2754, 2830, 2929, 3047, 3161, 3240, 3355, 3434, 3612, 3767, 4665, 4719, 4773, 4827, 4881, 4935, 4989, 5043, 5108, 5167, 5226, 5278, 5334, 5387, 5438, 5489, 5540, 6448, 6500, 6552, 6604, 7017, 7059, 7102, 7144` | `97caa478f153c616fa4868477d64df35b8296869ee9a34e49daf00d7d9a47ee2` |
| `common\decisions\DOD_hungary.txt` | 3 | 1 | `66, 109` | `17` | — | `d682361712e5f277c5f2b35e96f5ef1f80220970455d3ff10616645003e41a17` |
| `common\decisions\ENG.txt` | 108 | 108 | — | `52, 243, 282, 355, 428, 501, 574, 647, 720, 793, 866, 939, 1012, 1085, 1158, 1231, 1304, 1377, 1450, 1523, 1590, 1624, 1699, 1803, 1847, 1887, 1929, 1980, 2018, 2084, 2170, 2241, 2319, 2466, 2597, 2702, 2847, 2976, 3095, 3258, 3387, 3506, 3665, 3794, 4285, 4385, 4485, 4585, 4686, 4787, 4888, 4989, 5090, 5191, 5292, 5393, 5494, 5595, 5696, 5875, 6026, 6206, 6378, 6550, 6722, 6874, 7035, 7426, 7512, 7594, 7657, 7712, 7793, 7867, 7925, 8014, 8131, 8242, 8335, 8390, 8472, 8547, 8606, 8659, 8739, 8812, 8869, 8975, 9006, 9037, 9069, 9110, 9190, 9253, 9308, 9366, 9418, 9474, 9876, 9928, 10037, 10093, 10267` | `7163, 7217, 7254, 7291, 7328` | `83351419122bbc4f4a7fa693dbe7658396c1781b5aea28b5d100a0dd3b8d1fef` |
| `common\decisions\EST.txt` | 5 | 5 | — | `393, 437, 551, 650, 758` | — | `7842932556a53819211ac6832d76cc526348d12cdd00fc3673f7a71212445777` |
| `common\decisions\ETH.txt` | 56 | 54 | `669, 723` | `78, 143, 286, 316, 793, 843, 893, 943, 1308, 1432, 1659, 1726, 1778, 1838, 1886, 1939, 2145, 2244, 2328, 2404, 2452, 2491, 2531, 2571, 2614, 2687, 2735, 2783, 2843, 2916, 2972, 3006, 3042, 3105, 3160, 3261, 3336, 3377, 3470, 3520, 3552, 3584, 3617, 3649, 3681, 3714, 3747, 3780, 3817, 3853, 3989, 4061, 4129, 4208` | — | `a50f6aa755cf6dd619957e8ef73c196fe8a422b261a2805789426f43a373504f` |
| `common\decisions\FIN.txt` | 34 | 34 | — | `566, 1323, 1382, 1423, 1641, 1693, 1738, 1793, 1847, 1896, 1950, 1994, 2035, 2077, 2119, 2163, 2320, 2560, 2839, 3471, 3521, 3554, 3608, 3795` | `1259, 1473, 1551, 1589, 2218, 2269, 3035, 3097, 3266, 3328` | `2e2c580c5e54b75444199f3b3a0ffc4b27a2448b07e6557e35d6e2adfb5d2aa9` |
| `common\decisions\foreign_influence.txt` | 5 | 4 | `490` | `238, 296, 366, 436` | — | `046931f00256312f2a99f9c65aa6516d4661fbcaca3601c4df6e9b5ddf29782b` |
| `common\decisions\formable_nation_decisions.txt` | 42 | 42 | — | `3079, 3185, 3337, 3492, 3608, 3745, 3922, 4041, 4229, 4337, 4477, 4575, 4688, 5318, 5446, 5516, 5632, 5689, 5766, 5852, 5914, 5976, 6037, 6114, 6203, 6320, 6394, 6451, 6548, 6609, 6670, 6763, 9538, 14073, 14170, 16448, 16768, 16875, 16977, 17096, 17236, 17395` | — | `42dc38948a47ad7ce609847b94c1e5ceec460ad52b470d22e779323bf09eb4ce` |
| `common\decisions\FRA.txt` | 50 | 38 | `151, 305, 341, 352, 362, 881, 925, 972, 1026, 1097, 1156, 1753` | `472, 521, 569, 667, 735, 818, 857, 946, 1000, 1067, 1117, 1285, 1305, 1374, 1428, 1477, 1532, 1585, 1637, 1656, 1687, 1719, 1822, 1846, 1891, 1918, 2076, 2122, 2144, 2315, 2353, 2377, 2543, 2587, 2610, 2781, 2818, 2848` | — | `19422e278c26a662e4dbd2996d60e77ac04bf03af8d19db4b7d2b6b445a7376c` |
| `common\decisions\GER.txt` | 148 | 144 | `174, 13153, 13537, 13595` | `319, 434, 1115, 1166, 1216, 1270, 1319, 1373, 1424, 1490, 3233, 3449, 3575, 3737, 3905, 4108, 4367, 4536, 4643, 4788, 5018, 5308, 5456, 5489, 5758, 5849, 5986, 6113, 6179, 6338, 6442, 6691, 6941, 7125, 7280, 7454, 7598, 7747, 7830, 8065, 8486, 8651, 8901, 9174, 9499, 9840, 10001, 10169, 10318, 10447, 10671, 10893, 11054, 11390, 12047, 12488, 12727, 12765, 12811, 12838, 12879, 12924, 12968, 13089, 13188, 13313, 13695, 13809, 13880, 13992, 14063, 14132, 14207, 14293, 14378, 14459, 14573, 14645, 14715, 14807, 14890, 14973, 15059, 15142, 15225, 15308, 15391, 15476, 15669, 15844, 16036, 16125, 16213, 16258, 16364, 16521, 16580, 16723, 16874, 16923, 17101, 18788, 18867, 18978, 19086, 19176, 19302, 19524, 19662, 19796, 19916, 20030, 20166, 20315, 20479, 20651, 20739, 20795, 20848, 20954, 21035, 21087, 21144, 21218, 21285, 21377, 21468, 21540, 21670, 21725, 21820, 21883, 21945, 22163, 22240, 22316, 22376, 22436, 22496, 22556, 22616, 22676, 22736, 22796` | — | `6e109af4c268dcd4e67aec2d70ef7abd479d64b06ebb2fc439a9777591c5c3c8` |
| `common\decisions\GRE.txt` | 38 | 35 | `89, 3574, 3682` | `407, 481, 555, 621, 705, 770, 835, 895, 993, 1065, 1131, 1191, 1276, 1343, 1404, 1510, 1574, 1641, 1698, 1793, 1882, 1969, 2062, 2152, 2240, 2322, 2383, 2818, 2907, 3003, 3102, 3195, 3294, 3391, 3490` | — | `75c0c4bae4d67d7e00f2158a82a88fa3f174d9a4372bfb7813add6c54d325bd5` |
| `common\decisions\GUAY_decisions.txt` | 7 | 0 | `179, 208, 238, 272, 299, 327, 354` | — | — | `f6c963e12fd9b4a1abc1632fb822cfb8026277e402aade83b15e7810fb9cf4ff` |
| `common\decisions\HOL.txt` | 29 | 28 | `2162` | `56, 135, 181, 281, 390, 504, 599, 658, 718, 772, 848, 899, 960, 1001, 1061, 1283, 1488, 1639, 1778, 1817, 1862, 1928, 1988, 2034, 2071, 2109, 2218, 2315` | — | `20dc384cf1ea32d3476c3db154137df0df7d36386988c5348c615d2a7e4e6890` |
| `common\decisions\HUN.txt` | 58 | 58 | — | `33, 93, 153, 213, 273, 333, 420, 496, 576, 660, 772, 865, 926, 1005, 1080, 1141, 1236, 1297, 1384, 1471, 1558, 1645, 1732, 1819, 1906, 1993, 2080, 2161, 2452, 2601, 2688, 2797, 2878, 2960, 3041, 3112, 3209, 3296, 3380, 3475, 3575, 3660, 3758, 3927, 4012, 4092, 4174, 4264, 4391, 4462, 4694, 4761, 4856, 4936, 5011, 5152, 5245, 5395` | — | `7f0a6004a3fbb271d61214efb7ec34bc9d7d6557e31b0397d757dfec7ac58197` |
| `common\decisions\ICE.txt` | 11 | 11 | — | `149, 249, 351, 456, 641, 826, 1010, 1194, 1385, 1446` | `42` | `323701b2071415376404235f2bbcee31357d3a39b6a2733fc407712a346375d9` |
| `common\decisions\INS.txt` | 51 | 48 | `2148, 2180, 4323` | `175, 217, 260, 294, 473, 563, 648, 731, 814, 905, 988, 1076, 1164, 1252, 1322, 1705, 1793, 1854, 1898, 1952, 2032, 2089, 2241, 3566, 4073, 4127, 4690, 4826, 4874, 4986, 5039, 5107, 5189, 5311, 5366, 5422, 5489, 5555, 5621, 5688, 5757, 5832, 5907, 5982, 6057` | `322, 350, 381` | `8b642037a9a3d71de1bda8f07db2d1a962e8010148a71f11a6e8a163583f761b` |
| `common\decisions\IRQ.txt` | 7 | 7 | — | `22, 163, 230, 323, 436, 511, 676` | — | `65ff70ef72c952fea4327887c7bfb5ab2f5eee13e46e466d272d5f26e7a6906a` |
| `common\decisions\ITA.txt` | 52 | 52 | — | `137, 3166, 3213, 3263, 3298, 3333, 3369, 3407, 3442, 3475, 3573, 3606, 3657, 3721, 3779, 4094, 4880, 4933, 4986, 5039, 5093, 5263, 5439, 5998, 6066, 6192, 6322, 6445, 6513, 6600, 6682, 6747, 6817, 6894` | `1937, 2009, 2061, 2133, 2185, 2257, 2309, 2381, 2424, 2757, 2963, 3031, 3099, 3517, 4572, 5695, 5758, 5844` | `e3c582f0730af4b74196c00e825dff5fccc46db8eb2d8c9dbfb2fa8bcd21f76e` |
| `common\decisions\JAP.txt` | 124 | 121 | `1058, 1151, 1212` | `335, 1338, 1572, 1619, 1697, 1962, 2006, 2057, 2118, 2225, 2300, 2390, 2467, 2538, 2635, 2732, 2848, 2910, 3132, 3241, 3414, 3731, 3828, 3984, 4124, 4491, 4551, 4611, 4682, 4740, 4798, 4856, 4972, 5030, 5088, 5146, 5204, 5277, 5337, 5391, 5445, 5564, 5624, 6010, 6209, 6280, 6341, 6412, 6471, 6530, 6593, 6655, 6746, 8794, 8877, 8963, 9047, 9139, 9198, 9270, 9365, 9462, 9553, 9639, 9738, 9820, 9897, 10027, 10154, 10287, 10421, 10479, 10569, 10660, 10789, 10906, 11007, 11138, 11275, 11423, 11526, 11613, 11713, 11800, 11953, 12013, 12088, 12143, 12202, 12264, 12326, 12388, 12457, 12520, 12572, 12790, 12854, 12918, 12971, 13125, 13175, 13301, 14277, 14353, 14430, 14507, 14614, 14834, 14934, 15028, 15088, 15147, 15237, 15524, 15569, 15675, 15720, 15888, 15965` | `12729, 13067` | `2f936d32a11a4a6d196db972e566eb3d0e921d34fb52da0c14c56b8e5783dc80` |
| `common\decisions\KOR.txt` | 0 | 0 | — | — | — | `2b30a4d2b68d254d1123cfd40a0da0bec3219b026659621ad272f76006f050d0` |
| `common\decisions\lar_agent_recruitment_decisions.txt` | 16 | 8 | `101, 229, 358, 487, 616, 773, 902, 1066` | `36, 163, 292, 421, 550, 679, 836, 982` | — | `9a39df3b1892ff09dca85db2f4544d42b7d229c4d7fe8e3b1a2004d0387a7b96` |
| `common\decisions\LAT.txt` | 4 | 4 | — | `103, 174, 228, 348` | — | `29eea3da6a2ff324f81e35bb2f507f99acb28fe7a711f07d44fc7cde5434da35` |
| `common\decisions\LIT.txt` | 4 | 4 | — | `18, 85, 269, 344` | — | `260253e9f5a0ef4bbbd407098e47e8d6951463794a3fb24ad0700f7db963dbe6` |
| `common\decisions\MAL.txt` | 1 | 1 | — | `31` | — | `22b90c4f545333790b51d3338ef841830459994f122e64490d33edf52d6b67fc` |
| `common\decisions\MAN_decisions.txt` | 41 | 30 | `43, 91, 223, 275, 405, 453, 906, 1284, 1361, 1462, 1522` | `618, 692, 766, 838, 930, 997, 1064, 1124, 1192, 1216, 1345, 1390, 1694, 1749, 1804, 1889, 1985, 2080, 2181, 2252, 2302, 2352, 2401, 2468, 2593, 2718, 2842, 2906, 3160, 3205` | — | `d921bd2372e91dda3ee50f74a012013b4a8593de62f771e74f661c9df9e37278` |
| `common\decisions\MEN.txt` | 7 | 6 | `606` | `55, 182, 228, 322, 417, 515` | — | `b8a55616e6e4df3c5288e5b4299f1620800cc9f264aaf07ecbdb7119f3dcf9a5` |
| `common\decisions\MEX.txt` | 21 | 21 | — | `429, 809, 860, 911, 962, 1013, 1064, 1105, 1152, 1196, 1232, 1268, 1308, 1340, 1377, 1414, 1452, 1488, 1527, 1566, 1646` | — | `b1b2994901886eb68a3699c433878a6bac962674a0e8c45e6bab52a96034c32e` |
| `common\decisions\MON.txt` | 3 | 3 | — | `39, 112, 189` | — | `dd0f34b3b3457824a21ce46c75330ceedbbec5e938ef7e2e0ca6feed6d8112d1` |
| `common\decisions\MTG_congress.txt` | 14 | 10 | `17, 56, 158, 182` | `88, 113, 133, 202, 223, 465, 498, 530, 557, 592` | — | `045577929e6240d037c4b3fca295cf21639e849655f2b9b76339cc831074854b` |
| `common\decisions\MTG_naval_treaty.txt` | 7 | 7 | — | `13, 103, 210, 304, 399, 474, 601` | — | `4fd5ce58490fadfea0a111d56b06e3cc7df681e697f71434b0da03bd7f68a653` |
| `common\decisions\NATO.txt` | 2 | 2 | — | `39, 102` | — | `cbe2807647dc6f6c7112e50dad7ba234407555b71419aace079edd5e319fe087` |
| `common\decisions\NOR.txt` | 13 | 13 | — | `888, 920, 962, 1069, 1382, 1809, 1851, 2297, 2648, 2670, 2851, 2872, 2902` | — | `dcb40a1a2f2e1a484df677ef44451920ccf7f2d123db1dd035d2166cf1ebb531` |
| `common\decisions\NORDIC.txt` | 9 | 9 | — | `232, 490, 554, 596, 762, 798, 847, 893, 931` | — | `50d03b5fbfe46b7c7213dfc292063a2dfe663e8653980bc7e04fb10bf26870ff` |
| `common\decisions\NZL.txt` | 2 | 2 | — | `23, 84` | — | `9afac7d67ea4b3ac8682af6a1649e38885c92048fd7f0a7461c350f675b77e8a` |
| `common\decisions\OMA.txt` | 2 | 2 | — | `47, 131` | — | `a95225c292d4df29b068203bc91c8ef2439df559952ac4f26ed770419e00366d` |
| `common\decisions\PER.txt` | 13 | 12 | `79` | `146, 209, 269, 358, 414, 470, 536, 666, 727, 763, 801` | `594` | `fb33d1d2aae3bdc871261454f2f615fd75c760d6f349d52ac780b407aa9b439a` |
| `common\decisions\PHI.txt` | 27 | 27 | — | `137, 175, 251, 315, 430, 465, 533, 588, 672, 749, 818, 895, 1430, 1477, 1498, 1611, 1631, 1667, 1736, 1758, 1791, 1900, 1921, 2486, 2517, 2605` | `1949` | `468ae9a96eacd0e6339a810931a69c0228ad08eb652f8a0a0d58bcf48044a914` |
| `common\decisions\POL.txt` | 35 | 32 | `1311, 1351, 1391` | `15, 309, 339, 707, 769, 856, 1253, 1436, 1483, 1530, 1577, 1624, 1671, 1718, 1765, 1815, 1865, 1919, 1999, 2065, 2436, 2500, 2816, 2871, 3153, 3221, 3275, 3320, 3354, 3391, 3456, 3509` | — | `8f5d63c35addbae46304f051ed223f9bfdcc6f30b85829062753cddbdb4de179` |
| `common\decisions\political_decisions.txt` | 53 | 53 | — | `31, 75, 112, 169, 207, 241, 278, 321, 364, 441, 494, 540, 624, 668, 704, 741, 798, 837, 871, 908, 943, 978, 1054, 1098, 1136, 1204, 1252, 1292, 1333, 1394, 1437, 1475, 1516, 1555, 1594, 1670, 1718, 1760, 1821, 1864, 1928, 2019, 2181, 2255, 2324, 2438, 2535, 2633, 2720, 2800, 2865, 2921, 2986` | — | `7da36bfcd75c7b3fe8a73848ae6a0b40605c16ae20f4995f8ad3369dc2392067` |
| `common\decisions\POR.txt` | 21 | 8 | `21, 54, 87, 123, 212, 302, 391, 454, 1993, 2023, 2743, 2822, 2901` | `1925, 2108, 2220, 2410, 2504, 2549, 2603, 2664` | — | `269bcab0bd25207246ef2dfb8637fc1a70e977fc5f4077a4beab86ce316ad5c2` |
| `common\decisions\PRC.txt` | 63 | 62 | `2528` | `76, 433, 538, 643, 748, 853, 958, 1063, 1168, 1273, 1378, 1483, 1560, 1888, 1974, 2060, 2146, 2232, 2318, 2404, 2490, 2584, 2705, 2855, 2883, 2906, 2973, 3014, 3062, 3108, 3155, 3202, 3250, 3292, 3325, 3375, 3441, 3473, 3518, 3568, 3617, 3666, 3714, 3764, 3828, 3868, 3909, 3948, 3981, 6175, 6417, 6456, 7264, 7343, 7422, 7528` | `5735, 6023, 7010, 7079, 7195, 7231` | `19b5776bf0e91a419946bedaf3aa5e052ec09165ae8bdbcb0f1800cd081a01df` |
| `common\decisions\PRU.txt` | 3 | 3 | — | `74, 254, 333` | — | `59ad335dcec752ecad206452f607353260decd799017c4fc9a7f54036d386456` |
| `common\decisions\PSR.txt` | 1 | 1 | — | `31` | — | `66a910abde4355bf86e540e962e0734a2c194dc8725874e1cd2f96592e88e078` |
| `common\decisions\RAJ_GOE.txt` | 66 | 48 | `682, 1056, 1118, 1185, 1249, 1318, 1483, 1550, 1616, 1682, 1809, 2236, 2301, 4107, 4382, 4469, 4555, 5254` | `38, 90, 182, 248, 291, 361, 456, 499, 536, 593, 622, 709, 807, 844, 877, 930, 984, 1398, 1916, 2931, 3994, 4027, 4075, 4142, 4190, 4239, 4293, 4324, 4659, 4717, 4775, 4833, 4891, 4949, 5007, 5064, 5137, 5209, 5424, 5502, 5580, 5658, 5736, 5828` | `6460, 6483, 6506, 6538` | `3b99609b24365b753257f1b83ada542e612225318a8d16be06bc58ebda5806ff` |
| `common\decisions\RAJ.txt` | 2 | 2 | — | `42, 129` | — | `030f916f6682fc6d4f6cc6c43c6c60f6dee6d8d09d99161e87bbf1264a7b34d7` |
| `common\decisions\resource_prospecting.txt` | 117 | 117 | — | `35, 115, 195, 285, 365, 445, 525, 862, 948, 1031, 1115, 1206, 1294, 1378, 1466, 1549, 1635, 1720, 1804, 1898, 1988, 2077, 2173, 2256, 2349, 2434, 2520, 2627, 2736, 2845, 2954, 3063, 3172, 3281, 3391, 3500, 3611, 3728, 3810, 3903, 4013, 4123, 4225, 4302, 4379, 4456, 4539, 4630, 4706, 4782, 4858, 4943, 5029, 5115, 5205, 5308, 5394, 5480, 5598, 5716, 5830, 5948, 6066, 6179, 6265, 6351, 6435, 6547, 6636, 6746, 6834, 6922, 7010, 7097, 7186, 7296, 7384, 7472, 7554, 7636, 7718, 7807, 7897, 7992, 8086, 8177, 8269, 8357, 8439, 8519, 8577, 8635, 8690, 8757, 8872, 8955, 9027, 9098, 9169, 9268, 9336, 9425, 9505, 9584, 9663, 9742, 9821, 9900, 9979, 10058, 10137, 10216, 10295, 10385, 10464, 10543, 10629` | — | `d1c3d05467605cd66770434a2baaa41c9dbfcc2a7046dfee32baec2b1c731994` |
| `common\decisions\RKH.txt` | 1 | 1 | — | `12` | — | `61efd879dca1ff845be2ff744455f566f4fa76bc899941c8749fc1d8804f0e94` |
| `common\decisions\RNG.txt` | 1 | 1 | — | `39` | — | `bdf87fe14510de68e58c8994ea1bacf72d31b3d3a2d3d8bd5f564c052dd36188` |
| `common\decisions\ROM.txt` | 22 | 15 | `50, 200, 316, 484, 529, 574, 619` | `809, 1030, 1251, 1472, 1693, 1914, 2135, 2356, 2577, 2798, 3019, 3240, 3461, 3682, 3905` | — | `f3d65bba70840fe8376f3a0e0e409b70bc2f7f7b7f35a240031323fff170a4d1` |
| `common\decisions\SAF.txt` | 45 | 0 | `20, 53, 89, 120, 154, 187, 218, 250, 281, 312, 343, 381, 418, 449, 480, 511, 543, 574, 605, 636, 667, 698, 729, 760, 792, 826, 858, 889, 920, 951, 982, 1013, 1045, 1076, 1107, 1138, 1169, 1200, 1231, 1263, 1294, 1328, 1362, 1394, 1432` | — | — | `e88436a24891688e43ffc7321394d095f794c6f2bf10e36175c75eec85154378` |
| `common\decisions\SAU.txt` | 1 | 1 | — | `39` | — | `8b883f5875718d556c35fd399fed9cc7314655bc3e63ae48e921cdd024076257` |
| `common\decisions\SIA.txt` | 59 | 49 | `113, 2049, 2084, 2126, 2154, 2450, 2487, 2525, 2573, 2607` | `79, 766, 992, 1185, 1250, 1373, 1496, 1614, 1705, 1799, 1895, 2211, 2238, 2265, 2292, 2319, 2346, 2373, 2400, 2427, 2843, 2898, 2952, 3028, 3122, 3202, 3235, 3270, 3304, 3334` | `154, 202, 233, 261, 280, 298, 315, 332, 350, 367, 384, 410, 445, 483, 520, 575, 610, 648, 683` | `c56891a818d65262c3a1524f5913549b5ef5bc5f1ce87daaae22e862dadfa3e1` |
| `common\decisions\SLO.txt` | 2 | 1 | `146` | `13` | — | `9da3310a7bd7444d998bcb13a3931cdd38b9ff6a3f5bdeafa1dac39dcd8445b9` |
| `common\decisions\SOV.txt` | 208 | 159 | `22, 47, 72, 784, 832, 880, 928, 960, 986, 1012, 1038, 1066, 1093, 1118, 1141, 1164, 1187, 1210, 1233, 1256, 1279, 1302, 1325, 1348, 1373, 1396, 1419, 1442, 1465, 1491, 1514, 1537, 1560, 1587, 1612, 1637, 1662, 1687, 1712, 1742, 1821, 1848, 1876, 1906, 8586, 8622, 9815, 9843, 17590` | `503, 5069, 6847, 7688, 10758, 10877, 11053, 11222, 11370, 11472, 11567, 11687, 12621, 12665, 12750, 12799, 12848, 12919, 12983, 13060, 13105, 13161, 13262, 13313, 13355, 13395, 13436, 13501, 13544, 13966, 14242, 14322, 14409, 14486, 14558, 14621, 14900, 14973, 15046, 15119, 15192, 15265, 15339, 15501, 15613, 15751, 15878, 16016, 16148, 17345, 17426, 17531, 17659, 17809, 17872, 17912, 17960, 18022, 18116, 18156` | `167, 226, 287, 359, 418, 1966, 2046, 2122, 2220, 2289, 2355, 2433, 2521, 2641, 2722, 2794, 2917, 3173, 3419, 3500, 3584, 3654, 3723, 3821, 3904, 4006, 4078, 4154, 4245, 4333, 4442, 4548, 4647, 5247, 5310, 5389, 5585, 5648, 5819, 5881, 5945, 6125, 6201, 6267, 6654, 6729, 6794, 6928, 7087, 7254, 7477, 8235, 8323, 8424, 8670, 8728, 8786, 8851, 8913, 8974, 9033, 9093, 9155, 9216, 9275, 9337, 9395, 9459, 9523, 9583, 9643, 9701, 9759, 9886, 9935, 9977, 10019, 10061, 10103, 10145, 10187, 10229, 10271, 10313, 10440, 10482, 10524, 10566, 10608, 10650, 10692, 13607, 13689, 13757, 13860, 14040, 14117, 14189, 17710` | `75e1cfde7bcca928aac655ba2f89f2a009e0f8f8812200625dfe310761d06474` |
| `common\decisions\SPR.txt` | 108 | 88 | `8996, 9123, 9270, 9391, 9512, 9654, 9801, 9943, 10091, 10217, 10343, 10464, 10590, 10716, 10842, 10963, 11089, 11215, 11336, 11457` | `100, 160, 212, 265, 316, 376, 435, 500, 555, 12584, 12656, 12728, 12800, 12872, 12944, 13016, 13088, 13160, 13232, 13304, 13376, 13448, 13520, 13592, 13664, 13736, 13808, 13880, 13952, 14367, 14430, 14493, 14556, 14624, 14692, 14760, 14828, 14878, 14932, 14986, 15040, 15094, 15148, 15202, 15256, 15310, 15364, 15418, 15472, 15526, 15580, 15634, 15688, 15742, 15796, 15850, 15904, 15950, 16108, 16262, 16416, 16674, 16828, 17047, 17148, 17213, 18160, 18223` | `739, 913, 1136, 1364, 1592, 1768, 1991, 2219, 2395, 2566, 2789, 2965, 3130, 3301, 3472, 3643, 3814, 3985, 4156, 4327` | `9aabdcd2ecedcf0eee00ebe66dc16fc382d5725b75f1adc4aaae9fda3032a243` |
| `common\decisions\SS.txt` | 11 | 11 | — | `39, 96, 147, 204, 261, 307, 353, 400, 462, 508, 570` | — | `2bc16f73e3d4a0502f430b2331a649a74d623f7d5184f8204591cd618cdde6ea` |
| `common\decisions\stability_war_support.txt` | 5 | 3 | `26, 75` | `340, 493, 686` | — | `3eeaa8d95bcd450cc24e36fc18402b6d8be8b2219c49f646c066e93e7d5faf26` |
| `common\decisions\SWE.txt` | 37 | 26 | `312, 1407, 1898, 1962, 2018, 2073, 2558, 2708, 2740, 2771, 2802` | `385, 519, 572, 653, 716, 788, 835, 896, 963, 1028, 1092, 1470, 1569, 1683, 1709, 1735, 1875, 2152, 2489, 2546, 2942, 2973, 3009, 3041, 3131, 3682` | — | `c479af8de9dd17c190e5722735d0c8cd8c3de3ee95dd16b9c807cf6ee9208556` |
| `common\decisions\SWI.txt` | 54 | 54 | — | `143, 221, 385, 434, 484, 560, 670, 766, 814, 881, 945, 1005, 1043, 2047, 2158, 2208, 2244, 2297, 2477, 2606, 2634, 2679, 2726, 2770, 2817, 2863, 3052, 3166, 3252, 3318, 3376, 3410, 3455, 3494, 3542, 3617, 3692, 3767, 3832, 4099` | `1131, 1195, 1260, 1330, 1401, 1467, 1536, 1596, 1658, 1712, 1813, 1896, 1970, 2339` | `89c6ec1d1fd21c4c5cba9cec796736eac08e62e1043a07515757c388ba9522ae` |
| `common\decisions\TOA_formable_nation_decisions.txt` | 0 | 0 | — | — | — | `60b25a3f9af0d0ac022fdbe82b5cdab1a7d3d4ef7272d0be20ce579e79647837` |
| `common\decisions\TOA_shared_decisions.txt` | 30 | 30 | — | `26, 64, 400, 575, 740, 905, 1067, 1232, 1396, 1548, 1702, 1741, 1779, 1817, 1855, 1893, 2024, 2188, 2349, 2507, 2664, 2823, 2980, 3059, 3185, 3266, 3351, 3463, 3540, 3616` | — | `b2f9eb968f2a0db4008bb43663492606a486bf10fa9770a4cc5231316e6855aa` |
| `common\decisions\TUR.txt` | 69 | 54 | `16, 5701, 5753, 5805, 5863, 5925, 5975, 6020, 6060, 6094, 6135, 6223, 6311, 6397, 6512` | `67, 121, 192, 273, 334, 399, 508, 551, 612, 677, 745, 797, 852, 912, 1272, 1724, 1762, 1806, 1855, 1922, 1959, 2016, 2080, 2183, 2272, 3157, 3251, 3323, 3394, 3465, 3532, 3620, 3691, 3742, 3834, 4046, 4235, 4310, 4501, 4693, 4885, 5077` | `980, 1052, 1124, 1197, 1360, 1452, 1534, 1606, 1664, 3994, 4192, 5315` | `0a72eba0a0e658ac81588cbe15f773f7d4ecf74aac5fae1d402f536e9e4afc45` |
| `common\decisions\USA.txt` | 48 | 44 | `159, 430, 484, 538` | `21, 87, 601, 658, 715, 805, 887, 926, 969, 1017, 1085, 1172, 1230, 1261, 1291, 1322, 1352, 1371, 1409, 1446, 1484, 1524, 1554, 1618, 1658, 1693, 2160, 2207, 2268, 2317, 2364, 2411, 2479, 2532, 2585, 2638, 2706, 2753, 2801, 2896, 2992, 3016, 3042, 3148` | — | `13a134d35148a070645e8163070ebd662db8be187ef7594f7b077f8bacc6dd3c` |
| `common\decisions\VEN.txt` | 1 | 1 | — | `19` | — | `b0bb7a9d2d8f27f0168db9652844aed550aa7db8fc526a6ff26d86db94e4eb6d` |
| `common\decisions\WLS.txt` | 2 | 2 | — | `34, 182` | — | `ff91e2346ad7658e88f86354e3016a89d7066d84c0d5ec96568134b1c7dc8b5a` |
| `common\decisions\WTT_border_conflicts.txt` | 3 | 3 | — | `184, 521, 587` | — | `ff55d63228ffcb0b0474ebb83030e36146bf9e39b25b821e147f8d7f4401a9d2` |
| `common\decisions\WTT_politcal_power_struggle_decisions.txt` | 67 | 0 | `131, 215, 439, 661, 883, 1106, 1329, 1552, 1774, 1996, 2219, 2441, 2663, 2885, 3107, 3329, 3551, 3773, 3995, 4219, 4440, 4663, 4886, 5108, 5330, 5554, 5776, 5998, 6220, 6444, 6668, 6890, 7112, 7334, 7556, 7812, 8089, 8325, 8561, 8797, 9033, 9269, 9505, 9741, 9977, 10213, 10449, 10685, 10921, 11157, 11393, 11631, 11867, 12105, 12343, 12579, 12815, 13053, 13289, 13525, 13761, 13999, 14237, 14473, 14709, 14945, 15181` | — | — | `ce834402cd9e84aaf203f802ae18c045df87468342d2e3c40dc16e9f190ff4de` |
| `common\decisions\YUG.txt` | 17 | 16 | `723` | `51, 125, 200, 275, 350, 427, 494, 569, 644, 925, 979, 1033, 1197, 1255, 1315, 1375` | — | `856d7e22c378a11d6fec8b584f84543b45169f9bfc7e3c32a176cf622e7c7451` |

## Excluded native-cost occurrences

These raw matches are comments, not active declarations; they are outside the totals of active occurrences.

| Source | Owner path | Excluded count | Exact lines |
| --- | --- | ---: | --- |
| Vanilla | `common\decisions\_debug_decisions.txt` | 1 | `420` |
| Vanilla | `common\decisions\_generic_decisions.txt` | 8 | `714, 776, 838, 902, 966, 1030, 1093, 1157` |
| Vanilla | `common\decisions\ARG.txt` | 2 | `1466, 1516` |
| Vanilla | `common\decisions\BRA.txt` | 1 | `1274` |
| Vanilla | `common\decisions\CZE.txt` | 1 | `3665` |
| Vanilla | `common\decisions\DEN.txt` | 1 | `707` |
| Vanilla | `common\decisions\ENG.txt` | 1 | `9150` |
| Vanilla | `common\decisions\ETH.txt` | 5 | `3185, 3197, 3211, 3223, 3235` |
| Vanilla | `common\decisions\GER.txt` | 2 | `105, 222` |
| Vanilla | `common\decisions\JAP.txt` | 12 | `499, 570, 639, 674, 709, 746, 784, 821, 890, 949, 1844, 4914` |
| Vanilla | `common\decisions\NATO.txt` | 1 | `166` |
| Vanilla | `common\decisions\PHI.txt` | 1 | `77` |
| Vanilla | `common\decisions\RAJ_GOE.txt` | 4 | `1854, 3503, 3653, 3769` |
| Vanilla | `common\decisions\resource_prospecting.txt` | 3 | `606, 697, 779` |
| Vanilla | `common\decisions\SOV.txt` | 2 | `10356, 10398` |
| Vanilla | `common\decisions\SS.txt` | 1 | `594` |
| Vanilla | `common\decisions\SWE.txt` | 2 | `2573, 2632` |
| Vanilla | `common\decisions\TOA_shared_decisions.txt` | 2 | `137, 243` |
| Vanilla | `common\decisions\WTT_politcal_power_struggle_decisions.txt` | 2 | `7885, 7958` |

## Coverage disposition and final-freeze boundary

Disposition: implemented declaration discovery; all native owner-adapter and actual discount classifications remain unresolved unless the parent supplies independent owner evidence.
Vanilla declarations can be adapted through mod owner overrides; a missing generic hook alone is not an engine-inaccessible finding.
The prior top-level mod-only 1,328 / 1,033 / 295 snapshot and mixed-date CBRN rows are superseded by these current all-path tables.
The [current handoff](subagent_handoffs/2026-10-03_current_declaration_inventory.md) distinguishes owners removed from native discovery from paths actually removed from the worktree.
The RSA specialist's pending source patch is intentionally not audited or promoted; the current declaration and hash remain a refreshable discovery record.
The decision MCP inventory request returned no final result before its wait was terminated; no native scenario, display, debit, or discount proof was obtained.
Source declaration discovery is complete at these hashes, while manual semantic coverage and final-commit registry reconciliation remain incomplete.
