# Event 012 W4 successor, exile, and breakup callbacks

Date: 2026-08-03

Owner: Main Event 012 implementation agent

Status: Implemented source tranche; live-save acceptance remains open.

## Scope

This tranche wires the existing lifecycle acknowledgement events to their already implemented successor, exile, and breakup receipts without adding tags, models, or new gameplay stores.

## Callback wiring

`africa_world_union_war_commit_successor` now opens `.743` and `.748` on the receiving successor and `.746` and `.747` on the replaced predecessor after the accepted transfer helper has written their flags.

`africa_world_union_war_record_exile` now opens `.744`, `.748`, and `.749` after the exile receipt and terminal disposition are recorded.

`africa_world_union_war_record_breakup` now opens `.745`, `.748`, and `.749` after the breakup helper has written the package terminal receipt and before shared cleanup.

Event `.749` accepts the three existing terminal receipt forms: package terminal resolution, exile resolution, or successor registration. It no longer excludes the documented exile and successor paths.

## Validation evidence

- Every newly opened event is called only after its own trigger flag is written in the same lifecycle effect and before cleanup can clear transient state.
- The successor path preserves the original predecessor and candidate scopes through the existing global event target.
- Static event-ID census now finds source callers for `.743` through `.749` in the successor, exile, or breakup wrappers.
- Edited Clausewitz blocks were checked for balanced braces and quoted event IDs.
- No live Hearts of Iron IV launch or save validation was performed.

## Remaining boundary

Continental-war acknowledgement surfaces outside the successor/exile/breakup lifecycle remain separately gated by their existing settlement receipts and are not promoted by this tranche.
