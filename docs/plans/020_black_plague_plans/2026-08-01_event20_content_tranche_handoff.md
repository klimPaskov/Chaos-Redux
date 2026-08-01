# Event 020 content tranche handoff

Date: 2026-08-01

## Scope

This tranche extends the load-ready Event 020 gameplay core without producing 3D models, meshes, skeletal actions, or model-dependent assets.

The two-tag correction remains authoritative: `RTA` is the sole reusable Rat Nation carrier and `RTX` is the separate Rat King.

## Implemented in this tranche

- The shared disease category now includes a selectable Emergency Countermeasure Drive mission with stockpile payment, 90-day timeout, countermeasure progress gain, and timeout exposure and stability pressure.
- Royal Node strikes now require a military route, resolve against King Dominion, reduce infestation and Dominion on success, block the next royal pulse for a bounded period, and feed Dominion, hunger, and terminal preparation on counterfire.
- Royal Node success and counterfire have player-facing country reports `chaosx.nr20.54` and `chaosx.nr20.55`.
- Emergency Countermeasure Drive timeout has the player-facing report `chaosx.nr20.56`.
- Rat King pulse blocking is consumed by the existing rat runtime pulse and is cleared on King initialization.
- RTA reinforcement tracking now records capped brood divisions raised for achievement predicates.
- The superseded multi-country achievement condition now measures absorbed RTA brood states under the two-tag model.
- The pre-terminal continent achievement no longer depends on Evolution V having already been recorded, so its route can be evaluated before the terminal takeover.
- The fourteen Event 020 achievement contracts now have public registry entries and player-facing name, description, eligibility, and completion tooltip localisation.
- The fourteen Event 020 achievement contracts now have completed, grey, and not-eligible 64x64 DDS triplets, with 42 explicit aliases in `interface/chaosx_achievements.gfx`; source, processed, prompt, contact-sheet, and validation evidence is retained under the ignored Event 020 asset workspace.
- The RTA and RTX focus trees now apply route-aware AI weights to the four RTA archetype roots, the shared brood/crown progression, the three King governments, first crisis resolution, and the earned terminal route.
- The Rat King focus tree now includes twelve reachable, route-gated policy focuses: four Absolute Crown focuses, four Council focuses, and four Black-Breath Hierophancy focuses. Their rewards alter the royal meters, brood mass, force cap, overseas permission, and terminal preparation rather than granting human industry or manpower.
- The rat AI strategy file now has three route-specific RTX plans. Crown concentrates brutes and royal-node defense, Council favors distributed burrow and swarm coverage, and Hierophancy favors dock forces, coastal staging, and overseas pressure.
- Event 20 workbook and exported catalogs include the live Diseases cluster, public Black Plague world-end row, SCN-012 two-tag wording, and current Rat King grace-period detail.
- Event map documentation records the new Royal Node and mission report identifiers.

## Validation evidence

- The touched Event 020 script and localisation files have balanced braces and no unsupported `<=` or `>=` operators.
- The Event 020 namespace contains 38 unique event IDs with no duplicate IDs.
- Player-facing Event 020 localisation keys have no duplicate keys; hidden scheduler callbacks intentionally have no title or description keys.
- Event 020 localisation files retain UTF-8 BOM encoding.
- The mandatory catalog exporter completed successfully after the workbook update and rewrote all three CSV exports.
- `hoi4_event_inspect` returned `status: ok`, `code: EVENT_INSPECTED_PARTIAL`, and `blockingDiagnostics: 0` for `events/020_black_death.txt` after the tranche.
- `hoi4_focus_inspect` returned `status: ok` for both Event 020 trees after the AI-weight pass; layout metrics retained zero connector crossings and zero node intersections. Its inline report still lists generic vanilla icon references as workspace-scoped diagnostics.
- After the route-policy expansion, `hoi4_focus_inspect` reports 50 RTX focuses, 56 connectors, zero connector crossings, and zero node intersections. `hoi4_focus_render` also returned `status: ok`; its only remaining inline diagnostics are the known generic vanilla icon inventory limitation.
- The MCP report remains focused and workspace-partial; it reports deferred workspace-wide helper and lifecycle projections and is not a claim of full game validation.

## Remaining blockers and deviations

- RTA and RTX focus trees remain compact playable shells rather than the full accepted route depth; the main route-aware AI gates, twelve route-gated King policy focuses, and three route-specific RTX strategy plans are now present, but the broader accepted route architecture remains a follow-up.
- The accepted narrative and asset package still has queued unique Doctor Wu, outbreak, Rat Nation, weapon-delivery, Royal Node, and source-frame animation surfaces.
- The state-clipped black fog enhancement remains unverified and is not used as a runtime prerequisite.
- No in-game process was launched, per repository instructions, so scenario intensities, Royal Node outcomes, mission timeout behavior, and rat grace-period transfer still require live consumer validation.
- Rat 3D model production is intentionally excluded by the user and remains outside this goal tranche.

## Handoff

The Event 020 core and this content tranche are ready for the next content pass and targeted in-game validation.

The goal remains incomplete until the listed accepted content and presentation blockers are resolved.
