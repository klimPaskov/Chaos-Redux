# Event 12 Scramble Response and World Order

## Purpose

This subsystem begins after `africa_is_one` and preserves the original Event 12 host. It resolves the foreign Scramble response through recognition, conditional recognition, sanctions, ultimatums, an optional expedition war, and an aftermath congress. W1-W5 source includes the six continent-package polity loops, sponsorship, union, war, succession, breakup, terminal lifecycle, runtime-surface certification, and the four-role super-event presentation package.

The package sections below describe the six installed external packages and their acceptance surfaces. The current asset and presentation dispositions remain authoritative in `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv`, and the six late or episodic action families remain list-only decision content rather than duplicate Charter controls.

No response grants African membership, integration, annexation, or cores. The foreign response is a diplomatic and military settlement around the already negotiated Charter League.

## State flow

1. `chaosx.nr12.309` calls `africa_initialize_scramble_and_world_packages` once.
2. One explicit post-unification census registers foreign majors, faction leaders, and governments with African holdings. Its first bounded sweep prioritises eligible non-African majors, faction leaders, and current African-state owners that pass the shared expedition material-readiness gate; a second bounded sweep fills any remaining roster slots from the same registration pool. No recurring daily, weekly, or monthly world scan exists.
3. Each participant explicitly chooses recognition, conditional recognition, sanctions, or an ultimatum in `africa_world_order.1`.
4. Four timed phases track diplomatic shock, coalition formation, intervention or settlement, and aftermath.
5. Intervention can produce a real war. Pairwise on-actions record war, capitulation, and peace without periodic country iteration, and the host advances only after every flagged expedition actor is out of its war with the host.
6. During the aftermath, Action 85 can install one documented actor for each of the six external continent packages after the reviewed W5 effect certifies all six candidates together and sets the per-candidate `africa_world_package_implementation_ready` gate. Sponsorship creates a separate 180-day material obligation.
7. Full world-order opening requires all six dedicated packages, a resolved Scramble, and the writer-backed `africa_world_package_runtime_surfaces_reviewed` receipt. A documented mixed or absent roster can still close the Africa-only docket without opening world-order actions when no ready package is available.
8. Settled packages can consent to union, remain sovereign, become rivals, fight a prepared continental war, or accept a postwar submission settlement.
9. The terminal World identity remains unavailable until all continent packages are resolved, chaos is above the terminal threshold, no ordinary settlement remains pending, and the researched final super-event package sets `africa_the_world_super_event_package_ready`.

When a priority member has explicitly chosen the rival-bloc departure route and the current Africa host capitulates to that member, `on_capitulation` calls `africa_priority_member_record_rival_bloc_victory`. The receipt records the member-specific rival victory and feeds the recognised-confederation achievement owner. A normal peace or relationship state never infers victory without this bounded winner/capitulation pair.

When no external candidate carries the reviewed `africa_world_package_implementation_ready` gate, the host can instead close the Continental Docket after satisfying every Scramble recognition, sanctions, ultimatum, intervention, and peace requirement. This records a complete Africa-only settlement, leaves external governments outside the Charter League, and does not open world-order actions.

## Tuning and shared logic

- `common/script_constants/012_africa_world_order_constants.txt` contains phase identifiers, continent identifiers, package statuses, shared costs, durations, thresholds, and reward values.
- `common/scripted_triggers/012_africa_world_order_triggers.txt` contains candidate, phase, sponsorship, union, war, and terminal checks.
- `common/scripted_effects/012_africa_world_order_effects.txt` contains the one-time census, response choices, package installation, obligations, package ledgers, and terminal cleanup. Parallel focus contributions are counted independently, while the displayed package step remains the highest numbered step reached.
- Actions 77 through 92 continue to use the shared Action 1 through 102 selector and outcome kernel. The world-order file supplies their exact full, partial, and failure semantics.
- Candidate countries qualify as existing sovereign countries with a controlled non-African capital and a live package surface. Existing country trees are preserved until the package installer deliberately applies its dedicated regional tree.
- `africa_world_candidate_runtime_surfaces_are_registered` accepts only a candidate-owned, continent-specific seven-receipt mapping. The mapping names the existing route/protocol, focus, decision, idea, AI, identity, and localisation surfaces for Middle East, Europe, Asia, North America, South America, and Oceania; no host-wide source claim can satisfy a candidate.
- `africa_world_all_package_runtime_surfaces_are_certified` proves an exact six-entry, one-per-continent roster, live sovereign candidates, controlled non-African capitals, complete candidate-owned receipts, and no successor, exile, breakup, terminal, or high-chaos substitution state. `africa_world_review_runtime_surface_registry` records `africa_world_package_runtime_surfaces_reviewed` only after that proof succeeds, and `africa_world_certify_all_package_runtime_surfaces` sets `africa_world_package_implementation_ready` across the frozen candidate array in one bounded pass. The source/runtime certification is installed; political package installation and terminal presentation remain separately guarded.
- `africa_world_terminal_super_event_runtime_surfaces_are_registered`, `africa_world_register_terminal_super_event_runtime_surfaces`, and `africa_world_certify_terminal_super_event_runtime_surfaces` form a separate four-role source registrar and atomic setter for slots 101-104 and unique audio ids 58-61. Each role must provide its exact image, audio definition, localisation/text records, and runtime consumer before `africa_the_world_super_event_package_ready` is written; no generic terminal presentation receipt is accepted.
- A candidate still needs `africa_world_package_implementation_ready` before Action 85 can install its political package state. This is a gameplay readiness gate, not a missing-asset fallback.
- Every continent-package loader preserves completed-focus history. The installer remains one-shot through the candidate-to-installed state transition, so activating a reviewed package cannot silently erase earlier national progress.
- W4 union eligibility rejects the canonical `africa_world_submission_settlement` receipt written by Action 88 and continental-war submission; terminally submitted packages cannot re-enter the union partner route.
- The resolver no longer recognises the legacy `africa_world_package_terminal_absorbed` flag. That flag had no writer in the Event 012 source, while the accepted runtime paths require consent, submission, successor, exile, breakup, or explicit terminal-resolution receipts; no instant annexation path is implied.
- The Scramble ultimatum gate likewise uses only its writer-backed zero-count and answered-ultimatum receipts. The legacy `africa_scramble_ultimata_withdrawn` flag had no Event 012 writer or accepted response action, so it is not treated as a hidden blanket-withdrawal path.

Consent-based union dissolution now opens the `.713` and `.717` record events for both sovereign actors from the existing dissolution receipts before pair cleanup. If a registered continental war ends without an accepted armistice, submission, constituent release, successor, exile, or breakup receipt, the pairwise peace hook records the explicit `collapsed` status and opens `.733` for the attacker before running the shared cleanup; it does not infer a terminal settlement.

Successor transfer, exile certification, and breakup certification now open their existing W4 acknowledgement events from the same written receipts that drive terminal accounting. The review-close event accepts successor registration, exile resolution, and package terminal resolution as separate documented outcomes.

If breakup is certified while a registered continental war remains open, the guarded wrapper writes the existing bilateral `africa_world_war_settlement_breakup` receipt and settled status for both actors, opens `.725`, and then closes the protocol. A generic post-loss breakup outside an open war does not acquire a war settlement receipt.

Pairwise settlement hooks clear only the actor that actually left the war, while `africa_scramble_reconcile_intervention_war` closes the intervention global and opens aftermath only when no flagged coalition actor remains at war with the host.

### Scramble interest census and response roster

The one-time participant census is bounded at `constant:africa_scramble_response.participant_census_cap` and writes explicit host-owned arrays for former colonial relationships, ideological rivals, resource-nationalisation exposure, fear of a complete external continental unifier, and South Africa or Allied relationships. The first bounded sweep admits candidates that pass `africa_ai_scramble_expedition_materially_ready`; the second bounded sweep fills remaining capacity without changing the cap or registration kernel. These arrays are frozen when `africa_scramble_interest_census_complete` is set and are never rebuilt by a recurring on-action.

`africa_scramble_enlist_coalition_member` and `africa_scramble_remove_coalition_member` keep the participant flag, the host counter, and `africa_scramble_coalition_members` in lockstep under the six-member cap. Recognition leaves the coalition, sanctions enlist a bounded member, and ultimatum issuers enlist as expedition planners.

Recognition, conditional recognition, sanctions, ultimatums, expedition launches, and aftermath closure now carry material equipment, convoy, political-power, stability, and war-support consequences from `africa_scramble_response` constants. `africa_scramble_apply_class_response_consequences` records host pressure and integration burden for every accepted interest class, while `africa_world_order.8` reports the multi-member expedition response.

The expedition launch iterates only the frozen coalition array and gives every eligible planner a war role and expedition matériel after rechecking the shared material-readiness predicate, before declaring the existing treaty-enforcement war. `africa_scramble_cleanup_response_roster` clears transient participant and class state, arrays, and class counters after the settlement or defeat log is queued while preserving the host's outcome summary flags.

## AI policy binding

The exact 64-profile registry now controls the Scramble and world-order campaign instead of remaining a read-only scoring table. The Scramble classifier and the frozen-census first sweep share `africa_ai_scramble_expedition_materially_ready`, and final coalition launch checks the same predicate again before assigning expedition materiel or declaring war. Static registration is complete, but the strategy-plan probability adapter returned no usable surface and no campaign simulation or balance completion claim follows from the registry.

- `africa_ai_run_profiled_late_action_cycle` is an AI-only host decision with a fourteen-day re-enable period. It runs only for the current Event 12 host and reads the maintained Scramble participant, package candidate, package actor, and relationship arrays. It performs no country census.
- The host refresh composes its regional overlay, constitution, and full-host playbook. A selected target then contributes its relationship, foreign-power, high-chaos, or continent profile before final approval.
- Actions 77 through 92 receive separate semantic priorities and exact availability checks. The dispatcher selects only a real target that satisfies the same action-specific validator used by the player quote path. The full dispatcher covers all 102 action rows; rows 73-76 and 85-92 retain their explicit runtime gates.
- Every approved AI action passes through `africa_begin_quoted_action_against_target`. Dynamic costs, capacity, target cooldowns, shared missions, full and partial outcomes, failure, and cleanup therefore remain identical for player and AI use.
- Partial-outcome tolerance changes high-risk action weighting. Retry stance reads the target's immutable last-action ledger and can require resource recovery before another attempt.
- The host stores the last composite policy, all active layer IDs, selected action, selected target, partial tolerance, retry stance, and launch counters as normal variables for audit and save-state inspection.
- Foreign participants are classified into the five accepted outside-power profiles before `africa_world_order.1` chooses recognition, conditions, sanctions, or an ultimatum. The chosen response profile is recorded separately from the pre-response forecast.
- World-route decisions consume the saved profile risk, partial-tolerance, Scramble, and world-order weights alongside their constitutional preferences.
- Action 91 uses the selected continent actor's controlled capital region as its AI state cursor. Human players can select any valid controlled state in that actor. This administration creates no automatic ownership transfer.

Post-World Actions 91 and 92 remain available after `world_end_africa_the_world`. Their terminal phase and profile predicates recognise this specific Event 12 identity, while unrelated world ends continue to block the system. The World identity is additionally gated by the registered four-role super-event package and the ordinary terminal protocol checks.

## Continent packages

The six package mechanics are distinct and use separate public values:

- Middle East: Crossroads Balance, including Arab, Persian, Anatolian, minority, holy-site, water, and oil values.
- Europe: Continental Settlement, including industry, sovereignty, war memory, ideology, colonial debt, and borders.
- Asia: Centers of Asia, including eastern, southern, inland, archipelago, food and river, and corridor values.
- North America: Continental Bargain, including industry, federal representation, sovereignty, Caribbean inclusion, indigenous settlement, migration, and command.
- South America: Andes, Amazon, and Plata Balance, including three regional voices, indigenous representation, resources, and foreign debt.
- Oceania: Ocean Network, including convoy reach, island representation, naval protection, indigenous settlement, air routes, and dispersed industry.

All six packages have dedicated focus architectures in their respective `common/national_focus/012_africa_world_<region>_focus.txt` files. Their political, decision, identity, AI, localisation, and presentation surfaces are registered in the Event 012 runtime, and the host certifies the exact six-entry candidate roster before installation. High-chaos constitutional routes retain their explicit content and sensitivity gates; they do not make the base package dormant.

### Package identity contract

Each package keeps the existing selected carrier tag and adds a distinct identity surface only after Action 85 installs it. The installer loads the region's focus tree, sets the region package flag, initializes the region-specific value ledger and polity foundation, and creates one named male fictional steward with the registered route portrait. The six generated emblems are consumed by each package root focus and are not interchangeable recolours. The terminal World identity uses the separate six-star seal and the host's established sovereign rather than creating a seventh country tag or an invented leader.

| Package | Focus root | Public mechanic ledger | Emblem | Steward |
| --- | --- | --- | --- | --- |
| Middle East | `africa_middle_east_world_focus_tree` | Crossroads Balance | `GFX_012_africa_world_package_middle_east_emblem` | Hadi al-Qamar |
| Europe | `africa_europe_world_focus_tree` | Continental Settlement | `GFX_012_africa_world_package_europe_emblem` | Niko Veyra |
| Asia | `africa_asia_world_focus_tree` | Centers of Asia | `GFX_012_africa_world_package_asia_emblem` | Arun Sen |
| North America | `africa_north_america_world_focus_tree` | Continental Bargain | `GFX_012_africa_world_package_north_america_emblem` | Thomas Ironwind |
| South America | `africa_south_america_world_focus_tree` | Three Rivers Balance | `GFX_012_africa_world_package_south_america_emblem` | Mateo Yupanqui |
| Oceania | `africa_oceania_world_focus_tree` | Ocean Network | `GFX_012_africa_world_package_oceania_emblem` | Tane Moana |

The six steward portraits use plain matte backgrounds and one route-specific visual motif each, with no extra people in the image. They are fictional presentation assets, not historical African portraits. Historical priority-member portraits follow the separate direct-source rule in `docs/assets/portraits/012_africa/source_locked_runtime_mapping.md`.

## Middle East implementation

The Crossroads Balance begins by ending foreign mandates and establishing water, food, pipeline, and holy-city settlements. It has five mutually exclusive constitutional routes:

- Arab Federal Pact
- Plural Crossroads Federation
- Royal Concert
- Union of Socialist Republics
- Desert Covenant

The Desert Covenant is additionally locked by `africa_middle_east_high_chaos_package_reviewed`. That flag must remain unset until the dedicated source and sensitivity review confirms its text, nonhuman actors, symbols, and asset treatment. It never turns a human Middle Eastern identity into a supernatural species.

Every route must complete representation, command, Africa diplomacy, withdrawal law, and a final settlement congress before receiving a public cosmetic identity and replacing the founding-problem spirit.

## Europe implementation

The Continental Settlement begins with border guarantees, industrial and rail reconstruction, and a colonial reckoning. It has six mutually exclusive routes: democratic federation, socialist union, royal concert, continental command, neutral confederation, and a reviewed mythic compact. Each route receives its own representative institution before converging on common defence, withdrawal and crisis law, a post-colonial treaty with Africa, and final ratification. The mythic compact remains locked until `africa_europe_high_chaos_package_reviewed` confirms its separate source and sensitivity review.

## Asia implementation

Centers of Asia uses four founding regional institutions and five mutually exclusive settlements: plural federation, revolutionary union, imperial congress, anti-colonial common front, and a reviewed celestial covenant. Each route has its own congress before converging on food, river, and monsoon management, rail and maritime corridors, common defence, autonomy and withdrawal law, an Indian Ocean partnership with Africa, and final ratification. The celestial covenant remains locked until `africa_asia_high_chaos_package_reviewed` confirms its separate source and sensitivity review.

## North America implementation

The Continental Bargain begins with four negotiations over the industrial grid, Caribbean and Central American membership, indigenous and regional consent, and equal citizenship and mobility. Five mutually exclusive settlements follow: republic of republics, continental commonwealth, hemisphere command, socialist continental union, and a reviewed storm frontier compact. Each route receives its own constitutional institution before the tree converges.

The converged resource, defence, island, and Africa treaty lanes call route-aware scripted effects. The republics route favours bicameral representation and equalisation. The commonwealth favours sovereign transfer compacts and government boards. The command route gains stronger military coordination at a real sovereignty cost and remains subject to civilian and regional consent. The socialist route uses worker and republic congresses. The storm compact is bounded by published containment and ecological law. It remains locked until `africa_north_america_high_chaos_package_reviewed` confirms its separate nonhuman, ecological, text, and asset review.

The Africa treaty is based on citizenship, skills, investment, Atlantic convoys, and locally accepted development. Return is always voluntary. The receiving community can accept, negotiate, or refuse a project, and no opinion value can create integration.

After every mandatory lane is completed, the route payoffs produce the following bounded values. The command route has the strongest military integration and the lowest sovereignty. The commonwealth concentrates on industry and intergovernmental compacts. The republics route produces the strongest formal representation. The socialist route gives Caribbean membership and collective industry greater weight. The reviewed storm route prioritises indigenous settlement, ecological limits, and containment command.

| Settlement | Industry | Federal representation | Sovereignty | Caribbean and Central inclusion | Indigenous settlement | Migration compact | Command integration |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Republic of republics | 55 | 100 | 100 | 95 | 55 | 75 | 35 |
| Continental commonwealth | 100 | 45 | 100 | 100 | 55 | 75 | 35 |
| Hemisphere command | 75 | 45 | 50 | 75 | 55 | 75 | 95 |
| Socialist continental union | 85 | 65 | 70 | 100 | 65 | 75 | 35 |
| Storm frontier compact | 55 | 35 | 95 | 95 | 100 | 75 | 65 |

### North America focus icon contracts

North America focus sprites and registrations are installed for the Continental Bargain package. The authoritative asset matrix remains the row-level record for the exact filenames and consumers.

- `GFX_goal_012_africa_continent_sponsorship_north_america_continental_bargain` uses `goal_012_north_america_continental_bargain.dds`.
- `GFX_goal_012_africa_continent_sponsorship_north_america_industrial_grid` uses `goal_012_north_america_industrial_grid.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_caribbean_central` uses `goal_012_north_america_caribbean_central.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_indigenous_settlement` uses `goal_012_north_america_indigenous_settlement.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_citizenship` uses `goal_012_north_america_citizenship.dds`.
- `GFX_goal_012_africa_continent_union_north_america_republics` uses `goal_012_north_america_republics.dds`.
- `GFX_goal_012_africa_continent_union_north_america_commonwealth` uses `goal_012_north_america_commonwealth.dds`.
- `GFX_goal_012_africa_continent_union_north_america_hemisphere_command` uses `goal_012_north_america_hemisphere_command.dds`.
- `GFX_goal_012_africa_continent_union_north_america_socialist_union` uses `goal_012_north_america_socialist_union.dds`.
- `GFX_goal_012_africa_continent_union_north_america_storm_compact` uses `goal_012_north_america_storm_compact.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_bicameral_congress` uses `goal_012_north_america_bicameral_congress.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_governments_council` uses `goal_012_north_america_governments_council.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_command_statute` uses `goal_012_north_america_command_statute.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_workers_republics` uses `goal_012_north_america_workers_republics.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_storm_law` uses `goal_012_north_america_storm_law.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_resources_withdrawal` uses `goal_012_north_america_resources_withdrawal.dds`.
- `GFX_goal_012_africa_continent_sponsorship_north_america_two_ocean_defence` uses `goal_012_north_america_two_ocean_defence.dds`.
- `GFX_goal_012_africa_continental_representation_north_america_islands_settlement` uses `goal_012_north_america_islands_settlement.dds`.
- `GFX_goal_012_africa_continent_union_north_america_africa_diaspora_treaty` uses `goal_012_north_america_africa_diaspora_treaty.dds`.
- `GFX_goal_012_africa_continent_union_north_america_ratification` uses `goal_012_north_america_ratification.dds`.

## South America implementation

The Andes, Amazon, and Plata Balance begins with mountain transport, Amazon river and forest law, La Plata and two-ocean access, and a public audit of concessions and foreign debt. Six mutually exclusive settlements follow: congress of republics, plural federation, socialist continental union, continental command, restored continental concert, and a reviewed sun covenant. Each route receives its own chamber before converging on resource and debt sovereignty, defence and corridors, the South Atlantic partnership with Africa, and final ratification.

The converged lanes remain constitution-specific. Republican institutions favour formal regional representation and public concessions review. The federation equalises the three regional voices. The socialist union favours collective resource control. The command route gains the strongest mountain and naval coordination while carrying lower indigenous representation and debt freedom. The restored concert binds courts to regional institutions. The sun covenant gives ecological and indigenous law priority, and remains locked until `africa_south_america_high_chaos_package_reviewed` confirms its separate nonhuman, ecological, text, and asset review.

The South Atlantic partnership covers shipping, cultural links, voluntary diaspora ties, resources, and security. Cultural and development projects require local acceptance. No opinion value creates integration.

| Settlement | Andean voice | Amazon voice | La Plata voice | Indigenous representation | Resource sovereignty | Debt freedom |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Congress of republics | 100 | 45 | 100 | 95 | 75 | 75 |
| Plural federation | 100 | 85 | 100 | 100 | 65 | 65 |
| Socialist continental union | 80 | 75 | 100 | 65 | 100 | 65 |
| Continental command | 100 | 45 | 100 | 35 | 85 | 50 |
| Restored continental concert | 100 | 45 | 100 | 85 | 65 | 50 |
| Sun covenant | 80 | 100 | 70 | 100 | 85 | 55 |

### South America focus icon contracts

South America focus sprites and registrations are installed for the Andes, Amazon, and Plata package. The authoritative asset matrix remains the row-level record for the exact filenames and consumers.

- `GFX_goal_012_africa_continent_sponsorship_south_america_three_regions_balance` uses `goal_012_south_america_three_regions_balance.dds`.
- `GFX_goal_012_africa_continent_sponsorship_south_america_andean_transport` uses `goal_012_south_america_andean_transport.dds`.
- `GFX_goal_012_africa_continental_representation_south_america_amazon_river` uses `goal_012_south_america_amazon_river.dds`.
- `GFX_goal_012_africa_continent_sponsorship_south_america_plata_ports` uses `goal_012_south_america_plata_ports.dds`.
- `GFX_goal_012_africa_continental_representation_south_america_resource_debt_audit` uses `goal_012_south_america_resource_debt_audit.dds`.
- `GFX_goal_012_africa_continent_union_south_america_republics` uses `goal_012_south_america_republics.dds`.
- `GFX_goal_012_africa_continent_union_south_america_plural_federation` uses `goal_012_south_america_plural_federation.dds`.
- `GFX_goal_012_africa_continent_union_south_america_socialist_union` uses `goal_012_south_america_socialist_union.dds`.
- `GFX_goal_012_africa_continent_union_south_america_continental_command` uses `goal_012_south_america_continental_command.dds`.
- `GFX_goal_012_africa_continent_union_south_america_restored_concert` uses `goal_012_south_america_restored_concert.dds`.
- `GFX_goal_012_africa_continent_union_south_america_sun_covenant` uses `goal_012_south_america_sun_covenant.dds`.
- `GFX_goal_012_africa_continental_representation_south_america_republican_chamber` uses `goal_012_south_america_republican_chamber.dds`.
- `GFX_goal_012_africa_continental_representation_south_america_three_regions_council` uses `goal_012_south_america_three_regions_council.dds`.
- `GFX_goal_012_africa_continental_representation_south_america_workers_communes` uses `goal_012_south_america_workers_communes.dds`.
- `GFX_goal_012_africa_continental_representation_south_america_command_statute` uses `goal_012_south_america_command_statute.dds`.
- `GFX_goal_012_africa_continental_representation_south_america_council_of_realms` uses `goal_012_south_america_council_of_realms.dds`.
- `GFX_goal_012_africa_continental_representation_south_america_sun_covenant_law` uses `goal_012_south_america_sun_covenant_law.dds`.
- `GFX_goal_012_africa_continental_representation_south_america_resource_sovereignty` uses `goal_012_south_america_resource_sovereignty.dds`.
- `GFX_goal_012_africa_continent_sponsorship_south_america_defence_corridors` uses `goal_012_south_america_defence_corridors.dds`.
- `GFX_goal_012_africa_continent_union_south_america_south_atlantic_partnership` uses `goal_012_south_america_south_atlantic_partnership.dds`.
- `GFX_goal_012_africa_continent_union_south_america_ratification` uses `goal_012_south_america_ratification.dds`.

## Oceania implementation

The Ocean Network treats Australia, New Zealand, Melanesia, Micronesia, Polynesia, and the island governments as negotiating partners joined by protected sea and air links. It begins with an island sovereignty congress, a convoy network, dispersed air and industrial capacity, locally accepted development and voluntary evacuation guarantees, and anti-colonial land settlements. It is not an expanded-Australia route, and it does not treat islands as empty bases.

Five mutually exclusive settlements follow: maritime federation, treaty dominion, indigenous-led ocean union, socialist maritime commonwealth, and a reviewed deep-sea covenant. Every route has its own constitutional institution before converging on withdrawal law, Pacific defence and disaster reserves, an Indian Ocean and southern sea treaty with Africa, and final ratification. The dominion route carries a real indigenous-settlement loss when central authority is established, then must recover consent through its island council and treaty obligations. The deep-sea covenant is limited to explicitly nonhuman actors and remains locked until `africa_oceania_high_chaos_package_reviewed` confirms its separate ecological, containment, text, and asset review.

The shared lanes remain constitution-specific. The maritime federation favours island votes and federal convoy administration. The treaty dominion concentrates naval command and dispersed industry under treaty limits. The indigenous-led union gives indigenous nations and island governments the strongest land and representation guarantees. The socialist commonwealth gives shipping and industry to workers, ports, cooperatives, and republics. The deep-sea covenant prioritises containment, ecological law, air warning, and human refusal rights.

The Africa treaty covers convoy protection, island obligations, and Indian Ocean and southern sea access. Every base requires treaty consent. It establishes no integration right, and it records rivalry management where dominion and African strategic claims overlap.

| Settlement | Convoy reach | Island representation | Naval protection | Indigenous settlement | Air network | Dispersed industry |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Maritime federation | 85 | 100 | 45 | 85 | 65 | 55 |
| Treaty dominion | 55 | 100 | 100 | 50 | 55 | 95 |
| Indigenous-led ocean union | 45 | 100 | 45 | 100 | 65 | 75 |
| Socialist maritime commonwealth | 100 | 95 | 45 | 55 | 45 | 100 |
| Deep-sea covenant | 55 | 65 | 100 | 100 | 95 | 55 |

### Oceania focus icon contracts

Oceania focus sprites and registrations are installed for the Ocean Network package. The authoritative asset matrix remains the row-level record for the exact filenames and consumers.

- `GFX_goal_012_africa_continent_sponsorship_oceania_ocean_network` uses `goal_012_oceania_ocean_network.dds`.
- `GFX_goal_012_africa_continental_representation_oceania_island_congress` uses `goal_012_oceania_island_congress.dds`.
- `GFX_goal_012_africa_continent_sponsorship_oceania_convoy_network` uses `goal_012_oceania_convoy_network.dds`.
- `GFX_goal_012_africa_continent_sponsorship_oceania_air_industry` uses `goal_012_oceania_air_industry.dds`.
- `GFX_goal_012_africa_continental_representation_oceania_development_evacuation` uses `goal_012_oceania_development_evacuation.dds`.
- `GFX_goal_012_africa_continental_representation_oceania_liberation_land` uses `goal_012_oceania_liberation_land.dds`.
- `GFX_goal_012_africa_continent_union_oceania_maritime_federation` uses `goal_012_oceania_maritime_federation.dds`.
- `GFX_goal_012_africa_continent_union_oceania_treaty_dominion` uses `goal_012_oceania_treaty_dominion.dds`.
- `GFX_goal_012_africa_continent_union_oceania_indigenous_union` uses `goal_012_oceania_indigenous_union.dds`.
- `GFX_goal_012_africa_continent_union_oceania_socialist_commonwealth` uses `goal_012_oceania_socialist_commonwealth.dds`.
- `GFX_goal_012_africa_continent_union_oceania_deep_sea_covenant` uses `goal_012_oceania_deep_sea_covenant.dds`.
- `GFX_goal_012_africa_continental_representation_oceania_federal_chamber` uses `goal_012_oceania_federal_chamber.dds`.
- `GFX_goal_012_africa_continental_representation_oceania_dominion_council` uses `goal_012_oceania_dominion_council.dds`.
- `GFX_goal_012_africa_continental_representation_oceania_peoples_congress` uses `goal_012_oceania_peoples_congress.dds`.
- `GFX_goal_012_africa_continental_representation_oceania_workers_ports` uses `goal_012_oceania_workers_ports.dds`.
- `GFX_goal_012_africa_continental_representation_oceania_deep_sea_law` uses `goal_012_oceania_deep_sea_law.dds`.
- `GFX_goal_012_africa_continental_representation_oceania_constitution_withdrawal` uses `goal_012_oceania_constitution_withdrawal.dds`.
- `GFX_goal_012_africa_continent_sponsorship_oceania_pacific_defence` uses `goal_012_oceania_pacific_defence.dds`.
- `GFX_goal_012_africa_continent_union_oceania_africa_sea_treaty` uses `goal_012_oceania_africa_sea_treaty.dds`.
- `GFX_goal_012_africa_continent_union_oceania_ratification` uses `goal_012_oceania_ratification.dds`.

## Asset contracts

The accepted matrix entries are registered in `interface/012_africa_world_order.gfx`. No generic texture redirection is used.

- Scramble news: `GFX_news_event_012_africa_scramble_response` at `gfx/event_pictures/012_africa/news_event_012_africa_scramble_response.dds`
- Continental war news: `GFX_news_event_012_africa_continental_war` at `gfx/event_pictures/012_africa/news_event_012_africa_continental_war.dds`
- Middle East focus icons: `gfx/interface/goals/012_africa/world_order/goal_012_middle_east_<focus_slug>.dds`
- Europe focus icons: `gfx/interface/goals/012_africa/world_order/goal_012_europe_<focus_slug>.dds`
- Asia focus icons: `gfx/interface/goals/012_africa/world_order/goal_012_asia_<focus_slug>.dds`
- North America focus icons: `gfx/interface/goals/012_africa/world_order/goal_012_north_america_<focus_slug>.dds`
- South America focus icons: `gfx/interface/goals/012_africa/world_order/goal_012_south_america_<focus_slug>.dds`
- Oceania focus icons: `gfx/interface/goals/012_africa/world_order/goal_012_oceania_<focus_slug>.dds`
- Package ideas: `gfx/interface/ideas/012_africa/world_order/idea_012_<continent>_<identity>.dds`
- External package emblems: `GFX_012_africa_world_package_<continent>_emblem` at `gfx/interface/012_africa/world_order/emblems/012_world_package_<continent>_emblem.dds`
- External package stewards: `GFX_portrait_012_africa_world_<continent>_leader` at `gfx/leaders/012_africa/world_order/portrait_012_africa_world_<continent>_leader.dds`
- Route flags: the seven `continent_package_*` identity packages in `docs/specs/012_africa_specs/matrices/012_africa_asset_animation_matrix.csv`
- Scramble super-event: `GFX_super_event_012_africa_scramble_response`
- Continental-wars super-event: `GFX_super_event_012_africa_continental_wars`
- Terminal World package: `GFX_012_africa_world_package_the_world_emblem` at `gfx/interface/012_africa/world_order/emblems/012_world_the_world_emblem.dds`, plus its separate researched final image, audio record, achievement, and final flag

World-order source, registrations, certified W5 runtime surfaces, four super-event roles, and the six package presentation surfaces are installed. The 239-row matrix remains the visual disposition authority; remaining deferred rows are controlled-pool or political-state gated, with no model-required or unique-package blocker. No fallback art or silent rights substitution is used.

## Cleanup

Scramble phase flags and intervention-war flags are cleared at settlement or defeat. Sponsorship missions remove their target from the bounded sponsorship array on fulfilment or default. Continental-war target flags are cleared when war launches or resolves. The final World effect closes incompatible world-order and Scramble flags only after its complete presentation readiness gate passes.

## Remaining acceptance work

- Maintain the writer-backed W5 certification receipt whenever a package surface or candidate roster changes; the initialization call must continue to set it only after the six package surfaces are registered.
- Run positive and negative acceptance scenarios for all sixteen priority packages on their existing carrier tags. The Luba, Lunda, and Kilwa carriers use their direct Event 012 tag predicates and do not require Event 006 receipts or newly created country tags.
- Resolve the two AI evidence blockers with a materially incapable Scramble scenario and a compatible strategy-plan score probe; do not bulk-rewrite the 107 flat focus weights from an empty probability surface.
- Preserve the permanent list-only disposition for Scramble response, world order, constitutional crises, post-unification governance, host opening, and regional restorations rather than adding duplicate Charter controls.
- Keep the installed news, super-event, animation, and audio rows aligned with the authoritative asset matrix, and preserve their source and rights evidence. Remaining work is final playback, localisation, and event-completion review rather than production of missing media.
- Keep high-chaos continent routes behind their separate text, identity, ecological, rights, and runtime gates; the grounded six package routes and terminal presentation are already source-registered.

## World-order roster and polity foundation (tranche 1)

The W5 certification effect is called from `africa_initialize_scramble_and_world_packages` after the one-time candidate nomination pass. It atomically marks the exact six candidates implementation-ready and records the certification receipt without changing country tags or transferring territory. This is the installed source callsite for the accepted package tranche; the candidate proof still fails closed when the six-entry roster is not valid.

The trigger requires the exact six-entry pending roster and one candidate for each continent. The setter rechecks that proof and sets readiness for all six candidates in one bounded pass.

The external roster is a one-time, host-owned census. `africa_world_nominate_missing_package_candidates` still nominates existing sovereign countries with the approved generic or replacement focus surface, but `africa_world_finalize_package_roster` now records each of the six continent slots in one of three bounded arrays: `africa_world_package_resolved_continents`, `africa_world_package_pending_continents`, or `africa_world_package_absent_continents`. `africa_world_package_roster_documented` is set only after all six slots have a disposition. A pending implementation-ready candidate still blocks the partial docket close, so the Scramble cannot silently discard a package that is ready to install.

The aftermath mission can close the Africa-only docket when political conditions do not activate all six installed package surfaces. This path sets `africa_world_order_deferred`, publishes `africa_world_order.110`, captures the settled hostile-control snapshot, and leaves no substitute actor in the registry. Political package installation still uses `africa_scramble_ratify_aftermath`, captures the same snapshot before roster cleanup, and opens the World-Order Council. The two paths are mutually gated by `africa_world_packages_are_installed`.

Each installed actor keeps its original country tag and receives `africa_world_initialise_package_polity_foundation`. The helper records the actor in the constituent ledger, scans sovereign same-continent capitals once, records controlled same-continent heartland states, and sets `africa_world_package_heartland_proof` only when the centralised `africa_world_roster.minimum_heartland_states` threshold is met. `on_state_control_changed` refreshes this proof for only the old and new controllers when either is a package actor.

Constituent countries carry `africa_world_constituent_status` and explicit consent, refusal, coercion, withdrawal, successor, or exile flags. Package actors receive bounded target-array decisions for consent, refusal, coercion, and withdrawal. No decision transfers states, manufactures cores, changes a country tag, or substitutes opinion for a recorded polity outcome.

When an actor capitulates or is annexed, the narrow loss helper opens a successor review and records one eligible same-continent sovereign candidate when available. If no candidate exists, the actor receives an explicit exile or breakup certification path. A recognised successor replaces the predecessor in the host actor store, inherits the continent identity and live package balances, receives the package focus tree, and rebuilds heartland and constituent proof under its own sovereignty. The predecessor loses active package ownership. Successor recognition is continuity rather than a terminal settlement, so the replacement must still earn an accepted sovereign, union, submission, exile, or breakup result. Exile and breakup enter the terminal ledger exactly once, and breakup applies the documented authority loss.

It does not install packages or set terminal presentation readiness.

### Foundation helper map

| Helper | Scope | Inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- | --- |
| `africa_world_finalize_package_roster` | Africa host | six candidate and actor checks | disposition arrays, counters, documented/partial/absence flags | one-time nomination pass |
| `africa_world_initialise_package_polity_foundation` | package actor | installed actor and package-continent flag | constituent arrays, heartland snapshot, original-actor/host proof | package installation |
| `africa_world_refresh_package_polity_proof` | package actor | current owned and controlled states | heartland array and proof/loss flags | state-control on-action |
| `africa_world_record_constituent_consent`, `...refusal`, `...coercion`, `...withdrawal` | constituent with package actor as ROOT | target decision and current status | status flags, actor arrays, authority deltas | package-polity decisions |
| `africa_world_handle_package_actor_loss` | package actor | capitulation or annexation | successor review, exile/breakup opening, heartland loss | capitulation, peace, annex on-actions |
| `africa_world_commit_package_successor`, `africa_world_record_exile_resolution`, `africa_world_record_package_breakup` | package actor | reviewed target or explicit certification | lifecycle resolution flags and cleanup | package-polity decisions |

The new shared tuning category is `africa_world_roster` in `common/script_constants/012_africa_world_order_constants.txt`. It owns heartland and constituent thresholds, decision costs, and authority deltas. The lifecycle enum is `africa_world_package_resolution`; constituent statuses use `africa_world_constituent_status`.

### Cleanup and unsupported surfaces

The on-action hooks do not run a recurring all-country scan. Successor candidate flags are cleared when a successor is committed or a breakup is certified, constituent member flags are cleared during breakup, installed actors are removed from the candidate store, roster entries are removed when a candidate installs politically, and absent entries are retained as the documented historical disposition. W0-W5 source includes the dynamic union-war and terminal lifecycle. The initialization call runs the explicit candidate receipt mapper, writes `africa_world_package_runtime_surfaces_reviewed` only after the all-six proof, runs the atomic certification pass, and invokes the four-role terminal presentation registrar. Model and presentation production are installed; final political-state, live-consumer, localisation, AI, and completion audits remain separate gates.
