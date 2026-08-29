# Event 025 implementation prompt

Implement the complete Event 025 Alien Technology in Antarctica rework in the live Chaos Redux repository.

## Required source

Read in full before editing:

- live `AGENTS.md`
- live `chaos-redux-events`
- live `chaos-redux-decisions-missions`
- live `chaos-redux-event-assets`
- live `chaos-redux-frame-animation`
- live `chaos-redux-super-events`
- live `chaos-redux-improvement-loop`
- live `chaos-redux-subagents`
- every file under `docs/specs/025_alien_technology_in_antarctica_specs/`
- every accepted Event 025 plan or handoff under `docs/plans/025_alien_technology_in_antarctica_plans/`
- Event 016 custom technology implementation and public external-grant helpers
- current Event 036 files, reservation state, or accepted specs
- current event-log, Event Details, major-event, achievement, super-event, Deaths, and GUI patterns

Consult the mandatory offline Paradox wiki pages and all relevant vanilla documentation. Inspect live vanilla precedents for events, decisions, missions, technology grants, scripted GUI, super-events, and polar or expedition presentation where applicable.

Use the installed HOI4 MCP routes for every supported event, GUI, technology, and probability surface. Record exact blockers when a required route is unavailable. Do not treat source-only review as equivalent.

## Accepted event identity

- Event ID `25`
- canonical entry `chaosx.nr25.1`
- type Major
- minimum Chaos tier Calm World
- standalone runtime event, not an active cluster member
- one opening super-event
- international expedition race
- every current human-controlled country may enter, including a player-controlled special actor
- bounded AI roster from valid majors, with only the accepted Kruger State exception
- baseline race must be fully completable with all evolutions disabled
- five independent evolutions at 200, 400, 600, 800, and 1000 Chaos
- no new country, focus tree, combat unit, character portrait, flag family, or required 3D model

## Core mechanic

Implement the six-phase loop from the specs:

1. entry and observation
2. mobilization and staging
3. crossing and Antarctic outpost
4. survey and triangulation
5. final recovery
6. analysis and settlement

The active runtime may evaluate only the stored participant registry. Do not add a recurring whole-world daily, weekly, or monthly scan.

Expose exactly three main values on the Expedition Board:

- Expedition Progress
- Logistics Readiness
- Exposure Risk

After Evolution V, valid technology holders replace Exposure Risk with Alien Dependence.

Keep route burden, gateway, outpost integrity, survey certainty, crew condition, intelligence, wreck integrity, and fragment ownership as supporting states or hidden logic.

## Costs and actions

Use real commitments such as convoys, fuel, support equipment, civilian industrial capacity, personnel requirements, scientists, access, and time.

One action may have no more than four spendable cost types. Do not hide personnel or scientist commitments as a fifth spendable cost. Do not turn the system into a political-power store.

Each phase normally shows three to five primary actions. Six is the hard maximum. Hide invalid, obsolete, or target-irrelevant actions.

Use one selected rival at a time for human players. AI evaluates all valid rivals through the same action helpers. Hostile actions need target validation, cooldowns, evidence states, counterplay, costs, partial outcomes, and cleanup.

## Winner and rewards

The first valid participant to complete final recovery secures the main core. Resolve same-day completions through the deterministic tie rules in the specs.

The winner receives one duplicate-safe Event 016 external custom technology reward. Event 025 must call the owner API and must not copy Event 016 technology logic.

The shared reward route must resolve:

1. random valid missing base operational family
2. otherwise random valid compatible upgrade
3. otherwise Alien Systems Integration

Place the reusable duplicate-safe helper with Event 016 or the shared custom-technology owner, document it, and return clear result state.

Event 025 player-facing text must describe the result as alien-derived. It must never identify Kruger as the source.

Do not create Warren Kruger, Kruger ownership, Directorate state, Event 016 project history, Event 016 evolution progress, the Kruger State, Strategic Singularity, free custom units, or free equipment beyond existing neutral runtime consumer rebuilds.

Implement losing survey and fragment reward tiers based on verified work. Do not give entry-only rewards.

Implement the shared Event 025 and Event 036 alien-recovery ledger and exact overlap conversion. Event 036 must later upgrade or replace an overlapping aircraft result. Event 036 being unavailable must not block Event 025.

## Evolutions

Implement every evolution as a separate logged mutation milestone with enabled-state gating and MTTH pacing. It may enter during the active race or intensify first firing. It may not replace ordinary phases.

- Evolution I Active Signal
- Evolution II Something Survived
- Evolution III Militarised Antarctica
- Evolution IV The Wreck Is Breaking Apart
- Evolution V The Technology Changes Its Users

Disabled evolutions must not set recorded flags, unlock actions, alter AI, or block baseline completion.

Evolution III may create blockades, seizures, patrols, and armed incidents. It must not automatically create a global war.

Evolution V creates contain, destroy, transfer, conceal, and integrate policy routes. Dependence remains recoverable.

## Expedition Board

Create the event-owned scripted GUI from Part 008.

Required regions:

- phase header
- left three-value status column
- central six-sector Antarctic operations panel
- bounded rival cards
- phase action tray

Use a full background with safe text regions. Do not paint fake controls into it. Every sector and button state needs readable normal, hover, selected, disabled, warning, cooldown, active, and resolved treatment where applicable. Preserve multiplayer privacy.

Route the accepted UI implementation to `chaosx_event_ui_worker` with `fork_context=false`. Require `hoi4.gui_inspect`, pre-change renders, `hoi4.gui_rewrite`, and matching post-change comparison at supported resolutions.

## AI and probability

Implement participation, route, phase action, rival target, withdrawal, and Evolution V policy strategy.

Use the named P01 through P15 scenarios and timing scenarios from the package. Every weighted patch requires:

1. read-only baseline audit by `chaosx_ai_probability_auditor`
2. owner patch
3. `hoi4.probability_compare` on the same scenarios

AI must preserve post-spend reserves, repair critical logistics, avoid invalid final recovery, and use cooperation where rational.

## Logs, presentation, and shared systems

Wire:

- one opening History row
- five evolution milestones
- Event Details premise, public phase, participant count, public evolution state, and winner
- opening super-event with final image, verified quote, unique licensed musical WAV, unique audio ID, settings-aware wrappers, and documentation
- winner news and bounded report families
- Deaths ledger for actual casualties
- opinion and world-tension consequences for observed escalation

Do not expose private coordinates, exact rival progress, sabotage authors, internal technology keys, or hidden reward arbitration.

## Assets and achievements

Produce every required asset in the asset matrix. Use generated period-authentic documentary art for fictional scenes. Use separate source art for decision, idea, GUI, and achievement icon families. Accepted animation must use real per-frame source art, frame sheets, DDS output, static fallbacks, and verified consumers.

Implement all fourteen achievements or report any proposed removal before source implementation is declared complete. Each needs tracking, disqualifiers, localisation, DDS triplet, documentation, and tests.

## Documentation and catalog

Keep implementation, localisation, docs, assets, super-event research, achievement docs, Event 016 helper docs, Event 036 integration docs, and Event Details wording aligned.

Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, then run `python .tools/export_event_catalog_csv.py`. Never edit the CSV exports directly.

## Required subagents

Use relevant project subagents with `fork_context=false` and the package prompts. The parent owns final integration and completion. Do not claim completion before the improvement planner, probability auditor, decision auditor, UI worker, localisation auditor, completion auditor, documentation curator, and spreadsheet worker have returned and their findings have been dispositioned.

## Completion standard

Use `specs/014_acceptance_criteria.md` as the pass or fail contract. Report every simplification, omitted route, missing asset, unavailable MCP path, unresolved audit, or fallback. Do not claim the event complete while any accepted requirement is missing or any placeholder remains.
