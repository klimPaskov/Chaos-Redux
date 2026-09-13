# Event 064 Improvement Loop Tooling Blocker

## Status

Blocked by unavailable subagent execution tooling in the planning environment.

## Required subagent

`chaosx_improvement_loop_planner`

Required invocation mode:

`fork_context=false`

## What was available

The complete `chaosx_improvement_loop_planner.toml` definition was supplied inside `subagents(4).zip`, extracted, and read in full.

The available tool registry exposed repository connectors and two Codex-native inspection functions. It did not expose a subagent spawn, run, task, or dispatch function. No valid tool call could execute the planner as an independent agent.

## What was completed

The parent agent applied the full planner contract as a review lens and recorded the result in:

`docs/specs/064_border_fortifications_specs/research/improvement_loop_review.md`

Accepted review changes were merged into the source specification. They include:

- one-level gradual baseline waves and caps below level ten
- strategic anchors, lower ordinary sectors, and bounded depth
- integrated Fortress State support packages
- internal redoubts for Fortress World and island-country coverage
- defense, logistics, and breach response postures
- real offensive counterplay
- material decision costs and one active project cap
- multi-cluster arbitration and duplicate prevention
- footprint-based Chaos sources and shared-source audit
- bounded achievement tracking
- restrained asset scope
- single-transaction performance rules

## Why the blocker remains

A parent-led self-review is not independent. The planning skill requires a spawned loop planner near completion for event design. The task therefore cannot record an independent closure handoff from this environment.

The current planning package remains usable and complete as a source handoff. Formal implementation completion remains blocked until the independent pass runs against the implemented files and current evidence.

## Required implementation-stage prompt

Spawn `chaosx_improvement_loop_planner` with `fork_context=false` and pass the following self-contained task:

```text
Event ID: 064
Event slug: border_fortifications
Current goal: Review the near-complete implementation of Chaos Redux Event 064 Border Fortifications for remaining shallow design, missing gameplay consequences, disconnected mechanics, AI gaps, asset-state gaps, aftermath gaps, performance risk, or scope bloat.

Accepted identity: Minor Repeatable, Chaos Level 1, primary Sudden Abundance cluster Medium, additional Military Preparation cluster Medium. Accepted evolutions are Defense in Depth at 200+, Fortress States at 400+, and Fortress World at 600+.

Source specification folder:
docs/specs/064_border_fortifications_specs/

Relevant plans folder:
docs/plans/064_border_fortifications_plans/

Inspect the implemented event root, global transaction, frontier definition, caps, evolution targeting, response postures, decisions, AI, probability evidence, Chaos impact map, both cluster memberships, multi-cluster arbitration, event log, Event Details, achievements, localisation, assets, catalog exports, performance evidence, and completion evidence.

User constraints: Keep the event global and repeatable. Every valid current foreign land-frontier province receives land forts. Preserve the three accepted evolutions and both accepted cluster memberships. Keep the review bounded to the accepted event transaction, response category, clusters, achievements, assets, documentation, and validation surfaces.

Known risk areas: worldwide fortification can cause stalemate, supply hubs can become free economy, multi-cluster membership can double fire or shadow one cluster, island countries can receive no local baseline result, fort target checks can become recurring world scans, and achievement shortcuts can use state transfer or third parties.

Return either an expansion addendum with concrete accepted-scope changes or a closure handoff. Mark every optional idea separately. Do not rely on inherited conversation context.
```

## Resolution rule

- If the planner returns an expansion addendum, resolve every accepted item in the source spec and implementation, or reject it with a recorded reason.
- If the planner returns a closure handoff, save it under `docs/plans/064_border_fortifications_plans/subagent_handoffs/`.
- Rerun completion checks after any accepted change.
- Do not claim Event 064 complete while the addendum or closure handoff is unresolved.
