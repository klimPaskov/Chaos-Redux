# Event 097 Collaboration: Chaos Impact Map

Event 097 is destabilizing. It makes every war end faster, every occupation easier, and late in its evolution it replaces defeated governments with prepared regimes. It must therefore feed the Chaos Meter through its own concrete consequences. Evolution activation itself never changes Chaos.

The shared Chaos Meter already reacts to wars, peace, capitulations, annexations, puppets, liberations, freed countries, exiles, coups, and deaths. Event 097 adds Chaos only where its own networks change an outcome in a way those generic sources do not measure. Each row names the distinct abnormal significance that justifies it.

All values are tuning anchors in one constant group. Every change is recorded through the shared Chaos history path with an Event 097 reason.

## Impact table

| Milestone or outcome | Why global Chaos changes | Direction | Starting magnitude | Dynamic factors | Repeat guard | Shared-source overlap | Reversal or containment counterpart |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Firing applies layers | Every country now holds prepared collaborators inside every other country, which is a real new loss of political trust worldwide | Up | +1 at the base layer, +2 at the Deep Networks layer | Layer size | Once per firing, and this row stops adding after a lifetime total of +10 | No generic source measures collaboration | None. Networks do not vanish, so their creation is not refunded |
| Deep Networks deepening tranche | Existing networks deepen across the whole world at once | Up | +1 | none | Once per campaign | none | none |
| First seated administration | The first time a prepared local administration takes over a captured state | Up | +1 | none | Once per campaign | War and capture Chaos count the fighting, not the administration that changed sides | none |
| Seats reach five hosts | Prepared administrations have appeared in five different countries | Up | +2 | none | Once per campaign | as above | none |
| Seats reach fifteen hosts | Prepared administrations are a worldwide pattern | Up | +3 | none | Once per campaign | as above | none |
| Host reaches Collapsing | A state apparatus has begun serving the enemy before defeat | Up | +1 | +1 more when the host is a major power | Once per host per war, and at most +5 from this row in any 365 days | Capitulation Chaos has not happened yet, and war Chaos counts the war itself | Host survives Collapsing, below |
| Open Gates | A district hands itself to the enemy without a battle | Up | +2 | none | At most three per host per war, matching the incident cap | Generic sources do not record control transfers without combat | none |
| Capitulation under the Fifth Column | The host surrendered from inside as much as from the front | Up | +2 at Defecting, +3 at Collapsing | +1 more when the host is a major power | Once per host per war | Generic capitulation adds its own +1 or +3 for the capitulation itself. This row measures only the internal collapse that drove it. | none |
| Government installed through Event 097 | A prepared regime replaces a defeated government | Up | +2 | +1 more for an installer's first government | Once per installation | The wiki documents the generic puppet source only for peace conferences, so this row assumes it does not fire for a scripted collaboration government. If live testing shows that it fires, this row adds nothing for that installation and only the first-government bonus and the milestone rows remain. | Government removed by restoration, below |
| Installer reaches three governments | One power runs a system of prepared regimes | Up | +3 | none | Once per installer per campaign | none | none |
| Competing orders | At least two powers each run several prepared regimes, which reorganizes world politics | Up | +5 | none | Once per campaign, together with the super-event | none | none |
| Turned Regime | A prepared government changes masters during a war | Up | +3 | none | Once per government per war, and at most two per campaign from this row | Generic sources do not record a subject changing sides | none |
| Host survives Collapsing | A host that reached Collapsing ends the war without capitulating | Down | -1 | none | Once per host per war | Generic peace Chaos counts the end of the war. This row measures the recovery of a state apparatus that was serving the enemy. | Counterpart of Host reaches Collapsing |
| Government removed by restoration | A prepared government is overthrown by its own country through Event 095 or another restoration route | Down | -2 when removed by an uprising, -1 when removed by a peace-conference liberation | none | Once per government | A peace-conference liberation also triggers generic liberation or freed-country Chaos, so the Event 097 reduction is smaller on that route | Counterpart of Government installed |

## Values that never change Chaos

- Evolution eligibility, MTTH completion, activation, logging, or any evolution flag.
- Stance choices, vetting spirits, and every Divided Loyalties action.
- Prepared cadres at capitulation, because the capitulation row already covers the outcome.
- Each individual seat after the milestones above, because capture and war Chaos already count the fighting.
- Arm the Installed Administration.
- Collaborators Unmasked.

## Lifetime perspective

A long campaign with four firings, all four evolutions, several Fifth Column wars, and a competing-orders world produces roughly 30 to 45 points of Event 097 Chaos over many years. This is a meaningful contribution to a campaign's climb, comparable to a regional crisis, without letting one repeatable event push a calm world toward collapse by itself. The firing row's lifetime cap protects against repeated firings in long games.

## Wiring

Every row uses the shared Chaos add path with a signed amount, an Event 097 history reason, and the custom-reason marker. Rows with a natural actor, such as the installer or the host, save that actor for the history entry. The firing and deepening rows have no actor.

History reasons are new entries in the special reason block of the Chaos Meter constants. Source shows the block ending at id 221, so Event 097 reasons start at the next free id at implementation time. Each reason needs a row in the Chaos history reason selector and a localisation key, which Event 097 keeps in its own localisation file. Event-owned amounts live in the Event 097 constant group, not in the shared delta table.

The Chaos add path is blocked while the settings disable the meter. Event 097 does not work around that block.

## Validation

The implementation must show, through the shared Chaos history, that each row fires at its outcome, that guards stop repeats, and that no row duplicates a generic source for the same fact. The probability audit should include a long-campaign scenario that sums the expected Event 097 Chaos.
