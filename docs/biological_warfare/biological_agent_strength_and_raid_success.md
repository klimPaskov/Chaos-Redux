# Biological Agent Strength and Raid Success

## Canonical hierarchy

Ordinary biological weapon strength follows `Tularemia < Anthrax < Plague < Smallpox`.

Tularemia is low severity with a 0.85 canonical lifecycle-strength multiplier.

Anthrax is moderate severity with a 1.00 multiplier.

Plague is serious with a 1.15 multiplier.

Smallpox is severe with a 1.30 multiplier.

Only Smallpox belongs to the severe weapon tier.

The hierarchy is applied inside `bio_lifecycle_finalize_seed_values`, after the operational result is loaded and before weaponization quality and Chaos Warfare doctrine are applied.

This keeps every ordinary delivery route on one potency model while preserving agent-specific incubation, growth, spread, detection, persistence, countermeasure, medical-load, and mortality behavior.

## Delivery probability boundary

Agent potency does not determine raid delivery success.

All four strategic biological raids use a 0.50 native success base, 0.12 critical-success base, and 0.10 disaster base.

All four battlefield biological raids use a 0.50 native success base.

Verified aircraft, assigned formations, intelligence, air defence, interception, radar, reliability, Headquarters preparation, doctrine, and other supported operational conditions may modify the result where the native raid schema allows them.

Agent identity does not modify the base probability.

Agent-specific AI weights describe strategic willingness and preferred use, not a different chance of delivery.

## Operational results and severity

The lifecycle result identifies delivery quality.

The canonical agent profile identifies weapon severity.

The existing internal `catastrophic` result token is the critical operational-result multiplier used by ordinary raids and does not promote a lower agent into the severe tier.

The doomsday route uses the successful-release result for Tularemia, Anthrax, and Plague.

Smallpox alone uses the severe doomsday result.

## Mortality and medical pressure

The low, serious, and catastrophic weekly exposed-population death bands rise strictly through the canonical hierarchy.

Medical pressure per point of active intensity also rises strictly from Tularemia through Smallpox.

Agent-specific treatment sensitivity and spread remain distinct, so a lower-tier agent can still be operationally disruptive without exceeding a higher-tier agent’s overall weapon strength.

## Assets and wiring

No asset was created, resized, replaced, or used as a cross-type substitute for this balance correction.

Strategic and battlefield biological raids continue to reuse the existing registered Chaos Redux sprites under `gfx/interface/military_raids/`.

The raid sprite registrations remain in `interface/chaosx_raids.gfx`.

## Future plans

The final package audit should compare every raid, operation, decision, accident, and historical campaign caller against this canonical hierarchy.

That audit may preserve route-specific release quantities and AI preferences, but it must not introduce agent-specific native raid success probabilities or classify a non-Smallpox agent as severe.
