# Event 32: Missiles

## Catalog identity

- Event ID: `32`
- Event name: Missiles
- Type: Minor Repeatable
- Status target: Reworked and ready for normal selection
- Minimum event chaos level: Calm World
- Cluster: None
- Entry event: `chaosx.nr32.1`
- First public country report family: `chaosx.nr32.2`
- Working manual scenario identity: `SCN-015`, subject to final registry audit

## Event premise

Every valid existing country gains a missile program when Event 32 fires. A country without missile technology receives its first operational step. A country with an existing program receives its next available step. A country that has completed the supported line receives a mature-program package instead.

Every recipient receives an operational missile reserve and at least one usable launch state. The capability appears inside the country's own military structure with enough equipment, trained crews, and technical knowledge to function. Its origin remains unexplained. The event should feel strange through concrete details such as complete bunkers, sealed canisters, authenticated codes, and crews who can operate equipment that has no procurement history.

Event 32 creates a persistent missile-warfare layer. Repeat firings deepen programs, strengthen existing sites, expand reserves, and advance technology. The five evolutions change how the entire system behaves.

## Player promise

The baseline should create immediate strategic choices:

- where the first launch site is placed
- whether the new program is maintained or neglected
- whether missiles are used for precise infrastructure attacks or broad strategic barrages
- whether a country invests in readiness, guidance, hardening, and command security
- whether newly inherited or captured sites are secured, integrated, scuttled, or left vulnerable
- how much reserve to keep for deterrence, conventional strikes, or later special payloads

The baseline must work as a complete event without any evolution. A campaign can use conventional missiles, expand sites through repeat firings, and finish wars through strategic damage while all evolution toggles remain disabled.

## Global firing model

Event 32 is one global pacing event.

The entry event performs one bounded dispatch over valid country scopes at the moment of firing. It does not create a recurring daily, weekly, or monthly all-country scan.

The global transaction has five phases:

1. freeze the current recipient pool
2. validate every candidate against the Event 32 recipient contract
3. initialize or advance each accepted country's missile program
4. send reports only to human recipients and apply AI setup silently
5. record one global Event 32 history entry and any first-fire news item

Freezing the recipient pool prevents a release, annexation, civil war, or country transformation inside one recipient transaction from changing who is processed later in the same firing.

The implementation may process the frozen pool in deterministic chunks if a one-frame global pass causes performance problems. Chunking must preserve one event history row, one repeatable-event weight transaction, one firing date, and the same final result.

## Valid recipient contract

A valid recipient must satisfy all of the following:

- the country exists
- the country owns at least one land state
- the country controls at least one state that can support a launch-site record
- the country is not a dummy, observer, temporary script carrier, or reserved system scope
- the country has a functioning country scope that can hold variables, flags, decisions, and technology
- the country has not been marked as permanently ineligible by an owning special-country system

Subjects are valid recipients when they meet the ordinary requirements. Government-in-exile countries without controlled land are deferred. A capitulated country with a controlled enclave may qualify if it has a usable state.

`is_special_chaos_country` and `is_actual_nonhuman_country` are classification inputs, not blanket exclusions. An industrial or organized special actor can use Event 32 through an explicit recipient profile. A temporary horde, outbreak carrier, pure map effect, or nonindustrial actor without a command structure is skipped with a stable reason.

Recommended recipient profiles:

| Profile | Meaning | Result |
| --- | --- | --- |
| Ordinary state | Normal country with controlled land and institutions | Full program |
| Special industrial actor | Special or nonhuman country with proven industry and command structure | Full program through an adapter |
| Government in exile | Existing country without usable controlled land | Deferred until a later firing |
| Temporary military actor | Short-lived revolt or scripted force without a durable country package | Skipped |
| System carrier | Tag or scope used only for script storage or presentation | Skipped |
| Invalid landless actor | No owned or controlled state | Skipped |

Skipped countries do not receive a fake zero-weight program, invisible missiles, or a site in another country's land. The global result summary records accepted, deferred, and skipped counts for debug and testing. Player-facing news does not list those counts.

## Program initialization

A newly accepted country receives:

- normalized missile technology stage `1`
- the exact first available supported missile technology
- one operational missile reserve package
- one primary launch-state record
- initial launch readiness
- initial command control
- the baseline conventional strike action family
- a missile-program status idea or dynamic modifier
- the first country report if the country is human-controlled

Suggested initial tuning anchors:

| Value | Suggested target |
| --- | --- |
| Operational reserve | `4` base plus economy and territory scaling, capped near `18` |
| Launch readiness | about `60` |
| Command control | about `70` |
| Primary site capacity | about `4` missiles per prepared operation |
| Base strike cooldown | `30` to `45` days |
| First-site hardening | low |
| First-site security | moderate |

These are tuning anchors. The coding agent must centralize them and adjust them through probability and balance review.

## Technology progression

Each Event 32 firing grants one next available missile step.

The normalized progression is:

| Program stage | Design meaning |
| --- | --- |
| `0` | No missile program |
| `1` | Experimental rocketry and first operational short-range capability |
| `2` | Reliable guided missile operations |
| `3` | Extended range and improved targeting |
| `4` | Advanced ballistic systems and hardened command |
| `5` | Strategic missile network |
| `6` | Supported line complete |

The implementation must map this normalized progression to the exact installed vanilla and mod technology graph. It must use `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` before locking technology IDs, prerequisites, DLC variants, or research-folder placement.

The event must not grant an incompatible mutually exclusive technology, skip a required prerequisite, erase already researched technology, or assume that the current legacy pair `experimental_rockets` and `rocket_engines` is the complete modern graph.

A country that already owns later technology is normalized upward before the new step is granted. A country cannot be pushed backward by Event 32.

## Mature-program package

A country at the end of the supported missile line receives a mature-program package instead of a nonexistent technology step.

The package should normally include:

- a larger reserve increase
- partial readiness restoration
- capacity improvement at an existing site
- hardening or security progress where still available
- a new site only when the country's current capacity, territory, and redundancy rules justify one
- a small reduction in the cost or time of the next replenishment action
- a country report variant for a human player

A mature package must not create unlimited missiles, duplicate launch states, exceed the site cap, or convert every repeat firing into a free strategic barrage.

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
9. refresh the visible program status
10. send a repeat report to human recipients

The site priority is deliberate. A repeated firing should usually make current infrastructure stronger. It should not scatter two new rocket sites across random states on every firing.

## Newly created countries

A country released after an earlier Event 32 firing does not receive a free catch-up transaction merely because it now exists.

It can enter the system through one of three routes:

- inherit an existing launch state and resolve the captured-site transaction
- receive Event 32 on a later global firing
- receive an explicit bridge from its owning event or scenario when that bridge is part of the accepted design

A new country that inherits no launch infrastructure begins at stage `0`. A new country that captures a site may control the physical infrastructure without having the technology, reserve, codes, or command control needed to use it safely.

## Human and AI reports

Human recipients receive one report after their country transaction is complete.

AI recipients receive no popup. Their program values, site records, decisions, and AI strategy are initialized silently.

In multiplayer:

- each human country receives its own country report
- no human receives another player's report
- one global news item may appear on the first global firing
- the event creates one global Event 32 history row
- report delay and ordering must not allow one player's option to change another player's setup package

Country reports have one acknowledgement option unless the report introduces a real emergency choice. Ordinary program setup should not force every human player through several ceremonial options.

## News behavior

The first global firing creates one news event about simultaneous missile proliferation.

The news event should communicate visible global evidence:

- launch structures appearing in many countries
- missile canisters and range activity
- governments sealing newly active sites
- military traffic and test plumes
- foreign observers unable to explain the common origin

The first-fire news item does not list raw technology levels, reserve counts, or future evolution names.

Repeat firings do not create global news by default. They use country reports and Event Logs. A later evolution may create its own news item when the change is globally visible.

## Event Logs integration

Event 32 must have full Event Logs coverage.

### History

One global history row is recorded for each Event 32 firing.

Recommended row data:

- event ID `32`
- event type Minor Repeatable
- date
- no actor
- firing count
- accepted recipient count for debug detail only
- repeatable weight and cap behavior through the normal event system

The row must not be duplicated once per recipient.

### Event Details

The Event Details premise should explain worldwide missile proliferation, repeated technological advancement, launch-site expansion, and the risk of command failure. It should not expose hidden chances, raw tuning values, future incidents, scenario bypasses, or implementation state.

### Evolutions

Each of the five global evolution tracks receives one catalog row and one logged unlock entry when it becomes active.

Country adoption, site accidents, rogue incidents, and individual retaliation choices are ordinary event or decision history. They are not separate evolution milestones unless the spec explicitly says otherwise.

### Default enable state

Event 32 remains disabled by default while its catalog status is To Be Reworked. The implementation change that satisfies this specification adds it back to the reworked-event default enable allowlist.

## Chaos effects

Suggested direct chaos changes:

| Event 32 action | Suggested chaos change |
| --- | --- |
| First global firing | `+10` |
| Later ordinary firing | `+4` |
| Rogue Launch Commands unlock | `+6` |
| Unreliable Guidance unlock | `+6` |
| Saturation Arsenals unlock | `+10` |
| Special Warheads unlock | `+15` |
| Automatic Retaliation unlock | `+20` |

Conventional strikes may add a small direct chaos increase when they hit major strategic targets or neutral territory. Special payloads use the existing nuclear, thermonuclear, chemical, biological, contamination, condemnation, and death ladders. Event 32 must not apply those shared changes twice.

## Baseline completion state

The baseline event is complete when:

- every valid recipient has one technology step
- every accepted country has a reserve and usable launch state
- country reports and first-fire news behave correctly
- repeated firings advance technology and strengthen programs
- conventional strikes can be prepared and executed
- damage, deaths, diplomacy, and cleanup work
- captured and inherited sites have a defined lifecycle
- AI can maintain and use the system
- Event Logs, Event Details, documentation, and catalog fields agree

No evolution is required for this baseline completion.
