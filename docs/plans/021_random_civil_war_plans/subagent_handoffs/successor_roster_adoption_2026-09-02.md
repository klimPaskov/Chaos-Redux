# Event 021 successor roster adoption handoff

Status: implemented within the exclusive successor-helper scope on 2026-09-02.

This tranche adds reusable same-crisis preparation/adoption logic only. It does not establish war continuity and does not edit existing gameplay files.

## Files changed

- `common/scripted_effects/021_random_civil_war_successor_effects.txt`
- `common/scripted_effects/021_random_civil_war_successor_effects.md`
- `common/scripted_triggers/021_random_civil_war_successor_triggers.txt`
- `docs/plans/021_random_civil_war_plans/subagent_handoffs/successor_roster_adoption_2026-09-02.md`

No existing parent, lifecycle, Event 006, on-action, constants, GUI, asset, or call-site file was edited. No commit was created.

## Helper map

`event021_prepare_successor_roster_adoption` is a COUNTRY-scope before-annex effect. It requires the explicit chain-local `event021_history_predecessor` target, a distinct living normal-human same-crisis government predecessor, and the promoted successor's explicit host pointer to that target. It snapshots successor/predecessor/expected-host targets, the crisis receipt, host counters, and host multifront role flags, then builds a bounded provisional roster.

`event021_adopt_successor_roster` is a ROOT/successor after-annex effect. It requires the pending receipts, matching crisis receipt, the chain-local preparation target, and `event021_lifecycle_successor` resolving to the current ROOT with the same crisis id. It adopts active/government host roles, clears the successor's opposition role, normalizes host pointers to itself, clears only a self-opponent pointer, rebuilds the local unresolved actor roster, saves a chain-local completion target, clears the transient crisis receipt, and closes the pending transaction.

`event021_rebuild_successor_roster` is an internal effect. It loops backward over `global.random_civil_war_front_ids^num`, gates each row by matching crisis id and active status, proves the optional front-host or actor-host link, filters live actor role/registry receipts, and appends each candidate once. It never changes the global front arrays, active-theater rows, cursors, or counts.

`event021_successor_adoption_context_valid` proves the before-annex ROOT/FROM transaction.

`event021_successor_adoption_after_annex_valid` requires the current lifecycle successor witness and its same-chain `event021_lifecycle_successor_transfer = one` latch rather than inferring current proof from saved-target presence.

`event021_successor_roster_actor_valid` excludes missing/dead/capitulated, nonhuman, self, and different-crisis actors while retaining valid Event 006 actors without changing their package identity. A separate internal-front completion receipt does not exclude an actor whose current row and role remain active.

## Exact caller obligations

1. The parent must bind `event021_history_predecessor` to the explicit predecessor before the before-annex helper. A history receipt or unrelated global host pointer is not a substitute.

2. The before helper must run after the parent's ordinary same-crisis successor proof and before white peace or annexation. The predecessor's crisis id, government role, host role, front rows, and transfer target must remain available through `on_annex`.

3. Any required war-transfer operation must occur before the predecessor's war relations are destroyed. The successor helpers contain no war effect.

4. In the vanilla `on_annex` contract ROOT is the winner/annexer and FROM is the disappearing country. The parent recognition/preparation path must prove ordinary opposition winner, explicit host pointer to FROM, and equal nonmissing crisis ids.

5. The lifecycle order must be `FROM = { event021_handle_annexed_country = yes }` before predecessor cleanup or receipt clearing.

6. The parent must call `event021_adopt_successor_roster = yes` immediately after that lifecycle call in ROOT. If the current lifecycle witness is unavailable, the helper intentionally skips instead of accepting a stale local target.

7. A zero adopted actor count is a valid bounded result, but the parent must not launch multifront logic from a missing `random_civil_war_opposition_actor_scope`; it needs an explicit settlement/closure path.

8. The lifecycle helper owns aligned global front-row rebinding/removal and cursor/count repair. This helper does not certify that the successor's own actor row, if still present in the global ledger, should be settled or unregistered.

9. The parent must preserve Event 006 package identity and the durable `random_civil_war_event6_origin_recorded` marker. This helper neither copies nor clears Event 006 identity/origin variables; transient `random_civil_war_event6_origin` remains lifecycle-owned.

10. If preparation is abandoned before annexation, the parent must clear `random_civil_war_successor_roster_pending`, `random_civil_war_successor_government_role_pending`, and `random_civil_war_successor_adoption_crisis_id`; the chain-local event targets expire automatically.

## Array and idempotence proof

The worker uses `global.random_civil_war_front_ids^num` as its only iteration bound, so it does not scan the world. It reads `front_ids` and `front_actors` at the same row index and requires the actor's live `random_civil_war_front_id` to equal the row id before using the actor's live crisis id as the current writer contract. A present `front_crisis_ids` row is an additional aligned witness and must match; a missing or short optional crisis array does not invalidate a live actor row. Optional `front_hosts` and `front_statuses` are read at the same row index.

Rows with a present non-active status are skipped. A short or missing status row is treated as unresolved so partially initialized ledgers are not silently erased. Every candidate must still have a live `random_civil_war_front_registered` receipt, a registered front id, and an actor-side same-crisis host pointer or matching front-host row.

The successor's local opposition array is cleared only inside an authorized, non-completed transaction and every append is guarded with `is_in_array`. Repeating the parent call after preparation or adoption is blocked by chain-local event-target receipts; repeated candidate rows cannot duplicate the roster and no recurrence-sticky adoption flag is created.

The current successor is explicitly excluded from its own opposition roster. Other valid same-crisis actors are rebound to the successor after annex when their surviving row proves the transfer and an actor host pointer still needs repair.

## War continuity blocker

Source review proves Event 021 uses actual wars through `start_civil_war`, `declare_war_on`, `has_war_with`, and explicit `white_peace`, but does not prove automatic inheritance of remaining wars through `annex_country`.

The installed vanilla effects documentation documents `annex_country` with optional troop transfer and separately documents `add_to_war` and `declare_war_on`; it does not document annexation as a war-roster transfer. Event 021's external-war boolean and single immediate-opponent pointer cannot identify every enemy.

The parent therefore still owns a bounded pre-annex enemy snapshot, explicit war handoff/recreation in the correct context, and post-annex `has_war_with` checks. Registry rebinding, `transfer_troops = yes`, and a historical external-war flag are not war-continuity evidence.

## Evidence and validation

The required offline wiki pages for data structures, scopes, triggers, effects, and on actions were consulted, including event targets, array effects, scope persistence, and the ROOT/FROM `on_annex` contract.

The installed vanilla `effects_documentation.md` and `triggers_documentation.md` were consulted for `save_event_target_as`, arrays, bounded loops, `annex_country`, `add_to_war`, `declare_war_on`, `white_peace`, and `has_event_target`.

The post-edit narrow read-only `hoi4.event_inspect` lint for `chaosx.nr21.1` completed as `EVENT_INSPECTED_PARTIAL` with revision `65f53c2f4a099c16d11d6ab9960f409df2c881e6ad4b02f663cc098b6d5137bd`, graph hash `55dcd8960c2bd627731619ebee30060c151e6e8594bde4b0bc9a750493a67657`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80cbc4cdd5836bb4ff83237315ddf4cf19c8d2603f694f3e6de42713a4d5845e/5a03640746f7cfcd809756d54825c5e73b37de36ac8bf367c1b086fa63e3c3f1/event-lint-65f53c2f4a09.json`.

That MCP result was partial because the large workspace returned truncated inline sources and deferred helper/lifecycle projections; it had zero blocking diagnostics. No timeout occurred in this bounded inspection.

Post-edit validation will check the four new files for balanced Clausewitz blocks, required helper/trigger identifiers, absence of forbidden war effects and world iterators, and a clean changed-file boundary. Live game execution and save validation remain parent/user responsibilities.

## Limitations and follow-up

No weighted or probability-bearing helper was added, so no probability inspection or balance choice was applicable.

No front metadata repair, war declaration, annexation, white peace, Event 006 cleanup, recurrence reset, history reset, constant, GUI, asset, or existing call-site change was made.

The parent must integrate the exact before/after sequence and independently certify surviving actual wars and natural-engine annexation behavior.
