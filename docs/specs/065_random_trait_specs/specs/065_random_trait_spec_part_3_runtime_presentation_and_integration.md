# Event 065 Random Trait

## Part 3: Runtime, Presentation, Integration, and Performance

## Event architecture

Event 65 uses one hidden executor and one human-facing report path.

### Hidden executor

The root event remains `chaosx.nr65.1`.

It owns:

- Evolution resolution
- world eligibility pass
- country-leader targeting
- trait rolls
- source-trait application
- Event 65 ledger updates
- global and player result counters
- direct Chaos milestone
- event history
- Evolution history
- cluster outcome data when fired as a member
- human report dispatch

The root executes once per selected Event 65 firing.

It is the only path that changes leader traits.

### Human report

A report event or equivalent global-report pattern opens once for each human-controlled country after the executor has finished.

It owns:

- event picture
- final player-facing title and description
- the local player's trait-result list
- global result summary
- active Evolution display
- acknowledgment option
- report-only cleanup when needed

Its acknowledgment option does not own gameplay effects.

### AI countries

AI-controlled countries receive the trait mutation through the hidden executor.

They do not need a visible popup.

The implementation must avoid creating a queue of report events for AI countries.

## Deterministic multiplayer behavior

All random rolls occur in one synchronized game-state execution path.

Clients must not roll traits independently through their own visible events.

The host-authoritative result must be identical on every client.

The implementation must use deterministic country traversal and deterministic source-pool logic supported by the engine.

Every human player receives a report derived from the already committed game state.

Closing one player's report must not affect another player's report or any leader result.

A late report dismissal must not hold global temporary state needed by other clients.

Use persistent last-firing result variables that are overwritten on the next Event 65 firing, or use another synchronized report-safe storage pattern.

## Result data

The root records these global values for the last firing:

- active Event 65 form
- target grants per eligible leader
- existing countries inspected
- eligible leader roles found
- leaders changed
- total traits added
- rejected owned-trait collisions
- rejected Event 65 ledger collisions
- same-firing collisions
- unavailable-source rejections
- invalidated leader targets
- no-leader countries skipped
- saturated leaders
- near-saturated leaders
- technical application failures
- vanilla-origin traits added
- Chaos Redux-origin traits added
- ordinary traits added
- featured traits added
- registry count
- registry checksum or version
- direct or cluster firing source

The implementation may combine collision counters in ordinary player text.

Debug evidence must keep the detailed breakdown.

## Player-country result data

Each human country needs report-safe data for its active leader at the time of firing:

- whether the country had an eligible leader
- whether that leader changed
- registry index for each accepted trait slot, up to five
- actual number of traits added
- whether saturation prevented the full target count
- leader identity used for the grant
- active Event 65 form

The registry generator should emit the scripted localisation selector needed to turn a stored registry index into the source trait's localized display name.

The report must not expose raw source IDs or numeric registry indexes.

## Report content direction

The report title and description should present an unexplained global shift in the behavior and reputations of political leaders.

The viewpoint is international public reporting.

The cause remains unknown.

The text should use concrete observations such as changed habits, sudden convictions, odd public behavior, unexpected expertise, or conflicting reputations.

The tone is dry, direct, and mildly absurd.

The report should not become a joke list.

It should not claim that every leader became stronger or weaker.

It should not explain implementation, weights, source files, databases, or random-number logic.

It should avoid generic phrases about the world never being the same, the public watching closely, history taking a strange turn, or leaders approaching government and war differently.

## Report result block

The report should show:

- active Evolution name or baseline state
- number of traits assigned per eligible leader
- total leaders changed
- total traits added worldwide
- current complete pool size
- the local player's leader name
- the local player's accepted trait names
- a clear saturation note when the local leader received fewer than the stage target

The global report does not list every country's assigned traits.

The player can inspect foreign leaders normally.

## Option direction

The single acknowledgment option should sound like a short official reaction to an impossible personnel report.

A bureaucratic, resigned, skeptical, or dryly practical tone fits.

The final wording needs a focused localisation pass.

The option must remain short enough for the normal event window.

## Dynamic grammar

The report needs separate singular and plural handling for:

- one trait and several traits
- one leader and several leaders
- one skipped country and several skipped countries
- one remaining source trait and several remaining source traits

A leader receiving zero traits because of saturation must not use success wording.

A country with no eligible leader must receive a report state that explains the absence without claiming a mutation occurred.

## Trait-name display

Use the source trait's own localized name when available.

Use the Event 65 fallback mapping only when the source name is missing or not safe to render through the report selector.

Descriptions do not need to reproduce every source trait modifier.

The leader interface remains the authoritative place for source trait effects.

For multi-trait results, display one trait name per line.

Five names must fit without clipping at supported UI scale.

If the normal event description cannot fit the full list cleanly, put the list in the option tooltip while the description gives the global summary.

The localisation auditor must inspect the rendered result at every supported report length.

## Event picture

The report uses `GFX_report_event_leader_trait`.

The runtime file remains:

`gfx/event_pictures/065_random_trait/report_event_leader_trait.dds`

The final image is an opaque `210x176` report-event picture.

The intended scene is a fictional mid-century political press or conference setting with several anonymous leaders showing visibly different temperaments and roles.

The image should suggest incompatible identities without using text, interface symbols, or recognizable real people.

The treatment should match the existing Chaos Redux report-event documentary style.

The current repository asset must be validated before reuse because repository metadata reports an unusually small file size.

The asset prompt defines the full handoff.

## Event history

A successful Event 65 firing records one event-history entry.

The history row represents the global firing.

It does not create one history row per country.

The row should use the existing global or no-actor event-log presentation.

It must not attribute the event to a random country merely because a country scope was available.

The recorded data should include:

- event ID `65`
- firing date
- direct or cluster source
- active Event 65 form
- leaders changed
- traits added
- registry version
- result status

A firing that finds no eligible leader should record a clear zero-result status and must not claim a successful mutation.

## Event Details integration

The Event Details panel should explain the premise and repeat behavior.

It should show:

- global country-leader coverage
- complete country-leader trait pool direction
- cumulative stacking
- duplicate redraw rule
- baseline grant count
- each Evolution's grant count and weighting change
- current generated pool size
- cluster name and Medium severity after cluster registration is complete

The panel should not display the whole registry.

The generated manifest is documentation, not an in-game list.

## Evolution history

The first successful firing at each manifested Event 65 Evolution records that Evolution in the shared Evolution history.

A threshold becoming available does not create the record.

A disabled Evolution does not create the record.

A direct jump to Evolution III records Evolution III as the manifested result.

It does not create false firing records for Evolution I or Evolution II.

## Random-event registration

Event 65 remains in `global.repeatable_events`.

The implementation must preserve the shared repeatable behavior:

- initial active weight and cap from the common system
- cap reduction after firing
- monthly recovery
- active-pool selection
- event enable state
- shared minor-event timer behavior
- major-pool contribution
- one global pacing commitment per firing

Event 65 must not add a second weight, cooldown, or timer unless the shared framework requires a documented event-specific guard.

## Cluster entry path

The Randomizations cluster invokes the same Event 65 root.

A cluster wrapper must not call a second implementation of the trait logic.

Direct and cluster firings must produce identical trait behavior for the same Evolution, registry, seed, and eligible world state.

The firing-source difference is limited to logging, cluster participation, and shared pacing context.

## Direct Chaos timing

The direct Chaos milestone resolves only after the executor proves that at least one trait was added.

The report reads the committed result.

It does not create Chaos on acknowledgment.

The full milestone map is in Part 4.

## Debug controls

Event 65 needs bounded developer-only controls.

They should support:

- force baseline firing
- force Evolution I firing
- force Evolution II firing
- force Evolution III firing
- run through the direct path
- run through the Randomizations cluster path
- restrict the trait pool to a small declared test set
- force an owned-trait collision
- force an Event 65 ledger collision
- force a same-firing collision
- force a no-leader country
- force a near-saturated leader
- force a saturated leader
- print current registry count and checksum
- print result counters
- print the local player's stored registry indexes
- clear Event 65 test data from the designated test country
- run a multiplayer synchronization test without changing production weights

Debug controls must be restricted to the existing debug setting or test country pattern.

They must not appear in normal player decisions.

## Performance requirements

The event performs one bounded global pass when it fires.

It does not perform periodic world scans.

The maximum ordinary work is the number of eligible country-leader roles multiplied by the active trait count, up to five.

The complete pool can be large, so the selection method must avoid evaluating the full registry several times for every accepted slot when an exact generated hierarchy can reduce cost.

The final method must be profiled against:

- a 1936-style ordinary country count
- a late-game high-tag count
- full supported DLC
- a large Chaos Redux trait set
- Evolution III
- repeated firings with growing collision rates
- near-saturation debug data

The event must finish within the same synchronized execution sequence without a sustained game stall or multiplayer timeout.

The completion report should compare the reworked path with the current flat-list implementation or another reproducible baseline.

## Error behavior

A missing registry, stale generated pool, parser mismatch, invalid source index, or failed mandatory selector is a development error.

The event must not silently fall back to a small emergency list and still claim full coverage.

In a development build, the root should abort safely, record the exact blocker, and avoid partial world mutation when the pool is structurally invalid.

A single leader target becoming invalid during a valid firing does not abort the whole event.

It is counted and skipped.

## File ownership

The main implementation agent owns the event script, scripted effects, triggers, constants, generated-runtime integration, event log, Evolution wiring, cluster wiring, localisation wiring, `.gfx` wiring, documentation, workbook alignment, and validation.

The asset worker owns the source image, processed preview, DDS conversion, manifest, and handoff notes.

The probability auditor is read-only.

The completion auditor is read-only.

The localisation auditor may patch Event 65 text after inspection within the assigned scope.

The spreadsheet and documentation worker may update the authoritative workbook and permanent event documentation after implementation evidence exists.
