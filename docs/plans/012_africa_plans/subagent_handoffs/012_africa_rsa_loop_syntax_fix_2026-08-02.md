# Event 012 RSA loop syntax repair — 2026-08-02

## Scope

The South Africa Allied-rupture package already enters through the canonical Event 12 dispatcher and owns its civil-war, intervention, peace-settlement, and exile-recovery lifecycle. This tranche changes only cleanup-loop syntax in `common/scripted_effects/012_africa_rsa_effects.txt`.

## Finding

Vanilla `for_each_scope_loop` accepts the array and loop effects, but does not document a direct `limit` field. The affected RSA cleanup and host-transfer loops therefore place their existence and exclusion predicates inside an ordinary `if = { limit = { ... } ... }` effect, which is the supported form.

## Acceptance evidence

- The RSA effects file remains balanced at 757 opening and 757 closing braces.
- No unsupported `<=` or `>=` operators were introduced.
- The loops still release only the intended Event 12 members and copy only surviving state into the selected exile patron.
- No tags, states, cores, portraits, models, or world-order packages changed.

## Remaining validation

Live civil-war, capitulation, pairwise settlement, and exile-recovery replay remains parent-owned and must be checked in a game session. The package still intentionally requires the original player-led SAF, Allied framework, supported autonomy, frozen contact patron, and current-map state gates.
