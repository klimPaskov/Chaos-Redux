# Missile startup loader repair handoff

Status: implemented source repairs; parent startup validation pending; required MCP comparison blocked.
Acceptance basis: parent delegated the two missile effect files under the user-authorized all-startup-errors repair pass.
No commit created.

## Files changed

- `common/scripted_effects/032_missiles_operations_effects.txt`
- `common/scripted_effects/032_missiles_scenario_effects.txt`
- Matching `032_missiles_operations_effects.md` and `032_missiles_scenario_effects.md` documentation added.
- This handoff and `script_missile_lifecycle_references.md` exact-token evidence added.

Original script bytes are retained under `baseline/scripts/common/scripted_effects/` in this QA run directory.
Baseline error evidence is `logs/cycle_01/error.log` in this directory.

## Repairs and lifecycle proof

The operations file had 17 invalid temporary-clear calls and the scenario file had 24.
The repair removes 23 terminal scratch clears (17 operations and six scenario), while migrating the other 18 cleanup calls together with their nine input setters to country-scoped variables.
This is not a replacement of temporary cleanup with regular cleanup: all nine package writers were migrated in the same change.
The exact-token companion inventories all 27 affected identifiers with writers, readers, owning helpers and direct callers across common, events, interface and localisation.
The matching helper docs give initialization, nested-call, loop and continuation proofs.

Scenario package presence semantics are retained: stage/reserve/site-capacity presence gates still work; explicit zero readiness/control values remain different from absent inputs.
Every recipient assigns all nine input variables before nested package initialization and clears them on both success and failure completion paths.
Bounded finish cleanup clears the same nine input names again for every selected country.
The nested state-loop capacity reads and controller predicate use PREV, the package country, so another country's manual scenario origin cannot supply the capacity input or exclude the recipient's own sites.

Calculation scratch values retain all arithmetic and durable writes.
Guidance training scratch is read only in the branch that initializes it.
Capture scratch remains alive from `missiles_transfer_captured_reserve` through the enclosing capture debit/credit operation.
Civil-war and annex receipt scratch is initialized per applicable transaction/iteration and copied into conservation records before terminal return.
The requested-count calculation publishes its result to an explicitly global variable before selection.
Evolution selections are assigned directly before recorder/track calls; subsequent calls initialize their own selection.
Warning schedule scratch is consumed by the queued event duration; continuations use stored warning dates and recalculate it before another schedule.

The regular warning-recipient target is left to documented automatic chain expiry; every warning seed overwrites it before reading it and durable participants are recorded separately.
The global warning root keeps its persistence and closure cleanup; `has_event_target` replaces the nonexistent global-only trigger.
The divisions-in-state size parser receives a file-local `@missiles_division_presence_floor = 0`, retaining the strict positive-division condition and dynamic state reference.
The nonexistent attribution key `uncertain` is repaired to existing `unknown = 4`, preserving the comparison operator and highly-likely result.
No probability or AI weight, random draw, pool, reserve formula, timing formula, or mechanic was removed.

## Helper map, constants and migration

No helper declarations or direct external call sites were added.
`missiles_scenario_apply_country_package` supplies country input variables to existing `missiles_initialize_or_advance_program` then `missiles_initialize_scenario_package`, with durable program/site results and explicit package cleanup.
`missiles_scenario_finish_transaction` retains array-bounded cleanup.
The only added constant is the parser-compatible file-local division presence floor.
No central tuning tables, recurring hooks, assets or player-facing text were changed.

## Meaningful validation

Reviewed the baseline-relative diff for both owned files.
Verified exactly nine country package assignments and 18 country package cleanup calls.
Reviewed exact-token consumers and direct callers, including the scenario initializer bypass gate, capture helper output continuation and scheduled warning event.
Verified `missiles_prepare_guidance_weights` and `missiles_select_operation_guidance_outcome` are byte-equivalent as decoded source to baseline.
All arithmetic, weights and outcomes in those helpers remain unchanged.
This source evidence is not a live behavior or probability-scenario pass; the parent owns the global probability auditor and runtime validation.

Required references consulted: AGENTS.md; events, subagents and explicitly requested debug-playtest skills; the eleven core offline wiki pages, especially Data structures event-target and temporary-variable lifetime sections; vanilla effects/triggers documentation for clear_variable, save_event_target_as, clear_global_event_target, has_event_target and divisions_in_state; both script-constant documentation sources; existing dynamic-effect registry and vanilla save/has-event-target precedents.
No skill was changed.

## MCP evidence and blockers

Selector supplied as instructed: `{kind: event, eventId: chaosx.nr032.1}`.
Trace returned EVENT_INSPECTED_PARTIAL; targets render returned EVENT_RENDERED_PARTIAL.
Both explicitly defer workspace-wide helper projection/lifecycle passes because of workspace size, so they do not prove this full helper lifecycle.
The source's scheduled warning event is `chaosx.nr32.82`; exact source consumers were traced separately.
Compare with the returned revision failed with EVENT_REVISION_NOT_CACHED.
Artifact-backed comparison using the emitted render JSON then failed with EVENT_GRAPH_ARTIFACT_INVALID: event graph artifact uses an unsupported schema version.
These exact route limitations remain blockers, not equivalent successful engine evidence.

## Simplifications, omissions and follow-up

No gameplay simplification or zero-reset fallback was used.
Runtime startup/error-clearance acceptance is pending the parent loop.
Required event comparison is blocked as above.
No new save, game launch, console action, or process control was performed by this worker.

Artifact references:

- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2f4b3a071e32ea7974321c5fa7ecccba655084186848593d0d0a729dca08ada4/54779c5751e9b8d45777838b20fd19457685c6edbf86b7cd30f4b3b2e92eec61/event-targets-4bccb6ec7fe1-manifest.json
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ff4153b6218e74679bb168d47be5de6a055e12f0b4659aabac29ca9b5732a97/cd5289b18295f51a048268bd67393a5a740ad40f0d8b386ac9975223b3d00249/event-targets-4bccb6ec7fe1.json
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b02dbd41211f124726c8014edb05da13725abea8f587cad22ce026c0ca1bde7/82a8e6f056c221cc76f889ba7d642d4eb60ead3e1e4095d098fdca2427c7baec/event-targets-4bccb6ec7fe1.svg
- hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a9cc8fe7fbab996469f6ba4aada7190391457ae494928851492c7febd15554f/faa4a978291b82ebc8f468e344c90ef8187edf0af043f4faa17caaf58c642d96/event-targets-4bccb6ec7fe1.png

