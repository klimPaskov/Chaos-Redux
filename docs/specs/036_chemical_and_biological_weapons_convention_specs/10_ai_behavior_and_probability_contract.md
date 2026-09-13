# AI behavior and probability contract

## AI design purpose

AI must understand Event 036 as a strategic diplomatic system.

It should choose a posture and later actions from its actual military, diplomatic, scientific, industrial, and humanitarian situation.

Government ideology can influence choices, but it cannot replace capability and campaign logic.

## Opening posture evaluation

### Full Ratification score factors

Increase willingness when the country:

- already possesses chemical or biological technology
- has strong industry and research capacity
- is at war or expects a major war
- has missile, aircraft, nuclear, or protection relevance
- tolerates public Condemnation
- seeks a research or military network
- has recently used or suffered unconventional warfare
- is aligned with a likely sponsor

Reduce willingness when the country:

- has no relevant capability or strategic need
- strongly prioritizes public restraint
- has high public Condemnation and low tolerance for further sanctions
- faces internal instability that makes ratification costly
- is a leading public opponent of unconventional warfare

### Chemical Accession score factors

Increase willingness when the country:

- has chemical technology or production capacity
- lacks a viable biological program
- fears uncontrolled outbreaks
- wants protection and delivery cooperation
- prefers a narrower military commitment

Reduce willingness when biological capability is central to national strategy or when the country rejects all unconventional normalization.

### Retaliation Reservation score factors

Increase willingness when the country:

- prioritizes protection and deterrence
- has been attacked or threatened
- wants treaty access without offensive first use
- is politically sensitive to civilian harm
- has high protection capability
- is a subject or minor power seeking guarantees
- has high Condemnation aversion

Reduce willingness when the country is planning offensive first use or rejects the convention entirely.

### Public Rejection score factors

Increase willingness when the country:

- prioritizes the old prohibition
- has little military benefit from membership
- has high diplomatic influence among holdouts
- is strongly concerned about civilian harm or outbreak risk
- has active sanctions against unconventional users
- belongs to another restraint-oriented treaty network

Reduce willingness when it needs member research, protection, or project access.

### Covert Preparation score factors

Increase willingness when the country:

- publicly benefits from rejection
- secretly values chemical or biological capability
- has strong counter-intelligence
- can support hidden research or production
- distrusts inspection and foreign control
- accepts cover-up and exposure risk

Reduce willingness when the country lacks research capacity, has weak intelligence protection, faces high discovery risk, or already has a public member route that serves its strategy better.

The covert route must remain uncommon and situational.

## Treaty voting

AI treaty response uses:

- primary posture
- current first-use policy
- active evolution
- treaty family
- sponsor relationship
- war state
- relevant technology
- protection need
- recent attack or use
- public Condemnation
- opposition leadership
- implementation capacity
- prior treaty failures
- reservation compatibility

A country must never ratify a treaty whose participant trigger is false.

A reservation should be preferred only when it preserves a coherent part of the treaty.

AI should abstain or reject when a reservation would have no meaning.

## Sponsorship and lobbying

AI sponsors an agenda when it can implement the treaty and expects enough support.

It should avoid sponsorship when:

- it cannot pay the commitment
- the agenda conflicts with its posture
- the ratification pool is impossible
- it is near capitulation
- a recent failed sponsorship cooldown is active
- the relevant capability does not exist

Lobbying targets countries that can legally change their response.

AI must not target invalid actors, current enemies when the agenda forbids it, or countries already locked into an incompatible response.

## First-use AI

A permissive policy increases willingness but does not guarantee use.

Chemical first use requires:

- war or another valid hostile context
- a valid target
- physical payload
- delivery system
- readiness
- military benefit
- acceptable friendly exposure

Biological first use additionally evaluates:

- outbreak control
- spread direction
- border proximity
- friendly population risk
- containment
- expected retaliation
- target logistical or strategic value

Nuclear first use additionally evaluates:

- payload scarcity
- target value
- fallout
- civilian density
- retaliation risk
- war trajectory
- national survival

Thermonuclear willingness does not receive an Event 036 routine-use bonus.

## Doctrine AI

AI adopts Theater Integration when it has at least two usable capability components and a war plan that benefits from integration.

AI adopts Strategic Integration when it has major-power, alliance, nuclear, missile, or large-war reasons to coordinate several capability families.

Small countries should specialize in protection, laboratories, delivery support, equipment, or regional deterrence when full strategic integration is wasteful.

## Opposition AI

The Opposition Leader should:

- prioritize defeating permissive treaty votes
- recruit public opponents and reservation members
- publish valid evidence
- support sanctions
- protect members from attack without normalizing first use
- exploit treaty breaches
- avoid spending resources on an opposition campaign it cannot sustain

Ordinary opponents can support the leader or pursue bilateral policy.

They do not form a normal faction through Event 036.

## Covert AI

A covert opponent should:

- choose one plausible chemical or biological route
- invest only when it can protect the program
- avoid obvious public contradictions
- respond to inspection and evidence risk
- end or reveal the program when continued concealment is irrational
- never receive hidden free technology or equipment

Exposure must change its strategy immediately.

## Project AI

AI contribution willingness depends on:

- provider relevance
- recipient eligibility
- project progress
- expected completion time
- industry
- research capacity
- equipment stockpile
- manpower
- current war needs
- current contribution share
- intention to remain a member
- safety reserves

A large country can lead repeated tranches.

A small country should choose the contribution family it can afford and still reach the minimum meaningful amount.

AI should avoid overcontributing after its expected share is already high unless the project is near completion or strategically critical.

The active project identity does not affect selection probability.

## Required probability scenarios

The implementation must audit at least these named scenarios:

| Scenario ID | Situation | Expected ordering |
| --- | --- | --- |
| `E36_P01` | Aggressive major at war with chemical and biological technology | Full Ratification above Chemical Accession, reservation, rejection, and covert rejection |
| `E36_P02` | Peaceful restraint-oriented democracy with no CBRN technology and low threat | Retaliation Reservation or Public Rejection above Full Ratification |
| `E36_P03` | Threatened minor with weak industry and no weapons | Retaliation Reservation above Full Ratification and covert preparation |
| `E36_P04` | Chemical-capable country with no biological program and high outbreak fear | Chemical Accession above Full Ratification and rejection |
| `E36_P05` | Public opponent with strong intelligence and secret research capacity | Covert Preparation above Full Ratification, but not dominant without additional risk tolerance |
| `E36_P06` | Nuclear power losing a major war after Evolution II | Nuclear first-use willingness rises, but invalid targets and missing payload still force zero |
| `E36_P07` | Reservation member attacked with chemical weapons | Retaliatory use above continued restraint when payload and target are valid |
| `E36_P08` | Reservation member considering offensive use | Offensive use at zero unless reservation is repealed or breached through an explicit path |
| `E36_P09` | Major program participant with surplus industry | Industrial and research contributions above no action |
| `E36_P10` | Minor program participant with low stockpiles | Affordable facility or research contribution above equipment depletion |
| `E36_P11` | Opposition Leader during a close first-use vote | Organize Opposition above unrelated posture revision |
| `E36_P12` | Project candidate pool with three eligible projects | Each project has exactly one-third probability |
| `E36_P13` | Project candidate pool with duplicated provider registration attempt | Deduplication restores equal probability across unique project IDs |
| `E36_P14` | Active selected project becomes normally available | Cancellation probability is one and completion probability is zero |
| `E36_P15` | Thermonuclear target after Evolution III | Event 036 does not increase willingness through routine convention doctrine |

## MCP probability workflow

Every probability-bearing surface begins with `hoi4.probability_inspect`.

The audit must state whether the full candidate pool and external factors are known.

Use:

- `hoi4.probability_evaluate` for named posture and action scenarios
- `hoi4.probability_sweep` for Chaos, war-state, Condemnation, and capability thresholds
- `hoi4.probability_simulate` for sampled conference outcomes when exact normalization is impractical
- `hoi4.probability_sequence` only when the complete conference cadence and state-transition contract is declared
- `hoi4.probability_compare` after every source change to AI weights or project selection logic
- `hoi4.probability_render` when a comparison or sensitivity view improves review

The `chaosx_ai_probability_auditor` remains read-only.

The parent or owning patch agent chooses the intended balance target and applies changes.

## Hard AI safety rules

AI weights are zero when:

- the posture or treaty is invalid
- the country is not eligible
- the target is invalid
- the physical payload is absent
- the delivery system is absent
- the active evolution is disabled
- the country cannot pay the action cost
- a project contribution is paused or cancelled
- a project recipient trigger is false
- a selected weapon became normally available
- the action would duplicate an existing receipt

No positive strategic factor can override a hard invalidity gate.
