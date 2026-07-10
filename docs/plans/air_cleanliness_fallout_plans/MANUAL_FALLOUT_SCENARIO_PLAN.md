# Manual Fallout Scenario Plan

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Required player experience

The manual Fallout scenario is a direct sandbox launch. It does not require Chaos, prior Air Contamination, a previous event, a focus route, or the ordinary Fallout risk model.

## Event ownership

The scenario registry and selection UI remain part of the generic triggerable-scenario system. Once the player confirms Fallout, the generic launch effect calls a `chaosx.fallout.*` event defined in `events/fallout_world_end_events.txt`.

The Fallout file owns confirmation follow-up, province-strike sequencing, seven-day countdown completion, blackout entry, world rewrite, and post-transition orientation. No Fallout event block is added to `events/chaosx_triggerable_scenarios.txt`.

On confirmation:

1. every valid province receives a thermonuclear strike
2. the strike aftermath remains visible for seven days
3. the normal Fallout blackout begins
4. the normal world rewrite runs
5. the post-Fallout campaign begins

The manual scenario uses the same transition and successor systems as every other Fallout caller.

## Scenario id allocation

Fallout must use the next id in the live triggerable-scenario registry. No fixed id is reserved in this plan.

Allocation procedure:

1. inspect the complete `triggerable_scenario_id` category in the writable checkout
2. verify that existing assignments are unique
3. find the highest assigned integer
4. assign Fallout to that integer plus one
5. use the same allocated value in all registry, sort, display, dispatch, event, documentation, and catalog surfaces
6. record the final id in the implementation handoff and source-of-truth map

Do not move Africa Is One or any other existing scenario. Do not reuse a gap unless the user later asks for gap reuse. Do not copy the next value observed in an older repository snapshot.

The public row should display `SCN-<allocated padded id>` only after the allocation has been verified from the live registry.

## Engine feasibility gate

The exact province strike requirement is non-negotiable.

Before implementation, prove one of these with official documentation and a vanilla or verified working test:

- a nuclear effect that accepts `all_provinces = yes` in state scope
- a province iterator or province selector that can execute the actual nuclear strike effect
- a supported meta-effect that expands a verified province list into nuclear effects
- another engine-native path that produces a real strike on every valid province

The proof must demonstrate:

- visual strike effect or equivalent engine strike state on every valid province
- thermonuclear classification
- state and province damage
- fallout seeding
- no invalid sea or lake targeting
- bounded performance
- deterministic completion

Applying one strike per state does not satisfy this requirement. Adding only province modifiers does not satisfy it. Setting fallout variables without the actual strike does not satisfy it.

If the engine cannot perform the exact sweep, stop the scenario implementation and report the blocker. Do not substitute a smaller barrage without explicit approval.

## Valid province definition

A province is valid when:

- it is a land province
- it belongs to a valid map state
- it is not a lake, sea zone, impassable engine-only province, or invalid placeholder
- the strike effect accepts it

The final trigger is based on verified province properties from official documentation.

## Strike batch architecture

The manual scenario can generate thousands of strike calls. It must avoid multiplying unrelated global systems thousands of times.

At launch:

1. set `fallout_manual_scenario_active`
2. set `fallout_synthetic_strike_batch`
3. stop ordinary event pacing and manual scenario UI actions
4. initialize strike counters
5. execute the exact province sweep
6. apply state-level aggregate direct-strike count and thermonuclear fallout intensity
7. clear `fallout_synthetic_strike_batch`
8. write one aggregate Chaos and death-history context entry where appropriate
9. start the seven-day countdown

During the synthetic batch, normal nuclear hooks should still apply physical state effects that are needed. They should suppress:

- one news event per strike
- one global Chaos history row per strike
- one condemnation update per strike
- one treaty violation event per strike
- one sound or popup per strike
- recursive Fallout request checks

After the sweep, apply one aggregate diplomatic and historical consequence if the pre-Fallout world remains active for the seven-day interval.

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

The blackout begins after the week, not immediately on confirmation.

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

Update all explicit scenario paths:

- id constants
- sort value constants
- registry arrays
- name-sorted arrays in both directions
- id-sorted arrays in both directions
- selected name mapping
- entry name mapping
- entry id mapping
- description mapping
- type mapping
- intensity impact mapping
- launch gate
- click enablement
- confirmation action
- launch dispatch
- scenario event ids
- documentation
- catalog row

The scenario framework uses explicit text and sort branches. Missing one branch will create an incomplete row or wrong default text.

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

- public scenario row shows Fallout with the verified padded allocated id
- allocated raw id is unique and equals the previous live maximum plus one
- every existing scenario keeps its prior id and stored selection meaning
- every valid province receives a verified thermonuclear strike
- no invalid province is targeted
- synthetic strike spam is aggregated
- seven-day delay is exact and persistent
- the standard Fallout blackout begins on day seven
- no normal super-event appears
- selected intensity changes aftermath severity but not strike coverage
- scenario can launch from a clean 1936 game without ordinary prerequisites
