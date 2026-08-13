# Chaos Warfare Decision and Mission Implementation Prompt

## Task

Implement the decision, mission, and optional scripted-GUI layer for the accepted CBRN rework. Read `chaos-redux-decisions-missions`, the full spec pack, current chemical and biological decisions, current scripted GUI patterns, and verified vanilla 1.19 examples. Use dynamic costs, named targets, AI behavior, cleanup, and custom tooltips. Do not create a political-power store.

## Categories

### CBRN Program Management

Lifecycle: visible after protective or offensive program establishment. It closes only if the program is fully dismantled and no contamination, outbreak, or sanction response remains.

Actions:

- establish national respirator reserve
- designate CBRN command
- select use policy
- choose shell-filling profile
- establish air payload program
- expand or reduce stockpiles
- improve laboratory safety
- relocate vulnerable stockpiles
- destroy or surrender offensive stock
- accept or reject inspection
- declare retaliation policy
- pursue autarky, compliance, or sanctioned procurement

Costs use factories, equipment, XP, time, stability, trade, and program risk. Policy changes require real institutions and cooldowns.

### Civil Defence and Protective Distribution

Target management: selected state flow or dynamic state list with clutter control.

Actions:

- register and fit population
- issue masks to priority state
- full state distribution
- emergency distribution during alert
- replace filters and damaged masks
- protect hospitals and utilities
- move civilians into shelters
- collect and recondition old masks
- supply occupied population
- export protective equipment

Costs scale from state population, infrastructure, urban status, occupation, active combat, and civil-defence efficiency. AI must prioritize frontline armies and high-value civilian states.

### Chemical Operations

Only show operations supported by doctrine, technology, headquarters, payload, policy, target, and cooldown.

Actions and missions:

- prepare order for chemical offensive
- reserve payload and shell lots
- choking barrage
- persistent blister barrage
- nerve shock barrage
- incapacitating barrage
- armored local delivery
- chemical air interdiction
- strategic chemical raid
- decontamination corridor
- cancel or abort operation

Preparation uses timed missions. Completion rechecks order, target, payload, weather, aircraft or artillery, protection, and national policy. Failure, partial success, success, friendly blowback, and abort all need distinct effects.

### Biological Operations and Containment

Offensive actions:

- prepare strategic biological raid
- launch operative outbreak operation
- seed battlefield contamination where supported
- sabotage selected infrastructure through biological release

Defensive actions:

- activate surveillance
- investigate suspected outbreak
- quarantine selected state
- deploy field hospitals
- distribute antibiotics
- launch vaccination campaign
- close border or transport corridor
- request international medical mission
- secure captured laboratory
- safely destroy captured payload

Outbreak missions use incubation, detection, spread, containment, and partial outcomes. AI must avoid operations likely to spread into its own territory.

### Occupation CBRN Measures

Visible only with relevant occupied states.

Actions:

- adopt Protected Occupation Administration
- authorize nerve suppression in selected state
- deploy protective aid to occupied civilians
- seal contaminated district
- preserve or destroy records
- permit inspection or medical mission

Nerve suppression has state cooldown, payload and protection cost, immediate suppression, delayed trauma, deaths, evidence, and Condemnation. It is not a passive store purchase.

## Mission design

### Establishment mission

Duration: 90 to 180 days.

Objectives:

- produce minimum mask reserve
- field one qualifying CBRN HQ
- train one protected formation
- maintain support-equipment and decontamination reserve

Success raises readiness. Failure leaves the doctrine active but offensive actions blocked until repaired.

### Operation preparation mission

Duration varies by method from 7 to 45 days.

Auto-completes when preparation and target remain valid. Failure occurs on target loss, headquarters invalidation, stockpile shortfall, aircraft or artillery loss, policy change, or world-end conflict.

### Cleanup mission

Target state, duration based on severity. Requires decon equipment, trucks, fuel, masks, and controlled access. Partial success lowers class but may not fully clear the state.

### Outbreak containment mission

Duration 90 to 365 days by intensity. Success requires maintaining quarantine, medical capacity, supply, and spread limit. Partial success contains spread but leaves local outbreak. Failure creates new states or higher intensity.

## Dynamic cost principles

- command power never exceeds the project ceiling and scales with affected force
- population distribution uses mask crates, administration, and time
- chemical operations use payload, shell or air lots, masks, supply, command power, and preparation
- quarantine uses equipment, manpower, output, stability, and movement
- medical response uses support equipment, trucks, and medical capacity
- inspections cost secrecy and can expose programs
- stockpile destruction consumes time and removes real equipment

## UI and tooltips

Show:

- selected order or state
- exact available and required stock
- protection and payload ratio
- forecast confidence band
- expected contamination class
- expected death and Condemnation band, not false exact values
- cooldown and abort conditions
- current evidence and attribution

Use custom trigger tooltips. Do not expose long raw triggers.

## AI

Every decision family needs `ai_will_do`, valid target selection, policy checks, route checks, stockpile checks, equipment checks, and refusal rules from the AI matrix.

## Cleanup

Clear selected state, selected order, operation payload reservation, temporary event targets, preparation flags, invalid decision targets, stale missions, expired evidence flags, and dead-country sanction interactions.

## Audit

After implementation, run the decision and mission auditor. Resolve cost clarity, duplicate missions, passive checklist objectives, AI validity, cleanup, exploit, and route integration findings before completion.
