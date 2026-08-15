# Goal Prompt: Complete Event 19 Infantry Spawn Rework

Implement Chaos Redux Event ID `19`, Infantry Spawn, from `docs/specs/019_infantry_spawn_specs/` to its fullest extent. Preserve ID 19 and Minor Repeatable classification. The request prefix `017` is not the event ID. Read the package, `AGENTS.md`, relevant skills, local code, offline wiki pages, vanilla documentation, and current precedents.

Replace the flat infantry loop with the full generation system. Evaluate every valid country. Use diminishing coverage so large countries gain more units while a smaller share of states is selected. Implement weighted formation lots, equipment accounting, Muster Control, Army Congestion, integration, demobilization, AI, and exploit protection.

> **Current implementation boundary (2026-08-09):** The consolidated Event 19 registry file remains the only dedicated registry code file, but owner adapters for providers `511-514`, `518`, `520-522` intentionally live in their existing parent integration surfaces. This accepted architecture satisfies the one-entry/no-list-edit rule; do not migrate owner callbacks into the consolidated file or add another registry file without a new design decision.

Implement four evolutions with active-event and pre-fire paths. Evolution I improves organization and equipment. Evolution II adds multiple serious, advanced, and strange units, finite technology-locked equipment, and costly requests. Evolution III stops normal automatic spawning by default, enables fully random safe battalion and support composition, separates quality from coherence, and adds claimant demands, takeover, and revolt. Evolution IV uses an opt-in Chaos unit registry with train-versus-spawn rules, containment, saturation, and derivative revolts.

Create 20 separate fictional claimant army/muster identity scenes through the asset workflow, delivered through the fixed technical portrait slots with no individual focal human/person. Preserve matching regional male names, male-default leader metadata, and profile gates. Revolts transfer only recorded loyal Event 19 formations. One-state countries use takeover or failed-coup logic.

A future Chaos family must need one registry entry and no Event 19 list edit. Keep all Event 19-specific registry entries and callbacks in an existing Event 19 file or exactly one consolidated Event 19 registry code file; never create family-specific Event 19 registry files. Base zombies are the only trainable zombie variant. Ghosts and golems are spawn-only by default. Verify local identifiers. Keep Event 19 units and derivatives isolated from parent tags, counts, stages, super-events, evolutions, and world-end progression.

Implement complete zombie, ghost, and golem derivative packages through safe dynamic creation. A fixed-tag fallback requires approval. Give each distinct identity, flags, leaders or councils, idea lifecycles, actual revolting units, family reinforcement, decisions, AI, roughly 25 to 35 focus-scale route content or an adapted equivalent, expansion, and defeat cleanup. Use shared special and nonhuman classifiers. Ghost decline remains slow. Derivatives stay weaker than parent actors and have no world-end route.

Implement the phased category and selected-lot Muster Board. Show claimant and anomalous tabs only when relevant. GUI buttons use shared decision logic with equivalent AI paths. Wire assets, including three real frame-sheet UI animations with static fallbacks, and implement all eleven achievements.

Add The Unbidden Muster as approved `SCN-013`, with four types and four intensity stops. It bypasses normal event prerequisites, creates immediate revolts or takeovers and wars, handles microstates safely, clears setup bypasses, and never sets the terminal world-end flag.

Integrate Event Log history, evolution records, Event Details, shared tracking, civil-war safety, related military events, and parent systems without duplicate counts, deaths, wars, transfers, or progression. Keep Event 19 unclustered unless a complete multi-member cluster is approved.

Centralize tuning and run balance, performance, isolation, AI-validity, scenario, and exploit checks. Write final in-world localisation from the spec direction. Update documentation, helper and classifier docs, asset manifests, achievements, scenario docs, and the catalog workbook.

Use project subagents with `fork_context=false`. Run the mandatory improvement-loop planner near completion, resolve its addendum or closure handoff, then run specialist audits and the final completion auditor. Do not claim completion while any mapped mechanic, country, route, AI, asset, localisation, documentation, catalog field, or validation remains missing. Report every simplification, fallback, and blocker. Fallbacks require approval.
