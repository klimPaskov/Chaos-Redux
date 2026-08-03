# Event 012 W4 war-breakup settlement receipt

Date: 2026-08-03

Owner: Main Event 012 implementation agent

Status: Implemented source tranche; live-save acceptance remains open.

## Scope

The W4 trigger `africa_world_continental_war_protocol_settlement_is_proven` listed `africa_world_war_settlement_breakup`, but no effect wrote that receipt. This tranche closes that source mismatch without changing generic successor-loss breakup certification.

## Implementation

When `africa_world_union_war_record_breakup` certifies a breakup while the registered continental-war protocol is still open, the defeated actor and the registered attacker receive the existing `africa_world_war_settlement_breakup` and `africa_world_continental_war_protocol_settled` flags plus the existing `settled` status value.

Both actors open event `.725` before the existing lifecycle acknowledgement and cleanup events. The generic post-loss breakup path remains outside the war guard and continues to record only the package terminal disposition.

## Validation evidence

- Repository census now finds a writer for `africa_world_war_settlement_breakup` in the guarded W4 breakup path.
- The settlement proof trigger and event `.725` read the same receipt written on both war actors.
- The existing cleanup helper remains responsible for closing the active protocol and clearing transient targets.
- Edited Clausewitz blocks were checked for balanced braces and quoted event IDs.
- No live Hearts of Iron IV launch or save validation was performed.
