# Chaos Warfare Full Implementation Prompt

Implement the complete Chaos Warfare CBRN rework from this planning package in the Chaos Redux repository. Treat the spec pack as accepted design after user approval. Do not reduce it to a doctrine-stat pass.

Before editing, read `AGENTS.md`, every relevant repo skill, the current chemical and biological docs and implementation, the condemnation impact spec, the offline Paradox wiki pages required by AGENTS.md, and current Hearts of Iron IV 1.19 documentation and vanilla examples. Inspect exact Army Headquarters, regimental support, essential equipment, company-gated ability, `unit_modifiers`, raid, air mission, MIO, AI, unit, equipment, and scripted GUI patterns. If a planned engine surface is unsupported, stop that surface and report the blocker. Do not silently substitute an approximation.

Promote the accepted package into `docs/specs/chaos_warfare_system_specs/` or the approved system-spec path. Put working handoffs and audit reports in `docs/plans/chaos_warfare_system_plans/`. Record a source-of-truth map and disposition every old plan or conflicting doc.

Implement in the staged order from the handoff:

1. Verify engine syntax and current vanilla balance.
2. Create shared constants, readiness, policy, protection, exposure, evidence, attribution, operation records, and cleanup.
3. Add producible gas-mask equipment, decontamination equipment, CBRN instruments, technologies, military coverage, civilian distribution, filter consumption, and differentiated starting reserves.
4. Consolidate agent-specific support units into role-based regimental support. Rebuild Chaos Battalion as a coherent protected assault battalion. Add essential equipment and AI templates.
5. Add Army HQ support companies and company-gated order abilities with command-power scaling and current `unit_modifiers` behavior.
6. Rework the grand doctrine, four tracks, four milestones, doctrine-only technologies, officer corps, traits, icons, and AI.
7. Refactor cylinder, projector, artillery, armor, aircraft, raid, and tactic delivery through one chemical exposure helper. Explicit chemical air operations and raids must consume payload and contaminate exact target states only through the shared pipeline. Continuous mission contamination remains fail-closed until a verified current-version mission hook exists; no estimator, aircraft-presence proxy, or other fallback may be retained, and idle aircraft never count as use.
8. Refactor biological raids, operative operations, accidents, incubation, detection, spread, countermeasures, captured facilities, evidence, and doomsday release. Keep weaponized zombies separate except for shared helper call sites.
9. Wire one action record to Deaths, Air Cleanliness, Condemnation, chaos, and diplomatic consequences without double counting.
10. Implement nerve suppression as a targeted occupation operation with immediate suppression, delayed trauma, deaths, contamination, evidence, Condemnation, cooldown, and AI restraint. Remove doctrine-linked genocide terminology and keep camps separate.
11. Implement AI program posture, research, production, templates, headquarters, operation use, protection, containment, and sanctions response for the country profiles.
12. Implement UI, dynamic localisation, assets, achievements, docs, and relevant catalog alignment.

Use shared scripted effects and triggers. Centralize tuning in script constants. Do not add a broad all-country daily, weekly, or monthly pass without user permission. Use targeted operation, combat, state, and existing approved pulse hooks. Register every new equipment bonus type in `common/script_enums.txt`. Document every reusable dynamic helper with scope, inputs, outputs, defaults, side effects, and example.

Keep final player-facing text in-world. Do not paste working labels from the plan as final localisation. Do not use placeholders. Every visible asset needs final source, PNG, DDS, manifest, and GFX wiring. Animated assets require real source frames, frame sheet, preview, static fallback, and verified GUI precedent.

Use patch-capable subagents for bounded focus, decision, country, localisation, and scripted helper work when available. Every patch needs a handoff. Use the improvement-loop planner near completion and resolve its addendum or closure. Run decision, country, localisation, focus if touched, and final completion audits.

Balance against current 1.19 regimental support and doctrine values. Strong effects must depend on equipment, preparation, counterplay, and aftermath rather than permanent stat bloat. Run every validation scenario in the balance spec at weak, normal, and high-chaos conditions. Record casualties, contamination, cleanup, stock use, command cost, AI action, evidence, Condemnation, and sanctions.

Do not claim completion with missing AI, assets, localisation, docs, migration, unsupported air behavior, placeholder content, or unresolved accepted plans. Report every simplification, omission, fallback, blocker, and unverified engine assumption.
