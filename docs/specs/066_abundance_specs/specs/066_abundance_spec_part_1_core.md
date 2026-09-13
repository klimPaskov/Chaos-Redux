# Event 066 Abundance

## Catalog entry

- Event ID: `66`
- Event name: Abundance
- Type: Minor Repeatable
- Status during planning: To Be Reworked
- Chaos level: `1`
- Cluster: Sudden Abundance
- Cluster slots: Low, Medium, High

## Event promise

An impossible surplus settles over the world, but it does not take the same form in every country.
One government may find fuel tanks full beyond expectation, another may gain political authority, another may watch a dangerous crisis value climb, and another may discover that a country-specific institution has accumulated more influence than it can safely use.

Every valid country receives four choices built from the values that actually exist for that country at that moment.
The four choices are generated separately for every country.
Two countries affected by one firing can see no values in common.
The same country can see a completely different set when the event repeats.

The player selects one choice.
AI countries choose independently from their own stored choices.
The selected value becomes absurdly abundant.
The remaining three choices disappear without effect.

## What counts as a value

A value is a player-meaningful quantity, stock, capacity, pressure, stage, balance, or owner-defined resource that can be read and changed safely.
It must have a clear semantic identity that can be shown without exposing hidden script state.
It must have an owner-defined operation that represents abundance.

Political Power, Command Power, military experience, Stability, War Support, manpower, fuel, international-market resources, country-specific currencies, crisis pressure, event values, DLC mechanics, and Chaos Redux systems are examples.
They establish the breadth expected from the provider registry, but they do not define a closed pool.

A raw helper variable, temporary calculation, sequence number, hidden proof flag, internal array index, or debug counter is not a value merely because it is numeric.
The owner must expose a semantic candidate before Event 66 may use it.

## Global baseline

When Event 66 fires, the world receives one Abundance wave.
The wave takes a snapshot of every country that can build four valid choice cards and is not already waiting on an unresolved Abundance choice.
Each participant builds its own candidate pool from registered providers.
Each participant receives four stored cards.

At baseline every card contains one value.
The four values should be different whenever the country has enough valid candidates.
The player chooses one card through a normal event option.
AI countries resolve one of their cards through the same stored data and the same application path.

The chosen value reaches its owner-defined abundance state.
An accumulative quantity receives an enormous grant.
A bounded quantity is driven to its upper practical range.
A staged mechanic enters a high valid stage through the owner lifecycle.
A stock or capacity fills according to its own rules.
A harmful pressure rises in the same direction that its public name describes.

## Abundance can hurt

Candidate generation does not remove a value because increasing it is bad.
A corruption value, instability pressure, disease burden, condemnation source, famine pressure, or other low-is-desirable quantity remains eligible when its owner can apply and display it safely.

The system does not reverse harmful values into rewards.
If the candidate is called corruption, abundance means more corruption.
If the candidate is called panic, abundance means more panic.
If the candidate is called food reserves, abundance means more reserves.

Harm classification exists for presentation, evolution weighting, AI judgment, achievements, and audits.
It does not act as a baseline eligibility filter.

## Country validity

A country is valid when all of the following are true:

- it is a live country scope that can receive and resolve the event
- it is not a pure system carrier, dead shell, or invalid temporary actor
- it is not already holding an unresolved Event 66 choice
- its provider pass can produce four distinct card signatures under the current evolution rules
- at least one card can still create a meaningful owner transaction when chosen

Ordinary civilian providers may use the shared normal-civilian classifier.
Nonhuman or special Chaos countries are not excluded as a class.
They participate when their owner systems expose enough valid values, while ordinary values that do not make sense for them stay unavailable through provider validation.

## Repeat firing

Event 66 follows the normal Minor Repeatable weight and cap rules.
A repeat firing performs a new country snapshot and a new provider query.
Earlier choices do not become permanent menu entries.
A value selected before may appear again, but recent appearance and recent selection can be given a modest novelty penalty so the event does not feel stuck on one family.

Novelty never becomes a ban.
Every currently valid value remains capable of returning.
The repeatable event does not build a campaign-long draft deck or consume values permanently.

## Player experience

The event should take little time to understand even when the provider system behind it is large.
The popup presents one shared situation and four compact choices.
Each option line uses the provider's short value name or short bundle name.
The tooltip explains the current amount or stage, the broad abundance result, the target when one matters, and any reliable danger classification.

The player should not need to inspect another mechanic window before choosing.
The choice may still be difficult because the values can be strange, harmful, or connected to systems already under pressure.

## Narrative direction

The event text should describe simultaneous reports of impossible surplus without claiming one universal cause.
It should keep the phenomenon open enough to cover physical stockpiles, political power, institutional values, and active crisis pressures.
The country viewpoint should focus on officials and institutions realizing that several different forms of excess are possible, with one about to become permanent.

The option tone should follow the selected value.
Ordinary resources can use practical or opportunistic wording.
Harmful values can use alarmed understatement, denial, resignation, or grim administrative absurdity.
Country-specific and strange values can use terminology supplied by their owner package.

Final wording must name dynamic values cleanly and must not reveal future secret branches, raw variables, provider IDs, weighting, safety caps, or implementation history.

## Design boundary

Event 66 is a choice generator and abundance transaction system.
It should remain quick at the player-facing layer.
Its depth comes from coverage, replayability, owner integration, harmful possibilities, AI judgment, evolutions, and cluster behavior.
Additional persistent meters or a separate management loop would obscure the event's purpose.
