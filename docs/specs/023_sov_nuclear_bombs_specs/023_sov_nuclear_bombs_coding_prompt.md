# Event 023 complete implementation prompt

Implement the complete Chaos Redux Event 23 rework from `docs/specs/023_sov_nuclear_bombs_specs/`.

## Core result

Event 23 remains a Minor Fire-Once event for `SOV`, planned at Chaos level 2.

At baseline, add exactly 100 atomic bombs to the existing Soviet stockpile. Do not overwrite existing stockpile.

Create a decision-driven Soviet nuclear system with:

- Four custody doctrines.
- Arsenal Readiness from 0 to 100.
- Command Integrity from 0 to 100.
- Hidden, demonstrated, coercive, retaliatory, unrestrained, broken-chain, and moratorium postures.
- Storage, reactor, assembly, delivery, command, safety, and dismantlement play.
- Exact-state test preparation and outcomes.
- Public knowledge and credibility memory.
- Selected-target demands, target responses, exact strike preparation, final authorization, hold, redirect, and abort.
- Limited wartime use.
- Evolution II coercion against valid minors and Soviet breakaways.
- Evolution III multi-major retaliation and exchange.
- Evolution IV rare AI major first use at 1000 or more Chaos under severe strategic-loss gates.
- Event 5 custody integration.
- One nonterminal first multi-major exchange super-event.
- Seven achievements.

## Non-negotiable boundaries

- Event 23 does not absorb Event 5, Event 32, Event 76, Event 47, shared Fallout, or shared nuclear consequences.
- No new Soviet focus tree.
- No full scripted GUI.
- No triggerable scenario.
- No portraits, flags, tags, custom units, 3D models, counters, or animation.
- No free bombers, missiles, or thermonuclear capability.
- Every detonation routes through the verified shared nuclear consequence system.
- Event 23 never duplicates deaths, population loss, damage, contamination, Air Cleanliness, condemnation, direct nuclear-use Chaos, or Fallout progression.
- A breakaway holding devices does not gain instant operational control.
- AI major first use is impossible below Evolution IV.
- High Chaos alone never authorizes AI first use.
- Invalid exact targets fail closed and never redirect randomly.
- No simplification or fallback without explicit user approval and disclosure.

## Required preflight

Read all project rules, skills, this full specification, current Event 23 source, Event 5, shared nuclear systems, event logs, world threat, Fallout, super-events, achievements, current Soviet content, authoritative workbook, offline wiki, vanilla documentation, and vanilla precedents.

Use the installed HOI4 MCP for event, probability, technology, focus, GUI, and map surfaces that are actually touched. Record exact blockers when a required route is unavailable.

Spawn all project subagents with `fork_context=false`.

Start with `chaosx_repo_explorer` because the feature spans many systems and the exact live APIs are unknown.

Use `chaosx_scripted_system_architect` for shared nuclear action adapter verification or creation, custody ledger, event targets, script constants, dynamic helpers, and Event 5 bridge.

## Event and evolution grants

Use this reconciled cumulative ladder:

- Baseline: 100 bombs, 0 free reactors.
- Evolution I: 175 bombs, 2 reactors.
- Evolution II: 275 bombs, 4 reactors.
- Evolution III: 400 bombs, 6 reactors.
- Evolution IV: 600 bombs, 8 reactors.

If the event fires at a later stage, grant the cumulative package.

If it fired at baseline, grant increments of 75, 100, 125, and 200 bombs with two additional reactors at each evolution.

Record each reached evolution once and in order.

## Technology and delivery

Grant the minimum verified current-vanilla atomic capability required by the premise. Preserve existing Soviet progress. Do not grant missiles or thermonuclear weapons.

Support at least one verified current-vanilla delivery route. Use current DLC and non-DLC routes only after direct documentation and vanilla inspection.

Any technology or project change requires `hoi4.tech_inspect`, render, and compare.

## Decisions and AI

Implement the full decision map with phase visibility and selected-target or selected-site management.

Use no more than six primary visible actions and no more than three active missions per phase.

Use no more than four spendable cost types per action.

Run the probability audit before changing complex weights. Apply accepted balance changes, then run the same named scenarios through probability compare.

Use event-driven and bounded updates. Do not add a new all-country daily, weekly, or monthly loop without user approval.

## Assets and super-event

Lock runtime names before production.

Route generated pictures to `chaosx_generated_event_art` and icons or achievement art to `chaosx_icon_artist`.

Use separate `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher` passes.

The exchange super-event needs a verified real quote, unique licensed musical track, generated period image, settings-aware sound, final WAV, slot, localisation, docs, and audio catalog row.

It must not set `world_end`.

## Audits

After implementation:

- Run `chaosx_decision_mission_auditor`.
- Run baseline and comparison passes with `chaosx_ai_probability_auditor`.
- Run `chaosx_localisation_auditor`.
- Run focus audit only if narrow Soviet focus hooks were added.
- Run country-package audit for any operational breakaway nuclear actor integration.
- Run `chaosx_spreadsheet_doc_worker` after final in-game wording exists.
- Use `chaosx_documentation_curator` if plans and handoffs need reconciliation.
- Spawn `chaosx_improvement_loop_planner` near completion. Implement, promote, queue with a reason, or reject its addendum. Resolve a closure handoff before claiming completion.
- Run `chaosx_event_completion_auditor` before completion.

## Completion

Update event registration, default enable state, history, Event Details, all evolution views, actor mapping, world-threat source, shared API docs, Event 5 docs, super-event docs, achievements, event docs, authoritative workbook, and CSV exports.

Execute the acceptance scenarios in Part 10 through source, MCP, and project validation routes available to the coding environment. Live in-game testing belongs to the explicit debug-playtest workflow only when separately invoked by the user.

Create a focused Git commit only after the complete accepted implementation is ready.

The final report must list files changed, systems implemented, subagents and skills used, meaningful probability and integration findings, assets and audio, docs and workbook updates, and every remaining blocker or simplification.
