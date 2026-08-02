# Event 012 Scramble census priority repair

## Scope

This tranche hardens the one-time post-unification Scramble participant census in `common/scripted_effects/012_africa_world_order_effects.txt`.

The existing participant cap remains the single bounded roster store, and no new country tag, recurring world scan, model, or fallback war was added.

## Runtime change

`africa_initialize_scramble_and_world_packages` now performs two bounded sweeps inside the same explicit census.

The first sweep admits eligible non-African countries that pass `africa_ai_scramble_expedition_materially_ready`, which requires a deployable army, available manpower, and a controlled coastal naval base.

The second sweep admits the remaining eligible majors, faction leaders, and current African-state interest holders until the existing `constant:africa_scramble_response.participant_census_cap` is reached.

`africa_scramble_register_participant` remains the sole registration kernel, so duplicate flags, class arrays, counters, response events, and cleanup behavior are unchanged.

## Acceptance impact

This closes the source-level rank-starvation defect where iteration order could fill the capped roster with recognition or sanctions contacts before any materially ready expedition actor was registered.

Recognition, sanctions, ultimatums, treaty pressure, South Africa or Allied contacts, and rivalry classes still use the same frozen participant arrays and flags after registration.

The material predicate remains a capability gate for expedition planning and launch; it does not force a war or turn every capable country into an intervention actor.

## Validation

Event Chain Viewer lint for `chaosx.nr12.1` returned `status=ok`, `blockers=[]`, and `blockingDiagnostics=0` after the patch.

The report remains `EVENT_INSPECTED_PARTIAL` because the large-workspace helper and lifecycle projection is deferred, so campaign and live scenario acceptance remain open.

No new tags or models were created, and no portrait consumer was changed by this tranche.

## Remaining gates

The six-slot census is still intentionally bounded and does not certify multi-power coalition balance, naval distance, supply, or campaign outcomes.

W5 continent-package receipts, live Scramble scenarios, achievement disqualifier proof, two missing super-event audio roles, external continent identities, and the remaining controlled-pool surfaces remain open in the acceptance ledger.
