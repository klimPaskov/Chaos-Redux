# Goal Prompt: Event 021 Random Civil War

Implement `docs/specs/021_random_civil_war_specs/` in full.

Read `AGENTS.md`, every Event 021 spec and prompt, Event 006 specs and implementation, relevant skills, the offline Paradox wiki, installed vanilla documentation, and current civil-war, cluster, scenario, AI, decision, and asset precedents. Use HOI4 MCP schemas. Spawn project subagents with `fork_context=false`.

Event 021 is Minor Repeatable, chaos level 1, with entry `chaosx.nr21.1`. Add it to Cluster 1, Wars, at Medium severity. Keep it unavailable until the rework is ready. When no valid target exists, show `N/A` and remove live weight.

Build a reusable framework with hidden Fracture Pressure, visible State Authority, target weighting, severity, connected regions, viable capitals, protected remnants, dynamic force and stockpile allocation, actor adapters, front registry, decisions, missions, active and prefire evolutions, neighboring exposure, bounded global scheduling, settlements, recurrence, caps, scenario setup, and cleanup. Centralize tuning. Never blindly split half the army or territory.

Baseline supports ideological uprisings, rival legal governments, regional secessions, command schisms, complete Event 006 independence actors, and same-tag contests for unsafe one-state or all-island countries. Stable targets receive limited crises. Weak, exhausted, occupied, divided, or poorly administered targets receive severe crises.

Use a normal decision category with one static picture, concise dynamic text, one State Authority value, three to five actions, and one to three missions. Do not create a custom GUI, animation, super-event, or 3D asset. Use equipment, manpower, experience, supply, factories, diplomacy, unit commitments, state control, and time. An action can spend at most four resource types.

Event 021 may initialize a human Event 006 package even if Independence Wave never fired. Reuse its carrier, identity, leaders, flags, tree, politics, ideas, forces, reinforcement, formables, decisions, AI, and assets. Record Event 021 origin. Do not mark Event 006 fired, change its weight or cap, advance its evolutions, duplicate a tag or character, create an incomplete or actual nonhuman package, or auto-enroll it in Event 006 league systems. Human Event 006 countries remain vulnerable. Use `is_actual_nonhuman_country` for immunity.

Evolution I adds viable multi-front wars, independence fronts, and reduced-weight major targeting. Evolution II adds Regional Exposure, neighbor actions, sponsors, stronger sides, and rare uncertain strange incidents. Separate civilian relief from armed support. Evolution III creates nonterminal Global Fracture through Stable, Exposed, Fractured, and Critical bands, due-country reviews, a Critical queue, tested theater caps, nested crises, successor grace, recurrence memory, and a generation cap. Do not add an unrestricted whole-world daily, weekly, or monthly loop.

Integrate Events 004, 007, and 021 in the Wars cluster with target reservation, collision rules, skip reasons, and one pacing event. Add The Fracture Cascade manual scenario with a verified free ID, four types, and four intensities. Maximum commits every eligible normal human country. Immediate setup is preferred. Locked deterministic setup over no more than seven game days is allowed only after measured one-frame performance failure.

Implement role-specific AI, Event Logs, Event Details, three evolution records, settlement, reconstruction, six achievements, static assets, documentation, and workbook alignment. Route weighted surfaces through the probability auditor before and after changes. Run the mapped MCP, acceptance, cleanup, edge-case, and performance checks.

Near completion, run the improvement-loop planner and resolve its output, then run the event completion auditor. Do not claim completion until every requirement is implemented and proven. Report every omission, simplification, blocker, placeholder, or fallback.
