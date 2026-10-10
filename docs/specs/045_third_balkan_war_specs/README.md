# Event 045: Third Balkan War specification pack

This package is the source planning handoff for Chaos Redux Event 045, **Third Balkan War**.

The package defines the complete event design, the dynamic opening war builder, the single public escalation mechanic, regional claims, foreign intervention, settlements, three true evolutions, AI strategy, achievements, assets, super-events, testing scenarios, and implementation acceptance criteria.

## Package map

| Folder | Purpose |
| --- | --- |
| `specs/` | Proposed source design split by gameplay surface |
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

Package-generation source, review, validation, and tooling reports are historical evidence.
Their PASS labels and transport errors do not establish current package validation, implementation, service health, or design approval.
The package does not retain an attributable original user or parent acceptance record for all expanded requirements, so unsupported acceptance claims remain unresolved.
The six parts under `specs/` and their linked supporting documents are the maintained reading set; the redundant combined copy was removed after proving all 26 included bodies matched their siblings.

The original planning session read every supplied source and applied the stored specialist contracts manually; its failed specialist invocation is recorded in `quality/045_third_balkan_war_subagent_blocker.md` as historical evidence only.
The runtime slot `events/045_third_balkan_war.txt` still holds the legacy stub; no part of this package is implemented.

## Open questions

- Whether the decision consolidation in Part 3 (one shared Register a Claim, one support transaction with request and commit entry points, mediation as an event, one transit policy action) should also collapse Coordinate an Arms Suspension and Apply Coordinated Sanctions; they stay separate because one lowers and one raises escalation.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:
- Part 4 and the coding prompt now record that Event 045 is already a High member of the Wars cluster (ID 1) in the workbook and live registry; the old "member list becomes 4, 7, 45" note was stale.
- Replaced `AGENTS.md` with `CLAUDE.md` and the `.agents` asset path with `.claude`, reduced the goal prompt to a pointer at the coding prompt it duplicated, and removed the obsolete extraction instructions.
- Marked the Codex-tunnel blocker as historical and recorded that the runtime slot is still the legacy stub.

Pass 2, design improvement:
- Consolidated the decision menu from 24 actions to 19: one shared Register a Claim for belligerents and neutrals, one support transaction (Request Foreign Support and Commit Support, each covering arms and personnel), outside mediation as an event response, and one Set Transit Policy covering transit and neutral corridors.
- The header shows the stage, the latest cause, and the missing proof for the next stage; the raw number is no longer a headline value.
- Settled the two "candidate" Chaos rows: Event 045 owns no Chaos source, since violations and settlements already move the shared war and Deaths sources.
- Made the famine and migration link concrete through the existing capture adapter, local war evidence, and port blockade proof, so the corridor and capital-rail missions carry humanitarian stakes.
