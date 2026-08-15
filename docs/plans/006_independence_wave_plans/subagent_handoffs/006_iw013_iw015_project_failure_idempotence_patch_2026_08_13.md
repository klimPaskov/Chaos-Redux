# IW-013/IW-015 project-failure idempotence patch

Date: 2026-08-13.

## Scope

The Iberian NAV and GLC paid-project cancellation effects now refuse to apply the generic project-failure penalty after their founding compact mission has already marked the compact crisis as failed.

This closes the race in which founding-mission timeout or cancellation applies the failure deltas and an active paid project cancellation applies the same package penalty again in the same lifecycle transition.

The guard is limited to the cancellation effect; normal project failure before compact failure still applies the existing package-specific deltas.

## Source change

`common/decisions/006_independence_wave_iberian_decisions.txt` adds the matching `NOT = { has_country_flag = independence_wave_nav_compact_crisis_failed }` or GLC equivalent to all twenty timed NAV/GLC project `cancel_effect` limits.

The founding missions still set their package failure flag and apply the bounded failure effect exactly once.

No central content-attestation, adapter, Join, allocator, flag, portrait, or formable gate was widened.

## Validation

The source scan finds ten NAV and ten GLC guarded cancellation effects, with no remaining unguarded Iberian timed-project cancellation effect.

The existing NAV decision, localisation, portrait, flag, and probability handoffs remain authoritative for the separate admission gates.

The mandatory post-change `hoi4.probability_inspect` on `common/decisions/006_independence_wave_iberian_decisions.txt` with `mission_ai_will_do` returned `PROBABILITY_SOURCE_INSPECTED` at source hash `42753b8bc65f5cbd1b49b30dedc2e40f366ceabf766e8cb9b9e40879f8846ef6`, source revision `5a316510b35db5b50c66ebc4d2d42b0d4ceb8bd3622b286459fec4ef1f8e0b1e`, with 22 candidates, 12 required inputs, zero inspect-unresolved items, and an incomplete pool with zero available candidates; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/850e27dbd5030a70a36bbb43e789445e29539f5cb39b80babb64feda0f0c9c24/fb00bc76fdc2d251236dc948a403a794059b88d83ca006812b1ce1496cad8388/probability-inspect-42753b8bc65f.json`.

This lifecycle-only guard does not change any mission AI score or candidate weight, so no balance comparison is claimed; central package admission remains fail-closed.

No live game, save/load, or runtime transaction validation was performed.
