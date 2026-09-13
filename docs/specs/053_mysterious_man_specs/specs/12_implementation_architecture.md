# 12. Implementation Architecture

## Ownership layout

The Event 53 implementation should use event-owned files for lifecycle and selection.

Recommended file map:

| Surface | Recommended path |
| --- | --- |
| Event chain | `events/053_mysterious_man.txt` |
| Script constants | `common/script_constants/053_mysterious_man_constants.txt` |
| Event-owned effects | `common/scripted_effects/053_mysterious_man_effects.txt` |
| Event-owned triggers | `common/scripted_triggers/053_mysterious_man_triggers.txt` |
| Event-owned scripted localisation | `common/scripted_localisation/053_mysterious_man_scripted_localisation.txt` |
| Player-facing localisation | event-specific English localisation file following repo naming |
| Event-owned GFX registration | event-specific GFX file following repo pattern |
| Report-event DDS folder | `gfx/event_pictures/053_mysterious_man/` |
| Event documentation | `docs/events/053_mysterious_man/` |
| Source specification | `docs/specs/053_mysterious_man_specs/` |
| Working implementation plans | `docs/plans/053_mysterious_man_plans/` |

Owner adapters stay in their own event or system files.

## Working event roles

The final numeric suffixes should be chosen after inspecting the namespace. Recommended roles:

| Working role | Suggested namespace identity |
| --- | --- |
| Parent entry and first appearance | `chaosx.nr53.1` |
| Recurring appearance dispatcher | Event 53 follow-up |
| Payment resolution | Event 53 follow-up |
| Refusal selector bridge | Event 53 hidden follow-up or direct effect call |
| Direct consequence reports | Event 53 follow-ups |
| Evolution activation | Event 53 hidden follow-ups |
| Pause recheck | Event 53 hidden follow-up |
| Target cleanup | Event 53 hidden follow-up |
| Legal-successor transfer receipt | Event 53 hidden follow-up or effect |

Only the parent entry counts as Event 53 firing.

## Core flags

Recommended persistent flags or equivalent state markers:

- Event 53 target
- Event 53 chain active
- Event 53 visit scheduled
- Event 53 visit paused
- Event 53 visit present
- Event 53 consequence resolving
- Event 53 transfer in progress
- Event 53 Evolution I active
- Event 53 Evolution II active
- Event 53 Evolution III active

Use flags for true or false state. Do not use numeric variables that only store zero or one.

## Core variables

Recommended persistent variables on the target or owner ledger:

- total visits
- total payments
- total refusals
- consecutive refusals
- first appearance date components if the project stores them
- latest visit date components
- latest demand type
- latest demand amount
- latest consequence package ID
- current transaction sequence ID
- latest accepted receipt ID
- current behavior tier when a derived value is needed

Temporary variables can hold pool counts, random index, amount calculations, state counts, and adapter inputs. Temporary variables must not be scope-prefixed.

## Persistent target pointer

Use a global event target or another established persistent country pointer only when the engine and repository pattern support safe persistence. The selected country marker remains the recovery proof.

Global event targets require explicit cleanup. The implementation must clear the pointer on target extinction, incompatible transformation, final chain closure, or successful transfer.

## Constants

Centralize all tuning in `common/script_constants/053_mysterious_man_constants.txt`.

Constant categories should cover:

- interval minimums and maximums by behavior tier
- absolute interval floor
- refusal interval reductions and caps
- visit progression
- payment progression
- refusal progression
- demand-family minimums
- demand-family proportions
- demand-family caps
- protected Stability and War Support payment floors
- temporary industrial-burden durations
- direct consequence severity profiles
- evolution thresholds when the project does not already expose shared tier constants
- package IDs
- demand type IDs
- transaction result IDs
- adapter origin IDs

Do not scatter values across event options and effects.

## Demand engine helpers

Recommended Event 53-owned effects and triggers:

- `mysterious_man_select_valid_demand_type`
- `mysterious_man_calculate_locked_demand`
- `mysterious_man_can_pay_locked_demand`
- `mysterious_man_apply_locked_payment`
- `mysterious_man_clear_locked_demand`
- `mysterious_man_get_next_visit_interval`
- `mysterious_man_schedule_next_visit`
- `mysterious_man_pause_visit`
- `mysterious_man_resume_visit`

Each demand family should use a bounded calculator helper or a clear dispatch table. Static engine fields that need dynamic tokens can use a verified meta effect pattern.

## Consequence registry helpers

Recommended Event 53-owned surfaces:

- `mysterious_man_build_valid_consequence_pool`
- `mysterious_man_apply_random_consequence`
- `mysterious_man_dispatch_selected_consequence`
- `mysterious_man_record_adapter_receipt`
- `mysterious_man_handle_adapter_rejection`
- `mysterious_man_clear_consequence_transaction`

A registry-oriented dispatch can use stable package IDs and meta effects when the engine pattern is verified.

Each package needs an owner-specific validity trigger with a predictable naming pattern. Example working pattern:

- `mysterious_man_consequence_<package>_is_valid`
- `mysterious_man_consequence_<package>_apply`

The Event 53 selector owns the list of registered packages. Owner adapters own the real crisis work.

## Uniform selection implementation

The preferred implementation builds an array or equivalent list containing each valid package ID once, then selects one random member or one random ordinal.

If engine constraints require a `random_list`, every active entry must have the same fixed weight and the implementation must prove that invalid entries are absent. Repeated branches are forbidden.

The probability auditor must inspect the final engine structure. Hand reasoning is not enough.

## Visit transaction sequence

Every visit receives a new sequence ID.

The sequence ID is copied into:

- locked demand state
- payment or refusal state
- selected package state
- owner adapter inputs
- owner receipts
- cleanup state

A helper must reject a stale sequence ID. This prevents delayed owner events from closing or modifying a later visit.

## Adapter registration

The Event 53 registry manifest under `quality/consequence_registry_manifest.md` is the design source for package coverage.

Implementation should convert each accepted row into:

- one stable package constant
- one Event 53 registration branch
- one validity call
- one dispatch call
- one receipt expectation
- one documentation row

A reserved adapter stays out of the live registration path until the owner implementation exists.

## Evolution implementation

Evolution checks run only after Event 53 is active and only for the selected target.

Recommended flow:

1. schedule one target-local evolution check
2. inspect the next unrecorded enabled threshold
3. use a dynamic delay or MTTH-equivalent pacing around the project's normal evolution standard
4. activate the behavior feature
5. set shared evolution context
6. record the shared evolution row with target actor
7. schedule the next check only when another milestone can become relevant

When Event 53 first fires above one or more thresholds, setup can activate enabled behavior immediately and record enabled milestones in order.

Evolution activation gives zero Chaos.

## Registration and Event Log work

Implementation must update the normal Event 53 integration surfaces in one change:

- Fire-Once event array
- Chaos level registration
- event type resolver
- default enabled allowlist after rework completion
- event name mapping
- History actor mapping
- Event Details premise and status data
- evolution catalog and history display
- event documentation
- authoritative catalog workbook after final localisation exists

The current export-only CSV must never be edited directly.

## Asset wiring

Register stable sprite names for the five report-event images after the asset handoff is accepted.

The event dispatcher chooses a valid location and corresponding image. The image selection is presentation-only.

The implementation must preserve one fictional identity across all scenes and reject any asset that visually explains the man's nature.

## Startup reconciliation

Use an existing bounded startup or event-system repair path to call one Event 53 reconciliation effect. Do not add a recurring whole-world scan.

The reconciliation effect checks:

- unique target marker
- persistent pointer recovery
- schedule-state exclusivity
- stale locked demand
- completed adapter receipt
- stale transaction cleanup

When proof is ambiguous, end the chain and log the error instead of selecting a target by guess.

## Required MCP work

Before and after implementation:

- use `hoi4.event_inspect` for the Event 53 chain
- use `hoi4.event_render` for event flow and scope review
- use `hoi4.event_compare` against the pre-rework chain when available
- use `hoi4.probability_inspect` before probability analysis
- use `hoi4.probability_evaluate` for named complete-pool scenarios
- use `hoi4.probability_sweep` for demand and severity thresholds
- use `hoi4.probability_compare` after any weighted or selection patch
- use `hoi4.probability_render` when the pool matrix or comparison improves auditability

The probability auditor remains read-only. The implementation owner applies changes and requests comparison with the same scenarios.

## Recommended implementation order

1. inspect the existing Event 53 namespace and registration
2. inspect relevant wiki, vanilla documentation, and local event precedents
3. add constants and owner lifecycle state
4. implement target selection and parent firing
5. implement visit scheduling and player-control pause
6. implement demand selection, amount locking, and payment transactions
7. implement the Event 53 direct consequence packages
8. implement registry construction, uniform selection, receipts, and rejection recovery
9. add owner adapters one system at a time
10. implement compound packages after component adapters pass independently
11. implement Evolution III catastrophe adapters
12. wire evolution logs, Event Details, and History
13. produce and wire assets
14. write final localisation and run localisation audit
15. update event docs
16. update the authoritative catalog workbook and export CSVs
17. run probability comparison and event completion audit

## Implementation boundaries

The implementation should not add a dedicated decision category, custom scripted GUI, focus tree, country package, portrait package, 3D model, triggerable scenario, achievement set, or super-event unless the user separately expands the accepted design.

Those additions would create maintenance and presentation weight without improving the core recurring choice.
