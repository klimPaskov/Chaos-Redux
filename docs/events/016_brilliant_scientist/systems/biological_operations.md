# Biological operations and native-raid ownership

Event 016 biological warfare uses the shared CBRN equipment and disease systems. Actual equipment in the national stockpile is the only payload quantity source. No Event 016 numeric stockpile or parallel reservation ledger exists.

## Unlock and selection contract

The compact `brilliant_scientist_biological_operations_category` appears after the country owns at least one authorized agent. Anthrax, plague, tularemia, and smallpox accept either their completed native special project or their grantable delivery technology. Weaponized zombies accept their delivery technology, completion flag, or special project. Black Plague accepts its completed weaponization program or an explicit Kruger authorization receipt.

One persistent country variable, `brilliant_scientist_selected_biological_agent`, records the operational agent used by Event 016 production and decision-led deployments. The selection can be changed while no Event 016 biological production or deployment transaction is active. Changing this selection does not modify an active native raid, because native raids already own their selected payload and reservation.

## Production and staging

`brilliant_scientist_produce_single_biological_payload` takes 30 days, uses two civilian factories, 80 Support Equipment, and 250 manpower, and produces one native payload lot of the selected agent. `brilliant_scientist_produce_triple_biological_payload` takes 60 days, uses four civilian factories, 240 Support Equipment, and 750 manpower, and produces three lots. The output is the actual native equipment type: `anthrax_bomb_1`, `plague_bomb_1`, `tularemia_bomb_1`, `smallpox_bomb_1`, or `zombie_disease_bomb_1`. Black Plague uses one plague-bomb item per lot, matching its shared Event 020 delivery contract.

`brilliant_scientist_stage_biological_operations` takes 90 days and uses one civilian factory. It reserves no payload. Completion grants a 180-day readiness window which improves native strategic, battlefield, and zombie raid success calculations and increases AI willingness. It also shifts Event 016 decision-led deployment weights toward success and away from failure or accident.

Production and staging check available project factories before selection and use the native timed-decision factory modifier for occupation and release.
The production callback is private to those decisions, not a free-standing public grant API.
If authorization disappears during production, its receipt is cleared without producing a payload or refunding already committed support equipment and manpower.
Cancelling staging clears its active receipt without granting readiness.
The native raid preparation duration itself remains native-owned; staging is advance preparation that improves the outcome profile rather than an override of that timer.

## Independent deployment transaction

`brilliant_scientist_battlefield_biological_release` targets an enemy-controlled frontline or operational state. It lasts seven days, spends 25 Command Power, and debits one selected payload lot at start.

Operational Teleportation extends that same decision to other enemy-held states for ten `teleportation_equipment_1` items.
Conventional targets never pay this extra cost.
The transport amount is stored alongside the payload receipt, and pending validity reads that committed amount rather than requiring another ten items in the unreserved stockpile.
Losing conventional access cannot silently convert an unpaid operation into a Portal deployment.
Cancellation returns both the payload and any committed transport exactly once; every settled Portal attempt records permanent actor and target history without creating a Portal raid or beachhead.

`brilliant_scientist_strategic_covert_biological_release` targets an enemy core industrial or strategic state. It lasts fourteen days, spends 50 Command Power, and debits two selected payload lots at start. Its consequences and exposure risk are stronger.

Both decisions use one Event 016-owned receipt containing the selected agent, route, target state, victim country, and exact debited amount. A target that becomes invalid before execution refunds that receipt exactly once. Success, failure, and accident settle it exactly once. Failure consumes the committed payload; an accident releases it at the actor's capital. These receipts are separate from native raid reservations and can never refund or settle a native raid payload.

The shared world-end flag prevents new releases and invalidates pending releases so their decision cancellation returns the committed equipment.
Capitulation refunds a pending decision reserve from `on_capitulation_immediate`, before native equipment capture, and clears unfinished production and staging receipts.
Direct annexation instead transfers any still-reserved payload and Portal transport to the annexing country, then clears the former actor's receipt; native stockpile capture cannot already contain those debited items.
If capitulation already settled the reserve, annexation and subsequent decision callbacks have nothing left to award.
Production inputs already consumed remain consumed, and no unfinished production output or staging readiness is awarded.
Production and staging cannot begin or pay out after capitulation or the shared world-end state.
Their native timed decisions cancel when the active country or their own receipt becomes invalid, so cleared transactions do not keep factories occupied until the old timer expires.

The target must remain owned and controlled by the original victim throughout the operation.
Ownership passing to another belligerent cancels the original operation rather than silently changing the victim.
The start effects recheck the requested route, agent, payload, Command Power, and target before creating a receipt.
Targets exclude wasteland, zero-population states, and states already controlled by zombies.
The ordinary-pathogen dispatcher must accept the seed before the operation records successful delivery.
If the dispatch rejects execution, the attempted operation settles as a consumed-payload failure without delivery-success history or a success-only Directorate Exposure award.

Standard pathogens dispatch into `bio_lifecycle_dispatch_seed` with explicit actor, victim, actual payload debit, and one internal-use history receipt.
The lifecycle owns subsequent detection, attribution, and condemnation; an operational success is not fabricated public confirmation.
Weaponized zombies use the existing outbreak creator, and only a deliberate successful release invokes the strike-consequence effect.
An attacker accident cannot grant the confirmed-offensive-use history.
Black Plague uses the ordinary plague lifecycle plus `black_plague_apply_weaponized_exposure_runtime`; it does not call the Event 020 public delivery effect and therefore cannot debit the same payload twice.
The runtime bridge initializes Event 020 only when its shared runtime has never started, applies the accepted weaponized exposure once, and creates or repairs one event-owned seven-day scheduler receipt without inventing a natural origin or recognition report.
The bridge exports an exact acceptance result, so Event 016 records Black Plague provenance and delivery history only when the shared state machine accepted the selected state.

## Native raid authority

The native strategic, battlefield, and zombie raids remain authoritative for preparation, equipment reservation, cancellation, expiry, outcome selection, refund, history, contamination, condemnation, and confirmed-use attribution. Their visibility accepts API-granted delivery technologies as well as project completion. Warren Kruger's active host or KRG receives aggressive AI weights, but Kruger is not a player-access requirement and does not create a separate raid system.

## Runtime identifiers

- Category: `brilliant_scientist_biological_operations_category`
- Selection variable: `brilliant_scientist_selected_biological_agent`
- Query root: `brilliant_scientist_has_any_unlocked_biological_agent`
- Production effects: `brilliant_scientist_begin_biological_production`, `brilliant_scientist_complete_biological_production`
- Staging effects: `brilliant_scientist_begin_biological_staging_directive`, `brilliant_scientist_complete_biological_staging_directive`
- Transaction effects: `brilliant_scientist_begin_biological_deployment`, `brilliant_scientist_refund_biological_deployment`, `brilliant_scientist_resolve_biological_deployment`
- Transaction flag: `brilliant_scientist_biological_deployment_pending`
- Native readiness flag: `brilliant_scientist_biological_staging_ready`

## Public stockpile query

The country-scoped pair `brilliant_scientist_calculate_selected_biological_payload_requirement` and `brilliant_scientist_selected_biological_stockpile_is_sufficient` lets another system price the selected operational agent without reserving equipment.
The calculation reads the persistent selected agent and temporary `brilliant_scientist_biological_payload_multiplier`, then writes temporary `brilliant_scientist_biological_agent_request` and `brilliant_scientist_biological_payload_required`.
An absent or nonpositive multiplier uses one lot; an invalid agent yields zero, which the stockpile query rejects.
The query reads the calculated requirement and the actual matching native equipment stockpile, requires the selected agent to remain unlocked, and changes no flags, stockpiles, history, or native raid state.
Callers must calculate and query in the same effect chain and must not treat a positive result as a reservation.

```txt
set_temp_variable = { brilliant_scientist_biological_payload_multiplier = 1 }
brilliant_scientist_calculate_selected_biological_payload_requirement = yes
# In the immediately following limit/trigger block:
# brilliant_scientist_selected_biological_stockpile_is_sufficient = yes
```

Production, staging, and deployment start/finish helpers remain private callbacks of their owning decisions.
Other events grant access through the technology API and let those decisions own their transactions; they must not call a private production callback to bypass the native factory occupation.

## Black Plague elapsed timing

Black Plague state devastation uses `black_plague_next_devastation_num_days` on the elapsed-day axis `global.num_days`.
Its event-owned pulse scheduler likewise stores `black_plague_scheduler_due_num_days` on `global.num_days`, keeping the delayed `.900` callback and its validation receipt in the same unit.
The shared phase-dependent intervals and once-per-pulse application remain authoritative; calendar snapshots used for history are not deadlines.

## Visual assets and sprite wiring

The category is registered in `common/decisions/categories/016_brilliant_scientist_raid_lifecycle_categories.txt` and reuses `GFX_decision_category_brilliant_scientist_krg_exotic_biological` from `interface/016_brilliant_scientist_kruger_state_decisions.gfx`.
The actions reuse the registered Event 016 Biological Weapons icons in `interface/016_brilliant_scientist_project_icons.gfx`: `GFX_decision_brilliant_scientist_project_biological_weapons_theory`, `GFX_decision_brilliant_scientist_project_biological_weapons_prototype`, `GFX_decision_brilliant_scientist_project_biological_weapons_deployment`, and `GFX_decision_brilliant_scientist_project_biological_weapons_weaponization`.
Native payload equipment and raid icons remain owned by their shared CBRN and zombie registries.
These existing generated assets cover the transaction surface without another scripted GUI.

## Future extensions

Future events can authorize one of the native delivery technologies or call the existing custom-technology API, then use the same stockpile and native-raid surfaces. A future operation may add its own transaction only when it owns a distinct decision-led deployment and stores its own exact debit/refund receipt. It must never reuse Event 016's pending flag or intercept a native raid reservation.
