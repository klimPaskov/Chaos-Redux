# chaosx.nr1.1 Communism Spread System

## Scope

This file documents the communism spread chain rooted at `chaosx.nr1.1`.

It covers:

- the initial global communism spread bootstrap
- the recurring communist strikes event
- threat-stage popup notifications
- the anti-communist decision set
- the monthly idea-tier updater and its cooldown logic

## Main Files

- `events/001_communism_spread.txt`
- `common/scripted_effects/001_communism_spread_effects.txt`
- `common/script_constants/communism_spread_constants.txt`
- `common/decisions/chaosx_communism_fight_decisions.txt`
- `common/decisions/categories/chaosx_decisions_categories.txt`
- `common/on_actions/chaosx_on_actions.txt`
- `common/ideas/chaosx_ideas.txt`
- `localisation/english/001_communism_spread_l_english.yml`
- `localisation/english/chaosx_decisions_l_english.yml`
- `localisation/english/chaosx_ideas_l_english.yml`

## Event Map

- `chaosx.nr1.1`: starts global communism spread and seeds support in all non-communist countries
- `chaosx.nr1.2`: communist strikes and sabotage event
- `chaosx.nr1.3`: communist uprising and civil war pressure event
- `chaosx.nr1.4`: generic warning that communist influence is growing
- `chaosx.nr1.5`: generic warning that communist influence is weakening
- `chaosx.nr1.6`: critical communist threat warning
- `chaosx.nr1.7`: communist threat greatly reduced
- `chaosx.nr1.8`: communist rebels seize territory
- `chaosx.nr1.9`: military crackdown succeeds
- `chaosx.nr1.10`: military crackdown partially fails
- `chaosx.nr1.11`: military crackdown completely fails
- `chaosx.nr1.12`: hidden strike-cooldown cleanup event
- `chaosx.nr1.13`: hidden threat-notification cooldown cleanup event

## Runtime Flow

### 1. Global spread bootstrap

`chaosx.nr1.1` turns on the global `communism_spread` flag once and then pushes communist support into every other country.

The initial gain still scales with the chaos-tier helper logic. The event also gives each affected country the first communism spread idea so the monthly updater has a state to manage.

### 2. Monthly tier sync

`update_communism_spread_idea` in `common/scripted_effects/001_communism_spread_effects.txt` is the central runtime controller.

Each monthly refresh now:

1. reads the current active communism spread idea tier
2. derives the target tier from live communist popularity
3. swaps to the correct idea tier, or removes all spread ideas once support falls to `10%` or below
4. fires a threat-status popup only if the shared notification cooldown is not active

The monthly on-action now also runs the updater when a country still has a communism spread idea, even if support already fell below `1%`. That closes the old cleanup gap where weak communist support could leave stale ideas behind.

### 3. Threat notification cooldown

The “influence growing”, “influence weakening”, “critical threat”, and “threat greatly reduced” popups all share one country-level cooldown.

Current behavior:

- the first eligible tier-change popup sets `communism_spread_status_notification_cooldown`
- hidden event `chaosx.nr1.13` clears that flag after `210` days
- further tier oscillation during that window updates gameplay state normally but does not spam status popups

This stops the old loop where the player could reduce support, ignore it for a short period, and then get repeated “reduced / increased / reduced” notifications around the same thresholds.

### 4. Communist strikes cadence

`chaosx.nr1.2` now requires `NOT = { has_country_flag = communism_spread_strike_cooldown }`.

When the strike event fires, it immediately starts a tier-based cooldown through `queue_communism_spread_strike_cooldown`.

Current strike cooldowns:

- tier 1 threat: `240` days
- tier 2 threat: `225` days
- tier 3 threat: `210` days
- tier 4 threat: `195` days
- tier 5 threat: `180` days

Hidden event `chaosx.nr1.12` clears the strike cooldown flag after the scheduled delay.

This means strikes still exist as a recurring pressure tool, but they cannot roll repeatedly every few weeks anymore. Lower communist threat now also directly means a longer wait before the next strike can happen.

### 5. Anti-communist decisions

The category now stays visible for any non-communist country while the communism spread system is active, and all five suppression decisions stay visible at the same time.

Availability, resource costs, and cooldowns still decide whether a specific decision can be clicked. Visibility no longer hides part of the toolkit just because communist support is currently in a lower tier.

The decisions now have long re-enable cooldowns, while keeping their original active durations:

- propaganda: `30` active days, `180` re-enable days
- economic counter-measures: `60` active days, `150` re-enable days
- military intervention: `20` active days, `190` re-enable days
- industrial crackdown: `25` active days, `185` re-enable days
- emergency measures: `60` active days, `180` re-enable days

That puts repeat access roughly into the requested `6-8` month window instead of allowing the same tools to cycle back much faster.

Support reduction was also increased:

- propaganda: `-3%`
- economic counter-measures: `-4%`
- industrial crackdown: `-4%`
- emergency measures: `-12%`
- military success: `-7%`
- military partial failure: `-3%`

Complete military failure still backfires and can strengthen communism, so the military line remains risky instead of becoming a guaranteed reduction button.

## Implemented Support-Driven Escalation

These are not event-log evolutions. They are the baseline domestic escalation layers that now exist inside the communism chain and are driven by communist support plus rebel activity.

### Stage I: Cadre Networks

Trigger:

- a non-communist country rises above `20%` communist support

Gameplay effect:

- hidden pressure package:
  - `communism_drift = +0.01`
  - `political_power_gain = -0.05`
- `chaosx.nr1.2` strikes upgrade from:
  - `3` damaged buildings to `4`
  - `10%` state coverage to `12%`

### Stage II: Strike Committees

Trigger:

- a non-communist country rises above `25%` communist support, or the first strike event has already happened and support is still above `10%`

Gameplay effect:

- `chaosx.nr1.2` becomes a real sabotage event:
  - `5` damaged buildings
  - `15%` state coverage
  - `0.35` damage modifier
- ignoring the strike now also costs:
  - `-1%` stability
  - `-1%` war support

### Stage III: Armed Cells

Trigger:

- a non-communist country rises above `40%` communist support

Gameplay effect:

- military anti-communist action loses `10` success chance
- military partial failure takes a larger share of failed outcomes, making full failure more common
- `chaosx.nr1.8` rebel escalation gains:
  - `+2` rebel-state percentage
  - `+1` division per seized state
- hidden weekly decay:
  - `stability_weekly = -0.001`
  - `war_support_weekly = -0.001`

### Stage IV: Parallel Soviets

Trigger:

- a non-communist country rises above `50%` communist support, or rebels already exist while support is above `40%`

Gameplay effect:

- `chaosx.nr1.3` civil-war pressure MTTH drops from `180` days to `90`
- military anti-communist action loses `15` success chance and uses an even harsher failure split
- `chaosx.nr1.8` rebel seizure gains:
  - another `+3` rebel-state percentage
  - minimum `2` states captured
- hidden weekly decay:
  - `political_power_gain = -0.10`
  - `stability_weekly = -0.002`
  - `war_support_weekly = -0.002`

## Suggested Chaos Evolutions

These are the actual event evolutions I would add next. They should be country-scoped evolutions recorded against event `1`, with the affected country stored as `events_log_evolution_actor`.

The difference is important:

- support-driven escalation is always on once local communist pressure reaches the threshold
- a chaos evolution is a world-chaos milestone that changes how the communism event behaves from that point onward

### Evolution I: International Coordination

Recommended trigger:

- first time global `chaos_tier = 2`
- only for countries where communism spread is active and communist support is already at least `15%`

Recommended behavior change:

- `chaosx.nr1.2` strike MTTH falls from `20` to around `14` days
- `fight_communism_propaganda` and `fight_communism_economic` each lose around `1%` of reduction strength, representing outside support keeping the movement supplied
- `chaosx.nr1.11` complete military failure should queue another unrest pulse, for example by forcing a fresh strike roll after `10-20` days

Why this would feel meaningful:

- the player feels the world getting less governable as chaos rises, not just the support number climbing locally
- soft containment starts to slip specifically because the movement is now externally coordinated

### Evolution II: Insurrectionary Bloc

Recommended trigger:

- first time global `chaos_tier = 4`
- only for countries where communism spread is active and support is already at least `30%`

Recommended behavior change:

- `chaosx.nr1.3` should loosen from `communism > 0.4` and `stability < 0.3` to something like `communism > 0.3` and `stability < 0.4`
- `chaosx.nr1.8` should gain a rebound path so that crushing one rebel outbreak does not fully solve the crisis if support stays high
- military complete failure should become capable of immediately pushing the country into the rebel/uprising path instead of only adding support

Why this would feel meaningful:

- this is the point where the communism event stops being “recurring unrest” and becomes a true pre-insurrection system
- the player is forced to deal with regime fragility, not just sabotage and popularity drift

No world-end branch is recommended for this chain. The event resolves cleanly through suppression, civil war, or communist takeover instead of a terminal global scenario.

## Icons And UI Assets

No new icons or UI assets were added in this pass.

Existing assets used by the mechanic remain unchanged:

- category icon: `GFX_decision_category_generic_communism`
- propaganda decision icon: `GFX_decision_generic_speech`
- economic decision icon: `GFX_decision_generic_consumer_goods`
- military decision icon: `GFX_decision_generic_military`
- industrial decision icon: `GFX_decision_generic_factory`
- emergency decision icon: `GFX_decision_generic_protection`

## Future Plans

- Add dedicated strike-scaling by tier beyond cooldown alone if the chain needs sharper differentiation between early agitation and late revolutionary sabotage.
- Replace repeated percentage thresholds with a fuller communism spread threshold table in script constants if this mechanic gets another broader rebalance pass.
- Add event-log details for this chain if communism spread becomes important enough to deserve history browsing parity with the larger chaos systems.
