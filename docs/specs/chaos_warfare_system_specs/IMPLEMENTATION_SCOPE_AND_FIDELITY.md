# Fictional Game Scope and Implementation Fidelity

## Purpose

This package specifies a fictional Hearts of Iron IV mod system. It intentionally uses direct terms such as chemical warfare, biological warfare, nerve agents, gas masks, chemical shells, chemical air bombs, outbreaks, civilian deaths, military deaths, population loss, contamination, suppression, and Condemnation because those are the game systems being designed.

These terms are not a request for real-world operational guidance. Implementation must remain at Clausewitz game-script level and may use abstract equipment units, agent profiles, state modifiers, probability bands, casualty formulas, stockpile costs, mission effects, and AI weights.

## Required implementation approach

- Keep player-facing text specific when clarity benefits. Use the actual in-game technology, agent, equipment, unit, and operation names defined by the accepted package.
- Keep the tone factual, period-appropriate, and focused on consequences. Do not celebrate suffering or turn mass death into casual humor.
- Implement every accepted mechanic, formula, unit, equipment family, delivery path, countermeasure, AI behavior, designer, asset, achievement, and audit requirement.
- Do not generalize chemical and biological systems into one generic hazard mechanic.
- Do not collapse distinct agent profiles, delivery types, protective systems, disease behavior, or national programs into cosmetic variants.
- Do not reduce deaths, population loss, suppression, contamination, outbreak severity, or Condemnation because the subject is severe.
- Do not remove offensive features required by the specs, including chemical shells, air bombs, armored delivery, raids, outbreak weapons, suppression operations, and last-resort releases.
- Keep every use path integrated with protection, logistics, detection, attribution, weather, terrain, treatment, cleanup, evidence, Condemnation, sanctions, retaliation, and AI behavior.
- Use exact historical names only where the package calls for them and source checks support them.

## Non-procedural boundary

The implementation agent must not add real-world synthesis recipes, culturing steps, weaponization procedures, storage or handling instructions, dose calculations, dissemination engineering, target-selection advice, or other operational detail that could be used outside the game.

Historical research should support names, broad capabilities, protective equipment, institutions, national programs, and period context. Gameplay realism must come from abstract mechanics such as equipment demand, weather, terrain, persistence classes, protection coverage, medical capacity, detection, evidence, casualty bands, population effects, and diplomatic consequences.

## Public-facing wording

Public-facing text may directly name chemical warfare, biological warfare, nerve agents, specific agent classes, chemical artillery, chemical air bombs, gas masks, outbreaks, deaths, population loss, contamination, and suppression. The wording should be clear enough that the player understands the system and its consequences.

CBRN may remain an internal umbrella label where useful. It must not replace more specific terms when the player needs to understand what an action, technology, unit, or consequence actually represents.

## Conflict rule

This file does not soften or override the numbered specs, matrices, balance tables, or specialist prompts. It only clarifies how to interpret and implement them.

If an implementation choice trades depth for vagueness, the deeper accepted mechanic controls. If wording can stay specific without adding real-world procedural detail, keep it specific.

## Completion standard

Any omission, merging, weakening, renaming into a generic system, or smaller substitute justified by subject sensitivity is a simplification and must be treated as incomplete. A compliant implementation preserves the full game design while keeping all technical work inside fictional game abstractions.
