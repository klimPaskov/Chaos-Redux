# Event 012 Africa achievement implementation handoff

> Release-candidate correction (2026-07-29): all 44 achievement icon triplets are installed as 132 DDS files, and every row below now records `triplet installed`. Owner-system milestone and disqualifier callsite review remains open.

## Status

The complete 44-row achievement matrix has 44 registered definitions, 44 completion triggers, one English name/description/tooltip triplet per row, central thresholds, normal-launch eligibility, successor-safe lifetime ledgers, live member proof, duration deadlines, and explicit positive and disqualifying conditions. The 2026-07-29 callsite audit classifies 27 rows as REACHABLE/PARTIAL, 9 as ACTIVE/BLOCKED, 4 as MODEL-GATED, and 4 as WORLD-GATED. All 44 remain blocked and none has a completion claim.

The common runtime hooks for initial host registration, action start, full and failed action resolution, immutable diaspora parameters, protection-war starts and settlements, Scramble expedition defeat, continental-war victory and settlement, post-unification sponsorship, negotiated two-continent integration, terminal-formation evidence, pre/post unification snapshots, valid RSA succession, and Tier A player-origin validation are integrated. The callsite audit still finds missing positive owners for restoration, maritime, Horn, development, reserve, weather, and terminal super-event rows, together with many result-specific disqualifier and cleanup writers. Those calls must be made by the owning system when each result becomes final.

All 44 unique three-state DDS sets are installed as 132 DDS files under `gfx/achievements/`. They are not a substitute for the remaining owner-system milestone and disqualifier callsite review.

## Implementation surfaces

- `common/achievements/chaos_redux_achievements.txt`
  - Event 012 block: lines 3415-3659 at final audit time (concurrent registry work shifted the original append downward without changing the Event 012 block).
  - Identifiers: the 44 `achievement_key` values from `012_africa_achievement_matrix.csv`, in matrix order.
  - At the Event 012 append boundary, the first 103,846 pre-existing bytes of the shared registry were preserved byte-for-byte; the Event 012 section was appended after the then-current Event 019 block. Concurrent registry additions account for the later line shift above.
- `common/script_constants/012_africa_achievement_constants.txt`
  - Counts, durations, ratios, region/origin/program/corridor/unit/terrain/restoration enums, and bounded profile/milestone inputs.
- `common/scripted_effects/012_africa_achievement_effects.txt`
  - Normal-host and successor registration, action ledgers, live relationship-registry counts, deadline clocks, formation/Scramble snapshots, parameterised proof helpers, terminal credits, and disqualifier/reset hooks.
- `common/scripted_triggers/012_africa_achievement_triggers.txt`
  - Common eligibility plus exactly 44 `<achievement_key>_is_complete` triggers.
- `localisation/english/012_africa_achievements_l_english.yml`
  - UTF-8 BOM, no `:0`, direct public names, and no forced-return content.

## Integrated runtime hooks

| Owning surface | Integrated call | Required scope and ordering |
|---|---|---|
| `012_africa_effects.txt` | `africa_achievement_initialize_normal_host = yes` | Current normal host after the opening state and host commitment exist. Forced scenario setup does not call it. |
| `012_africa_achievement_effects.txt` | `africa_achievement_record_initial_host_profiles = yes` | Called by normal-host initialization to freeze communist, authoritarian, monarchical/restored, and coastal launch eligibility before later government changes. |
| `012_africa_action_effects.txt` | `africa_achievement_record_action_start = yes` | Action target immediately after immutable action-record creation. |
| `012_africa_action_effects.txt` | `africa_achievement_record_full_action = yes` | Action target after full action semantics and before active-record cleanup. |
| `012_africa_action_effects.txt` | `africa_achievement_record_action_outcome = yes` | Action target after full, partial, or failure semantics; records coercion and failure disqualifiers and audits burden, confidence, confederal ceiling, and diaspora trust. |
| `012_africa_action_effects.txt` | Diaspora parameter snapshot | Player GUI or AI selects one of four origin or skill enums; the value is copied into the immutable active action record, validated, consumed only on full completion, and cleared with the record. |
| `012_africa_world_order_on_actions.txt` | Protection, expedition, member-capitulation, continental-war, and settlement helpers | Pairwise war/capitulation/peace hooks only; no daily, weekly, monthly, or unbounded country iteration. |
| `012_africa_world_order_effects.txt` | Sponsorship, negotiated union, and terminal-formation helpers | Called only at fulfilled-package identity, compatible union commit, and ready-gated Africa-owned world identity barriers. |
| `012_africa_focus_route_effects.txt` | `africa_achievement_capture_pre_unification_food_snapshot = yes` | Host immediately before committing `africa_is_one`. |
| `012_africa_focus_route_effects.txt` | `africa_achievement_capture_africa_is_one_snapshot = yes` | Host immediately after the final relationship/formation state exists. |
| `012_africa_rsa_effects.txt` | `africa_achievement_register_valid_host_successor = yes` | Valid exile patron during the one-use host transfer. Global lifetime ledgers remain intact. |
| `012_africa_priority_member_effects.txt` | `africa_achievement_register_valid_priority_player = yes` | Human Tier A start or authorised switch after origin validation. |
| `012_africa_focus_route_effects.txt` | `africa_achievement_record_host_profile = yes` | Records the voluntary-League profile when Continental Confederation is actually committed. |
| Achievement action hook | `africa_achievement_capture_scramble_settlement_snapshot = yes` | Called automatically after a full `break_intervention_coalition` result, after its ordinary semantics. |

Duration achievements do not use a daily, weekly, or monthly world iteration. A meaningful action/milestone starts or resets a central deadline, and the achievement trigger compares `global.num_days` to that deadline directly. Live member counts iterate only the host-owned `africa_relationship_countries` registry.

## Remaining authoritative API

These calls are deliberately not guessed from presentation flags. Initial host profiles and the voluntary Confederation route are integrated at their authoritative launch and route-commit barriers; any later host-monarchy restoration must call the same profile API only when that restoration becomes final.
- A completed regional result can set `africa_achievement_region_id` plus `africa_achievement_region_proof_id`, then call `africa_achievement_record_region_proof = yes`. Normal full actions already record representation, overlap, republic institution, worker/peasant representation, food, connection, and development evidence when the action target owns a valid overlay.
- A completed restoration sets `africa_achievement_restoration_identity_id` and calls `africa_achievement_record_restoration_identity = yes`.
- Settlement owners set `africa_achievement_milestone_id` and call `africa_achievement_record_milestone = yes` for Nile overlap/corridor, Savanna overlap/common order, a nonhuman great-power victory, recognition of the priority-member alternative confederation, Stoneborn constitutional status, or a weather-war victory.
- Diaspora origin waves and skill programmes are integrated through action rows 52 and 54. Project ownership helpers remain authoritative for locally controlled investments not represented by the shared action result.
- Pairwise hooks integrate last-convoy settlement, protection wars, expedition/intervention defeat, member capitulation, continental-war victory, and continental settlement. Reserve, weather-army, and elephant owners still call their helpers only after the named deadline, capital-control, terrain, supply, and victory evidence is final.
- Sponsorship, negotiated union, and Africa-owned terminal formation are integrated at their actual commit barriers. The terminal super-event owner must still call `africa_achievement_record_world_terminal_super_event` only after the fully researched and wired super-event fires.
- Existing explicit disqualifier helpers cover coercive annexation, broken guarantees, member capitulation, congress expulsion/coerced accession, member cascade, burden/confidence/ceiling breach, forced relocation, trust collapse, network split, concession breach, ecological bargain breach, nonhuman-rights violation, other world ends, and forced scenarios. Other matrix-specific terminal owners must set the identically named `africa_achievement_*` disqualifier flag at the authoritative failure transition.

## Row-by-row coverage and disposition

The direction cells below retain their original visual wording while every row now records its exact 2026-07-29 callsite-audit classification and the installed three-file art disposition. Owner-system proof and disqualifier callsites remain open unless the audit identifies a safe package gate.

Every icon entry below maps to the installed three-file set `gfx/achievements/<key>.dds`, `gfx/achievements/<key>_grey.dds`, and `gfx/achievements/<key>_not_eligible.dds`. No `.gfx` registration is required for custom achievement IDs. Presence of the triplet does not close the row's gameplay proof or owner-system callsite.

| # | Achievement key | Gameplay proof and remaining dependency | Callsite audit classification | Icon direction and disposition |
|---:|---|---|---|---|
| 1 | `africa_guardians_without_borders` | Full guarantee actions count distinct independent partners; protection-war helpers and the Africa-is-One live snapshot prove survival/settlement. Annexation, destruction, or broken-guarantee owners must call the matching DQ hook. | REACHABLE/PARTIAL | Open shield around distinct state seals — triplet installed. |
| 2 | `africa_last_convoy_home` | Action-start proof requires surrender progress above 80%; full corridor and `record_last_convoy_war_settlement` prove 180-day survival plus independence/victory. War owner must call settlement or DQ. | REACHABLE/PARTIAL | Train and ship entering a defended gate — triplet installed. |
| 3 | `africa_no_empty_promises` | Guarantee ledger plus Africa-is-One live high-confidence snapshot; voluntary/confederal route is live/profile proof. Coercive-annex/broken-guarantee hooks remain authoritative. | REACHABLE/PARTIAL | Unbroken chain joining shield clasps — triplet installed. |
| 4 | `africa_the_interveners_left` | Full coalition-breaking action writes Scramble victory, one expedition defeat, and the hostile-state snapshot. Capitulation/partition owners set DQs. | REACHABLE/PARTIAL | Broken expedition helmet before continental shield — triplet installed. |
| 5 | `africa_archive_of_the_living_state` | Evacuation actions plus `record_archive_restoration` count three independent/autonomous restorations. Destruction, sale/suppression, and later annexation require the matching DQ transition. | REACHABLE/PARTIAL | Archive chest carried past a burning capital — triplet installed. |
| 6 | `africa_twelve_empty_chairs_filled` | `record_congress_agenda_completed` verifies 12 live full members before starting the 365-day deadline; member-loss/expulsion/coerced-accession resets are exposed. Congress owner must call the agenda helper. | REACHABLE/PARTIAL | Twelve linked chairs around a charter seal — triplet installed. |
| 7 | `africa_the_clause_is_the_country` | Full-action clause records, dispute-resolution flag, and Africa-is-One member snapshot prove ten members with three clauses. Clause cancellation/untracked annexation owners set DQs. | REACHABLE/PARTIAL | Layered charter sheets beneath linked seals — triplet installed. |
| 8 | `africa_exit_without_war` | Exit action records the start; `record_peaceful_reassociation` proves 720 days and consensual associate/ally return. War/coup/coerced-return owner sets DQ. | REACHABLE/PARTIAL | Open gate returning a seal — triplet installed. |
| 9 | `africa_no_second_capital` | Monitor action starts a per-rival clock; arbitration/defection counts only resolutions within 180 days. Annexation/terminal-coercion owner sets DQ. | REACHABLE/PARTIAL | Two seals before a divided map — triplet installed. |
| 10 | `africa_every_region_speaks` | Full congress/representation and overlap actions record each valid overlay; formation requires all nine of both proof sets. Region-loss/unresolved owner sets DQ. | REACHABLE/PARTIAL | Nine regional emblems around a speaking staff — triplet installed. |
| 11 | `africa_confidence_is_contagious` | Host relationship registry counts 15 live high-confidence members; low burden starts a 720-day deadline. Cascade, annexation, burden, and confidence transitions use exposed hooks/live checks. | REACHABLE/PARTIAL | Radiating member seals — triplet installed. |
| 12 | `africa_federation_by_consent` | Live federal route plus formation snapshot proves 12 autonomous-federal members with representation and fiscal settlement. Military/covenant/coercion owners set DQs. | REACHABLE/PARTIAL | Federal seals and ballots — triplet installed. |
| 13 | `africa_republic_of_many_capitals` | Regional congresses record distinct republican institution regions; election/succession actions activate succession; five-year deadline is direct. Suspension/centralisation/military-transition owners set DQs. | REACHABLE/PARTIAL | Five civic buildings linked by a republic star — triplet installed. |
| 14 | `africa_crowns_at_one_table` | Monarchical/restored profile, recognised-court helper, crown succession action, Council route, and formation snapshot prove eight courts. Court deposition/abolition owners set DQs. | REACHABLE/PARTIAL | Distinct crowns around a congress table — triplet installed. |
| 15 | `africa_union_of_work_and_land` | Socialist profile, People’s route, worker-region proof, per-state socialised processing, food proof, and three-year deadline are implemented. Takeover/private concession/famine owners set DQs. | REACHABLE/PARTIAL | Hammer, field, and rail seal — triplet installed. |
| 16 | `africa_order_without_partition` | Military profile/route, `record_major_intervention_defeated`, representation action, and postwar/commander review prove bounded emergency rule. Genocide/partition/permanent-rule owners set DQs. | REACHABLE/PARTIAL | Sheathed sword beside open charter — triplet installed. |
| 17 | `africa_confederation_that_endured` | Live sovereign relationship count, live burden ceiling, Scramble result, and ten-year deadline are implemented. Federal-annexation/cascade owners set DQs. | REACHABLE/PARTIAL | Loose ring of flags around shield — triplet installed. |
| 18 | `africa_covenant_with_the_impossible` | Registered high-chaos actors receive rights/obligations only through the constitutional-member helper; three live members start five-year peace. Rights/rampage/disease owners set DQs. | MODEL-GATED | Human charter joined to forest, stone, animal emblems — triplet installed. |
| 19 | `africa_kings_of_the_savanna` | Restoration enum counts Luba/Lunda/Kuba once; milestone API records settled overlaps and common order. Court annexation/destruction owners set DQs. | ACTIVE/BLOCKED | Three distinct court regalia motifs — triplet installed. |
| 20 | `africa_nile_has_many_memories` | Restoration enum counts Kush/Nubia/Makuria/Alodia once; Nile milestone API records overlap and corridor proof. Erasure/failure/capital-dispute owners set DQs. | ACTIVE/BLOCKED | Layered river, crown, and court silhouettes — triplet installed. |
| 21 | `africa_ports_of_the_monsoon` | Distinct maritime-polity helper, per-state port actions, coastal/overlay eligibility, active access, and three-year deadline are implemented. Port-loss/shortcut owners set DQs. | ACTIVE/BLOCKED | Dhow linking six port seals — triplet installed. |
| 22 | `africa_walls_courts_and_caravans` | Live Aksum/Harar package triggers and exact priority flags are consumed; restoration identities and operational-corridor flag start one-year peace. Package war/abolition/corridor-loss owners remain authoritative. | ACTIVE/BLOCKED | Fortified wall, stela, and caravan — triplet installed. |
| 23 | `africa_the_old_gold_roads` | Three plateau identity proofs, processing counts, local ownership, five-year deadline, and exact Great Zimbabwe package flags are consumed. Annexation/corridor/foreign-majority owners set DQs. | ACTIVE/BLOCKED | Stone enclosure, gold, and rail — triplet installed. |
| 24 | `africa_member_who_said_no` | Exact Tier A player origin, live refusal flag, rival-bloc victory, four-member count, independence, and recognised-alternative milestone are required. Puppet/League-destruction/high-chaos owners set DQs. | ACTIVE/BLOCKED | Small restored seal before broken chain — triplet installed. |
| 25 | `africa_return_without_compulsion` | Voluntary-wave helper records eight waves and four origins; citizenship action and live trust finish proof. Forced relocation/disaster/discrimination owners set DQs. | REACHABLE/PARTIAL | Families approaching an open civic gate — triplet installed. |
| 26 | `africa_tools_books_and_ballots` | Skill-program enum requires all four families; project actions count twelve; citizenship convention protects representation. Labour-only/denial/trust-collapse owners set DQs. | REACHABLE/PARTIAL | Book, medical bag, wrench, ballot, passport — triplet installed. |
| 27 | `africa_four_oceans_homeward` | Origin-group array requires all four exact groups from voluntary route calls. Catastrophic-loss/forced-relocation owners set DQs. | REACHABLE/PARTIAL | Four routes converging on port and rail hub — triplet installed. |
| 28 | `africa_capital_without_capture` | Distinct local diaspora projects, live local-ownership threshold, and ten-project count are implemented. Government-capture/corruption owners set DQs. | REACHABLE/PARTIAL | Coin and factory held in an open hand — triplet installed. |
| 29 | `africa_rails_rivers_roads_and_ports` | Rail, river, and port project actions plus the member-capital road connection record all four corridor enums; failure outcomes record a network split and regional connection proof starts the 720-day access deadline. | REACHABLE/PARTIAL | Four transport systems crossing one seal — triplet installed. |
| 30 | `africa_ore_leaves_as_machines` | Per-state resource/processing counts, live concession share, and five-year deadline are implemented. Dependency/breach/seizure owners set DQs. | REACHABLE/PARTIAL | Ore entering furnace and leaving as machinery — triplet installed. |
| 31 | `africa_bread_before_banners` | Food actions record all nine regions and reserves; pre-unification snapshot enforces ordering; drought action proves survival. Famine/early-formation/civilian-wrath owners set DQs. | REACHABLE/PARTIAL | Grain store and water beneath folded banner — triplet installed. |
| 32 | `africa_development_without_overstretch` | Unique state/action projects, all-nine-region proof, live burden/confidence, and 720-day deadline are implemented. Breach/collapse/scandal owners use hooks/DQs. | ACTIVE/BLOCKED | Scales holding factory and village — triplet installed. |
| 33 | `africa_common_reserve_answers` | Distinct defended-partner helper counts six deadline/capital-safe defensive responses. Deadline/capital/offensive-abuse owners set DQs. | ACTIVE/BLOCKED | Reserve standard before six shields — triplet installed. |
| 34 | `africa_no_foreign_boot_remains` | Full Scramble victory performs a one-time African-state controller snapshot and requires zero hostile non-African control. Core cession/unreversed capitulation/external puppet owners set DQs. | REACHABLE/PARTIAL | Empty bootprint beside spear and shield — triplet installed. |
| 35 | `africa_beasts_but_not_caricatures` | Four unique nonhuman formation families, constitutional-rights helper, and nonhuman great-power victory milestone are required. Caricature/extermination/rights-removal owners set DQs. | MODEL-GATED | Four impossible silhouettes under constitutional standard — triplet installed. |
| 36 | `africa_elephants_crossed_the_desert` | Elephant formation, unique terrain enum including desert, supply proof, and protection-victory helpers are implemented. Formation/supply/abuse owners set DQs. | MODEL-GATED | Armoured elephant with rail and water drums — triplet installed. |
| 37 | `africa_the_forest_kept_its_word` | Distinct ecological bargains and disaster containments plus live wrath start five-year deadline. Broken-bargain helper exists; weaponisation/rampage owners set DQs. | REACHABLE/PARTIAL | Living canopy forming protective arch — triplet installed. |
| 38 | `africa_rain_on_command` | Distinct hostile-army weather helper counts three; weather-war milestone proves victory. Member-disaster/neutral-target/wrath-collapse owners set DQs. | ACTIVE/BLOCKED | Storm held by an oracle staff — triplet installed. |
| 39 | `africa_disease_made_and_unmade` | Disease actions prove branch/create/countermeasure; outbreak and containment helpers maintain exact active count. Uncontrolled/irreversible/terminal owners set DQs. | REACHABLE/PARTIAL | Sealed vial beside restored leaf — triplet installed. |
| 40 | `africa_stone_walks_into_parliament` | Stoneborn milestone records identity/constitutional status and starts five-year deadline after rights/obligations. Rights/war/erasure owners set DQs. | MODEL-GATED | Stone figure beside charter tablet — triplet installed. |
| 41 | `africa_another_continent_stood_up` | Post-unification sponsor action, identity helper, friendly proof, and five-year deadline are implemented. Collapse/puppet/betrayal owners set DQs. | WORLD-GATED | Two continent emblems linked by open bridge — triplet installed. |
| 42 | `africa_two_continents_one_name` | Negotiation/formation actions plus exact integration helper start five-year medium-confidence deadline. Forced submission automatically marks conquest-only; confidence/civil-war owners set DQs. | WORLD-GATED | Two continent silhouettes in one civic seal — triplet installed. |
| 43 | `africa_war_between_worlds` | Continental-war victory and settlement helpers start the three-year no-revolt deadline. Debug surrender/global-revolt owners set DQs. | WORLD-GATED | Two continental emblems and broken spear — triplet installed. |
| 44 | `africa_the_world_is_one` | Final world-formation helper records last eligible actor, all valid rival resolutions, world identity, and Africa-owned world end; terminal super-event helper is separate. Other-world-end/unresolved-identity owners set DQs. | WORLD-GATED | Single globe-scale final seal — triplet installed. |

## Icon manifest requirement

All 44 icon concepts come directly from the achievement matrix. Each final triplet must be 64x64 DDS under `gfx/achievements/`, use the achievement key as the filename stem, and contain purpose-built eligible, grey, and not-eligible states. Reusing an unrelated achievement image, omitting one state, or supplying a transformed placeholder is not accepted.

## Satisfiability and identifier audit

- Matrix rows: 44; registry entries: 44; completion triggers: 44; duplicate Event 012 IDs: 0.
- Registry keys not in matrix: 0; matrix keys not registered: 0.
- Visible/hidden mismatch: 0; hidden rows: 21 exactly as specified.
- Missing `_NAME`, `_DESC`, or `_tooltip` keys: 0.
- Declaration-level positive flag and helper references resolve, but runtime callsite reachability is governed by the row-complete 2026-07-29 audit.
- All 179 referenced script constants resolve to a declared category/key.
- All custom scripted effect/trigger calls in the achievement files resolve to a definition.
- Duration deadline predicates avoid recurring world scans, but rows whose start writer is absent remain unreachable as documented by the callsite audit.
- Priority-member dependencies resolve to the current exact identifiers in `012_africa_priority_member_effects.txt` and `012_africa_priority_member_triggers.txt`.
- The HOI4 MCP lint request was blocked by `ARTIFACT_STORAGE_LIMIT`; it produced no scan or validation result. Source-level audits above remain the available evidence.

## Simplifications, omissions, and blockers

- All 44 unique achievement icon triplets are installed. No fallback art was used.
- The common reserve, elephant route, weather-army proofs, restoration milestone families, and terminal super-event still require their owning gameplay systems to call the exact helper or set the exact DQ flag identified above. Until those owners wire every applicable transition, the affected achievement is not completion-ready in play.
- No criteria, rows, thresholds, routes, visibility settings, localisation entries, or public names were simplified.
