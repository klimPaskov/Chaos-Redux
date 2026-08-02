# Air Winter Response Decision Proof

## Status

The Air Winter response layer has static engine support for targeted state decisions, timers, dynamic custom costs, one-country project ownership, deterministic reception selection, population-scaled evacuation, cancellation, terminal event handoff, cleanup, and dedicated sprite registration. HOI4 was not launched. Runtime behavior is not claimed.

## Required references consulted

- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
  - The custom-cost section defines the base, blocked, and tooltip localisation keys and requires payment in `complete_effect`.
  - The timed-decision section defines `days_remove`, `remove_effect`, `cancel_trigger`, and `cancel_effect`.
  - The targeted-decision section defines ROOT as the acting country and FROM as the selected state for `state_target = any_controlled_state`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
  - Scope values may be stored in variables and arrays, then entered with `var:`.
  - Temporary variables carry arithmetic across nested scopes without a scope prefix.
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
  - State-scope `add_manpower` changes total state population.
  - The state entry records that a negative value also credits recruitable manpower. The implementation compensates that documented quirk at country scope.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`
  - `state_population_k` exposes population in thousands and is the documented route for avoiding variable overflow.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
  - `add_manpower` supports STATE and COUNTRY scope.
  - Arrays support scope values, `clear_array`, and `for_each_scope_loop`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AFG.txt`
  - State integration decisions use FROM state targets, timed removal, and cancellation cleanup.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/SIA.txt`
  - Timed decisions use script constants for removal and re-enable durations.
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
  - The equipment affordability trigger uses `meta_trigger` to inject a dynamic cost into a static comparison field. Air Winter follows the same structure for quoted trains, convoys, support equipment, manpower, and stability.
- `common/scripted_effects/010_death_effects.txt`
  - State population arithmetic reads `state_population_k` and converts to people only immediately before state `add_manpower`.

## Decision ownership and lifecycle

The category contains twenty decision blocks:

- one response-priority selector
- one disabled priority summary
- one reception-state selector
- one disabled reception summary
- sixteen timed operational projects

Only one priority state and one reception state can be active per country. The designation effects clear stale ownership before writing the replacement. Monthly reconciliation removes designations whose owner, controller, phase, or eligibility no longer matches.

Every timed project writes `air_winter_response_project_active` on the source state and the acting country. The country stores the active state. Completion, cancellation, state reset, country reset, and global reset clear both sides. This prevents parallel projects in different states from bypassing the intended national response capacity.

## Evacuation quote derivation

The quote is rebuilt after the existing monthly state pass for each country that registered a valid priority state during that pass. The post-pass helper iterates only `global.air_winter_evacuation_cache_countries`, a bounded owner array created during the existing world-state iteration. It does not add a country-wide or state-wide periodic scan.

For each owner, the source is the selected priority state. The receiver is the lowest numeric state id among valid entries in that country's reception array. The quote records the current Air Winter cycle id, source id, receiver id, source population, receiver population, and receiver Refugee Pressure.

Controlled evacuation transfers 15 percent of the source population. Final evacuation transfers 35 percent. Formula work stays in population thousands:

1. Read `state_population_k`.
2. Multiply by the configured transfer share.
3. Derive train, convoy, support-equipment, staff, stability, source-relief, and receiver-pressure values from the K-unit transfer.
4. Convert the transfer to people once with `population_people_per_k`.
5. Round the people value once and cache both representations.

This avoids whole-thousand quantization and follows the official overflow-safe dynamic-variable guidance. All divisors, floors, ceilings, shares, and conversion values live in `common/script_constants/fallout_consolidated_constants.txt`.

The receiver pressure increase is proportional to transfer population divided by receiver population. A receiver floor prevents a near-empty state from producing an undefined or extreme divisor. A quote is invalid when the resulting receiver pressure exceeds the configured ceiling.

Availability checks require the cached cycle to equal the open global cycle. They also revalidate the exact source and exact receiver, including ownership, control, reception flag, reception owner, array membership, eligibility, and source-receiver inequality. A different valid receiver cannot satisfy a stale quote.

## Payment and delayed result

Controlled evacuation charges quoted trains, convoys, administrative manpower, and population-scaled stability. Final evacuation charges quoted trains, convoys, support equipment, and administrative manpower. The custom affordability triggers inject the exact quote into static trigger fields. The payment effects deduct those same country variables.

At decision start, the source state snapshots both transfer representations, receiver id, receiver pressure gain, receiver pressure limit, source pressure relief, cycle id, and source population. Monthly quote refreshes cannot alter an active project.

The priority owner is not registered for quote refresh while its country project lock is active. This preserves the paid country quote used by the visible timed card. Quote refresh resumes on the first monthly cycle after project release.

The delayed completion validates that:

- the project type and quote lock still match
- the source remains owned and controlled by the project owner
- the source still contains at least the locked K-unit transfer
- the locked receiver remains owned, controlled, designated, present in the reception array, eligible, and different from the source
- current receiver pressure remains within the locked pre-transfer limit

An invalid project cancels instead of recomputing or clamping the paid result.

The valid result removes the exact cached people value from the source and adds it unchanged to the receiver. It then subtracts the same negative value from ROOT country manpower. This last operation is a documented workaround for the offline wiki's negative state `add_manpower` recruitable-manpower credit. No stronger native population effect exists in the installed official effect catalogue or reviewed vanilla files.

## Balance review

The following hand calculations use the installed constants and show the scaling envelope before receiver pressure is applied:

| Source population | Controlled transfer | Controlled trains | Controlled convoys | Controlled staff | Controlled stability | Final transfer | Final trains | Final convoys | Final support | Final staff |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 100K | 15K | 1 | 1 | 500 | 0.5% | 35K | 1 | 1 | 4 | 500 |
| 1M | 150K | 2 | 3 | 500 | 0.6% | 350K | 5 | 7 | 35 | 875 |
| 5M | 750K | 10 | 15 | 1,875 | 3.0% | 1.75M | 24 | 35 | 175 | 4,375 |
| 10M | 1.5M | 20 | 30 | 3,750 | 5.0% cap | 3.5M | 47 | 70 | 350 | 8,750 |

For a receiver with the same population as the source, controlled evacuation adds 7.5 Refugee Pressure and final evacuation adds 17.5. A receiver with half the source population receives 15 and 35. The result is blocked whenever existing pressure plus that increase would exceed 90.

The minimum staff cost prevents low-population states from receiving nearly free administration. The controlled stability floor keeps small evacuations politically meaningful. The stability cap prevents very large cities from making the controlled route impossible solely through the political component. Final evacuation omits stability but adds support equipment and a larger transport and staff burden.

## Terminal event handoff

The abandonment vote and mass decontamination save FROM as the regular `air_winter_response_state` event target before firing `chaosx.fallout.201` or `.202`. Each result event validates the typed event target and the matching pending branch. `chaosx.fallout.203` handles a stale visible choice whose ownership changed before click resolution.

## Asset wiring

`interface/fallout_consolidated.gfx` registers the category and decision sprites under dedicated Fallout-owned paths. The priority selector uses `GFX_decision_air_winter_response_priority`. Its source, transparent master, processed PNG, decoded proof, DDS, contact sheet, prompt, manifest row, and handoff are recorded under `docs/assets/air_cleanliness_fallout/`.

## Static validation scenarios

The reviewed script establishes these invariants:

1. Repeating priority or reception designation replaces the prior state and clears stale ownership.
2. Repeating cache preparation on the same monthly cycle cannot duplicate an owner in the bounded array.
3. Equal receiver candidates select the lowest state id.
4. Equal transfer inputs produce the same quote without random selection.
5. Only one active timed project can exist for a country.
6. A source population drop below the locked transfer cancels the result.
7. Receiver loss, ownership change, control change, designation change, or pressure growth beyond the locked limit cancels the result.
8. Completion uses the paid snapshot and does not read the refreshed quote.
9. Source and receiver state-population changes use the same people value.
10. Country reset clears quotes, arrays, state locks, country locks, and project snapshots. Global reset applies country cleanup through the bounded registered-owner array and requests state cleanup on the next existing monthly pass.
11. Active projects preserve their paid country quote until release.
12. Missing project-owner recovery clears the current owner's matching country pointer when that pointer still identifies the state.

## Unobserved engine boundary

The source and receiver population arithmetic is exact in script. The country-scope compensation follows the offline wiki's description of the negative state-population quirk, but the installed generated effect documentation does not describe that quirk. Without launching HOI4, the available-manpower neutrality of the three-step transfer is not runtime proven.

Runtime observation would also be required to confirm the final targeted-decision layout, timer presentation, dynamic stability formatting, cancellation presentation, and all decision icons in the live interface. These are not claimed as passed.
