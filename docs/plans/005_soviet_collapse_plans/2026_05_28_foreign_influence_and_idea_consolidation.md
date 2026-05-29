# Soviet Collapse Foreign Influence and Idea Consolidation

## Overview

Foreign intervention in the Soviet collapse now uses the existing sponsor-influence variables as the main state carrier instead of creating a separate national spirit for every aid track. Recognition, armaments, advisers, trade, construction, press, league logistics, and dependency actions still update their own influence variables, but republics receive a consolidated external-support spirit for the visible country modifier layer.

## Player-Facing Flow

Foreign patrons use the foreign patron decision category to invest in breakaway republics. Target priority is evaluated dynamically from current major status, factories, divisions, faction or League position, recognition, and republican institutions rather than fixed country tags. Each supported republic tracks sponsor influence on a 0-100 scale, with target decision descriptions showing the acting sponsor's influence, total influence, patronage risk, and independence resilience.

Dependency sponsorship also records the acting sponsor by country ID. The older named sponsor buckets remain for the existing display and balance surface, while dynamically qualified countries without a named bucket accumulate unbucketed sponsor influence and can still advance the dependency chain if they invest enough.

Every active intervention commitment applies a temporary sponsor-side consumer goods burden. This is implemented as an active targeted decision modifier rather than a new idea, so multiple simultaneous republic commitments stack without creating extra idea entries.

Republic strength now erodes unused sponsor leverage each month. Stronger republics still attract larger support packages, but current divisions, institutions, and independence resilience make dependency harder if a patron waits too long.

## Balance Rules

Recognition now costs political power and convoys. Liaison offices now cost political power and command power. These costs match the actual complete effects and scale by target tier.

Puppeting is deliberately difficult. A sponsor needs overwhelming influence, high total foreign penetration, local patronage risk, low enough resilience, and the staged dependency chain before a client cabinet can succeed. The current thresholds are:

- Dominant sponsor influence: 70
- Total foreign influence floor: 95
- Strong-republic total influence floor: 130
- Patronage risk floor: 35
- Independence resilience ceiling: 20
- Major-target independence resilience ceiling: 16
- Strong-republic independence resilience ceiling: 14

High-priority targets receive larger influence packages, but also gain independence resilience and shed unused sponsor leverage faster as their army, institutions, and state capacity grow.

## Idea Consolidation

The consolidated republic update now only applies these visible staged idea families:

- republican institutions
- league coordination
- external support
- local authority pressure

Detailed foreign tracks remain as variables for decision unlocks, AI, tooltips, and puppet pressure, but no longer add separate recognition, supply, reconstruction, volunteer, adviser, or patronage spirits.

## Future Extensions

The influence display could be expanded into scripted GUI bars for all active sponsors on a selected republic. That would make the full competition clearer than decision descriptions alone, but the current localisation keeps the system visible without adding a new UI surface.
