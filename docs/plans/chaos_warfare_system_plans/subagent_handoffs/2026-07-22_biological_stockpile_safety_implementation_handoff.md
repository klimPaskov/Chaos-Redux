# Biological Stockpile Safety Implementation Handoff

## Scope

This tranche implements exact national-arsenal designation, live four-agent
stockpile risk, targeted ordinary-accident checks, exact payload loss, stable
legacy accident notifications, and shared biological-lifecycle entry. It does
not implement a biological delivery decision. Deliberate battlefield and
strategic use remain native raids; operative release remains an intelligence
operation.

## Implemented surfaces

- `common/script_constants/biological_stockpile_safety_constants.txt`
  centralizes risk bands, agent risk weights, thresholds, monthly incident
  weights, severity tables, stock-loss fractions, designation cost, cooldown,
  and AI weights.
- `common/scripted_triggers/biological_stockpile_safety_triggers.txt` validates
  the exact arsenal pointer, operational designation candidates, live snapshot
  contracts, matrix bands, agent selection, severity selection, and ordinary
  fail-safe immunity.
- `common/scripted_effects/biological_stockpile_safety_effects.txt` reads exact
  stockpiles and facility condition, assigns a matrix band, synchronizes the
  visible risk spirit, selects and debits one matching agent, records evidence
  and history, enters `bio_lifecycle_dispatch_seed`, and owns exact cleanup.
- `events/biological_stockpile_safety_events.txt` runs one delayed monitor only
  for the country with a recorded arsenal. Invalid control or facility state
  suspends the roll while re-arming the same exact pointer; it never searches
  for a replacement.
- `common/decisions/biological_stockpile_safety_decisions.txt` provides one
  storage-management decision for exact arsenal designation or relocation. It
  has no victim scope, release effect, delivery route, or agent deployment.
- `common/special_projects/projects/biowarfare_main_projects.txt` records the
  first exact facility state exposed by each of the four agent project outputs.
- `events/biowarfare_events.txt` retains ids `chaosx_bioweapon.4`, `.9`, `.102`,
  and `.203` as notification-only events. Their old MTTH rolls, random-state
  selection, duplicate payload debit, and direct legacy contamination were
  removed.
- Four visible risk spirits, scripted severity text, final localisation, five
  registered sprites, five independently produced DDS assets, asset manifests,
  contact sheet, and player/system documentation are wired with the mechanic.

## Accounting and invariants

- Each accident selects from exact live agent stock counts and executes one of
  four mutually exclusive matching-equipment debit branches.
- A contained incident records stock loss, severity, evidence, exact state,
  date, and history but creates no outbreak seed.
- Every non-contained incident supplies exact domestic actor/victim scopes,
  route `laboratory_accident`, source/result `accident`, debit proof, payload
  consumed, intensity, exposed share, evidence, Condemnation, and forced
  detection to the ordinary lifecycle.
- One pending-notification flag prevents a later monitor tick from overwriting
  an unresolved accident record.
- Doctrine multipliers remain user-approved escalation: Theater Contamination
  uses 1.10 and Terminal Hazard uses 1.20 for medical saturation, so neither
  reduces or erases medical consequences. Evidence and attribution are not
  doctrine-modified; only Terminal Hazard Condemnation is below 1.00.
- No all-country periodic on-action, production estimator, inferred facility,
  random replacement state, infrastructure-as-damage proxy, delivery decision,
  or zombie state is present.

## Audit disposition

The decision/mission specialist completed a read-only audit.

- Exact-state monitoring failed to resume after recapture: **fixed** by
  re-arming the same targeted delayed event while the exact pointer is invalid.
- Notification fields could theoretically collide: **fixed** with the pending
  notification guard and acknowledgement cleanup.
- Doctrine medical effects were reported as prohibited: **rejected as a design
  conflict**. The accepted user correction explicitly makes doctrine increase
  deaths, contamination, and operational effects while reducing only political
  consequences. The audited multipliers are 1.10 and 1.20, never reductions.
- Eleven special-project prototype rewards still used placeholder art:
  **accepted audit finding, queued in the active asset workflow**. This finding
  must be closed before Stage 7 completion.

The localisation and event-completion specialist prompts were rejected by the
biology safety filter. Their audits are unavailable and are not counted as
passes. Parent review checked localisation key coverage, scripted severity
resolution, BOM encoding, exact event ids, notification options, helper
resolution, and sprite paths. A narrow HOI4 Event Chain Viewer lint returned a
partial global report with `validation.passed = false`; it is recorded as
unavailable evidence, not a passing validation.

## Meaningful validation

- All 47 scripted helper calls in the bounded surface resolve to definitions.
- Exactly four project `facility_state_effects` blocks initialize exact arsenal
  state, one for each ordinary agent project.
- The private monitor is scheduled only from exact project output,
  exact-selection management, or its own country-specific continuation.
- The old four notification ids contain no MTTH, random target, equipment debit,
  or direct contamination path.
- Final DDS inspection and the source contact sheet confirm four distinct 60x68
  risk-spirit icons and one independent 32x32 decision icon. Existing
  `gfx/interface/military_raids/` assets are unchanged.

## Remaining Stage 7 work

- Replace all eleven biological special-project reward placeholders with
  dedicated reward-card assets and wire their sprites.
- Implement captured-facility secure/destroy/evidence/release handling through
  exact native containment/recovery raids with verified Biological Security
  Assault Detachment participation.
- Add exact immediate risk callbacks for verified arsenal bombing, dedicated
  arsenal sabotage, facility damage, and any documented production-threshold
  hook. The current country-specific sampler remains authoritative but is not
  evidence that these event-driven callbacks are complete.
- Implement native doomsday release raids, remaining countermeasures and
  treatment, designer risk traits, risk-aware production AI, package scenarios,
  and the remaining specialist/completion audits.
