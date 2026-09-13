# Event 056: Acceptance Criteria

## Completion meaning

Event 56 is complete only when the global event, every fleet identity, repeat scaling, all three evolutions, human and AI commissioning, dual-cluster membership, Chaos milestones, achievements, assets, Event Log surfaces, documentation, and catalog workbook agree with this specification.

A working popup and a few granted ships do not satisfy the event.

## Baseline event acceptance

- Event 56 is registered as Minor Repeatable with Chaos level 1.
- One automatic firing creates one global pacing event.
- Every eligible country is processed once.
- Every eligible human country receives one personal commissioning flow.
- AI recipients use the same package construction and legal choices.
- Landlocked countries are skipped and can qualify on a later repeat after gaining direct usable coast.
- The event never places ships in enemy-controlled, inland, or otherwise invalid locations.
- The Event Log records one global row with no actor.
- The package origin remains unexplained.

## Eligibility acceptance

Test and confirm these cases separately:

| Case | Expected result |
| --- | --- |
| Coastal major with several ports | Receives one package in one to three suitable ports. |
| Coastal minor with one port | Receives a coherent package scaled to safe local and world limits. |
| Island country | Receives a package normally. |
| Country with coast but no naval base | Receives delayed emergency commissioning when a valid state exists. |
| Fully landlocked country | Receives nothing during that firing. |
| Landlocked overlord with coastal subject | Overlord is skipped, subject is evaluated independently. |
| Coastal subject | Receives its own package. |
| Government in exile without controlled coast | Skipped. |
| Civil-war sides with separate coast | Each valid side is evaluated independently. |
| Special country permitted ordinary fleets | Uses owner-approved naval behavior. |
| Special country without ordinary fleet support | Fails closed. |
| Recipient annexed before delayed delivery | Delivery cancels once with no transfer or duplication. |
| Recipient loses original port before delayed delivery | One safe re-selection occurs, otherwise delivery cancels. |

## Fleet identity acceptance

Every baseline identity must have a legal and recognizable implementation:

- Balanced Surface Fleet
- Submarine Raiding Fleet
- Destroyer Swarm
- Convoy-Heavy Escort Fleet
- Cruiser-Focused Fleet
- Capital-Ship Fleet
- Carrier-Focused Fleet
- Coastal Defense Fleet
- Invasion-Support Fleet
- Minelaying and Sea-Denial Fleet when supported

For each identity, confirm:

- defining ships dominate the package as specified
- support reinforces the identity
- screens and carrier aircraft are functional where required
- compact, standard, and heavy bands remain coherent
- task forces are usable and bounded
- the personal report describes the result accurately
- global compression preserves the defining core

The sea-denial identity must disappear cleanly when mine warfare is unavailable.

## Commissioning acceptance

### Full Commissioning

- delivers all legal active ships and support once
- applies the intended short commissioning support
- creates immediate ordinary fuel and repair burden
- cannot duplicate through repeated clicks or reload

### Phased Commissioning

- delivers the first tranche once
- identifies the reserved second tranche clearly
- resolves through one bounded follow-up
- re-evaluates a lost port once
- delivers or cancels the reserve once
- preserves package identity and value

### Break Up the Package

- appears only for a package with meaningful convertible value
- preserves the defining operational core
- removes actual package hull value
- returns a deliberately lossy support package
- cannot convert support twice
- records achievement disqualifiers
- cannot become more valuable than full commissioning

## Repeat acceptance

Test at least four receipts for the same country and a first receipt for a newly coastal country.

- first receipt uses the full local scale
- second receipt targets 75 percent before global normalization
- third receipt targets 55 percent
- fourth and later target 40 percent, or the enabled Evolution I floor
- each receipt rolls a fresh identity
- cosmetic and ideology changes do not reset history
- cohort tracking survives save and reload
- delayed tranches from different firings do not collide
- event-system repeat weight and cap behavior remain governed by the shared system

## Evolution acceptance

### Evolution I at 200 or higher

- activates through evolution pacing when Event 56 already exists
- can be active before the first firing when the threshold is already met
- unlocks Extreme packages and stronger identity skew
- affects future packages only
- raises the late-repeat floor only while enabled
- records one global evolution row
- adds zero Chaos for activation

### Evolution II at 400 or higher

- accepts only owner-registered experimental assets
- grants no research
- fails closed on missing registration or content
- affects future packages only
- records one evolution row
- adds event-owned Chaos only when the first experimental asset is actually delivered

### Evolution III at 600 or higher

- enables coherent impossible hybrid packages
- preserves one primary fleet identity
- respects owner registrations and global limits
- affects future packages only
- records one evolution row
- adds event-owned Chaos only when the first impossible package is actually delivered

### Evolution toggle matrix

Test:

- all evolutions enabled
- each evolution disabled alone
- lower stage disabled while a higher stage is enabled
- all evolutions disabled

Baseline Event 56 must remain complete in every valid toggle combination.

## Chaos acceptance

Confirm the exact one-time milestones:

- first manifestation: +5
- first firing reaching at least 25 successful recipients: +5
- first experimental delivery: +10
- first impossible delivery: +15
- first previously landlocked recipient after gaining coast: +3

Confirm that:

- evolution activation adds zero
- no milestone repeats
- ships, convoys, aircraft, recipients, battles, and blockades do not add direct Event 56 Chaos individually
- generic war, tension, death, famine, and other shared sources are not duplicated
- no unsupported negative reversal exists

## AI acceptance

Run the named scenarios from `quality/ai_probability_scenario_matrix.md` through the required probability workflow.

Confirm that:

- package identity remains random before AI handling
- invalid choices are excluded rather than given tiny weight
- commissioning ordering matches each scenario
- AI creates usable task forces
- AI does not deploy unscreened carriers or capital ships
- AI does not waste the full fuel grant on purposeless peacetime missions
- production reaction avoids obvious redundant overbuilding
- carrier-air support receives attention when possible
- the AI can keep part of a large package in reserve

Weighted behavior requires a baseline audit, implementation, and comparison audit using the same scenarios.

## Cluster acceptance

### Sudden Abundance

- includes Events 19, 29, 32, 37, 42, 56, and 64
- uses the specified per-membership severities
- unlocks at cluster Chaos level 1
- treats the selected event as required and other members as optional
- records one cluster pacing transaction
- records participating and skipped member results

### Military Preparation

- includes Events 32, 42, 56, and 64
- uses the specified per-membership severities
- unlocks at the approved cluster tier, with Chaos level 2 as the planning proposal
- does not start wars directly
- records one cluster pacing transaction

### Dual membership

- one Event 56 selection can enter at most one cluster
- Event 56 applies once inside either cluster
- a manual cluster firing applies the member once
- cluster selection and member participation pass probability inspection
- cross-event support cannot duplicate the same aircraft, convoys, or other grant

## Connection acceptance

- Event 54 research can widen later legal naval content without Event 56 granting research.
- Event 55 port and logistics improvements affect commissioning capacity without changing package identity.
- Event 42 support enters only through an explicit adapter and cannot duplicate Event 56 support.
- Event 32 naval assets enter only through owner registration.
- Famine reacts only to a real live blockade that satisfies its own requirements.
- Event 56 never applies famine directly.
- Other events can damage or destroy the fleets through ordinary systems.

## Performance acceptance

Run a benchmark with a large eligible-country set and all three evolution stages.

Record:

- eligible recipients
- successful recipients
- skipped reasons
- ships created
- hull-equivalent value
- package distribution
- task-force count
- delayed tranche count
- execution time
- save-size impact
- repeat-firing impact

Confirm that:

- the event uses one bounded global processing pass during firing
- no new daily, weekly, or monthly whole-world scan exists
- only affected recipients receive delayed work
- no recipient uses more than three commissioning ports
- arrays and temporary allocation state clear after resolution
- cohort and achievement memory stays bounded
- the tested world and per-country ship limits preserve playability

If the initial planning budget does not preserve a meaningful package for every valid recipient, tune the internal value scale or budget. Do not silently skip recipients to keep an arbitrary number.

## DLC and compatibility acceptance

Test the supported DLC matrix, including a minimal-content setup.

Confirm that:

- baseline fleet identities use legal ships in every supported setup
- carrier packages have a legal aircraft route or leave the recipient's legal pool
- sea-denial packages leave the pool when mine warfare is unavailable
- experimental entries fail closed when owner content or DLC is absent
- no technology is granted as a compatibility shortcut
- package identity survives fallback to predefined legal designs

## Achievement acceptance

### `the_navy_from_steppe_to_sea`

- records first-manifestation landlocked status correctly
- requires later direct usable coast
- requires a later actual package
- requires meaningful combat participation by a granted defining ship
- survives save and reload

### `the_navy_three_gifts_one_admiralty`

- requires three separate firings and three distinct identities
- excludes breakup receipts
- measures retention from delivered value
- requires two strategic regions with cohort battle proof
- handles failure or restart according to the final bounded design

### `the_navy_wrong_fleet_right_war`

- records objective mismatch before delivery
- sets a 540-day deadline
- requires direct cohort participation in a reliable strategic result
- fails on breakup or timeout
- clears invalid attempts

For every achievement, confirm full localisation, tracking, disqualifiers, documentation, and the unlocked, grey, and not-eligible icon triplet.

## Presentation acceptance

- global report appears once
- personal reports show correct dynamic package and port information
- no raw keys, variables, or debug wording appear
- options state visible consequences clearly
- repeat and evolution text preserves the unresolved origin
- Event Details describes premise rather than raw effects
- History and Evolution rows use correct metadata
- cluster details summarize Event 56 without listing every recipient
- no text uses update-history or developer-facing language

## Asset acceptance

- four report images exist at the consumer's verified dimensions
- each image matches its progression stage
- all final images use period-authentic documentary treatment
- no generated text, modern equipment, fused ships, bad crops, overflow, or bleeding remain
- three achievement icon triplets exist and match final IDs
- icons remain readable at native size
- final assets are installed in engine-facing folders
- manifests and permanent provenance notes are complete
- no runtime reference points into a temporary documentation workspace

## Catalog and documentation acceptance

- the authoritative event catalog workbook contains the corrected Event 56 details and evolution summaries
- the workbook records both cluster memberships through a supported multi-membership structure
- Sudden Abundance and Military Preparation receive approved unused IDs only after registry inspection
- cluster member lists and severities match this specification
- Event 56 remains To Be Reworked until implementation and required validation are complete
- the catalog exporter runs after workbook changes
- export CSVs are not edited directly
- event documentation, Event Details, Event Log wording, and workbook text agree

## Required implementation audits

Before completion, the implementation owner should use the relevant project routes:

- event inspection and comparison for the full chain
- scripted-system architecture review for package allocation and owner registration
- AI probability audit before and after weighted changes
- localisation audit for all visible text
- generated event-art and icon workers for the accepted assets
- spreadsheet worker for the authoritative workbook
- improvement-loop planner near completion
- event completion auditor after all accepted addenda are resolved

The autonomous debug-playtest skill remains explicit-invocation only. Do not claim live in-game validation through that skill unless the user separately authorizes and the required desktop capability exists.

## Final completion gate

Do not mark Event 56 complete while any of these remain unresolved:

- missing package identity
- invalid recipient case
- unbounded world ship creation
- missing AI handling
- untested weighted logic
- missing cluster membership or dual-cluster protection
- missing Chaos milestone or repeat guard
- missing evolution toggle behavior
- missing achievement tracking or icons
- placeholder or unwired report art
- stale Event Details, documentation, or catalog workbook
- unresolved accepted improvement addendum
- unreported simplification or fallback
