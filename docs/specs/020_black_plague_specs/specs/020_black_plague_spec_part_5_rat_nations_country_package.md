# 020 Black Plague spec Part 5 - Rat nations and Evolution III

## Evolution III purpose

Working label, not final localisation: `rat nations`.

Evolution III turns uncontrolled Black Death states into nonhuman political actors. In the most diseased and broken regions, rat nations can appear. They are not ordinary breakaway countries. They are hostile nonhuman swarms that use mutated rats as units, ignore human manpower and equipment, and keep spreading plague in occupied states.

This evolution should be rare in a controlled campaign and terrifying in a neglected one. It should require connected infected states or deeply diseased states with high rat warren pressure. It should not happen just because one state was infected for a short time.

## Rat emergence conditions

Rat nations can appear when several conditions combine:

- one or more states have collapse-level infection
- rodent pressure is high
- rat warren pressure is high
- containment failed for a long period
- cumulative local deaths are high
- states are connected to other infected states
- the owner is weak, occupied, at war, or has low control
- chaos tier is high enough for Evolution III
- no strong cleanup or army containment is active

The first emergence should prefer the worst infected connected state group. A state with higher population, higher deaths, more disease load, and longer neglect should create a stronger rat country.

## Breakaway shape

A rat nation can break away from one or more connected infected states. It should not clear the Black Death modifier. Rat-held states remain plague states.

Initial territory:

- one state for a small emergence
- several connected infected states for a severe emergence
- a larger pocket if many connected collapse states exist

The rat nation should receive cores or special control logic only where needed to function. It should be treated as a special chaos country and as an actual nonhuman country. Normal systems that assume human governments should exclude it through shared nonhuman triggers.

## Initial army scaling

The rat nation should start with a strong army. It should not be easy to wipe out immediately.

Initial rat army strength should scale from:

- number of infected states released
- state population before deaths
- cumulative local deaths
- current disease load
- rat warren pressure
- infrastructure and urban density
- chaos value
- evolution stage
- owner weakness
- whether the state was weaponized

The worse the disease in the released state, the stronger the starting army.

Suggested opening bands:

| Emergence band | Conditions | Army direction |
| --- | --- | --- |
| Small warren | One collapsed state, moderate death total | Several strong mutated-rat divisions, enough to resist local militia. |
| Major warren | Multiple connected collapsed states | Large initial swarm with defensive bonuses and fast reinforcement ticks. |
| Black warren | Weaponized or long-neglected cluster | Heavy swarm army, strong attrition pressure, and immediate neighboring threat. |
| Continental nest | Huge uncontrolled infected region | Major chaos country with enough force to threaten surrounding powers. |

## Mutated rat units

Rats are not human. They do not use manpower or ordinary equipment. The player should not manually deploy rat units. Rat nations gain units through periodic ticks, focuses, state control, and plague pressure.

Unit rules:

- Mutated rat divisions are stronger than ordinary infantry in raw shock, breakthrough, recovery, and attrition pressure.
- They should have weaknesses such as poor armor, low air defense, poor anti-tank, or vulnerability to specialized containment operations.
- They should ignore human manpower and most equipment costs.
- They should grow faster in high-population infected states.
- They should gain more units over time if they occupy plague states.
- They should not require the player to train them manually.
- They should have special attrition or terrain behavior if supported by the implementation.

Template families:

| Template family | Use |
| --- | --- |
| Warren swarm | Core rat infantry replacement, stronger than basic infantry. |
| Sewer rush | Fast attack unit for urban and infrastructure-rich states. |
| Plague gnawers | Attrition and breakthrough unit that worsens state disease load. |
| Burrow guard | Defensive garrison unit for rat-held plague states. |
| Brood mass | Late rat nation unit with large width and high soft attack. |

## Rat reinforcement tick

Rat nations should grow through a tick. The tick should be dynamic and tied to occupied plague states.

Tick factors:

- number of rat-held plague states
- population remaining in those states
- local disease load
- rat warren pressure
- active focus bonuses
- King of Rats command if Evolution IV happened
- enemy containment pressure
- supply and terrain
- continent control

The tick should create units, strengthen existing units, or add temporary combat buffs. It should not produce ordinary equipment. Human countries fight rats by retaking territory, lowering plague load, clearing warrens, and using military containment decisions.

## Rat diplomacy and hostility

Rat nations are hostile to everyone except themselves. They should not join normal factions, accept normal diplomacy, or behave like ordinary minors.

Rat-to-rat behavior:

- Rat nations do not fight each other by default.
- If two rat nations border each other, the stronger should eventually annex the weaker.
- Annexation transfers units or growth pressure to the stronger rat nation.
- This prepares the world for the King of Rats unification path.

Human-to-rat behavior:

- Nearby countries should receive military containment decisions.
- Countries at war with rats can create cordon lines, emergency forts, anti-rat operations, evacuation decisions, and joint response actions.
- The disease board should show rat-held states as infected and militarized.
- Biowarfare countries may try to study rat-held plague, with high accident risk.

## Rat country package

Working tags, not final implementation tags:

| Working tag | Role | Notes |
| --- | --- | --- |
| `RAT_A` | first rat nation template | Used for first breakaway if available. |
| `RAT_B` | second rat nation template | Used for another connected region. |
| `RAT_C` | extra rat nation template | Used if several nests emerge. |
| `RAT_D` | reserve rat nation template | Used for high-chaos multi-region outbreak. |
| `RAT_KING` | King of Rats country | Separate country for Evolution IV. |

Final tags must avoid conflicts and use shared special-chaos and actual-nonhuman classifiers.

Country package matrix:

| Surface | Rat nation direction |
| --- | --- |
| Public name | Short rat-country names tied to nest, warren, or swarm identity. Final names are implementation localisation, not planning copy. |
| Leader | Institutional or creature leader portrait for ordinary rat nations. A one-rat personal leader is not required for base nests. |
| Portrait | Generated fictional nonhuman portrait or symbolic warren portrait. |
| Flag | Fictional flag with rat, plague, warren, or black-mark symbol. Needs normal, medium, and small sizes. |
| Ideology | Fixed high-chaos nonhuman ideology or event-specific ideology mapping if the repo supports it. |
| Parties | Nonhuman institutional party names, not normal human parties. |
| Starting ideas | Plague immunity, nonhuman swarm, warren growth, hostile to humanity, poor diplomacy. |
| Focus tree | Base rat tree with survival, swarm growth, warren building, plague spread, and annex weaker nests. |
| Units | Mutated rats, automatic growth, no manual training. |
| AI | Pure aggressive expansion and survival logic. |
| Economy | Uses warren growth and plague-state control instead of normal production identity. |
| Diplomacy | No normal diplomacy, hostile to humans, rat annexation logic. |

## Base rat focus-tree architecture

Base rat countries need focus trees, but they should be smaller than the King of Rats tree. The tree should make each rat nation dangerous and playable enough if a player switches to it.

Architecture map:

| Lane | Purpose | Focus group direction |
| --- | --- | --- |
| Awakening warren | Establish the rat country after emergence. | Stabilize control, reveal nonhuman identity, harden rat-held state. |
| Swarm growth | Increase automatic rat unit growth. | Brood chambers, scavenging, corpse-feeding, tunnel nests, mass swarms. |
| Plague spread | Turn occupied states into plague states faster. | Infect roads, poison depots, spread through ports after Evolution II. |
| Human war | Improve combat against human countries. | Night attacks, urban swarms, supply sabotage, border breaches. |
| Warren defense | Make nests harder to destroy. | Burrow forts, attrition defense, hidden reserves, infected ruins. |
| Rat annexation | Absorb adjacent rat nations. | Compare strength, annex weaker nest, inherit units, prepare unification. |

Reward style:

- unit growth upgrades
- state infection upgrades
- local attrition effects
- warren defense ideas
- stronger mutated rat templates
- automatic unit ticks
- AI aggression changes
- annexation decisions against weaker rat nations

Avoid:

- normal human economic focus rewards as the main tree identity
- generic political power rewards
- normal diplomatic focuses
- ordinary manpower or equipment grants

## Base rat AI

Base rat AI should:

- attack nearby weak states
- prioritize infected and threatened neighbors
- avoid naval fantasy until Evolution II and port access exist
- absorb weaker adjacent rat nations
- defend core warren states
- grow units through plague-state control
- target high-population states when strategically possible
- ignore normal diplomacy
- avoid suicidal attacks against overwhelming major powers until swarm growth is high

## Human counterplay to rat nations

Humans need ways to fight rat countries beyond ordinary fronts.

Counterplay families:

- emergency anti-rat cordon in bordering states
- evacuation of threatened high-population states
- burn out warrens after retaking a rat-held state
- anti-rat field hospitals and cleanup crews
- fortify rat border lines
- special operations against nests
- global cooperation when rats control enough states
- defeat recovery decisions after rat states are cleared

Human counterplay should use equipment, manpower, supply, stability, and industry. It should not be a simple political power click.
