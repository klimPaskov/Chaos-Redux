# Event 54 Completion Audit Prompt

Use `chaosx_event_completion_auditor` as a read-only final reviewer for Event 54, Gift from Scientists.

Read every file in `docs/specs/054_gift_from_scientists_specs/`, all Event 54 gameplay and localization files, the technology registry and every registered owner integration, the Scientific Research cluster implementation, event logs, Event Details, evolution records, achievements, asset manifests and runtime files, event documentation, catalog workbook, and generated CSVs.

## Compare against the specification

Audit:

- event identity, type, Chaos level, registration, enable state, and repeat behavior
- one bounded world transaction and independent per-country draws
- one, three, five, and ten grant targets with pool exhaustion
- active-graph inventory, DLC handling, ahead-of-time eligibility, and technology localization
- doctrine exclusion and Event 27 ownership
- mutually exclusive branch safety and final revalidation
- all five safety profiles
- owner registration, callback limits, dependency packages, lifecycle preservation, and provider migration
- consolidated human reports and AI popup suppression
- normal history, evolution history, Event Details, actor handling, and cluster history
- guarded Chaos milestones and repeat protection
- multiplayer, save-reload, country invalidation, and transaction idempotence
- Scientific Research membership, severities, mixed event types, many-to-many Event 27 membership, and one pacing commitment
- report-event image wiring and final asset evidence
- both achievements, all disqualifiers, provider gates, localization, icon triplets, and persistence
- permanent event documentation and workbook alignment

## Required evidence

Review final `hoi4.event_inspect`, render, and compare evidence. Review `hoi4.tech_inspect`, render, and compare evidence for every affected graph. Review probability scenario results and the last `hoi4.probability_compare` for changed weighted surfaces. Verify final asset consumers and checksums.

Source-only review cannot clear a missing MCP result. A planned asset cannot clear a missing DDS or runtime consumer. A CSV edit cannot clear a missing workbook update.

## Report format

List:

- verified complete requirements
- missing or contradictory requirements
- silent simplifications and fallbacks
- stale specs, docs, localization, manifests, or workbook fields
- missing task-specific evidence
- exact blockers to completion
- files and identifiers involved

Do not patch source. Do not infer a passing result from intent. Mark the event incomplete when any accepted mechanic, owner contract, cluster behavior, report, asset, achievement, documentation field, or required evidence remains missing.
