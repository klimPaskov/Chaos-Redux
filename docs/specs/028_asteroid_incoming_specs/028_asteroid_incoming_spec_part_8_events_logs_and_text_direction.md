# Asteroid Incoming, Part 8: Events, Logs, and Text Direction

## Event family

The implementation can choose exact subevent IDs. The player-facing and hidden roles should remain distinct.

### Entry and target event

The chooser receives the four-option event after all target pairs are valid and locked. This event explains the temporary redirection capability, the certainty of the center and ring damage, and the miss path.

### Confirmation event

A short confirmation repeats the selected target country and state. It contains no new roll and no hidden alternative.

### Target emergency event

The locked target country chooses one preparedness stance during the two-day delay.

### Observer trajectory notice

Other human players receive a compact notice after confirmation. The notice names the intended target and impact date. It does not reveal fragment sites.

### Hidden impact resolver

One hidden transaction applies the main impact, fragments, Deaths, crater states, dust, and incident aggregation.

### Affected-country report

Each affected country receives one dynamic report. It names its worst affected state, total deaths, number of damaged states, capital relocation when relevant, and the opening recovery problem.

### Global fragment summary

When fragmentation applies, one global news event reports the actual fragment count and broad world regions struck.

### Impact super-event

The super-event follows the completed impact transaction. It identifies the locked main target and region and uses one dynamic impact package.

### Dust milestone reports

A small set of global reports marks major recovery thresholds.

### National recovery closeout

A country receives a final local report when its timed impact-zone burdens are resolved.

### Close-passage news

The miss option produces one global news event. It identifies the object as a narrowly avoided impact and describes observatory follow-up. It creates no super-event and no recovery chain.

## Player-facing text direction

All labels in this package are working labels. Final wording belongs to implementation and research.

### Entry event

**Viewpoint:** Scientists and the chooser's government confronting a short-lived ability to alter the trajectory.

**Visible information:** Three target countries and states, two-day lock, center destruction, adjacency-ring damage, dust, active evolutions, and miss outcome.

**Uncertain information:** Exact fragment sites, exact death totals, exact dust severity, and later political consequences.

**Tone:** Controlled, technical, and morally severe. The event should avoid heroic planetary-defense framing because the player can direct the object toward a country.

**Avoid:** Generic final-crisis language, long scientific exposition, jokes about mass death, invented equations, and language that calls the options warnings or threats.

### Impact options

Each option represents a deliberate target selection. The option tone can use cold administrative brevity or grim scientific understatement. It should not celebrate civilian destruction.

The country and state names must be dynamic. A capital marker can be included when relevant.

The miss option should sound like preserving the natural close-passage path. It should be clear and practical.

### Target emergency event

**Viewpoint:** The targeted government with forty-eight hours to protect what can survive outside the center.

**Visible information:** Locked state, whether it is the capital, the three preparedness stances, and the limits of each stance.

**Tone:** Urgent and practical. The choices should focus on command, transport, hospitals, shelters, and water.

**Avoid:** False hope that the center can be saved, melodramatic speeches, and cheap humor.

### Country reports

**Viewpoint:** The affected country's first consolidated assessment.

**Visible information:** Total deaths, worst affected state, number of damaged states, local phase, and available recovery response.

**Tone:** Specific and restrained. State names, rail loss, hospital pressure, fires, and displaced populations carry the weight.

**Avoid:** One generic paragraph reused for every country, one line per state, map-table framing, and raw hidden variables.

### Fragment summary

**Viewpoint:** Global news after the main strike.

**Visible information:** Actual fragment count and broad regions.

**Uncertain information:** Full material composition and long-term mineral value before Evolution II reports reveal it.

**Tone:** Global factual coverage. It should not compete with the main super-event.

### Dust reports

**Viewpoint:** Weather services, transport networks, factories, and civilians living under changing sky and air conditions.

**Visible information:** Current stage, production and supply consequences, and broad recovery direction.

**Tone:** Period scientific reporting with concrete observations.

**Avoid:** Repeating the same global-collapse wording at every stage.

### Close-passage news

**Viewpoint:** Astronomers and the public observing a near miss.

**Visible information:** The object passed close to Earth, the danger ended, and observatories continue tracking it.

**Tone:** Relief mixed with scientific interest. It can use restrained irony or period newspaper style in the option response after research.

**Avoid:** A hidden implication that the asteroid will return during this event chain.

## Event History

Event 028 receives one major-event history row when it fires.

The row should include:

- Event ID and major type
- Date
- Chooser as actor
- Outcome status: impact or close passage
- Chosen target country and state after selection
- Main impact date when applicable
- Total civilian deaths after resolution
- Actual fragment count
- Opening dust stage

The normal major-event history row must not be duplicated by the target emergency event, country reports, fragment summary, dust milestones, or super-event.

## Event Details

Before firing, Event Details should describe the premise without listing hidden target scores or exact formulas.

After firing, it should show outcome-specific information.

### Close passage

- Miss outcome
- Date of closest passage
- No impact and no dust

### Main impact

- Chooser
- Intended target country
- Locked state and region
- Impact date
- Total deaths
- Number of affected countries and states
- Actual fragment count
- Current Dust Load and stage
- Main crater controller
- Fragment-site controllers under Extraordinary Minerals

The detail view should update current controller information without rewriting historical target information.

## Evolution views

### Global Fragmentation preview

The catalog preview describes worldwide fragment strikes, two-ring fragment damage, country reports, and added dust. It should not show future random locations.

### Extraordinary Minerals preview

The catalog preview describes transferable main and fragment armour benefits and strategic crater control. It can state the plus 100 and plus 20 values because they are visible mechanics.

### Logged rows

Global Fragmentation and Extraordinary Minerals each produce one global evolution row when applied. They use no actor flag. The main Evolutions tab and selected-history related-evolution view show their source event, tier, stage, and date. Event Details remains a preview and current-state surface, not a fake history log.

## Event list availability

Event 028 should show `N/A` weight when fewer than three valid target pairs can be constructed. It should not show a misleading zero weight that looks like ordinary major-event accumulation.

The event remains disabled by default until the rework is complete. The same implementation change that completes registration, logs, assets, AI, docs, and catalog alignment can add it to the normal enabled allowlist.

## Dynamic names and snapshots

The impact super-event and reports need both historical and current context.

- Historical target uses the country name and flag context saved at trajectory lock.
- Current affected-country reports use the country that holds the damaged territory at impact time.
- Current crater-controller displays use live controller context.
- Region text uses the locked state's broad geographic context.

If the intended target no longer exists at impact time, the super-event can identify the former target and region through the saved snapshot. It should not display a missing scope or raw key.

## Super-event text direction

The final super-event package requires sourced quote and cultural-remark research.

**Role:** First global reveal of the completed main impact.

**Title direction:** Short, specific, and tied to the target or impact. Avoid generic apocalypse titles.

**Description direction:** State where the main body struck, that surrounding regions were damaged, and that atmospheric consequences are developing. Mention fragments when active without listing every site.

**Button direction:** A brief reaction suitable for a mass-casualty scientific disaster. Use restrained cultural reference, scientific understatement, or grim administrative response only after source research.

**Quote direction:** Use a verified historical, literary, religious, philosophical, or scientific source about falling bodies, human control, catastrophe, dust, or consequences. Do not invent or misattribute a quote.

## Spreadsheet-facing direction

The catalog detail should present the event premise and visible choices. It should not expose internal target scoring, hidden AI weights, raw formulas, implementation history, or random-location pools.

Evolution detail fields should match the Event Details localisation in meaning. The authoritative workbook is edited first. CSV exports are regenerated after the workbook update.
