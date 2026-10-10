# Event chain, reactions, and localisation direction

Writing rules come from [the events skill](../../../.claude/skills/chaos-redux-events/SKILL.md#event-writing-and-player-facing-text).
This file owns the event map, log integration, and the direction for each text surface.

## Namespace plan

The canonical namespace stays `chaosx.nr36`.
Final numbers may move to avoid collisions while the ranges keep their roles.

| Range | Role |
| --- | --- |
| `chaosx.nr36.1` | Canonical entry and global setup |
| `.2` to `.9` | Opening response, opening news, AI resolution |
| `.10` to `.19` | Agenda announcement, national response, resolution, failure |
| `.20` to `.39` | Evolutions I to III |
| `.40` to `.49` | Program selection, stage reports, completion, cancellation, dormancy |
| `.50` to `.59` | Covert exposure, reservation breach, suspension, expulsion |
| `.60` to `.69` | Accession, withdrawal, collapse, reconstruction |
| `.70` to `.79` | Global news |

## Event types

The entry is the only normal random-event firing.
It records Event 036 in History once and applies the fire-once lifecycle.

Every other event is an Event 036 follow-up.
None enters the random-event pool, adds pacing, or records another History row.

AI countries resolve responses through hidden effects with the same weights.

## News

Global news is reserved for changes to the international order:

- the convention entering force
- the first chemical and the first biological first-use clause
- the Strategic WMD Doctrine Charter
- the Arsenal Without Limits Articles
- the program Charter and each completed project
- collapse to Provisional Standing after broad withdrawal
- exposure of a major country's covert program

Routine accessions, contributions, and failed agendas use country report events.

## Event log integration

History records Event 036 once at the opening, with the coordinator as actor, falling back to the triggering country only when it is an ordinary country.

The Evolutions view records First Use Becomes Acceptable, Strategic WMD Doctrine, and The Arsenal Without Limits through the shared evolution context and enable state.

Program completions and treaties are not shown as separate random events.

## Event Details

Event Details describes the convention, the competing national answers, the gradual normalization of chemical, biological, and nuclear warfare, recurring treaty rounds, each enabled evolution, and the late research program once Evolution III is visible.

It never lists multipliers, weights, membership arithmetic, candidates, provider rules, other countries' covert programs, or future outcomes.

The row shows Chaos level 1 and Minor Fire-Once.

## Opening direction

The opening shows what the convention means on the ground for the reading country: chemical plants asking for contracts, staff officers requesting stockpile figures, health ministries preparing masks, and laboratories under military guard.
The five options are the government's answer.

| Option | Voice |
| --- | --- |
| Full Ratification | A government ready to build on the convention and accept responsibility for it |
| Chemical Accession Only | A government that accepts gas on the battlefield and refuses to breed disease |
| Retaliation Reservation | A government that wants masks, guarantees, and the right to answer, never to start |
| Public Rejection | A government defending the old prohibition and warning that regulation will become permission |
| Reject publicly, prepare in secret | A government saying one thing in public and ordering another in private, written without villain caricature |

Each option tooltip shows the visible consequences: the posture idea, the opening Condemnation change as a tier where it applies, and treaty access.
The covert option may tell the controlling player the program is secret, but never its discovery risk.

Sample opening line: "The chemical works at the edge of the capital have asked the War Ministry for permission to triple their night shifts, and the Health Ministry wants to know how many masks each school should keep."

## Conference direction

Announcements name the sponsor, the subject, the material dispute (declarations, inspections, laboratory access, delivery, assistance, first use), and the deadline.
Resolutions say who ratified, which reservations were accepted, and what obligations begin, without vote arithmetic.

## Evolution direction

- Evolution I: operational authority, chemical mobilization, biological risk, and the retreat of retaliation-only policy.
- Evolution II: joint planning, reserves, delivery, target categories, and protection.
- Evolution III: unrestricted arsenals, routine use, and pooled research into weapons no member has yet built.

Each reads as a choice governments made, never as a game tier or content unlock.

## Program direction

Selection names only the selected project.
Stage reports describe research work in broad terms.
Completion, cancellation, and dormancy follow [08](08_international_chaos_weapons_program.md#player-facing-text).

## Exposure direction

An exposure report names the contradiction between the public rejection and the hidden program and its diplomatic consequences.
It never invents a laboratory, stockpile, victim, or weapon the game does not hold.

## Reaction families

Response and report text varies by situation, read from game state:

- existing CBRN power: protecting its capability and its partners
- unarmed major: the research gap and protection first
- threatened minor: guarantees, masks, and dependence on larger members
- recent victim: retaliation rights, aid, and whether joining forgives the attacker
- public opponent: the old prohibition, sanctions, and recruiting holdouts
- nuclear power: targeting doctrine and the remaining nuclear restraint

Government type changes rhetoric, never a fixed moral stereotype.

## Localisation coverage

Every event, option, news item, header line, decision, mission, cost and requirement tooltip, posture, Standing state, agenda, treaty, reservation clause, doctrine idea, program stage and report, History and Event Details selector, evolution row, and achievement needs final text.
Player-facing wording must match the workbook fields that mirror it.
