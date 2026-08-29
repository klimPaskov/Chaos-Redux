# Event logs, evolution, and presentation

## Event chain anatomy

Event 26 should use a compact chain with distinct internal roles.

| Role | Function |
| --- | --- |
| Entry event `chaosx.nr26.1` | Receives automatic or manual selection and reserves or immediately activates Event 26 |
| Player-facing report event | Broadcasts the Friday sale to human-controlled countries |
| Hidden activation helper | Snapshots the tier, applies the global source, records history, and starts expiry |
| Hidden expiry helper or timed source | Removes the active source on the next daily tick |
| Optional status refresh helper | Adds or refreshes the temporary human-player status after tag changes or joins |

The final subevent numbers can follow existing namespace availability. The canonical entry remains `chaosx.nr26.1`.

## Actor and broadcast

The event is actorless. The selecting country does not cause the sale and should not appear as its owner.

The history row and Event Details should present a global identity. If the shared event log supports actorless rows, use that route. Do not assign a random country flag merely to fill the actor field.

The player-facing report should reach each human-controlled country once. AI countries do not need a popup.

## History timing

The event history is recorded on activation Friday.

The history row includes:

- Event ID 26
- Black Friday event name
- Minor Fire-Once type
- Friday activation date
- actorless global context
- 50 percent or 75 percent payload for detail display when the current log contract supports payloads

Reservation does not create a history row.

## Event list states

The Events tab should present truthful status.

| State | Weight or status display |
| --- | --- |
| Below 200 chaos | `N/A` |
| Eligible and unfired | Current live weight |
| Reserved | `Reserved` or an equivalent pending state, not zero |
| Active | `Active Today` or equivalent |
| Fired and expired | Fired state with zero future weight |
| Disabled | Disabled state through the existing toggle contract |

If the shared row cannot display words in the weight field, add a concise status line in Event Details and preserve the existing row layout.

## Event Details premise

Event Details should describe the premise without listing every covered cost family. It should explain that a global Friday sale briefly lowers government, military, intelligence, and procurement costs.

The detail surface should show:

- minimum chaos tier
- fire-once classification
- current availability or pending status
- baseline 50 percent sale premise
- one Evolution I row
- active discount and expiry when currently active

It should not expose internal basis points, queue latches, helper names, coverage classes, or unsupported engine surfaces.

## Evolution I: Seventy-Five Percent Off

Evolution I is a pre-fire severity evolution.

### Eligibility

- Current chaos is at least 600 when the sale activates.
- Event 26 is enabled.
- Evolution I is enabled through the shared evolution control.

### Result

- Snapshot a 75 percent discount.
- Record one Event 26 evolution entry.
- Keep the same one-day duration, Friday rule, rounding, composition, coverage, and expiry.

### Disabled evolution behavior

If Evolution I is disabled, Event 26 still fires at baseline strength even when chaos is 600 or higher. No evolution entry is recorded and no evolution flag is set.

### Evolution log context

The evolution entry uses:

- parent event ID 26
- one stable evolution type
- stage 1
- Chaos Tier display tier
- no actor

The context must be set before the shared logger is called. Disabled evolution logic must not set recorded flags that later displays read.

## Active status marker

Human-controlled countries should receive a short temporary status marker during the active day. The marker is presentation support, not the source of the discount.

The marker should show:

- active sale percentage
- sale end on the next daily tick
- positive minimum-cost rule
- reminder that requirements and cooldowns remain active

The marker expires automatically with the sale. A tag-switch or join refresh may add it to the current human country when the global source is already active.

## Cost tooltip direction

When a cost surface supports dynamic text, present the final price first and explain the sale in one short line. When enough space exists, include the ordinary current price.

The text must distinguish:

- ordinary current cost
- Black Friday price
- minimum-unit rounding when relevant
- blocked requirement unrelated to cost

A cost that remains one because of the minimum rule should not claim that the arithmetic result was one.

## Event popup writing direction

### Viewpoint

The description observes the sale through civilians, quartermasters, ministry clerks, officers, intelligence offices, and suppliers.

### Visible information

The player knows the percentage, the one-day duration, and the broad scope. The text should not enumerate internal adapter categories.

### Humour mode

Use dry administrative absurdity and period retail language. The same sale reaches laws, appointments, command actions, equipment, and government projects.

### Avoid

- modern e-commerce language
- current retailer names
- internet culture
- fabricated quotations
- generic crisis language
- long mechanic lists in the description
- claims that the sale changes requirements, time, output, or penalties

### Option direction

Use one short acknowledgment from a purchasing office or government. It should convey urgency and opportunism. Final wording belongs to implementation and localisation review.

## Localisation surfaces

Implementation must align:

- event title, description, and option
- temporary status title and description
- Event Details title and premise
- Event list status text
- Evolution I name and detail text
- cost-source label and tooltip text
- achievement text
- debug event name
- spreadsheet mirror fields

All localisation files must follow repository encoding and key rules. Broad visible text requires a localisation audit before completion.
