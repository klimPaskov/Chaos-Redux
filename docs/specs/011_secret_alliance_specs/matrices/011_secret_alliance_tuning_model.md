# Event 011 Secret Alliance tuning model

This model defines dynamic factors and tuning relationships. It does not prescribe final script constants. Exact values should be centralized during implementation and validated against several country sizes.

## Core values

| Value | Visibility | Conceptual range | Purpose | Main gains | Main losses |
| --- | --- | --- | --- | --- | --- |
| Pact Cohesion | Hidden until reveal conversion | 0 to 100 | Measures willingness to accept shared risk and obey coalition decisions | successful operations, target aggression, sponsor aid, common ideology, public accusation without proof | failed operations, motive disputes, target concessions, sponsor weakness, turned members |
| Pact Readiness | Hidden until Evolution III, then broad band | 0 to 100 | Measures plans, access, depots, intelligence, and mobilization preparation | intelligence success, military surveys, access agreements, major sponsor, target unpreparedness | exposed routes, depot strikes, false plans, member withdrawal, target protection |
| Evidence | Visible from Evolution II | 0 to 100 | Measures confidence that incidents form an organized network and identifies actors | investigations, captured material, leaks, failed operations, turned channels | false leads, network cleanup, careless public accusation, source loss |
| Preparedness | Visible from Evolution II | 0 to 100 | Measures practical defense against the coalition opening | protection projects, mobilization, allied consultation, known plans, secured borders | repeated successful sabotage, overstretched wars, failure to maintain projects, premature demobilization |
| Pact Alertness | Hidden | 0 to 100 | Measures awareness of target counterintelligence | visible probes, failed raids, exposed sources, public dossier | quiet period, successful deception, false confidence | 
| Recruitment Attraction | Hidden per candidate | Open score | Measures why a candidate might join | fear, grievance, target aggression, sponsor pressure, coalition success | target reassurance, security guarantee, good relations, pact failures |
| Suspect Confidence | Visible by band | 0 to 100 per candidate | Measures player confidence in a country's involvement | linked clues, captured routes, repeated methods, confirmed meetings | false traffic, innocent explanation, lost source | 
| Coalition Resolve | Visible after reveal | 0 to 100 | Wartime conversion of cohesion plus public commitment | victories, sponsor aid, target aggression narrative, shared losses | defeats, conflicting war aims, separate terms, sponsor collapse, exposed deception |
| War Pressure | Visible at Evolution III | 0 to 100 | Measures proximity to public coalition war | readiness, cohesion, mobilization, target preemption, external war | settlement, member exit, sponsor withdrawal, successful deterrence |

## Starting bands

Normal baseline opening with three minor founders should usually begin with:

- Cohesion in the Uneasy or low Functional band
- Readiness in the Improvised band
- Evidence at zero or near zero
- Preparedness at zero or a small country-derived baseline
- Alertness low
- no suspect above the Possible band

Pre-fire Evolution II opening should usually begin with:

- Cohesion in the Functional band, adjusted by motive compatibility
- Readiness in the Networked band
- one major sponsor
- one developed operational route
- Evidence below the threshold that would immediately reveal a member
- a short delay before the response category opens through a serious incident

## Dynamic scaling principles

### Country scale

Target scale should affect burden rather than raw event eligibility.

- Larger industry increases the number of possible sabotage targets and the cost of comprehensive protection.
- Larger armies increase the value of stolen plans and the cost of compartmentalization.
- Larger territory increases travel and border-protection burden.
- Smaller countries face fewer targets but greater proportional damage from a severe incident.
- Major targets attract stronger sponsors and broader recruitment, but also possess more counterintelligence and diplomatic capacity.

### Chaos

Chaos affects tempo, risk tolerance, and evolved opening strength.

- Calm World favors long intervals, subtle incidents, and defensive motives.
- Gathering Storm enables Evolution I and broader minor recruitment.
- Rising Chaos enables Evolution II and major sponsorship.
- Chaos Tier intensifies Evolution II operations without consuming another evolution stage.
- Totalen Chaos enables Evolution III and the possibility of a second major.
- World Collapse conditions can increase desperation but do not create a world-end branch for this event.

### Target behavior

Pact pressure should rise when the target:

- annexes countries
- breaks guarantees or non-aggression agreements
- creates high world tension
- defeats neighboring states rapidly
- threatens members' claims or borders
- publicly accuses countries without sufficient proof
- uses force against an innocent suspect

Pact pressure should fall when the target:

- signs credible security agreements
- settles a founder's specific grievance
- guarantees a fear-motivated country credibly
- exposes sponsor coercion
- restrains expansion for a sustained period
- turns or removes important liaison networks

## Operation pacing model

Use a dynamic MTTH or pulse window rather than a fixed timer.

### Base influences that shorten the interval

- higher chaos
- more active members
- major sponsor present
- higher readiness
- recent target aggression
- doctrine favors action
- Evolution I or II active

### Influences that lengthen the interval

- high target Preparedness
- high pact Alertness after a failed operation
- low cohesion
- recent operation repetition
- sponsor distraction
- member validity changes
- a successful target deception operation

### Anti-spam rules

- One substantial operation active at a time by default.
- The same operation family should have a recent-use penalty.
- A severe operation creates a recovery window.
- Permanent building damage is rare and limited to Evolution II onward.
- Political killings are rare, gated, and cannot repeat against the same protected office without a major state change.

## Cohesion model

Cohesion should be calculated from components, then allowed to move through play.

Suggested components:

- motive compatibility
- ideology compatibility
- sponsor confidence
- shared border or theater value
- success memory
- grievance satisfaction
- target threat
- member war burden
- leadership dispute
- exposed or turned member penalty

A mixed-motive pact can begin strong when target threat is high, then fracture once victory, spoils, or regime goals become concrete.

## Readiness model

Readiness should represent real preparation layers.

| Layer | Sources | Counterplay |
| --- | --- | --- |
| Intelligence picture | stolen plans, ciphers, recruited staff | compartmentalization, cipher rotation, turned channels |
| Access and basing | ports, airfields, transit, border routes | diplomacy, inspections, access denial |
| Logistics | forward depots, stockpiles, rail surveys | depot strikes, hardened rail, controlled shipments |
| Staff coordination | conferences, exercises, liaison committees | conference disruption, false plans, exposed agendas |
| Mobilization | member readiness and war preparations | deterrence, preemption, allied consultation |

Readiness gains should have diminishing returns when one layer is complete and other layers remain weak.

## Evidence model

Evidence is not a single clue count. It combines quality and corroboration.

Suggested evidence classes:

- method evidence from sabotage signatures
- communications evidence from ciphers and couriers
- financial evidence from funding routes
- diplomatic evidence from meetings and coordinated statements
- military evidence from surveys, depots, and exercises
- human evidence from defectors, intermediaries, and turned members

Two independent classes should be more valuable than repeated clues from one class. A complete public dossier should require corroboration.

### Confidence bands

| Band | Meaning | Player actions supported |
| --- | --- | --- |
| Unconnected | No credible link | No country-targeted action |
| Possible | One weak or indirect link | Quiet monitoring only |
| Plausible | Multiple related clues | Quiet diplomatic probe and surveillance |
| Likely | Strong corroboration | Targeted counter-network actions |
| Confirmed | Direct evidence or trusted source | Public naming, turn attempt, preemption against a member |

## Preparedness model

Preparedness should combine maintained projects rather than only cumulative clicks.

Suggested components:

- staff security
- industrial protection
- transport protection
- border readiness
- leadership continuity
- allied coordination
- known enemy plans

Some projects should decay after their duration ends. A country cannot permanently maximize every component without cost.

## Reveal conversion

At reveal, calculate wartime effects from capped components.

### Coalition side

- Cohesion converts into Coalition Resolve.
- Readiness converts into planning, mobilization speed, access, and opening logistics.
- Major sponsor adds command and material support, scaled by its current condition.
- Member count adds breadth but also a coordination burden.
- Motive incompatibility creates a fracture reserve that can activate after setbacks.

### Target side

- Preparedness converts into opening defense, mobilization protection, secured logistics, and reduced surprise.
- Evidence converts into known fronts, exposed depots, intelligence bonuses, and member-specific diplomatic actions.
- A turned member creates one or more concrete weaknesses.
- False accusations reduce diplomatic credibility and can strengthen coalition public justification.

No single prewar value should grant automatic victory. Strong preparation should create better options and a survivable opening.

## Evolution pacing

| Evolution | Normal unlock tier | Active-event pacing | Pre-fire opening | Key limiter |
| --- | --- | --- | --- | --- |
| I | Gathering Storm | Dynamic MTTH near the project norm, shortened by membership and target aggression | Four to five minor founders | Recruitment validity and secrecy |
| II | Rising Chaos | Dynamic MTTH after meaningful baseline activity | One major founder or sponsor plus minors | Major strategic validity |
| III | Totalen Chaos | Dynamic MTTH after Evolution II, with pressure from readiness and exposure | Start at Evolution II, then accelerate toward III | Prevent instant no-counterplay war |

If an evolution is disabled, required baseline flow must still have a safe route. The pact can continue, collapse, or reveal through hostile war without depending on disabled evolution content.

## Scenario scaling

| Intensity | Starting coalition | Readiness | Resolve | Target preparation window | AI risk tolerance |
| --- | --- | --- | --- | --- | --- |
| Low | Three minors | Low to medium | Functional | Short but meaningful | Cautious |
| Medium | Four to six valid countries | Medium | Functional to committed | Short | Normal |
| High | One major plus five to seven others | High | Committed | Very short | Aggressive |
| Maximum | Up to two majors and eight to twelve total, limited by valid pool | Very high | High but motive-dependent | Immediate public crisis | Very aggressive without ignoring validity |

The selected type changes composition and doctrine. Intensity changes scale and starting state. Both controls must be read at confirmation time.

## Balance scenarios

### Scenario A: Small peaceful target

Verify that three founders can be selected without distant nonsense, sabotage remains proportionate, protection is affordable, and a major sponsor does not join without strategic reach.

### Scenario B: Expansionist regional major

Verify that recruitment and cohesion rise, neighboring grievances matter, Evidence can still be built, and the coalition does not become unstoppable before Evolution III.

### Scenario C: Island major

Verify that members need naval or air access, landlocked minor founders do not create implausible opening war effects, and port protection matters.

### Scenario D: Target already in a large war

Verify that operation pressure does not create unavoidable collapse, Preparedness actions have opportunity cost, and sponsor AI considers current fronts.

### Scenario E: High Evidence, low Preparedness

Verify that public exposure can weaken the coalition but does not replace military preparation.

### Scenario F: Low Evidence, high Preparedness

Verify that the target survives better but lacks member-specific fracture actions.

### Scenario G: Turned founder

Verify that the channel remains valuable, can be exposed, and produces a concrete reveal or war effect.

### Scenario H: Two-major coalition

Verify leadership rivalry, theater allocation, Resolve pressure, and achievement tracking.

### Scenario I: Disabled evolutions

Verify that baseline activity, hostile-war reveal, collapse, and cleanup work without Evolution I, II, or III.

### Scenario J: Maximum triggerable scenario

Verify safe candidate caps, human consent, immediate faction and war, super-event firing, and achievement eligibility.

## Exploit controls

- No repeatable Evidence farming from the same clue.
- No permanent Preparedness stacking without maintained cost or caps.
- No free equipment or unit loops.
- No repeated public dossier after reveal.
- No target switching through player tag changes.
- No member duplication across recruitment and evolved opening.
- No coalition call loop after a member exits or becomes invalid.
- No separate-terms farming against the same country.
- No scenario achievement at lower intensity through later variable changes.
- No innocent-country accusation loop that becomes a cheap war-goal generator.
