# Event 19 Infantry Spawn
## Part 8: Triggerable scenario, cross-event integration, presentation, and acceptance

> **Current UI and status boundary (2026-08-22):** This part preserves accepted scenario and presentation design. Former Muster Board and GUI asset references are archival provenance only. The live scenario is `SCN-013`, and the player-facing Event 19 surface is decisions-only with no scripted GUI.

## Triggerable scenario

### Registry identity

- **Approved scenario ID:** `SCN-013`
- **Final player-facing label:** The Unbidden Muster
- **Catalog relationship:** first collision-free identity after live IDs 1 through 11 and Event 20's raw ID 12 reservation

The shared name-sort value is `5.75`, placing The Unbidden Muster after The Hunger Lines and before The World in Fury. The generic Triggerable Scenarios window supplies its dynamic row, four-stop intensity control, type arrows, launch button, and confirmation flow.

### Scenario promise

The scenario creates an immediate world military crisis. Countries receive large event formation packages and those formations revolt or attempt takeover at once. Wars begin as part of setup rather than after a long claimant-management phase.

The scenario is a sandbox or challenge launch. It is separate from automatic Event 19 eligibility, chaos, evolution timing, date, and prior event history.

Each ordinary actor commits the full country-entry state required by its selected package as a minimum profile: I-II for Conventional Flood and Arsenal Lottery, I-III for General Mutiny, and I-IV for Anomalous Rising. A fresh actor keeps exactly that profile. A pre-existing same-tag Event 19 participant keeps any fully applied higher stage so setup does not destroy live claimant, registry, or management transactions. Once marked as a scenario actor, its proved applied set is frozen against later global evolution activation. Nonhuman and claimant derivatives instead keep their private derivative package and no ordinary applied-stage surface.

### Launch gates

The scenario can be launched whenever:

- no terminal world-end state makes launch invalid
- the game has at least one country and valid controlled state
- required dynamic country creation or takeover paths can be built

It must not require:

- Event 19 to have fired
- Evolution III or IV to be naturally active
- a minimum chaos value
- a date gate
- a claimant already existing
- a parent zombie, Death, or golem event

A tightly scoped scenario launch flag forces the required generation and revolt logic. It is cleared after setup.

## Scenario types

All names are working labels, not final localisation.

### Conventional Flood

Content:

- ordinary baseline, Evolution I, and Evolution II families
- many formations
- immediate military mutinies or claimant breakaways
- no anomalous families

Player experience:

- large conventional civil wars
- supply collapse and command fragmentation

### Arsenal Lottery

Content:

- serious and strange Evolution II formations
- armor, mechanized, motorized, armored cars, amphibious, and valid helicopter lots
- immediate revolts

Player experience:

- uneven wars where some rebels have powerful unsupported equipment and others have narrow curiosities

### General Mutiny

Content:

- Evolution III random composition
- claimant generals assigned immediately
- every affected country gets a claimant crisis or takeover attempt

Player experience:

- personalized military revolts with frightening commanders

### Anomalous Rising

Content:

- Evolution IV registered families
- high saturation
- derivative zombie, ghost, golem, or future eligible revolts
- parent-event isolation remains active

Player experience:

- immediate nonhuman regional wars without firing parent event chains

## Scenario intensity

The scenario uses the standard four-stop intensity slider.

### Low

- lower state coverage
- one principal revolt per selected country group
- fewer units per state
- stronger takeover preference for microstates
- limited anomalous family count

### Medium

- broad state coverage
- several formation lots
- ordinary immediate revolt strength
- claimant and derivative selection follows local context

### High

- high state coverage
- multiple units per selected state
- larger random and advanced pools
- more countries experience simultaneous revolt
- higher chance of rival claimant fronts

### Maximum

- maximum safe state coverage under the diminishing model
- many units and lots
- immediate revolt or takeover in nearly every valid country
- rival claimants or multiple family crises where safe
- aggressive war setup beyond the former parent where regional targets exist

Maximum does not set the global `world_end` flag. It is an extreme ongoing campaign scenario, not a terminal state.

## Immediate revolt setup

### Multi-state countries

The scenario builds one or more coherent revolt regions from selected states, claimant districts, depots, and unit placement.

### One-state countries

The scenario uses:

- claimant takeover
- government replacement
- aggressive external war plan

It does not attempt to split the only state.

### Tiny and island countries

The scenario uses takeover or one coherent local revolt. It does not create stranded micro-rebels with no army or transport.

### Existing civil wars

The scenario should avoid invalid nested civil wars. Depending on engine-safe precedent, it can:

- add a claimant faction to an existing side
- create an additional dynamic country when safe
- trigger a takeover inside one side
- defer one local revolt and compensate with stronger units elsewhere

The implementation must choose a verified pattern rather than assume nested civil-war syntax is safe.

### Immediate diplomacy

Revolt countries begin at war with former parents. At High and Maximum, they can receive aggressive regional war plans or direct wars against adjacent valid targets.

They should not receive impossible overseas wars without access.

## Scenario UI direction

The scenario row should explain the visible premise and the differences among types and intensity. It should not reveal implementation flags, parent isolation, or exact probability formulas.

The confirmation window reads selected type and intensity at launch time.

The scenario can reuse the existing Triggerable Scenarios UI. Dedicated art is not required unless the current window cannot present the type and intensity text clearly.

## Event cluster position

Event 19 remains unclustered in this source design.

Reason:

- no existing catalog cluster has a clear thematic and mechanical fit
- a one-member cluster would add no meaningful interaction
- Event 56 Navy, Event 127 Warlords, Event 131 Widespread Mutiny, and related military events are not yet all confirmed reworked and compatible (Event 96 Division Lock has a live marker contract, below)

A future working cluster concept could be a sudden mobilization or command-collapse cluster, but it should be created only after at least two or three member events have complete behavior, ordered roles, and safe shared runtime context.

## Cross-event integration

## Event 2: Zombie Outbreak

Required integration:

- base `zombies` remains the only trainable zombie body; its provider 501 keeps the derivative route
- derivative zombie countries use distinct origin and identity
- parent zombie counts, leagues, mutations, stages, evolutions, super-events, and world-end conditions exclude Event 19 derivatives
- if the parent event is active, Event 19 can react through visible containment or hostility decisions without claiming the derivative is the parent outbreak
- the owner-approved provider 511 may supply its recorded mutation and armour variants as spawn-only, family-only lots; it has no derivative profile and grants neither zombie training nor parent mutation progression
- unregistered or unapproved variants remain unavailable; the exact variant inventory stays in the [owner coverage ledger](../../../events/019_infantry_spawn/systems/unit_family_coverage.md) and Part 5 rather than another list here

Potential interaction:

A parent zombie country can view a derivative as a rival, prey, failed offshoot, or recruitment target through future content. This is optional and must not be required for Event 19 completion.

## Event 10: Death

Required integration:

- ghost derivative does not use the Death tag, original tag identity, or parent flag
- slow derivative wasteland and population effects do not enter parent consumed-state or soul counts
- parent Death super-events and world-end progression remain isolated
- shared Deaths tracking records real population loss once, without Event 19 adding duplicate death totals

Potential interaction:

Death can react to derivative ghosts through a future rivalry or absorption event. It is not part of this required package.

## Golem parent event or system

Required integration:

- verify current local identifiers before implementation
- derivative golems remain weaker and spawn-only
- no parent stage, super-event, or world-end flags are set
- material and quarry mechanics use reusable helpers only where they do not advance the parent event

The installed golem body is `coal_golem`; it is registered as spawn-only provider 503 (Part 5) and stays isolated from the parent golem package.

## Event 56: Navy Spawn

The Event 56 package is `docs/specs/056_the_navy_specs/`.

Interaction direction:

- avoid duplicating the same random-generation architecture independently where a reusable formation registry or request framework can serve land and future naval systems
- do not let land event templates create naval units
- a future cluster can connect simultaneous land and naval manifestation only after Event 56 is reworked

## Event 67: Generalissimo

Live implementation: the Event 67 bridge exists (two extra demand codes, subordinate commission and parallel command); see `docs/events/019_infantry_spawn/overview.md`.

Interaction direction:

- a country with an existing supreme leader or generalissimo needs claimant demand variations
- claimant appointment can conflict with the existing command office
- the event should prefer rivalry, co-option, duel of authority, or subordinate command instead of blindly replacing the leader
- leader and country changes must respect the Generalissimo event’s ownership flags

## Event 96: Division Lock

Live implementation: Event 96 owns the shared `division_template_lock_event_active` marker, and Event 19 pauses management and conversion transactions while it is set.

Interaction direction:

- event-owned audit locks must remain distinguishable from Event 96’s division lock mechanics
- Event 19 cleanup must not permanently trap divisions after a generation closes
- Event 96 should not remove Event 19 accounting or enable equipment farming

## Event 127: Warlords

No specification package exists for Event 127 yet, so these rows stay design direction until its owner package defines a bridge.

Interaction direction:

- do not create duplicate regional breakaways from the same state and unit base
- a claimant can become a warlord actor only through an explicit bridge
- Warlords pressure can raise claimant influence or lower control
- Event 19 derivative countries keep distinct family identity

## Event 131: Widespread Mutiny

No specification package exists for Event 131 yet.
The Famine and Migration package records that Event 131 needs an actual military ration conflict, so civilian famine alone never forces a mutiny; Event 19 formations add no ration conflict of their own.

Interaction direction:

- mutiny pressure can increase claimant revolt risk
- Event 19 loyalty records determine which formations defect
- the two events must not each transfer the same units
- if both fire together, one system owns the actual revolt and the other records or modifies it through a shared bridge

## Civil war and coup systems

Event 019 owns a revolt whose defining cause is its recorded formations, claimant, or registered family.
Event 021 owns a distinct domestic political fracture under its [specialized-event precedence](../../021_random_civil_war_specs/021_random_civil_war_overlap_and_catalog_reconciliation.md#specialized-event-precedence).
When both plans touch the same host, a pending Event 019 release has priority over its frozen region and recorded formations; Event 021 must select another viable opening or leave that opening uncommitted.
It cannot create a second actor from the same district or treat the same loyal formations as ordinary defections.
The receiving player's existing containment, reassignment, negotiation, and demobilization choices therefore determine whether the formation crisis remains a live competing claim.

Ordinary managed Event 019 lots alone do not give the host blanket immunity from Event 021.
A separate political opening may proceed only through an accepted integration that preserves actual formation identity, equipment obligations, generation ownership, and pending transactions across the resulting actor and state changes.
A native army ratio or territory transfer is not proof that those Event 019 records transferred correctly.
Without that proof, the combined opening remains unresolved and must not substitute a new free army, settle debt, or reroll the old lots.

AI uses the same ownership and viability checks: it cannot plan two releases against one frozen formation base, and it rechecks political eligibility under Event 021's normal cooldown, grace, and viability rules after the specialized transaction resolves.
One-state takeover, former-parent context, annexation cleanup, and negotiated settlement retain their existing Event 019 rules.
Wars and deaths still reach their shared owners once; the connection adds no separate Chaos reward.

## Chaos Meter

Event 19 contributes chaos only through meaningful event outcomes that are not already counted by shared systems.

Live state (spec audit 2026-10-10): Event 19 adds no direct Chaos Meter amount.
Its wars reach the meter through the native `on_war_relation_added` hook, and a claimant takeover that changes the ruling party reaches it through `on_ruling_party_change` and `chaos_meter_on_ideology_change`, both in `common/on_actions/chaosx_on_actions_chaos_meter.txt`.
The Chaos Meter tier range also feeds the evolution score (Part 3), so the event reads the meter more than it writes to it.
A claimant takeover is applied with `set_politics` and fires no native coup hook, so the shared `chaos_meter_on_coup_succeeded` helper is not called; whether a military takeover should also count as a coup is listed under Open questions in the package README.

Outcomes that no shared hook counts, and therefore the only candidates for a direct contribution:

- major claimant revolt
- derivative nonhuman revolt
- mass command collapse
- scenario launch

Do not add duplicate chaos for:

- wars already counted by the shared war system
- deaths already counted by the shared Deaths system
- annexations or puppets already counted elsewhere

## Deaths system

The event does not create immediate civilian deaths simply by spawning ordinary units.

Deaths can arise from:

- combat
- ghost derivative population drain
- family-specific violent incidents
- claimant repression or revolt where designed

All real population reduction uses the shared death pipeline and is not double-counted.

## Famine and Migration

Event 19 adds no famine, displacement, or refugee amount of its own.
The Famine and Migration package already lists Event 019 custom forces among sources that can create displacement through actual battles, control change, and occupation, and states that custom-force identity alone supplies no danger or civilian amount.
Derivative wars and revolt territory therefore reach those systems only through the shared state-level owners, with no Event 19 adapter.

## World threat framework

Derivative states are dangerous but do not automatically set `world_in_threat`.

A future threshold can register a derivative source when a family becomes a genuine global external threat. This is outside the normal event package and should use the shared source-count framework rather than a new one-off global flag.

## Event Log integration

### Event history

The global firing records Event 19 once through the normal repeatable history pipeline.

Because every valid country can be affected, the row can use a global or no-actor presentation rather than choosing one arbitrary country.

### Evolution history

Record four evolution stages:

1. organized muster
2. arsenal lottery
3. command fracture
4. anomalous muster

These are working design labels, not final localisation.

Each evolution is recorded once globally with the correct Event 19 ID, type, stage, tier, and enabled-state handling.

### Country follow-up history

Claimant appearance, takeover, military revolt, derivative release, derivative defeat, and the four first-family reception outcomes are normal follow-up history events. They are not additional evolution stages. First-family cantonment, negotiated reception, refusal, and failed reception use stable Event 19 payloads while the visible reception event uses the frozen provider's identity and host scene.

### Event Details evolution catalog

The Event Details preview should show four evolution entries without fake dates or history indices.

Text direction should explain how the event’s pattern changes without exposing exact random formulas or secret revolt thresholds.

## Default enable state

Event 19 is in the reworked-event default-enabled allowlist (`event_log_event_is_reworked_default_enabled` in `common/scripted_triggers/chaosx_settings_triggers.txt`, through `constant:infantry_spawn_event.id`).

## Player-facing text direction

## Event title direction

Use a short title about formations appearing or assembling across the country. Avoid generic apocalypse language and avoid a technical military-administration label.

## Entry description direction

Show concrete local military scenes:

- recruits and veterans arriving together
- equipment unloaded without matching records
- horses, trucks, guns, or stranger machines occupying public space
- officers presenting incompatible orders
- communities discovering that a local formation already considers itself permanent

Keep the cause unexplained.

## Option direction

Use one concise reaction from the receiving state. Minor absurdity or grim administrative disbelief is suitable. Avoid bland approval and avoid jokes about real historical child mobilization or atrocities.

## Evolution directions

### Evolution I

Show that the formations are more coherent, better supplied, and harder to dismiss.

### Evolution II

Show serious combined-arms forces and equipment that should not exist in the receiving country.

### Evolution III

Show that governments can call for formations but cannot control what composition or commander answers.

### Evolution IV

Show anomalous units entering military service and creating family-specific fear, containment, or fascination.

## Claimant text direction

Claimants should sound and look personally dangerous. Their demands must be specific to troops, depots, districts, victories, and offices. Avoid generic villain speeches.

Regional names, military idioms, and political forms should vary by country. Final wording needs localisation research and regional name pools.

## Derivative country text direction

Public text should describe what the derivative visibly does and how it organizes itself. It must not tell the player that the country is a weaker copy of a parent event.

## Event Details direction

Describe the recurring phenomenon and its visible uncertainty. Do not list gameplay effects, exact state-coverage curves, random battalion limits, claimant thresholds, achievements, or hidden derivative outcomes.

## Asset coverage summary

The full inventory appears in `matrices/019_asset_inventory.md` and the asset handoff in `prompts/019_infantry_spawn_asset_prompt.md`.

Required major asset families:

- baseline and evolution report images
- decision category icon
- decision icons
- idea and national spirit icons
- former Muster Board panel and state icons (archival provenance only; no runtime consumer)
- three former animated UI packages with static fallbacks (archival provenance only; no runtime consumer)
- 20 fixed claimant portrait-slot assets displaying distinct regional army/muster scenes with no individual focal person
- derivative country flags
- six fixed derivative portrait-slot assets displaying massed zombie, ghost, or golem hosts; councils use exactly three formations/cohorts
- one identity-neutral technical muster scene for unresolved UI and unknown-provider display states; it assigns no gameplay identity
- direct-scenario provisional authorities use those army/muster and massed-host scenes; no SCN-013 government identity uses a focal human or generic unknown portrait
- derivative focus icon family
- derivative decision and idea icons
- achievement icons

No super-event image or audio package is required.

## Documentation and catalog alignment

Implementation must update:

- one canonical Event 19 document under `docs/events/019_infantry_spawn/overview.md`
- event name and Event Details localisation
- event history and evolution display selectors
- triggerable scenario system documentation
- dynamic helper documentation
- Chaos unit registry documentation
- shared classifier documentation
- asset manifest and GFX handoff
- achievement documentation
- event catalog workbook row for Event 19
- scenario catalog workbook row for SCN-013 if the workbook includes scenario entries

The spreadsheet mirror fields must use final in-game wording rather than this planning language.

## Implementation acceptance map

The implementation is not complete unless every item below is finished or explicitly blocked and reported.

### Core event

- repeatable global registration remains correct
- diminishing territorial coverage works
- larger countries receive more absolute formations
- state weighting changes formation identity
- lot and generation data exist
- repeated unresolved generations stack pressure

### Baseline

- at least six formation families
- audit, integration, territorial role, standardization, and demobilization
- equipment and manpower accounting
- AI handling
- real-effect incidents

### Evolution I

- better training and equipment
- stronger coherent templates
- muster districts and staff organization
- active-event and pre-fire paths

### Evolution II

- multiple units per selected state
- advanced and strange serious formations
- technology-locked finite equipment
- on-demand random requests
- supply, training, command, and prototype decisions
- active-event and pre-fire paths

### Evolution III

- no ordinary automatic generation by default
- fully random valid battalion and support composition
- one to 25 combat battalion design range or verified safe equivalent
- quality and coherence axes
- claimant generals, demands, influence, and revolts
- 20 male claimant gameplay profiles with regional male names and 20 separate region-compatible army/muster identity scenes
- one-state takeover handling
- ordinary claimant releases work without Evolution IV or a family row
- exact claimant-loyal formations are the only ordinary release force
- an unprovable ordinary release resolves as a visible failed coup
- active-event and pre-fire paths

### Evolution IV

- documented family registry
- base zombie trainable; approved stronger provider-511 variants spawn-only and without a derivative profile
- ghost and golem spawn-only
- future explicit opt-in
- saturation and containment
- derivative release and parent isolation
- one-time pre-fire first-family reception with three proved outcomes
- pending country-local retry when no provider is eligible
- anomalous claimant and claimant-independent family release modes
- exact claimant-free family breach under weak control
- verified one-state same-tag provider takeover
- active-event and pre-fire paths

### Derivative countries

- zombie, ghost, and golem package coverage
- dynamic or approved tag model
- distinct names and flags
- leader identity
- starting ideas and lifecycle
- starting units from revolt
- mode-aware exact recreate, prove, delete transfer
- claimant and family pre-commit consequences remain visible
- reinforcement path
- focus-scale route content
- decisions, AI, expansion, defeat cleanup
- shared special and nonhuman classification

### Triggerable scenario

- SCN-013 registration with aligned ID/name arrays and all four sort orders
- four scenario types
- four intensity stops
- direct launch without normal prerequisites
- immediate revolt and war
- one-state safety
- cleanup of launch bypass
- no terminal world-end flag

### UI and assets

- phased decision category
- ordinary decision-based lot management; no Event 19 scripted GUI
- former Muster Board, selected-lot, claimant-tab, registry-tab, and animation requirements remain historical design evidence only
- no missing visible asset

### AI and balance

- ordinary country AI
- claimant AI
- derivative AI with continuing aggression toward all reachable ordinary countries
- request safety
- no free equipment loop
- no free civil-war army
- no invalid target or route use
- task-specific scenario validation
- P19-CW-RESERVED: a host with a pending claimant or family release and a competing Event 021 plan preserves one region, one formation owner, and one obligation set; the conflicting political opening remains uncommitted
- P19-CW-ORDINARY: a host with managed ordinary lots and a distinct political premise receives no blanket immunity, while an unproved formation-transfer adapter grants no duplicate army or debt settlement
- P19-ZOMBIE-MODES: a provider-511 lot materializes only its registered spawn-only variants, with no training unlock, derivative creation, or parent mutation/evolution credit

### Logs and documentation

- event history
- four evolutions
- Event Details
- first-family reception outcome history
- natural release-mode and containment wording
- scenario docs
- helper docs
- classifiers
- event docs
- spreadsheet wording
- asset and achievement manifests

## Completion boundaries

A final implementation report must list any simplification, omitted family, missing army/host identity scene, individual-focal-subject violation, unwired animation, fallback tag model, missing AI path, unverified parent isolation, stale spreadsheet field, or skipped scenario validation.

The current planning package deliberately leaves exact script syntax, constant values, final localisation, final tags, and final asset filenames for implementation after inspection of the local repository, offline Paradox wiki, vanilla documentation, and existing Chaos Redux patterns.
