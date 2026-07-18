# Fallout scheduler numerical-contract implementation handoff

Status: incomplete and dormant. This handoff records the scripted numerical
substrate only. It does not claim the accepted Fallout event scheduler or the
full Fallout living-world goal is complete. No gameplay caller was activated,
no new on-action/world iterator was added, and no HOI4 runtime execution was
performed.

## Owned files changed

- `common/script_constants/fallout_world_end_event_constants.txt`
  - Added typed scheduler enums for country size, phase mode, repeatability,
    crisis breaks, Air Winter, and pressure provenance.
  - Added phase-by-frozen-size cooldown table, inclusive AI registry-count
    batch thresholds (1-30/31-60/61-90/91+), score/tie tuning, fatigue,
    pressure, crisis-break, due-date, budget, and player-relevance constants.
  - Advanced empty-only compact child-ledger schemas to v3 and ordinary
    receipts to v2 with explicit previous-empty versions.

- `common/scripted_triggers/fallout_world_end_event_triggers.txt`
  - Added current-runtime schema-3 empty-row migration proof and old
    global-ready v1 empty ordinary-receipt re-promotion proof.
  - Added candidate source/pressure provenance, bounded required/match booleans,
    composite identity and independent transaction-key uniqueness, parent-arc
    identity/actor checks, typed control-mode/cost checks, deterministic
    player relevance (100 current human, 50 authenticated human bilateral
    partner, otherwise 0),
    bilateral pair/family 90-day memory, and current partner survival/runtime
    proof.
  - Added an explicit fail-closed eligibility gate for `major_arc` and
    `relationship` candidates until their typed atomic reserve payloads exist.
  - Added the index-zero fatigue invariant (`family_fatigue_entries^0 = 0`).

- `common/scripted_effects/fallout_world_end_event_effects.txt`
  - Added fatigue decay using the shared decay constant while preserving the
    zero family slot. Opening fatigue/history is applied only after an issued
    ordinary receipt is current.
  - Added deterministic cooldown, pressure normalization, scoring, tie-break,
    selection, and commit helpers. Commit-time crisis-break and broadcast
    receipts are generation/day/ticket idempotent.
  - Added frozen control-mode fields to ordinary, arc, delayed, and bilateral
    ledgers. New child reservations authenticate current control mode while
    exact retries use the frozen mode/cost receipt.
  - Added bounded human/AI review reconciliation before selection, with AI
    batch sizing from frozen registry count.
  - Added dormant old-ready ordinary-receipt re-promotion and current-runtime
    child-ledger migration effects.
  - Added bilateral pair/family memory recording after issue, guarded by a
    current partner proof. The candidate gate consumes that memory for the
    rolling 90-day check.

## Helper map and call sites

| Helper | Scope / inputs | Outputs / side effects | Main call sites |
| --- | --- | --- | --- |
| `fallout_event_calculate_base_cooldown_days` | Country with current phase and frozen size | `fallout_event_base_cooldown_days` | broadcast extension and ordinary commit |
| `fallout_event_normalize_candidate_pressure` | Country with candidate validation index | resource/Air Winter normalized pressure temps | candidate scoring |
| `fallout_event_calculate_candidate_score` | Country with candidate validation index | rounded score and score component temps | deterministic selector and commit recheck |
| `fallout_event_select_reviewed_candidate` | Country reviewed arrays | selected index/identity/score temps | human/AI review lanes |
| `fallout_event_commit_selected_candidate` | selected candidate temps | ordinary receipt, cooldown, selection receipt, crisis/broadcast commit receipts | selector |
| `fallout_event_decay_family_fatigue` | Country runtime row | family fatigue decay with slot 0 remaining zero | selector and issued-opening helper |
| `fallout_event_apply_opening_fatigue_and_history` | issued ordinary receipt | +60 fatigue once, visible history/completion memory | dispatch issue path |
| `fallout_event_record_bilateral_family_memory` | issued relationship ordinary receipt | reciprocal pair/family/day memory when both current rows prove valid | opening fatigue/history helper |
| `fallout_event_repromote_old_ready_empty_ordinary_receipts` | dormant coordinator/global registry | v1-empty to v2 receipt promotion only | scheduler reconcile |

## Migration, event-target, and cleanup plan

- Schema promotion remains empty-only and generation-bound. Current runtime v3
  migration clears only newly introduced child cost/control arrays. Ordinary
  v1 migration rewrites only exactly empty rows. Pending/nonempty rows fail
  closed. A second pass handles saves where the global ordinary-receipt-ready
  flag already existed.
- Short-lived transaction targets continue to use ordinary `save_event_target`
  semantics. No new global event target was introduced. Existing global
  broadcast receipts are cleared only by the existing uncommitted-registry
  reset path and are committed before opening issue.
- Child ledgers retain reciprocal cleanup through the existing cancellation,
  release, and reconciliation effects. Pair/family memory is durable runtime
  data and is checked by day cutoff. It is not fabricated during migration.

## Remaining blockers and unsupported surfaces

- `major_arc` and `relationship` ordinary openings are deliberately
  fail-closed. The reviewed candidate payload has no typed arc identity /
  cleanup reservation fields or bilateral reciprocal response/cleanup fields,
  so an atomic reserve-before-ordinary commit cannot be proven without a
  broader payload/schema tranche. Do not remove this gate until that tranche
  exists and both reciprocal rows are committed before dispatch.
- Pair/family memory is dormant behind that gate. It is bounded semantically by
  the 90-day eligibility cutoff, but a future activated tranche should add
  deterministic expiry compaction and a dedicated schema receipt if long-lived
  campaigns can create unbounded memory rows.
- Current capitals authenticate the recurrence exception through the documented
  state trigger. Active-siege exceptions remain fail-closed until Fallout owns
  a typed current-siege producer receipt.
- No event-specific actor reservation ledger, war/mission target surface, or
  content producer was added. Unsupported relevance surfaces remain zero and
  fail closed rather than borrowing live ownership.
- Parent added final safety fixes after interruption: restored `is_ai = no` on
  the human lane, removed the duplicate arc budget bound, added the current
  origin bilateral cap for new rows, proved fatigue index 0 is zero, retained
  fail-closed `major_arc`/`relationship` eligibility, normalized bilateral due
  checks to engine days, hardened empty promotion against every existing
  numerical memory, and authenticated the current-capital recurrence exception.

## Validation performed

- Per-line brace scans (comments/quoted text ignored) returned zero final
  balance and no negative balance for all three owned script files.
- Unsupported `<=`/`>=` operators were absent from the three owned files.
- `git diff --check` completed without whitespace errors for the owned files.
- An independent read-only completion audit found three contract defects in its
  initial pass. Parent corrected the bilateral due clock, empty promotion gate,
  and capital recurrence authentication. The focused re-audit returned no P0
  through P3 finding on those corrected surfaces or dormancy checks.
- No HOI4 executable run or live save validation was performed. Activation and
  content-level event audits remain the parent agent's responsibility.
