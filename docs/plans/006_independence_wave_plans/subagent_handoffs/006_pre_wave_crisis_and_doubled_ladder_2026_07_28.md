# Event 006 doubled automatic ladder and host-facing crisis handoff

> Documentation reconciliation note (2026-07-28): This source handoff is retained as implementation evidence, but the focused completion audit narrows its status to HOLD / PARTIAL. Durable crisis-success receipt/Event Log attribution, requester-loss recovery, player-facing branch/consequence disclosure, and the accepted pending-versus-fourteen-day retry disposition remain unresolved. Its workbook/CSV mirror statement has no changed-cell list or exporter receipt and is not catalog authority; use the current source map and spreadsheet-worker audit for catalog status.

## Scope

This tranche applies the later user decision that doubles the automatic Independence Wave release bands and adds a scoped instability/occupation crisis that can request the ordinary synchronized wave. It supersedes the earlier 3/4/5/7/10 automatic ladder; scenario-bound counts remain owned by the SCN-008 matrix.

## Implemented surfaces

- `common/script_constants/006_independence_wave_constants.txt` now targets 6, 8, 10, 14, and 20 automatic releases, with World Collapse also at 20.
- `common/script_constants/006_independence_wave_super_event_constants.txt` and the 6002 qualification comments use the twenty-country high-chaos threshold.
- `common/script_constants/006_independence_wave_crisis_constants.txt` centralizes the 35% stability threshold, 50 resistance threshold, 120-day mission, 365-day cooldown, and visible failure deltas. Timing values use an integer schema and gameplay values use fixed-point tuning.
- `common/scripted_triggers/006_independence_wave_crisis_triggers.txt` exposes pressure from low stability, an enemy-controlled owned state, or a controlled foreign-owned state with severe resistance and gates the mission on the world-end, joint-presentation, coordinator, cooldown, and queue barriers.
- `common/scripted_effects/006_independence_wave_crisis_effects.txt` charges the existing standard security commitment, records the pressure source and transient queue/history data when the timed mission queues a wave, then queues the normal Event 006 entry and applies explicit failure/cooldown consequences without changing ownership. The focused completion audit finds no durable success receipt or crisis-specific host/cause Event Log attribution, so those accepted surfaces remain open.
- `common/decisions/categories/006_independence_wave_crisis_categories.txt` and `common/decisions/006_independence_wave_crisis_decisions.txt` provide the visible host-facing selectable mission. It is costed, including Command Power, AI-weighted, cancellable when pressure ends, and remains visible while its timer is active.
- `events/006_independence_wave.txt` adds `chaosx.nr6.3` as a queue consumer. It delegates to `independence_wave_prepare_and_execute_standalone_incident`, clears stale queue state, records blocked resolution, and never runs a second release path.
- `localisation/english/006_independence_wave_decisions_l_english.yml`, `localisation/english/chaosx_gui_l_english.yml`, and the Event 006 source docs expose the doubled bands and crisis conditions in player-facing wording.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and exporter-generated catalog CSVs mirror the doubled bands and crisis queue note.

## Reservation and safety contract

The crisis does not release a state directly. It only schedules the normal Event 006 root after the timed pressure window; if the shared coordinator is busy, the endpoint retries once per day up to the centralized retry limit before applying the blocked consequence. The existing frozen planner therefore remains responsible for host survival, capital preference, unique anchors, collision rerolls, Event 005 ordering, content attestation, rollback, and synchronized ownership mutation. No broad `on_daily` or `on_monthly` world loop was added.

## Validation evidence

- `python -B .tools/audit_event6_allocator.py` passes with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, the 6/8/10/14/20 ladder, World Collapse 20, and Event 005-first joint reservation order.
- New and touched Clausewitz files have balanced braces and no unsupported `<=` or `>=` operators in the focused static check.
- Localisation files retain UTF-8 BOM encoding.
- The crisis Event Log row uses Event 006 payloads 6003/6004/6005 for occupation, stability, and combined pressure and keeps the requester country id as the actor.

## Remaining risk / disposition

This is a source-level implementation handoff, not whole-event completion evidence. Only eleven package IDs across ten compatible reservation groups are currently content-attested, so the 14- and 20-country automatic bands remain fail-closed until additional complete packages and reservation capacity are admitted. Live mission timing, AI selection, queue cleanup, save/load persistence, host-survival execution, and scenario/runtime evidence remain open under the whole-event HOLD / PARTIAL disposition. A crisis resolution queues a full normal wave; it is not a per-state direct-liberation fallback. If the requesting host disappears before the scheduled endpoint executes, the global queue cleanup remains a runtime risk requiring focused evidence. The bounded fourteen-day retry is a deliberate fail-closed safety limit rather than an unbounded pending queue.
