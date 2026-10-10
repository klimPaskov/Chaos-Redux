# Event 033 Acid Rain, Part 9, reports, super-event, and text direction

## Event graph

Status: `implemented` in `events/033_acid_rain.txt` under the `chaosx.nr33` namespace.
The report facts listed below are implemented through D25 to D27, D32 and D35.

| Event | Scope | Purpose |
| --- | --- | --- |
| `chaosx.nr33.1` | Root recipient | Formation dispatcher; starts the runtime and latches the launch origin |
| `.20` to `.23`, `.30` to `.33`, `.41` | Hidden | Host worker and lifecycle steps |
| `.42` to `.46` | Hidden country | National operation completions (Shelter Protocols, water, medical, transport, demobilization) |
| `.47` | Hidden state | Evacuation and state recovery completion |
| `.101` | Country report | First arrival over the country's territory |
| `.102` | Country report | Advance warning, once per front visit |
| `.103` | Country report | Severe cell or superstorm forecast, once per episode, with the forecast cue |
| `.104` | Country report | Severe impact, once per episode |
| `.105` | Country report | Casualty threshold |
| `.106` | Country report | Preparation success |
| `.107` | Country report | Departure, or a temporary respite while a warning remains |
| `.108`, `.111` to `.114` | World notice to every player | Severe Storm Cells, A Global Acid Layer Forms, Global Acid Rain, The Front Divides, The Rain Concentrates |
| `.109` | Country report to participants | Dissipation summary |
| `.110` | Country report | Recovery work completed in a state |
| `.201` to `.205` | News | Formation, second front, third front, global layer, final dispersal |

Routine drift pulses, state entries and state exits remain scripted effects and never raise popups.

## Report ownership

A report goes to the country responsible for the affected state when the report becomes due. Permanent history records the responsible country at impact. If control changes during a forecast, migrate the forecast and actionable state decision to the new responsible country through the bounded state-transfer helper.

The original owner can receive a separate strategic summary only when the shared occupation or exile reporting policy requires it. Do not send duplicate full reports by default.

## Formation super-event

Status: `implemented` as super-event `117` with its audio, image, title, quote and allusion.
Event 33 receives one mandatory super-event at atmospheric formation.

### Trigger

Show it only after:

- the frozen registry exists
- the first front or global transition is valid
- every country category record has been initialized
- the event history row can be committed

Do not show it during a failed initialization or old-save repair.

### Image direction

A wide 457 by 328 scene of a 1930s or 1940s capital under dark corrosive rain. Use damaged stone, stained metal, flooded streets, civilians moving toward shelters, civil-defense workers in period protective equipment, and a low cloud ceiling. The scene should communicate world-scale danger without modern hazmat suits, neon green rain, or science-fiction machinery.

### Text

Title: "Acid Rain".
Quote: Robert Angus Smith, *Air and Rain* (1872), p. 444, verified and recorded in `research/033_acid_rain_science_and_source_research.md`.
Allusion: "For the rain it raineth every day," Shakespeare, *Twelfth Night*.
Keys: `chaosx_super_event.117.t`, `.q`, `.a` and `.d` in `localisation/english/033_acid_rain_l_english.yml`.

### Audio

The cue is an 80-second excerpt (61.5 to 141.5 seconds) of the Wikimedia Commons public-domain recording of Mussorgsky's *Night on Bald Mountain*, confirmed public domain worldwide by Wikimedia VRT ticket 2008012110017088.
It ships as `sound/033_acid_rain/super_event_033_acid_rain_formation.wav` and `.ogg`, playback ID 117 is exclusive to Event 033, and the conversion, loudness, uniqueness and audition record is in `music/chaosx_music_track_list.html`.
Hearing it in game is a user live check.

### Change rule

Any replacement quote, allusion or recording must carry the same source, rights, uniqueness and audition record before it replaces the current one.

## Advance warning report

Send one warning per front visit and destination country, so a return to the same region warns again (D25). It states:

- destination region
- estimated arrival window
- exposed controlled-state count
- national Preparedness
- most urgent missing component
- decision-category link

Do not reveal the exact future state footprint. The weather remains uncertain until it arrives.

A country with no controlled eligible state in the destination receives no warning event, though it can still inspect the global GUI.

## National arrival report

The first state entry for a country starts or increments national exposure. Send an arrival report when:

- national active exposed-state count changes from zero to positive
- no arrival report has fired in the previous thirty days

The report identifies the first affected state, current front, intensity band, Preparedness, and available urgent actions. Later states entering under the same continuous national exposure do not each fire a popup.

## Severe forecast and impact reports

### Forecast

Send once per country per severe episode when at least one forecast state is under its responsibility. It names the highest-population forecast state and total forecast state count. It exposes the evacuation decision and countdown.

### Impact

Send after the first positive severe or superstorm pulse of each episode in the country's territory. It names the state, says whether its evacuation finished, is under way with partial protection or is absent, gives the country's deaths so far with the estimated deaths prevented, and gives the days left in the episode (D26, D27).

The report shows no building damage points or per-component contribution figures, because neither changes what the player can do while the cell lasts; the damage reaches the player through the aftermath tier and the recovery decisions.
A later end summary is folded into the departure report instead of creating a third popup.

## Casualty-threshold report

Use the thresholds and cooldown in Part 4. A threshold report should explain cumulative losses, current exposure, Preparedness, and the main observed vulnerability. It should not blame a country for low preparation when the actual driver was occupied supply collapse unless both facts are shown.

## Preparation-success report

The report can fire once every sixty days and only after a meaningful counterfactual difference. Suggested first threshold is 25,000 prevented deaths or 25 percent lower applied loss than the unprotected estimate, whichever requires the larger material result for that country.

The text should identify the dominant effective component, such as shelters or protected water. It must describe prevented losses as an estimate.

## Departure report

Send when national active exposed-state count reaches zero after having been positive. Include:

- exposure duration
- cumulative national Event 33 deaths
- prevented-death estimate
- remaining aftermath-state count
- highest aftermath tier
- recovery-category direction

If another front is already warning the same country, call the event a temporary departure and keep urgent actions visible.

## Evolution reports

### Multiple-front split

One global report after the second front becomes stable. A third front receives a smaller global report or news line only on its first successful formation.

### Global-layer transition

Use one warning report at the three-day transition and one global-layer start report after the transition shock. The formation super-event is not replayed.

### Evolution text rule

The report describes the physical outcome. It does not say that a game tier unlocked the evolution.

## Dissipation report

One global report confirms acute rain has stopped. It includes:

- total duration
- total Event 33 deaths
- total states touched
- lifetime Event 33 contamination addition
- number of severe cells or superstorms
- unresolved global aftermath-state count

National recovery reports remain separate.

## News policy

Use news only for world-facing milestones:

- formation through the super-event framework
- stable atmospheric split if the news registry supports it
- global layer beginning
- final dissipation

Do not send news for each region movement, warning, or national casualty threshold.

## Writing direction

### Tone

- concise government and scientific reporting
- visible uncertainty before arrival
- concrete human and infrastructure consequences after impact
- period-compatible institutions and equipment
- no modern climate-policy slogans
- no jokes in severe casualty reports

### Scientific wording

Use terms such as lethal acid rain, corrosive aerosol, poisoned runoff, atmospheric anomaly, exposed skin, respiratory injury, and infrastructure corrosion. The origin may remain unknown or supernatural. Do not add pH figures, realism disclaimers, or wording that reduces actual civilian deaths to manpower shortages.

### Option direction

Most reports need one acknowledgment option and a category link. Add a policy choice only when options create distinct costs, risks, or effects. Avoid false branches.

### Localization boundary

This package supplies purpose, facts, and tone. Final localisation lives in `localisation/english/033_acid_rain_l_english.yml` and must pass the localisation auditor.

## Report cooldown ledger

Store separate cooldowns for:

- arrival
- casualty threshold
- successful preparation
- departure
- severe forecast by episode ID
- severe impact by episode ID
- warning by front visit ID

One report class cannot accidentally suppress a different urgent class.

## Event-history payload

The Event 33 history row should retain:

- firing date
- trigger context, ordinary, cluster, or manual debug
- highest stage at formation
- highest stage reached
- first region or global opening
- event end date
- duration
- eligible and touched state counts
- total deaths
- prevented-death estimate
- building damage points
- Event 33 lifetime contamination added
- front count peak
- severe-cell count
- superstorm count
- global-layer receipt
- cluster sequence when applicable
- dissipation or administrative termination reason

History values are written from stored counters. The Event Log does not reconstruct them by scanning old state modifiers.
