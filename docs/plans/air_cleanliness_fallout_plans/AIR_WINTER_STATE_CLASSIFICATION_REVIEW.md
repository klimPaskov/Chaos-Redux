# Air Winter State Classification Review

## Status

**Primary manual review:** complete for the pinned installed vanilla build.

The ledger in `common/script_constants/fallout_consolidated_constants.txt` assigns every live vanilla state ID from 1 through 1081 to exactly one of the nine Air Winter presentation classes. The primary reviewer inspected all 1,081 state rows and manually adjudicated regional baselines, precedence conflicts, impassable states, island cases, and terrain/climate anomalies.

**Independent half-review:** complete and reconciled for IDs 541–1081. A fork-without-context reviewer inspected every state in that range and returned four disagreements. The primary reviewer accepted two changes and retained two primary assignments after rechecking the installed strategic-region weather and state evidence. The full 1–1081 primary review therefore has no unresolved rows.

**Authority boundary:** state IDs are the classification authority. Strategic-region membership and weather, province terrain, coast/island topology, approximate latitude, and sampled elevation were review evidence only. They are not runtime inference rules and must never become a silent fallback.

## Numeric contract and accepted counts

| Class ID | Typed array | Presentation identity | States |
| ---: | --- | --- | ---: |
| 1 | `boreal_continental` | Boreal and continental winter | 244 |
| 2 | `temperate_maritime` | Temperate maritime winter | 76 |
| 3 | `mediterranean` | Mediterranean winter | 58 |
| 4 | `desert_arid_plateau` | Desert and arid-plateau winter | 202 |
| 5 | `tropical_coast_monsoon` | Tropical coast and monsoon winter | 152 |
| 6 | `equatorial_rainforest` | Equatorial rainforest winter | 47 |
| 7 | `mountain_highland` | Mountain and highland winter | 176 |
| 8 | `island_oceanic` | Island and oceanic winter | 77 |
| 9 | `polar_subpolar` | Polar and subpolar winter | 49 |
| **Total** | **Nine exclusive arrays** |  | **1,081** |

The numeric meanings are part of the Air Winter presentation contract. Consumers must not renumber or reinterpret them independently.

## Installed-build topology fingerprint

Fingerprint captured on 2026-07-13 from the installed Steam build at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

| Surface | Installed value or SHA-256 |
| --- | --- |
| Game version | `Operation Postern v1.19.2.0.a729 (d245)` |
| Raw version | `1.19.2.0` |
| Steam build ID | `23969257` |
| Steam manifest update | `1783424596` / `2026-07-07 11:43:16Z` |
| `history/states/*.txt` | 1,081 files; composite `f0dee19235db9f5dd6dcb2a7d73c4474c251dce2f458bca35d0aa1953da9450c` |
| `map/strategicregions/*.txt` | 304 files, 243 with live land states; composite `086505885cd92e175f0e443b4dd09389c4dd02f5e226628bae3c097a0bcfd6f2` |
| `map/definition.csv` | `86846be71198d6772c651638aa22e3656133198de9b7c49c6234ed48cf33d87b` |
| `map/provinces.bmp` | `e131d30e5dcb13d9c2a8598f820a2de0ae9828f3a24f2bddc1bcfff40f71660a` |
| `map/heightmap.bmp` | `615300ea13a136ed99d3cba1a8f0b71bb9677d60b27cf474f8abe028f3db4aa4` |
| `map/terrain.bmp` | `41f95665077c5c4cc3366a966becd88e6c1a19fee686de4c29a767f49f9f3c9e` |
| `map/adjacencies.csv` | `26a26c3f42a4b01fb905c99659024e857ffc05e3172fcd9953395321fb76ed64` |
| `localisation/english/state_names_l_english.yml` | `f7247c8df59674f02a68358761bd6f2b6509364354baf6e6a5a1121d9a2641a7` |
| Classification ledger | 78,653 bytes; `7a4a78cb9d795dfff38180c123048ba3db10df429a377a815813871c6e0419eb` |

The two directory composites are reproducible: sort files by filename, emit `filename|byte_length|file_sha256` for each file, join the records with UTF-8 line feeds, and SHA-256 the resulting byte sequence.

Any installed-build change that alters a state file, province topology, strategic-region membership, terrain/elevation evidence, adjacency, or state-name source invalidates this review until the ledger and fingerprint are checked again.

## Required references consulted

- Offline Paradox wiki snapshot: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, State modding, and Map modding.
- Vanilla official documentation: `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, `documentation/script_collection_input.md`, and `documentation/script_collection_operator.md`.
- Vanilla typed-collection precedent: `common/script_constants/state_groups.txt` and `common/script_constants/country_groups.txt`.
- Air Winter design sources: `fallout_winter_visual_state_matrix.md`, `02_winter_climate_visual_overhaul.md`, and `AIR_WINTER_NORMAL_MAP_PROOF.md`.

Vanilla official documentation and installed data were treated as the engine and topology authority. The offline wiki remained the parallel syntax and behavior reference.

## Classification method

1. Parsed every installed vanilla state file and confirmed the live ID domain is exactly 1–1081.
2. Resolved installed English state names for review comments. Duplicate display names, such as the impassable Amazon states, remain distinct because IDs are authoritative.
3. Collected each state's strategic region, strategic-region weather context, province count, coastal-province count, terrain mix, land-neighbor count, impassable status, approximate map northing, and sampled heightmap evidence.
4. Established a regional baseline for each land-bearing strategic region as an organizing aid.
5. Manually inspected every state row and overrode the baseline wherever elevation, aridity, ice, monsoon/rainforest identity, maritime exposure, or island isolation better described the Air Winter presentation.
6. Ran targeted exception passes over highland states without explicit mountain terrain, mountain-heavy states assigned to other climates, isolated landmasses not assigned oceanic, oceanic states with land neighbors, polar/subpolar islands, equatorial states without explicit jungle terrain, and every impassable state.
7. Routed IDs 541–1081 to an independent fork-without-context reviewer, reconciled all four returned disagreements against installed evidence, and recorded the disposition below.
8. Regenerated the typed ledger from the reconciled ID map and audited the written file rather than trusting the review dataset.

Approximate map northing and heightmap samples are not real-world latitude or elevation measurements. They were supporting evidence and never overruled a defensible geographic or climate judgment on their own.

## Precedence rules

These rules resolve conflicts; they are not runtime classifiers.

1. **Polar/subpolar over island/oceanic** when persistent ice, subpolar exposure, or polar winter defines the presentation.
2. **Mountain/highland over tropical/monsoon or arid** when elevation, snow line, passes, and highland isolation define the state's winter.
3. **Island/oceanic only when isolation defines the presentation.** Being surrounded by water is not enough when Mediterranean, tropical/monsoon, equatorial, or polar identity is stronger.
4. **Desert/arid plateau may beat mountain/highland** when dryness, water systems, cold dust, exposed plateaus, and exceptional rather than routine snow define the presentation.
5. Regional baselines lose to state-specific evidence. A strategic-region label never automatically assigns every member state.

## Strategic-region review batches

All 243 strategic regions containing live land states were reviewed in bounded region-ID batches. Class distributions are shown as `B/TM/M/D/T/E/H/I/P` in numeric-contract order.

| Strategic-region IDs | Land-bearing regions | State rows | Class distribution |
| --- | ---: | ---: | --- |
| 1–60 | 44 | 277 | `110/36/25/8/10/0/60/24/4` |
| 61–120 | 28 | 66 | `14/2/2/4/4/0/0/35/5` |
| 121–180 | 52 | 276 | `75/6/12/57/42/21/47/10/6` |
| 181–240 | 57 | 241 | `25/10/18/67/59/12/33/6/11` |
| 241–304 | 62 | 221 | `20/22/1/66/37/14/36/2/23` |
| **Total** | **243** | **1,081** | **`244/76/58/202/152/47/176/77/49`** |

Region IDs with no live land state remain part of the installed 304-file strategic-region topology but do not contribute state rows. The primary state review also used consecutive bounded ID batches spanning 1–1081 so no geographic cluster could hide a missing ID.

## Independent half-review reconciliation

| State | Independent proposal | Final disposition |
| --- | --- | --- |
| Eritrea 550 | Class 4 to class 7 | Retained class 4. Its mountain-heavy interior was considered, but the installed Danakil weather has year-round heat, negligible rain, and no snow; aridity defines the Air Winter contrast. |
| Yakutsk 574 | Class 9 to class 1 | Retained class 9. Western Sakha's installed winter reaches -55 to -31, with strong snow and blizzard probabilities; the subpolar presentation is defining even without an oceanic ice signal. |
| South West Australia 871 | Class 4 to class 3 | Accepted class 3. The southwest coastal winter-rain pattern and real regional climate identity are Mediterranean rather than desert-dominant. |
| Aysén 949 | Class 2 to class 7 | Accepted class 7. Five of six provinces are mountain terrain, so relief, passes, and highland isolation outweigh the maritime baseline. |

The independent reviewer also consciously accepted the primary assignments for borderlines 543, 546, 553, 581, 595, 619, 670, 792, 860, 867, 887, 929, 1026, 1042, and 1050.

## Precedence and exception decisions

| Conflict | Representative IDs | Decision |
| --- | --- | --- |
| Ice versus isolation | Iceland 100, Greenland 101, Kuril Islands 555, Attu 650, Kerguelen 713, South Georgia 720, Jan Mayen 914 | Class 9. Ice or subpolar exposure defines the visual language, so polar/subpolar beats island/oceanic. |
| Southern oceanic versus subpolar | Falkland Islands 299; Magallanes 507; Tierra del Fuego 953 | Falklands use class 8 because ocean isolation dominates; the Patagonian states use class 9 because subpolar land climate dominates. |
| Elevation versus monsoon/rainforest | Bhutan 324, Yunnan 325, Arunachal Pradesh 434, Dali 747, Sikkim 985, Interior Papua 1073 | Class 7. Passes, snow line, and elevation define the presentation. |
| Elevation versus arid plateau | Nagqu 322, Kashmir 441, Chamdo 601, Qinghai 604, Pamir 732, Ganzi 752, Golog 754, Shigatse 757, Ngari 758 | Class 7. These are highland systems where elevation remains the defining winter constraint despite aridity. |
| Dryness versus mountain terrain | Tehran 266, Taklamakan 287, Magwe 288, Nejd 292, North Yemen 293, Muscat 294, Ulaanbaatar 330, Konya 346, New Mexico 376, Arizona 377, Nevada 379, Utah 380, South Baluchistan 444, Gobi 817, Tacna-Moquegua 947, Atacama 952, Khotan 1042 | Class 4. Cold dust, water, exposed plateau, and exceptional-snow cues are more representative than routine deep-snow/pass cues. |
| Island topology versus regional climate | Corsica 1, Sardinia 114, Sicily 115; Ceylon 422, Taiwan 524, Madagascar 543, Hainan 591 | Mediterranean islands remain class 3; the large tropical/monsoon islands remain class 5. Water separation alone does not justify class 8. |
| Appalachian label versus state evidence | Kentucky 369 | Class 1. The exception pass rejected a mountain/highland assignment because elevation and pass conditions do not define the statewide presentation. |
| Impassable states | 21 total | All are retained: 11 class 4 desert/arid states, 9 class 6 rainforest states, and Interior Papua 1073 in class 7. Impassability never removes a live state ID from coverage. |

## Written-ledger audit

The audit parsed the final file's nine named arrays and the state ID lines under each array.

| Check | Result |
| --- | --- |
| Root collection | `air_winter_presentation_states` |
| Typed schema | `any_key = yes`, `array = state` |
| Named arrays | Exactly 9; names and order match the numeric contract |
| Parsed state rows | 1,081 |
| Unique state IDs | 1,081 |
| Minimum / maximum ID | 1 / 1081 |
| Missing IDs | None |
| Duplicate assignments | None |
| Out-of-range IDs | None |
| Invalid class assignments | None |
| Impassable states represented | 21 / 21 |
| Rows with name, region, and rationale comment | 1,081 / 1,081 |
| Sum of class counts | 1,081 |

## Consumer invariants and change control

- Consumers read the explicit typed arrays. They must not infer a class from weather, terrain, latitude, elevation, coast count, strategic region, continent, tag, or state category at runtime.
- There is no default presentation class and no fallback array. A missing or multiply assigned state is an invariant failure that requires a ledger correction.
- All live states, including impassable states and one-province islands, remain classified.
- State ID is authoritative even when installed localisation repeats a display name.
- Inline comments are review evidence only and have no gameplay meaning.
- The ledger is presentation data. It does not independently calculate Air Winter gameplay effects.
- A state-topology or numeric-contract change requires a fresh exact-cover audit and targeted manual review before acceptance.
- If another system needs a broader climate family, it must map from these accepted class IDs explicitly rather than silently reclassifying states.

## Simplifications, omissions, and blockers

**Ledger simplifications or omissions:** none. All 1,081 live vanilla states are explicitly assigned, all 21 impassable states are present, and no runtime fallback was introduced.

**Review blockers:** none. Independent cross-check coverage was the assigned second-half range, IDs 541–1081; the primary manual review covered the full 1–1081 domain.
