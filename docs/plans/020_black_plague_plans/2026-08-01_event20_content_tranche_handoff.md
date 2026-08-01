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
- The Rat King focus tree now has 70 focuses. Six additional Crown, Council, and Hierophancy lanes plus Royal Node Watch and Crown Strike Preparations deepen the route without creating a new tag, disease category, human manpower, ordinary equipment, or model dependency. All 20 added focus keys are localized and use registered Event 020 custom goal sprites.
- The rat AI strategy file now has three route-specific RTX plans. Crown concentrates brutes and royal-node defense, Council favors distributed burrow and swarm coverage, and Hierophancy favors dock forces, coastal staging, and overseas pressure.
- The reachable RTA archetype lanes now have persistent route effects: Urban Citadel Relays, Field Migration Burrows, Dock Cross-Sea Cargo, and War Rail Breach contribute to capped Brood Mass pulses, division-cap refreshes, route exposure, and route-aware RTA AI. Cross-Sea Cargo remains subordinate to Evolution II's overseas gate.
- The rat categories now expose seven route operations: four timed RTA operations (Citadel Stockpile, Migration Lanes, Tide Manifest, Rail Breach Order) and three timed RTX policy operations (Crown Tithe, Council Audit, Hierophant Broadcast). Their costs and gains are centralized and their flags are consumed by spread, cap, or royal preparation logic.
- RTA and RTX focus and decision division-cap rewards now write to `black_plague_rat_division_cap_bonus`; the pulse refresh reapplies that persistent bonus instead of overwriting it when controlled-state counts are recalculated.
- The route-module behavior and asset contract are documented in `docs/systems/black_plague_rat_route_modules.md`.
- Event 20 workbook and exported catalogs include the live Diseases cluster, public Black Plague world-end row, SCN-012 two-tag wording, and current Rat King grace-period detail.
- Event map documentation records the new Royal Node and mission report identifiers.
- Scoped Rat King defeat hooks now live in `common/on_actions/020_black_plague_on_actions.txt`; `common/scripted_effects/020_black_plague_rat_effects.txt` records deduplicated major human participants, duration/peak metrics, and idempotent `.71`, eligible `.72`, gated slot 087, and `.73-.75` dispatch.
- The current qualification constants and trigger are in `common/script_constants/020_black_plague_constants.txt`, `common/script_constants/020_black_plague_evolution_constants.txt`, and `common/scripted_triggers/020_black_plague_rat_triggers.txt`: 180 days, 250,000,000 deaths, 24 peak controlled states, 12 peak continent states at ratio 0.50, and 3 major participants.
- Slot 087 presentation is promoted: `interface/020_black_plague_super_events.gfx`, `localisation/english/020_black_plague_super_events_l_english.yml`, `sound/chaosx_sound.asset`, and `music/chaosx_music_track_list.html` register the final art, selected text, audio ID 103, and settings wrappers.

## Validation evidence

- The touched Event 020 script and localisation files have balanced braces and no unsupported `<=` or `>=` operators.
- The Event 020 namespace contains 38 unique event IDs with no duplicate IDs.
- Player-facing Event 020 localisation keys have no duplicate keys; hidden scheduler callbacks intentionally have no title or description keys.
- Event 020 localisation files retain UTF-8 BOM encoding.
- The mandatory catalog exporter completed successfully after the workbook update and rewrote all three CSV exports.
- `hoi4_event_inspect` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, and `blockingDiagnostics: 0` for `events/020_black_death.txt` after the tranche.
- `hoi4_focus_inspect` returned `status: ok` for the RTA tree. The current RTA layout has two connector crossings and zero node intersections; the remaining inline errors are the MCP's workspace-scoped generic vanilla icon inventory diagnostics. These do not change the focus prerequisites or runtime route gates, but the geometry remains a presentation follow-up.
- The RTX route-policy inspection returned `focusCount: 70`, complete title resolution, and no missing icon diagnostics. Remaining inline diagnostics are authored layout/filter warnings only.
- Focused static checks after the scheduler, evolution, mapmode, and defeat-runtime patches report balanced braces and no unsupported comparison operators in every touched Event 020 script.
- The MCP report remains focused and workspace-partial; it reports deferred workspace-wide helper and lifecycle projections and is not a claim of full game validation.

## Remaining blockers and deviations

- The RTA and RTX trees now meet the accepted focus-count floors at 50 and 70 nodes. Route-specific decisions and court operations are wired; remaining narrative depth is primarily report text, dedicated crisis art, and live route validation.
- The accepted narrative and asset package still has queued outbreak, Rat Nation, weapon-delivery, reconstruction, crisis-seal, and animated Rat King portrait surfaces. The shared-board rat-infestation source-frame badge, five evolution report cards, Severe Crisis, Doctor Wu, Crown Strike, route crises, Rat King aftermath, Royal Burrow aftermath, and slot 087 art/text/audio wiring are promoted, but broader dedicated art/depth remains queued.
- The state-clipped black fog enhancement remains unverified and is not used as a runtime prerequisite.
- No in-game process was launched, per repository instructions, so scenario intensities, Royal Node outcomes, mission timeout behavior, and rat grace-period transfer still require live consumer validation.
- No in-game process was launched, so the new scoped defeat hooks, metric gate, `.72` coupling, slot-087 trigger/audio, and `.73` audience behavior also require live consumer validation; the current `.73` audience remains the first eligible human response host.
- Rat 3D model production is intentionally excluded by the user and remains outside this goal tranche.
- The bounded report/news art package is now promoted into runtime wiring. Origin recognition and late origin reports use `GFX_report_event_020_black_plague_origin`, overseas establishment uses `GFX_news_event_020_black_plague_overseas`, and Rat emergence/resurgence reports use `GFX_report_event_020_rat_emergence`; the sprites are registered in `interface/020_black_plague_event_pictures.gfx` and the final DDS evidence is recorded in `docs/assets/020_black_plague/event_art/manifest.md`.
- SCN-012 now converts intensity-scaled severe or collapsed candidates into several internal RTA warrens after the first carrier state. The target is two, three, four, or six total RTA brood states for Low, Medium, High, or Maximum intensity; no additional country tag is created, and the states use the normal Rat-Controlled phase, infestation, brood-strength marker, and capped pulse runtime.
- SCN-012 now nominates an established anchor for the shared state-owned scheduler and schedules the first `.900` callback before bootstrap cleanup, so scenario launches continue into normal disease, spread, evolution, and rat pulses.
- Scenario candidate collection now preserves existing established disease states when launched over an active crisis, excludes those states from reseeding, and still offers severe or collapsed human states as internal RTA brood candidates.
- Natural evolution readiness and activation now respect the five Event 020 disabled-evolution flags. Evolution checks use the existing MTTH-backed next-check date instead of attempting all eligible stages on every weekly pulse; SCN-012 remains an explicit I-IV force path.
- The contaminated-state mapmode now applies the player-visibility gate before painting an established Black Plague base, preventing private Incubating states from leaking black to unauthorized viewers while preserving black for visible established states.
- Rat King zero-state defeat now converges through an idempotent resolver that retires RTX, clears active royal and terminal-preparation state, records scoped participants and peak metrics, removes its active-country registry entry, emits the defeat report once, conditionally dispatches eligible `.72` and gated slot 087, and leaves RTA and surviving plague states intact.

## Handoff

The Event 020 core and this content tranche are ready for the next content pass and targeted in-game validation. The scoped defeat/slot-087 wiring is static implementation evidence, not a live completion claim.

The goal remains incomplete until the listed accepted content and presentation blockers are resolved.
