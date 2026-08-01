# Event 20 Event Chain Map

All event numbers after the canonical entry are planning allocations. The implementation agent must inspect existing namespace use before final assignment.

| Working event | Role | Primary actor | Player-facing | Repeats |
| --- | --- | --- | --- | --- |
| `chaosx.nr20.1` | canonical random-event entry and origin selection | global then origin owner | hidden setup plus owner report dispatch | no |
| `chaosx.nr20.2` | early owner recognition | origin owner | yes | no |
| `chaosx.nr20.3` | late owner recognition after failed surveillance | origin owner | yes | no |
| `chaosx.nr20.4` | first neighboring threat alert | exposed neighbor | yes | limited by country |
| `chaosx.nr20.5` | first foreign infection | new infected country | yes | limited by country |
| `chaosx.nr20.6` | first state enters Severe Crisis | state owner | yes | first global plus selective local reports |
| `chaosx.nr20.7` | first successful Containment | state owner | yes | first global, later local only |
| `chaosx.nr20.8` | relapse | state owner | yes | yes with cooldown |
| `chaosx.nr20.9` | first Cured state | state owner | yes | first global, later log only |
| `chaosx.nr20.10` | ten million event-attributed deaths | global | news | no |
| `chaosx.nr20.11` | global eradication | leading countermeasure country | news or report | no per natural outbreak cycle |
| `chaosx.nr20.20` | Evolution I resolution | global | report or news | no |
| `chaosx.nr20.21` | country adaptation milestone | country | yes | limited by country |
| `chaosx.nr20.30` | Evolution II resolution | global | news | no |
| `chaosx.nr20.31` | first overseas infection | destination owner | news | no global, local later |
| `chaosx.nr20.40` | Evolution III resolution and first rat emergence | basin owner and new rat tag | report plus news | no |
| `chaosx.nr20.41` | later rat emergence | basin owner and new rat tag | selective report | yes with basin and global caps |
| `chaosx.nr20.42` | rat dominance standoff | superseded by the two-tag correction; no third Rat Nation is created | no separate event | no |
| `chaosx.nr20.43` | state-level brood absorption | reusable RTA carrier | report or log | yes |
| `chaosx.nr20.44` | rat resurgence | affected human owner and rat tag | yes | limited by basin cooldown |
| `chaosx.nr20.45` | hierarchy acknowledgement after the RTA route choice | RTA | yes | one per carrier |
| `chaosx.nr20.50` | Evolution IV candidate selection | leading rat country | yes | no per coronation cycle |
| `chaosx.nr20.51` | Rat King transfer and coronation | Rat King | yes | no |
| `chaosx.nr20.52` | coronation super-event launcher | global | super-event | no |
| `chaosx.nr20.53` | disputed crown crisis | Rat King | yes | limited |
| `chaosx.nr20.54` | successful Royal Node strike report | responding human country | yes | one per completed strike |
| `chaosx.nr20.55` | failed Royal Node strike and counterfire report | responding human country | yes | one per failed strike |
| `chaosx.nr20.56` | emergency countermeasure mission timeout | responding human country | yes | one per failed mission |
| `chaosx.nr20.57` | Absolute Crown Hunger crisis | Rat King | yes | one route crisis |
| `chaosx.nr20.58` | Council of Burrows Hunger crisis | Rat King | yes | one route crisis |
| `chaosx.nr20.59` | Black-Breath Hierophancy Hunger crisis | Rat King | yes | one route crisis |
| `chaosx.nr20.64` | successful Crown Strike report | responding human country | yes | one per completed strike |
| `chaosx.nr20.65` | Crown Strike timeout and royal recovery report | responding human country | yes | one per failed strike |
| `chaosx.nr20.60` | Evolution V resolution | Rat King | yes | no |
| `chaosx.nr20.61` | continent selected | Rat King | yes | one active target |
| `chaosx.nr20.62` | continent crowned | Rat King and human world | news | no per target |
| `chaosx.nr20.63` | world-end terminal launcher | global | super-event | no |
| `chaosx.nr20.70` | Rat Nations defeated | leading human actor | news or report | no per rat phase |
| `chaosx.nr20.71` | Rat King defeated | global and response hosts | news or super-event if global | no per king cycle |
| `chaosx.nr20.72` | global reconstruction milestone | leading recovery actor | report | limited |
| `chaosx.nr20.73` | Royal Basin defeat aftermath choice | first human response host | yes | one per King defeat |
| `chaosx.nr20.74` | Royal Burrow sealing success | sealing operation owner | yes | one per completed site |
| `chaosx.nr20.75` | Royal Burrow sealing timeout | sealing operation owner | yes | one per failed site |
| `chaosx.nr20.80` onward | weaponization iteration pool when event events are used | project owner | yes | project controlled |
| `chaosx.nr20.90` | triggerable scenario launch report after bootstrap | global and affected human players | yes | no |

Implementation status note: the current worktree defines and calls `.45`, `.57-.59`, `.64-.65`, and `.71-.75`; these rows are implemented static event evidence rather than future allocations. Reconstruction `.72` still follows global eradication logic rather than earned aftermath sealing. This matrix remains the behavioral contract and does not claim live-game validation.

## Runtime families

### Mortality pulse

Processes registered active Black Plague states, applies one population loss effect, updates Deaths and event totals, and schedules the next state update.

### Spread pulse

Processes registered source states and valid route targets. It creates Threatened or Incubating status and calls the shared mapmode refresh.

### Containment pulse

Updates disease load, containment, treatment, relapse, and state phase transitions.

### Evolution pulse

Evaluates only the next unrecorded evolution against current world and event state. It uses dynamic mean-time pacing and cancels invalid contexts.

### Rat growth pulse

Processes active rat countries, calculates one capped batch, and creates unlocked unit templates.

### Rat dominance pulse

Evaluates only adjacent active rat pairs, maintains one standoff per pair, and transfers the weaker package when the countdown resolves.

### Triggerable scenario bootstrap

Builds the intensity-scaled continent, state, Rat Nation, and Rat King package with ordinary pulses suspended. It records Evolutions I through IV once, sets the Chaos floor, performs one full mapmode rebuild, and clears every temporary bypass before live play resumes.

### World-end readiness check

Runs after Rat King focus completion, continent state changes, capital changes, and Evolution V progress. It does not require a whole-world daily scan.

## Event log ownership

- normal event history records Event 20 once at the initial firing
- baseline milestones can create history details without registering new random events
- the five evolutions use the shared evolution logger
- Evolution III uses the first Rat Nation as actor
- Evolution IV and V use the Rat King as actor
- triggerable scenario records one scenario history entry and never duplicates ordinary event or evolution rows
- world-end scenario records the terminal scenario flag and super-event history
