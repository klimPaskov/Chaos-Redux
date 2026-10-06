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
| Open Gates | A district hands itself to the enemy without a battle | Up | +2 | none | The first incident per host per war only. Later incidents in the same war add nothing. | Generic sources do not record control transfers without combat | none |
| Capitulation under the Fifth Column | The host surrendered from inside as much as from the front | Up | +2 at Defecting, +3 at Collapsing | +1 more when the host is a major power | Once per host per war | Generic capitulation adds its own +1 or +3 for the capitulation itself. This row measures only the internal collapse that drove it. | none |
| Government installed through Event 097 | A prepared regime replaces a defeated government | Up | +2 | +1 more for an installer's first government | Once per installation, and once per original tag per war | The wiki documents the generic puppet source only for peace conferences, so this row assumes it does not fire for a scripted collaboration government. If live testing shows that it fires, this row adds nothing for that installation and only the first-government bonus and the milestone rows remain. | Government removed by restoration, below |
| Installer reaches three governments | One power runs a system of prepared regimes | Up | +3 | none | Once per installer per campaign | none | none |
| Competing orders | At least two powers each run several prepared regimes, which reorganizes world politics | Up | +5 | none | Once per campaign, together with the super-event | none | none |
| Turned Regime | A prepared government changes masters during a war | Up | +3 | none | Once per government per war, and at most two per campaign from this row | Generic sources do not record a subject changing sides | none |
| Host survives Collapsing | A host that reached Collapsing ends the war without capitulating | Down | -1 | none | Once per host per war | Generic peace Chaos counts the end of the war. This row measures the recovery of a state apparatus that was serving the enemy. | Counterpart of Host reaches Collapsing |
| Government removed by restoration | A prepared government is overthrown by its own country through Event 095 or another restoration route | Down | -2 when removed by an uprising, -1 when removed by a peace-conference liberation | none | Once per government | A peace-conference liberation also triggers generic liberation or freed-country Chaos, so the Event 097 reduction is smaller on that route | Counterpart of Government installed |

## Values that never change Chaos

- Evolution eligibility, MTTH completion, activation, logging, or any evolution flag.
- Stance choices, vetting spirits, and every Divided Loyalties action.
- Prepared cadres at capitulation, because the generic capitulation source already counts the capitulation and the cadres change only how the occupation proceeds afterward.
- Each individual seat after the milestones above, because capture and war Chaos already count the fighting.
- Arm the Installed Administration.
- Collaborators Unmasked.

## Event-wide rate guard

The recurring rows share one rolling cap: Host reaches Collapsing, Open Gates, Capitulation under the Fifth Column, Government installed, and Turned Regime together add at most +10 Chaos in any 365 days. A row that would pass the cap adds only the remainder, and the history entry still records the outcome. The one-time milestone rows, the firing row with its own lifetime cap, and the reversal rows are outside this cap.

## Lifetime perspective

A planning estimate suggests that a high-Chaos world war without the rate guard could produce around 35 to 40 Event 097 Chaos per year, which is too much for one minor event. With the guard, the recurring rows stay at or below +10 per year, and the milestone and firing rows add a bounded total over the campaign. The real lifetime contribution is an output of probability scenario P27, not a figure fixed here, and it should stay comparable to a regional crisis rather than drive a calm world toward collapse on its own.

## Wiring

Every row uses the shared Chaos add path with a signed amount, an Event 097 history reason, and the custom-reason marker. Rows with a natural actor, such as the installer or the host, save that actor for the history entry. The firing and deepening rows have no actor.

History reasons are new entries in the special reason block of the Chaos Meter constants. Source shows the block ending at id 221, so Event 097 reasons start at the next free id at implementation time. Each reason needs a row in the Chaos history reason selector and a localisation key, which Event 097 keeps in its own localisation file. Event-owned amounts live in the Event 097 constant group, not in the shared delta table.

The Chaos add path is blocked while the settings disable the meter. Event 097 does not work around that block.

## Validation

The implementation must show, through the shared Chaos history, that each row fires at its outcome, that guards stop repeats, and that no row duplicates a generic source for the same fact. The probability audit should include a long-campaign scenario that sums the expected Event 097 Chaos.
