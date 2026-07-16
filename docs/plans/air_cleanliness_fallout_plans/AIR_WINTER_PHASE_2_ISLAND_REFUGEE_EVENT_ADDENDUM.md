# Air Winter Phase 2 Island Refugee Event Addendum

Status: implemented and statically audited

## Scope

This addendum covers the accepted Phase 2 island-state row in `specs/baseline/02_winter_mapmode_and_state_effects.md`:

- refugee boats reach an island state
- the owner chooses rescue, port quarantine, or naval exclusion
- every choice changes real state population and national Stability
- the route writes durable state and country memory for later Fallout identity content

The chain is an Air Winter precursor to the larger post-Fallout refugee system. It does not implement citizenship, return, property, military service, family reunification, treaty assistance, or a successor focus package. Those remain separate reviewed systems.

## Event ownership and route

The opening is `chaosx.fallout.38` and the delayed result is `chaosx.fallout.39`. Both remain in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

The route is eligible only when the state passes the exact engine classifier:

```txt
OR = {
	is_island_state = yes
	is_one_state_island = yes
}
```

`is_island_state` covers states whose provinces have no ordinary land connection. `is_one_state_island` also permits ordinary connections within the state while rejecting ordinary connections to another state. The union is the engine's topology definition for this route. It is not a claim that every geographically intuitive island qualifies. Vanilla records Taiwan as an exception to `is_one_state_island`, and mixed-island states can also fall outside the union. This tranche intentionally follows the engine topology instead of silently substituting the broader Air Winter presentation class. Any explicit geographic exception ledger requires its own reviewed state audit.

Within Phase 2, the route order is:

1. mountain capital
2. engine-recognized island state
3. city
4. maritime, oceanic, or tropical coast
5. arid or Mediterranean
6. highland or polar
7. boreal or equatorial food route

This preserves the already reviewed mountain-capital precedence. It gives the dedicated island row priority over the generic city and coast routes inside one state. First-frost markers reuse the same selector and must accept event id 38.

Candidate comparison occurs after route selection. Event 38 therefore receives a same-phase score bonus larger than the full pressure-score range. An eligible island state wins against another Phase 2 state owned by the same country, while a genuinely later-phase state can still take the current monthly dispatch. The Phase 2 seen flag remains unset until event 38 actually dispatches, so the island row can return in a later month instead of being silently consumed.

## Source registry and population transaction

The boats have an actual source state, source country, and source Air Winter region. No source is invented in localisation or replaced with an unknown-origin marker.

The existing monthly state pass collects one valid coastal source candidate per owner. A candidate must be owned and controlled by that owner, have an active Air Winter ledger at Phase 2 or worse, retain more than the protected population minimum, and pass `is_coastal = yes`. The score is the existing Air Winter phase score plus current state pressure. The owner keeps only its highest score, with lower state id breaking a tie. The candidate records its current Air Winter cycle and presentation region. Owners with a candidate enter a bounded global country array once.

When event 38 is the selected receiver dispatch, the dispatcher scans only that bounded owner array. It chooses the highest-scored current source whose country differs from the receiver, with lower source state id breaking a tie. Dedicated temporary values are initialized for every receiver and determine whether the current scan found a source. A regular event target left by an earlier receiver is never accepted as proof for the current receiver.

The selection saves regular event targets for the source country and state. It also freezes the source state, source country, source region, candidate family, origin year, and current Air Winter cycle on the receiver as a pending offer. If no source is valid, the dispatcher clears only the receiver candidate. It does not set the Phase 2 seen flag, change a seasonal marker, refresh the cooldown, or fire event 38.

A valid source selection sets the country cooldown to prevent another popup while the player considers the offer, but it defers the Phase 2 seen flag and seasonal-marker commit. Every option rechecks the frozen offer, destination, source, current cycle, source ownership and control, coastal status, source phase, source population, Fallout state, and its payable resources inside the executed effect. A positive balanced transfer commits the seen flag, coalesces or clears the matching first-frost marker, records its event year when required, reanchors the cooldown, and clears the offer. A stale or zero transfer clears the offer and cooldown without consuming the Phase 2 route. The candidate can then be reconsidered in the next monthly cycle.

After the full receiver dispatch loop, the dispatcher clears every source-owner candidate receipt and the bounded source array. Pending offers remain self-contained and do not depend on those monthly candidate fields. Global and country reset clear both source receipts and pending offers.

Every valid opening choice calculates requested arrivals from the selected island's live population at click time. The helper multiplies `state_population_k` by 1,000 and by the selected share, rounds the result, and clamps it only to the selected ceiling. There is no population floor that can overwhelm a small island.

| Policy | Population share | Maximum | Reason for people remaining ashore |
| --- | ---: | ---: | --- |
| Rescue | 2 percent | 40,000 | Rescue launches and shore crews land the fleet |
| Shore quarantine | 1 percent | 20,000 | Screened passengers enter guarded landing camps |
| Naval exclusion | 0.25 percent | 5,000 | People already ashore and passengers from disabled craft cannot be returned safely |

The source state passes the requested amount through `apply_exact_state_civilian_population_loss` with Deaths logging disabled and the existing 1,000-person protected remainder. The exact applied output is then added to the destination with positive state-scope `add_manpower`. This is a balanced migration transaction. It does not create people, credit the source owner with recruitable manpower, or enter migration in the Deaths ledger.

The exact applied amount is stored on the destination state as `air_winter_island_refugee_last_arrivals`. The receiver adds the same amount to `air_winter_island_refugee_arrivals_total`. These are population memories, not a second population grant. The source state records the departure and receives matching refugee-pressure relief.

Any later local loss at the destination uses `air_winter_event_apply_deaths` and the existing `air_winter_exposure` Deaths reason.

## Opening choices

### Rescue every boat that can still make shore

Requirements and payment:

- at least 500 available Manpower
- at least 3 Convoys
- spend 500 Manpower and 3 Convoys

Immediate state changes:

- transfer the rescue population from the recorded source state
- Food Reserve falls by 6
- Shelter Capacity falls by 6
- Refugee Pressure rises by 6
- Disease Pressure rises by 2
- Adaptation rises by 2

National Stability falls by 2 percent. The destination records admitted maritime refugees and the receiver records an open-shore identity memory. The source records an organized departure.

Refugee Pressure in the source state falls by 6 after the exact transfer succeeds.

### Establish quarantine inside the landing cordon

Requirements and payment:

- at least 200 available Manpower
- at least 15 Support Equipment
- spend 200 Manpower and 15 Support Equipment

Immediate state changes:

- transfer the quarantine population from the recorded source state
- Food Reserve falls by 2
- Shelter Capacity falls by 2
- Refugee Pressure rises by 4
- Disease Pressure rises by 1
- Building Damage Pressure rises by 8
- Adaptation rises by 2

National Stability falls by 1 percent. The destination records controlled admission and shore quarantine. The receiver records a quarantine-station identity memory. The source records a screened departure.

Refugee Pressure in the source state falls by 4 after the exact transfer succeeds.

### Enforce naval exclusion beyond the shore lights

This option has no payable resource gate, so a valid event always has one executable choice.

Immediate state changes:

- transfer the exclusion population from the recorded source state for people who cannot be returned to sea
- Food Reserve falls by 2
- Shelter Capacity falls by 2
- Refugee Pressure rises by 2
- Exposure rises by 2
- Adaptation rises by 2

National Stability rises by 0.5 percent. The destination records forced exclusion and the receiver records a closed-waters identity memory. The source records that most of the fleet was refused.

Refugee Pressure in the source state falls by 2 after the exact transfer succeeds.

All three openings clear an older island-refugee branch, write exactly one new branch, refresh the state, refresh the 46-day country cooldown, and schedule event 39 after 30 days.

## Deterministic delayed results

The result has six mutually exclusive options. Exactly one is visible for a valid branch and live state condition.

### Rescue harbor registered

Success requires:

- Food Reserve at least 25
- Shelter Capacity at least 20
- Disease Pressure at most 55
- Refugee Pressure at most 35

The state gains 4 Adaptation and 4 Reclamation. Disease Pressure falls by 2. The state and country record a successful open-harbor memory.

### Rescue sheds overwhelmed

This is the inverse of the rescue success predicate.

Food Reserve falls by 4, Shelter Capacity falls by 4, Refugee Pressure rises by 2, Disease Pressure rises by 4, and Exposure rises by 1. National Stability falls by 1 percent. Local residents and rescue crews lost to cold inside the overloaded harbor shelters equal 0.01 percent of remaining state population and enter the Deaths ledger.

### Quarantine register completed

Success requires:

- Water Security at least 30
- Disease Pressure at most 50
- Building Damage Pressure at most 65
- Refugee Pressure at most 30

The state gains 2 Adaptation, 2 Shelter Capacity, and 2 Reclamation. Disease Pressure falls by 2 and Building Damage Pressure falls by 8. The state and country record an orderly quarantine memory.

### Quarantine cordon failed

This is the inverse of the quarantine success predicate.

Shelter Capacity falls by 2, Refugee Pressure rises by 2, Disease Pressure rises by 4, and Building Damage Pressure rises by 8. National Stability falls by 1 percent. Local patients, guards, and dock workers lost to exposure in the failed cordon equal 0.01 percent of remaining state population and enter the Deaths ledger.

### Exclusion line held

Success requires:

- Adaptation at least 15
- Exposure at most 60
- Refugee Pressure at most 25

The state gains 2 Adaptation. Exposure falls by 1 and Refugee Pressure falls by 2. The state and country record a maintained exclusion line.

### Exclusion line broke

This is the inverse of the exclusion success predicate.

Food Reserve falls by 2, Refugee Pressure rises by 2, Exposure rises by 2, and Disease Pressure rises by 1. National Stability falls by 1 percent. Local patrol and harbor casualties equal 0.01 percent of remaining state population and enter the Deaths ledger.

## AI contract

Each opening choice has a complete AI weight.

- Rescue, quarantine, and exclusion begin at 60, 30, and 10.
- Democratic and neutral governments prefer rescue when the exact delayed success remains plausible.
- Communist and neutral governments prefer controlled quarantine when the exact delayed success remains plausible.
- Fascist governments, countries at war, and owners with low food or shelter place more weight on exclusion.
- Low Shelter Capacity and low Food Reserve strongly reduce rescue weight.
- An implausible deterministic result reduces the matching choice weight.

The pre-choice AI boundaries exactly translate the opening changes into the delayed thresholds:

| Branch | Pre-choice AI boundary |
| --- | --- |
| Rescue | Food Reserve at least 31, Shelter Capacity at least 26, Disease Pressure at most 53, Refugee Pressure at most 29 |
| Quarantine | Water Security at least 30, Disease Pressure at most 49, Building Damage Pressure at most 57, Refugee Pressure at most 26 |
| Exclusion | Adaptation at least 13, Exposure at most 58, Refugee Pressure at most 23 |

The delayed event has no probabilistic AI roll. Its branch and live ledger produce one valid option.

## Memory and later identity hook

The destination state keeps the exact latest arrivals, the latest admission policy, the source country, the source Air Winter presentation region, entry as voluntary or forced, quarantine treatment, and the latest result. Rescue and quarantine record voluntary entry. Exclusion records forced landing for the people already ashore or aboard disabled craft. The receiver keeps the cumulative arrival total plus its latest source, policy, and result. The source state and source country record the departure policy applied by the receiver. State memory survives ownership changes, so a later successor can inspect the shore policy even if the original receiver disappears. Country memory remains available to a surviving or converted old tag.

These flags and variables are live hooks only. This tranche does not claim that the later Fallout country-memory, focus, or successor consumer is complete. The consumer must be implemented and reviewed with the broader Fallout identity layer before the full goal can be complete.

## Pending-chain and reset contract

The three branch flags are exclusive. The branch trigger for each route requires its own flag and rejects the other two. The result trigger requires the exclusive disjunction. Reconciliation cancels any row with more than one island-refugee branch.

`air_winter_event_cancel_pending_chain` clears all three branch flags. Full state reset also clears route, result, source, origin-region, entry, quarantine-treatment, departure, and latest-arrival memory. Full country reset clears source, policy, and result memories plus the cumulative arrival total. Monthly candidate preparation clears the old bounded source registry before the existing state pass rebuilds it.

Ownership loss, an invalid stored owner, active Fallout, or an active Fallout transition invalidates the delayed result. The existing Fallout snapshot freezes the Air Winter gameplay row before pending-branch cleanup. It does not consume the new identity hook.

## Assets and localisation

Both blocks use a dedicated Fallout-owned report sprite, `GFX_report_event_air_winter_island_refugee_harbor`. The fictional documentary scene shows a small island harbor or improvised anchorage under cold rain, crowded civilian boats, a patrol launch, quarantine sheds, dim light, and winter surf. It uses no zombie image, audio, sprite, file, or path.

The source PNG, processed PNG, final DDS, `.gfx` registration, manifest row, and contact-sheet update are part of the same implementation tranche.

Localisation must name the source state and country, landing water, patrol craft, quarantine sheds, food stores, and household pressure. A harbor description can be used when a naval base exists, while an anchorage description covers an island without one. Government-aware authority terms remain dynamic. The text must not imply that naval exclusion leaves every passenger at sea.

## Proof boundary

Static proof can establish the official state scopes for both island triggers and `add_manpower`, bounded source collection, deterministic source comparison, exact balanced population transfer, proportional ceilings, branch exclusivity, target retention structure, cleanup coverage, deterministic result partition, asset wiring, and localisation coverage. It can also record known topology exceptions. Static inspection does not prove the complete live truth set of the island predicates.

Without running HOI4, runtime popup presentation, save and reload behavior, delayed regular-target propagation, AI selection frequency, multiplayer host behavior, and live population display updates remain unobserved. The user has explicitly prohibited running HOI4, so the proof document must retain that boundary.

## Review record

The design and balance review accepted the revised branch costs, population shares, pressure ceilings, deterministic result thresholds, and AI plausibility boundaries.

The engine review accepted the exact topology predicates, bounded source-country registry, regular-target chain structure, state-scope positive population effect, and exact source population transaction. It retained the documented runtime proof boundary.

The route and identifier review accepted event ids 38 and 39, the mountain-capital precedence, the same-phase island score bonus, first-frost participation, and the expected post-tranche block and option counts.

The source-transaction review accepted the positive-transfer commit rule, stale-offer rollback, exact applied-output handoff, protected source remainder, receipt cleanup, and durable origin memory.

## Implementation record

Events 38 and 39, their constants, triggers, source registry, transaction helpers, pending-chain cleanup, localisation, dedicated sprite, source PNG, processed PNG, DDS, contact sheet, manifest, and handoff are wired. The engine-sensitive implementation record is `AIR_WINTER_PHASE_2_ISLAND_REFUGEE_SOURCE_AND_POPULATION_PROOF.md`.

The runtime boundaries in this addendum remain open. No post-Fallout focus, successor-identity, or migration consumer is claimed.
