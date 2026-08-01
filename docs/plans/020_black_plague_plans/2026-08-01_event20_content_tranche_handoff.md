# Event 020 content tranche handoff

Date: 2026-08-01

## Scope

This tranche extends the load-ready Event 020 gameplay core without producing 3D models, meshes, skeletal actions, or model-dependent assets.

The two-tag correction remains authoritative: `RTA` is the sole reusable Rat Nation carrier and `RTX` is the separate Rat King.

## Implemented in this tranche

- The shared disease category now includes a selectable Emergency Countermeasure Drive mission with stockpile payment, 90-day timeout, countermeasure progress gain, and timeout exposure and stability pressure.
- Royal Node strikes now require a military route, resolve against King Dominion, reduce infestation and Dominion on success, block the next royal pulse for a bounded period, and feed Dominion, hunger, and terminal preparation on counterfire.
- The shared disease category now includes an earned Crown Strike against the Royal Basin and a post-defeat Seal Royal Burrows operation. Crown Strike has route-specific Dominion, Cohesion, and overseas-exposure consequences; Royal Burrow sealing has fixed equipment, manpower, fuel, command-power, factory, Response Capacity, and 180-day costs and does not cure the underlying disease.
- Royal Node success and counterfire have player-facing country reports `chaosx.nr20.54` and `chaosx.nr20.55`.
- Emergency Countermeasure Drive timeout has the player-facing report `chaosx.nr20.56`.
- Rat King route Hunger crises now fire distinct Absolute Crown, Council of Burrows, and Black-Breath Hierophancy country events with route-specific trade-offs.
- Rat King pulse blocking is consumed by the existing rat runtime pulse and is cleared on King initialization.
- RTA reinforcement tracking now records capped brood divisions raised for achievement predicates.
- The superseded multi-country achievement condition now measures absorbed RTA brood states under the two-tag model.
- The pre-terminal continent achievement no longer depends on Evolution V having already been recorded, so its route can be evaluated before the terminal takeover.
- The fourteen Event 020 achievement contracts now have public registry entries and player-facing name, description, eligibility, and completion tooltip localisation.
- The fourteen Event 020 achievement contracts now have completed, grey, and not-eligible 64x64 DDS triplets, with 42 explicit aliases in `interface/chaosx_achievements.gfx`; source, processed, prompt, contact-sheet, and validation evidence is retained under the ignored Event 020 asset workspace.
- The RTA and RTX focus trees now apply route-aware AI weights to the four RTA archetype roots, the shared brood/crown progression, the three King governments, first crisis resolution, and the earned terminal route.
- The Rat King focus tree now includes twelve reachable, route-gated policy focuses: four Absolute Crown focuses, four Council focuses, and four Black-Breath Hierophancy focuses. Their rewards alter the royal meters, brood mass, force cap, overseas permission, and terminal preparation rather than granting human industry or manpower.
- The rat AI strategy file now has three route-specific RTX plans. Crown concentrates brutes and royal-node defense, Council favors distributed burrow and swarm coverage, and Hierophancy favors dock forces, coastal staging, and overseas pressure.
- The reachable RTA archetype lanes now have persistent route effects: Urban Citadel Relays, Field Migration Burrows, Dock Cross-Sea Cargo, and War Rail Breach contribute to capped Brood Mass pulses, division-cap refreshes, route exposure, and route-aware RTA AI. Cross-Sea Cargo remains subordinate to Evolution II's overseas gate.
- RTA and RTX focus and decision division-cap rewards now write to `black_plague_rat_division_cap_bonus`; the pulse refresh reapplies that persistent bonus instead of overwriting it when controlled-state counts are recalculated.
- The route-module behavior and asset contract are documented in `docs/systems/black_plague_rat_route_modules.md`.
- Event 20 workbook and exported catalogs include the live Diseases cluster, public Black Plague world-end row, SCN-012 two-tag wording, and current Rat King grace-period detail.
- Event map documentation records the new Royal Node and mission report identifiers.

## Validation evidence

- The touched Event 020 script and localisation files have balanced braces and no unsupported `<=` or `>=` operators.
- The Event 020 namespace contains 38 unique event IDs with no duplicate IDs.
- Player-facing Event 020 localisation keys have no duplicate keys; hidden scheduler callbacks intentionally have no title or description keys.
- Event 020 localisation files retain UTF-8 BOM encoding.
- The mandatory catalog exporter completed successfully after the workbook update and rewrote all three CSV exports.
- `hoi4_event_inspect` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, and `blockingDiagnostics: 0` for `events/020_black_death.txt` after the tranche.
- `hoi4_focus_inspect` returned `status: ok` for the RTA tree. The current RTA layout has two connector crossings and zero node intersections; the remaining inline errors are the MCP's workspace-scoped generic vanilla icon inventory diagnostics. These do not change the focus prerequisites or runtime route gates, but the geometry remains a presentation follow-up.
- The RTX route-policy inspection and render remain structurally valid; its known generic vanilla icon inventory limitation is separate from Event 20's custom wiring.
- Focused static checks after the scheduler, evolution, mapmode, and defeat-runtime patches report balanced braces and no unsupported comparison operators in every touched Event 020 script.
- The MCP report remains focused and workspace-partial; it reports deferred workspace-wide helper and lifecycle projections and is not a claim of full game validation.

## Remaining blockers and deviations

- RTA and RTX focus trees remain compact playable shells rather than the full accepted route depth; the main route-aware AI gates, twelve route-gated King policy focuses, and three route-specific RTX strategy plans are now present, but the broader accepted route architecture remains a follow-up.
- The accepted narrative and asset package still has queued unique Doctor Wu, outbreak, Rat Nation, weapon-delivery, Royal Node, and source-frame animation surfaces. Crown Strike, route crises, and Royal Burrow aftermath are wired, but their final dedicated art/audio/quote package is still queued.
- The state-clipped black fog enhancement remains unverified and is not used as a runtime prerequisite.
- No in-game process was launched, per repository instructions, so scenario intensities, Royal Node outcomes, mission timeout behavior, and rat grace-period transfer still require live consumer validation.
- Rat 3D model production is intentionally excluded by the user and remains outside this goal tranche.
- The bounded report/news art package is now promoted into runtime wiring. Origin recognition and late origin reports use `GFX_report_event_020_black_plague_origin`, overseas establishment uses `GFX_news_event_020_black_plague_overseas`, and Rat emergence/resurgence reports use `GFX_report_event_020_rat_emergence`; the sprites are registered in `interface/020_black_plague_event_pictures.gfx` and the final DDS evidence is recorded in `docs/assets/020_black_plague/event_art/manifest.md`.
- SCN-012 now converts intensity-scaled severe or collapsed candidates into several internal RTA warrens after the first carrier state. The target is two, three, four, or six total RTA brood states for Low, Medium, High, or Maximum intensity; no additional country tag is created, and the states use the normal Rat-Controlled phase, infestation, brood-strength marker, and capped pulse runtime.
- SCN-012 now nominates an established anchor for the shared state-owned scheduler and schedules the first `.900` callback before bootstrap cleanup, so scenario launches continue into normal disease, spread, evolution, and rat pulses.
- Scenario candidate collection now preserves existing established disease states when launched over an active crisis, excludes those states from reseeding, and still offers severe or collapsed human states as internal RTA brood candidates.
- Natural evolution readiness and activation now respect the five Event 020 disabled-evolution flags. Evolution checks use the existing MTTH-backed next-check date instead of attempting all eligible stages on every weekly pulse; SCN-012 remains an explicit I-IV force path.
- The contaminated-state mapmode now applies the player-visibility gate before painting an established Black Plague base, preventing private Incubating states from leaking black to unauthorized viewers while preserving black for visible established states.
- Rat King zero-state defeat now converges through an idempotent resolver that retires RTX, clears active royal and terminal-preparation state, removes its active-country registry entry, and emits the defeat report once without touching RTA or surviving plague states.

## Handoff

The Event 020 core and this content tranche are ready for the next content pass and targeted in-game validation.

The goal remains incomplete until the listed accepted content and presentation blockers are resolved.
