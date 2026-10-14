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
A successful roll scans the leader's units in controlled frontline states through the supported `num_units_in_state@state` value and gathers their valid human enemy neighbors.
The candidate state pointers and aligned originating unit counts use native unscoped temporary arrays across the country and state scopes.
One candidate-array entry is chosen uniformly, retaining the original duplicate-state multiplicity and originating unit count for the total budget calculation.
The source-country event target identifies the owner while ROOT remains the army leader.
The selected entry carries its originating frontline unit count into the unchanged rate, environment, random multiplier and cap calculation.
That amount is the total budget for this successful leader callback, bounded by whole civilians available in the selected state.
It is not multiplied by the number of recipient states and is not calculated from military casualties.
The same candidate pointers are then deduplicated, and each state's originating unit contributions are summed.
Its allocation weight is that unit sum multiplied by the existing density and infrastructure environment factor.
Normalized shares are allocated sequentially from the remaining budget and remaining weight, using the final eligible share to absorb rounding.
Each planned share is bounded by that state's whole available population; a second bounded planning pass places any unused capacity or rounding remainder before population changes.
The completed plan then calls the existing exact civilian population-loss primitive once per allocated state.
Only its measured applied debit enters the state and victim Deaths ledgers.
Any difference between the requested budget and observed debit remains an unlogged residual; no extra population debit fills a short native transaction.
The old `num_units_offensive_combats_against@state` token is invalid because the current installed API targets terrain, such as `@plains`, rather than states.
The parent accepted the supported frontline-state adapter on 13 October within the owner's restore-and-fix instruction.
It identifies enemy neighbors of formations belonging to an actively attacking leader and does not claim exact observed per-state combat identification.

The shared combat tuning uses the pre-6c266388b rates, trigger chances, tier bonuses, unit divisor, and unit-factor bounds.
The population rate entries are stored multiplied by `chaos_meter_combat_civilian_deaths.scale` to preserve all original fractional digits.
`chaos_state_deaths_percent_divisor` converts the scaled value after multiplication by state population, and the shared helper consumes that divisor.
Combat cap and random multipliers retain their pre-April values.
The current state-population transaction, human-country filtering, death causes, UI, and attribution remain in place.

Victim attribution uses existing human core countries as a game proxy, not an inference about a state's demographic composition.
When the human owner is a core country and other eligible cores exist, the owner receives the configured 0.50 share and the remaining measured deaths are split among the other cores.
Without an eligible owner core, the eligible human cores share the measured deaths equally.
When no eligible core exists, an existing human owner, or otherwise human controller, receives the attribution.
Dormant and nonhuman core countries receive no row.
Sequential integer shares consume the measured debit, with the final recipient receiving the exact remainder.
The state Deaths ledger receives the measured amount once; victim shares register global, cause and country records with population mutation and state-ledger registration disabled.
The broad casualty-derived country allocator remains excluded because it lacks the current offensive-leader gate and would introduce another aggregate rate.

### Helper contract and lifetime

| Helper | Scope and inputs | Outputs, side effects and callers |
| --- | --- | --- |
| `chaos_meter_calculate_state_civilian_deaths_percent` | STATE; existing percent, scale divisor, multiplier, random and cap envelope | Returns caller-preinitialized `chaos_deaths_change`, default zero; consumes the existing one-shot tuning envelope. Performs the existing two random multiplier draws without population or ledger changes. Called by the existing percent registration wrapper and the combat budget calculator. |
| `chaos_meter_calculate_combat_civilian_budget_to_state` | STATE; current profile and selected originating unit count | Returns caller-preinitialized `chaos_combat_civ_budget`, default zero. Uses the current unit-factor bounds, environment, scaled rate and percent calculator, then clamps to whole available civilians. Called once from the original raw-entry selection. |
| `chaos_meter_distribute_leader_combat_civilian_budget` | COUNTRY; positive budget and aligned temporary candidate arrays | Plans deduplicated states, summed units, weights, whole capacities and allocations, then invokes the exact state registration helper once per state. Local `chaos_combat_frontage_applied` and `chaos_combat_frontage_remaining` distinguish observed loss from unused budget. Called only by the current offensive-leader adapter. |
| `chaos_meter_register_combat_civilian_deaths_to_state` | STATE; requested `chaos_deaths_change` | Returns caller-preinitialized `chaos_combat_civ_state_applied`, default zero; performs one exact debit, one measured state-ledger write and conserved human victim shares. Called only by the completed frontage plan. |

The registration wrapper retains every contamination and occupation call site and its original percent calculation.
Combat profile outputs are initialized in the calling owner scope before the profile helper returns.
Every allocation loop uses an explicitly initialized private break variable; candidate, plan and victim temporary arrays are cleared when their consumer finishes.
The existing regular leader/source-country event targets are confined to the current callback chain.
No global target, saved per-state distribution weight, periodic hook or cleanup registry is introduced.
Rates, chances, unit-factor limits and environment factors remain in their existing constant groups; only the historical owner-core share is centralized as `chaos_meter_deaths.combat_owner_core_share`.

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

1. Extend the existing victim-country proxy only when a separately evidenced demographic source is available; keep physical losses and attribution shares conserved.
2. Add dedicated deaths-log filtering by cause family (combat, contamination, occupation).
3. Add occupation-law counterplay decisions that trade compliance/output for lower civilian deaths.
4. Add per-region humanitarian pressure events that react to high sustained civilian death rates.
