# AI behaviour and probability contract

AI chooses from its military, diplomatic, scientific, and industrial situation.
Ideology adjusts weights but never replaces capability and campaign logic.

Named scenarios and their expected orderings live in [the AI matrix](matrices/ai_probability_scenarios.md).
The probability workflow and auditor routing follow `CLAUDE.md` and [the subagent skill](../../../.claude/skills/chaos-redux-subagents/SKILL.md).

## Hard gates

Every weight is zero when the country is ineligible, the target is invalid, the action cannot be paid, the evolution is disabled, the project is paused or cancelled, the participant trigger is false, or the action would duplicate a receipt.
No positive factor overrides a hard gate.

## Opening posture

| Response | Raised by | Lowered by |
| --- | --- | --- |
| Full Ratification | Chemical and biological technology, strong industry, war or expected major war, high Condemnation tolerance, existing Condemnation that normalization would cut | No CBRN capability, low threat, leading role among opponents |
| Chemical Accession Only | Chemical capability without a biological program, outbreak fear | Biological program central to strategy |
| Retaliation Reservation | Threat without capability, recent victim of CBRN use, minor or subject status, democratic government | Planned offensive use |
| Public Rejection | Little military benefit, high diplomatic weight among holdouts, active sanctions against users | Need for protection or program access |
| Reject publicly, prepare in secret | Public restraint combined with research capacity and a non-democratic government | Weak research base, existing exposure, low threat |

The covert response stays uncommon and situational.

## Treaty responses

AI ratifies when the family suits its posture, capability, war state, and threat, and declines otherwise.
It uses the reservation clause only when that clause keeps a coherent part of the treaty for it.
Lobbying and opposition from the current agenda move these weights for the rest of the negotiation.
AI never ratifies a family its posture forbids.

## Sponsorship and lobbying

AI sponsors when it can pay the commitment, expects the quorum, and is not near capitulation or in sponsorship cooldown.
AI lobbies when the count is within two ratifications of the quorum and organizes opposition when the agenda would expand first use and it is an opponent or reservation member.

## First use

First-use behaviour lives in the existing CBRN use-policy and delivery AI.
Event 036 adds bounded factors only:

- a ratified first-use clause raises the weight of Battlefield Authorization and of initiating a valid chemical or biological action
- the Arsenal raises Unrestricted Authorization
- a Retaliation Reservation member keeps Retaliation Only and has zero weight for initiating use unless it repeals first
- integrated doctrine raises use of the existing battlefield operations and raids when payload, delivery, and protection exist
- the Nuclear Accord raises nuclear use against military, industrial, and logistical targets only

Every existing payload, delivery, readiness, target, friendly-exposure, outbreak, and fallout check stays in force.
Thermonuclear use gets no Event 036 factor.

## Doctrine

AI starts Doctrine Integration when it has two usable families and a war plan that benefits.
Small countries without two families skip it and invest in protection research.

## Opposition

The Opposition Leader prioritizes defeating first-use and Arsenal agendas, recruits withdrawals, publishes forensic evidence, and demands inspections.
It does not spend on opposition it cannot pay for.

## Covert program

A covert AI expands the program only while its hidden evidence is low and ends it when an inspection demand is pending or exposure would cost it a sanction tier.

## Project contributions

AI contributes when it passes the participant trigger and expects to remain a member until completion.
Industry-rich countries prefer industrial and research families, and minors prefer the family they can afford without dropping below their own equipment reserve.
Contribution weight rises near completion and falls once the country's share is already high.
The selected project never changes selection probability.
