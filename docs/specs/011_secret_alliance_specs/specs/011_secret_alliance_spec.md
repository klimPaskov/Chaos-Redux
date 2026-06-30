# Event 011 Secret Alliance core specification

## Working identity

Event 011 starts as a quiet diplomatic conspiracy against the country that receives the event. Three eligible countries create a hidden anti-target pact. They are not at war with the target when chosen, and the selection strongly favors independent minor countries outside any faction. The pact is not a faction at first. It exists as a hidden compact, an intelligence network, a diplomatic promise, and a set of coordinated covert actions.

The public name after reveal is dynamic: `Anti-[target country] Pact`. The implementation uses `secret_alliance` as its internal script stem. Visible player text should stay anchored on the target country's current public name and adjective where the surface supports it.

The playable promise is that the player slowly learns that ordinary diplomatic friction is becoming coordinated pressure. The player should notice patterns before the conspiracy is fully known. Early incidents should feel plausible on their own. Later incidents should make the pattern harder to dismiss, then the decision category gives the player ways to investigate, harden the country, negotiate, and prepare for war.

## Root event role

The root event creates one hidden compact against the target. It should not feel like a simple random faction spawn. It is a live system with:

- Founding members.
- Hidden member expansion.
- Pact cohesion.
- Pact secrecy.
- Pact pressure against the target.
- Target suspicion.
- Target counter-preparedness.
- Evidence and exposure.
- War preparation.
- A reveal state that converts the hidden compact into a visible faction.

The event must remain Minor Fire-Once because the compact is a campaign memory. Its later behavior is handled by pact state, evolution entries, missions, events, and decisions rather than by firing the root event again.

## What the player sees first

The player does not receive a direct statement that several countries formed a hostile compact. The first visible surface should be a small report event or event detail entry about unusual foreign behavior:

- Similar diplomatic complaints appear in unrelated capitals.
- Trade missions from different countries ask almost identical questions.
- Military observers request access to the same rail and port regions.
- Newspapers in unrelated states begin using matching accusations against the target.
- A minor border customs incident repeats in different languages.

The player should infer that the world is becoming less friendly. The text direction should use fear, rumor, repeated detail, and mismatched official explanations. Do not reveal the pact member list in baseline wording.

## Baseline stage

Baseline begins after the hidden founding meeting. Three minor countries are stored as founding members. They begin low-tempo actions against the target.

Baseline actions should be slow, subtle, and individually weak:

- Small opinion damage between the target and each hidden member.
- Low chance of minor industrial disruption in one target state.
- Small chance of a suspicious attache visit report.
- Small chance of pact members quietly improving relations with each other.
- Rare pressure on third countries to cool relations with the target.
- Very small intelligence leakage if the target lacks an agency or counterintelligence capacity.

The baseline should add a visible trace only after enough small incidents accumulate. Suspicion can rise without showing the decision category until a threshold is crossed or the second evolution entry opens the public response layer.

## Evolution I: widening table

Evolution I is an active-event evolution when the pact already exists. It unlocks invitations to additional minor countries and more visible pressure. If the event has not fired yet, Evolution I increases the chance that the baseline opening chooses members with stronger reasons to hate or fear the target.

The new behavior:

- More minor countries can be invited.
- Hidden member cap rises with chaos tier, target strength, and pact cohesion.
- Covert pressure incidents become more frequent.
- Some members begin supporting countries that already oppose the target.
- The pact can finance newspapers, trade obstruction, and arms transfer routes.
- Suspicion rises faster after repeated incident patterns.

The pact remains hidden. It should not create a formal faction, public alliance, or direct war plan at this stage.

## Evolution II: major patron and counter-play

Evolution II is the major turning point. If the pact already exists, one eligible major country can join as patron when conditions support it. If the root event first fires at this stage, an eligible major can be the founder and can recruit at least two minors into the hidden compact. If no valid major exists, the major-led opening is not used.

Evolution II opens a decision category for the target country. The category should feel like an internal security and diplomatic counter-conspiracy office, not a store. It gives the player choices that change later war readiness and pact weakness.

The new behavior:

- The pact can damage factories, railways, and supply routes through sabotage events.
- The pact can fund political provocations or military threats.
- The pact can attempt assassinations of generals, advisors, or political staff through event chains.
- The target can investigate, harden industry, protect command staff, trace couriers, bargain with wavering members, and expose partial evidence.
- Neighboring pact members can become border operation targets before the pact is fully public.
- Counter-play can remove members, lower cohesion, raise preparedness, or force an early reveal.

The target does not receive a full retaliation war option during Evolution II. Border operations are limited and state-based when a pact member is adjacent.

## Evolution III: public compact

Evolution III makes the pact visible. The compact becomes a faction named `Anti-[target country] Pact`. The reveal can happen through the normal progression route, a successful investigation route, an attempted ultimatum, or immediately when any hidden pact member enters war with the target.

The new behavior:

- The faction appears on the map.
- All hidden members become public pact members.
- Members that are valid to join the war are called into war when the reveal is caused by war.
- The target receives war and diplomacy options.
- Pact pressure becomes open military preparation, ultimatums, guarantees against the target, and coordinated war support.
- A second major can join if the target failed to weaken the pact, exposure remained low, and the pact's cohesion is high.
- Counter-preparedness from earlier decisions weakens the public pact's opening strength.

If the root event first fires when this evolution tier is already available, the opening starts from the Evolution II package. The public reveal should follow after a compressed but readable delay so the player still experiences the counter-play layer before the faction appears.

## Immediate reveal rule

If any hidden pact member enters war with the target for any reason, the pact reveals itself. The hidden compact becomes the public faction, every valid pact member joins or is called into the war, and a reveal event fires. This rule must be centralized so wars caused by focus trees, decisions, scripted effects, guarantees, or ordinary diplomacy all route through the same reveal helper.

The reveal should not duplicate war calls. Members already at war stay at war. Members that cannot be called due engine rules should still receive a public pact stance and an AI plan to join when valid.

## Member recruitment fantasy

Pact recruitment should feel like a diplomatic infection. Countries do not join because they love each other. They join because they fear the target, hate the target, want a patron, or believe the target can be boxed in before it grows.

Member recruitment should use these story motives:

- Fear of the target's recent wars or annexations.
- Rival ideology.
- Border disputes.
- Desire for a major patron.
- Prior diplomatic humiliation.
- Trade dependence on an existing member.
- Shared hostility with another member.
- Panic after other Chaos Redux events.

The pact should never recruit the target, current subjects of the target, countries at war with the target before selection, special chaos countries, countries that are invalid for normal diplomacy, or countries whose existence is temporary and hostile to ordinary diplomatic logic.

## Public reveal outcomes

The reveal has several possible outcomes. Implementation should route them through the same reveal state so event logs, decisions, AI, and assets stay aligned.

| Reveal route | Cause | Player outcome | Pact outcome |
| --- | --- | --- | --- |
| Forced by war | A hidden member joins or starts war against the target | The player receives the reveal and war emergency layer | The pact becomes a faction and valid members join war |
| Evidence reveal | Target reaches the evidence threshold | The player can expose the pact before it chooses timing | Some weak or frightened members can leave before public faction formation |
| Ultimatum reveal | Pact pressure and war preparation reach high levels | The player receives a public diplomatic crisis | Pact cohesion is high and war pressure is strong |
| Leak reveal | Low cohesion or failed pact action creates a leak | The player gets partial member list first | Pact loses secrecy and may accelerate to public formation |
| Major patron reveal | Major patron joins and chooses public leadership | The player learns the threat is larger than minors | The patron can call members into formal faction structure |

## Player agency goals

The player should have meaningful choices before the war layer:

- Quiet investigation reduces uncertainty but costs intelligence effort and can fail.
- Public diplomacy can scare away weak members but may raise pact hostility.
- Industrial security reduces sabotage but ties down resources.
- Border operations can hurt a neighboring member but can push reveal faster.
- Negotiation can split the pact but can require concessions or temporary laws.
- War preparation improves the opening crisis but can harm stability or consumer goods.

The strongest route is not always full exposure. A player with a strong army may prefer to let the pact reveal itself while preparing. A weak player may try to split members and delay the reveal. A diplomatic player may expose enough evidence to isolate the pact before it becomes a war bloc.

## Connections with Chaos systems

Chaos value and tier affect pace, member ambition, and severity. Higher chaos does not replace the event's own progression. It changes how fast the pact acts and how far members are willing to go.

World tension and the target's recent actions feed recruitment. Existing wars, annexations, and faction behavior can make countries more willing to join. The pact can also generate small chaos increases when sabotage kills civilians, when faction creation raises tension, and when war begins. These should be modest in baseline and stronger after public reveal.

The Deaths system can receive entries from sabotage, assassination, and major bombing or industrial incidents when those incidents cause population loss. The design should avoid turning routine baseline incidents into large death spikes.

## Documentation and event log identity

Event Details should describe the premise and escalating pattern rather than listing effects. It should show the event as a hidden diplomatic compact that becomes more aggressive through evolutions. The History tab should record the root firing with the target as actor. Evolution entries should record the stage, actor, and public stage direction. The public reveal should have a clear history entry, especially if it leads directly to war.

## Finish criteria for implementation

Event 011 is implemented only when:

- The root event selects exactly three valid founding members for baseline opening.
- Evolved openings are handled without bypassing the counter-play layer.
- Hidden pact members are stored, displayed only when revealed, and cleaned up safely.
- The immediate reveal rule catches all member war paths.
- The decision category opens at the correct point and uses dynamic costs.
- AI uses the hidden pact actions, member invitations, reveal route, and post-reveal war logic.
- Assets, scripted localisation, event details, event log entries, achievements, and docs are aligned.
- The spreadsheet row is updated after final in-game wording exists.
