# 117 Autonomy: the worldwide grant

Autonomy gives every country that is currently a subject an immediate advance along its existing autonomy progression.
A government close to its next threshold may become ready to seek a different relationship, while a tightly controlled dependency makes a smaller step toward the same possibility.
The subject chooses what to do with that position, and its master has to respond through the political relationship that actually exists.
The event is complete at this point when evolutions are disabled.

All labels introduced in this package are working design labels, not final localisation.
The supplied title Autonomy and the supplied evolution labels identify the user's design.
Player-facing wording remains a later writing task under the directions in Part 7.

## What changes immediately

At the firing boundary, take the current set of living countries in actual subject relationships.
Every member receives the award once, regardless of ideology, continent, faction, master, origin event, human or AI control, military strength, or whether its subject type is called a puppet.
A dominion, collaboration government, protectorate, event-created client, nested subject, and special country all enter the same compatibility review.
A country that merely has foreign military access, a guarantee, an occupation, claims against it, or an informal alliance is outside this set.

The award happens before the informational popup.
Closing, ignoring, or acknowledging that popup cannot apply it again or undo it.
The event gives points and a truthful account of their effect.
It does not choose a new autonomy state, remove a master, transfer territory, levy a fee, recruit troops, change the government, or replace a country's established political content.

The normal relationship still determines what a higher status requires.
Sufficient score can coexist with an unmet political cost, a war restriction, a consent requirement, an owner-controlled constitutional process, or another legal gate.
The interface must distinguish the score threshold from these remaining requirements.
[PS-S068, PS-S069, PS-S088]

## Award size and why it scales this way

The full-planning tuning anchor is **25 percent of the full native interval for the subject's current autonomy tier**.
Call that interval width W and the requested grant G, so G = 0.25 × W.
W is the full interval, rather than the distance still needed to fill it.
The amount is expressed and applied in native autonomy points.
The actual active ladder and its current native definitions determine the conversion.

This choice preserves differences in starting position while giving a comparable political advance across ladders with different point widths.
It also avoids making a near-threshold subject receive an almost meaningless fraction of its remaining gap.
The grant does not scale with factories, population, army size, or the master's size.
Small dependencies deserve the same share of political progress as large ones.

| Illustrative native interval | Position before the firing | Requested award | Intended reading |
| --- | --- | --- | --- |
| W = 1,000 points | 100 points into the interval | 250 points | Meaningful progress, with most of the tier still ahead |
| W = 1,000 points | 700 points into the interval | 250 points | Close to the next threshold, with ordinary requirements still relevant |
| W = 1,000 points | 900 points into the interval | 250 points | Native cap and overflow behavior determine the retained amount |
| W = 500 points | 100 points into the interval | 125 points | The same quarter-tier advance on a shorter interval |

These are arithmetic examples, not claims about any particular installed ladder.
Do not hardcode a universal 5,000-point scale from the offline reference.
Use the installed definitions, overrides, and supported native queries to establish each family.
Choose the native precision deliberately, then show exactly the amount that the engine can retain.
[R-AUTONOMY, V-AUTONOMY]

The recommended first balance comparison is 20, 25, and 30 percent of W.
Twenty-five percent is the design default.
Move away from it only after the scenario suite shows a concrete pacing problem.
Increasing the amount cannot repair a relationship whose rules forbid any use of points.

## Thresholds, caps, and existing political processes

Points may put a subject in a position to seek its next status.
They do not authorize an automatic sequence of promotions, an automatic independence demand, or a free native political purchase.
Where the engine naturally clamps at a ceiling, the displayed result reports the retained change and the existing readiness of the country.
The event does not invent an overflow bank or a second autonomy currency.

Ordinary legal progress remains available during an evolution.
A player does not have to wait for an Autonomy petition to use a normal native action.
If the existing system changes the subject's status, the event observes that result and updates its own political episode.
It does not reverse the change to preserve an earlier plan.

## Compatibility across subject arrangements

Universal distribution and universal usable progress are separate acceptance requirements.
A successful call to a native effect is insufficient proof that a subject actually retained useful points.
Every supported family needs evidence of the native score change, the legal route through which that score matters, and the treatment of a full or restricted interval.

| Relationship family | Required behavior | Specific question to close before implementation is accepted |
| --- | --- | --- |
| Ordinary multi-tier subjects | Receive 25 percent of the current full interval and retain normal promotion requirements | Exact widths, caps, native costs, and legal next states |
| Dominions or other subjects with `is_puppet = no` | Receive the same treatment as other subjects | General subject eligibility must include them |
| Integrated or heavily restricted subjects | Receive points without removing restrictions | Whether score is stored and when a lawful transition can use it |
| Collaboration governments | Preserve the existing collaboration relationship and its owner | Whether the native score has an operative route at all |
| DLC-specific or government-specific ladders | Use the actual enabled family | Full support with each relevant DLC configuration, including no DLC |
| Event-created clients and protectorates | Use their existing owner and relationship contract | Whether creator-specific consent or settlement rules govern advancement |
| Africa Charter subjects | Preserve Event 012's consent and generation rules | Both inspected special states prohibit ordinary level-taking, and their current owner does not consume native autonomy score |
| Country at a score ceiling | Apply native clipping truthfully and retain its readiness | No fictitious retained award or automatic transition |
| Nested subject that is also a master | Receive one award in its subject role and retain its separate master responsibilities | No duplicate award from visiting both roles |
| Unrecognized future custom family | Enter compatibility inventory before being declared supported | No silent fallback to the default ladder or a generic economic reward |

The Africa Charter conflict is established in current repository source.
Its owner explicitly controls the relationship stages, consent, and status writes.
The two autonomous-state definitions prohibit taking and losing levels, and disable ordinary autonomy AI desires.
The current owner contract provides no demonstrated native-score input to its negotiated progression.
[R-AFRICA-STATE, R-AFRICA-OWNER]

**The universal useful-effect requirement remains an explicit compatibility blocker for such families.** The accepted behavior is still that every current subject participates.
An implementer may not close the blocker by excluding these subjects, replacing their relationship, spending a different currency, awarding a generic buff, or merely recording an attempted points call.
A bounded owner-approved extension may make native score meaningful within that owner's existing consent process, but it needs its own exact rule, owner review, and evidence before acceptance.
No such extension is represented as already accepted or implemented here.

This is a feature acceptance gate, rather than a new player-facing exemption.
Do not claim complete support or enable a supposedly universal implementation until each supported family has a useful compatible disposition.
The supplied sources and accessible repository do not permit an honest stronger claim today.

## The firing boundary

The relevant world is the world at the event's immediate boundary.
A subject created before that boundary receives the award.
A subject created afterward waits for a later firing.
A country that became independent before the boundary receives no subject award.
An annexed or nonexistent country receives nothing through a stale tag reference.

The baseline is one immediate transaction across the frozen recipient set.
No slow presentation queue delays the actual grant until a later political world.
The first write for each recipient belongs to that firing and that living country incarnation.
A master transfer during follow-up cannot make the same country eligible for a second copy of the same firing's award.
The country receives a fresh award when a genuinely later firing occurs.

## Recurrence and useful differences between campaigns

The event can enter the existing repeatable pool whenever subjects exist and the normal shared selection rules permit it.
It has no private periodic timer that manufactures additional worldwide grants.
The proposed entry tier is Chaos level 1, and the proposed Liberations membership has Low severity.
Those classifications concern availability and cluster composition.
They are not instructions to add one Chaos point when the event fires.

Later firings reward the subjects that exist then.
An empire that has negotiated independence may have fewer recipients.
A partition or warlord settlement may create new ones.
A subject retained through cooperation may make repeated ordinary progress without ever being forced to leave.

An empire with many subjects receives no multiplier to an individual award.
It faces a larger political management problem only if an enabled evolution creates several simultaneous opportunities or disputes.
A master with one subject receives the complete applicable experience.

## Player outcomes with both evolutions disabled

The baseline has several valid conclusions without adding a decision minigame.
A distant dependency makes progress and remains in its current status.
A prepared subject uses its normal legal action to advance.
A country near independence waits for security, political resources, or consent.
A master invests in the relationship through the systems it already has.
A full subject bar stays full while the remaining legal conditions determine what comes next.

There is no baseline random punishment, instability roll, compulsory petition, or automatic war.
The harmful possibilities belong to the enabled evolutions described in the next two parts.

## Design evidence and acceptance boundary

The unconditional worldwide point award, current-subject eligibility, optional later choices, recurrence, and the two named evolution directions come from the user's draft.
The normalized quarter-tier grant is a full-planning design choice.
The distinction between subjects and puppets and between points and legal status follows the supplied diplomacy sources and the offline autonomy reference.
The locked Africa relationship is a current repository finding.
Native engine behavior and complete DLC coverage remain unverified implementation requirements.
The evidence companion identifies every source and the exact limits of those claims.
