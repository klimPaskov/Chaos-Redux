# Event 31 Random Terror specification

## Part 13: Documentation, catalog alignment, and acceptance

## Source-of-truth location

The completed specification package belongs under:

`docs/specs/031_random_terror_specs/`

Implementation plans, subagent handoffs, audit follow-up notes, blocked reports, and completion reports belong under:

`docs/plans/031_random_terror_plans/`

The final event documentation should use an event-owned folder under `docs/events/` that matches current repository convention.

The implementation agent must inspect the live repository before choosing exact documentation filenames.

## Catalog alignment

The authoritative catalog source is:

`docs/spreadsheets/chaos_redux_events_catalog.xlsx`

The supplied CSVs are export-only snapshots.

They must not be edited directly.

After the workbook update, run:

`python .tools/export_event_catalog_csv.py`

The exporter should refresh the Events, Clusters, and Scenarios CSV snapshots.

## Event catalog row

Event 31 should contain player-facing fields aligned with final in-game wording.

### Identity fields

- ID: `31`
- Event Name: `Random Terror`
- Type: `Minor Repeatable`
- Status after completion: the repository's accepted implemented or playable status
- Chaos level: `1` where the workbook exposes it
- Cluster ID: blank until Internal Fracture is formally registered, then the verified cluster ID
- Member severity: severe after cluster registration

### Details direction

The detail should explain that several countries suffer fictional armed attacks in exact active states, governments manage a compact response, unresolved cells spread and organize, and severe failure can create coups, civil wars, territorial extremist countries, and international networks.

It should state that the later jihadist movement is fictional and that Muslim governments and communities can be among its main opponents.

It should not list raw modifiers, exact thresholds, hidden readiness, or the entity's true identity.

### Evolution fields

The workbook should use the accepted names and public premises:

- Organized Cells
- Transnational Terror Network
- Territorial Insurgency
- The Jihadist International
- The Final Jihad

### World-end field

Public title: The False Revelation.

The detail should explain that a united extremist movement accepts an ambiguous entity as divine and begins a terminal global conquest after substantial territorial and network success.

It must state that the game does not confirm the entity's identity.

### Scenario field

The Event row can reference Global Jihad and direct the player to the Triggerable Scenarios entry.

## Scenario catalog row

Global Jihad needs one authoritative Scenarios-sheet row after its ID is verified.

Required fields include:

- stable ID, proposed `SCN-014`
- scenario name
- owner Event 31
- public details
- type selector descriptions
- Low impact
- Medium impact
- High impact
- Maximum impact
- launch limitations
- Final Jihad behavior
- False Revelation gate behavior

The wording must match the scenario UI.

## Cluster catalog row

The proposed Internal Fracture cluster should not be added until its members are ready.

When approved, the authoritative Clusters sheet should include:

- verified ID, proposed `9`
- name
- public premise
- minimum Chaos tier
- member list
- Event 31 severe role
- member availability and skip behavior
- cluster firing and history behavior

Until then, Event 31's Cluster ID remains blank.

## Event registration and status

Implementation should register Event 31 in the repeatable-event array and add it to the reworked-event default enable allowlist only in the same change that delivers the complete playable event.

The event must resolve through the shared type and name selectors.

It should show a live weight when available and `N/A` only when no valid target exists.

A partially implemented event should remain disabled by default.

## Event log history

The automatic global firing records one history row.

The row should show:

- Event 31
- Minor Repeatable type
- date
- meaningful primary actor or global context
- the affected-country count
- the public incident stage when useful

Follow-up national incidents do not create false global pacing rows.

Territorial actor formation, major attack waves, the Jihadist International, the Final Jihad, and the world-end branch can receive event-owned reports or evolution records according to their role.

## Default actor mapping

The generic fired-event handler records history before the entry event's immediate block can create a new actor.

Implementation should prepare any needed primary actor or representative target through the shared pre-fire helper before history recording.

If no meaningful actor exists, the row should use a global event context instead of a stale target.

## Evolution log coverage

Every recorded evolution needs consistent display across:

- main Evolutions tab
- selected History details related evolutions
- Event Details evolution catalog
- selected evolution detail title and body
- actor flag and name when relevant

History surfaces show real index and date.

The Event Details catalog does not show fake history metadata.

Disabled evolutions do not set recorded flags or unlock content.

## Event Details content

The Event Details page should include:

- event identity
- type
- current enabled state
- current weight or `N/A`
- fired count
- concise public premise
- five evolution rows
- one public world-end row
- actor display when a meaningful territorial organization exists
- scenario reference only through the normal scenario system

The public premise should describe the event's current idea and progression.

It should not expose implementation history, hidden formulas, secret variants, Apocalyptic Readiness, or the entity's identity.

## Public world-end row

The False Revelation requires:

- stable registry identity
- Event 31 owner ID
- one row
- independent persistent toggle
- default enabled state
- premise and terminal-state details
- broad current status when useful
- automatic-selection gate tied to the toggle

Toggling the branch must not disable Event 31, its evolutions, or another event's world end.

## Triggerable Scenarios UI

Global Jihad should use the existing data-driven scenario window.

Required UI behavior:

- stable sort order
- row selection
- detail update
- scenario-specific type cycle
- four-stop intensity slider
- current impact text
- confirmation window
- cancel behavior
- launch button state using the same eligibility as the launch effect

The scenario does not need dedicated art unless the current scenario UI cannot present its details.

A required technical sprite can use the established UI pattern, but a placeholder must be reported until replaced.

## Event documentation

The event documentation should explain:

- event identity and classification
- core values
- state activity stages
- targeting principles
- incident families
- response category and missions
- baseline territorial escalation
- five evolutions
- country package and focus framework
- Global Jihad scenario
- The False Revelation
- interactions with Event 14 and shared systems
- Deaths and Condemnation integration
- asset inventory
- AI and balance model
- achievement package
- debug and acceptance scenarios
- future cluster role

Player-facing documentation should not expose hidden route conditions or implementation-only variable names.

Technical docs can record stable identifiers, inputs, outputs, cleanup, and validation.

## System documentation updates

Implementation should update the owning documentation for:

- world-threat source registry
- special Chaos country classification
- country-carrier consumption
- scenario registry
- event log evolution and Event Details coverage
- Deaths reasons
- Condemnation source mapping
- event-owned state map mode
- any reusable dynamic effect or trigger created for several systems

A helper used only inside Event 31 belongs in Event 31 documentation.

It should not be added to the public dynamic helper registry merely because several Event 31 files call it.

## Technical identity proposals

The following identifiers are accepted working identities and need collision verification in the live repository.

- entry event: `chaosx.nr31.1`
- event actor marker: `random_terror_actor`
- takeover marker: `random_terror_takeover_country`
- ordinary crisis marker: `random_terror_crisis_active`
- world-threat source: `world_threat_source_random_terror`
- scenario ID: `SCN-014`
- future cluster ID: `9`
- world-end flag family: Event 31 False Revelation specific
- state map mode: Event 31 active-state map mode

The implementation agent can refine internal names to match repository style.

Public names, IDs, scenario title, evolution names, and world-end title remain stable unless a collision or research gate requires a reported change.

## Required implementation audits

### Repository exploration

Map the existing Event 31 placeholder, event registration, event log, scenario registry, carrier registry, country collections, special-country trigger, world-threat aggregate, state map modes, decisions, focus-tree loading, achievement registry, assets, super-event slots, sound registry, and docs.

### Event-chain MCP pass

Use event inspection and rendering before edits, then compare the final chain.

The pass should cover entry, national incidents, evolutions, territorial creation, scenario launch, and world-end transition.

### Decision and mission audit

Check:

- action count
- cost variety
- four-cost limit
- mission count
- target validity
- AI
- cleanup
- exploit protection
- dynamic text
- category presentation

### Focus-tree audit

Check:

- route coverage
- first-glance branch clarity
- layout
- prerequisites
- mutual exclusions
- search filters
- Focus Navigation
- AI
- idea lifecycles
- icons
- decision integration

### Country-package audit

Check:

- carrier
- territory
- capital
- leader
- flag
- parties
- ideas
- forces
- technology
- supply
- focus loading
- AI
- merger
- split
- defeat cleanup

### Localisation audit

Check every event, decision, mission, focus, idea, character, country, flag identity, achievement, Event Details row, evolution row, scenario row, world-end row, and scripted value.

### Probability audit

Use the named scenarios in Part 9 for target selection, incident pools, response choices, route AI, evolution pacing, territorial creation, scenario AI, and world-end readiness.

### Event completion audit

Compare every spec part, matrix, prompt, asset manifest, research handoff, and accepted improvement addendum with the final repository.

## Required implementation validation scenarios

### V01 Baseline containment

A stable country receives one attack, uses intelligence and victim support, clears the state, and closes the category.

### V02 Coercive recurrence

A country uses rapid coercion, clears the first cell, loses legitimacy, and receives a stronger later recurrence.

### V03 Cross-state spread

A failed raid displaces survivors into a valid neighboring state after the cooldown.

### V04 Transnational network

One organization connects several countries through a safe haven and corridor, then loses the corridor through joint action.

### V05 Territorial creation

A valid actor seizes connected territory, receives a complete country package, and fights the parent.

### V06 Parent viability

A small country reaches severe pressure without producing an invalid zero-state or capital-less parent.

### V07 Government takeover

An actor captures the government and transforms the country without duplicating units or leaving stale response content.

### V08 Actor defeat

The parent defeats the actor, restores authority, clears the carrier, and preserves history and Deaths.

### V09 Cannibal rivalry

Event 31 and Event 14 actors share a border, remain unable to ally, and fight according to practical AI priorities.

### V10 Evolution disable

Each disabled evolution leaves baseline progression playable and does not set its recorded state.

### V11 Jihadist representation

Evolution IV creates a fictional movement, Muslim opposition content activates, and ordinary target scores remain identity-neutral.

### V12 Global Jihad intensities

Low, Medium, High, and Maximum create distinct valid setups.

### V13 Scenario cancellation and failure

Cancel changes nothing and a failed setup validation leaves no partial state.

### V14 Final Jihad

Existing networks coordinate uprisings using real prior pressure and actors merge or subordinate safely.

### V15 False Revelation blocked

The branch remains blocked below `1000` Chaos, when disabled, or without territorial proof.

### V16 False Revelation transition

The branch sets one terminal state, assigns the entity, triggers valid uprisings, and freezes ordinary events.

### V17 World-end counterplay

Coalition action against capitals, corridors, unity, and high-pressure countries weakens final abilities.

### V18 Defeat aftermath

The final state is defeated and the aftermath, reconstruction, second super-event, and cleanup function.

### V19 Save and reload

Ordinary crisis, territorial actor, scenario, evolution, and world-end state survive save and reload.

### V20 Multiplayer

Several player countries receive one global firing without duplicate effects, and a player actor is not silently absorbed.

## Asset acceptance

The implementation must reconcile every accepted asset row with a final runtime consumer.

No required flag, portrait, icon, category picture, report image, news image, super-event image, animation fallback, achievement triplet, or audio cue can remain a placeholder in a completion claim.

The final asset manifest should show source, processing, final path, sprite, consumer, review, and hash.

## Documentation and temporary workspace cleanup

During implementation, event assets can use:

`docs/assets/031_random_terror/`

Before full completion:

- durable provenance, licensing, review, and crosswalk facts move into permanent docs
- final runtime files move into engine folders
- no runtime path points into the temporary workspace
- the temporary event workspace is deleted
- the durable portrait source archive remains

A missing temporary folder after proper cleanup is expected.

## Git and completion report

After each complete implementation plan, create a focused Git commit.

The final completion report should list:

- files changed
- event chain and registration
- decisions and missions
- evolutions
- country packages
- focus routes
- AI and probability evidence
- assets and audio
- achievements
- scenario
- world end and aftermath
- shared-system integrations
- docs and workbook updates
- meaningful validation findings
- unresolved blockers
- simplifications or fallbacks

No completion claim is valid while an accepted route, asset, AI surface, evolution, scenario intensity, achievement, world-end component, documentation row, or audit remains missing.

## Simplification reporting

The final implementation must report every deviation from this specification.

This includes:

- merged or removed decisions
- reduced country count
- reused portraits or flags
- missing focus routes
- missing AI
- missing animation
- missing audio
- unavailable carrier
- reduced scenario intensity
- weaker world-end ability
- hidden placeholder
- unvalidated probability
- stale documentation

The planning package itself uses no unapproved fallback or quick-output truncation.

Its deliberate exclusions are the custom unit family, 3D model package, and dedicated scripted GUI because the accepted design is stronger and cleaner with existing units and normal decision surfaces.

## Final acceptance statement

Event 31 is complete only when a normal automatic firing can progress through containment or territorial crisis, every evolution works and can be disabled safely, created countries are fully playable, Global Jihad supports all four intensities, The False Revelation meets the terminal contract, AI and assets are complete, shared systems agree, and the final repository passes the required audits without an unreported simplification.
