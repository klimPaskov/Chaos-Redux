# Event 20 Core Readiness Report

## Disposition

The Black Plague core-stabilization runtime supplies the epidemic lifecycle, response loop, evolution state machine, Rat country runtime, weaponization bridge, triggerable-scenario transaction, mapmode integration, logs, super-events, and earned terminal route. Shared completion remains partial: the natural event is default enabled, but the accepted Diseases cluster and the public Black Plague world-end row are not registered, and the Rat absorption decision still needs a design disposition.

This report does not claim that the entire original content specification is complete. Narrative expansion, bespoke models, and presentation depth remain deliberately queued.

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
- Finite Rat Nation pool and separate Rat King package with identity, AI, forces, decisions, origin archetypes, and focus trees.
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
- 23 Rat Nation and 38 Rat King focus nodes with complete title/description coverage, registered regular and shine sprites, and zero rendered connector crossings or intersections;
- 31 shared response decisions with resolved, action-specific cost strings and population-band material displays;
- 44.1 kHz stereo super-event audio with matching visible and dynamic audio IDs.

The HOI4 event inspection completed without a blocking focused diagnostic, but its workspace-wide projection was partial because of repository size. Hearts of Iron IV was not launched; engine-load and live-consumer validation belong to the user.

## Deferred content and assets

The following are explicitly outside this core-stabilization commit:

- bespoke Rat Nation and Rat King 3D unit models, materials, rigs, walking/attack/death actions, `.mesh` and `.anim` exports, and reimport evidence;
- additional triggerable scenario variants and scenario-specific narrative content;
- additional outbreak, response, brood, court, crisis, accident, and aftermath events;
- deeper Rat Nation and Rat King route content beyond the functional core trees;
- the accepted Severe Diseases cluster registration, member projection, UI/localisation mappings, and workbook cluster row;
- the public Black Plague terminal row in the world-end scenario registry, Event Details, localisation, and workbook;
- a design-backed resolution for the paid Rat absorption decision, whose current helper intentionally performs no territorial absorption;
- source-frame animated UI and evolution presentation packages;
- visible achievement registry, icons, and player-facing achievement presentation;
- a unique Doctor Wu report image;
- a dedicated weapon-delivery decision icon instead of the accepted Event 20 military-acceleration art reuse;
- state-clipped black fog, pending a verified safe engine rendering method;
- the queued defeat-aftermath super-event and other nonessential narrative presentation.

Rat units currently use a valid registered infantry entity so the country package has no missing model reference. This is an engine-safe core consumer, not the requested final rat model package.

## Historical handoffs

The 2026-07-24 Part 9 adapter and completion-audit handoffs describe an earlier fail-closed state. Their implementation blockers are superseded by this report and the live `020_black_plague_scenario_effects.txt` transaction. They remain in the plans directory as historical audit evidence.

## Live-validation boundary

The user should treat the commit as the stable source baseline for an in-game smoke test. Any live finding belongs to a follow-up stabilization patch. Additional content and model production can proceed from this baseline without redesigning the core state machine.

The editable event catalog workbook and its exported Events snapshot identify Event 20 as a minor fire-once event. The cluster and world-end scenario catalogs do not yet contain the accepted Diseases cluster or public Black Plague terminal route.
