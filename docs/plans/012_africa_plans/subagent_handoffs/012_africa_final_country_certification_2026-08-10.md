# Event 012 Africa final country-package certification

Date: 2026-08-10

Disposition: **PARTIAL — source/runtime country surfaces are present, but the strict country-package acceptance gate remains blocked.**

This is a read-only completion audit of the current shared worktree. No gameplay source, map, asset, localisation, tag, country, history, or documentation file other than this handoff was changed. No file was staged or committed. The user waived live Hearts of Iron IV validation; that waiver is recorded as a limitation rather than a source defect.

## Scope and evidence basis

I read `AGENTS.md`, the required Chaos Redux subagent, event, focus-tree, decisions/missions, event-assets, ComfyUI, and improvement-loop skills, the required offline Paradox wiki pages, the applicable vanilla documentation, and the vanilla country/history/tag precedents under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

The acceptance sources reviewed were `docs/specs/012_africa_specs/README.md`, `PACKAGE_MANIFEST.md`, `matrices/012_africa_polity_catalog.csv`, `matrices/012_africa_host_country_playbook_matrix.csv`, `matrices/012_africa_priority_member_package_matrix.csv`, `matrices/012_africa_focus_route_payoff_matrix.csv`, `matrices/012_africa_asset_animation_matrix.csv`, `matrices/012_africa_ai_profile_matrix.csv`, `matrices/012_africa_achievement_matrix.csv`, the related notes/diagrams/research/prompts, and all 809 rows of `docs/plans/012_africa_plans/012_africa_acceptance_ledger.csv`.

The latest country, focus, priority, promoted Tier A, RSA, asset/animation, localisation, AI/probability, W4, W5, achievement, decision, and world-order handoffs dated 2026-08-09 or 2026-08-10 were read as evidence, not treated as automatic certification.

Required read-only HOI4 MCP routes were used for the country-linked focus, event, map, and technology surfaces. No map rewrite or focus rewrite was attempted from this audit.

## Executive certification result

| Acceptance surface | Current source/runtime result | Strict status | Evidence and reason |
| --- | --- | --- | --- |
| Host playbooks | 22 full implemented; 26 compact implemented; `basutoland`, `swaziland`, and `zanzibar` blocked | **PARTIAL** | 48/51 ledger rows are `implemented`; three exact no-state/no-fallback rows remain `blocked`. |
| Six promoted Tier A packages | EBX/EHX/DPX/EEX/DFX/DHX on states 900/768/298/548/460/448+661 | **SOURCE-COMPLETE / CONDITIONAL** | Existing Independence Wave tags and exact state guards are wired; no new tag or substitute state is used. High-chaos, host, sovereign, model/formation, and live receipt gates remain. |
| Sixteen priority members | All 16 have package-aware effects, decisions, ideas, focus overlay, force profiles, parties, sovereign characters, localisation, and cleanup | **BLOCKED** | All 16 `priority_member_package` ledger rows remain `blocked` by formation/release integration, Action 102/host commitment, route/runtime review, origin/receipt validation, and portrait/icon provenance. |
| RSA South Africa branch | SAF Allied branch and optional ESX Republican Nationalist branch are source-wired with dynamic state selection and cleanup | **SOURCE-COMPLETE / CONDITIONAL** | Exact states 275, 681, and 719 are guarded; ESX has no fixed fallback and excludes EQX. Live branch receipt remains unverified. |
| Focus payoff matrix | 78 rows are `implemented`; shared continental tree has 276 focuses; priority tree has 8 focuses and 9 connectors | **IMPLEMENTED WITH MCP LIMITATION** | Priority focus inspect/render is clean. Continental render has branch-unaware layout warnings and unrelated global vanilla icon diagnostics. |
| Decision/action matrix | 96 rows implemented; six High Chaos rows gated | **PARTIAL** | `contain_emergent_disease`, `research_disease_countermeasure`, `weaponise_fictional_pathogen`, `awaken_stone_cohort`, `train_gorilla_heavy_infantry`, and `organise_pan_sappers` remain `blocked_with_gate`. |
| AI profiles | 64 rows are source-described and policy-wired | **BLOCKED** | All 64 `ai_profile` ledger rows remain `blocked` pending mandatory probability scenarios, campaign balance, and matrix acceptance. |
| Achievements | 44 owner/trigger families are present | **BLOCKED** | All 44 `achievement` ledger rows remain `blocked` pending positive-owner, disqualifier, cleanup, and scenario acceptance. |
| Polity catalog | 16 priority candidates are implemented as conditional overlays; 199 other candidates remain controlled-pool entries | **PARTIAL** | The 16 named priority rows are `blocked`; the remaining 199 are `queued`, not country packages. |
| Country-linked assets | 84 installed runtime, 28 installed dormant, 117 controlled-pool, 10 runtime-gated | **PARTIAL** | Six Tier A visual packages and eight strange-force identity packages are installed on approved carriers; priority portraits remain source-locked placeholders; optional host overlay art remains controlled-pool. |
| W4/W5/world order | Source protocols, receipts, successor, exile, breakup, and terminal registrars are present | **SOURCE-COMPLETE / ACCEPTANCE-BLOCKED** | W4/W5 require live package actor, heartland, sovereign, six-continent, and terminal receipt proofs. W5 does not create tags or transfer territory. |

The strict result is therefore not a country-package completion certificate. It is a source/runtime coverage certificate with explicit unresolved acceptance gates.

## Host playbook row checklist

The exact source mapping is `africa_apply_mapped_host_playbook` in `common/scripted_effects/012_africa_effects.txt:316-375`, with the tag roster and state-signature helpers in `common/scripted_triggers/012_africa_triggers.txt:1-121` and IDs 1–51 in `common/script_constants/012_africa_constants.txt:337-395`.

All 22 full rows are implemented: `ethiopia`, `egypt`, `sudan`, `morocco`, `algeria`, `tunisia`, `libya`, `liberia`, `nigeria`, `gold_coast`, `senegal_fwa`, `sierra_leone`, `belgian_congo`, `angola`, `french_equatorial_africa`, `kenya`, `uganda`, `tanganyika`, `somali_territories`, `madagascar`, `south_africa`, and `southern_rhodesia`.

Twenty-six compact rows are implemented: `portuguese_guinea`, `cape_verde`, `gambia`, `cote_divoire`, `dahomey`, `togo`, `french_sudan_mali`, `mauritania`, `niger`, `upper_volta`, `chad`, `cameroon`, `gabon`, `equatorial_guinea`, `sao_tome`, `ruanda_urundi`, `northern_rhodesia`, `nyasaland`, `mozambique`, `bechuanaland`, `eritrea`, `djibouti`, `mauritius`, `comoros`, `seychelles`, and `reunion`.

The exact compact rows still blocked are:

- `basutoland` on HZX, because the current map has no accepted unique Basutoland state and `africa_is_niche_origin_country` is deliberately disabled rather than given a fallback.
- `swaziland` on EUX, for the same no-unique-current-state reason.
- `zanzibar` on ELX, which remains scenario-only and unbound to an accepted current state.

The niche trigger requires the exact existing Event 006 carrier tag, Event 006 origin/ownership flags, an African capital, and owned, controlled, cored territory; it does not infer a package from a cosmetic tag or a guessed state ID. No fallback host, replacement tag, or map write is authorised by the current design.

## Six promoted Tier A packages

The promoted Tier A carriers are existing Event 006 country identities, not new country tags.

| Package | Carrier | Exact claimed state(s) | Source/runtime result | Remaining acceptance gate |
| --- | --- | --- | --- | --- |
| Pan | EBX (Aro Confederacy) | 900 | Runtime state and package guards present | High-chaos phase, host commitment, sovereign completion, formation/model receipt, AI/probability, live reachability |
| Gorilla Kingdom | EHX (Ankole) | 768 | Runtime state and package guards present | Same gates; state 768 is shared-map territory and must remain collision-free |
| The Green | DPX (Fante) | 298 | Runtime state and package guards present | Same gates |
| Living Rivers | EEX (Bunyoro) | 548 | Runtime state and package guards present | Same gates; no Uganda/EHX collision |
| Stoneborn | DFX (Kabylia) | 460 | Runtime state and package guards present | Same gates |
| Ancient Hosts | DHX (Tripolitania) | 448 capital + 661 extension | Both-state guard, reveal, and cleanup present | Both states must be owned/controlled; no global claim; same high-chaos and model gates |

The exact constants are in `common/script_constants/012_africa_promoted_tiera_constants.txt:8-35`. Carrier predicates are in `common/scripted_triggers/012_africa_promoted_tiera_triggers.txt:33-73`; reveal and cleanup are in `common/scripted_effects/012_africa_promoted_tiera_effects.txt` and `012_africa_promoted_tiera_settlement_effects.txt`.

The six existing country shells and neutral histories are `common/country_tags/006_independence_wave_countries.txt`, `common/countries/006_independence_wave_EBX.txt`, `EHX`, `DPX`, `EEX`, `DFX`, `DHX`, and the matching `history/countries/EBX - Aro Confederacy.txt`, `EHX - Ankole.txt`, `DPX - Fante.txt`, `EEX - Bunyoro.txt`, `DFX - Kabylia.txt`, and `DHX - Tripolitania.txt`.

Each package has a cosmetic identity in `common/countries/012_africa_cosmetic.txt`, a localised public identity, one male fictional sovereign character in `common/characters/012_africa_fictional_characters.txt`, bounded AI strategy in `common/ai_strategy/012_africa_promoted_tiera.txt`, package-specific decisions/events/focus/ideas, strange-force consumers, and defeat cleanup. The six fictional leaders use personal/regnal names and `gender = male`; no council or group portrait is used.

The asset ledger marks the six country package rows `country_package_pan_high_chaos`, `country_package_gorilla_kingdom`, `country_package_the_green`, `country_package_living_rivers`, `country_package_stoneborn`, and `country_package_ancient_hosts` as `installed_runtime`, but the owning visual handoff still treats portrait/model provenance and final runtime review as worker-owned gates. This audit does not promote those rows beyond the ledger disposition.

## Sixteen priority-member row checklist

The priority implementation is a shared country-package overlay, not sixteen newly created country tags. Registration, origin, package IDs, politics, ideas, force profiles, League/refusal/counterproposal paths, overlap settlement, lawful departure, rivalry, and cleanup are in `common/scripted_effects/012_africa_priority_member_effects.txt`, `common/scripted_triggers/012_africa_priority_member_triggers.txt`, `common/scripted_effects/012_africa_priority_member_character_effects.txt`, and `common/scripted_effects/012_africa_priority_member_force_effects.txt`.

| Package | Existing carrier/origin | Current state evidence | Country-package result |
| --- | --- | --- | --- |
| Asante | DOX | State 274 current-map anchor | Overlay is source-wired; ledger row is `blocked`; Action 102 and portrait receipt remain required |
| Oyo | DSX | State 558 current-map anchor | Overlay is source-wired; ledger row is `blocked`; Action 102 and portrait receipt remain required |
| Sokoto | SOK vanilla carrier | Carrier/origin path; no unique state claim in current acceptance | Overlay is source-wired; ledger row is `blocked`; host commitment and Action 102 remain required |
| Kanem-Bornu | DUX | State 901 current-map anchor | Overlay is source-wired; ledger row is `blocked`; Action 102 and portrait receipt remain required |
| Manden | MLI vanilla carrier | Origin marker path; no unique state claim in current acceptance | Overlay is source-wired; ledger row is `blocked`; host commitment and Action 102 remain required |
| Kongo | COG vanilla carrier | Existing `COG_kingdom_of_kongo` cosmetic identity path; no new state | Overlay is source-wired; ledger row is `blocked`; host commitment and Action 102 remain required |
| Buganda | UGA vanilla carrier | Carrier/origin path; no unique state claim in current acceptance | Overlay is source-wired; ledger row is `blocked`; host commitment and Action 102 remain required |
| Aksum | TIG vanilla carrier | Origin marker path; no unique state claim in current acceptance | Overlay is source-wired; ledger row is `blocked`; host commitment and Action 102 remain required |
| Harar | HAR vanilla carrier | Carrier/origin path; no unique state claim in current acceptance | Overlay is source-wired; ledger row is `blocked`; host commitment and Action 102 remain required |
| Kilwa | EMX | No accepted unique current-map state | Overlay is source-wired but dormant/gated; ledger row is `blocked`; no substitute state/tag is allowed |
| Nubia | SUD vanilla carrier | Origin marker path; no unique state claim in current acceptance | Overlay is source-wired; ledger row is `blocked`; host commitment and Action 102 remain required |
| Luba | DYX | No accepted unique current-map state | Overlay is source-wired but dormant/gated; ledger row is `blocked`; no substitute state/tag is allowed |
| Lunda | DZX | No accepted unique current-map state | Overlay is source-wired but dormant/gated; ledger row is `blocked`; no substitute state/tag is allowed |
| Great Zimbabwe | ZIM vanilla carrier | Origin marker path; no unique state claim in current acceptance | Overlay is source-wired; ledger row is `blocked`; host commitment and Action 102 remain required |
| Merina | MAD vanilla carrier | Carrier/origin path; no unique state claim in current acceptance | Overlay is source-wired; ledger row is `blocked`; host commitment and Action 102 remain required |
| Zulu | EQX | State 719 current-map anchor | Overlay is source-wired; ledger row is `blocked`; Action 102 and portrait receipt remain required |

The seven Event 006 niche histories are DOX, DSX, DUX, DYX, DZX, EMX, and EQX. SOK, COG, UGA, HAR, MAD, MLI, TIG, SUD, and ZIM resolve to vanilla tag/history definitions under `common/country_tags/00_countries.txt` and `history/countries/` in the installed game; Event 012 does not add duplicate country shells for them.

All sixteen characters in `common/characters/012_africa_priority_member_characters.txt` have `gender = male`, one named sovereign ID, and a large portrait reference. Localised names include Prempeh I, the Alaafin, Siddiq Abubakar III, Shehu Sanda Kura, Mansa Musa, Pedro VII Afonso, Daudi Cwa II, Haile Selassie I, Emir Abdullahi, Khalifa bin Harub, Abd al-Rahman al-Mahdi, Albert Kalonji, Mwaantayaav Mbaku Citend, Lobengula, Radama II, and Dinuzulu kaCetshwayo.

The priority package has three explicit political routes through shared installers: neutrality/council, democratic/civic, and communist/producer. Each package gets its own party names, leader role, lifecycle ideas, mechanic track, force profile, League disposition, overlap settlement, post-settlement actions, and cleanup. No package-specific advisor, high-command, or commander roster is required by the current matrix; the absence is intentional rather than an untracked missing file.

The shared focus overlay is `africa_priority_member_focus_tree` in `common/national_focus/012_africa_priority_member_focus.txt`. `africa_priority_member_ensure_focus_tree_loaded` preserves a meaningful carrier focus tree and only loads the eight-node shared overlay on safe carriers; it sets an explicit skipped flag when the carrier tree must be preserved. The design does not promise sixteen separate focus trees.

## Country tag, history, startup, release, and map surfaces

No Event 012 country tag file exists and no new country tag was introduced. Existing Event 006 tags are registered in `common/country_tags/006_independence_wave_countries.txt`; vanilla carriers remain vanilla. The source explicitly forbids tag switching as a substitute for a missing state or package receipt.

Promoted Tier A shells are neutral and absent from the start, with runtime territory, capital, politics, forces, ideas, focus, AI, and cosmetic identity assigned only after the exact high-chaos reveal gate. Priority packages remain on the existing carrier tag and carrier flag; Action 102 and the host/formation/receipt conditions are the admission path.

The current map inspection covered all six promoted bindings, the exact priority anchors and candidate states, RSA states, and the bounded ESX candidate range: `900, 768, 298, 548, 460, 448, 661, 274, 558, 901, 902, 556, 782, 898, 899, 295, 538, 718, 769, 719, 275, 681, 893, 894, 895`.

The current `hoi4_map_inspect` returned `MAP_INSPECTED` with 25 states, `unknownProvinceIds=[]`, and `missingGeometryProvinceIds=[]`; map files, state definitions, bitmap, state-region membership, networks, and adjacencies passed. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f95a3b31b739c76917df72537d3e60a9ac2c8fb753c9c9d4099fcb1a9e0ab24c/8b40a37cf5ad8fefd06c379f588178ea076e9924bddeb2576b7dd125049e55d9/map-inspect.17d3c6af4f7bb226.json`.

The map validation remains false only because the workspace reports unrelated global `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics from `mod:map/buildings.txt`; no Event 012 country state in the inspected set has an unknown province or missing geometry. No map write was made.

The remaining state risks are semantic rather than geometry failures: COG wider historical notes mention states 888–890 outside the bounded current scan, and DYX/Luba, DZX/Lunda, and EMX/Kilwa have no unique current-map admission in their dormant niche histories. These are parent-owned state-admission decisions, not safe grounds for a guessed fallback.

RSA uses the exact current SAF core/port corridor in `common/scripted_triggers/012_africa_rsa_triggers.txt`: state 275 must be owned and controlled, while 681 and 719 must be owned, controlled, and have a naval base. The optional ESX branch saves one deterministic valid state after the war, excludes capital/ports/EQX, and never uses a fixed fallback.

## Politics, parties, leaders, portraits, flags, advisors, and localisation

Priority party and leader installation is in `common/scripted_effects/012_africa_priority_member_character_effects.txt`; the direct vanilla-carrier recruitment branches are in `events/012_africa_priority_member_events.txt`. The three constitutional installers always call the sovereign-role installer after settlement. A prior stale handoff note said the Zulu description “awaits an eligible sovereign”; the current `localisation/english/012_africa_priority_member_characters_l_english.yml:144` describes Dinuzulu as the active sovereign, so that predecessor note is not a current source defect.

All sixteen priority GFX registrations in `interface/012_africa_priority_member_characters.gfx` point to existing `_source_locked.dds` files under `gfx/leaders/012_africa/priority_members/`. The files exist, but they are explicit source-locked placeholders rather than accepted grounded source/rights/HOI4-style final portraits. This is a blocking asset/provenance issue for all sixteen priority country rows; runtime must not point into the durable archive as a substitute.

The six promoted fictional GFX registrations in `interface/012_africa_leaders_fictional.gfx` point to existing ImageGen DDS variants under `gfx/leaders/012_africa/fictional/`. They are male personal/regnal actors and not council/group portraits. The owning portrait/asset handoffs still retain provenance and final runtime review as a worker-owned gate, so this audit records the files as present but does not erase that gate.

RSA has the grounded male leader `King Mgolombane Sandile` and portrait `GFX_portrait_012_africa_rsa_mgolombane_sandile` from the archived source master `docs/assets/portraits/012_africa/source_master_rsa_mgolombane_sandile_archival.jpg`, registered in `interface/012_africa_rsa_portraits.gfx` and installed at `gfx/leaders/012_africa/rsa/portrait_012_africa_rsa_mgolombane_sandile.dds`. The remaining RSA uncertainty is branch reachability and live acceptance, not a missing source file.

Priority packages reuse carrier flags and do not define sixteen new cosmetic identities. `common/countries/012_africa_cosmetic.txt` contains RSA, continental route identities, and the six promoted Tier A identities. Flags and emblems for the six promoted packages are present in the Tier A visual package; priority-member promotion and distinct-mechanic icon rows are installed/dormant according to the asset ledger.

The final localisation audit reports 4,569 unique Event 012 keys across 20 YML files and 46 scripted-localisation names, with no missing source references in the inspected set. Country names, adjectives, parties, leaders, advisors where used by shared systems, ideas, focuses, decisions, missions, cosmetic identities, debug names, and W4/W5 public names are covered. Localisation completeness does not override the blocked priority portrait and ledger gates.

No Event 012 country package adds an advisor, high-command, or commander roster. The current matrix and source use sovereign characters, shared action/idea systems, and carrier-owned leaders; adding an advisor roster would be an unapproved identity expansion.

## Focus, decision, idea, equipment, technology, and asset surfaces

The priority focus MCP inspect returned `FOCUS_INSPECTED` for `africa_priority_member_focus_tree` with 8 focuses, 9 connectors, zero crossings, zero node intersections, zero long connectors, and zero tree diagnostics. Render artifacts are:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61ff2f86f475c748c79565617cfcc83383167267c5dae3614b5737eec14020bc/70676f24560f9093ddbe181e5cf7c5498c29fad580f0f14df39f9a877481e24c9/africa_priority_member_focus_tree.focus.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64ff52a12478e69cad0499d65a5470c2bc87e68bee5df574218e0b4356cafda6/9401c97d08ea9f7b24c487a8033ab02459d8f0ee5f1517e8433db47f0f05c15e/africa_priority_member_focus_tree.focus.svg`
- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7b5e8be08120d936ab079c3ca5727aa1477707782b4d7c409837ec7f18a812b/2317d385c9afa3e730e847505c36d33ed66707d95cf76dd499f6985110c6d3bd/africa_priority_member_focus_tree.focus.html`

The shared continental focus MCP render returned 276 focuses and 348 connectors. It has authored same-row spacing and branch-unaware conditional overlay crossing warnings, plus 14 unrelated global vanilla continuous-focus icon errors; the Event 012 focus IDs and localisation were not missing. The current source-level census found 276 unique focus IDs and zero dangling prerequisite IDs. Artifact JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/209696102fde60d96feda351d505cd5e76c628e74e0b64cbed1a55f5f8ef0c7d/998b77d1dc94d9addc128879f9cc121417ca9ec45fd4ac41a7f83cf629584e8f/africa_continental_focus_tree.focus.json`.

The 78 `focus_payoff` rows in the acceptance ledger are all `implemented`; the visible country gap is not a missing focus anchor. AI route weights remain under the probability-owner gate described below.

Priority decisions are in `common/decisions/012_africa_priority_member_decisions.txt`; promoted decisions/events are in `common/decisions/012_africa_promoted_tiera_decisions.txt` and `events/012_africa_promoted_tiera_events.txt`; the RSA branch uses `common/decisions/012_africa_rsa_decisions.txt` and `events/012_africa_rsa.txt`. Shared host and action decisions are in `common/decisions/012_africa_decisions.txt`.

Priority lifecycle ideas are in `common/ideas/012_africa_priority_member_ideas.txt`; promoted and host ideas are in their package files. Ideas replace the starting problem and route/mature state rather than stacking indefinitely. The source does not create a country-specific technology tree for each priority member.

The shared elephant bridge is implemented through `common/technologies/012_africa_elephant_technologies.txt`, `common/units/equipment/012_africa_elephant_equipment.txt`, `common/units/012_africa_elephant_forces.txt`, and `common/scripted_effects/012_africa_elephant_effects.txt`. `africa_elephant_unlock_warfare` grants vanilla `elephantry` and `chaosx_africa_elephant_warfare_tech`; member preparation seeds `chaosx_elephant_equipment_1` and the shared guard formation. Custom equipment entries are present in `common/script_enums.txt`.

Priority force setup uses five structural division-template profiles and named primary/reserve formations in `common/scripted_effects/012_africa_priority_member_force_effects.txt`. The effects are under package/formation gates and scale equipment/manpower rather than adding a large unconditional starting army. Starting carrier technology, production, stockpiles, fuel, trains, convoys, ports, railways, and supply remain carrier-owned and require parent scenario balance review.

The asset ledger rows most relevant to country surfaces are:

- `country_package_pan_high_chaos`, `country_package_gorilla_kingdom`, `country_package_the_green`, `country_package_living_rivers`, `country_package_stoneborn`, and `country_package_ancient_hosts`: `installed_runtime`.
- `country_package_asante`, `oyo`, `sokoto`, `kanem_bornu`, `manden`, `kongo`, `buganda`, `aksum`, `harar`, `kilwa`, `nubia`, `luba`, `lunda`, `great_zimbabwe`, `merina`, and `zulu`: `installed_dormant`.
- Controlled-pool candidate rows `garamantes`, `songhai`, `mossi`, `futa_toro`, `futa_jallon`, `ife`, `edoland`, `dahomey`, `bamum`, `ndongo`, `matamba`, `kazembe`, `kuba`, `kush`, `makuria`, `alodia`, `adal`, `ajuran`, `bunyoro`, `rwanda`, `burundi`, `zanzibar`, `comoros`, `mutapa`, `rozwi`, `mthwakazi`, `swazi`, `basotho`, `barotse`, and `sakalava`: `deferred_controlled_pool`.
- `unit_identity_elephant_logistics` and `unit_identity_elephant_shock`, plus `unit_identity_gorilla_heavy_infantry`, `unit_identity_pan_sappers`, `unit_identity_stone_cohorts`, `unit_identity_riverborn`, `unit_identity_forest_giants`, `unit_identity_oracle_recon`, `unit_identity_disaster_wardens`, and `unit_identity_plague_carriers`: `installed_runtime`.
- `host_overlay_federal_amalgamation`, `host_first_proof_state_kit`, and `priority_member_promotion_card`: `installed_runtime`; `priority_member_distinct_mechanic_icons`: `installed_dormant`.
- `host_overlay_sovereignty_treaty`, `host_overlay_invasion_resistance`, `host_overlay_concession_resource`, `host_overlay_land_settlement`, `host_overlay_corridor_island`, and `host_legacy_post_unification_card`: `deferred_controlled_pool`.
- `focus_family_ancient_host`, `focus_family_scramble_diplomacy`, `focus_family_scramble_defence`, `focus_family_high_chaos_nature`, `focus_family_high_chaos_nonhuman`, `focus_family_high_chaos_disease`, `focus_family_continent_sponsorship`, `focus_family_continent_union`, `focus_family_terminal_continent_war`, and `focus_family_the_world`: `deferred_runtime_gated`.

The 18 animation rows have authored frames, runtime DDS, GFX registration, contact sheets, and consumers according to `012_africa_animation_acceptance_final_2026-08-09.md`; this confirms country-linked presentation assets but does not close country identity or AI acceptance.

The Technology Tree Viewer route is not exposed by the installed HOI4 package. `hoi4_tech_inspect mode=scan refresh=true` returned a partial 663-technology scan with deferred helper projections and no independent viewer render/compare route. This is an evidence limitation, not a justification to claim a country technology tree complete.

## AI, playability, formable behavior, and diaspora ownership

Country and route policy code is present in `common/scripted_effects/012_africa_ai_profile_effects.txt`, `common/scripted_triggers/012_africa_ai_profile_triggers.txt`, `common/ai_strategy/012_africa_promoted_tiera.txt`, the priority focus `ai_will_do` blocks, and the host/route AI helpers. The six promoted packages have bounded package strategies; priority members have package-aware focus and decision preferences; host playbooks have route-aware dispatch.

The acceptance ledger nevertheless marks all 64 `ai_profile` rows `blocked`. A narrow previous probability inspect of the promoted strategy returned `PROBABILITY_SURFACE_EMPTY`; the mandatory `chaosx_ai_probability_auditor` must run baseline and compare scenarios through `hoi4.probability_inspect`/`hoi4.probability_compare` before any AI completion claim. This audit made no AI weight change and did not invent a balance target.

The source has dynamic action 24 (`form_regional_federation`) and action 89 (`form_dynamic_two_continent_union`) with explicit consent, compatibility, identity, faction, cleanup, and achievement owners. There is no new standalone Event 012 formable country-tag suite; dynamic constitutional/cosmetic identities are the accepted formable behavior. Any request for additional country tags or a broad formable suite is outside this narrow audit and remains unimplemented by design.

The diaspora ownership protocol is in `common/scripted_effects/012_africa_diaspora_effects.txt`, `common/scripted_triggers/012_africa_diaspora_triggers.txt`, and `events/012_africa_diaspora_protocol.txt`. It stores host/target ledgers, local ownership share, capacity, consent, owner counterterms, withdrawal generations, and cleanup; it explicitly does not transfer ownership, create tags, scan the world, or infer consent from opinion/ownership. Country package routes therefore link to diaspora only through explicit owner-response and action receipts.

## W4, W5, world-order, and country links

W4 source ownership is in `common/scripted_effects/012_africa_world_union_war_effects.txt`, `common/scripted_triggers/012_africa_world_union_war_triggers.txt`, `events/012_africa_world_package_union_war.txt`, and `localisation/english/012_africa_world_union_war_l_english.yml`. The existing `africa_world_commit_package_successor` remains the sole successor transfer owner; successor, exile, breakup, bilateral union, registered continental war, and terminal cleanup are not duplicated by country overlays.

W4 requires an installed package actor, sovereign completion, proven heartland, compatible factions/constituents, and explicit settlement receipts. A priority or promoted carrier therefore cannot enter W4 merely because its tag, cosmetic identity, or source overlay exists.

W5 source ownership is in `common/scripted_effects/012_africa_world_order_effects.txt`, `common/scripted_triggers/012_africa_world_order_triggers.txt`, and the latest `012_africa_world_w5_certification_fix_2026-08-09.md`. The frozen candidate array writes seven explicit route/focus/decision/idea/AI/identity/localisation receipts per external candidate; the all-six certificate requires one valid candidate per continent. The W5 registrar does not create tags, mutate identity, or transfer territory.

Terminal presentation registrars write their explicit image/audio/localisation receipts and remain separate from country identity and political proof. The latest W4/W5 source audits are source-complete but not campaign-accepted because the required live actor, sovereign, heartland, six-continent, and terminal receipts have not been observed in a save.

The Event 012 entry event remains `chaosx.nr12.1` in `events/012_african_union.txt`; it branches to the host or RSA path and does not itself certify priority/promoted package completion.

## Acceptance-ledger census

The complete 809-row ledger currently reads as follows.

| Surface | Disposition | Count |
| --- | --- | ---: |
| `action_concept` | `implemented` | 96 |
| `action_concept` | `blocked_with_gate` | 6 |
| `focus_payoff` | `implemented` | 78 |
| `host_playbook` | `implemented` | 48 |
| `host_playbook` | `blocked` | 3 |
| `priority_member_package` | `blocked` | 16 |
| `polity_candidate` | `queued` | 199 |
| `polity_candidate` | `blocked` | 16 |
| `asset_item` | `installed_runtime` | 84 |
| `asset_item` | `installed_dormant` | 28 |
| `asset_item` | `deferred_controlled_pool` | 117 |
| `asset_item` | `deferred_runtime_gated` | 10 |
| `ai_profile` | `blocked` | 64 |
| `achievement` | `blocked` | 44 |

The six blocked action keys are `contain_emergent_disease`, `research_disease_countermeasure`, `weaponise_fictional_pathogen`, `awaken_stone_cohort`, `train_gorilla_heavy_infantry`, and `organise_pan_sappers`.

The sixteen blocked polity keys are `kanem_bornu`, `manden`, `asante`, `oyo`, `sokoto`, `kongo`, `luba`, `lunda`, `nubia`, `aksum`, `harar`, `buganda`, `kilwa`, `great_zimbabwe`, `zulu`, and `merina`; they are the same sixteen priority rows listed above and are not additional country packages.

The achievement ledger contains all 44 matrix rows, including country-linked restoration, priority promotion, diaspora, W4, W5, high-chaos, and terminal achievements; none is promoted to accepted in this strict audit. The AI ledger contains all 64 matrix rows; none is promoted to accepted without the mandatory probability pass and scenario evidence.

## MCP evidence and limitations

`hoi4_focus_inspect` and `hoi4_focus_render` were run for the priority and continental trees. The priority tree is structurally clean; the continental tree is complete at source level but has renderer geometry warnings and unrelated global vanilla continuous-focus icon diagnostics. The focus rewrite route was not used for a gameplay patch.

`hoi4_map_inspect` was run for the 25 country-linked/promoted/RSA states listed above and returned no unknown province or missing geometry IDs. The map render validated the inspected state layer; the only false validation flag came from unrelated global building/port locator diagnostics.

`hoi4_event_inspect` and `hoi4_event_render` were run from the canonical `chaosx.nr12.1` selector. Both returned partial projections because inline workspace files were truncated; blocking diagnostics were zero in the current event projection, but unresolved helper/lifecycle nodes remain an MCP evidence limitation.

`hoi4_tech_inspect mode=scan refresh=true` returned a partial technology scan. No Technology Tree Viewer or independent technology render/compare route is exposed by the installed package, so technology evidence is source-plus-scan only.

No Hearts of Iron IV process was launched and no in-game screenshot, save, or live receipt is claimed, per the explicit user waiver and repository policy.

## Missing, stale, blocked, or intentionally deferred surfaces

- The three compact host rows `basutoland`, `swaziland`, and `zanzibar` have no accepted unique current-map state and must remain fail-closed; no fallback tag or state is authorised.
- All 16 priority package ledger rows remain blocked despite broad source coverage; the ledger is the current acceptance authority and must not be silently rewritten to `implemented`.
- All 16 priority sovereign GFX endpoints use `_source_locked.dds`; grounded provenance, rights, identity/framing review, and accepted final portrait receipts are missing from strict country certification.
- DYX/Luba, DZX/Lunda, and EMX/Kilwa have dormant/no-unique-state admission risk; COG wider state notes 888–890 were outside the bounded map selection.
- Carrier-owned starting military, stockpiles, production, research, fuel, supply, and industry were not replaced with country-specific starting setups; the package effects add gated forces and ideas rather than inventing a new balance shell.
- No package-specific advisors, high-command roster, or separate priority focus tree per country exists because the current design intentionally uses shared package-aware overlays.
- Six High Chaos action families are runtime-gated, all AI rows are probability/acceptance-blocked, and all achievement rows are owner/disqualifier/cleanup acceptance-blocked.
- W4/W5/world-order source registrars are present but require live package actor, sovereign, heartland, six-continent, and terminal receipts.
- The Technology Tree Viewer route is unavailable; source scan cannot be reported as independent viewer certification.

## Changed files, commits, and parent handoff

Only this read-only handoff was created: `docs/plans/012_africa_plans/subagent_handoffs/012_africa_final_country_certification_2026-08-10.md`.

No gameplay file, map, asset, localisation, spreadsheet, tag, country definition, history, or AI file was changed. No commit or stage operation was performed.

Parent action required: retain the overall Event 012 completion status as partial/blocked until the ledger dispositions, portrait provenance, three dormant host decisions, mandatory AI probability comparisons, achievement ownership checks, and user-owned live W4/W5/package receipts are explicitly closed.
