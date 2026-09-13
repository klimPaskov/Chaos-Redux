# Prompt: Event 037 achievement implementation

Implement the complete achievement package for Event 037, Mysterious People.

Read Part 7, the acceptance criteria, balance matrix, event skill, event-assets skill, achievement precedents in the repository and installed game, and the final Event 037 gameplay implementation. Do not implement achievements before the underlying population, pressure, Famine, Migration, project, atrocity, and event-history facts are stable.

Use these exact IDs:

- `chaos_redux_037_room_for_everyone`
- `chaos_redux_037_a_billion_more`
- `chaos_redux_037_three_censuses`

Keep all Chaos Redux achievements in the established root achievement registry. Use existing shared achievement rules for player-country continuation, game mode, disqualification, and persistence.

## Room for Everyone

Track one continuous `365` day success period.

Requirements:

- at least `25%` of current player-country population is living Event 037 mysterious population
- Overpopulation Pressure below `40`
- no controlled Event 037 state at severe or catastrophic Famine during the timer
- at least one completed Event 037 housing or services project
- at least one completed integration mission
- no Event 037-targeted atrocity action by the player
- no Event 037-targeted forced-displacement death caused by the player during the timer

Reset the continuous timer when a required condition fails. Permanent atrocity disqualifiers remain permanent where the spec requires them.

## A Billion More

Track one continuous `180` day management period after the scale threshold is reached.

Requirements:

- Evolution III active
- living Event 037 population worldwide at least `1,000,000,000`
- player country contains at least `100,000,000` living mysterious people
- Overpopulation Pressure below `60`
- no controlled Event 037 state at Breakdown during the timer
- no active player-owned Event 037-targeted camp or extermination route
- no violent border action or unsafe forced return against Event 037 cohorts
- at least one completed national food-expansion or international-settlement program

The world and country population values must come from current living provenance, not lifetime-created totals.

## Three Censuses

Track three distinct Event 037 manifestation sequence entries for the player country.

For each firing:

- player controls at least one valid affected state
- a meaningful Event 037 support mission completes before the next counted firing
- no player-controlled Event 037 state reaches catastrophic Famine during the sequence
- player uses no violent pushback, unsafe forced return, forced labor, or systematic killing against Event 037 population

At the third firing, player pressure must be below Emergency.

Use firing identities or counters that cannot increment twice from reports, reload, cluster presentation, or multiplayer duplication.

## Disqualifiers and ownership

Use exact owner facts:

- Event 037 atrocity targeting from Camp and Repression
- forced-displacement deaths from Migration
- Famine stages from Famine
- project and mission completion from Event 037
- current pressure and living provenance from Event 037
- player-country continuation from the shared achievement framework

Do not infer a disqualifier from generic country ideology alone. Do not clear historical disqualifiers through tag change, annexation exploit, or category closure.

## Localisation

Write final player-facing title and description text. The working title directions may be retained when they fit, but the text must describe the actual achievement conditions clearly and use no developer wording, update history, raw variable names, or hidden implementation details.

## Assets

Use the final achievement triplets from the Event 037 asset package. Verify filenames, IDs, sprite or achievement references, dimensions, normal state, grey state, and not-eligible state.

Do not substitute copied or resized unrelated achievement art.

## Documentation and validation

Update event documentation and completion report with:

- achievement IDs
- requirements
- timers
- disqualifiers
- persistence behavior
- asset paths
- localisation keys
- test cases

Validate success, timer reset, permanent disqualification, country continuation, save and reload, three-firing identity, world threshold, country threshold, Famine failure, pressure failure, atrocity failure, forced-displacement failure, and asset display.

Report every changed file, identifier, meaningful test, unresolved blocker, and skipped evidence. Do not claim completion while any triplet, localisation key, trigger, disqualifier, or persistence path is missing.
