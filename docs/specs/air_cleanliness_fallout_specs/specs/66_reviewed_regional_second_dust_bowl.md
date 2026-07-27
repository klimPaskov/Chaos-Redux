# Spec 66: The Second Dust Bowl

Status: accepted source design for a dormant Fallout implementation tranche. No gameplay implementation or runtime acceptance is claimed by this specification.

The Second Dust Bowl is a North American plains crisis about wind erosion, improvised field shelter, and farm households deciding whether to protect the soil, move the farm, seed cold crops, or leave the open plain. It is fictional Fallout content. It does not claim a named historical district, Indigenous institution, provincial agency, or real Dust Bowl archive without a separate research receipt.

The chain is Fallout-owned and uses `chaosx.fallout` only. It is an ordinary crisis incident, not a super-event, decision category, mission, focus route, bilateral partner, country creation, recurring on-action, scripted GUI, achievement, formable, or map rewrite.

## Identity ledger

| Surface | Assigned value |
| --- | --- |
| Candidate and human opening | `656` |
| Hidden-AI opening | `657` |
| Human delayed result | `658` |
| Hidden-AI delayed result | `659` |
| Human planting-season callback | `660` |
| Hidden-AI planting-season callback | `661` |
| Authenticated cleanup | `662` |
| Transaction key | `710065` |
| Scheduler route | `7165` |
| Required new route upper bound | `7166` |
| Event Log history | `9171` |
| Catalogue identity | `FALLOUT-656` |
| Report asset identity | `fallout_second_dust_bowl` |

The reservation is collision-free in the current Fallout namespace and ledgers. Raw `7165` and `9171` values elsewhere are unrelated province, subsystem, or upper-bound values and do not own this candidate.

The row remains dormant while `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` are unset.

Implementation evidence is recorded in `docs/plans/air_cleanliness_fallout_plans/FALLOUT_SECOND_DUST_BOWL_PROOF.md`. That proof records source surfaces and completion blockers only. It does not promote this accepted design to runtime acceptance, scheduler activation, or a claim that Hearts of Iron IV has been launched.

The current implementation review records repaired opening-target rehydration, scoped result-variable access, callback ledger coverage, AI state-pressure scope, dynamic-modifier localisation, branch-preparation grading, and committed-row cleanup after same-generation target drift. Pre-result stale cancellation, generation drift, and runtime engine acceptance remain open implementation boundaries. Those findings do not alter this accepted source design.


## Scheduling identity

- Runtime region: `fallout_region.north_america`
- Primary family: `fallout_event_primary_family.regional_and_biome`
- Preferred phase: `fallout_event_phase.first_winter_year`
- Secondary phase: `fallout_event_phase.consolidation`
- Class: `fallout_event_class.crisis_incident`
- Cooldown family: `fallout_event_cooldown_family.climate`
- Primary and required resource index: `fallout_survival_resource.food`
- Visible budget cost: `3`, covering the opening, delayed result, and planting callback.
- Result delay: `35` days
- Callback delay: `240` days after result settlement

Candidate pressure is the selected state's current Dust Load and inverse Food reserve. Candidate severity is current Exposure. The state value receipt is current Supply Access. The implementation must calculate inverse Food with temporary-variable subtraction and must not use unary negation.

## Country admission

The country must have a current Fallout country identity, durable resource row, current generation, exact North American regional row, ordinary-event eligibility, campaign day from `365` through `1599`, no committed or closed Second Dust Bowl memory, no conflicting ordinary transaction, and at least one affordable branch.

| Surface | Minimum |
| --- | ---: |
| Food | `14` |
| Clean Water | `10` |
| Scrap | `10` |
| Fuel | `8` |
| Power | `6` |
| Shelter Capacity | `12` |
| Recognition | `6` |
| Cohesion | `20` |

The candidate producer must evaluate exact branch costs before appending the row. Human and hidden-AI scheduling must recheck the selected branch affordability before payment.

## Engine-exposed state target

The producer scans owned states and selects the lowest native state id that satisfies every requirement below:

- The requesting country owns and controls the state.
- The state has the current Fallout generation and durable state row.
- The state has a produced Air Winter snapshot for the current generation.
- The native state terrain is `plains`.
- The pretransition category is rural, pastoral, or town.
- The state retains at least `3k` surviving population.
- Native infrastructure is above zero and is not already damaged beyond the accepted entry condition.
- Current Supply Access is at least `10`.
- Current Adaptation is from `8` through `55`.
- Current Reclamation is below `65`.
- Current Exposure is from `20` through `75`.
- Current Disease Pressure is below `65`.
- Current Food reserve is from `5` through `40`.
- No Second Dust Bowl completion memory or exclusive state reservation is present.

The plains trigger and current state ledgers prove the target. The implementation must not infer a named historical Dust Bowl district and must not invent a province, receiving state, country tag, or partner.

## Candidate variables and frozen receipt

The producer owns candidate state id, Food pressure, Dust Load, Supply Access, Adaptation, Reclamation, Exposure, Disease Pressure, and phase values. Before payment, freeze generation, owner, controller, target state id, terrain, category, branch, human or AI mode, event token, transaction key, route, result ticket, callback ticket, population, infrastructure, Supply Access, Food, Adaptation, Reclamation, Exposure, Disease Pressure, country Food, Clean Water, Scrap, Fuel, Power, Shelter Capacity, Medicine, Recognition, Cohesion, Stability, and War Support.

The result grade consumes the frozen receipt. The callback consumes the settled policy and current authenticated state values. It must not recalculate the original result grade.

## Four authored branches

### Shelter the Fields

Spend Scrap `4`, Fuel `2`, and Shelter Capacity `2`.

Families and crews build windbreaks, cover seed rows, and move livestock into authenticated field shelter. Success raises Topsoil Retention, Windbreak Coverage, Adaptation, and Reclamation. Partial success protects the inner plots while the outer fields continue to lose soil. Failure reduces Food and infrastructure and raises Dust Load, Exposure, and Disease Pressure.

### Move the Farms

Spend Fuel `4`, Food `2`, and Shelter Capacity `3`.

Farm households consolidate into protected parcels inside the same authenticated state. Success raises Farm Mobility and Supply Access without transferring population to another state. Partial success moves only the most exposed plots. Failure strands equipment, reduces Food, and increases Displacement Pressure.

### Seed Cold Crops

Spend Food `4`, Scrap `2`, and Power `2`.

The settlement turns its remaining seed stores toward cold-tolerant crops. Success raises Cold-Crop Adoption and later Food potential. Partial success saves a seed reserve but leaves the first planting thin. Failure consumes the allocation, lowers Food, and raises Dust Load without adding Air Contamination.

### Abandon the Open Plains

Spend Fuel `3`, Shelter Capacity `4`, and Medicine `2`.

The country shelters households inside the authenticated plains state and closes the most exposed fields. Success reduces Exposure and Disease Pressure and raises Shelter Capacity while sacrificing Food output. Partial success closes only the outer plots. Failure leaves a disordered withdrawal, reduces Food and Reclamation, and may request bounded Deaths.

Human tooltips must disclose each cost, the 35-day result timing, the affected state, and the branch risk. Unaffordable branches remain hidden for the human lane and receive invalid AI priority.

## Grade contract

The result combines frozen country Food, Clean Water, Scrap, Fuel, Power, Shelter Capacity, Medicine, Recognition, Cohesion, Stability, state Food, Adaptation, Supply Access, Reclamation, infrastructure, inverse Exposure, inverse Disease Pressure, Dust Load, and branch ledger bonus into one clamped viability score.

| Branch | Success threshold | Partial threshold |
| --- | ---: | ---: |
| Shelter the Fields | `60` | `40` |
| Move the Farms | `62` | `42` |
| Seed Cold Crops | `64` | `44` |
| Abandon the Open Plains | `58` | `38` |

The callback succeeds at `63`, is partial from `41`, and fails below `41`.

Result and callback effects may adjust Food, Supply Access, Adaptation, Reclamation, Exposure, Disease Pressure, infrastructure, Cohesion, Stability, War Support, and branch-specific country or state modifiers. The chain must not write a natural-disaster contamination source, add Air Contamination, change the native state category, or transfer population between states.

Result failure may damage one native infrastructure level. It must not invent a damaged target or damage an unrelated building as a substitute. Result failure may request `0.0014` of the authenticated state population through `apply_exact_state_civilian_population_loss`. Callback failure may request `0.0006`. Both use the Fallout aftermath cause and the minimum remaining population contract.

## Durable ledgers

All ledgers are country-scoped and clamped from `0` through `100`.

| Ledger | Initial value | Primary consumers |
| --- | ---: | --- |
| Topsoil Retention | `30` | Shelter result and callback Food potential |
| Windbreak Coverage | `10` | Exposure and Reclamation |
| Farm Mobility | `10` | Move the Farms and migration pressure |
| Cold-Crop Adoption | `10` | Seed result and later recovery |
| Displacement Pressure | `15` | Abandon result and migration memory |
| Rural Trust | `35` | Cohesion and callback grade |
| Dust Load | `50` | Candidate pressure and callback grade |

The accepted design requires branch settlement to apply ledger changes before the result grade is locked. The opening now applies a small branch-preparation delta to the frozen ledger score before grading, then applies the settled outcome delta to the durable ledgers. Successful cleanup preserves these memories while clearing only transaction receipts, frozen values, payment flags, reservations, and transient ownership state.

## Planting-season callback

The callback is scheduled exactly 240 days after result settlement. It reads current Food, Supply Access, Adaptation, Reclamation, Exposure, Disease Pressure, infrastructure, Cohesion, and the seven durable ledgers. It produces a protected planting season, a partial field recovery, or a failed soil reserve according to the settled branch and current state.

The callback closes the chain after one review. It does not install a recurring scheduler, yearly pulse, decision category, or on-action.

## Hidden-AI behavior

Human and hidden-AI lanes use the same admission, affordability, payment, frozen grade, result, callback, Event Log, and cleanup effects.

- Continuity Government, Bunker Authority, and Scavenger Syndicate prefer Shelter the Fields when Scrap is affordable.
- Food Compact, Technate, and Machine Protocol prefer Seed Cold Crops when Food and Power are strong.
- Nomad Convoy and Maritime Remnant prefer Move the Farms.
- Warlord Command prefers Move the Farms during war and Shelter the Fields otherwise.
- Quarantine State, Religious Refuge, and Mutant Polity prefer Abandon the Open Plains under high Exposure or Disease Pressure.
- Tie order is Shelter, Cold Crops, Move, Abandon.
- Every invalid or unaffordable branch receives `-1000`. No randomness or MTTH is used.

## Event Log and assets

History `9171` records the four opening choices, twelve result payloads, three callback payloads, and authenticated cancellation. The country is the primary actor and the authenticated plains state is the secondary actor. The authoritative workbook is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Update it only after gameplay and player-facing wording are final, then run `python .tools/export_event_catalog_csv.py`.

Current implementation evidence lists exported row `FALLOUT-656` at `docs/spreadsheets/chaos_redux_events_catalog.csv:613` with `Needs Testing` status. The export covers the four branch choices, twelve result outcomes, three callback outcomes, authenticated cancellation, and visible budget cost `3`. The wording pass removed internal state-variable references and matches the current player-facing terms.

The dedicated asset package is `docs/assets/656_second_dust_bowl/` with sprite `GFX_report_event_fallout_second_dust_bowl` and runtime DDS `gfx/event_pictures/fallout_world_end/report_event_fallout_second_dust_bowl.dds`. The fictional report card shows blowing soil, improvised windbreaks, covered seed rows, trucks, and farm families beneath a cold ash-darkened sky. It contains no famous archival recreation, readable brands, flags, real people, zombie imagery, animation, or audio.

## Cleanup and proof

Result, callback, and cleanup reauthenticate candidate `656`, transaction `710065`, route `7165`, current generation, owner, controller, target state, plains terrain, category, branch, mode, event token, delayed tickets, payment, and commitment receipts. Stale receipts cancel only this transaction, refund only paid but uncommitted costs, release the exact state reservation, and leave newer transactions untouched.

The stale-receipt behavior above remains the accepted cleanup contract. The committed-row cleanup gate uses the generic country registry so same-generation ownership, control, category, or terrain drift can release an already-scheduled cleanup row. Pre-result stale cancellation and generation drift remain explicit implementation blockers until separately repaired and reviewed. The exact engine-native all-valid-province thermonuclear sweep remains outside this chain and is still blocked. The manual Fallout survival contract remains a direct `90` to `95` percent prestrike population-loss band, with the seven-day rewrite reconciling only the remaining grade-specific delta.

Static proof must cover identity uniqueness, plains target selection, separation from False Spring and Orchard memories, exact branch affordability, no contamination or state-category mutation, delayed replay rejection, Deaths wiring, refund and commitment behavior, hidden-AI ordering, Event Log routing, localisation coverage, and DDS geometry. Runtime dispatch, terrain evaluation, save recovery, host authority, multiplayer behavior, Event Log rendering, and player-visible art remain engine-sensitive boundaries until user validation.
