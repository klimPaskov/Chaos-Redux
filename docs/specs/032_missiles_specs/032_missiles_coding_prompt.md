# Event 32 coding-agent prompt

## Goal

Rework Event 32, Missiles, into the complete global repeatable missile-program system defined in `docs/specs/032_missiles_specs/`.

Treat every accepted specification, prompt, matrix, acceptance item, and test case in that folder as part of the implementation contract. Do not replace mapped mechanics with a smaller legacy-compatible version.

## Required reading and evidence

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents` before editing.

Read the required offline Paradox wiki pages and the installed vanilla documentation for events, scopes, effects, triggers, modifiers, localisation, decisions, ideas, AI, technologies, raids, buildings, and on actions. Inspect current Chaos Redux and installed vanilla precedents.

Use the HOI4 MCP event tools to inspect and render the current `chaosx.nr32` chain before editing and compare it after implementation. Use `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` to prove the normalized technology adapter. Use the required probability workflow for every weighted surface. Record an exact blocker when a required route is unavailable.

## Preserve and replace

Keep Event ID `32`, namespace `chaosx.nr32`, and entry event `chaosx.nr32.1`.

Replace the current blanket grant of two technologies and two capital rocket-site levels with the specified bounded global firing transaction.

Preserve the existing Event 16 reaction by calling `brilliant_scientist_record_missile_crisis` from the appropriate first-recipient path. Do not duplicate Event 16 state.

Keep Event 23 nuclear ownership and Event 76 testing ownership separate. Event 32 provides missile progression and delivery adapters, not their entire content.

## Core event implementation

Register Event 32 as Minor Repeatable with Calm World minimum chaos and no cluster. Keep it disabled by default until the full rework is ready, then add it to the reworked-event default allowlist in the same completion change.

Freeze and process every valid recipient exactly once per firing. Count the firing once for pacing, repeatable weight, history, and first-news behavior. Do not add a recurring daily, weekly, or monthly whole-world scan.

Implement recipient profiles, one-step normalized technology progression, mature-program packages, country reports, first global news, one global Event 32 history row, Event Details, evolution previews, and actor handling.

Implement Operational Reserve, Launch Readiness, Command Control, derived guidance status, retaliation posture, and a readable program idea or dynamic modifier. Centralize tuning.

Implement launch-state selection, scoring, capacity, hardening, security, damage, repair, capture, reserve custody, civil-war split, release inheritance, annexation cleanup, and exact no-duplication accounting. Upgrade existing sites before creating new sites.

## Operations and shared consequences

Implement one normalized strike contract for precision, strategic, saturation, counterforce, command, logistics, industry, air and coastal, and broad strategic profiles.

Prove the installed native raid adapter and provide the accepted scripted adapter only where native support cannot satisfy parity. Do not silently substitute one route for the other.

Implement preparation, commitment, reach, capacity, reserve debit, guidance resolution, bounded drift, interception, strategic building damage, civilian and military deaths, evidence, attribution, diplomacy, incident records, recovery, and cleanup.

Special payloads require existing technology, policy, stockpile, and site custody. Consume the real payload and call shared chemical, biological, nuclear, thermonuclear, Air Cleanliness, Deaths, Condemnation, and Fallout consequence paths. Event 32 owns no terminal branch.

## Evolutions

Implement all five parallel tracks with enable gates, dynamic pacing, context, logs, country adoption, AI, interactions, and disabled-state safety:

- Saturation Arsenals
- Unreliable Guidance
- Special Warheads
- Rogue Launch Commands
- Automatic Retaliation

Use the tier mapping and unlock conditions in part 4. Automatic retaliation must use the bounded incident queue, causal-depth cap, participant cap, launch cap, duplicate-pair guard, and closure rules. Direct recursion is forbidden.

## Decisions, scenario, AI, and achievements

Implement the full decision and mission contract from `032_missiles_decision_mission_prompt.md`.

Implement `SCN-015` only after a fresh collision audit. Reuse the shared scenario window and make launch setup atomic and idempotent.

Implement every AI doctrine profile and weighted surface in part 6. Spawn `chaosx_ai_probability_auditor` with `fork_context=false` before weighted patches and again for the required compare pass.

Implement all eight achievements from `032_missiles_achievement_prompt.md`, including tracking, disqualifiers, localisation, icon triplets, docs, and tests.

## Assets and text

Produce and wire every authorized asset from `032_missiles_asset_prompt.md` through the correct bounded asset workers. Do not create portraits, flags, focus art, animation, custom 3D models, or super-event assets.

Write final player-facing localisation from the direction in part 7. Do not paste working labels, expose hidden variables, or use generic crisis prose. Run the localisation auditor after the broad text pass.

## Cross-system integration

Implement the bridges in `032_missiles_system_connections.md`, including Event 5 succession, Event 6 inheritance, Event 13 site damage, Event 16 reaction, Event 19 future custom-unit obligations only if a new custom combat unit is introduced, Event 23 payload custody, Event 76 test data, civil wars, coups, occupation, Air Cleanliness, Condemnation, Deaths, Event Logs, and Fallout consequence eligibility.

Do not absorb another event's political route, source event, evolution, history, or terminal state.

## Documentation and completion

Update the event doc, shared system docs, scenario docs, asset documentation, achievement documentation, probability evidence, and the authoritative event catalog workbook. Run the catalog exporter and never edit the three CSV exports directly.

Use the project subagents with `fork_context=false` according to the spec and skill contracts. Every patching subagent writes a handoff under `docs/plans/032_missiles_plans/subagent_handoffs/`.

Near completion, spawn `chaosx_improvement_loop_planner`. Resolve its addendum, fold accepted design into the specs, queue it with a reason, reject it with a reason, or accept a closure handoff. Then run the event completion auditor.

Do not invoke autonomous desktop testing unless the user explicitly requests it. Still complete all static source, MCP, probability, asset, documentation, and test-plan work available in the implementation environment.

Keep iterating until every acceptance criterion is satisfied. Report every simplification, fallback, blocked engine surface, skipped meaningful validation, missing asset, or unresolved plan. Do not claim completion while any accepted requirement remains missing.
