# Chaos Warfare Expansion Planning Package

## Purpose

This package redesigns Chaos Warfare as a complete chemical, biological, radiological, and contamination command system for Chaos Redux. It is a planning and implementation handoff. It does not contain gameplay code.

The design integrates the existing Chaos Redux chemical warfare, biological warfare, Air Cleanliness, Deaths, Condemnation, outbreak, genocide-discovery, special project, doctrine, aircraft designer, unit template, decision, and AI systems with the Hearts of Iron IV 1.19 Army Headquarters and regimental support model.

## Package map

### Specifications

1. `specs/01_core_system_and_gameplay_loop.md`
2. `specs/02_doctrine_architecture.md`
3. `specs/03_hq_command_and_regimental_support.md`
4. `specs/04_equipment_tech_and_subunits.md`
5. `specs/05_chemical_delivery_and_battlefield_effects.md`
6. `specs/06_biological_warfare_and_outbreaks.md`
7. `specs/07_gas_masks_civil_defence_and_population_protection.md`
8. `specs/08_suppression_occupation_and_nerve_agents.md`
9. `specs/09_condemnation_deaths_air_cleanliness_and_diplomacy.md`
10. `specs/10_ai_country_programs_and_designers.md`
11. `specs/11_balance_tuning_and_consistency_rework.md`
12. `specs/12_ui_localisation_assets_achievements.md`

### Matrices

The `matrices/` folder contains implementation-oriented content maps for doctrine, technologies, headquarters support, regimental support, subunits, equipment, agents, countermeasures, country starting packages, AI, and balance.

### Research

The `research/` folder records the existing-system audit, current vanilla mechanics, historical gas-mask and program anchors, and source notes. Historical quantities are converted into gameplay bands rather than copied literally.

### Prompts

The `prompts/` folder contains bounded handoffs for assets, achievements, decisions and missions, coding, and the final goal. The goal prompt is intentionally kept within the planning skill's required length band.

### Handoffs

The `handoffs/` folder maps implementation surfaces, staged work, a manual improvement-loop pass, a completion audit, and limitations.

## Core design outcome

Chaos Warfare becomes a high-power doctrine with real logistics and counterplay. Its strongest effects require protective equipment, payloads, specialist units, headquarters support, favorable conditions, and command preparation. Chemical and biological use can win battles and destroy regions, but it also causes casualties, contamination, outbreak risk, equipment exhaustion, friendly exposure, public evidence, Condemnation, sanctions, and retaliatory escalation.

The doctrine no longer grants broad, stacked attack bonuses as its main identity. It changes what the player can build, assign, prepare, deliver, defend against, conceal, clean up, and politically survive.

## Source-reading statement

Every project file supplied with this task was read in full, including the skill markdown files, subagent TOML files, three catalog CSV files, the mechanics guide, AGENTS.md, and every markdown file in `biological_warfare.zip`.

The entire live GitHub repository, the user's local offline Paradox wiki snapshot, and the user's local Hearts of Iron IV installation were not available as a complete mounted filesystem. Targeted current repository files were inspected through the GitHub connector. Current vanilla 1.19 behavior was checked through official Hearts of Iron IV announcements and patch notes. This limitation is carried into the implementation handoff and must be closed by the implementation agent before changing engine-facing files.

Project custom subagents were provided as definitions but no subagent-spawn tool was available in this environment. Their standards were applied manually. A manual improvement-loop pass and completion audit are included. No claim is made that the actual custom agents ran.
