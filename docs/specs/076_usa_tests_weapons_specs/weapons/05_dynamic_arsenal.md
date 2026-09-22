# 05 · Dynamic arsenal

## An extensible catalogue with real providers

The catalogue must grow from the technologies, equipment, doctrines, projects and owner-exposed weapon systems present in the installed mod and game. It cannot be a short fixed random list that merely rotates twelve named effects.

Use a provider registry with family classification and live availability checks. Build-time enumeration of installed definitions may supply known equipment and technology entries. Runtime triggers then resolve which entries the United States can actually use. This is an implementation approach, not a claim that HOI4 exposes arbitrary runtime reflection over every definition or equipment variant.

The implementation must document what it can enumerate and what requires explicit registration. Newly discovered incompatible definitions are reported instead of silently being treated as ordinary artillery. The registry must accept additional owner-approved experimental systems without another redesign of the event's scheduling, reports or reward logic.

## What each provider supplies

Each provider needs a stable ID, owner, family, current availability predicate, required evolution, test-article source, valid state rules, preparation and analysis timing, physical-effect adapter, exact result receipt and typed reward resolver. It also supplies its presentation family and any continuing-effect ownership.

Availability includes the actual American technology or narrowly authorized prototype route. A delivery system's existence does not grant its payload. A missile provider cannot infer nuclear, chemical or biological warheads from missile technology alone. The same rule applies to aircraft and naval delivery.

A resource requirement must describe a real consumed item or reserved capability. Reusable artillery pieces, aircraft, tanks and ships are not automatically destroyed because they participate in a trial. Consumable experimental articles, missiles or owner-defined stocks can be consumed once. If an ordinary test lacks an appropriate physical stock in the game, represent its preparation through a verified industrial or research allocation. Do not invent an ammunition stockpile that the owning game systems do not contain.

The provider must identify whether its physical adapter already removes population, registers Deaths, changes Chaos, applies contamination, damages units or spends weapons. Event 076 composes those effects without duplicating them.

## Family and variant selection

Select a broad family first, then a compatible current variant. This prevents a family with many equipment definitions from crowding out every other service just because it has more internal entries. A tank family with many chassis and module variants still receives one family-level selection weight.

Within a family, favor a relevant newer or less recently tested variant, an active American research direction, and a state where its declared physical target exists. Older equipment remains eligible when it can still produce useful doctrine, reliability or production findings. A fully exhausted variant with no meaningful remaining benefit should not generate a nominally successful but worthless experiment.

Record recent use at both family and variant level. Recent use reduces preference, not lifetime eligibility. The same variant may return after a delay or when research priorities change. Variety must not become a one-time checklist that permanently removes conventional weapons from the late game.

## Required coverage

The baseline catalogue must represent artillery shells and heavy artillery, aerial bombs, tactical and strategic bombing, incendiary bombing, rockets, available missiles, tank guns, anti-tank weapons, explosives, aircraft weapons, naval guns and torpedoes, and compatible prototype equipment. Some families share preparation infrastructure but must retain different damage and reward identities.

Nuclear prototype and mature nuclear providers enter with their proper authorization. Chemical, biological, weaponized-disease and contamination providers enter through their owners at Evolution III. Other Chaos Redux experimental providers, including relevant laboratory inventions, can register when their effects, costs and military-development outputs are verified.

This list establishes minimum design coverage. It is not the complete future runtime list. The provider inventory must enumerate every compatible installed candidate considered and explain exclusions such as missing effect support, an absent dependency, no meaningful reward or an invalid target contract.

## Meaningful eligibility, not convenient fiction

A naval torpedo trial needs a valid naval target or an owner-approved coastal-installation variant. A generic inland factory cannot stand in for a fleet. A naval-gun trial against a coastal fort is a different valid variant and must be labeled accordingly.

A unit trial cannot say it destroyed deployed tanks when the adapter only reduces a national stockpile. Likewise, a stockpile debit used to pay for an American prototype does not count as enemy equipment destroyed. The record separates test cost, target losses and reward.

A mature nuclear trial requires a real expendable nuclear article or an explicit development-owner issuance. A pre-mature prototype requires the narrow proving-ground route. Disabling a related random event does not automatically delete a shared weapon system, but a feature setting that disables the weapon itself must be respected.

## Availability when optional features are absent

Resolve optional DLC mechanics by capability. When special-project progress is unavailable, use a relevant nuclear or missile technology bonus where that preserves the same development objective. When a specific designer statistic has no supported modifier, use a documented same-family research or production improvement. This is an explicit reward alternative, not an excuse to remove the test's required physical result.

When actual nuclear-scale damage, real state population loss or required disease ownership cannot be supported, the affected provider is blocked. The final implementation cannot claim full specification coverage until those gates are resolved. Unsupported advanced providers must not be hidden behind a generic fallback while the package is marked complete.

## Research-directed player choice

Player USA sees generated valid program emphases such as land weapons, air development, naval systems, delivery systems or the available unconventional program. These are working classifications. Only relevant choices appear, and selecting one biases several jobs without requiring selection of every internal equipment variant.

The chosen emphasis does not authorize tests that fail availability. It does not remove foreign player priority or geographical variety. A general program remains available whenever several different valid families exist. The interface reports expected reward families and preparation commitments before commission.
