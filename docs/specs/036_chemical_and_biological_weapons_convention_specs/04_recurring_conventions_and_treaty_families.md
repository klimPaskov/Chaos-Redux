# Recurring conventions and treaty families

Per-family stage, eligible postures, quorum class, capability gate, reservation clause, benefits, obligations, and breach consequence are tabulated in [the treaty matrix](matrices/treaty_family_matrix.md).
This file owns the conference process and what makes each family distinct.

Treaty names are working labels until the localisation pass.

## Conference scheduler

One agenda is active at a time.
The coordinator schedules it with a self-rescheduling hidden event and reads only the registries.

| Interval | Rule |
| --- | --- |
| First agenda | 90 to 180 days after the opening ([01](01_event_identity_and_playable_promise.md#early-pacing)) |
| Later agendas | 180 to 360 days after the previous resolution, never below 120 |
| Emergency agenda | 30 to 90 days after a public member CBRN use, a reservation breach, or a project cancellation |

Established or Dominant Standing, a war between members, recent public CBRN use, and a newly activated evolution shorten the interval.
Divided Standing, widespread reservations, and two consecutive failed agendas lengthen it.
Provisional Standing pauses ordinary agendas and leaves only a reconstruction agenda.

## Agenda pool

An agenda family is eligible when its evolution is active and enabled, its capability gate passes among current members, it is not already in force, and its failure cooldown has ended.

The pool is weighted by the campaign:

- Protection and assistance after a member suffers a CBRN attack
- Inspection after hidden evidence disputes or a covert exposure
- Delivery when members hold payloads without delivery technology
- Nuclear when two or more members have nuclear technology
- The newest unlocked family after an evolution activates

The weighted agenda pool needs the probability workflow in [10](10_ai_behavior_and_probability_contract.md).
Equal-probability selection applies only to Chaos weapon projects, never to agendas.

## Sponsor

Each agenda has one sponsor: the eligible member with the best fit for the family (technology, industry, recent attack or use) outside a 365-day sponsorship cooldown.

A human member can claim sponsorship through Sponsor the Current Agenda while the agenda is open.
The sponsor's ratification is automatic, its Lobby for Ratification counts double, and it must deliver the family's obligation first if the treaty enters force.

## Conference sequence

1. **Announcement.**
   A report event names the sponsor, the subject, the clause dispute, and the deadline.
2. **Negotiation, 60 to 120 days.**
   The header shows the ratification count against the quorum.
   Members can lobby, opponents can organize opposition, and AI response weights move with those actions.
3. **National response.**
   At the deadline each eligible human member receives a response event with up to three options: Ratify, Ratify with the family's reservation clause where the matrix defines one, or Decline.
   A human who does not answer declines.
   AI members resolve through their response weights.
4. **Resolution.**
   The treaty enters force when the ratifications meet the quorum and the capability gate still passes.
   It binds only its ratifiers.
5. **Implementation.**
   Framework treaties persist until withdrawal or repeal, and operational programs last 365 days with renewal at a later agenda.
   Obligations open the implementation missions in [09](09_decisions_missions_costs_and_visibility.md#mission-catalog).

## Quorum

| Quorum class | Ratifications needed | Additional rule |
| --- | --- | --- |
| Ordinary | `max(3, ceiling(35% of active members))` | The family's capability gate |
| Strategic | `max(4, ceiling(45% of active members))` | Ratifiers cover the family's capability gate |
| Arsenal | `max(5, ceiling(50% of active members))` | One major ratifier or two ratifiers with at least 40 factories each |

Chemical Accession members count only for families they may ratify.
The minimums and percentages are script constants and must be checked in a world with five or fewer members.

## Treaty families

### Baseline

**Protection and Assistance Compact.**
Shared masks, decontamination, detection, and medical aid, plus the guarantee clause: when a ratifier suffers a confirmed hostile CBRN action, every other ratifier receives an Assistance Guarantee mission.
The mission is fulfilled by delivering protective equipment or by the existing `cbrn_sponsor_decontamination_mission`, for which Compact ratification counts as valid access.
Failing it suspends the ratifier.

**Chemical Production Articles.**
Chemical production and stockpiling become declared military preparation.
Ratifiers gain chemical research and production modifiers and a Declaration Deadline mission every 365 days, where a missed declaration suspends them.
The reservation clause keeps declarations and drops the production modifiers.

**Biological Laboratory Registry.**
A weak registry for laboratories and containment.
Ratifiers gain biological research and containment modifiers and the same declaration obligation.
It never claims verification the game cannot prove, and a covert biological program inside a ratifier is exposed only through ordinary disclosure.

**Inspection and Verification Protocol.**
Ratifiers may use `cbrn_demand_inspections` against another ratifier without the Formal Censure and sanctions-participant requirements.
Accepted inspections start the existing international inspections and disclose hidden evidence, including camp and restricted-site atrocity evidence.
Refusal records the existing blocked-inspection cover-up source and suspends the refuser.
The reservation clause limits it to chemical inspections.

### Evolution I

**First-Use Revision.**
Two clauses, chemical and biological, each ratified separately in the same response event.
A ratified clause makes first use of that family policy-compatible, moves the country to relief stage I for the family, and raises AI first-use willingness.
The biological clause also raises biological stockpile and delivery priorities.
Chemical Accession members can ratify only the chemical clause, and Retaliation Reservation members cannot ratify either without repealing.
Nuclear first use is not a clause, it belongs to the Nuclear Materials and Targeting Accord.

**Missile and Delivery Cooperation Accord.**
Research bonuses for rockets, missiles, and air delivery, and owner-approved special-project progress where a delivery project exists.
It never creates missiles or payloads.

### Evolution II

**Strategic WMD Doctrine Charter.**
Ratifiers can run the Doctrine Integration mission ([06](06_evolution_ii_strategic_wmd_doctrine.md#integrated-doctrine)), whose success moves them to relief stage II.
Its allied clause lets ratifiers in the same faction share protective equipment and assistance without an assistance request.
Reservation members can ratify its defensive sections only.

**Nuclear Materials and Targeting Accord.**
Nuclear research cooperation, nuclear relief stage II, and higher AI willingness against military, industrial, and logistical targets.
It grants no bomb, and capital and thermonuclear limits in [03](03_condemnation_normalization_and_cbrn_integration.md#eligible-contexts) still hold.

### Evolution III

**Arsenal Without Limits Articles.**
Relief stage III, every use policy-compatible for its ratifiers, the strongest AI production and use priorities, and minimal member-on-member sanction pressure.
Every hard limit in [07](07_evolution_iii_arsenal_without_limits.md#remaining-hard-limits) remains.

**International Chaos Weapons Program Charter.**
Opens the program in [08](08_international_chaos_weapons_program.md) when at least one registered project is eligible.

## Research cooperation

Treaty research help uses timed research bonuses, owner-approved special-project progress, or modifiers on the posture idea.
Event 036 never creates a native research-sharing group, because one cannot be revoked cleanly.
Leaving a treaty ends future bonuses and never removes completed research.

## Agenda failure

A failed agenda records its family, sponsor, final count, and failure date.
It starts a 180-day cooldown after a narrow failure (at least two-thirds of the quorum) and a 365-day cooldown otherwise.
A failure costs the sponsor political power and gives the Opposition Leader a 90-day lobbying bonus.
Failure creates no Chaos.

## Collapse and reconstruction

When Standing becomes Provisional, ordinary agendas pause, treaties already in force stay active, and the coordinator opens a reconstruction agenda after 90 days.
Reconstruction succeeds when Standing leaves Provisional, which needs accessions rather than a vote.
An active project pauses while the program charter's ratifiers fall below the Arsenal quorum and resumes when they return, as [08](08_international_chaos_weapons_program.md#quorum-pause) describes.
