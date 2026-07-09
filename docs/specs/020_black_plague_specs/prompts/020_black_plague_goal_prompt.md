# 020 Black Plague goal prompt

Implement Event 020 Black Plague from the planning package at `docs/specs/020_black_plague_specs/`. Start from `prompts/020_black_plague_coding_prompt.md`, then read every spec part, matrix, prompt, research note, and handoff. Treat the old Event 20 catalog row as stale. The new design is state-based Black Death, not a continent-wide temporary idea.

Read and follow `AGENTS.md`, the required Chaos Redux skills, decision and focus skills, offline wiki pages, vanilla docs, and repo patterns before editing.

Build a living disease system. The first outbreak picks a weighted mainland state, biased toward high population, low development, poor infrastructure, weak disease protection, and poor state capacity. Use state statuses for clean, prepared, threatened, infected, contained, recovering, cured, weaponized, and rat-held states. Wire mapmode and disease UI updates whenever status changes.

Use the shared biological warfare and disease-containment system. Do not create a duplicate Black Plague category. The shared disease board should change by state status, from prevention and threat controls to quarantine, hospitals, monitoring, cleanup, weapon exposure response, and rat-border containment.

Deaths must reduce real state population over time and feed the shared Deaths and Chaos systems. Ignored high-population states must be able to lose very large population shares. Cure progress lowers deaths first, spread second, then allows cleanup. Weaponization must use existing special projects and biowarfare abstraction only. Do not add real-world lab procedures.

Implement the evolution chain. Evolution I makes the strain harder to cure, more lethal, and faster to become a crisis. Evolution II unlocks overseas spread through ports, convoys, troops, and naval routes. Evolution III creates rat nations from the worst diseased connected states. Rat nations keep plague in their states, ignore human manpower and normal equipment, use mutated rat units, grow through ticks, are hostile to humans, and absorb weaker adjacent rat nations. Evolution IV creates a separate King of Rats country from the strongest rat nation and transfers rat states. Evolution V unlocks the King focus-tree world-end path.

Create complete rat and King country packages: tags, history setup, names, parties, leaders, portraits, flags, ideas, units, ticks, trees, decisions, AI, localisation, docs, and shared nonhuman classification. Base rat trees need warren growth, swarm warfare, plague spread, defense, and annexation. The King tree needs sentience, government routes, swarm command, warren economy, plague mastery, continental conquest, and a terminal world-end path.

Implement the world-end scenario where the King of Rats takes over the world after finishing the path and controlling the required continent or state set with enough deaths or rat-held territory. Research and wire the King reveal and rat world-end super-events through the super-event skill. Do not use unresearched titles, quotes, remarks, allusions, or audio.

Produce or wire required assets, including black fog or approved disease presentation, shared board UI, rat flags, portraits, focus, decision, idea and unit icons, super-event images, report images, news images, and achievement icons. Implement achievements with tracking and disqualifiers.

Before near completion, spawn `chaosx_improvement_loop_planner` with `fork_context=false` for the mandatory depth and anti-bloat pass. Resolve its addendum or closure handoff. Then run relevant audits and completion checks. Do not claim completion while specs, assets, localisation, AI, focus trees, country packages, docs, event logs, spreadsheet alignment, achievements, or super-events are missing.

<!-- Character count: 3760 before this comment -->
