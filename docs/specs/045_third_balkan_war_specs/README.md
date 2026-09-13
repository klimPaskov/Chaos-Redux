# Event 045: Third Balkan War specification pack

This package is the accepted planning handoff for Chaos Redux Event 045, **Third Balkan War**.

Extract the top-level folder to:

```text
docs/specs/045_third_balkan_war_specs/
```

The package defines the complete event design, the dynamic opening war builder, the single public escalation mechanic, regional claims, foreign intervention, settlements, three true evolutions, AI strategy, achievements, assets, super-events, testing scenarios, and implementation acceptance criteria.

## Package map

| Folder | Purpose |
| --- | --- |
| `specs/` | Accepted source design split by gameplay surface |
| `diagrams/` | Lifecycle, decision, claim, and escalation maps |
| `research/` | Historical design research, bibliography, and source manifest |
| `prompts/` | Bounded implementation handoffs for assets, super-events, achievements, decisions, coding, and the final goal |
| `quality/` | Probability scenarios, acceptance criteria, design review, closure handoff, and tooling blocker report |
| `handoffs/` | Cross-system implementation map and documentation alignment requirements |

## Core non-negotiables

- Event ID `45` remains a Minor Fire-Once event with Chaos level `1`.
- The entry event remains `chaosx.nr45.1`.
- The opening always creates a multi-country regional war when the event is valid.
- The event exposes exactly one persistent custom value, **Balkan War Escalation**.
- Baseline escalation stages remain separate from Evolutions.
- Evolutions alter the structure of the war and do not act as ordinary escalation stages.
- Generic wars, deaths, annexations, puppeting, faction changes, and peace continue through shared Chaos Redux systems without duplicate Event 045 Chaos awards.
- **Another World War** is a handoff to normal war and faction systems, not a terminal world-end scenario.
- The event belongs to the Wars cluster with High member severity.
- The implementation must remain dynamic across changed borders, successor states, player countries, and alternate-history faction maps.

## Source status

Every supplied project source file and every archived subagent definition was read in full before this package was written. The stored specialist contracts were applied during the design review. Actual specialist invocation through the outer Codex tunnel was attempted and failed with transport errors. The exact blocker is recorded in `quality/045_third_balkan_war_subagent_blocker.md`.
