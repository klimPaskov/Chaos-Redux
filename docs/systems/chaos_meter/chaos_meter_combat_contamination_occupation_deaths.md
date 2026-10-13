# Chaos Meter Combat, Contamination, and Occupation Deaths

## What This Adds

This update expands the `Deaths` system so civilian losses are now tracked from three additional sources:

1. active frontline combat behavior,
2. ongoing contaminated-state exposure,
3. occupation-law severity in occupied states.

These losses are added into the same global death toll and continue to feed chaos through the existing rule:

- every `1,000,000` weighted civilian deaths adds `+1` chaos, with military losses using their direct casualty scale.

## Combat Civilian Casualties

The existing `on_army_leader_daily` callback calls `chaos_meter_on_combat_civilian_casualties` when the Chaos Meter and Deaths systems are enabled.
The army leader must have offensive combat and a valid human owner at war.
The complete pre-6c266388b callback evaluates ideology, Chaos Warfare doctrine, and Chaos tier, then draws its historical trigger chance.
A successful roll scans the leader's units in controlled frontline states through the supported `num_units_in_state@state` value, gathers their valid enemy neighbors, and chooses one candidate-array entry uniformly.
The original candidate-array multiplicity is preserved, with one aligned originating unit-count entry per candidate.
The source-country event target identifies the owner while ROOT remains the army leader.
The selected entry carries its originating frontline unit count into the rate calculation.
The old `num_units_offensive_combats_against@state` token is invalid because the current installed API targets terrain, such as `@plains`, rather than states.
The parent accepted the supported frontline-state adapter on 13 October within the owner's restore-and-fix instruction.
It identifies enemy neighbors of formations belonging to an actively attacking leader and does not claim exact observed per-state combat identification.

The shared combat tuning uses the pre-6c266388b rates, trigger chances, tier bonuses, unit divisor, and unit-factor bounds.
The population rate entries are stored multiplied by `chaos_meter_combat_civilian_deaths.scale` to preserve all original fractional digits.
`chaos_state_deaths_percent_divisor` converts the scaled value after multiplication by state population, and the shared helper consumes that divisor.
Combat cap and random multipliers retain their pre-April values.
The current state-population transaction, human-country filtering, death causes, UI, and attribution remain in place.

Historical correction: `b45c83d41^` contains a broad controlled-state/neighbor helper but its entry effect is empty.
Its original chemical leader-daily on-action calls that empty entry and does not call the broad helper.
The file history establishes no earlier working broad callback, so that orphan helper is not activated.
The restored source model is the complete callable pre-6c266388b single-state model.

Military casualties remain recorded in Deaths.
Their direct Chaos scaling follows the cumulative pre-1b2cd634a threshold of 250k casualties per point and does not also add a one-per-million military contribution.
Civilian causes retain their existing Deaths-to-Chaos conversion and cause weights.

## Contaminated-State Monthly Death Ticks

Monthly contaminated-state deaths are now population-percentage based instead of flat values.

### Chemical Contamination

- Chemical contamination now applies a stronger monthly civilian death percentage than before.

### Biowarfare Outbreaks

- Outbreak states now apply drastically higher death percentages than before.
- Deadlier outbreaks still apply stronger monthly death percentages than milder outbreaks.
- This pass pushes outbreak lethality up much more aggressively, with plague and smallpox raised again on top of the broader outbreak increase, so outbreaks now stand out clearly as the deadliest recurring contamination source by a wide margin.

Severity order:

- tularemia (lowest),
- anthrax (moderate),
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

This creates a direct death-toll consequence for repression-heavy occupation policy, and the current pass raises those occupation-law death rates substantially.

## Zombie-Controlled State Decay

Zombie-controlled states now use a separate long-form collapse mechanic documented in `docs/systems/cbrn_warfare/biological_warfare/zombie_state_decay_and_civilian_deaths.md`.

Summary:

- `1.7%` monthly population loss for up to `36` months per state,
- one structural degradation pass every `180` days,
- deaths feed the same chaos-meter pipeline under the cause `Zombie occupation collapse`.

## Air Contamination Modifier Visibility

The global air contamination country modifier is now hidden from the visible spirit list by removing its icon binding.

Gameplay effects remain active.
Only the visible spirit card is suppressed.

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
