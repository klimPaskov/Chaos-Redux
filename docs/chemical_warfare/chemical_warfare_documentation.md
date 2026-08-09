# Chemical Warfare System

## Gameplay identity

Chemical warfare is an equipment-backed exact-state system. The player researches an agent, produces its real payload and protective equipment, establishes Chemical Readiness and a use policy, selects a supported delivery route, and receives disruption and area-denial power in exchange for deaths, contamination, medical load, evidence, attribution, Condemnation, treaty response, and sanctions risk.

Chaos Warfare makes this route substantially faster, more lethal, and more persistent. Its Integrated CBRN Command ladder can reduce Condemnation impact, but doctrine never erases payload expenditure, protection failure, evidence, attribution, deaths, contamination, medical saturation, resistance trauma, confirmed-use history, or responsibility.

## Active delivery routes

- Selected-state chemical air raids cover Chlorine, Phosgene, Mustard, Lewisite, Tabun, Sarin, Soman, Malodor, and Behavioral Agent payloads. Sarin and Soman also have strategic-rocket variants. Every native outcome reserves exact class equipment; only partial, successful, and catastrophic releases enter exposure. Aborted and failed attempts record bounded evidence and Condemnation without fabricating toxic effects.
- Japan's China campaign provides a visible agent selector and an exact selected-state attack decision. It consumes 120 matching legacy cylinders, pays 20 command power or 16 with Reagent Optimization, and dispatches through the canonical exposure pipeline.
- The chemical doomsday decision consumes the real national legacy-cylinder arsenal once, allocates each supported agent across exact eligible controlled states, and dispatches every accepted state through the same pipeline.
- The restricted-site nerve route consumes researched Sarin or Soman stock inside an already authorized extermination, gulag, or experiment site. Nerve-agent doctrine mastery increases camp killing efficiency and chemical consequences; it does not create or authorize camp infrastructure and does not conceal the result.
- Special Malodor and Behavioral-Agent raids use distinct payloads and state modifiers focused on disruption. They retain evidence and Condemnation through the common consequence contract.

## Shared release contract

Every release-bearing adapter must supply an exact state, a researched and route-valid agent, a real payload debit or authoritative native equipment reservation, target protection, positive release efficiency, and policy/readiness authorization. It then calls `cbrn_prepare_chemical_action_record` and `cbrn_dispatch_chemical_action_record` exactly once.

The dispatcher records hostile disruption, friendly exposure where applicable, civilian deaths, canonical state contamination, continuing deaths, medical saturation, evidence, attribution, confirmed-use history, treaty response, Condemnation, and victim memory. Dimercaprol reduces general chemical deaths by 15%, adds a further 50% reduction against blister-agent deaths, and reduces medical saturation by 35%; it does not protect against political or evidentiary consequences.

The canonical contract and complete source map are documented in `docs/systems/cbrn_chemical_delivery.md`.

## Equipment and formations

Strategic agent lots, filled shell lots, and four class-specific prepared air-payload families are producible equipment. Exact-agent aircraft racks fit CAS and tactical-bomber designs; an installed rack is eligibility equipment, not proof that a release occurred.

The division layer uses CBRN regimental support formations with essential-equipment shortage scaling. Projector batteries, ammunition trains, armored delivery detachments, and nerve-suppression detachments carry real standing payload loads but do not pay for an operation; an adapter must also debit the national route cost.

Army Headquarters is the theater preparation layer. Its powerful packages have real essential equipment, preparation, duration, cooldown, upkeep, AI gating, and cleanup. A headquarters does not manufacture an exact target receipt where the engine does not expose one.

## Protection and recovery

Gas masks are producible model-progressing equipment. The national ledger distinguishes reserves, military issue, divisional equipment, civilian distribution, fitting, filters, stock loss, and population-scaled demand. Target protection is refreshed from those real ledgers at release time rather than inferred from technology alone.

Chemical contamination is state-owned. Overlapping exposure refreshes the canonical receipt, Air Cleanliness contribution, expiry, and continuing-death schedule. State-targeted recovery events reduce medical saturation and evidence without adding a broad all-country daily, weekly, or monthly pulse.

## Doctrine rewards

Chaos Warfare grants 15% planning speed and 35% soft attack, breakthrough, and defense to chemical support companies at adoption. Combat Support mastery reaches 1.65 chemical operational effect and 1.80 contamination output. Integrated CBRN Command reaches 1.70 operational effect, 1.60 chemical-air dose, 1.50 chemical-air duration, and a 0.35 Condemnation multiplier. Officer-corps postures add strong formation, preparation, cleanup, casualty, contamination, medical-saturation, and camp-efficiency rewards according to the chosen route.

## AI behavior

AI adoption and escalation are profile-aware. Prepared, military-first, industrial-reserve, retaliation, theater-use, and unrestricted profiles receive different doctrine, policy, production, raid, headquarters, designer, and decision weights. Japan's campaign selector repairs itself toward a researched agent with matching stock and prioritizes Chinese core states. Every active AI route still pays its exact equipment and command cost.

## Fail-closed engine boundaries

- Ordinary continuous air missions expose no verified current-version eligible-activity callback. Idle or merely deployed chemical-capable aircraft never contaminate a region, and no estimator is retained.
- Army-leader abilities and ordinary combat tactics cannot prove an exact selected state, payload debit, and release-condition receipt. Their stable identifiers remain unavailable for compatibility; their old direct helpers and misleading preview localisation were removed.
- A generic active Army Headquarters-to-formation command relationship is not exposed in script. Unsupported ground release routes remain unavailable instead of choosing a nearby, border, capital, or random target.
- The selected-state raid outcome scope does not expose verified live target weather or terrain. Active raids use native release efficiency and leave optional environmental inputs absent rather than assigning neutral or estimated values.

## Primary implementation surfaces

- Payload and exposure: `common/scripted_effects/cbrn_payload_effects.txt`, `common/scripted_effects/cbrn_exposure_effects.txt`, and `common/scripted_effects/cbrn_consequence_effects.txt`
- Air raids: `common/raids/cbrn_chemical_air_raids.txt` and `common/scripted_effects/cbrn_chemical_raid_effects.txt`
- Japan campaign: `common/decisions/japan_chemical_campaign_decisions.txt` and `common/scripted_effects/JAP_chemical_campaign_effects.txt`
- Doomsday: `common/scripted_effects/cbrn_chemical_doomsday_effects.txt`
- Restricted sites: `common/scripted_effects/cbrn_camp_effects.txt`
- Protection and state recovery: `common/scripted_effects/cbrn_protection_effects.txt`, `common/scripted_effects/cbrn_chemical_state_effects.txt`, and `events/cbrn_chemical_delivery_events.txt`
- Doctrine and officer corps: `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt`, `common/doctrines/subdoctrines/land/chaos_warfare_*_subdoctrines.txt`, and `common/ideas/cbw_spirits.txt`
- Consequences: `common/scripted_effects/condemnation_sanctions_effects.txt` and `docs/systems/condemnation_sanctions.md`
