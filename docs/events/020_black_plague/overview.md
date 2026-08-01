# Event 20: Black Plague

Event 20 is a playable state-level epidemic, containment, biowarfare, and Rat emergence system. The source-of-truth design package is `docs/specs/020_black_plague_specs/`; this document records the live runtime contract and the content currently wired into it. The scripted gameplay core, 50-focus RTA route, 70-focus RTX route, and scoped Rat King defeat/slot-087 presentation tranche are wired for static validation, while the accepted full-design audit still tracks broader narrative depth, presentation polish, rights attribution, and live validation as remaining work.

The natural incident is registered as a minor fire-once event and is default enabled through `constant:black_plague_identity.event_id`. Doctor Wu remains a separate Event 163 companion registration. Event 20 is registered in the shared Diseases cluster and in the public world-end scenario catalog; the terminal row remains inactive until Evolution V's earned conditions are met.

The player-facing report chain is wired under `events/020_black_death.txt`. Natural play reports origin recognition, the first threatened neighbour, late origin recognition, the first foreign and overseas infections, Severe Crisis, Containment, relapse, cure, countermeasure learning, ten million deaths, eradication, Rat emergence, resurgence, brood absorption, the sentient crown, the royal crisis, Royal Node success or counterfire, emergency countermeasure timeout, and the earned terminal route. SCN-012 uses `chaosx.nr20.90` for its launch briefing; the `.4` allocation remains the first neighboring-threat report.

## Natural origin

The natural entry event chooses one eligible mainland state through a weighted ticket pool. It favors population, crowding, underdevelopment, occupation, resistance, troops, refugees, war, ports, railways, and weak protection. Prevention, field hospitals, stability, infrastructure, and response capacity reduce the weight. The chosen state begins Incubating, nearby eligible states begin Threatened, and the system records the historical owner and controller.

## State lifecycle

`black_plague_phase` is the authoritative state phase:

| Value | Phase | Established | Map base |
| ---: | --- | --- | --- |
| 0 | Clear | No | Shared background |
| 1 | Threatened | No | Shared warning |
| 2 | Incubating | Yes | Black |
| 3 | Infected | Yes | Black |
| 4 | Severe Crisis | Yes | Black |
| 5 | Collapsed | Yes | Black |
| 6 | Contained | Yes | Black |
| 7 | Recovery | Yes | Black |
| 8 | Cured | No | Monitored recovery |
| 9 | Rat-Controlled | Yes | Black |

Disease load, mortality pressure, spread pressure, containment, treatment coverage, relapse risk, incoming exposure, Rat Infestation, and untreated time are stored separately. Phase changes do not erase those values. Cleanup lowers the underlying pressures and requires sustained response rather than instantly removing infection. Severe Crisis, Collapsed, and Rat-Controlled states suffer recurring physical devastation.

## Mortality and spread

The seven-day pulse calculates nonlinear mortality once and sends the applied population loss through the shared exact-loss transaction. Its returned value is the sole input to the Event 20 Deaths ledger and Chaos contribution, preventing double counting.

Spread is produced from a frozen source snapshot and resolved through a target ledger, preventing same-pulse cascades. Routes cover land borders, rail and transport, troop presence, occupation and fronts, refugees, war disruption, ports, Evolution II overseas contact, biological delivery, and Rat occupation. Countermeasure progress, containment, quarantine, inspection, and protection reduce exposure without erasing established infection.

## Shared disease UI and response

Event 20 uses `chaosx_disease_containment_category`, the existing disease interface, and the existing contamination mapmode. It does not create a dedicated Black Plague category.

The selected-state response surface provides rat cleaning, sealed food storage, sewer and burrow clearance, flea control, rail-yard and dock purges, demolition of lost blocks, emergency hospitals, quarantine, cordons, treatment, and Doctor Wu's protocol. Visibility and availability depend on the selected state, its phase, control, and response conditions. Actions have material, military, economic, and time costs. National countermeasure progress runs from 0 to 100 and reduces deaths and spread while enabling sustained cleanup. The shared disease category also exposes a timed Emergency Countermeasure Drive, route-specific Rat King crises, Royal Node strikes, the earned Crown Strike, and post-defeat Royal Burrow sealing; none of these operations cures a state instantly.

Authorized established Black Plague states retain a black base in the shared mapmode. Phase, containment, weaponization, and rat control are conveyed by the existing border and tooltip layers while other diseases retain their own colors. Private Incubating states are visibility-gated before the black base is painted. State-clipped black fog is not used because the supported scripted-mapmode layers do not provide a verified safe clipping mechanism.

## Evolutions and weaponization

Five logged evolutions have dynamic active and pre-fire Event Details entries. Natural evolution checks obey the five Event 020 disabled-evolution settings and the existing MTTH-backed next-check date; SCN-012's explicit bootstrap bypass still forces Evolutions I through IV:

1. Evolution I strengthens the strain.
2. Evolution II enables physically proven overseas spread.
3. Evolution III creates the Rat Nation from an uncontrolled basin.
4. Evolution IV creates the separate sentient Rat King.
5. Evolution V is the earned terminal route.

Ordinary disease phases are not evolutions.

The natural pulse advances at most one unrecorded evolution per due check and only marks the pulse as advanced after the corresponding activation succeeds. Evolution II requires a verified human-controlled destination port, Evolution III records the first active RTA carrier, and Evolutions IV and V require the live RTX country as their actor; a stale King flag cannot create an actorless Evolution IV row. SCN-012 keeps its explicit I-through-IV sequence under the scoped bootstrap bypass.

The weaponization project has six phases, eighteen unique iteration roles, four mutually exclusive approaches, accidents, condemnation, and payload integration with the existing delivery system. After completion, the shared category exposes paid expansion and destruction operations for the native payload stockpile; expansion adds one batch under an accident cooldown, while destruction removes the stored payloads without erasing research or delivery history. Doctor Wu uses one persistent validated host and accelerates response only through the normal selected-state and resource rules.

## Rat countries

The country package uses the reusable Rat Nation tag `RTA` and the separate Rat King tag `RTX`. The Rat Nation chooses one of four origin archetypes from its founding basin and represents additional broods through rat-controlled states, state-level brood strength markers, capped force-growth pulses, and internal Brood Mass rather than extra country tags. Its living carrier meters are Hunger, Coherence, and derived Disease Dominion. Hunger rises when territory stops feeding the brood and can open a destructive feeding crisis, while Coherence improves through hierarchy, stable plague ground, and absorption. Stronger adjacent markers can consolidate weaker warrens through the automatic state-marker absorption path and inherit their surviving brood units; the obsolete paid absorption decision is not a runtime surface. The package includes country identity, leaders, flags, ideas, common and archetype AI, route-aware focus weights, route-aware Rat King strategy plans, locked zero-manpower division templates, starting forces, decisions, focus trees, plague immunity, and occupation-driven infection. The King tree also exposes route-specific policy lanes for the Absolute Crown, Council of Burrows, and Black-Breath Hierophancy, with distinct hunger, cohesion, sentience, dominion, force-cap, and terminal-preparation consequences.

Rat units do not consume human manpower or normal equipment and cannot be manually deployed. Their current map models intentionally use the registered infantry entity as an engine-safe visual consumer. Bespoke Rat Nation and Rat King unit models and skeletal animations are outside this gameplay-readiness tranche and are not required for Event 20's scripted systems to load.

The shared RTA tree now has reachable second lanes for Urban Warren, Field Brood, Dock Brood, and War Brood origins. Citadel, migration, tide, and rail route flags change the continuing Brood Mass pulse, the persistent division-cap bonus, the route-aware AI, and the physically proven exposure path. Dock route bonuses remain subordinate to Evolution II's overseas-spread gate. The division-cap bonus is reapplied after every pulse refresh, so focus and decision rewards remain effective instead of being overwritten by state-count recalculation. The separate RTX tree has 70 focuses: three mutually exclusive government cores, six-focus Crown, Council, and Hierophancy lanes, advanced forces, crisis knowledge, shared Royal Node and strike lanes, and an earned terminal branch. See `docs/systems/black_plague_rat_route_modules.md`, `docs/events/020_black_plague/rat_route_depth.md`, and `docs/events/020_black_plague/rat_king_depth.md` for the runtime contracts.

Route-specific decision surfaces are live in the existing rat categories. RTA can strip outer districts during a Hunger spike, establish timed Burrow Nodes in selected rat-held states, follow a real refugee road into a human enemy state, concentrate or scatter a brood, devour an adjacent weaker brood marker, resist absorption in a selected weaker basin, open a Citadel Stockpile, open Migration Lanes, issue a Tide Manifest, or order a Rail Breach after the matching capstone; RTX can collect a Crown Tithe, audit Council charters, or broadcast the Hierophant's ash liturgy. Feeding and Burrow Nodes are consumed by the live RTA pulse, the refugee-road action uses the canonical exposure adapter with a state cooldown, and the four hierarchy actions change the shared carrier's growth clock, cap, meters, or state-level merger shield. The route operations use centralized meter costs and timed route consumers, so each choice changes state pressure, pulse capacity, or physically proven spread rather than only setting an unused flag.

The Rat King's court also exposes a state-targeted Royal Strike. During a war, RTX selects a human-controlled enemy state and spends Dominion and Brood Mass while reserving a civilian factory slot for a timed operation. Completion uses the canonical rat-occupation exposure path, reopens the shared disease lifecycle and mapmode provenance, and sends the affected controller a state-named report; a country cooldown and a separate state cooldown prevent repeated targeting.

The origin, overseas, organized-rat, Severe Crisis, Rat King crisis, Crown Strike, Rat King aftermath, and Doctor Wu bridge report surfaces use distinct final art. `GFX_report_event_020_black_plague_origin`, `GFX_report_event_020_rat_emergence`, `GFX_news_event_020_black_plague_overseas`, `GFX_report_event_020_black_plague_severe`, `GFX_report_event_020_rat_king_crisis`, `GFX_report_event_020_crown_strike`, `GFX_report_event_020_rat_king_aftermath`, and `GFX_report_event_020_doctor_wu` are registered in `interface/020_black_plague_event_pictures.gfx` and consumed by their existing Event 20 or Doctor Wu entries. The crisis-seal and animated Rat King presentation packages remain separate queued work.

## SCN-012 and terminal route

Black Plague Unbound is implemented in the existing triggerable-scenario UI as `SCN-012`. Each intensity directly seeds established outbreaks across multiple eligible continents, guarantees one verified human-controlled port for the forced Evolution II milestone, creates several internal RTA warrens from infected-or-worse candidates without creating another tag, forces Evolutions I through IV, creates the Rat Nation carrier, creates the Rat King in a separate Royal Basin, grants a coexistence grace period, initializes AI, forces, disease values, decisions, logs, coronation, and performs one mapmode rebuild. Low intensity may begin with Infected rather than Severe states, so the RTA carrier uses a narrowly scoped bootstrap spawn gate and returns to the natural Severe/Collapsed gate as soon as setup clears. The setup reserves geography and fails closed before mutation when the selected package cannot be supported, then uses a scoped bypass that is cleared after the transaction. Successful launches are idempotent; a downstream setup failure remains retryable, clears its temporary reservations and event targets, and is surfaced in the scenario UI, but a complete rollback of every already-applied disease or transfer mutation is not yet proven. It never grants Evolution V, `world_end`, or automatic victory and disqualifies ordinary-progression achievements.

Evolution V remains gated by Chaos above 1000, catastrophic plague deaths, conquest, the completed Rat King route, and 90 percent control of an eligible continent together with its designated capitals and refuge nodes. Evolution V opens the earned route; the Rat King must then issue the visible final-order decision before deterministic takeover and the world-end super-event can begin. The terminal transaction records each remaining human-state population through the shared exact-loss ledger once, then transfers the state and closes the world.

Once Evolution V opens, human countries that still hold established Black Plague ground can start one of two timed projects in the same shared disease category: Hold the Line or Secure the Refuge. Each pays support, motorized, infantry, train, fuel, manpower, command-power, factory, stability, and war-support costs up front, then gains weekly progress for war, countermeasure progress, and held states. Secure the Refuge additionally requires a held terminal capital, refuge node, or city and receives a node bonus. Success lowers Rat King terminal preparation, adds countermeasure progress, and raises containment without curing a state; timeout raises terminal preparation, Rat King hunger, and incoming exposure. Missions are removed idempotently when a country loses its eligible ground or the terminal takeover begins.

The complete mission contract, exact payment values, progress inputs, outcomes, and file ownership are documented in `docs/events/020_black_plague/last_response_missions.md`.

## Runtime ownership

Event 20 uses an event-owned seven-day scheduler rather than adding a world-iterating daily, weekly, or monthly on-action. Natural initialization, scenarios, and weekly pulses batch state writes and rebuild the shared mapmode once per transaction. SCN-012 saves one seeded anchor and schedules its first `.900` callback before clearing bootstrap arrays, so a fresh scenario continues into the ordinary runtime. If launched over an active crisis, existing established states are preserved and only unestablished candidates are seeded; a human-controlled port is reused when present or seeded once when continent sampling missed every port.

The authoritative event catalog workbook records Event 20 under cluster 8 (Diseases), Severe member severity, the `The Kingdom of Teeth` terminal scenario row, and SCN-012's RTA/RTX intensity contract. The three catalog CSVs are export-only snapshots regenerated from that workbook.

SCN-012 rebuilds its internal-brood count from the reusable RTA carrier and surviving state markers before attempting any intensity top-up. A repeat launch therefore preserves the minimum brood postcondition even when no unoccupied candidate state remains.

Primary implementation surfaces include:

- `common/script_constants/020_black_plague_*.txt`
- `common/scripted_triggers/020_black_plague_*.txt`
- `common/scripted_effects/020_black_plague_*.txt`
- `common/decisions/020_black_plague_*.txt`
- `common/national_focus/020_black_plague_*.txt`
- `common/special_projects/projects/020_black_plague_weaponization_projects.txt`
- `events/020_black_death.txt`
- `events/020_black_plague_*.txt`
- `history/countries/RT*.txt`
- `history/units/RT*_1936.txt`
- `interface/020_black_plague_*.gfx`
- `localisation/english/020_black_plague_*_l_english.yml`

## Core-readiness boundary

The scripted core is source-complete for the current gameplay tranche, subject to the explicit SCN-012 rollback limitation above. Static audits resolve the Event 20 custom constants, scripted calls, event callers, GFX references, and texture paths covered by that tranche. The fourteen ordinary-progression achievements now have public registry entries, completion triggers, localisation, and completed, grey, and not-eligible icon triplets.

Rat King zero-state defeat now uses an idempotent resolver that retires RTX, clears active royal preparation, records scoped defeat participants and peak metrics, emits the defeat report once, conditionally dispatches reconstruction `.72` and gated super-event slot 087, opens the shared Royal Burrow cleanup operation for a human responder, and preserves RTA and surviving plague states. Slot 087's final art, localisation, audio ID 103, sprite registration, and sound wrappers are promoted in `interface/020_black_plague_super_events.gfx`, `localisation/english/020_black_plague_super_events_l_english.yml`, `sound/chaosx_sound.asset`, and `music/chaosx_music_track_list.html`; defeat metrics and resolver coupling live in `common/on_actions/020_black_plague_on_actions.txt`, `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_triggers/020_black_plague_rat_triggers.txt`, and `common/script_constants/020_black_plague_constants.txt`. Remaining accepted full-design work is intentionally separate: broader route and aftermath narrative depth, the source-frame crisis seal and animated Rat King presentation packages, release attribution, and focused live validation. The `.73` audience prefers the saved defeat actor, then a registered response country, then the first eligible human response host. Bespoke rat 3D units and animations are outside this goal by instruction and are not load-time prerequisites for the Event 20 gameplay systems.

The shared board now also carries a four-frame source-authored rat-infestation badge registered in `interface/020_black_plague_rat_identity.gfx` and gated by the existing Black Plague tab trigger. The crisis-seal animation and animated Rat King portrait remain separate queued presentation work. The full audit and deferral record is `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`.
