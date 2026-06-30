# Event 011 Secret Alliance AI and Targeting Matrix

This matrix defines how the compact selects targets and how AI countries behave inside the system.

## Candidate scoring tables

### Minor founder score

| Input | Score direction | Notes |
| --- | --- | --- |
| Is minor | Large positive | Baseline founders should usually be minors |
| Not in a faction | Large positive | Keeps the compact hidden from existing blocs |
| Same faction as target | Exclude | Avoid unreadable betrayal |
| At war with target | Exclude | Required rule |
| Subject of target | Exclude | Avoid target controlling its own enemy member |
| Subject of another country | Large negative unless high autonomy | Only plausible if the subject can act |
| Poor opinion of target | Positive | Grievance basis |
| Different ideology group | Positive | Recruitment narrative |
| Target has generated world tension or conquered nearby land | Positive | Makes the compact reactive |
| Border with target | Positive for knife hand role | Should not dominate all roles |
| Strong industry for a minor | Positive for purse holder | Allows funding actions |
| High stability | Positive | Can sustain secret commitments |
| Near civil war or capitulation | Negative | Too unstable to coordinate |

### Major patron score

| Input | Score direction | Notes |
| --- | --- | --- |
| Major status | Required for patron role | Evolution II or III only |
| At war with target | Exclude | Required rule |
| Same faction as target | Exclude unless an accepted betrayal design later exists | Keep current design clean |
| Rival ideology or strategic rivalry | Positive | Gives role meaning |
| Low opinion of target | Positive | Grievance basis |
| Target borders major sphere or threatens its allies | Positive | Creates plausible patronage |
| Already leading a faction | Mild negative | It can still run shadow patronage |
| Losing a major war | Negative | Avoids suicidal joining |
| Has strong army and industry | Positive | Makes patron significant |
| Has a pact minor in sphere | Positive | Gives route for patron entry |

## AI country roles

| AI actor | Main priorities | Avoid |
| --- | --- | --- |
| Convenor | Keep secrecy high, invite minors, host meetings, preserve cohesion | Starting war too early unless reveal rule fires |
| Purse holder | Fund press, trade squeeze, contract sabotage, bribe intermediaries | Overexposure when evidence is already high |
| Knife hand | Border probes, military scouting, limited sabotage | Reckless border war if target is much stronger |
| Major patron | Increase war readiness, shield minor members, sponsor public reveal | Joining if it would be instantly crushed or if target is a vital ally |
| Weak member | Seek security, accept bribes, waver under exposure | Staying committed after repeated humiliation |
| Defector | Provide evidence and lower pact cohesion | Rejoining without a special event |

## Target country AI behavior

If the current target is AI-controlled because of multiplayer, tag switch, or observer setup, AI response should be route-aware.

| Target situation | AI preference |
| --- | --- |
| Low industry and weak army | Defensive hardening and splitter diplomacy |
| Strong army and high war support | War cabinet preparation and hard exposure |
| High stability and strong intelligence | Evidence route and defector recruitment |
| Low stability | Avoid reckless exposure and heavy public accusations |
| Neighbor member identified | Guard border before border war |
| Major patron identified | Seek public evidence and foreign support before war |
| Public compact and pact readiness high | Prepare war or demand dissolution depending strength ratio |

## Foreign nonmember AI

Foreign nonmembers can be invited, pressured, or used as observers.

| Nonmember type | Behavior |
| --- | --- |
| Friendly to target | More likely to share evidence, refuse pact invitations, or become observer |
| Rival of target | More likely to join if eligible |
| Neighbor of both target and member | Can host talks or suffer border spillover |
| Faction leader of a suspected member | Should react if member is exposed, possibly forcing exit or doubling down |
| Neutral major | Can condemn sabotage after strong evidence, or exploit the crisis for influence |

## Reveal and war AI

The public compact should not instantly launch war from Evolution III. It should evaluate strength and preparation.

| Input | War readiness AI effect |
| --- | --- |
| Pact member count high | Increase |
| At least one major patron | Increase |
| Target preparedness high | Decrease or delay |
| Pact cohesion low | Decrease |
| Evidence scandal high | Decrease, unless major patron hardline |
| Target already in a major war | Increase |
| Target has strong allies | Decrease |
| Compact has border access | Increase |
| Failed ultimatum | Increase sharply |
| Player attacked any member | Reveal and war helper |

## Failure and cleanup AI

If the compact is failing, AI members should not behave like perfect fanatics.

| Failure state | AI response |
| --- | --- |
| Multiple members identified | Burn files, stop risky actions, or public denial |
| Defector exists | Cohesion loss and member exit checks |
| Convenor isolated | Patron leadership contest or compact collapse |
| Major patron abandons | Minors seek exit and war readiness falls |
| Target wins border war | Neighbor commitment falls and exposure chance rises |
| Target defeats public pact | Clear member AI plans and remove public compact ideas |

## AI validation expectations

Implementation should prove that AI decisions cannot target dead countries, countries at war with the target before selection, same-faction target allies, non-existing event targets, or countries that already left the compact. Target scoring should be centralized through helper triggers and effects rather than copied in every decision.
