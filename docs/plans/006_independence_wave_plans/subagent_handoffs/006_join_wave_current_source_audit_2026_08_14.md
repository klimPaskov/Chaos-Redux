# Event 006 Join-the-Independence-Wave Current Source Audit

Status: current source parity and documentation audit completed on 2026-08-14.

## Current source contract

The Join conversion path is implemented in `common/scripted_effects/006_independence_wave_join_effects.txt`, `common/scripted_triggers/006_independence_wave_join_triggers.txt`, `common/on_actions/006_independence_wave_join_on_actions.txt`, `events/006_independence_wave_join.txt`, and `localisation/english/006_independence_wave_join_l_english.yml`.

The deterministic first-success probe contains exactly the 32 current content-attested package IDs in this order: IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-038, IW-040, IW-044, IW-045, IW-033, IW-041, IW-070, IW-071, IW-072, IW-173, and IW-184.

The set of probe IDs is exactly equal to `has_independence_wave_runtime_package_content_attestation_for_execution_id`, and every ID has a matching `independence_wave_reserve_package_iw_*` wrapper.

The Join path observes only scoped war-entry, state-control, peace-conference, capitulation, and release callbacks, and its seven-day hidden `.40` retry is single-flight under `independence_wave_join_retry_pending`.

The threshold remains at least two states lost and a 50% or greater reduction from the largest observed owned-state baseline, with a 90-day decline cooldown and no periodic or world-wide scan.

Acceptance retains the ordinary frozen Event 006 release transaction, including package setup, generic focus assignment, force/package mechanics, final validation, Event Log/history, and the human-only post-commit tag switch.

## Source checks

Join effects, triggers, on-actions, and events have balanced Clausewitz braces at 313/313, 35/35, 25/25, and 20/20 respectively, and the touched scripts use tab indentation without unsupported comparison operators.

The Join localisation file is UTF-8 with BOM and contains the report title, description, options, cooldown tooltip, failure receipt, and four history payload strings.

The current allocator audit reports 149 publishers, 32 content-attested packages, 29 compatible reservation groups, 161 unattested selectable rows, and 40 runtime adapters, with the 3/4/5/7/10 ladder and World Collapse ceiling of 10 unchanged.

The current scenario-matrix audit passes all 32 SCN-008 cells and 8 edge cases.

## MCP evidence and limits

Focused `hoi4.event_inspect` on `chaosx.nr6.36` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`; the linked scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7019e5bc170ece518ebfc85e057cd6abcf54f24cd5f6fbe00fdba84ead453943/b9e8bc67709814c566361c8dda142e4a8a6276516a1e5352e5cb4091ea3a6a61/event-scan-741883f50501.json`.

The partial result deferred workspace-wide helper and lifecycle projection, so it is source-linked engine evidence rather than a complete runtime or live-game validation.

The Join candidate probe is deterministic and has no weighted selection surface; no normalized probability, timing, or AI-balance claim is made.

## Scope and remaining boundary

This tranche does not promote IW-047 MEL or IW-050 KOM, does not widen adapter-only packages, and does not alter formable GUI, super-event 23 audio/firing, or technology-viewer boundaries.

The broader Event 006 authority remains HOLD/PARTIAL until the unattested package breadth, portrait/flag rights gates, typed probability fixtures, GUI family-isolated evidence, super-event 23 approval, and other documented blockers are resolved.
