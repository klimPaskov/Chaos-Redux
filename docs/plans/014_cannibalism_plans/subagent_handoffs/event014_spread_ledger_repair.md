# Event 014 foreign-spread ledger repair handoff

Date: 2026-07-11  
Mode: implementation patch; no commit created  
Source audit: `event014_spread_ledger_architect_audit.md`

## Outcome

The accepted foreign-spread audit findings are implemented across the parent-owned gameplay surface. The queue now has executable alignment and row-identity validation, expected-ID mutation guards, exact per-state inbound identity, idempotent lifecycle tombstones, queue-derived cache rebuilds, physical route provenance, click-time-safe screening, narrow lifecycle hooks, and registry-derived global residue checks.

No malformed-array repair fallback was added. An invalid shape or live-row identity sets `cannibalism_spread_queue_invariant_failure`, stops indexed mutation, and also counts as global residue so cleanup cannot erase the evidence.

## Files changed

- `common/scripted_effects/014_cannibalism_spread_effects.txt`
  - added queue validation, authoritative target availability, cache rebuild, exact-ID finalization/invalidation, lifecycle invalidators, state/country reconciliation, and an ID-safe unification migration helper;
  - persisted `cannibalism_inbound_spread_id` and per-state warning snapshots;
  - restricted the automatic border producer to retreat;
  - added the real `on_naval_invasion` convoy producer;
  - split control-change recovery from occupation-turnover production;
  - corrected deliberate-seed and survivor source/target state pairs;
  - replaced unguarded screening payments with guarded `try_...` effects;
  - used a file-scoped 45-day automatic-route cooldown literal.
- `common/scripted_triggers/014_cannibalism_spread_triggers.txt`
  - added nine-array alignment, live-status, route-range, route-specific source-state, exact loaded-row, warning-instance, and inclusive affordability predicates;
  - changed spread recovery exclusion to active recovery only, allowing stabilized states to be reinfected.
- `common/scripted_effects/014_cannibalism_country_effects.txt`
  - replaced direct nine-array deletion with the canonical lifecycle invalidator before incarnation reset;
  - quarantines slot release when the queue invariant is invalid;
  - places a warlord created after public reveal into `cannibalism_pending_absorption` and the convergence response roster, then queues `.71`.
- `common/scripted_effects/014_cannibalism_core_effects.txt`
  - delegates pending-spread cache rebuild to the validated queue helper;
  - uses a file-scoped 180-day reinfection-protection literal;
  - calls `cannibalism_process_wendigo_transformation_pulse` only from the registered Event 014 actor pulse for the merged Wendigo-Hannibal actor.
- `common/scripted_triggers/014_cannibalism_triggers.txt`
  - derives recurring residue from compacted registries/counts rather than `any_country`/`any_state` scans;
  - treats the invariant-failure flag as residue;
  - permits only the public merged Wendigo-Hannibal owner through the otherwise nonhuman Larder exclusion.
- `common/on_actions/014_cannibalism_on_actions.txt`
  - added lifecycle invalidation/reconciliation for capitulation, annexation, civil-war consolidation, puppet creation, release, subject freedom, and subject annexation;
  - invalidates state rows before state-control recovery/route handling;
  - added the documented `on_naval_invasion` adapter.
- `common/decisions/014_cannibalism_spread_decisions.txt`
  - changed both targets to `any_controlled_state`;
  - kept target discovery independent of affordability;
  - routed completion through the guarded expected-ID effects.
- `events/014_cannibalism.txt`
  - changed only `.60`: it opens a state-scoped warning snapshot, passes its expected ID to guarded screening, and closes only that warning instance.

## Canonical queue and lifecycle contracts

### Validation

`cannibalism_validate_spread_queue` is the mandatory precondition for indexed mutation. It verifies:

1. all nine array lengths are equal;
2. each row has a positive ID, positive scope payloads/source generation/due date, a route from 1 through 8, and a recognized status;
3. every live row loads all four scopes without reusing a stale regular event target;
4. every live target state has exact ID, route, source-country, and source-generation metadata;
5. live IDs and live target states are unique;
6. a terminal row cannot be compacted while its own inbound ID is still cached on the target state.

### Canonical invalidation

`cannibalism_invalidate_loaded_spread_entry` accepts `cannibalism_spread_queue_index` and `cannibalism_expected_spread_id`. It re-reads the ID, accepts only queued/in-transit status, writes `invalidated` before clearing, clears exact state/country/global ledgers once, and never removes an index. `cannibalism_compact_spread_queue` is the sole physical row remover and removes all nine arrays from the end after a fresh validation.

### Unification migration handoff

The unification owner must replace its raw spread-array loop with:

```txt
cannibalism_migrate_spread_entries_between_countries = yes
```

Required regular event targets:

- `cannibalism_runtime_migration_source_country`: old/absorbed actor;
- `cannibalism_runtime_migration_destination_country`: unified destination.

Required destination state:

- it exists;
- it has positive `cannibalism_actor_generation`.

Output:

- temp `cannibalism_spread_migration_result = 1` only after live source country/generation references, exact target-state source metadata, live target-country references, and all caches are updated and revalidated.

No tenth target-generation array was introduced. Target-incarnation safety remains the combined contract of narrow country lifecycle invalidation, state control invalidation, exact state inbound ID, target-controller revalidation at resolution, and release/puppet reconciliation. The migration helper updates target-country rows before the absorbed identity is retired.

## Acceptance-scenario proof

| # | Structural outcome |
|---:|---|
| 1 | Enqueue increments target count per row; canonical clear decrements once; the warning flag clears only at zero; the validated rebuild derives the same count from live rows. |
| 2 | Enqueue requires both authoritative live-row count zero and clean state metadata; live-row validation also rejects duplicate target states. |
| 3 | Reusable-tag retirement calls lifecycle invalidation before reset, clears the remote state/country ledgers once, and leaves terminal rows for later compaction. |
| 4 | Capitulation, annex, civil-war, puppet, release, subject-free, and subject-annexed hooks invalidate/reconcile rows before identity reuse. |
| 5 | Unequal arrays fail the alignment trigger before indexed access, set the invariant flag, and are neither compacted nor cleared. Context-loaded flags prevent reuse of prior regular event targets. |
| 6 | Convoy assignment exists only in the invaded-state helper called by `on_naval_invasion`; it records ROOT, FROM, THIS, and THIS's controller and requires a live ROOT port/island node. |
| 7 | Volunteer-return assignment remains only in the recalled-volunteer helper; the generic border producer always assigns retreat. |
| 8 | Occupation and conquest assignments remain only in state-control handlers. Recovery runs first and does not require the old source to remain at war or uncapitulated; occupation enqueue does. |
| 9 | Survivor selection chooses the target directly from the selected source state's neighbors. Spread target filters exclude active recovery, not the terminal stabilized marker. |
| 10 | Screening revalidates expected ID, live row, exact metadata, controller, unscreened state, warning snapshot when open, and full affordability inside one outer limit before deduction. |
| 11 | Manpower, command power, support equipment, and convoy checks use `greater_than_or_equals`. |
| 12 | Both decisions use `any_controlled_state`; recurring residue uses rebuilt actor/node/recovery/spread/convergence/anchor registries and counts. |
| 13 | No warning/arrival localisation or event text was changed, so existing pre-reveal identity gating remains intact. |

## Localisation requests for the parent owner

No localisation file was edited under this task's ownership boundary. The two audited P3 strings still need an in-world wording pass:

- `cannibalism_humane_route_screening_effect_tt`: remove “active Event 14 response”; describe reception teams, supervised transfer, and containment of the active domestic route.
- `cannibalism_seed_foreign_formation_effect_tt`: remove “Queues one generation-checked” and “Event 14 cell”; describe dispatching a formation along a verified land or sea route and the risk of a predatory cell taking root if it is not contained.

## Validation notes

- All nine queue arrays have exactly one append site and one physical removal site in the spread owner.
- Every indexed runtime consumer is behind the aligned-row validator; fixed-tag direct deletion no longer exists.
- Route assignment review found one producer per required action family: retreat/border, prisoner operation, naval invasion, volunteer recall, occupation control change, deliberate operation, conquest control change, and adjacent survivors.
- The eight touched script/event files have balanced blocks and tab-only indentation.
- No daily, weekly, or monthly on-action was introduced.

## Simplifications, omissions, and blockers

No fallback, placeholder, route omission, hardcoded variable-duration token, or gameplay simplification was used. The only cross-owner integration action is replacing the raw unification spread loop with the migration helper above. The two P3 localisation rewrites remain intentionally assigned to the localisation owner.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`.
