# Chaos Meter Combat, Contamination, and Occupation Deaths

## What This Adds

This update expands the `Deaths` system so civilian losses are now tracked from three additional sources:

1. active frontline combat behavior,
2. ongoing contaminated-state exposure,
3. occupation-law severity in occupied states.

These losses are added into the same global death toll and continue to feed chaos through the existing rule:

- every `1,000,000` tracked deaths adds `+1` chaos.

## Combat Civilian Casualties

Combat now generates civilian deaths while fighting is active.

Behavior:

1. The system checks army leaders that currently have offensive units in combat.
2. It picks a random enemy frontline state where that leader is actively fighting.
3. It applies a state-population-based civilian death loss there.
4. The trigger itself is random, so democratic countries only cause this rarely while harsher regimes do it much more often.
5. The death rate is ideology-based:
   - fascist: highest baseline,
   - communist: lower,
   - non-aligned: very low,
   - democratic: extremely low.
6. If the country has `chaos_warfare`, an additional combat civilian-death rate and trigger bonus are added on top.
7. Higher chaos tiers now scale the combat death rate upward.

Result:

- `chaos_warfare` + ideology rates stack additively.
- The deaths are registered as civilian and reduce state population directly.
- This pass is now materially stronger than the previous tuning.

## Contaminated-State Monthly Death Ticks

Monthly contaminated-state deaths are now population-percentage based instead of flat values.

### Chemical Contamination

- Chemical contamination applies a very low monthly civilian death percentage.

### Biowarfare Outbreaks

- Outbreak states apply higher death percentages.
- Deadlier outbreaks apply stronger monthly death percentages.
- These death rates are now stronger than before.

Severity order:

- anthrax (lower),
- tularemia (mid),
- plague (high),
- smallpox (highest).

Mitigation:

- Existing outbreak prevention systems now reduce these monthly deaths:
  - outbreak-prevention tech tiers,
  - quarantine protocols and border-closure prevention,
  - active state-level contamination defense effectiveness (quarantine, medical/vaccination protections, etc).

## Occupation-Law Civilian Deaths

Occupied states now apply monthly civilian deaths based on occupation-law harshness.

Rules:

1. Only occupied states are checked.
2. Harsher laws produce higher civilian death percentages.
3. `concentration` is the harshest and produces the highest death rate.

This creates a direct death-toll consequence for repression-heavy occupation policy.

## Zombie-Controlled State Decay

Zombie-controlled states now use a separate long-form collapse mechanic documented in `docs/zombie_state_decay_and_civilian_deaths.md`.

Summary:

- `0.5%` monthly population loss for up to `36` months per state,
- one structural degradation pass every `180` days,
- deaths feed the same chaos-meter pipeline under the cause `Zombie occupation collapse`.

## Air Contamination Modifier Visibility

The global air contamination country modifier is now hidden from the visible spirit list by removing its icon binding.

Gameplay effects remain active; only the visible spirit card is suppressed.

## Icons and GFX Wiring

No new sprites are required.

This update reuses existing chaos meter UI elements and log entry styling.

If custom icons are desired later, place them in:

- `gfx/interface/`

and register them in:

- `interface/chaosx.gfx`

## Future Plans

1. Add detailed attribution for combat civilian casualties (attacker/defender split in details view).
2. Add dedicated deaths-log filtering by cause family (combat, contamination, occupation).
3. Add occupation-law counterplay decisions that trade compliance/output for lower civilian deaths.
4. Add per-region humanitarian pressure events that react to high sustained civilian death rates.
