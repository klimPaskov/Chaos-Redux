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

1. The system now starts from each country's real daily military casualty increase, using the existing deaths tracker instead of army-leader combat scope.
2. If that country is at war, it converts part of that daily casualty delta into civilian collateral pressure using ideology, `chaos_warfare`, and chaos-tier scaling.
3. It resolves valid enemy frontline states directly by iterating enemy-controlled states that border the source country's currently controlled territory, and only keeps states that still have population to lose.
4. The collateral total is split across every valid frontline state instead of only one random state, so all affected frontier states on that front can register deaths on the same day.
5. Each frontline state first gets a dynamic distribution weight from density, population, and inverse infrastructure, then the full daily collateral pool is divided across those states by their share of the total weight.
6. The distribution pass keeps its running allocation totals in global scratch variables for the duration of the country pass, so the state loop no longer depends on fragile inline cross-scope variable reads.
7. This means combat civilian deaths no longer depend on unit-leader state lookups or daily combat-scope edge cases; they piggyback on the military casualty stream that is already working.
8. The death rate is ideology-based:
   - fascist: highest baseline,
   - communist: lower,
   - non-aligned: very low,
   - democratic: extremely low.
9. If the country has `chaos_warfare`, an additional combat civilian-death rate and collateral-pressure bonus are added on top.
10. Higher chaos tiers now scale the combat death rate upward.

Result:

- `chaos_warfare` + ideology rates stack additively.
- The deaths are registered as civilian and reduce state population directly.
- Border states are only considered once per pass, so multi-neighbor frontlines no longer get extra random-weight just from adjacency duplication.
- Frontline states are now all eligible to take part of the same day's collateral losses instead of combat deaths concentrating into one random state.
- The overall daily collateral pool is preserved, but denser, more populous, and less developed frontline states receive a larger share of it.
- This pass is tied to real tracked combat losses rather than inferred leader placement, and the deaths map highlights the states that actually receive those registered civilian combat deaths through the shared state-population death pipeline.

## Contaminated-State Monthly Death Ticks

Monthly contaminated-state deaths are now population-percentage based instead of flat values.

### Chemical Contamination

- Chemical contamination now applies a noticeably stronger monthly civilian death percentage than before.

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

This creates a direct death-toll consequence for repression-heavy occupation policy, and the current pass raises those occupation-law death rates substantially.

## Zombie-Controlled State Decay

Zombie-controlled states now use a separate long-form collapse mechanic documented in `docs/zombie_state_decay_and_civilian_deaths.md`.

Summary:

- `1.4%` monthly population loss for up to `36` months per state,
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
