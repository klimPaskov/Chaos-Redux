# Implementation Tranche Plan

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Tranche 0: repository proof and source cleanup

### Goal

Establish verified engine behavior and a clean implementation baseline before gameplay expansion.

### Required work

1. Check out the repository in a writable local workspace and record the starting commit.
2. Read every local offline wiki page and official documentation file required for the touched systems.
3. Inspect the selected and deselected mapmode strip DDS files and reconcile frame count, dimensions, and slot ownership.
4. Confirm the exact effect and scope needed to thermonuclear-strike every valid province.
5. Scan the complete live scenario registry, record every assigned id, and reserve the next integer after the highest assigned id for Fallout.
6. Build a tag conflict ledger from vanilla, releasables, Chaos Redux base tags, dynamic tags, and other feature packages.
7. Confirm a full-screen scripted GUI parent, drawing order, and input-blocking pattern from vanilla.
8. Search for every Fallout event definition, caller, namespace, asset path, super-event slot, and audio wrapper. Record all stale ownership before deletion.
9. Write `docs/plans/air_cleanliness_fallout_plans/source_of_truth_map.md` in the repository.
10. Mark stale Air and Fallout docs as pending reconciliation or update them to describe current behavior before the first gameplay commit.

### Exit gate

Tranche 0 is complete only when the province sweep, mapmode slot, scenario id, and full-screen GUI patterns are documented with exact local evidence.

## Tranche 1: state phase model and winter mapmode

### Goal

Make winter a persistent state system that can be seen and understood before any new population or building damage is added.

### Required work

1. Add dedicated Air Winter constants.
2. Add state variables and initialization helpers.
3. Add target phase, escalation, recovery, and hysteresis logic.
4. Integrate one state update into the existing monthly Air pass.
5. Aggregate global phase counts and exposed population.
6. Add one dynamic modifier per visible phase.
7. Add the dedicated winter mapmode.
8. Add ordered scripted tooltip data.
9. Add mapmode assets after slot verification.
10. Add debug-only inspection helpers for state phase, pressure, and target phase.
11. Update Air and mapmode documentation.

### Scope boundary

Do not add Fallout world rewrite logic in this tranche. Do not add the manual scenario. Do not add successor countries.

### Exit gate

A test save can move selected states through all seven phase values, recover them through hysteresis, display them correctly in the mapmode, and preserve the state across save-load.

### Audit

Run `chaosx_scripted_system_architect` in audit or narrow patch mode for the new constants, state lifecycle, duplicated logic, and cleanup.

## Tranche 2: real winter consequences, incidents, treaty, and AI

### Goal

Turn phase visibility into a complete playable Air Winter system.

### Required work

1. Register winter population loss through the shared Deaths pipeline.
2. Implement bounded building damage.
3. Gate state-category degradation behind sustained severe exposure.
4. Add food reserve, shelter, monitoring, adaptation, and relief values.
5. Add staged state-target response decisions and missions.
6. Add flavour incident families with real effects.
7. Add recovery incidents and reconstruction actions.
8. Restore and modernize the treaty layer.
9. Add route-aware AI behavior.
10. Add event-log, death-log, and Chaos history integration.
11. Update docs and visible UI summaries.

### Exit gate

A severe winter campaign produces different state outcomes based on shelter, food, supply, industry, treaty support, and player decisions. Population, buildings, supply, and categories change through one coherent system.

### Audits

- `chaosx_decision_mission_auditor`
- `chaosx_localisation_auditor` after final visible strings exist
- `chaosx_documentation_curator`

## Tranche 3: Fallout request coordinator and blackout transition

### Goal

Create the reusable transition framework without yet performing the complete country rewrite.

### Required work

1. Add Fallout request constants and source enum.
2. Add idempotent request, validate, start, and abort helpers.
3. Create `events/fallout_world_end_events.txt` with `add_namespace = chaosx.fallout`.
4. Move every Fallout entry, blackout, rewrite, manual scenario, recovery, and aftermath event into that file.
5. Delete the old Fallout block from `events/chemical_warfare_events.txt` and migrate callers directly.
6. Add normal contamination and direct scripted callers through `fallout_request_aftermath`.
6. Capture the pre-transition snapshot.
7. Set terminal locks in the correct order.
8. Add full-screen blackout GUI and GFX.
9. Add a persistent transition-phase variable and dirty variable.
10. Add timed text-beat sequencing.
11. Add a processing phase with placeholder no-op batch helpers for later state and country work.
12. Add a safe abort path for pre-rewrite failures.

### Exit gate

Each allowed caller can request Fallout once. The screen becomes black, progresses through timed beats, blocks dismissal, preserves state across save-load, and exits through a controlled test finish without setting a normal super-event.

### Audit

Run `chaosx_scripted_system_architect` before world rewrite implementation.

## Tranche 4: state grading and world rewrite foundation

### Goal

Transform the old world into a stable post-Fallout map with deterministic state grades and valid surviving actors.

### Required work

1. Calculate and store state grade and survival value.
2. Apply one-time state population, building, resource, supply, and category consequences.
3. Mark wasteland and terminal zones.
4. Capture and clear incompatible old-world diplomacy.
5. Calculate country survival and fragmentation scores.
6. Preserve valid old governments where the design allows.
7. Select successor candidates from the approved matrix and tag ledger.
8. Reserve player continuation states and candidates.
9. Transfer states in deterministic regional batches.
10. Apply minimal valid country packages and generic Fallout framework content for internal testing only.
11. Validate every state owner, capital, controller, and player scope.
12. Finish the blackout only after map validation succeeds.

### Internal testing rule

Temporary internal tests may use flat debug rectangles and debug localisation in an explicitly unshipped development branch. They must not borrow another feature's assets and cannot be presented as completed Fallout content.

### Exit gate

The rewrite can complete from several world states without orphan states, invalid players, duplicate ownership, missing capitals, dead-country references, or active old-world wars.

### Audits

- `chaosx_country_package_auditor` on the rewrite foundation
- `chaosx_event_completion_auditor` for the transition surface only

## Tranche 5: manual Fallout scenario

### Goal

Add the manual scenario exactly as specified after the engine proof exists.

### Required work

1. Allocate Fallout to the next integer after the highest id in the live scenario registry. Preserve every existing scenario id.
2. Register Fallout in every scenario registry and sort path.
3. Add launch gate, confirmation, type, and intensity behavior.
4. Add exact thermonuclear strike sweep over every valid province.
5. Suppress per-strike global spam while preserving real state effects.
6. Record one aggregate synthetic-strike entry.
7. Start a persistent seven-day countdown.
8. Request Fallout on day seven.
9. Ensure the normal blackout and rewrite path is used.
10. Add documentation and catalog alignment using the allocated scenario id.

### Exit gate

Manual launch from a clean campaign strikes every valid province, survives save-load during the seven-day interval, then enters the same blackout and rewrite system as every other caller.

### Audit

Run `chaosx_decision_mission_auditor` for scenario UI and lifecycle, followed by the completion auditor for this scenario tranche.

## Tranche 6: first successor and focus proof batch

### Goal

Prove the country package and focus composition architecture before large-scale production.

### Batch size

Twelve selected successors, one for each archetype, spread across several regions. Final candidates are chosen only after the tag and state ledgers are complete.

### Required work per country

- valid source tag or creation route
- exact state package
- capital and fallback capital
- cosmetic identity
- leader or institutional body
- starting ideas with lifecycles
- starting forces and reinforcement path
- archetype mechanic
- regional overlay content
- country memory branch
- focus tree and decisions
- route-aware AI
- localisation
- complete visible assets
- documentation and matrix status

### Focus proof

Implement both of these as prototypes if needed:

- verified shared-focus composition
- compiled full-tree composition

Choose the safer architecture based on real engine behavior and audit results.

### Exit gate

All twelve countries are playable for several years, have distinct identities, do not share generic text or identical rewards, and pass country and focus audits.

## Tranche 7: regional successor expansion

### Goal

Scale the proven package in manageable regional waves.

Recommended order:

1. North America
2. Europe
3. Soviet and Eurasian interior
4. East Asia
5. South Asia
6. Middle East and North Africa
7. Sub-Saharan Africa
8. Latin America and the Caribbean
9. Oceania and remote islands

Each wave begins with state and tag assignment review and ends with audits. Do not start the next wave while the previous wave has unresolved blocking defects.

## Tranche 8: ten-year content depth

### Goal

Ensure the scenario remains playable and reactive for a full post-Fallout decade.

Required systems:

- seasonal survival cycles
- food and shelter development
- salvage and expedition systems
- refugee and population movement
- regional diplomacy and recognition
- successor wars and negotiated borders
- faction and coalition systems
- reconstruction and state restoration
- technological regression and recovery
- route-specific late-game projects
- mutant fiction routes
- old-world memory events
- second-generation political conflicts
- achievements and rare outcomes

Content should unlock over time through focus routes, decisions, missions, state control, and world conditions. It should not all appear at transition finish.

## Tranche 9: final assets, documentation, spreadsheet, and completion audits

### Required work

1. Complete all missing assets and manifests.
2. Finalize localisation and scripted localisation.
3. Update canonical system and event documentation.
4. Update scenario and event catalog spreadsheets through the spreadsheet worker.
5. Run country, focus, decision, localisation, documentation, scripted-system, and completion audits.
6. Resolve every accepted plan disposition.
7. Run the full validation matrix.
8. Produce a completion report that lists every simplification, omission, blocker, or approved deviation.

### Completion gate

The goal remains incomplete while any active successor has generic focus content, missing AI, missing assets, invalid state setup, stale docs, unresolved accepted design, or an unproven manual province sweep.
