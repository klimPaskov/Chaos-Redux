# Chemical and Biological Weapons Convention

## Complete event architecture

Event 036 is a global diplomatic reordering that makes chemical and biological warfare increasingly legitimate among participating governments.

Its opening remains a Minor Fire-Once event, but the convention persists as a treaty network, a source of recurring conference rounds, a modifier of national doctrine and diplomatic reaction, and a late-game gateway to registered Chaos weapon research routes.

The event’s core promise is that the world begins rewriting the accepted rules of unconventional warfare.

The player chooses a national posture, responds to later treaty rounds, manages the conflict between military advantage and public responsibility, influences whether first use becomes normal, and may join or oppose an international program that recreates weapon prerequisites normally tied to separate Chaos events.

## Playable loop

The event has five connected layers.

### National posture

Every eligible ordinary country adopts one enduring public posture:

1. Full Ratification
2. Chemical Accession Only
3. Retaliation Reservation
4. Public Rejection
5. Public Rejection with Covert Preparation

The posture determines treaty rights, research access, Condemnation relief, AI behavior, inspection exposure, first-use policy, and access to later programs.

Postures can change after the opening, but public reversals carry diplomatic memory, cooldowns, and costs that prevent stance cycling.

### Convention standing

The convention tracks its global strength as a qualitative state derived from active membership and the diplomatic importance of its members.

The public states are Provisional, Divided, Established, and Dominant.

Standing changes conference frequency, diplomatic pressure, sanction participation, research cooperation, and the chance that permissive treaties secure enough ratifications.

It does not directly replace the shared Condemnation score.

### Recurring treaty rounds

The original convention opens a continuing sequence of follow-up conferences.

Each round selects one eligible agenda, identifies a sponsor, opens a negotiation period, allows countries to lobby or oppose the proposal, records reservations, and resolves whether the treaty enters force.

These conferences are Event 036 subevents.

They never become separate entries in the global random-event pool and never advance global event pacing.

### Evolution-driven escalation

Evolution I at `200+` Chaos makes offensive first use acceptable.

Evolution II at `400+` Chaos integrates chemical, biological, nuclear, missile, protection, and conventional planning into one strategic doctrine.

Evolution III at `600+` Chaos removes most remaining restraint among participating states and opens the International Chaos Weapons Program.

Evolution activation itself changes no Chaos.

Only concrete normative outcomes, such as a first-use charter entering force or a Chaos weapon project completing, create Event 036 Chaos entries.

### International Chaos Weapons Program

Evolution III creates one shared project at a time from a provider-owned registry of real event-gated Chaos weapon prerequisites.

Every currently eligible project has exactly equal selection probability.

Participants contribute through industry, research, specialist equipment, facilities, scientists, or manpower according to the selected provider profile.

Completion opens only the registered weapon prerequisite or research route for active contributing participants.

It never fires the source event and never activates the source event’s countries, crises, evolutions, world threats, narrative progression, super-events, or terminal logic.

If the selected weapon becomes available through its legitimate normal route before completion, the project is cancelled immediately, all shared progress is discarded, and the pool is rebuilt.

## Public information budget

The decision category and attached status presentation expose only information that changes an immediate player choice.

The public state consists of:

- National Posture
- Convention Standing
- Current Agenda

When a Chaos weapon project is active, Current Agenda becomes the project identity and progress bar.

The interface may show concise supporting facts such as current member count, the next ratification deadline, or the player’s contribution status in tooltips.

It must not expose a component ledger, raw AI weights, hidden candidate arrays, source event flags, internal project points, or condemnation formulas.

## Event opening

The entry event creates the convention coordinator, initializes the membership generation, records the event in History, asks each human-controlled eligible country for a response, resolves AI responses, calculates initial standing, and applies the one-time Condemnation normalization after all opening responses have been recorded.

A country that cannot use ordinary civilian and diplomatic systems is excluded unless its owner explicitly supplies an Event 036 compatibility contract.

The setup must not use a recurring whole-world daily or monthly country scan.

One bounded event-time pass may issue response receipts and build the initial membership array.

Later work uses registered members, registered opponents, the current sponsor, and the current project participants.

## Condemnation doctrine

Event 036 changes how new public CBRN sources are converted into Condemnation and how countries react to those sources.

It never deletes CBRN action records.

It never changes exact civilian deaths, military casualties, outbreak intensity, contamination, evidence, attribution, weapon history, retaliation proof, or first-use proof.

The convention may reduce ordinary chemical, biological, nuclear, and repeat-use source values according to posture and evolution.

Atrocity and cover-up sources receive no convention relief.

Thermonuclear use receives no convention relief.

Catastrophic biological outbreaks, populated-capital attacks, extreme civilian destruction, and other severe actions retain high source floors.

Hidden evidence remains hidden until the normal disclosure path reveals it.

## Research and production doctrine

Ratification changes willingness and access, not starting inventories.

Countries without relevant technologies become more interested in research.

Countries with relevant technologies become more willing to produce and stockpile compatible payloads and protective equipment.

Treaty cooperation may grant bounded research bonuses or owner-approved special-project progress.

It may not grant a weapon, technology, special project, or event prerequisite unless the relevant owner contract explicitly permits that grant.

## Decisions and missions

The event uses one phased decision category with an optional static category picture.

A phase exposes three to five primary decisions and never more than six.

One to three missions may be active at once.

Each action uses no more than four spendable cost types.

Political power is appropriate for diplomacy, but military, industrial, research, equipment, convoy, manpower, facility, and public-trust costs must be used when they fit the action better.

## AI contract

AI posture and action choices must use current war state, existing CBRN capabilities, protection, public Condemnation, government priorities, strategic threat, industrial capacity, access to valid targets, retaliation status, faction obligations, research gap, and current evolution.

AI must never receive a free payload or bypass a physical-use gate because it adopted a permissive posture.

Every probability-bearing surface requires the repository probability workflow before completion.

The equal selection rule for the Chaos weapon pool is absolute and cannot be changed by AI strategy.

## Persistent memory and cleanup

The event records national posture, public reversals, treaty ratifications, reservations, withdrawal history, covert exposure, contribution receipts, completed projects, cancelled projects, and source isolation proofs.

Obsolete decisions disappear when a posture, treaty, sponsor, target, membership generation, project, or source event becomes invalid.

A save and reload must preserve standing, active agenda, treaty deadlines, project progress, participant shares, cancellation state, and evolution state without duplicating invitations or contributions.

## Completion standard

Implementation is complete only when the opening, every posture, all three evolutions, recurring treaty rounds, Condemnation integration, AI behavior, the project registry contract, equal project selection, cancellation callbacks, contribution logic, source-event isolation, assets, achievements, event logs, Event Details, localisation, documentation, and catalog workbook agree.

A smaller diplomatic modifier event, a free-technology event, a generic research-sharing group, or a guessed project list does not satisfy this specification.
