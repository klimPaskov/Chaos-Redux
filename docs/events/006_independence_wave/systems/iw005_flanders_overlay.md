# Event 006 IW-005 Flanders Overlay

## Purpose

IW-005 is an additive package for the living Belgian country when it carries the vanilla `BEL_flanders` cosmetic identity. It is not a release package and it is not a separate country. The package gives that route a costed civic-industrial progression while retaining the complete Belgian country underneath it.

The authoritative design sources are:

- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv`
- `docs/plans/006_independence_wave_plans/006_form03_language_industry_progression_addendum_2026_07_15.md`

## Identity and preservation contract

The exact runtime identity is:

```txt
original_tag = BEL
has_cosmetic_tag = BEL_flanders
```

The overlay never performs any of the following operations:

- registers or releases a country
- assigns an Event 006 origin or liberation origin
- changes the Belgian focus tree
- changes Belgian history, cores, ownership, control, capital, autonomy, leaders, or characters
- transfers states 6 or 977
- changes the cosmetic identity that activated it
- changes FORM-03 invitation, membership, carrier, or sovereign-associate flags
- reads or writes Soviet Collapse state

The vanilla Belgium focus tree remains the country's meaningful focus surface. This package supplies decisions, a mission, values, and national-idea lifecycles only.

## Activation, suspension, and return

`common/on_actions/006_independence_wave_iw005_flanders_on_actions.txt` adds only `on_daily_BEL`. It does not iterate through all countries.

The daily hook applies this lifecycle:

1. A living `BEL` without `BEL_flanders` receives nothing.
2. The first day that `BEL_flanders` is present, the package sets its one-time initialization flag, starts both values, and installs the contested-command idea.
3. Completed action flags, the chosen institution, the two values, and guard-duty progress remain stored on Belgium.
4. Loss of `BEL_flanders` removes the package ideas and hides the action category. It does not remove or alter any vanilla Belgian content.
5. If the guard mission was running, the same active mission and running flag are preserved, its accumulated continuous-duty count is frozen, and its timeout is extended by one day on the first and every later suspended `on_daily_BEL` tick.
6. Return of `BEL_flanders` restores the correct idea stage and clears the interruption marker on that same mission. The lifecycle never removes, recreates, or restarts the mission, so neither its deadline nor its material cost is reset.

The lifecycle is idempotent. The starting values are written only once, so route loss cannot reset or duplicate progress.

Static limitation: official documentation does not define whether mission timeout decrement or `on_daily_BEL` executes first. The source applies the extension on the first observed suspended tick, but documentation alone cannot prove that a route loss with one day remaining is extended before timeout processing. The lifecycle does not use a restart or fresh-deadline fallback.

## Visible values

The category exposes two values from 0 to 100:

| Value | Meaning | Start | Coordinated command |
|---|---|---:|---:|
| Civic-Industrial Coordination | Agreement among municipalities, factories, rail administration, and civilian warrants | 30 | 55 |
| Scheldt Security | Depot custody, corridor defence, officer screening, and territorial command readiness | 25 | 55 |

Every gain, loss, threshold, cost, timeout, modifier, and AI weight is centralized in `common/script_constants/006_independence_wave_iw005_flanders_constants.txt`. The localisation reads those constants directly.

## Playable progression

### Municipal and factory ledgers

The player commits command power and manpower to reconcile municipal rolls, industrial employment, railway allocations, and civil-defence duties. The result strongly improves Civic-Industrial Coordination and gives a smaller Scheldt Security gain.

### Scheldt rail depots

Belgium must own and control states 6 and 977. Command power, trains, and support equipment establish shared custody over the Flanders and Antwerp rail-depot network. The result strongly improves Scheldt Security and gives a smaller civic gain.

### Defecting regulars

The player may spend manpower, Army Experience, infantry equipment, and support equipment to screen defecting officers and specialists. The action produces a substantial security gain and a smaller civic loss. It represents the accepted risk that a professional officer corps can become a rival political centre. It does not create units, leaders, characters, or free equipment.

### Factory and railway guard mission

After the ledgers and depots are prepared, the player may pay to begin `independence_wave_iw005_hold_scheldt_guard_line`.

For 60 continuous days Belgium must:

- own and control state 6
- own and control state 977
- station at least one Belgian division in state 6
- station at least one Belgian division in state 977

The counter resets when any condition fails. The mission times out after 150 active-route days and reduces national stability. A failed mission may be attempted again with a new material commitment. Cosmetic-route suspension freezes the counter and offsets each suspended day with a one-day timeout extension; restoration continues the original mission instead of creating a fresh 150-day deadline.

### Final institution

Completing the guard mission opens two mutually exclusive settlements:

| Institution | Gate | Cost profile | Strategic result | Tradeoff |
|---|---|---|---|---|
| Municipal-Industrial Board | 65 civic, 55 security | Command power, manpower, trains | Stability, factory output, efficiency gain | Higher military supply consumption |
| Scheldt Territorial Compact | 65 security, 55 civic | Manpower, Army Experience, infantry and support equipment | Defence, organisation, lower supply consumption | Lower stability and factory output |

The choice is permanent package progress. Its national idea is removed while the cosmetic route is absent and restored when the route returns.

## AI behaviour

Every selectable action has a nonzero AI weight. The AI gives early priority to the ledger and depot foundations, raises officer priority during war, and will not begin the corridor mission without divisions already present in both required states. Peace increases the Municipal-Industrial Board preference. War increases the Scheldt Territorial Compact preference.

This is an additive and bounded AI strategy. It does not replace Belgian focus selection or add a broad AI strategy file.

## FORM-03 relationship

The package leaves FORM-03 gameplay files untouched. Current FORM-03 eligibility already checks for a living `BEL` with `BEL_flanders`, Belgian ownership and control of state 6, sovereignty, invitation state, and a verified carrier connection.

The Flemish participant remains a Belgian sovereign delegation. FORM-03 may record autonomous membership through its own effects, but this overlay never transfers Belgian territory, applies `LCX`, adds cores, or treats Belgium as an Event 006 origin.

## Files

- `common/script_constants/006_independence_wave_iw005_flanders_constants.txt`
- `common/scripted_triggers/006_independence_wave_iw005_flanders_triggers.txt`
- `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt`
- `common/on_actions/006_independence_wave_iw005_flanders_on_actions.txt`
- `common/decisions/categories/006_independence_wave_iw005_flanders_categories.txt`
- `common/decisions/006_independence_wave_iw005_flanders_decisions.txt`
- `common/ideas/006_independence_wave_ideas_registry.txt`
- `common/scripted_localisation/006_independence_wave_iw005_flanders_scripted_localisation.txt`
- `localisation/english/006_independence_wave_iw005_flanders_l_english.yml`

## Visual assets

No new visual asset is required.

- Country identity and flags use vanilla `BEL_flanders` assets.
- Decision icons reuse `GFX_decision_independence_wave_government_actions`, `GFX_decision_independence_wave_army_integration_actions`, and `GFX_decision_independence_wave_integration_missions` from `interface/006_independence_wave.gfx`.
- Idea art reuses `GFX_idea_independence_wave_fragmented_command`, `GFX_idea_independence_wave_improvised_government`, and `GFX_idea_independence_wave_founding_identity` from the same file.

There are no sprite handoff requirements and no asset manifest is needed.

## Validation scenarios

1. A normal living Belgium without `BEL_flanders` receives no package flags, values, ideas, category, or mission.
2. Applying `BEL_flanders` to living Belgium initializes the package exactly once without changing country history, focus tree, territory, cores, autonomy, capital, leaders, or characters.
3. Completing decisions changes the two values by their displayed constants and pays every displayed resource cost. A stockpile or resource total exactly equal to the displayed cost is accepted.
4. The guard counter advances only while both states are Belgian-owned, Belgian-controlled, and garrisoned. It resets when any requirement fails.
5. Losing `BEL_flanders` suspends the category and ideas. The first and every later suspended daily tick extends the still-active guard mission by one day, while the hold counter remains unchanged. Restoring the route continues that same mission with its original remaining deadline.
6. Either final institution locks the other and restores correctly after route suspension.
7. FORM-03 continues to consume the existing `BEL_flanders` identity and its own sovereignty, invitation, connection, and territorial gates.
8. No IW-005 file registers a tag, releases a country, sets a cosmetic tag, loads a focus tree, or references Soviet Collapse state.

## Future plans and extension rules

Any later expansion should stay inside the same preservation contract. Suitable extensions include researched Flemish municipal or industrial incident events, a sourced officer-screening dispute, and FORM-03 delegate prose that distinguishes the participating Flemish delegation from all Belgian institutions. Such work must not create a standalone Flemish country, overwrite Belgium's focus tree, or infer Belgian-wide consent from the cosmetic identity alone.
