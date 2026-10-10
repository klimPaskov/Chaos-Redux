# Chaos Warfare Expansion Planning Package

## Purpose

This package redesigns Chaos Warfare as a complete chemical, biological, radiological, and contamination command system for Chaos Redux. It is a planning and implementation handoff. It does not contain gameplay code.

The design integrates the existing Chaos Redux chemical warfare, biological warfare, Air Cleanliness, Deaths, Condemnation, outbreak, genocide-discovery, special project, doctrine, aircraft designer, unit template, decision, and AI systems with the Hearts of Iron IV 1.19 Army Headquarters and regimental support model.

## Package map

The user's explicit 2026-09-20 implementation request is recorded in [`specs/13_2026_09_20_accepted_cbrn_overhaul.md`](specs/13_2026_09_20_accepted_cbrn_overhaul.md). That accepted amendment takes precedence over conflicting older proposals, and its [requirement ledger](../../plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md) keeps implementation evidence separate from design acceptance.

Older numbered specifications and matrices remain design context unless a requirement has recorded acceptance in the amendment or owner ledger.
The original validation report, manual review and source-reading ledger are historical package receipts, while the staged plan is subordinate to the current requirement ledger.
The `corrections/` folder preserves dated user decisions, parent-selected corrections and their evidence limits. Check the matching owner handoff before replaying an older instruction.
Current repository workflows belong to `AGENTS.md` and the owner skills, rather than the imported source-reading receipts.

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
13. `specs/13_2026_09_20_accepted_cbrn_overhaul.md`

### Matrices

The `matrices/` folder contains implementation-oriented content maps for doctrine, technologies, headquarters support, regimental support, subunits, equipment, agents, countermeasures, country starting packages, AI, and balance.

### Research

The `research/` folder records the existing-system audit, current vanilla mechanics, historical gas-mask and program anchors, and source notes. Historical quantities are converted into gameplay bands rather than copied literally.

### Prompts

The `prompts/` folder contains bounded handoffs for assets, achievements, decisions and missions, coding, and the final goal. The compact goal prompt points to the detailed coding brief and current acceptance ledger.

### Handoffs

The `handoffs/` folder maps implementation surfaces, staged work, a manual improvement-loop pass, a completion audit, and limitations.

## Core design outcome

Chaos Warfare becomes a high-power doctrine with real logistics and counterplay. Its strongest effects require protective equipment, payloads, specialist units, headquarters support, favorable conditions, and command preparation. Chemical and biological use can win battles and destroy regions, but it also causes casualties, contamination, outbreak risk, equipment exhaustion, friendly exposure, public evidence, Condemnation, sanctions, and retaliatory escalation.

The doctrine no longer grants broad, stacked attack bonuses as its main identity. It changes what the player can build, assign, prepare, deliver, defend against, conceal, clean up, and politically survive.

## Status and evidence

Chaos Warfare is implemented; current behaviour lives in [`docs/systems/cbrn_warfare/`](../../systems/cbrn_warfare/README.md) and the condemnation layer in [`condemnation_sanctions.md`](../../systems/cbrn_warfare/condemnation/condemnation_sanctions.md).
Design authority is the accepted amendment in [`specs/13_2026_09_20_accepted_cbrn_overhaul.md`](specs/13_2026_09_20_accepted_cbrn_overhaul.md); the [requirement ledger](../../plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md) and the [6 October takeover status](../../plans/chaos_warfare_system_plans/takeover_status_2026-10-06.md) hold accepted requirements and unresolved implementation evidence.
The original package's source-reading statements, validation report and manifest describe the 2026-09 planning environment, not this checkout; they are provenance, and the implementation gates they raised are tracked in the takeover record instead.

## Revision log

### 2026-10-10 spec audit

- Replaced the 2026-09 planning source-reading, subagent-availability and post-takeover evidence paragraphs with one status section that names the implemented system documents, the design authority and the ledgers that track unresolved evidence.
- Prompts now use the repository's self-contained-prompt rule instead of Codex spawning syntax, and skill links point at the tracked `.claude/skills/` location.
- Checked the condemnation tier table and the humanitarian carve-out owner link against the reworked condemnation spec: both still match.
