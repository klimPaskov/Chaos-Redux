# Presentation and Writing Direction

## Presentation hierarchy

Event 51 should use the least complex surface that keeps the crisis readable.

1. Entry event establishes the global crisis.
2. Decision category header carries the two public values and current national situation.
3. State map shading and state modifiers show Local Heat Stress.
4. Reports explain local changes and consequences.
5. Event Details stores the premise, evolutions, and status.
6. Evolution III uses one escalation super-event after a real world milestone.

The decision category and map should do most of the work. Repeated popups should not be the only way to understand the event.

# Entry event direction

## Viewpoint

The entry event should speak from the perspective of a government receiving converging evidence from civilian authorities, military commands, rail systems, farms, and foreign reports.

## Visible information

The player should learn:

- abnormal heat is affecting the world
- the country's most exposed states
- the initial global intensity band and trend
- the need to choose a protection priority
- the expectation that the crisis can last for months

## Information kept uncertain

The entry should not reveal:

- exact duration
- number of future surges
- hidden intensity ceiling
- future evolution activation
- exact mortality or terrain thresholds
- whether the first easing will be final

## Tone

Use practical alarm and physical detail. The event should focus on warm nights, water demand, slowing transport, exhausted troops, and altered work schedules.

Avoid:

- generic claims that the world will never be the same
- staff-table or sealed-report clichés
- a list of modifier effects
- modern climate-policy language
- direct prediction of world collapse

## Option direction

The first option represents accepting emergency coordination and opening the Heat Wave response category. It can carry restrained irony or administrative frustration, but the wording should remain suitable for a serious worldwide crisis.

Do not write a bland confirmation unless the event style calls for it. Final wording should be researched and localized during implementation.

# Decision category layout

## Header order

1. Category picture.
2. Global Heat Wave Intensity band, trend, and phase.
3. National exposure summary.
4. Active national protection priority.
5. Hotspot list of up to three states.
6. Current active missions.
7. Primary actions for the current phase.

The category description should use short natural lines. It must not simulate columns or a ledger with repeated divider characters.

## Hotspot row

Each hotspot row should show:

- state name
- Heat Stress icon and band
- trend
- one dominant risk icon
- active mitigation status

The dominant risk can be water, population, army, harvest, industry, rail, or environmental degradation.

Do not show six numeric subcomponents.

## Tooltips

### Global intensity tooltip

Explain:

- what the value represents
- current trend
- next public threshold
- that local conditions determine actual state harm

### Local Heat Stress tooltip

Explain:

- current band and trend
- two or three strongest actionable causes
- current protection
- next likely consequence

### Decision tooltip

Explain:

- target
- visible costs with icons
- immediate protection
- sacrifice or risk
- success or failure condition for missions

Tooltips should usually fit in two to four short lines per value or control. Complex mission tooltips can be longer when they name exact states and objectives.

# Map presentation

## Heat Stress map mode

Preferred visual states:

- no active heat or Manageable
- Strained
- Dangerous
- Extreme
- Scorched
- permanent environmental degradation overlay or icon

Use color and a non-color cue such as icon, border, pattern, or band label. The player should not rely on color alone.

The map mode should be available while the event is active and during recovery. Permanent degradation remains visible through its owner presentation after cleanup.

## Selection behavior

Selecting a state should show:

- Heat Stress band and trend
- dominant risk
- protection status
- accumulated warning stage where public
- available targeted action

Exact hidden exposure points belong in debug output only.

# Notifications

Use notifications for:

- episode onset
- intensity crossing into a new public band
- major surge
- first national state reaching Extreme or Scorched
- mission failure with real consequence
- mortality beginning in a state
- environmental degradation warning
- permanent degradation
- transition into recovery
- full cleanup

Do not notify the player for every small score change.

# Report writing rules

## Baseline

Use concrete daily and institutional effects:

- reservoirs and pumps
- altered shifts
- exhausted soldiers
- rail inspections
- crop and livestock stress
- hospitals and water queues
- warm nights in unexpected regions

## Evolution I

Use factual descriptions of illness, death, triage, failed water delivery, and military casualties. Avoid cheap jokes and exaggerated gore.

## Evolution II

Use soil, vegetation, wells, canals, abandoned farms, repeated repair, and movement away from damaged land.

## Evolution III

Show temporary uninhabitability through empty daytime streets, guarded water, collapsed work schedules, withdrawing armies, and abandoned settlements. Avoid generic apocalypse phrasing.

# Dynamic localisation

Final text should mention real scopes where relevant:

- affected state
- country
- capital
- critical corridor
- agricultural region
- active front
- protection priority
- current intensity band
- evolution stage

Use scripted localisation for dynamic state and country names. Do not expose raw variable names or fallback text from another country.

# Ideology and government variation

Government type can alter response tone and available coercive variants.

Possible directions:

- democratic governments emphasize municipal coordination, public health, and parliamentary pressure
- authoritarian governments emphasize orders, guarded distribution, and production quotas
- revolutionary governments emphasize committees, collective distribution, and labor mobilization
- monarchies can use court, provincial, military, or charitable institutions where appropriate
- occupation regimes can produce unequal allocation and resistance risk

These variations should change wording, AI, or a meaningful choice. They should not create four cosmetic copies of every report.

# Country and regional variation

Regional detail should come from terrain, climate, infrastructure, and culture where the repository has a defensible source.

Examples of useful distinctions:

- desert states with existing hot-weather routines
- humid jungle fronts where shade does not remove physiological stress
- northern buildings designed to retain warmth
- mountain regions receiving displaced people
- industrial cities dependent on pumps and power
- river and canal agriculture competing for water
- island states dependent on ports and imports

Do not write stereotypes or unsupported claims about national competence.

# Event Details direction

Event Details should describe:

- a persistent global heat system
- changing intensity and uneven state impact
- military, water, food, industry, transport, and environmental stakes
- repeatability after full cleanup
- three evolution premises

It should not list numeric modifiers, hidden MTTH, exact death formulas, or secret super-event conditions.

# Localisation completion checks

- no raw keys
- no `:0` localisation version markers
- UTF-8 with BOM
- no em dash or semicolon in prose
- no process or rework history in player text
- no fake warning labels or generic dramatic filler
- no exact hidden thresholds in reports
- all dynamic fallbacks are neutral and country-safe
- event, decision, mission, achievement, super-event, Event Details, and catalog wording agree
