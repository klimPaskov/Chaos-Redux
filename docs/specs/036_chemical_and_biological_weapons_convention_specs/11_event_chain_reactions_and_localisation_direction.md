# Event chain, reactions, and localisation direction

## Namespace plan

The implementation keeps the canonical Event 036 namespace.

The exact final subevent numbers may be adjusted to avoid live repository collisions, but the role map should remain stable.

| Working range | Role |
| --- | --- |
| `chaosx.nr36.1` | Canonical entry and global setup |
| `chaosx.nr36.2` to `.9` | National opening responses, initial standing, and opening reactions |
| `chaosx.nr36.10` to `.19` | Baseline agenda announcements, national treaty responses, resolutions, and implementation reports |
| `chaosx.nr36.20` to `.29` | Evolution I activation and first-use conference chain |
| `chaosx.nr36.30` to `.39` | Evolution II activation and strategic doctrine chain |
| `chaosx.nr36.40` to `.49` | Evolution III activation and arsenal charter chain |
| `chaosx.nr36.50` to `.59` | Chaos weapon program selection, milestones, completion, cancellation, and dormancy |
| `chaosx.nr36.60` to `.69` | Inspection, exposure, covert program, and treaty-breach reports |
| `chaosx.nr36.70` to `.79` | Retaliation guarantees, assistance requests, and victim reactions |
| `chaosx.nr36.80` to `.89` | Convention collapse, reconstruction, accession, withdrawal, and expulsion |
| `chaosx.nr36.90` to `.99` | Global news and bounded regional reactions |

## Event types

### Canonical entry

The entry is the only normal random-event firing.

It records Event 036 in the shared History view and applies the fire-once lifecycle.

### Country response events

Each eligible human country receives its own response event.

AI countries use the same posture contract through hidden response effects or hidden events.

A country response does not record another normal Event 036 History row.

### Conference subevents

Agenda, vote, resolution, implementation, inspection, and project events are Event 036 follow-ups.

They do not enter the global random-event pool.

They do not add minor pacing pressure or major-event gain.

### News events

Use a global news event when the outcome changes international norms or publicly reveals a major program result.

Suitable news thresholds include:

- the convention entering force
- the first successful offensive first-use charter
- the strategic doctrine charter
- the Arsenal Without Limits Articles
- activation of the International Chaos Weapons Program
- completion of a registered Chaos weapon prerequisite
- collapse of the convention after broad withdrawal
- exposure of a major covert opponent when the evidence is internationally significant

A routine agenda failure, minor accession, ordinary contribution, or small inspection result should use a country or report event instead.

## Event log integration

The shared History view records Event 036 once at the canonical opening.

The history actor is the convention coordinator when valid.

If no coordinator can be resolved, use the triggering country only when it is a meaningful ordinary actor.

Do not display an invalid special actor as the event’s public sponsor.

The Evolutions view records:

- Evolution I, First Use Becomes Acceptable
- Evolution II, Strategic WMD Doctrine
- Evolution III, The Arsenal Without Limits

Each evolution uses the shared evolution context and respects its enable state.

Recurring treaties and project milestones should not be misrepresented as separate random events.

## Event Details

Event Details should explain:

- the international convention and its competing national postures
- the gradual normalization of chemical, biological, and nuclear warfare
- recurring treaty rounds
- each enabled evolution
- the late international research program once its evolution is visible

Event Details should not list:

- exact Condemnation multipliers
- AI weights
- raw membership scores
- project candidate lists
- source-event flags
- project isolation tests
- hidden covert states belonging to other countries
- exact future news outcomes

The event row shows Chaos level 1 and Minor Fire-Once.

## Opening text direction

Viewpoint: senior ministers, diplomats, military planners, scientists, and medical officials reviewing a treaty that treats prohibited weapons as legitimate policy subjects.

Visible facts:

- an international conference has adopted or proposed the new convention
- the country must choose its public posture
- chemical and biological warfare will receive different diplomatic treatment among participants
- nuclear restraint is also under pressure

Information to preserve:

- exact future treaty content
- later Chaos weapon project candidates
- exact membership outcome before responses resolve
- hidden AI motives
- covert programs of other countries

Tone: formal, controlled, unsettling, and specific.

Avoid generic statements that the world is changing, dramatic fragments, administrative debug language, and direct descriptions of hidden mechanics.

## Option direction by posture

### Full Ratification option

Speaker: government prepared to use the convention as a military, scientific, and diplomatic framework.

Tone: confident, official, and willing to accept responsibility for implementation.

The option should imply broad accession without promising free weapons.

### Chemical Accession option

Speaker: government drawing a hard distinction between battlefield gas and uncontrolled disease.

Tone: narrow, practical, and skeptical of biological warfare.

### Retaliation Reservation option

Speaker: government seeking protection and deterrence while preserving a public line against initiation.

Tone: cautious, legalistic in-world, and defensive.

### Public Rejection option

Speaker: government defending the prior taboo and warning that regulation will become permission.

Tone: firm and politically credible.

### Covert Preparation option

Speaker: government publicly rejecting the convention while privately ordering preparations.

Tone: controlled duplicity without comic villain language.

The text may clearly tell the controlling player that preparation is secret.

It must not reveal future exposure events or exact discovery risk.

## Conference text direction

Agenda announcements should identify:

- the sponsor
- the subject
- the broad clause dispute
- the deadline
- the country’s public options

Negotiation events should use concrete political and material disputes, such as declarations, inspections, laboratory access, delivery systems, assistance obligations, and first-use reservations.

Avoid generic debate text that could belong to any treaty.

Resolution events should explain who ratified, whether reservations were accepted, and what public obligations begin.

They should not present raw vote arithmetic as a debug report.

## Evolution text direction

### Evolution I

Focus on operational authority, first-use clauses, chemical mobilization, biological risk, and the weakening of retaliation-only policy.

### Evolution II

Focus on joint planning, reserves, delivery systems, target categories, protection, and the integration of unconventional attacks with conventional campaigns.

### Evolution III

Focus on unrestricted arsenals, routine military use, large stockpiles, weak member-on-member backlash, and the creation of an international program for previously unavailable weapons.

Each evolution should feel like a diplomatic and military change that governments chose.

Do not describe it as a game tier or a content unlock.

## Project text direction

Project selection text identifies only the selected registered project.

It should explain why the convention program wants the prerequisite and what kinds of contribution are needed.

It must not claim that the source incident occurred.

Milestone reports describe progress in broad research stages.

Completion text states that eligible participants can begin the registered research or project route.

Cancellation text states that the normal source route made the program redundant and that accumulated work was abandoned.

Dormancy text states that no registered unavailable project currently qualifies.

## Covert exposure text direction

Exposure requires valid evidence.

The report should identify the contradiction between public rejection and private preparation, the relevant program or facility, and the diplomatic consequences.

It should not invent a laboratory, stockpile, victim, or weapon that the game state does not support.

The controlling country’s options can include admission, denial, controlled accession, inspection, or continued obstruction when each route is valid.

## Country reaction families

### Existing CBRN power

Focus on securing legal protection for current capability, preserving stockpiles, gaining research partners, or resisting inspections.

### Unarmed major power

Focus on whether the convention creates a dangerous research gap and whether protection should come before offensive capability.

### Threatened minor power

Focus on guarantees, masks, detection, access to research, and dependence on larger signatories.

### Recent victim

Focus on retaliation rights, assistance, evidence, and whether joining the convention legitimizes the attacker’s conduct.

### Public opponent

Focus on preserving the old prohibition, sanctions, inspection, and recruiting holdouts.

### Nuclear power

Focus on targeting doctrine, first-use restraint, retaliation, materials cooperation, and the higher remaining consequences of nuclear action.

### Covert preparer

Focus on concealment, competing public policy, intelligence exposure, and the cost of joining later.

## Ideology and government tone

Government type can change emphasis and rhetoric, but it should not produce a fixed moral stereotype.

Relevant distinctions include:

- military command versus civilian cabinet
- centralized secrecy versus parliamentary scrutiny
- revolutionary doctrine versus conservative restraint
- colonial security concerns versus metropolitan diplomacy
- alliance dependence versus strategic autonomy

Final text should mention actual dynamic countries, wars, sponsors, victims, and projects where the event scope supports them.

## Forbidden wording

Player-facing text must not use:

- implementation history
- update history
- rework language
- raw variable names
- source-event bypass terminology
- provider registry terminology
- hardcoded or capped wording
- debug labels
- phrases that announce a hidden route or future surprise
- unsupported claims that a weapon, facility, stockpile, or treaty exists

## Localisation coverage

Implementation must cover:

- event titles, descriptions, and options
- news events
- decision category and status header
- every decision and mission
- cost and requirement tooltips
- posture names and explanations
- Convention Standing states
- agenda names and summaries
- treaty names and reservation states
- doctrine states
- project phases and selected-project names
- completion, cancellation, pause, and dormancy reports
- Event History and Event Details selectors
- evolution list and detail text
- achievement names and descriptions
- asset sprite-facing labels where needed

All final wording must be reviewed by the localisation auditor and must match the authoritative workbook fields that mirror in-game text.
