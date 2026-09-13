# Presentation, Event Logs, and System Connections

## Presentation choice

Event 66 uses the standard country event surface.
The interface has four fixed option shells whose text and tooltips are populated from stored card records.
This surface matches the action the player takes and avoids a separate window for a one-step choice.

The event picture establishes the impossible worldwide surplus.
The dynamic option names carry the country-specific content.

## Popup structure

The visible popup needs:

- one event title
- one event description that works for every country and value family
- four option lines
- four effect tooltips
- a compact result path after selection when one or more items fail revalidation

At baseline an option line shows one short value name.
A pair joins two short names.
A triple joins three short names.
Providers must supply compact forms that fit an event option line.
Long institutional names belong in the tooltip.

Existing texticons should be used when they improve recognition and remain correct for the value.
A provider without a valid texticon uses text.
Event 66 does not require a new icon for every possible value.

## Option tooltip

A card tooltip should tell the player:

- the full value name or bundle contents
- the current value, stage, stock, or qualitative state when available
- the broad result of abundance
- the named state, subject, target, or mechanic when the card depends on one
- whether the owner classifies high values as dangerous, mixed, contextual, or unknown
- whether the effect is expected to persist

The tooltip does not reveal:

- provider IDs
- raw variables
- hidden event stages
- future secret consequences
- exact generation weights
- exact AI scores
- safe arithmetic ceilings
- reroll history

A harm label must be precise.
It should not call every contextual value dangerous or provide false certainty.

## Event title and description direction

The title should be brief and broad enough to cover political, military, economic, social, and crisis values.
The accepted event name is Abundance.

The description should present several kinds of excess appearing at once inside the country, with one becoming dominant through the player's choice.
The tone can carry mild absurdity because this is a global minor event, but the text must stay serious when a card represents mass suffering or an atrocity-linked pressure.

The description should not center a map, a conference table, a sealed dossier, or a generic broadcast.
It should describe warehouses, institutions, commands, ministries, markets, laboratories, and public systems reporting quantities that no longer behave normally.

## Option wording direction

The option line is primarily the short candidate or bundle identity.
The surrounding reaction can vary by harm class and owner tone:

- practical acceptance for useful ordinary values
- opportunistic confidence for power or stockpile values
- restrained alarm for harmful pressures
- bureaucratic absurdity for strange administrative values
- route-specific vocabulary for country mechanics
- uncertainty for contextual or poorly understood values

Final wording must be generated from stored candidates and must not contain generic placeholders.

## Event Details

Event Details should explain:

- every country receives four country-specific choices
- values come from mechanics that the country currently possesses
- harmful values remain eligible
- later evolutions add strange weighting, pairs, and triples
- the event belongs to three Sudden Abundance severity slots

The details text should describe the premise and visible rules.
It should not list the full provider registry, raw magnitude formulas, audit requirements, or hidden values.

Evolution previews use their accepted names:

- Strange Abundance
- Abundance Comes in Pairs
- Everything in Excess

The previews explain the visible change without exact probabilities.

## Event history

One Event 66 history row is recorded for the global wave.
The actor is global or absent.
A random recipient country must not become the event actor.

The history row records:

- date
- Event 66 identity
- direct or cluster source
- highest active evolution stage
- highest cluster profile when relevant
- number of participating countries

Country choices do not create hundreds of global history rows.
Technical country receipts remain available for debugging, achievements, and completion evidence.

## Evolution history

Each enabled evolution is recorded once through the shared evolution pipeline when a wave first uses it.
The actor is global.
A disabled evolution does not record, change card generation, or unlock related achievement conditions.

When one wave activates several eligible stages, the log order follows Evolution I, Evolution II, then Evolution III.

## Cluster details

Sudden Abundance details show Event 66 three times with Low, Medium, and High severity.
The display should make clear that overlapping Event 66 slots merge into one wave.

Cluster history records the coalesced Event 66 member once.
The technical details can retain selected slot count and highest severity for audit purposes.

## Localisation ownership

Event implementation owns final player-facing text for:

- title and description
- four dynamic option shells
- card tooltips
- partial-result follow-up
- Event Details premise
- evolution names and details
- cluster name and details
- cluster member labels
- achievement names and descriptions
- provider risk and status phrases
- debug rejection reasons that appear in developer surfaces
- spreadsheet fields that mirror in-game wording

Provider owners supply their own candidate names and owner-specific explanations.
Event 66 supplies shared sentence frames and separators.
A provider cannot rely on Event 66 to invent a name for its mechanic.

## Related event boundaries

Event 66 overlaps many abundance-themed catalog ideas, but it has a distinct role.
It is global, country-local, choice-driven, repeatable, and provider-extensible.
It does not replace fixed events that have their own narrative, targeting, escalation, or aftermath.

| Event | Existing identity | Boundary with Event 66 |
| --- | --- | --- |
| 18 Resources Found | Persistent discovery and development of a state deposit | Event 66 may expose resource abundance through a provider, but it does not run the Resources Found chain |
| 29 Riches Found | One country's wealth discovery and related crisis | Event 66 can increase a wealth value only when its owner exposes it |
| 34 Industrial Boom | A major economic boom with overheating and collapse | Factory or industrial capacity abundance does not create the Industrial Boom lifecycle unless its owner permits activation |
| 42 Equipment from heavens | Fixed equipment abundance | Event 66 can roll concrete stockpiles among many other values |
| 54 Gift from scientists | Random technology grant | Event 66 uses value providers and does not grant a technology unless a research resource provider defines that value |
| 55 Great Infrastructure Project | Infrastructure expansion | Event 66 can affect a capacity or construction value without replacing a map project chain |
| 56 The Navy | Naval expansion | Event 66 can increase naval resources, stockpiles, or capacities without creating the event's full navy package |
| 57 The Radar | Radar expansion | Event 66 can affect radar-linked capacity only through a safe owner provider |
| 58 The Industrial Complex | Factory expansion | Event 66 remains a random four-choice wave, while Event 58 has a fixed industrial identity |
| 64 Border Fortifications | Fortification abundance and defensive depth | Both belong to Sudden Abundance, but Event 64 always produces fortifications |
| 82 Law upgrade | A law change | A law itself is not a numeric value unless an owner exposes a coherent abundance interpretation |
| 83 Agency upgrade | Intelligence agency development | Event 66 can use agency currencies or capacities, while Event 83 owns upgrade progression |
| 84 PP | Fixed Political Power grant | Political Power is one candidate among the dynamic Event 66 space |
| 85 XP | Fixed experience grant | Event 66 can select Army, Navy, or Air Experience separately or in bundles |
| 89 Tech sharing | Research-sharing network | Event 66 does not create diplomacy or network membership through a scalar grant |
| 98 New Ore | New resource deposit | Event 66 can produce a state-resource surplus through a provider without taking over the New Ore event identity |
| 103 Conscription | Conscription change | Manpower abundance does not silently change conscription law unless the provider defines that relation |
| 104 Stability or War support | A fixed tradeoff between two gauges | Event 66 rolls either value independently and can combine them only through random later-evolution bundles |
| 114 Fuel crisis | Worldwide removal of fuel | Fuel abundance can counter its current state, but it does not erase Fuel Crisis history or owner effects |
| 132 Investment | Investment event concept | Event 66 can affect investment currencies when a provider exists |
| 135 Equipment choice | Equipment choice event concept | Event 66 uses the shared provider pool and four country-specific cards |
| 137 Research Investment | Research investment event concept | Event 66 can increase an exposed research currency without duplicating that event's route |

## Shared country classifiers

Event 66 uses shared country classification only where it answers a cross-system question.
Ordinary civilian providers can require normal civilian systems.
Nonhuman providers can expose their own values.
Event-specific participant and candidate rules remain in Event 66 ownership.

The event must not copy the full special-country or nonhuman registry into a private trigger.

## Shared dynamic helpers

The general dynamic-effect registry contains neutral helpers used across unrelated systems.
Event 66 provider orchestration is owned by Event 66 because it exists to serve this event.

A helper should move into the neutral shared registry only when another unrelated system becomes a real caller.
Any such move requires a documented public contract and a call-site audit.

## Catalog alignment

The current export-only Events row for ID 66 must be replaced in the authoritative workbook after implementation text is final.
The old `CIC` name and random-major market description are obsolete under this accepted design.

The Events row needs:

- Event Name: Abundance
- Details: final in-game Event Details premise
- Evolution I: Strange Abundance
- Evolution II: Abundance Comes in Pairs
- Evolution III: Everything in Excess
- Type: Minor Repeatable
- Chaos level: `1`
- Cluster: Sudden Abundance
- Member Severity: Low, Medium, High, represented without losing the three logical slots
- Status: unchanged until implementation evidence supports the next catalog state

The Clusters sheet needs a Sudden Abundance row and ordered Event 66 member entries.
The authoritative workbook is the only editable catalog source.
The three CSV files remain generated exports.
