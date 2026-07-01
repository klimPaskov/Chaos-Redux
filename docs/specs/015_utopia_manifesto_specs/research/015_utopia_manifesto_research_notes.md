# Event 015 research notes

## Purpose

These notes support the design of `utopia_manifesto`. They are not player-facing localisation.

## Provided project files read

I read the uploaded project files in `/mnt/data` before writing the spec package:

- all `chaosx_*.toml` subagent files
- `AGENTS.md`
- `CHAOS_REDUX_MECHANICS.md`
- all uploaded skill markdown files
- `hoi4-decisions-missions.md`
- `hoi4-focus-trees.md`
- `chaos_redux_events_catalog.csv`
- `chaos_redux_clusters_catalog.csv`
- `chaos_redux_scenarios_catalog.csv`

The event catalog row for ID 15 currently says `World Tension Subsides`, `Reserved`, `Minor Repeatable`, and `To Be Reworked`. The user's prompt changes that target to `utopia_manifesto`, ID 15, Minor Fire-Once.

## Thomas More and `Utopia`

Sources consulted online:

- Project Gutenberg page for `Utopia` by Saint Thomas More: https://www.gutenberg.org/ebooks/2130
- The Open Utopia, Book II: https://theopenutopia.org/full-text/book-ii-of-utopia/

Stable research points used:

- `Utopia` is a work by Thomas More, written in Latin and published in 1516.
- Book II describes a fictional island society with shared social customs, common stores, occupations, state governance, foreign policy, and war rules.
- The island has planned towns, shared agriculture, and no ordinary desire by towns to enlarge bounds.
- Agriculture is taught to everyone.
- Each person has a trade, and a person can be moved to a family practicing a preferred trade if their genius lies that way. A second trade can also be learned.
- Goods are brought into houses or stores, and households take what they need without payment.
- The Utopians give surplus to neighbors and use external treasure mainly for war or crisis.
- Overpopulation can lead to colonies on the neighboring continent. The same section contains a coercive claim that unused land can be taken for subsistence if inhabitants refuse the Utopian order.
- Utopian foreign policy distinguishes neighbors and friends, distrusts formal leagues, dislikes war glory, and prefers war only for defense, friends, oppressed nations, or injuries that demand remedy.

## Design implications

### Need versus greed

The user wanted territorial demands only when needed. The source material supports a mechanic where expansion requires a measured Need value. That value should include supply, industry, state capacity, blockade, population pressure abstractions, and loss of core land.

### Chosen labor versus public necessity

The user wanted people choosing their own jobs. The source material supports a Vocation Accord mechanic where citizens can choose or petition for trades. The state can override choices when public need demands it, but doing so lowers Consent and raises Overreach.

### Island society

The event should not require an island target. The tree should let coastal countries become literal island or harbor commonwealths and let landlocked countries build an inland island through rail, forts, supply hubs, and civic corridors.

### Common stores

Common stores translate naturally into decisions and missions that use civilian factories, support equipment, trains, convoys, infrastructure, supply hubs, and state modifiers. They should not be abstract free stability buttons.

### More's Problem

The source material contains generous welfare and labor ideas alongside a hard coercive territorial doctrine. This contradiction is useful for gameplay. The tree should make peaceful and coercive interpretations compete through Consent, Need, Surplus, and Overreach.

### War without glory

The military branch should be defensive and indirect rather than pacifist. It can include citizen drills, household guards, mercenary or indirect war methods, arbitration, and peacekeeping. Aggressive war without Need should hurt Consent and raise Overreach.

## Project instruction implications

The planning skill requires the deliverable to be a markdown spec package with separate prompt files and a final zip. It also requires direction-only localisation, asset coverage, achievements, focus tree architecture, AI behavior, decision maps, and a goal prompt under 4000 characters.

The event, focus, decision, asset, super-event, frame-animation, improvement-loop, and subagent skills all affected the final package structure. The package does not implement gameplay files. It is a planning handoff.

