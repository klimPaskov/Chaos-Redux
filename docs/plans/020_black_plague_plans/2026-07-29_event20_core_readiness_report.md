# Event 20 Core Readiness Report

> Historical core baseline, reconciled 2026-08-01: the later content tranche statically wires the RTA hierarchy consumers, RTX route crises `.57-.59`, Crown Strike `.64-.65`, and defeat/aftermath `.71-.75`. This report retains the baseline audit and its no-live-validation boundary; it is not a claim that those later surfaces are whole-spec complete.

## Disposition

The Black Plague core-stabilization runtime supplies the epidemic lifecycle, response loop, evolution state machine, Rat country runtime, weaponization bridge, triggerable-scenario transaction, mapmode integration, logs, super-events, and earned terminal route. The live registry now includes the Diseases cluster, the public Black Plague world-end row, the two-tag Rat lifecycle, and SCN-012. The later Event 020 consequence tranche also supplies the `.45` hierarchy acknowledgement, static RTA hierarchy consumers, RTX route crises, Crown Strike reports, and a scoped, metrics-gated defeat/aftermath path. Shared completion remains partial because broader route depth, narrative breadth, native-mission API decisions, selected crisis/route presentation assets, rights documentation, and live consumer validation remain open.

This report does not claim that the entire original content specification is complete. Narrative expansion and presentation depth remain deliberately queued. No bespoke 3D models are required or planned for this event; Rat units use the valid registered infantry entity documented below.

## Core systems in place

- Weighted single-mainland origin and nearby Threatened states.
- Threatened, Incubating, Infected, Severe Crisis, Collapsed, Contained, Recovery, Cured, and Rat-Controlled phases.
- Nonlinear population loss with one shared Deaths and Chaos feed.
- Border, railway, troop, occupation, refugee, war, port, overseas, biological-delivery, and Rat-occupation spread.
- Selected-state shared disease decisions with material, military, economic, and time costs.
- Visible Rat Infestation and 0–100 national countermeasure progress.
- Black base rendering for authorized established Black Plague states in the existing mapmode.
- Doctor Wu host bridge.
- Six-phase weaponization project, eighteen roles, four approaches, accidents, condemnation, and payload integration.
- Five logged evolutions with dynamic active and pre-fire Event Details entries.
- Reusable `RTA` Rat Nation and separate `RTX` Rat King packages with identity, AI, forces, decisions, origin archetypes, and focus trees.
- Three-way RTA hierarchy route graph with runtime cap, pulse, absorption, candidacy, route-aware AI consumers, and the `.45` acknowledgement event. RTA also carries live Hunger, Coherence, and derived Disease Dominion meters, a staged Fractured Instinct spirit, and the `.46` Hunger crisis event; dedicated hierarchy icons remain absent.
- RTX route-policy crisis events `.57`, `.58`, and `.59` with route-specific pulse and meter consumers.
- Crown Strike shared timed state action with `.64` success and `.65` timeout reports; this is not yet a native `activate_mission`/`days_mission_timeout` implementation.
- Evolution V last-response operations `Hold the Line` and `Secure the Refuge` are native `activate_mission`/`days_mission_timeout` missions in `common/decisions/020_black_plague_shared_response_decisions.txt`; live progress, success, timeout, and teardown validation remains open.
- Scoped `on_capitulation`/`on_state_control_changed` participant hooks and an idempotent Rat King defeat resolver with `.71`, eligible `.72`, gated slot 087, and `.73-.75` aftermath/sealing events; duration, peak, deaths, and major-participant metrics feed the explicit gate. The `.73` audience still falls back to the first eligible human response host, broader aftermath depth remains compact, and live validation is missing.
- Direct, idempotent `SCN-012` launch transaction that forces Evolutions I–IV but never grants Evolution V or world end.
- Earned Evolution V gates and deterministic terminal takeover.
- Event-owned seven-day scheduler and batched mapmode refresh.

## Audit evidence

The bounded implementation audits covered focus, country, decision, localisation, GFX, texture, constants, event-call, and block-balance surfaces. The repository cleanup audit then corrected the default-enabled settings gate, missing Rat decision-category registrations, incomplete custom-cost localisation, duplicate sound definitions, catalog type, and audio-hash records. The shared registry gaps listed in this report remain deferred multi-file work.

Specific source checks found:

- no unresolved Event 20 `constant:` reference;
- no duplicate `black_plague_*` or `doctor_wu_*` scripted effect or trigger;
- no unresolved custom Event 20 GFX reference or missing referenced DDS;
- matching definitions and callers for the Event 20 root, pulse callbacks, scenario callbacks, Doctor Wu callbacks, and weaponization callbacks;
- the reusable Rat Nation tag `RTA` and separate Rat King tag `RTX`, with matching country history, OOB, flags, portraits, leaders, AI, ideas, and locked zero-manpower templates;
- valid focus prerequisites after correcting two impossible mutually exclusive route locks;
- 50 Rat Nation and 70 Rat King focus nodes with complete title/description coverage, route-aware AI weights, registered regular and shine sprites, and no missing icon diagnostics; the focus inspections retain layout and filter warnings for authored spacing but no unresolved focus references;
- fourteen Event 20 achievement contracts with registry entries, completion triggers, localisation, and completed, grey, and not-eligible icon triplets;
- 31 shared response decisions with resolved, action-specific cost strings and population-band material displays;
- 44.1 kHz stereo super-event audio with matching visible and dynamic audio IDs.

The HOI4 event inspection completed without a blocking focused diagnostic, but its workspace-wide projection was partial because of repository size. Hearts of Iron IV was not launched; engine-load and live-consumer validation belong to the user.

## Current tranche delta and unresolved surfaces

The RTA hierarchy, RTX crises, Crown Strike, static defeat/aftermath surfaces, native last-response missions, dedicated weapon-delivery icon, source-frame Rat King portrait and Royal Burrows seal packages, Severe/Collapsed crisis seal, Rat King terminal-readiness seal, and three 44.1 kHz Event 020 WAVs are now present as implementation evidence, so the older broad “additional crisis and aftermath events” wording below is superseded.
The remaining queued work is broader narrative and route-specific decision depth beyond the implemented RTA/RTX trees, Crown Strike and Seal Royal Burrows native-mission API review, dedicated crisis-report/Doctor Wu/aftermath art, rights attribution, and focused live validation. The target-continent commitment is now fail-closed at 20 eligible states, two capital targets, and two refuge targets per candidate; after the earned route opens, `black_plague_rat_king_close_the_harbors` and `black_plague_rat_king_silence_the_capitals` provide timed state-targeted operations with Dominion, Brood Mass, division-cap, factory, and time costs, with `.83`/`.84` success and `.85`/`.86` invalidation reports before the 180-day Crown-the-Continent mission. Defeat or King recreation calls `black_plague_rat_king_clear_terminal_target_state`, the idempotent target teardown that clears selection, crown, and report flags, resets target counters and per-state markers, and clears operation cooldowns and active flags. The active `.80-.86` Event 020 map is `.80` target selection, `.81`/`.82` Crown-the-Continent success/break, `.83`/`.84` harbor/capital success, and `.85`/`.86` harbor/capital invalidation. The six hierarchy icons and the organized-rat news strip are promoted; the shared-board crisis seal and final-order decision seal are promoted; the scoped actor hooks, defeat metrics/gate, `.72` coupling, slot-087 package wiring, and the 50-focus RTA plus 70-focus RTX route surfaces are no longer queued.

Current tranche evidence is `common/on_actions/020_black_plague_on_actions.txt` for the narrow actor hooks; `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_triggers/020_black_plague_rat_triggers.txt`, and `common/script_constants/020_black_plague_constants.txt` for participant tracking, duration/peak metrics, and the explicit gate; `interface/020_black_plague_super_events.gfx`, `localisation/english/020_black_plague_super_events_l_english.yml`, `sound/chaosx_sound.asset`, and `music/chaosx_music_track_list.html` for slot-087 art/text/audio registration; and the resolver-owned `.72` dispatch in `common/scripted_effects/020_black_plague_rat_effects.txt`.

## Deferred content and assets

The following are explicitly outside this core-stabilization commit:

- bespoke Rat Nation and Rat King 3D unit models, materials, rigs, walking/attack/death actions, `.mesh` and `.anim` exports, and reimport evidence are explicitly not required or planned; the registered infantry entity is the accepted Rat visual consumer;
- additional triggerable scenario variants and scenario-specific narrative content;
- deeper route branches, additional accident/court narrative, and any further aftermath expansion;
- broader route-specific narrative, court-crisis presentation, and aftermath depth beyond the implemented 50-focus RTA and 70-focus RTX trees and the currently wired continuing decisions;
- additional source-frame crisis and evolution presentation beyond the promoted Rat King portrait, Royal Burrows seal, Severe/Collapsed crisis seal, and Rat King terminal-readiness seal packages;
- a unique Doctor Wu report image;
- broader crisis, Doctor Wu, route/hierarchy, and aftermath presentation beyond the promoted source-frame Rat King portrait, Royal Burrows seal, Severe/Collapsed crisis seal, and Rat King terminal-readiness seal packages;
- state-clipped black fog, pending a verified safe engine rendering method;
- broader nonessential narrative presentation beyond the promoted defeat-aftermath super-event 87 package.

Rat units currently use a valid registered infantry entity so the country package has no missing model reference. No bespoke Rat Nation or Rat King model package is required or planned for this event.

## Historical handoffs

The 2026-07-24 Part 9 adapter and completion-audit handoffs describe an earlier fail-closed state. Their implementation blockers are superseded by this report and the live `020_black_plague_scenario_effects.txt` transaction. They remain in the plans directory as historical audit evidence.

## Live-validation boundary

The user should treat this report as a static documentation baseline, not as evidence of a live smoke test. No in-game validation is claimed for the later RTA/RTX/Crown/aftermath tranche. Any live finding belongs to a follow-up stabilization patch. Additional content can proceed from this baseline without redesigning the core state machine.

The authoritative workbook and exported snapshots contain the live Event 20 row, Diseases cluster membership, public terminal row, and SCN-012 scenario contract. Historical pre-implementation reports in this directory retain their original wording where they document earlier fail-closed states.
