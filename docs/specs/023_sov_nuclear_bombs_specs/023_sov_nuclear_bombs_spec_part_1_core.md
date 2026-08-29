# Event 023 specification, Part 1: Core experience and opening

## Core event promise

Event 23 introduces a Soviet nuclear arsenal years before the wider world expects it. The arsenal begins as a secret state project, then becomes a tool of deterrence, coercion, wartime release, internal control, and possible global escalation.

The event should give the Soviet player a strong new strategic asset and a serious command problem at the same time. The player receives a large stockpile, but practical use depends on delivery forces, authorization discipline, test evidence, secure storage, target selection, and the risk that the Soviet state may fragment while the weapons remain distributed across its territory.

The design should create several valid campaign identities:

- A hidden arsenal that is maintained as a private reserve and never used.
- A tested deterrent that changes foreign behavior without forcing immediate war.
- A coercive arsenal used to pressure enemies, minors, and Soviet breakaways.
- A limited-use doctrine that strikes military or logistics targets under severe conditions.
- A retaliatory command designed to survive an enemy nuclear attack.
- A high-chaos first-use posture that can begin a major exchange.
- A controlled dismantlement or moratorium route that ends the immediate danger while preserving political consequences.

These identities are expressed through one custody doctrine, two visible command values, one staged posture, phased decisions, and event choices. The event should not become a separate grand-strategy game inside the mod.

## Classification and chaos placement

Event 23 remains a Minor Fire-Once event.

Its planned chaos level is `2`, Gathering Storm, which begins at 200 Chaos. The event is too disruptive for Calm World selection because the baseline instantly grants 100 nuclear bombs and opens nuclear coercion during an era when most countries have no comparable capability.

The level 2 placement gives Event 23 a clear escalation ladder:

| World state | Event 23 state |
| --- | --- |
| Calm World, below 200 Chaos | Event unavailable |
| Gathering Storm, 200 to 399 Chaos | Baseline opening |
| Rising Chaos, 400 to 599 Chaos | Evolution I opening or active evolution |
| Chaos Tier, 600 to 799 Chaos | Evolution II opening or active evolution |
| Totalen Chaos, 800 to 999 Chaos | Evolution III opening or active evolution |
| World Collapse, 1000 or more Chaos | Evolution IV opening or active evolution |

The event should show `N/A` in the Events list when the Soviet Union cannot validly receive it. It should not show a misleading zero weight.

## Valid Soviet actor

The normal and only opening actor is `SOV`.

Event 23 is valid when all of the following design conditions can be satisfied:

- The Soviet Union exists as a country scope.
- The Soviet Union is not fully capitulated or reduced to a state where no valid central command, storage, test, or delivery preparation site can be created.
- The Soviet Union controls at least one valid core state for the central command site.
- The Soviet Union controls enough territory to create a bounded storage network without assigning all devices to one exposed state.
- The shared nuclear consequence system is available, because Event 23 must not create a private fallback strike model.
- The event has not already fired.

Active Soviet Collapse does not invalidate Event 23. The event may fire while Event 5 is active if `SOV` still exists and can support a central arsenal. In that case, the opening immediately uses the collapse-custody package from Part 6.

Event 23 does not transfer its opening to Russia, a Soviet successor, a generic communist country, or a breakaway if `SOV` has already ceased to exist. The event name and premise are tied to the Soviet Union. Post-collapse nuclear inheritance occurs only when Event 23 fired before or during the collapse and recorded actual storage-site custody.

## Existing Soviet nuclear progress

The event must work whether the Soviet Union has no nuclear research, partial nuclear progress, a completed nuclear capability, reactors, or an existing bomb stockpile.

The opening always adds exactly 100 nuclear bombs at baseline. It does not set the total to 100.

Existing progress changes the supporting package:

- Missing current-vanilla nuclear capability is granted only to the minimum level needed for normal nuclear ownership and use.
- Existing capability is preserved and does not receive duplicate technology rewards.
- Existing reactors count toward production and test preparation.
- Existing nuclear bombs remain in the stockpile and are added to the 100-bomb event grant.
- Existing advanced delivery systems are recognized, but Event 23 does not grant missile technology, thermonuclear technology, or unrelated advanced research.
- Existing nuclear use history remains authoritative for shared condemnation, deaths, contamination, and chaos tracking.

The implementation must inspect the current installed nuclear technology and special-project structure before choosing exact grants. The specification does not assume that an older vanilla technology path still matches the installed game.

## Opening structure

The random event selection fires `chaosx.nr23.1` against `SOV`.

The opening has four responsibilities:

1. Establish the arsenal and current evolution stage.
2. Select a custody doctrine.
3. Register the central command, production, test, and storage network.
4. Activate the appropriate decision categories, ideas, AI plans, and event-log state.

The opening grant is immediate. The command and storage setup may use a short initialization chain so the actor, state targets, and pre-fire evolution package are stable before player choices resolve.

The opening should not be presented as a public global announcement. Soviet players receive the full event. Foreign players receive no public news until detection, public testing, an ultimatum, a leak, or confirmed use.

## Baseline opening grant

At the baseline opening, the Soviet Union receives:

- Exactly 100 nuclear bombs added to its current stockpile.
- The minimum current-vanilla nuclear capability needed to maintain the stockpile and use the shared nuclear delivery route.
- One event-owned visible national spirit representing the secret arsenal and current posture.
- Arsenal Readiness and Command Integrity initialized from the selected custody doctrine.
- A central command site and a bounded network of storage sites.
- A candidate test ground selected from valid Soviet-controlled territory.
- The main Soviet nuclear decision category.
- Access to development, storage, safety, delivery-preparation, and testing actions.
- Wartime targeting access once delivery and authorization requirements are met.
- Hidden cross-event markers that future Event 32, Event 76, and Event 47 implementations may read without being required by Event 23.

The baseline does not grant free strategic bombers, missile systems, thermonuclear weapons, a new focus branch, a custom nuclear unit, a new country, or a global arms-race package.

## Custody doctrine choice

The first Soviet choice determines who controls the arsenal and how the command system balances use reliability against unauthorized use, political interference, scientific safety, strategic survivability, and collapse risk.

The following names are working route labels, not final option text.

### Party custody

The Politburo and state security organs keep release authority highly centralized.

Narrative role:

- The arsenal belongs to the political center.
- Codes, transport orders, and production authority pass through party channels.
- Military commanders receive weapons only after direct authorization.

Mechanical direction:

- High starting Command Integrity.
- Moderate or low starting Arsenal Readiness.
- Strong secrecy and reduced early foreign discovery.
- Slower release authorization and delivery preparation.
- Better resistance to independent military use.
- Greater risk that purges, leadership crisis, capital loss, or Event 5 authority collapse disrupt the entire chain at once.
- Soviet AI prefers this doctrine when stable, at peace, and governed by a strong central party apparatus.

### Military custody

The General Staff and selected long-range aviation commands control operational preparation.

Narrative role:

- The arsenal is treated as a weapon that must work under combat conditions.
- Air crews, logistics officers, and field commands gain earlier access.
- Political control remains present, but military urgency shapes the system.

Mechanical direction:

- High starting Arsenal Readiness.
- Moderate starting Command Integrity.
- Faster delivery preparation and shorter wartime authorization delays.
- Stronger retaliation after an enemy nuclear strike.
- Higher risk of unauthorized loading, commander refusal, premature escalation, or disputed orders during collapse.
- Soviet AI prefers this doctrine during a difficult war or when an enemy can threaten Soviet command sites.

### Scientific safety veto

The design bureau and a state scientific safety council retain a formal ability to delay unsafe tests or releases.

Narrative role:

- Weapon reliability, storage safety, test evidence, and contamination risk receive institutional weight.
- Scientists cannot independently launch a weapon, but they can withhold technical certification.

Mechanical direction:

- Very high starting Command Integrity.
- Low starting Arsenal Readiness.
- Safest testing route and lower accident risk.
- Slower production and release preparation.
- Better chance to detect false warnings and abort an invalid target package.
- Stronger dismantlement and moratorium routes.
- A player may overrule the safety veto later, but doing so damages integrity and can trigger internal conflict.
- Soviet AI prefers this doctrine at lower Chaos when not under immediate military threat.

### Dispersed special commands

Warheads, codes, transport units, and technical teams are distributed among several special commands.

Narrative role:

- The arsenal is designed to survive bombing, decapitation, and occupation.
- No single attack can remove the entire capability.
- Local commands gain more physical access than under the other doctrines.

Mechanical direction:

- Good starting Arsenal Readiness.
- Low starting Command Integrity.
- Better survival after strategic bombing and capital loss.
- Faster local retaliation when central communications are damaged.
- Higher risk of missing devices, split custody, false orders, and breakaway seizure during Event 5.
- Stronger need for rail security, depot guards, and periodic accounting.
- Soviet AI prefers this doctrine when the capital is threatened, the country is already fragmented, or enemy strategic bombing pressure is high.

## Custody doctrine commitment and reform

The opening doctrine is a serious commitment. It should not be freely switched through a cheap button.

A later reform is possible only through a timed restructuring action that:

- Temporarily lowers Arsenal Readiness.
- Consumes concrete logistical and administrative resources.
- Requires the arsenal to be below a severe emergency release state.
- Cancels active strike authorization and target dossiers.
- Re-registers storage and authorization responsibilities.
- Creates a cooldown before another restructuring.
- May become unavailable during the final stages of Soviet Collapse.

A doctrine can also be transformed by failure. A party system can become a decapitated chain. A military system can become fractured command. A scientific council can be purged or overruled. A dispersed system can become unsecured custody.

## Central command and storage initialization

The opening should create a distributed network with distinct roles. The stockpile needs a clear map relationship.

The network contains:

- One central command state.
- One primary design and technical state.
- One primary production or reactor-support state.
- One candidate test state.
- Several storage states selected according to the current stockpile and evolution stage.

State selection should favor Soviet-controlled core territory with rail access, adequate infrastructure, distance from an active front, and room to distribute risk. It should avoid assigning every role to Moscow or stacking the whole system in one state.

The network may use state flags, state modifiers, event targets, and an event-owned ledger. It does not require a new visible building type.

The central command site controls authorization and high-level coordination. The storage sites matter during bombing, occupation, civil war, and Event 5. The test state matters for secrecy, contamination, safety, and foreign observation. The production state matters for reactor construction and assembly speed.

## Test-ground candidate rules

The event should select a valid low-population interior state suitable for a secret or public test.

The preferred state has:

- Soviet ownership and control.
- No active front or hostile occupation.
- Low population compared with other valid candidates.
- No capital role.
- Adequate distance from densely populated neighboring states.
- A rail or infrastructure connection for moving equipment.
- No existing catastrophic contamination that would make test results meaningless.

The test ground is not fixed to one historical location because Chaos Redux campaigns can change Soviet borders before Event 23 fires. A Central Asian steppe location is preferred when valid, which gives the system a historical visual and geographic basis. Another interior state is selected when that region is unavailable.

The Soviet player can later move the test program through a costly relocation action. Relocation should not erase existing contamination or foreign knowledge.

## Information visibility

The event begins secret.

The player-facing information model has four knowledge states:

| Knowledge state | Foreign information |
| --- | --- |
| Unknown | No public news and no exact event detail |
| Suspected | Foreign intelligence or observers know that an unusual Soviet atomic program exists |
| Demonstrated | A public test or explicit ultimatum confirms a Soviet weapon capability |
| Used | A confirmed combat detonation records public responsibility through the shared consequence system |

Soviet players always see the current arsenal controls, Readiness, Integrity, posture, and storage status.

Foreign players should not see the exact Soviet bomb count, exact storage states, exact command doctrine, or internal authorization state before public reveal. Event Details may show a classified or uncertain public premise until the arsenal becomes demonstrated.

The event name used by debug and catalog systems may remain `SOV Nuclear Bombs`, but foreign-facing detail text should not reveal the exact opening grant or internal mechanics.

A public reveal is permanent. Later secrecy actions may conceal movements and targets, but they cannot make the world forget a demonstrated arsenal.

## Event lifecycle

The event has six broad phases. They are baseline phases, not evolution entries.

### Phase 1: Secret arsenal

- The custody doctrine is selected.
- Storage, command, production, and test sites are registered.
- The player improves Readiness and Integrity.
- Foreign discovery remains limited.

### Phase 2: Tested capability

- The Soviet Union conducts a laboratory proof, covert test, or public test.
- Test evidence improves reliability.
- Detection risk and contamination depend on the chosen route.
- The first public test confirms the arsenal and creates foreign reactions.

### Phase 3: Deterrent posture

- The Soviet Union can maintain a hidden reserve, issue wartime warnings, or prepare retaliation.
- Targeting remains limited and exact.
- The arsenal influences diplomacy without guaranteeing submission.

### Phase 4: Coercive posture

- Evolution II opens direct ultimata against valid minors and Soviet breakaways.
- Target countries receive a response window.
- Soviet credibility changes according to whether threats are resolved, abandoned, or followed by war and use.

### Phase 5: Exchange posture

- Evolution III permits full exchange planning once more than one major has a usable arsenal.
- AI avoids initiating a major exchange below 1000 Chaos.
- Emergency stand-down and armistice routes remain available.

### Phase 6: Collapse, moratorium, or runaway escalation

- Event 5 may divide physical custody.
- The Soviet Union may preserve, recover, transfer, dismantle, or lose devices.
- A major exchange may stop below the Fallout threshold or contribute to the shared Fallout terminal route.
- The event can end in a controlled arsenal, dismantlement, fragmented custody, Soviet defeat, or an ongoing deterrent state.

## Event completion state

Event 23 is Fire-Once, but its system can remain active for the rest of the campaign.

The random-event entry is complete when the opening resolves. The persistent system closes only when one of these states applies:

- The arsenal is fully dismantled or transferred and no Soviet or Event 23 breakaway operational capability remains.
- The Soviet Union no longer exists and every recorded device is accounted for, destroyed, dismantled, or transferred.
- A shared terminal world-end state freezes incompatible event systems.
- A controlled moratorium seals the arsenal and disables normal targeting while keeping limited maintenance and reactivation consequences.

The persistent category should hide when no action remains. Obsolete target, testing, collapse, and production actions must be removed. Dead buttons are unacceptable.

## Player experience standard

The event should feel powerful immediately because the stockpile is real and large. It should also be clear why the player cannot erase every enemy with rapid button presses.

The central choices are:

- Who controls the weapons.
- How much readiness is worth the risk of fragmented control.
- Whether to remain secret, test covertly, or demonstrate publicly.
- Whether to use the arsenal for deterrence, coercion, limited military use, or exchange preparation.
- Whether to preserve or dismantle the arsenal during a Soviet internal crisis.
- Whether to retaliate after an enemy strike.
- Whether to stop an exchange while a negotiated off-ramp remains possible.

The event should reward preparation and judgment. It should punish empty threats, careless testing, impossible target choices, weak custody, and rapid repeated use through direct strategic, political, and shared global consequences.
