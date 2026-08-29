# Murder Mystery Specification Part 18: Acceptance, Validation, and Completion Contract

## Completion definition

Event 39 is complete only when baseline investigation, all five evolutions, the international network, safe character handling, Assassin State country package, focus tree, decision systems, custom unit family, foreign derivatives, manual scenario, Intelligence cluster, World of Anarchy, super-events, assets, achievements, AI, catalog alignment, documentation, and cleanup are implemented and validated as one system.

A working opening event does not count as a completed rework. A functional Assassin State without safe investigation and character handling also does not count.

## Required implementation tranches

### Tranche 1: Registry and ownership preflight

- reserve event IDs, tag carriers, cosmetic identities, scenario ID, cluster ID, super-event slots, audio IDs, provider ID, equipment profile IDs, and achievement IDs
- audit every candidate character and successor
- audit country carrier collisions and dynamic-country ownership
- inspect live event, focus, decision, tech, asset, counter, 3D, and super-event precedents
- establish source-of-truth docs and constants

Exit condition: no unresolved identifier collision and no opening host without a verified safe succession row.

### Tranche 2: Baseline investigation

- implement host selection and opening transaction
- implement public values and category
- implement protection, missions, incidents, and capture
- implement event logs, news, reports, Chaos map, and cleanup
- implement La Résistance and non-DLC paths

Exit condition: baseline can start, progress, succeed, fail, save, reload, and resolve permanently without character or roster damage.

### Tranche 3: Evolution I and II

- implement Murder Cult behavior
- implement active-cell registry and foreign investigations
- implement evidence sharing, local dismantling, immunity, and movement inheritance
- implement evolution logs and catalog presentation

Exit condition: a bounded international network can spread, be contained, and end globally without world scans or stale rows.

### Tranche 4: Assassin State

- implement validated state split and rollback
- implement country package, war, focus tree, decisions, AI, flags, portraits, units, technology, equipment, 3D, counters, and audio
- implement defeat, host victory, movement inheritance, and cleanup

Exit condition: both sides are viable, the country is playable, no placeholder asset remains, and the complete unit provider passes Event 19 and CXT audits.

### Tranche 5: Evolution IV, derivatives, and faction

- implement foreign revolt preflight and reduced country package
- implement subjects, Veiled Compact, central support, autonomy, defection, and inheritance
- implement bounded derivative capacity

Exit condition: several foreign derivatives can coexist, fight, receive support, defect, inherit once, and clean up safely.

### Tranche 6: Evolution V and World of Anarchy

- implement command settlement and terminal route
- implement terminal registry, sectors, wars, leadership pressure, government dismantling, administrations, victory, defeat, and postwar content
- implement all terminal presentation and shared world-end integration

Exit condition: terminal activation, victory, and defeat are reachable and performant, protected actors survive correctly, and post-victory play continues.

### Tranche 7: Scenario, cluster, achievements, docs, and final audit

- register Assassin Network and all intensities
- activate Intelligence cluster and member row
- implement achievements and icons
- update authoritative workbooks and regenerate CSV exports
- complete documentation, provenance, catalogues, and acceptance evidence
- run final completion and improvement audits

Exit condition: every accepted spec row has an implementation disposition and no unresolved fallback remains.

## Functional scenario matrix

### Baseline cases

- stable major with strong agency captures before a second murder
- weak wartime major reaches Murder Cult but can still recover
- player-controlled nonmajor passes all host and split gates
- candidate with unsafe leader succession is excluded
- event has no eligible host and safely returns to selection without partial state
- no La Résistance path remains complete
- save and reload during every investigation phase

### Character cases

- named national leader opening succession
- later named commander murder with minimum roster preserved
- advisor protected by another focus or event is excluded
- no safe named target falls back to generic office casualty
- failed protected-target attack produces evidence and no deletion
- repeated incident cannot target an already removed character
- imported or special-event character remains protected

### Evolution cases

- each evolution activates after threshold and real readiness
- each evolution remains absent when disabled
- prefire high-Chaos opening stages content without popup flood
- capture before Evolution II ends chain
- capture after Evolution II triggers correct inheritance test
- Evolution III waits for valid split
- Evolution IV creates only validated derivatives
- Evolution V reveals terminal content but does not auto-activate it

### Country cases

- compact host with normal valid split
- host capital preserved
- host capital must relocate before transfer
- coastal and landlocked Assassin State packages
- small and large host scaling
- original government remains viable
- carrier reservation failure rolls back
- capital loss triggers valid relocation
- original host wins
- Assassin State wins
- central state dies and one derivative inherits
- central state dies with no viable heir

### Unit cases

- every custom profile trains and reinforces from real stockpiles
- operations-kit production and shortage are visible
- caps work and survive reload
- AI maintains a mixed army
- Mechanized Assassins require fuel and equipment
- Master Assassins remain cap limited
- low hit points and heavy-combat weaknesses create counterplay
- Event 19 provider registers once with all callbacks
- Event 19 derivative does not activate Event 39
- CXT coverage includes every concrete sub-unit and equipment token
- 3D models and animations reimport and bind to live entities
- unit audio and counters match runtime consumers

### International cases

- cell seeding uses a concrete route
- strong secondary country dismantles a cell
- weak secondary country loses an office but retains viable government
- evidence sharing helps several countries
- compromised member creates a bounded leak
- immunity blocks ordinary reseeding
- stage 4 revolt succeeds with valid territory
- revolt is prevented by government action
- derivative cap blocks new country cleanly
- annexed or transformed country row retires

### Scenario cases

- Low, Medium, High, and Maximum setup matches the accepted intensity
- current eligible player country can be chosen as host
- invalid player country falls back to valid selection
- cancel changes nothing
- confirmation reads current intensity and host
- bypass flags clear after setup
- scenario does not fabricate natural history
- duplicate launch is blocked
- World of Anarchy still uses normal terminal gate

### World-end cases

- branch toggle blocks activation without disabling Event 39
- incompatible world end blocks activation
- activation rollback clears partial state
- sector fanout remains bounded
- special Chaos and nonhuman countries are exempt
- ordinary government leadership uses safe dispositions
- conquered country receives viable administration
- no instant universal cores
- victory registry updates through hooks
- central command contradiction affects play
- movement victory continues as a playable state
- movement defeat restores or settles countries safely
- defeat super-event fires only after scale gate

## Visual and localisation audit

Verify:

- no pink or missing textures
- event, report, news, category, focus, idea, decision, unit, tech, flag, portrait, achievement, counter, 3D, and super-event art use the correct consumer
- icons remain readable at native size
- alpha-backed assets have no matte or square background
- animation has stable frames, correct sheet, loop, static fallback, and supported consumer
- flags have normal, medium, and small variants
- portraits use allowed fictional source mode
- no generated text appears in art
- no Nizari, religious, ethnic, or generic ninja stereotype appears
- no raw localisation key, clipped text, excessive decimal, or hidden implementation detail appears
- event log, Event Details, evolution rows, scenario details, cluster details, and terminal row agree

## AI and probability audit

Every complex weight must complete the probability workflow in Part 13. The audit report should include inputs, tool route, scenario result, expected ordering, anomalies, changes, and residual limits.

No route, decision, target, or event should be accepted solely from source inspection when the required MCP route is available.

## Focus and technology audit

The focus tree must pass first-glance branch review, route coverage, prerequisite semantics, layout, filters, navigation, hidden route, AI, decision integration, spirit lifecycle, and payoff tests.

The technology branch must pass graph inspection, asset coverage, prerequisites, unit and equipment unlock, AI research, and no-orphan checks.

## Decision and mission audit

The decision auditor should verify action quality, costs, four-cost maximum, mission objectives, duration, success and failure, target selection, cleanup, duplicate missions, route integration, AI, exploitation, and visible impact.

A large category full of small political-power purchases fails even if its syntax works.

## Country package audit

The country auditor should verify carrier safety, territory, capital, cores, claims, history, parties, leader, portrait, laws, technology, research slots, stockpiles, production, units, commanders, agency, focus, decisions, AI, flags, cosmetic names, subjects, faction, DLC branches, war, defeat, inheritance, and cleanup.

## 3D acceptance

For every required model job, preserve one approved input image, provider task lineage, source downloads, Blender checkpoints, textures, rigs, actions, parser or reimport evidence, runtime paths, and live entity bindings. Reject transform-only or static-alias animations.

Audio needs identifiable source, license, original file, final conversion, runtime ID, and synchronization notes. Missing or unsuitable audio remains blocked.

## Super-event acceptance

Each accepted super-event needs one unique slot, aligned role, final title, description, button, verified quote, full-scene image, unique licensed musical WAV, sound definitions, settings wrappers, playback, catalogue entry, docs, and live test. No element can be borrowed from another slot as a completion shortcut.

## Achievement acceptance

Every achievement needs exact scope, conditions, irreversible disqualifiers, scenario policy, tracking, localisation, normal, grey, and not-eligible icons, and live unlock testing. No debug or current-state shortcut may unlock an achievement.

## Documentation and catalog acceptance

The authoritative XLSX workbooks remain the only editable catalog source. Implementation must update them through the spreadsheet worker, regenerate CSV exports, and keep docs, event settings, Event Logs, scenario registry, cluster registry, super-event catalog, unit registry, CXT inventory, 3D docs, and achievements aligned.

The documentation curator should review the final package for stale paths, orphan docs, copied planning notes, wrong status, and source-of-truth conflicts.

## Specialist-role review

The final integration should receive the relevant narrow reviews:

- repository exploration before implementation
- scripted-system architecture
- AI probability
- country package
- decision and mission
- focus tree
- event UI if a new UI surface is later accepted
- localisation
- asset source research
- generated event art
- icon art
- portrait production
- 3D model pipeline
- super-event text and audio research
- documentation curation
- event completion audit
- improvement-loop anti-bloat review

The parent implementation agent owns integration and must review all returned work.

## Debug-playtest boundary

The autonomous debug-playtest skill is explicit-invocation only. This specification does not authorize autonomous desktop control or a live HOI4 debug session. Normal implementation validation should use source checks, MCP inspection, repository validators, and targeted manual test instructions. Live autonomous testing begins only after the user explicitly invokes that skill and the environment passes its capability gate.

## Hard blockers

Do not claim completion when any of these remain:

- unsafe or unregistered character removal
- host without verified succession
- carrier or super-event slot collision
- invalid state split or derivative package
- empty country or army package
- missing Event 19 callback or CXT registration
- missing final asset, portrait, flag variant, counter, model, animation, audio, or super-event element
- unverified quote or unclear audio license
- custom unit with no production or counterplay
- world scan used for normal cell or terminal processing
- stale scenario bypass
- duplicate history or evolution record
- unvalidated complex AI weight
- catalog workbook and CSV export mismatch
- placeholder, generic substitution, or undocumented simplification

## Final completion report

The implementation report should state:

- files changed
- identifiers and registries added
- source specs used
- baseline, evolution, country, unit, scenario, cluster, terminal, asset, achievement, AI, and cleanup status
- MCP evidence
- probability scenarios
- focus and technology renders
- model, animation, audio, and asset manifests
- catalog and documentation updates
- tests performed
- unresolved blockers
- explicit simplifications or fallbacks, which require user approval

The event should be marked complete only when every accepted specification requirement has an implemented or explicitly user-approved disposition.
