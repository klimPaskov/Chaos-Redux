# Achievement Implementation Prompt for Event 22 Concentration Camps

## Task

Implement and validate the Event 22 achievement suite defined in `022_concentration_camps_achievements.md`.

The achievements reward closure, rescue, evidence preservation, successor accountability, refusal to continue operation, relief, and safe resettlement. No achievement may reward camp deaths, extermination, forced-labour output, chemical killing, successful concealment, network expansion, or repeated site construction.

## Required reading

Read before editing:

- repository `AGENTS.md`
- Event 22 index and all five specification parts
- `022_concentration_camps_achievements.md`
- `022_concentration_camps_acceptance_criteria.md`
- `022_concentration_camps_asset_manifest.md`
- current Chaos Redux achievement definitions, scripted triggers, localisation, GFX, and unlock handling
- current Event 22 state, responsibility, evidence, survivor, closure, and history helpers
- current tag-switch, civil-war, multiplayer, and save-persistence patterns
- achievement and localisation reference assets under the canonical vanilla reference root

Do not implement achievements against placeholder variables that the event does not actually maintain.

## Accepted achievements

Implement these ten priority achievements:

1. `chaosx_achievement_022_close_every_gate`
2. `chaosx_achievement_022_names_restored`
3. `chaosx_achievement_022_evidence_survives`
4. `chaosx_achievement_022_no_one_disappears_twice`
5. `chaosx_achievement_022_the_machine_stopped`
6. `chaosx_achievement_022_government_answers`
7. `chaosx_achievement_022_safe_harbor`
8. `chaosx_achievement_022_against_the_order`
9. `chaosx_achievement_022_from_camps_to_care`
10. `chaosx_achievement_022_no_second_operator`

Implement `chaosx_achievement_022_the_long_return` only when the shared migration and displaced-person proof is complete. Do not fake it with a country flag if the population destinations are not tracked.

The exact proof, failure, and exploit conditions are in the achievement specification. Preserve them.

## Proof architecture

Use event-owned persistent proof. Transient idea checks are insufficient.

Each achievement should rely on a bounded helper that can answer:

- which player country owns the proof
- which Event 22 network generation is relevant
- which responsible actor created the network
- how many sites and states qualify
- whether the player continued operation
- whether relief, registration, evidence, closure, or resettlement completed
- whether a failure condition occurred
- whether the proof window is still active

Use idempotent event-driven updates at meaningful transitions:

- site closure
- site liberation
- survivor registration
- evidence preservation
- relief completion
- network verification
- tribunal cooperation
- responsibility-generation creation
- forced evacuation or liquidation result
- government succession
- safe-destination completion

Do not run a whole-world daily achievement scan.

## Tag switch and civil war

- Track the human player country through the existing achievement-owner pattern.
- A cosmetic-tag change must preserve progress.
- A civil-war split must not grant both sides the same player proof automatically.
- A player that switches to another country must not carry an unrelated network proof unless the project achievement framework explicitly supports cross-country campaign achievements.
- A successor can continue a proof only where the achievement says successor action qualifies.
- Responsibility evidence must remain linked to the original operator.

## Failure locking

When an achievement has a permanent failure condition, store it once and do not clear it through:

- building deletion
- state loss
- annexation
- government change
- save and reload
- category cleanup
- event repeat firing
- a later transparent action

Examples:

- continuing one inherited site permanently fails `No Second Operator` for that network
- completing a liquidation permanently fails `No One Disappears Twice` for that network
- reopening a site during the proof window fails `Close Every Gate`

A failure in one network should not necessarily block a later achievement attempt with a new network unless the achievement specification says campaign-wide purity is required.

## Exploit prevention

Prove that achievements cannot be earned by:

- using console building deletion in normal logic
- losing camp states to an ally without relief
- releasing a subject solely to move responsibility
- switching tags
- reloading before a failure transition
- converting a site to another building without closure
- destroying records and then satisfying only a generic closure flag
- accepting survivors and immediately expelling them
- briefly controlling five sites without stopping operation
- reusing one liberated site under another state modifier

Use original responsibility, later operator generation, survivor status, evidence status, and operation-state helpers.

## Localisation

Write player-facing achievement name and description localisation from the directions in the achievement specification.

Requirements:

- concise and respectful
- no graphic descriptions
- no jokes
- no invented quotations
- no reward framing around perpetrators
- clear objective without revealing hidden future event branches
- correct dynamic values only where the achievement UI supports them
- all keys present with correct encoding and BOM

Working names can be retained when they remain clear.

## Icons

Coordinate with the Event 22 icon handoff. Do not create final icons inside the achievement scripting task unless the parent explicitly assigns `chaosx_icon_artist`.

Every achievement requires:

- completed `64x64` master
- grey locked state
- not-eligible state where the framework uses it
- correct sprite definition
- correct runtime path
- native and `4x` review

Do not use victim, corpse, gas-chamber, execution, or graphic imagery. Use the symbolic directions in the asset manifest.

## Validation scenarios

### Close Every Gate

- baseline network
- full transparent closure
- 180-day no-death proof
- save and reload during proof
- reopen one site in a separate save and verify permanent failure for that network

### Names Restored

- three liberated sites
- registration, evidence, and safe status complete
- one destroyed archive but several surviving evidence types
- verify that deliberate record destruction by player fails it

### The Evidence Survives

- destroyed-site cover-up
- preserve physical, testimony, and independent documentary evidence
- tribunal cooperation
- verify duplicate discovery does not count as another category

### No One Disappears Twice

- known enemy retreat network with three sites
- interrupt each evacuation or liquidation
- succeed at relief
- separate failure save where one liquidation completes

### The Machine Stopped

- Evolution III network
- complete closure within 730 days
- decontaminate chemical site
- separate failure save with one new conversion after closure starts

### A Government Answers

- government succession
- archives opened
- no successor operation generation
- accountability and relief complete

### Safe Harbor

- survivors from three networks
- receiving capacity, housing, medical, and legal status
- no forced return

### Against the Order

- underground-network mission
- nonlethal secure outcome
- records and survivors preserved

### From Camps to Care

- five former sites
- all relief and recovery transitions complete
- no reuse

### No Second Operator

- capture or inherit five active sites
- stop immediately
- no new responsibility generation
- one-year closed proof

### The Long Return

- run only after migration API is complete
- dispersed destinations and later safe resolution

## Required audit routing

After implementation:

- run `chaosx_localisation_auditor`
- run the event completion auditor against achievement requirements
- use the decision or scripted-system auditor if proof helpers touch shared event state
- run live QA with dedicated saves

Patch-capable agents may fix small local trigger, localisation, cleanup, or icon-reference defects. Broad changes to Event 22 state architecture return to the parent.

## Completion report

Return:

- achievements implemented
- helper IDs and files
- persistent proof model
- failure-lock model
- icon and GFX status
- localisation keys
- validation scenarios run
- screenshots or logs
- save and reload results
- multiplayer result
- exploits tested
- skipped achievements and exact blockers
- remaining defects

Do not claim the suite complete while any accepted proof can be earned through state loss, tag switch, building deletion, operation reuse, or missing persistent history.
