# Manual Fallout Scenario Plan

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Current implementation status

The exact installed-map sweep substrate exists but is dormant.

- The proof targets installed Hearts of Iron IV build 1.19.2.0.
- `chaosx.fallout.900` is the bootstrap, `.910` through `.950` identify batches 0 through 40, `.960` through `.966` identify verifier attempts 0 through 6, and `.903` is the exact seven-day callback.
- The former generic `.901` and `.902` callbacks are absent.
- Forty-one generated batch effects issue 10,154 native thermonuclear province calls across all 1,081 installed states. Batches 0 through 39 contain 250 targets and batch 40 contains 154.
- The ledger excludes 118 assigned non-land provinces and includes 126 assigned land targets in impassable states because no official exclusion was found.
- The native observer and state-sum verifier must pass before the countdown begins.
- Each verified struck state applies exact population loss against its frozen
  prestrike baseline until 90 to 95 percent is gone. The observed total is then
  written once to the shared Deaths ledger with state mutation disabled on the
  accounting call, and the Fallout exception keeps that receipt mandatory even
  when the general Deaths setting is disabled. Aggregate nuclear fallout, Air
  Contamination, Chaos history, condemnation, and treaty consequences run only
  after complete verification.
- Save recovery extends the existing host daily coordinator for hourly sweep and verifier callbacks and never adds a second recurring world iterator. The seven-day callback remains engine-owned and cannot be reconstructed from a calendar-day value.

The manual sandbox row and dispatch use raw id 14. The live triggerable-scenario registry includes Black Plague at raw id 12 and reaches raw id 13 with The Unbidden Muster. Fallout remains absent from the world-end Event Details card, ordinary Event Log, evolution, and ordinary super-event registries. Existing ids remain unchanged.

Runtime acceptance and bounded performance remain unobserved because Hearts of Iron IV was not run and must not be run for this documentation task. The dormant substrate is not a release claim.

Vanilla `on_nuke_drop` schedules twelve one-day nuclear news events per callback. If every scripted call emits the callback, the sweep may schedule about 121,848 vanilla news event attempts. The mod callback cannot suppress that separate vanilla branch. Callback occurrence, callback synchrony, and the news-event load are release blockers.

Static proof and map hashes are recorded in `FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md`.

## Required player experience

The manual Fallout scenario is a direct sandbox launch. It does not require Chaos, prior Air Contamination, a previous event, a focus route, or the ordinary Fallout risk model.

## Event ownership

The generic manual-scenario framework may dispatch a Fallout-owned bootstrap callback after an authorized request. The callback owns confirmation follow-up and province-strike sequencing.
It is not the Fallout consequence itself. The manual sandbox entry is only a launch surface. Fallout is not inserted into the ordinary Event Log, evolution, or ordinary super-event registries, and the world-end selector row describes the consequence without becoming an ordinary event.

The Fallout file owns the strike transaction, seven-day countdown completion, blackout entry, world rewrite, and post-transition orientation. No Fallout event block is added to `events/chaosx_triggerable_scenarios.txt`.

On confirmation:

1. every valid province receives a thermonuclear strike
2. the strike aftermath remains visible for seven days
3. the normal Fallout blackout begins
4. the normal world rewrite runs
5. the post-Fallout campaign begins

The thermonuclear aggregate consequence removes 90 to 95 percent of each
state's prestrike population during the verified strike resolution. The first
strike uses the 90 percent floor and additional province strikes provide only
a small capped increment. Each state mutation is recorded through the shared
Deaths ledger after the exact loss is observed, even if the general Deaths
setting is disabled. The later rewrite reconciles the original baseline
against the grade-specific survivor target and never applies a second full
population percentage to the already reduced state.

The manual scenario uses the same transition and successor systems as every other Fallout caller.

## Scenario id allocation

Fallout uses reserved id 14, the next integer after the live maximum of 13 observed during implementation.

Allocation procedure:

1. inspect the complete `triggerable_scenario_id` category in the writable checkout
2. verify that existing assignments are unique
3. find the highest assigned integer
4. assign Fallout to that integer plus one
5. use the same allocated value in Fallout-owned reservation, dispatch, manual sandbox row, and documentation surfaces while keeping ordinary Event Log, evolution, Event Details, and ordinary super-event surfaces Fallout-free
6. record the final id in the implementation handoff and source-of-truth map

Do not move Africa Is One or any other existing scenario. Do not reuse a gap unless the user later asks for gap reuse. Do not copy the next value observed in an older repository snapshot.

The manual sandbox row displays `SCN-014`. The Fallout-owned constant `fallout_manual_scenario_identity.triggerable_scenario_id` holds the reservation for that launch surface. No ordinary Event Log, evolution, or ordinary super-event row displays it, and the world-end selector keeps Fallout as a consequence description rather than an ordinary event.

## Engine feasibility and runtime release gate

The exact province strike requirement is non-negotiable.

Static source proof now establishes a supported province-valued `launch_nuke` call and an exact installed-map expansion. Runtime release still requires proof of these properties:

- each `launch_nuke` call is accepted, including the 126 land targets in impassable states
- `use_nuke = no` emits exactly one `on_nuke_drop` callback inside the guarded batch window
- each target produces the required native province result
- the exact thermonuclear classification and state damage remain intact
- 250-call batches remain bounded for performance, save integrity, and multiplayer synchronization
- the vanilla one-day news-event branch remains bounded
- completion stays deterministic across all 41 batches

Applying one strike per state does not satisfy this requirement. Adding only province modifiers does not satisfy it. Setting fallout variables without the actual strike does not satisfy it.

If the engine cannot perform the exact sweep, stop the scenario implementation and report the blocker. Do not substitute a smaller barrage without explicit approval.

## Valid province definition

A province is included in the installed-build ledger when:

- it is a land province
- exactly one installed state assigns it
- its id is greater than zero

The ledger excludes 118 assigned non-land ids. It includes 126 assigned land targets in states marked `impassable = yes` because neither the official effect documentation nor the offline wiki documents an exclusion. Runtime rejection of any such target is a blocker and does not authorize silently reducing the strike set.

## Strike batch architecture

The manual scenario can generate thousands of strike calls. It must avoid multiplying unrelated global systems thousands of times.

The dormant substrate currently sequences launch work as follows:

1. `.900` initializes the manual transaction and schedules batch token `.910`.
2. Batch tokens `.910` through `.950` execute exactly one expected batch each.
3. Verifier tokens `.960` through `.966` allow a bounded callback-settling window.
4. Complete issued, observed, unique-state, state-sum, and array-size agreement applies aggregate consequences once.
5. The verified transaction stores a seven-day countdown and schedules `.903`.

Manual runtime schema 4 binds each scheduled callback and the completed prestrike population baseline ledger to the active transaction generation. Capture records the exact installed state count once, then the host validator and scheduled callbacks use the generation-bound O(1) receipt before more native work. The callback also validates the last completed batch and observed-count bounds before opening the launch window. The countdown event and request wrapper both validate the active token before handoff. Schema 1 through schema 3 active transactions fail closed. Successful request handoff clears the due flag and countdown schedule provenance.

During the synthetic batch, normal nuclear hooks should still apply required physical state effects. Mod-owned callback consequences should suppress or aggregate:

- one Chaos Redux news or report event per strike
- one global Chaos history row per strike
- one condemnation update per strike
- one treaty violation event per strike
- one sound or popup per strike
- recursive Fallout request checks

Chaos Redux owns aggregation for its callback consequences. It cannot suppress the twelve one-day news events scheduled by the separate vanilla `on_nuke_drop` branch. That unresolved engine load blocks public wiring.

After the sweep, one aggregate diplomatic and historical consequence is applied only after complete verification and while the pre-Fallout world remains active for the seven-day interval.

## Thermonuclear classification

Do not rely on the attacker merely owning thermonuclear technology. The manual scenario must pass an explicit thermonuclear mode into the strike helper.

The strike helper should support:

- ordinary live nuclear hook mode
- explicit thermonuclear scenario mode
- explicit scripted terminal mode

This prevents a normal nuke from being misclassified because a country has thermonuclear stock and prevents a manual thermonuclear strike from being weakened because the launcher lacks the technology.

## Seven-day countdown

Use a persistent global countdown or timed global flag with a verified constant-compatible field.

Required behavior:

- countdown starts only after the complete strike sweep finishes
- countdown survives save-load
- ordinary Air and nuclear deaths continue during the week
- no duplicate countdown can begin
- the player can see a restrained scenario status indicator or event direction
- on day seven, a host-owned event calls `fallout_request_aftermath`
- request source is manual Fallout scenario
- bypass is enabled
- intensity includes selected scenario intensity and measured strike result

The live static path stores the end day as the verified start day plus seven and schedules `.903` with a literal seven-day delay. Only that engine-scheduled callback may submit the standard Fallout request. Daily reconciliation cannot submit early and cannot rebuild a lost countdown from an integer day. Lost ownership and an overdue callback fail closed. The blackout begins after the week, not immediately on confirmation.

## Intensity control

Every launch still strikes every valid province. Intensity changes the aftermath, not the completeness of the sweep.

Suggested effects:

- Low: slightly better shelter survival and lower state-grade bias
- Medium: baseline grade model
- High: higher infrastructure and category damage bias
- Maximum: highest terminal-zone and mutant-fiction weighting

The selected intensity also affects:

- starting survivor resources
- old-government survival chance
- successor fragmentation count
- severity of the opening winter
- rare route eligibility

It must not reduce the strike set.

## Scenario type control

A type selector is optional. The simplest accepted form has one type: total thermonuclear exchange.

Add additional types only when they change the scenario meaning without weakening the required default. Possible later types:

- total thermonuclear exchange
- silent terminal event using the same state-grade floor
- mixed chemical and nuclear collapse

Do not add types during the first implementation if they delay the required scenario.

## Registry integration checklist

Keep ordinary Event Log, evolution, Event Details, and ordinary super-event registries Fallout-free. Audit the Fallout-owned surfaces instead:

- reserved id constant
- manual launch gate
- confirmation action
- strike dispatch
- countdown callback
- blackout handoff
- documentation and blocker records

The manual framework uses explicit launch and dispatch branches. Missing one Fallout-owned branch can strand the transaction or create a duplicate request. Adding a public registry row is out of scope.

## Launch gate

Allow launch when:

- no Fallout transition is active
- no completed Fallout world is active
- no other terminal rewrite is processing
- a valid player country scope exists
- province-strike proof has been enabled in the build

Do not require:

- Chaos threshold
- contamination threshold
- prior event
- evolution
- date
- ideology
- nuclear technology
- nuclear stockpile

## Save-load and duplicate safety

Persist:

- manual scenario active flag
- strike completed flag
- countdown start date or remaining days
- request source and intensity

On load:

- if strike is complete and countdown remains, resume the countdown
- if request is already sent, do not repeat the strike
- if Fallout transition is active, hide scenario actions
- if Fallout is active, remove the pending scenario state

## Performance validation

Measure:

- strike sweep execution time
- state update time on the first daily and monthly ticks after the sweep
- save size increase
- event log and history row count
- multiplayer host and client behavior

If the sweep needs batching, the seven-day countdown begins after the final batch. The screen does not falsely claim the week has begun while provinces remain unprocessed.

## Acceptance checks

- the manual sandbox row alone contains `SCN-014`
- no ordinary Event Log, evolution, or ordinary super-event row contains Fallout
- the world-end selector row describes the Fallout consequence without registering an ordinary event
- allocated raw id is unique and equals the previous live maximum plus one
- every existing scenario keeps its prior id and stored selection meaning
- every valid province receives a verified thermonuclear strike
- no invalid province is targeted
- mod-owned callback consequences are aggregated once after complete verification
- vanilla `on_nuke_drop` news-event amplification is resolved without weakening the strike set
- seven-day delay is exact and persistent
- the standard Fallout blackout begins on day seven
- no normal super-event appears
- selected intensity changes aftermath severity but not strike coverage
- scenario can launch from a clean 1936 game without ordinary prerequisites
