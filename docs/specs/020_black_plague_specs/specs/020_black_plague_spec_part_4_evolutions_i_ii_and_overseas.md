# 020 Black Plague spec Part 4 - Baseline escalation and Evolutions I to II

## Baseline escalation

The baseline is the normal disease lifecycle after Event 020 fires. It can become severe without any evolution. Baseline escalation should be driven by infected states, deaths, spread, containment failure, and cure progress.

Baseline escalation stages:

| Stage | Trigger direction | Result |
| --- | --- | --- |
| First outbreak | Event fires and first state is infected. | Shared disease board opens. |
| Regional spread | Several nearby states become threatened or infected. | Neighboring countries receive prevention options. |
| National crisis | The owner has multiple infected states or high deaths. | Harsher internal decisions and cure pressure unlock. |
| Cross-border crisis | Neighbor countries receive infected states. | Border closure, aid, blame, and diplomatic reaction decisions unlock. |
| Contained outbreak | Disease load falls and spread slows. | Recovery and monitoring decisions replace emergency actions. |
| Runaway outbreak | Many states have high load and death pressure. | Rat warren pressure and high-chaos risks rise. |

Ordinary baseline stages are not evolution log entries. Evolution log entries are only for the mutation tracks below.

## Evolution entry standard

Each evolution should support two entry paths when relevant:

- Active-event evolution: the Black Death already exists, and the evolution changes existing infected states, cure rules, decisions, AI, and future spread.
- Pre-fire evolved opening: Event 020 has not fired yet, and the world state allows the first outbreak to begin with evolved severity.

The implementation should not require the event to fire again for active actors to receive evolution content.

## Evolution I - harder strain

Working label, not final localisation: `harder strain`.

Evolution I makes the Black Death harder to cure and more dangerous. It should usually become possible once the disease has survived long enough or enough deaths and infected states exist. High chaos can make it more likely.

Active-event evolution effects:

- Existing infected states gain higher disease load growth.
- Cure progress loses some efficiency.
- Death pressure rises faster after early infection.
- Containment failures become more likely in weak states.
- Threatened states with poor protection become infected more easily.
- Field hospital and treatment decisions become more important.
- New project iteration events appear for doctors, military officials, and biowarfare researchers.
- Evolution log records the strain change.

Pre-fire evolved opening:

- The first infected state starts with higher hidden disease load.
- Nearby threatened states start closer to infection.
- The owner receives harsher first-response choices.
- The cure track begins with a penalty.

Design factors that make Evolution I more likely:

- high chaos value
- several active infected states
- high cumulative Black Death deaths
- weak global cure progress
- multiple weaponized exposures
- poor containment across borders
- active war around infected states

Design factors that make it less likely:

- strong cure progress
- high containment in infected states
- early successful cleanup
- broad international medical cooperation

Player-facing direction:

The text should show that the disease is becoming less predictable through treatment failures, faster relapses, overloaded hospitals, and local fear. It should not explain hidden formulas or call the change a world-end signal.

## Evolution II - overseas spread

Working label, not final localisation: `overseas spread`.

Evolution II unlocks overseas spread. The disease can now jump through ports, convoys, overseas troop routes, naval invasions, and weaponized incidents.

Active-event evolution effects:

- Ports connected to infected or threatened states become higher-risk nodes.
- Overseas states with active ports can become threatened.
- Convoys, troop transfers, exiled divisions, naval invasions, and refugee routes increase risk.
- Port inspections and travel restrictions become important prevention tools.
- Island states can become infected through ports, but ordinary random island selection should still be weighted by exposure.
- Disease mapmode must update overseas threatened and infected states.
- Evolution log records the first confirmed sea or overseas spread milestone.

Pre-fire evolved opening:

- The first outbreak can still start on the mainland, but port states near the first outbreak begin threatened.
- If the first state has a port or nearby port, one overseas port may start under exposure pressure.
- The owner receives port-focused prevention decisions earlier.

Spread factors after Evolution II:

| Factor | Overseas effect |
| --- | --- |
| Infected port state | High chance to threaten connected ports. |
| Threatened port state | Low to moderate chance to export exposure. |
| Open convoy routes | Increases port jumps. |
| Naval invasion from infected region | Strong temporary spread risk. |
| Large troop movement | Strong risk when units came from infected states. |
| Port inspections | Reduces risk. |
| Travel restrictions | Strongly reduces risk with trade and supply costs. |
| Island quarantine | Strongly reduces risk but damages economy and supply. |
| Weaponized deployment | Can create direct overseas infection. |

Player-facing direction:

The text should focus on sick crews, closed quays, cargo left untouched, sailors refused entry, port districts emptying, and fear traveling along ordinary wartime routes. It should avoid generic global panic phrasing.

## Evolution I and II interaction

If Evolution I and II are active, overseas spread becomes more dangerous because new port infections start harder to treat. Strong port controls and cure progress can still stop the disease from becoming global.

The player should see that a country can lose through geography. A prepared island nation can keep infection out. A busy empire with war convoys and weak port controls becomes a bridge.

## Event Details evolution catalog direction

The Event Details evolution catalog should show that Evolution I changes disease severity and treatment difficulty, while Evolution II changes geographic spread rules. It should not list hidden variables or formulas. It should not describe rat nations until Evolution III is actually included in the catalog preview according to the normal evolution detail rules.
