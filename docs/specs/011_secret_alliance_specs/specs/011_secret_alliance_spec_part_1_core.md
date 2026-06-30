# Event 011: Secret Alliance

Player-facing wording note: every title, option, decision name, focus-style label, achievement title, GUI label, event-detail line, report text, and news text in this package is direction only. Working labels are internal handles for implementation and asset routing. The implementation pass must write final localisation from the directions here, without copying working labels into the game unless a label is explicitly marked as an identifier.

## Core playable promise

Secret Alliance turns ordinary diplomacy into a hidden hostile network aimed at the player country. The event begins as a set of small countries quietly coordinating against the target. The early stage should feel like a pattern the player notices only after repeated small frictions: strange border procedures, delayed freight, anonymous money moving through newspapers, repeated trade refusals, and security services finding the same kind of coded note in unrelated places.

The pact is not a public HOI4 faction at first. It is a covert compact with hidden members, hidden readiness, hidden recruitment, and a growing record of operations. The player does not begin with a named enemy. They begin with a country that is being watched, tested, and irritated by other governments that refuse to appear together in public.

The core loop is:

1. Three eligible countries create a covert pact against the player country.
2. The pact builds secrecy, cohesion, readiness, and hostility through timed operations.
3. The player sees indirect effects first, then stronger evidence as the system escalates.
4. Later stages expose a counterintelligence decision category, a clearer member list, and military response tools.
5. If a pact member enters war against the player, the hidden compact is revealed and the members act together.
6. The player can weaken the pact before reveal through evidence, diplomacy, counterintelligence, border readiness, and targeted pressure.

The event should be tense without becoming a scripted doom clock. A careful player can identify members, split weaker governments away, prepare borders, expose the compact under favorable conditions, and enter any later war with advantages. A careless player sees an ordinary world turn into a prepared coalition.

## Root target and pact identity

The target is the country whose event system fired Event 011. In ordinary single-player use this is the player country. In multiplayer, the event targets the player scope that received the event timer result and does not automatically retarget to other human countries unless the shared event system already selected them.

Use a dynamic pact name in player-facing text after reveal: Anti-[target country] Pact. Before reveal, do not show that name as a public object. The hidden network can be referred to in event details and reports by direction only, such as unidentified coordination, repeated diplomatic pressure, or suspected compact activity. Final wording must avoid direct labels that reveal the hidden pact too early.

The pact has these actor roles:

| Role | Meaning | Visibility to player |
| --- | --- | --- |
| Target | The country the pact opposes | Always known |
| Founder | The first selected country or major patron if the event opens evolved | Hidden until exposed or revealed |
| Core member | A country that will join the revealed faction and war package | Hidden at first, then exposed individually or all at once |
| Associate | A country influenced by the pact but not committed to war | Usually hidden, may appear in reports |
| Major patron | A major country that funds, directs, shields, or later joins the pact | Hidden until evidence, public pressure, or reveal |
| Defector | A former member persuaded, exposed, or pressured into leaving | Visible after the defection event |
| Compromised neutral | A country being courted but not yet a member | Hidden unless a player operation finds it |

## Initial member selection

The initial baseline firing selects three core members. They should preferably be minor countries outside factions, with no ongoing war against the target.

Hard disqualifiers:

| Candidate state | Reason |
| --- | --- |
| Candidate is the target | The pact opposes the target |
| Candidate is at war with the target | The hidden compact cannot begin as an existing war |
| Candidate is a subject of the target | It would behave like an internal revolt system instead |
| Candidate is in the target faction | It would make reveal logic nonsensical |
| Candidate is capitulated or only an exile shell | It cannot operate as a pact member |
| Candidate is a nonstandard actor that shared systems should exclude | The event is diplomatic and should not recruit invalid special actors |
| Candidate already belongs to an incompatible event-created hostile bloc | Avoid double membership and broken faction behavior |
| Candidate lacks any plausible diplomatic reach | Tiny isolated cases can still become associates, but core membership needs a state-level actor |

Soft preference scoring:

| Factor | Candidate gets more weight when |
| --- | --- |
| Faction state | It is outside any faction |
| Country rank | It is a minor during baseline and Evolution I |
| Proximity | It borders the target, shares a sea zone, or sits near target trade routes |
| Grievance | It has claims, negative opinion, border memories, rival ideology, or a recent diplomatic penalty with the target |
| Fear | The target is much stronger, mobilized, expansionist, or recently gained territory |
| Opportunity | The candidate has enough industry, manpower, ports, or intelligence capacity to help |
| Similarity | It shares ideology or strategic interests with another selected member |
| Chaos state | Higher chaos makes stranger cross-regional combinations possible |
| Neutrality posture | It is not already bound by a major alliance that would block covert action |

The three baseline members should not all be adjacent unless the score strongly supports a regional conspiracy. A mixed composition is more interesting: one border country, one trade or naval route country, and one ideologically aligned or diplomatically aggrieved country.

## Hidden pact values

The event should use a compact set of visible and hidden values. Values are directionally specified here, with final numeric constants left to implementation tuning.

| Value | Scope | Visibility | Purpose |
| --- | --- | --- | --- |
| Pact secrecy | Global or pact state | Hidden, then estimated | How hard it is to expose members and operations |
| Pact cohesion | Pact state | Estimated after Evolution II | How likely members stay aligned, reinforce each other, and join reveal war |
| Pact readiness | Pact state | Estimated after Evolution II | How close the pact is to coordinated open action |
| Pact hostility | Pact state | Hidden, then partly visible | How aggressive operations become |
| Recruitment pull | Pact state | Hidden | How likely new members or associates join |
| Target suspicion | Target country | Visible after repeated incidents | General player sense that coordinated activity exists |
| Target evidence | Target country | Visible after counterintelligence opens | Proof that can expose members, split members, or trigger public reveal |
| Target preparedness | Target country | Visible after counterintelligence opens | War and sabotage readiness created by decisions and missions |
| Counter-network strength | Target country | Visible after counterintelligence opens | Intelligence and diplomatic capacity for fighting the pact before reveal |
| Member exposure | Per member | Visible only for exposed members | Whether the player has enough proof to act against that country |
| Member commitment | Per member | Hidden or estimated | Whether that member joins war immediately, hesitates, defects, or remains associate |

Dynamic factors for these values:

| Factor | Secrecy | Cohesion | Readiness | Hostility | Recruitment | Player evidence or preparedness |
| --- | --- | --- | --- | --- | --- | --- |
| Higher chaos | Can reduce secrecy through sloppy panic, can also increase strange operations | Increases if fear of target is high | Increases | Increases | Increases | Raises urgency and decision effects |
| Target world tension contribution | Slightly reduces secrecy through foreign attention | Increases | Increases | Increases | Increases | Raises target suspicion |
| Target military strength | Increases secrecy and recruitment | Increases among fearful members | Increases | Increases if target is threatening | Increases | Raises need for preparedness |
| Target diplomatic isolation | Increases secrecy | Increases | Increases | Increases | Increases | Weakens diplomatic counter-actions |
| Target faction backing | Lowers recruitment among cautious minors | Lowers for weak members | Lowers war confidence | Can increase sabotage instead of war | Lowers | Improves diplomacy options |
| Successful pact operation | Can lower secrecy if sloppy | Increases | Increases | Increases | Increases | Raises suspicion |
| Failed pact operation | Lowers secrecy | Lowers | Lowers | May increase retaliation | Lowers | Adds evidence |
| Player investigation success | Lowers secrecy | Lowers | Lowers | May increase hostility | Lowers | Adds evidence and counter-network |
| Player public accusation without enough proof | Can raise secrecy through cover stories | Increases among members | Increases | Increases | Slightly increases | Damages credibility |
| Member defection | Lowers secrecy | Lowers heavily | Lowers | Can increase anger in hardliners | Lowers | Adds evidence and preparedness |

## Baseline progression

Baseline is quiet and slow. It should not open the full counter-pact decision category. The player receives isolated hints and minor effects, but not a clear target list.

Baseline operation families:

| Working family | What happens in play | Impact level | Reveal behavior |
| --- | --- | --- | --- |
| Diplomatic chill | Repeated small opinion shocks, trade reluctance, attaché refusals, or denied transit | Low | Adds suspicion only after repeats |
| Anonymous press money | Small ideology drift against the target, propaganda pressure, or temporary stability irritation | Low | Can create a later evidence trail |
| Courier pattern | Intelligence agencies find similar codes in unrelated border or embassy incidents | Low | Adds hidden evidence seed |
| Supply nuisance | Delays or small disruptions to convoys, trains, or market routes when plausible | Low | Raises suspicion if target has strong trade exposure |
| Embassy meetings | Pact countries quietly improve relations with each other or align diplomatic posture | Low | Not exposed unless investigation later checks meeting records |
| Border testing | Small border state tension if one member borders the target | Low | Can unlock a later border watch mission |

Baseline should last long enough that the player can feel pattern before mechanics become explicit. Its pressure is subtle, but repeated incidents should accumulate a sense of being watched.

## Public event and report direction

The first public-facing event should not say that a pact exists. It should describe a pattern of unrelated frictions that do not fit normal diplomacy. The text direction should focus on material behavior: customs officers delaying target cargo in several countries, private newspapers repeating the same accusation, and military attachés hearing the same phrase in different capitals. Do not center the scene on sealed reports, confidential memos, or a formal warning label.

Option direction for the first popup:

| Option role | Meaning | Tone direction | Immediate gameplay direction |
| --- | --- | --- | --- |
| Watch quietly | The target government avoids public escalation | Controlled, suspicious, restrained | Slight suspicion gain, better future investigation odds |
| Dismiss the pattern | The government spends attention elsewhere | Irritated, practical, slightly arrogant | Lower early cost, pact gains secrecy or readiness |
| Quietly ask friends | The target uses informal diplomatic contacts | Measured, social, uncertain | Small evidence seed if faction or friendly countries exist |

These are option roles, not final option text.

## Pact operations before reveal

The pact should run operations through paced events or on-action hooks that do not require daily global iteration. Each operation picks a member or small member pair, checks validity, scores plausible targets, then applies a bounded effect.

Operation intensity bands:

| Band | Campaign stage | Typical frequency | Operation severity |
| --- | --- | --- | --- |
| Quiet coordination | Baseline | Slow | Opinion, meeting, suspicion, minor trade effects |
| Active pressure | Evolution I | Moderate | More member invitations, small sabotage, propaganda |
| Covert action | Evolution II | Faster | Industry damage, killings, intelligence leaks, provocations |
| Open crisis | Evolution III | Fast but bounded | Ultimata, border clashes, public declarations, war countdowns |

The implementation should avoid a daily all-country poll. Use event-scoped member arrays, scheduled pulses, and compact per-member loops only when the pact state changes or a pulse fires.

## Pact membership life cycle

A member can move through these states:

| State | Meaning | How it changes |
| --- | --- | --- |
| Candidate | Eligible for invitation | Scored by pact recruitment |
| Courted associate | Receives pact pressure but not committed | Can become core member, refuse, or leak information |
| Core hidden member | Bound to the pact and participates in operations | Can be exposed, defect, be removed, or reveal with faction |
| Exposed member | The target has public or private evidence against it | Can be pressured, attacked through decisions, or become reveal trigger |
| Revealed member | Publicly part of the Anti-[target] Pact | Joins faction or war package according to reveal type |
| Defected member | Left the pact before reveal | May give evidence, guarantees, or temporary target cooperation |
| Invalid member | Annexed, subject-locked, faction-locked, or otherwise unusable | Removed by cleanup and replaced only if the stage allows recruitment |

Member cleanup is part of the feature, not polish. The pact must not keep dead countries, deleted tags, invalid subjects, or members already at war with the target without reveal handling.
