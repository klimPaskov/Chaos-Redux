# Event 025 improvement-loop addendum

## Status and disposition

This is the independent precision pass requested by the Event 025 package closure review.

The package is already broad enough. Another route family, public meter, country package, formable, focus branch, or super-event would add bloat rather than improve the race. The useful work is to make the accepted race, sectors, evolutions, shared reward contracts, privacy rules, and achievements concrete enough that implementation does not have to invent them.

No earlier Event 025 improvement-loop addendum was found unresolved. The existing closure note explicitly left this independent pass open, so this addendum resolves that gate rather than stacking a second plan over an accepted design.

This document is plan-only. It does not claim that the inspected in-progress Event 025 source, Event 016 API extension, Event 036 ledger, Expedition Board, assets, achievements, or audits are implemented.

Working labels in this document are design labels, not final localisation.

## Evidence boundary

### Repository evidence

The complete package under `docs/specs/025_alien_technology_in_antarctica_specs/` was reviewed, including its specifications, matrices, research notes, asset material, prompts, handoffs, acceptance criteria, and checksum ledger. The ledger matched every listed package file.

The source snapshot inspected on 2026-08-29 included the legacy Event 025 implementation and an in-progress replacement at `events/025_alien_technology_in_antarctica.txt`. The replacement already points in the right direction by selecting AI participants after the human entry window, storing a bounded participant registry, scheduling participant-scoped pulses, and reserving coherent event ranges. It is not evidence of completion: the associated helpers, constants, decisions, GUI, localisation, shared reward adapters, and audits were not all present in the inspected snapshot.

The live Event 016 custom-technology API has seven base families and eleven upgrades. Its existing random helper chooses only among missing base families and can legitimately do nothing once every base family is held. It has no generic valid-upgrade selector, no full-pool `Alien Systems Integration` arbitration result, and no complete selected-result metadata contract.

The live Event 036 reward grants jet technology and aircraft, records `brilliant_scientist_alien_spacecraft_recovered`, and schedules Event 016 contact. It has no shared Event 025/Event 036 overlap ledger. The current jet reward cannot be called an exact duplicate of an Event 016 base family without an accepted domain mapping.

The stable compatibility idea `antarctica_success` is already read by Event 016. The rework must preserve that exact identifier and continue to call `brilliant_scientist_try_schedule_alien_artifact_contact` after a valid recovery.

The live Kruger State support is real. The narrow AI exception should use `brilliant_scientist_is_active_kruger_state = yes`, not a brittle direct `tag = KRG` check.

### Historical and public-source grounding

The six-sector design below uses real expedition methods and route memories without pretending that a 1930s government possessed a modern Antarctic territorial grid.

- The British Antarctic Survey describes Operation Tabarin as a wartime mission that combined strategic presence, weather work, and bases at Deception Island and Port Lockroy. This grounds the Graham Coast sector's station, radio, and South Atlantic access play. Source: [BAS, Operation Tabarin](https://www.bas.ac.uk/about/history/operation-tabarin/).
- The Australian Antarctic Program describes BANZARE's 1929–1931 voyages, the use of the *Discovery*, seaplane flights, coastline work, science, and claims. This grounds the Mac Robertson Soundings sector's mixed maritime, aerial, and magnetic methods. Source: [Australian Antarctic Program, BANZARE 1929–31](https://www.antarctica.gov.au/about-antarctica/history/exploration-and-expeditions/banzare-1929-31/).
- The Smithsonian records Byrd's *Stars and Stripes* aircraft as part of the first Antarctic expedition's aerial photography and radio-supported work. This grounds the Ross Barrier sector's aviation-heavy survey identity. Source: [Smithsonian National Air and Space Museum, *Stars and Stripes*](https://www.si.edu/object/fairchild-fc-2w2-stars-and-stripes%3Anasm_A19720533000).
- The Australian Antarctic Program's account of Antarctic wireless describes relay stations, masts, weather failures, and the difficulty of maintaining links. This grounds signal evidence, communications exposure, and false confidence rather than a magic radar reveal. Source: [Australian Antarctic Program, The wireless of Wireless Hill](https://www.antarctica.gov.au/about-antarctica/history/communications/the-wireless-of-wireless-hill/).
- The Norwegian Polar Institute describes aircraft used for Antarctic mapping from the *Norvegia* expeditions. This grounds the Queen Maud Air Grid's photographic transects and weather-corrupted imagery. Source: [Norwegian Polar Institute, aircraft and Antarctic mapping](https://sorpolen2011.npolar.no/en/did-you-know/2011-12-11-airplanes-were-used-in-the-mapping-of-antarctica.html).
- BAS records the Discovery Investigations as long-running Southern Ocean marine and oceanographic survey work. This grounds Weddell Drift hydrographic and ice-edge evidence. Source: [BAS, history of BAS ships](https://www.bas.ac.uk/about/history/history-of-bas-ships/).
- BAS records the British Graham Land Expedition's surveying and geological work and its clarification of local geography. This grounds cross-checked traverse evidence and the risk of charts being wrong without making one whole sector a joke. Source: [BAS, British research stations and refuges](https://www.bas.ac.uk/about/history/british-research-stations-and-refuges/).
- The Australian Antarctic Program preserves magnetic, meteorological, auroral, and radio records from the Australasian Antarctic Expedition. This grounds the Adélie Static Field's magnetic and radio methods. Source: [Australian Antarctic Program, scientific collections and data](https://mawsonshuts.antarctica.gov.au/national-heritage/scientific-collections-and-data/).

These sources support expedition methods, route identities, and institutional flavor. The alien wreck, six-sector arrangement, and gameplay effects are design inferences. The design must not import the Antarctic Treaty system into a pre-1959 setting.

### Mandatory MCP evidence blocker

The configured `hoi4_agent_tools` server is registered in `.codex/config.toml`, but this planner's own callable inventory exposes none of the required event, GUI, map, technology, or probability routes. The required read-only probability work was therefore routed through `chaosx_ai_probability_auditor`.

The auditor could call `hoi4.probability_inspect`, but every schema-valid source attempt either timed out after 180 seconds or returned `PROBABILITY_SOURCE_NOT_FOUND` with `filesScanned: []`. An initial string-source probe was rejected as `Invalid input: expected object, received string at source`. No probability artifact, source revision, scenario hash, analysis ID, comparison ID, or probability render URI was produced. The MCP workspace exposed only the legacy Event 025 `ai_chance`, decision `ai_will_do`, deterministic target scan, and unweighted `random_army_leader`; it did not expose an implemented participant, route, action, rival, evolution, six-sector, or technology-reward pool.

The auditor did obtain partial `hoi4.event_inspect` evidence:

- workspace: `mod_chaos_redux_ea3b2d67c2c0`
- result: `EVENT_INSPECTED_PARTIAL`
- artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78994e7f7a2e75b0b3d341f3b7d14beb2873c17a9c656971f288389332efa31d/0453bc42eeabaec8edfc1e152758e6e11b61d729ad8b01e629ebda1d5f1ae885/event-scan-fc004230aebc.json`
- revision: `fc004230aebc47f013434598a54b3f98da50c59b8fe79c1e1f2272b4eea95d23`
- graph hash: `c1fabf5553ab8381b838193353c1d06a562d2a2cd84de34694915001bef50f72`
- global-scan result: 2,129 diagnostics and 8,327 unresolved nodes

The requested event render was interrupted before completion and produced no artifact. `hoi4.gui_inspect`, `hoi4.gui_render`, and `hoi4.map_inspect` remain unavailable to this planner. No rewrite route was used. Event and Technology Tree Viewers are read-only by contract, and the installed package available to this planner has no Technology Tree Viewer route.

Therefore the event render/compare, GUI render/privacy review, southern-gateway map table, custom-technology graph view, participant weights, random pools, evolution timing, and post-patch probability comparisons remain unresolved engine-evidence blockers. The partial global event scan is not a substitute for a narrow clean Event 025 artifact, and source review is not a substitute for the missing evidence.

The implementation owner must not mark the affected acceptance criteria complete until the routes are callable and the required evidence is captured. If they remain unavailable, the exact blocker must be carried into completion reporting.

## Precision design decisions

### 1. Bounded participant race

The race invites every valid human country. Humans never lose a place to an AI cap, and human entry has no probability gate.

At initialization, Event 025 may perform one world scan to snapshot human invitees and valid AI candidates. After the bounded entry window closes, it must never rescan the world to maintain the race. All recurring work iterates only the stored participant registry.

Use these tuning concepts in `constant:chaosx_nr25_participants.*`:

| Constant | Provisional design target | Purpose |
| --- | ---: | --- |
| `preferred_total` | 6 | Target field size after accepted humans are known |
| `max_ai_participants` | 6 | Hard bound on AI rows and AI pulse work |
| `minimum_starting_participants` | 1 | A lone human can still play the expedition |
| `public_rival_card_count` | 4 | Maximum ordinary rival cards rendered for one viewer |

The exact formula is:

`ai_slots = clamp(preferred_total - accepted_human_count, 0, max_ai_participants)`

If seven or more humans enter, the race adds no AI. The registry capacity is accepted humans plus six AI, so the implementation remains bounded without rejecting multiplayer entrants.

Build the AI candidate pool from valid majors, then add the narrow Kruger exception when `brilliant_scientist_is_active_kruger_state = yes`. Exclude AI-controlled special-chaos or genuinely nonhuman countries unless another accepted narrow exception is documented. Sample without replacement. A country cannot occupy two rows.

Recommended identifiers:

- `global.chaosx_nr25_participants`
- `global.chaosx_nr25_ai_candidates`
- `global.chaosx_nr25_participant_sequence_next`
- `chaosx_nr25_register_participant`
- `chaosx_nr25_build_ai_candidate_pool`
- `chaosx_nr25_select_ai_participants`
- `chaosx_nr25_is_valid_ai_candidate`
- `chaosx_nr25_is_active_participant`
- `chaosx_nr25_invalidate_participant`

AI candidate weighting should recognize route burden, available convoys, fuel, support equipment, civilian factories, research/electronics capacity, competing war pressure, and reserve floors. The Kruger exception changes eligibility, not reward identity or free resources. Its weight should be competitive only when its actual route and reserves justify entry.

The final recovery resolver must be order-independent. Mark all countries that complete a valid final mission on the same date, close that date's candidate set once, and compare this tuple in order:

1. valid final-mission completion state
2. higher verified survey evidence
3. higher Logistics Readiness
4. higher outpost integrity
5. lower Exposure Risk
6. earlier date on which final-recovery readiness was reached
7. earlier stable participant sequence

The participant sequence is the deterministic last tie-breaker. This order resolves the package contradiction in favor of `specs/006_outcomes_rewards_and_aftermath.md` and the deterministic acceptance criterion, superseding the seeded random fallback and ambiguous mission-timestamp priority in `specs/002_expedition_race_system.md`. Do not let event-file iteration order or an unaudited random fallback choose the winner.

### 2. Six-sector survey board

The sectors are six geographic choices on one board. They are not six decisions, six progress bars, or six additional public values. A player selects one sector, then receives three to five context-valid survey methods in the ordinary action tray.

The current in-progress generic labels such as `signal basin`, `magnetic silence`, and especially a dedicated `false map` sector should not become final geography. False coordinates are an incident that can corrupt evidence in any sector; making them a permanent location undermines replayability after the first campaign.

Recommended stable sector enum and working labels:

| Enum | Working label | Historical method identity | Natural gateway bias | Strong evidence channels | Principal hazard |
| --- | --- | --- | --- | --- | --- |
| `ross_barrier` | Ross Barrier | Byrd-style aviation, radio, and inland logistics | Ross Sea / Australasian-Pacific | photographic, ground | crevasse and fuel strain |
| `graham_coast` | Graham Coast | Rymill/Tabarin station network and coastal traverse | South Atlantic | ground, radio-magnetic | exposure, rivalry, false coordinates |
| `weddell_drift` | Weddell Drift | Discovery-style hydrography and pack-ice work | South Atlantic | hydrographic, ground | pack ice and convoy loss |
| `queen_maud_air_grid` | Queen Maud Air Grid | Norwegian-style aerial photographic transects | South Atlantic or southern Indian Ocean | photographic, radio-magnetic | weather-corrupted imagery |
| `mac_robertson_soundings` | Mac Robertson Soundings | BANZARE maritime, seaplane, and magnetic survey | Southern Indian Ocean | hydrographic, photographic, radio-magnetic | distance and mechanical failure |
| `adelie_static_field` | Adélie Static Field | Australasian radio, auroral, and magnetic observations | Australasian-Pacific | radio-magnetic, ground | communications disruption and Evolution I pulses |

These are route biases, never hard locks. A chartered or sponsored expedition can survey any sector by paying its route burden.

Use `constant:chaosx_nr25_sector.*` enum values and these country-scoped families:

- `chaosx_nr25_selected_sector`
- `chaosx_nr25_sector_<sector>_state`
- `chaosx_nr25_sector_<sector>_confidence`
- `chaosx_nr25_sector_<sector>_evidence_ground`
- `chaosx_nr25_sector_<sector>_evidence_photo`
- `chaosx_nr25_sector_<sector>_evidence_radio_magnetic`
- `chaosx_nr25_sector_<sector>_evidence_hydrographic`
- `chaosx_nr25_sector_<sector>_evidence_corrupted`

The sector state ladder is `unvisited`, `sampled`, `probable`, `excluded`, or `confirmed`. Exact confidence and evidence-channel flags belong to the participant country. The hidden primary crash sector belongs to global server state. A sector becomes confirmed for one country only after it reaches the configured confidence threshold and has at least two independent evidence channels. This prevents one lucky roll and makes route/method combinations meaningful.

Recommended survey methods:

- `chaosx_nr25_survey_overland_traverse`: trucks/support equipment, strong ground evidence, readiness risk
- `chaosx_nr25_survey_aerial_photo_grid`: fuel/air capability, strong photographic evidence, weather-corruption risk
- `chaosx_nr25_survey_radio_magnetic_transect`: electronics/support equipment, radio-magnetic evidence, signal exposure
- `chaosx_nr25_survey_ice_edge_soundings`: convoys/fuel, hydrographic evidence, pack-ice risk
- `chaosx_nr25_cross_check_survey_data`: valid partner or intelligence source, converts an independent public/received clue without exposing exact coordinates

Not every method appears in every sector. Each selected sector should expose three or four sensible methods, with a fifth situational action only when a rescue, deception, signal, or fragment incident is active.

The global script may publish broad reports such as unusual activity in a named sector. It must not publish the true crash sector, a country's exact confidence, a hidden evidence channel, or the country that secretly confirmed the site.

### 3. Five independently gated evolutions

The five evolutions are parallel opt-in complications mapped to different chaos tiers. Baseline phases are not evolutions, and no evolution requires a previous evolution to have activated.

Use the existing shared enable checks and distinct state for every evolution:

- `chaosx_nr25_evolution_1_is_enabled` and `events_log_disabled_evolution_25_25_1`
- `chaosx_nr25_evolution_2_is_enabled` and `events_log_disabled_evolution_25_25_2`
- `chaosx_nr25_evolution_3_is_enabled` and `events_log_disabled_evolution_25_25_3`
- `chaosx_nr25_evolution_4_is_enabled` and `events_log_disabled_evolution_25_25_4`
- `chaosx_nr25_evolution_5_is_enabled` and `events_log_disabled_evolution_25_25_5`

Recommended runtime flags are `global.chaosx_nr25_evolution_<n>_eligible`, `_scheduled`, `_active`, and `_recorded`. Do not use one `global.chaosx_nr25_current_evolution` variable; it cannot represent independent combinations such as Evolution II active while Evolution I is disabled.

| Evolution | Independent eligibility | Active-race entry | First-firing entry | No-prerequisite rule |
| --- | --- | --- | --- | --- |
| I: The Ship Is Still Active | Gathering Storm and an active race or pre-fire seed | Signal incidents can begin in any active phase; baseline actions remain valid | Seed nonzero Signal Intensity and alter the opening report | Does not require confirmed wreck or another evolution |
| II: Something Survived | Rising Chaos and an active race or pre-fire seed | May begin once outpost or survey evidence exists | Seed tracks, opened compartments, or a missing survey party | If I is absent, physical evidence alone activates it; no signal dependency |
| III: Antarctica Becomes Militarised | Chaos Tier plus at least two active participants, or a pre-fire militarised opening | Opens escort, blockade, seizure, and de-escalation after ordinary route/outpost gates | AI may enter with escorts and public security claims | If II is absent, rivalry and escorts supply all evidence; no survivor dependency |
| IV: The Wreck Is Breaking Apart | Totalen Chaos plus probable/confirmed site, or pre-fire instability seed | Starts Wreck Integrity and six fragment categories while preserving one core winner | Wreck begins unstable and fragments appear earlier | If III is absent, pulses, ice, time, and extraction stress drive damage; no clash dependency |
| V: The Technology Changes Its Users | World Collapse plus at least one valid alien-material holder | Global milestone records once; country aftermath incidents begin only for holders | Seed warnings and containment opportunities, not instant Dependence ownership | No I–IV prerequisite; Event 025 or compatible Event 036 material is sufficient |

Place separate entries in `common/mtth/025_alien_technology_in_antarctica_mtth.txt`, for example `chaosx_nr25_evolution_1_interval` through `_5_interval`. Use an event-owned scheduled check or incident chain, never a whole-world periodic on-action. The package's approximately 90-day base is a starting target, not accepted balance until `hoi4.probability_inspect`, named scenario evaluation, timing sweeps, seeded simulations, and post-patch comparison are available.

When an evolution is disabled before activation, it must create no gated action, AI weight, incident, state flag, or log record. If a user disables an already active evolution through supported settings behavior, stop future gated incidents and actions but do not reverse casualties, public incidents, fragment transfers, rewards, or historical records that already occurred. Cleanup must leave baseline completion possible.

Evolution V must not gain a sixth main route. The five accepted holder routes remain Contain, Destroy, Transfer, Conceal, and Continue Integration. A rare international commission may exist only as a resolved variant of Transfer Custody when at least three valid participant governments have completed public cooperation and the recipient/custodian contract is valid. Recommended result flag: `chaosx_nr25_transfer_international_commission`. It receives no new public meter, route family, or permanent GUI panel.

### 4. Event 016 owner API reward arbitration

The duplicate-safe technology decision belongs to the Event 016/shared custom-technology owner, not Event 025. Event 025 owns recovery eligibility and its physical aftermath; the custom-technology owner knows the whole grant graph and is reusable by Event 036 and future alien sources.

Recommended public effect:

`chaosx_grant_random_custom_technology_reward`

Required inputs:

- current country scope is the recipient
- `chaosx_custom_technology_reward_source` enum, including Event 025 and Event 036
- optional broad recovery domain enum from the shared alien-recovery ledger
- optional preferred family enum, treated as a weighting hint rather than permission to grant an invalid result

Required outputs, initialized on every call:

- `chaosx_custom_technology_reward_applied`
- `chaosx_custom_technology_reward_kind`
- `chaosx_custom_technology_reward_family`
- `chaosx_custom_technology_reward_upgrade`
- `chaosx_custom_technology_reward_overlap_converted`

Use owner-defined enums in `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt`. The helper must leave a documented failure kind if no valid recipient or source exists; it must never leave stale output from a previous call.

Arbitration order:

1. Build the valid missing-base-family pool from the seven supported base families.
2. If empty, build a pool of valid compatible upgrades for already owned families.
3. If empty, grant the shared `Alien Systems Integration` capstone.
4. If the capstone is already held, apply one documented bounded reinforcement result instead of silently doing nothing.

The eleven current upgrades are not one blind pool. The four xenobiological control upgrades are mutually constrained, so an owner trigger such as `chaosx_can_grant_custom_technology_upgrade` must validate base ownership, incompatible alternatives, prior ownership, and any graph prerequisite before a candidate enters the pool.

The reinforcement result must be modest, once-per-recovery-source, and alien-program-specific. A bounded research bonus or a staged capstone modifier refresh is acceptable only after the Event 016 owner documents the exact result. It must not create Kruger, the Kruger State, Directorate state, Event 016 project history, Event 016 evolution state, free divisions, or unrelated technology.

Event 025 calls the public helper once after winner validation, checks `chaosx_custom_technology_reward_applied`, then sets the stable `antarctica_success` idea/receipt and calls `brilliant_scientist_try_schedule_alien_artifact_contact`. Player text describes an alien-derived field and never exposes an internal technology key or names Kruger as the source.

### 5. Shared Event 036 overlap ledger

The overlap ledger is a neutral alien-recovery integration layer, not an Event 025 private copy and not a rewrite of Event 036.

Recommended shared surfaces:

- `common/script_constants/chaosx_alien_recovery_constants.txt`
- `common/scripted_effects/chaosx_alien_recovery_effects.txt`
- `common/scripted_triggers/chaosx_alien_recovery_triggers.txt`
- `docs/systems/chaosx_alien_recovery_ledger.md`

Recommended public helpers:

- `chaosx_record_alien_recovery`
- `chaosx_alien_recovery_has_exact_overlap`
- `chaosx_select_alien_recovery_conversion`
- `chaosx_record_alien_recovery_conversion`

Country-scoped receipts:

- `chaosx_alien_recovery_event_025`
- `chaosx_alien_recovery_event_036`
- `chaosx_alien_recovery_last_source`
- `chaosx_alien_recovery_domain_<domain>`
- `chaosx_alien_recovery_tier`
- `chaosx_alien_recovery_conversion_used`
- `chaosx_alien_recovery_conversion_source_pair`
- exact reward kind/family/upgrade receipts returned by Event 016

Global state may store only a bounded occurrence count, public first/second-recovery order, and public reaction milestones. Duplicate prevention and reward conversion are country-scoped. Different countries can receive the two events without blocking or upgrading one another.

Event 025 records its recovery even when Event 036 is unavailable. Event 036 later records its aircraft recovery and asks the shared helper whether an exact overlap exists. Preserve `brilliant_scientist_alien_spacecraft_recovered` and the Event 016 contact call when Event 036 is updated.

The Event 036 source currently supports an `airframe` or `jet_aircraft` broad domain only. It is unresolved whether this maps to one Event 016 family, an aircraft upgrade consumer, or a distinct reinforcement result. Do not label it a portal, propulsion, or other exact duplicate until the Event 036 rework and Technology Tree Viewer evidence establish the mapping. `Two Crashes, One Answer` unlocks only when `chaosx_alien_recovery_conversion_used` and an actually applied upgraded/integration result prove conversion.

### 6. GUI and player privacy

The Expedition Board is justified because it combines a selected geographic sector, three public expedition values, rival intelligence, and a context action tray. It remains one Event 025-owned GUI and must be routed to `chaosx_event_ui_worker` only after gameplay helpers and data ownership are stable.

Exact private country state:

- Expedition Progress
- Logistics Readiness
- Exposure Risk, later replaced by Alien Dependence for valid holders
- per-sector confidence and evidence channels
- selected sector and selected rival
- exact mission result and next pulse
- sabotage author and attribution evidence
- exact reward key and hidden survivor profile

Public or intelligence-derived rival state:

- country identity when publicly known
- phase
- progress band
- readiness band
- exposure band only when observable or intelligence-supported
- public outpost/escort/withdrawal incident
- intelligence confidence and report age

Build country-scoped viewer snapshots such as `chaosx_nr25_rival_public_ids`, `chaosx_nr25_rival_progress_band`, `chaosx_nr25_rival_readiness_band`, `chaosx_nr25_rival_exposure_band`, `chaosx_nr25_rival_intel_confidence`, and `chaosx_nr25_rival_report_age`. Do not let the GUI iterate global participant rows and read exact rival variables directly.

Use `dirty = chaosx_nr25_gui_revision` or the verified equivalent. Rebuild only the current viewer after its own action, a public milestone, intelligence refresh, selected-target invalidation, or race resolution. Decorative sector art must not intercept input. Observer countries cannot open the board.

The GUI must show only three equal-status meters. Sector confidence is a label/band on the selected sector; Wreck Integrity and Militarisation are broad global stages; Signal Intensity is a compact visual state. None becomes a fourth peer meter.

Before implementation, `hoi4.gui_inspect` and `hoi4.gui_render` must establish the existing consumer, supported resolutions, click regions, and baseline privacy states. After the event UI worker's bounded implementation, the same states and resolutions require post-change render comparison. The current MCP blocker leaves exact layout acceptance unresolved.

### 7. Achievements

Keep the 14 package achievements and add no more. They are distinct if the implementation records exact proof rather than inferring from final state.

| Stable working ID | Required proof that makes it distinct |
| --- | --- |
| `025_alien_technology_antarctic_vanguard` | winner receipt and successful main reward application |
| `025_alien_technology_long_way_south` | no direct coastal access at entry, chartered/sponsored/improvised route through departure, then victory |
| `025_alien_technology_white_science` | no hostile-action ledger entry before victory |
| `025_alien_technology_nobody_left_on_ice` | a real rival crisis, prevented/reduced loss, unique target, then victory |
| `025_alien_technology_false_map` | deception applied, exposed, pre-deception verified confidence restored, then victory |
| `025_alien_technology_without_escort` | Evolution II or III active, no military escort commitment ever, then victory |
| `025_alien_technology_reclaim_the_station` | involuntary outpost loss, same-country restoration, then victory |
| `025_alien_technology_fragments_of_a_losing_cause` | non-winner at resolution with the highest valid losing fragment tier acquired before winner announcement |
| `025_alien_technology_six_fields_of_debris` | six unique Evolution IV fragment-category receipts with transfer provenance |
| `025_alien_technology_listen_without_answering` | Evolution I, passive remote analysis, no jam/broadcast/amplify action, then victory |
| `025_alien_technology_human_factors` | containment, retained technology, controlled Dependence, and 365 uninterrupted accident-free days |
| `025_alien_technology_system_prefers_us` | integration route, high stable Dependence, retained government/program control, and 730 days |
| `025_alien_technology_two_crashes_one_answer` | both source receipts plus exact overlap conversion plus successful upgraded/integration result |
| `025_alien_technology_first_among_equals` | at least five active outpost-phase participants, two unique pre-recovery data-share targets, then victory |

`Six Fields of Debris` refers to the six fragment categories from Evolution IV, not the six geographic survey sectors. Final name/description/tooltips must make that distinction unmistakable.

Track hostile acts, route identity, crisis/rescue proof, false-map confidence checkpoint, escort use, outpost transitions, signal-policy actions, fragment ownership provenance, accident-free timers, and unique data-share targets before cleanup. Tag switching, annexation, transfer, and save/reload behavior must follow an explicit country-continuity rule. A post-resolution transfer cannot retroactively satisfy a winner or fragment achievement.

Each achievement requires independent normal, grey, and not-eligible DDS art. Reusing a resized decision or idea icon is not acceptable. If any of the 14 routes or DDS triplets is intentionally removed, that is an accepted design change and must be recorded before implementation closure.

## Exact implementation surfaces

### Event 025 owner

| Surface | Responsibility |
| --- | --- |
| `events/025_alien_technology_in_antarctica.txt` | entry, phase reports, incidents, same-day finalist collection, winner/loser reports, evolution events, cleanup dispatch |
| `common/script_constants/025_alien_technology_in_antarctica_constants.txt` | participant bounds, sector/route/phase enums, evidence thresholds, costs, reserve floors, timings, AI target bands |
| `common/mtth/025_alien_technology_in_antarctica_mtth.txt` | five independent evolution intervals and any approved event-owned timing entries |
| `common/scripted_effects/025_alien_technology_in_antarctica_effects.txt` | participant registry, value clamps, sector evidence, missions, rival state, finalist comparator, aftermath, idempotent cleanup |
| `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt` | participant/action/sector/evolution/achievement eligibility and private/public view gates |
| `common/decisions/025_alien_technology_in_antarctica_decisions.txt` | board entry, phase missions, urgent actions, same helpers as AI |
| `common/decisions/categories/025_alien_technology_in_antarctica_categories.txt` | bounded event-owned category and visibility |
| `common/ideas/025_alien_technology_in_antarctica_ideas.txt` | expedition and aftermath lifecycles; preserve `antarctica_success` |
| `common/dynamic_modifiers/025_alien_technology_in_antarctica_dynamic_modifiers.txt` | route/outpost/Dependence state where a combined visible modifier is needed |
| `common/on_actions/025_alien_technology_in_antarctica_on_actions.txt` | registration or narrow country hooks only; no recurring whole-world pulse |
| `common/scripted_guis/025_alien_technology_in_antarctica_scripted_guis.txt` | participant-only view state and actions after helper stabilization |
| `interface/025_alien_technology_in_antarctica.gui` | board layout, sector click regions, cards, bands, confirmations |
| `interface/025_alien_technology_in_antarctica.gfx` | stable Event 025 sprite registrations |
| `common/scripted_localisation/025_alien_technology_in_antarctica_scripted_localisation.txt` | route, sector, public band, fragment field, reward field, winner, and safe unknown text |
| `localisation/english/025_alien_technology_in_antarctica_l_english.yml` | final player-facing event, decision, GUI, achievement, log, detail, and super-event wording |

The implementation must also update the existing shared major-event registration, event-name/debug mappings, Event Details, event/evolution logs, super-event slot selectors, achievement registry, asset manifests, docs, and authoritative event-catalog workbook through their current owner files. Exact shared filenames must be taken from live source at implementation time rather than guessed from this addendum.

### Shared owners

| Owner | Required change |
| --- | --- |
| Event 016 custom-technology API | add `chaosx_grant_random_custom_technology_reward`, compatibility triggers, enums, full output metadata, capstone/reinforcement result, and owner documentation |
| Neutral alien-recovery integration | add the Event 025/Event 036 country ledger and bounded global public occurrence state |
| Event 036 | later record its recovery, preserve current contact receipt, consume the shared ledger, and apply a documented exact-overlap conversion |
| Shared event logs/details | register one opening history row, five independently gated evolution rows, public phase/count/winner details, and sanitized actor state |
| Shared achievements | register all 14 stable Event 025 IDs and testable unlock triggers |

## Dependency and implementation order

1. Restore callable HOI4 MCP inspection routes or record the continuing blocker. Inspect the live event chain, current GUI precedents, gateway map data, and custom-technology graph before owner patches.
2. Freeze participant, route, sector, phase, evolution, recovery-domain, and reward-result enums in constants.
3. Implement and document the Event 016 reward helper and neutral alien-recovery ledger first. Event 025 must consume their public contracts rather than a private copy.
4. Implement the Event 025 participant registry, private country ledger, six-sector evidence model, same-day comparator, five evolution gates, and idempotent cleanup.
5. Implement decisions and AI through the same action helpers and real resource/reserve checks.
6. Run the baseline probability audit before changing weights or timing. The owner selects balance targets; the read-only auditor evaluates them.
7. Implement the Expedition Board through `chaosx_event_ui_worker` after data ownership is stable, with required inspect/render and post-change comparisons.
8. Wire logs/details, achievements, assets, localisation, super-event, documentation, and workbook alignment.
9. Run post-patch probability compare with the same named scenarios, then the decision/mission, localisation, event-completion, and documentation audits.
10. Promote accepted normative design into the Event 025 specifications and record this plan as promoted, queued with a reason, or rejected with a reason before another Event 025 improvement pass.

## Required probability scenarios

The existing package scenarios P01–P15, A01–A10, R01–R06, and T01–T08 remain authoritative and all are unresolved because `hoi4.probability_inspect` produced no usable candidate manifest. Add these named precision checks to the auditor prompt and use the same scenarios for baseline and compare:

| Scenario | Evidence question |
| --- | --- |
| `P16_many_humans_no_ai` | Seven accepted humans produce zero AI participants and no human is removed |
| `P17_ai_sampling_without_replacement` | A valid major cannot occupy two participant rows and invalidated candidates cannot be selected |
| `P18_kruger_exception_reserve_pressure` | Active Kruger eligibility is visible, but sharply inferior reserves keep its selection chance below well-supplied majors |
| `P19_sector_core_uniform_baseline` | With no evolution or route modifier, the six hidden core sectors have the accepted baseline distribution |
| `P20_sector_method_validity` | Invalid survey methods have zero probability and two-channel confirmation is achievable in every sector |
| `P21_independent_evolution_combinations` | Each evolution can activate with all four others disabled; no hidden prerequisite remains |
| `P22_reward_base_pool` | A country missing multiple base families receives only a valid missing base result |
| `P23_reward_upgrade_pool` | A country owning all bases receives only compatible unowned upgrades |
| `P24_reward_full_pool` | A country owning every valid base and upgrade receives capstone, then bounded reinforcement on a later valid source |
| `P25_event_036_both_orders` | Event 025 first and Event 036 first both record source order and convert only exact same-country overlap |
| `P26_same_day_finalists` | Reordering finalist iteration produces the same winner under the comparator |
| `P27_evolution_timing_sweep` | Each evolution's eligibility-to-activation distribution stays inside its accepted campaign pacing band |

Every weighted participant score, route/action choice, rival target, random survivor profile, sector core, fragment category, Event 016 reward pool, and MTTH entry begins with `hoi4.probability_inspect`. Any owner-applied tuning requires `hoi4.probability_compare` under the identical named scenarios.

## Acceptance scenarios added by this pass

### Participant and lifecycle

1. One landlocked human accepts; no AI slot calculation removes it; a chartered route reaches all six sectors at higher burden.
2. Seven humans accept; no AI is selected; every participant receives an initialized private ledger before acting.
3. Two humans and four AI enter; only the participant registry is pulsed after entry closure.
4. An AI candidate becomes invalid between snapshot and selection; it is skipped without a second world scan.
5. An active participant is annexed while selected by a rival; both participant and viewer snapshots clear idempotently.
6. Two final missions complete on the same day; repeated runs and reversed registry iteration produce the same winner.

### Six sectors and privacy

7. Every sector can be confirmed through at least two different valid method pairs; no route family is hard-locked from a sector.
8. A false-coordinate incident corrupts one country's Graham Coast evidence without changing the global true sector or another country's evidence.
9. A country with one high-confidence channel remains at probable rather than confirmed.
10. A public incident updates rival bands but not exact confidence, next pulse, sabotage author, or reward field.
11. Two human clients inspect the same sector and rival; each receives only its own private confidence and intelligence snapshot.
12. An observer cannot open the board or query a participant's view state.

### Evolutions

13. Run five separate campaigns with only one evolution enabled each. Every enabled evolution activates and resolves without another evolution's flags.
14. Run all evolutions disabled. Baseline route, survey, final recovery, reward, and cleanup still complete.
15. Pre-fire Evolution II seeds physical tracks with Evolution I disabled; no signal state is created.
16. Evolution IV activates with Evolution III disabled; ice, extraction, and time alter Wreck Integrity without a military incident.
17. Evolution V activates from compatible Event 036 material before Event 025 resolves; only a valid holder receives country incidents.
18. Disable an active evolution through supported settings behavior; future gated incidents stop, baseline actions remain, and already recorded history is not erased.

### Reward and overlap

19. A winner with no Event 016 family receives one valid base result, `antarctica_success`, and the Event 016 contact scheduling call.
20. A winner with all base families receives one compatible unowned upgrade, never an incompatible xeno control.
21. A winner with the full base/upgrade pool receives `Alien Systems Integration`; a later valid recovery receives the documented reinforcement rather than a silent no-op.
22. Event 025 resolves while Event 036 is unavailable; the Event 025 ledger receipt remains valid and no Event 036 dependency blocks closure.
23. Event 025 first and Event 036 first produce the same exact-overlap conversion for the same country after an accepted Event 036 domain mapping.
24. Different countries receive Event 025 and Event 036; neither is upgraded by the other's receipt.

### Achievements and persistence

25. `Six Fields of Debris` remains locked after surveying all six sectors and unlocks only after six unique fragment-category receipts.
26. `First Among Equals` rejects two exchanges with one country and accepts two distinct pre-recovery targets.
27. `The False Map` restores from the recorded pre-deception confidence checkpoint rather than any arbitrary later threshold.
28. `Two Crashes, One Answer` rejects two non-overlapping rewards and unlocks only after `chaosx_alien_recovery_conversion_used` plus successful reward metadata.
29. Dependence accident timers survive save/reload and reset on a qualifying accident.
30. Save/reload in entry, crossing, outpost, survey, final-candidate, resolved, and Evolution V aftermath states preserves arrays, private sector evidence, source receipts, timers, and one-shot flags.

### GUI and presentation

31. Render every supported resolution with zero, one, four, and more-than-four relevant rivals; no clipping, overlapping click regions, raw keys, or leaked hidden state appears.
32. Render each phase, disabled reason, cooldown, selected sector, selected rival, hidden/suspected/attributed sabotage state, winner, loser, and Evolution V holder state.
33. Verify decorative art does not capture clicks and every sector click region matches its visible shape.
34. Verify the board contains exactly three peer meters and that Signal Intensity, Militarisation, Wreck Integrity, and sector confidence remain subordinate states.

## Contradictions, blockers, and unresolved conclusions

1. The in-progress Event 025 source uses one `global.chaosx_nr25_current_evolution` concept. That contradicts five independently gated evolutions and must not become the final architecture.
2. The in-progress source stores sector state and confirmer identity globally. Exact participant confidence and confirmation must be country-scoped or a multiplayer client can infer private progress.
3. The in-progress six-sector labels include a dedicated false-map sector. False coordinates should be a cross-sector incident; all six final sectors need geographic and methodological identity.
4. The package asks for a direct southern-access state table, but `hoi4.map_inspect` is unavailable. Source review suggests candidate gateway regions, but no exact state list is accepted until map inspection verifies states, ports, adjacency, ownership assumptions, and route grouping. This conclusion remains unresolved.
5. Event 016 has no valid-upgrade/full-pool public helper yet. Event 025 cannot satisfy duplicate-safe reward acceptance until the Event 016 owner implements and documents that API.
6. Event 036 has no accepted exact-overlap domain mapping. Its current jet reward may be recorded as aircraft recovery, but conversion to a particular Event 016 family or upgrade remains unresolved until the Event 036 owner and technology evidence define it.
7. The installed toolset has no Technology Tree Viewer route. Event 016 graph placement, dependencies, icons, and Event 036 aircraft consumers remain unresolved viewer evidence.
8. The auditor's `hoi4.probability_inspect` calls timed out or could not resolve the planned sources, while GUI, map, and technology routes are unavailable to this planner. The event scan is partial and its render produced no artifact. All affected render, privacy, timing, and weighted-balance conclusions are evidence-blocked.
9. The provisional participant and approximately 90-day evolution targets are design starting points, not accepted balance. They require the mandated probability baseline and compare passes.
10. Exact behavior when a player disables an already active evolution must be confirmed against the shared settings contract. This addendum recommends stopping future gated content without undoing history; if the shared owner requires a different transition, specs and tests must be updated together.
11. A rare international commission is accepted only as a Transfer Custody outcome. Promoting it to a separate route or mechanic would reopen scope and requires explicit design approval.
12. `specs/002_expedition_race_system.md` ends exact ties with a seeded random roll and gives mission timestamp first priority, while `specs/006_outcomes_rewards_and_aftermath.md` requires a deterministic survey/readiness/outpost/exposure/readiness-date/sequence order. This addendum resolves the contradiction in favor of the latter; promotion must update the former rather than leave both rules live.

## What should not be added

- no seventh survey sector
- no permanent false-map sector
- no fourth equal-status public meter
- no hardcoded country whitelist for participation
- no automatic Antarctic war declaration
- no Antarctic Treaty mechanic in the event's historical window
- no private copy of Event 016 technology effects
- no Event 025-owned Event 036 aircraft conversion table
- no sixth Evolution V route or international-commission subsystem
- no extra achievement beyond the accepted 14
- no second Event 025 super-event for ordinary race resolution unless a later accepted spec replaces the current opening role
- no focus tree, country package, formable, or 3D model solely to make the event appear larger

## Promotion into specifications

If accepted, merge the normative content rather than merely linking this sidecar:

- bounded roster formula and deterministic comparator into `specs/002_expedition_race_system.md`
- six-sector table, evidence channels, and false-map correction into `specs/002_expedition_race_system.md` and `specs/008_scripted_gui_and_presentation.md`
- independent evolution state matrix and disable behavior into `specs/004_evolutions.md`
- Event 016 API contract and Event 036 ledger contract into `specs/006_outcomes_rewards_and_aftermath.md` and `specs/013_implementation_architecture.md`
- privacy ownership and viewer snapshots into `specs/008_scripted_gui_and_presentation.md`
- P16–P27 into `matrices/025_ai_probability_scenarios.md` and `specs/009_ai_strategy_and_probability.md`
- achievement proof clarifications into `specs/011_achievements.md`
- the new deterministic scenarios and MCP blockers into `specs/014_acceptance_criteria.md`

Until that promotion is accepted and performed, this file remains in `docs/plans/025_alien_technology_in_antarctica_plans/` as an open implementation addendum. After promotion, record it as promoted and do not run another Event 025 improvement pass unless implementation uncovers a genuinely new gap.

## Parent handoff

### Design problem

The package promises a deep race but leaves the exact six-sector grammar, roster bound, independent evolution representation, duplicate-safe reward API, Event 036 overlap ownership, multiplayer privacy boundary, and achievement proof architecture open enough that implementation could diverge or become generic.

### Proposed resolution

Keep the package's overall scope closed and implement the precision contracts in this addendum: all humans plus at most six sampled AI, six grounded sector choices with private two-channel evidence, five independent evolution tracks, Event 016-owned reward arbitration, a neutral country-scoped Event 036 ledger, country-scoped GUI snapshots, and exact proof for all 14 achievements.

### Research basis and regional connections

The sector identities and methods are grounded in Byrd aviation and radio work, Operation Tabarin and Graham Land stations, Discovery oceanography, Norwegian aerial mapping, BANZARE seaplane/maritime work, and Australasian radio/magnetic science. Alien outcomes remain openly fictional design inferences.

### Files written

- `docs/plans/025_alien_technology_in_antarctica_plans/025_improvement_loop_addendum.md`

No gameplay file is owned or modified by this pass.

### Implementation surfaces affected

Event 025 events, constants, MTTH, scripted effects/triggers, decisions/categories, ideas/dynamic modifiers, narrow on-actions, scripted GUI/interface/GFX, scripted localisation/localisation, shared registration/log/details/super-event/achievement surfaces, Event 016 custom-technology API, neutral alien-recovery ledger, Event 036 adapter, assets, docs, and catalog workbook.

### Open questions

- exact southern gateway state groups after `hoi4.map_inspect`
- exact Event 036 recovery-domain mapping after Event 036 owner and technology-graph review
- probability-approved participant scores, sector distributions, reward pools, and evolution intervals
- exact shared settings transition when an already active evolution is disabled
- final GUI coordinates and supported-resolution evidence

### Prior addendum state

No previous Event 025 improvement-loop addendum remains unresolved. This addendum is the open precision layer created from the package's explicit independent-pass gate.

### Recommendation

Keep this document in `docs/plans` until the parent accepts it. If accepted, promote its normative contracts into the listed Event 025 specs before implementation closure. Do not add another broad expansion layer; after these contracts are implemented and audited, the appropriate next improvement-loop output should be a closure handoff limited to final validation, localisation, assets, documentation alignment, and blocker resolution.
