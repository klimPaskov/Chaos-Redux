# Validation and Audit Plan

Ownership authority: `FALLOUT_EVENT_AND_ASSET_OWNERSHIP.md`.

## Validation philosophy

This feature is complete only when the state system, mapmode, transition, world rewrite, manual scenario, successor countries, focus trees, decisions, AI, assets, localisation, documentation, and catalogs agree.

Passing a parser or reaching the main menu is not completion proof.

## Pre-edit reference validation

Before each implementation surface, record the exact local references used.

### Core Air and state logic

Read local official documentation for:

- effects
- triggers
- modifiers
- variables and arrays
- state scope
- script constants
- on-actions

Inspect at least one vanilla example for every nontrivial state effect used.

### Mapmode

Read:

- offline mapmode documentation if present
- interface and graphical asset pages
- vanilla scripted mapmode definitions
- vanilla mapmode strip `.gfx` and textures

Record:

- exact frame width
- actual frame count
- slot numbering convention
- update behavior
- tooltip context scope

### Blackout GUI

Read:

- scripted GUI documentation
- interface documentation
- vanilla full-screen or top-layer window examples
- input and parent-window behavior

Record the exact parent, draw order, and input-blocking precedent.

### Province strike

Read official effects documentation and vanilla nuclear files. Record the exact effect name, accepted scope, province selector, thermonuclear parameter, and performance behavior.

No manual scenario implementation proceeds without this record.

### Country and focus

Read:

- country creation
- cosmetic tags
- dynamic tags
- state transfer
- character creation
- focus trees
- shared focuses
- AI strategy plans
- unit and template creation

Record tag-pool and shared-focus limits.

## Static implementation checks

### Identifiers

Check for:

- duplicate event ids
- duplicate focus ids
- duplicate decision ids
- duplicate cosmetic tag localisation
- duplicate scripted GUI ids
- duplicate mapmode ids
- duplicate script constant keys
- raw scenario id collisions

### References

Check that every reference resolves:

- shared focus roots
- focus prerequisites
- decision categories
- scripted effects and triggers
- localisation keys
- sprite names
- texture paths
- leader portraits
- flag files in three sizes
- audio and sound definitions if used
- state group ids
- country tags

### Lifecycle

Search for every transition flag and variable. Confirm one setter and all required clear paths.

Critical items:

- `fallout_requested`
- `fallout_transition_active`
- processing flags
- player choice flag
- scenario strike batch flag
- scenario countdown
- mapmode phase-change flags
- treaty member cache

### Event and asset ownership

After migration, verify:

- every `chaosx.fallout.*` definition is in `events/fallout_world_end_events.txt`
- no Fallout event block exists in `events/chemical_warfare_events.txt`
- no Fallout event block exists in `events/chaosx_triggerable_scenarios.txt`
- no Fallout caller uses another namespace
- no Fallout texture points into another feature folder
- no Fallout sprite uses a normal super-event slot
- no Fallout sound uses another feature's wrapper or file
- scenario registry labels use the live next-free id
- stale random winter helpers are gone
- docs claiming only chaos above 1000 can trigger Fallout

Any retained compatibility reference must have a documented reason.

## Air Winter scenario tests

### Phase entry and escalation

- start below winter threshold
- cross first threshold gradually
- verify only appropriate states enter Phase 1
- add local fallout and verify faster escalation
- verify phase changes by at most one step without emergency override

### Recovery and hysteresis

- reduce global forcing
- apply local mitigation
- verify recovery counter grows
- verify no immediate multi-phase collapse
- verify exposure remains after phase reduction

### State diversity

Test:

- high-population capital
- rural food state
- desert state
- tropical state
- mountain state
- polar state
- small island
- enclave
- heavily industrialized state
- state with no infrastructure
- state with nuclear and chemical contamination

### Population

- verify winter deaths reduce real state population once
- verify global and state death totals match
- verify Chaos change matches shared death rules
- verify death mapmode receives the loss
- verify no phase modifier applies duplicate population loss

### Buildings

- verify Phase 2 causes no premature damage
- verify Phase 3 pressure accumulates
- verify at most one building family is damaged per eligible monthly tick
- verify protected unique facilities remain safe unless explicitly allowed
- verify recent-damage cooldown works

### Categories

- verify sustained Phase 4 or above is required
- verify original category memory is stored
- verify one-step degradation
- verify cooldown prevents repeated monthly collapse
- verify wasteland is terminal without a restoration route

### Mapmode

- verify all phases have distinct fills
- verify Phase 0 is readable and not falsely highlighted
- verify tooltip order and forecast precision
- verify selected and deselected button frames
- verify mapmode remains responsive at daily updates
- verify no wrong state scope in tooltip

### Flavour and decisions

- verify incident cooldowns
- verify player-state prioritization
- verify AI receives an effect path
- verify every visible choice has a real effect
- verify response costs are varied and explained
- verify obsolete decisions hide after recovery

### Treaty

- form treaty at the accepted severe threshold
- invite and reject members
- use an unconventional weapon as a member
- verify one expulsion and one violation event
- verify cached relationship changes
- verify relief project affects state phase or adaptation
- verify no repeated monthly opinion spam

## Fallout request tests

Test each source:

- gradual contamination just above 100 percent
- severe state share with moderate contamination
- guaranteed upper threshold
- Final Silence direct caller
- another scripted terminal event
- manual scenario day-seven caller
- duplicate request while one is pending
- request while Fallout is active
- request during an incompatible terminal transition

Verify cause and intensity memory.

## Blackout tests

- blackout covers the full screen at each supported resolution
- underlying map and windows cannot be clicked
- no close button exists during processing
- text beat changes only when the host phase changes
- dirty variable prevents unnecessary GUI reevaluation
- save-load resumes the correct beat
- normal super-event does not appear
- super-event audio id remains unset
- abort before destructive processing restores control
- processing failure after destructive work enters recovery and must not clear the screen blindly

## State rewrite tests

Use several pre-transition worlds:

1. low-war historical map
2. active world war
3. fragmented Soviet Collapse world
4. active zombie or Death actor world
5. high contamination with few direct strikes
6. mass thermonuclear exchange
7. island-heavy survivor world
8. multiple human players

Verify:

- deterministic grade for identical input
- grade floor from direct thermonuclear strikes
- shelter and remoteness survival effects
- every valid state processed once
- no invalid owner or controller
- wasteland states follow the accepted ownership rule
- capitals are valid
- resources and buildings match grade
- population totals match death records

## Diplomacy rewrite tests

Before reveal, verify:

- old wars are ended or intentionally mapped
- no old-world truce remains after war settlement
- factions are removed or rebuilt
- subjects and overlords are valid
- guarantees and access are cleared
- no ordered country pair has market access
- docking-rights generation receipts prove exhaustive inverse application without claiming runtime readback
- no observable resource-rights grant remains and the blind resource-free subset has a current exhaustive inverse receipt
- volunteers and expeditionaries are handled
- lend lease and expeditionaries either have exact empty-surface receipts or keep reveal blocked
- ordinary trade and full intelligence remain blocked until exact reset routes exist
- governments in exile are handled
- no peace conference remains in a broken state
- no invalid country target remains in arrays or event targets

After reveal, verify regional diplomacy begins only after the grace period.

## Player continuation tests

- old government survives intact
- old government survives as refuge
- old government fragments
- old government disappears
- several successor candidates exist
- no obvious candidate exists
- player does not choose before timeout
- two human players overlap
- player disconnects during choice

Verify a valid country is always controlled after transition.

## Manual scenario tests

- launch from clean 1936 start
- launch with no nuclear technology
- launch while at peace
- launch during world war
- launch with Air system disabled if manual scenario is intended to override it
- verify every valid province strike
- verify no sea or lake strike
- verify one aggregate history entry
- save and load on days 1 through 7
- verify blackout begins exactly after the configured seven-day interval
- verify intensity changes grade outcomes and not strike coverage
- verify scenario row remains correctly sorted by id and name

## Successor country tests

For every package:

- tag and cosmetic identity load
- capital and fallback work
- state group is connected or intentionally maritime
- leader and party data exist
- flags exist at normal, medium, and small sizes
- starting ideas appear and have a lifecycle
- starting units have equipment and supply
- reinforcement decisions work
- focus tree loads
- archetype branch exists
- regional branch exists
- country memory branch exists
- AI has a valid route
- invalid routes are blocked
- assets and localisation resolve

## Focus tests

- no duplicate coordinates where the layout forbids them
- no invalid relative position recursion
- prerequisites have intended AND and OR semantics
- mutual exclusions represent real route conflicts
- shared focus roots exist
- tree has a non-shared anchor
- country memory content is not generic
- branch payoffs change play
- every major route has AI behavior
- every expansion route has postwar handling
- no repeated fairy-dust rewards
- no free unit, equipment, core, or war-goal loop

## Performance tests

Measure on representative hardware:

- monthly Air state pass before and after winter implementation
- daily Deaths pass with severe global winter
- mapmode daily update cost
- blackout GUI update cost
- state grading time
- state ownership rewrite time
- country package application time
- manual province strike time
- save size and save time before and after Fallout

Performance fixes must preserve behavior. Do not remove required state effects as an optimization without approval.

## Audit order

### After Tranche 1

- scripted system architecture audit
- documentation curation

### After Tranche 2

- decision and mission audit
- localisation audit
- scripted system recheck
- documentation curation

### After Tranche 3 and 4

- scripted system audit
- country package audit for rewrite foundation
- completion audit limited to transition and world-state surfaces
- documentation curation

### After Tranche 5

- decision and mission audit for scenario UI
- completion audit for the allocated manual Fallout scenario

### After each successor wave

- country package audit
- focus tree audit
- decision and mission audit
- localisation audit
- asset handoff review
- documentation curation

### Final

- spreadsheet worker
- full event completion auditor
- manual improvement-loop closure or a new addendum only if a new large gap appeared after implementation

## Completion report evidence

The final report must include:

- files changed
- implemented tranches
- route and country coverage tables
- tag and state ledger status
- mapmode slot proof
- province strike proof
- performance results
- meaningful scenario results
- audit reports and disposition
- assets created, sourced, wired, or blocked under Fallout-owned paths, with any same-country identity reuse documented
- documentation and spreadsheet updates
- every simplification, omission, blocker, or approved deviation

If no simplifications remain, say so and support the claim with the completed matrices and audits.

## Final quality bar

The feature is ready only when a player can experience gradual environmental decline, understand the winter map, make costly survival choices, watch the old world disappear through a dedicated blackout, continue as a valid post-Fallout country, and play a distinct ten-year campaign without generic successor content or broken world state.
