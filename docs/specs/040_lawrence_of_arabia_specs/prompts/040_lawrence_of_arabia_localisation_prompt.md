# Event 40 Localisation Prompt

Use `chaosx_localisation_auditor` after Event 40 gameplay, decisions, federation routes, achievements, and super-events have stable IDs.

## Required reading

Read:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-focus-trees`
- `chaos-redux-super-events`
- every Event 40 specification file
- final gameplay files and existing Event 40 localisation

## Writing principles

Write complete in-world text. Do not paste planning notes, working labels, hidden conditions, tuning history, or implementation explanations.

The event must show Arabian governments as active political actors. Local rulers, officers, ministries, tribal leaders, urban political groups, smugglers, railway workers, and foreign sponsors act for their own reasons.

Lawrence is a British liaison, organizer, adviser, and possible political figure. Do not write him as the sole creator of an Arab military or political movement.

The opening must communicate that Lawrence was believed dead and has been secretly recalled. It should not describe a supernatural resurrection.

Use a serious, suspicious, opportunistic tone. Dry official irony is acceptable in small reactions. Do not use cheap comedy for colonial domination, betrayal, revolt, or mass violence.

Avoid:

- em dashes
- semicolons
- staccato dramatic fragments
- thesis and counter-thesis templates
- generic crisis clichés
- map-summary prose as the emotional center
- film quotations or film imitation
- raw variable names
- raw trigger blocks
- fake UI tables made with separators
- hidden-route spoilers

## Dynamic content

Use dynamic actors and places when the player needs them:

- sponsor and target country
- active route or state
- current Influence band
- next threshold
- settlement identity
- Lawrence's current role
- federation core and members
- congress city

Do not expose hidden British reach, cell score, trust, credibility, or federation-readiness numbers.

## Surfaces

Audit and complete:

- event names and descriptions
- event options
- news or report events
- decision categories
- decisions and missions
- custom trigger tooltips
- effect tooltips
- idea and dynamic-modifier text
- character roles and traits
- Event Log names
- Event Details
- evolution titles and descriptions
- federation country names and adjectives
- parties and government names
- focus names and descriptions
- Federal Authority presentation
- achievement names and descriptions
- super-event title, description, button, and quote
- scripted localisation selectors
- debug names
- catalog-facing wording that mirrors implemented text

## Influence wording

The player should understand:

- current band
- whether Influence is rising, stable, or falling
- the next threshold
- why one current actionable factor matters

Keep the tooltip concise. Do not print a full component ledger.

## Options and decisions

Options should state the public action and visible consequence. They should not reveal secret follow-up events or hidden route checks.

Useful tone families include:

- British administrative confidence
- cautious national bargaining
- anti-imperial resolve
- official suspicion
- military urgency
- bitter reaction to broken promises
- rare personal trust in Lawrence

Research cultural or historical allusions before using them. Do not invent a quotation.

## Super-events

Use only the quote and button wording selected by the super-event research process. Verify attribution and translation.

The three federation outcomes require distinct tone:

- British Arabia is formal and uneasy
- Independent Arab Federation is constitutional and sovereign
- Lawrence's Kingdom is strange, personal, and politically contested

## Technical rules

- localisation files use UTF-8 with BOM
- keys omit `:0`
- no duplicate keys
- texticons match the displayed costs
- long conditions use custom tooltips
- country-specific fallback branches cannot leak another country's wording
- all scripted-localisation defaults are neutral and valid

## Audit output

Patch narrow localisation defects directly. Write a handoff listing:

- files changed
- keys changed
- missing keys found
- dynamic branches tested
- terminology choices
- mismatches with Event Details or catalog wording
- unresolved source or translation questions
