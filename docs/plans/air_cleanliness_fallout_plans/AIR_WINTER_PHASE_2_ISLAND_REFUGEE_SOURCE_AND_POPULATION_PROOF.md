# Air Winter Phase 2 Island Refugee Source and Population Proof

## Proof boundary

This document records the static implementation proof for `chaosx.fallout.38` and `chaosx.fallout.39`. The accepted design contract is `AIR_WINTER_PHASE_2_ISLAND_REFUGEE_EVENT_ADDENDUM.md`. Hearts of Iron IV was not launched.

The chain belongs to the Air Winter pilot. It is not a Fallout living-world event family and does not count toward the 660-block Fallout release floor.

## Engine references

The implementation uses the installed engine and offline references reviewed for this tranche:

- `documentation/triggers_documentation.md` for `is_island_state`, `is_one_state_island`, `is_coastal`, `is_owned_and_controlled_by`, `state_population`, and event-target validation
- `documentation/effects_documentation.md` for `add_manpower`, regular event targets, arrays, delayed events, and `meta_effect`
- `common/collections/collections.txt` for the vanilla state-524 exception comment attached to `is_one_state_island`
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` for regular event-target lifetime across a fired event chain
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` for country and state scope changes
- the existing repository helper `apply_exact_state_civilian_population_loss` for one observed state-population deduction with a protected remainder and an exact applied output

The destination classifier is the exact documented engine topology:

```txt
OR = {
	is_island_state = yes
	is_one_state_island = yes
}
```

This proves the scripted predicate. It does not prove the complete geographic truth set produced by those engine triggers on the live map.

## Bounded source registry

`air_winter_island_refugee_collect_source_candidate` runs from `air_winter_schedule_phase_event` inside the existing monthly state pass. It adds no country-wide or state-wide periodic iterator.

A source state must be initialized, coastal, owned and controlled by its current owner, in Phase 2 through Phase 6, and above the protected 1,000-person remainder. Each source owner keeps one receipt containing:

- source state id
- source score
- current Air Winter cycle id
- source presentation region

The source score is phase multiplied by 1,000 plus current Air Winter pressure. Higher score wins. Lower numeric state id breaks an exact tie. Each owner appears at most once in `global.air_winter_island_refugee_source_countries`.

During bounded owner dispatch, the receiving country compares only that source-owner array. It rejects itself as a source, rejects stale receipts, selects the highest score, and uses lower state id as the exact tie rule. The chosen source country and state are saved as regular event targets. The frozen scalar offer also stores source state, source country, source region, destination state, scheduler family, origin year, and cycle id.

Candidate preparation clears prior source receipts and the array. Dispatch clears the current receipts and array after every receiver has been considered. Full global reset clears the array. Full country reset clears receipts and pending offers.

## Deferred scheduler commit

Event id 38 is a special dispatch transaction. The generic dispatcher does not write the Phase 2 seen flag, consume the first-frost marker, or fire the generic event route before a source is found.

When no live foreign source exists:

- no offer is written
- no cooldown is applied
- no Phase 2 seen flag is written
- no first-frost receipt or marker is consumed
- no event opens

The transient owner candidate is cleared with the rest of the cycle, so a later monthly cycle can select the route again.

When a source exists, dispatch freezes the offer, applies the 46-day country cooldown, and opens event 38. The Phase 2 seen flag and any matching first-frost receipt are committed only after a positive population transfer. A stale or zero transfer clears the offer and cooldown while leaving the phase memory and seasonal marker retryable.

The offer validator uses the persistent global cycle id and year snapshot. It does not require `air_winter_cycle_open`, because the monthly pass closes before a human can resolve the popup. First-frost offers additionally require the original complete marker row. Ordinary offers can coalesce a matching first-frost marker only after the population transaction succeeds.

## Route ordering

Within Phase 2, the mountain-capital classifier remains first. Engine-classified island states route next, before the generic city, coast, regional food, and shelter routes.

The island route adds 131 to the normal phase and pressure score. The proven Air Winter pressure range ends at 130. This makes an island-refugee candidate win against another ordinary Phase 2 candidate owned by the same country while leaving every Phase 3 candidate at least 739 points higher. The same bonus is applied to ordinary and first-frost capture.

## Balanced population transaction

Each option sets a share and ceiling from `air_winter_event_island_refugee`:

| Policy | Destination population share | Ceiling |
| --- | ---: | ---: |
| Rescue | 2 percent | 40,000 people |
| Quarantine | 1 percent | 20,000 people |
| Exclusion | 0.25 percent | 5,000 people |

The transfer helper performs this sequence once:

1. Read the destination state's current `state_population_k`.
2. Convert it to people, multiply by the selected share, and round once.
3. Clamp only to zero and the selected ceiling.
4. Ask the recorded source state to apply that requested loss through `apply_exact_state_civilian_population_loss`.
5. Protect 1,000 people at the source and disable Deaths logging for the migration deduction.
6. Read the helper's exact applied output.
7. Add only that exact positive output to the destination state with state-scope `add_manpower`.

There is no minimum transfer floor. A depleted source can therefore apply less than the requested amount without creating population. The source loses exactly what the destination gains. The migration itself does not enter the Deaths ledger. Later local failure losses at the destination use `air_winter_event_apply_deaths` at the dedicated 0.01 percent rate.

Only a positive applied output may clear and rewrite source, destination, receiver, and source-country memories. It records exact latest arrivals and departures, cumulative country totals, source and receiver identities, source presentation region, and source refugee-pressure relief.

## Choice and result partition

Event 38 has three resource-aware AI choices:

- rescue spends 500 Manpower and 3 Convoys
- quarantine spends 200 Manpower and 15 Support Equipment
- exclusion has no resource gate

Every choice repeats the complete offer and resource validation inside its executed effect. Every positive transfer writes exactly one rescue, quarantine, or exclusion branch, applies its accepted ledgers and Stability effect, refreshes state ownership, commits the offer, and schedules event 39 after 30 days. Every stale validation or zero transfer rolls the offer back.

Event 39 requires the original bound country and state plus exactly one island-refugee branch. Its six visible result options are the complete partition of:

- rescue success and inverse failure
- quarantine success and inverse failure
- exclusion success and inverse failure

The three failure results enter local losses through the Deaths system. Every result writes matching state and country memory, clears the pending island branch, and lets the shared reconciliation clear the generic pending-owner transaction.

## Cleanup and conflict ownership

`air_winter_event_cancel_pending_chain` owns branch cancellation. Monthly pending-chain reconciliation rejects multiple island branches and ownership drift. State reset clears route, entry, quarantine, result, source, receiver, presentation-region, and latest migration memory. Country reset clears receiver and source identity memory, cumulative totals, pending offers, and source receipts. Fallout snapshot cancellation therefore uses the same established pending-chain cleanup surface.

The implementation uses only `chaosx.fallout.38`, `chaosx.fallout.39`, `GFX_report_event_air_winter_island_refugee_harbor`, and dedicated Fallout Air Winter asset paths. It reuses no zombie event id, file, image, audio, sprite, or path.

## Presentation wiring

Both event blocks use `GFX_report_event_air_winter_island_refugee_harbor`, registered in `interface/air_cleanliness_winter.gfx` and backed by:

- `gfx/event_pictures/fallout/report_event_air_winter_island_refugee_harbor.dds`
- `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_island_refugee_harbor_source.png`
- `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_island_refugee_harbor.png`

The localisation names the real source state and country, destination state, harbor or improvised anchorage, patrol craft, landing water, quarantine sheds, food stores, and household pressure. Naval exclusion explicitly retains forced landings for passengers who cannot safely return to sea.

## Independent review

A read-only event-completion audit returned no findings across topology, route precedence, source selection, deferred receipt ownership, population balance, resources, AI, branches, results, Deaths, memory, cleanup, assets, counts, and documentation.

A separate read-only localisation audit crosswalked all 28 event keys and the generalized event 203 notice. It returned no finding for value fidelity, source and destination wording, government-aware terms, punctuation, prose style, encoding, sprite registration, or DDS resolution. It noted that the existing Air Winter neutrality fallback `the crown commissioner` can sound monarchical for some non-aligned tags. That shared wording predates this route and remains a broader presentation refinement.

## Unobserved runtime boundary

Static review does not establish:

- the live geographic truth set of the two island topology triggers
- popup presentation and option layout
- regular event-target retention through a delayed event after save and reload
- the visible state population readback after the balanced transaction
- AI choice frequency across campaign conditions
- simultaneous-host and multiplayer behavior

These remain runtime observation gates because Hearts of Iron IV was not launched.

A refreshed narrow `hoi4.event_inspect` lint request for `chaosx.fallout.38` reached the installed read-only service but returned `ARTIFACT_STORAGE_LIMIT` before producing an artifact or diagnostic. The proof above relies on direct source inspection and the cited engine documentation, not that failed request.

The state and country memories are ready for a later post-Fallout migration, focus, successor, or identity consumer. No such consumer is claimed by this tranche.
