# 020 Black Plague spec Part 8 - Decision, mission, mapmode, and UI blueprint

## Part 8 role

This part deepens the shared disease and biological warfare response layer. The Black Death must use the shared disease and biological warfare category. It must not create a duplicate Black Plague-only decision category. The player should see the same disease board change its available actions as states move from prepared, threatened, infected, contained, recovering, weaponized, or rat-held status.

All decision, mission, button, and UI names in this file are working labels, not final localisation.

## Shared disease board structure

The shared disease board should act as a changing crisis board. It should read state and country conditions, then show only relevant actions.

Suggested board sections:

| Section | Visible when | Purpose |
| --- | --- | --- |
| National preparedness | country has no infected states or only distant threat | prevention laws, surveillance, stockpiles, medicine, inspections |
| Threatened borders and ports | country borders infected states, has infected neighbors, or has exposed ports | border controls, port checks, troop-route restrictions, refugee management |
| Active infected states | country owns or controls infected states | state quarantine, hospitals, army cordons, treatment, cleanup preparation |
| Contained and recovering states | country has contained or recovering states | maintain cordon, controlled reopening, relapse monitoring, cleanup crews |
| Rat-front response | country borders or fights rat-held states | anti-rat cordons, evacuation, nest-clearing operations, military containment |
| Research and cure | country has infection exposure, samples, or medical capacity | cure progress, treatment improvement, sample sharing, cure deployment |
| Biowarfare integration | country has biological warfare capability and the disease exists | safe study, dangerous samples, special-project hooks, accident risk management |

The board should not show all sections at once. It should feel like a curated state of the crisis.

## State target pools

The disease board should build dynamic state target pools. These pools are shared disease concepts. Black Death adds a more dangerous disease identity inside those pools.

| Target pool | Contains | Typical actions |
| --- | --- | --- |
| Prepared states | clean states with prevention investment | surveillance, stockpiles, early warning |
| Threatened states | adjacent, port-exposed, troop-route-exposed, refugee-exposed states | border checks, port checks, movement controls, local medical buildup |
| Infected states | states with active disease load | quarantine, hospitals, army cordons, treatment, emergency lockdown |
| Contained states | states where spread is suppressed but disease remains | maintain cordon, controlled reopening, monitor relapse |
| Recovering states | cure and cleanup are working | cleanup crews, repair hospitals, restore supply |
| Weaponized exposure states | states hit by deliberate payload or lab accident exposure | high-risk containment, evidence handling, condemnation and accident hooks |
| Rat-held frontier states | human states adjacent to rat-held plague states | anti-rat forts, evacuation, military cordons, supply defense |
| Retaken warren states | states retaken from rats but not cleaned | warren purge, corpse-field sanitation, hidden remnant checks |

A state should not appear in incompatible pools at the same time. If it does, the highest danger status should control visibility.

## National preparedness decisions

Preparedness decisions should exist before infection reaches a country. These should lower the chance that the first contact becomes a disaster. They should cost real resources and hurt the economy enough that overpreparing has a price.

| Working decision family | Availability | Cost direction | Result direction | AI behavior |
| --- | --- | --- | --- | --- |
| Disease surveillance | clean or distant-threat country | political power, medical production burden, civilian factory burden | raises detection, lowers hidden spread, reveals threatened states earlier | high for majors, port countries, and neighbors of outbreaks |
| Medical stockpiles | clean or threatened country | support equipment, trucks, trains, civilian factories, temporary consumer goods | lowers early deaths and improves treatment readiness | high for rich countries and countries near infected states |
| Public health inspections | clean states with ports, rail hubs, or high population | stability strain, small production disruption | lowers port and rail exposure | high for port countries after overseas spread exists |
| Reserve hospital plans | prepared states, large population states | construction capacity and support equipment | reduces time and cost of emergency hospitals later | high if large population or low medical capacity |
| Prevention law strengthening | national law or staged policy | stability, war support, consumer goods, political power | broad reduction to spread and death severity | AI chooses based on threat, economy, ideology, and war state |

Preparedness should not make countries immune. It should reduce severity, detect spread sooner, and lower the cost of later action.

## Threatened-state decisions

Threatened-state actions should appear when infection is nearby or routes expose the state.

| Working decision family | Target | Cost direction | Success direction | Failure or tradeoff |
| --- | --- | --- | --- | --- |
| Border health cordon | threatened land-border state | infantry equipment, support equipment, command power, divisions nearby | lowers cross-border spread and refugee-driven exposure | hurts supply and relations, raises local strain |
| Port inspection regime | threatened port state | convoys, naval command attention, civilian factories, stability | lowers sea-jump and port exposure | hurts trade and naval logistics |
| Troop-route restriction | state crossed by active armies or supply lines | command power, army XP, supply burden | lowers spread from troop movement | weakens local operations and planning |
| Refugee triage and shelter | threatened or adjacent state | trains, trucks, support equipment, stability | lowers panic and uncontrolled movement | costs industry and can raise local supply burden |
| Local medical buildup | threatened high-population state | support equipment, civilian factories, medical stockpile | lowers first infection death spike and raises containment strength | visible economic cost |

These actions should matter most before the state becomes infected. After infection, the board should offer harsher actions.

## Infected-state decisions

Infected-state actions should be powerful, expensive, and risky. They are not a flat checklist. The player should underreact or overreact based on war, economy, and state value.

| Working decision family | Target | Cost direction | Result direction | Risk and tradeoff |
| --- | --- | --- | --- | --- |
| Emergency quarantine | infected state | stability, war support, local supply, civilian factory burden | lowers spread pressure quickly | damages local economy, resistance, and compliance |
| Full lockdown | severe infected state | stronger stability and production cost, supply hit | sharply lowers spread and movement | raises panic if maintained too long |
| Army cordon | infected state with military access | manpower commitment, infantry equipment, support equipment, command power, divisions required nearby | lowers spread and rat warren growth | ties down troops and can suffer attrition |
| Field hospitals | infected state | support equipment, trucks, civilian factories | lowers daily deaths and improves treatment | weaker if supply is bad |
| Emergency hospital construction | infected or threatened high-population state | construction capacity, civilian factories, support equipment | persistent local death reduction and cure support | slows other construction |
| Treatment campaign | infected state with cure progress | medical stockpile, support equipment, political effort | reduces death pressure and disease load | weak before enough cure progress exists |
| Local cleanup crews | contained or low-load infected state | manpower, equipment, civilian factories | moves state toward recovering | failure can cause relapse |

Death reduction should never be free. The player can save lives by accepting economic and military burden.

## Contained and recovering-state decisions

Contained and recovering states should keep some pressure. The disease should not vanish when a cure value reaches a threshold.

| Working decision family | Target | Cost direction | Result direction | Risk and tradeoff |
| --- | --- | --- | --- | --- |
| Maintain containment | contained state | continuing supply and equipment burden | prevents relapse and spread | prolongs local economic damage |
| Controlled reopening | contained state | political pressure, stability risk | restores some economy and supply | raises relapse chance if early |
| Relapse monitoring | contained or recovering state | support equipment, small civilian burden | detects relapse early and prevents hidden growth | cheaper than full quarantine, weaker against severe relapse |
| Final cleanup | recovering state with low disease load | manpower, support equipment, construction capacity | removes active disease status | can fail if rat warren pressure remains |
| Recovery support | cured or recovering state | civilian factories, trains, construction | restores supply, reduces resistance, supports population recovery direction | does not restore dead population instantly |

The cure should reduce deaths and spread, then enable cleanup. It should not be an instant erase button.

## Cure and research decisions

Cure progress should be shared through the biological warfare and disease system. Countries can contribute alone or through cooperation.

| Working decision family | Availability | Cost direction | Result direction | Notes |
| --- | --- | --- | --- | --- |
| Study Black Death cases | country has infected or contained states | civilian factories, support equipment, research slot burden or timed project pressure | adds cure progress and local treatment knowledge | safe baseline study |
| Share disease data | country has cure progress and diplomacy access | political power, relations, intelligence exposure | gives allies or coalition shared progress | AI should use under world-threat pressure |
| Fund medical production | country with industry | civilian factory burden, support equipment, trucks | increases treatment capacity and lowers death ticks | useful before infection reaches the country |
| Deploy treatment protocol | infected or contained state with cure progress | medical stockpile and local capacity | lowers death pressure and spread pressure | stronger at higher cure progress |
| Emergency vaccine or prophylaxis program | late cure progress stage | high industry and stability cost | prevents severe outbreaks in prepared states | should not cure rat-held states directly |

The implementation can model cure progress nationally, coalition-wide, or globally. The design requirement is that cure progress changes death ticks, spread chance, and cleanup eligibility before it removes disease.

## Biological warfare integration

Black Death should enter the biowarfare ecosystem once it exists. This means study, safe handling, special projects, deployment hooks, accident risk, condemnation, and retaliation risk. The spec must keep this gameplay-only. It must not include real-world lab methods, pathogen handling steps, or biological weapon instructions.

| Working family | Availability | Gameplay role | Risk |
| --- | --- | --- | --- |
| Safe sample study | country has infected state access or intelligence access | improves cure progress and defensive knowledge | small accident risk if containment is poor |
| Dangerous sample acquisition | biowarfare-capable country with access to infected or rat-held states | unlocks special-project progress faster | high accident, condemnation, and spy exposure risk |
| Weaponization special project hook | disease exists and country has biowarfare capability | starts long special-project path | lab leak, stockpile accident, diplomatic fallout |
| Delivery payload unlock | after special project completes | enables existing biowarfare delivery systems to use Black Death payload | retaliation and runaway spread |
| Stockpile safety protocols | country holding weaponized Black Death | reduces accident risk | costs industry and slows offensive use |

Weaponized Black Death should be extremely dangerous for both target and user. It should also make rat emergence more likely in badly hit states.

## Rat-front response decisions

Rat-front response decisions should appear in the same shared disease board, not in a separate rat-only category. They are disease plus military containment actions.

| Working decision family | Target | Cost direction | Result direction | Failure direction |
| --- | --- | --- | --- | --- |
| Anti-rat border cordon | state bordering rat-held territory | divisions in state, infantry equipment, support equipment, supply burden | lowers rat attack preparation and spread across border | fails if underdefended or supply breaks |
| Evacuate threatened population | high-population threatened state near rats | trains, trucks, stability, civilian factory burden | lowers future death pressure if state falls | hurts industry and war support |
| Fortify warren front | border state or supply route | construction capacity, forts, anti-air, support equipment | improves defense and cordon strength | slow and expensive |
| Nest-clearing operation | retaken warren state | divisions present, support equipment, flame or engineering abstraction if repo supports safe wording | lowers hidden warren pressure and rat relapse | casualties, supply strain, possible infection relapse |
| Secure medical corridors | infected frontier state | trucks, trains, convoys, support equipment | keeps hospitals and cordons functioning | vulnerable to rat raids |
| Joint rat response | world-threat active and rat threat large enough | diplomacy, equipment shipments, convoys | shares containment bonuses and AI response | sponsor influence or relations cost |

The wording should avoid real extermination instruction detail. It should describe military containment, cleanup, cordons, and state recovery at gameplay level.

## Mission pools

Missions make the disease board feel active. They should appear only when they ask the player to do something.

| Mission pool | Owner | Objective direction | Duration direction | Success direction | Failure direction |
| --- | --- | --- | --- | --- | --- |
| Hold the cordon | human country with infected border state | keep supplied divisions in named border states | medium, longer if bad terrain | lowers spread and rat pressure | outbreak spreads or rat breach pressure rises |
| Keep the port clean | country with threatened port | maintain port inspections, convoys, and no active infection | medium | lowers overseas spread risk | port becomes exposed or infected |
| Save the hospital network | country with infected high-population state | supply hospitals and maintain equipment stockpile | medium to hard | lowers deaths and improves cure progress | deaths rise and panic increases |
| Clean the retaken warren | country that retook rat-held state | hold state, keep units present, run cleanup | hard | removes hidden warren pressure | relapse or renewed rat emergence risk |
| Prove containment | country with contained outbreak | keep disease load below threshold for a period | medium | state moves to recovering | relapse to infected |
| Maintain medicine supply | country under broad outbreak | keep support equipment, trucks, and factory burden | medium | treatment actions remain effective | treatment weakens and death ticks rise |

Mission durations should vary with state size, severity, terrain, supply, and war state. Emergency missions can be shorter, but most should give enough time for player and AI response.

## Costs and tradeoff palette

The shared disease board should use varied costs.

| Action type | Cost palette |
| --- | --- |
| Medical action | support equipment, trucks, civilian factories, construction capacity, research burden |
| Border control | infantry equipment, manpower commitment, command power, divisions in state, supply burden |
| Port and travel control | convoys, trains, stability, trade disruption, civilian factories |
| Lockdown | stability, war support, production disruption, resistance or compliance pressure |
| Cure research | research capacity, civilian factories, medical stockpile, time |
| Rat-front military action | divisions, equipment, supply, forts, army XP, command power below conservative caps |
| Weaponization | special-project time, biowarfare stockpile risk, condemnation, accident risk, security burden |

Political power can appear, but it should not be the main cost for most actions.

## Dynamic cooldowns

Cooldowns should depend on what the action represents.

| Cooldown type | Factors |
| --- | --- |
| Quarantine cooldown | state population, severity, stability, panic, last quarantine date |
| Hospital construction cooldown | construction capacity, infrastructure, state damage, supply access |
| Port inspection cooldown | port size, convoy use, overseas exposure, prior failure |
| Cordon cooldown | division presence, supply, terrain, active rat attacks, army route |
| Cure deployment cooldown | cure progress, medical capacity, disease load, state status |
| Cleanup cooldown | remaining disease load, hidden warren pressure, terrain, local damage |

Cooldowns should be visible through broad state text and tooltips. Raw values can remain implementation details.

## AI use

AI countries must use the shared disease board. AI behavior should be state-aware.

| AI actor | Preparedness | Threat response | Infected response | Rat-front response | Weaponization |
| --- | --- | --- | --- | --- | --- |
| rich major | strong, early | strong border and port controls | high hospital and cure spending | strong coalition support | only if biowarfare path and risk appetite support it |
| poor minor | limited | prioritizes capital and high-population states | uses quarantine and cheaper cordons | requests aid or fortifies capital route | almost never |
| authoritarian | strong lockdown willingness | hard borders | harsh quarantine, higher stability damage | aggressive cordon and evacuation | more likely if already using biowarfare |
| democratic | higher cost sensitivity for harsh lockdown | port and medical focus | treatment and public health first | coalition and humanitarian support | rare and politically costly |
| country at war | lower economy tolerance | troop-route restrictions matter | cordons if front allows | prioritizes rat border over distant disease | risky if desperate |
| biowarfare specialist | better sample and cure actions | stronger safety protocols if sane | may study samples | may seek rat-held samples | likely, but accident risk gates it |

AI should never click actions that require missing states, invalid targets, impossible borders, or resources it cannot afford. If a country is an actual nonhuman country, it should not use human disease prevention actions unless a specific rat route says so.

## Mapmode and visual update rules

The disease mapmode should update whenever a state changes disease status. The map must show infected states dynamically and reflect spread, containment, cure, weaponized exposure, and rat-held status.

Update triggers:

- first infection
- disease load threshold change
- state enters threatened status
- containment starts or ends
- cure progress changes state severity enough to alter status
- state enters recovering or cured status
- weaponized exposure starts
- rat nation captures state
- human country retakes rat-held state
- cleanup removes active warren pressure

Suggested mapmode visual states:

| State status | Visual direction |
| --- | --- |
| Clean | no special disease overlay |
| Prepared | subtle protective tint or icon in disease board only |
| Threatened | light warning tint in disease mapmode |
| Infected | strong dark disease color |
| Severe infected | darker color and stronger state icon |
| Contained | infected color with containment ring or distinct icon direction |
| Recovering | faded disease color with recovery marker |
| Weaponized | sharp high-risk marker distinct from natural infection |
| Rat-held | black disease color plus rat or warren marker |

The user asked for black fog over Black Plague states if possible. The design should request a real attempt at a state-level black fog presentation. If the engine surface cannot support true per-state fog in the mapmode, the implementation must report that blocker and use an approved visible alternative such as a dark state tint, pulsing infected-state icon, and disease-board state card art. The visible alternative must still update dynamically with state status.

## Scripted GUI design

The shared disease board can use normal decisions plus a scripted GUI header or attached window if the existing biological warfare UI supports it.

Suggested player view:

| UI element | Purpose |
| --- | --- |
| disease selector | shows active disease identities, including Black Death once discovered |
| state status cards | lists current infected, threatened, contained, and recovering states |
| mapmode toggle | switches to the disease mapmode |
| cure progress meter | shows broad cure progress and treatment strength |
| spread risk summary | explains where spread pressure is coming from |
| deaths trend summary | shows whether deaths are rising or falling |
| action groups | opens relevant decision families without showing obsolete actions |
| rat-front alert | appears only when rat-held states exist or border the country |
| weaponized exposure alert | appears only when deliberate payload or accident exposure exists |

Useful animated assets:

| Animated element | State logic | Purpose |
| --- | --- | --- |
| disease seal pulse | infected states exist | draws attention to active disease without hiding values |
| black fog state card | selected state is infected or severe infected | indicates Black Death identity in the board |
| containment ring pulse | contained states at relapse risk | warns that reopening is risky |
| cure meter shimmer | cure progress crossed a meaningful threshold | shows treatment improvement |
| rat-front warning border | rat-held frontier states exist | separates military containment from ordinary disease response |

Animation must follow the frame-animation rules. Static fallbacks are required.

## Cleanup rules

The disease board must remove stale actions.

Cleanup requirements:

- remove state-target decisions when the state is no longer valid
- cancel missions when owner, controller, or state status makes them impossible
- clear selected-state GUI targets when state status changes
- retire preparedness decisions that no longer apply during active infection, unless they still make sense nationally
- hide infected-state decisions after final cleanup
- convert contained-state actions into recovery actions after disease load drops
- remove rat-front actions when no rat-held frontier exists
- keep monitoring actions for a short period after cure or rat defeat
- clear weaponized exposure actions only after exposure, evidence, and accident risk have been resolved

The board should never become a wall of obsolete decisions.
