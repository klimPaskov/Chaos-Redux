# Event 42: Equipment from Heavens specification package

## Package identity

- Event ID: `42`
- Event slug: `equipment_from_heavens`
- Event name: Equipment from Heavens
- Intended extraction folder: `docs/specs/042_equipment_from_heavens_specs/`
- Package filename: `042_equipment_from_heavens_specs.zip`
- Event type: Minor Repeatable
- Event Chaos level: 1
- Cluster assignment: Various Anomalies
- Cluster member severity: Low

## Design summary

Equipment from Heavens selects one uniformly random eligible ordinary country and gives it an enormous mixed military stockpile that falls across several owned states. Recipient size, manpower, industry, ideology, war status, and strategic need never reduce the reward. The equipment mix remains deliberately unoptimized. A tiny country can receive more armor, aircraft, artillery, trains, or convoys than it can crew, fuel, supply, or deploy.

The event develops through three global evolutions. Evolution I widens the conventional equipment pool and raises the likely technology level. Evolution II permits the highest conventional equipment tiers and substantial nuclear stockpiles. Evolution III can add existing Chaos Redux equipment only after each exact token passes a repository-backed stockpile, fielding, AI, cleanup, and source-isolation audit.

The event uses a main recipient popup, several delayed landing-zone reports, Event Log integration, three evolution records, three achievement routes, static report-event artwork, and the ordinary stockpile and military systems. The design avoids a separate mechanic window and persistent custom meter because the player can understand and use the incident through the manifest summary, stockpile, division designer, air interface, logistics, lend lease, and nuclear systems.

## File index

### Source specifications

- `specs/042_equipment_from_heavens_spec_part_1_core.md`
- `specs/042_equipment_from_heavens_spec_part_2_delivery_manifest.md`
- `specs/042_equipment_from_heavens_spec_part_3_evolutions_and_integrations.md`
- `specs/042_equipment_from_heavens_spec_part_4_ai_presentation_and_acceptance.md`

### Implementation prompts

- `prompts/042_equipment_from_heavens_asset_prompt.md`
- `prompts/042_equipment_from_heavens_achievement_prompt.md`
- `prompts/042_equipment_from_heavens_coding_prompt.md`
- `prompts/042_equipment_from_heavens_goal_prompt.md`

### Research and audit inputs

- `research/042_equipment_from_heavens_source_reading_ledger.md`
- `research/042_equipment_from_heavens_repository_findings.md`
- `research/042_equipment_from_heavens_probability_scenarios.md`
- `research/042_equipment_from_heavens_special_equipment_audit_matrix.md`

### Quality and completion material

- `quality/042_equipment_from_heavens_acceptance_matrix.md`
- `quality/042_equipment_from_heavens_parent_improvement_review.md`
- `quality/042_equipment_from_heavens_process_blockers.md`

## Catalog reconciliation

The current exported event catalog row identifies Event 42 as a Chaos level 1 Minor Repeatable event with status To Be Reworked, but it has no cluster assignment. The current cluster export contains an unavailable, unnumbered Various Anomalies row at Chaos level 4 with no members. The accepted design places Event 42 in Various Anomalies as a Low member.

Implementation must reconcile the live cluster registry and the authoritative workbook before assigning any numeric cluster ID. The CSV files are export snapshots and must not be edited directly. Once implementation wording is final, update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and run `python .tools/export_event_catalog_csv.py`.

## Source status

Every supplied top-level Markdown file, TOML file, CSV row, and every subagent TOML inside `subagents(4).zip` was fully read before this package was written. Targeted current repository inspection was also completed through the connected GitHub repository for the existing special-equipment tokens and their owner contracts.

Literal project subagents could not be launched in this interface because the only exposed tool-registry request failed with an MCP 429 response and no spawn function became available. The package therefore includes a parent-performed provisional improvement review and preserves the real `chaosx_improvement_loop_planner` pass as a required implementation-stage closure gate. No supplied source file was skipped.

The local Windows repository, offline Paradox wiki snapshot, installed vanilla game files, and HOI4 MCP server were not mounted in this interface. Their required checks are therefore assigned to implementation and are not represented as completed evidence here.
