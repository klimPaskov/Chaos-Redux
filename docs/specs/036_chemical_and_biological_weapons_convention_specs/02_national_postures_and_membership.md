# National postures and membership

## Posture model

Every eligible country holds one primary Event 036 posture.

The posture is public unless the country chooses covert preparation, which retains Public Rejection as the visible stance and stores the covert program separately.

A country cannot hold two public postures at once.

The posture must be represented through one owner-controlled state package, with a stable flag or enum, a player-facing status, AI strategy hooks, and cleanup rules.

## Opening posture matrix

| Posture | Public commitment | Military and research direction | Convention rights | Main risk |
| --- | --- | --- | --- | --- |
| Full Ratification | Accept chemical and biological normalization under the convention | Highest CBRN research, stockpile, delivery, protection, and doctrine interest | Full voting, treaty cooperation, research benefits, Condemnation relief, and later project access | Dependence on convention legitimacy and exposure to inspection or treaty breach |
| Chemical Accession Only | Accept chemical articles while retaining the biological prohibition | Strong chemical and protection interest, low biological interest, moderate missile and nuclear interest | Chemical votes and benefits, limited general treaty participation, no biological project access through Event 036 | Isolation during biological and integrated doctrine rounds |
| Retaliation Reservation | Join the network while preserving no-first-use commitments | Protection, detection, retaliation reserves, delivery readiness, and defensive research | Protection, inspection, retaliation guarantees, limited research cooperation, and reduced Condemnation only for policy-compatible use | Offensive use becomes a public treaty breach |
| Public Rejection | Preserve the old prohibition and oppose normalization | Protection, sanctions, investigation, and counter-convention diplomacy | Opposition actions, independent inspections, bilateral sanctions, and recruitment of holdouts | Loss of convention research and project benefits |
| Public Rejection with Covert Preparation | Reject publicly while building undeclared capabilities | Hidden chemical or biological research, concealed production, intelligence protection, and evidence suppression | Public opposition actions plus covert preparation decisions | Discovery creates cover-up Condemnation, diplomatic exposure, and loss of credibility |

## Full Ratification

Full Ratification is the broadest membership route.

The country accepts the convention as the governing diplomatic framework for chemical and biological warfare.

It can participate in every baseline treaty family, vote on first-use revisions after Evolution I, join strategic doctrine agreements after Evolution II, and contribute to the International Chaos Weapons Program after Evolution III.

Full Ratification increases AI interest in:

- chemical and biological research
- delivery systems
- protective equipment
- decontamination and containment
- physical stockpiles and compatible payloads
- retaliation planning
- treaty participation

The posture gives no technology, payload, stockpile, missile, laboratory, or nuclear weapon by itself.

The country must still satisfy every ordinary research, production, readiness, delivery, target, and physical-payload gate.

## Chemical Accession Only

Chemical Accession Only is a separate permanent posture, not a temporary reservation inside Full Ratification.

The country accepts chemical production, protection, delivery, battlefield doctrine, and ordinary chemical-use normalization.

It does not receive biological research cooperation, biological condemnation relief, biological treaty voting rights, or biological Chaos weapon project access through Event 036.

It may participate in general missile, nuclear, protection, inspection, and retaliation agendas when the agenda permits limited members.

A chemical-only member counts as a full member for chemical votes and as a non-member for biological votes.

It counts as a partial member for Convention Standing.

## Retaliation Reservation

Retaliation Reservation is a membership posture with a binding public policy.

The country accepts the convention’s protective, investigative, research, and retaliatory infrastructure while declaring that it will not initiate chemical, biological, or nuclear use.

A valid retaliatory action can receive convention relief when the shared CBRN action record proves retaliation status.

An offensive first use receives no reservation relief and creates a treaty-breach memory.

The country may later repeal its reservation through a public decision after Evolution I.

Repeal is not automatic and should carry a diplomatic and domestic cost.

A country may also strengthen its reservation into a broader non-use opposition policy, which converts it to Public Rejection after the normal withdrawal process.

## Public Rejection

Public Rejection preserves the old prohibition and refuses Event 036 benefits.

The country keeps normal Condemnation treatment for its own unconventional warfare.

It can organize opposition, recruit other holdouts, demand inspections, publish evidence, support sanctions, send protective equipment, and try to reduce Convention Standing.

A public opponent may form a counter-convention network, but that network is not a new faction.

It is a diplomatic coordination layer that affects AI sanction participation, treaty voting, and access to opposition decisions.

The strongest public opponent can become the Opposition Leader when it has sufficient diplomatic weight, active opposition actions, and a valid government.

Leadership transfers when the leader withdraws from opposition, is annexed, becomes invalid, or loses the required standing.

## Public Rejection with Covert Preparation

This route publicly behaves as Public Rejection.

The covert state is visible only to the controlling player and to systems that have valid intelligence or evidence access.

Covert preparation can support:

- hidden research priority
- concealed laboratories or production work
- stockpile concealment
- counter-intelligence protection
- false declarations
- evidence suppression
- a later secret accession or public revelation

The route must use the existing evidence and cover-up systems where they apply.

Discovery cannot be represented only by an opinion modifier.

A valid exposure should create a public report, reveal the covert state, add cover-up Condemnation through the shared source path, change foreign AI behavior, and close decisions that require the program to remain hidden.

The event must not grant hidden technologies or stockpiles directly.

Covert preparation changes access and priority while retaining ordinary research and production requirements.

## Membership generations and registries

The system uses a versioned membership generation so stale receipts cannot survive a convention reconstruction or save migration.

The owner maintains bounded registries for:

- full members
- chemical-only members
- reservation members
- public opponents
- covert opponents
- active treaty ratifiers for each treaty
- active Chaos weapon project participants

Each registered country stores the current generation and its posture.

A country is added once per generation.

Changing posture moves it between registries through one atomic owner effect.

The same transaction must update Convention Standing, decision visibility, treaty rights, AI strategy, and relevant modifiers.

## Accession after the opening

A public opponent can seek accession after a minimum 180-day public cooling period.

The decision begins a 90-day accession mission.

The country chooses Full Ratification, Chemical Accession Only, or Retaliation Reservation when the mission completes.

Accession can fail if the country becomes invalid, the convention loses all active members, or a route-specific public condition makes the selected posture impossible.

Accession does not restore a missed treaty automatically.

The new member joins treaties that explicitly permit late accession and must separately ratify closed agreements.

## Posture revision

Members can revise their posture after a minimum 365-day lock from the last public change.

Allowed revisions include:

- Full Ratification to Chemical Accession Only
- Full Ratification to Retaliation Reservation
- Chemical Accession Only to Full Ratification
- Chemical Accession Only to Retaliation Reservation
- Retaliation Reservation to Full Ratification after Evolution I
- any member posture to Public Rejection through withdrawal

A covert opponent can end covert preparation without joining.

It can also seek accession, but any unresolved public evidence or active exposure must be processed before the accession completes.

Posture revision should use political and diplomatic costs, a temporary public-trust penalty, and a cooldown.

It must not allow a country to switch posture immediately before use, receive relief, and switch back without consequence.

## Withdrawal

Withdrawal is a public process with a 90-day mission unless a treaty explicitly permits emergency withdrawal.

During the mission, the country retains current obligations and cannot start a second posture change.

Completion removes future convention benefits, voting rights, and project access.

It does not erase action records, treaty breaches, contribution costs, inspection evidence, or prior Condemnation.

A country that withdraws during an active Chaos weapon project keeps its historical contribution receipt but becomes ineligible for the completion unlock unless it rejoins and is an active valid member at completion.

## Expulsion and suspension

Expulsion is rare because the convention legitimizes conduct that older systems would condemn.

A member may be suspended for:

- falsifying a required declaration after evidence becomes public
- attacking another member in violation of a ratified retaliation guarantee
- refusing a binding inspection after accepting the relevant treaty
- sabotaging an active shared project
- becoming an invalid actor for ordinary diplomacy

Suspension removes voting and new contribution access while preserving posture and prior history.

The member may complete a compliance mission, withdraw, or be expelled after a failed deadline.

Expulsion converts the country to Public Rejection with an Exposed Former Member memory.

## Puppet, faction, and alliance behavior

A subject chooses its own posture when it retains ordinary diplomatic and research systems.

Its overlord may influence the choice through AI weights, pressure decisions, and treaty lobbying.

An overlord cannot silently choose for a human subject.

Faction membership does not force convention membership.

Allied signatories gain access to joint treaty content only when each relevant country has ratified the agreement.

A faction does not receive collective CBRN permissions from one member’s posture.

## Posture modifier design

Posture effects should be expressed through event-owned ideas, dynamic modifiers, AI strategy, scripted triggers, or bounded helpers that integrate with existing CBRN systems.

Avoid large flat combat bonuses.

The main effects should change:

- research priority and bonuses
- production priority
- protection and inspection access
- Condemnation conversion
- sanction willingness
- first-use and retaliation policy
- treaty and project eligibility
- AI use willingness

Every posture modifier needs a lifecycle and must be removed or replaced atomically when the posture changes.
