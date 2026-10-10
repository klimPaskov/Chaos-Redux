# Event 42: Equipment from Heavens specification package

## Package identity

- Event ID: `42`
- Event slug: `equipment_from_heavens`
- Event name: Equipment from Heavens
- Event type: Minor Repeatable
- Event Chaos level: 1
- Clusters: Various Anomalies (11), Sudden Abundance (15), Military Preparation (18), Low member in each
- Catalog status: Needs Testing

## Design authority

Recorded accepted amendments are in [the 5–6 October owner decisions](../../plans/042_equipment_from_heavens_plans/agent_decisions_2026-10-05.md).
The 5 October presentation decision cites parent G6 authority; the 6 October Borrowed Nightmare follow-up cites the director’s explicit approval.
Those amendments supersede original popup allocation and combat-loss criteria; current source corroboration and validation limits are recorded in the [audit handoff](../../plans/repo_cleanup/specification_package_audit_2026-10-07/handoffs/037_042.md).
The catalog wording queued in the [catalog owner handoff](../../plans/042_equipment_from_heavens_plans/catalog_changes_pending.md) is now in the workbook: details, three evolution texts, clusters 11, 15, and 18, and status Needs Testing.


The imported package preserves its premise, proposed expansions and source-reading provenance.
Claim-specific acceptance remains `unresolved` when an explicit user decision or parent acceptance within existing authorization is not cited.
Use the [repository acceptance rules](../../../CLAUDE.md#specs-and-plans) and current [event workflow](../../../.claude/skills/chaos-redux-events/SKILL.md) rather than treating the imported accepted labels as approval.

## Design summary

Equipment from Heavens selects one uniformly random eligible ordinary country and gives it an enormous mixed military stockpile that falls across several owned states. Recipient size, manpower, industry, ideology, war status, and strategic need never reduce the reward. The equipment mix remains deliberately unoptimized. A tiny country can receive more armor, aircraft, artillery, trains, or convoys than it can crew, fuel, supply, or deploy.

The event develops through three global evolutions. Evolution I widens the conventional equipment pool and raises the likely technology level. Evolution II permits the highest conventional equipment tiers and substantial nuclear stockpiles. Evolution III can add existing Chaos Redux equipment only after each exact token passes a repository-backed stockpile, fielding, AI, cleanup, and source-isolation audit.

The accepted presentation uses discovery followed by one final recovery summary or halt report, with three-to-seven hidden recovery visits.
It preserves Event Log integration, three evolution records, three achievement routes, six report-art roles, and ordinary stockpile and military systems. The design avoids a separate mechanic window and persistent custom meter because the player can understand and use the incident through the manifest summary, stockpile, division designer, air interface, logistics, lend lease, and nuclear systems.

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

## Implementation status

Implemented (5 to 6 October 2026, `events/042_equipment_from_heavens.txt` and the `042_equipment_from_heavens_*` files under `common/`, `interface/`, and `localisation/`): uniform recipient draw, one persisted manifest and stockpile transaction, magnitude and family tables, the three ordered evolutions, nuclear caches, the seven-family special allowlist, landing burdens, the two-popup presentation with hidden visits, guarded Chaos milestones, AI assessment, Event Log and Event Details, six report cards, and the three achievements including the approved Borrowed Nightmare victory rule.

Open: live acceptance of the recovery chain, nuclear launch from a received cache, and Event Details at 1920x1080; the MCP probability comparison; and the plans folder's release review items.
The source review evidence is in `docs/plans/042_equipment_from_heavens_plans/release_review_2026-10-05.md`.

## Historical source status

The original package was written in a planning interface without the local repository, wiki, game files, or MCP; its source-reading ledger and process-blocker notes under `research/` and `quality/` are historical evidence of that session only.

## Open questions

- Discovery currently offers acknowledgment only, and the recipient's real choices happen afterwards through ordinary systems (Part 1).
  A proposal for the user: when a nuclear cache arrives, let the recipient choose between declaring it (the world learns of a new nuclear power, which can drive guarantees and tension) and keeping it secret (no announcement, but a later use is treated as a hidden-stockpile breach by the condemnation owner).
  It is not adopted because it changes accepted, implemented presentation and needs a condemnation-owner hook.

## Changelog

### 2026-10-10 spec audit

Pass 1, consistency and cleanup:
- Replaced the planning-era catalog reconciliation with the current state: the workbook row is aligned and Event 42 is a Low member of clusters 11, 15, and 18 in the workbook and live registry (README, Parts 1, 3, 4).
- Rewrote Part 1's landing sequence, which still described seven randomized per-visit report roles, to match the accepted two-popup presentation with hidden visits.
- Recorded that the Chaos milestones are implemented in script constants, added an implementation status section, marked the coding and goal prompts as historical, and fixed `AGENTS.md` and `.agents` links.
- Deleted `MANIFEST.sha256`, a byte-hash ledger that every documentation edit made stale.

Pass 2, design improvement:
- Reviewed the implemented event against the value and decision budget: it has no meter, no decision category, and one combined landing burden per state, so nothing was removed.
- Recorded one proposal (declare or conceal a nuclear cache) in Open questions instead of changing accepted presentation.
