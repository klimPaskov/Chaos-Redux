# Air Cleanliness and Fallout Implementation Status

Status reviewed against the live working tree on 2026-07-14.

Overall status: partial implementation with hard release blockers. This document does not claim that Fallout, the manual scenario, the world rewrite, or the player handoff is complete.

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Design authority

The source specifications under `docs/specs/air_cleanliness_fallout_specs/` remain authoritative. This plans directory records implementation evidence, blockers, accepted decisions, audits, and resume state. It does not narrow the source design.

Fallout remains an unnumbered system package with dedicated ownership of:

- `events/fallout_world_end_events.txt`
- the `chaosx.fallout` event namespace
- Fallout scripted effects, triggers, constants, GUI, GFX, assets, and documentation
- the blackout transition and post-Fallout rewrite
- the dormant exact-province manual scenario substrate

## Environment and proof basis

- Installed Hearts of Iron IV build inspected: 1.19.2.0
- Required offline wiki pages inspected from `paradox_wiki/`
- Official installed documentation and vanilla precedents inspected locally
- Hearts of Iron IV runtime was not launched and must not be launched for this documentation reconciliation
- Static artifacts and source inspection are evidence only, not runtime acceptance

## Live implemented foundations

### Air Cleanliness

The live Air system includes global contamination basis points, monthly host-owned updates, chemical and nuclear state inputs, natural smoke and ash pressure, threshold behavior, winter pressure, treaty behavior, nuclear fallout state intensity, UI read models, and a request path into the dedicated Fallout coordinator.

### Fallout request and blackout skeleton

The live Fallout package includes:

- `fallout_request_aftermath` and request validation
- one host-owned reconciliation path
- a versioned transition envelope with schema 4
- blackout GUI state and phase events
- player and world snapshots
- deterministic state grading and survival values
- population-loss, building-damage, category-conversion, and grade-modifier helpers
- partial old-world diplomacy cleanup
- deterministic provisional classification for eleven live government archetypes, with Machine Protocol fail closed
- player-first reservation planning
- generation-bound successor conflict inventory with country, possible-country, state, reservation, and known package-ownership rows
- schema-1 post-allocation proof contract with unique country and capital checks, exact landholder coverage, package layers, conflict receipts, and cleanup ownership
- two-pass player commit preflight for existing current-generation targets
- durable assignment recording, retry recovery, commit reconstruction, and collision validation
- strict map-return postconditions

These are foundations. The phase chain cannot yet produce a valid complete post-Fallout world.

## Dormant manual scenario substrate

The installed-build sweep proof contains 10,154 valid assigned land provinces across 1,081 states.

- 118 assigned non-land provinces are excluded.
- 126 assigned land targets in impassable states are included because no official exclusion was found.
- Batches 0 through 39 contain 250 targets each.
- Batch 40 contains 154 targets.
- The total is 41 batches.
- The ledger CSV `batch_index` uses floor division of the zero-based target position by 250 and matches the generated effects.

The event token layout is identity-bearing:

- `.900` is the bootstrap.
- `.910` through `.950` identify batches 0 through 40.
- `.960` through `.966` identify verifier attempts 0 through 6.
- `.903` is the exact countdown callback.
- The former generic `.901` and `.902` callbacks are absent.

The dormant manual runtime ledger is schema 2. Each scheduled batch, verifier, and countdown callback records the active transaction generation. Both the host validator and the hourly callback preflight reject stale or inconsistent ledgers before another native batch can run. The callback recomputes the exact issued-count-to-cursor and last-completed-batch invariants before opening the launch window. The countdown event and request wrapper independently validate the active token. Successful standard-request handoff clears both the due flag and countdown schedule provenance. Schema 1 active manual transactions fail closed.

Static control flow requires issued calls, observed callbacks, unique struck states, state strike totals, and array size to agree before aggregate consequences run. Aggregate Deaths, fallout, Air Contamination, Chaos history, condemnation, and treaty consequences then run once. The countdown end is stored as the verified start day plus seven. Only the engine-scheduled seven-day callback may submit the request. Daily reconciliation cannot submit or reconstruct it, and lost ownership or an overdue callback fails closed.

The public scenario row and dispatch are absent. The live registry ends at SCN-011. Event 20 reserves raw id 12 for Black Plague without registering a live SCN-012 row. Fallout cannot honestly allocate id 12 or claim id 13 as one greater than the live maximum.

## Runtime release boundary

Static inspection does not prove that `launch_nuke` with `use_nuke = no` emits exactly one synchronous `on_nuke_drop` callback for every scripted call. It also does not prove native acceptance for all target classes, bounded batch cost, save integrity, multiplayer synchronization, or presentation quality.

Vanilla `on_nuke_drop` schedules twelve one-day nuclear news events per callback. If all 10,154 scripted calls emit callbacks, vanilla may schedule about 121,848 one-day news event attempts. The Chaos Redux callback cannot suppress that separate vanilla branch. Callback occurrence, callback synchrony, and this news-event load are release blockers.

## Transition and migration boundary

Schema-v4 migration is fail closed:

- completed saves are promoted non-destructively
- only the exact schema-3 map-return-error signature is recovered
- every other incomplete schema 1 through 3 state remains under blackout
- an incomplete terminal state with no schema remains under blackout
- migration does not infer that a missing `fallout_transition_destructive_started` marker means an old transition is safe
- no generic pre-destructive restart and no legacy altered-grade replay are active behavior

Player reservations are calculated before the successor conflict inventory and before any successor allocation is permitted. Derived inventory schema 1 binds every row to the active transition generation. The validator checks every live country, every possible country scope, every state, exact candidate and reservation membership, human ownership and control, known overlapping event-package ownership, and capital consistency. A proposed target is commit-ready only when it already exists, has country and focus packages from the current transition generation, owns survivable territory, and owns and controls the exact capital reserved for that player. A global two-pass preflight validates all existing commits and proposed targets before any player switch. Exact single-error signatures can re-enter the inventory builder or player commit path for a clean retry. Other errors retain ownership of the transition ledger.

The government classifier aggregates frozen Fallout snapshot inputs before ownership changes. Eleven archetypes are live. Machine Protocol requires machine-continuity, command-network, EMP-survival, technical-state, and remote-refuge evidence, and remains unreachable until the missing producers exist. The classifier does not change politics or activate content.

The conflict inventory is not an allocator. It does not choose tags, final package layers, conflict results, or cleanup owners. Its known package-ownership helper must be reviewed again against the live repository before ownership changes begin. The separate post-allocation proof requires unique assigned countries and capitals, exact live-landholder coverage, current package generations, and conflict and cleanup receipts. Its guarded finalizer is the only setter for `fallout_successor_allocation_complete`, but no active allocator calls it or produces the required rows.

The commit path writes a durable assignment origin and generation before an optional `change_tag_from`, commits only after the target appears human controlled, and rebuilds and revalidates persisted commits on retry. This can commit an uncommitted player to an already materialized, current-generation target.

Actual successor materialization, country and focus package producers, candidate-choice UI, and general successor allocation are not implemented. The code can set `fallout_player_materialization_required`, but it cannot resolve it. Package and focus generations remain mandatory for every commit and map-return validation.

Static inspection cannot prove that `change_tag_from` makes the destination report `is_ai = no` immediately in the same effect chain. No Hearts of Iron IV run was authorized, so this immediate observation remains a runtime blocker.

The old-world diplomacy proof gate also remains unresolved. Map return must stay blocked until all required postconditions are genuinely satisfied.

## Hard release blockers

1. Resolve the SCN-012 ownership conflict and register a truthful public Fallout row and dispatch only after a valid next id exists.
2. Prove native strike acceptance, one callback per call, callback timing, performance, save behavior, and multiplayer behavior in a separately authorized runtime pass.
3. Resolve the possible 121,848 vanilla news-event attempts without reducing the exact 10,154-target requirement.
4. Implement general successor allocation and the country and focus package producers, including current transition generation ledgers. Re-audit every live event-package producer before the first state transfer or tag materialization.
5. Implement player-successor materialization, candidate selection and choice UI, and collision-safe multiplayer handling where the source spec requires them. Prove the immediate `change_tag_from` handoff observation in an authorized runtime pass.
6. Complete and prove the old-world diplomacy reset surfaces.
7. Close the tracked blackout input, scripted-GUI binding, all-resolution drawing-order, and mapmode frame gates.
8. Finish regional successor content, focus content, AI, localisation, assets, documentation alignment, and the required audits.

## Resume map

- Exact sweep proof: `FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md`
- Manual scenario contract and release gates: `MANUAL_FALLOUT_SCENARIO_PLAN.md`
- Current hard blockers and accepted decisions: `BLOCKERS_AND_DECISIONS.md`
- Transition ordering and postconditions: `FALLOUT_TRANSITION_ARCHITECTURE.md`
- Source-of-truth routing: `SOURCE_OF_TRUTH_RECONCILIATION.md`
- Implementation tranches: `IMPLEMENTATION_TRANCHE_PLAN.md`
- Gameplay status for Air Cleanliness: `docs/systems/air_contamination_mechanic.md`
- Manual runtime constants: `common/script_constants/fallout_manual_scenario_constants.txt`
- Manual sweep effects: `common/scripted_effects/fallout_manual_province_sweep_effects.txt`
- Manual coordinator effects: `common/scripted_effects/fallout_manual_scenario_effects.txt`
- Fallout transition effects: `common/scripted_effects/fallout_world_end_effects.txt`
- Fallout postcondition triggers: `common/scripted_triggers/fallout_world_end_triggers.txt`
- Fallout event tokens and phase events: `events/fallout_world_end_events.txt`

## Simplifications and fallbacks

No fallback is approved. The exact province sweep, seven-day delay, full successor rewrite, player continuation, and postcondition-gated map return remain required. Missing work is reported as blocked rather than presented as complete.
