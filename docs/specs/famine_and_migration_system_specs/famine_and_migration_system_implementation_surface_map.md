# Famine and Migration Mechanics Implementation Surface Map

This is a repository exploration guide. The implementation agent must verify exact paths and identifiers locally before editing.

## Likely shared script surfaces

- shared script constants for thresholds, pressure bands, AI tuning, durations, capacity, and cooldowns
- shared scripted effects for famine requests, flight requests, exact transfers, route resolution, reception, return, integration, and cleanup
- shared scripted triggers for state eligibility, route safety, island blockade proof, destination safety, origin safety, cohort validity, border policy, and special-country exclusion
- dynamic state modifiers for famine and displacement states
- shared decisions and categories for active management
- accounting/presentation seams and report context without an incident-event layer
- scoped on-action adapters
- AI strategies, decision weights, and complete weighted pools
- scripted localisation for dynamic state, route, cause, capacity, policy, and cost text

## Existing systems that require direct inspection

- Chaos Meter Deaths effects, reasons, arrays, logs, filters, and GUI
- Air Cleanliness value, threshold flags, recovery, winter, and UI
- Condemnation source registration and hidden-evidence flow
- camps, genocide, gulags, forced labor, deportation, and site discovery
- occupation laws and occupation-law change hooks
- strategic bombing state aftermath
- nuclear and thermonuclear state aftermath
- outbreak exposure, spread, quarantine, and medical countermeasures
- natural-disaster call and aftermath jobs
- event and cluster pacing boundaries
- special Chaos and actual nonhuman classifiers
- exact state population loss helper and manpower reconciliation

## New public contracts to document if implemented

- request state food-security pressure
- request state flight pressure
- transfer exact state civilian population
- resolve civilian movement route
- register famine deaths
- register occupation-repression deaths
- register forced-labor deaths
- register forced-displacement deaths
- refresh reception capacity
- evaluate voluntary return
- integrate displaced cohort
- resettle displaced cohort
- clear invalid movement cohort

Every public reusable effect or trigger must be documented with purpose, scope, inputs, outputs, defaults, side effects, and an example.

## Event-owned adapters

Event-owned source files should call the public contracts after they resolve exact actors, states, causes, and severity.

Do not put shared population-transfer logic into event files.

## Localisation and UI surfaces

- system report and accounting/presentation localisation
- state modifier localisation
- decision and mission localisation
- dynamic cause breakdowns
- Deaths reason and detail localisation
- Condemnation source localisation
- achievement localisation
- category icon, category picture, state-modifier icons, decision icons, achievement triplets, and report images

## Permanent documentation

Create separate permanent famine and migration documents plus a neutral civilian-transfer contract document under `docs/systems/`, and update every owning system or event document that gains an adapter.

Update the authoritative workbook only after final implementation and localisation are known.
