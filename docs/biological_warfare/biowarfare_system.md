# Biowarfare System (Mechanics Guide)

This is a player-facing guide to Chaos Redux biowarfare.

It explains what the system does in gameplay terms: what you unlock, how you deploy it, what spreads, and how to contain it.

## Big Picture

Biowarfare has seven connected pillars:

1. Development and unlocks.
2. Payload production and exact stockpile safety.
3. Delivery by native raids and operative operations.
4. Incubation, detection, and state contamination.
5. Spread between states and countries.
6. Medical containment and recovery.
7. Evidence, attribution, deaths, and Condemnation.

It is a long-horizon system: strong strategic impact, high political risk, and heavy management demands.

## Development and Unlocks

Bioweapons are unlocked through special project progression.

Each completed project opens practical deployment options for that agent family and increases your strategic leverage, but also raises risk.

Overall weapon strength follows `Tularemia < Anthrax < Plague < Smallpox`.

Tularemia is low severity, Anthrax is moderate, Plague is serious, and only Smallpox belongs to the severe weapon tier.

Agent identity changes the harm that follows a release, not the native chance that a raid reaches its target.

That means:

- safer research paths reduce the chance of your own program backfiring,
- some projects let you prepare domestic medical countermeasures while research is still underway,
- skipping those protections can leave you exposed if accidents or later retaliation reach your own territory.

## Delivery

Deliberate battlefield and strategic deployment uses dedicated native raids.

Operative release uses the intelligence-operation route, while food, water, and medical sabotage uses its separate covert route.

The historical Japan-China campaign uses exact-state Anthrax and Plague decisions on its explicit route, and the exceptional doomsday release remains a decision.

Those exceptions consume exact payload and enter the same ordinary lifecycle; they do not replace the native raid system for ordinary strategic or battlefield deployment.

In practice:

- native routes reserve or consume the exact matching payload,
- the raid or operation supplies the exact target state and responsible actor,
- the ordinary lifecycle creates incubation before an outbreak becomes active,
- detection, deaths, medical pressure, evidence, attribution, contamination, spread, and Condemnation continue after the initial release.

All four ordinary agents use the same native strategic-raid success, critical, and disaster factors and the same native battlefield-raid success factor.

Aircraft, air defense, intelligence, assignment, headquarters preparation, and other verified operational conditions can change delivery reliability.

The selected agent changes post-release potency, incubation, detection, persistence, spread, treatment, deaths, and medical pressure.

## Contamination Effects

Contaminated states suffer major penalties to local performance.

Typical consequences include:

- weaker local economy and logistics,
- reduced military efficiency,
- growing pressure on stability and war capacity.

Different agents create different contamination profiles.

## Spread

Contamination can spread into neighboring states if not contained.

Spread chance is influenced by broader conditions such as:

- preparedness,
- infrastructure and local capacity,
- social and wartime stress,
- public-health response strength.

Some agents spread faster and are harder to stabilize than others.

## Countermeasures

You are not locked into passive defense.

Available responses include:

- emergency containment decisions,
- medical production programs,
- vaccination-scale mitigation for Smallpox and agent-specific treatment or containment for the other ordinary agents.

A strong response can slow spread, reduce damage, and eventually clear contamination.

## Stockpile Safety and Accidents

One exact owned biowarfare facility is designated as the national arsenal.
Anthrax, Plague, Tularemia, and Smallpox inventories are read from their live
equipment stockpiles and combined with Biosecurity, safety technology, facility
condition, bombing, sabotage, and recent handling.

The player sees one of four bands: Controlled, Strained, Dangerous, or Critical.
Ordinary incidents range from a contained loss to an internationally exposed
major outbreak. The exact matching equipment is debited once, and every
non-contained result enters the shared incubation and outbreak lifecycle in the
exact arsenal state.

Biowarfare therefore includes internal risk:

- high-risk research choices can backfire,
- stockpile mismanagement can cause catastrophic domestic consequences,
- emergency release paths are possible but extremely dangerous politically and strategically.

Stockpile accidents are cooldown-gated per payload type. After an Anthrax,
Plague, Tularemia, or Smallpox stockpile accident, that same payload type cannot
produce another ordinary accident for 730 days. Other payload types keep their
independent cooldowns. Fail-Safe Containment Facilities stop ordinary accidents
but do not stop sabotage, bombing, capture release, or doomsday release.

See [Biological Stockpile Safety](biological_stockpile_safety.md) for exact
designation, risk-band, scheduler, lifecycle, AI, and asset contracts.

## Diplomacy and International Consequences

Biological weapon use carries major diplomatic costs.

Repeated use drives increasing international backlash and can reshape your strategic relationships, especially with ideologically opposed blocs.

## AI Behavior

AI chooses research, production, stockpile safety, countermeasures, and delivery according to country program, doctrine route, war state, retaliation status, medical readiness, likely friendly spread, sanction exposure, and target evidence.

Ordinary profiles avoid biological first use.

Retaliatory, historical Japan-China, high-chaos, radical, and near-defeat routes can become more aggressive only after their explicit gates are satisfied.

Agent-specific route preferences may differ because their strategic effects differ, but AI preference never changes the equal native raid-success factors.

## Player Strategy Notes

- Biowarfare is strongest when paired with a containment plan of your own.
- Raid success is only part of the story; post-strike pressure and spread management matter more.
- Overuse can win short wars but lose long diplomatic positioning.

## Implementation surfaces and remaining validation

Strategic and battlefield raids, operative release, food-water-medical sabotage, the Japan-China campaign decisions, field testing, stockpile accidents, captured-facility recovery raids, doomsday release, agent-specific incubation and treatment, evidence, attribution, deaths, contamination, spread, and designer integration all enter the ordinary biological lifecycle.

Captured facilities are secured or destroyed through native land raids and never through a deployment decision.

The doomsday route remains the explicitly authorized decision exception.

Package scenario validation, balance recording, and the mapped specialist completion audits remain part of the wider CBRN completion stages and are not claimed by this guide.
