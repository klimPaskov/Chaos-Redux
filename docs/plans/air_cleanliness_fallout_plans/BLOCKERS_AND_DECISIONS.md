# Blockers and Parent Decisions

## Blocking items before gameplay edits

## B1: writable repository and local official documentation

Status: blocked in this environment

Required evidence:

- writable local Chaos Redux checkout
- local `paradox_wiki/` snapshot
- local Hearts of Iron IV `documentation` folder
- local vanilla game files

Reason:

`AGENTS.md` requires the offline wiki, official documentation, and vanilla precedent before edits. The GitHub repository made the offline wiki visible for planning, but the local official documentation and game installation were not available here.

Resolution:

Complete Tranche 0 locally. No gameplay code was edited in this pass.

## B2: exact province-wide thermonuclear strike

Status: unproven

Accepted requirement:

Every valid province must receive a thermonuclear strike.

Observed evidence:

- a global `every_state` scope exists
- province selectors exist for some state effects
- no repository precedent for `every_province` was found
- no verified nuclear effect accepting all provinces was found in this pass

Resolution gate:

Prove the exact effect and scope with local official documentation and a working test.

Forbidden resolution:

- one strike per state
- province modifiers only
- setting fallout variables without actual strikes
- reducing the strike set for performance

## B3: manual scenario id allocation

Status: live registry scan required

Observed snapshot:

- reserved raw id 7
- Africa Is One raw id 8

Allocation rule:

- inspect every assigned scenario id in the live checkout
- set Fallout to one greater than the highest assigned id
- preserve every existing scenario id and stored selection value
- update registry arrays, sorting, localisation, dispatch, and documentation with the allocated id

The inspected snapshot is historical evidence only. A newer checkout may already contain additional scenarios, so the assigned Fallout id must come from the live registry scan.

## B4: mapmode strip frame mismatch

Status: local asset inspection required

Live state:

- `.gfx` declares 19 frames
- comment claims vanilla 18 plus two Chaos Redux slots
- documentation claims 20 frames and assigns slots 19 and 20

Resolution:

Inspect actual DDS dimensions and frames. Correct metadata and documentation before appending the winter icon.

## B5: full-screen GUI drawing order

Status: local vanilla precedent required

Need proof that the blackout:

- covers all ordinary windows and popups
- blocks underlying input
- remains visible through the rewrite
- works at supported resolutions
- remains synchronized in multiplayer

Do not assume a top-bar parent is sufficient.

## B6: old `world_end_fallout` save migration

Status: parent policy required

Potential old save states:

- terminal flag set with no rewrite
- Fallout super-event visible
- event system stopped
- contamination at terminal threshold

Recommended policy:

Route old terminal Fallout saves into the new transition using a versioned compatibility event, after clearing only the old Fallout presentation state.

The parent must decide whether old terminal saves are supported or explicitly unsupported. Do not leave the behavior implicit.

## Design decisions already resolved

### D1: normal super-event removal

Resolved:

Fallout uses a dedicated blackout scripted GUI. It does not use a super-event slot, quote, reaction button, or super-event audio id.

### D2: treaty disposition

Resolved for implementation planning:

Restore and modernize the treaty because it is part of the accepted design. Live code disabling it is not treated as a design rejection.

### D3: three-layer focus architecture

Resolved:

Archetype, region, and memory are design layers. Implementation can use verified shared focuses or compiled full trees. Every final country is manually reviewed.

### D4: candidate pool size

Resolved:

The 99 matrix rows are candidates. The rewrite selects a coherent subset. No requirement exists to spawn all 99 at once.

### D5: population ownership

Resolved:

All winter and Fallout population loss uses the shared Deaths pipeline.

### D6: periodic loop ownership

Resolved:

Extend the existing host monthly Air state scan. Do not add another global monthly country loop.

### D7: mutant science boundary

Resolved:

Mutant countries are fictional high-chaos content and are never described as real radiation science.

## Decisions required during the pilot

## P1: shared focus or compiled tree

Decision timing:

After two prototype countries use the same archetype.

Choose shared focus composition only when:

- both trees load safely
- layout remains readable
- country memory remains distinct
- no hidden branch leaks
- audit finds no brittle dependency

Otherwise use compiled full trees with shared scripted helpers.

## P2: wasteland ownership

Options to test:

- leave wasteland owned by a regional actor with severe state rules
- assign wasteland to a dedicated non-playable exclusion actor
- keep ownership but remove normal economic value

Decision criteria:

- AI pathing
- front creation
- supply behavior
- diplomacy
- performance
- player readability

The source spec should guide the choice, but engine behavior determines the safe representation.

## P3: player successor selection scope

Options:

- automatic strongest direct successor
- limited candidate list tied to former player territory
- broader regional list when the former territory is entirely terminal

Accepted default:

Use automatic continuation when the old government survives. Use a limited candidate list when it does not.

## P4: treaty membership survival after Fallout

Possible uses:

- treaty memory increases successor legitimacy
- treaty relief infrastructure improves state survival
- former treaty members receive a reconstruction diplomacy route
- violators receive distrust and isolation memory

This is expected content, but exact numerical influence is tuned during implementation.

## P5: ordinary world-end documentation

The root event skill and mechanics guide say world ends normally require Chaos above 1000 and use super-events.

Required documentation decision:

Add Fallout as an explicit system exception without weakening the ordinary rule for other world-end scenarios.

## Not accepted as shortcuts

- replacing state phases with global modifiers
- using the existing contamination mapmode instead of adding winter visibility
- applying only attrition and no population or building effects
- firing generic flavour with no effects
- leaving active successors on the generic focus tree
- applying one universal Fallout focus tree with renamed text
- spawning countries without starting units or AI
- using a normal super-event for the blackout
- skipping the seven-day manual scenario delay
- one thermonuclear strike per state
- calling the feature complete before regional and country audits


## Resolved ownership decision: dedicated Fallout package

Status: fixed design rule

Fallout owns `events/fallout_world_end_events.txt`, the `chaosx.fallout` namespace, its scripted system files, its blackout GUI and GFX, its asset folders, and any accepted audio files.

Delete stale Fallout blocks in other event files. Do not retain compatibility events in an older namespace. Do not reuse another feature's visual or audio assets. Generic systems may call the Fallout entry helper, but ownership transfers at that call boundary.
