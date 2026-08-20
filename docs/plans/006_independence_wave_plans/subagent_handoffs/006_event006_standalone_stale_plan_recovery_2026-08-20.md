# Event 006 standalone stale-plan recovery handoff

Date: 2026-08-20

## Disposition

The manual `chaosx.nr6.1` entry path is source-wired and remains hidden until a positive committed allocation exists. This handoff records a narrow recovery fix for an Event 006-only plan left in `collecting`, `allocating`, or pre-execution `locked` state. It does not add a decision category, pressure system, queue, mission, cost surface, or other pre-event player-facing indication.

## Source change

Changed `common/scripted_effects/006_independence_wave_execution_effects.txt`.

Added `independence_wave_reset_stale_standalone_plan` and called it at the start of `independence_wave_prepare_and_execute_standalone_incident`.

The reset is limited to plans owned by Event 006 that exclude Event 005 and have not crossed either execution or finalization. A pre-execution locked plan first restores host capitals, then clears the Event 006 contribution and aborts the stale transaction when restoration has not failed. Joint plans and plans past the execution barrier are untouched.

## Why this matters

`liberation_release_begin_plan` rejects a second begin call while an Event 006 standalone plan is still collecting, allocating, or locked. A failed manual entry could therefore leave the next `chaosx.nr6.1` invocation with no allocation and no public report. The new state-only reset allows a fresh standalone transaction without presenting a false release.

The separate allocator fix in commit `e7992bbbb` also matters: unattested rows no longer receive the minimum selection weight. This prevents unimplemented rows from consuming random-selection attempts before an attested package can be reserved.

## Pre-event surface and cost localization

The current source has no live `independence_wave_crisis_category`, `independence_wave_open_host_crisis`, or pre-wave crisis cost localization. `chaosx.nr6.1` is hidden and triggered-only, while `chaosx.nr6.2` is gated on a positive committed presentation count. `chaosx.nr6.3` is hidden cleanup-only compatibility code. Current Event 006 cost rows are compact amount-plus-icon strings; the screenshot's long pre-wave cost sentence is not present in the current localization tree.

## Capital-scope log audit

The three logged package trigger files currently contain fixed numeric state scopes and no `capital_scope` references:

- `common/scripted_triggers/006_independence_wave_epirus_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_thrace_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_banat_package_triggers.txt`

The pasted `capital_scope` messages therefore come from an older or different source snapshot. Legitimate `capital_scope` uses elsewhere were left unchanged.

## Evidence

- `python .tools/audit_event6_allocator.py` passes with 149 publishers, 40 adapters, 32 attested packages, 29 compatible reservation groups, and a static standalone witness of 20 admitted packages. The audit reports the pre-event crisis surface retired.
- Mandatory `hoi4.event_inspect` for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, revision `98ac244e0b194a88389dbe53658d4876e5d76d2c5eb52b52ff572abea77b4fe3`, with zero selected blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d43ba69c4d0fc1ae60a12140441afb9eda815014074ea93f9a864390d6cd96b/c1093035ac42d54e1fc954802b90f59c502c23ea34c4090f01236af1316efcc2/event-lint-98ac244e0b19.json`.
- Mandatory `hoi4.event_render` for the same entry returned `EVENT_RENDERED_PARTIAL`, zero selected blocking diagnostics. State artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/daf382bc014cf0098b06ae702dbb5fd02d344a0e6888fc21fef447b1a3b619c1/ce95c617b2690b546dcbd1c32979fe196423cece587474a6d897891bbacda758/event-state-98ac244e0b19.json`.
- Weighted inspection of the planner random-list source returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`; the allocator's scripted/meta assembly is outside the adapter's inspectable surface, so no quantitative probability claim is made.

## Remaining boundary

Event 006 remains a partial system. Central authority is 40 adapters, 32 attestations, 29 compatible groups, and 161 unattested selectable rows. This patch does not promote packages, widen attestation or Join lists, or claim live-game completion.
