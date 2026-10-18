# Event 32: Missiles

## Catalog identity

- Event ID: `32`
- Event name: Missiles
- Type: Minor Repeatable
- Catalog status: `To Be Reworked` until the open rows in the README status table close; the event is already in the default-enable allowlist
- Minimum event chaos level: Calm World
- Cluster: None
- Entry event: `chaosx.nr32.1`
- Country report: `chaosx.nr32.2`; first global news: `chaosx.nr32.3`
- Manual scenario: `SCN-015` Missile Age at raw ID 15 (collision-audited and registered)

## Event premise

Every valid existing country gains a missile program when Event 32 fires.
A country without missile technology receives its first operational step.
A country with an existing program receives its next available step.
A country that has completed the supported line receives a mature-program package instead.

Every recipient receives an operational missile reserve and at least one usable launch state.
The capability appears inside the country's own military structure with enough equipment, trained crews, and technical knowledge to function.
Its origin remains unexplained.
The event should feel strange through concrete details such as complete bunkers, sealed canisters, authenticated codes, and crews who can operate equipment that has no procurement history.

Event 32 creates a persistent missile-warfare layer.
Repeat firings deepen programs, strengthen existing sites, expand reserves, and advance technology.
The five evolutions change how the entire system behaves.

## Player promise

The baseline should create immediate strategic choices:

- where the first launch site is placed
- whether the new program is maintained or neglected
- whether missiles are used for precise infrastructure attacks or broad strategic barrages
- whether a country invests in readiness, guidance, hardening, and command security
- whether newly inherited or captured sites are secured, integrated, scuttled, or left vulnerable
- how much reserve to keep for deterrence, conventional strikes, or later special payloads

The baseline must work as a complete event without any evolution.
A campaign can use conventional missiles, expand sites through repeat firings, and finish wars through strategic damage while all evolution toggles remain disabled.

## Global firing model

Event 32 is one global pacing event.
The entry event performs one bounded dispatch over valid country scopes at the moment of firing.
It does not create a recurring daily, weekly, or monthly all-country scan.

The global transaction has five phases:

1. freeze the current recipient pool
2. validate every candidate against the recipient contract
3. initialize or advance each accepted country's missile program
4. send reports only to human recipients and apply AI setup silently
5. record one global Event 32 history entry and any first-fire news item

Freezing the pool prevents a release, annexation, civil war, or country transformation inside one recipient transaction from changing who is processed later in the same firing.
The implemented transaction is `missiles_global_firing_transaction`, which freezes `global.missiles_frozen_recipients` and sends each accepted recipient the hidden immediate receiver `chaosx.nr32.5` so that `ROOT` is the recipient.

Deterministic chunking is allowed if a one-frame pass causes performance problems.
Chunking must preserve one history row, one repeatable-weight transaction, one firing date, and the same final result.

## Valid recipient contract

A valid recipient must satisfy all of the following:

- the country exists
- the country owns at least one land state
- the country controls at least one state that can support a launch-site record
- the country is not a dummy, observer, temporary script carrier, or reserved system scope
- the country can hold variables, flags, decisions, and technology
- no owning special-country system has marked it permanently ineligible

Subjects qualify when they meet the ordinary requirements.
Government-in-exile countries without controlled land are deferred.
A capitulated country with a controlled enclave may qualify if it has a usable state.

`is_special_chaos_country` and `is_actual_nonhuman_country` are classification inputs, not blanket exclusions.
An industrial or organized special actor can use Event 32 through an explicit recipient profile.
A temporary horde, outbreak carrier, pure map effect, or nonindustrial actor without a command structure is skipped with a stable reason.

| Profile | Meaning | Result |
| --- | --- | --- |
| Ordinary state | Normal country with controlled land and institutions | Full program |
| Special industrial actor | Special or nonhuman country with proven industry and command structure | Full program through an adapter |
| Government in exile | Existing country without usable controlled land | Deferred until a later firing |
| Temporary military actor | Short-lived revolt or scripted force without a durable country package | Skipped |
| System carrier | Tag or scope used only for script storage or presentation | Skipped |
| Invalid landless actor | No owned or controlled state | Skipped |

Skipped countries do not receive a fake program, invisible missiles, or a site in another country's land.
The transaction records accepted, deferred, and skipped counts for testing.
Player-facing news does not list those counts.

## Program initialization

A newly accepted country receives:

- normalized missile technology stage `1` and the first supported missile technology
- one operational missile reserve package
- one primary launch-state record
- initial Launch Readiness and Command Control
- the baseline conventional strike actions
- the program status idea
- the first country report if the country is human-controlled

Initial tuning anchors (the implemented values in `missiles_reserve`, `missiles_program_value` and `missiles_site_capacity` in `common/script_constants/032_missiles_constants.txt` are authoritative):

| Value | Design target |
| --- | --- |
| Operational Reserve | `4` base plus economy and territory scaling, capped at `18` |
| Launch Readiness | `60` |
| Command Control | `70` |
| Primary site capacity | `4` missiles per prepared operation |
| First-site hardening | low |
| First-site security | moderate |

Later tuning goes through balance review and the constants, not through new literals.

## Technology progression

Each Event 32 firing grants one next available missile step.

| Program stage | Design meaning |
| --- | --- |
| `0` | No missile program |
| `1` | Experimental rocketry and first operational short-range capability |
| `2` | Reliable guided missile operations |
| `3` | Extended range and improved targeting |
| `4` | Advanced ballistic systems and hardened command |
| `5` | Strategic missile network |
| `6` | Supported line complete |

The implementation maps this progression onto the installed rocket line starting at `experimental_rockets` through `missiles_normalize_technology_stage` and `missiles_apply_next_technology_step`.
Without the optional improved-guidance project technology, the adapter uses the supported `improved_rocket_engines` successor; this is the documented no-DLC path.
Technology grants suppress their own notification because the human recipient already receives the country report.

The event must not grant an incompatible mutually exclusive technology, skip a required prerequisite, or erase already researched technology.
A country that already owns later technology is normalized upward before the new step is granted.
A country cannot be pushed backward by Event 32.

## Mature-program package

A country at the end of the supported line receives a mature-program package instead of a nonexistent technology step.

The package normally includes:

- a larger reserve increase
- partial readiness restoration
- capacity improvement at an existing site
- hardening or security progress where still available
- a new site only when capacity, territory, and redundancy rules justify one
- a country report variant for a human player

A mature package must not create unlimited missiles, duplicate launch states, exceed the site cap, or turn every repeat firing into a free strategic barrage.

## Repeated firing flow

On later firings, each valid country resolves these priorities in order:

1. initialize the program if it became valid after earlier firings
2. normalize the program against already researched technology
3. grant one next technology step or the mature package
4. add an operational reserve package
5. reinforce an existing active launch site
6. restore a bounded amount of readiness
7. repair a damaged or compromised site if the normal program can repair it
8. create a secondary site only when the site-cap and redundancy conditions are met
9. refresh the program status
10. send a repeat report to human recipients

A repeated firing should usually make current infrastructure stronger.
It should not scatter new rocket sites across random states.

## Newly created countries

A country released after an earlier firing does not receive a free catch-up transaction merely because it now exists.
It can enter the system by inheriting an existing launch state through the capture or inheritance contract, by receiving a later global firing, or through an explicit bridge from its owning event or scenario.

A new country that inherits no launch infrastructure begins at stage `0`.
A new country that captures a site may control the physical infrastructure without the technology, reserve, codes, or command control needed to use it safely.

## Human and AI reports

Human recipients receive one report after their country transaction is complete.
AI recipients receive no popup; their program values, sites, decisions, and AI profile are initialized silently.

In multiplayer:

- each human country receives its own country report
- no human receives another player's report
- one global news item may appear on the first global firing
- the event creates one global history row
- report delay and ordering cannot let one player's option change another player's setup package

Country reports have one acknowledgement option unless the report introduces a real emergency choice.

## News behavior

The first global firing creates one news event about simultaneous missile proliferation.
It communicates visible evidence: launch structures appearing in many countries, canisters and range activity, governments sealing new sites, military traffic and test plumes, and foreign observers unable to explain the common origin.
It does not list technology levels, reserve counts, or future evolution names.

Repeat firings do not create global news.
They use country reports and Event Logs.
An evolution may create its own news item when the change is globally visible (part 4, Evolution news and reports).

## Event Logs integration

### History

One global history row is recorded for each firing:

- event ID `32`, type Minor Repeatable, date, no actor
- the frozen recipient count as the row payload; the visible row is the shared event-name row used by every event (user decision recorded in commit `78e6554af`, Restore event history rows to event names, which removed the bespoke `missiles.event_log.history.row` text)
- a firing with no valid recipient records a zero payload and shows the same event-name row
- repeatable weight and cap behavior through the shared event system

The row is never duplicated per recipient.

### Event Details

The Event Details premise explains worldwide missile proliferation, repeated technological advancement, launch-site expansion, and the risk of command failure.
It does not expose hidden chances, raw tuning values, future incidents, scenario bypasses, or implementation state.

### Evolutions

Each of the five tracks receives one catalog row and one logged unlock entry when it becomes active.
Part 4, Evolution logging, owns the log identity.
Country adoption, site accidents, rogue incidents, and individual retaliation choices are ordinary history, not evolution milestones.

### Default enable state

Event 32 is in `event_log_event_is_reworked_default_enabled` (agent decision item 10, 2026-10-04).
Default enablement does not promote the catalog status.

## Chaos effects

Status: `unresolved` proposal, not implemented.
The constants `missiles_tuning.first_chaos`, `repeat_chaos` and `*_unlock_chaos` exist but no effect reads them.
Their `_unlock_` names contradict the rule below that unlocking pays nothing, so an implementation must rename them to outcome names when the map is accepted.

The design principle is that Event 32 pays Chaos only for an abnormal outcome that has actually happened.
Evolution eligibility, MTTH completion, unlock, logging, doctrine adoption, payload integration, retaliation posture, and operation preparation add zero direct Chaos.
Deaths, destruction, contamination, nuclear use and war keep their own shared Chaos sources; these budgets never act as casualty multipliers.

| Budget family | Proposed amount | Qualifying outcome | Repeat limit |
| --- | ---: | --- | --- |
| First global manifestation | `+10` | The first firing commits at least one complete program package of unexplained origin | Once per campaign; all recipients and chunks share one receipt |
| Later material manifestation | `+4` | A later firing actually adds a technology step, reserve, or site capacity somewhere | Once per firing with real new material; paid replenishment, repair and recapture never qualify |
| Rogue Launch Commands | `+6` | A rogue crew completes an unauthorized launch | First qualifying launch per campaign; a stopped launch, bluff or surrender gives zero |
| Unreliable Guidance | `+6` | A Neutral Drift result lands in a country that was neutral to the launcher | First qualifying impact per campaign; duds, debris without impact and wrong objects in the enemy state give zero |
| Special Warheads | `+15` | The first confirmed missile-delivered special payload release | Once per campaign across all payload families; integration, stock and failed release give zero |
| Automatic Retaliation | `+20` | A false, forged or mistaken warning chain reaches a third country through committed linked launches | First qualifying root per campaign; verified bilateral retaliation and stopped chains give zero |
| Saturation Arsenals | none | No distinct abnormal outcome exists; ordinary authorized bombardment is not a Chaos event | Proposed removal of the earlier unassigned `+10` (README open question 1) |

One closed operation or root chain pays at most one evolution-family budget, the largest that qualified.
Every qualifying milestone is still recorded as having occurred, so a later root cannot claim a suppressed milestone again.
Duplicate callbacks, linked strikes, renewed warnings and reloads cannot reopen a settled root.

Scenario setup keeps its own instant-Chaos contract and retains the seeded manifestation receipt, so a later firing cannot relabel it as the first appearance.

Acceptance cases for when the map is accepted: unlocking all five tracks pays nothing; a stopped rogue launch and a verified false warning pay nothing; a neutral impact pays the Guidance budget once; a mixed rogue, special-payload and automated root pays only its largest budget after closure.

## Baseline completion state

The baseline is complete when:

- every valid recipient has one technology step
- every accepted country has a reserve and usable launch state
- country reports and first-fire news behave correctly
- repeated firings advance technology and strengthen programs
- conventional strikes can be prepared and executed
- damage, deaths, diplomacy, and cleanup work
- captured and inherited sites have a defined lifecycle
- AI can maintain and use the system
- Event Logs, Event Details, documentation, and catalog fields agree

No evolution is required for baseline completion.
