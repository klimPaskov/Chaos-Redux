# 9. Presentation, Event Logs, and Assets

## Visible event family

The Event 53 chain needs a compact visible event family:

| Working event role | Purpose |
| --- | --- |
| Initial appearance | Selects and opens the first demand for the target |
| Recurring appearance | Opens later demands using dynamic location and demand text |
| Payment resolution | Confirms that the current demand was taken and the man vanished |
| Refusal transition | Connects the refusal to the selected consequence without revealing registry logic |
| Direct consequence report | Used only when the selected Event 53-owned package has no better owner presentation |
| Target-loss closure | Ends the chain when the target ceases to exist or use normal civilian systems |
| Evolution milestone | Records a real evolution and adjusts behavior without explaining hidden formulas |

Hidden scheduler, pool builder, adapter, receipt, and cleanup events must remain hidden.

## Appearance locations

Each visit chooses one valid secure-location setting. The setting changes presentation only and receives no extra mechanical ballot.

Recommended location family:

### Executive office

Use when the country has a normal head-of-government setting. The man is already seated or standing inside the most protected private office.

### Locked archive or cabinet room

Use for a government with a strong administrative state or when the current demand concerns Political Power, Stability, War Support, or civilian capacity.

### Military bunker or command room

Use more often during war, mobilisation, or military demands. The room should be physically secured, with guards and access controls that failed to record his arrival.

### Intelligence headquarters

Use when an intelligence agency or security institution exists. The location should underline the failure of surveillance without turning the event into an investigation path.

### Restricted government meeting

Use when several senior institutions are present. The man is already in the room before the meeting begins, or enters through a door that nobody remembers opening.

The implementation can add more settings if they preserve the same ordinary, secure, period-appropriate identity. Location variety must not create extra demands, consequences, or hidden weights.

## Appearance writing direction

The event description should establish:

- the exact secure setting
- the physical fact that he is already present
- one or two concrete signs that normal access controls failed
- the demanded resource and exact amount
- his calm refusal to explain anything

The text should not open with a broad global summary. It should stay inside the room and describe what the government can observe.

Later visits can refer to changed locks, replaced guards, sealed rooms, or revised procedures. These measures have failed before the popup begins. The text must not offer a security decision or imply that another attempt could stop him.

## Option direction

### Payment stance

The voice belongs to the selected government. The tone should be direct compliance mixed with practical unease. The option means that the full displayed demand is paid and no punishment follows from this visit.

Avoid heroic, philosophical, or comic wording. Avoid any promise that this ends the chain.

### Refusal stance

The voice belongs to the selected government. The tone should be a plain rejection, hardened calculation, anger, or exhausted resistance depending on country and campaign state.

The option means that Event 53 rolls one valid consequence package. The button must not reveal the selected package or list the pool.

### Inability to pay

When payment is disabled, the tooltip explains the exact resource shortfall or protected floor. The visible refusal can acknowledge that the demand cannot be met, but it remains mechanically the same refusal transaction.

Final option wording belongs to implementation and localisation review.

## Consequence presentation

Borrowed systems should use their real gameplay reports when those reports can run without source-event firing or opening presentation.

Event 53 should not duplicate a disaster report, civil-war opening, outbreak report, embargo notice, or Independence Wave release report with another large popup.

A short Event 53 transition can establish that the consequence followed the refusal. It should not explain causation.

Direct Event 53-owned packages need one concise report or visible state change. The report names the practical damage and current crisis. It does not expose the package ID, roll, evolution formula, or registry size.

## Event History

The parent firing creates one Event 53 History row with the selected country as actor.

The row should identify:

- Event 53
- the selected actor
- the date of first appearance
- Minor Fire-Once classification through existing UI behavior

Recurring visits do not create ordinary History rows.

Borrowed packages do not create source-event History rows. Owner operational reports remain allowed outside the random-event History ledger.

## Evolution log

Each enabled Event 53 evolution milestone records one shared evolution entry with:

- Event ID 53
- selected country as actor
- Event 53 evolution type
- correct stage
- correct Chaos tier display
- date

The milestone itself gives zero Chaos.

If the event first fires after several enabled thresholds have already been crossed, the setup records the enabled milestones in order without opening several redundant evolution popups.

Disabled milestones are not recorded and do not set recorded flags.

## Event Details

Event Details should present the public premise:

- an unexplained man repeatedly enters secure locations
- he makes demands
- payment settles one visit
- refusal has dangerous consequences

When the shared UI supports dynamic status, it can show:

- whether the chain is active
- the current target country
- the date of the latest completed visit

It should not show:

- demand formulas
- visit interval formulas
- current valid package count
- consequence registry entries
- exact consequence odds
- hidden adapter status
- internal counters
- future evolution behavior
- source-event bookkeeping rules

Evolution previews describe visible changes in his demands and the scale of refusal consequences without listing exact package IDs.

## Catalog fields

The current Event 53 catalog Details field is stale and describes a scientific breakthrough. It must be replaced after final in-game Event Details localisation exists.

The catalog worker should mirror final player-facing Event Details and evolution wording from the game. It should not invent text from this planning file.

The row retains:

- ID `53`
- name Mysterious Man
- Minor Fire-Once
- Chaos level `1`
- no cluster ID
- no member severity

Status changes only after implementation evidence supports the new status.

## Asset family

Event 53 needs a small generated report-event image family. These are scene assets, not character portraits.

Recommended assets:

| Asset working name | Scene | Suggested runtime basename |
| --- | --- | --- |
| Office appearance | The man inside a protected executive office | `event_053_mysterious_man_office` |
| Archive appearance | The man waiting inside a locked government archive | `event_053_mysterious_man_archive` |
| Bunker appearance | The man inside a wartime command bunker | `event_053_mysterious_man_bunker` |
| Intelligence appearance | The man inside an intelligence headquarters | `event_053_mysterious_man_intelligence` |
| Cabinet appearance | The man present at a restricted government meeting | `event_053_mysterious_man_cabinet` |

Use the exact report-event canvas and processing pattern confirmed from the installed vanilla and Chaos Redux reference family. The working target is `210x176`, subject to local consumer verification before final conversion.

## Visual direction

The images should resemble period documentary photography from the late 1930s or early 1940s. Use monochrome, restrained sepia, or the exact treatment established by the selected report-event references.

The man should appear:

- ordinary
- calm
- cleanly dressed in a plain period suit or overcoat
- neither wealthy nor impoverished in an exaggerated way
- recognizably the same person across the set
- physically present in the secure room
- unarmed
- without insignia or readable documents

The scene should communicate impossible access through locked doors, guards outside, secure furnishings, maps or cabinets, restricted equipment, and the reactions of officials.

Avoid:

- supernatural light
- visible teleportation
- distorted anatomy
- glowing eyes
- occult marks
- masks
- villain poses
- modern electronics
- readable generated text
- cinematic colour grading
- a portrait crop that hides the secure location
- comedy or meme styling

## Asset production route

Use `chaosx_generated_event_art` because the scenes are fictional, period-staged, and do not depict a real historical person.

The asset worker should:

1. inspect the canonical report-event reference family
2. create one approved identity anchor for the fictional man
3. generate the five location scenes with consistent identity and period detail
4. preserve source PNGs and prompt evidence
5. process exact report-event previews
6. convert final DDS files through the repository converter
7. create a contact sheet for identity and scene consistency
8. write manifest and GFX handoff data

The asset worker does not edit event or GFX files. The implementation agent wires the approved sprites.

## UI and audio treatment

The event uses normal event popups and existing event presentation. Its gameplay does not need a dedicated scripted GUI.

The core asset need is the report-event image family. Final implementation should use the existing event sound pattern that fits ordinary country events, without creating a separate super-event package.

These scope choices belong to the event's restraint. A custom window, animated portrait, or global announcement would draw attention away from the direct recurring choice.
