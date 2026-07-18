# Event 019 Release Modes and First-Family Reception Handoff

Date: 2026-07-16

Owner: `event19_exact_transfer`

Status: implementation complete; ready for parent integration review and fresh
Event 019 specialist audit. This is not a full Event 019 closure finding.

Source addendum:
`docs/plans/019_infantry_spawn_plans/019_near_completion_improvement_addendum_2026_07_16.md`

## Implemented result

### Natural release modes

| Frozen mode | Required identity | Exact transferred set | Actor result | Proved pre-commit failure |
| --- | --- | --- | --- | --- |
| ordinary claimant | Evolution III and the selected male claimant; no Evolution IV, registry row, family, or provider dependency | active recorded rows loyal to the selected claimant inside the connected claimant-headquarters/origin region | dynamic human claimant breakaway | existing visible failed coup |
| anomalous claimant | Evolution IV, selected claimant, and a complete eligible derivative-capable provider row | exact union of the selected family rows and claimant-loyal rows in the frozen region | dynamic nonhuman provider actor led by the copied claimant | existing visible failed coup |
| claimant-independent family | Evolution IV, complete eligible provider row, sufficient claimant-free family presence and pressure, and weak central control | only exact rows of the selected family whose claimant UID is invalid | dynamic provider actor; an exactly proved one-state whole-army case converts the same tag | visible deferred-containment event `chaosx.nr19.206` |

All multi-state modes use the existing approved recreate, prove, delete
transaction. The release mode and monotonic nonce are copied to and proved on
the provisional actor. Mode-aware proof no longer assumes that every actor has
both a family and a claimant. Source/global accounting still commits only after
replacement proof and exact source deletion. Existing recovery and post-commit
quarantine behavior remains authoritative.

The one-state family takeover proves all of the following before provider setup:

- exactly one controlled state;
- no active claimant rows;
- every live national division is one exact, live, claimant-free row of the
  selected family;
- exact UID, cohort, generation, lot, template, origin, scope, and ledger
  alignment;
- unchanged private row counts and live division count after provider setup.

It then removes former-parent war surfaces and never creates a zero-state actor
or declares war on itself.

### First-family reception

A country whose first Event 19 manifestation applies already-active Evolution IV
now receives one country-local reception incident:

1. The generic family registry is iterated only on that country's entry or
   country pulse.
2. The strongest currently eligible complete row is frozen as registry index,
   family ID, provider ID, visual profile, and monotonic incident nonce.
3. `chaosx.nr19.105` is queued once after the Event 19 context is installed.
4. The visible event offers guarded cantonment, a negotiated compact, and
   refusal to player and AI alike.
5. Either acceptance invokes the existing provider materialization snapshot,
   spawn, exact proof, and rollback transaction. It creates exactly one
   registered package without provider payment, request overhead, cooldown, or
   request-count consumption.
6. Refusal creates no family formation. All three resolved outcomes receive
   distinct centralized balance effects and history payloads.
7. If no row is eligible, the pending state remains and retries only on that
   country's existing Event 19 pulse.
8. Active Evolution IV transitions, derivative countries, scenario actors,
   scenario transactions, management locks, and derivative creation locks do
   not dispatch the natural reception.

The frozen row loader deliberately does not reevaluate provider eligibility.
Later eligibility changes cannot replace the promised provider. A changed or
misaligned registry identity produces the visible failed-reception history. A
failed rollback quarantines the country and marks the ledger invariant failure
instead of granting a partial package.

### Future-family invariant

`GetInfantrySpawnSelectedFamilyName` and
`GetInfantrySpawnFirstFamilyReceptionPicture` are display-only readers. Neither
is part of reception eligibility or provider materialization. A future family
registered from its own external integration surface remains mechanically
selectable with an unmapped positive family/visual profile:

- the unconditional name path uses `infantry_spawn_family_name_unrecorded`;
- the unconditional picture path uses the identity-neutral army scene
  `GFX_portrait_infantry_spawn_unassigned_muster`;
- the provider's callback ID still controls its real template, spawn,
  sustainment, cleanup, and derivative behavior.

The sole Event 19 registry file's header and the current specifications now say
that a future provider defines its registration and callbacks in its own
integration surface and calls registration from its parent startup path. No
future provider needs an Event 19 family list, name map, picture map, or registry
file edit.

The generic name and art results are an explicitly required display
compatibility fallback. They are not a gameplay substitute: no ordinary unit,
fixed tag, hardcoded family dispatch, or fabricated claimant is used.

## AI, isolation, and cadence

- Player and AI resolve the same visible `.105` options and the same exact
  provider transaction.
- Reception AI weights use containment strength, war state, manpower need,
  saturation pressure, affordability, and the already-proved provider
  compatibility row.
- Claimant resolution runs before independent-family breach resolution, and a
  country can attempt at most one natural recorded-formation transfer on one
  country pulse.
- A failed independent breach receives a 30-day constant-backed defer flag,
  control loss, saturation pressure, and `.206`, preventing same-tick repeats.
- SCN-013 continues to use its direct scenario path. None of the natural
  Evolution, claimant, pressure, or cooldown gates were added to the scenario
  transaction.
- No daily, weekly, monthly, or other all-country recurring scan was added.

## Gameplay and data files changed

- `common/script_constants/019_infantry_spawn_derivative_package_constants.txt`
  - release mode, reception choice/outcome, nonce/delay, AI, and deferred-family
    constants
- `common/script_constants/019_infantry_spawn_constants.txt`
  - history payload IDs 15 through 18
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
  - reception provider completeness; common, claimant, family, weak-control, and
    mode-aware natural-release gates
- `common/scripted_effects/019_infantry_spawn_pressure_effects.txt`
  - mode-aware provider selection and claimant-free family presence
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
  - ordinary claimant evidence; mode-aware exact transaction; three-way actor
    identity/proof; visible failure routing; one-state family proof/takeover;
    transaction and reception cleanup
- `common/scripted_effects/019_infantry_spawn_pulse_effects.txt`
  - reception retry, claimant-first/family-second release order, one-attempt
    pulse latch
- `common/scripted_effects/019_infantry_spawn_core_effects.txt`
  - four reception history helpers
- `common/scripted_effects/019_infantry_spawn_evolution_effects.txt`
  - pre-fire row freeze, dispatch, exact materialization, rollback, outcomes,
    one-time finalization
- `common/scripted_effects/019_infantry_spawn_management_effects.txt`
  - ordinary final-cleanup coverage for all added country flags and variables
- `common/scripted_effects/019_infantry_spawn_scenario_effects.txt`
  - scenario actors cannot consume the pending natural reception
- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`
  - header contract corrected; no provider row or registry was added
- `events/019_infantry_spawn.txt`
  - visible events `chaosx.nr19.105` and `chaosx.nr19.206`
- `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`
  - frozen host-scene selection and explicit registry-default displays for
    future providers without bespoke Event 19 mappings
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
  - title and description mappings for all four reception histories
- `localisation/english/019_infrantry_spawn_l_english.yml`
  - event, tooltip, history, and Event Details text

## Specifications and documentation changed

- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_4_evolution_iii.md`
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_5_evolution_iv.md`
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_6_derivative_countries.md`
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_8_scenario_interactions_acceptance.md`
- `docs/events/019_infantry_spawn.md`

No workbook, generated catalog, asset, sprite definition, or asset manifest was
changed by this tranche.

## Validation evidence

- All touched Clausewitz/localisation files have balanced braces.
- No touched file contains the unsupported `<=` or `>=` operators.
- Event 19 English localisation remains UTF-8 with BOM.
- `chaosx.nr19.105` and `chaosx.nr19.206` each have one event definition.
- Every newly introduced scripted effect and trigger has one definition.
- Each reception history has one payload constant, one recorder helper, one
  title mapping, one description mapping, and one title/description
  localisation pair (eight event-log mappings total).
- Each bespoke reception picture target and the generic Evolution IV picture
  target resolve to an existing sprite. The generic family-name localisation
  key also exists once.
- No reception trigger or materialization helper depends on either display
  scripted-localisation function.
- `git diff --check` returned exit code 0 for the touched tracked files.

The required HOI4 MCP lint was attempted independently for `.105` and `.206`.
Both calls stopped before scanning with `ARTIFACT_STORAGE_LIMIT`; the tool
reported no source diagnostics because no files were scanned. This is a tooling
blocker for MCP evidence, not a lint pass and not a reason to weaken the source.

## Simplifications, omissions, and blockers

No gameplay simplification, fixed-tag substitute, ordinary-unit substitute, or
new registry was introduced. Existing owner-approved exact-transfer engine
limitations remain unchanged: current equipment inventory/variants, exact
current manpower fill, organization, post-creation veterancy and experience,
medals, officer history, army assignment, battle plans, and orders cannot be
preserved exactly by the recreate/prove/delete substitute.

This subagent did not update the Event 19 workbook or generated CSV exports and
did not claim full Event 19 completion. A fresh parent/specialist integration
audit remains necessary, including the wider SCN-013, achievement, decision,
asset, and catalog closure surfaces owned by other tranches. The only validation
tool blocker in this tranche is the HOI4 MCP artifact-storage limit described
above.

## Skills used

- `chaos-redux-events`
- `chaos-redux-improvement-loop`

No project skill was created or modified. This tranche did not reveal a reusable
workflow gap beyond the existing registry, event, and improvement-loop guidance.
