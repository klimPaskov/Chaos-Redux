# Infantry Spawn localisation and event log handoff

This file is direction only. Do not paste these working labels into localisation as final player-facing text.

## Localisation surface inventory

| Surface | Keys or ids to create in implementation | Direction |
| --- | --- | --- |
| event name | Event 019 name selector and debug selector | Use final event name and keep catalog, settings, and event log aligned |
| Event Details title | event-details title selector | short direct name for the event |
| Event Details body | event-details body selector | describe sudden formations appearing across controlled states and the public command confusion, no formulas |
| baseline popup | event 019 entry and options | grounded military confusion, useful but weak units, no hidden future spoilers |
| Evolution I popup or report | evolution milestone | formations look more coherent and better supplied, with unease from order that nobody scheduled |
| Evolution II popup or report | evolution milestone | heavier units, strange equipment, and logistics burden arrive together |
| Evolution III popup or report | evolution milestone | the army must choose whether to request more units and deal with generals whose authority feels wrong |
| Evolution IV popup or report | evolution milestone | ordinary recruitment touches nonstandard unit families, with containment language and no parent event spoilers |
| decision category | category name and description | readable summary of command coherence, strain, backlog, absurdity, appetite, and leakage |
| decision titles | every decision family | direct public action, no hidden reward language |
| decision descriptions | every decision family | what the government or army is visibly doing |
| cost text | scripted localisation if needed | icon-first costs, short missing requirement text, no long raw triggers |
| mission titles | mission families | named objective direction with target region when possible |
| mission descriptions | mission families | clear place, time, success, and failure direction |
| general events | demand chain and revolt events | possessed or unsettling officer influence without cheap comedy |
| breakaway country names | country localisation and cosmetic names | short map-readable names, not internal agency names |
| breakaway ideas | country national spirits | starting problem and route identity, not passive badges |
| achievements | achievement localisation | mastery conditions and route direction, no easy event-fire unlocks |
| scenario UI | scenario name, type labels, detail, impact text | describe instant crisis and intensity effects without final campaign language |
| super-events if accepted | title, description, button, quote | research-gated through super-event workflow |

## Dynamic placeholders

Implementation should use dynamic placeholders when final text benefits from them:

- country name
- selected state name
- selected general name
- selected splinter country name
- current command coherence band
- current supply strain band
- current officer appetite band
- current chaos leakage band
- latest spawned unit quality class
- scenario type and intensity

Values that are conceptually integers should display as integers.

## Event log evolution directions

| Evolution | Log title direction | Log body direction | Actor use |
| --- | --- | --- | --- |
| Evolution I | organized sudden muster | stronger registers and better supplied units appear | actor optional if first country proves it |
| Evolution II | arsenal muster | heavier units and strange equipment enter the wave | actor if first country receives serious wave |
| Evolution III | possessed command | generals and random templates turn the event into a command crisis | actor required when first demand or revolt belongs to a country |
| Evolution IV | chaos muster | registered chaos units enter Infantry Spawn under lesser profile rules | actor required when first chaos unit or splinter belongs to a country |

Do not log every repeat wave as an evolution.

## Spreadsheet handoff

The spreadsheet worker should update Event 019 only after final in-game Event Details and evolution text exist. The Details field should mirror the Event Details premise. Evolution columns should mirror the four evolution descriptions. The triggerable scenario field should mention the instant crisis setup only if the workbook has a scenario field for that event. Do not list raw script effects, formulas, hidden variables, or final achievement routes in the Details field.

## Writing constraints

Final text should avoid generic disaster wording, update-history wording, hidden mechanic spoilers, and role labels from this spec. Options can use grim irony, official understatement, or country-specific military tone when final localisation is written.
