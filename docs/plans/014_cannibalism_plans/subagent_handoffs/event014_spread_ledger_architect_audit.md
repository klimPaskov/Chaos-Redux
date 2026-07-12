# Event 014 foreign-spread ledger architecture audit

Date: 2026-07-11  
Mode: read-only audit; no gameplay, localisation, interface, or spreadsheet files were edited  
Verdict: **not ready for a completion claim**. The normal enqueue/resolve path is coherent, but lifecycle cancellation, row identity, physical-route provenance, screening revalidation, and reinfection/recovery edge cases still violate the design contract.

## Audited surface and references

Primary implementation:

- `common/scripted_effects/014_cannibalism_spread_effects.txt`
- `common/scripted_triggers/014_cannibalism_spread_triggers.txt`
- relevant portions of `common/scripted_effects/014_cannibalism_core_effects.txt`
- `common/on_actions/014_cannibalism_on_actions.txt`
- `common/decisions/014_cannibalism_spread_decisions.txt`
- `events/014_cannibalism.txt`, events `.60` through `.62`
- `common/script_constants/014_cannibalism_core_constants.txt`
- `localisation/english/014_cannibalism_l_english.yml`

The trace also followed two adjacent owners that mutate or expose this ledger:

- `common/scripted_effects/014_cannibalism_country_effects.txt`, especially `cannibalism_remove_current_country_from_spread_ledger`
- `common/scripted_triggers/014_cannibalism_triggers.txt`, especially recovery and global-residue triggers

Required references were consulted from the offline wiki snapshot: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. Vanilla documentation consulted included `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, `common/on_actions/_documentation.md`, and `common/decisions/_documentation.md`. The approved Kaiserreich on-action file was used to verify recalled-volunteer scopes.

The most important design contract is `docs/plans/014_cannibalism_plans/014_scripted_system_architecture.md`, especially its aligned-array, expected-ID, lifecycle-invalidation, and post-iteration-compaction requirements.

## Required invariants

These invariants should be made executable preconditions, not comments:

1. **Array alignment:**

   `id^num == source_country^num == source_state^num == target_country^num == target_state^num == route^num == source_generation^num == due_date^num == status^num`.

2. **Row identity:** every live row has a positive, unique spread ID; its status is `queued` or `in_transit`; its route is one of 1 through 8; and an effect may mutate or clear the row only after re-reading and matching its expected spread ID.

3. **One target, one pending row:** for every target state, the number of live rows targeting it is either zero or one. The state flag `cannibalism_spread_inbound_active` and stored route/source/generation metadata must exist if and only if exactly one such row exists.

4. **Ledger equality:**

   - source `cannibalism_outbound_spread_count` equals its matching live source-generation rows;
   - target `cannibalism_inbound_spread_count` equals its live target rows;
   - the two country flags are present if and only if their corresponding count is positive;
   - `global.cannibalism_pending_spread_count` equals the number of live statuses.

5. **Lifecycle identity:** annexation, capitulation/source defeat, fixed-tag retirement, release, puppet creation, civil-war consolidation, and tag reuse must invalidate every old row before the old identity can be reused. No old target row may apply to a newly released country merely because it has the same tag.

6. **Compaction discipline:** queue traversal only changes status and clears ledgers. Physical index removal happens after traversal, from the end of all aligned arrays, and only if the alignment invariant holds.

7. **Physical route provenance:** every row records the actual country/state pair that performed the travel action. A route name must come from a proved border transfer, naval movement, volunteer return, control change, deliberate operation, conquest, or adjacent survivor movement—not from the source node's type alone.

## Severity-ranked findings

### [P0] Fixed-tag retirement and ordinary country lifecycle can leave stale ledgers or apply rows to a later incarnation

The normal resolver correctly calls `cannibalism_clear_loaded_spread_pending_state` (`014_cannibalism_spread_effects.txt:129-180`) before the main reverse compactor removes a row. The fixed-tag retirement path bypasses that API. `cannibalism_remove_current_country_from_spread_ledger` directly removes all nine indices (`014_cannibalism_country_effects.txt:1085-1117`), and it is called after `cannibalism_reset_current_country_incarnation_state` (`:1195`, `:1217`).

Consequences:

- retiring a source can leave another country's inbound count, warning flag, target-state inbound flag, and route/source metadata behind;
- retiring a target can leave its former target state marked inbound after control transfers;
- `cannibalism_rebuild_runtime_counts` repairs only the global pending count, not per-country counts or state metadata;
- the stale state flag permanently blocks a replacement row because every producer treats it as the one-target lock;
- the target side has no generation in the row, while `cannibalism_loaded_spread_entry_is_valid` checks only the source actor generation (`014_cannibalism_spread_triggers.txt:113-138`);
- `014_cannibalism_on_actions.txt` has capitulation, annexation, and civil-war pulse rehoming but no general row invalidation and no puppet/release lifecycle adapters. An annexed ordinary actor is not unregistered here.

Required patch locations and behavior:

1. In `014_cannibalism_spread_effects.txt`, add one canonical `cannibalism_invalidate_loaded_spread_entry` effect that:

   - accepts the current queue index and expected ID;
   - operates only on `queued`/`in_transit` status;
   - loads and revalidates the expected ID;
   - changes the status to `invalidated` before clearing ledgers, making repeated calls idempotent;
   - calls the existing pending-ledger clearer exactly once;
   - never removes an index.

2. Add `cannibalism_invalidate_spread_entries_for_current_country_lifecycle`. It must scan live statuses, match current country against both source and target country arrays, and call the canonical invalidator. Leave tombstones for `cannibalism_compact_spread_queue`.

3. Replace the direct removals in `cannibalism_remove_current_country_from_spread_ledger` with that helper. Move the call before `cannibalism_reset_current_country_incarnation_state`, so source generation and counters still exist while ledgers are cleared.

4. In `014_cannibalism_on_actions.txt`, invoke lifecycle invalidation on the documented narrow hooks before reuse: at least `on_capitulation`, `on_annex`, `on_civil_war_end_before_annexation`, `on_puppet`, `on_release_as_free`, `on_release_as_puppet`, and `on_subject_annexed`. Reconcile released scopes before they can inherit old Event 014 flags or variables. These are the same lifecycle families already required by the architecture plan.

5. Rebuild per-country/state pending ledgers from live rows after lifecycle reconciliation, or prove through the canonical invalidator that every mutation preserves the equality invariant. Do not silently clear a mismatched queue as a repair fallback.

### [P1] The nine arrays are aligned on the happy path, but alignment and spread ID are never validated

`cannibalism_enqueue_spread_entry` appends all nine fields in order (`014_cannibalism_spread_effects.txt:97-105`), and the main compactor removes all nine in reverse-index order (`:431-455`). That part is sound.

However:

- processing uses `status_entries^num` as the sole length (`:402-429`);
- loading dereferences route, generation, and four scope arrays without checking each length (`:362-370`);
- the ID array is appended, compacted, initialized, and cleaned, but never loaded or compared during resolution;
- the target state's stored route/source/generation metadata is not compared with the loaded row;
- a missing scope entry can leave a prior regular event target in the current effect chain, allowing a malformed row to reuse the previous row's scope;
- enqueue uniqueness relies only on the target-state flag, not an authoritative live-row check.

Required patch locations and behavior:

1. Add `cannibalism_spread_queue_arrays_are_aligned` to `014_cannibalism_spread_triggers.txt`, comparing all nine `^num` values.
2. Gate `cannibalism_process_spread_queue`, lifecycle invalidation, pending-count rebuild, and `cannibalism_compact_spread_queue` with this trigger before any indexed access.
3. Extend `cannibalism_load_spread_entry_context` to load `cannibalism_expected_spread_id` from the ID array and reject non-positive IDs.
4. Persist `cannibalism_inbound_spread_id` on the target state at enqueue. Resolution/clear must require the state ID, route, source country, and source generation to match the loaded row before mutating that state's flags.
5. Reject enqueue if a live status already targets the state, even if its cache flag is missing. Conversely, flag-without-row is an invariant failure that must be reconciled explicitly.
6. If alignment fails, stop queue mutation and expose a dedicated invariant-failure state for repair; do not guess which array is authoritative.

### [P1] All eight route numbers exist, but several producers do not prove the route they label

`cannibalism_set_automatic_spread_route_from_source_state` (`014_cannibalism_spread_effects.txt:461-514`) converts a source node type into prisoner transfer, convoy, occupation turnover, volunteer return, or conquest. Its caller always chooses adjacent enemy states (`:519-550`). Therefore a port/island node crossing a land border is labelled `convoy`, a rail node crossing a border is labelled `volunteer_return`, and an occupation/warlord node can create turnover/conquest without the corresponding control-change action.

There is no separate overseas convoy producer anywhere in the route assignments. The only convoy assignment is the adjacency mapper at `:482`.

Two other physical-pair defects remain:

- deliberate seeding proves either a shared border or two ports, but always records the source country's capital as `cannibalism_spread_source_state` (`:837-878`, especially `:847`), even when the capital is neither the bordering state nor the departure port;
- local-victory survivors choose an arbitrary controlled source state, a neighboring country, and then an arbitrary controlled target state (`:728-788`). The two recorded states need not share the border that made the countries neighbors.

Required route changes:

- Restrict the automatic border pulse to a route whose action it actually proves—normally retreat. Keep prisoner transfer only in the explicit prisoner-transfer operation unless a dedicated transfer condition is added. Remove convoy, volunteer-return, occupation-turnover, and conquest inference from node type.
- Keep the dedicated `on_state_control_changed` producers for occupation turnover and conquest and the dedicated `on_recall_volunteers` producer for volunteer return.
- Add a real convoy producer using the documented `on_naval_invasion` scope contract. The offline wiki and vanilla on-action list verify: default/THIS is the invaded state, ROOT is the invading country, and FROM is the starting state. Add an `on_naval_invasion` adapter in `014_cannibalism_on_actions.txt` and an invaded-state-scoped helper in `014_cannibalism_spread_effects.txt` that records ROOT as source country, FROM as source state, THIS as target state, and THIS's controller as target country. Require the departure state to be ROOT-controlled, coastal/port-bearing, and a live port/island Event 014 node; require a different valid target controller and an eligible invaded state. This is a real, narrow, engine-fired overseas movement and needs no periodic world scan.
- For deliberate land seeding, save the actual ROOT-controlled neighboring state. For coastal seeding, save the actual ROOT-controlled departure port. Do not save `capital_scope` unless it independently satisfies that route.
- For survivors, select a controlled source state that has an eligible foreign neighboring state, then select that neighboring state directly and derive its controller. Do not select the two states independently.

Route coverage after semantic audit:

| Route | Current producer | Result |
|---|---|---|
| Retreat | Adjacent wartime border pulse | Pass, if made the border pulse's explicit route |
| Prisoner transfer | Explicit prison-host operation; also generic prison-node adjacency | Partial; keep the explicit operation and remove the generic relabel |
| Convoy | Port/island node plus adjacent land target | Fail; add verified `on_naval_invasion` producer |
| Volunteer return | Verified `on_recall_volunteers`; also generic rail-node adjacency | Partial; dedicated hook passes, generic relabel fails |
| Occupation turnover | Verified state-control change; also generic occupation-node adjacency | Partial; dedicated hook passes, generic relabel fails |
| Deliberate seed | Border/port target proof, but capital recorded as source | Partial |
| Conquest | Verified state-control change; also generic warlord-node adjacency | Partial; dedicated hook passes, generic relabel fails |
| Survivor | Neighbor-country proof with independently chosen states | Partial |

### [P1] Screening effects are not click-time safe and can spend resources or screen the wrong current row

Event `.60` exposes options based on cost triggers at event fire (`events/014_cannibalism.txt:260-286`) and then calls unguarded payment helpers. Offline Event modding states that an option trigger is evaluated when the event fires and does not update while the event remains open; the default timeout is 13 days. During that interval, resources, state control, row validity, screening state, or even the row occupying that state can change.

The decision effects have the same canonical-helper weakness (`014_cannibalism_spread_decisions.txt:21-26`, `:46-51`). `cannibalism_pay_humane_route_screening_cost` and `cannibalism_pay_hard_route_screening_cost` (`014_cannibalism_spread_effects.txt:794-835`) deduct first and set state flags without an internal cost/controller/pending/unscreened/expected-ID guard.

The payment triggers also use strict `>` for manpower and command power (`014_cannibalism_spread_triggers.txt:219-230`), so a country with exactly the displayed cost cannot pay even though equipment equality is accepted.

Required patch:

- Replace each payment helper with a `try_...` effect whose single outer limit rechecks: expected spread ID, target-state metadata, `is_controlled_by = ROOT`, inbound flag, not already screened, route still live, and current full affordability. Only then deduct and set flags. Return an explicit result variable.
- Give event `.60` a per-state warning instance rather than a country-global numeric snapshot. At enqueue, persist the row ID as `cannibalism_inbound_spread_id`. In `.60` immediate, copy it to `cannibalism_warning_expected_spread_id` on the target state and set `cannibalism_spread_warning_event_open`. Every `.60` option clears that warning-instance metadata; lifecycle cleanup clears it if the recipient disappears. While the warning instance is open, reject a replacement enqueue to that state. The guarded option then requires `warning_expected_spread_id == inbound_spread_id` and a live row with that ID. This remains safe with several simultaneous warnings because the snapshot is state-scoped, and the normal minimum route delay (14 days) exceeds the default event timeout (13 days).
- Make event `.60` and both decisions call only the guarded effects. Decisions act on the currently stored inbound ID and must resolve that ID to one live row before payment. A stale event becomes a no-op with no cost and cannot screen a later row in the same state.
- Use `check_variable` with `greater_than_or_equals` for manpower and command power, matching the displayed cost.
- In the decisions, keep affordability in `available`/`custom_cost_trigger`; do not use it as target discovery.

### [P1] Stabilized states are permanently excluded from real external reinfection

`cannibalism_state_is_liberated_recovery` includes `cannibalism_state_stabilized` (`014_cannibalism_triggers.txt:339-346`). Every spread target and producer excludes that broad trigger, in addition to separately excluding `cannibalism_recovery_active` (`014_cannibalism_spread_triggers.txt:24-74`, `:130-137`, and the producer limits).

Recovery clears `cannibalism_recovery_active` when it reaches stabilized, but leaves `cannibalism_state_stabilized`. Therefore a one-state recovered country—or a country whose controlled states all recovered—can never receive the external route that is supposed to reactivate it. The country-level `cannibalism_external_reinfection_protected` flag is not what blocks the route; the permanent state exclusion is.

Required patch:

- In foreign-spread target filters, exclude only active recovery (and genuinely unusable states), not the terminal stabilized marker.
- Keep `cannibalism_state_is_liberated_recovery` broad for systems that need historical recovery identity; introduce a narrower spread-specific trigger rather than changing unrelated callers.
- On successful arrival, the existing state-stage setter clears the stabilized marker before applying the new stage, so no extra fallback stage is needed.

### [P1] Liberation recovery is coupled to an enqueue-only war/source test and can be skipped after capitulation or peace transfer

`cannibalism_try_enqueue_occupation_turnover_from_control_change` puts both recovery and route production under one outer condition (`014_cannibalism_spread_effects.txt:558-618`). That condition requires the old controller to remain a valid, non-capitulated spread source and still be at war with ROOT (`:564-567`). The actual recovery begins later at `:601-617`.

Thus the changed state can retain a live Event 014 node when control changes as part of capitulation/peace and the old controller no longer passes those producer conditions. Recovery should depend on the node and new controller, not on whether a second rear-area route can be enqueued.

Required patch:

- Split `cannibalism_handle_state_control_recovery` from `cannibalism_try_enqueue_occupation_turnover_from_control_change`.
- Run recovery first from `on_state_control_changed` when the changed state is a live, generation-matching node and the new controller is an eligible ordinary country. Do not require the old controller to be non-capitulated or currently at war for recovery.
- Separately attempt occupation-turnover enqueue only if the old source is still generation-valid, non-capitulated, and at war, and an eligible distinct target state exists.

### [P2] Spread cooldown and reinfection-protection timed flags use a disallowed duration-token pattern

The automatic route cooldown passes an unprefixed temporary variable to a timed country flag (`014_cannibalism_spread_effects.txt:546-547`). Local victory does the same for reinfection protection (`014_cannibalism_core_effects.txt:1156-1157`). The repository's `chaos-redux-events` skill explicitly requires file-scoped `@` literals for these static flag durations because these fields can reject `constant:` and variable tokens; current vanilla examples that use a variable use an explicit `var:` token, while an older vanilla SOV precedent records that the unprefixed form did not work.

Required patch:

- Mirror `cannibalism_spread.automatic_route_cooldown_days = 45` with a file-scoped `@... = 45` in the spread file and pass that literal to `days =`.
- Mirror `cannibalism_timing.clean_recovery_days = 180` with a file-scoped literal in the core file and pass it to the reinfection-protection flag.
- Audit the other Event 014 timed flags separately; do not assume the current unprefixed temporary-variable pattern is valid because the value was first loaded from a script constant.

### [P2] The foreign-spread surface still performs broad daily/pulse scans

There is no `on_daily`, `on_weekly`, or `on_monthly` Event 014 on-action, and queue resolution itself iterates registered arrays. That part passes.

Two literal world-scan paths remain:

- both spread decisions use `state_target = yes` (`014_cannibalism_spread_decisions.txt:13`, `:38`). Vanilla decision documentation states that `yes`/`any` checks every state in the world daily once the root prefilter passes and should be avoided; these decisions need only controlled states;
- every Event 014 pulse calls `cannibalism_check_global_victory` (`014_cannibalism_core_effects.txt:2168`), whose worldwide-victory trigger calls `cannibalism_has_global_residue`. That trigger uses `any_country` and `any_state` world scans (`014_cannibalism_triggers.txt:110-117`).

Required patch:

- change both decisions to `state_target = any_controlled_state`;
- change `target_root_trigger` to the stable visibility/pending-route prefilter and leave affordability in `available`;
- for the recurring pulse, derive residue from the validated actor/node/recovery/spread registries and the counts rebuilt immediately before the victory check. If a direct world scan is retained as a repair audit, make it non-periodic and explicit; the current runtime cannot truthfully claim zero broad periodic world iteration.

### [P3] Two player-facing tooltips leak implementation terminology, though hidden-identity gating passes

`cannibalism_humane_route_screening_effect_tt` calls the mechanic an “active Event 14 response,” and `cannibalism_seed_foreign_formation_effect_tt` says it “Queues one generation-checked” route and creates an “Event 14 cell” (`014_cannibalism_l_english.yml:330`, `:340` in the audited snapshot). These describe implementation and ledger behavior rather than the world state.

Rephrase them in-world, for example around an active domestic cell, a verified foreign formation, and an arrival/containment outcome. This is not a Hannibal/Oth-Kesh identity leak.

## Scope and engine checks that pass

- **Scoped generation expression is valid.** `event_target:cannibalism_spread_source_country.cannibalism_actor_generation` is valid variable scoping. The offline Data structures page explicitly documents `event_target:my_event_target.var_name`. The current uses at `014_cannibalism_spread_effects.txt:103` and `:119` are syntactically correct; the lifecycle coverage around that generation is the defect.
- **State-control stack is valid.** Offline On actions documents `on_state_control_changed` as ROOT = new controller, FROM = old controller, FROM.FROM = changed state. The current `FROM.FROM` uses at `014_cannibalism_spread_effects.txt:568-583` and `:635-663` are correctly scoped. `FROM` remains the hardcoded old-controller scope inside the changed-state block.
- **Volunteer return stack is valid.** Approved Kaiserreich precedent states `FROM = country losing volunteers, ROOT = country recalling volunteers`. The current helper correctly treats FROM as the infected host/source and ROOT as the returning volunteer owner/target.
- **Main queue compaction order is sound.** The pulse processes the spread queue before reverse compaction (`014_cannibalism_core_effects.txt:2151-2152`), and the main compactor removes all nine arrays from the end. The separate warlord retirement bypass is the failure.
- **Local-victory source generation is preserved long enough to enqueue one survivor row.** Local victory clears the active flag but retains actor generation, and the survivor source-valid trigger explicitly permits the survivor route. A later external activation registers a new generation, invalidating old source-generation rows. The physical state-pair selection still needs correction.
- **All eight route constants and parameter sets exist.** The problem is producer provenance, not missing enum values or delay/strength parameters.
- **Cleanup includes all nine arrays.** Initialization and global cleanup clear/resize the aligned queue arrays together.
- **Pre-reveal identity gating passes.** Events `.60-.62` and their localisation do not name Hannibal, Oth-Kesh, or a supreme organizer. Event-detail scripted localisation selects the pre-reveal text until `cannibalism_reveal_complete`, and the Evolution III detail preview is added only after that flag.

## Recommended implementation order

1. Add executable array/ID/state-ledger invariants and the canonical idempotent invalidator.
2. Replace fixed-tag direct removal and complete country lifecycle invalidation hooks.
3. Make route producers action-specific; add the verified `on_naval_invasion` convoy adapter; correct deliberate-seed and survivor state pairs.
4. Bind warning/screening actions to the current row ID and revalidate inside the payment effects.
5. Decouple state recovery from occupation-route production and allow stabilized states to receive a real external route.
6. Repair timed-flag durations, targeted-decision scope, recurring residue scans, and player-facing meta wording.

## Acceptance scenarios

Before declaring the spread ledger complete, verify at least these scenario outcomes:

1. Two live rows into two states of one target produce target count 2; resolving one leaves count 1 and the warning flag; resolving the other clears both.
2. Attempting a second live row into the same state is rejected by both the authoritative row check and state metadata.
3. Retiring a reusable warlord that is a source clears the other country's warning/count/state metadata exactly once and leaves a tombstone until post-loop compaction.
4. Annexing then releasing a source or target tag before the due date cannot make the old row valid in the new incarnation.
5. A malformed unequal-array test state performs no indexed mutation and exposes the invariant failure; it does not reuse a prior row's event targets.
6. A naval invasion from an Event 014 port/island node creates a convoy row whose recorded FROM departure state and invaded target state prove the overseas movement. Mere adjacent land contact never creates a convoy row.
7. Volunteer recall uses infected host FROM and returning owner ROOT; no generic rail-border pulse creates the same route.
8. Occupation/conquest rows occur only from the matching state-control action. A peace/capitulation control transfer still starts recovery even when no route can be enqueued.
9. A local-victory survivor row uses two actually adjacent states. A fully stabilized one-state country can later be externally reinfected through a real route.
10. Leaving event `.60` open, spending the resources, transferring the state, invalidating the row, or replacing the row never causes negative payment or screening of a different spread ID.
11. A country holding exactly the displayed manpower, equipment, and command cost can pay.
12. Spread decisions inspect only controlled states, and the recurring Event 014 pulse does not scan all countries/states for spread residue.
13. Before reveal, warning, arrival, event-detail, and evolution-preview text exposes no hidden organizer identity.

## Simplifications, omissions, and blockers

No fallback or implementation simplification was used: this was a read-only audit. The blockers above remain unimplemented. No commit was created.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`.
