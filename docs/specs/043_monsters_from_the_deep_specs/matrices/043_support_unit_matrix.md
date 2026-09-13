# Event 043 support-unit matrix

## Shared family rules

Every family uses zero ordinary manpower and no normal equipment. Units enter through Event 043 receipts, focuses, decisions, scenario setup, or terminal milestones.

| Family | Role | Combat direction | Earned spawn sources | Model direction | Sound roles | Counter direction | Limits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Riptide Shoal | Fast amphibious screen | High speed, low armor, strong amphibious movement, modest staying power | Port capture, island-chain objective, or successful pursuit mission | A coordinated school of medium aquatic predators that reads as one formation | Water rush, grouped calls, movement, attack impact, and death dispersal | Fast swarm silhouette with clear forward motion | Cannot hold deep inland fronts and should not become a cheap universal line unit |
| Abyssal Raider | Mobile coastal assault | Balanced attack, breakthrough, pursuit, and port assault | Coastal capital objective, raiding focus, or earned Hunger expenditure | Large amphibious hunter with limbs suited to brief land movement | Wet footfall, scrape, call, attack, impact, and collapse | Single aggressive amphibious silhouette | Moderate durability and rising inland weakness |
| Reefbreaker | Heavy siege brute | High hard attack and fort pressure, low speed, strong coast defense | Fortified port destruction, reef-lair focus, or heavy brood milestone | Armored crustacean or plated brute with clear siege anatomy | Shell grind, heavy step, strike, structure impact, and shell collapse | Broad plated silhouette with a crushing limb | Expensive reinforcement receipt and poor pursuit |
| Trench Stalker | Ambush and defense | High defense and surprise pressure, good night fighting, low open-ground attack | Lair defense, blue-hole or fog route, or successful coastal consolidation | Dark deep-sea predator with readable limbs and a low silhouette | Low call, scrape, submerged movement, ambush strike, and death withdrawal | Low angular predator silhouette | Weak when forced into exposed inland battle |
| Venom Brood | Disruption and attrition | Organization damage, recovery suppression, modest direct attack | Poison, ink, venom, or disease-themed route milestone | Multi-creature brood with clear toxic anatomy and no CBRN equipment | Hiss, wet movement, spray, impact, and dispersal | Coiled or spined swarm silhouette | Cannot independently break strong fortified lines |
| Drowned Colossus | Slow line anchor | High defense, armor, and strength, low speed and poor amphibious initiative | Major feeding reserve, deep-lair capstone, or terminal reinforcement | Large non-apex brute whose scale remains visibly below the named creature | Deep call, heavy movement, body impact, attack, and collapse | Tall heavy silhouette with a low center of mass | Strict cap, high earned cost, and severe inland supply pressure |

## Required runtime identifiers

Each row must resolve:

- subunit ID
- division template ID
- owner-side unit-family disposition
- spawn helper
- sustainment helper
- cap and cleanup helper
- localisation
- icon
- map counter
- 3D entity
- material
- idle action
- locomotion action
- attack action
- death action
- sourced selection sound
- sourced acknowledgement sound
- sourced movement sound
- sourced idle sound
- sourced attack sound
- sourced impact sound
- sourced death sound
- CXT setup effect
- provider registration
- runtime test receipt

## Cap rule

Drowned Colossi and Reefbreakers use the strictest caps. Riptide Shoals and Abyssal Raiders remain easier to raise, while Hunger and lair capacity still prevent spam.
