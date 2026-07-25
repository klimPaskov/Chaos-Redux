# The Ammunition Winter

## Acceptance role

The Ammunition Winter is a dormant Fallout global-survival chain for the first winter after the world-end rewrite. It is not an Air Winter opening and it does not open either Fallout scheduler activation flag. The candidate producer adds one generation-bound state row only when a country has a low military equipment stockpile and an active threat through war or elevated winter crime pressure.

## Native target contract

The candidate selects the lowest owned state id that has a current produced Air Winter snapshot, durable Fallout state identity and resource rows, an exposed Air Winter value from 25 through 99, at least 80 thousand people, at least 10 Supply Access, and a valid rural, town, large-town, or city category. The target is stored as a state subject and re-authenticated before every delayed lane. No invented province, supply node, tag, or neighbour is created.

## Four authored policies

1. `reduce_patrols` shortens patrol routes around wells and the depot. It spends a small amount of Fuel, raises defence around the state, and leaves outer roads exposed when the result is partial or failed.
2. `melt_civilian_metal` converts rail fittings, stove plates, and farm tools into a small arms run. It spends Fuel and Scrap, improves Army Experience when successful, and carries an industrial accident risk.
3. `trade_food` sends winter food to a river market for cartridges. It spends Food and Recognition, changes Stability and War Support, and creates a concrete trade memory.
4. `seize_private_arms` registers and confiscates household weapons. It spends Recognition, changes militia alignment and civic trust, and can create future crime pressure when the seizure becomes a raid.

Each policy has human and hidden-AI lanes. The result is reserved for 60 days and graded deterministically from Supply Access, cohesion, War Support, Army Experience, arms readiness, Air Winter exposure, and crime pressure. Success, partial, and failure apply distinct resources, military modifiers, state Supply Access, Air Winter reclamation and exposure, cause memory, building damage, and Deaths-backed loss. A callback is reserved 180 days after the result, applies a second deterministic grade, writes a second Event Log payload, and releases both delayed receipts through one hidden cleanup event.

## Durable ledgers

The country stores arms readiness, crime pressure, civic trust, militia alignment, and a cause-memory code. The state stores the committed receipt flag and the existing Air Winter ledger. Cleanup clears only the transaction receipt and temporary frozen values. The five country ledgers survive candidate rebuilds so the chain cannot erase its own memory.

## Engine surfaces and evidence

The chain uses the established Fallout ordinary receipt, delayed-result, hidden-AI, delayed-cleanup, owner-bound state target, `var:` state scope, dynamic modifier, `apply_exact_state_civilian_population_loss`, `damage_building`, and Event Log history routes already proven by the preceding reviewed chains. Its new engine-sensitive surfaces are the low-equipment gate and the `has_war` or crime-pressure threat gate. Static source review confirms both are evaluated in country scope before the state row is appended. Runtime event issuance, popup ordering, multiplayer behavior, and save recovery remain unobserved because HOI4 was not launched.

## IDs and assets

The chain owns event ids `chaosx.fallout.534` through `chaosx.fallout.540`, candidate id `534`, transaction key `710050`, route `7150`, and Event Log history `9155`. Its dedicated sprite is `GFX_report_event_fallout_ammunition_winter`, backed by `gfx/event_pictures/fallout_world_end/report_event_fallout_ammunition_winter.dds` and the source manifest at `docs/assets/air_cleanliness_fallout/fallout_ammunition_winter/manifest.md`.

## Review boundary

This tranche is implemented and dormant. It is not release-floor credit until the Fallout scheduler activation proof, human review, hidden-AI review, Event Log presentation, and runtime receipt behavior are accepted. The exact engine-native manual all-valid-province thermonuclear sweep remains a separate blocker.
