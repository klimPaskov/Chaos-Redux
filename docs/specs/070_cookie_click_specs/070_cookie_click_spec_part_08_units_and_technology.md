# 070 Cookie Click: units and technology

## A Cookie army

The Empire's army uses the six requested military families as real unit roles.
They need distinct subunit definitions, equipment, technology unlocks, templates, counters, models and sound coverage.
Renaming vanilla infantry while leaving every consumer unchanged does not satisfy this requirement.

Use the nearest installed vanilla role as the baseline for exact fields and combat width.
The relative targets below guide balance.
They do not claim verified current vanilla numbers.
All final stat values and category membership must be recorded in the unit manifest.

The Cookie body is the common reinforcement component.
Specialist equipment supplies the weapon, armor, oven or riding frame.
Factories produce those components through valid production definitions.
Captured equipment can enter defined conversion recipes or compatible templates.

## The six core families

| Family | Battlefield role | Relative starting target | Limitation |
| --- | --- | --- | --- |
| Cookie Infantry | Main line holder with ordinary ranged weapons | 100 percent of infantry defense, 110 percent soft attack, ordinary organization recovery before the shared appetite modifier | More expensive replacement body and the shared hunger attrition penalty |
| Crumb Swarms | Cheap screens, encirclement fillers and expendable local defense | 50 percent equipment cost, 75 percent defense and 75 percent soft attack of infantry | Poor armor, piercing and staying power, cannot replace a mature line army |
| Chocolate Guard | Expensive assault and capital-defense infantry | 125 percent defense, 150 percent breakthrough and 125 percent soft attack | High equipment and food demand, specialist recruitment cap |
| Dough Golems | Slow shock formations and difficult-position assault | 150 percent breakthrough and 150 percent durability against the matched role | Low speed, high supply use and a large hunger penalty |
| Oven Artillery | Strong soft attack and fort pressure | 150 percent soft attack of comparable artillery, with a focus-unlocked fort role | Vulnerable unsupported and expensive to move and feed |
| Wafer Riders | Fast exploitation, reconnaissance and pursuit | 125 percent cavalry or motorized speed target, depending on the verified equipment model | Fragile in prolonged combat and poor against armor |

A relative target is evaluated against the exact matched unit and technology tier.
Do not multiply every inherited modifier again and accidentally produce twice the intended result.
The hunger modifiers belong to the national appetite system and must not be duplicated in each unit definition.

Cookie Infantry and Chocolate Guard use separately generated and attached firearms.
Oven Artillery requires a distinct body, gun or oven mechanism and firing action.
Crumb Swarms require real multi-body movement or a properly rigged aggregate model.
Dough Golems and Wafer Riders require their own articulated rigs and locomotion.
A single infantry animation renamed for all six families is not acceptable.

## Unlock order

The uprising starts with Cookie Infantry and Crumb Swarms.
Its strength tier may include a small pre-unlocked specialist detachment, but not the entire mature roster.
The military tree opens Chocolate Guard and Oven Artillery in its first major development tier.
Dough Golems and Wafer Riders follow through separate meaningful programs.
The player can develop both, but must pay their different industrial and supply costs.

Specialist development requires the corresponding shaping technology and a real equipment-production path.
A focus that only unlocks a portrait or template does not count as unlocking the unit.

At Level 30 and with the appropriate military capstone, elite forms become available.
At world-end, two additional late formations are authorized: a colossal mobile oven for sustained siege and a small elite monster guard for concentrated assault.
These are working role descriptions, not final localized names.
They require separate models, counters, equipment art, technology and sound packages.
The two late formations must not make the six core families obsolete.

## Recruitment and reinforcement

Use ordinary deployment and reinforcement where compatible, backed by Cookie equipment and the Cookie manpower pool.
Special scripted reinforcement packages are limited to uprising setup, paid conversion operations, major focus payoffs and the world-end launch.
They are not a free daily army generator.

Starting Chocolate Guard capacity is 10 percent of deployed Cookie battalions, with a floor sufficient for one meaningful unit.
Its dedicated branch can raise the cap to 20 percent.
Late elite monster formations use a separate 5 percent battalion share.
These are role caps, not arbitrary fixed division limits that punish a large Empire.

A capacity reduction does not delete existing units.
It blocks further expansion until the army composition is valid again.
The tooltip explains the excess.
The same rule applies when ordinary divisions are disbanded.

Training costs consume actual body and specialist equipment.
A disbanded formation returns only the equipment and manpower that the native system legitimately returns.
Its original conversion or scripted-spawn reward cannot be claimed again.
Template duplication never bypasses the roster's eligibility.

## Suggested template families

These are functional templates for implementation, not mandatory names.

| Template | Composition direction | Use |
| --- | --- | --- |
| Early defensive formation | Cookie Infantry with a small Crumb screen | Survive the host's first counterattack |
| Main line formation | Mostly Cookie Infantry with logistics and limited artillery | Hold a sustainable front |
| Cheap local screen | Crumb Swarms with no costly assault support | Protect rear areas and ports |
| Guard assault formation | Chocolate Guard with Oven Artillery and support | Break a selected defended sector |
| Golem assault formation | Dough Golems with artillery and logistics | Slow, supplied assault on cities and forts |
| Rider exploitation formation | Wafer Riders with reconnaissance and light support | Exploit gaps after infantry wins a battle |
| World-end siege formation | Colossal oven, golems and heavy logistics | Attack fortified global holdouts |
| Monster reserve | Elite monster guard inside a balanced formation | A small high-value operational reserve |

The coder selects exact battalion counts after checking combat width and supply in the installed version.
Each final template must have a reason to exist.
Do not create ten almost identical templates for cosmetic variation.

## Research architecture

Use a compact Cookie shaping technology group with a clear tier graph.
It contains basic bodies, durable bodies, disciplined shaping, oven mechanisms, mobile frames, stable conversion, efficient reinforcement and the two late formation unlocks.
Reuse compatible ordinary weapons, logistics, radio, engineering and industry technologies.

The graph has three ordinary tiers and one world-end tier.
Tier one makes the starting army sustainable.
Tier two differentiates specialist roles.
Tier three creates mature combined-arms forces.
The world-end tier unlocks the two late formations and the highest consumption efficiency.

A technology may improve an existing unit, unlock an equipment tier, open a recipe or satisfy a focus gate.
Avoid duplicate technologies that each add a small generic attack bonus.
Every technology needs an icon, a real effect and a route in the AI research plan.

Technology grants are additive and compatibility checked.
Do not copy every host technology into the new country without checking exclusive branches.
Preserve useful ordinary military and industrial knowledge where compatible.
Do not copy an advanced doctrine and simultaneously unlock its exclusive competitor.

## Army doctrine

A Hungry State chooses a governing method.
Legions of Dough separately chooses a military emphasis.

The mass branch favors Crumb screens, cheap bodies and fast replacement.
It sacrifices elite quality and creates greater total appetite through army size.
The disciplined branch favors Cookie Infantry and Chocolate Guard, with better recovery and more expensive losses.
The heavy branch favors golems and ovens, with strong breakthrough and a demanding supply network.

These emphasis branches use real mutual exclusions only for their central doctrine commitment.
Basic reconnaissance, logistics, anti-air, engineers and medical or repair support remain common where compatible.
The military spirit carries the doctrine stages within the three-spirit limit.

The doctrine choice should change AI templates, equipment production and operation priorities.
A label that changes only a hidden variable is insufficient.

## Air power

Use captured or built ordinary aircraft with Cookie country identity and appropriate asset skins where the final consumer supports them.
A separate fictional aircraft family is not required for the six requested land families.

The air branch first secures airfields, repair capacity, fuel and a small viable aircraft reserve.
It then chooses emphasis between defensive interception and army support.
Later programs improve operational reach and coordination with the Cookie assault army.
Actual aircraft production and technology remain necessary.

An inland Empire can develop air power.
A country without a usable airfield first receives a targeted construction route.
Do not grant aircraft to a country that cannot base or supply them.

## Naval power

A landlocked Empire can see the future naval branch but cannot spend resources on unusable ships.
Capturing or receiving a viable port opens the first coastal program.
The early route provides convoy production, port repair and naval invasion preparation.
Later routes develop escorts, raiding or a surface-fleet core.

The global conquest route must be able to reach overseas enemies.
It therefore requires a verified path to transports, sea access, operational range and the relevant invasion technology.
The Final Bite does not teleport divisions onto a different continent to hide a missing navy.

A small island uprising receives a bounded coastal survival package from its initial budget.
Its early AI prioritizes leaving the island and protecting a supply route.
A continental uprising can delay major naval spending until it reaches a coast.

## Units as shared project content

Each subunit and equipment family needs its owning provider registration.
Distinguish a new unit provider, a support attachment and a parent-owned equipment family.
Do not add unused providers merely to fill a registry.

The CXT test-country extension must expose every new unit, equipment tier, technology and template through its established idempotent setup.
Its carrier must be hidden and modifier-free.
Startup application and repair are bounded and tag scoped.
Document the exact inventory and expected unlock state.

## Military counterplay

Conventional armies should have practical responses.
Destroying supply routes hurts heavy Cookie formations.
Armor and piercing punish Crumb screens.
Mobile forces can isolate slow ovens.
Air attacks can disrupt exposed bakery states.
Taking a key industrial state can create food pressure without special scripted immunity.

Do not give the Empire universal terrain immunity, unlimited organization, free fuel or complete protection from normal combat rules.
Its strength comes from a developed economy of consumption and an increasingly dangerous roster.
Its opponent should be able to observe that economy and interrupt it.
