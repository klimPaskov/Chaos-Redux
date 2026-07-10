# Event 017 Random Faction improvement-loop closure handoff

- Date: 2026-07-10
- Status: completion-audited closure handoff, not a design expansion
- Source of truth: `docs/specs/017_random_faction_specs/`
- Reviewed implementation state: current Event 017 script, localisation, assets, documentation, shared event-system diff, architecture and explorer reports, icon handoff, and the completed decision and mission audit handoff

## Resolution status on 2026-07-10

This table records the live implementation disposition. The accepted specs remain unchanged.

| Closure item | Status | Evidence |
| --- | --- | --- |
| Evolution III survivor, share cap, and overlap control | Resolved | `random_faction_run_evo3_cascade` computes the response budget as the smallest of half rounded up, candidate count minus one, and five. It refuses pools below two, keeps the counters country-scoped, and applies a 45-day dynamic lock to the anchor's region. |
| Exact history-row faction leader | Resolved | Event 17 binds the shared history sequence on the selected minor, then stores the successful leader in the matching secondary-actor history entry by sequence and Event ID. History and Event Details expose bound, lost-leader, and unresolved branches. |
| Three Event Details evolution previews | Resolved | `events_log_rebuild_open_event_details_view` adds Regional Bloc Race, Pressured Neutrality, and Collapse of Neutrality previews at tiers 1, 2, and 3. |
| Architecture tuning ownership | Resolved | Event effects use shared script constants directly for fixed delays and bridge computed delays, timed flags, and timed ideas through temporary variables. Decision re-enable fields use script constants directly, while mission timeout variables are initialized from constants before activation. Only parser-static `ai_hint_pp_cost` and maritime `random_select_amount` retain documented file-scoped values. |
| Pressure expiry and achievement-proof lifetime | Resolved | Every timed pressure or liaison application schedules its own buffered `.85` cleanup probe. Later effects therefore retain the target through their actual final duration, and the last probe removes obsolete pressure state. Active achievement candidates guard ordinary expiry; `.81`, `.82`, `.83`, `.84`, and `.86` re-enter cleanup after the exact proof closes, while lifecycle and world-end invalidation still clear it immediately. |
| Continuous achievement proof | Resolved | Frontier Commitment snapshots the launch capital and all national core-border states and cancels on the first stored-state loss. Liaison Web registers exactly three original support targets and persists disqualification for subject status, capitulation, annexation, special invalidity, or direct war while allowing faction membership. Not Everyone Signed registers only the original regional survivors and permanently removes each country on alignment or invalidation, so the day-180 check cannot substitute a later survivor. |
| Canonical documentation and GFX consumer | Resolved by the documentation curator | `docs/events/017_random_faction.md` matches the live dynamic selection, local cascade budget, exact history result, decisions, cleanup, achievements, and asset wiring. `docs/assets/017_random_faction/gfx_handoff.md` names `random_faction_bloc_pressure_category`. |
| Catalog workbook | Resolved by the spreadsheet worker | `subagent_handoffs/017_random_faction_spreadsheet_alignment_handoff.md` records exact localisation writeback and readback for `Events!18`, plus the final `8, 17` member list and Diplomatic Panic text in `Clusters!4`. |
| Decision and mission closure | Resolved | `subagent_handoffs/017_random_faction_decision_mission_audit_handoff.md` covers all eleven decision and mission families. |
| Asset closure | Resolved | `subagent_handoffs/017_random_faction_icon_artist_handoff.md`, `docs/assets/017_random_faction/manifest.md`, and `docs/assets/017_random_faction/gfx_handoff.md` record the complete static, animated, and achievement package. |
| Final localisation audit | Resolved | `subagent_handoffs/017_random_faction_localisation_audit_handoff.md` records a pass after the Four Doors, Frontier Commitment, Liaison Web, and Not Everyone Signed proof contracts were aligned. It found no blocker, fallback, simplification, missing key, duplicate key, orphan key, or unresolved gameplay/localisation mismatch. |
| Completion-audit corrections | Resolved | Evolution II wartime reach is a hard validity gate; special identities are set before lifecycle cleanup; rebuilt regional targets schedule cleanup; leader reaction has a 180-day cooldown; Crowded Border is confined to Event 17 pressure regions; Frontier Commitment uses the exact war/enemy-faction-border predicate; baseline history state is marker-gated; and terminal paths clear option counts. |
| Final completion audit | Resolved | `subagent_handoffs/017_random_faction_event_completion_audit_handoff.md` records a full PASS over the accepted requirement matrix and adversarial scenarios. No blocker, fallback, simplification, missing visible surface, or omitted accepted content remains. |

## Closure decision

Event 017 is deep enough for its Minor Repeatable role. The implemented tranche already has weighted country selection, one to four living-faction choices, the same saved choices for humans and AI, one shared join result, persistent alignment and pressure memory, three playable decision holder roles, narrow lifecycle hooks, three evolution stages, six proof-based achievements, finished asset families, event-log and cluster integration, and a fully audited eleven-family decision map.

No additional route, country package, focus tree, formable, super-event, custom window, evolution stage, decision family, achievement, or asset family is needed for completion. The final completion-audit gate passed; the remaining parent-owned action is the scoped implementation commit.

## Mandatory closure blockers

### 1. Preserve an Evolution III regional survivor [resolved]

Pre-closure evidence:

- `common/script_constants/chaosx_random_faction_constants.txt` sets `evo3_min_followups = 2` and `evo3_max_followups = 5`.
- `random_faction_run_evo3_cascade` in `common/scripted_effects/017_random_faction_effects.txt` sends the first two selected candidates into the forced faction-choice route.
- A two-candidate regional pool can therefore align every eligible country in that pool. The later survivor check only observes the result and does not reserve a survivor.

This conflicts with the accepted Evolution III rules that one firing cannot align every eligible country in a region and that some countries can remain outside factions.

Implemented bounded correction:

1. Count the valid, unique candidates in the current regional bucket before resolving any candidate.
2. Do not start a cascade with fewer than two candidates.
3. Compute one local response budget from centralized constants. The default budget should be the smallest of:
   - the absolute five-country cap,
   - one half of the current candidate pool rounded up,
   - the current candidate count minus one.
4. Clamp the guaranteed follow-up count to that response budget. With two candidates, only one may enter the forced choice route. The existing resistance draw may operate only inside the remaining budget.
5. Keep candidate uniqueness and recent-alignment cooldown checks. Do not introduce a shared world counter.
6. Prevent overlapping active cascades for the same regional identity from exceeding the same regional-share budget. Use the region identity and active-cascade ledger from the architecture handoff only to the extent needed to enforce this invariant. It must be cleaned when the cascade expires or its owner becomes invalid.

Acceptance cases:

| Valid regional candidates at cascade start | Maximum resolved by one cascade | Required outside-faction capacity |
| --- | ---: | ---: |
| 0 or 1 | 0 | all candidates |
| 2 | 1 | at least 1 |
| 3 | 2 | at least 1 |
| 4 | 2 | at least 2 |
| 5 | 3 | at least 2 |
| 8 | 4 | at least 4 |
| 9 or more | one half rounded up, capped absolutely at 5 | at least the starting count minus the response budget, subject only to unrelated world changes |

Run one overlapping-cascade case as well. Two anchors resolving the same regional identity during the lock window must not each receive an independent full budget.

### 2. Bind the chosen faction leader to the exact history row [resolved]

Resolution: the shared Event Log owns parallel secondary-actor arrays, and Event 17 fills the matching row by exact history sequence and Event ID after the join succeeds. Bound, lost-leader, and unresolved text branches are wired into History and Event Details.

The selected minor is correctly used as the main actor, and live Event Details text can resolve its stored chosen leader. Event 017 is repeatable, however, so reading the actor's current leader memory is not sufficient for an older history row after succession, departure, or a later Event 017 alignment.

Implemented bounded correction:

1. In `common/scripted_effects/chaosx_events_log_effects.txt`, add Event 017 parallel history storage for the chosen leader, keyed to the exact history sequence created for that firing.
2. Bind that secondary actor after the shared join succeeds. Do not assume that the newest history entry is still array index zero.
3. Copy, sanitize, clear, and expose the secondary actor anywhere the existing history/detail arrays are rebuilt or reset.
4. In `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, render the bound historical leader or faction for history context. Live context may continue to use current Event 017 memory.
5. If the historical leader no longer exists, retain the selected minor and use neutral wording rather than substituting an unrelated live faction.

Acceptance test: fire Event 017 twice with different selected minors and leaders, then open both history rows after a faction-leadership transfer. Each row must retain its own selected minor and original chosen-leader result.

### 3. Add the three Event Details evolution previews [resolved]

Resolution: the Event 17 branch adds exactly three ordered preview rows at tiers 1, 2, and 3 through `events_log_add_event_detail_evolution_preview`.

`events_log_rebuild_open_event_details_view` currently has preview branches for other events but no branch for Event 17. The Event 017 evolution title and body selectors already exist, so this is wiring rather than new writing.

Implemented surface in `common/scripted_effects/chaosx_events_log_effects.txt`:

- match `event_id` to `constant:random_faction_event.id`
- add exactly three preview rows through `events_log_add_event_detail_evolution_preview`
- use `constant:random_faction_event.evolution_type`
- use tiers 1, 2, and 3
- use the stages `regional_bloc_race`, `pressured_neutrality`, and `neutrality_collapse`

Acceptance test: Event Details shows all three ordered previews before Event 17 fires, preserves their enabled or disabled state, and opens the correct title and body for every row. History evolution views must continue to show only stages actually recorded.

### 4. Reconcile the final documentation and catalog workbook [resolved]

Resolution status: the canonical event document and GFX handoff are corrected. The parallel spreadsheet worker completed workbook writeback and readback and recorded the result in `subagent_handoffs/017_random_faction_spreadsheet_alignment_handoff.md`.

Pre-closure documentation findings:

- `docs/events/017_random_faction.md` says manual settings dispatch first prefers the current player. The live shared dispatch correctly uses the weighted eligible-country pool for automatic, manual, Event Details, and cluster routes.
- The same document names `global.random_faction_evo3_cascade_count`, while the implemented counter is country-scoped and the final capped regional budget must remain cascade-local.

The documentation curator removed both stale statements after the cascade correction and exact history binding. The decision-category consumer in `docs/assets/017_random_faction/gfx_handoff.md` is also corrected to include the `_category` suffix.

`docs/spreadsheets/chaos_redux_events_catalog.xlsx` remained unchanged during the planning pass. The parallel spreadsheet worker owns these updates:

- `Events!18` for ID 17 with the final Event Details wording, all three evolution detail entries, Minor Repeatable type, final status, Diplomatic Panic cluster assignment, and low member severity
- `Clusters!4` so the member list is `8, 17` in the workbook's established string format

Fields intended to match the UI must copy final in-game localisation exactly rather than paraphrasing it.

Acceptance test: read the workbook back after saving and compare the Event 17 detail and evolution cells with their localisation keys. Confirm the cluster member list remains index-aligned with the scripted cluster arrays.

## Mandatory closure evidence

These are validation gates, not requests for more mechanics.

### Core selection and AI

- Prove zero valid leaders blocks dispatch cleanly.
- Prove one, two, three, and four-or-more valid leaders yield exactly one, two, three, and four unique saved choices.
- Prove the AI resolver uses the same saved targets shown to a human and never recollects its option set.
- Permute equivalent faction leaders across option slots and confirm AI factors do not change because of slot position.
- Invalidate a saved leader before click or resolution and confirm same-country reselection or clean cancellation applies no partial join, pressure, history result, or achievement proof.

### Evolution and lifecycle

- Evolution I schedules at most one nearby response.
- Evolution II accepts a valid wartime or war-adjacent minor but rejects every direct enemy faction.
- Evolution III passes the survivor, regional-share, uniqueness, and overlapping-cascade cases above.
- Extending pressure must leave the target tracked until the final active duration ends, then remove its decisions, missions, ideas, pointers, variables, and array membership.
- External faction entry, faction departure, subject conversion, annexation, special-country conversion, faction-leader succession, and every current world-end launcher must leave no incompatible Event 017 state.
- No periodic whole-world on-action may be added.

### Decisions, localisation, assets, and achievements

- Treat `docs/plans/017_random_faction_plans/subagent_handoffs/017_random_faction_decision_mission_audit_handoff.md` as the decision closure record. The decision category and full decision file were re-read after that handoff. No missing decision family or known decision blocker remains.
- Give the variable-valued border garrison and equipment comparisons one focused integration check, as requested by the decision auditor.
- The Event 017 localisation audit passed after every mandatory finding was resolved. Run the event completion audit and resolve any mandatory finding before the plan commit.
- Read back every report image, decision and category sprite, five idea sprites, both eight-frame animations with static fallbacks, and all six achievement triplets from `interface/017_random_faction.gfx`. No additional art production is required.
- Recheck each achievement through its complete timed proof and disqualifier path. A firing or evolution unlock alone must not award it.

## Optional future depth and rejected bloat

The following items are not completion blockers unless a mandatory acceptance case exposes a concrete failure:

- replacing the working per-slot AI weights with a generic meta-effect scorer
- converting existing bounded delays to a new MTTH table
- replacing event-driven pressure cleanup with a larger generic lifecycle framework when the focused expiry cases pass
- adding country-specific prose branches, faction-template goals, bespoke faction diplomacy, or extra regional reports
- adding a custom scripted GUI, focus content, formables, country packages, super-events, or more evolution tiers
- regenerating finished art solely to create stylistic variants

Those changes would increase implementation surface without closing an accepted Event 17 promise.

## Handoff disposition

This file is a closure checklist. It does not amend the accepted source design, so no spec promotion is required. All four bounded closure blockers are resolved, and the final localisation audit passed. The final completion-audit handoff is the only remaining closure evidence not owned by this document. Event 017 should proceed to the final completion report and one plan-scoped commit only after that record is present.

This planning pass changes no gameplay, localisation, asset, specification, or workbook file. It introduces no fallback, simplification, omitted route, or substitute mechanic.
