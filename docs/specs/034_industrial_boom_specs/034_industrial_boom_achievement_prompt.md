# Event 34 Industrial Boom achievement implementation prompt

## Assignment

Implement the complete Event 34 achievement package described in `034_industrial_boom_spec_part_10_achievements_acceptance.md`. Treat the specification as the source of truth for route coverage, tracking, disqualifiers, difficulty, visibility, and icon direction. Do not replace the mapped achievements with easier final-state checks.

This prompt covers achievement implementation and its direct dependencies. It does not authorize a redesign of Event 34.

## Required preparation

Read these files before editing:

- `AGENTS.md`
- the complete Event 34 specification pack
- `chaos-redux-events`
- `chaos-redux-event-assets`
- the current repository achievement registry and localisation
- the installed vanilla achievement definitions and relevant local documentation
- the Event 34 implementation, tuning constants, decisions, evolution state, landing outcomes, regional project ledger, Event 35 inheritance record, and event history surfaces

Inspect the current Chaos Redux achievement naming, triplet asset, visibility, eligibility, and tracking patterns before allocating final identifiers. Working labels in the specification are directions, not final localisation.

## Achievement set

### Managed Expansion

Purpose: reward a controlled baseline landing that converts extraordinary growth into lasting development without relying on an evolved opening.

Required story state:

- The player country receives Event 34 at baseline.
- The boom reaches a controlled landing.
- At least one structural project completes.
- The country retains a meaningful legacy tier.
- The country never reaches the terminal crash threshold during that firing.

Disqualifiers:

- Any Event 34 evolution active during that firing.
- Event 35 beginning from that boom.
- Debug, forced-success, or scenario bypass state when the project contract excludes achievement credit.

Tracking need: preserve the firing identity, entry evolution, peak Overheating, completed project proof, landing result, and depression handoff result until the achievement check resolves.

Icon direction: a factory complex passing through a narrow cooling ring into an orderly rail network. Keep the result readable at achievement size.

### The Miracle Holds

Purpose: reward mastery of Evolution II under sustained pressure.

Required story state:

- Evolution II is active for the player country.
- Every designated Miracle Region reaches its durable completion state.
- The boom reaches a controlled landing.
- Event 35 does not begin from the firing.
- No Miracle Region is abandoned, lost at resolution, or converted into a depression scar.

Disqualifiers:

- Fewer than the required valid Miracle Regions were ever designated because of an invalid target pool. In that case the achievement remains unavailable and the requirement text must explain why.
- A state exploit that transfers a completed project away and back without preserving project continuity.
- Debug completion or direct variable injection.

Tracking need: use the registered project ledger and country firing identity. Do not infer completion only from current buildings.

Icon direction: several illuminated industrial cities linked by rails, with one stable central turbine motif.

### Redline Nation

Purpose: reward surviving a deliberately dangerous Evolution III boom while retaining a major permanent legacy.

Required story state:

- Evolution III becomes active during the firing or the event begins with the evolved opening.
- Peak Overheating reaches the specified redline band without reaching the crash threshold.
- The player completes the Runaway Industrialization landing objective.
- The final legacy reaches the high-tier requirement.
- Event 35 does not begin from the firing.

Disqualifiers:

- Peak Overheating never enters the required band.
- The player receives a safe achievement through a lower-evolution repeat firing after first activating Evolution III.
- A terminal crash occurs and is later repaired through Event 35.

Tracking need: freeze peak Overheating and highest evolution per firing. A later safer firing cannot overwrite the qualifying or disqualifying history.

Icon direction: an overloaded turbine and factory skyline held inside a reinforced circular gauge just below its final marker.

### The Long Fall

Purpose: reward recovery from the full Event 34 to Event 35 failure chain.

Required story state:

- The player country crashes from an Evolution III Industrial Boom.
- Event 35 begins at the inherited Evolution III level with all lower depression evolutions active.
- Starting Depression Severity qualifies as very high under the shared handoff contract.
- The country later resolves Event 35 through a genuine recovery outcome.
- At least one inherited Miracle Region or Runaway Region is restored through Event 35's recovery logic.

Disqualifiers:

- Event 35 was started independently.
- The inherited level or source record is missing.
- The country ends the depression through a debug clear, annexation cleanup, or generic crisis reset.
- The inherited regions are all abandoned or cease to be valid before recovery.

Tracking need: rely on Event 35's source receipt, inherited evolution floor, frozen severity snapshot, and state continuity ledger.

Icon direction: a darkened factory floor with one restored assembly line and a damaged industrial skyline behind it.

### Built to Last

Purpose: reward long-term legacy management across two legitimate repeat firings.

Required story state:

- The same player country completes two separate Event 34 firings.
- Both firings end without Event 35.
- The second firing respects the repeat-memory pressure and reduced raw legacy budget.
- The country improves or completes a different valid state network on the second firing.
- The combined country legacy remains within the event cap.

Disqualifiers:

- Both firings farm the same completed state projects without meaningful new work.
- One firing is a duplicate or overlapping active instance.
- State transfers are used to reset per-state reward caps.
- Either firing resolves through a rough result below the specified achievement floor.

Tracking need: preserve a bounded firing-history record, distinct project identities, state completion receipts, and the country legacy cap.

Icon direction: two different factory districts connected by an established freight line and a shared engineering seal.

### Every Link Held

Purpose: reward material preparation against real external shocks.

Required story state:

- The player country has several protected Industrial Regions active.
- At least two qualifying external disruptions affect distinct protected regions during one firing.
- Qualifying disruptions come from registered systems such as bombing, blockade, natural disaster, rail or port loss, occupation change, or another exact adapter.
- The protected regions prevent their full shock outcome.
- The country reaches a controlled landing.

Disqualifiers:

- The incidents are event-owned harmless flavor rolls with no material state effect.
- The same incident or same state shock is counted twice.
- Protection was applied after the incident.
- The boom collapses before landing.

Tracking need: use exact incident receipts, protected-state status at incident time, distinct-state proof, and one firing identity.

Icon direction: rail, port, and factory symbols linked by a continuous reinforced chain around a compact industrial map motif.

## Implementation rules

- Keep all achievement thresholds and qualifying bands in script constants or the event tuning file.
- Use persistent bounded receipts when the final state alone cannot prove the route.
- Every achievement must define valid start, firing identity, unlock moment, disqualifiers, and cleanup behavior.
- Prevent puppet, tag-switch, annexation, state-transfer, repeated-event, and debug farming.
- Do not count evolution activation as a concrete outcome by itself.
- Do not expose hidden future outcomes in public achievement descriptions.
- Make visible achievements explain the public objective clearly. A hidden achievement may conceal its exact route until discovered, but its implementation still needs a complete documented contract.
- Register achievements in the single project achievement registry according to existing repository practice.
- Route all six icon triplets through `chaosx_icon_artist` and `chaos-redux-event-assets`.
- Achievement files must use the engine-required root placement and exact final IDs.
- Keep achievement, localisation, icon, documentation, event-detail, and workbook references aligned.

## Asset handoff

For each achievement, create a coordinated completed, grey, and not-eligible triplet according to the current Chaos Redux and vanilla achievement consumer. Inspect the exact reference family before production. Each final icon must remain readable at native size and must not be a resized decision, focus, or idea icon.

The asset handoff must include source evidence, prompt direction, native dimensions, final filenames, final DDS paths, transparency or full-canvas treatment based on the consumer, contact-sheet review, and wiring identifiers.

## Required specialist passes

After implementation:

- Run `chaosx_icon_artist` for the achievement asset family.
- Run `chaosx_localisation_auditor` for all visible achievement and blocked-state text.
- Run `chaosx_event_completion_auditor` against the achievement section of the accepted specification.
- Use `chaosx_spreadsheet_doc_worker` only after final player-facing wording exists and only when the authoritative workbook contains achievement-facing fields that require alignment.

## Completion evidence

Return an achievement coverage table with these columns:

| Required achievement | Final achievement ID | Tracking surfaces | Disqualifiers implemented | Icon triplet | Localisation | Tested scenarios | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

Also report:

- files changed
- constants and receipt identifiers
- icon paths and sprite or achievement identifiers
- each positive unlock scenario
- each principal negative or exploit scenario
- any missing, merged, simplified, substituted, or blocked requirement

Do not claim the achievement package complete while an icon is missing, a route is inferred from an unreliable final state, or any mapped disqualifier is absent.
