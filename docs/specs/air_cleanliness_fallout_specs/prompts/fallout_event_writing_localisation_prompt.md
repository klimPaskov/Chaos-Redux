# Fallout Event Writing and Localisation Prompt

Write and audit the final player-facing text for the implemented Fallout living-world event library after event ids, actors, mechanics, choices, and effects are stable.

Working labels in the source specs are planning labels. Do not paste them automatically into final localisation.

## Required reading

Read:

- `AGENTS.md`
- `chaos-redux-events`
- the complete Fallout source specs and event matrices
- the final event scripts and scripted effects
- current country, government, region, character, decision, focus, and idea localisation
- the relevant historical and regional research notes
- the local offline localisation documentation

## Voice and information

Each event needs a clear viewpoint.

Possible viewpoints include:

- shelter residents
- ration officials
- engineers
- doctors
- farmers
- sailors
- railway crews
- refugees
- militia officers
- judges
- teachers
- religious relief workers
- altered-community representatives
- foreign envoys
- children and second-generation adults

The text should show what these people see, need, fear, repair, argue over, exchange, celebrate, conceal, or remember.

Do not make most events read as detached global narration.

## Regional specificity

Final text should use researched and implemented details from the active region:

- food and crops
- climate
- terrain
- buildings
- transport
- tools
- institutions
- clothing
- local political language
- religious and social practices
- old borders and public memories
- new successor institutions

Do not reduce regions to stereotypes. A region needs competence, internal disagreement, ordinary life, and recovery alongside danger.

## Government specificity

The same crisis should sound different under:

- continuity government
- emergency republic
- military remnant
- technocratic enclave
- municipal league
- agrarian commune
- religious refuge
- commercial caravan state
- bunker hierarchy
- raider confederation
- altered polity
- machine administration

Government language should affect who speaks, what law is invoked, what sacrifice is considered legitimate, and what failure threatens the regime.

## Choice text

Every option must communicate the visible public action.

Option text can be:

- practical
- grim
- bureaucratic
- ideological
- frightened
- bitter
- restrained
- locally humorous
- ritual
- defiant

Humor must fit the stakes. Famine deaths, atrocities, radiation sickness, mass displacement, and child death do not use cheap comedy.

Do not use generic buttons such as:

- We must act
- This is terrible
- The world has changed
- Do what must be done

Do not reveal hidden outcomes, secret routes, event weights, achievements, or implementation state.

## Dynamic text

Use dynamic localisation when the event depends on:

- country
- state
- region
- government archetype
- successor memory
- active character
- bilateral partner
- winter phase
- survival resource
- route
- compact
- war cause
- number of days
- population loss
- building damage
- cost
- mission objective

Integer values should display as integers unless fractional precision affects player decisions.

## Style rules

Never use em dashes or semicolons.

Avoid staccato prose.

Avoid staged contrast formulas that set one report against an official denial or delay.

Avoid thesis, antithesis, synthesis structures.

Avoid reusable finality, crossroads, darkness, abstract hope, and odds-defying formulas.

Use concrete material detail instead of vague intensity.

Do not write process language such as reworked, newly added, dynamic baseline, placeholder, or implementation.

## Event structure

A normal event description should establish:

- immediate situation
- people or institution involved
- concrete shortage, opportunity, conflict, or discovery
- consequence of delay
- information the player can reasonably know

The option and tooltip then explain the visible action and baseline effect.

A delayed result should remember the earlier choice and name the relevant character, state, institution, or partner.

A callback should not repeat the opening paragraph. It should show how the choice changed later life.

## Tone range

The full library should include:

- serious crisis
- technical work
- ordinary competence
- family conflict
- affection
- grief
- ritual
- local humor
- celebration
- political argument
- corruption
- discovery
- cultural invention
- generational change

No more than two thirds of routine society events should be purely negative.

## Research gates

Do not invent:

- quotations
- songs
- slogans
- proverbs
- scripture excerpts
- literary references
- film or game references
- historical statements attributed to a person
- regional sayings

Use the approved text research workflow, record the source, and keep copyrighted excerpts short.

## Mutant-fiction boundary

Fictional altered societies should speak as societies, not as monsters or medical specimens.

Their text can cover:

- citizenship
- family
- health
- law
- naming
- ritual
- prejudice
- diplomacy
- work
- military service
- reproduction
- memory
- internal disagreement

Do not state that ordinary radiation scientifically creates rapid fantasy mutation.

## Key coverage

For every implemented event, provide:

- title
- description
- every option
- custom effect tooltip where needed
- custom requirement tooltip where needed
- delayed result text
- news or report text when used
- event-log name and detail text where used
- character and institution names
- dynamic scripted-localisation support

Also cover connected decisions, missions, focuses, ideas, GUI labels, mapmode text, country names, party names, and catalog mirror fields.

## Audit output

Report:

- missing keys
- duplicate keys
- raw working labels
- generic repeated phrases
- regional or government text that reads identically
- dynamic values printed statically
- hidden mechanics exposed
- unsourced cultural references
- mutant-science errors
- style violations
- spreadsheet mismatches
- exact changed keys and files
