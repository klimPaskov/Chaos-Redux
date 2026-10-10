# Military Madness: Campaign and Presentation

## Acting on an advantage

Military Madness gives the player a deadline and a reason to reconsider existing plans.
It does not choose those plans.

A speed result can turn a limited offensive into an attempt to cut a rail junction or close a pocket.
It does not protect an overextended spearhead.
A defense result can support a delaying action while factories replace lost equipment.
A recovery result can support repeated attacks, but the army still needs a viable front.

An extreme armor result can make ordinary opposition ineffective until the enemy changes its equipment or rolls a countervailing piercing result.
A planning bonus rewards preparation, while a near deadline can make a long preparation waste the opportunity.

A weak naval power can spend the year building a force that benefits from its roll, use what it already owns, or leave the bonus unused.
The event provides no free fleet.

## Reading an enemy

An opposing country can hold its own exceptional advantages, including the one that counters the player's result.
The event does not equalize the two sides.
Combat, reconnaissance and the normal national-information interface remain the only sources of knowledge about an enemy's results; the package rows are visible only to their own country.
An enemy package expiring can open an opportunity, but the player learns of it only through what the normal interface shows.

## Overlapping opportunities

Repeated firings create different clocks.
A country might hold a strong defense result that ends soon and a newer offensive result that lasts much longer, and can attack before the protection disappears or keep the newer advantage in reserve.
A broad result and a narrow terrain result can align with one front; the event does not name or construct that pairing.
A saturated reduction can stay at its limit while enough surviving contributions support it, so the player needs to see the next change rather than assume every expiry removes everything.

## AI behavior

AI countries receive exactly the same draw counts, broad minima, magnitudes, duplicates and expiry as human countries, with no archetype, war order or reroll.
The native military calculations must include every bonus; a custom Chaos Redux statistic needs a real military consumer, not a tooltip.

The AI also uses what it rolls, without changing any draw:

| Active result | AI response while the contribution lasts |
| --- | --- |
| Land attack, breakthrough, speed or organization recovery totaling at least +200% across active packages, while at war | A temporary aggressive front-control strategy toward its current enemies |
| Naval invasion preparation or capacity, while at war with a coastal enemy | A temporary raised naval-invasion priority |
| Defensive results only | No change |

The strategies end when the qualifying contribution expires.
They create no war, target or reward, and the AI probability auditor checks that they do not dominate ordinary AI planning.

## Player information

The opening report explains the anomaly and names the stage, the 365-day duration and the country's actual results.
Reading, postponing or reopening it never changes the package.
Event Details holds the premise and progression only, never rolled values.

### The combined spirit

The country has one visible Military Madness spirit built on a dynamic modifier.
Its native tooltip shows the applied total for each statistic across all active packages, plus one line for any statistic held at a technical limit (Part 3) and the date of the next expiry.
Ten rolls never become ten spirits.

### Package rows

Each active package appears as one row in the Military Madness decision category, using the native timed-decision display for its remaining days.
The row's tooltip lists that package's stage and every individual roll, including duplicates, with signs and units.
Rows cost nothing, do nothing when hovered or opened and cannot consume randomness; there is no reroll, selection, renewal or exchange control.
The category is hidden while the country has no active package.

The row pool is sized for the most packages the event's repeat cadence can overlap within 365 days, and the implementation documents that bound; a package must never exist without a row.
No dedicated scripted GUI is needed.

## Report tone

The humor comes from military professionals trying to explain impossible results in ordinary reports: instruments fail, staff estimates turn absurd, officers insist the improvement proves their doctrine.
Each stage raises the scale: a startling result at baseline, several incompatible successes in Military Insanity, unreliable terrain and conditions in Impossible Warfare, and familiar military categories failing to describe what armies do in Gods of War.
The writing stays concrete and never implies that every country rolled the same thing, that the report caused the bonus or that free units were granted.
Final text is written during implementation from these directions.

## Connections with other events

Doctrine Research can give a country methods for using a temporary advantage; Military Madness spends or grants no doctrine choices.
Law Upgrade can raise mobilization while Military Madness improves what the forces can do; neither refreshes the other.
Agency Upgrade and Intel Leaked affect what governments know through their own systems and never expose another country's package rows.

When the recipient already has a [World Claims target](../086_world_claims_specs/086_world_claims_spec_part_4_integration.md), a useful speed, attack, defense or recovery result creates a choice between taking that state during the package and consolidating ground already held.
The target must carry the recipient's own World Claims provenance, and ordinary diplomatic restrictions still decide whether an offensive is possible.
Control and high-Compliance intervals run under World Claims rules even if the military advantage ends earlier.
Expiry removes only the sampled contribution, leaving holdings, spent integration entitlements and valid control history intact.
A speed result cannot substitute for holding time, and a claim cannot supply divisions.
If an offensive fails and control is lost, World Claims resets its clocks under its own rules without refreshing the package.
This connection adds no war order, reward or claim wave.

Equipment, naval and reinforcement events can make an unused result useful later, without extra trigger chance.
Movement restrictions and division locks stay authoritative over speed results, and a supply or fuel crisis still matters, especially after expiry.
Other bonuses combine through the game's normal calculations.

## Chaos impact

A naturally committed worldwide occurrence adds +5 Chaos once, at any stage.
The planning rules give a pre-fire evolved opening no extra Chaos for its stage, and the larger packages' consequences reach Chaos through the wars, deaths and destruction they cause, which their own systems already count.
Recipients and rolls never multiply the impulse.

Reports, package rows, recomputation, threshold changes and expiry add nothing.
Debug or forced occurrences create no Chaos and no achievement progress.
Each natural repeat is a new manifestation with its own impulse, under the existing repeat weights and cluster pacing, and any generic member or cluster shock for the same occurrence is not added a second time.
