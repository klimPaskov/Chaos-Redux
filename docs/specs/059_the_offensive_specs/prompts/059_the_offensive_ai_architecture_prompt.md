# Event 059 AI architecture subagent prompt

Spawn `chaosx_scripted_system_architect` with `fork_context=false` after the parent has read the full Event 059 spec pack and inspected the actual repository.

## Task

Design the smallest complete runtime architecture for a permanent global AI-only strategic posture with three independently gated evolution layers.

The architecture must satisfy these non-negotiable behaviors:

- Event 059 is Minor Fire-Once and creates one global active state
- human-controlled countries never use Event 059 AI behavior
- player takeover suspends the behavior without a direct modifier or penalty
- AI handback restores every active layer after reassessment
- countries created or released later receive current layers when AI-controlled
- no new unbounded daily, weekly, or monthly whole-world scan
- no direct combat, production-output, research, organisation, planning, supply, or equipment-stat bonus
- country and event owner strategies remain authoritative when they conflict
- Evolution I controls persistence and follow-up
- Evolution II controls legal opportunity wars and intervention
- Evolution III controls scale and accepted risk
- a disabled evolution cannot be recreated by a higher layer

## Required repository inspection

Map:

- the existing Event 059 implementation and save-facing identifiers
- generic AI strategy plan precedents
- country-local AI strategy registration precedents
- native enable and abort conditions for AI plans
- country creation, release, civil-war, annexation, restoration, player-control, and AI-control hooks already present
- special Chaos actor classifiers and owner strategy precedence
- Event Logs and evolution state helpers
- existing tuning constant locations
- any current global iteration that could be reused without adding duplicate work

Inspect installed vanilla AI strategy documentation and examples before naming exact strategy types or fields.

## Architecture questions

Decide and document:

1. Whether a generic declarative AI plan can cover every country through a global flag and current `is_ai` state.
2. Whether the engine reevaluates the plan correctly after player takeover and AI handback.
3. How newly created and restored countries receive coverage.
4. Which state belongs globally and which state must be country-local.
5. How owner-specific plans block, dominate, or combine with Event 059.
6. How each evolution remains independent.
7. How legacy Event 059 fired state migrates without duplicate activation.
8. Which factors can be read directly at AI evaluation time instead of stored.
9. Which constants need one event-owned tuning surface.
10. Which repeated helper, if any, is truly generic enough for shared ownership.

## Preferred architecture

Prefer native declarative AI evaluation. If the engine requires country-local registration, use one-time activation plus bounded country creation and release hooks. A dormant AI strategy state may exist on a human-controlled country only when it has no observable gameplay effect and becomes relevant solely after AI control resumes.

Do not propose a scan-based architecture as the default.

## Deliverable

Write a plan under `docs/plans/059_the_offensive_plans/` containing:

- current architecture map
- proposed state model
- plan and strategy ownership
- control-transition flow
- new-country flow
- evolution-layer flow
- special-actor precedence
- migration flow
- constants and tuning ownership
- call-site map
- cleanup and invalidation behavior
- performance assessment
- exact open engine questions
- parent handoff

Do not implement broad event design changes. Small direct patches are allowed only when the parent explicitly authorizes them.
