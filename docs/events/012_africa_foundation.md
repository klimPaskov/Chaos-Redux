# Event 012 Africa Foundation API

This document describes the Event 012 Africa implementation surfaces currently in the repository. It began as a foundation API note, but now also records the live event, focus, decision, country, asset, achievement, AI, and documentation wiring added around that API.

## Files

- `common/script_constants/012_africa_constants.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `events/012_african_union.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/national_focus/012_africa_focus.txt`
- `common/national_focus/012_africa_authority_focus.txt`
- `common/ideas/012_africa_ideas.txt`
- `common/factions/templates/012_africa_factions.txt`
- `common/on_actions/012_africa_on_actions.txt`
- `common/ai_strategy/012_africa.txt`
- `common/scripted_localisation/012_africa_scripted_localisation.txt`
- `events/chaosx_triggerable_scenarios.txt`
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
- `localisation/english/chaosx_gui_l_english.yml`
- `interface/012_africa.gfx`
- `docs/assets/012_africa/implementation_asset_manifest.md`

## Runtime Context

`africa_select_random_unifier_candidate` selects a weighted random country that passes `is_africa_valid_unifier_candidate`. The trigger requires an existing country with capital in Africa, at least one owned or controlled African state, and excludes special chaos countries, actual nonhuman countries, capitulated countries, existing Africa formables, world-end actors, and flagged broken shells. Subject countries qualify only through the explicit subject allowance flag or an active liberation-war story.

Selection weight comes from `africa_score_unifier_candidate_for_selection`, then `africa_select_weighted_unifier_candidate` expands eligible countries into a temp-array pool and uses `random_scope_in_array`. Independent African capitals, subject liberation stories, active wars against non-African enemies, recent chaos-liberation states, RSA in the Allies, and small candidates are favored by script constants in `africa_selection_weight`.

If no valid country exists, `chaosx.nr12.1` fires `chaosx.nr12.0`, sets `africa_no_valid_unifier_candidate`, and leaves runtime state not ready. The event reports that the Charter found no eligible African-capital seat instead of silently failing.

`africa_prepare_runtime_context_from_this` runs in the selected country scope. It saves the global event target `africa_unifier_country`, sets the numeric reference `global.africa_unifier_country_id`, sets `global.africa_runtime_ready`, `africa_runtime_context_ready`, `event_012_africa_fired`, and the country flag `africa_unifier_active`, then initializes all core values.

`africa_clear_runtime_context` clears the global event targets, country flags, and runtime variables owned by this foundation API, including the unifier, Charter League leader, RSA branch targets, RSA branch state, and World Is One gate state. It does not clear terminal world-end flags after the World Is One scenario starts.

## Triggerable Scenario SCN-012

`Africa Is One` is registered in the shared triggerable scenario window as SCN-012. It is blocked if Event 012 has already fired or another world-end branch is active. The scenario stores `global.africa_triggerable_scenario_type` and `global.africa_triggerable_scenario_intensity`, then calls `africa_triggerable_scenario_launch_selected`.

Standard, Liberation League, High-Chaos Covenant, and Continental Pole types use the weighted unifier selector. If no valid African-capital country exists, the manual scenario creates the `WAC` fallback host from the West Africa seat and uses it as the host, which is the explicit scenario exception to the ordinary `chaosx.nr12.0` no-target result. The RSA Civil War type is available only when South Africa exists, qualifies as an Africa candidate, and is in the Allies with England; it reuses `africa_start_rsa_allies_civil_war`, so the Allied peace rule still belongs to the same civil-war branch.

Scenario intensity changes manpower, stockpiles, colonial alarm, and regional-authority seeding. The Liberation League type opens the Liberation War Office, starts the liberation mission state, registers outside African holders, and declares one opening anti-colonial war if a valid outside holder exists. High-Chaos Covenant opens the Authority Atlas and unlocks Bestiary package activity. Continental Pole opens the post-unification Scramble and sponsor testing surface, but it does not set `world_end_africa_world_is_one` and still leaves the terminal World Is One branch behind shared certification, high-chaos, and one-charter gates.

## Core Values

`africa_initialize_core_values` initializes all mapped values from the specs:

- `africa_legitimacy`
- `africa_authority`
- `africa_league_cohesion`
- `africa_liberation_momentum`
- `africa_regional_trust`
- `africa_colonial_alarm`
- `africa_paper_core_burden`
- `africa_covenant_pressure`
- `africa_archive_mandate`
- `africa_old_seat_legitimacy`
- `africa_local_sovereignty`
- `africa_restoration_debt`
- `africa_mythic_pressure`
- `africa_nonhuman_sovereignty`
- `africa_bestiary_alarm`
- `africa_habitat_trust`
- `africa_mythic_volatility`

Initial values and clamp bounds live in `africa_initial_value` and `africa_value_bounds`.

## Paper-Core Staging

The foundation API deliberately avoids instant full cores across Africa.

- `africa_grant_continental_paper_claims`: adds claims on African states and marks them with `africa_paper_claim`.
- `africa_unlock_state_integration_from_from`: country scope, with `FROM` as the target state. Marks a claimed African state as integration-unlocked.
- `africa_mark_state_authority_tracked_from_from`: country scope, with `FROM` as the target state. Marks a state as tracked by a regional authority or integration office.
- `africa_complete_living_core_from_from`: country scope, with `FROM` as the target state. Adds a real core only after the state is owned and controlled by the caller and has been integration-unlocked.

## Charter League

`africa_create_charter_league_from_template` creates the Pan-African Charter League through `create_faction_from_template` using `faction_template_africa_charter_league`, `africa_charter_league`, and `GFX_faction_logo_generic_democratic`.

The faction template lives in `common/factions/templates/012_africa_factions.txt`. The entry event and Charter focuses call the helper after a valid unifier is selected.

Membership helpers:

- `africa_add_from_to_charter_league`
- `africa_mark_from_as_protected_charter_member`
- `africa_mark_from_as_full_charter_member`

These helpers expect the unifier in `ROOT` and the target African country in `FROM`.

The decision layer now exposes leader-side and member-side Charter gameplay:

- invite African-capital and protected countries into the Charter;
- send aid to full members or protected members through their separate target arrays and, when aid goes to a Charter-side country already at war, start a one-active-at-a-time member confidence mission;
- influence member cohesion and regional trust;
- docket regional authorities for integration;
- allow members to request aid, leave the Charter, or raise a resistance war.

## RSA Branch

RSA-in-Allies state is tracked by:

- `africa_mark_rsa_allies_branch_start`
- `africa_mark_rsa_continental_side`
- `africa_mark_rsa_loyalist_side`
- `africa_mark_rsa_continental_victory`
- `africa_white_peace_allies_after_rsa_continental_victory`

`common/on_actions/012_africa_on_actions.txt` hooks the civil-war end path. When the RSA continental side wins, `africa_white_peace_allies_after_rsa_continental_victory` white-peaces countries in England's faction that are still at war with `event_target:africa_rsa_continental_side`.

The shared focus tree includes an RSA crisis branch gated to `africa_rsa_continental_side`: underground congress, mine/port strikes, defecting units, Allied pressure, Pretoria test, and victory settlement. The RSA decision category adds supply, mine-port belt, Allied negotiator, and post-victory settlement work. The mine-port belt and Pretoria deadline gates require the continental side to control the Transvaal (`275`), Cape (`681`), and Natal (`719`) objective states, covering the Pretoria/Johannesburg mine belt, Cape Town, and Durban at HOI4 state granularity.

## Authority Atlas

`africa_register_authority_atlas_catalog` seeds global arrays with 32 historical dossier IDs and 11 high-chaos package IDs. Required minimum counts are constants:

- `africa_authority_atlas.minimum_historical_dossiers = 24`
- `africa_authority_atlas.minimum_historical_macro_regions = 6`
- `africa_authority_atlas.minimum_high_chaos_packages = 6`

Registered count constants are also provided:

- `africa_authority_atlas.historical_dossier_count = 32`
- `africa_authority_atlas.high_chaos_package_count = 11`

Historical dossier IDs include Kush/Meroe, Aksum, Punic Harbor Ledger, Numidia, Garamantes, Manden, Songhai, Jolof-Wolof, Futa, Asante, Oyo, Benin/Edo, Dahomey, Kanem-Bornu, Hausa, Wadai-Baguirmi, Funj/Sennar, Adal/Harar, Ajuran, Swahili Coast, Kilwa, Kongo, Ndongo-Matamba, Luba, Lunda, Buganda, Bunyoro, Great Zimbabwe, Barotse, Merina, Comorian Sultanates, and Zulu-Nguni.

High-chaos package IDs include Gorilla Highlands, Chimpanzee Marshes, Okapi Forest, Crocodile Rivers, Baobab Roots, Termite Surveyors, Honeyguide Routes, Great Herds, Tidemark, Ananse Ledger, and Orisha/Vodun Wilds.

`africa_mark_selected_dossier_opened` expects `africa_selected_dossier_id` to be set on the current country. `africa_mark_selected_high_chaos_package_unlocked` expects `africa_selected_high_chaos_package_id`.

The focus and decision layers turn the catalog into an active register:

- the main tree opens macro-regional dossier lanes, old-seat settlement routes, and high-chaos safety gates;
- `africa_open_next_historical_dossier` funds a selected-dossier survey and starts `africa_selected_dossier_survey_mission`; the dossier only opens on mission success while its representative seat remains secured;
- local office, guard, and settlement decisions resolve the active dossier and only then advance the register;
- active dossiers are grouped into eight visible profiles: Nile/Red Sea, Maghreb/desert, Sahel charter, western crowns, central river, Great Lakes, Indian Ocean, and southern stone seats. Survey completion, local offices, old-seat guards, observer settlement, and direct Archive settlement apply profile-specific value movement rather than identical dossier rewards. The Authority Atlas header shows the active profile and its public outcome summary.
- each active historical dossier stores a representative old-seat state from the dossier-state table; local office, guard, and settlement decisions require that state to be controlled by the unifier or protected by a loyal Charter-side actor;
- dossier settlement records both the settlement style and macro-region coverage: observer settlements increment `africa_dossier_observer_settlement_count`, direct Archive settlements increment `africa_dossier_direct_archive_settlement_count`, and first settlements in North/Nile-Horn, West/Sahel, Central, Great Lakes, Indian Ocean, and Southern Africa increment `africa_dossier_macro_region_count`; the Continental Register and World Is One gates require the minimum dossier count and all six macro-region lines;
- all 11 Bestiary package IDs apply concrete case outcomes and visible value movement;
- all 11 Bestiary packages also have explicit fictional/supernatural/nonhuman subject actors when their seat state can be transferred or protected by the Charter side;
- Bestiary habitat seats can be secured as map decisions on the explicit high-chaos actor seat states, incrementing `africa_bestiary_habitat_seat_count` and marking the state with `africa_bestiary_habitat_secured`.
- all 11 Bestiary actor tags have one-time target actions after their case is opened. The original set covers Gorilla forest guards, Crocodile river crossings, Baobab memory arbitration, Tidemark convoy watch, Ananse counterfeit-treaty audit, and Orisha/Vodun Wilds cases. The expanded set covers Chimpanzee Telegraph relays, Okapi Forest shadow dossiers, Termite Citadel engineers, Honeyguide Routes aid paths, and Great Herds relief columns. These actions spend equipment, manpower, convoys, command power, or army XP, reinforce the actor or its capital where appropriate, move visible Bestiary values, set actor-side completion flags to avoid repeat farming, and fire visible local consequence events for the five expanded actors.
- the five expanded Bestiary packages also keep one-time package actions: Chimpanzee Marsh scout lines, Okapi Forest observers, Termite Citadel treaties, Honeyguide Routes, and Great Herds migration corridors. These actions spend equipment, manpower, convoys, command power, or army XP, move visible Bestiary values, and increment `africa_bestiary_package_action_count`.
- verified Bestiary warnings can be issued against registered outside holders in the Scramble docket after the omen reliability review succeeds and package work exists. The holder-level warning target receives a response event and can comply, settling the holder case and improving legitimacy/trust while lowering alarm, or defy the warning, raising Colonial Alarm and Mythic Volatility. A separate map decision can warn the holder of a specific African state; this marks that state as complied or defied without settling the whole holder case. One warning may be pending at a time, holder-level targets only answer one holder warning, state warnings cannot repeat the same state, and overuse lowers legitimacy.

## Focus and Decision Surfaces

`common/national_focus/012_africa_focus.txt` contains the main Africa tree: Charter politics, industry/logistics, military, diplomacy, regional authority, Authority Atlas, Archive of Old Seats, Scramble for Africa, high-chaos Bestiary, sponsor, post-unification, and World Is One gate branches.

The main tree includes mutually exclusive political route locks and payoffs for Federal Charter, Sovereign Seats, People's Liberation Front, Continental General Staff, and Crown Congress. The Federal Charter route now has a dedicated Congress sub-branch: Charter Assembly Votes, Regional Autonomy Statutes, Federal High Court, Continental Citizenship, and Congress of Capitals. Those focuses add the route spirit, open targeted member/authority decisions, require federal work before the federal Integrated Regions payoff, and start the regional integration proof loop through the Congress of Capitals. The tree also includes a Diaspora Return / Pan-Atlantic branch and an RSA civil-war branch. Route flags now feed integration, sponsor, AI, and decision unlocks.

The post-unification sponsor/world-order branch now continues past `AFR_africa_is_one`: The Continental Export Office opens the cross-continent branch, Nile-to-Euphrates Charter Staff, Afro-Asian Liaison Columns, European Charter Observers, and South Atlantic Return Mandate unlock their matching sponsor decisions, Congress of Continents requires all four staff branches and all four sponsored charters before opening the dynamic union proclamation, Unifier Proof Ledger unlocks the four external proof decisions, The Last Borders Are Administrative unlocks certification, One Charter Above Nations unlocks the final gate preparation decision, and only `AFR_the_world_is_one` fires the terminal World Is One effect after `can_africa_start_world_is_one_gate` passes.

`common/national_focus/012_africa_authority_focus.txt` contains companion trees for regional authority subjects and high-chaos actors. These trees now include role-gated subject branches rather than a single identical ladder: West/Sahel authorities use caravan-motor mobility, Maghreb/East African/Indian Ocean authorities use coast-and-rail links, Nile-Horn/Great Lakes/Congo authorities use interior guard posts, and southern authorities use workshop-industrial support before their Charter future settles. Each regional authority then receives a tag-specific capstone focus for its named seat and role. High-chaos actors route through forest/court/citadel/guide/herd covenant, river/tide, or Ananse signal-line work before World Witness, then each Bestiary actor receives a tag-specific capstone focus for its explicit nonhuman or supernatural package.

`common/ai_strategy/012_africa.txt` gives the unifier broad route postures and differentiates Event 012 created subjects by role and by tag. The unifier has route bands for liberation, General Staff, Crown Congress, diaspora return, RSA emergency handling, and world-order sponsorship; the sponsor band prioritizes convoys, support equipment, dockyards, and restraint once the sponsor office, export office, charter staff, cross-continent charters, proof ledger, certification, or one-charter terminal preparation are active. Regional authorities have separate AI bands for West/Sahel mobility, coastal/rail networks, interior guard states, and southern industry plus one per-tag posture for all ten created regional authorities. High-chaos actors have separate forest/covenant, river/coast, Ananse support, signal/court, citadel-engineer, and Great Herds supply postures plus one per-tag posture for all eleven explicit Bestiary actors. These are still shared companion trees with tag-specific capstones rather than full bespoke country focus trees, but they prevent every created actor from using a single identical build and production priority.

The Scramble route registers outside powers that still own or control African territory when Foreign-Holder Case Files or Scramble Counter-Dockets are opened. The pool uses a fixed registered holder count, while the target array refreshes unsettled holders and counts holders that have actually lost their African holdings as settled. `africa_press_scramble_treaty_settlement` spends convoys, support equipment, manpower, and command power against a selected outside holder; `africa_issue_bestiary_warning_to_holder` uses the high-chaos warning network to force a response event from an unsettled holder and can settle that holder on compliance; `africa_issue_bestiary_warning_to_state_holder` targets an African map state owned or controlled by a registered holder and records state compliance or defiance without closing the holder docket; `africa_scramble_treaty_deadline_mission` requires every registered holder to be settled while the African capital remains controlled. `ACH_AFR_NO_SECOND_SCRAMBLE` keys on this mission success instead of only the focus flags.

`common/scripted_guis/012_africa_scripted_gui.txt` and `interface/012_africa_scripted_gui.gui` add a Continental Congress decision-category panel for the active Africa unifier. The panel surfaces the core mandate values, regional authority count, living-core count, dossier progress, Bestiary progress, World Gate status, active dossier, active Bestiary case, regional seat card values, and Bestiary seat card values from live variables.

`common/decisions/012_africa_decisions.txt` provides the active gameplay layer for:

- continental congress and register refreshes;
- Charter diplomacy and member-side requests, departures, and resistance wars;
- Federal Charter votes, regional autonomy statutes, and High Court arbitration against selected Charter members or regional authorities;
- liberation preparation, border columns, rail-belt objectives, and targeted front-state objectives;
- paper-claim surveys, authority-tracked rail work, and living-core integration;
- diaspora return offices, return settlements, officer schools, and Pan-Atlantic congress work;
- selected-dossier survey missions, local office, old-seat guard, and guarded settlement;
- high-chaos Bestiary unlock, habitat, omen, warning, binding, actor-specific package decisions, and non-actor package operations;
- continent sponsor, cross-continent charter sponsorship, dynamic union proclamation, and terminal gate preparation;
- RSA civil-war emergency supply, mine-port belt, Allied pressure, and victory settlement.

The decision layer also contains true timed missions with `days_mission_timeout` rather than only instant decision payouts:

- `africa_member_confidence_mission`: starts when League aid is sent to a Charter member or protected member already at war. Success requires the target to remain in the Charter relationship, avoid capitulation, and finish its war; failure raises Colonial Alarm and lowers League Cohesion.
- `africa_aid_corridor_mission`: starts when the League opens a full aid corridor to a warring Charter member or protected member. The League spends command power, support equipment, convoys, and trains, the target receives manpower and logistics stockpiles, and success requires the target to remain in the Charter relationship, avoid capitulation, and finish its war before the deadline.
- `africa_liberation_front_deadline_mission`: complete border-column, rail-belt, and secured front-state objectives during an active war, or take Colonial Alarm and Cohesion penalties.
- `africa_regional_integration_deadline_mission`: convert paper claims into living cores, seat regional authorities, and secure authority-seat rail belts in multiple regions, or add Paper-Core Burden and trust loss.
- `africa_selected_dossier_survey_mission`: keep the active dossier's old-seat state secured through the survey period. Success opens and surveys the dossier; failure raises Restoration Debt and Local Sovereignty pressure while allowing a retry.
- `africa_archive_guard_deadline_mission`: remembers the surveyed dossier id and representative old-seat state, blocks the next survey while active, and requires that exact dossier's local office, guard, settlement, and secured old seat before the deadline, or adds Restoration Debt and sovereignty pressure.
- `africa_direct_archive_seal_mission`: starts after a direct Archive settlement. Success requires enough Legitimacy and Old-Seat Legitimacy while Restoration Debt stays below the seal cap; failure exposes a counterfeit-claim crisis, raises Restoration Debt and Colonial Alarm, and fires the Counterfeit Crowns super-event surface.
- `africa_omen_reliability_review_mission`: starts when the Omen Reliability Office commissions a review. Success requires enough Habitat Trust while Bestiary Alarm and Mythic Volatility remain below the review caps, then unlocks verified warnings; failure raises Bestiary Alarm, Mythic Volatility, and Covenant Pressure.
- `africa_bestiary_containment_deadline_mission`: negotiate habitat terms, secure the required Bestiary habitat seats, verify omen reliability, bind a Bestiary actor to the Charter, and complete the required Bestiary actions, or raise Bestiary Alarm and Mythic Volatility.
- `africa_continent_sponsor_readiness_mission`: starts from the Continent Sponsor Office after Africa Is One. Success requires the Continental Register, the required regional authorities and living cores, and minimum historical dossier coverage across all six macro-region lines; failure raises Colonial Alarm and Restoration Debt. World Root, Bestiary containment, and Bestiary action thresholds remain terminal World Is One requirements rather than ordinary Africa Is One prerequisites.
- `africa_rsa_pretoria_deadline_mission`: on the RSA branch, hold the Transvaal, Cape, and Natal objective states, force Allied negotiators, complete victory settlement, and secure Allied peace before momentum collapses.

Core values are visible in the Event 012 decision category descriptions and move through focuses, decisions, wars, state control, foreign influence, dossier work, high-chaos packages, and AI. Covenant Pressure is surfaced in the high-chaos decision header and moves through Bestiary unlocks, habitat terms, omen review, actor binding, package-specific outcomes, actor-specific Bestiary actions, non-actor Bestiary actions, warnings, and containment mission outcomes.

The Continental Congress scripted GUI is attached to the main congress decision category. It shows the core value board, current dossier, current Bestiary case, active warning/status line, a regional seats card, a Bestiary seat card, and action buttons for Congress, Register, Dossier, Sponsor, Seats, and Terms. These buttons call scripted GUI handlers, spend the same PP/equipment/convoy/command-power layers as their decision equivalents, and use timed recent-action flags to prevent repeat-click loops. The Seats action binds controlled regional authority seat states into Charter subjects; the Terms action negotiates the one-time Bestiary habitat terms from the Congress panel. A visual strip below the cards uses static fallback sprites and route-gated animated overlays for the Charter banner, Authority Atlas seal, and Bestiary warning seal.

Regional integration and high-chaos decisions now expose additional objective counters in their category headers. `africa_integration_rail_region_count` advances when a secured integration rail belt falls on a regional-authority seat state and records the first rail corridor in each broad authority region. `africa_bestiary_habitat_seat_count` advances through the Bestiary habitat-seat map decision, `africa_bestiary_package_action_count` advances through actor actions and non-actor package operations, and the warning counters track issued, complied, and defied Bestiary warnings. Defied warnings also apply route-specific pressure from unlocked Bestiary cases: habitat trust loss, liberation disruption, old-seat debt, paper-core strain, Archive Mandate loss, alarm, volatility, or Covenant Pressure depending on which high-chaos systems are active. The containment mission depends on protected states and concrete package work rather than only route flags.

Dynamic force setup is handled through `012_africa_effects.txt` helpers rather than fixed guard counts. The selected unifier's opening Continental Charter Guard count scales from controlled states, military factories, manpower, war state, and subject status, then clamps to the Event 012 force band. Border Liberation Columns use a separate reinforcement band so later decisions do not repeat the full opening package. Regional authority and high-chaos actors likewise calculate their opening guard counts from their local state/industry/manpower base, with trust or mythic-pressure bonuses from the unifier, and their authority/high-chaos focus trees can raise bounded relief guards as reinforcement routes. Created Event 012 actors also receive one-time role-family production setup: support-equipment lines for every created actor, infantry-equipment lines for combat-facing roles, convoy lines for maritime/route actors, and small static naval or air OOBs where the actor's seat has a matching port or airbase.

The continent-sponsor category now has a pre-unification sponsor readiness mission plus staged cross-continent routes for Middle East, Asia, Europe, and South Atlantic sponsorship after Africa is one. The readiness mission spends convoys, support equipment, command power, and time; it makes `AFR_africa_is_one` reachable only after the continental register, World Root mandate, regional authorities, living cores, historical dossier coverage across all six macro-region lines, and Bestiary package thresholds are proven. The later cross-continent decisions require their matching post-unification focus unlocks, then spend convoys, equipment, manpower, command power, and time before `AFR_congress_of_continents` unlocks the final `africa_proclaim_dynamic_cross_continent_union` decision. After that union, `AFR_unifier_proof_ledger` opens four route-specific proof decisions for Middle East, Asia, Europe, and South Atlantic continent-unifier records through separate convoy, train, equipment, manpower, command-power, and army-XP costs. Those proof decisions also require external readiness hooks from the matching continent systems: `middle_east_continent_unifier_world_end_ready`, `asia_continent_unifier_world_end_ready`, `europe_continent_unifier_world_end_ready`, and `south_atlantic_continent_unifier_world_end_ready`. When all four proofs are verified, the identity is promoted to `AFR_CONGRESS_OF_CONTINENTS` without replaying the dynamic-union rewards. `AFR_last_borders_are_administrative` then unlocks the certification decision, `AFR_one_charter_above_nations` unlocks the final gate preparation decision, and `AFR_the_world_is_one` is the only terminal starter. The sponsor header shows `africa_external_continent_unifier_proof_count` against the required four proofs and reports when Africa is still waiting for other continent mandates. The current identity set is:

- `AFR_AFRICAN_MIDDLE_EASTERN_UNION`
- `AFR_AFRO_ASIAN_UNION`
- `AFR_AFRO_EURASIAN_UNION`
- `AFR_AFRO_ATLANTIC_UNION`
- `AFR_CONGRESS_OF_CONTINENTS`

## Country Packages

The regional authority tags are:

- `WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`

The explicit fictional/supernatural/nonhuman high-chaos actor tags are:

- `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`

Each tag has country registration, a country file, a history file, direct display-name localisation, generated symbolic root/medium/small flag families, focus loading, AI strategy coverage, setup hooks from `012_africa_effects.txt`, dynamic starting guard counts, and at least one focus-based reinforcement path. Regional authority tags are marked as event-managed special countries, while high-chaos actors are also marked as nonhuman where appropriate. All 11 high-chaos actors receive package-specific target actions from the unifier decision layer, with actor-side flags recording whether the actor has performed its guard, crossing, arbitration, convoy, audit, court, relay, shadow-dossier, engineering, aid-route, or relief-column action. The expanded actor actions fire visible consequence events `chaosx.nr12.40` through `chaosx.nr12.44`; those are local action reports, not final variant super-events.

The 21 created tags use direct public display identities: West Africa, Sahel, Maghreb Coast, Nile-Horn, East African Railways, Great Lakes, Congo Basin, Zambezi-Stone Cities, South African Liberation, Indian Ocean, Gorilla Highlands, Baobab Roots, Tidemark, Ananse Web, Orisha/Vodun Wilds, Crocodile Rivers, Chimpanzee Telegraph, Okapi Forest, Termite Citadels, Honeyguide Routes, and Great Herds. Party names may still use congresses, councils, assemblies, or other internal bodies where they represent factions rather than the country identity.

The 21 created tags now use distinct one-state seats for runtime transfer and history capitals. The high-chaos actors that previously overlapped regional authorities use separate states: `GHP` Rwanda `768`, `BBS` Upper Volta `778`, `TDM` Mombasa `905`, and `ANW` Ivory Coast `779`. The expanded Bestiary actor seats are `CTL` Stanleyville `718`, `OKP` Costermansville `890`, `TRM` Elisabethville `889`, `HGD` Garissa `903`, and `GHC` Nyanza-Rift Valley `904`.

Created country setup applies one-time role logistics through `africa_apply_created_country_setup_package` for all 21 created actors. Each tag receives a stable role flag, a visible role spirit, initial equipment or manpower keyed to its role, and a small movement in the relevant Event 012 values on the Charter leader. Coastal actors receive ports/convoys where relevant; rail, interior, southern, forest, river, archive, signal, court, citadel, guide, herd, and nature-court actors receive matching logistics or support packages. The shared production setup adds support-equipment lines for every created actor, infantry-equipment lines for combat-facing and field-escort roles, convoy lines for maritime or route actors, motorized lines for caravan/rail/river/courier actors, and train lines for rail or heavy-logistics actors. The affected histories also carry the matching motorized or train technologies. Every created tag loads a small role-specific static land OOB from `history/units/TAG_1936.txt`, so standalone or alternate package starts have at least one matching division template and placed guard force in the tag's seat state. Nine coastal or river-seat actors also load DLC-split static naval OOBs through `set_naval_oob`, with MTG cutter variants and legacy destroyer patrols for `MAG`, `EAC`, `IOC`, `TDM`, `CRR`, `WAC`, `CBC`, `ANW`, and `OVN`. Five actors with airbases in their seat state load DLC-split air OOBs through `set_air_oob`: `MAG`, `IOC`, `OVN`, `NHR`, and `SLC`. `africa_generate_created_country_role_staff` adds two generated advisors to every created actor, using vanilla advisor slots and traits matched to the actor's role and its support needs. `africa_generate_created_country_command_staff` adds one role-specific generated corps commander to every created actor and naval commanders to the nine actors that already have naval OOBs, using generated-character roles, matching vanilla unit-leader traits, and either generic African land/naval portraits or the actor's fictional/nonhuman portrait. The authority focus companion tree adds a second layer of role-specific rewards and value movement. This remains a bounded setup pass, not a substitute for full bespoke minister rosters, deeper country-specific naval and air branches, or fully bespoke focus trees.

## Assets and Presentation

`interface/012_africa.gfx` registers Event 012 report/news/super-event images, custom focus icons, idea icons, decision category headers, achievement icons through `chaosx_achievements.gfx`, static fallback sprites for animated Congress visuals, and frame-animated sprite sheets for the Authority Atlas seal, Charter banner pulse, and Bestiary warning loop. `interface/012_africa_scripted_gui.gui` provides the live Continental Congress decision panel.

Final asset wiring status is documented in `docs/assets/012_africa/implementation_asset_manifest.md`.

The Event 012 achievement set is wired through `common/achievements/chaos_redux_achievements.txt`, `localisation/english/chaosx_achievements_l_english.yml`, and `interface/chaosx_achievements.gfx`. Implemented entries cover Charter authority subjects, Federal Charter accessions without Charter resistance war, peaceful historical dossier maturation across macro-regions, no-counterfeit respectful Archive unification, Bestiary seats, loyal forest delegation signatories, staged living cores, Scramble counter-dockets, regional-integration safety, autonomous-authority unification, RSA Allied rupture, diaspora return, the Kilwa-to-Kush old-seat chain, Baobab Senate arbitration, old-seat preservation inside the dynamic cross-continent union, dynamic cross-continent union sponsorship, impossible-signatory World Is One, World Is One prerequisite proof, RSA city-control treaty proof, Great Herds logistics, Ananse signal work, Tidemark port defense, forest-guardian pacts, Sahel caravan trade, no-instant-map-paint integration, Congress-vs-Command route discipline, old-seat votes, all regional seats represented, continent-sponsor schooling, Afro-Asian and Afro-Eurasian dynamic identities, explicit nonhuman/supernatural identity safety, Forest Votes No, anti-ivory Great Herds play, Crocodile/Tidemark treaty pressure, World Root prerequisites, small-throne old-seat survival, high-chaos pacts, Great Zimbabwe/Termite Stone Congress defense, Archive survival through Scramble, Coral Admiralty, and Kuomboka floodplain campaign play. The Bestiary seat achievement accepts actor actions from all 11 explicit Bestiary actor tags, the forest-signatory achievement requires Gorilla Highlands, Chimpanzee Telegraph, and Okapi Forest to be bound Charter actors with their actor actions complete, and `ACH_AFR_CHARTER_HAS_TOO_MANY_SIGNATURES` explicitly requires all 11 Bestiary package outcome flags before the terminal signature condition can pass.

Achievement prompt rows whose exact actors are not present in the implemented Event 012 actor package are queued rather than faked through unrelated flags: Hyena Radio Dominion / `africa_who_gave_them_a_microphone`, Bonobo Kinship Congress / `africa_gentle_veto`, Bird of the Walls / `africa_bird_was_right`, and the Sao Terracotta Host / `ACH_AFRICA_TERRACOTTA_LINE`. The implemented replacements use only durable flags from existing routes, decisions, missions, and focus outcomes.

Eight super-event roles are wired into the shared super-event framework with scripted localisation, music-mode tracks, and sound-mode tracks:

- slot `68`: `Africa Is One`
- slot `69`: `The Second Scramble`
- slot `70`: `The Archive of Old Seats`
- slot `71`: `Counterfeit Crowns`
- slot `72`: `The World Is One`
- slot `73`: `The Continental Pole`
- slot `74`: `The Continental Settlement`
- slot `75`: dynamic cross-continent union title from `[GetAfricaDynamicCrossContinentUnionName]`

## Evolution Logging

The evolution helpers follow the existing `record_events_log_evolution_entry` pattern:

- `africa_record_evolution_i_if_needed`
- `africa_record_evolution_ii_if_needed`
- `africa_record_evolution_iii_if_needed`
- `africa_record_evolution_iv_if_needed`
- `africa_certify_continent_unifiers_for_world_is_one`
- `africa_mark_world_is_one_gate_ready`

Each helper sets `events_log_evolution_event_id`, `events_log_evolution_type`, `events_log_evolution_stage`, `events_log_evolution_tier`, and actor context from `event_target:africa_unifier_country`, then checks `is_current_evolution_enabled = yes` before recording. Disabled evolutions do not set the recorded flags or unifier unlock flags.

`africa_certify_continent_unifiers_for_world_is_one` is the final pre-terminal certification step. It requires Totalen Chaos, Africa Is One, the Africa super-event, Africa's continental pole, all four verified external continent-unifier proof flags, the matching external continent world-end readiness flags, the dynamic cross-continent union, six regional authorities, twelve living cores, twenty-four historical dossiers across all six macro-region lines, six Bestiary packages, successful Bestiary containment, and the required Bestiary actions. It then sets `all_continent_unifiers_world_end_ready` and the unifier-side `africa_continent_unifiers_certified_for_world_is_one` marker.

`africa_prepare_world_is_one_gate` is a pre-terminal decision. It requires `can_africa_prepare_world_is_one_gate`, which checks `world_end`, `world_end_disabled`, Totalen Chaos, verified and certified continent-unifier readiness, the external proof counter, and the Africa-side prerequisites; it only sets the unifier-side `africa_world_is_one_gate_prepared` marker. `africa_mark_world_is_one_gate_ready` is the terminal scenario start and is now reached only by `AFR_the_world_is_one`, because `can_africa_start_world_is_one_gate` also requires that prepared-gate marker. When the gate starts, it sets `world_end`, `world_end_africa_world_is_one`, `africa_world_is_one_terminal_started`, and the compatibility flag `africa_world_is_one_gate_ready`, then fires slot `72` and records the final evolution entry when evolutions are enabled.

## Known Integration Requirements

- The eight final Event 012 super-event roles are packaged and wired.
- Variant audio packages now exist for Forest Parliament, World Root, Root and Fang, and archive-world in `docs/assets/012_africa/super_events/audio/manifest.md`; these are not wired super-event slots, do not have sound/music definitions, and still need accepted gameplay triggers, images, and final slot decisions. `africa_world_is_one_root_variant_terminal` remains blocked until the design decides whether it is a distinct terminal event or an explicitly shared presentation variant.
- Created Event 012 country flags are generated symbolic final flag families for all 21 created tags. The five expanded Bestiary actor flag/portrait families are documented in `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_bestiary_actor_assets_handoff.md`. Historical symbol/flag rows in `docs/assets/012_africa/source_research/manifest.md` remain separate dossier research and several are low-confidence or not downloaded.
- Dynamic cross-continent cosmetic identities have generated symbolic flag families, country localisation, cosmetic tags, decision routes, and a dedicated super-event slot.
- Generated art and icon package handoffs exist and selected assets are wired into live game folders. Remaining visual blockers are tracked in `docs/assets/012_africa/implementation_asset_manifest.md`.
- Spreadsheet alignment should be performed after implementation facts and audit fixes settle.
