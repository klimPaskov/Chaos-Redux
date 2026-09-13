# Event 059 implementation prompt

Implement the complete rework of Event 059, The Offensive, from the source-of-truth package under `docs/specs/059_the_offensive_specs/`.

Read every specification part, matrix, prompt, quality record, and the implementation handoff before editing. Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `chaos-redux-improvement-loop`. Read the installed vanilla documentation and offline Paradox wiki pages required for events, AI strategy plans, AI strategy types, triggers, effects, scopes, on-actions, localisation, achievements, graphical assets, and the exact consumers touched by the implementation.

## Core result

Event 059 remains a Minor Fire-Once event at Chaos level 1. Its stable entry identity is `chaosx.nr59.1` unless repository inspection proves that a migration wrapper is required. The event creates one permanent global offensive-AI state. It changes AI choices and priorities. It grants no direct combat, production-output, research, organisation, planning, supply, or equipment-stat bonus.

Human-controlled countries must never use Event 059 AI behavior. Player takeover, co-op control, hotjoin, and tag control changes must suspend the AI layer for that country. Returning the country to AI must restore every active layer after a fresh assessment. Countries created, released, restored, or split after activation must receive current layers when AI-controlled.

Do not implement a new unbounded daily, weekly, or monthly whole-world scan. Prefer declarative AI strategy plans gated by the global state and current AI control. If verified engine behavior requires country-local strategy registration, apply it once and use bounded existing creation or release hooks. Dormant internal AI strategy state on a human country is acceptable only when it produces no player-facing effect.

## Required specialist routing

- Spawn `chaosx_repo_explorer` with `fork_context=false` before editing if locations or existing AI architecture are uncertain.
- Spawn `chaosx_scripted_system_architect` with `fork_context=false` using `prompts/059_the_offensive_ai_architecture_prompt.md` before creating new AI plumbing.
- Spawn `chaosx_ai_probability_auditor` with `fork_context=false` using `prompts/059_the_offensive_probability_audit_prompt.md` for every weighted AI surface and any weighted Diplomacy cluster member metadata.
- Route the report image through `chaos-redux-event-assets` and `chaosx_generated_event_art`.
- Route the achievement icon through `chaos-redux-event-assets` and `chaosx_icon_artist`.
- Spawn `chaosx_localisation_auditor` after broad visible text is written.
- Spawn `chaosx_event_completion_auditor` before claiming completion.
- Spawn `chaosx_spreadsheet_doc_worker` after implementation when the authoritative workbook, generated CSV exports, event docs, and route records need alignment.
- Spawn `chaosx_improvement_loop_planner` near completion. Resolve its addendum, queue each item with a reason, reject it with a reason, or obtain a closure handoff before final completion.

## AI behavior

Implement four independent layers exactly as mapped:

1. Baseline Offensive Posture improves activity, concentration, exploitation, offensive production support, air allocation, viable naval invasion, use of existing war goals, and useful war participation.
2. Relentless Offensives at 200+ Chaos increases operational persistence, follow-up, reserve commitment, reinforcement, resupply, and recovery behavior.
3. Predatory Powers at 400+ Chaos increases valid opportunity-war, claim, war-goal, intervention, and call-to-arms behavior.
4. Total Offensive at 600+ Chaos increases operation scale, theater count, invasion ambition, and accepted strategic risk.

A higher layer must not reproduce a disabled lower layer. Owner-specific country and event strategies remain authoritative when they conflict with the generic posture.

Implement the full safety envelope. Supply, replacement, manpower, fuel, transport, reserve, homeland, existing-war, legal-path, subject, and special-actor limits must remain meaningful. Weak minors must not chase impossible armour, air, or naval programs. Naval invasions require transport, convoys, route control, a useful target, a supply plan, and enough home defense.

Do not claim direct encirclement control unless the verified engine surface supports it. Use front, concentration, target, reserve, and exploitation behavior to pursue the intended outcome.

## Evolution pacing

Support active-event evolution and pre-fire evolved openings.

- Evolution I target pacing is about 90 days at 200 Chaos, 75 days at 300, and 60 days at 400 or above.
- Evolution II target pacing is about 105 days at 400 Chaos, 85 days at 500, and 70 days at 600 or above.
- Evolution III target pacing is about 120 days at 600 Chaos, 95 days at 800, and 75 days at 1000 or above.

Use dynamic factors and existing bounded world-state data. Do not add a scan only to calculate pacing.

When the event first fires after evolution thresholds, activate every enabled eligible layer in stage order, show one combined report, and record each evolution separately. Disabled evolutions must not set recorded flags or unlock behavior. Re-enabling an unactivated evolution begins its normal MTTH path. Do not roll back an already activated historical evolution through a settings toggle.

Evolution activation adds zero Chaos.

## Chaos

Implement the complete Chaos impact map. The first global manifestation adds one bounded 15 to 25 Chaos gain, scaled by living ordinary AI countries and AI major powers, then permanently guarded. Wars, casualties, annexations, faction changes, and tension use shared systems with no Event 059 duplicate. Cluster entry, control changes, save reload, new countries, and evolution activation must not repeat the gain.

## Cluster

Assign Event 059 to the Diplomacy cluster with High member severity. Treat Diplomatic Panic as the superseded name of the same cluster, not a second alias. Inspect the authoritative aligned member arrays and use current project defaults for required or optional role, participation chance when relevant, and minimum tier. Audit any weighted value against the complete cluster pool. Preserve one cluster pacing event, Event 059's own history, Fire-Once removal, and one-time Chaos effect.

## Reports and logs

Send one activation report to every human player without creating duplicate Event History rows. Active-event evolutions send one report each. A pre-fire evolved opening sends one combined report. Use a global or neutral actor presentation.

Wire the full Events, History, Evolutions, Event Details, and Clusters contract. Add Event 059 to the reworked default-enabled allowlist only when the implementation is ready for testing. Write final localisation from the direction in Part 5. Do not copy working labels as final text. Do not expose raw AI weights or claim direct combat bonuses.

## Assets and achievement

Follow `prompts/059_the_offensive_asset_prompt.md` and `prompts/059_the_offensive_achievement_prompt.md`. Produce the final report image, achievement icon states, manifests, handoffs, DDS files, sprite registration, and live consumer evidence. Do not use placeholders.

Implement the achievement with guarded qualification, 180-day survival, stronger attacking AI major, no major ally, independence, capital and core control, target defeat, save persistence, and exploit protection.

## Inspection and validation

Use `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` for the event chain. Use the probability workflow in the AI scenario matrix. Verify exact AI strategy names and fields against the installed game and documentation. Do not invent unsupported keys.

Run repository validation, targeted script checks, asset checks, localisation checks, event-log checks, save migration checks, and all named acceptance scenarios. Perform live tests for control transition, new-country coverage, severe supply failure, viable and inviable invasions, valid and invalid Evolution II targets, Total Offensive risk, pre-fire catch-up, cluster firing, save reload, and achievement unlock and disqualifiers.

Update the authoritative event catalog workbook, then regenerate all CSV snapshots with the repository export tool. Do not edit export CSV files directly.

Report every changed file, identifier, subagent handoff, validation result, live gap, queued item, rejected item, and blocker. Keep iterating until every mapped requirement is implemented and verified. Do not claim completion while a required AI behavior, evolution, log surface, asset, achievement, workbook row, or acceptance scenario remains unresolved.
