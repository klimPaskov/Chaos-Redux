# 020 Black Plague coding prompt

Implement Event 020 Black Plague according to the accepted spec package under `docs/specs/020_black_plague_specs/` or the equivalent package path provided by the parent. Treat the current user brief, continuation prompts, and this package as the design authority. The old catalog row that describes a continent-wide temporary idea is stale.

Read every spec part, matrix, prompt, reading note, and handoff in the package before editing. Read and follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `hoi4-decisions-missions`, and `hoi4-focus-trees`. Read the relevant offline Paradox wiki pages, vanilla documentation, and existing Chaos Redux patterns for every system touched.

## Core implementation goals

- Replace Event 020 with a state-based Black Death outbreak that begins in a weighted mainland state.
- Integrate it with the shared biological warfare, disease containment, disease mapmode, Deaths, Chaos, condemnation, world-threat, event-log, event-detail, and evolution systems.
- Do not create a duplicate Black Plague decision category. Use the shared disease board and make it dynamic by state status.
- Implement state statuses for clean, prepared, threatened, infected, contained, recovering, cured, weaponized, and rat-held states.
- Apply real population deaths over time through the shared Deaths system. Ignored high-population states must be able to suffer very large population loss.
- Make spread dynamic through adjacency, population, development, infrastructure, ports, war, occupation, troop movement, refugees, containment, cure progress, and evolution state.
- Implement cure progress as a long response track that lowers deaths, lowers spread, and only later allows cleanup.
- Implement gameplay-only Black Death weaponization through the existing special-project and biowarfare structure. Do not write real-world lab or biological weapon procedure content.

## Evolution goals

- Evolution I makes the strain harder to cure, more lethal, and faster to become a crisis.
- Evolution II unlocks overseas spread through ports, convoys, troop routes, and naval movement.
- Evolution III creates rat nations from the worst diseased connected states. Rat nations keep plague modifiers, use nonhuman mutated rat units, grow through ticks, and are hostile to humans.
- Evolution IV creates a separate King of Rats country that unites rat nations and receives a deeper focus tree.
- Evolution V unlocks the King focus-tree world-end path and terminal world-end scenario after focus, territory, death, and world-end conditions are met.

## Country and focus goals

Implement rat nation and King country packages fully. Include tags, history setup, public names, adjectives, parties, leaders, portraits, flags, starting state setup, plague state retention, ideas, focus trees, decisions, unit logic, AI, localisation, docs, and shared special chaos country plus actual nonhuman classification.

Base rat focus trees must include real route families for warren growth, swarm warfare, plague ecology, defense, absorption, and King preparation. King focus tree must include coronation, sentience, government routes, swarm command, warren economy, plague mastery, human terror, rat unity, continental conquest, and a terminal world-end route. Do not implement these trees as thin vertical chains or repeated small modifier lines.

Rat nations and the King must not use human manpower or ordinary equipment as their core force model. Implement mutated rat unit families and automatic growth based on warren strength, plague states, severity, terrain, focus progress, and King route state.

## Decision, mission, UI, and map goals

Implement the dynamic disease-board decision and mission families from Part 8, Part 9, and the decision mission matrix. Use meaningful costs beyond political power and command power. Use target selection, phased visibility, cooldowns, and cleanup to avoid decision spam.

Update the disease mapmode and disease UI whenever a state becomes infected, contained, recovering, cured, weaponized, rat-held, or cleaned. Implement black fog or the closest approved engine-supported disease presentation. Report limitations clearly if true black fog on the map cannot be supported.

## Super-event, asset, and achievement goals

Research and wire the King reveal and rat world-end super-events through the super-event workflow. Optional continental threat and defeat aftermath packages should be implemented only if their thresholds are accepted. Do not use unresearched titles, quotes, remarks, slogans, allusions, or audio.

Produce or wire required assets, including disease status visuals, black fog or approved disease presentation, shared board UI assets, decision icons, focus icons, idea icons, rat flags, King flags, rat portraits, King portrait, unit icons, report images, news images, super-event images, and achievement icons. Do not silently use placeholders. Report blocked assets clearly.

Implement the achievement suite with real tracking, disqualifiers, icons, docs, and no trivial unlocks.

## AI, docs, and validation goals

Implement dynamic AI behavior for outbreak owners, threatened countries, infected countries, port countries, biowarfare countries, rat nations, King of Rats, human neighbors, major powers, coalition responders, and cleanup actors.

Write final localisation from the direction in the spec. The spec is not pasteable text. Keep event details descriptive and avoid mechanical effect lists. Do not reveal hidden rat or King content in early disease text.

Update event docs, system docs if needed, music docs, asset manifests, event logs, event details, evolutions, cluster membership if accepted, achievements, and spreadsheet after final in-game wording exists.

Before near completion, spawn `chaosx_improvement_loop_planner` with `fork_context=false`. Resolve its addendum or closure handoff. Then run relevant audits: scripted systems, decisions, focus trees, countries, localisation, assets, super-events, documentation, spreadsheet, and final completion.

Report every simplification, blocked asset, missing route, missing AI behavior, skipped meaningful validation, unresolved plan, or unsupported presentation feature. Do not claim completion if any accepted spec surface is missing.
