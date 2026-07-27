# Spec 64: The Mine Generator

Status: accepted source design for a dormant Fallout implementation tranche. No gameplay implementation or runtime acceptance is claimed by this specification.

The Mine Generator is a Sub-Saharan African regional chain about a resource-bearing settlement whose surviving generator, workshops, workers, and food ledger can no longer support every old obligation. The player chooses whether the works trade for food, compel labor, submit to engineers, or close and shelter the workforce.

The chain is Fallout-owned and uses `chaosx.fallout` only. It is not a super-event, decision category, mission, focus route, bilateral partner, country creation, recurring on-action, scripted GUI, achievement, formable, or map rewrite.

## Identity ledger

| Surface | Assigned value |
| --- | --- |
| Candidate and human opening | `642` |
| Hidden-AI opening | `643` |
| Human delayed result | `644` |
| Hidden-AI delayed result | `645` |
| Human operating-season callback | `646` |
| Hidden-AI operating-season callback | `647` |
| Authenticated cleanup | `648` |
| Transaction key | `710063` |
| Scheduler route | `7163` |
| Required new route upper bound | `7164` |
| Event Log history | `9169` |
| Catalogue identity | `FALLOUT-642` |
| Report asset identity | `fallout_mine_generator` |

The reservation is collision-free in the current Fallout namespace and ledgers. Raw `7163` and `9169` values elsewhere are unrelated province, hash, or subsystem values and do not own the Fallout route or Event Log history domains.

The row remains dormant while `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` are unset.

## Scheduling identity

- Runtime region: `fallout_region.sub_saharan_africa`
- Primary family: `fallout_event_primary_family.regional_and_biome`
- Preferred phase: `fallout_event_phase.first_season`
- Secondary phase: `fallout_event_phase.first_winter_year`
- Class: `fallout_event_class.routine_incident`
- Cooldown family: `fallout_event_cooldown_family.food_security`
- Primary and required resource index: `fallout_survival_resource.food`
- Visible budget cost: `2`
- Result delay: `42` days
- Callback delay: `270` days after result settlement

The candidate mechanic pressure is the inverse of the selected state's current Food reserve, the candidate severity is current Exposure, and the state-value receipt is current Supply Access. The implementation must calculate inverse Food with normal temporary-variable subtraction rather than unary negation.

## Country admission

The country must have a current Fallout country identity, durable resource row, current generation, exact Sub-Saharan African regional row, ordinary-event eligibility, campaign day from `300` through `2599`, no committed or closed Mine Generator memory, no conflicting ordinary transaction, and at least one affordable branch.

The reviewed country floors are:

| Surface | Minimum |
| --- | ---: |
| Food | `12` |
| Power | `18` |
| Scrap | `10` |
| Fuel | `8` |
| Recognition | `8` |
| Cohesion | `20` |

The affordability gate must evaluate the exact branch costs against current values before the row is appended. The opening must revalidate the same costs before payment.

## Engine-exposed state target

The producer scans owned states and selects the lowest native state id that satisfies every requirement below:

- The requesting country owns and controls the state.
- The state has the current Fallout generation and durable state row.
- The state has a produced Air Winter snapshot for the current generation.
- The state retains at least `3k` surviving population.
- Non-damaged native infrastructure is at least `1`.
- Current Supply Access is at least `15`.
- Current Reclamation is at least `8`.
- Current Food reserve is at least `5` and no more than `45`.
- Current Exposure is below `75`.
- Current Disease Pressure is below `65`.
- No Mine Generator completion memory or exclusive state reservation is present.
- At least one native `steel`, `tungsten`, `chromium`, `aluminium`, or `coal` resource count is above zero.

The installed `triggers_documentation.md` documents the resource-count trigger for both STATE and COUNTRY scopes and lists `oil`, `aluminium`, `rubber`, `tungsten`, `steel`, `chromium`, and `coal` as supported resource identities. This chain deliberately admits only the five mineral or coal identities above. Oil belongs to the separate fuel and pipeline design space, while rubber does not prove a mine.

The implementation should isolate the direct resource comparison in `fallout_event_642_state_has_native_resource_work = yes` and reuse that trigger for admission, result reauthentication, callback reauthentication, and proof. The resource deposit is evidence for an operating resource settlement; the specification does not authorize adding or removing the deposit.

The state target is the only scoped target. The chain creates no partner country, receiving state, province target, route object, mine building, or generator building. Country Power, Scrap, and Fuel represent the surviving generator and machinery inputs.

## Candidate variables and frozen receipt

The producer should own these candidate values:

- `fallout_event_642_candidate_state_id`
- `fallout_event_642_candidate_food`
- `fallout_event_642_candidate_food_pressure`
- `fallout_event_642_candidate_supply`
- `fallout_event_642_candidate_exposure`
- `fallout_event_642_candidate_resource_class`
- `fallout_event_642_candidate_phase`

The resource class uses a fixed display priority when more than one admitted deposit exists: coal, steel, tungsten, chromium, then aluminium. This class is localisation and Event Log evidence only and never changes the native resource.

Before payment, freeze the generation, owner, controller, target state id, selected resource class, branch, human or AI mode, event token, transaction key, route, result ticket, callback ticket, population, infrastructure, Supply Access, Food reserve, Adaptation, Reclamation, Exposure, Disease Pressure, country Food, Power, Scrap, Fuel, Shelter Capacity, Medicine, Recognition, Cohesion, Stability, and War Support.

The result grade consumes the frozen receipt. The callback consumes the already-settled policy and current authenticated state values and must not recalculate the original grade.

## Four authored branches

### Trade Mineral Shares

Trade Mineral Shares spends Power `3`, Scrap `2`, and Recognition `2`.

The settlement promises a bounded share of future output in exchange for current food and repair inputs. Success raises Food, Recognition, worker trust, and extraction continuity while increasing foreign concession pressure. Partial success creates a food debt without stabilizing the full shift. Failure raises food debt and concession pressure and reduces Cohesion.

### Conscript the Labor Shift

Conscript the Labor Shift spends Food `3`, Fuel `2`, and Command Power `10`.

The garrison extends the working day and guards the stores. Success raises short-term extraction continuity and military control but reduces worker trust and Cohesion. Partial success leaves both output and coercion high. Failure creates a stoppage, raises Exposure and Disease Pressure, and may damage infrastructure.

The branch does not create a unit, occupation law, forced-labor decision category, or country leader.

### Establish Engineer Rule

Establish Engineer Rule spends Power `4`, Scrap `3`, and Recognition `2`.

The maintenance board receives authority over generator time, workshop access, ration priority, and safety shutdowns. Success raises engineer authority, Supply Access, Reclamation, and worker trust. Partial success improves machinery while leaving the food ledger unresolved. Failure raises food debt and reduces Power without changing government archetype.

### Evacuate the Works

Evacuate the Works spends Fuel `4`, Shelter Capacity `3`, and Medicine `2`.

Workers leave the exposed work face and move into authenticated shelter inside the same state. Success lowers Exposure and Disease Pressure and raises evacuation readiness and worker trust while reducing extraction continuity. Partial success closes only the most dangerous section. Failure represents a disordered withdrawal and may request bounded Deaths.

This branch performs no cross-state population transfer and selects no receiving state.

Human tooltips must disclose each cost, the 42-day result timing, the affected state, and the branch's principal risk. Unaffordable branches remain hidden for the human lane and receive invalid AI priority.

## Grade contract

The result combines frozen Food, Power, Scrap, Recognition, Cohesion, Supply Access, Reclamation, Exposure, Disease Pressure, infrastructure, the admitted native-resource receipt, and the branch ledger bonus into one clamped viability score.

| Branch | Success threshold | Partial threshold |
| --- | ---: | ---: |
| Trade Mineral Shares | `60` | `40` |
| Conscript the Labor Shift | `64` | `44` |
| Establish Engineer Rule | `62` | `42` |
| Evacuate the Works | `58` | `38` |

The callback succeeds at `64`, is partial from `42`, and fails below `42`.

Result and callback effects may adjust Food, Power, Scrap, Fuel, Recognition, Cohesion, Stability, War Support, Supply Access, Reclamation, Exposure, Disease Pressure, infrastructure, and a branch-specific local resource-efficiency modifier.

Result failure may damage one native infrastructure level and then one present industrial complex if infrastructure cannot be damaged. It must not invent a damaged target, remove a native resource deposit, or damage an unrelated building as a substitute.

Result failure may request `0.0015` of the authenticated state population through `apply_exact_state_civilian_population_loss`. Callback failure may request `0.0007`. Both requests use the Fallout aftermath cause and the minimum remaining population contract.

## Durable branch ledgers

All ledgers are country-scoped and clamped from `0` through `100`.

| Ledger | Initial value | Primary consumers |
| --- | ---: | --- |
| Extraction continuity | `35` | Result output, callback output, local resource modifier |
| Food debt | `30` | Callback grade, Food changes, concession risk |
| Worker trust | `35` | Cohesion, callback grade, stoppage risk |
| Labor coercion | `10` | Military branch, callback unrest, War Support |
| Engineer authority | `20` | Maintenance, Supply Access, Reclamation |
| Evacuation readiness | `15` | Exposure, Disease Pressure, closure outcome |
| Foreign concession pressure | `10` | Recognition, food credit, later diplomacy memory |

Branch settlement applies these directional ledger changes before the result grade is locked:

| Branch | Ledger direction |
| --- | --- |
| Trade | Extraction `+3`, Food debt `-8`, Worker trust `+2`, Concession pressure `+10` |
| Labor | Extraction `+10`, Food debt `-3`, Worker trust `-10`, Labor coercion `+12` |
| Engineers | Extraction `+7`, Food debt `-2`, Worker trust `+3`, Engineer authority `+12` |
| Evacuation | Extraction `-8`, Food debt `+2`, Worker trust `+8`, Evacuation readiness `+15`, Concession pressure `-3` |

Successful cleanup preserves the ledgers and the selected resource-class memory. Transaction-only frozen values, payments, tickets, and reservations are always cleared.

## Operating-season callback

The callback is scheduled exactly 270 days after result settlement and represents the next operating season, ration account, or closure inspection.

The callback authenticates the same state and reads current Food reserve, Supply Access, Reclamation, Exposure, Disease Pressure, infrastructure, country Food, Power, Cohesion, and the seven durable ledgers. It produces one of three outcomes:

- A stable works compact when the score succeeds.
- A rationed or reduced shift when the score is partial.
- A stoppage, concession crisis, coercive mutiny, or failed withdrawal according to the settled branch when the score fails.

The callback closes the chain after one review. It does not install a recurring scheduler, yearly pulse, decision category, or on-action.

## Hidden-AI behavior

Human and hidden-AI lanes use the same admission, affordability, payment, frozen grade, result, callback, Event Log, and cleanup effects.

- Continuity Government and Food Compact prefer Trade Mineral Shares.
- Warlord Command prefers Conscript the Labor Shift during war, low Food, or weak Cohesion.
- Technate, Machine Protocol, and Scavenger Syndicate prefer Establish Engineer Rule when Power and Scrap are sufficient.
- Quarantine State, Religious Refuge, Mutant Polity, and Bunker Authority prefer Evacuate the Works when Exposure or Disease Pressure is high.
- Nomad Convoy prefers Trade Mineral Shares and then Evacuate the Works.
- Maritime Remnant prefers Trade Mineral Shares when Recognition is affordable and otherwise Establish Engineer Rule.

The deterministic tie order is Trade, Engineers, Evacuation, then Labor. Every unaffordable or invalid branch receives the reviewed invalid priority of `-1000`. No `random_list`, MTTH, or probability pool is required.

## Event Log contract

History `9169` records explicit opening choice, branch-specific success, partial, and failure, callback success, partial, and failure, and cancellation payloads.

The country is the primary actor. The authenticated state is the secondary actor. The selected native resource class may appear through dedicated scripted localisation, but no Event Log text may claim a specific company, union, people, commodity grade, or political institution without a country-memory receipt.

The authoritative workbook is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. The workbook should be updated only after gameplay and player-facing wording are final, followed by `python .tools/export_event_catalog_csv.py`. The export CSV files must not be edited directly.

## Cleanup and refund proof

The result, callback, and cleanup reauthenticate:

- Candidate `642`
- Transaction `710063`
- Route `7163`
- Current generation
- Country registry identity
- Owner and controller
- Target state id
- Selected resource class
- Branch and human or AI mode
- Expected event token
- Result ticket
- Callback ticket
- Cost-paid receipt
- Result-commitment receipt

Stale generation, ownership, control, state identity, native-resource evidence, event token, or delayed ticket cancels only transaction `710063`.

Cancellation records history `9169`, refunds only a payment whose result was not committed, releases the exact state reservation, clears only this transaction's frozen and transient values, and does not clear a newer transaction or replacement generation.

Focused proof must cover generation reset before result, ownership loss before result, control loss before callback, loss of the native-resource admission receipt, duplicate result delivery, duplicate callback delivery, duplicate cleanup, paid-but-uncommitted refund, committed no-refund, and replacement-transaction survival.

## Asset contract

The dedicated workspace is `docs/assets/642_mine_generator/`.

Required outputs are `source_generated.png`, `processed_210x176.png`, `manifest.json`, `README.md`, `handoff.md`, and the final DDS.

The report sprite is `GFX_report_event_fallout_mine_generator`. The runtime texture is `gfx/event_pictures/fallout_world_end/report_event_fallout_mine_generator.dds` at `210x176`.

The image should be a fictional period-documentary scene of a Sub-Saharan African resource settlement under ash-darkened light, with a generator shed, ore carts or stockpiles, workers around a ration ledger, guarded machinery, and visibly sparse food stores. The treatment is black-and-white with restrained sepia.

The image must not contain readable text, modern branding, a real flag, an identifiable real person, borrowed zombie imagery, or reused zombie paths. No animation, portrait, audio, achievement icon, super-event card, 3D model, or alternate route frame is warranted.

## Deliberate limits and proof boundary

This tranche must not create a mine building, generator building, resource deposit, partner country, receiving state, company, union, successor tag, government archetype change, claim, core, focus route, decision category, scripted GUI, or recurring scheduler.

Specific political, ethnic, linguistic, labor, company, union, or mining-history references require later country-memory research. Generic regional localisation must not present Sub-Saharan Africa as one undifferentiated polity or resource economy.

Static review can prove identity uniqueness, direct state-resource trigger ownership, deterministic state selection, branch affordability, delayed-ticket authentication, refund rules, localisation coverage, Event Log routing, asset geometry, and the absence of scheduler activation setters.

Live scheduler dispatch, delayed queue delivery, invalid-target behavior, Event Log rendering, save recovery, multiplayer delivery, host authority, and player-visible art remain unobserved until the user validates them in HOI4.

The installed package has no Technology Tree Viewer. This chain touches no technology or doctrine tree, so that limitation creates no implementation substitute or completion claim.

## Future consumers

Later successor-country or diplomacy tranches may consume the durable food-debt, worker-trust, engineer-authority, or concession-pressure memories. They require their own accepted specs, country-memory research, target proof, ids, assets, and cleanup.

The Mine Generator itself stops after one callback.
