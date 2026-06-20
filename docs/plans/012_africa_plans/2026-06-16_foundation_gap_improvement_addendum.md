# Event 012 Africa Foundation Gap Improvement Addendum

Date: 2026-06-16

Scope: planning only. This addendum does not edit gameplay, localisation, assets, or spreadsheets.

Disposition status, 2026-06-20: this addendum is retained as planning history, but it is no longer one undifferentiated unresolved blocker. Use `docs/plans/012_africa_plans/2026-06-20_foundation_addendum_disposition.md` for the accepted implemented/folded, superseded/modified, queued/still-open, and rejected/held status map. That ledger does not claim Event 012 completion.

## Planning Status

No earlier Event 012 improvement-loop addendum was found under `docs/plans/012_africa_plans/`. The existing handoffs cover source research, super-event text research, and audio research, so this addendum is not stacking a second unresolved design layer for the same gap.

Keep this file in `docs/plans/012_africa_plans/` until the parent accepts the tranche. If accepted, fold the implemented design into:

- `docs/specs/012_africa_specs/specs/012_africa_focus_tree_plan.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
- `docs/specs/012_africa_specs/specs/012_africa_evolutions_world_end_and_scenarios.md`
- `docs/specs/012_africa_specs/matrices/012_africa_acceptance_criteria.md`
- `docs/specs/012_africa_specs/matrices/012_africa_decision_map.md`
- `docs/specs/012_africa_specs/matrices/012_africa_ai_strategy_matrix.md`
- `docs/specs/012_africa_specs/matrices/012_africa_asset_matrix.md`

Parent implementation status, 2026-06-17: the selected-dossier survey portion of this addendum has been accepted into implementation. `africa_open_next_historical_dossier` now starts `africa_selected_dossier_survey_mission`; mission success opens and surveys the active dossier, while failure raises Restoration Debt and Local Sovereignty pressure and leaves the dossier retryable. The broader addendum remains unresolved for package-specific historical dossier missions, deeper settlement forks, local resistance events, and richer per-package AI.

## Current Foundation Gap

The first foundation tranche has useful scaffolding:

- `common/script_constants/012_africa_constants.txt` defines 32 historical dossier IDs, 11 high-chaos package IDs, active caps, minimum counts, shared value deltas, and decision durations.
- `common/scripted_effects/012_africa_effects.txt` registers the dossier and high-chaos catalogs, selects the next unopened item, records generic opened/unlocked flags, and advances Evolution III/IV thresholds.
- `common/scripted_triggers/012_africa_triggers.txt` gates valid unifiers, historical dossier IDs, high-chaos package IDs, and Bestiary Clause unlocks.
- `common/national_focus/012_africa_focus.txt` exposes the Authority Atlas, Archive of Old Seats, three aggregate dossier focuses, the high-chaos door, Forest Parliament, and Archive Bestiary Clause.
- `common/decisions/012_africa_decisions.txt` exposes a single generic `africa_open_next_historical_dossier` decision and a single generic `africa_unlock_bestiary_package` decision.
- `localisation/english/012_african_union_l_english.yml` contains names for all cataloged dossier and high-chaos IDs.

The missing tranche is not more IDs. The missing tranche is playable consequence. The catalog currently behaves like a queue of labels with uniform cost/value rewards. It does not yet deliver macro-region dossier missions, selected-target authority work, settlement forks, local resistance, subject/tag outcomes, asset-backed dossiers, or AI behavior specific to each package.

Do not add a new catalog on top of this. Deepen the existing catalog.

## What Not To Add Yet

- Do not add more than the existing 32 historical IDs or 11 high-chaos IDs in this tranche.
- Do not implement every possible historical polity as a spawned country. Most dossiers should remain observer, protected office, regional authority, state modifier, idea, or mission content until a tag is justified.
- Do not add final super-event titles, quotes, or audio from placeholder role labels. The super-event handoffs remain research-gated.
- Do not use invented "historical" flags when `docs/assets/012_africa/source_research/manifest.md` marks a polity as Low confidence. Use a neutral archive-office placeholder only with explicit parent approval.
- Do not make human historical packages supernatural. High-chaos fiction must stay explicitly nonhuman or explicitly supernatural and must not be used as a coded human group.
- Do not use daily or weekly world iteration for dossier maintenance. Use focus completion, decision completion, event chains, targeted decisions, selected targets, and scoped helpers.

## Route Families and Focus Clusters To Implement Next

These are exact missing focus clusters to add after the existing `AFR_archive_of_old_seats`, `AFR_dossier_kush_to_kilwa`, `AFR_dossier_manden_to_benin`, `AFR_dossier_kongo_to_merina`, `AFR_high_chaos_door`, `AFR_forest_parliament`, and `AFR_archive_bestiary_clause` scaffolding.

### 1. Authority Register Cluster

Purpose: turn `africa_selected_dossier_id` from a passive queue variable into a player-facing dossier surface.

Suggested focus IDs:

- `AFR_authority_register`
- `AFR_dossier_selection_office`
- `AFR_integration_temperature_board`
- `AFR_old_seat_mission_calendar`
- `AFR_local_sovereignty_hearings`

Rewards and gates:

- Unlock selected-dossier decisions instead of relying only on `africa_open_next_historical_dossier`.
- Set `africa_authority_register_open`.
- Add modest `africa_archive_mandate` and `africa_regional_trust`.
- Unlock active caps from existing constants: early 2 active dossiers, mid 4, late 7.
- Gate after `AFR_archive_of_old_seats`; AI should take it before any regional dossier lane.

### 2. Macro-Regional Dossier Lanes

Purpose: replace the three aggregate dossier focuses with region-specific clusters that unlock mission families and asset calls.

Suggested focus groups:

- North/Nile/Horn: `AFR_nile_stelae_and_red_sea_gates`, `AFR_cataract_registers`, `AFR_horn_well_laws`
- West/Sahel: `AFR_western_rivers_and_crowns`, `AFR_sahel_lake_chad_ledger`, `AFR_gold_forest_stools`
- Central: `AFR_kongo_memory_rings`, `AFR_copperbelt_title_roads`, `AFR_forest_court_settlements`
- East/Indian Ocean: `AFR_swahili_monsoon_ledgers`, `AFR_island_diwan_office`, `AFR_coralline_port_charters`
- Great Lakes: `AFR_lake_kingdom_hearings`, `AFR_kabaka_and_omukama_arbitration`
- Southern/Zambezi/Madagascar: `AFR_stone_city_registers`, `AFR_floodplain_calendar_office`, `AFR_red_earth_rova_files`

Rewards and gates:

- Each lane should unlock only the dossiers mapped to its macro-region.
- Completion should not instantly open dossiers. It should unlock survey decisions and raise region-specific trust.
- Each lane should have one infrastructure or logistics reward tied to its geography, such as Red Sea convoys, Niger river routes, Congo river posts, Lake Victoria ferry logistics, Zambezi flood planning, or Madagascar highland rice bureaucracy.

### 3. Settlement Fork Cluster

Purpose: give opened dossiers consequences and route identity.

Suggested focus IDs:

- `AFR_respect_the_old_seats`
- `AFR_documents_before_consent`
- `AFR_seal_them_under_one_archive`
- `AFR_the_league_must_not_become_a_museum`
- `AFR_the_museum_must_not_become_a_prison`
- `AFR_continental_register`

Fork identities:

- Respect route: higher `africa_regional_trust` and `africa_old_seat_legitimacy`, slower cores, more observer/protected member outcomes.
- Documents route: faster mission throughput, higher forgery risk, lower local trust if pushed.
- Seal route: stronger central authority and integration speed, higher `africa_restoration_debt` and foreign exploitation risk.
- Anti-museum focus pair: prevents either route from becoming pure restoration cosplay or pure central erasure.
- Continental Register: requires 24 opened historical dossiers and at least one resolved dossier per macro-region.

### 4. Liberation and Regional Authority Bridge Cluster

Purpose: tie the Archive to map objectives instead of letting it float as a flavour queue.

Suggested focus IDs:

- `AFR_guard_the_old_capitals`
- `AFR_charter_roads_to_the_seats`
- `AFR_regional_guard_schools`
- `AFR_foreign_holder_case_files`
- `AFR_scramble_counter_dockets`

Rewards and gates:

- Unlock old-seat protection missions for states held by foreign or resistant countries.
- Add equipment and manpower costs to prevent free militia loops.
- If a foreign holder owns the relevant historical area, raise `africa_colonial_alarm` and unlock a claim/objective path, not instant annexation.
- If the unifier owns and controls the relevant area, unlock local authority, state modifier, or living-core progress.

### 5. Bestiary Clause and High-Chaos Safety Cluster

Purpose: replace the current high-chaos queue with explicit safe nonhuman/supernatural gameplay.

Suggested focus IDs:

- `AFR_no_seats_for_caricature`
- `AFR_first_nonhuman_envoys`
- `AFR_habitat_trust_board`
- `AFR_omen_reliability_office`
- `AFR_treaty_of_teeth_and_roots`
- `AFR_court_of_thunder_and_tides`
- `AFR_spider_at_the_signature_table`
- `AFR_world_root_mandate`

Gates:

- `AFR_no_seats_for_caricature` must be required before any high-chaos subject/tag can appear.
- `AFR_first_nonhuman_envoys` requires Evolution III and at least 24 historical dossiers opened.
- `AFR_world_root_mandate` requires 6 high-chaos packages unlocked, `africa_bestiary_alarm` below a danger threshold, and no unresolved Bestiary disaster mission.

Safety rule:

- Every high-chaos package must set a clear nonhuman/supernatural classification flag, be excluded from normal human unifier selection, and use fictional institutional naming. It must never be framed as a human ethnicity, real-world polity, or human country under an animal name.

## Historical Dossier Gameplay Packages

Use these 24 as the first playable dossier tranche. The remaining existing catalog IDs can stay as later optional rows after this tranche is implemented.

Asset status uses `docs/assets/012_africa/source_research/manifest.md`. "No clean final source" means the package can still be implemented with neutral Archive UI and no final historical flag/portrait until source work catches up.

| Dossier ID | Macro-region | Gameplay package | Costs and objectives | Subject/tag surface | Source and asset status |
| --- | --- | --- | --- | --- | --- |
| `kush_meroe` | North/Nile | Cataract and royal-cemetery dossier. Survey Nile states, protect monument/state heritage, then choose observer register or Nile authority office. | 45 PP, 120 command power-equivalent gate through constants, infantry equipment for guards, 120-day protect mission. Objective: own/control a Nile corridor state or have a protected local partner. | No immediate tag required. Later Nile-Horn authority hook. | UNESCO Meroe source lead available online. Manifest does not list a final Kush asset; needs archive/monument source pass. |
| `aksum` | North/Nile/Horn | Stelae and Red Sea gate dossier. Pairs monument protection with port/convoy access. | 45 PP, convoys, support equipment, 120-day Red Sea route mission. Objective: control/ally a Red Sea or northern Ethiopian access point. | Potential AXM subject only if tag work is approved. | Manifest has High source lead for Axum obelisk engraving but local pull incomplete. |
| `adal_harar` | Horn | Frontier emirate and fortified trade-gate dossier. Creates a Red Sea inland route with local sovereignty pressure. | 35 PP, infantry equipment, 90-day caravan gate mission. Objective: prevent simultaneous coercion of Aksum and Adal. | No tag in first pass; observer/protected seat. | Manifest Low; no attested period symbol or portrait selected. |
| `ajuran` | Horn/Indian Ocean | Hydraulic sultanate and well-law dossier. Adds supply, desert attrition relief, and well protection. | 35 PP, support equipment, trucks or trains if available, 100-day well survey. Objective: hold Somali coast or partner with a Horn state. | No tag in first pass; local office/state modifier. | Manifest Low; no clean symbol/portrait selected. |
| `songhai` | West/Sahel | Niger river ledger dossier. Builds river patrols, scholar registries, and Sahel supply links. | 45 PP, infantry equipment, 120-day Niger corridor objective. | Observer or Sahel Caravan authority. No instant SNG tag unless country package exists. | No manifest row; source pass needed. Britannica confirms middle Niger trading empire basis. |
| `jolof_wolof` | West/Atlantic | Senegambia arbitration dossier. Focus on nested coastal seats and Atlantic diplomacy. | 35 PP, convoys, 90-day coastal hearing. Objective: no active war against local Senegambia target. | JLF tag possible from expanded matrix but blocker is country package/flags. | No manifest row; source pass needed. |
| `mossi` | West/Sahel | Cavalry houses and fortified towns dossier. Improves local cavalry/recon and raises integration resistance if coerced. | 40 PP, infantry equipment, cavalry/motorized XP gate if possible, 105-day mission. | MOS tag possible from matrix. | No manifest row; source pass needed. |
| `kanem_bornu` | West/Sahel/Lake Chad | Lake Chad and trans-Saharan road dossier. Strong desert logistics, high restoration debt if centralized too fast. | 45 PP, trucks or trains, 140-day Lake Chad road mission. Objective: control or protect a Lake Chad state. | BOR tag possible from matrix, but needs country setup and safe modern-border handling. | No manifest row. Britannica source confirms long Lake Chad trading empire. |
| `asante` | West/Forest | Golden Stool and forest confederacy dossier. High legitimacy if respected; severe trust loss if exploited. | 45 PP, support equipment, 120-day regalia protection mission. Objective: no looting/forced-centralization branch active. | ASH tag possible from matrix; can also be protected seat. | Manifest High for Prempeh I portrait. Golden Stool/regalia handling needs sensitivity; do not use generic artifact-plunder framing. |
| `oyo` | West/Yoruba | Cavalry road and tributary arbitration dossier. Creates mobile guard bonus and coastal dispute chain with Dahomey/Benin. | 40 PP, infantry equipment, army XP, 110-day cavalry road mission. | OYO tag possible from matrix; no immediate spawn unless Yoruba package exists. | No manifest row. Britannica source supports Oyo/Dahomey/coastal trade and cavalry hooks. |
| `benin_edo` | West/Yoruba/Edo | Court guild and restitution dossier. Protect regalia and craft offices, never frame as artifact extraction. | 45 PP, civilian factory burden, 120-day court-guild mission. Objective: stable local trust above threshold. | EDO tag possible from matrix. | Manifest Low for Benin bronze lead. Use a specific open-access museum object only after source review. Met Museum source supports court art/oba chronology. |
| `dahomey` | West/Guinea Coast | Abomey palace guard and coastal tribunal dossier. Strong military/police outcome, higher alarm if authoritarian route abuses it. | 40 PP, infantry equipment, manpower, 110-day palace guard mission. | DAH tag possible from matrix. | Manifest High for Behanzin portrait. |
| `kongo` | Central/Atlantic | Cross-river kingdom and coastal-interior diplomacy dossier. Adds river customs and foreign-holder dispute hooks. | 45 PP, convoys/support equipment, 130-day Kongo river mission. | KNG tag possible, or Congo Basin Charter regional authority hook. | Manifest Medium for Cavazzi-derived Kongo flag reference. |
| `ndongo_matamba` | Central/Angola | War office and resistance corridor dossier. Gives defense, retreat, and anti-colonial raid objectives. | 40 PP, infantry equipment, command power, 120-day corridor mission. | No first-pass tag unless package exists; can be protected office. | Manifest High for Queen Nzinga engraving. |
| `luba` | Central/Copperbelt | Memory-board and copper road dossier. Improves authority memory, supply, and copperbelt integration. | 40 PP, support equipment, 110-day memory-board mission. Objective: avoid coercive direct-rule settlement. | LUB tag possible but blocked by assets/country setup. | Manifest Low for lukasa lead; needs rights-clean museum/archive file. |
| `lunda` | Central/Copperbelt | Title roads and satellite-court dossier. Adds regional authority depth and copperbelt diplomacy. | 40 PP, trucks/support equipment, 110-day title road mission. | LND tag possible; can remain regional office. | No manifest row; source pass needed. |
| `buganda` | Great Lakes | Kabaka council and lake road dossier. Strong centralized local partner with lake logistics. | 45 PP, convoys/support equipment, 120-day lake road mission. Objective: hold or protect Lake Victoria access. | BUG tag possible from matrix. | Manifest High lead for Mwanga II portrait, not locally pulled. Britannica supports Buganda centralized kingdom/lake-region role. |
| `bunyoro` | Great Lakes | Bunyoro-Kitara restoration dossier. Pairs with Buganda as rivalry/arbitration, not a duplicate. | 40 PP, infantry equipment, 120-day arbitration mission. Objective: if Buganda dossier opened, solve dispute before either gets final settlement. | Observer/protected seat first; tag later only with source pass. | Manifest Low; Kabalega source missing. Britannica supports Bunyoro-Kitara regional dominance. |
| `swahili_coast` | East/Indian Ocean | Coral-port and dhow ledger dossier. Adds ports, convoys, and monsoon trade missions. | 45 PP, convoys, 140-day port ledger mission. Objective: own/control or protect one Swahili coast port. | SWA regional subject possible; first pass can be Indian Ocean Congress office. | No direct manifest row. UNESCO Kilwa source supports port-city heritage. |
| `kilwa` | East/Indian Ocean | Kilwa/Songo Mnara monument-port dossier. More focused than `swahili_coast`: monument protection plus port development. | 40 PP, convoys, civilian factory burden, 120-day ruins and harbor mission. | No separate tag in first pass. | UNESCO Kilwa source available; no final asset in manifest. |
| `comorian_sultanates` | Indian Ocean | Island passage and ocean diwan dossier. Island convoy, naval access, and Madagascar/Swahili bridge. | 35 PP, convoys, 90-day island passage mission. | IOC authority hook; no direct tag first. | Manifest Low for Zanzibar/Comoros lead because the clean flag source is too late. |
| `great_zimbabwe` | Southern/Zambezi | Stone-city and Great Enclosure dossier. Strong legitimacy and construction/logistics reward, no invented monarchy. | 45 PP, civilian factory burden, 140-day stone-city mission. Objective: control/protect Zimbabwe plateau state. | STC or ZSC hook possible, but first pass can be state modifier and regional authority. | Manifest Medium lead for Great Zimbabwe photo not locally pulled. UNESCO source supports site and period. |
| `barotse` | Southern/Zambezi | Floodplain court and flood calendar dossier. River crossing, supply, and flood-warning mechanics. | 40 PP, support equipment, 120-day floodplain calendar mission. | LOZ/Barotse tag possible; blocker is country package and final flag/portrait. | Manifest High lead for Lewanika portrait not locally pulled. |
| `merina` | Madagascar/Islands | Red earth kingdom and Rova/highland bureaucracy dossier. Island integration and rice/administration branch. | 45 PP, convoys, support equipment, 130-day highland office mission. Objective: Madagascar access or protected island partner. | MER tag possible from matrix. | Manifest High for Ranavalona III portrait and Medium Merina flag reference. Britannica source supports Merina highland kingdom and irrigation bureaucracy. |

## High-Chaos Gameplay Packages

Implement at least these 8 first. The constants already list 11 packages; this subset is enough to satisfy the 6-package acceptance threshold while leaving room to defer weaker rows.

Every package needs:

- a `special_chaos_country` and/or `actual_nonhuman_country` classification if it spawns a tag;
- exclusion from `is_africa_valid_unifier_candidate`;
- no human ideology party or human leader-name pool;
- institutional or descriptive leader titles only;
- a safe visible explanation that this is explicit fictional/supernatural high-chaos content;
- a non-spawn decision path for games that do not want extra tags.

| Package ID | Safe framing | Gameplay | Costs and failure state | Asset/source status |
| --- | --- | --- | --- | --- |
| `gorilla_highlands` | Explicit nonhuman great-ape polity, not a human population metaphor. | Highland sanctuary, mountain infantry defense, habitat corridors, Great Lakes/Congo diplomacy. | 60 PP, support equipment, habitat trust gate. Failure raises Bestiary Alarm and closes recruitment bonus. | Generated or neutral high-chaos art acceptable; no historical asset needed. Existing GHP country/flag files appear present in worktree but must be reviewed by main agent before use. |
| `chimpanzee_marshes` | Explicit nonhuman assembly with no human ethnic analogue. | Recon/sabotage intelligence, forest scouting, riverbank warning missions. | 55 PP, infantry equipment, `africa_habitat_trust` gate. Failure adds Mythic Volatility and disables scouting for 180 days. | Needs generated/fictional package art or neutral icon. |
| `okapi_court` | Explicit nonhuman secret forest court. | Congo Basin stealth diplomacy, hidden route warnings, low-profile observer status. | 55 PP, command power, low Bestiary Alarm gate. Failure creates foreign exploitation incident. | Needs generated/fictional art; no real-human portrait. |
| `crocodile_rivers` | Explicit nonhuman river sovereignty. | Nile/Congo/Zambezi river tolls, crossing defense, flood-route warnings. | 60 PP, support equipment, river-state objective. Failure creates river blockade mission. | Existing CRR country/flag files appear present in worktree but must be reviewed by main agent. |
| `baobab_senate` | Explicit supernatural tree parliament. | Long-memory legitimacy, slower but safer dossier settlement, drought/famine warning flavor where applicable. | 60 PP, civilian factory burden, high Archive Mandate gate. Failure raises Restoration Debt and Mythic Pressure. | Existing BBS country/flag files appear present in worktree; generated/neutral art acceptable. |
| `termite_surveyors` | Explicit nonhuman engineering colony. | Fort, infrastructure, repair speed, and hidden tunnel mission with hard caps. | 55 PP, support equipment, steel/industrial gate if usable. Failure causes local infrastructure damage/state repair mission. | Needs generated/fictional icon. Do not use infestation horror framing. |
| `tidemark_dominion` | Explicit supernatural water-court, separate from real coastal communities. | Indian Ocean storms/tide warnings, convoy protection, island diplomacy. | 65 PP, convoys, Bestiary Alarm below threshold. Failure causes port disruption mission. | Existing TDM country/flag files appear present in worktree; must be reviewed. |
| `ananse_ledger` | Explicit mythic/supernatural trickster ledger, not a human group. | Counterfeit detection, spy/cipher bonus, forgery crisis interception. | 60 PP, agency/intelligence gate if DLC-safe, Archive Mandate gate. Failure causes forged dossier scandal. | Existing ANW country/flag files appear present in worktree; must be reviewed. |

Follow-up status: the later country-package tranche implemented explicit actor surfaces for `chimpanzee_marshes`, `okapi_court`, `termite_surveyors`, `honeyguide_commons`, and `great_herds`; `orisha_vodun_nature_courts` already has an explicit actor package. The expanded actors also have package-specific target actions and local action-report events. Remaining Bestiary depth work belongs in disaster events, settlement hooks, and longer package-specific consequence chains, not in deferring these catalog entries.

## Decision and Mission Families To Replace Thin Decisions

The current thin decisions are:

- `africa_open_next_historical_dossier`
- `africa_unlock_bestiary_package`

Keep them only as parent-approved generic maintenance surfaces if the parent explicitly wants a generic path. The main playable layer should be these families.

### 1. Select Authority Dossier

Surface: `africa_authority_atlas_category`

Pattern:

- Decisions select a macro-region and a dossier ID.
- Store `africa_selected_dossier_id`.
- Show selected dossier name through existing scripted localisation.
- Enforce active cap from `africa_authority_atlas.active_dossier_cap_early/mid/late`.

Costs:

- 10-20 PP for selection only.
- No value reward until survey or mission completion.

Objectives:

- Use visible conditions: region lane focus completed, dossier not opened, no active mission for this dossier.

### 2. Survey Old Seat

Surface: targeted state or targeted country decision.

Pattern:

- Starts a 90-140 day timed mission depending on dossier terrain.
- Sets `africa_dossier_<id>_survey_active`.
- On success sets `africa_dossier_<id>_surveyed`, adds small `africa_old_seat_legitimacy`, and unlocks settlement.

Costs:

- 25-45 PP.
- 200-700 infantry equipment or 50-120 support equipment depending package.
- Convoys for coastal/island dossiers.
- Trucks/trains for Sahel, Lake, Zambezi, and Congo corridors where appropriate.

Objectives:

- Own/control relevant state, have protected partner in relevant area, or complete a foreign-holder case file.
- Failure if state is lost, target capitulates, or Bestiary/forgery crisis interrupts.

### 3. Charter Local Office

Surface: decision unlocked after survey.

Pattern:

- Creates observer/protected office without tag spawn.
- Adds regional trust and local sovereignty.
- Reduces coercion risk for later living-core work.

Costs:

- 35 PP.
- 1 civilian factory for 60-90 days if the engine surface is practical; otherwise use stability/PP/support-equipment cost.

Objectives:

- No active rebellion/resistance flag for that dossier.
- Not on direct-rule settlement path.

### 4. Raise Local Guard

Surface: mission or decision tied to surveyed dossier.

Pattern:

- Spawns limited defensive units or adds equipment/manpower to protected member.
- Use strict caps per macro-region and per dossier.

Costs:

- 300-900 infantry equipment.
- 50-120 support equipment.
- 1,000-4,000 manpower.
- Command power gate for military routes.

Objectives:

- Guard mission must defend a state, port, corridor, or monument for 90-180 days.
- Failing the defense raises Restoration Debt or Colonial Alarm.

### 5. Protect Regalia, Monument, or Archive

Surface: timed mission.

Pattern:

- Package-specific mission for Asante, Benin/Edo, Kush/Meroe, Aksum, Great Zimbabwe, Kilwa, Merina, Luba, Kuba if later used.
- Avoid "loot artifact" gameplay.

Costs:

- 30-45 PP.
- Support equipment.
- Civilian factory burden or stability hit.

Objectives:

- Hold/protect site.
- Prevent forged or foreign-holder exploitation.
- Reward is legitimacy/trust, not free factories.

### 6. Settlement Fork

Surface: decision after survey plus one completed mission.

Options:

- Observer Seat: low authority, high trust, no tag spawn.
- Protected Seat: medium trust, defensive tie, possible subject tag if package exists.
- Regional Authority Office: high authority and integration support, medium sovereignty.
- Direct Archive Seal: fast integration, high Restoration Debt and resistance risk.
- Reject Counterfeit Claim: closes forged branch, raises trust, lowers immediate authority.

Costs:

- 40-70 PP.
- Route-specific value gates:
  - Respect route: `africa_regional_trust` and `africa_old_seat_legitimacy`.
  - Federal/direct route: `africa_authority` and `africa_league_cohesion`.
  - Military route: `africa_liberation_momentum` and command power.

Objectives:

- Require surveyed dossier.
- Require no active forgery crisis.
- Require local area not controlled by a hostile non-African holder unless doing a foreign-holder case.

### 7. Forgery and Museum Crisis

Surface: timed negative missions, triggered by fast queueing or low trust.

Pattern:

- If the player opens too many dossiers without surveys or settlements, start `africa_forged_dossier_crisis`.
- Ananse Ledger can intercept once unlocked.
- Direct Archive Seal route creates stronger but riskier crisis.

Costs:

- Crisis response costs PP, stability, agency/intelligence if available, or support equipment.

Objectives:

- Resolve within 90 days or lose Old-Seat Legitimacy and gain Restoration Debt.

### 8. Bestiary Clause Package Missions

Surface: `africa_high_chaos_category`.

Pattern:

- Replace `africa_unlock_bestiary_package` with package-specific unlock missions.
- Use active Bestiary cap 2.
- Each mission has safe explanation text and an opt-out "record but do not spawn" completion path.

Costs:

- 55-70 PP.
- Support equipment/convoys/industrial resources depending package.
- `africa_habitat_trust`, `africa_mythic_pressure`, or `africa_archive_mandate` gates.

Objectives:

- Keep Bestiary Alarm below threshold.
- Complete habitat/protection/disaster-warning objective.
- Failure raises Mythic Volatility and temporarily locks package selection.

## Country Package, Tag, and Blocker Surfaces

The main agent should split dossier implementation into three country-surface classes.

### Class A: No Tag In First Pass

Use decisions, ideas, state modifiers, and local office flags only.

Recommended for:

- `kush_meroe`
- `adal_harar`
- `ajuran`
- `songhai`
- `jolof_wolof`
- `mossi`
- `kanem_bornu`
- `oyo`
- `luba`
- `lunda`
- `bunyoro`
- `swahili_coast`
- `kilwa`
- `comorian_sultanates`
- `great_zimbabwe`

Reason: These need gameplay now, but tags would require country files, flags, leaders, history, cosmetic naming, AI, and map ownership decisions that can easily delay the playable Archive.

### Class B: Possible Historical Subject Tags After Source/Country Review

Use only if the main agent confirms tag availability, flags, localisation, history files, country colors, leaders or institutional councils, AI, and spawn states.

Candidates:

- `asante` -> ASH surface
- `benin_edo` -> EDO surface
- `dahomey` -> DAH surface
- `kongo` -> KNG surface
- `ndongo_matamba` -> protected office or future tag
- `buganda` -> BUG surface
- `barotse` -> LOZ surface
- `merina` -> MER surface

Blockers:

- `common/country_tags/` conflicts must be checked.
- `common/countries/`, `history/countries/`, and `gfx/flags/` must exist for any spawned tag.
- Historical symbol sources must match `docs/assets/012_africa/source_research/manifest.md`.
- Player-facing names must be direct polity names, not generic office names.
- No invented flags for Low-confidence rows without explicit parent approval.

### Class C: High-Chaos Special Tags

The worktree appears to already contain untracked high-chaos and regional files for several tags, including `GHP`, `CRR`, `BBS`, `TDM`, `ANW`, and `OVN`. The main agent must review those files before treating them as implemented.

Required blockers to clear:

- Add or verify country flags and country history.
- Add or verify `is_special_chaos_country` and `is_actual_nonhuman_country` classification.
- Exclude from normal Charter invitations, normal human integration, and normal Africa unifier selection.
- Provide nonhuman/supernatural leader title localisation without human name pools.
- Give each package at least one decision or mission consequence.
- Add AI strategies that prevent early spam and prevent human-route AIs from choosing Bestiary content without Green Covenant/high-chaos route commitment.

## AI and Balance Risks

### Risk: Generic Queue Spam

Current queue logic can open all dossiers with uniform cost and no map objective.

Mitigation:

- Require survey missions before settlement.
- Enforce active dossier caps.
- Add AI weights by macro-region proximity and route.
- Let AI prefer nearby, owned, controlled, allied, or protected areas before distant prestige dossiers.

### Risk: Free Legitimacy Farming

Uniform dossier opening currently gives Old-Seat Legitimacy and Archive Mandate without package-specific obligations.

Mitigation:

- Selection gives no reward.
- Survey gives small reward.
- Settlement gives main reward but adds cost/risk.
- Repeated unfinished surveys increase Restoration Debt.

### Risk: Subject and Unit Explosion

Historical and high-chaos packages can spawn too many subjects or units.

Mitigation:

- Make most historical dossiers no-tag offices.
- Cap local guards per macro-region and dossier.
- Spawn only defensive or template-limited units.
- Use equipment/manpower costs for every armed reward.

### Risk: Direct-Rule Exploit

Central route could convert old seats into quick living cores.

Mitigation:

- Direct Archive Seal increases Restoration Debt and local resistance.
- Living-core completion should require state ownership/control plus integration authority and no unresolved dossier crisis.
- Respect route should be slower but more stable.

### Risk: High-Chaos Unsafe Framing

Nonhuman packages can become coded human caricature if they use ordinary country, leader, or party conventions.

Mitigation:

- Mandatory `AFR_no_seats_for_caricature` focus.
- Use fictional institutional titles.
- Explicitly classify actual nonhuman/supernatural actors.
- Keep historical human polities and nonhuman packages separate in effects, triggers, names, and assets.

### Risk: Performance and World Iteration

Archive maintenance can tempt daily/weekly global scans.

Mitigation:

- Do not add daily or weekly world-iteration on_actions.
- Use targeted decisions and focus/event completions.
- If periodic cleanup is required, ask the parent for permission before adding any all-country on_action.

### Risk: Source-Sensitive Asset Gaps

Several historical packages lack safe asset sources.

Mitigation:

- Use source-backed rows first for portraits and flags.
- For Low-confidence rows, implement gameplay with neutral Archive UI and clear asset blockers.
- Do not invent historical flags.

## Concrete File Touch List For Main Agent

The main agent should expect to touch these files if this addendum is accepted:

- `common/script_constants/012_africa_constants.txt`: add per-dossier cost/duration/category constants, settlement thresholds, crisis thresholds, AI weights, active cap tuning, and package-class IDs. Keep using `constant:...`.
- `common/scripted_effects/012_africa_effects.txt`: add selected-dossier helpers, macro-region unlock helpers, survey start/complete helpers, settlement helpers, guard/office helpers, crisis helpers, high-chaos package effects, and cleanup.
- `common/scripted_triggers/012_africa_triggers.txt`: add per-dossier validity triggers, macro-region triggers, can-survey/can-settle triggers, active-cap triggers, high-chaos safety gates, no-caricature gate, and package-specific blockers.
- `common/decisions/012_africa_decisions.txt`: replace or subordinate generic dossier and Bestiary decisions with Authority Register, survey, local office, guard, regalia/monument, settlement, forgery, and package-specific Bestiary decisions/missions.
- `common/national_focus/012_africa_focus.txt`: add the route families and focus clusters listed above. Existing aggregate focuses can become prerequisites or be kept as early trunk unlocks, but they should not be the final depth.
- `common/ideas/012_africa_ideas.txt`: add or upgrade ideas for Archive Mandate, Old-Seat Legitimacy, Local Sovereignty, Restoration Debt, Mythic Pressure, Nonhuman Sovereignty, Bestiary Alarm, Habitat Trust, and package-specific temporary spirits.
- `events/012_african_union.txt`: add dossier survey events, settlement/refusal events, crisis events, high-chaos incident events, and super-event trigger hooks. Keep final super-event titles/quotes/audio gated by research handoff.
- `common/scripted_localisation/012_africa_scripted_localisation.txt`: expand dynamic names/status text for selected dossier, selected high-chaos package, settlement path, active mission status, and package safety labels.
- `localisation/english/012_african_union_l_english.yml`: add player-facing names, descriptions, tooltips, mission text, event text, effect descriptions, and safe high-chaos explanation. Preserve UTF-8 BOM.
- `interface/` and `common/scripted_guis/` if the selected-target Authority Register UI is implemented now: add selected dossier widgets, active cap counters, mission cards, and Bestiary warning panel.
- `interface/*.gfx` and `gfx/interface/...`: register dossier icons, macro-region icons, Bestiary icons, and neutral Archive placeholders before final art replacement.
- `common/country_tags/`, `common/countries/`, `history/countries/`, `gfx/flags/`, and `common/characters/` only for accepted spawned subject/tag surfaces.
- `common/ai_strategy/` or existing AI strategy surfaces: add route-specific AI preferences, dossier proximity weights, settlement weights, and Bestiary route controls.
- `docs/assets/012_africa/source_research/manifest.md` and asset handoff docs: update only when new source/asset work is completed.
- `docs/events/012_africa_foundation.md` and accepted specs/matrices: update after implementation so docs match gameplay.
- Spreadsheet rows only after gameplay/localisation are implemented and wording is final.

## Research Basis

Local source basis:

- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/prompts/012_africa_coding_prompt.md`
- `docs/specs/012_africa_specs/specs/012_africa_focus_tree_plan.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
- `docs/specs/012_africa_specs/specs/012_africa_evolutions_world_end_and_scenarios.md`
- `docs/specs/012_africa_specs/specs/012_africa_niche_country_expansion.md`
- `docs/specs/012_africa_specs/specs/012_africa_high_chaos_absurd_paths.md`
- `docs/specs/012_africa_specs/matrices/012_africa_expanded_subject_matrix.md`
- `docs/specs/012_africa_specs/matrices/012_africa_absurd_high_chaos_routes_matrix.md`
- `docs/assets/012_africa/source_research/manifest.md`

External historical cross-checks used for package grounding:

- UNESCO World Heritage Centre, Aksum: https://whc.unesco.org/en/list/15/
- UNESCO World Heritage Centre, Archaeological Sites of the Island of Meroe: https://whc.unesco.org/en/list/1336/
- UNESCO World Heritage Centre, Great Zimbabwe National Monument: https://whc.unesco.org/en/list/364/
- UNESCO World Heritage Centre, Ruins of Kilwa Kisiwani and Ruins of Songo Mnara: https://whc.unesco.org/en/list/144/
- Britannica, Kanem-Bornu: https://www.britannica.com/place/Kanem-Bornu
- Britannica, Songhai empire: https://www.britannica.com/place/Songhai-empire
- Britannica, Asante empire: https://www.britannica.com/place/Asante-empire
- Britannica, Oyo empire: https://www.britannica.com/place/Oyo-empire
- Britannica, Buganda: https://www.britannica.com/place/Buganda
- Britannica, Uganda Bunyoro and Buganda: https://www.britannica.com/place/Uganda/Bunyoro-and-Buganda
- Britannica, Merina: https://www.britannica.com/topic/Merina
- The Metropolitan Museum of Art, Benin Chronology: https://www.metmuseum.org/essays/benin-chronology

Use these as grounding only. Package implementation still needs local state IDs, tag review, source-rights review for art, and final wording review.
