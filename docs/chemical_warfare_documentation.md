Summary: Player-facing and technical chemical warfare guide for Chaos Redux, covering delivery systems, contamination rules, logistics, and diplomatic consequences.

# Chemical Warfare System

## Overview

Chemical warfare is implemented as one connected gameplay package:

1. Chemical cylinder abilities for generals.
2. Chemical Livens support companies (per chemical type).
3. Chemical tank support companies (per chemical type and chassis class).
4. Nerve-agent raid options (Sarin and Soman).
5. US special-project raid options (Malodor and Aphrodisiac bombs).
6. Global diplomatic backlash (international condemnation).
7. Chemical air bomb modules marked as under-development.

The system rewards preparation and logistics while making repeated chemical use politically costly.

## System Structure and Behavior

- Chemical support companies are type-specific (chlorine, phosgene, mustard, lewisite, sarin, soman).
- Contamination from support companies is applied only when those supports are confirmed in active combat.
- Payload requirements for Livens and chemical tank supports use a 10x multiplier, so sustained operations require dedicated supply planning.
- Livens and tank support are tuned for high battlefield pressure with reduced staying resilience.
- The nerve branch uses G-series progression:
  - GA (Tabun) -> GB (Sarin) -> GD (Soman).
- Nerve raids are tactical and short-lived in contamination persistence.
- US special-project raids are also short-lived and focus on disruption rather than direct casualties.
- US special-project raids do not add international condemnation.
- Air bomb modules are visible in progression, while plane-based contamination and condemnation behavior remains disabled.

## Core Gameplay Flow

1. Research a chemical type.
2. Unlock the matching chemical payload family.
3. Choose a delivery method:
   - General ability,
   - Livens support company,
   - Chemical tank support company,
   - Nerve raid (Sarin/Soman),
   - US special raid (Malodor/Aphrodisiac).
4. Execute usage while managing condemnation growth.
5. Adjust operations around weather, stockpiles, and diplomatic pressure.

## Cylinder Abilities (General Abilities)

These are command abilities tied to generals.

- Provide fast tactical impact.
- Performance depends on stockpile depth and combat conditions.
- Weather and terrain can amplify or reduce effectiveness.
- The visible ability timer matches the full active window of the applied 7-day chemical attack buff.
- Frontline contamination is applied to the active frontline touched by the attacking army. The system prefers enemy-adjacent states and falls back to the leader's bordering controlled state if the enemy-side state count cannot be resolved cleanly.
- Usage against human targets contributes to international condemnation.
- Cylinder use against zombie-held fronts does not add condemnation.
- Japan's general-led cylinder use during the China campaign adds reduced condemnation instead of the full normal amount.

## Livens Support Companies

Livens support is separated by chemical type.

- A division template selects one chemical-specific Livens support variant.
- Each variant consumes Livens hardware plus matching chemical payload stock.
- It adds chemical pressure during active ground combat.
- Contamination and condemnation from Livens apply only when that support is confirmed in active fighting, and combat condemnation no longer depends on a separate state-contamination flag landing first.

## Chemical Tank Support Companies

Chemical tank supports are separated by chemical type and chassis class.

- Light, medium, and heavy support variants exist per chemical type.
- They are support-role units and can coexist with flamethrower support.
- Each variant consumes tank equipment plus matching chemical payload stock.
- Payload requirements use a 10x multiplier, making logistics a primary limiter.

Balance profile:

- Strong offensive support in chemical-favorable engagements.
- Lower long-fight resilience and staying quality than conventional support paths.

## Contamination Behavior

Ground-support contamination from Livens and chemical tank supports is:

- combat-gated,
- weather-influenced,
- chemical-profile-dependent.

Practical rule:

- If chemical supports are not confirmed as active participants in combat, contamination does not trigger.

## Nerve Agent Branch (GA/GB/GD)

Nerve sequence:

1. Tabun (GA): entry point to nerve agents.
2. Sarin (GB): stronger tactical nerve profile.
3. Soman (GD): highest short-window tactical pressure.

Nerve agents are high-intensity and lower-persistence battlefield tools.

## Nerve Raids

Sarin and Soman raids are dedicated strike options.

- Strong direct military disruption.
- Short contamination persistence relative to persistent agents.
- Significant diplomatic cost when used repeatedly.

## US Special Chemical Raids

The malodor and aphrodisiac bombs are US-only special-project raid payloads.

- Delivered only through raids.
- Built around temporary state disruption rather than major strength damage.
- Malodor adds immediate org shock plus severe short-term disruption.
- Aphrodisiac focuses on coordination, planning, reinforce, and defense breakdown.

## International Condemnation and Diplomacy

Most major chemical delivery paths feed condemnation:

- cylinder abilities,
- Livens support combat use,
- chemical tank support combat use,
- nerve raids.

Exception:

- Cylinder abilities used only against zombie-held fronts do not add condemnation.
- US special-project malodor and aphrodisiac raids do not add condemnation.
- Japan's targeted chemical campaign decisions against China do not add condemnation.

As condemnation rises, external diplomatic pressure and penalties intensify.

## Defensive Mitigation

Chemical protection research is a core countermeasure layer.

- Gas masks reduce chemical harm in modeled mitigation paths.
- Dimercaprol provides additional protection, especially for blister-agent interactions.
- `Gas Mask Defense` is treated as defensive counterplay and is not intended to add international condemnation by itself.

## AI Behavior

AI treats chemical warfare as a strategic path with tradeoffs.

- It evaluates escalation pressure.
- It does not use general-led cylinder abilities unless enemy condemnation is already considerable, except for Japan's China war exception.
- Only Japan is allowed to use the general-led cylinder abilities against Chinese war targets.
- It still incurs condemnation costs from overuse.
- It does not proactively select `tactic_chemical_shelling` as a normal combat tactic.
- `tactic_gas_mask_defense` is reserved for counterplay rather than proactive tactic picks.
- `tactic_chemical_barrage` remains the doctrine-specific automatic chemical tactic for `chaos_warfare`.

## Chemical Air Bomb Modules

Chemical air bomb modules are marked as under-development content.

- They are present in progression and UI.
- Plane-based chemical contamination behavior is disabled.
- Plane-based condemnation behavior is disabled.

## Operational Notes

- Build chemical stockpiles before committing to support-company-heavy chemical warfare.
- Use nerve agents for tempo and disruption rather than persistent area denial.
- Track condemnation before running repeated chemical cycles.
- Account for weather because persistence and impact shift by climate conditions.
