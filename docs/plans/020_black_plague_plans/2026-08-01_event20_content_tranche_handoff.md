# Event 020 content tranche handoff

Date: 2026-08-01

## Scope

This tranche extends the load-ready Event 020 gameplay core without producing 3D models, meshes, skeletal actions, or model-dependent assets.

The two-tag correction remains authoritative: `RTA` is the sole reusable Rat Nation carrier and `RTX` is the separate Rat King.

## Implemented in this tranche

- The triggerable SCN-012 bridge is now safe to signal again after a successful launch. A repeat signal performs only runtime-count, air-cleanliness, shared-threat, mapmode, and board reconciliation; it does not reseed states, reset intensity values, re-run Evolutions I-IV, create another report, or emit another coronation. The initial seed preserves already established scenario state ledgers and increments the seeded-state counter only for newly seeded anchors. The public launch status distinguishes repeat reconciliation from a terminally unavailable launch, and the scoped bootstrap flag is cleared in both paths.

- The narrow `on_state_control_changed` hook now makes eligible non-Rat-Controlled states captured by RTA or RTX immediately Rat-Controlled through the shared exposure adapter. It records one mortality transaction, applies the occupation devastation, registers the reusable RTA brood marker where applicable, and updates the shared controlled-state registry and mapmode without adding a tag.

- The reusable RTA carrier now has the three missing live pressure registers
  from the country specification: Hunger, Coherence, and derived Disease
  Dominion. They initialize with each carrier, update on the existing capped
  pulse, appear in the Rat category description, and feed route and hierarchy
  behavior without adding a country tag or a second disease category.
- RTA hierarchy choices now remove the starting `Fractured Instinct` spirit
  and raise Coherence. The spirit supplies the early coordination penalty and
  is cleaned up when the carrier retires or becomes the Rat King source.
- RTA Hunger now has a player-facing `.46` crisis event. Rationing spends mass
  to restore coordination, while destructive feeding adds mass at the cost of
  Coherence and state devastation, infestation, and mapmode dirtiness.

- The shared disease category now includes a selectable Emergency Countermeasure Drive mission with stockpile payment, 90-day timeout, countermeasure progress gain, and timeout exposure and stability pressure.
- The shared disease category now includes two Evolution V human last-response missions: Hold the Line and Secure the Refuge. They pay equipment, trains, fuel, manpower, command power, civilian factories, stability, and war-support costs, gain weekly progress from live war/countermeasure/held-state conditions, lower terminal preparation on success, and raise royal pressure and exposure on timeout. Runtime and terminal cleanup remove both missions idempotently.
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
- The RTA brood category also exposes `Strip the Outer Districts` and state-targeted `Establish a Burrow Node`. Feeding trades Hunger for Brood Mass and visible infestation/devastation in one rat-held state under a timed scar/cooldown; Burrow Nodes spend Brood Mass and return local Brood Mass plus Coherence during their timed pulse window. Both remain inside the existing category and use only the reusable `RTA` carrier.
- RTA can also `Follow the Refugee Road` into a selected human enemy state adjacent to rat-held ground. The decision spends Brood Mass, applies the canonical refugee-movement exposure with Rat Occupation provenance, and sets a state cooldown so the route cannot cascade within one pulse.
- The same RTA category now exposes `Concentrate Brood`, `Scatter Brood`, `Devour Rival`, and state-targeted `Resist Absorption`. Concentration delays the shared growth clock while raising the persistent cap and Coherence; scattering spends low Coherence for a capped two-formation burst and adds Hunger; Devour Rival clears the merger clock for one immediate state-marker absorption attempt; Resist Absorption spends carrier mass to reinforce a weaker marker and set a timed shield that the automatic merger comparison respects.
- The RTA hierarchy focus choice now has route-aware AI weights. Distributed Instinct is favored by broad Field or Urban carriers, Dominant Beast by concentrated War carriers or an active Hunger crisis, and Emergent Cunning by Dock carriers after Evolution II. The three hierarchy follow-ups carry the same route signal, using centralized fixed-point factors rather than disconnected focus weights.
- Each RTA hierarchy route now has a continuing choice in the same category. Distributed Instinct can distribute nest signals across more than one controlled state for Coherence and capped capacity; Dominant Beast can seat an alpha command pattern for Sentience and capacity at a Hunger cost; Emergent Cunning can decode a selected human enemy rail, supply, capital, or coastal logistics state beside rat-held ground through the canonical internal-transport exposure ledger.
- The RTX court's Royal Strike is now a state-targeted wartime operation. It selects a human-controlled enemy state, spends Dominion and Brood Mass, reserves one civilian factory for 45 days, applies the canonical Rat Occupation exposure, records the selected state as a short-lived event target, and reports the strike to that controller through `chaosx.nr20.76`; separate country and state cooldowns prevent repeat targeting for 90 days.
- The weaponization category now exposes paid post-project stockpile controls. Expand the native payload reserve in one-batch, 60-day runs that consume support equipment, motorized transport, command power, fuel, and two civilian factories while raising risk; destroy the entire reserve in a guarded 30-day operation that consumes support equipment, command power, fuel, lowers risk, and closes the accident scheduler until another expansion.
- RTA and RTX focus and decision division-cap rewards now write to `black_plague_rat_division_cap_bonus`; the pulse refresh reapplies that persistent bonus instead of overwriting it when controlled-state counts are recalculated.
- The route-module behavior and asset contract are documented in `docs/systems/black_plague_rat_route_modules.md`.
- Event 20 workbook and exported catalogs include the live Diseases cluster, public Black Plague world-end row, SCN-012 two-tag wording, and current Rat King grace-period detail.
- Event map documentation records the new Royal Node and mission report identifiers.
- Scoped Rat King defeat hooks now live in `common/on_actions/020_black_plague_on_actions.txt`; `common/scripted_effects/020_black_plague_rat_effects.txt` records deduplicated major human participants, duration/peak metrics, and idempotent `.71`, eligible `.72`, gated slot 087, and `.73-.75` dispatch.
- The current qualification constants and trigger are in `common/script_constants/020_black_plague_constants.txt`, `common/script_constants/020_black_plague_evolution_constants.txt`, and `common/scripted_triggers/020_black_plague_rat_triggers.txt`: 180 days, 250,000,000 deaths, 24 peak controlled states, 12 peak continent states at ratio 0.50, and 3 major participants.
- Slot 087 presentation is promoted: `interface/020_black_plague_super_events.gfx`, `localisation/english/020_black_plague_super_events_l_english.yml`, `sound/chaosx_sound.asset`, and `music/chaosx_music_track_list.html` register the final art, selected text, audio ID 103, and settings wrappers.
- Evolution IV's Events Log now consumes the ten-frame authored Rat King portrait through `GFX_portrait_black_plague_rat_king_animated`, while ordinary leader views retain `GFX_portrait_black_plague_rat_king` as the static fallback. Source frames, processed frames, review previews, DDS dimensions, and hashes are recorded in `docs/assets/020_black_plague/rat_king_animation/manifest.md`.
- Natural Evolution III now requires a verified three-state connected Infected/Severe/Collapsed basin. The spawn selector and both readiness gates use the shared `black_plague_rat_state_has_connected_basin_signal` trigger, while SCN-012 keeps its scoped bootstrap path for deliberate multi-basin setup.

## Validation evidence

- The touched Event 020 script and localisation files have balanced braces and no unsupported `<=` or `>=` operators.
- The Event 020 namespace contains 53 unique event IDs with no duplicate IDs.
- Player-facing Event 020 localisation keys have no duplicate keys; hidden scheduler callbacks intentionally have no title or description keys.
- Event 020 localisation files retain UTF-8 BOM encoding.
- The mandatory catalog exporter completed successfully after the workbook update and rewrote all three CSV exports.
- `hoi4_event_inspect` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, and `blockingDiagnostics: 0` for `events/020_black_death.txt` after the tranche.
- `hoi4_focus_inspect` returned `status: ok` for the RTA tree. The current RTA layout has two connector crossings and zero node intersections; the remaining inline errors are the MCP's workspace-scoped generic vanilla icon inventory diagnostics. These do not change the focus prerequisites or runtime route gates, but the geometry remains a presentation follow-up.
- The RTX route-policy inspection returned `focusCount: 70`, complete title resolution, and no missing icon diagnostics. Remaining inline diagnostics are authored layout/filter warnings only.
- Focused static checks after the scheduler, evolution, mapmode, and defeat-runtime patches report balanced braces and no unsupported comparison operators in every touched Event 020 script.
- The MCP report remains focused and workspace-partial; it reports deferred workspace-wide helper and lifecycle projections and is not a claim of full game validation.

## Remaining blockers and deviations

- The RTA and RTX trees now meet the accepted focus-count floors at 50 and 70 nodes. Route-specific decisions, the three hierarchy actions, and court operations are wired; remaining narrative depth is primarily report text, dedicated crisis art, and live route validation.
- The accepted narrative and asset package still has queued outbreak, Rat Nation, weapon-delivery, reconstruction, and crisis-seal surfaces. The shared-board rat-infestation source-frame badge, five evolution report cards, Severe Crisis, Doctor Wu, Crown Strike, route crises, Rat King aftermath, Royal Burrow aftermath, slot 087 art/text/audio wiring, and the Evolution IV Rat King portrait are promoted, but broader dedicated art/depth remains queued.
- The state-clipped black fog enhancement remains unverified and is not used as a runtime prerequisite.
- No in-game process was launched, per repository instructions, so scenario intensities, Royal Node outcomes, mission timeout behavior, and rat grace-period transfer still require live consumer validation.
- No in-game process was launched, so the new scoped defeat hooks, metric gate, `.72` coupling, slot-087 trigger/audio, and `.73` audience behavior also require live consumer validation; `.73` prefers the saved defeat contributor, then a registered response country, then the first eligible human response host.
- The terminal route now records remaining human-state population once per state through the shared exact-loss contract before transfer, so the final death and Chaos ledgers are not skipped when world end begins.
- Rat 3D model production is intentionally excluded by the user and remains outside this goal tranche.
- The bounded report/news art package is now promoted into runtime wiring. Origin recognition and late origin reports use `GFX_report_event_020_black_plague_origin`, overseas establishment uses `GFX_news_event_020_black_plague_overseas`, and Rat emergence/resurgence reports use `GFX_report_event_020_rat_emergence`; the sprites are registered in `interface/020_black_plague_event_pictures.gfx` and the final DDS evidence is recorded in `docs/assets/020_black_plague/event_art/manifest.md`.
- SCN-012 now converts intensity-scaled infected-or-worse candidates into several internal RTA warrens after the first carrier state. The target is two, three, four, or six total RTA brood states for Low, Medium, High, or Maximum intensity; no additional country tag is created, and the states use the normal Rat-Controlled phase, infestation, brood-strength marker, and capped pulse runtime.
- SCN-012 now performs a fail-closed geography/package preflight before initializing the disease or rat registries, nominates an established anchor for the shared state-owned scheduler, and schedules the first `.900` callback before bootstrap cleanup, so scenario launches continue into normal disease, spread, evolution, and rat pulses.
- Scenario candidate collection now preserves existing established disease states when launched over an active crisis, excludes those states from reseeding, and still offers severe or collapsed human states as internal RTA brood candidates.
- Scenario brood bookkeeping now counts the reusable RTA carrier and surviving state markers before attempting a top-up, so an idempotent repeat launch does not fail merely because the candidate pool is exhausted.
- The triggerable-scenario impact text now reports the live established-state, internal-brood, and Royal Basin targets from shared constants. The launch report records the actual continent, state, brood, and Royal Basin totals, explicitly preserves the `RTA`/`RTX` two-tag boundary, and explains that Evolutions V and world end remain earned routes.
- A failed SCN-012 postcondition now has an explicit retryable launch-status line after the effect clears temporary reservations, so the scenario window distinguishes a recoverable setup failure from an unavailable world.
- Natural evolution readiness and activation now respect the five Event 020 disabled-evolution flags. Evolution checks use the existing MTTH-backed next-check date and advance at most one stage per due pulse, marking progress only after activation succeeds; SCN-012 remains an explicit I-IV force path. Evolution II requires a verified human-controlled destination port, Evolution III records the first active RTA carrier, and Evolutions IV and V require RTX as their actor.
- Before forcing Evolution II, SCN-012 reuses an established human-controlled port or seeds one valid human port if ordinary continent sampling missed every port. The preflight rejects a world with no human-controlled port, preserving the verified-port actor contract and preventing an actorless Evolution II log row.
- The contaminated-state mapmode now applies the player-visibility gate before painting an established Black Plague base, preventing private Incubating states from leaking black to unauthorized viewers while preserving black for visible established states.
- Rat King zero-state defeat now converges through an idempotent resolver that retires RTX, clears active royal and terminal-preparation state, records scoped participants and peak metrics, removes its active-country registry entry, emits the defeat report once, conditionally dispatches eligible `.72` and gated slot 087, and leaves RTA and surviving plague states intact.

## Handoff

The Event 020 core and this content tranche are ready for the next content pass and targeted in-game validation. The scoped defeat/slot-087 wiring is static implementation evidence, not a live completion claim.

The goal remains incomplete until the listed accepted content and presentation blockers are resolved.
