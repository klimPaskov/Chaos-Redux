# CBRN native raid operations

Chemical and biological attacks use the native raid planner under `chemical_raids` and `biological_raids`, both detected with army intelligence.
Chemical air attacks retain their existing native air raids; chemical ground attacks use state targets, an assigned land division, a supply-node origin, a native preparation timer, and one agent-specific payload reservation.
Biological strategic air attacks, battlefield dissemination, supply-chain sabotage, and captured-facility recovery appear under `biological_raids`.
The unrelated Brilliant Scientist portal raid keeps its own category.
Ordinary battlefield biological raids require Theater CBRN Headquarters technology, full Chemical Readiness, battlefield-use authority, and the matching completed agent project.
Their fixed 21-day native preparation is the whole attack preparation; an active Combined CBRN Overmatch headquarters order is not required.

## Operation flow

The player selects a route and target in the raid interface, assigns a qualifying division or aircraft, and starts native preparation.
The raid engine collects `essential_equipment` at creation and allocates the listed Command Power.
Each completed native outcome saves the exact actor, victim, and selected state as chain-local regular event targets, with one marker for each fixed route, agent, and result.
An immediate hidden country event restores actor-country `ROOT`, validates exactly one marker per required family, reconstructs the outcome inputs, and runs the corresponding adapter.
The biological adapters record failed deliveries or dispatch one lifecycle seed; the chemical ground adapter dispatches only successful releases. None of these adapters debits or refunds the reserved payload again.
If the target changes controller, authority is lost, or the native context becomes invalid before completion, the adapter fails closed without selecting another state or applying a release.
Chemical ground outcome text describes the attempted delivery and any viable release, because the native callback's success level can be determined before the actor-country bridge performs its final context check.
No script-side cancellation hook issues a refund.
The installed raid documentation describes collection at creation and outcome effects, but does not specify the exact handling of essential equipment when a player cancels preparation; live-game cancellation behavior remains a user validation point.

The 54 ordinary chemical ground raid IDs cover nine agents across cylinder release, projector barrage, artillery fire plan, and light, medium, and heavy armored delivery.
For each agent, the first three IDs are `chemical_<agent>_<route>_raid`; the nine original `chemical_<agent>_armored_delivery_raid` IDs identify medium armor, and the 18 additional IDs are `chemical_<agent>_<light|heavy>_armored_delivery_raid`.
Each armored variant requires the matching armor battalion and delivery detachment, reserves one matching light, medium, or heavy flame tank chassis, and checks its own tank technology and chassis stock.
The 27 armored entries increase native raid-list density, but each represents a real division and equipment class rather than an interchangeable generic chassis; unavailable classes remain locked by their tech, stock, and assigned-division checks.
`chemical_malodor_phantom_mist_raid` is a separate project-gated malodor cylinder operation that favors disruption over lethal exposure and requires extreme-use authority at preparation and outcome.
Artillery variants reserve the existing shell archetype and require `cbrn_shell_filling_agent` to match the displayed agent; all other variants reserve the exact agent archetype.
The artillery reservation is exactly 121 filled shells: 120 route payload shells plus the pre-existing one-shell support cost, all from the same concrete shell lot.
The native availability gate checks the same 121-shell stock level and the equipment UI displays that complete reservation.
The 12 biological supply-chain raid IDs follow `bio_sabotage_<agent>_<base|theater|terminal>` for Anthrax, Plague, Tularemia, and Smallpox.
Their three doctrine tiers retain distinct preparation and cooldown timings, while successful releases enter the ordinary food, water, and medical supply-chain lifecycle.
Strategic and battlefield biological raids no longer gain AI weight or success bonuses from the retired Brilliant Scientist biological staging flag; their native preparation and assigned formations determine the operation.
The former global `bio_sabotage_operation_in_progress` flag cannot be set by a documented native raid-creation effect, so separate native variants may prepare simultaneously.
Each has its own native payload and Command Power reservation, and each completed result is still resolved only once.
Facility recovery also uses the immediate country-event bridge, retaining its selected site as an exact event target and checking that the site is still controlled by the actor before any ledger transfer, destruction, or accidental release.

## Chemical ground payment and balance

The old decisions debited one of two equipment sets after a separate preparation and also charged Political Power and Chemical Readiness.
Native raids reserve the fixed former shortage-floor equipment set at creation, retain the former route Command Power allocation, and require the former route readiness threshold without a separate readiness debit.
Payload values remain the existing route costs of 40, 70, 120, and 80.

| Route | Old Political Power → native | Old Command Power → native | Old full / shortage equipment → native reservation |
| --- | ---: | ---: | --- |
| Cylinder release | 12 → 0 | 8 → 8 | Masks/decon/instruments/support 8/6/4/12 or 4/3/2/6 → 4/3/2/6, plus 40 exact agent payload |
| Projector barrage | 18 → 0 | 12 → 12 | Masks/decon/instruments/support 12/6/10/12 or 6/3/5/6, plus one projector chassis → 6/3/5/6 and one chassis, plus 70 exact agent payload |
| Artillery fire plan | 24 → 0 | 16 → 16 | Masks/decon/instruments/support 18/14/16/24 or 9/7/8/12, plus one support shell → 9/7/8/12 and 121 filled shells, of which 120 are the chemical payload |
| Armored delivery | 22 → 0 | 15 → 15 | Masks/decon/instruments/support 16/12/14/22 or 8/6/7/11, plus one medium chassis and 10 or 5 motorized equipment → 8/6/7/11, one matching flame chassis, five motorized equipment, plus 80 exact agent payload |

The former armored fuel debit was 15 at full supply or 8 at shortage.
The native route checks at least 8 fuel and a fuel ratio above 0.08 at preparation and launch, and a healthier fuel ratio increases success chance; it does not spend fuel separately.
The fixed shortage-floor reservation and removal of Political Power, readiness, and fuel debits are deliberate rebalance choices under the approved native raid plan.
The former medium route committed a generic `medium_tank_chassis`, while the medium CBRN armored detachment needs `medium_tank_flame_chassis`; the native light, medium, and heavy variants each commit one flame chassis matching the assigned detachment.
Native armored AI divides the route's agent weight across three chassis classes, retaining one shared battlefield outcome adapter and one reservation per selected operation.
Assigned divisions require the corresponding CBRN support detachment or train, whose own unit equipment needs provide protective and route hardware requirements.

## Biological supply-chain payment

The four agent raids retain their original payload, support, and Command Power amounts: Anthrax 10/40/12, Plague 12/50/15, Tularemia 10/40/12, and Smallpox 8/60/20.
The old 50 Political Power decision cost is removed for all four agents.
Native Command Power allocation is the single payment at creation, leaving net Command Power costs of 12, 15, 12, and 20 respectively.
The native sabotage, strategic, and battlefield release adapters set `bio_native_raid_dispatch_in_progress` on the exact actor only while calling the shared biological lifecycle and clear it immediately afterward; the lifecycle skips its legacy integrated-doctrine Command Power recovery during that flag.
Legacy nonnative biological seeds retain their existing doctrine recovery.
The eight shared `bio_sabotage_raid_{failure,partial,success,critical}_{actor,target}_tt` keys are each used by all 12 sabotage raid types.
Their outcome text describes attempted delivery, failed-attempt evidence, and the possible outbreak in plain language; it does not promise a release when the final exact-state and policy gate rejects it.
Source checks confirmed 12 references per key and preserved the localisation file's UTF-8 BOM.

## Biological strategic handling location

The strategic biological raid interface does not expose its selected source airbase as a scripted state variable.
The attacker-accident branch therefore selects an internal handling location at outcome: a valid owned and controlled capital first, otherwise a qualifying owned and controlled state with an airbase or supply node.
This is a stockpile-handling representation, not a claim that the accident occurred at the engine-selected airbase.
If no valid handling state remains at outcome, the operation records a rejected reservation and creates neither an attacker accident nor a target release.
The player-facing staging-complex decision has been removed.
Completed strategic outcomes consume the full native payload reservation; the old ratio-based payload and Command Power refund helpers no longer run.

## Icons and UI wiring

`interface/cbrn_battlefield_operations.gfx` supplies the existing route map sprites `GFX_decision_cbrn_battlefield_cylinder_release`, `GFX_decision_cbrn_battlefield_projector_barrage`, `GFX_decision_cbrn_battlefield_artillery_fire_plan`, and `GFX_decision_cbrn_battlefield_armored_delivery` from `gfx/interface/decisions/stage_6_chemical_delivery/battlefield_operations/`.
`interface/cbrn_chemical_delivery.gfx` supplies each `GFX_<agent>_agent_lot_1_medium` equipment sprite from `gfx/interface/technologies/stage_6_chemical_delivery/equipment/`.
The biological supply-chain variants reuse `GFX_raid_type_icon_<agent>_strike` in `interface/chaosx_raids.gfx` and `GFX_<agent>_bomb_equipment_medium` in `interface/chaosx_equipment.gfx`.
The target icon `GFX_other_target_icon` comes from vanilla.
No new DDS is required for these raid routes; a future dedicated Phantom Mist map icon could be added to `interface/chaosx_raids.gfx` with a matching DDS under `gfx/interface/military_raids/`.

## Future plans

Measure native cancellation equipment behavior and AI route frequencies in a live session, then adjust only documented native fields if the observed behavior differs from the reservation contract.
Consider dedicated route art after the two-category layout and exact target tooltips have been validated in game.
