# Goal: Implement the Air Cleanliness and Fallout Living World

Implement `docs/specs/air_cleanliness_fallout_specs/`. Read `AGENTS.md`, relevant skills, accepted plans, engine references, and repo precedents. Record proof for engine-sensitive surfaces.

Define Fallout events in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. Do not reuse zombie ids, files, assets, audio, sprites, or paths. Remove stale ownership and use one idempotent request coordinator. Fallout is not a super-event. Use a full-screen blackout GUI with sequential text, input blocking, save recovery, and host authority.

Implement Air Winter first. Use state phases 0 through 6 with exposure, recovery, adaptation, food, shelter, and reclamation values. Winter must affect population through the Deaths system, buildings, supply, state categories, military operations, disease, and events. Add a winter mapmode and make the normal map visibly colder. Use regional snow, frost, cold rain, ash, dead vegetation, frozen water, dim light, and thaw. Universal snow and a mapmode-only result fail. Prove the normal-map route before final assets.

Fallout can be requested at 100 percent Air Contamination, by terminal events, or through the manual scenario. It does not require Chaos above 1000. Allocate the manual scenario as the highest live scenario id plus one, without renumbering existing entries. It must thermonuclear-strike every valid province, finish the batch, wait exactly seven days, then run the standard blackout and rewrite. One strike per state, province modifiers, or variable-only fallout do not count. Report a blocker if the exact engine-native sweep cannot be proven.

Build deterministic state grading, wasteland conversion, population and building loss, supply collapse, government change, successor allocation, player continuation, tag conflicts, and migration. Preserve the player country before general assignment. Use existing or dynamic tags only after a live conflict ledger. The 99-successor matrix is a candidate pool.

Build a Fallout-owned scheduler using phase, region, government, memory, winter, crises, characters, bilateral partners, fatigue, cooldown, arc caps, delayed results, hidden AI resolution, determinism, and cleanup. The release floor is 660 manually reviewed event blocks. Expansion toward 910 begins only after the floor passes review. A human campaign should normally show 90 to 180 meaningful events over ten years.

Cover global survival, nine regions, twelve archetypes, selected successors, characters, diplomacy, war, cause memory, fictional altered societies, recovery, generation change, and Year 10 order. Every selected successor needs opening, domestic, external, and late identity chains. Every major chain needs conflict, choice, delayed results, varied outcomes, memory, AI, and cleanup. Do not bulk-generate content.

Every surviving playable country receives non-generic Fallout focus content through archetype, regional, and country-memory layers with manual customization. Connect focuses, decisions, leaders, units, diplomacy, AI, and event memory. Use varied costs and meaningful effects. Avoid political-power stores, harmless failures, tiny modifiers, reward loops, stale decisions, and invalid targets.

Working labels are not final localisation. Write concrete regional and government-aware text. Never use em dashes or semicolons. Avoid staccato prose, generic apocalypse wording, staged contrast formulas, process language, and unsourced references. Mutant countries are fictional high-chaos content, not ordinary radiation science.

Use dedicated Fallout assets and manifests. Source real people, flags, and attested symbols. Generate fictional content through the approved workflow. Implement in reviewed batches, audit each tranche, and review depth after the pilot. Do not claim completion with placeholders, missing AI, stale docs, unwired assets, unresolved plans, hidden blockers, or unreported simplifications.
