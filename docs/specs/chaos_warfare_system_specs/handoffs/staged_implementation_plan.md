# Staged Implementation Plan

Disposition: historical implementation sequence, superseded where incompatible with the [accepted amendment](../specs/13_2026_09_20_accepted_cbrn_overhaul.md) and [requirement ledger](../../../plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md).
Resume only open accepted requirements from that ledger. These stages do not authorize repeating completed work or promoting older unresolved proposals.

Stage 7's public operative-retention claim is specifically superseded by the accepted native-raid-only/removal design and the [consolidation map](../../../plans/chaos_warfare_system_plans/2026-10-08_native_biological_operation_consolidation.md).
The five intelligence attacks and operation-only preparation/phases/capture/refunds retire; shared research, lifecycle, covert history/achievements and zombie profile/outbreak requirements remain.

## Stage 0: Local engine and source verification

Read the required offline wiki pages and current vanilla documentation. Inspect exact 1.19 Army HQ, regimental support, essential equipment, ability, unit-modifier, MIO, raid, aircraft mission, and AI patterns.

Deliverable:

- verified syntax note
- supported and unsupported feature list
- no gameplay edit yet

Keep continuous chemical-air contamination fail-closed unless a verified current-version mission hook exists. The recorded user constraint forbids retaining an estimator or proxy. Inspect the explicit-raid path separately. Lack of the continuous hook does not establish raid support.

## Stage 1: Shared data model and constants

Create or refactor:

- readiness
- policy
- protective coverage
- payload profiles
- contamination classes
- evidence and attribution
- operation record
- shared source labels

Centralize constants and document helpers.

Deliverable:

- helper map
- constants table
- migration plan
- no UI dependency yet

## Stage 2: Gas-mask and protection equipment

Implement:

- gas-mask equipment models
- decontamination equipment
- CBRN instruments
- technologies
- military coverage helper
- filter consumption
- civilian stockpile and distribution model
- country starting reserves

Validate protection against every existing chemical pipeline before adding new delivery.

## Stage 3: Consolidated regimental support and Chaos Battalion

Implement:

- Gas Mask and Decon
- Chemical Recon
- Hazard Pioneer
- Projector Battery
- Ammunition Train
- Armored Delivery
- Medical Countermeasure
- Epidemiology
- Biosecurity Assault
- Nerve Suppression
- redesigned Chaos Assault Battalion

Hide and migrate legacy agent-specific units. Verify essential equipment scaling and template AI.

## Stage 4: Army Headquarters integration

Implement six HQ companies and five or more company-gated abilities using verified 1.19 patterns.

Validate:

- assignment to orders
- equipment status
- command-power scaling
- active duration
- cleanup
- AI use

## Stage 5: Doctrine rework

Replace adoption bonuses, fill four milestones, rework four tracks, add doctrine-only technology visibility, update officer corps, traits, icons, and localisation.

Run doctrine balance audit before delivery expansion.

## Stage 6: Chemical delivery migration

Refactor cylinder abilities, projectors, artillery, armored delivery, chemical tactics, air modules, and raids to call the shared exposure helper.

Implement explicit chemical air operation first. Add continuous mission effects only after the Stage 0 support decision.

## Stage 7: Biological integration

Resume open native biological raid, accident, outbreak, facility, countermeasure and evidence contracts; do not recreate the superseded public operative interface.
Preserve Event 016's shared route and zombie project/profile/outbreak separation through genuine current consumers, with no synthetic native capture callback.

Validate all agent profiles and countermeasure paths.

## Stage 8: Deaths, Air Cleanliness, Condemnation, and diplomacy

Wire one operation record into the shared systems. Implement attribution progression, latent responsibility, treaty and retaliation context, inspections, protective aid, stockpile destruction, and sanction interaction.

Audit double counting.

## Stage 9: Suppression and occupation

Implement Nerve-Agent Camp Methods as the killing-efficiency mastery reward of Gas-Chamber Saturation Drills. The mastery plus any researched nerve agent unlocks the method; runtime use consumes real cylinders and records deaths, contamination, resistance trauma, evidence, attribution, and Condemnation through the established camp action. Retain the superseded selected-state occupation route only as invisible migration code.

## Stage 10: AI and country differentiation

Implement posture, research, production, templates, headquarters, operations, countermeasures, and sanction response. Replace history stockpiles and assign country program profiles.

Run manual scenario matrix for all seven major programs and at least three minor profiles.

## Stage 11: UI, localisation, and assets

Implement the CBRN management surface or a staged decision-category presentation. Wire dynamic values and tooltips. Produce every listed asset through the proper asset subagents or workflows. Do not leave placeholders.

## Stage 12: Achievements and documentation

Implement achievement tracking, icons, docs, mechanics guide, system docs, and relevant catalog rows.

## Stage 13: Audits

Run:

- scripted system architecture review
- decision and mission audit
- localisation audit
- country package audit
- completion audit
- manual improvement-loop closure check

Resolve every accepted finding or disposition it explicitly.

## Stage 14: Balance validation

Test the ten scenarios in the balance spec at weak, normal, and high-chaos settings. Record operation costs, casualties, contamination, cleanup time, Condemnation, sanctions, and AI decisions.

Completion requires no undisclosed simplification, fallback, placeholder, or unsupported surface.
